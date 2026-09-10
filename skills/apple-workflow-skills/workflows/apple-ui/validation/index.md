# UI Validation

Choose the shortest path that can answer the current question. Do not run every environment for every change.

| Question | Evidence path |
| --- | --- |
| Component appearance, typography, and state layout | Native Preview of the production component |
| Navigation, keyboard, sheets, permissions, imports, lifecycle | Full app in Simulator or the target environment |
| Sensors, background execution, thermal behavior, energy, real services | Physical device for an appropriate observation period |

## Preview

Render the actual production view with bounded, repeatable loading, empty, error, and long-content states. Preview initialization must not start real sync, scan an entire database, or begin background recording.

Discover the available native Xcode preview path. If unavailable, use the current Canvas or Simulator and report the actual route; do not restructure the project merely to satisfy a mirroring tool.

A visual check requires a current rendered image that was actually inspected. Compilation, a returned file path, or a loaded browser is not equivalent to seeing the UI.

Check truncation, unintended gaps, collapse after hidden sections, text scaling, safe areas, and action discoverability. After an edit, inspect the affected states again rather than citing an old image.

## Full app and physical device

Preview does not guarantee real navigation, keyboard, or loading lifecycle behavior. Exercise the affected flow before reporting interaction success.

Representative data can validate layout; real-data authorization is separate. Do not commit private snapshots.

A Simulator install or visible Home Screen is not a passed test. Record what was observed inside the app.

Choose stationary, movement, foreground/background, and long-duration device scenarios according to the symptom. Do not extrapolate a few minutes into all-day energy behavior.

Use project-specific tools or focused skills when available, following their current documentation rather than assuming a tool name or connection exists.

Report the path used, what was actually seen or operated, and remaining gaps. Routine UI changes do not need a separate long report.
