# Coverage

**English** · [Chinese](coverage.zh-CN.md) · [Back to README](../README.md)

Applies to **v0.3.3**, including the October 6, 2026 Duo refresh. **v0.2.0** retains the September 10 review; v0.1.0 has general Duo guidance only. Coverage means guidance, not SDK or device validation.

The October 10 revision in v0.3.1 makes the guided approach explicit across the package: defaults help the agent begin, while the user's goal and engineering judgment guide alternatives. These modules do not exhaust the possible implementations or make every Apple recommendation mandatory. Actual API availability and demonstrated behavior remain relevant when choosing and validating an approach.

The selective upstream review in v0.3.2 adds localization, state/identity refinements, scoped API guidance, and deep-performance options. Seventeen representative Xcode 27.0 source probes compiled or failed as expected; this is not app or agent-behavior QA. See the [integration review](../upstream/reviews/swiftui-pro-2.0.0.md).

The October 20 practice update in v0.3.3 adds scoped validation priorities and stop conditions, automation diagnosis, and compact reusable evidence. Conditional [layout cases](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/duo-layout-cases.md) and [interaction cases](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/duo-interaction-cases.md) generalize local hybrid-app records; they do not establish new package-level SDK, Simulator, or hardware validation. Installing this version supplies guidance; actual app runtime acceptance remains separate. A shared [toolchain preflight](../skills/apple-workflow-skills/shared/toolchain-preflight.md) checks actual Xcode, SDK, and runtime/destination readiness for the task; historical versions are not current minimum requirements.

## Devices and platforms

- **iPhone & iPad:** SwiftUI guidance for existing projects, including models predating Duo. Apply APIs according to the project's supported OS versions.
- **iPhone Duo — Beta:** refreshed against current Apple HIG, preparation and camera articles, individual API declarations, and selected staff Q&A. Includes readiness auditing, layout, bars, scenes/camera, and motion guidance. iOS 27.1 compilation and device behavior still need validation.
- **Mac:** selected SwiftUI and desktop conventions are included.

These are guidance targets. A tested model-by-model or OS-version compatibility matrix is not yet available.

## Included

| Area | What is covered |
| --- | --- |
| [Design principles](../skills/apple-workflow-skills/workflows/apple-ui/design/principles.md) | Hierarchy, typography and native controls |
| [Localization](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/localization.md) | Resources, deferred text, bundles, translation context, and locale formatting |
| [SwiftUI components](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/index.md) | Forms, navigation, state and refactoring |
| [Adaptive layout](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/adaptive-layout.md) | Window sizes, safe areas and state continuity |
| [Accessibility](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/accessibility.md) | Dynamic Type, VoiceOver and contrast |
| [Liquid Glass](../skills/apple-workflow-skills/workflows/apple-ui/liquid-glass/index.md) | Native materials, grouping and transitions |
| [Performance & validation](../skills/apple-workflow-skills/workflows/apple-ui/validation/index.md) | UI diagnosis, Preview, Simulator and device checks |
| [Swift concurrency](../skills/apple-workflow-skills/shared/swift-concurrency/index.md) | Isolation, tasks, cancellation and streams |
| [iPhone Duo · Beta](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/foldable-layout.md) | Readiness audit, design, fold layout, bars, scenes/camera, motion; optional current source links and original transcripts |

## Duo references and limits

The local entry point loads only the audit/validation, layout, bars, or scenes/camera module needed for the task. The [reading catalog](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/duo-sources.md) links to current official articles and declarations, Group Labs and Q&A, and the six original English transcripts pinned to a commit. The [coverage review](iphone-duo-review.md) records inclusion choices and evidence gaps. Transcripts and exported Apple skills stay outside the installable ZIP.

On October 6, 2026, the hub listed Xcode 27.1 Release Candidate and live preparation documentation. Current API declarations and per-symbol iOS minimum versions were reviewed. At that review, the local toolchain was Xcode 27.0; no iOS 27.1 compilation, Duo Simulator interaction, or hardware validation was performed. Group Lab links and Q&A indexes are resource inventory, not a claim of exhaustive recording or thread review.

## Not included yet

API versions follow OS availability: selected guidance covers [navigation in iOS/iPadOS 16+](https://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types), [Observation integration in 17+](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app), and [Liquid Glass in 26+](https://developer.apple.com/documentation/swiftui/glasseffectcontainer). These milestones do not mean complete SDK coverage.

Dedicated UIKit/AppKit or framework-bridging workflows, SwiftData, Swift Testing, widgets, App Intents, and signing/App Store release. The listed areas cover selected tasks, not every API in each framework.

**Duo Beta** describes the maturity of our guidance. It will graduate after official SDK checks and representative app/device validation. Existing iPhone/iPad guidance remains available alongside it.

[Apple SwiftUI documentation](https://developer.apple.com/documentation/swiftui) · [Apple UIKit documentation](https://developer.apple.com/documentation/uikit) · [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
