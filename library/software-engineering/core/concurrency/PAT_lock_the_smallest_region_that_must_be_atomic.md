---
object_id: PAT_lock_the_smallest_region_that_must_be_atomic
object_type: pattern
name: Lock the Smallest Region That Must Be Atomic
library_path:
- software-engineering
- core
- concurrency
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- locking
- threading
- performance
- contention
cross_links:
- rel: related_to
  target_object_id: PAT_extract_a_routine_even_when_it_seems_too_small
- rel: prerequisite_for
  target_object_id: PAT_take_the_simplest_lock_type_that_does_the_job
- rel: related_to
  target_object_id: PAT_atomic_steps_do_not_compose_into_a_safe_whole
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: related_to
  target_object_id: PAT_break_one_of_deadlocks_four_conditions
- rel: prerequisite_for
  target_object_id: PAT_match_the_lock_to_the_length_of_the_critical_section
- rel: prerequisite_for
  target_object_id: PAT_split_a_lock_only_where_the_structure_makes_the_regions_disjoint
- rel: prerequisite_for
  target_object_id: PAT_cover_many_regions_with_a_fixed_number_of_locks
- rel: prerequisite_for
  target_object_id: PAT_search_without_locks_then_lock_and_validate
reference:
  source_title: 'Clean Code: A Handbook of Agile Software Craftsmanship'
  author: Robert C. Martin, with Brett L. Schuchert
confidence: high
references: []
variants: []
---

# Lock the Smallest Region That Must Be Atomic

## Pattern Rule
**IF** you are placing a guard around code that several threads will run
**THEN** cover exactly the span across which the invariant is temporarily untrue and no more, while separately arranging the design so that few such spans exist at all
**ELSE** where the span you would have to cover keeps growing as you examine it, that is a sign the state is shared too widely, and the fix belongs in the design rather than in the guard.

## Do
- Hold the two goals at once, because they pull in opposite directions and only one of them is obvious. Guarded regions should be few, and each should be small; pursuing either alone produces a design that fails on the other.
- Establish the boundary from the invariant rather than from convenience. What has to be covered is the stretch during which the rule about the state does not hold — that is a property of the rule, and it is usually narrower than the method that happens to contain it.
- Treat every guard as a cost paid on every pass. Acquiring and releasing takes time whether or not anyone is contending, and the delay is borne by all the traffic through that path, not merely by the collisions.
- Reduce the count by narrowing what is shared, not by widening what is covered. Fewer places touching the state is the outcome you want; fewer, larger guarded regions is a different outcome that looks similar on a diagram.
- Watch what a widened region drags inside it. Anything slow that gets enclosed — a read from disk, a call across a network, a wait on something else — is now held while everyone else queues, and that is how a guard meant to protect a field ends up serialising the system.
- Weigh the narrowing against how the release is guaranteed, because those two also pull against each other and the second one is the safety-critical half. A release bound to a scope happens on every way out, including the ones added later and the ones taken by a failure; a release written by hand has to appear on each of them, and the exit that gets missed is usually the early return added months afterwards by somebody who did not know a guard was open. Failing to release is a hang, which is a worse outcome than the contention the narrowing was buying back.
- Buy both by moving the boundary rather than by managing the release manually. Where the invariant covers less than the routine, lift the guarded stretch into a routine of its own: the scope-bound release then covers exactly the invariant, because the boundary it follows has been made to coincide with it deliberately rather than by accident. This is the resolution to the tension above and it is available far more often than it is taken, since it costs one small routine and the same routine usually wants a name anyway.
- Take the manual release only where a measurement says the hold matters and the extraction will not serve, and treat it as a local exception with every exit accounted for. A hot path holding a guard across work it does not need to is a real cost and worth removing; the discipline is that removing it this way makes correctness depend on a reader noticing every branch, forever.
- Check the acquisition order whenever a guarded region contains another. Nesting is where cyclic waiting appears, and the answer is either to avoid the nesting or to fix the order globally.

## Don't
- Don't widen a region to reduce how many you have. It is the natural way to satisfy the count and it makes throughput worse, because contention rises with how long the guard is held.
- Don't wrap a whole method by default because that is where the boundary is easiest to see. The method boundary and the invariant boundary coincide only by accident.
- Don't scatter guards until the state stops looking unsafe. Coverage arrived at by adding one at a time protects nothing in particular and costs on every path.
- Don't call one guarded region from inside another without knowing the order everywhere. That is the arrangement that seizes up, and it does so only under interleavings you will not see while developing.

## Checklist
- What is the invariant, and exactly where does it stop holding?
- Does the guarded span match that stretch, or the enclosing method?
- Is anything slow enclosed — a disk read, a network call, a wait?
- How many places are guarded, and is the count falling because sharing narrowed?
- Does any guarded region enter another, and is the order the same everywhere?

## Notes
The advice to cover the invariant rather than the routine is right and is routinely
outvoted in practice, and it is worth being clear about what outvotes it. Wrapping the
whole routine is not merely the lazy reading of where the boundary goes; in most languages
it is also the form whose release cannot be forgotten, because it is attached to leaving
the scope rather than to a statement somebody has to write. That makes the wide region the
safe default and the narrow one the thing that has to be justified, which is the reverse of
how this card reads if the release mechanism is left out of it. A codebase that uses both
forms in quantity is usually not inconsistent — it is defaulting to the safe one and
narrowing where it measured a reason to.

The tension mostly dissolves once the routine boundary is treated as something you can
move. A guarded stretch extracted into its own routine gets a scope-bound release that
covers precisely the invariant, so the safety of the wide form and the span of the narrow
one stop being alternatives. What remains is the case where the extraction is genuinely
unavailable or would itself distort the code, and there the manual release is the honest
answer — but it should be recognised as taking on an obligation that grows with every
future branch, rather than as simply the tighter option.

The tension is real and is what makes this a decision rather than a rule. Guards are expensive, so you want few of them; state must be protected, so you cannot simply remove them. The trap is that the cheapest way to reduce the count is to make each one bigger — one guard around an entire operation instead of three around the parts that need it — and that satisfies the visible goal while making the invisible one worse. Time spent holding a guard is time other threads spend waiting, so a design with a handful of large regions can serialise a system more thoroughly than one with many small ones.

Deriving the boundary from the invariant rather than from the code structure is what resolves it. The question is not which method contains the shared field but across which stretch the rule about the state is temporarily violated — from the moment the first change is made until consistency is restored. That stretch is a property of the data and the rule, not of where the braces fall, and it is regularly narrower than the enclosing method and occasionally wider, which is why it has to be worked out rather than assumed.

The enclosed slow operation is the specific failure worth watching for, because it is invisible in review and catastrophic in production. A region widened for convenience quietly comes to contain a call that waits on something outside the process. The guard is now held for the duration of that wait, every other thread needing it is stopped for the same duration, and a mechanism intended to protect a few bytes of state has become the system's throughput limit. Nothing in the code looks wrong; the fault is entirely in what the boundary happens to enclose.
