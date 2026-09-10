# Isolation and Diagnostics

- Other work may change actor state while a method is suspended at `await`. Recheck request identity, cache version, and eligibility after resuming.
- A synchronous actor segment cannot be interleaved by another actor call. Saving an awaited result in a local variable can simplify reasoning but does not prevent duplicate concurrent downloads.
- In-flight task deduplication must define ownership, whether one waiter may cancel shared work, and whether stale results may be written after invalidation.
- UI state commonly belongs on `MainActor`. Other shared data can use a dedicated actor, immutable `Sendable` values, or appropriate synchronization. Choose the boundary that matches semantics.
- `Sendable` describes safe boundary crossing. Do not add annotations the compiler does not require; verify toolchain and ownership semantics before using newer transfer features.
- When protocol isolation mismatches an implementation, decide whether protocol consumers actually need actor state. Do not use `nonisolated` to disguise isolated access.
- Nonisolated async execution depends on toolchain and feature settings. Do not generalize one target's behavior to every Swift configuration.
- Use `@unchecked Sendable`, `nonisolated(unsafe)`, and `@preconcurrency` only with a documented compatibility or synchronization argument.
- Do not block cooperative threads with semaphores or synchronous waits for async results.

Test shared cache requests, invalidation interleavings, cancelled waiters, reloads, and stale-result rejection. One successful request does not prove actor correctness.
