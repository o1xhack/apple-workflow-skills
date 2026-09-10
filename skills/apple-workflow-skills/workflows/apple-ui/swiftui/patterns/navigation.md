# Navigation and Presentation

- Organize shared dependencies, tabs, and per-tab navigation history near the app root. Avoid one global path that unintentionally links every tab's history.
- Use semantic types for tab selection and enumerable routes. When domain objects can disappear, persist stable IDs and resolve them on entry.
- Use `NavigationStack` for linear flows and `NavigationSplitView` for collection, selection, and detail. Preserve project architecture and avoid nested duplicate system bars.
- Register `navigationDestination` at a stable visible level, not inside a lazy child that may not exist. Avoid ambiguous duplicate registrations for the same type.
- Use item-based presentation for content-bearing sheets and booleans for simple toggles. Model mutually exclusive presentations with one enum instead of multiple booleans.
- Define save and cancel contracts. Dismiss after successful save; retain edits and present recovery when save fails. Parent callbacks are reasonable when the parent coordinates a transaction.
- Attach `confirmationDialog` to the actual trigger and test popover anchoring on iPad and after layout changes.
- Validate deep-link URLs and parameters, prepare required account or data state, then route. Invalid or unauthorized targets must not end on a blank screen.
- Test back navigation, tab switches, dismissal, restoration, and wide-to-narrow changes rather than inspecting only the first screen.

Prefer initializer injection for feature-scoped dependencies and environment injection for genuinely app-wide services. Do not impose sample names such as `AppTab` or `RouterPath` on an existing project.
