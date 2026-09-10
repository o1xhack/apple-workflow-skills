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
