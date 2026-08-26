---
object_id: DRILL_trace_divergence_and_coalescing_from_an_index_mapping
object_type: drill
name: Trace Divergence and Coalescing From One Index Mapping
target_skill: Predicting a lockstep group's control-flow and memory cost from how indices map to data
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
- gpu
- performance
- data_layout
cross_links:
- rel: related_to
  target_object_id: PAT_keep_a_lockstep_group_on_one_path
- rel: related_to
  target_object_id: PAT_lay_data_out_for_the_group_that_reads_it_together
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Trace Divergence and Coalescing From One Index Mapping

## Practice Task
Take a routine that processes a collection of records on hardware executing threads in fixed-size lockstep groups — summing one field of every record, with negative, zero, and positive values each handled along their own path — and predict, without running it, how many paths each group serializes and how many memory units it touches per instruction.

## Target Skill
Predicting a lockstep group's control-flow and memory cost from how indices map to data.

## Setup
Work one stated instance, because every number the drill produces is a property of the inputs rather than of the code: lockstep groups of 32 threads; one million records of 32 bytes each, with the summed field at offset 0; and a sign condition that holds in runs of 100 consecutive records.

Two of those decide whether the drill shows anything at all. The **record size** decides whether the mapping can change which memory units a group touches — at a record size equal to the memory unit size, every thread touches its own unit under both mappings, the transaction counts come out identical, and the mapping is not what is at fault. And the **run length must not divide the group size**: a run commensurate with the group makes every group uniform and manufactures a clean result out of the arithmetic rather than out of the mapping.

Report both costs twice: per instruction for one group, and aggregated over one group's whole pass through the kernel. Per instruction the two mappings are barely distinguishable; the aggregate is what step 6 needs.

## Instructions
1. Write down the mapping: for a thread with a given index, which record and which field does it touch, and which of the three paths does it take. The condition's distribution is fixed in Setup and deliberately has structure at the group scale — runs of records falling on one side rather than an independent draw per record — because a per-record random condition leaves every group mixed under every mapping, and then there is nothing for the mapping to change.
2. Take one group of consecutive thread indices. For the branch, list which members take each path. Report the cost as the sum of the paths taken, not as a proportion of threads. Then change only the proportion of records on each path — same run structure, same run length — and count again. Record both.
3. Declare the size of the aligned memory unit your hardware model serves. The counts depend on it, so it has to be fixed before you count rather than assumed. For the same group and one instruction, list the addresses touched and count how many distinct units of that size they fall into. That count is the transaction cost.
4. Change only the mapping — assign each thread a contiguous run of records instead of a strided one, or the reverse — and redo steps 2 and 3. Record both numbers for both mappings.
5. Reorganize the records into one array per field, leaving the mapping alone, and redo step 3.
6. State which single change bought the most, and whether the control-flow cost and the memory cost moved together or in opposite directions.

## Success Check
- The unit size is declared before any transaction is counted, and both costs are reported as counts derived from the mapping — with the group's addresses listed and sorted into units, so the arithmetic can be checked — rather than as impressions of whether the code looks parallel.
- The branch cost is the sum of paths taken by the group, and the recount at the changed proportion in step 2 leaves it unchanged, because the distribution did not change.
- The two mappings produce different numbers for both costs, and the relationship between them is stated.
- If the branch cost did not move between the mappings, the fault is the branch distribution. If the memory cost did not move, the fault is the record size against the declared unit size, and the branch distribution has nothing to do with it. Name which one, and name the value that would move it — do not retune an input until the expected result appears.
- The layout change and the mapping change are evaluated separately rather than applied together.

## Common Failures
- Reasoning about one thread's access pattern, which can look perfectly sequential while the group's simultaneous accesses land in a different unit each.
- Reporting divergence as a percentage of threads rather than as which groups are split, when a condition true for one thread in ten costs nothing if those threads are gathered and nearly double if they are spread.
- Choosing a run length commensurate with the group size, which makes every group uniform and produces a clean result the mapping did not cause. Step 1 warns against too little structure at the group scale; this is the same mistake inverted.
- Assuming a layout good for a cache is good here, when sequential-over-time and simultaneous-at-one-instant are different requirements.
- Changing the mapping and the layout in the same step, so neither effect is attributable.

## Notes
The exercise exists to make one point concrete: both costs come from the same decision. Divergence and scattered access are consequences of how thread indices map onto data, so a mapping that assigns contiguous work to contiguous threads tends to fix both, and one that interleaves by some property tends to break both. That makes the mapping a single choice with two large effects, belonging where the decomposition is designed rather than in a later tuning pass — which is why predicting the numbers on paper is the skill worth having.
