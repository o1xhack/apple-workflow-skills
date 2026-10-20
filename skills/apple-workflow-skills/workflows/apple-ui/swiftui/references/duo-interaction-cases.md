# Duo Interaction Cases

Read only for editing continuity or presentation lifetime failures, via [Duo Validation](duo-validation.md), [Duo Layout](duo-layout.md), or [Duo Bars](duo-bars.md). These cases generalize a hybrid UIKit/SwiftUI app's local implementation and Simulator records. They illustrate diagnosis and acceptance criteria, not universal fixes or hardware certification. Framework declarations are in [External Reading](duo-sources.md).

## Editing survives, but typing does not

**Symptom:** A search query survives opening and closing the device, but the user must tap the field again to continue. A long editor may retain focus while its caret disappears behind the keyboard.

Treat these as separate outcomes:

| Outcome | Check |
| --- | --- |
| Draft/query retained | Read the actual text after the transition |
| Focus retained or appropriately restored | Check the intended field's focus/responder and continue without tapping it again |
| Software keyboard visible | Inspect the actual keyboard in software-keyboard mode; a hardware keyboard changes this expectation |
| Caret/selection visible | Inspect the insertion point, including the end of a long draft above the keyboard |
| Input still works | Enter or delete a distinctive character through the intended input path and read back the change |

Use the sequence: **type -> open -> partially fold -> close -> continue typing -> explicitly dismiss editing -> fold again**. Check text, focus, keyboard, caret, and typing at the relevant transitions. After explicit dismissal, the next fold must respect that decision. Also test leaving the page, covering it with another presentation, and scene deactivation if the implementation schedules focus recovery. A final screenshot alone does not verify intermediate continuity.

First inspect view identity and state ownership. Keep the draft, selection identity, and navigation above pose-dependent branches where necessary. Avoid recreating the editor merely to update width, and avoid ambiguous focus bindings. Inspect the actual content viewport too: a system presentation can reflow usable content without changing the outer window width.

If the system already preserves editing, keep that behavior. If reliable observation establishes a recovery gap, a scene-local recovery task can preserve genuine editing intent through reflow. Coalesce relevant layout events, target the same visible editor in the same active scene/window, and invalidate stale callbacks before they apply. Cancel pending work and clear recovery intent on explicit close/dismiss, leaving the page, covering presentation, and scene inactivity; returning to an active scene alone must not revive cancelled intent. A generation/token guard can prevent an already queued callback from stealing focus. The case's delay and UIKit bridge are implementation choices, not required constants or dependencies.

Restoring focus and revealing the caret are different repairs. Recheck scrolling/selection after reflow without resetting the draft or jumping unrelated reading content. Exercise short and long text when caret visibility is affected; add accessibility-size checks when text reflow changes the failure.

## Date, menu, and confirmation lifetimes

**Symptoms:** A compact date editor closes during expansion; a list confirmation describes the correct item but points at a header or another row.

Separate three responsibilities:

- **Page/session state:** owns the draft and selected date/value across temporary control changes. Dismissing a picker must follow the page's commit/cancel contract rather than accidentally submitting the form.
- **Operation identity:** identifies the intended record with a stable ID. Resolve and validate that ID when acting; a row index, label, or recycled cell is insufficient. Distinguish repeated requests so a stale dismissal cannot clear a newer request.
- **Presentation source:** comes from the actual triggering control or visible row for source-anchored UI. Persistent state alone does not establish the correct anchor. Full-page sheets and ordinary alerts retain their own presentation semantics.

Try system controls first, then verify the actual transition. For a date editor, open it, select a value, open/partially fold/close, change the value again, and finish or cancel. Confirm whether the presentation stays usable, where it appears, which value returns to the form, and whether cancellation leaves stored data unchanged. A page-owned system sheet is one alternative when a compact picker cannot support the required continuity; it is not a universal replacement for compact pickers.

For a menu or confirmation, test another row with similar content, a scrolled row, and the edit control if it is a separate trigger. Check both the described object and the visual source. For UIKit popovers, `sourceRect` is in `sourceView` coordinates; convert from the actual visible source when necessary. Revalidate source visibility, window membership, and record identity when layout or list contents change. If the source is removed, hidden, recycled for another record, or otherwise invalid, cancel the source-anchored request rather than inventing a page-center anchor. A still-valid source may be repositioned using supported presentation behavior.

Keep presentation work bounded to the affected source; this case does not require scanning every row each frame. If a bridge is needed, retain its callback/delegate for the presentation's lifetime and invalidate it on dismissal. Verify ordinary-device behavior after changing shared presentation code. Compilation and a visible dialog do not prove correct anchoring or action identity.
