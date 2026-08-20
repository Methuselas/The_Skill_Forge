---
object_id: PAT_use_unique_ptr_for_exclusive_ownership
object_type: pattern
name: Reach for Exclusive Ownership First
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
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: PAT_price_shared_ownership_before_choosing_it
- rel: related_to
  target_object_id: PAT_prefer_make_functions_to_direct_new
- rel: related_to
  target_object_id: PAT_pass_a_smart_pointer_only_to_transfer_ownership
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Reach for Exclusive Ownership First

## Pattern Rule
**IF** a dynamically allocated object needs an owner
**THEN** give it an exclusive-ownership smart pointer by default, and move up to shared ownership only when you can name the second owner
**ELSE** where the object genuinely has several independent owners whose lifetimes you cannot order, shared ownership is what the problem requires and its costs are the price of the requirement.

## Do
- Take the default seriously by knowing what it costs: an exclusive-ownership pointer is normally the same size as a raw pointer, and for most operations including dereferencing it compiles to the same instructions. Where a raw pointer is small and fast enough, this is too — which removes the usual excuse for managing lifetime by hand.
- Read it as a move-only type and let that express the design. A non-null one always owns what it points to; moving transfers ownership and nulls the source; copying is not available, because two owners of one object would each destroy it.
- Use it as the return type of a factory. The caller acquires exclusive ownership of what the factory produced, destruction happens on every path out including exceptional ones, and the result can be moved into a container, into a member, and down a chain of owners without any of them having to remember to release it.
- Return exclusive ownership even when some callers will want to share. Converting to a shared pointer is easy and cheap; the reverse is not available, so the exclusive form is the one that leaves the caller a choice.
- Supply a custom deleter where destruction is not a plain delete — a function object, or a lambda — and know that it becomes part of the pointer's type. That is what allows the compiler to store a stateless deleter for free.
- Watch the size when the deleter is not stateless. A capturing lambda, a stateful function object, or a function pointer all make the pointer larger than a raw pointer, which is worth knowing before it goes in a container of millions.

## Don't
- Don't reach for shared ownership as the safe default. It is the more expensive of the two in size, in allocation, and in synchronization, and the decision to use it should follow from a second owner actually existing.
- Don't keep the deprecated C++98 auto-pointer in new code. It co-opted copying to mean moving because the language had no moves yet, so copying one nulls the source and it cannot be stored in containers. Its only remaining use is compiling under a C++98 compiler; the exclusive-ownership pointer does everything it did, as efficiently, without deforming what a copy means.
- Don't hand a raw pointer to an array to a smart pointer expecting the array form of delete. Use a container instead, which is what the array case wants anyway.
- Don't treat automatic destruction as unconditional. Local objects are not destroyed if an exception escapes a thread's top-level function, if a non-throwing promise is violated, or if the program is aborted or exited outright.

## Checklist
- Does this object have exactly one owner at a time, and can you name it?
- If shared ownership is being proposed, who is the second owner?
- Is the factory here returning the most transferable ownership form?
- Does the deleter carry state, and has the resulting size been considered?
- Is any deprecated auto-pointer still in this code?

## Notes
The reason exclusive ownership is the right default is not that sharing is dangerous but that it is a stronger claim about the program. Exclusive ownership says the lifetime is determined by one place, which is a fact you can check by reading that place. Shared ownership says the lifetime is determined by whichever owner happens to release last, which is not visible anywhere in particular. Choosing the stronger claim when it is true costs nothing and keeps the weaker one available.

That the pointer is normally the size of a raw pointer, and compiles to the same instructions, is what makes the default practical rather than aspirational. Historically the argument for managing memory manually was that the wrapper cost something; here it does not, so the argument reduces to habit.

The custom deleter's effect on the type deserves attention when designing an interface around one, because it is easy to discover late. Two exclusive pointers to the same kind of object with different deleters are different types, and a container cannot hold both — a constraint that does not exist for the shared form, where the deleter lives in the control block instead of the type.
