---
object_id: PAT_handle_enums_exhaustively
object_type: pattern
name: Handle Enums Exhaustively So New Values Fail Loudly
library_path:
- software-engineering
- core
- avoiding-surprises
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- enums
- avoid_surprises
- exhaustive_switch
- fail_fast
cross_links:
- rel: related_to
  target_object_id: PAT_make_breakage_fail_compile_or_test
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
- rel: related_to
  target_object_id: AP_shape_a_multi_way_decision
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Handle Enums Exhaustively So New Values Fail Loudly

## Pattern Rule
**IF** your code branches on an enum whose set of values may grow over time
**THEN** handle every known value explicitly and arrange for an unhandled value to fail loudly — an exhaustive switch that throws after itself — rather than letting a new value be handled implicitly.

## Do
- Replace an if-statement that handles some values and implicitly assumes the rest: an `isOutcomeSafe` that only special-cases `COMPANY_WILL_GO_BUST` silently rules a future `WORLD_WILL_END` "safe."
- Make an unhandled value a fail-fast programming error: throw an unchecked exception after the switch, and back it with a unit test that calls the function for every enum value.
- Put the throw after the switch, not in a `default` case, so the compiler's exhaustiveness warning still fires as a second layer of protection.

## Don't
- Don't add a `default` case that returns a value; it silently absorbs new enum values — defaulting a new `COMPANY_WILL_AVOID_LAWSUIT` to "not safe" is just a different wrong answer.
- Don't assume the engineer adding an enum value will find your switch; it may be in another file, package, or team, so rely on the compiler or a test to force the update.

## Checklist
- Does every current enum value have an explicit branch?
- Will a newly added value cause a compile warning or a failing test rather than silent behavior?
- Is the catch-all a throw after the switch rather than a value-returning default?

## Notes
This flips the chapter's frame: the surprise now comes from a brittle assumption about code you depend on — that an enum will not gain values. Long's exhaustive-switch-plus-test makes a new value fail at compile time or in tests, the two reliable signals from chapter 3, and he is precise that a value-returning `default` reintroduces implicit handling while an exception in the default even suppresses the compiler's exhaustiveness warning. The caveat: for an enum owned by another project that may add values without warning, you may have to handle new values more permissively and use judgment.
