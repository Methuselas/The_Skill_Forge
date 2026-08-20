---
object_id: PAT_trade_exact_ordering_for_independent_substructures
object_type: pattern
name: Trade Exact Ordering for Independent Sub-Structures
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
- data_structures
- scalability
- design
- threading
cross_links:
- rel: related_to
  target_object_id: PAT_buy_concurrent_performance_with_restrictions
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: related_to
  target_object_id: PAT_make_every_concurrent_operation_a_complete_transaction
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Trade Exact Ordering for Independent Sub-Structures

## Pattern Rule
**IF** a shared container is a scaling bottleneck and the program does not truly depend on the exact order in which elements come out
**THEN** replace it with several independent sub-containers, each claimed exclusively by one thread for the duration of an operation, accepting an order that is right on average rather than exactly
**ELSE** where downstream logic genuinely requires that elements emerge in the order they went in, this is unavailable and the ordering has to be paid for.

## Do
- Claim a sub-structure by taking it away rather than by locking it. An array of handles, one per sub-container, is enough: atomically exchange one with an invalid value to acquire it, and write it back when finished. A thread that finds an invalid value moves to the next, and having claimed one, it is the only thread there — so the sub-container itself needs no thread safety at all and can be an ordinary single-threaded one.
- Decide what a failed claim means for each operation. Adding should keep trying until it acquires one, or report that the structure is too busy after a bounded number of attempts. Removing may acquire a sub-container and find it empty, which means trying another; an atomic total count makes the genuinely-empty case cheap to answer.
- Check what ordering you are actually giving up before deciding it is too much. A conventional concurrent queue does not deliver its elements in order either: a thread can be preempted between taking an element and returning it, so two threads that dequeued in one order can return in the other. What is lost here is a matter of degree.
- Size the number of sub-structures against the thread count. Too few and threads collide on claims; the arrangement earns its keep when a thread usually finds a free one on the first or second try.
- Expect the win where the guarded version has none. Under many threads with elements expensive enough to copy, the split version scaled while a spinlock-guarded container held flat at its single-thread throughput and then declined slowly with locking overhead.

## Don't
- Don't apply it where order carries meaning. Sequenced operations, anything replayed, and anything where a later element supersedes an earlier one all break, and they break rarely and unreproducibly rather than immediately.
- Don't expect the disorder to be bounded tightly. Elements come out approximately in order, and large rearrangements happen when a thread is delayed — infrequent, and not impossible.
- Don't reach for it before eliminating the sharing outright. Splitting a shared structure into several is a weaker move than giving each thread its own data, and it is only needed where every thread must be able to reach every element.
- Don't leave the weakened guarantee undocumented. What a container promises about ordering is part of its contract, and this one promises something unusual that a caller cannot infer from its operations.

## Checklist
- Does anything downstream depend on strict first-in-first-out or last-in-first-out behaviour?
- How many sub-structures are there relative to threads, and how often does a claim fail?
- What happens when a claimed sub-structure turns out to be empty?
- Is there a cheap way to answer "is the whole thing empty" without scanning?
- Is the relaxed ordering written into the type's documented contract?

## Notes
The reason this works is that sequential consistency is what the sharing was buying. A sequentially consistent program behaves as though every thread's operations were interleaved into one global order without reordering any thread's own sequence — a convenient property that makes concurrent behaviour analyzable, and an expensive one, since maintaining it is precisely why every thread must meet at the same shared state.

The technique generalizes past queues to any container where operations are independent of each other, and the general shape is the same: partition the state, hand exclusive ownership of a partition to one thread at a time, and let the partitions be ordinary single-threaded code. Nearly all of the difficulty of concurrent data structures lives in the operations that must coordinate, and this removes the coordination rather than optimizing it.

The cost is paid in reasoning rather than in cycles, which is why the documentation point is not a formality. A container that is "mostly a queue" is a genuinely different contract, and every use of it has to be checked against that contract by someone who knows it applies.
