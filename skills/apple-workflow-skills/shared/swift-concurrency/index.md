# Swift 并发

适用于网络、文件、数据库服务、后台任务和 UI，不要求加载 UI 工作流。

先核对每个 target/package 的 Swift 版本、语言模式、严格并发、默认 actor isolation 与相关 upcoming feature 设置。async 不等于后台线程，await 不保证发生切换。

- [隔离与诊断](isolation.md)：actor 重入、Sendable、全局状态和编译器边界。
- [任务与取消](tasks.md)：结构化并发、有界并行、生命周期。
- [流与桥接](streams.md)：AsyncStream、continuation、回调资源清理。

先找到跨隔离边界的数据与可变状态，再选择最小修复。不要为了消除诊断把整个业务层标为 MainActor，也不把 @unchecked Sendable 当快捷修复。
审查指出具体状态不变量、触发条件和证据。测试采用受控事件与顺序，不靠随机 sleep 假装覆盖竞态。
