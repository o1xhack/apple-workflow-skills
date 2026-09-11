# iPhone Duo coverage review

Reviewed September 10, 2026 against the [official hub](https://developer.apple.com/iphone-duo/), [Duo HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo), and [six user-supplied English caption tracks](../external-sources/apple/iphone-duo/2026-09-10/README.md). Canonical video identities were verified live. The source recordings total about 71.4 minutes.

## Before and after

| Source / topic | Previous coverage | Current local guidance | Deliberately external |
| --- | --- | --- | --- |
| HIG and Design for Duo (111466) | Generic responsive layout and continuity | Stable hierarchy/functionality, useful inner-display space, selective displacement, safe-area centering, pose-aware controls | Full illustrations, demonstrations, narration |
| Prepare your app (111461) | Insets, resizing, system containers | Local geometry/size classes, idiom/orientation pitfalls, asymmetric bars, validation scenarios | Exact build-mode transitions and Device Hub steps until SDK verification |
| Raise the bar (111462) | Generic toolbar guidance | Container ownership, axis/representation, groups, action order, overflow priority, sheets, RTL | Complete code samples and every placement combination |
| Adaptive layouts (111463) | Generic fold/occlusion principle | Active/inactive division and occlusion regions, displacement versus scrolling, split/overlay choice and nesting limits | Full arrangement walkthrough and exact signatures |
| Displays and scenes (111464) | Generic second-display caution | Hinge for effects, dynamic multiwindow availability, camera accessory requirements and lifetime | Guitar/teleprompter implementation walkthroughs |
| Camera experience (111465) | No dedicated Duo camera guidance | Virtual versus physical tradeoffs, viewer-relative direction, isolation boundary, switching, mirroring, rotation, preview | Full format tables and implementation examples |

The short entry point loads only the relevant local module. Complete transcripts are not needed for normal decisions; they are optional context for detailed questions. Official video links remain necessary for on-screen code and visual behavior that captions cannot capture.

## Source quality

- All six English and Chinese input caption tracks were present. Each reaches closing remarks; none has an internal gap above 15 seconds. This does not prove word-for-word audio accuracy.
- The English raw VTT files are byte-preserved. Reading copies omit only identical timestamp-and-text duplicates and join line wraps. Checksums and cue counts are in the archive manifest.
- The six live Apple video pages expose chapters and media downloads, but no populated transcript tab. The archive supplies searchable narration separately.
- HIG page history dates its introduction to September 9, 2026. At review time, the hub still described Xcode 27.1 beta and the preparation article as coming later that month.

## Compatibility and remaining work

This is source-reviewed design and decision guidance, not SDK-verified implementation support. API names from videos are explicitly marked as lookup terms. Before using them, verify current Apple declarations, the project's installed SDK and OS target, and runtime availability. No platform upgrade follows merely from applying this skill.

The acceptance scenarios in `tests/routing-cases.md` describe future app validation. This change's automated checks cover source fidelity, link restrictions, module reachability, and packaging only. SDK compilation, supported Simulator transitions, and physical-device camera/fold behavior remain unverified.

Full caption material remains outside the MIT skill package. The source archive and revised skill can be reviewed independently; existing Release assets and installed copies are unchanged.
