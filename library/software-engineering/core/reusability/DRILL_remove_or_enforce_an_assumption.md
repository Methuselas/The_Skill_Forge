---
object_id: DRILL_remove_or_enforce_an_assumption
object_type: drill
name: Remove an Unnecessary Assumption or Enforce a Necessary One
library_path:
- software-engineering
- core
- reusability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- assumptions
- reusability
- checks
- refactoring
cross_links:
- rel: teaches
  target_object_id: PAT_beware_assumptions_avoid_or_enforce
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: deciding whether to remove or enforce a baked-in assumption and doing so
references: []
variants: []
---

# Remove an Unnecessary Assumption or Enforce a Necessary One

## Practice Task
Take code with an unenforced assumption, decide whether to remove or enforce it, and apply the fix — naming it so callers opt in when the assumption stays.

## Target Skill
Judging whether a baked-in assumption is necessary, and either generalizing past it or enforcing and naming it.

## Setup
No special setup required.

## Instructions
1. Start from code with an assumption mentioned only in a comment — an image lookup that assumes an article has at most one image section.
2. Write the general version that drops the assumption (return images from all sections) and note the cost (a few extra iterations) versus the reuse benefit.
3. Now suppose a specific caller genuinely needs the single-section assumption; enforce it with an assertion or check so a violation fails fast.
4. Rename the function to advertise the assumption (getOnlyImageSection) so callers who do not want it steer clear.
5. Decide the enforcement by data source: assertion for internally generated data, an explicit error signal for user- or externally supplied data.

## Success Check
- Both versions exist as written code rather than one version and a description of the other, and the general one is demonstrated on an input the assumption excluded.
- The cost of dropping the assumption is stated as a quantity — extra iterations, an added allocation, one more parameter — and not as small or negligible. The trade this drill teaches cannot be made with one side unpriced.
- The enforcing version carries the assumption in its own identifier, tested by reading a call site cold: someone who has not seen the body can say what the function refuses to accept.
- The enforcement is chosen from where this function's data actually comes from, and that origin is stated for the case in hand. Reciting the rule about internal versus external data without applying it here satisfies the letter and demonstrates nothing.
- One case is written down where the choice would flip — the same function fed from the other kind of source — along with the enforcement it would take instead.

## Common Failures
- Leaving the assumption in a comment where reusing callers never see it.
- Asserting on externally supplied data that a caller would reasonably want to recover from.

## Notes
This drills Long's article example across both branches — remove the assumption when it only saves a little work, enforce and name it when a use case truly requires it. The discriminator for enforcement is recoverability: a programming error deserves an assertion, external input deserves an explicit signal.
