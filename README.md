# Apple Workflow Skills

一套中文、单入口、按需加载的 Apple 开发工作流。先完善 UI 的设计、实现、重构、性能诊断与实际验证；并发作为跨工作流共享能力。

## 安装

支持 Agent Skills 的工具可以安装仓库中的唯一顶层 skill：

```sh
npx skills add o1xhack/apple-workflow-skills --skill apple-workflow-skills
```

也可以把 skills/apple-workflow-skills 整个文件夹复制到工具的 skills 目录。必须连同内部 sources 一起复制，以保留许可证。跨设备使用时，以自己的同步目录为唯一维护来源，再由工具目录引用；不要维护多份独立副本。

使用示例：

```text
使用 $apple-workflow-skills 检查这个设置页的视觉层级和窄窗口适配。
使用 $apple-workflow-skills 重构这个 View，保留现有 MVVM 和行为。
使用 $apple-workflow-skills 诊断后台导入的 actor 重入问题。
```

## 能力与层级

- Apple 总入口：读取项目、平台、工具链、任务范围，选择需要的模块。
- Apple UI Workflow：设计原则、SwiftUI 模式与重构、自适应布局、Liquid Glass、性能、Preview / 模拟器 / 真机验证。
- Shared Concurrency：隔离、任务生命周期、取消、有界并行、流与回调桥接；不要求任务涉及 UI。

内部 index.md 是按路径读取的模块，不需要单独安装，也不会自动启动子代理。总入口不会一次读取所有文件。

## 当前边界

首版不含独立 SwiftData、Swift Testing、签名发布、Widgets 或 App Intents 工作流。遇到这些任务沿用项目工具与官方文档，不冒充已内置相应专项。SwiftUI 规则按实际平台与最低系统版本应用；本包不是 UIKit / AppKit 全面审查工具。

折叠设备通用布局规则已经整合；未经官方 SDK 验证的专用 API 不提供可执行示例。Swift 示例是规则演示，尚不代表所有 Apple 平台与 SDK 均已编译验证。

## 维护

[维护流程](docs/maintenance.md) · [整合决策](docs/decisions.md) · [来源索引](sources/README.md) · [变更记录](CHANGELOG.md)

GitHub Actions 每日进入轻量日期判断，仅每两天执行上游正式 Release 检查，支持手动运行。无新版本时不创建 Issue；有新版本时按映射生成可复核的更新事项，人工决定是否采用。自动检查不运行 AI、不自动生成或合并代码。

## 本地验证

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/check_upstream_releases.py
python3 scripts/package.py --output /tmp/apple-workflow-skills.zip
```

Release 检查默认只输出报告；--publish 才使用 GITHUB_TOKEN 和 GITHUB_REPOSITORY 创建审查 Issue。网络或认证错误返回失败，不能当作无更新。

## 许可

本项目原创部分采用 MIT。整合的第三方内容保留各自版权和 MIT 许可，集中存于安装包 sources/licenses；来源链接只在 sources 维护。
