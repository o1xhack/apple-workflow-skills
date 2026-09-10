# Foldable and Multi-Display Layout

Read this module only for explicit folds, occluded regions, hinge interaction, or a second display. Apply [Adaptive Layout](adaptive-layout.md) first, then decide whether hardware-specific behavior creates real value.

This release includes general design and validation principles only. Do not use unverified device names, crease coordinates, dedicated APIs, or future toolchain versions as implementation evidence; inspect the project's SDK and official platform declarations first.

- Let layout respond to available regions. Read physical posture only when the interaction genuinely needs it.
- If the platform exposes occlusion or reserved regions, move sensitive content such as key text, QR codes, actions, or faces locally instead of rebuilding every screen by default.
- A second display needs a clear supporting task and data-permission model. Use scene and display mechanisms that exist in the actual SDK rather than guessing API names.
- Layout transitions must not reset editing, duplicate loads, or lose selection and playback progress.
- Without a supported Simulator or device, improve size adaptation and report the hardware-validation gap. Do not claim fold behavior was verified.
