# Duo Hinge, Scenes, and Camera

Load only for these capabilities after [Duo Overview](foldable-layout.md). Source map: [External Reading](duo-sources.md), especially Multiple Displays and Camera. The following capabilities and API names come from the talks; verify the SDK and actual runtime support before implementing them.

## Hinge and scenes

- Use hinge status/angle for deliberate effects or interactions, not as a substitute for layout regions. The talk names `onHingeChange` and `UIHingeInteraction`; handle a missing hinge on other devices and reset the effect outside the supported interaction state.
- Multitasking includes side-by-side apps and vertically reduced space under pinned Picture in Picture. Keep scene state independent and preserve shared-model consistency.
- Multiple windows are dynamically available: the talk permits creating another scene on the inner display, not the outer display. Handle activation failure; evaluate `UIWindowSceneActivationAction` for a control that follows availability.
- Scene accessories pair supporting content with the primary UI. Observe availability rather than assuming it persists after a fold, camera change, or app transition.
- The talk's `CameraCaptureAccessory` requires an active camera session with the main app full-screen on the inner display. Register it with the camera view so accessory lifetime follows that feature; use `sceneAccessory` and `onAvailabilityChange` as lookup terms. This does not imply arbitrary always-on second-display UI.
- Decide what the outward-facing viewer should see; do not automatically mirror private controls or content from the primary scene.

## Choose camera complexity intentionally

- The described virtual front camera automatically switches between inner and outer front cameras. It exposes their common capabilities; the talk describes a maximum of 1080p/60 fps and no depth through the virtual device.
- Access physical cameras only when their additional capabilities matter. The talk describes inner 1080p/60 fps and outer up to 4K/120 fps; verify supported formats at runtime. Physical-camera selection makes the app responsible for switching.
- A camera's fixed `.front` / `.back` position is not its direction relative to the current view. Opening, closing, or moving displays can reverse the viewer-relative relationship.
- Evaluate `AVCaptureDeviceDirectionCoordinator` in AVKit. Create one per relevant view when using both displays; each reports directions relative to that view.
- The coordinator is main-actor isolated. Its `AVCaptureDeviceDescriptor` is described as sendable; pass it to the camera's isolation domain before using capture APIs. Do not run capture-session reconfiguration directly in the UI callback. Read [Shared Swift Concurrency](../../../../shared/swift-concurrency/index.md) only if this ownership boundary needs work.
- Coordinate switching, preview mirroring, and visible UI transitions. Rear-camera selfies may require mirroring for a natural preview. Adopt rotation coordination so previews and captured images stay upright as displays change.
- Choose preview fill versus fit intentionally, using extra space for controls where useful. The talk names `dynamicAspectRatio` for square sensors; verify formats rather than forcing a fixed crop. Disable sensor-orientation compensation only after adopting the documented rotation-coordinator path and verifying support.

Validate actual camera transitions on supported hardware. Simulator layout checks cannot establish camera availability, quality, direction, or frame-rate behavior.
