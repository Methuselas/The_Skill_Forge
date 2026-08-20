---
object_id: PAT_name_the_binding_constraint_before_choosing_a_remedy
object_type: pattern
name: Name the Binding Constraint Before Choosing a Remedy
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
- diagnosis
- measurement
- hardware
- tuning
cross_links:
- rel: related_to
  target_object_id: PAT_read_a_profile_as_a_statement_about_machine_code
- rel: prerequisite_for
  target_object_id: AP_tune_a_measured_bottleneck
- rel: related_to
  target_object_id: PAT_count_the_dependency_chain_not_the_operations
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
- rel: related_to
  target_object_id: PAT_confirm_a_branch_is_mispredicted_before_optimizing_it
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Name the Binding Constraint Before Choosing a Remedy

## Pattern Rule
**IF** measurement has identified the code that is costing you time and you are deciding what change to attempt
**THEN** classify what is actually limiting that code — memory traffic, branch misprediction, a dependency chain, or the sheer amount of work — before selecting a technique, because each limit has its own remedies and they are not interchangeable
**ELSE** where the region is small enough to read in full and its cost is obviously one operation repeated, the classification is already done and the remedy follows directly.

## Do
- Collect the counters over the bounded region, not the whole program. Whole-run totals tell you what kind of limit the program is against and never where; once a profile has narrowed the territory, the same counters over that territory answer what.
- Start from instructions against cycles. Several instructions retired per cycle means the hardware is busy and the code is genuinely doing the work — so the remedy is doing less of it. Well under one means the processor is stalled and the question becomes what it is waiting for.
- Read data-cache misses against loads for the memory case. A high miss rate points at the working set, the layout, and the access order — and the remedies there are structural: fit the data in a cache level, choose a structure for the traversal that dominates, convert scattered access to sequential, stop allocating in the loop.
- Read branch misses against branches for the control case, on the scale that applies to them. Below a tenth of a percent is healthy and one percent is already large, so a rate in that range means finding the conditional and treating it — after confirming the compiled code actually branches there.
- Suspect a dependency chain when the processor is stalled and neither cache nor branch counters explain it. Each step waiting on the previous one leaves execution units idle with no misses to show for it, and the remedy is shortening the chain rather than removing operations.
- Treat "the code is doing the work" as a real diagnosis rather than a failure to find one. A region running at high instruction throughput with no misses is not badly written; what is left is calling it less often, a better algorithm, or accepting the cost.
- Re-classify after each accepted change. Removing one limit exposes the next — code that was memory-bound and is no longer will be bound by something else, and the technique that just worked is unlikely to be the one that works again.

## Don't
- Don't select a technique because you know it. The available remedies are not alternatives to each other: branchless code does nothing for a cache-miss problem, and better data layout does nothing for a mispredicted branch, so a technique chosen by familiarity fails most of the time by construction.
- Don't infer the constraint from reading the code. What limits a region is a property of the data volumes and access patterns it actually sees, and the source shows neither.
- Don't stop at one counter. A region can miss cache and mispredict at once, and the useful question is which one accounts for the time you are trying to explain.
- Don't carry a classification across machines. Cache sizes, memory bandwidth, and branch predictors differ, so a region that is memory-bound on one machine can be compute-bound on another with the same code and data.

## Checklist
- What are the instructions-per-cycle, cache-miss, and branch-miss rates over this region specifically?
- Which of them is large enough to account for the time in question?
- If the processor is stalled and neither counter explains it, what is each step waiting for?
- Does the remedy you are about to attempt address the constraint you named?
- After the change lands, what does the classification say now?

## Notes
This sits between locating a bottleneck and tuning it, and it exists because those two activities leave a gap that gets filled by habit. Profiling says where the time goes. The tuning discipline says how to make a change safely and how to know whether to keep it. Neither says what to try, and in the absence of an answer people try what they last read about — which is why so many tuning attempts produce nothing while the measurements around them are impeccable.

The classification is worth holding as a small fixed set rather than a spectrum, because the remedies partition the same way. Stalled on memory, stalled on control flow, stalled on its own previous results, or not stalled at all: four states, four distinct families of technique, and almost no overlap between them. Most of the value here is in ruling out three families before spending effort on one.

Expect the diagnosis to move as the work proceeds, and treat that as progress rather than as the earlier diagnosis having been wrong. A limit is only binding until it is not; relieving it hands the constraint to whatever was second. A tuning effort that keeps re-measuring the classification will look like a sequence of unrelated fixes, and that is what a successful one usually is.
