---
object_id: PAT_cancel_complementary_operations_instead_of_applying_them
object_type: pattern
name: Cancel Complementary Operations Instead of Applying Them
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- concurrency
- contention
- scalability
- data_structures
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_match_the_lock_to_the_length_of_the_critical_section
- rel: related_to
  target_object_id: PAT_trade_exact_ordering_for_independent_substructures
- rel: related_to
  target_object_id: PAT_give_every_operation_one_instant_where_it_takes_effect
- rel: related_to
  target_object_id: PAT_match_the_problem_to_a_known_coordination_shape
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Cancel Complementary Operations Instead of Applying Them

## Pattern Rule
**IF** a shared structure limits throughput not because threads are contending for a lock but because every operation must pass through one point that orders them all
**THEN** check whether concurrent operations come in pairs that cancel — one supplying exactly what another consumes — and let such pairs satisfy each other directly, never reaching the shared structure at all
**ELSE** where operations have no complements, or the workload is lopsided enough that partners are rarely present, there is nothing to cancel and the bottleneck needs a different remedy.

## Do
- Separate contention from a sequential bottleneck first, because they call for different remedies and only one is on offer here. Contention is many threads arriving at one location at the same moment, and spreading arrivals out in time reduces it. A sequential bottleneck is that every operation must be ordered through one point *at all* — backing off does nothing to that, it only rearranges when threads queue. This is one of the few techniques that removes the ordering requirement rather than smoothing traffic into it.
- Confirm the pair genuinely cancels, meaning that performing both would leave the structure exactly as it was. On a stack this holds unconditionally: an addition and a removal that meet leave nothing behind. On a queue it holds *only when the queue is empty*, because otherwise the removal is owed the oldest element rather than the one just offered — a condition that is easy to skip and fatal to get wrong.
- Let the partners exchange directly and both return satisfied. The supplier hands its value to the consumer, and there is nothing to reconcile with the structure afterwards, because as far as the structure is concerned neither call happened.
- Order an eliminated pair at the moment of exchange. That is where both operations took effect, and it is what keeps the combined design linearizable even though neither call ever appeared at the shared structure.
- Spread the meeting places, or the meeting place becomes the bottleneck you were escaping. One rendezvous location serializes everyone again; an array of them with each thread choosing at random is what allows pairs to form in parallel.
- Size that array against the concurrency rather than the data. Too few locations and threads collide without matching; too many and partners never meet. It is a tuning parameter, it depends on the thread count and the arrival mix, and it wants measuring rather than guessing.
- Use elimination *as* the backoff rather than alongside it. A thread that has just failed at the shared structure has time to spend and good reason to think partners exist — precisely the conditions under which searching pays — so the wait it would otherwise spend idle becomes the search.
- Keep the ordinary path underneath and correct. A thread that finds no partner, or finds one wanting the same operation rather than its complement, must still complete the normal way. This is an accelerator over a correct structure, never a replacement for one.

## Don't
- Don't expect it to help a lopsided workload. It pays when supply and demand arrive in comparable volume; a structure that is mostly being filled, or mostly being drained, offers no partners and every thread pays for the search before falling back anyway.
- Don't let one operation cancel against two partners. Each elimination is an exclusive agreement between exactly two operations, and the pairing step has to be atomic — otherwise one addition satisfies two removals and the structure silently loses an element.
- Don't assume a pair that cancels in the abstract cancels in this structure. The test is whether the concrete state is unchanged, and identical-looking operations on a stack and on a nonempty queue give opposite answers.
- Don't reach for it before establishing which bottleneck you have. If the structure is contended but not sequentially limited, cheaper remedies apply, and this adds an entire parallel mechanism for no gain.
- Don't leave the array size as a constant nobody revisits. It is the parameter the whole technique's benefit turns on, and the right value moves with the thread count and the workload mix.

## Checklist
- Is the limit contention on one location, or the requirement that everything be ordered through it?
- Does performing both operations of a candidate pair leave the structure genuinely unchanged?
- What makes a pairing exclusive to two operations?
- Where do eliminated operations sit in the order, and is that written down?
- How many meeting places are there, and against what was that number chosen?
- What happens to a thread that finds no partner?

## Notes
The observation underneath is almost trivial once stated and is easy to walk past: two operations that undo each other need not be performed. What makes it powerful is where it applies — a structure whose throughput ceiling comes from every operation having to serialize through one point. Backoff, padding, and finer locking all attack the cost of reaching that point. This attacks whether you need to reach it, which is a different and much larger lever, and it is why a structure that looks inherently sequential can turn out not to be.

The cancellation test is the part to be careful about, because the intuition generalizes further than the property does. A stack is the friendly case: its two operations act on the same end, so a matched pair leaves nothing behind at any size. A queue is not, because its operations act on opposite ends, and a removal is owed a specific element that a concurrent addition is generally not offering. The rule to carry is the concrete one — does the structure end in the state it started in — rather than the abstract one about operations being inverses.

Folding the search for a partner into the backoff is the detail that makes this practical rather than merely elegant. A thread that has just lost a race is about to wait anyway, and it has just learned that other threads are active — which is exactly when a complementary operation is likely to be nearby. Spending that interval looking rather than sleeping means the mechanism costs almost nothing when it fails and removes work from the bottleneck when it succeeds, so the technique degrades to plain backoff rather than to a loss.
