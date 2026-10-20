# Toolchain Preflight

Read before SDK-dependent implementation, compilation, or runtime validation. For explanation, source review, or documentation-only work, inspect only the environment information needed to answer the task; an unavailable Xcode or Simulator need not block independent work.

## Establish the actual environment

Start with the project's supported platforms, deployment targets, compiler/language requirements, intended APIs, and requested evidence. Then check the tools that the planned command or integration will actually use:

- **Xcode:** record version, build number, and effective developer directory. Account for `DEVELOPER_DIR`, per-command overrides, CI configuration, and tool-specific selection; `xcode-select` alone may not describe the invoked toolchain.
- **Build SDK/compiler:** list the SDKs supplied by that toolchain and confirm the required platform and declarations exist. A runtime availability check cannot make an absent SDK declaration compile. Preserve supported deployment targets and compatibility paths.
- **Execution environment:** for Simulator checks, inspect available runtimes and compatible available devices; for hardware checks, inspect the connected destination, its OS, and tool support. An installed SDK does not establish an installed runtime, a usable destination, or physical-device evidence.

With the intended environment overrides applied, standard read-only CLI checks include:

```sh
xcode-select -p
xcodebuild -version
xcodebuild -showsdks
xcrun simctl list runtimes
xcrun simctl list devices available
```

Run only the checks relevant to the task. A wrapper or connected tool may select another Xcode; verify its effective selection rather than assuming it shares the shell's environment. Do not boot devices, download components, change global `xcode-select`, or upgrade project targets merely to inventory capabilities.

## Decide readiness for this task

Briefly state the observed Xcode/build SDK, intended runtime/destination when needed, and whether they support the requested implementation and evidence. Name a concrete minimum only when the project's requirements, required declarations, current official documentation, or tool compatibility establish it. A newer Xcode is not automatically necessary or sufficient.

If the environment is sufficient, continue with the selected tools. If a required declaration or destination is missing, identify the specific affected work and the capability needed. Use an already available suitable toolchain with a command-scoped selection when authorized by the task and project; otherwise continue independent source work and report the blocked build or interaction honestly. Do not report an unavailable check as passed or silently substitute a different device as equivalent evidence.

Dated Xcode, SDK, RC/beta, and runtime versions elsewhere in this package describe historical source or validation snapshots. They are not current minimum requirements or a live inventory. Recheck the actual environment when tool selection, required capabilities, or validation destinations change; reuse a still-valid inventory within the same task.
