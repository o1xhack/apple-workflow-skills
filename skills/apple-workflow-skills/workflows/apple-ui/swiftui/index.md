# SwiftUI Implementation and Review

Inspect existing components, dependency injection, deployment targets, and routing conventions before changing code. Do not introduce a new architecture or third-party framework automatically.

## Load as needed

- [API and Code Quality](references/api.md): modern APIs, availability, localization, and identity.
- [State Ownership](references/state.md): value state, Observation, bindings, and side effects.
- [Navigation and Presentation](patterns/navigation.md): tabs, stacks, split views, sheets, and deep links.
- [Controls and Content](patterns/controls.md): forms, lists, search, toolbars, and input.
- [UI Async State](patterns/async-state.md): loading, cancellation, and stale results.
- [Behavior-Preserving Refactoring](references/refactoring.md): views, dependencies, and ownership.
- [Adaptive Layout](references/adaptive-layout.md): changing windows and state continuity.
- [Accessibility](references/accessibility.md): semantics, text scaling, and interaction.

Define state and ownership before arranging components, navigation, and presentation. Keep `body` declarative; place business operations in testable methods, models, or services.

When supporting multiple OS versions, choose APIs available to the current target. Do not migrate an entire project merely to use a preferred property wrapper.

In review, report concrete issues with location, trigger, and the smallest correction. Do not elevate formatting preferences into defects.

For visible changes, use [UI Validation](../validation/index.md). For static-only review, state that runtime behavior remains unproven.
