# Localization

Load when adding or reviewing user-facing text, resources, or locale-dependent presentation. Follow the project's existing `.strings`, `.stringsdict`, or String Catalog workflow; a new feature does not require migrating the localization system.

## Text and resources

- SwiftUI localizes literals through initializers accepting `LocalizedStringKey`. A runtime `String` passed to `Text` displays verbatim; converting it to a key does not make Xcode extract an unknown runtime value. Existing explicitly cataloged dynamic keys can still be resolved intentionally.
- For new types carrying localizable interface text, consider `LocalizedStringResource` on supported targets. Existing `LocalizedStringKey` parameters remain valid. Preserve plain strings for user content, server text, and other values that should display as supplied.
- When catalog symbols are enabled, use generated resources according to the project's naming convention. Manually maintained keys can use `extractionState: "manual"`; automatically extracted literals are also valid. Do not assume symbol generation is configured.
- Preserve the owning resource bundle in packages and frameworks. `#bundle` is available in the reviewed Xcode 27 toolchain and back-deploys; otherwise use the project's explicit bundle lookup, such as a package's `Bundle.module` when its resources are configured. The app's main bundle is not a universal resource owner.
- Resource overloads differ by initializer. `Text` and resource-backed `Button` support iOS 16+, but the plain `TextField(_:text:)` and title/value `LabeledContent` resource forms require iOS 26. For earlier supported targets, use the label-closure initializer with `Text(resource)` instead. Confirm other overloads in the installed SDK.
- Prefer a single localized sentence with interpolation over concatenated fragments so translators can reorder placeholders. Explain ambiguous wording and placeholder meanings in translator comments. Add keys in supported languages through the existing translation process; do not present unreviewed translations as approved.

## Formatting and layout

- Use `FormatStyle` for dates, numbers, currencies, and units. Display lists with locale-aware `formatted()` rather than a fixed separator. Storage and API interchange may deliberately need fixed formats.
- If user-visible dates require `DateFormatter`, `setLocalizedDateFormatFromTemplate()` lets the locale choose ordering; use a year template such as `y`. Do not apply display-format advice to protocol dates or identifiers.
- Read locale, calendar, and time zone from the view environment when overrides matter. Their `.current` counterparts do not reflect per-view or preview overrides.
- Outside SwiftUI, consider `String(localized:)` for supported targets, including interpolated messages. Existing localization mechanisms remain valid when they serve the project.
- Inspect longer translations, plural forms, large text, and RTL layouts for the affected flow. Use semantic leading/trailing alignment where appropriate and distinguish text direction from hardware coordinates.
