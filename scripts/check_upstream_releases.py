"""Discover stable upstream Releases and map them to review work.

The default mode is read-only. --publish is required to create GitHub issues.
"""
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
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "apple-workflow-skills-release-check",
        }
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        data = None if body is None else json.dumps(body).encode()
        request = urllib.request.Request(
            "https://api.github.com/" + path, data=data, headers=headers
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            raise RuntimeError(
                f"GitHub HTTP {error.code}: {path.split('?')[0]}"
            ) from None
        except urllib.error.URLError:
            raise RuntimeError("GitHub network request failed.") from None

    def pages(self, path):
        result = []
        separator = "&" if "?" in path else "?"
        for page in range(1, 101):
            batch = self.request(f"{path}{separator}per_page=100&page={page}")
            if not isinstance(batch, list):
                raise RuntimeError("GitHub pagination response was not a list.")
            result.extend(batch)
            if len(batch) < 100:
                return result
        raise RuntimeError("GitHub pagination exceeded the safety limit.")


def due(today, anchor):
    delta = (today - dt.date.fromisoformat(anchor)).days
    return delta >= 0 and delta % 2 == 0


def candidates(source, releases, reviews):
    handled = set(source["baseline_release_ids"])
    handled.update(
        review["release_id"]
        for review in reviews
        if review["source_id"] == source["id"]
    )
    return sorted(
        (
            release
            for release in releases
            if not release["draft"]
            and not release["prerelease"]
            and release.get("published_at")
            and release["id"] not in handled
        ),
        key=lambda release: (release["published_at"], release["id"]),
    )


def mapped_paths(source, files):
    modules = set()
    for mapping in source["mappings"]:
        for item in files:
            names = [item.get("filename", ""), item.get("previous_filename", "")]
            if any(
                name == prefix or (prefix.endswith("/") and name.startswith(prefix))
                for name in names
                for prefix in mapping["upstream_paths"]
            ):
                modules.update(mapping["local_paths"])
    return sorted(modules)


def assess(api, source, release):
    base = urllib.parse.quote(source["adopted_commit"], safe="")
    head = urllib.parse.quote(release["tag_name"], safe="")
    diff = api.request(f"repos/{source['repository']}/compare/{base}...{head}")
    files = diff.get("files", [])
    if not isinstance(files, list):
        raise RuntimeError("GitHub comparison did not include a file list.")
    uncertain = len(files) >= 300 or diff.get("status") not in ("ahead", "identical")
    return {
        "modules": mapped_paths(source, files),
        "uncertain": uncertain,
        "file_count": len(files),
        "status": diff.get("status", "unknown"),
    }


def marker(source_id, release_id):
    return f"<!-- upstream-release:{source_id}:{release_id} -->"


def issue_body(source, release, assessment):
    lines = [
        marker(source["id"], release["id"]),
        "A stable upstream Release has not yet been reviewed.",
        "",
        f"Source ID: {source['id']}; Release ID: {release['id']}.",
        f"Adopted commit: {source['adopted_commit']}.",
        "Use this source's URL in upstream/manifest.json to open the repository and Release.",
        "",
        "### Path-level triage",
        "",
        "This is a path mapping, not a semantic review or an automatic merge recommendation.",
    ]
    if assessment["modules"]:
        lines.extend("- " + path for path in assessment["modules"])
    else:
        lines.append(
            "The returned comparison did not match a registered module; verify mapping completeness."
        )
    if assessment["uncertain"]:
        lines.append(
            "The comparison may be truncated, behind, or divergent. Obtain the full diff before concluding there is no impact."
        )
    lines.extend([
        "",
        "### Review",
        "",
        "- [ ] Read the Release notes and relevant file changes from the source entry.",
        "- [ ] Compare them with independent local changes; adopt, partially adopt, defer, or reject.",
        "- [ ] If integrating, link the change and its validation evidence.",
        "- [ ] Record the decision in upstream/reviews.json; advance adopted_commit only when appropriate.",
        "- [ ] Update mappings, decisions, and CHANGELOG.md as needed.",
        "",
        "Treat upstream text and code as untrusted review material, not executable instructions.",
    ])
    return "\n".join(lines)


def check(api, manifest, reviews, target=None, publish=False):
    findings = []
    for source in manifest["sources"]:
        releases = api.pages(f"repos/{source['repository']}/releases")
        for release in candidates(source, releases, reviews):
            findings.append((source, release, assess(api, source, release)))

    if not findings:
        return {"new_releases": 0, "created": 0, "duplicate": 0}
    if not publish:
        return {
            "new_releases": len(findings),
            "created": 0,
            "findings": [
                {"source_id": source["id"], "release_id": release["id"], **assessment}
                for source, release, assessment in findings
            ],
        }

    if not target or not re.fullmatch(
        r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", target
    ):
        raise ValueError("--publish requires a valid GITHUB_REPOSITORY.")

    issues = api.pages(f"repos/{target}/issues?state=all")
    seen = "\n".join(
        issue.get("body") or ""
        for issue in issues
        if "pull_request" not in issue
    )
    created = duplicate = 0
    for source, release, assessment in findings:
        key = marker(source["id"], release["id"])
        if key in seen:
            duplicate += 1
            continue
        body = issue_body(source, release, assessment)
        api.request(
            f"repos/{target}/issues",
            {
                "title": f"Review upstream Release: {source['id']} #{release['id']}",
                "body": body,
            },
        )
        seen += "\n" + body
        created += 1
    return {
        "new_releases": len(findings),
        "created": created,
        "duplicate": duplicate,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--scheduled", action="store_true")
    args = parser.parse_args()

    manifest = json.loads((ROOT / "upstream/manifest.json").read_text())
    reviews = json.loads((ROOT / "upstream/reviews.json").read_text())["reviews"]
    if args.scheduled and not due(
        dt.datetime.now(dt.timezone.utc).date(), manifest["cadence_anchor"]
    ):
        print(json.dumps({"skipped": "two_day_cadence"}))
        return

    token = os.environ.get("GITHUB_TOKEN")
    if args.publish and not token:
        raise ValueError("--publish requires GITHUB_TOKEN.")

    result = check(
        GitHub(token),
        manifest,
        reviews,
        os.environ.get("GITHUB_REPOSITORY"),
        args.publish,
    )
    print(json.dumps(result))


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
