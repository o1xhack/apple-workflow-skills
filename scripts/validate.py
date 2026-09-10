"""Validate the installable skill's closure, attribution, and portability.

This static check does not claim that Swift runtime behavior has been tested.
"""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/apple-workflow-skills"
CHINESE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


def validate():
    errors = []
    skill_files = list((ROOT / "skills").rglob("SKILL.md"))
    if skill_files != [SKILL / "SKILL.md"]:
        errors.append("The repository must contain exactly one installable SKILL.md.")

    entry = (SKILL / "SKILL.md").read_text()
    for field in ("name: apple-workflow-skills", "description:", "license: MIT"):
        if field not in entry:
            errors.append("Top-level frontmatter is missing: " + field)
    if not entry.startswith("---\n"):
        errors.append("Invalid SKILL.md frontmatter.")
    if not (SKILL / "LICENSE").is_file():
        errors.append("The installable skill must include LICENSE.")

    manifest = json.loads((ROOT / "upstream/manifest.json").read_text())
    ids = set()
    for source in manifest["sources"]:
        if source["id"] in ids:
            errors.append("Duplicate upstream source ID: " + source["id"])
        ids.add(source["id"])
        if not re.fullmatch(r"[0-9a-f]{40}", source["adopted_commit"]):
            errors.append("Adopted commits must be full SHAs: " + source["id"])
        if source["tracking"] != "stable_releases_only":
            errors.append("Commit polling is not allowed: " + source["id"])
        if source["license"] != "MIT" or "Copyright" not in source["copyright"]:
            errors.append("Missing MIT attribution: " + source["id"])
        for mapping in source["mappings"]:
            for target in mapping["local_paths"]:
                if not (SKILL / target).exists():
                    errors.append("Missing mapped runtime target: " + target)

    reviews = json.loads((ROOT / "upstream/reviews.json").read_text())["reviews"]
    for review in reviews:
        if review["source_id"] not in ids or review["decision"] not in (
                "adopt", "partial", "defer", "reject"):
            errors.append("Invalid upstream review record.")

    graph = {}
    runtime_files = (
        {SKILL / "SKILL.md"}
        | set((SKILL / "workflows").rglob("*.md"))
        | set((SKILL / "shared").rglob("*.md"))
    )
    for path in runtime_files:
        text = path.read_text()
        relative = str(path.relative_to(ROOT))
        if CHINESE.search(text):
            errors.append("Runtime guidance must be English: " + relative)
        if re.search(r"https?://|/Users/|/home/|TODO|PLACEHOLDER", text):
            errors.append("Runtime guidance contains a forbidden external value: " + relative)
        links = []
        for href in re.findall(r"\]\(([^)]+)\)", text):
            target = (path.parent / href.split("#")[0]).resolve()
            if not target.is_relative_to(SKILL.resolve()):
                errors.append("Runtime link escapes the installable skill: " + href)
            elif not target.exists():
                errors.append("Broken runtime link: " + relative + " -> " + href)
            else:
                links.append(target)
        graph[path.resolve()] = links

    reachable = set()
    pending = [(SKILL / "SKILL.md").resolve()]
    while pending:
        path = pending.pop()
        if path not in reachable:
            reachable.add(path)
            pending.extend(graph.get(path, []))
    for path in runtime_files:
        if path.resolve() not in reachable:
            errors.append("Unreachable runtime module: " + str(path.relative_to(ROOT)))

    forbidden_install_paths = [SKILL / "sources", SKILL / "upstream"]
    if any(path.exists() for path in forbidden_install_paths):
        errors.append("Maintainer-only provenance must not be bundled in the skill.")

    for path in SKILL.rglob("*"):
        if path.is_symlink():
            errors.append("The installable skill must not depend on symlinks: " + str(path))

    allowed_chinese = {ROOT / "README.zh-CN.md", ROOT / "docs/coverage.zh-CN.md"}
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path in allowed_chinese:
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        if CHINESE.search(text):
            errors.append("Chinese text must be in an approved translated document: " + str(path.relative_to(ROOT)))

    return errors


if __name__ == "__main__":
    issues = validate()
    print("\n".join(issues) if issues else "Skill structure, English content, attribution, and portability checks passed.")
    sys.exit(bool(issues))
