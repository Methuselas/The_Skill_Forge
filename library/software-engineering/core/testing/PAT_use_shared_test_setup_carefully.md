---
object_id: PAT_use_shared_test_setup_carefully
object_type: pattern
name: Keep Outcome-Affecting Setup Inside Each Test Case
library_path:
- software-engineering
- core
- testing
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- unit_testing
- shared_state
- test_setup
- determinism
cross_links:
- rel: related_to
  target_object_id: PAT_avoid_global_state_inject_shared_state
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Keep Outcome-Affecting Setup Inside Each Test Case

## Pattern Rule
**IF** a value or state affects the outcome of a test case
**THEN** set it up inside that case rather than in shared setup, reserving shared setup for things that are required but irrelevant to any case's outcome.

## Do
- Put the values a case depends on in the case itself, using a helper function to build them so you avoid repetition without sharing — a case that needs an order of exactly three items should construct that order via a helper, not rely on a shared one.
- Reset shared state between cases when sharing is unavoidable: if a slow, expensive dependency like a database must be shared, clear it in an after-each block so one case's writes cannot leak into the next.
- Share only outcome-irrelevant configuration — required-but-ignored metadata an object cannot be built without — as a shared constant, ideally of an immutable type so no mutable state is shared.

## Don't
- Don't set outcome-affecting values in shared setup; when another engineer adds a fourth (hazardous) item to a shared order, the "exactly three items" case silently starts testing four and no longer protects the behavior.
- Don't share mutable state across cases without resetting it; a shared database instance makes cases interfere and become ineffective.

## Checklist
- Does any case's result depend on a value defined in shared setup?
- If state is shared for cost reasons, is it reset before each case?
- Is the shared configuration truly irrelevant to every case's outcome?

## Notes
Shared setup is double-edged: it cuts repetition but can quietly break tests. Long's postage-label example shows the trap — a shared three-item order that a later edit turns into four items, silently gutting the large-package case. The fix is to keep outcome-affecting setup local (helper functions tame the boilerplate) and reserve shared constants for required-but-irrelevant data like order metadata. He notes that needing lots of irrelevant setup can itself signal unfocused parameters, echoing the focused-parameters rule; shared mutable state carries the same hazards as global state.
