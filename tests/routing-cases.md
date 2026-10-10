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
| Prepare an existing iOS 26-target app built with SDK 27.0 for Duo | Duo overview and audit/validation; affected layout or bars only | Confuse build SDK with deployment target, require a target upgrade, or claim the 27.1 APIs compile on 27.0 | Source locations, container geometry, build/runtime distinction, retained fallback |
| Keep a custom control clear of a Duo fold in RTL | Duo overview and layout | Use singular query names, treat inactive regions as active obstacles, or mirror region geometry twice | Current declarations, region frame/margins/active state, RTL interaction |
| Add a navigational sidebar with a player/transcript arrangement in its detail | Duo overview and layout | Reject the requested composition solely because Apple advises avoiding nesting, or promise it works without checking | Explain the source tension; evaluate navigation ownership, usable bounds, and access to both content regions |
| Make an ARKit session show subject-facing accessory content | Duo overview and scenes/camera | Follow the superseded negative reply, open a competing capture session, or promise two full AR experiences | Later staff correction, runtime availability, hardware result |
| Test capture through Device Hub physical-device interaction | Duo audit/validation and scenes/camera | Claim camera evidence from a mode that prevents camera/microphone access | Direct hardware capture interaction, separate preview/layout evidence |
| Confirm a destructive action reached through toolbar overflow | Duo overview and bars | Invent a SwiftUI overflow-button anchor or attach state to a disappearing menu item | Persistent presentation state and observed dialog behavior |
| Audit Duo using Xcode's exported resizability skill | Duo audit/validation | Install exported material automatically or claim the skill exists without inspecting the inventory | Installed Xcode version, export inventory, remaining manual review |
| Change one control in an existing iOS 16 app | relevant SwiftUI pattern | Upgrade Observation or deployment target without need | Original target compiles |
| Migrate a SwiftData model | project rules and official documentation | Claim a built-in SwiftData module exists | Explicit scope and actual method |
| Build a branded custom control that native components cannot express | UI, design, controls, and accessibility as relevant | Reject the design for differing from system defaults or add an approval step solely for that difference | Implement a suitable alternative and inspect the relevant interaction and assistive behavior |
| Add a deliberate pose-specific editing experience | Duo overview and relevant layout or scene guidance | Treat consistent features across poses as a ban on the requested experience | Useful fallback or continuation route, state behavior, and the intended pose interaction |
| Use UIKit bridging or an approach not covered by the package to complete a feature | Relevant guidance plus project rules and actual framework documentation | Treat missing module coverage as a reason to stop or insist on pure SwiftUI | An approach that serves the requested behavior, with actual availability and appropriate checks |
| Add package-localized text to an iOS 16 app using Xcode 27 | SwiftUI localization and affected control | Migrate existing localization resources, assume generated symbols, or use an iOS 26-only resource initializer | Owning bundle, preserved extraction convention, and label-closure fallback |
| Simplify a custom binding that saves on every setter call | State ownership | Substitute onChange without accounting for equal writes or programmatic changes | Retained side-effect contract or a justified different trigger |
| Add item alerts and dynamic toolbar entries to an older supported target | Navigation, controls, API guidance | Gate compiler-back-deployed capabilities as iOS 27-only or assume the old SDK declares them | Actual SDK, per-overload minimums, and retained target |
| Diagnose repeated updates from a nested value in an observable model | Performance and deep review when warranted | Split every observable model, use fixed field-count thresholds, or claim a getter narrows underlying dependencies | Specific dependency, reproduction, and before/after cost with preserved behavior |
| Add reordering to an iOS 27 scroll-based collection | Controls and state ownership | Assume SwiftUI persists moves, confuse internal reordering with external transfer, or omit the swipe container | Model updates, stable IDs, appropriate older-system fallback, and actual interaction evidence |
| Modernize an app with Xcode 27.0 after reading newer toolbar documentation | API and controls | Recommend toolbar hidden for iOS without checking SDK declarations or refuse conditional construction | Source/SDK distinction and a supported implementation |

Static validation proves only internal closure, attribution, a single entry point, English content, and packaging. CI does not run these Swift project scenarios.
