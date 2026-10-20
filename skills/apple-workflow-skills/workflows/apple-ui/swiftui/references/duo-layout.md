# Duo Layout

Use after [Duo Overview](foldable-layout.md) for layout adaptation. Source map: [External Reading](duo-sources.md), especially the preparation documentation, reserved-region declarations, and arrangement guidance. APIs in this module require iOS 27.1 unless stated otherwise; check the actual SDK before implementation.

## Space and continuity

For clipping across UIKit/SwiftUI boundaries or page-specific wide-screen choices, load [Layout Cases](duo-layout-cases.md). For text, focus, keyboard, caret, or continued-input failures, load [Interaction Cases](duo-interaction-cases.md).

- The talks describe compact width on the outer display and regular width on the full inner display. Multitasking changes available space: read the environment instead of hard-coding those defaults. Prefer scene/window-local geometry to a global main screen.
- The inner display has different orientation behavior. Do not infer layout from supported-orientation settings or treat a full-screen requirement as a promise that bounds never change.
- A conventional inset layout centers within usable content space. Immersive, non-scrolling visuals can center on the whole display if foreground controls remain unobstructed. Insets and margins may differ on opposite edges.
- A supported tabletop arrangement may place visible media above and controls on the stable lower surface. Preserve the same actions and hierarchy in other poses.
- Opening and closing is a resize/trait change, not an app teardown or a new scene. Keep navigation, edits, scroll identity, and playback alive; do not restart network or capture work solely because size classes change. Scene restoration remains relevant for an actual disconnect/reconnect.
- For games, keep play available across poses and adapt the viewport/aspect ratio to fill the available display instead of treating letterboxing as the default. Keep controls and critical content clear of reserved regions.

## Displacement and reserved regions

- Move a single control independently when possible; move related content together when separating it would break context. Avoid unnecessarily long jumps between regions.
- Keep scrolling content continuous. Transient menus, alerts, popovers, sheets, and important fixed controls are stronger candidates for displacement. Prefer built-in presentations before custom geometry.
- The talks distinguish division regions (fold) from occlusion regions (active camera). Query regions in the view's coordinates rather than using a fixed crease location or assuming the camera always occludes content.
- Safe-area insets alone do not describe the fold in a custom sheet or control. Query intersecting reserved regions, including their frames, margins, and `isActive`, before placing custom content. The outer camera always occludes; the inner camera occludes while active.
- The documented queries are `GeometryProxy.reservedRegions(kind:options:layoutDirectionBehavior:)` and `UIView.reservedRegions(kind:options:)`, returning arrays. Use `.division` for the fold and `.occlusion` for hardware obstructions. Use `.includeInactive` when structural choices need inactive regions, and check `isActive` when deciding whether to displace content; do not assume that every returned frame is an active obstacle.
- SwiftUI defaults to mirrored reserved-region geometry for layouts that themselves mirror in RTL. Use `layoutDirectionBehavior: .fixed` only when manually managing coordinates; avoid applying a second mirror. The hardware itself does not move with text direction.

## Choose a container

- Keep navigation in `NavigationSplitView` or the existing navigation container when the panels represent navigation hierarchy.
- For two related content views without navigation behavior, evaluate `ArrangementView` / `UIArrangementViewController` instead of implementing pose detection by hand. Both are general iOS 27.1 containers, not a device-detection mechanism.
- A split arrangement fits content that should not obscure either pane. An overlay arrangement puts primary controls over secondary media when flat; an active division can move the primary view to the trailing/bottom region and secondary content to leading/top.
- Arrangement choice also depends on size classes, aspect ratio, and division regions. If restricting split axes prevents a split, only one view may be shown; preserve a way to access the supporting content.
- Arrangements provide layout rather than navigation. A surrounding `NavigationStack` is a straightforward starting point, with scrolling inside the panes. Apple's HIG describes navigation split and tab containers around arrangements, while its preparation article advises avoiding arrangements inside a navigation split view or scrolling container because content may become inaccessible. Treat this as composition guidance with context, not a universal nesting prohibition.
- When a product needs sidebar navigation plus two related regions in its detail, evaluate an arrangement in that detail rather than rejecting the structure by its container names. More complex nesting can be appropriate; check the available size, navigation ownership, clipping, and access to secondary content as the layout changes. Use another composition if the combination does not behave well.
- Choose `.arrangementViewStyle(.split)` or `.overlay` for the actual content relationship; constrain supported axes with `.axes(...)` only when the product needs it. If a control belongs to one pane, attach its safe-area bar to that pane rather than to the whole arrangement. Preserve a way to access secondary content when an axis restriction hides it.
