---
object_id: PAT_hoist_allocation_out_of_the_work
object_type: pattern
name: Hoist Allocation Out of the Work
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
- memory
- allocation
- concurrency
- tuning
cross_links:
- rel: related_to
  target_object_id: PAT_ask_whether_the_hot_code_can_run_less_often
- rel: related_to
  target_object_id: PAT_choose_the_data_structure_for_the_dominant_access_pattern
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
- rel: related_to
  target_object_id: PAT_check_for_memory_saturation_before_adding_threads
- rel: related_to
  target_object_id: AP_build_a_pool_for_a_hot_allocation
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Hoist Allocation Out of the Work

## Pattern Rule
**IF** a loop or a repeated operation acquires memory from the system and releases it on every pass
**THEN** move the acquisition outside the repetition and reuse the same memory, sizing it to the maximum need or growing it without ever shrinking
**ELSE** where each pass genuinely needs an unrelated lifetime — the results outlive the iteration and are handed elsewhere — the allocation belongs where it is and the cost is real work.

## Do
- Measure the ceiling by removing the allocations rather than by reasoning about them. Hoisting a per-iteration buffer out of a loop that did nothing but fill it made the loop roughly two and a half times faster; the allocating version ran at about forty percent of the speed of the version that allocated once.
- Preallocate to the maximum where you know it. A single buffer sized to the largest case, reused every pass, is the fastest arrangement and usually the simplest — and a container that offers reserved capacity gives the same thing, since reducing its size does not give the capacity back.
- Use a grow-only buffer where the maximum is not known. Grow when a request exceeds the current size, never shrink, and the cost converges on the preallocated case after the early iterations. Grow by more than the amount requested so growth becomes rare — the usual container strategy — rather than exactly to fit.
- Keep each buffer separate rather than merging them. Several containers each with their own reserved capacity is the intent; packing unrelated uses into one allocation to save a call is a different and worse design.
- Expect the effect to be larger in a threaded program, and treat it as a scaling issue rather than a constant cost. The system allocator maintains internal structures that must be guarded, and that guard is global to the process, so a program allocating frequently on many threads is serializing through it.
- Keep each allocation's lifetime on one thread. Allocators with per-thread caches — the usual answer to that global guard — handle allocate-here-free-here well and cross-thread release badly: freeing on a different thread from the one that allocated measured at least an order of magnitude worse.

## Don't
- Don't assume a micro-benchmark shows the full cost. Allocation patterns in a small test are simple and the allocator performs better on them than it will inside a large program with a complicated mix of sizes and lifetimes.
- Don't hide the allocations and conclude there are none. Containers that manage their own storage allocate on construction, growth, and often assignment, so a loop with no explicit allocation call can still be dominated by allocation.
- Don't buy a per-thread caching allocator without accounting for the memory. Free memory held in one thread's cache is not available to another, so total usage rises — which is why such allocators cap the per-thread cache and return the excess under a lock.
- Don't tune for a non-uniform memory system until you have measured on it. Where each processor is closer to some memory banks than others, the effect ranges from nothing to a factor of two, and any tuning is specific to the machine you tuned it on.

## Checklist
- How many allocations does this code perform per unit of user-visible work?
- Is the maximum size knowable, and if not, does the buffer grow without shrinking?
- Does the growth policy over-allocate, so growth becomes rare?
- Is every block freed by the thread that allocated it?
- What does the same code measure with the allocations hoisted out entirely?

## Notes
The underlying instruction is to interact with the system as little as possible. An allocator is a shared, general-purpose service tuned to be acceptable for every program rather than good for yours, and each call is a request into a data structure someone else's code maintains — which is why removing calls beats making them faster.

There is a second failure this prevents that shows up as running out of memory rather than as slowness. Repeated allocation and release of varying sizes leaves free space scattered in pieces too small to satisfy later requests, so a program can exhaust its address space while most of it is free — one case cited failed after allocating a sixth of the machine's memory. Reusing buffers avoids the churn that produces this.

Where the churn is unavoidable, the escalation is fixed-size block allocation: take large chunks from the system, cut them into uniform blocks, and build everything on those. Uniformity is what removes fragmentation, since any returned block satisfies any future request, and reusing the most recently released block has a second benefit — it is the memory most recently touched and therefore still cached. The cost is that it constrains the whole program: no single large contiguous containers, small objects packed into shared blocks, and often a container library of your own. That is a large commitment and the reason it belongs at the end of this progression rather than the start.
