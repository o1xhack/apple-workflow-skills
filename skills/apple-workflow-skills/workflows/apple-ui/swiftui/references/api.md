# API and Code Quality

Treat target-SDK declarations and deprecation annotations as authoritative. These are review prompts, not an unconditional bulk-replacement list.

- Prefer `foregroundStyle`, shape-based clipping, modern `onChange`, and content-closure overlays when available. Do not label every older but supported API as a defect.
- Separate build-tool support from runtime availability. A runtime guard cannot make an older SDK recognize a declaration. Check the project's compiler and SDK as well as each API's minimum OS, retaining the supported target and compatibility path.
- With Xcode 27, `@ContentBuilder` is the unified builder name and `@ViewBuilder` is an alias; existing uses need no migration. The builder name has no new minimum iOS. Macro availability, including `@Entry`, is also distinct from the runtime availability of the keys it generates.
- Use [Localization](localization.md) for localizable text and formatting, and [State Ownership](state.md) for identity and environment defaults.
- Import Combine explicitly when using its types. Do not introduce a project-wide dependency or architecture migration merely to remove one warning.
- Follow the project's generated asset-symbol configuration. Do not assume generated accessors are enabled.
- Bind animation to the value that actually changes. Use explicit completion relationships instead of guessed delays, and respect Reduce Motion.
- Do not place secrets in source or examples, and do not store sensitive data in `AppStorage`. Comments should explain non-obvious constraints.
- Use the project's build targets, formatter, linter, and tests. Compilation does not prove UI or concurrency correctness.

## Scoped modernization

SDK annotations such as `deprecated: 100000.0` mark soft deprecations without ordinary build warnings. A clean build does not establish that every API is current. In a modernization review, explain the replacement and its availability; during feature work, keep unrelated migration suggestions separate.

| Existing API | Candidate replacement and behavior to preserve |
| --- | --- |
| `accentColor(_:)` | `tint(_:)` where supported; app-wide accent assets remain useful |
| Visibility overloads of `toolbar` and `toolbarBackground` | `toolbarVisibility` and `toolbarBackgroundVisibility` on iOS 18+; keep style-valued `toolbarBackground` |
| `statusBarHidden(_:)` | `toolbarVisibility(_:for: .statusBar)` on iOS 27+; retain the older modifier below that |
| `colorScheme(_:)` | `.environment(\.colorScheme, ...)` for the same subtree scope; `preferredColorScheme` requests presentation-wide appearance |
| `autocapitalization`, `disableAutocorrection` | `textInputAutocapitalization`, `autocorrectionDisabled` when available |
| `coordinateSpace(name:)` | `.coordinateSpace(.named(...))` on iOS 17+; named-space frame lookups remain valid |
| `Color.cgColor` | `resolve(in:)` on iOS 17+ for environment-dependent components; account for dynamic colors |
| View-valued `overlay`, `background`, or `mask` arguments | Builder closures when supported; style overloads such as `.background(.indigo)` remain appropriate |
| `AnimatableModifier` | An animatable `ViewModifier`; consider `@Animatable` with supported tooling, or manual `animatableData` when its setter needs custom behavior |

Check the actual declaration for other platforms rather than applying an iOS version universally. An alternative spelling is useful only if it preserves the requested behavior.
