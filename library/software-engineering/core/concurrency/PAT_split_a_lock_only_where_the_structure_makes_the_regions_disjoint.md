---
object_id: PAT_split_a_lock_only_where_the_structure_makes_the_regions_disjoint
object_type: pattern
name: Split a Lock Only Where the Structure Makes the Regions Disjoint
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
- data_structures
- locking
- design
- contention
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_lock_the_smallest_region_that_must_be_atomic
- rel: related_to
  target_object_id: PAT_make_every_concurrent_operation_a_complete_transaction
- rel: related_to
  target_object_id: PAT_trade_exact_ordering_for_independent_substructures
- rel: related_to
  target_object_id: PAT_break_one_of_deadlocks_four_conditions
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Split a Lock Only Where the Structure Makes the Regions Disjoint

## Pattern Rule
**IF** one lock over a whole data structure has become the bottleneck and you are considering a separate lock per region so that operations at different regions can proceed at once
**THEN** first establish that the regions can never refer to the same element, reshaping the structure until that is true by construction rather than true in the common case — because two locks over regions that can coincide is not finer-grained locking, it is an unguarded race that the second lock disguises
**ELSE** where contention is low, or where every operation acts on the same region anyway, one lock over the whole structure is correct, faster to write, and very much easier to keep correct.

## Do
- Test the split against the empty and nearly-empty cases, because those are where regions coincide. A queue holding one element has both of its ends on that element; a lock for each end then guards the same memory, and neither excludes the other. The design works at every size except the sizes that occur constantly — at startup, at drain, and whenever consumers keep pace with producers.
- Change the structure rather than the locking. A permanent placeholder element that carries no value, kept always between the two ends, means the ends never refer to the same element at any size. That is what makes the finer locking legal, and it is a change to the data structure's invariants rather than to its synchronization.
- Expect the reshaped version to be a genuinely different structure, and budget for that. Its operations must now create, skip, and maintain something that holds no data and can never be handed out, and every operation has to be re-derived against the new invariant rather than adapted from the old one.
- Find the operations that must still see both regions, and give them both locks. Answering whether the structure is empty means comparing the two ends, so it cannot be done under either lock alone. Take both, always in the same order, and hold them for that comparison only.
- Accept the fixed order as a local obligation rather than a global discipline. Two locks acquired in one order inside one component is checkable by reading that component; it becomes the hazard the deadlock rules describe only when the order is a convention spread across a codebase.
- Guard only what touches the shared structure. Constructing the new element is local work that no other thread can observe, so it belongs outside the guarded region; only the few operations that relink the shared structure belong inside.
- Recognise when no split exists. Where every operation acts on the same region by definition — a stack pushes and pops at one end — there are no disjoint regions to find, and the available moves are a different structure, less sharing, or accepting the single lock.
- Reach the coarse version first and keep it. It is the reference the fine-grained one is checked against, both for behaviour and for whether the split bought anything.

## Don't
- Don't add a second lock to a structure you did not reshape. This is the whole failure: the change reads as an optimization, compiles, passes ordinary testing, and produces a race precisely when the structure is nearly empty.
- Don't accept "the regions are usually far apart" as the argument. Usually is not a synchronization property, and the exceptional case here is not exotic — it is the empty structure, which every structure is at least once.
- Don't assume the finer version is faster before measuring it. It adds a second acquisition to the path that needs both regions and buys concurrency only when operations at different regions genuinely overlap in time.
- Don't leave the placeholder undocumented or reachable. An element that exists solely to keep the regions apart is invisible in the structure's contract, will look like a defect to the next reader, and breaks the structure if any operation ever hands it out or removes it.
- Don't split a lock as the first response to contention. Eliminating the sharing, splitting the structure into independent sub-structures, or shortening the guarded region are all cheaper, and all of them leave a structure that is easier to reason about than this one.

## Checklist
- With the structure empty, and with exactly one element in it, can the two regions refer to the same element?
- What in the structure guarantees they cannot — an invariant, or the way the operations happen to be written?
- Which operations need both locks, and are they taken in the same order everywhere?
- Is any work inside a guarded region that no other thread could observe?
- Does the coarse-grained version still exist to check this one against?
- Has the split been measured, and did the overlapping operations actually overlap?

## Notes
The reason this fails so reliably is that finer-grained locking is usually described as a locking decision, which invites the change to be made to the locks. It is not one. Whether two regions of a structure can be guarded separately is a question about the structure's shape, and the honest sequence is to establish disjointness first, reshape until it holds, and only then place the locks — at which point the locking is the easy part.

The placeholder element is worth dwelling on because it looks like a trick and is really the entire design. Keeping something between the two ends converts a property that holds at some sizes into one that holds at all sizes, and the whole safety argument rests on it. That is also why it must be an invariant of the structure rather than a fact about the current implementation: the next person to write an operation will maintain a documented invariant and will quietly break an undocumented convention.

The cost side deserves stating plainly, since the coarse version is often the right answer. One lock over the whole structure gives a design where the safety argument is a sentence, and its throughput ceiling only matters when threads are genuinely contending. The finer version costs a redesign, a subtler invariant, an acquisition order to maintain, and a second lock on any operation spanning both regions — paid always, against a benefit that appears only when different regions are in use at the same moment. Confirming that they are is a measurement, and it is the one that decides whether any of this was worth doing.
