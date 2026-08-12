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
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u06, pp. 163-167
  evidence_type: text
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
2. Rewrite it as a switch with an explicit case for every current value, and a throw of an unchecked exception placed after the switch, not in a default case.
3. Add a unit test that calls the function once for every value returned by the enum's values list.
4. Add a new value to the enum and confirm the test fails (and, in a language that warns on non-exhaustive switches, that the compiler warns) rather than the code silently mishandling it.
5. Handle the new value explicitly and confirm the test passes again, adding a case that asserts its intended result.

## Success Check
- Every existing enum value has an explicit branch.
- Adding a value triggers a failing test or a compiler warning, never silent behavior.
- The catch-all is a throw after the switch, preserving the exhaustiveness warning.

## Common Failures
- Using a value-returning default case, which silently absorbs new values.
- Putting the throw inside a default case, which makes the compiler think the switch is exhaustive and suppresses its warning.

## Notes
This drills the `PredictedOutcome` example, whose `WORLD_WILL_END` value would slip through an if-chain as "safe." The point is defense in depth: the exhaustive switch plus an all-values test plus, where available, the compiler's warning together guarantee that a future enum value cannot be handled by accident.
