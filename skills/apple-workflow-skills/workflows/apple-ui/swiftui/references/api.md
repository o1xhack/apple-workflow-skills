# API 与代码质量

以目标 SDK 的声明和弃用标记为准，以下是优先检查点，不是无条件批量替换清单。

- 可用时采用 foregroundStyle、clipShape、现代 onChange 和带内容闭包的 overlay；不把仍合法的旧写法一律判错。
- Tab、NavigationStack、NavigationSplitView、@Entry 和新 WebView 等按各自最低系统版本使用；旧目标继续保留兼容路径。
- 文字拼接优先可本地化插值；数字、日期、货币通过 FormatStyle 表达语义。标识符和年份不要误用千分位。
- 与 Combine 类型交互显式导入 Combine。不要为消除一个 warning 引入全项目依赖或架构迁移。
- 使用稳定领域 ID；enumerated 的 offset 不是可移动列表元素的业务身份。
- 资产符号和字符串目录沿用项目的生成配置；不要假设生成访问器已启用。
- 动画绑定实际变化值；连续动画使用明确完成关系，避免猜延迟串联。遵守减少动态效果。
- 密钥不进入代码或示例；敏感数据不放 AppStorage。注释解释不明显的约束。
- 编译目标、formatter、lint 和必要测试沿用项目配置。编译成功不证明界面或并发正确。
