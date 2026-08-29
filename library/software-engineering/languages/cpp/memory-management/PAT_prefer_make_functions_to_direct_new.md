---
object_id: PAT_prefer_make_functions_to_direct_new
object_type: pattern
name: Prefer the make Functions to Direct Use of new
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- smart_pointers
- exception_safety
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_use_unique_ptr_for_exclusive_ownership
- rel: related_to
  target_object_id: PAT_price_shared_ownership_before_choosing_it
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: PAT_choose_braces_or_parentheses_deliberately
- rel: related_to
  target_object_id: AP_give_an_acquired_resource_an_owner
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants:
- variant_id: VAR_standalone_new_statement
  variant_name: Put the new and Its Smart Pointer in a Standalone Statement
  variant_basis: constraint
  difference_from_foundation: The object is still created with a direct `new`, but the
    smart pointer that will own it is constructed in its own statement, before the call
    that consumes it, rather than inside the argument list.
  when_to_use: A make function cannot be used — a custom deleter is required, a braced
    initializer must be passed, or the type has class-specific allocation functions that
    a single-allocation make function would bypass. Compilers may not reorder operations
    across statement boundaries, so the raw pointer cannot be stranded between the
    allocation and its capture.
  when_not_to_use: A make function is available and none of those constraints apply. The
    standalone statement prevents the leak and does nothing about the duplicated type
    name or the second allocation.
  absorbed_from_object_id: PAT_store_newed_object_in_smart_pointer_standalone
---

# Prefer the make Functions to Direct Use of new

## Pattern Rule
**IF** you are creating an object to be owned by a smart pointer
**THEN** create it with the corresponding make function rather than passing a `new` expression to the smart pointer's constructor
**ELSE** where the pointer needs a custom deleter, or the object must be initialized with a braced initializer, the make functions cannot express it and direct `new` is the answer — under the standalone-statement discipline below.

## Do
- Take the leak first, because it is the reason this is a correctness rule and not a style one. Constructing a smart pointer from a `new` expression inside an argument list gives the compiler three operations to order — the allocation, the smart pointer's constructor, and the evaluation of the other arguments — and it is free to run the other argument between the first two. If that argument throws, the allocation has happened and nothing owns it.
- Let the make function close the window rather than reasoning about the ordering. It performs the allocation and the capture as one call, so there is no interval in which a raw pointer exists unowned.
- Count the second benefit where shared ownership is involved: a make function for a shared pointer performs one allocation for the object and its control block together, where a direct `new` performs two. The result is smaller and faster code and one less trip to the allocator.
- Stop writing the type twice. `new` names the type and so does the smart pointer being constructed, and the make function names it once — which matters most when the type is long and when it later changes.
- Fall back to direct `new` deliberately where the make functions cannot serve, and then keep the allocation in its own statement. That is the older discipline, preserved here as `VAR_standalone_new_statement`, and it still prevents the leak.
- Prefer passing a `new` expression directly to the smart pointer's constructor over passing a named raw pointer variable, in that fallback case. A named raw pointer invites a second smart pointer to be constructed from the same address, and two owners of one object each believe they must destroy it.

## Don't
- Don't use a make function when a custom deleter is required. There is no way to supply one, and the deleter is part of what the pointer is for.
- Don't use a make function expecting a braced initializer to be forwarded as one. The arguments are forwarded with parentheses, which is a deliberate documented choice — the make function cannot know which delimiter the caller wanted, and for some types the two select different constructors.
- Don't assume the single-allocation benefit is free of consequences for shared pointers. The object and its control block occupy one block of memory, so that memory cannot be released until the last weak reference is gone, not merely the last shared one. For a large object with long-lived weak references, two allocations may be preferable.
- Don't use a shared-pointer make function for a class with its own allocation functions. Those are written for objects of the class's size and the make function asks for a larger block containing the control block too.

## Checklist
- Does any `new` expression here appear inside an argument list?
- Is the type named more than once at this creation site?
- If a make function is not being used, which of the documented limitations applies?
- Where direct `new` is unavoidable, is it in its own statement, and is the result passed straight to the smart pointer rather than through a named variable?
- For shared ownership of a large object, will weak references keep its memory alive after the object is destroyed?

## Notes
The predecessor to this rule addressed the same leak by a different route: put the allocation and the smart-pointer construction in a statement of their own, since compilers may not reorder across statement boundaries. That works, it remains correct, and it is preserved here as a variant for the cases the make functions cannot cover. What it does not do is remove the duplicated type name or the second allocation, and it leaves the programmer responsible for a discipline that the make functions make unnecessary. It is recorded as `VAR_standalone_new_statement`, and it is the right form whenever a custom deleter, a braced initializer, or a class-specific allocation function rules the make functions out.

The exception-ordering hazard is worth understanding rather than memorizing, because it recurs wherever a resource is acquired inside an argument list. The language does not specify the order in which a call's arguments are evaluated, only that each is complete before the call. Any acquisition that has happened but not yet been captured by an owner is exposed to whatever else the compiler chooses to run in between.

The trade on the single allocation is the one place where the recommendation genuinely reverses, and it is worth stating precisely so it is not applied superstitiously. Combining the object and its control block is the source of the performance advantage and also means the block is freed only when both counts reach zero. Weak references keep the control block alive; with a separate allocation they keep only the control block alive, and with a combined one they keep the object's storage alive too.
