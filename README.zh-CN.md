<div align="center">

# Apple Workflow Skills

**一键安装、按需加载的 Apple 开发工作流 Skill。**

[![Swift](https://img.shields.io/badge/Swift-6_concurrency-f05138?style=for-the-badge&logo=swift&logoColor=white)](docs/coverage.zh-CN.md)
[![Release](https://img.shields.io/github/v/release/o1xhack/apple-workflow-skills?style=for-the-badge&label=release&color=7c3aed)](https://github.com/o1xhack/apple-workflow-skills/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/o1xhack/apple-workflow-skills/total?style=for-the-badge&label=downloads&color=7c3aed)](https://github.com/o1xhack/apple-workflow-skills/releases)
[![Stars](https://img.shields.io/github/stars/o1xhack/apple-workflow-skills?style=for-the-badge&label=stars&color=7c3aed)](https://github.com/o1xhack/apple-workflow-skills/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/o1xhack/apple-workflow-skills/validate.yml?branch=main&style=for-the-badge&label=CI)](https://github.com/o1xhack/apple-workflow-skills/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/o1xhack/apple-workflow-skills?style=for-the-badge&label=license&color=7c3aed)](LICENSE)
[![Sponsor](https://img.shields.io/badge/GitHub-Sponsors-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/o1xhack)

[English](README.md) · **简体中文**

[让 AI Agent 安装](#安装) · [下载最新 Release](https://github.com/o1xhack/apple-workflow-skills/releases/latest/download/apple-workflow-skills.zip) · [全部版本](https://github.com/o1xhack/apple-workflow-skills/releases)

</div>

Apple Workflow Skills 为 AI Agent 提供一套原生 Apple 界面的设计、实现、审查与验证方法。安装一次，直接描述你想完成的事情。

## 安装

选择一种方式，把对应的完整 prompt 发给你的 AI Agent。仅安装后，Agent 可以根据描述选择 Skill，但不保证每次选中；希望 Apple 开发任务默认优先使用它，选择第二种。

### 选项一：仅安装

```text
请从 https://github.com/o1xhack/apple-workflow-skills/releases/latest 的最新正式 Release 安装 Apple Workflow Skills，只使用该版本的 apple-workflow-skills.zip 资产，将完整文件夹安装到你配置的 skills 目录，保留本地自定义修改，并告诉我安装版本；资产不可用时停止。 不要修改 AGENTS.md 或其他全局指令文件。
```

### 选项二：安装并设为全局默认工作流

```text
请从 https://github.com/o1xhack/apple-workflow-skills/releases/latest 的最新正式 Release 安装 Apple Workflow Skills，只使用该版本的 apple-workflow-skills.zip 资产，将完整文件夹安装到你配置的 skills 目录，保留本地自定义修改，并告诉我安装版本；资产不可用时停止。

安装成功后，在当前 Agent 实际使用的用户级全局 AGENTS.md 中添加以下规则。先读取现有内容，保留其他规则；已有等效规则时不要重复添加。确认全局路径后，文件不存在则创建；无法确定当前 Agent 的全局指令位置时，询问我，不要猜路径或改用仓库内的 AGENTS.md。最后报告安装版本、修改的指令文件路径和最终规则。

For Apple UI design, SwiftUI implementation or refactoring, adaptive layouts,
Liquid Glass, UI performance or rendered validation, and Swift concurrency work,
use $apple-workflow-skills as the primary workflow.
Load only the modules relevant to the task; route non-UI concurrency work directly
to its shared Swift concurrency guidance. Preserve project-specific rules and
deployment targets.
```

第二种方式会为读取该全局指令的 Apple 项目设定优先工作流，同时保留项目自身的规则和部署目标。只想在某个项目生效时，可将 prompt 中的“用户级全局 AGENTS.md”改成该项目的 `AGENTS.md`。

## 当前覆盖什么

- **SwiftUI** — 原生界面设计、导航、Observation 状态管理与视图重构。
- **Liquid Glass · iOS 26+** — 原生玻璃材质、分组与转场。
- **Swift 6 并发** — actor、Sendable、异步任务与取消。
- **iPhone Duo · Beta** — 自适应与折叠布局指导，设备专项验证待完成。
- **UI 质量** — 无障碍、性能审查与 Preview／模拟器验证。

[完整覆盖范围 →](docs/coverage.zh-CN.md)

当前仓库的未发布修订版增加了 Duo 核心指导与[六份完整英文字幕资料](external-sources/apple/iphone-duo/2026-09-10/README.md)，按需读取且不打入安装 ZIP。已发布的 v0.1.0 尚不包含这些新增内容。

## 为什么用这套 Skills

**一个入口。** 直接描述任务，Agent 按需选择规则，省去在多个重叠 Skills 之间挑选的步骤。

**从设计到验证。** 不只讨论页面怎么写，还把界面如何组织、如何实现、实际检查了什么连起来。

**适应已有项目。** 以 SwiftUI 为原生界面实现重点，沿用项目的架构与系统兼容范围；使用这套 Skill 无需先迁移框架。

## 上游维护

我们选择性整合多个 MIT 来源，并独立维护内容。每两天检查上游正式 Release，判断哪些变化值得采用；Apple SDK 的更新也可以直接推动改进。

审查后的改进通过新的 Release 交付。安装和更新使用已发布的 ZIP，默认分支上的编辑不会改变已安装版本。

[来源记录](upstream/manifest.json) · [整合决策（英文）](docs/decisions.md) · [维护流程（英文）](docs/maintenance.md)

## 使用与技术说明

安装后，可以这样告诉 Agent：

```text
使用 $apple-workflow-skills 改进这个设置页的视觉层级和窄窗口布局。
使用 $apple-workflow-skills 重构这个 View，保持现有行为。
使用 $apple-workflow-skills 排查后台导入的取消问题。
```

一个可安装 Skill 按需进入 **Apple UI Workflow** 或 **Shared Swift Concurrency**。UI 分支覆盖设计、SwiftUI、布局、玻璃效果、性能与验证；通用并发可以独立使用。

安装成品位于 `skills/apple-workflow-skills/`。维护资料位于 `upstream/`、`docs/`、`scripts/` 和 `tests/`，不会进入 ZIP。

更新时，让 Agent 再次安装最新正式 Release。需要固定版本时，使用具体的 Release 页面，例如 `/releases/tag/v0.1.0`。手动安装则下载 Release ZIP，将完整文件夹复制到 Agent 的 skills 目录。

<details>
<summary>开发与验证</summary>

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/check_upstream_releases.py
python3 scripts/package.py --output /tmp/apple-workflow-skills.zip
```

这些检查覆盖包结构、引用、运行内容为英文、许可归属与 Release 监控。真实 App 行为需另行按[路由验收场景（英文）](tests/routing-cases.md)评估。

</details>

## 许可

采用 [MIT](LICENSE)，并保留[第三方归属声明](THIRD_PARTY_NOTICES.md)。
