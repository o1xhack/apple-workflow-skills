# iPhone Duo and Foldable Layout

Read for iPhone Duo design, fold adaptation, reserved regions, hinge interaction, or multiple displays. Apply [Adaptive Layout](adaptive-layout.md) first. Ordinary iPhone/iPad work does not need the Duo modules.

Evidence refreshed October 6, 2026: Apple's HIG, preparation guides, API declarations, camera articles, and Apple staff Q&A. At that review, the hub listed Xcode 27.1 Release Candidate; this is a historical snapshot, not today's toolchain requirement. Distinguish the SDK used to build an app from its deployment target and the OS on which it runs. Dedicated Duo APIs generally require iOS 27.1, while several supporting APIs already exist in 27.0 or earlier; use the individual declarations in the detail modules. Documentation review does not establish compilation or device behavior. Preserve the project's supported targets and compatibility paths.

## Default decisions

- Start with one resizable experience that keeps core actions and state accessible across poses. Pose-specific features or richer layouts can serve deliberate product goals; provide a useful way to continue the task when that pose is unavailable. Preserve editing, selection, navigation, and playback through transitions where the product expects continuity.
- Use size classes and local container geometry, not device-name checks, fixed screen dimensions, or interface orientation as a layout proxy. An open Duo remains an iPhone; do not equate regular width with iPad idiom.
- Use the wider interior for meaningful columns or supporting content. A sidebar is useful for dense navigation, not mandatory for every app.
- Prefer system navigation, presentations, and bars: they adapt to vertical controls and fold avoidance. Respect independent safe-area edges and layout margins; full-bleed backgrounds and inset interactive content can coexist.
- Favor targeted movement of obstructed controls or focused content. Continuous articles, feeds, lists, and documents generally keep scrolling across the fold; broader rearrangement may make sense for a specific experience if it remains understandable and usable.
- Prefer available regions and system arrangements for ordinary layout. Hinge-driven effects or custom geometry can support a deliberate interaction; account for resizing and the absence of a hinge rather than treating angle as a general proxy for space.

## Load only the relevant detail

| Task | Module |
| --- | --- |
| Prepare an existing app, audit resizing patterns, plan or run validation | [Duo Audit and Validation](duo-validation.md) |
| Centered UI, fold avoidance, custom panels, size changes | [Duo Layout](duo-layout.md) |
| Vertical toolbars, tabs, action ordering, overflow, sheets | [Duo Bars](duo-bars.md) |
| Hinge effects, multiwindow, second display, camera switching | [Duo Scenes and Camera](duo-scenes-camera.md) |
| Original HIG, full timed transcripts, video examples | [Duo External Reading](duo-sources.md) |

## Validation scope

For a Duo adaptation, use the relevant scenarios in [Duo Audit and Validation](duo-validation.md). Follow the original task's scope; a small unrelated edit does not require the whole matrix.

Without an available SDK, supported Simulator, or physical device, report which checks could not run. A transcript, compilation, Simulator interaction, and physical fold/camera behavior are different evidence levels.
