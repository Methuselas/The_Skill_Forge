---
object_id: PAT_follow_new_delete_conventions
object_type: pattern
name: Follow the Conventions When Writing new and delete
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- allocation
- conventions
cross_links:
- rel: related_to
  target_object_id: PAT_give_polymorphic_base_a_virtual_destructor
- rel: related_to
  target_object_id: PAT_match_new_and_delete_forms
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Follow the Conventions When Writing new and delete

## Pattern Rule
**IF** you write your own operator new or operator delete
**THEN** follow the required conventions: operator new loops calling the new-handler, returns a valid pointer even for a zero-byte request, and forwards wrong-sized requests to the global version; operator delete does nothing on a null pointer and forwards wrong-sized blocks to the global version.

## Do
- In operator new, loop: attempt the allocation, and on failure call the current new-handler (obtained via set_new_handler), throwing bad_alloc only when the handler pointer is null; treat a zero-byte request as a one-byte request.
- In a class-specific operator new, forward any request whose size differs from the class size to the global operator new (this also covers the zero-byte case, since a class size is never zero), and mirror the forwarding in operator delete.

## Don't
- Don't forget that a base class operator new is inherited, so it can be asked for a derived object's larger size; check the size and hand the wrong sizes to the global version.
- Don't omit the virtual destructor on a base class; without it the size_t value passed to operator delete can be wrong.

## Checklist
- Does operator new loop on the new-handler, handle zero bytes, and always return a valid pointer or throw?
- Do class-specific new and delete forward wrong-sized requests to the global versions?
- Do base classes have virtual destructors so operator delete receives the correct size?

## Notes
A conforming operator new returns a valid pointer even for zero bytes (treat it as one), loops calling the new-handler, and throws bad_alloc only when the handler is null. Because operator new is inherited, a base version may be handed a derived object's size, so forward any size that is not the class's own to the global operator new — a test that also subsumes the zero-byte case. operator delete must be null-safe and forward wrong-sized blocks; and a missing virtual destructor can make the size passed to delete wrong.
