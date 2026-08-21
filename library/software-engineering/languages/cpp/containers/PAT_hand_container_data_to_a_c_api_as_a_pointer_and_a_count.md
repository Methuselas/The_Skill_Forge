---
object_id: PAT_hand_container_data_to_a_c_api_as_a_pointer_and_a_count
object_type: pattern
name: Hand Container Data to a C API as a Pointer and a Count
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
- language_interop
- legacy_code
- undefined_behavior
cross_links:
- rel: related_to
  target_object_id: PAT_cross_a_c_boundary_with_only_what_c_can_express
- rel: related_to
  target_object_id: PAT_reserve_capacity_up_front_and_release_it_deliberately
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Hand Container Data to a C API as a Pointer and a Count

## Pattern Rule
**IF** you need to pass the contents of a container to an interface that takes a pointer and a length, or fill a container from one
**THEN** go through the growable array, which is the only container whose storage is laid out the way such an interface expects — take its data pointer and its element count, guarding the empty case — and route every other container's contents through one on the way in or out
**ELSE** where the interface is one you also control, take a non-owning view of contiguous memory instead and neither side has to spell out a pointer and a count.

## Do
- Guard the empty case explicitly, because it is the one thing here that is undefined rather than merely awkward. Subscripting element zero of an empty container to take its address has no defined meaning, so test for emptiness before making the call.
- Use the string's own C-string accessor rather than the address of its first character. It is defined even for an empty string, where it yields a pointer to a terminator, and it guarantees the terminator that the container's raw storage is not obliged to carry.
- Pass a pointer to const unless you specifically intend the call to write. For a string that is the only defensible direction, since the accessor is permitted to hand back a pointer to a formatted copy rather than to the object's own storage.
- Let a C routine write into a growable array's storage when you need it to, on one condition: it must not change how many elements there are. Size the container first, pass its data and its capacity, then set the element count from whatever the routine reports it wrote.
- Bridge in both directions through a growable array. To fill some other container from such an interface, let it fill one of these and then construct the real container from the resulting range; to send some other container's contents out, copy them into one first and pass that.

## Don't
- Don't use the beginning iterator where a pointer is wanted. Its type is an iterator, and although implementations often make that a pointer for this container, nothing requires it — so code relying on the equivalence works until it is moved to an implementation where it does not.
- Don't let a C routine grow the data. Writing into unused capacity leaves the container's element count disagreeing with its contents, and writing past the capacity is worse than that.
- Don't forget what an embedded null does at the boundary. The string object is content to hold one; the interface receiving it will treat it as the end, so the data crossing is truncated without complaint from either side.
- Don't hand out a container carrying an invariant to something that may reorder it. A sequence kept sorted so it can be searched is still sorted only if the routine you passed it to left it that way, and re-establishing that is your problem after the call returns.

## Checklist
- Is the container checked for emptiness before its data pointer is taken?
- Is the parameter a pointer to const, and if not, what justifies the write?
- If the routine writes, is the container sized beforehand and its element count set afterwards from what the routine reported?
- Could the data contain an embedded null, and does the receiving side care?
- Does the container carry an invariant that the call might break?

## Notes
The whole technique rests on one guarantee — that this container's elements occupy contiguous memory, exactly as an array's do — which is why every other container has to be routed through one. That guarantee is what makes the container the interoperability point for the whole library rather than merely one option among several.

Two of Meyers's cautions have since been resolved and are worth not carrying forward. Strings are now guaranteed contiguous as well, so his warning that their storage may be scattered no longer applies; and both containers now expose a named accessor for their data pointer, which is clearer than taking the address of the first element and, for the empty case, better behaved.

Where you control both sides of the call, the modern framing is different in kind rather than in detail. A non-owning view over contiguous memory carries the pointer and the length as one object, so the count cannot be passed wrongly and the empty case needs no special handling — which removes most of what this card is defending against. The card's advice is for the boundaries you do not control, and those are the ones that last.
