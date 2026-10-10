# Integration decisions

## 2026-10-10 — Guidance supports engineering judgment

- Treat the user's intended product behavior as the starting point across the package. Native controls, familiar navigation, simple composition, and Apple recommendations remain useful defaults, not a compliance gate. When those defaults cannot express the experience, explore custom composition, framework bridging, or other approaches and validate the relevant behavior.
- Distinguish design preferences from concrete SDK availability, state correctness, and scope or permission constraints. A design departure alone is neither a defect nor a reason to refuse implementation, require special approval, or impose an exhaustive validation matrix.
- Refine the October 6 arrangement decision: the current HIG explicitly describes navigation split and tab containers around arrangements, while the preparation article advises avoiding an arrangement inside a navigation split view or scrolling container because content may become inaccessible. Preserve this source tension instead of converting one recommendation into a universal ban. A sidebar with an arrangement in its detail has a plausible product purpose; evaluate navigation ownership, bounds, secondary access, and continuity in the actual composition. This is not a claim of completed 27.1 compilation or device validation.
- Audit the runtime modules for advice that could override a deliberate product choice. Reframe pose-specific features, custom bars, vertical-bar opt-outs, grid columns, and navigation nesting around their purposes and costs. Retain concrete technical facts and evidence boundaries.
- Publish this revision as 0.3.1, separately from the pending upstream 2.0.0 review. Published assets and the shared installed skill are separate distribution steps.

## 2026-10-06 — Current Duo declarations and readiness workflow

- Use current Apple preparation and camera documentation plus individual API declarations to update runtime decisions. Six September caption archives remain immutable historical sources; new Group Lab pages and Q&A indexes do not imply complete transcript or answer coverage.
- Separate an app's build SDK from deployment target and runtime OS. Apple documents different presentation defaults for SDK 26 and earlier, 27.0, and 27.1. Supporting bar/scene/motion APIs are not uniformly 27.1-only; record minimum iOS versions per declaration in `upstream/apple-references.json`.
- Replace singular transcript-derived region names with the documented plural queries. Check region active state explicitly, and account for SwiftUI's mirrored geometry in RTL. The region-query discussion broadly mentions inactive regions while the separate `includeInactive` option explicitly includes them; do not infer a default-result guarantee without SDK testing.
- Resolve arrangement guidance in favor of the current preparation article and focused staff navigation answer: split containers own hierarchical navigation; arrangements do not sit inside a navigation split, list, or scroll container. A surrounding navigation stack is supported by the staff's pane-local safe-area example. Do not turn this into a ban on every outer navigation container.
- Adopt the later Apple staff correction that ARKit capture qualifies for a camera accessory, preserving the distinction from a second full AR experience. Current accessory documentation establishes touch and separate availability/enablement. Earlier conflicting forum replies do not override the later clarification.
- Keep overflow confirmation state on a persistent view, but leave the unanswered SwiftUI overflow-button anchor question unresolved. User reports of Simulator automation gaps do not establish a supported fold command.
- Apply skill-creator's progressive disclosure: keep the top-level entry short, retain topic ownership in existing modules, and load the new audit/validation reference only for readiness work. Do not copy or install exported Apple skills. Xcode 27.0's exported inventory lacks the advertised resizability skill; this is a local tool-version observation.
- Keep external reading in one catalog. Add only official preparation and numeric Developer Forums Q&A URLs to its allowlist; adopt staff answers, not user questions. Preserve the package's English, portability, source, and license boundaries.
- The initial refresh was prepared without changing the distribution version or installed shared skill. Release preparation assigns its own version; previously published assets remain unchanged.

## 2026-10-06 — Version 0.3.0

- Publish the reviewed Duo refresh as a new stable 0.3.0 distribution, including the conditionally loaded readiness audit and corrected current API guidance. Keep the Duo Beta maturity designation and all 27.1 compilation, Simulator, and hardware evidence gaps explicit.
- Preserve the 0.1.0 and 0.2.0 tags/assets and original caption archive. Installation and upgrades use the new version-specific stable ZIP; publishing does not automatically install or modify global instructions.

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
