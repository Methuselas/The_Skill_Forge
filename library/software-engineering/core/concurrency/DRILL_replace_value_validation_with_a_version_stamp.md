---
object_id: DRILL_replace_value_validation_with_a_version_stamp
object_type: drill
name: Replace Value Comparison With a Version Stamp
target_skill: Distinguishing unchanged from changed-back when validating an optimistic read
library_path:
- software-engineering
- core
- concurrency
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- lock_free
- consistency
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_take_a_consistent_view_by_collecting_twice
- rel: related_to
  target_object_id: PAT_keep_memory_alive_until_the_compare_and_swap_completes
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Replace Value Comparison With a Version Stamp

## Practice Task
Take a routine that reads several locations, reads them again, and accepts the result because the two passes returned equal values — and convert it to one that can tell "nothing happened" from "something happened and was undone."

## Target Skill
Distinguishing unchanged from changed-back when validating an optimistic read.

## Setup
No special setup required.

## Instructions
1. Construct a schedule in which the values match across both passes and the collected view never existed. A location written and written back between the passes is the shortest one; a location written twice to the same value is another.
2. Add a counter to each location that advances on every write, and change the validation to compare counters rather than values.
3. Decide how wide that counter must be, in terms of the longest interval any participant could be delayed between its two passes. State the assumption rather than picking a size.
4. Handle a write that takes several steps: advance the counter before starting and again after finishing, and treat a pass that observes the in-progress state as a failed pass.
5. Decide what a collector does when it keeps failing — a bounded number of attempts, then a fallback or a report that no consistent view was available.
6. Apply the same reasoning to a conditional update elsewhere in the design, where a recycled address makes an unchanged comparison a lie.

## Success Check
- The schedule from step 1 is now rejected by the validation.
- The counter cannot repeat a value within one collection under the stated assumption.
- A partly-completed write is detectable rather than collectable.
- Repeated failure has a defined outcome that is not an unbounded retry.

## Common Failures
- Comparing values because it needs no extra storage and passes every test where values happen not to repeat.
- Sizing the counter by what seems large rather than by the maximum delay the protocol permits.
- Advancing the counter only after a write completes, leaving the intermediate state indistinguishable from a stable one.
- Fixing the collection and leaving an identically-shaped conditional update elsewhere unprotected.

## Notes
This is one failure wearing three costumes: a recycled address defeating a conditional update, equal values defeating a double collection, and a reset object letting a fast participant lap a slow one. The remedy is the same each time — make consecutive states distinguishable rather than restoring a previous one — and recognizing the shape is worth more than any of the three fixes.
