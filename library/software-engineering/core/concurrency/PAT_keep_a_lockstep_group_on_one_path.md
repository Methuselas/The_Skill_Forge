---
object_id: PAT_keep_a_lockstep_group_on_one_path
object_type: pattern
name: Keep a Lockstep Group on One Path
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- concurrency
- gpu
- performance
- control_flow
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_do_not_create_a_thread_for_every_task
- rel: related_to
  target_object_id: PAT_find_the_axis_the_parallelism_lies_along
- rel: related_to
  target_object_id: PAT_choose_between_a_parallel_program_and_parallel_regions
- rel: related_to
  target_object_id: PAT_trade_a_branch_for_unconditional_work
- rel: prerequisite_for
  target_object_id: DRILL_trace_divergence_and_coalescing_from_an_index_mapping
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Keep a Lockstep Group on One Path

## Pattern Rule
**IF** you are writing code for hardware that executes threads in fixed-size groups sharing one instruction stream — a graphics processor, or any vector unit presented as threads
**THEN** write the work so that every thread in a group takes the same branch, because when a group diverges the hardware executes *every* path taken, one after another, with the threads not on the current path idle throughout
**ELSE** where the code has no data-dependent branching at all, this does not arise and the constraint costs you nothing to satisfy.

## Do
- Understand what divergence actually costs, because the number is worse than it sounds. A group that splits two ways does not run the two halves concurrently — it runs one path with half the lanes idle, then the other path with the other half idle. The time is the *sum* of both paths, and the throughput is halved. A branch with several outcomes multiplies that accordingly.
- Locate the group boundary and treat it as a real unit of the design. The group size is a hardware property you do not choose, and divergence is only a cost *within* a group — different groups take different paths at full speed and cost nothing. So a branch on a condition that is uniform across each group is free, and the identical branch on a condition that alternates within a group is worst case.
- Arrange for the condition to correlate with the group rather than with the individual. Deciding by whether an index is even splits every group maximally; deciding by which contiguous block of indices a thread falls into keeps groups whole. The same logical partition of the work can be free or catastrophic depending only on how indices map to it.
- Prefer computing both results and selecting between them over branching, where both are cheap. On this hardware the branch was going to execute both paths anyway, so paying for both deliberately and picking one costs the same time and avoids the stall — which inverts the usual advice about avoiding wasted work.
- Push unavoidable divergence to the edges of the computation. If a small fraction of the data needs different handling, separating it into its own launch and processing it uniformly beats letting it split every group in the main body.
- Expect the cost to be invisible in the source. Nothing at a branch tells you whether it diverges; that depends on how the data maps to thread indices at run time, which is a property of the input as much as the code. This is one of the few performance characteristics that a reading of the kernel genuinely cannot reveal.
- Take the same reasoning to memory access, since it has the same grouped structure. Threads in a group issue their loads together, and whether those addresses can be served as one transaction or need many is decided by the same index-to-data mapping that decides divergence. The two problems are usually solved by the same layout choice.

## Don't
- Don't carry over the intuition that a branch is cheap because most threads skip it. On ordinary hardware, threads that fail a condition simply proceed; here they wait for the threads that passed, so an early-exit path that helps on a processor hurts on this one.
- Don't reason about divergence per thread. A condition that is false for ninety percent of threads costs nothing if the ten percent are gathered into a few groups, and costs nearly double if they are spread one per group. The distribution matters and the proportion does not.
- Don't leave a loop with a data-dependent trip count unexamined. Every thread in a group stays in the loop until the *last* one finishes, so a loop that usually runs twice and occasionally runs a thousand times costs a thousand iterations for the whole group.
- Don't assume a library call inside a kernel is uniform. Anything with internal branching on values can diverge just as user code does, and it does so invisibly behind an interface that looks like a single operation.
- Don't optimize divergence before establishing it is the constraint. Memory access patterns are more often the limit on this hardware, and a kernel restructured for uniform control flow while still reading memory badly has fixed the smaller problem.

## Checklist
- Which branches in this code depend on values that vary between threads?
- For each, does the condition change within a group, or only between groups?
- Could the index-to-data mapping be changed so the condition becomes group-uniform?
- Are both sides of any hot branch cheap enough to compute unconditionally instead?
- Does any loop have a trip count that varies across a group?
- Is divergence actually the limit here, or is memory access?

## Notes
The reason this needs stating at all is that the hardware presents itself in the vocabulary of threads, and that vocabulary carries assumptions which do not hold. On an ordinary processor threads are independent: they branch where they like, and one thread taking a slow path does not detain the others. Here a fixed-size group shares one instruction pointer, so independence is an illusion maintained by the hardware at a cost — and the cost is exactly the divergence it had to serialize. Everything surprising about performance on these devices follows from that gap between the model presented and the machine underneath.

The most useful practical consequence is that the *same* logical decomposition can be fast or slow depending only on how work is assigned to indices. Splitting a dataset by a property that alternates element to element and splitting it into contiguous runs are the same partition of the same work, and one of them keeps groups whole while the other splits every one. That is not an optimization applied after the fact; it is a consequence of the index mapping, which is chosen when the decomposition is designed and is expensive to change later.

Worth holding alongside this: the reason so many threads are wanted on this hardware in the first place is the opposite of the reason to limit them elsewhere. Each thread's execution context lives on-chip, so switching between groups is free, and the scheduler uses that to cover memory latency by running another group whenever one stalls. Oversubscription is therefore the mechanism rather than the waste — which reverses the usual rule about matching thread count to core count, and is the second place where CPU intuition points the wrong way.
