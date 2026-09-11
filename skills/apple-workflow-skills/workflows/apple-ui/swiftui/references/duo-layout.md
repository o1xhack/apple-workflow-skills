# Duo Layout

Use after [Duo Overview](foldable-layout.md) for layout adaptation. Source map: [External Reading](duo-sources.md), especially Design, Prepare, and Adaptive Layouts. New API names are video-described lookup terms pending SDK verification.

## Space and continuity

- The talks describe compact width on the outer display and regular width on the full inner display. Multitasking changes available space: read the environment instead of hard-coding those defaults. Prefer scene/window-local geometry to a global main screen.
- The inner display has different orientation behavior. Do not infer layout from supported-orientation settings or treat a full-screen requirement as a promise that bounds never change.
- A conventional inset layout centers within usable content space. Immersive, non-scrolling visuals can center on the whole display if foreground controls remain unobstructed. Insets and margins may differ on opposite edges.
- A supported tabletop arrangement may place visible media above and controls on the stable lower surface. Preserve the same actions and hierarchy in other poses.
- For games, keep play available across poses and adapt the viewport/aspect ratio to fill the available display instead of treating letterboxing as the default. Keep controls and critical content clear of reserved regions.

## Displacement and reserved regions

- Move a single control independently when possible; move related content together when separating it would break context. Avoid unnecessarily long jumps between regions.
- Keep scrolling content continuous. Transient menus, alerts, popovers, sheets, and important fixed controls are stronger candidates for displacement. Prefer built-in presentations before custom geometry.
- The talks distinguish division regions (fold) from occlusion regions (active camera). Query regions in the view's coordinates rather than using a fixed crease location or assuming the camera always occludes content.
- Active/inactive matters: the fold region is inactive and zero-width when flat; an inactive-region query can still inform structural choices such as an even column count. Normal queries return active regions.
- Lookup terms: `GeometryProxy.reservedRegion`, `UIView.reservedRegion`, `includeInactive`, division and occlusion kinds. Verify actual spelling, types, coordinate behavior, and OS availability in the target SDK before coding.

## Choose a container

- Keep navigation in `NavigationSplitView` or the existing navigation container when the panels represent navigation hierarchy.
- For two related content views without navigation behavior, evaluate the talk's `ArrangementView` / `UIArrangementViewController` instead of implementing pose detection by hand.
- A split arrangement fits main/detail content that should not obscure either pane. An overlay arrangement fits a foreground/background relationship where temporary overlap is acceptable.
- Arrangement choice also depends on size classes, aspect ratio, and division regions. If restricting split axes prevents a split, only one view may be shown; preserve a way to access the supporting content.
- Arrangements do not provide navigation infrastructure. Do not place a navigation container inside an arrangement or place an arrangement inside `List` / `ScrollView`; scrollable content can instead be a child pane.
- Lookup terms: `arrangementViewStyle`, split/overlay styles, `overlayArrangementZIndex`. These are optional implementation leads, not reasons to replace a suitable existing architecture.
