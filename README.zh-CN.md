<div align="center">

# Apple Workflow Skills

**一键安装、按需加载的 Apple 开发工作流 Skill。**

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

把这行 prompt 发给你的 AI Agent：

```text
请从 https://github.com/o1xhack/apple-workflow-skills/releases/latest 的最新正式 Release 安装 Apple Workflow Skills，只使用该版本的 apple-workflow-skills.zip 资产，将完整文件夹安装到你配置的 skills 目录，保留本地自定义修改，并告诉我安装版本；资产不可用时停止。
```

## 当前覆盖什么

[![SwiftUI](https://img.shields.io/badge/UI-SwiftUI-007aff?style=for-the-badge)](docs/coverage.zh-CN.md)
[![Swift concurrency](https://img.shields.io/badge/Swift_6-Concurrency_guidance-f05138?style=for-the-badge)](docs/coverage.zh-CN.md)
[![iPhone and iPad](https://img.shields.io/badge/iPhone_%26_iPad-SwiftUI_guidance-007aff?style=for-the-badge)](docs/coverage.zh-CN.md)
[![iPhone Duo](https://img.shields.io/badge/iPhone_Duo-Beta_guidance-f59e0b?style=for-the-badge)](docs/coverage.zh-CN.md)

当前版本重点覆盖 **SwiftUI 界面开发与 Swift 并发**，按项目实际支持的 Apple 平台和系统版本应用。

**语言范围：** 现代 SwiftUI 代码与 Swift 6 并发概念，同时按项目配置兼顾 Swift 5 语言模式。当前是专项开发指导，尚未定义“完整支持到 Swift 6.x 某个小版本”的语法或编译器验证范围。

| 能力 | 帮你解决什么 | 什么时候用 |
| --- | --- | --- |
| Apple UI Workflow | 把设计、实现和界面验证串成一套流程 | 新建页面，或改进已有操作流程 |
| Design Principles | 理清信息、操作、间距和文字的主次 | 页面显得拥挤，或看不出重点 |
| SwiftUI | 实现与重构原生组件、导航、表单和状态 | 增加功能，或整理复杂 View |
| Adaptive Layout 与 Liquid Glass | 适配窗口尺寸，并使用原生玻璃材质 | 做多尺寸适配，或更新界面外观 |
| UI Performance 与验证 | 排查界面卡顿，选择 Preview、模拟器或真机检查 | 滚动不流畅，或需要确认改动效果 |
| Swift Concurrency | 梳理后台任务、共享数据和取消行为 | 导入、搜索或异步操作出现异常 |

**iPhone Duo 适配 — Beta，部分覆盖。** 已包含通用布局和状态连续性指导；Duo 专用 API 与设备行为仍待验证。Beta 指我们这套指导的成熟度。

暂未包含 SwiftData、Swift Testing、Widgets、App Intents、签名发布、App Store 发布、UIKit 和 AppKit 专项流程。

**已涉及的 API 版本：** SwiftUI 指导包括 iOS/iPadOS 16+ 导航、17+ Observation 状态管理、26+ Liquid Glass。这些数字是具体功能的最低系统版本，不代表已完整覆盖 iOS 26 的全部 API。

[查看完整覆盖范围 →](docs/coverage.zh-CN.md)

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
