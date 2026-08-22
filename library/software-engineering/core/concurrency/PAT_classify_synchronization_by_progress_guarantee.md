---
object_id: PAT_classify_synchronization_by_progress_guarantee
object_type: pattern
name: Classify Synchronization by the Progress It Guarantees
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- threading
- locking
- lock_free
- design
cross_links:
- rel: related_to
  target_object_id: PAT_break_one_of_deadlocks_four_conditions
- rel: related_to
  target_object_id: PAT_match_the_lock_to_the_length_of_the_critical_section
- rel: related_to
  target_object_id: PAT_atomic_steps_do_not_compose_into_a_safe_whole
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Classify Synchronization by the Progress It Guarantees

## Pattern Rule
**IF** you are choosing between a lock, a lock-free retry loop, and a single atomic operation for a piece of shared state
**THEN** decide it on what each guarantees about threads making progress, not on which one you expect to be faster, because the speed ordering does not hold and the progress properties do
**ELSE** where the operation has a native atomic instruction and no surrounding invariant, take it — that case is both the simplest and the strongest, and there is nothing to weigh.

## Do
- Hold the three guarantees precisely, because the differences are what you are buying. Wait-free: every thread executes its operation and advances, with no retry and no waiting, though contention still makes each operation slower. Lock-free: several threads may attempt the update and exactly one succeeds, the rest discard their work and retry — so the program as a whole always advances even though a given thread may not. Lock-based: at most one thread can advance, and even that is not assured, since the holder may itself be blocked on something else.
- Reach for a retry loop built on compare-and-exchange whenever the operation you need has no atomic instruction. Read the value, compute the new one from it, and conditionally write it back only if the variable still holds what you read; loop until the write takes. The shape generalizes to any read-modify-write, which matters because the set of native atomic operations is small — integer addition is there, multiplication is not, on any common architecture.
- Buy the structural properties rather than the speed. A lock-free scheme cannot deadlock, so it needs none of the machinery for avoiding deadlock and none for the livelock that machinery introduces. It cannot convoy, since winning once confers no advantage on the next attempt. It inverts priority far less, because the thread that reaches the atomic operation first is the one that commits.
- Price the retries honestly before committing to lock-free. Under heavy contention the losing threads burn full CPU on work they will throw away, and they take those cycles from unrelated threads doing useful computation elsewhere in the program.
- Treat lock-free as the last rung of a ladder rather than a starting point, and check four things before stepping onto it. Whether the measured performance requirement actually demands it; whether an existing library already provides the structure, since the well-known ones do exist and are written by specialists; whether the expertise to maintain it is present and will stay present; and whether the platform supplies genuinely lock-free atomics for the types involved, which is a property to verify rather than assume. A no to any of them makes a guarded implementation the better engineering answer, and the guarded one is also what the lock-free version will need to be checked against.
- Weigh what it costs to reason about. A lock-based design has a checkable rule: name the lock that guards each piece of shared data and show that nothing touches it unheld. A lock-free design has no critical section to point at, so correctness means arguing about every interleaving of the atomic operations and about the visibility of all the surrounding data — which is why these are hard to get right and belong behind a module boundary.

## Don't
- Don't accept "lock-free is faster" as the reason. An optimized spinlock outperformed a compare-and-exchange loop on the same shared counter, and came close to the native atomic instruction; the measured ordering depends on the operation, the contention, and the processor generation.
- Don't treat wait-free as a scaling guarantee. Every thread advancing is not every thread advancing quickly — the hardware still serializes exclusive access to the line, so the cost per operation climbs steeply with thread count whatever the classification says.
- Don't count on combining two locks safely. Mutexes do not compose: there is no general way to make one guard out of two, which is why multi-lock code turns into ordering disciplines, try-and-back-off schemes, and the livelocks those produce.
- Don't let the word "nonblocking" carry one meaning across a conversation, because it names at least three unrelated properties. Of a correctness condition, it means any pending call can be given some valid answer immediately. Of a progress condition, it means no thread's delay can prevent others from advancing. Of an interface, it means a call returns before the work it requested is finished. An object can satisfy any one of these and fail the others, so a claim using the bare word has said less than it appears to.
- Don't leave a lock-free scheme spread through application code. The complexity is manageable only when it is confined to a module with a stated interface and stated guarantees, where the callers neither know nor care which implementation is inside.

## Checklist
- Which of the three progress guarantees does this design actually provide?
- Is there a native atomic operation for what you need, or does it require a retry loop?
- Under your expected contention, how much work gets discarded and redone?
- If this is lock-based, can you name the lock guarding every piece of shared state here?
- Is the synchronization confined to a module, or has it leaked into the callers?

## Notes
The reason to lead with progress rather than speed is that speed is contingent and the guarantees are not. Lock implementations vary enormously — a mutex tuned for long waits and a spinlock tuned for a few cycles differ by more than the gap between locking and not locking — so any general claim about which category is faster is really a claim about two particular implementations on one machine.

Where the categories genuinely differ is in the failure modes they admit. Deadlock, livelock, convoying, and priority inversion are all properties of holding exclusive access across an unbounded interval, and the lock-free classification removes the interval rather than managing it. Convoying is worth recognizing by name because it is the one that hides: a thread releases the lock, races through its next task, and reacquires before the sleeping competitors have woken, so one thread runs at full speed while the others make no progress and nothing in the code looks wrong.

The cost side has a shape too. Locks waste time waiting; lock-free schemes waste time computing results that get discarded. Neither is free under contention, and the choice between wasting on the threads that lose and blocking the threads that wait is a real design decision rather than a technicality.
