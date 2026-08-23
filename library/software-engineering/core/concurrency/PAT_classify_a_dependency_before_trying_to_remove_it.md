---
object_id: PAT_classify_a_dependency_before_trying_to_remove_it
object_type: pattern
name: Classify a Dependency Before Trying to Remove It
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
- decomposition
- design
- control_flow
- correctness
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: AP_design_a_parallel_decomposition
- rel: related_to
  target_object_id: PAT_derive_the_parallelism_from_work_and_span
- rel: related_to
  target_object_id: PAT_find_the_axis_the_parallelism_lies_along
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: prerequisite_for
  target_object_id: DRILL_classify_the_dependencies_in_a_loop
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Classify a Dependency Before Trying to Remove It

## Pattern Rule
**IF** a loop or a region resists parallelization because its steps depend on one another, and you are deciding what to do about it
**THEN** determine which kind of dependency each one is before attempting anything, because two of the three kinds exist only because two things share a name and dissolve when you give them separate storage, while the third carries actual information and can be removed only by changing the algorithm
**ELSE** where the only relationship between steps is that they both read the same value, there is no dependency at all and nothing needs removing.

## Do
- Separate the three by what flows between the steps. One step writes a location and a later one reads it: information genuinely passes, and the order is real. One step reads a location and a later one overwrites it: nothing passes, and the order exists only because the reader must go first. Two steps both write the same location: nothing passes, and the order exists only because one result must survive. Only the first is a dependency on *data*; the other two are dependencies on a *name*.
- Attack the name dependencies by removing the sharing, not by ordering around them. Two steps that write the same location can each write their own; a step that reads before another overwrites can read into its own copy. Giving each participant private storage makes both kinds vanish entirely, which is why privatization and renaming are the standard first moves and why they so often work.
- Treat a true dependency as a statement about the algorithm rather than about the code. Where information really does pass from one step to the next, no amount of restructuring the loop removes it — the remedy is a different algorithm with a different information flow, and if none exists then that part is sequential and the honest response is to say so and parallelize around it.
- Look for the true dependencies that have known algorithmic answers before concluding a loop is sequential. An accumulator threading through every iteration is a true dependency and is also a reduction, which parallelizes by giving each participant a partial result and combining at the end. An accumulator whose running value is also stored at every step is a true dependency and is also a scan, which parallelizes in two passes — a partial result per block, then each block shifted by the combined total of the blocks before it. A counter advanced by a fixed amount each iteration is a true dependency and is also a closed-form expression that each iteration can compute directly. All three look fatal and none is.
- Take iteration order into account, not just statement order, because that is where loop dependencies hide. A dependency exists between two statements when one touches in iteration *i* what the other touches in iteration *j*, so a statement written *earlier* in the body can depend on one written later, via the previous pass. Reading the body top to bottom will not find these; you have to ask which iterations touch the same location.
- Say which locations are shared and which are private before parallelizing anything. Most loop dependencies are discovered by that question rather than by staring at the code, and the answer is also what the parallelization will need stated explicitly.
- Stop when a dependency survives classification and has no algorithmic answer. Partial parallelization around it — running the independent portion in parallel while honouring the real ordering — is a legitimate outcome and far better than a version that ignores the dependency and is wrong.

## Don't
- Don't treat all dependencies as equally fatal. It is the common error and it stops parallelization early: a loop with several apparent dependencies where all but one are name conflicts is nearly always parallelizable, and looks impossible until they are sorted.
- Don't remove a true dependency by ignoring it. Violating a real ordering does not produce a slower program or a rare failure — it produces a wrong answer, sometimes reproducibly enough to be mistaken for correct on small inputs.
- Don't rely on reading statement order to find loop-carried dependencies. Source order and execution order are the same thing only within one iteration; across iterations they are not, and arrays are where this bites because the two sides of the dependency look like unrelated subscripts.
- Don't privatize a location that a true dependency runs through. Giving each participant its own copy of something whose value must flow between them replaces a correctness problem with a silent one, since each copy is then independently and confidently wrong.
- Don't conclude a dependency is real because your first attempt to remove it failed. The three kinds have different remedies, and applying the wrong remedy fails in a way that looks like the dependency being fundamental.

## Checklist
- For each pair of steps that conflict, does information actually flow, or do they merely share a location?
- For the ones that merely share, would private storage dissolve them?
- For the ones that carry information, is there a known algorithmic form — a reduction, a scan, a closed form — that removes the flow?
- Which locations are shared and which are private, stated explicitly?
- Have you checked for conflicts between different iterations, not only within one?
- If a true dependency survives, what parallelizes around it?

## Notes
The taxonomy earns its place by changing what you do next rather than by describing what you see. Faced with a loop that will not parallelize, the untrained response is to try harder or give up, and both are frequently wrong: most of what blocks a loop is two things sharing a location, which dissolves the moment they stop sharing it. Sorting the conflicts into "information flows here" and "these merely collide" turns an intractable-looking loop into a small number of real constraints, and the real constraints are usually few.

The distinction between a data dependency and a name dependency is the whole of it, and it is worth holding in those terms rather than by the conventional labels. A name dependency is an artifact of storage reuse — of the same variable being used for two unrelated purposes at two times — and reuse is a decision the code made, so it can be undone. A data dependency is a property of the computation, and the only way to change it is to compute something else.

Iteration order is where this reasoning is most often applied wrongly, and the reason is a habit that serves everywhere else. Within straight-line code, order in the source is order in execution, so reading downward finds every dependency. In a loop, a statement at the top of the body executes *after* every statement at the bottom of the previous iteration — so the dependency you are looking for may run backwards through the text. The question that finds these is not what the code says in order, but which iterations touch the same location.
