# UI Performance

Establish the symptom, reproduction action, data size, device or Simulator, and Debug or Release configuration. A diagnosis-only request does not authorize implementation.

## Code-level hypotheses

- Observation scopes are too broad, so one service change recomputes unrelated screens.
- List identity is unstable, generated on refresh, or based on position instead of domain identity.
- `body` performs filtering, sorting, formatting, image processing, or synchronous I/O.
- Geometry or preference feedback produces repeated layout.
- Full-resolution image decoding, unbounded caches, or heavy work occupies the main actor.
- Animation covers too much of the hierarchy or layout changes rebuild state.

Code evidence supports hypotheses, not measured conclusions. Use available Instruments, traces, or memory tools when the question requires runtime proof. If those tools are unavailable, state the evidence gap.

## Fix and retest

Choose the narrowest relevant change: reduce observation scope, stabilize identity, derive values from explicit inputs, bound caches, downsample images, or remove layout feedback.

Every cache needs an invalidation policy. Use equatable shortcuts only when comparison cost and value semantics justify them.

## Focused checks

- For expensive lazy rows, inspect whether each element produces a stable count and shape of top-level views. A container around conditional row content can preserve that structure; `Group` is a passthrough. `-LogForEachSlowPath YES` can identify nonconstant row counts in supported SwiftUI runtimes. Filtering before row construction can help, but repeated filtering also has a cost.
- For modifier-only changes, a conditional modifier value or `AnyShapeStyle` may preserve identity better than replacing the view. Intentional branch-specific views and type erasure remain valid choices; measure the affected lifetime or cost rather than flagging their presence alone.
- Retain per-row observable models when rows own them instead of recreating reference objects on every parent evaluation. Passing a row its value or existing model can avoid a repeated lookup dependency on the whole collection.
- For high-frequency scroll or geometry changes, derive the smaller state that readers need. `scrollTransition` or `visualEffect` may serve appearance changes without making every body observe raw measurements. Remove genuinely unused environment subscriptions where they add work.
- On iOS 27 runtimes, `AsyncImage` caches image data according to transport headers. The new request initializer and `asyncImageURLSession` require iOS 27+ for custom policies. Check size limits, server policy, eviction, and offline needs before adding or removing a cache; older supported runtimes may need another path.

Load [Deep Performance Work](deep-review.md) only for a requested deep review or an established update problem. Routine changes do not justify broad model restructuring.

Compare frames, CPU, memory, or operation latency in the same scenario and configuration. Do not claim a percentage improvement without a baseline. Simulator evidence does not establish physical-device energy use or all-day battery behavior. See [UI Validation](../validation/index.md).
