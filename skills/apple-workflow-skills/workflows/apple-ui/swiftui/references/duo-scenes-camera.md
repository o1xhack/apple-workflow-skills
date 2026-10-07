# Duo Hinge, Scenes, and Camera

Load only for these capabilities after [Duo Overview](foldable-layout.md). Source map: [External Reading](duo-sources.md), especially the current camera-direction and accessory articles, hinge declarations, and staff Q&A. Hinge observation, camera direction, and camera capture accessories require iOS 27.1; the general scene-accessory infrastructure starts in 27.0. Verify declarations in the actual SDK and keep older-target paths.

## Hinge and scenes

- Use hinge status/angle for deliberate effects or interactions, not as a substitute for layout regions. The documented APIs are `onHingeChange(isEnabled:_:)` and `UIHingeInteraction`. Handle a missing hinge when the view leaves a supported hierarchy; do not assume a fixed angle-update rate or precision.
- Multitasking includes side-by-side apps and vertically reduced space under pinned Picture in Picture. Keep scene state independent and preserve shared-model consistency.
- Multiple windows are dynamically available: the talk permits creating another scene on the inner display, not the outer display. Handle activation failure; evaluate `UIWindowSceneActivationAction` for a control that follows availability.
- Keep navigation, selection, and unsaved edits local to the scene; `UserDefaults` / `@AppStorage` remain app-wide. Folding changes traits within the existing scene rather than automatically reconnecting it. Restore state separately for actual scene disconnection.
- Scene accessories pair supporting content with the primary UI. Observe availability rather than assuming it persists after a fold, camera change, or app transition.
- Decide what the outward-facing viewer should see; do not automatically mirror private controls or content from the primary scene.

## Scope camera accessory content

- Register `CameraCaptureAccessory` through `sceneAccessory(content:)` on the capture view. The system finds the active capture session and chooses presentation while the app is foreground and the capture UI is on the inner display. Do not pass a display or camera to force placement, or treat it as a general second app interface.
- The outer display accepts touch. Keep it focused on a capture task, such as subject framing or teleprompter controls, and retain every essential action in the primary capture interface. Use a shared observable model for both views, keeping persistent state outside accessory view lifetimes.
- Availability and user enablement are separate. Observe `onAvailabilityChange(perform:)` and hide controls for unavailable content; use `CameraCaptureAccessory(isEnabled:content:)` to let people turn it off. Navigation, another registration of the same kind, capture stopping, backgrounding, or closing the device can withdraw it.
- In UIKit, retain `UISceneAccessoryRegistration` from `registerSceneAccessory(_:)`, observe `isAvailable`, and set `isEnabled` for the user's choice. Call `unregisterSceneAccessory(_:)` when withdrawing the feature. Supply scene configuration through `UISceneAccessory.cameraCapture(sceneConfiguration:userInfo:)`; the system assigns the accessory scene role, so a scene-manifest entry does not configure it. Retain shared model state yourself.
- The camera Q&A's later Apple staff clarification says an `ARSession` counts as an active capture session for an accessory. This permits supplementary subject-facing content, not two independent AR views. Do not create a competing capture session merely to make an accessory eligible; a second session can interrupt ARKit's capture.

## Choose camera complexity intentionally

- Existing front-camera discovery with `.builtInWideAngleCamera` / `.builtInUltraWideCamera` returns the virtual front camera on Duo. It follows the app between displays and exposes the physical cameras' common capabilities. `activePrimaryConstituent` identifies the streaming camera and can be nil until capture runs.
- Choose physical `.builtInInnerUltraWideCamera` / `.builtInOuterUltraWideCamera` devices only when their additional capabilities matter. Query formats, frame-rate ranges, and depth support at runtime; physical-camera selection makes the app responsible for switching. Avoid treating a talk's format example as a universal capability guarantee.
- A camera's fixed `.front` / `.back` position is not its direction relative to the current view. Opening, closing, or moving displays can reverse the viewer-relative relationship.
- Create and retain an AVKit `AVCaptureDeviceDirectionCoordinator` per preview view on the main actor. Include the physical front and rear built-in device types the app captures from; it ignores virtual front and external cameras. Its initial direction map is empty until the initial callback arrives, and each view has its own frame of reference.
- `AVCaptureDeviceDescriptor` and `AVCaptureDeviceDirectionMap` conform to `Sendable`. Pass a descriptor from the main-actor callback to the actor owning capture; resolve and reconfigure there. Handle a device disappearing before resolution, failed input replacement, and later direction changes rather than force-unwrapping or assuming the callback reserves a camera. Read [Shared Swift Concurrency](../../../../shared/swift-concurrency/index.md) only if this ownership boundary needs work.
- Prefer replacing one video input to opening multiple streams when only switching is needed. Coordinate the preview transition with arrival of frames from the replacement camera, not merely completion of the direction callback.
- Derive preview mirroring from viewer-relative direction. Before assigning `isVideoMirrored`, check support and disable `automaticallyAdjustsVideoMirroring`; reapply the policy when a new input creates a new connection. A rear-camera selfie may need mirroring, while a front camera facing away should not remain mirrored.
- Use `AVCaptureDevice.RotationCoordinator` for upright preview and capture, and recreate it when switching devices. Display rotation and camera direction are distinct concerns.
- Choose preview fill versus fit intentionally, using extra space for controls where useful. For dynamic aspect ratios, inspect `activeFormat.supportedDynamicAspectRatios`; an empty array means unsupported, and `dynamicAspectRatio` can be nil. Do not force a fixed crop or assume every camera supports a square format. Disable sensor-orientation compensation only after adopting the documented rotation-coordinator path and verifying support.

Validate actual camera transitions on supported hardware. Simulator layout checks cannot establish camera availability, quality, direction, or frame-rate behavior.

## Motion relative to the active view

For a level, compass, game, or other motion feature, evaluate `CMMotionManager.deviceMotionBody` and `CMBodyIdentifiable` (iOS 27.0). A conforming view associates sensor calculations with its UI/display coordinate frame; separate managers can track separate views. Preserve the default hardware-frame fallback on unsupported configurations. This is motion-feature guidance, not a replacement for size classes or reserved-region layout.
