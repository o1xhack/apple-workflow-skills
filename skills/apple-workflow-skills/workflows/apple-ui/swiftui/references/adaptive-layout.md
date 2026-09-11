# Adaptive Layout

Respond to available container space. A device model and full-screen dimensions usually do not describe the actual space inside a window or split view.

- Prefer `NavigationSplitView` for collection-detail structures. For local layouts, consider system containers, adaptive grids, `ViewThatFits`, and `AnyLayout` before reaching for geometry.
- Derive custom breakpoints from the content's minimum usable size rather than guessed device models. Preserve an explicit product breakpoint when it has a real requirement.
- Add useful structure on wide screens—sidebar, detail, inspector, or preview—while keeping text and forms at readable widths.
- `ViewThatFits` can select between distinct arrangements whose children may have different identity. Use `AnyLayout`, or lift state above the layout, when the same stateful subtree must rearrange.
- Let item content determine adaptive-grid minimum width. Use a fixed column count only when the design has a concrete reason.
- Respect each safe-area edge and keyboard inset. Do not mirror one edge's inset onto another. Let system bars participate in system layout.
- Preserve navigation, selection, input, playback, and unsaved content across layout changes.
- Validate narrow, intermediate, and wide windows, large text, and varied content amounts instead of testing only two device endpoints.

Read [iPhone Duo and Foldable Layout](foldable-layout.md) only when the task involves Duo design, folds, hinges, occlusion, or a second display.
