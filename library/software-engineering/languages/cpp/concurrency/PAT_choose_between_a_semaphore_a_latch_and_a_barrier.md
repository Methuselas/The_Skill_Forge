---
object_id: PAT_choose_between_a_semaphore_a_latch_and_a_barrier
object_type: pattern
name: Choose Between a Semaphore, a Latch, and a Barrier
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- coordination
- threading
- synchronization
cross_links:
- rel: related_to
  target_object_id: PAT_match_the_problem_to_a_known_coordination_shape
- rel: related_to
  target_object_id: PAT_wait_on_a_predicate_not_on_a_notification
- rel: related_to
  target_object_id: PAT_take_the_simplest_lock_type_that_does_the_job
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Choose Between a Semaphore, a Latch, and a Barrier

## Pattern Rule
**IF** threads must coordinate on counts or on phases rather than on exclusive access to one thing
**THEN** pick by the shape of the coordination — a semaphore where a count of permits limits access and the acquiring and releasing threads may differ, a latch where a group waits once for a count to reach zero, a barrier where they do that repeatedly — rather than assembling the same behaviour from a condition variable
**ELSE** where one thread waits for one value produced by another, a future carries the value and the readiness together and none of these is the right shape.

## Do
- Start from the semaphore's distinguishing property, because it is the one that decides most cases: a semaphore is not bound to a thread. The acquire and the release may happen on different threads, which a mutex forbids by design — and that is what makes a semaphore usable for signalling between a sender and a receiver rather than only for guarding a region.
- Read the counting form as permits for interchangeable resources. The counter is how many are available; acquiring takes one and blocks at zero, releasing returns one. The binary form is not a separate facility, only the alias where the maximum is one.
- Use a latch when the wait happens once. It counts down, the waiters proceed when it reaches zero, and it cannot be reset — which suits one task performed by several threads, and suits nothing that repeats.
- Use a barrier when the same group must synchronize again each round. It releases the waiters and then resets itself, so it fits repeated work in phases where every thread must finish phase n before any begins phase n plus one.
- Reach for the barrier specifically when something must happen *between* phases. Its completion step runs once, when the counter hits zero, before the waiters are released — which is exactly where you put the work that must see the finished phase and must not race with the next one.

## Don't
- Don't build these out of a condition variable when one of them fits. They enable nothing you could not already write, and that is not the argument for them: they are far easier to use correctly, and are often faster because implementations commonly build them without locks. The hand-assembled equivalent carries the predicate obligation and the lost-wakeup hazard; these carry neither.
- Don't try to reuse a latch. Single use is its definition rather than a limitation of the implementation, and a workflow that needs a second round needs a barrier.
- Don't decrement either by more than the counter holds, or by a negative amount. Both are undefined, and the arithmetic is easy to get wrong when the count is computed from the number of workers.
- Don't confuse a barrier with a memory barrier. The word is shared and the concepts are unrelated — one coordinates threads, the other constrains reordering.

## Checklist
- Does the coordination limit how many threads proceed, or when they proceed?
- If a count of permits, do the acquire and release happen on the same thread or different ones?
- Does the group wait once, or once per round?
- Is there work that must run between phases, seeing one finished and preceding the next?
- Is any latch being reset or reused?

## Notes
The honest framing of these facilities is the one Grimm gives, and it is worth keeping because it sets expectations correctly: they address no use case that was unavailable before. Everything here could be assembled from threads, futures, or condition variables with locks. What they change is how likely you are to assemble it correctly, and how much the assembly costs.

That makes the decision less about capability than about which shape you can name. A count of interchangeable permits, a one-time gate, and a repeating phase boundary are three recognisable arrangements, and picking the facility whose name matches the arrangement leaves code that states what it is doing — where the same thing built from a mutex, a flag, and a condition variable states only the mechanism.

The completion step is the barrier's genuinely distinctive feature and the reason to prefer it over a latch per round. Work that must observe the finished phase and complete before the next one starts has nowhere safe to live otherwise: run it in one of the participating threads and the others may already have moved on, run it after the wait and every thread runs it.

The unbound nature of the semaphore is the other thing to carry away, because it is what a mutex cannot do. A mutex must be released by the thread that took it; a semaphore released by a different thread is the normal case rather than an abuse, which is what lets one thread's completion admit another thread to a region it never entered.

The claim that these are often cheaper than the assembled equivalent has been measured on a ping-pong benchmark, where two threads hand control back and forth as fast as they can. Condition variables were the slowest at about 0.52; an atomic flag, the only always-lock-free atomic type, was the fastest at about 0.31; an atomic boolean sat between at 0.38. Semaphores came in at 0.33 — close enough to the atomic flag to suggest they are built on the same machinery, and well clear of the condition variable they would replace. That is the empirical form of this card's argument: choosing the facility that names your arrangement is not a trade of speed for clarity.
