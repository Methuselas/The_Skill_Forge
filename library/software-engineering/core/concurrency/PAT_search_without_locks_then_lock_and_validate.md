---
object_id: PAT_search_without_locks_then_lock_and_validate
object_type: pattern
name: Search Without Locks, Then Lock and Validate
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
- locking
- data_structures
- contention
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_take_a_consistent_view_by_collecting_twice
- rel: related_to
  target_object_id: PAT_split_a_lock_only_where_the_structure_makes_the_regions_disjoint
- rel: related_to
  target_object_id: PAT_mark_a_node_removed_before_unlinking_it
- rel: related_to
  target_object_id: PAT_give_every_operation_one_instant_where_it_takes_effect
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Search Without Locks, Then Lock and Validate

## Pattern Rule
**IF** modifying a structure requires first finding the place to modify it, and that search is long relative to the change itself
**THEN** perform the search taking no locks at all, then lock only the few positions you intend to touch, then *validate* that what you found is still true — and start over if it is not
**ELSE** where the search is short, or conflicts are frequent enough that validation usually fails, hold the lock throughout: the optimistic version then pays for the search twice and gains nothing.

## Do
- Split the operation into the expensive part and the committed part, because that split is the whole technique. Finding the position is long, touches many locations, and does not modify anything; the modification is short and touches two or three. Only the second needs excluding anyone.
- Treat the unsynchronized search as a hint rather than a result. What it returns was true at some moment and may not be now, so nothing may be modified on its strength until it has been rechecked under the locks.
- Write validation as an explicit step that can fail, and make failure ordinary. It is not an assertion or a sanity check — it is a normal outcome that returns the operation to the start, and code that treats it as an error condition has misunderstood the design.
- Check exactly what the modification depends on, not that the world is unchanged. Typically that is a short list: the positions you locked are still part of the structure, and they are still adjacent in the way the search found them. Anything else may have changed freely and does not concern you.
- Take the locks in a fixed order before validating. Locking two positions found by a search is locking two things at once, so the ordering discipline that prevents cycles applies here as it does anywhere else.
- Price validation before choosing this, because it is the part that decides whether the technique pays. Where confirming your findings means traversing the structure again, validation costs as much as the search did, and the operation is now two traversals rather than one — acceptable when contention is rare, and a poor trade otherwise. A structure that lets each position carry its own evidence of still being valid reduces that to a couple of reads, which is what makes the technique worthwhile rather than merely clever.
- Establish that traversing without locks is safe at all, which is a separate obligation. Readers walk over positions that other threads are actively modifying and may walk into ones already removed, so the structure must guarantee that following a link from a removed position still leads somewhere well-formed rather than into freed memory.
- Say plainly that this is blocking. Threads still take locks and can still be delayed indefinitely by a slow holder, and an operation can be forced to retry repeatedly by a stream of conflicting ones. The technique buys throughput under low contention; it does not buy a progress guarantee.

## Don't
- Don't validate by checking that what you found is still *there*. What matters is that the relationship you are about to rely on still holds — that one position still leads to the other. A position can remain perfectly intact after being detached from the structure, and modifying around it then updates something nobody can reach.
- Don't skip validation on the read-only path if that path returns a position rather than an answer. Returning something for a caller to act on later hands them a hint they will treat as a result, which moves the failure out of the structure and into code that has no idea it is racing.
- Don't apply it where the search is the cheap part. Optimism buys the ability to do expensive work without excluding anyone, so when the expensive part is the modification itself, there is nothing to buy.
- Don't let retries be unbounded and unmeasured. A workload where validation usually fails converts every operation into repeated traversals, and it looks like a mysteriously slow structure rather than like contention.
- Don't assume the retry starts from a clean position. Beginning again means beginning at the start of the structure with fresh state, not resuming from where the previous attempt was standing.

## Checklist
- What exactly does validation check, and is it the relationship the modification depends on?
- How expensive is validation compared to the search itself?
- Under what conflict rate does this stop paying, and what is the actual rate?
- Are the locks taken in a consistent order?
- Is a traversal that walks over a concurrently removed position still safe?
- Is there a bound on retries, and is anyone measuring how often they happen?

## Notes
The economics here are worth stating plainly, because the technique is often adopted for the wrong reason. It is not that locking is expensive in itself; it is that holding a lock across a long traversal serializes every other operation behind work that touches almost nothing. Moving the traversal outside the lock shortens the excluded region from the whole operation to a couple of pointer updates, and the resulting concurrency is the entire payoff. Any argument for it that does not turn on that ratio is probably an argument for something else.

Validation cost is the hinge, and it is why this design usually appears as a stepping stone rather than a destination. In its plain form, confirming that your findings still hold means walking the structure again, which doubles the work of every operation to save contention that may not exist. The refinements that make it practical all attack that one number — giving each position a flag that says whether it is still part of the structure, or a version that changes when it is touched, so validation becomes a couple of local reads. Recognizing that validation cost is the thing to optimize is more useful than any particular scheme for optimizing it.

The relationship to reading a consistent view is close enough to be worth distinguishing. Both do unsynchronized work and then check whether it still stands. The difference is what happens on success: a reader that validates has its answer and is finished, while this takes locks and then modifies, which is why it remains a blocking design with an ordering discipline and a starvation story. They are the same instinct applied to different obligations.
