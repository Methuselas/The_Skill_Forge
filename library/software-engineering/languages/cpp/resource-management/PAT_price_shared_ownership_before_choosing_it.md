---
object_id: PAT_price_shared_ownership_before_choosing_it
object_type: pattern
name: Price Shared Ownership Before Choosing It
library_path:
- software-engineering
- languages
- cpp
- resource-management
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- resource_management
- smart_pointers
- ownership
- concurrency
cross_links:
- rel: related_to
  target_object_id: PAT_use_unique_ptr_for_exclusive_ownership
- rel: related_to
  target_object_id: PAT_pass_a_smart_pointer_only_to_transfer_ownership
- rel: related_to
  target_object_id: PAT_prefer_make_functions_to_direct_new
- rel: related_to
  target_object_id: PAT_keep_memory_alive_until_the_compare_and_swap_completes
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Price Shared Ownership Before Choosing It

## Pattern Rule
**IF** you are considering a reference-counted smart pointer because several parties need to keep an object alive
**THEN** account for what the reference count costs in size, allocation, and synchronization before adopting it, and construct every additional owner from an existing owner rather than from a raw address
**ELSE** where an owner may legitimately outlive the object and must be able to tell, that is what a non-owning weak reference is for, and it is not the same decision.

## Do
- Know the three costs, since they are what distinguish this from exclusive ownership. The pointer is typically twice the size of a raw pointer, because it carries the address of a separately allocated control block as well as the object. That control block is an allocation of its own unless a make function combined them. And every copy and destruction adjusts the count atomically, because the count is shared mutable state.
- Read the atomic increment as the cost it is. Atomic operations are slower than ordinary ones, and copying such a pointer is not free even though nothing was allocated — which is why passing one by value into a function that only reads the object is a real waste rather than a stylistic one.
- Construct every subsequent owner from an existing smart pointer, never from the raw address again. A second smart pointer built from the same raw pointer creates a *second* control block, so two independent reference counts each reach zero and the object is destroyed twice.
- Avoid the named raw pointer variable entirely where you must use a direct allocation, and pass the allocation expression straight to the constructor. A raw pointer sitting in a variable is what makes the second construction look reasonable to whoever writes it.
- Use the standard base-class template when an object needs to hand out shared ownership of itself. Constructing a pointer from `this` inside a member function is the same double-control-block bug wearing a disguise, and the base class exists so the object can produce a pointer that shares the existing count instead.
- Reach for a weak reference where an observer must not keep the object alive: a cache whose entries may have been evicted, a list of observers that may have been destroyed, and breaking cycles between objects that point at each other. A weak reference is not a pointer you dereference — it is asked whether the object is still there, and yields a shared pointer if so.

## Don't
- Don't adopt shared ownership for convenience. It approaches the convenience of garbage collection and it is not free, and the decision should follow from a genuine second owner rather than from not wanting to think about lifetime.
- Don't create a shared pointer from a raw pointer that another shared pointer already owns. This is the central hazard of the type, and it produces a double destruction rather than a diagnostic.
- Don't expect cycles to be collected. Two objects holding shared pointers to each other keep each other alive forever; one side has to be a weak reference, and choosing which is a design decision.
- Don't assume the object's memory is released when the object is destroyed. Weak references keep the control block alive past the object's destruction, and where the object and control block share one allocation, the object's storage stays with it.

## Checklist
- Who are the owners, and does each genuinely need to keep the object alive?
- Is every owner after the first constructed from another smart pointer?
- Does any raw pointer variable here get handed to a smart pointer constructor?
- Does the object ever need to produce a shared pointer to itself?
- Is there a cycle, and which side of it should be weak?
- Is the pointer being copied on paths that only need to read the object?

## Notes
The control block is the thing to hold in mind, because nearly every hazard here follows from it. There is meant to be exactly one per object; it holds the reference count, a second count for weak references, and copies of any custom deleter and allocator. Construct a shared pointer from a raw address and one is created; construct it from another shared or weak pointer and the existing one is used. Every double-free in this family of bugs is two control blocks for one object.

Where the deleter lives is a genuine design difference from exclusive ownership rather than an implementation detail. Here it sits in the control block, so it is not part of the pointer's type — two shared pointers to the same kind of object with different deleters have the same type and can share a container. That flexibility is bought with the indirection that makes the pointer twice the size.

The weak reference is often introduced as the cycle-breaker and its more common use is the dangling-observer problem. Anything that holds a reference to an object it does not own — a cache entry, a registered observer, a handle into a table — needs to distinguish "the object is gone" from "the object is here", and a raw pointer cannot. That question is what the weak form answers, and answering it is not the same as owning.
