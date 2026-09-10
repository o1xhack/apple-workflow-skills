# 整合决策

## 2026-09-10 首版

- 总入口属于 Apple 开发。并发放 shared，不隶属于 UI。
- 只暴露一个 SKILL.md；内部 index.md 和参考文件由入口显式选择。
- SwiftUI Pro、Patterns、Refactor 的状态与导航重复内容统一在 SwiftUI 模块。按任务加载，不全量扫描。
- 设计采用一致性、语义层级、原生组件原则；不继承固定字号、间距白名单、圆角或所有场景禁用自定义布局的规则。
- MV / MVVM 服从项目；按职责和状态边界拆分视图，不按固定行数或“一文件只能有一个类型”强制重构。
- Concurrency 修正示例解释：await 是可能的挂起点，并非每次必然挂起；actor 内无 await 的连续片段不会被另一 actor 调用插入。缓存局部结果不等于消除重复下载；任务共享需单独定义取消与失效策略。
- 普通 task group 中子任务抛错不等于立刻取消所有兄弟；错误经组遍历或 next 传播到作用域外时才触发相应退出/取消，具体看所用 API。
- AsyncStream finish 可幂等；不能与 CheckedContinuation 的恰好一次 resume 要求混为一谈。
- Liquid Glass 保留系统材质与分组方法；去掉固定内部 padding 断言，滚动内容使用玻璃视为设计/性能风险而非编译禁令。
- 折叠专项保留场景与验证路径；ArrangementView、onHingeChange、指定 Duo / Xcode 版本等未独立验证，不复制为生产 API 范例。
- 上游链接只放 sources；随 skill 打包完整版权声明，不因重写内容就删除归属。
- 当前五个来源只有两个有正式 Release。其余也只监测将来的 Release，不回退 commit 检查。
