---
object_id: PAT_match_the_lock_to_the_length_of_the_critical_section
object_type: pattern
name: Match the Lock to the Length of the Critical Section
library_path:
- software-engineering
- core
- concurrency
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- locking
- performance
- threading
- contention
cross_links:
- rel: related_to
  target_object_id: PAT_lock_the_smallest_region_that_must_be_atomic
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: PAT_separate_per_thread_data_by_a_cache_line
- rel: related_to
  target_object_id: PAT_give_each_waiter_its_own_location_to_spin_on
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Match the Lock to the Length of the Critical Section

## Pattern Rule
**IF** a guarded region has been measured as a bottleneck and you are considering how it is locked rather than how wide it is
**THEN** choose the lock from how long the lock is held — busy-waiting for spans of a few instructions, a sleeping mutex for anything longer — since that is what decides whether waiting should burn CPU or yield it
**ELSE** where the region is held long enough for the waiting threads to be better off asleep, the platform mutex is already the right answer and the tuning is elsewhere.

## Do
- Read the general-purpose mutex as a compromise rather than a default. It is somewhat inefficient for guarding a single instruction, reasonable for a computation of dozens of nanoseconds, and clearly best once the hold time gets long — a millisecond being very long at processor speeds.
- Use a spinlock where the wait is a handful of cycles, and expect the gain to be large. Guarding a shared counter, the sleep-and-wake path costs far more than the operation being guarded, and the CPU time burned spinning is a few instructions.
- Poll with a plain read before attempting the exchange. Acquiring by unconditionally writing the flag takes exclusive access to its cache line on every failed attempt, bouncing the line between processors while the holder is not even touching it; reading until the flag clears and only then exchanging lets every waiter keep a valid shared copy, and the line moves only when the value actually changes.
- Back off before retrying when an attempt fails on a lock you had just seen free, and randomize how long. Failing there means somebody took it in between, which is evidence of contention specifically — whereas simply finding the lock held tells you nothing. Doubling the delay after each such failure, up to a ceiling, and drawing the actual wait randomly from that range is what keeps competing threads from falling into lockstep and colliding again together.
- Price backoff's two costs against the traffic it saves. The critical section goes underused, because when the lock frees there may be nobody awake to take it — and that gets worse at higher contention, which is when it can least be afforded. And it is markedly unfair: a thread that released the lock may never observe contention at all and so never back off, letting it reacquire repeatedly while others wait.
- Yield the processor after a bounded number of failed attempts. An unyielding spinner looks to the scheduler like a thread doing useful work, so it accrues CPU time while the thread that would release the lock waits to be scheduled — the pathology the yield exists to prevent. Somewhere between eight and sixteen attempts before yielding works well across hardware.
- Pick the yielding call by measurement, not by name. On Linux, sleeping for a single nanosecond outperformed the dedicated yield call in practice; either way it is a system call and costs far more than an instruction, which is what the attempt budget is protecting.
- Consider making the lock the only handle to what it guards. A lock holding a pointer, which hands the pointer out on acquisition and takes it back on release, makes unguarded access to the data impossible to write by accident — and measured slightly faster than a flag-based spinlock more often than not.

## Don't
- Don't spin around a long critical section. Waiting threads consume whole cores doing nothing, and they take those cores from threads that would be doing real work, so the loss is larger than the contention it was meant to avoid.
- Don't ship a naive spinlock and conclude spinlocks are slow. Unoptimized — unconditional exchange, no yielding — its performance is genuinely terrible; the two refinements above are what make the category competitive.
- Don't carry a measured ranking of primitives across machines. The same benchmark orders spinlock, pointer-lock, retry loop, and native atomic differently on two processors a generation apart, with newer parts generally handling busy-waiting better.
- Don't tune the lock before checking the region it covers. A hold time long enough to make the mutex the right choice is often a sign the guarded span includes work that did not need guarding.

## Checklist
- How long is this lock actually held, in instructions?
- Does the waiting loop read before it writes?
- After how many failed attempts does a waiter yield, and was that number measured?
- How many cores would be spinning at peak contention, and what else could they be running?
- Was the primitive chosen from a measurement on the target hardware?

## Notes
The whole question is what a waiting thread should do with the time. Busy-waiting keeps the thread hot and ready to take the lock the instant it clears, at the price of occupying a core; sleeping releases the core, at the price of a wake-up latency that dwarfs a short critical section. Neither is better in general, and the crossover is a property of the hold time.

Any lock is at some disadvantage against a single atomic operation on the same data, and for a structural reason worth keeping: the lock scheme touches two shared locations, the lock and the data, where the atomic scheme touches one. That is a floor no amount of tuning removes, which is why an operation with a native atomic instruction is normally better served by it than by a well-written lock around it.

That the general-purpose mutex is a compromise rather than a mistake is worth stating, because the measurements here can read as an argument against it. It is the right default precisely because it does not assume the hold time. Programs willing to spend engineering effort on this — which is a narrow set — either write locks specialized for short guarded regions or take them from a library that does.
