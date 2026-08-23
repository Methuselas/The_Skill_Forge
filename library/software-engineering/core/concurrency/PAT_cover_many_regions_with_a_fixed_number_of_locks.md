---
object_id: PAT_cover_many_regions_with_a_fixed_number_of_locks
object_type: pattern
name: Cover Many Regions With a Fixed Number of Locks
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
  target_object_id: PAT_split_a_lock_only_where_the_structure_makes_the_regions_disjoint
- rel: related_to
  target_object_id: PAT_trade_exact_ordering_for_independent_substructures
- rel: related_to
  target_object_id: PAT_separate_per_thread_data_by_a_cache_line
- rel: related_to
  target_object_id: PAT_match_the_lock_to_the_length_of_the_critical_section
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Cover Many Regions With a Fixed Number of Locks

## Pattern Rule
**IF** a structure divides naturally into many regions that operations rarely touch together, and one lock over the whole thing is the bottleneck
**THEN** take a fixed number of locks — far fewer than there are regions — and map regions onto them, rather than giving every region its own
**ELSE** where the regions are few, or where a single operation routinely spans several of them, per-region locks are simpler and there is nothing to economize.

## Do
- Choose the lock count against the thread count, not against the data. What decides whether two operations collide is how many threads are running, so a number of locks a small multiple of that is usually enough to make collisions rare. Scaling locks with the data instead buys almost no additional concurrency and costs memory that grows without limit.
- Map regions onto locks by the same value that picks the region. Taking the region index modulo the number of locks costs one operation, needs no lookup table, and spreads regions evenly across locks provided the index is already well distributed.
- Accept that two unrelated regions will sometimes share a lock, and price that honestly. It is a false conflict — two operations that could have run together are serialized for no reason but the mapping — and it is the entire cost of the technique. It is worth paying because the alternative is storage and initialization proportional to a structure that may be large and mostly idle.
- Let the structure grow without growing the locks. When the region count doubles, the same fixed set of locks simply covers twice as many regions each, and every operation still finds its lock by the same arithmetic. This is the property that makes the technique fit growable structures, and it is the reason not to tie the two arrays together in the first place.
- Take the lock before computing anything that the resize could invalidate, and recheck afterwards. A structure that can grow underneath an operation means the region an operation computed may no longer be the region it should touch, so the mapping has to be recomputed under the lock rather than trusted from before it.
- Hold every lock to resize, and take them in a fixed order. Growing the structure is the one operation that spans all regions at once, so it needs the whole set; a consistent order makes that safe, and checking on entry whether someone else already resized keeps it from happening twice.
- Pad the locks apart if they sit in an array. Locks adjacent in memory share cache lines, and threads taking different locks then invalidate each other's lines for no reason — which reinstates the contention the split was meant to remove.

## Don't
- Don't give every region its own lock by default. It looks like the natural refinement of one-lock-for-everything and it is usually waste: most regions are idle most of the time, and the storage, initialization, and cache footprint all scale with the structure rather than with the concurrency.
- Don't grow the lock array with the structure. It forces every in-flight operation to agree on which array it is using at the moment it changes, which is a much harder problem than the one being solved, and it buys concurrency that was not the constraint.
- Don't apply this where operations span regions. The technique assumes an operation touches one region and takes one lock; anything that routinely needs two has an ordering problem to solve, and the shared-lock collisions make it worse rather than better.
- Don't map regions onto locks with a distribution that clusters. The mapping inherits whatever bias the region index has, so a hash that clumps produces locks that clump, and a few locks carry all the traffic while the rest sit idle.
- Don't treat the fixed count as a constant nobody revisits. It is the parameter the whole technique turns on, it is chosen against the concurrency, and the right value moves when the deployment does.

## Checklist
- How many locks are there, and what number was that chosen against?
- How does an operation get from a region to its lock?
- Can two operations on unrelated regions collide, and how often at the expected thread count?
- If the structure can grow, what happens to an operation holding a lock while it does?
- Do any operations touch more than one region?
- Do two locks ever share a cache line?

## Notes
The insight is that lock count and region count answer different questions, and tying them together conflates the two. How many regions there are is a property of the data. How many locks are useful is a property of how many threads could be inside the structure at once — and that number is small, bounded by the machine, and does not grow when the data does. Once separated, the choice becomes obvious in a way it is not while the two are coupled.

The false conflicts this creates are worth being explicit about rather than treating as a hidden cost. Two operations on unrelated regions that happen to map to one lock are serialized for no reason connected to the data, and no amount of tuning eliminates that — it can only be made rare. What makes it acceptable is that the frequency depends on the lock count and the thread count, both of which are known and small, so the collision rate is something you can compute in advance rather than discover.

The interaction with growth is the part that is easy to get wrong and is the technique's best feature when it is right. A structure that doubles keeps the same locks, each simply covering more; nothing has to be migrated, no operation has to be told, and the arithmetic that finds a lock is unchanged. That is only true because the two arrays were kept independent from the start, which is a decision made once at design time and very awkward to retrofit.
