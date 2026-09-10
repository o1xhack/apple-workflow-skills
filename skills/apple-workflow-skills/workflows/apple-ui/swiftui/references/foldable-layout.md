# iPhone Duo and Foldable Layout

Read for iPhone Duo design, fold adaptation, reserved regions, hinge interaction, or multiple displays. Apply [Adaptive Layout](adaptive-layout.md) first. Ordinary iPhone/iPad work does not need the Duo modules.

Evidence reviewed September 10, 2026: Apple's Duo HIG and six Tech Talks. The hub still listed Xcode 27.1 beta and the preparation article as coming later that month. Design guidance is reviewed; new API spellings below are discovery terms from the talks, not SDK-verified declarations. Recheck current availability, installed SDK signatures, and deployment targets before implementation. Do not upgrade a project or claim device validation from these notes.

## Default decisions

- Design one resizable experience with consistent hierarchy and available actions. Do not make features exclusive to an open, closed, or partially folded pose. Preserve editing, selection, navigation, and playback through transitions.
- Use size classes and local container geometry, not device-name checks, fixed screen dimensions, or interface orientation as a layout proxy. An open Duo remains an iPhone; do not equate regular width with iPad idiom.
- Use the wider interior for meaningful columns or supporting content. A sidebar is useful for dense navigation, not mandatory for every app.
- Prefer system navigation, presentations, and bars: they adapt to vertical controls and fold avoidance. Respect independent safe-area edges and layout margins; full-bleed backgrounds and inset interactive content can coexist.
- Move obstructed controls or focused content only as needed. Continuous articles, feeds, lists, and documents generally keep scrolling across the fold; do not displace everything.
- For layout, use available regions and system arrangements. Read hinge angle only for an intentional interaction or effect.

## Load only the relevant detail

| Task | Module |
| --- | --- |
| Centered UI, fold avoidance, custom panels, size changes | [Duo Layout](duo-layout.md) |
| Vertical toolbars, tabs, action ordering, overflow, sheets | [Duo Bars](duo-bars.md) |
| Hinge effects, multiwindow, second display, camera switching | [Duo Scenes and Camera](duo-scenes-camera.md) |
| Original HIG, full timed transcripts, video examples | [Duo External Reading](duo-sources.md) |

## Validation scope

For a Duo adaptation, exercise outer portrait/landscape, inner portrait/landscape, partial fold, both sides of Split View, and vertical resizing from pinned Picture in Picture where supported. Add keyboard, large text, RTL, and overflow checks when controls are affected. Follow the original task's scope; a small unrelated edit does not require this whole matrix.

Without an available SDK, supported Simulator, or physical device, report which checks could not run. A transcript, compilation, Simulator interaction, and physical fold/camera behavior are different evidence levels.
