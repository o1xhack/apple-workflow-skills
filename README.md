<div align="center">

# Apple Workflow Skills

**One installable skill for practical Apple development workflows.**

[![Swift](https://img.shields.io/badge/Swift-6_concurrency-f05138?style=for-the-badge&logo=swift&logoColor=white)](docs/coverage.md)
[![Release](https://img.shields.io/github/v/release/o1xhack/apple-workflow-skills?style=for-the-badge&label=release&color=7c3aed)](https://github.com/o1xhack/apple-workflow-skills/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/o1xhack/apple-workflow-skills/total?style=for-the-badge&label=downloads&color=7c3aed)](https://github.com/o1xhack/apple-workflow-skills/releases)
[![Stars](https://img.shields.io/github/stars/o1xhack/apple-workflow-skills?style=for-the-badge&label=stars&color=7c3aed)](https://github.com/o1xhack/apple-workflow-skills/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/o1xhack/apple-workflow-skills/validate.yml?branch=main&style=for-the-badge&label=CI)](https://github.com/o1xhack/apple-workflow-skills/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/o1xhack/apple-workflow-skills?style=for-the-badge&label=license&color=7c3aed)](LICENSE)
[![Sponsor](https://img.shields.io/badge/GitHub-Sponsors-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/o1xhack)

**English** · [Chinese](README.zh-CN.md)

[Install with your AI agent](#install) · [Download latest release](https://github.com/o1xhack/apple-workflow-skills/releases/latest/download/apple-workflow-skills.zip) · [All versions](https://github.com/o1xhack/apple-workflow-skills/releases)

</div>

Apple Workflow Skills gives your AI agent a shared way to design, build, review, and verify native Apple interfaces. Install once; describe the result you want.

## Install

Choose one option and paste its complete prompt into your AI agent. Installation makes the skill available for selection by description, but does not guarantee selection on every task. Choose the second option to make it the primary workflow for Apple development.

### Option 1: Install only

```text
Install Apple Workflow Skills from the latest stable Release at https://github.com/o1xhack/apple-workflow-skills/releases/latest using its apple-workflow-skills.zip asset only; install the complete folder into your configured skills directory, preserve local customizations, and report the version. If the asset is unavailable, stop. Do not modify AGENTS.md or other global instruction files.
```

### Option 2: Install and set the global default workflow

```text
Install Apple Workflow Skills from the latest stable Release at https://github.com/o1xhack/apple-workflow-skills/releases/latest using its apple-workflow-skills.zip asset only; install the complete folder into your configured skills directory, preserve local customizations, and report the version. If the asset is unavailable, stop.

After successful installation, add the following rule to the user-level global AGENTS.md actually used by this agent. Read existing content first and preserve other rules; do not duplicate an equivalent rule. Once the global path is confirmed, create the file if it does not exist. If you cannot determine this agent's global instruction location, ask me instead of guessing a path or substituting a repository AGENTS.md. Report the installed version, the instruction file path changed, and the final rule.

For Apple UI design, SwiftUI implementation or refactoring, adaptive layouts,
Liquid Glass, UI performance or rendered validation, and Swift concurrency work,
use $apple-workflow-skills as the primary workflow.
Load only the modules relevant to the task; route non-UI concurrency work directly
to its shared Swift concurrency guidance. Preserve project-specific rules and
deployment targets.
```

The second option sets the primary workflow for Apple projects that read those global instructions, while preserving project rules and deployment targets. To apply it to one project only, replace “user-level global AGENTS.md” in the prompt with that project's `AGENTS.md`.

## Update notices

Starting in v0.2.0, an agent using the skill can run its bundled checker: at most one stable Release lookup every seven days, with one notice per new version and no automatic installation. It requires available Python 3 and permitted networking. No update or a failed check stays quiet during normal work. Users can opt out or explicitly request an immediate check. This is not a background notification service; execution depends on the agent following the entry-point guidance.

Existing v0.1.0 installations need one manual update using the installation prompt above to obtain the checker. Subsequent updates still use stable Release ZIPs and preserve local customizations.

## What it covers

- **SwiftUI** — native UI design, navigation, Observation, and view refactoring.
- **Liquid Glass · iOS 26+** — native glass surfaces, grouping, and transitions.
- **Swift 6 concurrency** — actors, Sendable, async tasks, and cancellation.
- **iPhone Duo · Beta** — adaptive and foldable-layout guidance; device-specific validation pending.
- **UI quality** — accessibility, performance review, and Preview / Simulator validation.

[Full coverage →](docs/coverage.md)

v0.2.0 adds focused Duo guidance and [six full English timed transcripts](external-sources/apple/iphone-duo/2026-09-10/README.md), read on demand and excluded from the ZIP.

## Why use it?

**One entry point.** Describe your task; the agent selects the relevant guidance without making you choose between overlapping skills.

**Design through verification.** The workflow connects how an interface should look, how it is built, and what was actually checked.

**Fits your project.** SwiftUI is the implementation focus for native interface work. The guidance follows your existing architecture and supported OS versions, so adopting the skill does not require a framework migration.

## Upstream maintenance

Guidance is selectively combined from MIT-licensed sources and maintained independently. Every two days, upstream stable Releases are checked for changes worth reviewing. Apple SDK changes can also drive updates directly.

Reviewed improvements reach users through a new Release. Installation and updates use published ZIP assets; edits on the default branch do not change an installed version.

[Sources](upstream/manifest.json) · [Integration decisions](docs/decisions.md) · [Maintenance process](docs/maintenance.md)

## Usage and technical details

After installation, ask your agent:

```text
Use $apple-workflow-skills to improve this settings screen's hierarchy and narrow-window layout.
Use $apple-workflow-skills to refactor this view while preserving its behavior.
Use $apple-workflow-skills to diagnose cancellation in this background import.
```

One installable skill routes to **Apple UI Workflow** or **Shared Swift Concurrency**. UI guidance covers design, SwiftUI, layout, glass, performance, and validation; general concurrency can be used independently.

The installable package lives in `skills/apple-workflow-skills/`. Maintainer files live in `upstream/`, `docs/`, `scripts/`, and `tests/` and are excluded from the ZIP.

To update, ask your agent to install the latest stable Release again. To pin a version, use a specific Release page such as `/releases/tag/v0.1.0`. For manual installation, download the Release ZIP and copy its complete folder into your agent's skills directory.

<details>
<summary>Development and validation</summary>

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/check_upstream_releases.py
python3 scripts/package.py --output /tmp/apple-workflow-skills.zip
```

These checks cover package structure, references, English runtime content, attribution, and Release monitoring. Real-app behavior is evaluated separately using [routing scenarios](tests/routing-cases.md).

</details>

## License

[MIT](LICENSE), including the attributions in [Third-Party Notices](THIRD_PARTY_NOTICES.md).
