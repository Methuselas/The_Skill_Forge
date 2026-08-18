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
  target_object_id: PAT_atomic_steps_do_not_compose_into_a_safe_whole
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: related_to
  target_object_id: PAT_break_one_of_deadlocks_four_conditions
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
The tension is real and is what makes this a decision rather than a rule. Guards are expensive, so you want few of them; state must be protected, so you cannot simply remove them. The trap is that the cheapest way to reduce the count is to make each one bigger — one guard around an entire operation instead of three around the parts that need it — and that satisfies the visible goal while making the invisible one worse. Time spent holding a guard is time other threads spend waiting, so a design with a handful of large regions can serialise a system more thoroughly than one with many small ones.

Deriving the boundary from the invariant rather than from the code structure is what resolves it. The question is not which method contains the shared field but across which stretch the rule about the state is temporarily violated — from the moment the first change is made until consistency is restored. That stretch is a property of the data and the rule, not of where the braces fall, and it is regularly narrower than the enclosing method and occasionally wider, which is why it has to be worked out rather than assumed.

The enclosed slow operation is the specific failure worth watching for, because it is invisible in review and catastrophic in production. A region widened for convenience quietly comes to contain a call that waits on something outside the process. The guard is now held for the duration of that wait, every other thread needing it is stopped for the same duration, and a mechanism intended to protect a few bytes of state has become the system's throughput limit. Nothing in the code looks wrong; the fault is entirely in what the boundary happens to enclose.
