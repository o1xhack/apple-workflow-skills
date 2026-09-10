# API and Code Quality

Treat target-SDK declarations and deprecation annotations as authoritative. These are review prompts, not an unconditional bulk-replacement list.

- Prefer `foregroundStyle`, shape-based clipping, modern `onChange`, and content-closure overlays when available. Do not label every older but supported API as a defect.
- Use `Tab`, `NavigationStack`, `NavigationSplitView`, `@Entry`, and newer web APIs only at their actual minimum OS versions. Preserve compatibility paths for older targets.
- Prefer localizable interpolation over string concatenation. Use `FormatStyle` for numeric, date, currency, and unit semantics. Do not accidentally group identifiers or years with thousands separators.
- Import Combine explicitly when using its types. Do not introduce a project-wide dependency or architecture migration merely to remove one warning.
- Use stable domain identity. An `enumerated()` offset is not the business identity of a movable list item.
- Follow the project's generated asset-symbol and string-catalog configuration. Do not assume generated accessors are enabled.
- Bind animation to the value that actually changes. Use explicit completion relationships instead of guessed delays, and respect Reduce Motion.
- Do not place secrets in source or examples, and do not store sensitive data in `AppStorage`. Comments should explain non-obvious constraints.
- Use the project's build targets, formatter, linter, and tests. Compilation does not prove UI or concurrency correctness.
