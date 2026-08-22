---
object_id: PAT_take_a_consistent_view_by_collecting_twice
object_type: pattern
name: Take a Consistent View by Collecting Twice
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
- consistency
- lock_free
- data_structures
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_keep_memory_alive_until_the_compare_and_swap_completes
- rel: related_to
  target_object_id: PAT_give_every_operation_one_instant_where_it_takes_effect
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: PAT_specify_a_concurrent_object_as_a_sequential_object_plus_a_correctness_condition
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Take a Consistent View by Collecting Twice

## Pattern Rule
**IF** you need a view of several independently updated locations that could genuinely have existed together at one instant, and excluding the writers while you read is unacceptable
**THEN** read them all, read them all again, and accept the result only if a per-location change indicator was identical across both passes — because two matching passes prove there was an interval in which nothing was written, and the values you collected are a consistent view as of that interval
**ELSE** where all the state fits behind one handle that can be swapped atomically, publish it there instead: one read of one location is consistent by construction and costs nothing to validate.

## Do
- Be clear about what the two passes actually prove. They establish that between the end of the first and the start of the second, no location changed — so the collected values are a view that really existed. They do not establish that the view is current, and by the time the operation returns, it may be long superseded.
- Validate on a change indicator, never by comparing the collected values. Equal values across two passes do not mean nothing happened: a location can be written and written back, or written twice to the same value, and the collection then blends values that never coexisted. This is exactly the recycled-pointer failure that defeats a compare-and-exchange, one level up, and it is the mistake this construction most often ships with.
- Give each location a counter that only ever moves forward, and bump it on every write. Its only job is to make change detectable, so it need carry no meaning and need not be read together with the value — but it must be impossible to advance and return to a previous value within the span of one collection.
- Make an in-progress write detectable, not merely a completed one. If a location's value takes several steps to update, advance its indicator before starting and again after finishing, and treat a pass that observes the intermediate state as a failed pass — otherwise a reader can collect a half-written value between two stable-looking indicators.
- Expect this to be obstruction-free and design for that. A collector racing writers that never stop can retry indefinitely; it succeeds when it gets an interval of quiet, which is exactly the guarantee that says progress requires the absence of interference.
- Decide what a collector does when its retries run out. Backing off, falling back to a guarded path, or reporting that no consistent view was available are all defensible; retrying forever inside an operation that was supposed to be quick is not.
- Buy the stronger guarantee with helping, when scans genuinely must not starve. Have each writer take and publish a view before performing its own write; a collector that keeps failing can then adopt a published one instead of trying again. The cost is that every write now performs a collector's work, and the subtlety is that the adopted view must be one that can be placed inside the collector's own interval — a view taken before the collection started does not describe it.
- Recognize the shape when you meet it under other names. A sequence counter that readers check before and after, a generation number validating an optimistic traversal, and a checkpoint taken without stopping the writers are all this construction.

## Don't
- Don't reach for it before asking whether the state can live behind one handle. Restructuring several locations into one immutable object published through a single pointer removes the problem rather than validating around it, and it is very often available.
- Don't let the indicator be narrow enough to wrap during a collection. A counter that can return to a previously observed value inside the window is not a change indicator, and the failure it produces is a plausible-looking view that never existed.
- Don't treat the view as fresh. It is consistent, which is a different property, and code that acts on it as though it describes the present is relying on a guarantee this does not give.
- Don't collect a target that is written continuously and expect to finish. Where every location is under constant modification, no interval of quiet arrives, and the answer is to reduce what must be collected together rather than to retry harder.
- Don't skip the second pass because the first looked self-consistent. A single sweep across several locations reads them at different moments by construction, and nothing about the values it returns reveals that they were never true together.

## Checklist
- What indicator is compared across the two passes, and can it repeat a value within one collection?
- Is a write that is partway through distinguishable from one that has not started?
- What happens to a collector that fails repeatedly — how many attempts, and then what?
- Does anything in this design require the view to be current rather than merely consistent?
- Could these locations be replaced by one atomically published object?
- If writers help, can the adopted view be placed inside the collector's own interval?

## Notes
The appeal of this construction is that readers never interfere with writers at all — no lock is taken, nothing is excluded, and a writer proceeds at full speed whether or not anyone is reading. What is given up is that the reader may have to try again, which relocates the whole cost onto the side that can usually absorb it. That trade is why the shape recurs so widely: wherever reads outnumber writes and readers must not slow writers down, some version of collect-and-validate is the answer.

The validation rule deserves the emphasis it gets because the wrong version is so natural to write. Comparing collected values is simpler, needs no extra storage, and is correct in every test where values do not repeat — which is most tests. It fails when a value returns to something previously observed, and that is not an exotic event but the ordinary behaviour of counters, flags, pointers into a pool, and any state that toggles. The counter exists to distinguish "unchanged" from "changed back," and those are different facts that the values themselves cannot tell apart.

The progress story is worth carrying because it is a clean illustration of the general shape. The simple construction is obstruction-free: correct always, complete only given a quiet interval. Upgrading it to complete unconditionally requires writers to do work on readers' behalf, which is the standard price of the stronger guarantee and appears the same way in other lock-free designs. It also relocates where the operation takes effect — a collection completed by adopting someone else's view took effect at their instant, not the collector's, which is precisely the case where the committing step belongs to another thread.
