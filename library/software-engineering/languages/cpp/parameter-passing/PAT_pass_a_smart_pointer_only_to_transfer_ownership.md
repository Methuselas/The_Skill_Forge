---
object_id: PAT_pass_a_smart_pointer_only_to_transfer_ownership
object_type: pattern
name: Pass a Smart Pointer Only to Transfer Ownership
library_path:
- software-engineering
- languages
- cpp
- parameter-passing
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- parameter_passing
- smart_pointers
- ownership
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_pass_by_reference_to_const
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Pass a Smart Pointer Only to Transfer Ownership

## Pattern Rule
**IF** a function needs to operate on an object whose lifetime is managed by a smart pointer
**THEN** pass a reference or a raw pointer to the object itself, and reserve passing the smart pointer for the case where the function genuinely takes over or shares ownership
**ELSE** where the function stores what it is given beyond the call, it does need ownership, and the smart pointer is the correct parameter.

## Do
- Let the parameter type state the ownership intent, because that is what a reader has to work out otherwise. A reference or raw pointer says the function uses the object and will not delete it; a smart pointer parameter says lifetime is changing hands.
- Choose between reference and raw pointer on whether absence is meaningful. A reference is a pointer that cannot be null, so a parameter that must always refer to an object should be a reference, and one the function is prepared to receive as null should be a pointer — the declaration then documents which case the function handles.
- Add const where the function does not modify the object, so the two facts a caller needs — no deletion, no modification — are both visible in the signature.
- Return owning pointers from factories as unique pointers. A caller that wants shared ownership can construct one from the unique pointer cheaply, and a factory that returns a shared pointer has made that choice for every caller including those that did not need it.
- Apply the same reasoning inside containers. A container of raw pointers is right where the objects' lifetimes are managed elsewhere; a container of unique pointers is right where the container itself should own them.

## Don't
- Don't pass a shared pointer by value out of habit. Copying one is not cheap — the reference count is atomic, so every copy and destruction is a synchronized read-modify-write on shared state, which is exactly the operation that does not scale across threads.
- Don't return a reference or a pointer to a local object. The object is destroyed when the function returns, and the caller receives something that refers to memory that no longer holds it.
- Don't hand out a raw pointer to an object whose owner may release it during the call. This is safe precisely because someone else is holding the object alive for the duration; where that is not true, the function does need a share of the ownership.
- Don't use a smart pointer parameter as a way to avoid thinking about lifetime. It settles the question by making the function an owner, which is a design decision with a cost, not a default.

## Checklist
- Does this function outlive the call in any way — does it store what it is given?
- If not, is the parameter a reference or raw pointer to the object rather than to its owner?
- Can the argument legitimately be absent, and does the parameter type say so?
- Is the object guaranteed alive for the duration of the call, and by whom?
- Does a factory here return the most transferable ownership type rather than the most convenient one?

## Notes
The performance argument and the design argument point the same way, which is why this is worth applying consistently rather than case by case. Copying a shared pointer costs an atomic increment now and an atomic decrement later; passing the object by reference costs nothing. And a signature that takes the object rather than its owner is the one that tells the reader what the function does with it.

Ownership types are worth thinking of as ordered by transferability. A unique pointer can become a shared pointer cheaply; the reverse is not available. So the general rule for anything crossing an interface is to hand over the form that leaves the receiver the most options, which for a newly created object is the unique pointer.

There is a boundary worth stating so the rule does not overreach. Non-owning access is safe only for as long as some owner is keeping the object alive, and in single-threaded code the call stack usually guarantees that. In concurrent code it does not: an object can be released by another thread mid-call, and that is a case where sharing ownership is the answer rather than an unnecessary cost.
