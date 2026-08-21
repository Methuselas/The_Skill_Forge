---
object_id: PAT_reach_for_a_fence_only_when_no_atomic_carries_the_order
object_type: pattern
name: Reach for a Fence Only When No Atomic Carries the Order
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
- memory_model
- atomics
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_specify_a_memory_order_the_operation_can_actually_carry
- rel: related_to
  target_object_id: PAT_make_the_acquire_actually_observe_the_release
- rel: related_to
  target_object_id: PAT_weaken_a_memory_order_only_against_a_measurement
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: medium
references: []
variants: []
---

# Reach for a Fence Only When No Atomic Carries the Order

## Pattern Rule
**IF** you need to stop memory operations being reordered across a point in the code
**THEN** attach the ordering to an atomic operation you are performing anyway, and use a standalone fence only when there is no such operation to carry it — because a fence orders everything around it rather than accesses relative to one variable, which makes it both broader than you usually need and more expensive
**ELSE** where the reordering to prevent is between a thread and a signal handler running on that same thread, the thread fence is the wrong tool and the signal fence is the one that fits.

## Do
- Frame reordering in terms of the four adjacent pairs, since that is what a barrier acts on: a read then a read, a read then a write, a write then a read, and a write then a write. A barrier placed between two operations guarantees that particular pair is not reordered.
- Know what each of the three does. The full fence prevents every reordering except a write followed by a read. The acquiring fence stops a read before it being reordered past any read or write after it. The releasing fence stops a write after it being reordered past any read or write before it.
- Reserve fences for the case where no atomic operation is available to carry the ordering, which is their genuine advantage: a fence requires no atomic variable at all, so it can order plain accesses that have no atomic to attach to.
- Keep the pairing discipline whichever you choose. Acquiring and releasing operations work in pairs, and where the ordering rides on atomic operations rather than fences, both sides must name the same atomic variable.
- Remember that reordering is only a risk where the accesses are non-atomic or relaxed. Operations already carrying stronger orders are constrained by those.

## Don't
- Don't reach for a fence as the default way to express ordering. It is the heavier instrument: an ordered atomic operation constrains accesses with respect to one variable, while a fence constrains everything crossing it, so the fence gives up optimization the narrower form would have kept.
- Don't expect the signal fence to synchronize threads. It orders a thread against a handler executing on that same thread, which is a compiler-level constraint rather than an inter-processor one, and using it between threads orders nothing.
- Don't assume the full fence prevents all reordering. A write followed by a read is the exception it does not cover, and that pair is exactly the one behind several of the classic counterintuitive results.

## Checklist
- Is there already an atomic operation at this point that could carry the ordering?
- If a fence is being used, which of the four adjacent pairs is it there to prevent?
- Is the fence a thread fence or a signal fence, and does that match what is being ordered?
- Are the accesses being protected non-atomic or relaxed, so that reordering was actually a risk?

## Notes
The distinction that makes this a decision rather than a style preference is what each construct scopes over. An acquiring load constrains what may move across *that load*, relative to *that variable*, which is a narrow and cheap promise. An acquiring fence constrains what may move across that point in the program at all. The second is strictly more restrictive, and more restrictive means less room for the compiler and processor to optimize.

That said, the confidence on this card is deliberately lower than its neighbours. The precise guarantees fences give — and how they interact with atomic operations of various orders — are among the subtlest parts of the memory model, and Grimm himself notes that a great deal of effort goes into getting the acquire and release fence definitions and their consequences right. Treat the summary above as orientation and check the standard before writing one.

The signal fence is easy to overlook and worth knowing exists, because the problem it solves has no other clean answer. Code interrupted by a handler on its own thread faces reordering by the compiler but not by the processor, and a full thread fence would emit hardware instructions that are pure cost for that case.
