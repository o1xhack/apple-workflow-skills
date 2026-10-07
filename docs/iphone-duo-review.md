# iPhone Duo coverage review

Refreshed October 6, 2026 for v0.3.0 against the [official hub](https://developer.apple.com/iphone-duo/), [preparation checklist](https://developer.apple.com/iphone-duo/prepare/), current HIG and preparation documentation, camera articles, individual declarations, and selected Apple staff Q&A. Version 0.2.0 retains the September 10 guidance; installed copies receive this revision through the v0.3.0 stable Release ZIP.

## October refresh

| Evidence | Change to runtime guidance | Review boundary |
| --- | --- | --- |
| Hub and preparation checklist | Xcode 27.1 RC status; separate SDK 26/27.0/27.1 presentation from deployment target; concrete resizing audit | Tool listing does not prove local installation |
| Preparation article and region declarations | Plural queries returning arrays; active-state handling; margins and RTL geometry; outer versus active inner camera occlusion | Inactive-result default needs SDK verification; check `isActive` explicitly |
| Arrangement article and focused navigation/pane Q&A | Keep hierarchical navigation in split containers; avoid arrangements inside split/list/scroll; attach safe-area bars to a pane | A surrounding navigation stack is valid; do not ban all navigation wrappers |
| Bar declarations | Correct `toolbarVerticalCompressionBehavior`; distinguish 27.0 supporting APIs from 27.1 vertical participation; sheet placement rules | Each UIKit/SwiftUI/platform declaration has its own availability |
| Camera direction article | Virtual discovery; per-view direction maps; Sendable descriptors; serialized capture ownership; switch/mirror/rotation transitions | Runtime formats and lens behavior require hardware |
| Camera accessory article and later ARKit staff reply | Outer touch; separate enablement and availability; retained shared state/registration; ARSession eligibility | Accessory enhances capture, not a second independent AR experience |
| Core Motion declarations | Optional view-relative motion using `deviceMotionBody` / `CMBodyIdentifiable` (iOS 27.0) | Not an ordinary-layout API |
| Device Hub documentation | Separate native Duo simulation, generic resizing, interaction and physical capture evidence | Physical-device interaction in Device Hub excludes camera/microphone |
| Overflow and fold-automation threads | Persistent confirmation state; do not invent a SwiftUI overflow anchor or fold CLI | Later user questions remain unresolved at review |

Thirty-two current API declarations and their minimum iOS versions are recorded in [Apple evidence](../upstream/apple-references.json). Exact names now come from documentation rather than caption spellings. The original transcripts remain useful for context but do not override current declarations.

The two Group Lab recording pages and three Q&A indexes were inventoried. Selected staff answers were read, including later corrections; this review does not claim complete lab transcription, exhaustive forum coverage, or that every original video changed. HIG page history still lists its September 9 introduction, so new hub material alone does not establish a HIG revision.

## Validation collected

- Local toolchain: Xcode 27.0, build 27A266a, iOS 27.0 SDK. No Xcode 27.1 installation or target upgrade was performed.
- An isolated iOS 27.0 `swiftc -typecheck` probe passed for SwiftUI pinned trailing placement, item visibility priority, overflow and sheet placement, UIKit item priority/sheet placement, and Core Motion view-relative motion. This verifies only those declarations on that SDK, not a complete Duo app.
- `xcrun agent skills export` succeeded with ten local Apple skills. Its inventory did not contain the preparation page's advertised resizability skill. Exported material was inspected as tool availability, not copied or installed into this package.
- iOS 27.1 compilation, native Duo Simulator interaction, and physical-device fold/capture behavior remain unverified. The new routing cases are acceptance criteria, not executed real-app QA.

The skill-creator review kept a single short entry point and existing topic ownership, adding only a conditionally loaded readiness audit. New external reading stays in the source catalog; packaging excludes both captions and exported Apple skills.

## September 10 baseline

The initial review used the official hub, Duo HIG, and [six user-supplied English caption tracks](../external-sources/apple/iphone-duo/2026-09-10/README.md). Canonical video identities were verified live. The source recordings total about 71.4 minutes. The following table describes that original v0.2.0 integration, not newly recorded evidence.

| Source / topic | Previous coverage | Current local guidance | Deliberately external |
| --- | --- | --- | --- |
| HIG and Design for Duo (111466) | Generic responsive layout and continuity | Stable hierarchy/functionality, useful inner-display space, selective displacement, safe-area centering, pose-aware controls | Full illustrations, demonstrations, narration |
| Prepare your app (111461) | Insets, resizing, system containers | Local geometry/size classes, idiom/orientation pitfalls, asymmetric bars, validation scenarios | Exact build-mode transitions and Device Hub steps until SDK verification |
| Raise the bar (111462) | Generic toolbar guidance | Container ownership, axis/representation, groups, action order, overflow priority, sheets, RTL | Complete code samples and every placement combination |
| Adaptive layouts (111463) | Generic fold/occlusion principle | Active/inactive division and occlusion regions, displacement versus scrolling, split/overlay choice and nesting limits | Full arrangement walkthrough and exact signatures |
| Displays and scenes (111464) | Generic second-display caution | Hinge for effects, dynamic multiwindow availability, camera accessory requirements and lifetime | Guitar/teleprompter implementation walkthroughs |
| Camera experience (111465) | No dedicated Duo camera guidance | Virtual versus physical tradeoffs, viewer-relative direction, isolation boundary, switching, mirroring, rotation, preview | Full format tables and implementation examples |

The short entry point loads only the relevant local module. Complete transcripts are not needed for normal decisions; they are optional context for detailed questions. Official video links remain necessary for on-screen code and visual behavior that captions cannot capture.

## Baseline source quality

- All six English and Chinese input caption tracks were present. Each reaches closing remarks; none has an internal gap above 15 seconds. This does not prove word-for-word audio accuracy.
- The English raw VTT files are byte-preserved. Reading copies omit only identical timestamp-and-text duplicates and join line wraps. Checksums and cue counts are in the archive manifest.
- The six live Apple video pages expose chapters and media downloads, but no populated transcript tab. The archive supplies searchable narration separately.
- HIG page history dates its introduction to September 9, 2026. At review time, the hub still described Xcode 27.1 beta and the preparation article as coming later that month.

## Compatibility and remaining work

Current names and availability are documentation-reviewed, with the limited iOS 27.0 typecheck evidence listed above. iOS 27.1 implementation support and device behavior are still unverified. Before using an API, verify the project's actual SDK, supported OS target, and runtime availability. No platform upgrade follows merely from applying this skill.

The acceptance scenarios in `tests/routing-cases.md` describe future app validation. The repository's automated checks cover source fidelity, link restrictions, module reachability, and packaging; the separate probe typechecks selected 27.0 declarations. iOS 27.1 compilation, supported Simulator transitions, and physical-device camera/fold behavior remain unverified.

Full caption material remains outside the MIT skill package. The source archive and revised skill can be reviewed independently; existing Release assets and installed copies are unchanged.
