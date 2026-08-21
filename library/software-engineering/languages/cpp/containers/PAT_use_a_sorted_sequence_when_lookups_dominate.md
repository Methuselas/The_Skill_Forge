---
object_id: PAT_use_a_sorted_sequence_when_lookups_dominate
object_type: pattern
name: Use a Sorted Sequence When Lookups Dominate
library_path:
- software-engineering
- languages
- cpp
- containers
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- containers
- performance
- data_structures
- memory
cross_links:
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
- rel: related_to
  target_object_id: PAT_give_an_ordered_container_a_comparison_type_that_is_a_strict_weak_ordering
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Use a Sorted Sequence When Lookups Dominate

## Pattern Rule
**IF** you need fast lookup and your program's use of the structure separates into phases — a build-up that is nearly all insertion, a working period that is nearly all lookup, and an occasional wholesale rebuild
**THEN** consider a sorted contiguous sequence searched by binary search rather than a tree-based associative container, because the tree is optimized for the case where insertion, erasure, and lookup are interleaved unpredictably and yours is not that case
**ELSE** where insertions and erasures really are mixed in among the lookups, the tree's cheap modification is the whole reason it exists and a sorted sequence will cost far more than it saves.

## Do
- Test your usage against the phase pattern before anything else, because it is the entire precondition. Setup, then lookup, then occasionally rebuild and return to lookup — with modification and searching essentially never interleaved — is the shape that makes this pay.
- Count the space, which is where the advantage starts. A tree node carries the element plus pointers to two children and usually a parent, so three pointers of overhead per element; the sequence carries the elements and nothing else. For a small element that is most of the storage.
- Follow the space to the real reason, which is locality rather than bytes. Fewer bytes per element means more elements per page, and a binary search over contiguous storage touches a predictable, tight set of addresses. A tree cannot promise that elements adjacent in traversal order are adjacent in memory, so the same search touches more pages.
- Re-sort at the end of each build-up phase, and use the stable sort when emulating a container that permits duplicates and you care about their relative order.
- Expect to write more comparison machinery when emulating a keyed container. Sorting compares two elements, but lookup compares a key against an element, and the key can arrive on either side — so a single comparison type needs the element-to-element form plus both key-to-element forms, all delegating to one private key comparison so they cannot drift apart.

## Don't
- Don't apply this where modifications are interleaved with lookups. Inserting into the middle of a sorted sequence moves every element after it, and erasing does the same, so the operations the tree does cheaply become the dominant cost.
- Don't forget that the element type changes when emulating a keyed container. The tree stores the key as const; a sequence cannot, because sorting assigns its elements around, so both parts must be assignable.
- Don't reason about this from complexity alone. Both structures give logarithmic lookup, so the complexity comparison says they are equivalent and the entire difference lives in constant factors and page behavior — which is measurable but not derivable.

## Checklist
- Do lookups and modifications interleave, or do they separate into phases?
- How large is an element compared to three pointers?
- Is the sequence re-sorted after every phase that modifies it?
- When emulating a keyed container, does the comparison type handle key-against-element in both argument orders?
- Has the difference been measured rather than assumed?

## Notes
The insight worth taking from this is not the technique but the observation behind it — that a balanced tree is a structure tuned for unpredictable interleaving of insertion, erasure, and lookup, and that a great many programs do not use their data that way. Once you see the phase structure in your own program, the question of which structure fits is answerable rather than a matter of habit.

The performance argument rests on locality rather than on operation counts, and that is why the complexity table cannot see it. Both structures are logarithmic; one of them touches a handful of cache lines that are near each other and the other chases pointers across the address space. Implementations do cluster tree nodes to mitigate this, and clustering is not the same as contiguity.

The technique has since been absorbed into the library as container types that do exactly this — an ordered interface presented over sorted sequences underneath — which removes the hand-written comparison machinery above and leaves the decision, which is the part that was always the hard bit. Where those are available, the choice is which container to name rather than a structure to build.
