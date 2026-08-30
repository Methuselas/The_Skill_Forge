---
object_id: DRILL_replace_magic_value_with_explicit_absence
object_type: drill
name: Replace a Magic Return Value With Explicit Absence
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
- magic_values
- avoid_surprises
- refactoring
- null_safety
cross_links:
- rel: teaches
  target_object_id: PAT_avoid_returning_magic_values
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: converting in-band magic return values to explicit nullable, optional, or error signals
references: []
variants: []
---

# Replace a Magic Return Value With Explicit Absence

## Practice Task
Take a function that returns a magic value for an absent or uncalculable result, convert it to signal absence explicitly, and watch a caller bug surface.

## Target Skill
Spotting in-band magic values and replacing them with a nullable, optional, or error signal.

## Setup
No special setup required.

## Instructions
1. Start from a function that returns a sentinel — a `getAge()` returning `-1` for a missing age, or a `minValue()` returning `Int.MAX_VALUE` for an empty list.
2. Write a caller that assumes a real value always comes back — sum ages into a mean, or pick the level with the highest minimum score.
3. Trace what the caller does when the magic value flows through, and name the resulting bug (a wrong mean, an unplayed level ranked easiest).
4. Change the function's return type to nullable or optional (or an error type if the reason matters) so absence is in the contract.
5. Fix the now-failing caller so it compiles, handling the absent case explicitly.

## Success Check
- The bug is produced by running the caller, with the wrong output recorded — the actual mean, the level actually chosen. Naming the bug in the abstract is exactly what the sentinel already permitted.
- The original caller fails to compile after the change and the compiler's message is recorded. If it still compiles, absence went into a comment or into a construct the language does not enforce, and the exercise has not happened.
- The corrected caller is run against the absent case and its output checked against a result worked out by hand. Handling absence and producing a different wrong answer passes every other bullet here.
- The fix is checked against the disguise it most readily becomes: absence must not be re-encoded as another in-band value, and the run states which representation was chosen and why it is out of band.
- Whether the caller needs the reason for the absence is decided and stated, rather than settled by whichever return type was easier to write.

## Common Failures
- Swapping one magic value for another (returning `0` or an empty list) instead of making absence explicit.
- Making the return nullable but casting away the null in the caller without really handling it.

## Notes
This drills Long's `getMeanAge` and maximin examples, whose point is that the magic value produces a plausible wrong answer that tests miss. The habit is to distrust any return type that has no room to say "no value," and to let the compiler force every caller to face absence.
