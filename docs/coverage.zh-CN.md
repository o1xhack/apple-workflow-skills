# 覆盖范围

[English](coverage.md) · **简体中文** · [返回 README](../README.zh-CN.md)

对应 **v0.3.3**，包含 2026 年 10 月 6 日的 Duo 更新。**v0.2.0** 仍对应 9 月 10 日审查，v0.1.0 只有通用 Duo 指导。这里的覆盖指指导内容，不代表已通过 SDK 或设备验证。

v0.3.1 的 10 月 10 日修改进一步明确了整个包的引导风格：默认建议帮助 Agent 起步，用户目标和工程判断决定何时选择其他方案。这些模块不穷尽所有实现，也不要求每条 Apple 建议都必须照做。选择和验证方案时，仍需考虑实际 API 可用性和观察到的行为。

v0.3.2 选择性整合上游更新，增加本地化、状态与身份细节、按范围使用的新 API 指导及深度性能选项。17 个代表性 Xcode 27.0 源码探针已编译通过或按预期失败；这不代表 App 或 Agent 行为验收。详见[整合审查（英文）](../upstream/reviews/swiftui-pro-2.0.0.md)。

v0.3.3 的 10 月 20 日实战更新补充验证优先级与停止条件、自动化诊断和轻量证据复用；按需读取的[布局案例（英文）](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/duo-layout-cases.md)与[交互案例（英文）](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/duo-interaction-cases.md)提炼本地混合架构项目记录，不代表新增了本包的 SDK、模拟器或真机验收。安装后可使用这些指导；具体 App 的运行验收仍需分别完成。共享[工具链开工检查（英文）](../skills/apple-workflow-skills/shared/toolchain-preflight.md)按当前任务核对实际 Xcode、SDK 与运行时／目标设备；历史版本不作为当前最低要求。

## 设备与平台

- **iPhone 与 iPad：** 面向已有项目的 SwiftUI 指导，包括 Duo 之前的机型；具体 API 按项目支持的系统版本使用。
- **iPhone Duo — Beta：** 已重新对照当前 Apple HIG、准备与相机文档、逐项 API 声明和部分官方工程师答疑，补充适配审计、布局、工具栏、双屏／相机与运动坐标指导；iOS 27.1 编译和设备行为仍待验证。
- **Mac：** 已包含部分 SwiftUI 与桌面交互惯例。

这些是指导适用的开发目标，目前还没有逐机型、逐系统版本的完整验证矩阵。

## 已有内容

| 领域 | 覆盖内容 |
| --- | --- |
| [设计原则](../skills/apple-workflow-skills/workflows/apple-ui/design/principles.md) | 信息层级、排版与原生控件 |
| [本地化](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/localization.md) | 资源、延迟解析的文本、Bundle、翻译上下文与地区格式 |
| [SwiftUI 组件](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/index.md) | 表单、导航、状态与重构 |
| [自适应布局](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/adaptive-layout.md) | 窗口尺寸、安全区域与状态连续性 |
| [无障碍](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/accessibility.md) | 动态字号、VoiceOver 与对比度 |
| [Liquid Glass](../skills/apple-workflow-skills/workflows/apple-ui/liquid-glass/index.md) | 原生材质、分组与转场 |
| [性能与验证](../skills/apple-workflow-skills/workflows/apple-ui/validation/index.md) | 界面诊断、Preview、模拟器与真机检查 |
| [Swift 并发](../skills/apple-workflow-skills/shared/swift-concurrency/index.md) | 隔离、任务、取消与流 |
| [iPhone Duo · Beta](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/foldable-layout.md) | 适配审计、设计与折叠布局、工具栏、双屏／相机、运动坐标；最新来源及原有字幕按需读取 |

## Duo 资料与边界

本地入口仅按任务加载审计与验证、布局、工具栏或双屏／相机模块。[资料索引](../skills/apple-workflow-skills/workflows/apple-ui/swiftui/references/duo-sources.md)提供当前官方文档和声明、Group Lab 与答疑，以及六份固定提交版本的原有英文字幕；[逐项覆盖审查（英文）](iphone-duo-review.md)记录取舍与验证缺口。字幕和导出的 Apple skills 不进入安装 ZIP。

2026 年 10 月 6 日检查时，官网已列出 Xcode 27.1 Release Candidate，准备文档也已上线。已核对当前 API 声明及逐项最低 iOS 版本。当时本机工具链为 Xcode 27.0，尚未进行 iOS 27.1 编译、Duo 模拟器交互或真机验证。Group Lab 链接与答疑索引属于资料目录，不表示已经完整审阅所有回放和帖子。

## 暂未包含

API 版本按系统可用性表示：已有指导涉及 [iOS/iPadOS 16+ 导航](https://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types)、[17+ Observation 集成](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app)、[26+ Liquid Glass](https://developer.apple.com/documentation/swiftui/glasseffectcontainer)。这些版本节点不表示完整覆盖对应 SDK。

UIKit/AppKit 与框架桥接专项、SwiftData、Swift Testing、Widgets、App Intents、签名及 App Store 发布。已有领域覆盖具体任务，并非对应框架的全部 API。

**Duo Beta** 表示我们这套指导还在完善，完成官方 SDK 核对及代表性 App／设备验证后再转为正式支持。已有 iPhone/iPad 指导与它同时提供。

[Apple SwiftUI 文档](https://developer.apple.com/documentation/swiftui) · [Apple UIKit 文档](https://developer.apple.com/documentation/uikit) · [人机界面指南](https://developer.apple.com/design/human-interface-guidelines)
