---
object_id: PAT_keep_a_spare_before_releasing_capacity
object_type: pattern
name: Keep a Spare Before Releasing Capacity
library_path:
- software-engineering
- core
- performance
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- pooling
- hysteresis
- resource_management
- thrashing
cross_links:
- rel: related_to
  target_object_id: PAT_name_the_allocation_pattern_before_choosing_a_strategy
- rel: related_to
  target_object_id: PAT_hoist_allocation_out_of_the_work
- rel: related_to
  target_object_id: PAT_choose_lazy_or_eager_by_how_often_the_result_is_needed
- rel: related_to
  target_object_id: AP_build_a_pool_for_a_hot_allocation
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Keep a Spare Before Releasing Capacity

## Pattern Rule
**IF** something grows by acquiring an expensive unit and shrinks by releasing one — a pool of memory, of connections, of threads, of buffers — and you are deciding when it should release
**THEN** require more than one idle unit before releasing any, so that a workload sitting exactly on the boundary cannot make every single cycle pay for an acquisition and a release.
**ELSE** where holding even one spare is unacceptable, make the release explicit and scheduled rather than a consequence of the count reaching zero.

## Do
- Separate the two thresholds. Grow when there is nothing free, and shrink only when at least two are free, so the point at which you release is not the point at which you would next acquire.
- Release the unit that is cheapest to give up rather than the one that happened to empty. Where the units live in a sequence, move the empty one to the end and release from there, so releasing never costs a shuffle of the rest.
- Pick the gap from what an acquisition costs. One spare is enough where acquiring is merely slow; a larger reserve earns its keep where acquiring can also block, fail, or contend.
- Watch the acquire and release counts, not just the current size. A count of acquisitions far exceeding the peak size is the signature this exists to prevent, and it is invisible in a size graph.

## Don't
- Don't release as soon as the last user is done. That is the arrangement where a loop creating and destroying one object at a time pays a full acquisition and a full release on every iteration, while the pool's size graph sits flat at zero and looks perfectly healthy.
- Don't treat this as a memory-only concern. Connection pools, thread pools, and buffer caches thrash the same way and cost more per cycle, since their acquisition can involve another machine.
- Don't set the reserve so high that the pool never gives anything back. The point is a gap between the two thresholds, not a floor that ratchets up and holds the peak forever.
- Don't expect this to fix every case. A workload that swings by more than the reserve on each pass defeats it, and the answer there is to stop the swing at its source rather than widen the gap indefinitely.

## Checklist
- Are the grow and shrink thresholds the same number, and if so why?
- What does a loop that uses exactly one unit per pass cost — one acquisition, or one per iteration?
- Is releasing cheap regardless of which unit went idle?
- Does anything record how many acquisitions happened, or only how large the pool got?

## Notes
The failure is a boundary effect, and boundary effects are easy to miss because the steady state on either side of the boundary is fine. A pool holding several units in use never releases, and a pool holding none never acquires; the expensive case is the one sitting exactly at the transition, where a single unit is repeatedly taken and given back and the pool obligingly acquires and releases around it.

Naming it as two thresholds rather than one is what makes the fix small. The condition to grow and the condition to shrink are separate decisions that happen to have been written as one comparison, and separating them by a single unit is enough to break the cycle, because the workload must now swing by two before it can make the pool move at all.

It is worth checking the acquisition counter rather than the size, because this shows up nowhere else. The pool's size is correct at every instant, its contents are correct, no resource leaks, and the program is simply slower than it should be for reasons the obvious instrumentation reports as healthy.
