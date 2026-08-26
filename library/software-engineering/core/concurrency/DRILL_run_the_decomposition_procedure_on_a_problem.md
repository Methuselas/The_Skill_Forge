---
object_id: DRILL_run_the_decomposition_procedure_on_a_problem
object_type: drill
name: Run the Decomposition Procedure on a Concrete Problem
target_skill: Splitting maximally, deriving dependencies, then merging and placing against them
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
- decomposition
- design
- scalability
cross_links:
- rel: related_to
  target_object_id: AP_design_a_parallel_decomposition
- rel: related_to
  target_object_id: PAT_find_the_axis_the_parallelism_lies_along
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Run the Decomposition Procedure on a Concrete Problem

## Practice Task
Take a sequential computation over a grid — applying a small stencil to every cell of an image, or advancing a heat-diffusion field one step — and carry it through the four-step decomposition, writing down the intermediate results at each step rather than jumping to an answer.

## Target Skill
Splitting maximally, deriving dependencies, then merging and placing against them, in that order.

## Setup
Work one stated instance rather than a general grid: a five-point stencil on an N x N field with N = 4096, on P = 64 execution units, with a one-cell halo. Four things have to be fixed before any counting starts, because each changes the answer rather than merely the units it is reported in.

- **Which sweep.** Jacobi, where the new field is written from the old, or in-place Gauss-Seidel, where a cell reads values already updated this sweep. The two have identical source structure and completely different dependency graphs, and the choice decides step 2 by itself. State which one you are decomposing.
- **The crossing unit.** Directed or undirected, values or bytes. Step 5 compares step 4's totals against step 3's, so the unit has to be identical across all three.
- **The same group count and equal-area groups for both groupings in step 4.** Step 5's claim that computation cancels holds only under that condition; two groupings at different group counts are not comparable.
- **Genuinely two-dimensional tiles.** A 1 x G rectangle is a strip, so grouping B collapses into grouping A and the comparison produces two identical numbers and no decision.

## Instructions
1. Choose the axis the parallelism lies along, and say which of the three it is and why the others were rejected.
2. Split as finely as the algorithm allows — one piece per independent unit of work, which for an in-place sweep is not one piece per cell. Count the pieces. The count should be a property of the problem rather than of the machine, and should exceed the execution units by at least an order of magnitude; if it came out close to the unit count, you split to the machine rather than to the algorithm and must go back.
3. For every piece, write down what it needs from its neighbours and how much. Total the crossings and the number of transfers.
4. Merge pieces into groups so the expensive crossings fall inside a group, aiming for a group count one to two orders of magnitude above the execution units so that placement still has slack to work with. Do this twice — once grouping along one dimension, once into rectangular tiles — and total the crossings and the number of transfers for each.
5. Compare the two totals against each other and against step 3. State which grouping wins, and at what ratio of fixed per-transfer cost to per-value cost the answer would flip — the transfer counts from steps 3 and 4 are what make that ratio computable, and volumes alone will not. Computation is identical across the two groupings because Setup fixed them to the same group count and equal areas, so it cancels and cannot decide between them.
6. Place the groups, balancing work and co-locating heavy communicators. Then state what would have to change if the execution unit count doubled.

## Success Check
- The piece count after step 2 is a property of the problem rather than of the machine — a formula in the problem's own dimensions where one exists, or the rule that generates the pieces where it does not — and it exceeds the execution unit count. For an in-place sweep, N-squared is the count of cells and not the count of independent pieces.
- The crossing totals and the transfer counts for both groupings are written down as numbers in the declared unit, with the arithmetic that produced them shown, and the two groupings are comparable — same group count, same unit, same halo convention.
- The chosen grouping is justified by those numbers plus the per-transfer-to-per-value ratio at which the choice flips, with a machine instantiated on each side of that threshold — or with the statement that no realizable machine sits on one side of it, and why.
- The final answer separates what changes when the machine changes from what does not, and says which steps would be redone, giving the numbers those steps produce at the doubled unit count rather than restating that they depend on it.

## Common Failures
- Splitting straight to the processor count, which fixes the granularity before the dependencies are known and disguises a mapping decision as a decomposition.
- Skipping the second grouping, so there is nothing to compare the first against.
- Deriving the pieces from the order the sequential code performs things rather than from what depends on what.
- Producing a design that only works for the machine in front of you, with no answer to the last question.

## Notes
Repeat the exercise on a divide-and-conquer computation, where the pieces are generated as the work proceeds. Steps 1 and 2 are unchanged — though there the piece count is a rule that generates pieces rather than a formula — while steps 4 and 5 cannot be completed statically, and the second run of the drill is to notice exactly where the procedure stops and what has to take over.

The ordering is the whole content and the first step is where it is usually broken. Splitting maximally and merging back looks like wasted motion next to splitting into the number of pieces you need — but the merge decision requires the dependency graph, and the graph does not exist until the pieces do. The counts at each stage are about preserving freedom rather than accuracy: excess pieces mean the merge has options, excess groups mean the placement has options, and neither costs anything because neither intermediate result is built.
