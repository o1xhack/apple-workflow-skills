# Apple UI Workflow

Confirm the screen's purpose, data semantics, and primary interaction. Load only the files relevant to the current problem.

| Task | Read |
| --- | --- |
| Visual hierarchy, spacing, information density, copy | [Design Principles](design/principles.md) |
| New components, state, navigation, existing UI implementation | [SwiftUI](swiftui/index.md) |
| Split a large view or revise dependencies and ownership | [Refactoring](swiftui/references/refactoring.md) |
| Multiple sizes, window changes, wide layouts | [Adaptive Layout](swiftui/references/adaptive-layout.md) |
| iPhone Duo design, fold, occlusion, or second-display work | [iPhone Duo and Foldable Layout](swiftui/references/foldable-layout.md) |
| VoiceOver, text scaling, reachable actions | [Accessibility](swiftui/references/accessibility.md) |
| Glass buttons, materials, system bars, transitions | [Liquid Glass](liquid-glass/index.md) |
| Scrolling jank, excessive updates, image pressure | [UI Performance](performance/index.md) |
| Visible UI changes or a validation request | [UI Validation](validation/index.md) |
| Async loading, duplicate work, cancellation, actor crossings | [Shared Swift Concurrency](../../shared/swift-concurrency/index.md) and [UI Async State](swiftui/patterns/async-state.md) |

## Execute

1. Find the production component and neighboring implementation. Establish data source, state ownership, navigation, and target platforms.
2. Complete the request with the selected modules. Preserve the existing design system and architecture.
3. For visible changes, choose the shortest evidence path that answers the question. Exercise lifecycle, keyboard, permissions, and navigation inside the real app flow when they matter.
4. Report changes and evidence. For diagnosis-only requests, explain the cause without implementing an unrequested fix.

Use production components and bounded representative states for design exploration. A separate illustrative mockup is not evidence that the production UI works.
