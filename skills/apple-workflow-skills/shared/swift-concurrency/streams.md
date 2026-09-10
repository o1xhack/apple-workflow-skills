# 流与回调桥接

AsyncStream 是事件序列；CheckedContinuation 是单次异步完成，不能混淆终止要求。

- 有限流完成后 finish；生产者终止和消费者取消都清理监听。AsyncStream 的 finish 可重复调用，不能套用单次 continuation 的崩溃语义。
- CheckedContinuation 每条路径恰好 resume 一次；成功、失败、取消、同步回调和资源注册竞态必须统一仲裁。
- 高吞吐流明确 buffering 策略与丢事件语义；有界 buffer 不是自动让生产者减速的 backpressure。
- 根据实际 AsyncSequence 实现验证取消；不能假定所有 for await 循环都立即停止。循环后的业务仍要判断结束原因。
- onTermination 和取消回调可能在不同执行上下文运行，清理动作不能无同步访问共享可变对象。
- 桥接 legacy API 优先利用它的取消 handle。旧队列/锁确有低层职责时可以保留，不机械改成 actor。

测试同步回调、重复回调、先取消后注册、生产者先结束、消费变慢和取消时资源释放。
