# Liquid Glass

仅在用户需求或设计明确采用玻璃材质时读取。优先系统控件和原生 glass API；按目标平台与版本核对 availability。

- 按钮用原生玻璃 buttonStyle，形状在按钮样式边界调整；不要在 label 上堆 blur、stroke、shadow 仿造系统玻璃。
- 自定义玻璃表面先完成尺寸、padding 与文字样式，再应用 glassEffect；交互效果只给真正可操作的表面。
- 相邻玻璃元素需要合并/变形时用 GlassEffectContainer；容器 spacing 与内部排布 spacing 各有职责。
- morph 使用稳定身份和 namespace，并验证出现、消失、快速重复动作及 Reduce Motion。
- 系统工具栏可能已提供共享材质，避免重复叠加；隐藏背景的修饰器应按 SDK 声明应用于正确 ToolbarContent 层。
- 固定操作栏优先系统 safe-area 布局机制；具体 bar API 按 SDK 可用性选，不复制未验证签名。
- 滚动内容中的大量玻璃表面容易造成层级混乱或额外渲染成本；优先把玻璃用于控件/导航层，实际需求例外需测量。
- 不硬编码某种系统按钮“固定内部 padding”；实际大小随 controlSize、平台、文字等变化。
- 旧系统 fallback 是不同外观的兼容方案，不能称为相同光学效果。

检查暗/浅背景、文字可读性、点击区域、邻近合并与滚动表现；可见变化走 [实际验证](../validation/index.md)。
