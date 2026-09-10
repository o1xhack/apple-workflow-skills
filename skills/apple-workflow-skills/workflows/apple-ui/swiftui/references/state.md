# State Ownership

Answer who owns, changes, and observes a value before choosing a property wrapper.

| Situation | Approach |
| --- | --- |
| Value state owned by one view | private `@State` |
| Child mutates parent value | `@Binding` |
| Observation-capable target and view-owned model | `@State` holding an `@Observable` object |
| Injected observable object | explicit property; `@Bindable` only when bindings are needed |
| Truly app-wide service | Environment, without making every dependency global |
| Older target or existing `ObservableObject` architecture | owner uses `StateObject`; consumer uses `ObservedObject` or `EnvironmentObject` as appropriate |

Observation does not automatically provide thread safety, and not every model belongs on `MainActor`. Define isolation from actual UI needs; use [Shared Swift Concurrency](../../../../shared/swift-concurrency/index.md) for business concurrency.

- Maintain one source of truth instead of storing the same derived result in several state values.
- Do not start network requests, write databases, or perform heavy initialization in `body`. Events call small methods; complex work belongs in models or services.
- Prefer naturally projected bindings. A custom `Binding` is fine for necessary conversion, but its setter must be predictable and avoid hidden heavy side effects.
- Cache derived collections only with a clear lifecycle and invalidation policy.
- Verify how `AppStorage` and Observation changes propagate; `@ObservationIgnored` does not solve observation by itself.
- A database count snapshot does not become live data automatically. The data layer must define update triggers.
