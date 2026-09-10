# SwiftUI 实现与审查

先查看项目已有组件、依赖注入、最低系统版本和路由约定；不自动引入新架构或第三方框架。

## 按需参考

- [API 与代码质量](references/api.md)：现代替代 API、版本与本地化。
- [状态所有权](references/state.md)：值状态、Observation、绑定与副作用。
- [导航与呈现](patterns/navigation.md)：Tab、Stack、SplitView、Sheet 和深链。
- [控件与内容](patterns/controls.md)：表单、列表、搜索、工具栏和输入。
- [UI 异步状态](patterns/async-state.md)：加载、取消和过期结果。
- [重构](references/refactoring.md)：保持行为的视图与依赖整理。
- [自适应布局](references/adaptive-layout.md)：窗口变化与状态连续性。
- [无障碍](references/accessibility.md)：语义、字号和交互。

## 实现路径

先定义状态及其拥有者，再组织组件、导航与呈现。UI body 描述界面，业务操作放在可验证的方法、模型或服务。
支持新旧系统时选当前目标可用的 API，不为使用某个 property wrapper 顺带迁移工程。
对审查只报告真实问题，说明位置、触发条件和最小改法；不要把格式偏好提升为缺陷。
可见修改完成后走 [实际验证](../validation/index.md)。仅静态审查时明确无法证明运行表现。
