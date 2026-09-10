# 导航与呈现

- 在 App 根部组织共享依赖、Tab 与每个 Tab 的导航历史；不用一个全局 path 意外串起所有标签页。
- Tab 选择和可枚举路由使用有语义的类型；领域对象可能失效时优先保存稳定 ID，进入详情时解析。
- 单列流用 NavigationStack，集合/选择/详情用 NavigationSplitView。沿用项目架构，避免嵌套重复的系统栏。
- navigationDestination 注册在稳定且可见的层级，不放在可能尚未创建的 lazy 子项内；避免同类型重复注册造成歧义。
- 携带内容的弹窗用 item 状态；单纯开关可用 Bool。互斥弹窗用一个可枚举状态，避免多个 Bool 同时为真。
- Sheet 的保存/取消合同明确：保存成功后 dismiss；失败时保留编辑值并显示恢复方式。回调在父级需要协调事务时是合理的。
- confirmationDialog 关联实际触发控件，检查 iPad popover 和布局后的锚点。
- 深链验证 URL 与参数，先完成所需账号/数据准备，再转入路由；无效或无权限目标不能落到空白页面。
- 检查返回、切换 Tab、关闭弹窗、状态恢复与宽窄转换；不能仅看首屏截图。

依赖属于某 feature 时优先 init 注入；跨 App 服务才放 environment。不要把上游示例中的 AppTab 或 RouterPath 名称强制推广到现有工程。
