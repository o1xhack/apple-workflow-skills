# Integration decisions

## 2026-09-10 — Initial release

- The top-level entry point covers Apple development. Swift concurrency is shared infrastructure, not a child of UI.
- The package exposes one `SKILL.md`; internal indexes and references are loaded only through explicit routing.
- Overlapping state, navigation, component, refactoring, and performance guidance from multiple sources is consolidated into one maintained SwiftUI branch.
- Design guidance keeps consistency, semantic hierarchy, and native-component principles without inventing universal font, spacing, corner-radius, or layout bans.
- MV and MVVM remain project decisions. Views are split by responsibility, state, and preview boundaries, not a fixed line count or one-type-per-file rule.
- `await` is a potential suspension point, not a guarantee that execution suspends. An actor's synchronous segment cannot be interleaved by another actor call. Caching a local result does not prevent duplicate downloads; shared tasks need explicit cancellation and invalidation semantics.
- A child throwing inside an ordinary throwing task group does not by itself guarantee immediate sibling cancellation. Propagation depends on the group API and how results are consumed.
- `AsyncStream.finish()` is idempotent; it must not be confused with a checked continuation's exactly-once resume contract.
- Liquid Glass guidance preserves native materials and grouping APIs while avoiding invented fixed padding rules. Glass in scrolling content is a design and performance risk to measure, not a blanket compile-time prohibition.
- Foldable guidance keeps scenario and validation principles. Unverified device names, hinge callbacks, and future toolchain APIs are not copied into production examples.
- Source URLs and provenance live in `upstream/`. The installable skill carries a combined MIT license notice.
- Only stable upstream Releases are monitored. Sources without releases are not polled by commit.

## 2026-09-10 — Explicit global workflow opt-in

- Offer separate install-only and install-with-global-workflow prompts in both READMEs so installation does not implicitly change agent-wide instructions.
- Resolve the agent's actual global instruction location rather than assuming a portable path; preserve existing rules and avoid equivalent duplicates. Project rules and deployment targets remain authoritative.
- Both options retain the stable Release ZIP installation contract. This documentation change does not alter runtime guidance or published assets.

## 2026-09-10 — Duo core guidance and optional source library

- Review the official Duo HIG and all six supplied English caption tracks. Replace the general-only foldable note with a short entry point and conditional layout, bars, and scenes/camera modules. Keep generic adaptive layout authoritative in its existing module.
- Include decisions that affect routine app work: pose continuity, small targeted displacement, scrolling exceptions, container ownership, vertical controls/overflow, dynamic scene availability, and camera isolation. Keep full narration and detailed visual examples external.
- Add a narrowly scoped external-link exception for one reading catalog. Permit official Apple resources and immutable repository transcript URLs; preserve local-only links elsewhere and keep upstream project promotion out of runtime guidance.
- Archive the user-supplied English captions separately from the MIT package. Keep raw bytes plus reading copies with exact duplicate cues removed and hash verification. Do not upload video or frames. Keep the supplied Chinese captions outside this English repository archive.
- Source review found no populated transcript sections on the six live video pages. The HIG was dated September 9, 2026; the hub still marked Xcode 27.1 beta as coming later in September. API names in the modules are video-described discovery terms, with SDK and hardware validation pending.
- Mark this runtime revision 0.2.0-dev. Do not replace v0.1.0 tags/assets or update an installed copy from a branch; distribute later through a new stable Release.

## 2026-09-10 — Version 0.2.0 and optional update notices

- Graduate the reviewed repository revision from 0.2.0-dev to the 0.2.0 distribution; Duo SDK and hardware evidence boundaries remain unchanged.
- Add a standard-library-only helper that reads this repository's stable Release metadata with a five-second timeout and bounded response. Accept only stable numeric versions and the expected uploaded ZIP asset; ignore remote release prose.
- Store only version and check timestamps in the user's cache, outside projects and the installed skill. Rate-limit normal checks to seven days, including failures; notify once per newer tag. Explicit checks bypass the cache. Never install automatically or run a background service.
- The source-catalog external-link rule applies to reading material. The update helper's fixed GitHub API endpoint and Release URLs are the narrowly scoped tooling exception; no credentials or project content are sent.
- Older installations cannot discover this mechanism until manually updated once. Agent compliance and tool availability govern usage-time checks; do not promise guaranteed notifications.
