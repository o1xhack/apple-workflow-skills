"""Validate the installable skill's closure, attribution, and portability.

This static check does not claim that Swift runtime behavior has been tested.
"""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/apple-workflow-skills"
CHINESE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


def allowed_reading_url(href):
    url = urlsplit(href)
    if url.scheme != "https" or url.username or url.password or url.query:
        return False
    if url.netloc == "developer.apple.com":
        return url.path.startswith(("/documentation/", "/design/", "/videos/play/")) or url.path == "/iphone-duo/"
    return url.netloc == "raw.githubusercontent.com" and bool(re.fullmatch(
        r"/o1xhack/apple-workflow-skills/[0-9a-f]{40}/external-sources/apple/iphone-duo/2026-09-10/(?:11146[1-6]|README)\.md",
        url.path,
    ))


def validate_archive(root):
    errors = []
    folder = root / "external-sources/apple/iphone-duo/2026-09-10"
    manifest = folder / "manifest.json"
    if not manifest.exists():
        return ["Missing Duo external-source manifest."]
    try:
        records = json.loads(manifest.read_text())["videos"]
        if len(records) != 6 or {v["id"] for v in records} != {str(n) for n in range(111461, 111467)}:
            errors.append("Duo archive must contain all six unique sessions.")
        expected = {"README.md", "manifest.json"}
        for video in records:
            for kind, suffix in (("vtt", ".en.vtt"), ("transcript", ".md")):
                filename = video["id"] + suffix
                if video[kind] != filename:
                    errors.append("Invalid archive path: " + video[kind])
                    continue
                expected.add(filename)
                path = folder / filename
                if not path.is_file() or path.is_symlink():
                    errors.append("Missing or indirect source: " + filename)
                elif hashlib.sha256(path.read_bytes()).hexdigest() != video[kind + "_sha256"]:
                    errors.append("Source checksum mismatch: " + filename)
        if {p.name for p in folder.iterdir()} != expected:
            errors.append("Duo archive must contain only its manifest, index, captions, and transcripts.")
    except (ValueError, KeyError, TypeError) as error:
        errors.append("Invalid Duo source manifest: " + str(error))
    return errors


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
        catalog = path == SKILL / "workflows/apple-ui/swiftui/references/duo-sources.md"
        if re.search(r"/Users/|/home/|TODO|PLACEHOLDER", text) or (not catalog and re.search(r"https?://", text)):
            errors.append("Runtime guidance contains a forbidden external value: " + relative)
        links = []
        for href in re.findall(r"\]\(([^)]+)\)", text):
            if urlsplit(href).scheme or href.startswith("//"):
                if not catalog or not allowed_reading_url(href):
                    errors.append("Unapproved external reading URL: " + href)
                continue
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

    errors.extend(validate_archive(ROOT))
    return errors


if __name__ == "__main__":
    issues = validate()
    print("\n".join(issues) if issues else "Skill structure, English content, attribution, and portability checks passed.")
    sys.exit(bool(issues))
