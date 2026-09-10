# 覆盖范围

[English](coverage.md) · **简体中文** · [返回 README](../README.zh-CN.md)

对应 **v0.1.0**。这里的覆盖，指下列开发任务已有可用的指导内容。

## 设备与平台

- **iPhone 与 iPad：** 面向已有项目的 SwiftUI 指导，包括 Duo 之前的机型；具体 API 按项目支持的系统版本使用。
- **iPhone Duo — Beta：** 已包含通用自适应与折叠布局指导，Duo 专用 API 和设备切换行为仍待验证。
- **Mac：** 已包含部分 SwiftUI 与桌面交互惯例。

这些是指导适用的开发目标，目前还没有逐机型、逐系统版本的完整验证矩阵。

## 已有内容

| 领域 | 覆盖内容 |
| --- | --- |
| [设计原则](../skills/apple-workflow-skills/workflows/apple-ui/design/principles.md) | 信息层级、排版与原生控件 |
| [SwiftUI 组件](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/index.md) | 表单、导航、状态与重构 |
| [自适应布局](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/adaptive-layout.md) | 窗口尺寸、安全区域与状态连续性 |
| [无障碍](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/accessibility.md) | 动态字号、VoiceOver 与对比度 |
| [Liquid Glass](../skills/apple-workflow-skills/workflows/apple-ui/liquid-glass/index.md) | 原生材质、分组与转场 |
| [性能与验证](../skills/apple-workflow-skills/workflows/apple-ui/validation/index.md) | 界面诊断、Preview、模拟器与真机检查 |
| [Swift 并发](../skills/apple-workflow-skills/shared/swift-concurrency/index.md) | 隔离、任务、取消与流 |
| [iPhone Duo · Beta](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/foldable-layout.md) | 通用折叠适配；专用 API 与设备验证待完成 |

## 暂未包含

API 版本按系统可用性表示：已有指导涉及 [iOS/iPadOS 16+ 导航](https://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types)、[17+ Observation 集成](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app)、[26+ Liquid Glass](https://developer.apple.com/documentation/swiftui/glasseffectcontainer)。这些版本节点不表示完整覆盖对应 SDK。

UIKit/AppKit 与框架桥接专项、SwiftData、Swift Testing、Widgets、App Intents、签名及 App Store 发布。已有领域覆盖具体任务，并非对应框架的全部 API。

**Duo Beta** 表示我们这套指导还在完善，完成官方 SDK 核对及代表性 App／设备验证后再转为正式支持。已有 iPhone/iPad 指导与它同时提供。

[Apple SwiftUI 文档](https://developer.apple.com/documentation/swiftui) · [Apple UIKit 文档](https://developer.apple.com/documentation/uikit) · [人机界面指南](https://developer.apple.com/design/human-interface-guidelines)
