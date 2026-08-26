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
Two conventions have to be fixed before the counting starts, or two correct runs of this drill cannot be compared.

Count one conflict per location and per kind: a location read and written across iterations contributes one flow and one name conflict, not one entry per statement pair. The same loop yields roughly four times as many conflicts under statement-pair counting and roughly a third as many counting locations alone, and all three readings are defensible from the words "every pair of touches."

And decide, before step 5, whether the restructured loop must reproduce the original bit for bit or only within a stated numeric tolerance. A reassociated floating-point reduction is not bit-for-bit, so the strict standard leaves a flow that the tolerant standard removes — the answer to step 6 changes with the choice.

## Instructions
1. List every location the loop body touches, and mark each as read, written, or both.
2. For every pair of touches on the same location, decide whether they happen within one iteration or across iterations. Check across iterations explicitly — a statement early in the body runs after every statement later in the body from the previous pass.
3. Classify each **cross-iteration** conflict: a write followed by a read is information flowing; a read followed by a write, or two writes, is a shared name. Only the cross-iteration classification gates a remedy. A pair whose touches both fall inside one iteration is satisfied by running the body in source order within whichever participant executes it — a scratch value written at the top of the body and read below is exactly that, and privatizing it is the cheapest win the loop offers.
4. For each shared-name conflict, give the participants their own storage and confirm the conflict disappears entirely rather than being reordered around.
5. For each genuine flow, ask whether it has a known algorithmic form — an accumulator that is a reduction, a counter that has a closed form — and remove it that way if so.
6. Write down what remains. If a flow survives, state what parallelizes around it rather than declaring the loop sequential.

## Success Check
- Every conflict is classified, and the classification says which remedy applies rather than merely naming the kind. For each cross-iteration pair, the iteration that writes the value and the iteration that reads it are both named, so the classification can be checked rather than taken on the word of the run.
- For every location given private storage, the reason no flow runs through it is written as which iteration writes the value it reads, not asserted. Any location carrying both a flow and a name conflict is identified as such, and left shared where the flow survives step 5.
- All shared-name conflicts are gone after privatization, with nothing reordered to accommodate them.
- The restructured loop reproduces the original's results to the standard fixed in Setup, and every deviation is declared and attributed to a named algorithmic change from step 5. Privatizing every location including the ones carrying flows satisfies the bullet above perfectly and fails here; that is what this bullet is for.
- Any surviving flow is stated explicitly, along with what still runs in parallel despite it.

## Common Failures
- Reading the body top to bottom and finding only the conflicts within one iteration.
- Treating every conflict as fatal, which stops the exercise before the name conflicts have been separated out.
- Privatizing a location that a genuine flow still runs through after step 5, which turns a visible ordering problem into a silently wrong answer.
- Concluding a flow is irreducible because the first attempt failed, when the attempt applied the remedy for a different kind.

## Notes
The point of the sort is that it changes what happens next, not that it labels what is there. Most of what blocks a loop is two things sharing a location, which dissolves the moment they stop sharing it — so a loop with several apparent dependencies is usually parallelizable and looks impossible until they are separated. Do this before reaching for any synchronization, since a conflict that dissolves needs none.
