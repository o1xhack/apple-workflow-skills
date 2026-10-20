# Duo Layout Cases

Read only for clipping in mixed containers or deciding how a page should use expanded space, via [Duo Layout](duo-layout.md). These examples generalize local hybrid-app observations. Their measurements explain the diagnosis, not device breakpoints or guaranteed system behavior. See [External Reading](duo-sources.md) for framework declarations and [Duo Validation](duo-validation.md) for scoped checks.

## Window shrinks, scroll view stays wide

**Observed case:** After closing an expanded window, window/navigation widths were approximately 466 points while an internal scroll view remained about 961 points wide and shifted offscreen. Other hosted pages lost usable width through repeated inset handling. These are different failures; compare the actual hierarchy before choosing a fix.

Inspect from outside inward after a settled transition:

| Layer | Record and compare |
| --- | --- |
| Current scene/window | Bounds and active display; confirm the window actually resized |
| Navigation/presentation container | Child content bounds, bars, safe areas, and layout ownership |
| Hosting controller and hosted root | UIKit constraints, containment, proposed content width, additional insets, and view identity |
| Scroll container | Viewport bounds versus content size, offsets, and adjusted insets |
| Content | Proposed width, reading cap, padding, minimum/intrinsic widths, and any cached measurement |

Use a common coordinate space for position comparisons. Record which layer applies each safe-area edge, bar inset, and keyboard adjustment. Account for background extension separately from interactive content. If both host and child subtract the same inset, correct that ownership locally; do not disable safe areas throughout the app.

Find the first layer that stops tracking the current parent. In a UIKit-hosted SwiftUI page, check whether the host resizes before changing SwiftUI content. In a UIKit scroll view, distinguish `frameLayoutGuide` from `contentLayoutGuide`: the viewport and scrollable content answer different questions. In SwiftUI, inspect which ancestor supplies the proposed width and whether content measurement is feeding back into that proposal.

Correct the proven boundary rather than layering arbitrary frames over the symptom. A local parent proposal, suitable constraints, or a custom layout can be appropriate. `GeometryReader` and `containerRelativeFrame` remain useful when their actual container and proposal match the requirement; removing one in this case does not establish a general ban. A reading-width cap alone cannot repair an already oversized viewport.

Repeat wide -> intermediate -> narrow -> wide with the same live page, including an affected scrolled or editing state. Verify edge controls, scroll reachability, and state continuity, then regress shared consumers on ordinary devices. A correctly sized initial launch does not prove live resizing works.

## One app, four uses of expanded space

Consider a drink-tracking app with a catalog, statistics, reading pages, and entry forms. Choose by the user's task and minimum usable content size, not by a requirement that every expanded page gain columns:

| Page/task | Narrow window | Expanded window | Accessibility text sizes | Reason |
| --- | --- | --- | --- | --- |
| Catalog: compare and choose a drink | Fewer grid columns or rows that fit names and actions | More columns when each item stays usable | Reduce columns or use rows; allow names to wrap | Extra width helps scanning only while labels and targets remain usable |
| Statistics: compare summaries and charts | Stack summaries and charts | Place related summaries/charts side by side where labels fit | Stack affected groups and preserve chart labels/actions | Comparison benefits from proximity; density is secondary to comprehension |
| Settings, membership, release notes: read and decide | Full available readable area | Cap reading width, with margins informed by actual safe areas | Natural height, wrapping, and scrolling | Longer lines add little value; expanded space need not become a second column |
| Entry: edit values, date, and a long draft | Vertical form with reachable completion/cancel | Keep a coherent vertical form; add a preview only if useful | Stack labels and controls; keep caret and actions reachable above the keyboard | Editing order and continuity matter more than filling width |

Keep stable model, navigation, and editing ownership when changing arrangements. For each affected page, compare the same content in narrow, expanded, and relevant accessibility-size states, including long names or drafts. Confirm that any hidden supporting content still has a route. These are reasoned product choices from one case, not mandated layouts, column counts, or numeric reading caps.
