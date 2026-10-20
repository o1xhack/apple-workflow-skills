# Release 0.3.3 review

Reviewed October 20, 2026 against stable 0.3.2. Scope: guidance, conditional routing, provenance, and release documentation; no executable helper or Swift implementation changes.

## Content and routing review

No blocking defect was found in the final guidance. The ten added practice scenarios in `tests/routing-cases.md` were evaluated by tracing their local references and checking the specified decisions against the runtime text:

| Scenarios | Review result |
| --- | --- |
| Multiple Xcodes, missing Simulator runtime, source-only work | Effective command/tool selection is distinguished from the global default. SDK compilation and runtime interaction are separate; historical RC versions impose no minimum, and independent source work can continue. |
| Retained query with lost typing, unreliable tap/AX output | Editing outcomes are separately observable, recovery respects explicit cancellation, and input/observation faults are diagnosed before changing the app. |
| Scoped closeout, reuse after shared changes | Required final gates remain required; optional checks and unrelated defects do not silently expand scope. Changed consumers invalidate relevant prior evidence. |
| Hosted clipping, date/confirmation lifetime | Width and inset ownership are traced through the actual hierarchy. Draft/value, operation identity, and presentation source have separate lifetimes; system UI still needs interaction checks. |
| Expanded catalog/statistics/reading/form choices | Layout follows each task and content size, with stable state and relevant accessibility checks. Neither extra columns nor a specific geometry API is mandatory. |

The main entry loads shared toolchain guidance only for SDK-dependent work. Duo layout, bars, and validation link the relevant cases; ordinary tasks need not preload them. External reading remains in the existing catalog. Supporting declarations were reviewed separately from app-specific engineering policy.

Release preparation updates paired English/Chinese documents and replaces unreleased wording without rewriting historical evidence. The combined license, update-helper behavior, upstream baselines, and immutable caption archives remain unchanged.

The version-read regression test initially failed because it still expected 0.3.2 after the metadata changed to 0.3.3. Its expected release value was updated; no updater implementation or assertion strength changed.

## Validation scope

Release gates: repository structural/English/link/attribution validation; all 21 Python unit tests; skill frontmatter validation; read-only upstream-release check; whitespace validation; and ZIP integrity, file closure, and byte comparison. The release commit must also pass the repository's GitHub validation workflow before publication.

This is a manual content/routing review, not independent agent forward-testing, new SDK compilation, Simulator execution, or hardware certification. Existing app records are case inputs, not fresh package-wide app acceptance. Public-asset and installed-copy checks are performed after publication; their results belong to the delivery record.
