# Liquid Glass

Read this module only when the request or design explicitly uses glass materials. Prefer native controls and system glass APIs, checking availability against the target platform and SDK.

- Use native glass button styles. Adjust shape at the button-style boundary instead of stacking blur, stroke, and shadow on the label to imitate system glass.
- Complete sizing, padding, and typography before applying a glass effect to a custom surface. Add interactive effects only to actionable surfaces.
- Use `GlassEffectContainer` when neighboring glass elements need to merge or morph. Container spacing and content-layout spacing serve different purposes.
- Give morphing elements stable identities and a namespace. Test appearance, removal, rapid repeated actions, and Reduce Motion.
- System toolbars may already provide shared material. Avoid duplicate layers, and apply toolbar-background modifiers to the API level declared by the SDK.
- Prefer system safe-area mechanisms for fixed action bars. Select concrete bar APIs by verified availability instead of copying an unverified signature.
- Many glass surfaces inside scrolling content can weaken hierarchy and add rendering cost. Prefer glass for controls and navigation unless measured requirements justify otherwise.
- Do not hard-code a claim that system glass buttons have fixed internal padding; their size varies with control size, platform, and content.
- A fallback on older systems is a compatible alternative appearance, not the same optical effect.

Inspect light and dark backgrounds, text contrast, hit targets, merging, and scrolling behavior through [UI Validation](../validation/index.md).
