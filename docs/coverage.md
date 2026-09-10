# Coverage

**English** · [Chinese](coverage.zh-CN.md) · [Back to README](../README.md)

Applies to **v0.1.0**. Coverage means development guidance for the topics below.

## Devices and platforms

- **iPhone & iPad:** SwiftUI guidance for existing projects, including models predating Duo. Apply APIs according to the project's supported OS versions.
- **iPhone Duo — Beta:** general adaptive and foldable-layout guidance is included. Dedicated Duo APIs and device transitions still need validation.
- **Mac:** selected SwiftUI and desktop conventions are included.

These are guidance targets. A tested model-by-model or OS-version compatibility matrix is not yet available.

## Included

| Area | What is covered |
| --- | --- |
| [Design principles](../skills/apple-workflow-skills/workflows/apple-ui/design/principles.md) | Hierarchy, typography and native controls |
| [SwiftUI components](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/index.md) | Forms, navigation, state and refactoring |
| [Adaptive layout](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/adaptive-layout.md) | Window sizes, safe areas and state continuity |
| [Accessibility](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/accessibility.md) | Dynamic Type, VoiceOver and contrast |
| [Liquid Glass](../skills/apple-workflow-skills/workflows/apple-ui/liquid-glass/index.md) | Native materials, grouping and transitions |
| [Performance & validation](../skills/apple-workflow-skills/workflows/apple-ui/validation/index.md) | UI diagnosis, Preview, Simulator and device checks |
| [Swift concurrency](../skills/apple-workflow-skills/shared/swift-concurrency/index.md) | Isolation, tasks, cancellation and streams |
| [iPhone Duo · Beta](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/foldable-layout.md) | General foldable adaptation; device-specific validation pending |

## Not included yet

API versions follow OS availability: selected guidance covers [navigation in iOS/iPadOS 16+](https://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types), [Observation integration in 17+](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app), and [Liquid Glass in 26+](https://developer.apple.com/documentation/swiftui/glasseffectcontainer). These milestones do not mean complete SDK coverage.

Dedicated UIKit/AppKit or framework-bridging workflows, SwiftData, Swift Testing, widgets, App Intents, and signing/App Store release. The listed areas cover selected tasks, not every API in each framework.

**Duo Beta** describes the maturity of our guidance. It will graduate after official SDK checks and representative app/device validation. Existing iPhone/iPad guidance remains available alongside it.

[Apple SwiftUI documentation](https://developer.apple.com/documentation/swiftui) · [Apple UIKit documentation](https://developer.apple.com/documentation/uikit) · [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
