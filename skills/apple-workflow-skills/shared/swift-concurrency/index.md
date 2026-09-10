# Shared Swift Concurrency

Use this module for networking, files, databases, background services, and UI work. It does not require loading Apple UI Workflow.

First inspect each target or package's Swift version, language mode, strict-concurrency settings, default actor isolation, and relevant upcoming features. `async` does not mean background-thread execution, and `await` does not guarantee a suspension.

- [Isolation and Diagnostics](isolation.md): actor reentrancy, `Sendable`, global state, and compiler boundaries.
- [Tasks and Cancellation](tasks.md): structured concurrency, bounded parallelism, and lifecycle.
- [Streams and Callback Bridging](streams.md): `AsyncStream`, continuations, and resource cleanup.

Find mutable state and cross-isolation data before choosing the smallest correction. Do not mark an entire business layer `@MainActor` merely to silence diagnostics, and do not use `@unchecked Sendable` as a shortcut.

Name the state invariant, trigger, and evidence behind each finding. Test with controlled events and ordering rather than random sleeps.
