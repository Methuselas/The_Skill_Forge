---
object_id: DRILL_signal_one_error_multiple_ways
object_type: drill
name: Signal One Error Several Ways and Compare the Tradeoffs
library_path:
- software-engineering
- core
- error-handling
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- error_handling
- result_type
- checked_exceptions
- api_design
cross_links:
- rel: teaches
  target_object_id: PAT_prefer_explicit_error_signaling_for_recoverable_errors
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: implementing and contrasting explicit and implicit error-signaling techniques
references: []
variants: []
---

# Signal One Error Several Ways and Compare the Tradeoffs

## Practice Task
Take one small function with a single error case and rewrite its signaling several ways, then compare which are explicit and what each conveys.

## Target Skill
Fluency in the error-signaling techniques and the ability to judge their tradeoffs.

## Setup
No special setup required.

## Instructions
1. Start from a function with one clear error case — the classic is a square-root function that errors on a negative input.
2. Write a version for each technique: a checked exception, an unchecked exception, a nullable return under null safety, a result type carrying an error object, and a magic value such as returning minus one.
3. For each version, also write the caller, and mark whether the caller is forced to acknowledge the error or is free to ignore it.
4. Label each technique explicit or implicit, and note what information it conveys — in particular which ones carry a reason for the failure and which do not.
5. Pick which you would ship for a recoverable error and justify it against forced awareness and error detail.

## Success Check
- All five versions are written as compiling function-and-caller pairs. Reasoning through them reproduces the table already in the reader's head and tests nothing.
- Each caller is checked by attempting to ignore the failure, with the result recorded as compiling or not. That attempt is what assigns the labels.
- Explicit and implicit are assigned from those results rather than from category, so an unchecked exception is implicit because the ignoring caller compiled, and the run says it in those terms.
- What each technique carries is stated separately from whether it compels attention, so the nullable's silence about the reason and the result type's answer to it are visible as an independent axis.
- The final choice names both axes and the case that would reverse it. A choice defended as best practice has not used the comparison it just built.

## Common Failures
- Treating an unchecked exception as explicit because it can be caught — the caller is not forced to know it exists.
- Choosing a nullable return when the caller needs the failure reason, which only a result type carries.

## Notes
This is Long's `getSquareRoot` walkthrough turned into deliberate practice. Writing the same error five ways makes the explicit/implicit distinction concrete and exposes the real axis of choice: whether the caller is forced to acknowledge the error, and whether the technique can carry why it happened. That comparison is what informs the recoverable-error signaling decision.
