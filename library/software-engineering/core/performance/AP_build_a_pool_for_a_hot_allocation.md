---
object_id: AP_build_a_pool_for_a_hot_allocation
object_type: ap
name: Build a Pool for a Hot Allocation
library_path:
- software-engineering
- core
- performance
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- pooling
- allocation
- resource_management
- tuning
cross_links:
- rel: supports
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: supports
  target_object_id: PAT_hoist_allocation_out_of_the_work
- rel: supports
  target_object_id: PAT_name_the_allocation_pattern_before_choosing_a_strategy
- rel: supports
  target_object_id: PAT_keep_a_spare_before_releasing_capacity
- rel: supports
  target_object_id: PAT_check_the_last_used_slot_before_searching
- rel: related_to
  target_object_id: AP_tune_a_measured_bottleneck
- rel: related_to
  target_object_id: PAT_reproduce_the_real_context_before_believing_a_microbenchmark
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Build a Pool for a Hot Allocation

## Objective
Replace a general-purpose allocation that measurement has shown to be hot with a pool sized and shaped for the one thing being allocated, and end holding a measured improvement on the real workload rather than on a loop written to flatter it. Success is a pool whose assumed workload is written down, whose worst case you can name, and which the program is measurably better for.

## Steps / Flow

1. *Gate.* **Have the measurement before anything else.** `PAT_let_measurement_decide_what_to_tune` owns what counts as evidence. A pool is a permanent structure with its own failure modes, and building one for an allocation that was never hot leaves all of the cost and none of the benefit. Most candidates should stop here.

2. **Try to remove the allocation before making it cheaper.** `PAT_hoist_allocation_out_of_the_work` owns this. An allocation lifted out of a loop, or replaced by reuse of one object, is faster than any pool and adds no structure at all. Reach the rest of this flow only for allocations that genuinely must happen at their current rate.

3. *Gate.* **Name the order in which the program takes and returns these units.** `PAT_name_the_allocation_pattern_before_choosing_a_strategy` owns the four orders and the reason they conflict. Every remaining decision is made against this answer, so a flow that reaches step 4 without it is choosing a structure by taste.

4. **Choose the unit and the shape that fits that order.** Fixed-size units are what make the rest cheap, so settle the size first — one size per pool, with distinct sizes getting distinct pools. Where the units are raw memory, the free list belongs inside the free units themselves rather than in a structure beside them.

5. *Gate.* **Set the grow and shrink thresholds apart from each other.** `PAT_keep_a_spare_before_releasing_capacity` owns the gap. Writing both as the same comparison is the default and it is what makes a workload sitting on the boundary pay an acquisition and a release on every pass, while every size measurement reports the pool as healthy.

6. **Add a last-used hint only where lookups cluster.** `PAT_check_the_last_used_slot_before_searching` owns it, including the part most often got wrong: taking and returning have separate locality and need separate hints, and one hint shared between them is worse than none.

7. **Decide the ceiling and what happens above it.** Name the size beyond which a request goes to the general allocator instead. A pool asked to serve units far larger than it was tuned for holds memory it cannot reuse, so the ceiling is part of the design rather than a later refinement.

8. *Recovery.* **When the measurement does not improve, suspect the order before the implementation.** A correct pool built for the wrong order behaves exactly like a slow one. Return to step 3, and check the assumption recorded there against what the calling code actually does.

9. **Verify on the real workload.** `PAT_reproduce_the_real_context_before_believing_a_microbenchmark` owns why a loop that takes and returns one unit proves nothing here — that loop is a single reuse order, and it is the one every strategy handles well.

10. **Completion check.** The improvement is measured on the program rather than on a benchmark; the assumed reuse order is recorded beside the pool; the order that would defeat it is named; a loop using one unit at a time costs one acquisition rather than one per pass; and requests above the ceiling still work.

## Notes
The shape is a gate followed by a short sequence, and the gates carry most of the value. Steps 1 and 2 end most attempts, and ending there is the protocol working — a pool is a durable piece of structure with its own thrashing and corruption modes, and it should be paid for by evidence rather than by the intuition that allocation is slow.

Step 3 before step 4 is the ordering that matters most. Choosing the structure first and discovering the workload afterwards is the common route, and it produces a pool that is fast on the author's loop and unremarkable in the program, with nothing written down that would let the next person tell which of the two was wrong.

This protocol is about building the pool. Deciding that allocation is where the time goes at all belongs to the measurement flow that precedes it, and language-level questions — how a pool interacts with the allocation operators, what a custom allocator can and cannot buy from a container — belong to the language module rather than here.
