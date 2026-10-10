# Deep Performance Work

Use for a requested deep performance review or an established problem that may require changing dependency structure. Begin with the reproduction and baseline from [UI Performance](index.md). Preserve architecture and behavior while choosing the smallest useful experiment.

## Narrow the relevant dependency

- Observable objects already track independently stored properties read by a view. A large model or several property reads is not proof that it needs splitting.
- When changing one field of an observed struct repeatedly updates readers of another, consider separating that field, passing the needed value, or using a retained nested observable model. A computed alias reading the same struct does not narrow the underlying dependency.
- Large value inputs can add comparison and propagation cost. A smaller display value or the existing observable owner may suit the affected view. Choose by ownership and measured behavior, not a fixed threshold of three or four fields, and do not convert value models wholesale to reference types.
- Caching an expensive computed result as stored state can reduce repeated work or dependencies. Account for every mutation path, batching, cancellation, and invalidation; an incomplete cache creates stale UI. A cheap getter may be simpler and entirely appropriate.
- Stable per-row models or per-row derived visibility can limit update scope when one collection or raw scroll measurement repeatedly invalidates unrelated rows. Retain their lifetimes and inspect memory as well as CPU.
- Isolating an observation used only by `onChange` in a small view or modifier may reduce an expensive body's update surface. Preserve its side-effect timing and do this only when that dependency contributes to the diagnosed cost.

Compare the same action, data, configuration, and runtime before and after. Report the measured change and any complexity or memory tradeoff; source restructuring alone does not establish an improvement.
