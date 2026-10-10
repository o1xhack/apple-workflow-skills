# Controls and Content

- Prefer `Form` and `Section` for settings, and `LabeledContent` for labels paired with values. Keep readable labels for toggles and semantic labels for custom visuals.
- Bind numeric input to numeric values and formats. A keyboard type is an input hint, not parsing, validation, or error presentation.
- Distinguish empty query, loading, no results, and failure. Use stable IDs for large lists, and avoid sorting or filtering the full collection on every `body` evaluation.
- Use lazy containers when content scale warrants them, not as a substitute for measurement. Control pagination and image-decoding cost at the data boundary.
- Prefer system toolbars. Keep primary actions discoverable and organize secondary actions. When the keyboard appears, test focus, submission, and dismissal.
- Use `ViewThatFits` for local alternate arrangements. Use `AnyLayout` when the same stateful subtree should change layout; see [Adaptive Layout](../references/adaptive-layout.md).
- Give `Menu`, `Button`, and `Label` semantic text alongside symbols. Icon-only visual presentation still needs an accessible name.
- Drive animation and scroll-reveal behavior from one progress source rather than conflicting gesture, scroll, and offset state.
- Verify macOS settings, menus, windows, and keyboard behavior according to platform conventions instead of copying iOS sheet and touch assumptions.

Find component examples in the current project rather than retaining paths into an upstream author's private app.

## Toolbar choices

Prefer semantic placements such as `cancellationAction`, `confirmationAction`, or `primaryAction` when they express the action; top-bar leading/trailing positions remain useful when no role fits. Related controls can share a `ToolbarItemGroup`.

On iOS 27+, `ToolbarOverflowMenu` contributes generic overflow actions directly; a task-specific `Menu` can legitimately remain a submenu. Use `visibilityPriority` to express which items matter when space is tight. Consider `topBarPinnedTrailing` for one indispensable action, `contentMarginsRemoved()` for intentionally fitted custom imagery, and `toolbarMinimizationBehavior(_:for:)` for content-led scrolling. Preserve standard margins and visible bars when they better serve the screen.

With the Xcode 27 SDK, `ForEach` can produce toolbar items back to iOS 16 without a new runtime guard. New iOS 27 modifiers still need their own availability checks. Current documentation lists toolbar-content `hidden(_:)` for iOS 26.4+, but it is unavailable for iOS in the reviewed 27.0 SDK: confirm that the installed SDK declares it before recommending it. Conditional toolbar construction remains an option.

For vertical adaptation, camera clearance, and overflow confirmations on Duo, load [Duo Bars](../references/duo-bars.md).

## Reordering and swipe actions

On supported iOS 27+ targets, consider `reorderable()` on the `ForEach` together with `reorderContainer(for:)` on the enclosing container. The callback supplies a `ReorderDifference`; the app applies the move to its source of truth. Preserve stable IDs and check multi-item order, same-collection moves, persistence, and cross-section destination IDs as relevant. SwiftUI does not automatically update the model.

Reordering and system drag-and-drop serve different purposes. Add `dragContainer(for:)` and transferable data only when the interaction also needs external transfer. Earlier targets can keep `List.onMove` or an appropriate custom implementation.

In iOS 27 scroll-based stacks or grids, row `swipeActions` also need `swipeActionsContainer()` on the surrounding scroll view. Check the platform declaration rather than assuming these APIs exist on tvOS, and retain accessible action routes when swipe or drag is unavailable.
