---
object_id: PAT_know_when_two_accesses_are_a_data_race
object_type: pattern
name: Know When Two Accesses Are a Data Race
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
- memory_model
- undefined_behavior
- threading
cross_links:
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: related_to
  target_object_id: PAT_treat_undefined_behavior_as_a_whole_program_assumption
- rel: related_to
  target_object_id: PAT_weaken_a_memory_order_only_against_a_measurement
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Know When Two Accesses Are a Data Race

## Pattern Rule
**IF** two threads reach the same object and at least one of them writes
**THEN** establish that one of exactly two escapes applies — the access is through an atomic operation, or one access is ordered before the other by a synchronization relationship — because if neither holds the program has a data race and the standard gives you nothing at all
**ELSE** where every thread that touches the object only reads it, and nothing writes for the object's whole lifetime, there is no race and no synchronization is needed.

## Do
- Check the condition against a *memory location* rather than against a variable name, because they are not the same thing. Each scalar object occupies its own location, but adjacent bit fields of non-zero length share one — so two threads writing two differently named bit fields in the same struct are writing the same location and are racing.
- Reach for the second escape as often as the first. Establishing that one access happens before the other is what a mutex actually does: the synchronization primitives create these orderings, and the orderings then cover ordinary non-atomic data too. That is why locking a mutex around plain variables is sufficient and does not require the variables to be atomic.
- Retrofit atomicity through a reference where you cannot change the object's type. A counter that is a plain member of a type you do not own, or an element of an array handed to you, can be accessed atomically by binding an atomic reference to it — provided every access for that period goes through one.
- Treat the absence of a race as the property to establish, not the presence of one to hunt for. A race is undefined behaviour, so the reasoning has to be a proof that it cannot occur rather than an observation that it has not yet.

## Don't
- Don't conclude that a program is fine because it produces the right answer. A data race makes the whole program undefined, so a run that looks correct is not evidence of anything — and the compiler is entitled to have optimized on the assumption the race cannot happen.
- Don't assume distinct member variables are automatically distinct locations. The bit-field case is the exception, and it is invisible at the point of access — nothing at the call site distinguishes writing a bit field from writing an ordinary member.
- Don't picture a racing read as returning either the old value or the new one. That is a real guarantee, but it is one a register has to be built to provide, and it is not what an unsynchronized access gives you — a read overlapping a write may produce a value that was never written at all. The intuition matters even though the language's answer is simply undefined behaviour, because "it will get one or the other" is the reasoning people use to talk themselves out of synchronizing.
- Don't count a read against a read. Two threads reading the same location, with nothing writing, is not a race no matter how many threads there are, which is why immutable data needs no protection at all.

## Checklist
- Which memory locations does more than one thread reach?
- For each, does any thread write?
- Where one does, is the access atomic, or is there a synchronization relationship ordering the accesses?
- Are any of the locations in question bit fields adjacent to other bit fields?
- Could the data be made immutable instead, removing the question?

## Notes
The definition is worth carrying precisely rather than approximately, because the approximate version — "concurrent access with a write" — omits the second escape and therefore makes locking look like a separate mechanism from atomics. It is not. Locks work *because* they establish the ordering relationship the definition names, and that relationship then extends to the ordinary data the lock protects.

The bit-field clause is the part most likely to be news. Two adjacent bit fields are one memory location, so a program that carefully gives each thread its own field is still racing, and no amount of inspection at the access sites will show it. The fix is either to separate them with something that forces distinct locations or to synchronize them together.

This sits underneath the ordering decisions rather than beside them. The question of which memory order to specify only arises once you have decided an access will be atomic; this is the earlier question of whether it has to be.
