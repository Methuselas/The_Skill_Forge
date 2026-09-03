---
object_id: DRILL_convert_enum_if_chain_to_exhaustive_switch
object_type: drill
name: Convert an Enum If-Chain to an Exhaustive Switch With a Test
library_path:
- software-engineering
- core
- avoiding-surprises
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- enums
- avoid_surprises
- exhaustive_switch
- testing
cross_links:
- rel: teaches
  target_object_id: PAT_handle_enums_exhaustively
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: making enum handling robust to future values via exhaustive switch and an all-values test
references: []
variants: []
---

# Convert an Enum If-Chain to an Exhaustive Switch With a Test

## Practice Task
Take code that handles an enum with an if-statement, convert it to handle every value explicitly and fail loudly on an unhandled one, then prove a new value is caught.

## Target Skill
Making enum handling robust to future values with an exhaustive switch and an all-values test.

## Setup
No special setup required.

## Instructions
1. Start from a function that special-cases one enum value and implicitly treats the rest — for example returning false for `COMPANY_WILL_GO_BUST` and true otherwise.
2. Take the list of values from the enum's own declaration, and write down that this is where the list came from.
3. Rewrite the function as a switch with an explicit case for every value on that list, and a throw of an unchecked exception placed after the switch, not in a default case. State the reason for putting it after the switch.
4. Add a unit test that calls the function once for every value returned by the enum's values list.
5. Add a new value to the enum, run the test, and record the failure (and, in a language that warns on non-exhaustive switches, the compiler's warning).
6. Handle the new value explicitly, adding a case that asserts its intended result, and state that result's reason. Run the test again and confirm it passes.

## Success Check
- Every current value has its own branch, and the list of values came from the enum's declaration rather than from the branches already written. Enumerating from what the code handles today reproduces the original omission exactly.
- The new value is actually added and the test actually run, with the failure recorded. That the test would fail is the property under examination and cannot also be the evidence for it.
- The catch-all is a throw after the switch and not a default case, and the reason is stated: a default case satisfies the compiler, which switches off the exhaustiveness warning this whole exercise was arranging to receive.
- The test iterates the enum's value list rather than naming values individually. A test with one case per value passes today and quietly stops covering the enum the moment somebody extends it, which is the failure being drilled.
- The new value's intended result is stated with its reason. A branch added to turn the test green, returning whatever the neighbouring case returned, satisfies every bullet above and has handled nothing.

## Common Failures
- Using a value-returning default case, which silently absorbs new values.
- Putting the throw inside a default case, which makes the compiler think the switch is exhaustive and suppresses its warning.

## Notes
This drills the `PredictedOutcome` example, whose `WORLD_WILL_END` value would slip through an if-chain as "safe." The point is defense in depth: the exhaustive switch plus an all-values test plus, where available, the compiler's warning together guarantee that a future enum value cannot be handled by accident.
