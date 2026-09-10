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

[使用 Skills CLI 安装](#安装) · [下载最新版本](https://github.com/o1xhack/apple-workflow-skills/releases/latest/download/apple-workflow-skills.zip) · [全部版本](https://github.com/o1xhack/apple-workflow-skills/releases)

</div>

Apple Workflow Skills 是一个单入口 Skill，会根据任务选择具体的 Apple 开发模块，不会一次加载整个资料库。首版重点覆盖原生 UI：设计、SwiftUI 实现、自适应布局、Liquid Glass、性能与真实界面验证；通用 Swift Concurrency 则保持为独立的共享分支。

## 安装

仓库只有一个顶层 Skill：

```sh
npx skills add o1xhack/apple-workflow-skills --skill apple-workflow-skills
```

也可以从 [GitHub Releases](https://github.com/o1xhack/apple-workflow-skills/releases) 下载版本化 ZIP，把其中的 `apple-workflow-skills` 文件夹复制到 Agent 的 skills 目录。

重新运行 Skills CLI 命令可以从仓库更新；如果需要可复现的固定版本，请使用 Release 资产。

## 架构

```text
apple-workflow-skills
├── Apple UI Workflow
│   ├── Design Principles
│   ├── SwiftUI
│   │   ├── API 与状态所有权
│   │   ├── 导航与控件
│   │   ├── 自适应与折叠布局
│   │   └── 保持行为的重构
│   ├── Liquid Glass
│   ├── UI Performance
│   └── Preview、Simulator 与真机验证
└── Shared Swift Concurrency
    ├── Isolation 与 Sendable
    ├── Tasks 与取消
    └── Streams 与回调桥接
```

整个仓库只有一个可安装的 `SKILL.md`。内部 Markdown 是按需读取的模块，不是需要分别安装的子 Skills。

Concurrency 故意放在 Apple UI Workflow 之外。UI 异步状态会在需要时引用它，但网络、文件导入、数据库和后台服务也可以独立使用并发模块，而不加载 UI 内容。

## 使用示例

```text
Use $apple-workflow-skills to review this settings screen's hierarchy and narrow-window behavior.
Use $apple-workflow-skills to refactor this SwiftUI view while preserving its MVVM architecture.
Use $apple-workflow-skills to diagnose actor reentrancy in this background import service.
```

Skill 会保留当前项目的架构、deployment targets 与产品决策，只读取任务需要的模块，并明确区分代码审查、编译、实际渲染、Simulator 交互和真机证据。

## 仓库结构

- `skills/apple-workflow-skills/`：完整的可安装成品。
- `upstream/`：仅供维护者使用的来源、采用 commit、Release 基线与审查状态。
- `docs/`：整合与维护决策。
- `scripts/`、`tests/`：结构校验、打包与上游 Release 监控。

`upstream/` 和仓库维护工具不会进入 Release ZIP。安装目录只保留运行规则和一份合并后的 MIT 许可声明。

## 当前范围

首版覆盖以 SwiftUI 为中心的 UI 工作和共享 Swift Concurrency。暂不声称内置 SwiftData、Swift Testing、签名发布、Widgets、App Intents、UIKit 或 AppKit 专项工作流。

折叠与多显示区域只采用保守的通用布局原则；未经验证的 API 与设备假设不会写成可直接生产使用的事实。

## 上游维护

本项目选择性整合并自主改写多个 MIT 来源，不是任何上游仓库的镜像。来源、精确采用 commit 和模块映射集中在 [upstream/manifest.json](upstream/manifest.json)，许可说明集中在 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

GitHub Actions 每两天检查一次上游正式 Release。发现新版本时只创建人工审查 Issue，不会自动覆盖本地内容或发布新版本。Apple SDK 的变化也可以直接推动独立更新，不必等待上游 Release。

## 开发验证

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/check_upstream_releases.py
python3 scripts/package.py --output /tmp/apple-workflow-skills.zip
```

静态校验覆盖单入口、内部引用闭合、运行内容为英文、许可归属与打包边界；它不代表真实 App 的 UI 或并发行为已经验证。

## 许可

Apple Workflow Skills 使用 [MIT License](LICENSE)。基于第三方 MIT 内容的部分列于 [Third-Party Notices](THIRD_PARTY_NOTICES.md)。
