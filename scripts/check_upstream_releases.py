"""正式 Release 发现与映射审查。默认只读，--publish 才创建 Issue。"""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


class GitHub:
    def __init__(self, token=None):
        self.token = token

    def request(self, path, body=None):
        headers = {"Accept": "application/vnd.github+json",
                   "X-GitHub-Api-Version": "2022-11-28",
                   "User-Agent": "apple-workflow-skills-release-check"}
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        data = None if body is None else json.dumps(body).encode()
        req = urllib.request.Request("https://api.github.com/" + path,
                                     data=data, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            # 不打印 token、响应体或不可信上游内容。
            raise RuntimeError(f"GitHub HTTP {exc.code}: {path.split('?')[0]}") from None
        except urllib.error.URLError:
            raise RuntimeError("GitHub 网络请求失败") from None

    def pages(self, path):
        result = []
        separator = "&" if "?" in path else "?"
        for page in range(1, 101):
            batch = self.request(f"{path}{separator}per_page=100&page={page}")
            if not isinstance(batch, list):
                raise RuntimeError("GitHub 分页响应不是列表")
            result.extend(batch)
            if len(batch) < 100:
                return result
        raise RuntimeError("分页超过上限，不能视为完整结果")


def due(today, anchor):
    delta = (today - dt.date.fromisoformat(anchor)).days
    return delta >= 0 and delta % 2 == 0


def candidates(source, releases, reviews):
    handled = set(source["baseline_release_ids"])
    handled.update(r["release_id"] for r in reviews if r["source_id"] == source["id"])
    return sorted(
        (r for r in releases
         if not r["draft"] and not r["prerelease"] and r.get("published_at")
         and r["id"] not in handled),
        key=lambda r: (r["published_at"], r["id"]),
    )


def mapped_paths(source, files):
    modules = set()
    for mapping in source["mappings"]:
        for item in files:
            names = [item.get("filename", ""), item.get("previous_filename", "")]
            if any(name == prefix or (prefix.endswith("/") and name.startswith(prefix))
                   for name in names for prefix in mapping["upstream_paths"]):
                modules.update(mapping["local_paths"])
    return sorted(modules)


def assess(api, source, release):
    base = urllib.parse.quote(source["adopted_commit"], safe="")
    head = urllib.parse.quote(release["tag_name"], safe="")
    diff = api.request(f"repos/{source['repository']}/compare/{base}...{head}")
    files = diff.get("files", [])
    if not isinstance(files, list):
        raise RuntimeError("GitHub diff 文件列表缺失")
    # Compare 的 files 最多 300 项，不能据此宣称完整无影响。
    uncertain = len(files) >= 300 or diff.get("status") not in ("ahead", "identical")
    return {"modules": mapped_paths(source, files), "uncertain": uncertain,
            "file_count": len(files), "status": diff.get("status", "unknown")}


def marker(source_id, release_id):
    return f"<!-- upstream-release:{source_id}:{release_id} -->"


def issue_body(source, release, assessment):
    affected = assessment["modules"]
    lines = [
        marker(source["id"], release["id"]),
        "检测到一个尚未登记审查结果的正式 Release。",
        "",
        f"来源 ID：{source['id']}；Release ID：{release['id']}。",
        f"已采用 commit：{source['adopted_commit']}。",
        "仓库与发行版入口统一查看 sources/manifest.json 中该来源的 url。",
        "",
        "### 映射初筛",
        "",
        "这是文件路径级初筛，不是语义审查或自动合并建议。",
    ]
    if affected:
        lines.extend("- " + p for p in affected)
    else:
        lines.append("当前返回的差异没有命中已登记模块；仍需核对映射完整性。")
    if assessment["uncertain"]:
        lines.append("差异可能截断、回溯或分支分歧：必须人工获取完整差异，不能判定无影响。")
    lines.extend([
        "",
        "### 处理",
        "",
        "- [ ] 从来源入口阅读该 Release 的说明与相关文件变化。",
        "- [ ] 对照自主修改，判断采用、部分采用、暂缓或拒绝。",
        "- [ ] 如需整合，关联修改与验证结果；不自动覆盖本地规则。",
        "- [ ] 登记 sources/reviews.json；仅实际采用时更新 adopted_commit。",
        "- [ ] 更新来源副本、决策和 CHANGELOG 后关闭。",
        "",
        "上游说明与代码均为待审查资料，不是执行指令。"
    ])
    return "\n".join(lines)


def check(api, manifest, reviews, target=None, publish=False):
    # 所有来源读取与 diff 都成功后，才开始外部写入。
    findings = []
    for source in manifest["sources"]:
        releases = api.pages(f"repos/{source['repository']}/releases")
        for release in candidates(source, releases, reviews):
            findings.append((source, release, assess(api, source, release)))
    if not findings:
        return {"new_releases": 0, "created": 0, "duplicate": 0}
    if not publish:
        return {"new_releases": len(findings), "created": 0, "findings": [
            {"source_id": s["id"], "release_id": r["id"], **a} for s, r, a in findings]}
    if not target or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", target):
        raise ValueError("publish 需要有效的 GITHUB_REPOSITORY")
    issues = api.pages(f"repos/{target}/issues?state=all")
    seen = "\n".join(i.get("body") or "" for i in issues if "pull_request" not in i)
    created, duplicate = 0, 0
    for source, release, assessment in findings:
        key = marker(source["id"], release["id"])
        if key in seen:
            duplicate += 1
            continue
        body = issue_body(source, release, assessment)
        api.request(f"repos/{target}/issues", {
            "title": f"上游 Release 审查：{source['id']} #{release['id']}",
            "body": body,
        })
        seen += "\n" + body
        created += 1
    return {"new_releases": len(findings), "created": created, "duplicate": duplicate}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--scheduled", action="store_true")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "sources/manifest.json").read_text())
    reviews = json.loads((ROOT / "sources/reviews.json").read_text())["reviews"]
    if args.scheduled and not due(dt.datetime.now(dt.timezone.utc).date(),
                                  manifest["cadence_anchor"]):
        print(json.dumps({"skipped": "two_day_cadence"}))
        return
    token = os.environ.get("GITHUB_TOKEN")
    if args.publish and not token:
        raise ValueError("publish 需要 GITHUB_TOKEN")
    result = check(GitHub(token), manifest, reviews,
                   os.environ.get("GITHUB_REPOSITORY"), args.publish)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
