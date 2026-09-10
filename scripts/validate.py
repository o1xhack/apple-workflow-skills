"""校验安装闭包、来源一致性与可移植性，不宣称 Swift 运行行为通过。"""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/apple-workflow-skills"


def validate():
    errors = []
    if list((ROOT / "skills").rglob("SKILL.md")) != [SKILL / "SKILL.md"]:
        errors.append("必须只有一个可安装 SKILL.md")
    entry = (SKILL / "SKILL.md").read_text()
    for field in ("name: apple-workflow-skills", "description:", "license: MIT"):
        if field not in entry:
            errors.append("顶层 frontmatter 缺少 " + field)
    if not entry.startswith("---\n"):
        errors.append("frontmatter 格式错误")
    manifest = json.loads((ROOT / "sources/manifest.json").read_text())
    portable = json.loads((SKILL / "sources/manifest.json").read_text())
    if manifest != portable:
        errors.append("sources 两份 manifest 不一致")
    ids = set()
    for source in manifest["sources"]:
        if source["id"] in ids:
            errors.append("重复 source ID")
        ids.add(source["id"])
        if not re.fullmatch(r"[0-9a-f]{40}", source["adopted_commit"]):
            errors.append("采用 commit 必须是完整 SHA")
        if source["tracking"] != "stable_releases_only":
            errors.append("不允许 commit 轮询")
        license_path = SKILL / "sources/licenses" / (source["id"] + ".txt")
        if not license_path.is_file() or "Copyright" not in license_path.read_text():
            errors.append("缺少原版权许可：" + source["id"])
        for mapping in source["mappings"]:
            for target in mapping["local_paths"]:
                if not (SKILL / target).exists():
                    errors.append("映射目标不存在：" + target)
    for review in json.loads((ROOT / "sources/reviews.json").read_text())["reviews"]:
        if review["source_id"] not in ids or review["decision"] not in (
                "adopt", "partial", "defer", "reject"):
            errors.append("审查记录无效")
    graph = {}
    runtime_files = {SKILL / "SKILL.md"} | set((SKILL / "workflows").rglob("*.md")) | set(
        (SKILL / "shared").rglob("*.md"))
    for path in runtime_files:
        text = path.read_text()
        if re.search(r"https?://|/Users/|/home/|TODO|PLACEHOLDER", text):
            errors.append("运行模块包含外部链接、个人路径或占位：" + str(path.relative_to(ROOT)))
        links = []
        for href in re.findall(r"\]\(([^)]+)\)", text):
            target = (path.parent / href.split("#")[0]).resolve()
            if not target.is_relative_to(SKILL.resolve()):
                errors.append("引用逃出安装包：" + href)
            elif not target.exists():
                errors.append("失效引用：" + str(path.relative_to(ROOT)) + " -> " + href)
            else:
                links.append(target)
        graph[path.resolve()] = links
    reachable, pending = set(), [(SKILL / "SKILL.md").resolve()]
    while pending:
        path = pending.pop()
        if path not in reachable:
            reachable.add(path)
            pending.extend(graph.get(path, []))
    for path in runtime_files:
        if path.resolve() not in reachable:
            errors.append("顶层不可达模块：" + str(path.relative_to(ROOT)))
    for path in SKILL.rglob("*"):
        if path.is_symlink():
            errors.append("安装包不允许依赖 symlink：" + str(path))
    return errors


if __name__ == "__main__":
    issues = validate()
    print("\n".join(issues) if issues else "安装引用、来源许可、单入口与可移植性检查通过")
    sys.exit(bool(issues))
