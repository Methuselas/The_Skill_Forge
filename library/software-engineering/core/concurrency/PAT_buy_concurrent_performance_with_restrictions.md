---
object_id: PAT_buy_concurrent_performance_with_restrictions
object_type: pattern
name: Buy Concurrent Performance With Restrictions, Not Cleverness
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
- design
- data_structures
- threading
- simplicity
cross_links:
- rel: prerequisite_for
  target_object_id: PAT_trade_exact_ordering_for_independent_substructures
- rel: prerequisite_for
  target_object_id: PAT_merge_concurrent_operations_into_one_before_applying_them
- rel: related_to
  target_object_id: PAT_make_every_concurrent_operation_a_complete_transaction
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: PAT_estimate_a_concurrent_designs_ceiling_before_building_it
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Buy Concurrent Performance With Restrictions, Not Cleverness

## Pattern Rule
**IF** a shared data structure is too slow and you are considering a more sophisticated synchronization scheme
**THEN** first inventory what your application guarantees about how the structure is used, and spend those guarantees instead — each one removes synchronization rather than optimizing it
**ELSE** where the usage genuinely is unrestricted in every dimension, the sophisticated implementation is what is left, and it should be entered knowing that.

## Do
- Ask the questions that have exploitable answers, one at a time. Is there one writer? Are producers and consumers separated in time rather than running together? Is there a known upper bound on size? Are there periods when nothing modifies the structure? Each yes deletes work: a queue with one producer and one consumer needs no atomic index at all, only an atomic size, and is wait-free.
- Take the wins from phase separation. A structure filled by many threads with no concurrent reading, then drained with no concurrent writing, has a simple correct answer for each half — an atomic index reserving slots — and it is the *overlap* of the two phases that creates every difficulty.
- Provide an unguarded operation for a genuinely single-threaded phase where the gap is large enough to be worth the caller's discipline. A structure populated by one thread up front and then worked by many is a common shape, and the unlocked fill is far faster than the guarded one.
- Amortize the guard over a batch where the callers have several items to hand. Pushing a thousand elements under one acquisition beats a thousand acquisitions, because the guarded region was cheaper than the locking around it — and be clear what this does not do: it does not make the operation scale, and it lengthens the wait for every other thread. It pays when threads mostly use the structure, and can lose when they mostly do other work.
- Keep the rare hard case off the fast path instead of designing for it. Check an atomic flag unguarded, and only if it indicates the rare condition take a lock and check again under it — the second check is what stops several threads that all saw the condition from all acting on it. Growing the storage is the usual case; any situation that is infrequent and awkward to do lock-free fits the same shape.
- Reconsider the data structure entirely when it is a linked one. Per-node locks deadlock as soon as an operation needs two of them, and a lock over the whole structure serializes every traversal; copying a region into thread-local form, or partitioning the graph so threads touch disjoint nodes, is frequently the better answer than making the structure itself concurrent.

## Don't
- Don't build the general version first. Unnecessary generality costs performance in a concurrent structure specifically, because every capability you support is a state the synchronization must account for even when nobody uses it.
- Don't take a restriction you cannot enforce or document. An unguarded operation on a shared type is a loaded weapon; it earns its place only where the phase boundary is real and stated, not assumed.
- Don't skip the simple guarded version. It is the baseline every alternative must beat, it is usually adequate, and it is enormously easier to establish correct — a distinction that matters most when the alternative is lock-free code, which is hard to write and much harder to debug.
- Don't reach for a more elaborate lock as the first upgrade. A shared-read lock did not improve read-only scaling at all on a short critical section and made the writing operations worse, because its extra machinery costs more than the region it protects; it pays only when the guarded work is long and mostly reading.

## Checklist
- How many threads write to this structure — and is it really more than one?
- Do the filling and draining phases overlap in time, or could they be separated?
- Is there a maximum capacity you could know in advance?
- Could callers batch their operations, and do they mostly use this structure or mostly do other work?
- What is the simple guarded implementation's throughput, and is it actually insufficient?

## Notes
The reason restrictions pay so much better than optimization here is that they change what has to be synchronized rather than how fast the synchronization runs. A single-producer queue is not a faster version of a multi-producer queue; it is a structure where two of the three shared variables stopped being shared. No amount of tuning a general implementation reaches that.

There is a strong asymmetry between producing and consuming that is worth carrying as a design instinct. Handling only producers, or only consumers, is straightforward — one atomic counter hands out disjoint slots and nothing else is needed. Handling both at once is where the complexity is, because the two roles meet at the same location and one of them must wait. Any application fact that separates the roles, in time or across threads, is worth a great deal.

One measured comparison against a genuinely lock-free stack is the useful summary: with a good lock, the guarded version offers reasonable performance and is far simpler; the lock-free version was justified on one of the two architectures tested and not the other. Complexity that is sometimes justified is still complexity to be entered deliberately.
