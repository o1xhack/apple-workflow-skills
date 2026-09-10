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
