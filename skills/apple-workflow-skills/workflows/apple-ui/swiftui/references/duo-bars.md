# Duo Bars and Presentations

Use after [Duo Overview](foldable-layout.md) for navigation, toolbars, tabs, and sheets. Source map: [External Reading](duo-sources.md), especially HIG Vertical Controls and Raise the Bar. New API names are video-described lookup terms pending SDK verification.

## Let the container own adaptation

- Use bars belonging to `NavigationStack`, `NavigationSplitView`, `TabView`, or UIKit navigation/tab controllers. Standalone custom `UIToolbar` / `UINavigationBar` / `UITabBar` instances do not automatically get the same coordinated behavior.
- Most Duo poses use vertical bars; full inner portrait retains horizontal bars. In Split View, controls can move to the left outer edge. Test actual layout rather than assuming controls always sit on the right.
- Keep controls with the content they affect. The talk limits vertical participation to the detail column of a split view; other columns retain local horizontal controls, and an expanded inspector does not gain its own vertical bar.
- The bar follows hardware placement rather than mirroring with RTL text. Check RTL content around it.
- Outer sheets can have vertical controls; centered inner sheets use horizontal controls. Placement can change participation. A control-heavy sheet with only a close action may benefit from disabling the vertical bar.

## Representation and ordering

- Keep back/close first, followed by prominent completion actions, then grouped contextual actions. Preserve semantic grouping as the axis changes. Let the system supply back navigation where appropriate.
- Supply both title and symbol, even for an icon-only appearance: overflow and expanded presentations need the title. Text-only items generally remain horizontal.
- Do not force meaningful text, segmented controls, or a symbol/text-changing custom action into a narrow vertical representation. Custom vertical views must fit the bar width and remain legible with Reduce Transparency.
- Let item groups supply spacing; do not add fixed spacing to reproduce a device-specific arrangement. Keyboard accessory bars stay attached to the keyboard.

## Overflow is part of the design

- For navigation-focused screens, preserve tab destinations by compressing toolbar actions first. For task-focused screens, consider preserving frequently used toolbar actions instead.
- Give common actions and status-bearing items higher visibility priority. Review groups first, then items within groups; test the menu with constrained height, keyboard, and Picture in Picture.
- Merge an app's generic overflow actions into the system overflow menu. Reserve the ellipsis for overflow; domain-specific menus can remain separate with a distinct symbol.
- Evaluate disabling vertical bars for genuinely bottom-heavy, single-page interfaces; do not disable them globally to avoid adapting one custom item.

## API lookup map

The talk names `AxisBehavior`, `toolbarVerticalEdge`, `toolbarCompressionBehavior`, `ToolbarOverflowMenu`, `visibilityPriority`, and `toolbarVerticalBehavior`. UIKit counterparts include `additionalOverflowItems` and `preferredVerticalBarBehavior`. Prominent action placement includes `topBarPinnedTrailing` / `pinnedTrailingGroup`. Resolve declarations and availability from current documentation and the installed SDK; these notes do not supply compile-ready signatures.
