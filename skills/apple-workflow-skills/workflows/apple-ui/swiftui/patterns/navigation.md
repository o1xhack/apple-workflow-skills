# Navigation and Presentation

- Organize shared dependencies, tabs, and per-tab navigation history near the app root. Avoid one global path that unintentionally links every tab's history.
- Use semantic types for tab selection and enumerable routes. When domain objects can disappear, persist stable IDs and resolve them on entry.
- Start with `NavigationStack` for linear flows and `NavigationSplitView` for collection, selection, and detail. Nested navigation or custom routing can serve more complex products; make path and presentation ownership clear, and check for unintended duplicate bars or broken back behavior.
- Register `navigationDestination` at a stable visible level, not inside a lazy child that may not exist. Avoid competing registrations for the same type in one stack; independent stacks may each register that type.
- Prefer item-based presentation for content-bearing sheets and booleans for simple toggles. An enum can clarify mutually exclusive presentations; retain another state model when it represents the flow well.
- Define save and cancel contracts. Dismiss after successful save; retain edits and present recovery when save fails. Parent callbacks are reasonable when the parent coordinates a transaction.
- With Xcode 27, item-based `alert` and `confirmationDialog` overloads can present one optional value without `Identifiable` or a second Boolean. Literal-title forms back-deploy to iOS 15, and resource-title forms to iOS 16. Retain another presentation model when it expresses the flow better, and check overload availability in the actual SDK.
- Attach `confirmationDialog` to the actual trigger and test popover anchoring on iPad and after layout changes.
- Validate deep-link URLs and parameters, prepare required account or data state, then route. Invalid or unauthorized targets must not end on a blank screen.
- Test back navigation, tab switches, dismissal, restoration, and wide-to-narrow changes rather than inspecting only the first screen.

Prefer initializer injection for feature-scoped dependencies and environment injection for genuinely app-wide services. Do not impose sample names such as `AppTab` or `RouterPath` on an existing project.
