---
object_id: PAT_wait_on_a_predicate_not_on_a_notification
object_type: pattern
name: Wait on a Predicate, Not on a Notification
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- condition_variables
- deadlock
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_take_the_simplest_lock_type_that_does_the_job
- rel: related_to
  target_object_id: PAT_make_the_acquire_actually_observe_the_release
- rel: related_to
  target_object_id: PAT_match_the_problem_to_a_known_coordination_shape
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Wait on a Predicate, Not on a Notification

## Pattern Rule
**IF** one thread must wait until another has made something ready, and you are using a condition variable to arrange it
**THEN** always wait with a predicate, and modify the variable that predicate tests while holding the same mutex the waiter uses — even when that variable is atomic — because a bare wait can miss a notification that arrives too early, and an unprotected flag leaves a window where it can miss one that arrives at the wrong instant
**ELSE** where the waiter only ever needs a single result computed once, a future carries the value and the readiness together, and none of this arises.

## Do
- Understand what the predicate form actually expands to, since that is the whole explanation: waiting with a predicate is a loop that tests the predicate and waits only while it is false. The test happens *before* any waiting, which is what makes an early notification harmless, and again after every wake, which is what makes a wake with no notification harmless.
- Modify the tested variable under the mutex, and treat this as non-negotiable rather than as belt-and-braces. Making it atomic is not sufficient: between the predicate returning false and the thread entering the wait there is a window, and a notification delivered inside that window is lost with the waiter then sleeping indefinitely. Holding the mutex across the modification is what guarantees the notification is only sent when the waiter is genuinely waiting.
- Send the notification after releasing the mutex where you can, so the woken thread does not immediately block trying to reacquire what the notifier still holds.
- Choose between waking one waiter and waking all of them on what the waiters do. Waking one is right when any single waiter can consume the event; waking all is right when the state change is relevant to every one of them.
- Prefer a facility that carries the state when the communication is one-shot. Condition variables are stateless signalling; a one-time handoff of a value is what futures are for, and it removes both failure modes below.

## Don't
- Don't call the bare wait without a predicate. It has no memory of anything, so a notification sent before the waiter arrives is simply gone — and this is timing-dependent, which means the version that deadlocks is the one that runs on a loaded machine rather than the one you tested.
- Don't assume a wake means the condition holds. A waiter may be woken with no notification having occurred at all, which is permitted and does happen — a wake stolen by another thread that runs first is one ordinary cause.
- Don't reason about the atomic flag in isolation from the wait. The flag being atomic makes reading it safe; it does nothing about the ordering between testing it and going to sleep, and that ordering is the whole problem.

## Checklist
- Does every wait call pass a predicate?
- Is the variable the predicate tests modified while the notifier holds the waiter's mutex?
- Is that true even where the variable is atomic?
- Is the notification sent after the mutex is released?
- Should this wake one waiter or all of them, and does the code match?

## Notes
Both hazards come from the same property: a condition variable holds no state. It is a mechanism for waking threads that are currently waiting, and it has no concept of an event that occurred earlier. The predicate is the state the mechanism lacks — it is the memory that lets a waiter discover that the thing already happened.

The requirement to modify the flag under the mutex is the part most often argued with, because an atomic flag looks like it should be enough. Walking the window makes it concrete: the waiter tests the predicate, gets false, and has not yet entered the wait. A notifier that sets an unprotected atomic and notifies in that interval sends its notification to nobody, and the waiter then enters a wait that will never end. Taking the mutex across the modification means the notifier cannot be in that interval, because the waiter holds the mutex throughout it.

Grimm's broader recommendation is worth carrying alongside the mechanics: for most use cases, task-based communication is the less error-prone way to synchronize threads. This card is what to do when a condition variable is genuinely the right shape — repeated signalling, several waiters, a condition that can become true more than once — rather than an argument for reaching for one.
