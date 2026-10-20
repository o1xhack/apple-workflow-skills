# Duo Audit and Validation

Load for an existing-app readiness audit or Duo validation after [Duo Overview](foldable-layout.md). Use [External Reading](duo-sources.md) for Apple's current preparation checklist and tools. An audit should identify concrete source locations, the affected flow, and the smallest suitable fix.

## Establish the build behavior

First complete [Toolchain Preflight](../../../../shared/toolchain-preflight.md) for the requested work. Report the actual Xcode/build SDK and available runtime/destination, and which Duo implementation or validation checks they support. Do not infer readiness from a dated RC/beta reference or from the presence of an SDK alone.

Distinguish build SDK, deployment target, runtime OS, and installed tools. Apple's October 2026 preparation page describes these build-dependent defaults:

| Build SDK | Duo presentation |
| --- | --- |
| iOS 26 or earlier | Familiar centered window on the inner display; content left of the status bar/camera when closed |
| iOS 27.0 | Dynamic resizing over most of the inner display, avoiding the status-bar area |
| iOS 27.1 or later | Full-display layout and vertical bars in supported contexts; audit custom content before shipping |

Rebuilding does not by itself verify app readiness. `UIRequiresFullScreen` can still restrict multitasking on Duo, but does not stop open/close resizing. Review its actual product purpose before removing it; supported orientations do not lock the inner display.

For apps built with SDK 27+, the full-screen compatibility key changes scene resizing behavior rather than preventing all resizing; Apple's migration note describes discrete resizing. Check the launch-screen declaration for an iOS 27 submission: an existing storyboard, `UILaunchScreen`, or the corresponding generated build setting can provide it. Inspect actual target settings and the intended product behavior before changing either configuration.

## Audit resizing assumptions

- Find `UIScreen.main.bounds`, cached screen dimensions, and fixed device-size comparisons. Size layout from the view, window, or SwiftUI container; observe changes throughout the session, not just at launch or `viewIsAppearing`. In UIKit, perform size-dependent layout in layout callbacks and coordinate transitions when needed.
- Replace scene-independent window creation with `UIWindow(windowScene:)` where the app uses scenes. If screen information is actually required, obtain it dynamically from the current window scene. Use traits/environment for display scale.
- Find layout decisions based on `UIDevice.current.orientation`, `statusBarOrientation`, or scene `interfaceOrientation`, including `effectiveGeometry`. Choose size classes and container aspect ratio instead. Camera rotation and genuine motion features have separate requirements; do not mechanically remove those uses.
- Find idiom branches that assume every phone is compact or every regular-width view is an iPad. Keep genuine platform behavior, but make space-dependent layout follow available space. `GeometryReader` and `containerRelativeFrame` are not inherently obsolete.
- Inspect asymmetric safe areas, custom bars, sheets, popovers, fixed controls near the fold, and hero images that crop important content when wide. Load [Duo Layout](duo-layout.md) or [Duo Bars](duo-bars.md) only for the affected concern.
- Review unusual container nesting in its actual flow. Understand what each layer contributes before proposing a replacement; look for clipping, inaccessible secondary content, navigation conflicts, or lost state rather than treating the nesting itself as a failure.
- Keep scene navigation and editing state per scene. `UserDefaults` and `@AppStorage` are app-wide stores; they do not isolate separate windows. Ensure resizing cannot recreate a submission or discard unsaved input.

Apple's preparation page offers an Xcode resizability skill and `xcrun agent skills export`. Use it only if the task benefits from the installed tool's audit; check what that version actually exports. Exporting is not installing, and the tool may not yet contain the advertised skill. Its findings do not replace manual review or authorize unrelated modernization.

## Choose validation scope and stop conditions

Start from the requested result, changed code, shared dependencies, and project-required gates. Use this order; expand when a concrete risk, requirement, or failure justifies it:

| Priority | Coverage | Completion evidence |
| --- | --- | --- |
| First | Changed pages and their primary actions at narrow, intermediate, and expanded sizes | Actual layout and action results, including cancel without unintended writes |
| First | Affected cross-display editing, selection, navigation, and presentations | Continue the task after each transition; use [interaction cases](duo-interaction-cases.md) for focus and presentation lifetimes |
| First | Ordinary supported iPhone/iPad paths affected by shared changes | Representative regression through those same paths, preserving supported OS fallbacks |
| Risk-driven | Long/localized text, accessibility sizes, RTL, VoiceOver, themes, constrained windows | Choose the dimensions affected by the change; typography or accessibility changes bring the relevant checks into the first pass |
| Task-dependent | Real accounts, capture hardware, physical folding, and older-device performance | Run when required by the task or project; otherwise report the specific untested boundary |

