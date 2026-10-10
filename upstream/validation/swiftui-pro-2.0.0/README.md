# Representative SDK source probes

These minimal fixtures support the 2.0.0 upstream review. They are not runtime examples or a complete app test suite and are excluded from the installable ZIP.

`results.json` records the reviewed compiler, per-source SHA-256, deployment target, and expected result. Build each source independently with the command shape in that file and the installed iOS Simulator SDK. Use the host’s approved build-scratch location for the module cache and diagnostics; do not silently switch toolchains or upgrade an app target to make a probe pass.

The three expected failures check actual availability boundaries, not regressions in supported code. Entry diagnostics and the compiling State double-initialization case also require reading the documented semantics. Typechecking does not exercise lazy state construction, movement order, resource lookup, UI presentation, or cache behavior.
