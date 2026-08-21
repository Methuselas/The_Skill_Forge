---
object_id: PAT_make_sure_the_destination_range_can_hold_the_output
object_type: pattern
name: Make Sure the Destination Range Can Hold the Output
library_path:
- software-engineering
- languages
- cpp
- algorithms
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- algorithms
- undefined_behavior
- containers
- iterators
cross_links:
- rel: related_to
  target_object_id: PAT_reserve_capacity_up_front_and_release_it_deliberately
- rel: related_to
  target_object_id: PAT_prefer_range_member_functions_to_repeated_single_element_calls
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Make Sure the Destination Range Can Hold the Output

## Pattern Rule
**IF** you are calling an algorithm that writes its results somewhere you name with an iterator
**THEN** decide whether that destination already contains enough elements to be assigned to, and where it does not, pass an inserting iterator rather than a position — because these algorithms write by assigning to existing elements, and assigning to elements that do not exist is undefined
**ELSE** where the destination genuinely does hold enough elements and you mean to overwrite them, a plain iterator to the first one is exactly right and no adapter is wanted.

## Do
- Read the destination parameter as "start assigning here," not as "start adding here." That single reframing is what makes the failure visible: naming a container's end as the destination asks the algorithm to assign to the element one past the last, which is not an element.
- Wrap the destination in the adapter matching where you want elements added — at the back, at the front, or before a position you name. Each turns the algorithm's assignments into insertions on the container underneath.
- Remember that adding at the front reverses the relative order of what you insert, since each new element is pushed ahead of the last. Where you want front insertion *and* the original order, traverse the source backwards.
- Size the destination first when you intend to overwrite rather than insert, either by growing it to at least the source's element count or by emptying it and inserting into it instead.
- Reserve capacity before a series of insertions into a contiguous container, since the algorithm inserts one element at a time and nothing you can do will make it do otherwise.

## Don't
- Don't reserve capacity and then name the container's end as the destination. Reserving changes only the capacity, so the elements still do not exist; the algorithm then assigns into raw storage, the container's element count never learns about it, and the container is left inconsistent with its own contents.
- Don't assume a wrong destination will announce itself. Assigning through an iterator past the end is undefined rather than diagnosed, and the common outcome is memory corruption at a distance from the call.
- Don't expect the range member functions to rescue the per-element insertion cost here. Where you control the call you can pass a whole range at once; when an algorithm is doing the writing, it writes one element per step by construction.

## Checklist
- Does the destination container already contain elements to assign to, or is it empty or short?
- If elements are to be added, is the destination wrapped in an inserting adapter?
- If capacity was reserved, is an inserting adapter also being used?
- When overwriting, is the destination at least as long as the source?
- For a contiguous destination receiving many insertions, was capacity reserved first?

## Notes
The mistake is a communication failure rather than a knowledge gap. Programmers writing this know perfectly well that they want the results added to the container; what they have not noticed is that the call as written does not say so, and the library has no way to infer an intention from a destination that merely happens to be the end.

The reserve-without-an-adapter version is the more dangerous of the two failures, because reserving makes the code look more careful rather than less. The capacity is genuinely there, so the writes may well land in memory the container owns — which means no crash, no diagnostic, and a container whose reported element count disagrees with what is actually stored in it.

The advice generalizes past the copying algorithms to anything taking a destination, including writing to an output stream through an iterator. What varies is only where the elements end up; the requirement that something exist to receive each assignment does not.
