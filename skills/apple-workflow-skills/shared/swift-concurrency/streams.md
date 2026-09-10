# Streams and Callback Bridging

`AsyncStream` represents a sequence of events. A checked continuation represents one asynchronous completion. Their termination contracts are different.

- Finish finite streams and release observers when either producer or consumer terminates. Repeated `AsyncStream.finish()` calls are allowed; do not apply checked-continuation crash semantics to them.
- Resume a checked continuation exactly once across success, failure, cancellation, synchronous callback, and registration races.
- Define buffering and event-loss semantics for high-throughput streams. A bounded buffer does not automatically apply backpressure to a producer.
- Verify cancellation against the actual `AsyncSequence`. Do not assume every `for await` loop stops immediately, and distinguish why the loop ended before continuing business work.
- `onTermination` and cancellation callbacks may run in different execution contexts. Protect shared mutable cleanup state.
- Prefer a legacy API's cancellation handle when bridging it. Existing queues or locks can remain when they still own a valid low-level responsibility.

Test synchronous and duplicate callbacks, cancellation before registration, producer-first completion, slow consumers, and cleanup after cancellation.
