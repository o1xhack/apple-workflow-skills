# Duo Audit and Validation

Load for an existing-app readiness audit or Duo validation after [Duo Overview](foldable-layout.md). Use [External Reading](duo-sources.md) for Apple's current preparation checklist and tools. An audit should identify concrete source locations, the affected flow, and the smallest suitable fix.

## Establish the build behavior

Distinguish build SDK, deployment target, runtime OS, and installed tools. Apple's October 2026 preparation page describes these build-dependent defaults:

| Build SDK | Duo presentation |
| --- | --- |
| iOS 26 or earlier | Familiar centered window on the inner display; content left of the status bar/camera when closed |
| iOS 27.0 | Dynamic resizing over most of the inner display, avoiding the status-bar area |
| iOS 27.1 or later | Full-display layout and vertical bars in supported contexts; audit custom content before shipping |

Rebuilding does not by itself verify app readiness. `UIRequiresFullScreen` can still restrict multitasking on Duo, but does not stop open/close resizing. Review its actual product purpose before removing it; supported orientations do not lock the inner display.

## Audit resizing assumptions

- Find `UIScreen.main.bounds`, cached screen dimensions, and fixed device-size comparisons. Size layout from the view, window, or SwiftUI container; observe changes throughout the session, not just at launch or `viewIsAppearing`. In UIKit, perform size-dependent layout in layout callbacks and coordinate transitions when needed.
- Replace scene-independent window creation with `UIWindow(windowScene:)` where the app uses scenes. If screen information is actually required, obtain it dynamically from the current window scene. Use traits/environment for display scale.
- Find layout decisions based on `UIDevice.current.orientation`, `statusBarOrientation`, or scene `interfaceOrientation`, including `effectiveGeometry`. Choose size classes and container aspect ratio instead. Camera rotation and genuine motion features have separate requirements; do not mechanically remove those uses.
- Find idiom branches that assume every phone is compact or every regular-width view is an iPad. Keep genuine platform behavior, but make space-dependent layout follow available space. `GeometryReader` and `containerRelativeFrame` are not inherently obsolete.
- Inspect asymmetric safe areas, custom bars, sheets, popovers, fixed controls near the fold, and hero images that crop important content when wide. Load [Duo Layout](duo-layout.md) or [Duo Bars](duo-bars.md) only for the affected concern.
- Review unusual container nesting in its actual flow. Understand what each layer contributes before proposing a replacement; look for clipping, inaccessible secondary content, navigation conflicts, or lost state rather than treating the nesting itself as a failure.
- Keep scene navigation and editing state per scene. `UserDefaults` and `@AppStorage` are app-wide stores; they do not isolate separate windows. Ensure resizing cannot recreate a submission or discard unsaved input.

Apple's preparation page offers an Xcode resizability skill and `xcrun agent skills export`. Use it only if the task benefits from the installed tool's audit; check what that version actually exports. Exporting is not installing, and the tool may not yet contain the advertised skill. Its findings do not replace manual review or authorize unrelated modernization.

## Validate the affected flows

- For a broad adaptation, exercise closed outer and open inner displays in portrait/landscape, partial folds, intermediate sizes, both Split View sides, and vertical resizing beneath pinned Picture in Picture where supported. A generic resizable simulator or iPhone Mirroring tests sizing; the Duo simulator also tests native bars and reserved regions.
- During each relevant transition, keep an edit, selection, scrolled item, navigation destination, or playback active. Verify continuity and the intended action afterward, rather than relying on a screenshot alone.
- For affected controls, inspect keyboard visibility, large text, RTL geometry, overflow access, VoiceOver traversal, and custom sheet/control avoidance. A custom layout crossing the fold may need accessibility grouping; do not rewrite focus order without observing a problem.
- Use documented Device Hub/Simulator controls available in the installed version. Do not invent a `simctl` fold command or claim resizing a generic window reproduces hardware posture. Check accessibility frames and successful interactions after live resizing.
- Test camera capture, lens handover, mirroring, and accessory availability on hardware. Device Hub's physical-device interaction prevents camera/microphone access; use direct device interaction for that evidence. Previewing accessory views verifies layout, not capture eligibility.

Report source review, SDK/typechecking, rendered inspection, successful interaction, and hardware results separately. State the build SDK and tested runtime for actual checks. Missing tools limit those checks without invalidating a completed source audit.
