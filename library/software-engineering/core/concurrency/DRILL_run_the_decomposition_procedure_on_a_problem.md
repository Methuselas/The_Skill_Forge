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
No special setup required.

## Instructions
1. Choose the axis the parallelism lies along, and say which of the three it is and why the others were rejected.
2. Split as finely as the algorithm allows — one piece per cell, not one per processor. Count the pieces and confirm the count is one to two orders of magnitude above the execution units you expect.
3. For every piece, write down what it needs from its neighbours and how much. Total the crossings.
4. Merge pieces into groups so the expensive crossings fall inside a group. Do this twice — once grouping along one dimension, once into rectangular tiles — and total the crossings for each.
5. Compare the two totals against each other and against step 3. State which grouping wins and at what ratio of communication cost to computation cost the answer would flip.
6. Place the groups, balancing work and co-locating heavy communicators. Then state what would have to change if the execution unit count doubled.

## Success Check
- The piece count after step 2 is far larger than the processor count, and nothing about the processors influenced it.
- The crossing totals for both groupings are written down as numbers, not as impressions.
- The chosen grouping is justified by those numbers plus a stated cost ratio, not by which looked tidier.
- The final answer includes what changes when the machine changes.

## Common Failures
- Splitting straight to the processor count, which fixes the granularity before the dependencies are known and disguises a mapping decision as a decomposition.
- Skipping the second grouping, so there is nothing to compare the first against.
- Deriving the pieces from the order the sequential code performs things rather than from what depends on what.
- Producing a design that only works for the machine in front of you, with no answer to the last question.

## Notes
Repeat the exercise on a divide-and-conquer computation, where the pieces are generated as the work proceeds. Steps 1 and 2 are unchanged; steps 4 and 5 cannot be completed statically, and the second run of the drill is to notice exactly where the procedure stops and what has to take over.

The ordering is the whole content and the first step is where it is usually broken. Splitting maximally and merging back looks like wasted motion next to splitting into the number of pieces you need — but the merge decision requires the dependency graph, and the graph does not exist until the pieces do. The counts at each stage are about preserving freedom rather than accuracy: excess pieces mean the merge has options, excess groups mean the placement has options, and neither costs anything because neither intermediate result is built.
