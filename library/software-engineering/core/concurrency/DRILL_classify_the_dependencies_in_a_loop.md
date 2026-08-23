---
object_id: DRILL_classify_the_dependencies_in_a_loop
object_type: drill
name: Classify the Dependencies in a Loop Before Parallelizing It
target_skill: Separating real information flow from shared-name conflicts in a loop
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
- correctness
- control_flow
cross_links:
- rel: related_to
  target_object_id: PAT_classify_a_dependency_before_trying_to_remove_it
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Classify the Dependencies in a Loop Before Parallelizing It

## Practice Task
Take a loop that resists parallelization — one carrying a running total, reusing a scratch variable across iterations, and writing into an array it also reads — and sort every conflict in it into information that genuinely flows and locations that are merely shared.

## Target Skill
Separating real information flow from shared-name conflicts, and knowing which remedy each kind takes.

## Setup
No special setup required.

## Instructions
1. List every location the loop body touches, and mark each as read, written, or both.
2. For every pair of touches on the same location, decide whether they happen within one iteration or across iterations. Check across iterations explicitly — a statement early in the body runs after every statement later in the body from the previous pass.
3. Classify each conflict: a write followed by a read is information flowing; a read followed by a write, or two writes, is a shared name.
4. For each shared-name conflict, give the participants their own storage and confirm the conflict disappears entirely rather than being reordered around.
5. For each genuine flow, ask whether it has a known algorithmic form — an accumulator that is a reduction, a counter that has a closed form — and remove it that way if so.
6. Write down what remains. If a flow survives, state what parallelizes around it rather than declaring the loop sequential.

## Success Check
- Every conflict is classified, and the classification says which remedy applies rather than merely naming the kind.
- All shared-name conflicts are gone after privatization, with nothing reordered to accommodate them.
- Any surviving flow is stated explicitly, along with what still runs in parallel despite it.

## Common Failures
- Reading the body top to bottom and finding only the conflicts within one iteration.
- Treating every conflict as fatal, which stops the exercise before the name conflicts have been separated out.
- Privatizing a location that a genuine flow runs through, which turns a visible ordering problem into a silently wrong answer.
- Concluding a flow is irreducible because the first attempt failed, when the attempt applied the remedy for a different kind.

## Notes
The point of the sort is that it changes what happens next, not that it labels what is there. Most of what blocks a loop is two things sharing a location, which dissolves the moment they stop sharing it — so a loop with several apparent dependencies is usually parallelizable and looks impossible until they are separated. Do this before reaching for any synchronization, since a conflict that dissolves needs none.
