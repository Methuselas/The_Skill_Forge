---
object_id: PAT_separate_per_thread_data_by_a_cache_line
object_type: pattern
name: Separate Per-Thread Data by a Full Cache Line
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
- performance
- threading
- memory
- shared_state
cross_links:
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: related_to
  target_object_id: PAT_check_for_memory_saturation_before_adding_threads
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Separate Per-Thread Data by a Full Cache Line

## Pattern Rule
**IF** you have given each thread its own slot in a shared array or structure so that nothing is actually shared
**THEN** check how far apart those slots are in memory and pad them to at least a full cache line, because the hardware's unit of exclusive access is the line and not the variable
**ELSE** where each thread's state lives in its own allocation — a local variable, a separately allocated block — the separation already exists and no padding is needed.

## Do
- Take the line size as the unit that matters: sixty-four bytes on x86 processors, and the quantity in which data moves between memory and every level of cache. Eight adjacent 64-bit values therefore occupy one line and are, to the coherence hardware, one object.
- Recognize the performance signature. An array of per-thread counters scaled exactly like a genuinely shared counter up to eight threads, then began improving — because past eight the array spans two lines, and two processors can hold one each.
- Pad or align deliberately once the slots are identified. Spacing per-thread state at least sixty-four bytes apart turned a program that barely scaled into one that scaled as expected, and left it roughly twice as fast at every thread count.
- Take the separation distance from the language where it offers one, rather than writing the number in. A portable constant for the minimum offset that avoids this interference — paired with one for the maximum offset that keeps data together on purpose — states the intent and follows the hardware it is compiled for, which a literal 64 does not.
- Accumulate into thread-local state and touch the shared result once. Adding to a shared accumulator on every step is the version that cannot scale; each thread summing privately and contributing its total at the end reduces the shared traffic to one access per thread.
- Suspect this whenever a structure is indexed by thread. The pattern that produces it is the reasonable-looking one — an array of partial results, a per-worker statistics block, a table of flags — and the sharing is created by the layout rather than by the code.
- Isolate cause from correlation by measuring the missing combination. Shared-and-guarded access was slow, unshared-and-unguarded access was fast, and concluding that sharing was the cause skips a case: unshared data that still shares a line. That case behaves like true sharing, which is what identifies the line rather than the variable as the contended thing.

## Don't
- Don't assume distinct variables are independent for performance purposes. Correctness-wise they are — writing to separate objects from separate threads is safe — but the coherence traffic does not know that the neighbours are unrelated.
- Don't fix it by making the slots atomic or adding a lock. Nothing is being raced; the cost is exclusive access to a line and additional synchronization only adds to it.
- Don't pad every structure defensively. This costs memory and cache capacity, and matters only where several threads write to nearby locations frequently — read-mostly neighbours do not contend.
- Don't expect this to show up as a hot function. The cost appears as poor scaling with no obvious contention in the code, which is why the layout has to be inspected rather than the logic.

## Checklist
- Which structures in this program are indexed or partitioned by thread?
- How many bytes apart are two adjacent threads' slots?
- Does scaling improve suddenly at the thread count where the structure exceeds one line?
- Could each thread accumulate privately and contribute once instead?
- Has an unshared-but-adjacent case been measured, or was sharing assumed to be the cause?

## Notes
The mechanism is cache coherence rather than mutual exclusion. When a processor takes exclusive access to a location in order to modify it, it takes the whole line; every other processor's copy of that line is now stale and must be refetched before any data in it can be touched. Two threads writing to different bytes of one line therefore hand the line back and forth, paying a main-memory-class cost per exchange, with no lock and no race anywhere in the program.

The same mechanism explains why locks get more expensive with thread count and not merely more contended. A lock necessarily contains shared data — that is how one thread signals another — so lock operations carry the same line-exclusivity cost that the counters do. Demonstrating it requires a lock small enough that several fit in one line, which a standard mutex at forty to eighty bytes does not; a spinlock or futex will.

There is a general measurement lesson embedded in how this was found, and it is worth more than the specific result. Two versions of a program that differ in two respects cannot tell you which respect mattered. The comparison here differed in both sharing and synchronization, the natural conclusion credited sharing, and constructing the fourth cell of the table — unshared, unsynchronized, but adjacent in memory — is what produced the actual explanation.
