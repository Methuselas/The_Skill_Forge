---
object_id: PAT_take_the_simplest_lock_type_that_does_the_job
object_type: pattern
name: Take the Simplest Lock Type That Does the Job
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
- locking
- deadlock
- raii
cross_links:
- rel: related_to
  target_object_id: PAT_break_one_of_deadlocks_four_conditions
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: PAT_dont_call_unknown_code_while_holding_a_lock
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Take the Simplest Lock Type That Does the Job

## Pattern Rule
**IF** you are guarding a critical section and choosing which lock construct to write
**THEN** take the least capable one that covers the case — the plain scope-bound guard for a single mutex held for a scope, the multi-mutex guard when more than one is needed, the shared guard when many readers must proceed together, and the flexible one only when you genuinely need deferring, timing, moving, or unlocking early
**ELSE** where the mutex is locked and unlocked by hand at all, none of these has been chosen yet and that is the first thing to fix.

## Do
- Start from the guarantee they all share, because it is the reason to use any of them: each binds its mutex on construction and releases it on destruction, so the release happens on every path out of the scope including the one an exception takes.
- Take all the mutexes you need in one step when you need more than one. The multi-mutex guard acquires them as a single operation, which means the acquisition order stops mattering — it removes the cycle condition by construction rather than by everyone remembering a convention.
- Reach for the shared guard where the access pattern is many readers and few writers. Any number of readers may hold it at once while a writer excludes them all, which does not remove contention but does stop readers queueing behind each other.
- Measure the shared guard against the exclusive one rather than assuming it wins, because its own machinery is heavier and can cost more than the queueing it removes. Ten readers and one writer over a table of some ninety thousand entries — a read-to-write ratio of about a hundred to one, which is as favourable as this gets — measured only about fifteen percent faster than exclusive locking on one Linux build, and about twice as slow on one Windows build. The access pattern argues for the shared guard; whether it pays is a property of the implementation you are running on.
- Reserve the flexible lock for the capabilities that distinguish it, and know what they are: constructing without a mutex, constructing without locking, locking and unlocking repeatedly, deferring the lock, attempting it with a timeout, and moving it. It is more expensive than the plain guard, so those capabilities should be ones you are using.
- Use a steady clock for any timed attempt. A clock that can be adjusted makes a timeout mean something different depending on what happened to the system time while you waited.

## Don't
- Don't hand-write the lock and unlock calls around a critical section. An exception thrown inside leaves the mutex held forever, and so does any early return added later by someone who did not notice the unlock at the bottom.
- Don't hand the multi-mutex guard a mutex this thread already holds. Unless the mutex is a recursive one the behaviour is undefined, and what it usually does in practice is deadlock.
- Don't write the guard without a name. An unnamed guard is a temporary: it locks and unlocks within the one statement that constructs it, and every line after it — the lines you meant to protect — then runs with the mutex free. Nothing fails, nothing reports, and the section is simply unsynchronized, which makes this worse than forgetting the guard entirely because the code reads as though it is protected.
- Don't reach for the flexible lock as a default because it can do everything. Capability here costs something at every acquisition, and a lock that can be unlocked early is also a lock a reader has to check for early unlocking.

## Checklist
- Is the mutex acquired and released by an object's lifetime rather than by statements?
- How many mutexes does this section need, and if more than one, are they taken in a single step?
- Is the access pattern many-readers-few-writers, and if so is the shared guard being used?
- If the flexible lock is used here, which of its extra capabilities is being exercised?
- Does any timed attempt use a clock that could be adjusted underneath it?

## Notes
The four constructs are usually presented as a feature list, which makes the choice look like a matter of taste. Read as a ladder of capability with a cost attached to each rung, it becomes a decision with an obvious default: the plain guard, until something specific forces you upward.

The multi-mutex guard deserves particular attention because it does more than save typing. Acquiring several mutexes atomically is the mechanism that removes the classic ordering deadlock — two threads taking the same two mutexes in opposite orders — without requiring a global acquisition convention that every future contributor has to know about and honour. Where it applies, it is strictly better than the convention.

Reader-writer locking is worth being clear-eyed about. It does not solve contention; it narrows it, by letting the operations that cannot interfere with each other proceed together. Whether that is a gain depends on the read-to-write ratio, and on a workload that writes often it can cost more than the plain exclusive lock it replaced.
