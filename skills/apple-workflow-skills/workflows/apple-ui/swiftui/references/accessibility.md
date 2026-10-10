# Accessibility

- Use semantic text styles with Dynamic Type. Scale custom fonts correctly for the platform. Long text should wrap rather than shrink indefinitely to hide layout defects.
- On iOS 15+, read `dynamicTypeSize` and its `isAccessibilitySize` for text-size-dependent layouts; older targets may retain `sizeCategory`. Consider `@ScaledMetric` for custom sizing, or supported scaled semantic-font APIs, rather than fixing a cross-language point size.
- Give every `Button` and `Menu` an accessible action name. Preserve semantics when visual text is hidden, and keep decorative images from producing duplicate speech.
- Prefer `Button` when a custom gesture represents a button action. If a gesture is necessary, provide equivalent semantics plus keyboard and assistive-input paths.
- Do not express state with color alone. Check increased contrast, reduced transparency, dark mode, and Reduce Motion.
- Evaluate hit targets for the platform and input method, especially touch controls. Icon pixel size alone is not the target size.
- Keep focus order, VoiceOver grouping, form labels, errors, and recovery actions understandable.
- For changing or complex control labels, `accessibilityInputLabels` can provide stable Voice Control commands. An SF Symbol's default description does not necessarily explain the action; an explicit accessible name can preserve an icon-only visual design.
- Generated accessibility identifiers are not accessibility validation. Report success only after exercising the relevant assistive behavior.

See [UI Validation](../../validation/index.md) for visual and interaction evidence.
