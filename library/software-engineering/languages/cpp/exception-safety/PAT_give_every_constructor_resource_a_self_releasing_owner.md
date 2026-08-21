---
object_id: PAT_give_every_constructor_resource_a_self_releasing_owner
object_type: pattern
name: Give Every Constructor-Acquired Resource a Self-Releasing Owner
library_path:
- software-engineering
- languages
- cpp
- exception-safety
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- exception_safety
- constructors
- raii
- resource_management
cross_links:
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: PAT_use_unique_ptr_for_exclusive_ownership
- rel: related_to
  target_object_id: PAT_offer_an_exception_safety_guarantee
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Give Every Constructor-Acquired Resource a Self-Releasing Owner

## Pattern Rule
**IF** a constructor acquires a resource and can still throw afterwards — which it can whenever it acquires a second one, or calls anything that might fail
**THEN** hold each resource in a member that releases itself when destroyed, rather than in a raw handle that the class destructor is expected to clean up, because a constructor that throws means that destructor is never going to run
**ELSE** where every member is already a self-owning type and the constructor body acquires nothing itself, there is nothing left to protect and no cleanup code belongs in the constructor at all.

## Do
- Fix the rule that creates the hazard, because everything else follows from it: only fully constructed objects are destroyed, and an object is not fully constructed until its constructor has run to completion. A throw partway through means the destructor is skipped permanently, not deferred.
- Notice the asymmetry the fix exploits. Members are constructed before the constructor body begins, so any member that finished constructing *is* destroyed during the unwind — the language is only refusing to clean up what the half-built enclosing object was managing by hand.
- Convert the raw handles into owning members and then check whether the destructor still has a body. Frequently it does not, and the class can drop it entirely, which is a signal the ownership actually moved rather than being duplicated.
- Treat const members as forcing the issue rather than complicating it. A const handle can only be set from the member initializer list, and the list admits expressions rather than statements, so no try block can be written there — the owning-member form is the only one that works.

## Don't
- Don't try to rescue the situation from the creation site by wrapping the construction in a try block and releasing the pointer in the handler. No assignment to that pointer happens unless the construction completes, so the handler releases a null pointer and the resource acquired inside the constructor is still lost.
- Don't settle for catching everything in the constructor body, releasing by hand, and rethrowing. It does work while the handles are non-const raw pointers, but it duplicates the destructor's body — so the class now has two copies of its cleanup logic — and it stops being available the moment any handle becomes const.
- Don't push each resource's cleanup into a separate private initializer function that catches and releases the ones initialized before it. That is correct, and it scatters what is conceptually one constructor across several functions whose correctness depends on remembering the exact order members are initialized in.

## Checklist
- Does this constructor acquire two or more things, or acquire one and then call anything that could throw?
- If it threw between the first acquisition and the last, what would release the first?
- Is each resource held by something whose own destructor frees it?
- Does the class destructor now contain anything the members would not do themselves?

## Notes
The language's refusal here is a deliberate cost decision rather than an oversight. Destroying a partly constructed object would mean knowing how far its constructor got, which means recording that progress in every object — larger objects and slower constructors, charged to all code to serve the exceptional path. The price of not paying it is that constructors have to clean up after themselves.

That framing explains why moving ownership into members is the real fix and the try-block versions are workarounds. Members convert the problem into one the language already solves, because per-member construction progress is exactly the bookkeeping compilers do keep.

The same reasoning covers members that are not pointers at all. Strings, containers, and any other fully constructed member are destroyed correctly during the unwind without help — but if their own constructors call something that might throw, they owe the same duty one level down.