For a broad adaptation, select relevant pose/window scenarios below. This is a menu of checks, not an automatic cross-product of every page, pose, language, and setting. A representative sample does not establish complete platform coverage.

Finish the scoped work when its acceptance checks and project-required final gates pass, affected regressions are covered, and material limitations are stated. Record unrelated business defects separately; do not silently absorb them into adaptation. A failed required gate remains failed until resolved or explicitly handled under the project's rules. Missing optional evidence is a limitation, not an automatic new delivery prerequisite. Revisit scope if a finding threatens correctness, data, permissions, or the requested behavior.

## Validate the affected flows

- For a broad adaptation, exercise closed outer and open inner displays in portrait/landscape, partial folds, intermediate sizes, both Split View sides, and vertical resizing beneath pinned Picture in Picture where supported. A generic resizable simulator or iPhone Mirroring tests sizing; the Duo simulator also tests native bars and reserved regions.
- During each relevant transition, keep an edit, selection, scrolled item, navigation destination, or playback active. Verify continuity and the intended action afterward, rather than relying on a screenshot alone.
- For affected controls, inspect keyboard visibility, large text, RTL geometry, overflow access, VoiceOver traversal, and custom sheet/control avoidance. A custom layout crossing the fold may need accessibility grouping; do not rewrite focus order without observing a problem.
- Use documented Device Hub/Simulator controls available in the installed version. Do not invent a `simctl` fold command or claim resizing a generic window reproduces hardware posture. Check accessibility frames and successful interactions after live resizing.
- Test camera capture, lens handover, mirroring, and accessory availability on hardware. Device Hub's physical-device interaction prevents camera/microphone access; use direct device interaction for that evidence. Previewing accessory views verifies layout, not capture eligibility.

Report source review, SDK/typechecking, rendered inspection, successful interaction, and hardware results separately. State the build SDK and tested runtime for actual checks. Missing tools limit those checks without invalidating a completed source audit.

## Diagnose automation before changing the app

A successful tool receipt may establish only that a command was issued. Verify the postcondition: the destination appeared, text changed, the intended row was selected, or cancellation left data unchanged. Empty accessibility output does not establish an empty app; a screenshot does not establish successful input.

When repeated attempts disagree with the visible result, stop repeating the same action and check:

1. The intended process, scene/window, and active inner/outer display. Obtain a fresh settled snapshot after the transition; discard stale element references.
2. The screenshot and input coordinate spaces: display, orientation, point/pixel scale, crop, and coordinate conversion. Reacquire the target on the current display rather than reusing an earlier coordinate.
3. The input mode: hardware versus software keyboard, keyboard layout, responder, and whether the action reached the intended field. Successful programmatic text injection does not prove that software-keyboard typing works.
4. The tool connection and installed version. Consult that tool's documentation for reconnecting or supported interaction paths; do not invent repair commands or restart unrelated shared services.

After repairing the observation/input path, repeat the smallest failed interaction and inspect its result. If it still fails with reliable input, inspect app geometry, focus, or presentation state. If the tool remains unavailable, record the check as blocked or untested and continue independent in-scope work; do not modify the app merely to explain tool failure. Keep original failures alongside later results.

## Small evidence record and reuse

Use the project's existing evidence format where possible. One row per meaningful scenario is enough:

| Source/build | Environment | Scenario | Expected / actual | Evidence and status |
| --- | --- | --- | --- | --- |
| Commit plus relevant dirty-diff fingerprint; installed build identity | Build SDK, runtime, device/window/pose, input mode; language/text size when relevant | Steps, starting state, transition and subsequent action | Separate text, focus, keyboard, caret and typing outcomes when editing | Screenshot/log/result reference; pass, fail, blocked or untested |

Reuse prior results when relevant source and environment are unchanged, the installed artifact is traceable to that source, and no new failure or doubt undermines the evidence. After a change, rerun affected checks, including shared consumers; retain unaffected results with their original provenance. Complete the project's required final gates at its required milestone. Neither every local edit nor a documentation-only change automatically calls for a new full product matrix. Keep closeout to changes, results, limitations, and remaining required work; link existing evidence instead of rewriting it.
