---
object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
object_type: pattern
name: Choose a Container on More Than Algorithmic Complexity
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
- data_structures
- design
- iterator_invalidation
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_data_structure_for_the_dominant_access_pattern
- rel: related_to
  target_object_id: PAT_cross_a_c_boundary_with_only_what_c_can_express
- rel: related_to
  target_object_id: AP_settle_a_containers_contract_before_filling_it
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Choose a Container on More Than Algorithmic Complexity

## Pattern Rule
**IF** you are deciding which standard container a piece of data will live in
**THEN** put the choice past the axes that complexity says nothing about — whether elements stay where you put them, which iterator category the code requires, whether existing elements may move, what survives an insertion or erasure, whether the storage must be readable from C, and whether a multi-element insertion has to be able to roll back
**ELSE** where the data is small, local to one function, and never outlives it, the default sequence container is right and this analysis costs more than the choice is worth.

## Do
- Sort the candidates by memory layout before anything else, because that single distinction predicts several answers at once. Containers storing many elements per allocated chunk have to shift their neighbors when one is inserted or erased; containers storing one element per chunk rearrange pointers instead, so element values never move.
- Follow the layout distinction to what it implies. Because node-based containers never move the elements themselves, insertions and erasures on them leave iterators, pointers, and references valid except to whatever was erased; on the contiguous ones, an insertion or erasure must be assumed to invalidate all of them.
- Ask the iterator-category question explicitly, because it silently constrains which algorithms you may call later. Random access is available only from the contiguous containers, and choosing a linked list rules out sorting it with the general-purpose algorithms.
- Treat rollback as its own axis. Where an insertion of several elements must either all happen or leave the container untouched, the linked list is the standard container offering it directly; obtaining the same guarantee from a contiguous container is possible, costs performance, and requires code nobody will find obvious.
- Where the bytes have to be handed to something written in C, only the contiguous containers can supply them, and only one of them promises the layout.

## Don't
- Don't take "use the default sequence container unless insertions and erasures in the middle are frequent" as the whole of the guidance. That advice is sound and answers exactly one of the questions above; it is quoted so often that the other questions never get asked.
- Don't let the invalidation axis go unexamined because it produces no diagnostic. Every other consideration here fails at compile time when you get it wrong. This one compiles, runs, and produces a program that reads memory the container no longer owns.
- Don't assume the standard containers agree about invalidation even when they agree about complexity. The double-ended queue is the outlier worth remembering: it is the only standard container that can invalidate its iterators while leaving pointers and references into it valid.
- Don't expect a container of bool to behave like a container of anything else. The specialization does not store what you think and does not hand back references to elements.

## Checklist
- Does the code need to insert at an arbitrary position, or is position determined by ordering?
- Which iterator category do the algorithms this data will be passed to require?
- After an insertion or erasure, what does the surrounding code still hold — iterators, pointers, references — and does it survive?
- Do the contents ever cross into code that expects a C array?
- Must a multi-element insertion be all-or-nothing?
- Is lookup speed the dominant cost, and if so, is ordering actually required?

## Notes
The reason this needs saying is that the standard's own guidance covers complexity and stops, so the complexity table has become the whole of most people's decision procedure. It is a good table. It answers one question of six or seven, and the ones it omits are the ones whose consequences appear at run time.

Several of Meyers's axes have been settled by the language since he wrote, and it is worth knowing which so the analysis does not waste time on them. Whether the container has to be standard used to eliminate the singly linked list and the hash-based containers; both are standard now. Whether you mind reference counting used to steer you away from the standard string; the standard now forbids that implementation. Sorted sequences as a replacement for the tree-based associative containers, which he presents as a hand-rolled technique, are now available as library types in their own right.

The layout distinction is the part most worth carrying away, because it is not a list to memorize but a single fact that generates the list. Whether elements are stored many-per-chunk or one-per-chunk determines whether insertion moves neighbors, which determines whether references into the container survive, which determines whether rollback is cheap — three answers from one property.
