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

Compare frames, CPU, memory, or operation latency in the same scenario and configuration. Do not claim a percentage improvement without a baseline. Simulator evidence does not establish physical-device energy use or all-day battery behavior. See [UI Validation](../validation/index.md).
