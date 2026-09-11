"""Optional, bounded stable-release notice. Never installs or executes remote content."""
import argparse
import json
import os
from pathlib import Path
import re
import time
import urllib.request

REPOSITORY = "https://github.com/o1xhack/apple-workflow-skills"
API = "https://api.github.com/repos/o1xhack/apple-workflow-skills/releases/latest"
INTERVAL = 7 * 24 * 60 * 60


def version(value):
    if not isinstance(value, str) or not re.fullmatch(r"v?(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", value):
        raise ValueError("Expected stable semantic version")
    return tuple(map(int, value.removeprefix("v").split(".")))


def installed_version():
    text = (Path(__file__).resolve().parents[1] / "SKILL.md").read_text()
    value = re.search(r'^  version: "([^"]+)"$', text, re.M).group(1)
    version(value)
    return value


def fetch_release():
    request = urllib.request.Request(API, headers={"Accept": "application/vnd.github+json", "User-Agent": "apple-workflow-skills-update-check"})
    with urllib.request.urlopen(request, timeout=5) as response:
        data = response.read(1024 * 1024 + 1)
    if len(data) > 1024 * 1024:
        raise ValueError("Response too large")
    return json.loads(data)


def check(current, cache, now, fetch=fetch_release, force=False):
    current_version = version(current)
    last = cache.get("checked_at", 0)
    if not force and cache.get("installed_version") == current and isinstance(last, (int, float)) and 0 <= now - last < INTERVAL:
        return {"status": "cached"}, cache
    state = {"checked_at": now, "installed_version": current, "notified_version": cache.get("notified_version")}
    try:
        release = fetch()
        tag = release.get("tag_name")
        latest = version(tag)
        if release.get("draft") is not False or release.get("prerelease") is not False:
            raise ValueError("Not a stable release")
        asset_url = f"{REPOSITORY}/releases/download/{tag}/apple-workflow-skills.zip"
        if not any(a.get("name") == "apple-workflow-skills.zip" and a.get("browser_download_url") == asset_url and a.get("state") == "uploaded" for a in release.get("assets", [])):
            raise ValueError("Stable asset unavailable")
        if latest <= current_version:
            return {"status": "up_to_date", "installed_version": current}, state
        if not force and state["notified_version"] == tag:
            return {"status": "already_notified"}, state
        state["notified_version"] = tag
        return {"status": "update_available", "installed_version": current, "latest_version": tag,
                "release_url": f"{REPOSITORY}/releases/tag/{tag}", "asset_url": asset_url}, state
    except (OSError, ValueError, TypeError, AttributeError):
        # Cache failed attempts too; this optional check must not become a retry loop.
        return {"status": "unavailable"}, state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Explicit user-requested check, bypassing cache and notice deduplication")
    args = parser.parse_args()
    cache_home = Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache")
    path = cache_home / "apple-workflow-skills" / "update-check.json"
    try:
        cache = json.loads(path.read_text())
        if not isinstance(cache, dict):
            cache = {}
    except (OSError, ValueError):
        cache = {}
    try:
        result, state = check(installed_version(), cache, time.time(), force=args.force)
        path.parent.mkdir(parents=True, exist_ok=True)
        temp = path.with_name(f"update-check-{os.getpid()}.tmp")
        temp.write_text(json.dumps(state) + "\n")
        temp.replace(path)
    except (OSError, ValueError, AttributeError):
        result = {"status": "unavailable"}
    print(json.dumps(result))


if __name__ == "__main__":
    main()
