# UI Async State

The UI owns presentation state and view lifecycle. For isolation, task groups, streams, and general cancellation semantics, read [Shared Swift Concurrency](../../../../shared/swift-concurrency/index.md).

- Use `.task` for appearance-driven loading and `.task(id:)` when an input change should restart work. Tasks must cooperate with cancellation; calling `cancel()` does not forcibly stop an underlying service.
- Model meaningful `idle`, `loading`, `loaded`, and `failed` states. Preserve existing results during refresh when the product calls for it.
- Treat debounce cancellation as normal. An old cancelled search must not clear a newer query's results.
- After `await`, check cancellation and confirm the result still belongs to the current input before updating UI. Reject stale results even if the service ignores cancellation.
- If a service wraps cancellation inside another error, combine error inspection with `Task.isCancelled`. Ordinary cancellation should not display a network failure.
- Give imports, uploads, and background operations that outlive the screen to an explicitly owned service. The screen observes progress rather than owning the entire business task lifecycle.
- Keep retry, offline, caching, and deduplication policies in services instead of duplicating them across views.
- Validate last-request-wins behavior with controlled slow responses and rapid input changes, not only the success path.
