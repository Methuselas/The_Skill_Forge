---
object_id: PAT_avoid_the_packed_bool_specialization
object_type: pattern
name: Avoid the Packed Bool Specialization
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
- proxy_types
- generic_programming
- avoiding_surprises
cross_links:
- rel: related_to
  target_object_id: PAT_interpose_a_proxy_when_an_operator_cannot_see_its_context
- rel: related_to
  target_object_id: PAT_hand_container_data_to_a_c_api_as_a_pointer_and_a_count
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Avoid the Packed Bool Specialization

## Pattern Rule
**IF** you want a growable sequence of boolean values and are about to instantiate the standard growable array with bool as its element type
**THEN** choose something else — a node-based sequence of real bools, a fixed-size bit collection, or a growable array of a byte-sized type — because that specialization is not a container and does not hold what it says it holds
**ELSE** where you genuinely want the packed representation, will never take an element's address, pass its storage outward, or feed it to generic code, it does that job and the objection is academic.

## Do
- State the requirement it breaks, because "it is not a container" sounds like invective until you see it. A container of some type that supports subscripting must let you take the address of a subscripted element and get a pointer to that type. Here you cannot: the elements are packed to a bit apiece, pointers to bits do not exist, so subscripting returns a stand-in object and taking its address yields a pointer to the stand-in.
- Pick the replacement by which property you actually need. A double-ended sequence of bools is a genuine container holding genuine bools, at the cost of contiguous storage. A fixed-size bit collection keeps the packing and adds bitwise operations, at the cost of iterators and of any change in size. A growable array of a byte-sized integer type keeps contiguity and the ability to hand storage to other interfaces, at the cost of eight times the space.
- Watch for it hardest in generic code, which is where it stops being a curiosity. A template that works for every other element type can fail to compile, or quietly do something else, for this one — and the failure appears at the instantiation rather than where the template was written.

## Don't
- Don't try the pointer-and-count handoff on it. Those techniques need a pointer to the element type and there is no such pointer to be had here, so the code does not compile — which is fortunate, because the packed representation is not what the receiving side expects anyway.
- Don't assume a template is safe here because it was tested on other element types. That is exactly the assumption this breaks, and the standard's own container requirements are what it breaks it against.

## Checklist
- Does any code take the address of an element of this sequence, or bind a reference to one?
- Is this sequence ever passed to a template written for containers generally?
- Does anything need to hand its storage to an interface expecting an array?
- Is the size fixed at compile time, in which case the bit collection is the better fit anyway?

## Notes
The reason this is in the standard is more interesting than the defect and is the part worth keeping. The committee built it deliberately, as a worked demonstration that the library could support containers whose elements are reached through stand-in objects, so that practitioners would have a reference implementation to copy. What the attempt established was the opposite: a container whose elements are reached through stand-ins cannot satisfy all of the container requirements. The demonstration failed and was standardized anyway.

That makes this a general result about interposed objects rather than a fact about bool. Where an interposed object earns its place, it does so by being nearly indistinguishable from the thing it stands for, and "nearly" is precisely the gap that the container requirements refuse to accept. Anyone considering a stand-in-based container of their own has the answer here already.

The practical shape of the trap is that everything works until it does not. Reading and writing elements behaves as expected, iteration behaves as expected, and the specialization goes unnoticed for as long as the code stays away from addresses, references, storage, and templates — which is why it tends to be discovered late and by somebody who did not choose it.
