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
Work on a stated artifact: a state object holding several separately-written locations — a bank of per-worker counters and a summary record — read by a collector that sweeps all of them twice; and, elsewhere in the same design, one conditional update that compares a value to decide whether to commit. Steps 1 through 5 work on the collector, step 6 on the conditional update.

Three quantities decide every number below, and none of them is craft — they are measurements about a target machine. Declare each before step 3 and say where it came from: the write rate per location, because wrap is a function of writes elapsed rather than time elapsed; the bound on how long a participant may be delayed between its two passes, which differs by two orders of magnitude between a scheduling quantum and a page-fault storm; and whether one value fits in a single atomic word.

## Instructions
1. Construct a schedule in which the values match across both passes and the collected view never existed. The writes must be interleaved into the collector's reads: change a location the collector has already read in pass 1 and restore it before pass 2 reaches it, while changing a second location pass 1 has not yet reached. A schedule whose writes all land in the gap between the two passes falsifies nothing — pass 1 collected during a quiet interval, so its view did hold and is merely stale, which is exactly what a double collect promises.
2. Add a counter to each location that advances when the location is written, and change the validation to compare counters rather than values. How far it advances per write is settled in step 4; carry that number back into step 3 rather than assuming one.
3. Decide how wide that counter must be. The width follows from the three declared numbers — write rate per location, the delay bound between a participant's two passes, and the per-write increment from step 4 — and the derivation is writes-elapsed arithmetic, not a judgement about size. Show the derivation, and name and reject a width that would wrap inside that bound; where the correct width is a single alternating bit and no smaller width exists to reject, argue that impossibility instead.
4. Decide first whether one value exceeds a single atomic word. If it does, a write takes several steps: advance the counter before starting and again after finishing, and treat a pass that observes the in-progress state as a failed pass. If every location is one naturally-atomic word, say so and say why a partly-completed write cannot be observed here.
5. Decide what a collector does when it keeps failing — a bounded number of attempts, then a fallback or a report that no consistent view was available. Returning the unvalidated view after the last attempt is not a defined outcome; it is the original bug with a retry count in front of it.
6. State what happens where no delay bound exists at all — a paused process, a stopped debugger — and answer it with a named mechanism rather than a wider counter.
7. Run the step-1 schedule through the new validation and confirm it is rejected, then run a schedule whose writes all fall in the gap between the passes and confirm it is accepted. Where you instead restructured the several locations into one immutable object behind a single atomic handle, show that the step-1 schedule cannot be expressed against that design at all.
8. Apply the same reasoning to the conditional update, where a recycled address makes an unchanged comparison a lie.

## Success Check
- The schedule from step 1 is rejected by the validation, and a schedule whose writes all fall in the gap between the passes is accepted — a validator that reports no consistent view every time has not been distinguished from one that works. If the remedy taken was instead to restructure the several locations into one immutable object behind a single atomic handle, this bullet is met by showing that the step-1 schedule cannot be expressed against that design at all; that is the stronger answer, not an omission.
- The counter's width is derived from the declared delay bound and write rate, and the derivation is shown. A width that would wrap inside that bound is named and rejected — or, where the correct width is a single alternating bit and no smaller width exists to reject, that impossibility is argued.
- What happens when no such bound exists — a paused process, a stopped debugger — is stated, and the answer is a named mechanism rather than a wider counter. Observing that no fixed width is safe restates the premise and does not satisfy this.
- A partly-completed write is detectable rather than collectable — or every location is a single atomic word and the case is shown not to arise.
- Repeated failure has a defined outcome that is neither an unbounded retry nor a return of the unvalidated view — or the collector cannot fail repeatedly by construction, and that is argued.

## Common Failures
- Comparing values because it needs no extra storage and passes every test where values happen not to repeat.
- Sizing the counter by what seems large rather than by the maximum delay the protocol permits.
- Advancing the counter only after a write completes, leaving the intermediate state indistinguishable from a stable one.
- Fixing the collection and leaving an identically-shaped conditional update elsewhere unprotected.

## Notes
This is one failure wearing three costumes: a recycled address defeating a conditional update, equal values defeating a double collection, and a reset object letting a fast participant lap a slow one. The remedy is the same each time — make consecutive states distinguishable rather than restoring a previous one — and recognizing the shape is worth more than any of the three fixes.
