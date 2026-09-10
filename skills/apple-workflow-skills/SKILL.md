---
name: apple-workflow-skills
description: Route Apple application work to focused guidance for native UI design, SwiftUI implementation and refactoring, adaptive layouts, iPhone Duo adaptation, Liquid Glass, UI performance, rendered validation, or shared Swift concurrency. Use for these Apple development tasks while preserving the project's platform and toolchain.
license: MIT
metadata:
  version: "0.2.0-dev"
---

# Apple Workflow Skills

Read the current project's rules, target platforms, minimum OS versions, Swift language mode, and actual request before choosing a path. Distinguish explanation, diagnosis, implementation, and validation. Do not expand the task merely because this skill covers multiple domains.

## Route the task

- For visual design, components, navigation, refactoring, adaptive layout, Liquid Glass, or UI performance, read [Apple UI Workflow](workflows/apple-ui/index.md).
- For actors, `Sendable`, task cancellation, networking, files, databases, or background imports, read [Shared Swift Concurrency](shared/swift-concurrency/index.md) directly.
- For iPhone Duo design, layout, hinge, scene, or camera adaptation, read [iPhone Duo](workflows/apple-ui/swiftui/references/foldable-layout.md), then only the relevant detail module.
- For mixed tasks, choose the primary path first and load the other module only for the concrete cross-cutting concern.
- Dedicated SwiftData, Swift Testing, signing, release, widgets, and App Intents modules are not included yet. Follow project rules and consult current official documentation when those topics arise.

Internal modules are not separate installation dependencies and do not authorize automatic delegation. Follow relative links only as needed; do not preload the entire package or run every validation path for every change.

## Shared boundaries

Project architecture, supported platforms, and user requirements outrank examples. Check new APIs against the actual SDK and deployment target; do not upgrade the toolchain or replace architecture merely to apply a preference.

Discover available tools at runtime. Installing this skill does not imply access to Xcode, a Simulator, or a physical device.

Report the concrete change, evidence actually collected, and remaining gaps. Compilation, image generation, rendered inspection, successful interaction, and physical-device behavior are distinct evidence levels.
