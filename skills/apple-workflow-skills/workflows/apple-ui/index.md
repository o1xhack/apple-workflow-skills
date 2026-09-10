# Apple UI Workflow

先确认页面的目标、数据语义与主要交互。按当前问题选下面的文件；小改动只读取受影响部分。

| 任务 | 读取 |
| --- | --- |
| 视觉层级、间距、信息密度、文案 | [设计原则](design/principles.md) |
| 新组件、状态、导航、已有 UI 实现 | [SwiftUI](swiftui/index.md) |
| 拆分大 View、调整依赖与所有权 | [重构](swiftui/references/refactoring.md) |
| 多尺寸、窗口变化、宽屏布局 | [自适应布局](swiftui/references/adaptive-layout.md) |
| 明确的折叠或第二屏幕需求 | [折叠专项](swiftui/references/foldable-layout.md) |
| VoiceOver、字号、动作可达性 | [无障碍](swiftui/references/accessibility.md) |
| 玻璃按钮、材质、系统栏、转场 | [Liquid Glass](liquid-glass/index.md) |
| 滚动卡顿、过度更新、图片压力 | [性能诊断](performance/index.md) |
| 可见 UI 变化或验证请求 | [实际验证](validation/index.md) |
| 异步加载、重复任务、取消、跨 actor | [共享并发](../../shared/swift-concurrency/index.md)，以及 [UI 异步状态](swiftui/patterns/async-state.md) |

## 执行

1. 找到生产组件与邻近实现，确认数据来源、状态所有权、导航与目标平台。
2. 用相关模块完成请求。保持已有设计系统与架构；只解决当前范围内的问题。
3. 可见变化选择最短有效渲染路径；生命周期、键盘、权限、导航需在真实 App 流程操作。
4. 报告改动与证据。仅诊断时给原因和证据，不顺带实施修复。

设计探索用生产组件和有界示例状态；不能另画一套示意 UI 后称生产界面通过。
