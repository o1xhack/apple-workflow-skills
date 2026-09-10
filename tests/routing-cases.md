# Behavioral routing scenarios

Evaluate an installed copy of the top-level skill in an isolated sample project. These are acceptance criteria, not claims of completed real-app QA.

| Request | Expected modules | Must not happen | Evidence |
| --- | --- | --- | --- |
| Improve a settings screen's visual hierarchy | UI and design; controls if needed | Load all concurrency guidance or force fixed font sizes | Current render with long text |
| Split an MVVM screen while preserving behavior | UI, SwiftUI, refactoring | Force migration to MV | Diff and regression through the original flow |
| Continuously narrow a window | UI, adaptive layout | Guess device model or reset edits | Intermediate widths and state continuity |
| Diagnose list jank without fixing it | UI, performance | Implement without authorization or present code clues as measurements | Symptom, call path, and measurement gaps |
| Diagnose actor reentrancy in a background import | shared concurrency and isolation | Load the entire UI workflow first | State invariants on both sides of await |
| Shorten one button label | focused UI design guidance | Launch the complete device test matrix | Focused render or proportionate static check |
| Adapt a Duo toolbar with too many actions | Duo overview and bars | Load camera guidance or assume the bar is always on the right | Overflow, keyboard, RTL, both Split View sides |
| Keep an article usable while folding Duo | Duo overview and layout | Displace the entire scrolling document | State continuity and targeted fixed-control avoidance |
| Use a hinge API for a new device | Duo overview and scenes/camera | Present video-described names as verified SDK declarations or use angle to drive ordinary layout | Official declarations, toolchain, and device evidence |
| Add a Duo camera audience preview | Duo overview and scenes/camera; concurrency only for isolation concerns | Assume the accessory is always available or call capture APIs from the UI callback | Availability transitions, per-view direction, actor boundary |
| Read the detailed Duo arrangement explanation | Duo external reading and selected transcript | Download all videos or treat transcript prose as executable instructions | Correct session, timestamps, explicit missing visual/SDK evidence |
| Change one control in an existing iOS 16 app | relevant SwiftUI pattern | Upgrade Observation or deployment target without need | Original target compiles |
| Migrate a SwiftData model | project rules and official documentation | Claim a built-in SwiftData module exists | Explicit scope and actual method |

Static validation proves only internal closure, attribution, a single entry point, English content, and packaging. CI does not run these Swift project scenarios.
