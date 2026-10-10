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
- Preserve trigger semantics when moving a binding setter's work into `onChange`: a setter handles writes through that binding, including equal-value assignments; `onChange` follows observed value changes, including programmatic ones. Writable computed properties or labeled subscripts can project conversions, but retain the custom binding when it better represents the flow.
- Cache derived collections only with a clear lifecycle and invalidation policy.
- Verify how `AppStorage` and Observation changes propagate; `@ObservationIgnored` does not solve observation by itself.
- A database count snapshot does not become live data automatically. The data layer must define update triggers.

## Initialization and observation

- With Xcode 27, `@State` is a macro. Private view-owned state supports lazy initial-expression evaluation; changing access control on existing state can change caller initialization, so inspect call sites before doing so. A parent-supplied value may belong in an input or binding instead.
- Give state one initial value, either at the declaration or in the initializer. Setting both can cause an initialization-order error; even a compiling assignment may lose to the declaration's initial expression. State persists with view identity, so a changing initializer input is not an automatic reset mechanism.
- Keep navigation, selection, and editing state scene-local when windows should operate independently. Scene-root `@State` or suitable `@SceneStorage` can serve this; app-wide stores couple windows unless that sharing is intentional.
- Observation tracks stored properties read during evaluation. A computed getter also reads its underlying properties, and a stored struct is one dependency even when only one field is used. Reading several independent properties from one observable object does not by itself justify splitting the model.
- With current Observation macro generation, meaningful `Equatable` conformance can suppress notifications for equal assignments. Consider equality cost and semantics before adding it to large values. More involved dependency changes belong in [Deep Performance Work](../../performance/deep-review.md).
- Keep custom environment and focused-value defaults stable. Fresh reference objects, UUIDs, or dates may invalidate readers during unrelated environment propagation. An optional default or deliberately owned shared fallback can avoid repeated construction; constant defaults need no change.
- Custom closures in environment values can compare poorly and produce extra updates, even inside a wrapper struct. A value or stable model exposing a method can be a better action representation when it fits. Assess the actual cost before reshaping existing APIs, and leave system actions such as `dismiss` and `openURL` intact.

## Collection identity

Use identity that survives the intended insertions, deletions, edits, filtering, and moves. Allocate it when storing the element, not afresh while constructing rows. Positional indices are suitable for fixed positions but can replace row state in a mutable domain collection.

Prefer a compact immutable key over hashing a whole editable struct through `id: \.self`; small unique values can legitimately identify themselves. For numbered rows, use the element ID rather than the offset. Direct `ForEach(items.enumerated(), id: \.element.id)` needs the iOS 26+ collection conformance; earlier targets can materialize `Array(items.enumerated())`.
