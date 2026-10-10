# Duo Bars and Presentations

Use after [Duo Overview](foldable-layout.md) for navigation, toolbars, tabs, and sheets. Source map: [External Reading](duo-sources.md), especially the current preparation guide and individual bar declarations. Names and minimum iOS versions below were documentation-reviewed; compile against the project's actual SDK before using them.

## Let the container own adaptation

- Prefer bars belonging to `NavigationStack`, `NavigationSplitView`, `TabView`, or UIKit navigation/tab controllers for their coordinated adaptation. Standalone custom `UIToolbar` / `UINavigationBar` / `UITabBar` instances can support a different product experience, but their adaptation needs to be handled by the app.
- Most Duo poses use vertical bars; full inner portrait retains horizontal bars. In Split View, controls can move to the left outer edge. Test actual layout rather than assuming controls always sit on the right.
- Keep controls with the content they affect. The talk limits vertical participation to the detail column of a split view; other columns retain local horizontal controls, and an expanded inspector does not gain its own vertical bar.
- The bar follows hardware placement rather than mirroring with RTL text. Check RTL content around it.
- Outer sheets use vertical bars by default. Inner sheets use horizontal bars at centered or leading placements and vertical bars at trailing placement. Request placement with `presentationPlacement(_:)` / `preferredPlacement`; evaluate disabling vertical bars only for the affected presentation.
- Custom bars receive no automatic relocation. If a product requires one, observe `toolbarVerticalEdge` / `verticalBarEdge` and query reserved regions to place it. Extend decorative backgrounds under bars with `backgroundExtensionEffect()` / `UIBackgroundExtensionView` without moving interactive content into an occlusion.

## Representation and ordering

- Keep back/close first, followed by prominent completion actions, then grouped contextual actions. Preserve semantic grouping as the axis changes. Let the system supply back navigation where appropriate.
- Supply both title and symbol, even for an icon-only appearance: overflow and expanded presentations need the title. Text-only items generally remain horizontal.
- Text-only and custom-view items do not participate vertically by default. `axisBehavior(_:)` / `axisBehavior` can control participation, but opting a custom view in does not redesign it. Adapt the representation to the available space; a horizontal segmented control may need a different presentation in a vertical bar.
- Let item groups supply spacing by default. Custom spacing can express a deliberate grouping; check it at changing sizes instead of relying on one device's geometry. Keyboard accessory bars stay attached to the keyboard.

## Overflow is part of the design

- For navigation-focused screens, preserve tab destinations by compressing toolbar actions first. For task-focused screens, consider preserving frequently used toolbar actions instead.
- Give common actions and status-bearing items higher visibility priority. Review groups first, then items within groups; test the menu with constrained height, keyboard, and Picture in Picture.
- Merge an app's generic overflow actions into the system overflow menu. Reserve the ellipsis for overflow; domain-specific menus can remain separate with a distinct symbol.
- For overflow confirmations, shared presentation state on a persistent view avoids depending on a disappearing menu item. State-driven presentation does not establish an exact SwiftUI overflow-button anchor; inspect the resulting dialog. A different presentation or UIKit bridge may better serve the requested interaction when supported by the actual APIs.
- Consider disabling vertical bars when another presentation better serves the interface, such as a bottom-heavy single-page flow. Choose the scope intentionally and check its effect on content space and action access.

## Documented API map

| Concern | SwiftUI | UIKit | Minimum iOS in reviewed documentation |
| --- | --- | --- | --- |
| Vertical-bar edge | `EnvironmentValues.toolbarVerticalEdge` | `UITraitCollection.verticalBarEdge` | 27.1 |
| Item axis participation | `ToolbarContent.axisBehavior(_:)`, `ToolbarItemAxisBehavior` | `UIBarButtonItem.axisBehavior` | 27.1 |
| Bar compression | `toolbarVerticalCompressionBehavior(_:)`, `ToolbarVerticalCompressionBehavior` | `UIVerticalBarCompressionBehavior` | 27.1 |
| Item priority | `visibilityPriority(_:)` | `UIBarButtonItem.visibilityPriority` | 27.0 |
| Dedicated overflow actions | `ToolbarOverflowMenu` | `UINavigationItem.additionalOverflowItems` | 27.0 / 16.0 |
| Prominent trailing action | `topBarPinnedTrailing` | `UINavigationItem.pinnedTrailingGroup` | 27.0 / 16.0 |
| Sheet placement | `presentationPlacement(_:)` | `UISheetPresentationController.preferredPlacement` | 27.0 |
| Vertical-bar policy | `toolbarVerticalBehavior(_:)` | override `UIViewController.preferredVerticalBarBehavior` | 27.1 |

Use `.prefersTabBar` to preserve destinations or `.prefersToolbarItems` to preserve task actions when setting SwiftUI compression behavior. UIKit and other platforms have their own declarations and availability; do not copy a SwiftUI spelling or iOS minimum into them. Build SDK changes can enable new default presentation without changing the app's deployment target.

On iOS 27+, a requested wide iPhone sidebar can combine `.tabViewStyle(.sidebarAdaptable)` with `.defaultTabBarPlacement(.sidebar)`. This is an intentional tab presentation choice, not an automatic consequence of regular width. Generic toolbar decisions live in [Controls and Content](../patterns/controls.md).
