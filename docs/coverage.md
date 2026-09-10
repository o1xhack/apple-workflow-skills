# Coverage

[English overview](../README.md#what-it-covers) · [Chinese overview](../README.zh-CN.md#当前覆盖什么)

Scope: published **v0.1.0** guidance. Reviewed on 2026-09-10.

This is a map of maintained guidance, not a count of supported SDK symbols or a claim of device certification. API names are representative review topics. Availability must be checked against the project's target SDK.

## Reading the map

- **Focused**: a dedicated module provides actionable guidance for the listed tasks.
- **Partial**: selected concerns are discussed; the broader Apple topic is not fully covered.
- **Not covered**: no dedicated guidance is shipped.
- **Beta**: our guidance is provisional and needs further validation. This describes this project's maturity, not Apple's product or SDK status.

The topic grouping follows Apple's SwiftUI and UIKit documentation. Design, shared concurrency, and hardware adaptation are additional cross-cutting sections.

## SwiftUI

| Apple topic | Coverage | Included guidance and representative APIs | Module |
| --- | --- | --- | --- |
| App structure | Partial | Navigation, modal presentation, toolbar and search patterns; `NavigationStack`, `NavigationSplitView`, `navigationDestination`, `confirmationDialog` | [Navigation](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/patterns/navigation.md), [Controls](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/patterns/controls.md) |
| Data and storage | Partial | State ownership, Observation, binding, environment and storage caveats; `@State`, `@Binding`, `@Observable`, `@Bindable`, `StateObject`, `AppStorage` | [State ownership](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/state.md) |
| Views | Partial | Forms, controls, semantic formatting, styles, identity and refactoring; `Form`, `Section`, `LabeledContent`, `Button`, `Menu`, `Label`, `foregroundStyle` | [Controls](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/patterns/controls.md), [API review](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/api.md), [Refactoring](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/refactoring.md) |
| View layout | Partial | Adaptive arrangements, grids, safe areas, list identity and continuity; `ViewThatFits`, `AnyLayout`, `NavigationSplitView` | [Adaptive layout](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/adaptive-layout.md), [Controls](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/patterns/controls.md) |
| Event handling | Partial | View-owned loading, input changes, cancellation and basic focus/gesture review; `.task`, `.task(id:)`, `onChange` | [Async state](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/patterns/async-state.md), [Controls](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/patterns/controls.md) |
| Accessibility | Focused | Labels, VoiceOver grouping, Dynamic Type, contrast, Reduce Motion and reachable actions | [Accessibility](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/accessibility.md) |
| Framework integration | Not covered | No dedicated `UIViewRepresentable`, `UIViewControllerRepresentable`, `UIHostingController`, AppKit or WatchKit bridging workflow | — |
| Tool support | Partial | Selecting native Preview, full-app interaction and profiling evidence | [Validation](../skills/apple-workflow-skills/workflows/apple-ui/validation/index.md), [Performance](../skills/apple-workflow-skills/workflows/apple-ui/performance/index.md) |

Other gaps include full scene/window/document management, custom Layout implementations, drawing, advanced animation, tables, drag and drop, clipboard, and persistence migrations. A passing mention of an API does not make its whole feature covered.

## UIKit and AppKit

| Framework area | Coverage | Boundary |
| --- | --- | --- |
| UIKit app structure and user interface | Not covered | No dedicated view-controller lifecycle, Auto Layout, table/collection view or diffable-data-source guidance |
| UIKit interactions, graphics and text | Not covered | No dedicated gesture recognizer, drawing, printing or TextKit workflow |
| AppKit | Not covered | macOS conventions appear in SwiftUI guidance; native AppKit implementation is not covered |

SwiftUI work on iOS does not imply UIKit API coverage.

## Cross-cutting capabilities

| Capability | Coverage | Included guidance | Module |
| --- | --- | --- | --- |
| Human Interface Guidelines / design | Partial | Hierarchy, semantic typography, spacing, native controls, copy and empty states | [Design principles](../skills/apple-workflow-skills/workflows/apple-ui/design/principles.md) |
| Liquid Glass | Focused | Native styles, surface grouping, morph identity, fallback and validation; `glassEffect`, `GlassEffectContainer` | [Liquid Glass](../skills/apple-workflow-skills/workflows/apple-ui/liquid-glass/index.md) |
| Swift concurrency | Focused | Isolation, reentrancy, Sendable, task groups, cancellation, streams and continuations | [Concurrency](../skills/apple-workflow-skills/shared/swift-concurrency/index.md) |
| iPhone Duo / foldable adaptation | Partial · **Beta** | Container-based adaptation, state continuity, occlusion and multi-display review principles | [Adaptive layout](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/adaptive-layout.md), [Foldable guidance](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/foldable-layout.md) |
| SwiftData, Swift Testing, widgets, App Intents and release/signing | Not covered | No dedicated workflow shipped | — |

**Duo Beta boundary:** v0.1.0 contains general foldable-layout guidance. Dedicated Duo API examples and device-specific interaction tests have not been validated. The Beta label does not imply those tests are already running or that Apple's hardware is itself beta.

Graduate this guidance from Beta after checking current official documentation and SDK declarations, validating a representative app through relevant display transitions and intermediate sizes, verifying editing/navigation/task continuity, and documenting Simulator or physical-device evidence and remaining limits.

## Platform scope

The guidance includes iOS/iPadOS interface patterns and selected macOS conventions. It is applied according to each project's platform and deployment target. This repository does not yet publish a tested OS/device compatibility matrix; watchOS, tvOS, and visionOS do not have dedicated workflows.

## Classification sources

- [Apple SwiftUI documentation](https://developer.apple.com/documentation/swiftui)
- [Apple UIKit documentation](https://developer.apple.com/documentation/uikit)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)

The category names organize the map; all coverage and maturity assessments are this project's own. Keep this map aligned with the published Release, and identify unreleased additions separately.
