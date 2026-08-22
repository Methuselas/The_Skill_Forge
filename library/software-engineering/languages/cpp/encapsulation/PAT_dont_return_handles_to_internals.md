---
object_id: PAT_dont_return_handles_to_internals
object_type: pattern
name: Don't Return Handles to Object Internals
library_path:
- software-engineering
- languages
- cpp
- encapsulation
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- encapsulation
- const_correctness
- dangling
cross_links:
- rel: related_to
  target_object_id: PAT_declare_data_members_private
- rel: related_to
  target_object_id: PAT_use_logical_constness_with_mutable
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Don't Return Handles to Object Internals

## Pattern Rule
**IF** a member function would hand back a reference, pointer, or iterator to the object's internal data
**THEN** avoid it — a returned handle breaks encapsulation, lets a const function's caller modify internals, and can dangle when a temporary owner is destroyed.

## Do
- Return by value, or return a const handle only when you deliberately intend read-only access to something the object genuinely exposes.
- Treat private and protected member functions as internals too — never return a pointer to a less-accessible member function.

## Don't
- Don't return a non-const reference, pointer, or iterator to a data member; a member is only as encapsulated as the most accessible function returning a handle to it, so this makes it effectively public.
- Don't return a handle from a function whose result may outlive the object — a handle into a temporary returned by value dangles at the end of the statement.
- Don't return one from a type that guards itself for concurrent use, on any path. The handle leaves the guarded region while still referring to what the guard protects, so the caller reaches the internals with no lock held at all — the type's whole guarantee, undone by one function that looked like an accessor.

## Checklist
- Does this function return a reference, pointer, or iterator into the object's internals?
- Could that handle let a caller modify a const object, or outlive the object and dangle?
- If access is intended, is it limited to read-only through a const handle?

## Notes
`Rectangle::upperLeft`/`lowerRight` returning non-const references to internal points let a caller mutate a const rectangle — a const member function handing out a writable handle. Making the return const fixes the modification hole but not the dangling one: `boundingBox(*pgo).upperLeft()` takes a handle into a temporary that dies at the statement's end. References, pointers, and iterators are all handles; returning any of them risks outliving the object. operator[] on string and vector is the rare, deliberate exception.
