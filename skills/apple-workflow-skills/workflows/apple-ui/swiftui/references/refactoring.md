# Behavior-Preserving Refactoring

Record current state ownership, navigation, and side effects before selecting the smallest refactoring scope. File length alone is not a reason to rewrite architecture.

1. Extract views around independent responsibilities, repeated regions, state, and preview boundaries. Pass only required values, bindings, or actions rather than the entire parent state.
2. Move nontrivial button, `task`, and `onChange` business logic into methods or services. Keep `body` focused on UI description and thin orchestration.
3. Small local `some View` helpers can remain. Prefer a distinct view for stateful, complex, or independently responsible regions.
4. Preserve existing MVVM or other architecture. Do not add forwarding view models for local value state or remove established business models without a requirement.
5. When structural changes affect identity, test editing, selection, scrolling, and task restarts. A legitimate `if` branch is not automatically a defect; do not hide content with opacity solely to avoid lifecycle.
6. Inject dependencies and initialize them at the correct owner. Keep optional models only for real loading or absence semantics rather than replacing them with false placeholders.
7. Follow project conventions for declaration order and file splitting. Do not impose one type per file.
8. Verify original behavior, navigation, and persistence boundaries. File count is not performance evidence.
