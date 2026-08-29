---
object_id: PAT_make_the_acquire_actually_observe_the_release
object_type: pattern
name: Make the Acquire Actually Observe the Release
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
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_weaken_a_memory_order_only_against_a_measurement
- rel: related_to
  target_object_id: PAT_specify_a_memory_order_the_operation_can_actually_carry
- rel: related_to
  target_object_id: PAT_know_when_two_accesses_are_a_data_race
- rel: prerequisite_for
  target_object_id: PAT_reach_for_a_fence_only_when_no_atomic_carries_the_order
- rel: related_to
  target_object_id: AP_make_shared_state_safe_in_cpp
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Make the Acquire Actually Observe the Release

## Pattern Rule
**IF** you have paired a releasing store with an acquiring load on the same atomic and intend the data written beforehand to be visible to the reader
**THEN** ensure the reader keeps loading until it actually observes the value the writer stored, because the visibility guarantee is conditional on that observation and buys you nothing if the load happens to run first
**ELSE** where the reader has been ordered after the writer by some other means — it was started by the writer, or joined to it, or woken through a synchronization primitive that already establishes the ordering — the observation has been established elsewhere and no loop is needed.

## Do
- Read the guarantee with its antecedent attached, since the antecedent is the whole difficulty. Everything the writer did before its releasing store becomes visible after the reader's acquiring load *if* that store happens before that load. It is not a promise about the two annotations; it is a promise about what follows once one particular thing has occurred.
- Supply the antecedent with a loop that spins until the flag reads as set. That loop is not a busy-wait bolted on for lack of a better mechanism — it is the construct that establishes the condition the guarantee depends on.
- Look for the same shape wherever a thread checks a flag once and proceeds. A single unguarded load that finds the flag clear has not synchronized with anything, so the ordinary data it goes on to read is being read with no ordering at all — which for non-atomic data is a race and therefore undefined.
- Prefer a facility that establishes the ordering for you where one fits. Waiting on the atomic itself, or on a condition variable, or joining the writing thread all create the relationship without a spin loop and without this trap.

## Don't
- Don't treat the pairing of the two annotations as sufficient. Writing the releasing order on one side and the acquiring order on the other is necessary and is not the guarantee; code that pairs them correctly and then reads the flag once is broken in exactly the way that pairing looks like it should prevent.
- Don't conclude from a passing test that the observation is established. Whether the reader happens to see the store is a timing question, so the failing interleaving is the rare one — and on a machine where the store lands quickly it may never appear during development at all.
- Don't reason about the data being published while ignoring the flag. The whole ordering hangs off the one atomic variable both sides name; the data has no ordering of its own and inherits all of it from that observation.

## Checklist
- Does the reader loop until it observes the written value, or read the flag once?
- If it reads once, what happens on the path where the flag is not yet set?
- Is the ordering established by some other relationship — thread creation, joining, a waiting primitive?
- Is the data being published non-atomic, making the unsynchronized path a race rather than merely a stale read?

## Notes
Grimm reports this as the trap his readers and students fall into most often, and the reason is that the correct and incorrect versions differ by one loop rather than by any annotation. Both name the releasing and acquiring orders, both look like textbook acquire-release publication, and only one of them establishes the condition under which the guarantee applies.

The conditional structure is worth stating as a sentence you can check code against: the relationship exists between a particular store and a particular load, not between the two threads in general and not between the two annotations. Until the load has returned the stored value, the two threads have no ordering relative to each other at all, and "before" and "after" have no content between them.

That is also why the remedy so often looks like a busy-wait and should not be read as one. The loop is doing semantic work — repeating the load until the relationship is established — rather than merely passing time until the other thread gets round to it.
