# Design Principles

Read this module when visual hierarchy, page organization, or copy requires judgment. For component implementation, read [SwiftUI](../swiftui/index.md).

- Emphasize what the user needs to understand and do now. Avoid repeating the same explanation in titles, descriptions, and footers.
- Preserve the project's spacing, typography, and semantic colors. Without a design system, begin with system defaults and a small consistent token set; a 4- or 8-point grid is an option, not a universal whitelist.
- Use semantic text styles and intentional weight to express hierarchy while preserving Dynamic Type. Example font sizes and corner radii are not cross-platform Apple rules.
- Use semantic foreground and background roles for emphasis. Check readability in dark mode, increased contrast, and varied backgrounds. Brand colors may come from assets instead of forcing system blue everywhere.
- Prefer `Form`, `Section`, `List`, and `LabeledContent` for settings and grouped information. A custom card needs a clear information or interaction benefit.
- Represent a single selection with one value, not multiple independent booleans. Reveal controls progressively for multi-mode editors.
- Button labels describe actions. Errors explain what happened and how to recover. Distinguish first-use empty states, no results, and failed loading.
- Keep numeric units and time granularity consistent. Do not present stale snapshots as live data.
- Size graphics and strokes proportionally without imposing one universal hero-number or progress-ring style.

Finish with [Accessibility](../swiftui/references/accessibility.md) and use [UI Validation](../validation/index.md) to inspect truncation, density, and layout collapse.
