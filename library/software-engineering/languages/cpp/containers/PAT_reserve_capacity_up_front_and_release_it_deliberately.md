---
object_id: PAT_reserve_capacity_up_front_and_release_it_deliberately
object_type: pattern
name: Reserve Capacity Up Front and Release It Deliberately
library_path:
- software-engineering
- languages
- cpp
- containers
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- containers
- performance
- memory_management
- iterator_invalidation
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_range_member_functions_to_repeated_single_element_calls
- rel: related_to
  target_object_id: PAT_hoist_allocation_out_of_the_work
- rel: related_to
  target_object_id: PAT_recover_the_iterator_from_erase_rather_than_advancing_it
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Reserve Capacity Up Front and Release It Deliberately

## Pattern Rule
**IF** you are filling a growable container whose eventual size you can predict, or you have shrunk one far below the peak it reached
**THEN** set the capacity before filling and give the excess back as its own explicit act, because growth proceeds by reallocations that invalidate everything pointing into the container, and removing elements never returns any memory at all
**ELSE** where the container is small or lives briefly, the default growth policy costs a handful of reallocations and neither step earns the line it takes.

## Do
- Keep the four steps of a reallocation in mind, since they are what you are paying for: fresh memory is allocated at some multiple of the current capacity, every element is moved across, the originals are destroyed, and the old block is released. Every iterator, pointer, and reference into the container dies at that moment.
- Separate the four related member functions, which are easy to confuse. One reports how many elements are present; one reports how many the current allocation could hold; one changes the number of elements present, destroying or default-constructing as needed; and one changes only the capacity and never the element count.
- Pick between the two strategies by what you know. If the final count is known or nearly so, ask for it once before filling. If only an upper bound is known, ask for that and trim afterwards.
- Use the size-against-capacity comparison to predict invalidation, which is the part that is useful outside performance work. When the count is strictly below the capacity, appending cannot reallocate and therefore cannot invalidate anything.
- Release excess capacity with the request the container provides for it, and reach for the older copy-and-swap spelling only when working against an implementation that lacks it, or when you want to clear the container and release its memory in one move.

## Don't
- Don't expect removing elements to give memory back. Erasing a range, or emptying the container entirely, reduces the element count and leaves the capacity where the high-water mark left it — so a container that briefly held a hundred thousand elements and now holds ten is still holding the memory for a hundred thousand.
- Don't read a reservation as a guarantee that nothing will be invalidated. It removes reallocation as a cause; an insertion anywhere but the end still invalidates everything from the insertion point onward, because the elements after it have to move.
- Don't treat a request to shrink as a command. Implementations may keep a minimum capacity or round it to a convenient size, so what you get is the smallest the implementation is willing to go given the current element count.
- Don't reason about a string's allocations from its size alone. Short values are commonly stored inside the string object itself, so a string may perform no allocation at all until it grows past that threshold, and the threshold varies.

## Checklist
- Is the final element count known, or bounded, before the filling loop starts?
- Does anything hold an iterator, pointer, or reference across the filling?
- After a large reduction in element count, is the memory still held, and does that matter here?
- Is a reservation being relied on to keep iterators valid across an insertion that is not at the end?

## Notes
The invalidation consequence is the reason this is not purely a performance concern, and it is the half most often missed. Inserting one element into a container can silently invalidate a data structure elsewhere in the program that was holding positions into it — so reserving is sometimes a correctness measure that happens to also be faster.

The two halves of capacity management are asymmetric in a way worth noticing. Growth is automatic and generous, doubling on each exhaustion in most implementations, which is why a naive filling loop over a thousand elements can reallocate ten times. Shrinkage is never automatic at all. Nothing the container does on your behalf will hand memory back, so if the peak was large and the steady state is small, releasing it is a decision somebody has to make explicitly.

The copy-and-swap spelling for shrinking — constructing a temporary copy and exchanging contents with it — is worth being able to read even though it is no longer worth writing. It fills older codebases, and it works because the copy is built sized to its contents while the exchange leaves the oversized allocation in the temporary, which is then destroyed. The same move against a default-constructed temporary both empties a container and releases its memory.
