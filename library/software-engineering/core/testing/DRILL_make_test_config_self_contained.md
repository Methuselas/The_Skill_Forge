---
object_id: DRILL_make_test_config_self_contained
object_type: drill
name: Move Outcome-Affecting Setup Out of Shared Config
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
- refactoring
cross_links:
- rel: teaches
  target_object_id: PAT_use_shared_test_setup_carefully
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: relocating outcome-affecting values from shared setup into each test case via helpers
references: []
variants: []
---

# Move Outcome-Affecting Setup Out of Shared Config

## Practice Task
Take tests whose outcomes depend on a shared configuration object, move the outcome-affecting values into each case, and show a later edit no longer silently breaks a case.

## Target Skill
Distinguishing outcome-affecting setup from irrelevant setup and keeping the former local to each case.

## Setup
No special setup required.

## Instructions
1. Start from tests that share a configured object in a before-each block or constant — an order with exactly three items — where a case relies on that specific value.
2. Simulate the hazard: add a fourth item to the shared object (as a new case might) and observe that the "three items" case now silently tests four.
3. Write a helper function that builds the object with case-specific values, and have each case call it with the values that case depends on.
4. Move any genuinely irrelevant-but-required data (metadata the code ignores) into a shared constant of an immutable type.
5. Confirm each case now sets up its own outcome-affecting values and that editing one case cannot alter another.

## Success Check
- The hazard is reproduced by actually adding the fourth item and running the suite, with the now-silently-passing case named. An account of how the shared object could drift describes the condition being removed, not evidence that it was present.
- Every value affecting an outcome is set inside the case depending on it, checked by reading each case alone and asking whether its expected result follows from what that case sets up.
- The shared remainder is justified item by item as irrelevant to every outcome, and its immutability is carried by the type rather than by an agreement not to touch it.
- One case is edited in a way that would previously have weakened another, and the other is shown still passing. This is the property the drill exists for and the one most easily assumed.
- The cost is stated — a builder called per case, more lines in each test — because a run concluding only that sharing is bad has not weighed what the sharing was buying.

## Common Failures
- Replacing a shared before-each with a shared constant that still holds outcome-affecting values.
- Sharing a mutable object across cases so they interfere.

## Notes
This drills Long's postage-label example, where a shared three-item order became four and gutted the large-package case. The habit is to keep anything a test's result depends on inside that test — helper functions remove the boilerplate — and to share only what no case's outcome depends on.
