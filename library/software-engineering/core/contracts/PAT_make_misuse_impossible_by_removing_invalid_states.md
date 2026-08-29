---
object_id: PAT_make_misuse_impossible_by_removing_invalid_states
object_type: pattern
name: Make Misuse Impossible by Removing Invalid States
library_path:
- software-engineering
- core
- contracts
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- hard_to_misuse
- factory_function
- immutability
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_hard_to_misuse
- rel: related_to
  target_object_id: PAT_prefer_null_safety_or_optionals
- rel: related_to
  target_object_id: AP_harden_a_code_contract
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Make Misuse Impossible by Removing Invalid States

## Pattern Rule
**IF** a type's or module's contract relies on callers performing a specific setup sequence or avoiding an invalid state
**THEN** redesign it so the invalid state cannot exist — return a fully-initialized instance from a static factory function, make the constructor and any state-mutating functions private, and stop exposing mutable state.

## Do
- Move setup inside a `create()` factory that performs loading and initialization and only ever hands back a valid instance, so every holder of the type is guaranteed a valid one.
- Make the constructor private to force callers through the factory, and make setup functions like `loadSettings()` and `init()` private so external code cannot drive the object into a half-built state.
- Once invalid states are gone, stop overloading return values to signal them: a `getUiColor()` that once returned null for both "no color chosen" and "not initialized" can now mean only "no color chosen."

## Don't
- Don't leave a public constructor plus public step functions that callers must invoke in a precise order — every ordering they can get wrong is a bug waiting to happen.
- Don't encode "the object might be in an invalid state" into an overloaded return value; that pushes a hidden term into small print and hides real bugs.

## Checklist
- Can external code obtain an instance that is not fully initialized? If so, close that path.
- Are all state-changing functions private or absent from the public surface?
- Does any return value carry two meanings because an invalid state is still possible?

## Notes
This is the worked fix for the `UserSettings` class whose original contract demanded `loadSettings()` then `init()` in exactly the right order and overloaded null to also mean "not set up." The redesign — static factory, private constructor, private mutators, no exposed mutable state — turns a contract full of small print into one where misuse does not compile. Long names the underlying technique as eliminating exposed state and mutability, the deep-dive subject of chapter 7, and notes signaling load failure with null is still imperfect, which chapter 4's error handling improves.
