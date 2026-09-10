# Tasks and Cancellation

Use `async let` for a fixed number of independent operations and task groups for dynamic work. Bound concurrency for large inputs by adding new work as prior work completes rather than creating thousands of tasks at once.

Structured scopes wait for their children. Group results arrive in completion order; carry a stable index when input ordering matters. Error propagation and sibling cancellation depend on the group API and how results are consumed. Do not assume one child throw instantly cancels every sibling. Collect partial success and failure explicitly when required.

`Task {}` and `Task.detached` both create unstructured tasks. The former may inherit actor context; the latter does not inherit the same context. Detaching is not a general performance fix.

Every unstructured task needs an owner, handle, error policy, completion path, and cancellation path. Prefer framework lifecycle tasks for view work and an owned service for longer business operations.

Cancellation is cooperative: `cancel()` sets state but does not forcibly stop underlying work. Check cancellation at safe points in CPU loops and understand whether awaited functions respond to it. Normal cancellation should not become a user-facing failure, and cancelled old work must not overwrite current results.

A cancellation handler may race with operation setup. Synchronize resource registration, cancellation, and completion. Releasing a task handle is not cancellation; design shared-task cancellation independently from any one waiter's lifetime.

Test fast restarts, completion after cancellation, child errors, concurrency limits, partial success, and resource cleanup.
