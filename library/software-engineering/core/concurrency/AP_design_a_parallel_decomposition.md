---
object_id: AP_design_a_parallel_decomposition
object_type: ap
name: Design a Parallel Decomposition
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- design
- decomposition
- scalability
- load_balancing
cross_links:
- rel: supports
  target_object_id: PAT_decide_if_the_problem_is_worth_parallelizing
- rel: supports
  target_object_id: PAT_find_the_axis_the_parallelism_lies_along
- rel: supports
  target_object_id: PAT_derive_the_parallelism_from_work_and_span
- rel: supports
  target_object_id: PAT_let_idle_workers_take_work_rather_than_busy_ones_hand_it_out
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: supports
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
- rel: supports
  target_object_id: PAT_price_communication_by_transfer_count_and_volume_separately
- rel: prerequisite_for
  target_object_id: DRILL_run_the_decomposition_procedure_on_a_problem
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Design a Parallel Decomposition

## Objective
Take a computation that currently runs as one sequential algorithm and produce a parallel design for it: a set of work groups, what must pass between them, and which group goes where. Success is a design you can hand to an implementation with the piece boundaries, the data that crosses them, and the placement all decided — and with the reason each was chosen still available to whoever questions it later.

## Steps / Flow

**Entry state.** You have a working sequential algorithm, or a specification precise enough to derive one, and you have already decided the computation is worth parallelizing at all — that decision belongs to `PAT_decide_if_the_problem_is_worth_parallelizing` and is not repeated here. You also need to know, at least roughly, how many execution units the result will run on, because three of the four steps below are stated relative to that number.

**1. Split as finely as the algorithm allows.** Choose the axis first — `PAT_find_the_axis_the_parallelism_lies_along` owns that choice — then cut along it as far as it will go, without regard for how many processors exist. The piece count is a floor, not a target: it must exceed the execution units by at least an order of magnitude, and on a large problem a maximal split will exceed them by far more than that. A count that lands close to the unit count means the split was made to the machine.

*This is the step most often done wrongly, and the error is always the same: partitioning into as many pieces as there are processors.* Doing that fixes the granularity before you know what the pieces need from each other, and every later decision then has to live with it. Over-splitting costs nothing at this stage because nothing has been committed to yet — the pieces are a description, not a design.

*Gate.* If the split produced roughly as many pieces as processors, go back. You have decided the mapping already and disguised it as a decomposition.

**2. Draw what has to cross.** For every pair of pieces, determine what one needs from the other and how much of it. `PAT_price_communication_by_transfer_count_and_volume_separately` owns pricing that: the number of transfers and the volume moved are separate costs, and a boundary can be cheap in one and ruinous in the other. Pieces plus these dependencies are the task graph, and it — not the source — is what the rest of the process reads from.

Derive it from data dependencies rather than from the order the sequential code performs things. Sequential order includes every ordering the algorithm needs *and* every ordering one processor happened to impose, and only the first kind survives parallelization.

*Gate.* If nothing crosses between any pieces, the remaining steps are trivial and you should say so — this is the case where the work divides cleanly and never communicates, and it deserves the simplest possible treatment rather than this procedure.

**3. Merge pieces back together against that graph.** Group pieces so that expensive dependencies fall *inside* a group and disappear. Aim for one to two orders of magnitude more groups than execution units — still more than you need, so the mapping step retains freedom.

Two properties are in tension here and both matter. Groups should be equal in the *work* they represent, because the slowest group sets the finish time — `PAT_decide_if_the_problem_is_worth_parallelizing` carries why imbalance behaves like a serial fraction. And groups should be drawn so the boundaries cut the cheapest dependencies. When those conflict, measure rather than argue: which one binds depends on the ratio of communication cost to computation cost, and that ratio is a property of the platform.

*Gate.* Compare the total crossing volume before and after. If merging did not reduce it substantially, either the axis was wrong — return to step 1 — or the problem genuinely has dependencies everywhere, which is worth knowing before implementation rather than after.

**4. Place the groups.** Assign groups to execution units to balance load and to co-locate the groups that exchange the most, since communication within a unit is far cheaper than between. Where placement affects which memory a group's data is near, `PAT_locate_the_working_set_on_the_memory_hierarchy` governs that.

Optimal placement is intractable in general, so do not search for it. A heuristic that balances work and keeps heavy communicators together captures nearly all of the available benefit, and the remaining gap is not worth the effort — the same shape as the result that any non-idling schedule is within a constant factor of optimal, which `PAT_derive_the_parallelism_from_work_and_span` carries.

**Branch — when the pieces are not known in advance.** If step 1 established that pieces are generated as the computation runs, steps 3 and 4 cannot be completed statically. Merge as far as the known structure permits, then hand placement to a run-time mechanism: `PAT_let_idle_workers_take_work_rather_than_busy_ones_hand_it_out` owns that. The first two steps are unchanged and still worth doing, because the axis and the dependency structure are properties of the algorithm rather than of when the work appears.

**Completion check.** You are done when you can state, for the design: which axis it was cut along; how many groups there are relative to execution units; what crosses between groups and roughly how much; what balances the groups; and what would have to change if the unit count doubled. If the last one has no answer, the design has been fitted to one machine.

## Notes
The order is the whole content of this procedure, and it is counterintuitive in one specific place. Splitting maximally and then merging back seems like wasted motion compared to splitting into the number of pieces you need — but the merge decision requires the dependency graph, and the dependency graph only exists once the pieces do. Partitioning straight to the processor count answers the hardest question first, using the least information, and then presents the answer as a starting point that everything else must accommodate.

The rules of thumb about how many pieces to produce at each stage are doing something more useful than they appear. They are not accuracy targets; they are a way of preserving freedom. Excess pieces at step 1 mean the merge has options; excess groups at step 3 mean the placement has options; and the cost of that freedom is nil, because neither intermediate result is built. A procedure that narrows to the final count early has spent its flexibility before reaching the step that needed it.

Two scope limits are worth stating. This produces a decomposition, not an implementation — nothing here says which synchronization mechanism the crossings become, and that choice belongs to the platform and to the Patterns that govern it. And it assumes the sequential algorithm is the right algorithm; a decomposition that comes out badly is sometimes evidence that a different algorithm with a shorter critical path would parallelize better, which is a question this procedure will surface and cannot answer.
