<div align="center">

# Apple Workflow Skills

**One installable skill for practical Apple development workflows.**

[![iPhone and iPad](https://img.shields.io/badge/iPhone_%26_iPad-SwiftUI_guidance-007aff?style=for-the-badge)](docs/coverage.md)
[![iPhone Duo](https://img.shields.io/badge/iPhone_Duo-Beta_guidance-f59e0b?style=for-the-badge)](docs/coverage.md)

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

Paste this into your AI agent:

```text
Install Apple Workflow Skills from the latest stable Release at https://github.com/o1xhack/apple-workflow-skills/releases/latest using its apple-workflow-skills.zip asset only; install the complete folder into your configured skills directory, preserve local customizations, and report the version. If the asset is unavailable, stop.
```

## What it covers

The current release focuses on **SwiftUI interfaces and Swift concurrency**, with guidance applied to your project's Apple platforms and OS versions.

| Capability | What it helps you do | When to use it |
| --- | --- | --- |
| Apple UI Workflow | Connect design, implementation, and visual checks into one process | Build a screen or improve an existing flow |
| Design Principles | Make information, actions, spacing, and typography easier to understand | A screen feels cluttered or its priorities are unclear |
| SwiftUI | Build and refactor native components, navigation, forms, and state | Add a feature or simplify an existing view |
| Adaptive Layout & Liquid Glass | Fit changing window sizes and apply native glass materials | Adapt an interface or update its visual treatment |
| UI Performance & Validation | Investigate slow UI and choose Preview, Simulator, or device checks | Scrolling stutters or a change needs verification |
| Swift Concurrency | Reason about background work, shared data, and cancellation | Imports, searches, or async operations behave inconsistently |

**iPhone Duo adaptation — Beta, partial coverage.** General layout and state-continuity guidance is included; dedicated Duo APIs and device behavior still need validation.

Dedicated SwiftData, Swift Testing, widgets, App Intents, signing, App Store release, UIKit, and AppKit workflows are not included yet.

[Explore coverage by Apple framework and API topic →](docs/coverage.md)

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
