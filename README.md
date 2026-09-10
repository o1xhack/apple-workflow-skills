<div align="center">

# Apple Workflow Skills

**One installable skill for practical Apple development workflows.**

[![Release](https://img.shields.io/github/v/release/o1xhack/apple-workflow-skills?style=for-the-badge&label=release&color=7c3aed)](https://github.com/o1xhack/apple-workflow-skills/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/o1xhack/apple-workflow-skills/total?style=for-the-badge&label=downloads&color=7c3aed)](https://github.com/o1xhack/apple-workflow-skills/releases)
[![Stars](https://img.shields.io/github/stars/o1xhack/apple-workflow-skills?style=for-the-badge&label=stars&color=7c3aed)](https://github.com/o1xhack/apple-workflow-skills/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/o1xhack/apple-workflow-skills/validate.yml?branch=main&style=for-the-badge&label=CI)](https://github.com/o1xhack/apple-workflow-skills/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/o1xhack/apple-workflow-skills?style=for-the-badge&label=license&color=7c3aed)](LICENSE)
[![Sponsor](https://img.shields.io/badge/GitHub-Sponsors-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/o1xhack)

**English** · [Chinese](README.zh-CN.md)

[Install with your AI agent](#install) · [Download latest release](https://github.com/o1xhack/apple-workflow-skills/releases/latest/download/apple-workflow-skills.zip) · [All versions](https://github.com/o1xhack/apple-workflow-skills/releases)

</div>

Apple Workflow Skills is a single entry-point skill that routes Apple development work to focused guidance without loading the entire library. The first release concentrates on native UI work—design, SwiftUI implementation, adaptive layout, Liquid Glass, performance, and real UI validation—while general Swift concurrency remains a separate shared branch.

## Install

Copy this prompt into your AI agent:

```text
Install or update Apple Workflow Skills from https://github.com/o1xhack/apple-workflow-skills/releases/latest: resolve the latest published stable Release, download its apple-workflow-skills.zip asset using the version-specific URL, extract and install the complete apple-workflow-skills folder into this agent's configured skills directory, preserve any local customizations before replacing an existing installation, and report the installed version; do not install from main, repository source archives, drafts, or prereleases, and stop if the Release asset is unavailable.
```

The agent handles the download and installation. To install a specific version, replace `/releases/latest` in the prompt with `/releases/tag/v0.1.0` (or the version you want).

Installations and updates use published Release assets. Changes pushed to `main` become available to users only when a new Release is published. An existing installation stays on its installed version until you ask the agent to update it.

For manual installation, [download the latest Release ZIP](https://github.com/o1xhack/apple-workflow-skills/releases/latest/download/apple-workflow-skills.zip) and copy the complete folder into your agent's skills directory. This link serves the published ZIP, even when `main` contains newer edits.

## Architecture

```text
apple-workflow-skills
├── Apple UI Workflow
│   ├── Design Principles
│   ├── SwiftUI
│   │   ├── API and state ownership
│   │   ├── Navigation and controls
│   │   ├── Adaptive and foldable layouts
│   │   └── Behavior-preserving refactoring
│   ├── Liquid Glass
│   ├── UI Performance
│   └── Preview, Simulator, and device validation
└── Shared Swift Concurrency
    ├── Isolation and Sendable
    ├── Tasks and cancellation
    └── Streams and callback bridging
```

There is exactly one installable `SKILL.md`. The nested Markdown files are conditionally loaded modules, not separately installed skills.

Concurrency is intentionally outside Apple UI Workflow. UI-specific async state links to it when needed, but networking, file imports, databases, and background services can use the same concurrency guidance without loading UI material.

## Usage

```text
Use $apple-workflow-skills to review this settings screen's hierarchy and narrow-window behavior.
Use $apple-workflow-skills to refactor this SwiftUI view while preserving its MVVM architecture.
Use $apple-workflow-skills to diagnose actor reentrancy in this background import service.
```

The skill preserves the current project's architecture, deployment targets, and product decisions. It chooses only the modules needed for the task and distinguishes code review, compilation, rendered UI inspection, Simulator interaction, and physical-device evidence.

## Repository layout

- `skills/apple-workflow-skills/` — the complete installable artifact.
- `upstream/` — maintainer-only provenance, adopted commits, Release baselines, and review state.
- `docs/` — integration and maintenance decisions.
- `scripts/` and `tests/` — deterministic validation, packaging, and upstream Release monitoring.

The `upstream/` directory and repository tooling are intentionally excluded from Release ZIPs. The installable folder keeps only runtime guidance and a combined MIT license notice.

## Scope

The initial release covers SwiftUI-centric UI work and shared Swift concurrency. It does not claim dedicated workflows for SwiftData, Swift Testing, signing, App Store release, widgets, App Intents, UIKit, or AppKit.

Foldable and multi-display guidance is conservative: general adaptive-layout principles are included, while unverified APIs and device assumptions are not presented as production-ready facts.

## Upstream maintenance

This project selectively integrates and independently rewrites ideas from MIT-licensed sources. It is not a mirror. Attribution, exact adopted commits, and module mappings live in [upstream/manifest.json](upstream/manifest.json); license notices live in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

A scheduled workflow checks upstream stable GitHub Releases every two days. New releases create review issues; they never overwrite local guidance or publish a new version automatically. Apple SDK changes may also drive independent updates without waiting for an upstream release.

## Development

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/check_upstream_releases.py
python3 scripts/package.py --output /tmp/apple-workflow-skills.zip
```

Static validation checks the single-entry structure, internal link closure, English runtime content, attribution, and packaging. It does not claim real-app UI or concurrency behavior has been validated.

## License

Apple Workflow Skills is released under the [MIT License](LICENSE). Portions are based on MIT-licensed work listed in [Third-Party Notices](THIRD_PARTY_NOTICES.md).
