# 状态所有权

先回答谁拥有值、谁修改值、谁需要观察，再选择包装器。

| 情形 | 方法 |
| --- | --- |
| 单个视图拥有值状态 | private @State |
| 子视图修改父级值 | @Binding |
| 支持 Observation 的目标，视图拥有模型 | @State 持有 @Observable 对象 |
| 注入可观察对象 | 显式属性，确实需要绑定时用 @Bindable |
| 真正共享的 App 服务 | Environment，避免把所有依赖都设成全局 |
| 旧目标或既有 ObservableObject 架构 | 所有者 StateObject，注入方 ObservedObject，按需 EnvironmentObject |

Observable 并不自动意味着线程安全，也不是所有模型都必须 MainActor；UI 状态按其隔离需求定义，业务并发读 [共享并发](../../../../shared/swift-concurrency/index.md)。

- 保持单一事实来源；不要用多个状态值重复保存相同派生结果。
- body 不发网络请求、不写库、不做重型初始化；事件调用小方法，复杂业务放服务。
- 优先自然投射的绑定。自定义 Binding 若用于必要转换可以保留，setter 必须可预测，避免隐式重型副作用。
- 派生集合只有在生命周期和失效策略明确时缓存，不能为了少计算就制造过期 UI。
- AppStorage 与 Observation 的交互需要确认真实变更能传播；不要以为添加 ObservationIgnored 就解决观察。
- 数据库计数快照不会自动变成实时数据；更新触发由实际数据层负责。
