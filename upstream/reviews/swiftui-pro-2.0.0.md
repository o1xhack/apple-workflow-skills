# SwiftUI Agent Skill 2.0.0 review

Reviewed October 10, 2026 for [Issue #2](https://github.com/o1xhack/apple-workflow-skills/issues/2). Decision: **partial**, independently rewritten into Apple Workflow Skills 0.3.2 after the separate 0.3.1 guided-workflow release.

## Snapshot and scope

- Source: [stable Release 2.0.0](https://github.com/twostraws/SwiftUI-Agent-Skill/releases/tag/2.0.0), Release ID `407978148`, published October 9, 2026.
- Previous baseline: `be297ff80dddec529af1f9b1f1f114aab6c9d11c`.
- Reviewed snapshot: `f9800713b24580bc444931949aad4519128605e8`.
- Read the complete one-commit, 17-file comparison. No truncation or divergent history was used to conclude coverage.
- Advance the reviewed baseline to this snapshot because all changes were considered, not because every upstream rule was adopted. Preserve the historical import Release metadata.

## Integration decisions

| Upstream changes | Local decision and destination |
| --- | --- |
| Root README, marketplace JSON, plugin JSON, and duplicate skill entry | Do not copy distribution metadata, promotional content, or a second entry point. Retain one portable skill and stable Release ZIP installation. |
| Main skill entry: iOS 27, Swift 6.4, SDK versus deployment target | Adopt the toolchain/runtime distinction in `swiftui/references/api.md`; preserve each project's targets. Do not impose iOS 27, Swift 6.4, pure SwiftUI, or one type per file as universal defaults. |
| Review findings and deprecation policy | Treat modernization as scoped advice. A deprecated API can matter to a modernization review without automatically being a defect in unrelated feature work. |
| Accessibility | Adopt `dynamicTypeSize`, action-oriented names, and stable Voice Control labels in `accessibility.md`. Preserve custom gestures and controls with appropriate behavior; do not turn every gesture or fixed dimension into a failure. |
| API replacements and result builders | Add a behavior-aware modernization table and the Xcode 27 builder alias distinction in `api.md`. Older supported spellings and target-compatible fallbacks remain valid. |
| State and bindings | Integrate private-state initialization, one initial value, scene ownership, stable environment defaults, and binding/onChange semantics in `state.md`. Keep isolation in shared concurrency guidance; Observation alone does not make every model main-actor isolated. |
| Identity and enumeration | Consolidate mutable domain identity and iOS 26 enumerated-collection availability in `state.md`. Fixed positions and small unique self-identifying values remain legitimate. |
| Localization and Swift formatting | Add conditionally loaded `localization.md`: preserve existing resources, deferred text, bundles, translator context, generated-symbol configuration, environment overrides, and locale formatting. Both automatic extraction and manually maintained catalog keys are supported. |
| Navigation and item presentations | Clarify per-stack destination registration and compiler-provided item alerts/dialogs in `patterns/navigation.md`. Existing equivalent presentation models remain supported. |
| Toolbar APIs | Integrate general choices in `patterns/controls.md` and wide-iPhone sidebar selection in `duo-bars.md`. Do not repeat the Duo-specific API map. Current toolbar `hidden(_:)` documentation and the installed SDK disagree on iOS support; require checking the actual declaration. |
| Reordering and swipe actions | Integrate the source-of-truth callback, collection identity, external-transfer distinction, older-system fallback, and scroll-view swipe container in `patterns/controls.md`. Do not ship a generic move helper as a universally correct persistence algorithm. |
| Routine performance | Add focused lazy-row, stable-model, modifier-identity, frequent-measurement, and AsyncImage checks to `performance/index.md`. Use cost and lifetime evidence, not the mere presence of a branch or type erasure, to justify changes. |
| Deep performance | Add `performance/deep-review.md`, loaded only for a deep review or established issue. Drop arbitrary three/four-field thresholds; preserve value semantics, explicit cache invalidation, and measured tradeoffs. |
| Resizability and design | Extend existing adaptive guidance for optional size classes and local display scale. Preserve the 0.3.1 product-driven nesting and pose decisions; do not copy a blanket Arrangement nesting prohibition, compulsory vertical bars, or an exhaustive testing gate. |
| Hygiene and release configuration | Add SDK 27 discrete-resizing and launch-screen checks to the readiness audit, supported by TN3192. Inspect real settings before changing product behavior. Dedicated signing/release workflows remain outside this package. |
| Swift concurrency changes | Retain the existing shared concurrency module and project isolation choices. Do not import blanket DispatchQueue bans or add a mandatory Swift upgrade to an unrelated UI task. |

## Evidence and validation limits

The review host is Xcode 27.0 (`27A266a`), Swift 6.4, and iOS Simulator SDK 27.0. Apple documentation, actual SwiftUI/SwiftUICore declarations, and selected Apple-bundled Xcode guidance were read as technical reference material. Their prescriptive wording was not copied as instructions.

Seventeen minimal source probes were typechecked: fourteen compiled and three failed as expected. The passing probes cover builder, State/Entry, item alerts/dialogs, toolbar ForEach back-deployment, resource text fallbacks, iOS 27 toolbars, AsyncImage, and reorder/swipe declarations. The expected failures establish that:

- A runtime guard does not provide `ArrangementView` to SDK 27.0.
- Toolbar-content `hidden(_:)` is unavailable for iOS in that SDK, despite newer documentation listing iOS 26.4.
- The plain resource-title TextField overload is unavailable at an iOS 16 target, while the label-closure fallback compiles.

The Entry probe produced class-default and closure-comparison warnings; a fresh UUID default was not diagnosed. The double-initialization State probe compiled, so the documented declaration-wins behavior is source evidence, not a runtime observation from that probe.

The fixture sources and portable result summary are maintained under `upstream/validation/swiftui-pro-2.0.0/`, outside the installable ZIP. They are targeted compiler checks, not app tests or proof of layout, cache eviction, drag behavior, nested arrangements, or performance improvement. No 27.1/27.2 compilation, Duo Simulator interaction, or physical-device validation is claimed.

Relevant manual routing scenarios are recorded in `tests/routing-cases.md`; they are acceptance criteria, not automatically exercised agent behavior. Structural validation, the existing 21 unit tests, release-check dry run, and package inspection validate the distribution separately.

## Primary references

- [TN3211: State and ContentBuilder source compatibility](https://developer.apple.com/documentation/technotes/tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder)
- [Generated localizable symbols](https://developer.apple.com/documentation/xcode/using-generated-localizable-symbols-in-your-code)
- [Managing model data](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app)
- [ForEach](https://developer.apple.com/documentation/swiftui/foreach)
- [AsyncImage](https://developer.apple.com/documentation/swiftui/asyncimage)
- [TN3192: Full-screen compatibility migration](https://developer.apple.com/documentation/technotes/tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key)
- [Preparing for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo)
- Per-declaration reference URLs and evidence boundaries are recorded in `upstream/apple-references.json`. Existing Duo source tension remains documented in the 0.3.1 decision.
