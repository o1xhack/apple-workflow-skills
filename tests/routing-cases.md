# 行为验收场景

在隔离的演示项目使用安装后的顶层 skill 验证。以下是验收标准，不是已完成的真实 App QA。

| 请求 | 应读取 | 不应发生 | 证据 |
| --- | --- | --- | --- |
| 调整设置页视觉层级 | UI、design，必要时 controls | 全量并发审查、强制固定字号 | 实际渲染与长文本 |
| MVVM 页面拆分，保留行为 | UI、swiftui、refactoring | 强制改成 MV | diff 与原流程回归 |
| 窗口连续变窄 | UI、adaptive-layout | 推测设备型号、重置编辑内容 | 中间宽度与状态连续性 |
| 列表卡顿，仅诊断 | UI、performance | 未授权实现；代码线索冒充测量结论 | 症状、调用链、测量缺口 |
| 后台导入 actor 重入 | shared concurrency、isolation | 先加载整个 UI 工作流 | await 两侧的状态不变量 |
| 按钮文字改短 | UI design 的局部指导 | 启动整套设备测试 | 局部渲染或合理静态检查 |
| 为新设备使用铰链 API | foldable-layout | 将未核验名称当可用 SDK | 官方文档、工具链、设备证据 |
| 已有 iOS 16 项目改一个控件 | swiftui 对应模式 | 无关升级 Observation / deployment target | 原目标编译 |
| 使用 SwiftData 迁移 | 项目规则、官方资料 | 假称包内已有 SwiftData 专项 | 说明范围和实际方法 |

静态校验只证明引用闭合、来源完整、单入口可打包。CI 不运行这些 Swift 项目场景；人工验收时记录请求、实际读取模块、行为与缺口。
