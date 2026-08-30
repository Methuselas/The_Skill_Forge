---
object_id: AP_give_an_acquired_resource_an_owner
object_type: ap
name: Give an Acquired Resource an Owner
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
- raii
- resource_management
- ownership
- smart_pointers
cross_links:
- rel: related_to
  target_object_id: PAT_give_every_acquired_resource_one_named_owner
- rel: supports
  target_object_id: PAT_use_unique_ptr_for_exclusive_ownership
- rel: supports
  target_object_id: PAT_prefer_make_functions_to_direct_new
- rel: supports
  target_object_id: PAT_price_shared_ownership_before_choosing_it
- rel: supports
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: supports
  target_object_id: PAT_choose_raii_copying_behavior_deliberately
- rel: supports
  target_object_id: PAT_provide_access_to_raw_resource_in_raii_class
- rel: supports
  target_object_id: PAT_give_every_constructor_resource_a_self_releasing_owner
- rel: supports
  target_object_id: PAT_match_new_and_delete_forms
- rel: related_to
  target_object_id: AP_write_copy_control_for_a_resource_owning_class
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted C++ sources
confidence: high
references: []
variants: []
---

# Give an Acquired Resource an Owner

## Objective
Take code that acquires something needing release — heap memory, a file descriptor, a mutex lock, a socket, a connection — and move it behind an object whose destruction releases it, so that release happens on every exit path including the ones nobody wrote. Success is that no path out of the scope can skip the release, and that the ownership decision is visible in the type rather than implied by a comment.

## Steps / Flow

1. **Name the resource and its release call.** Write down what was acquired and the exact call that must eventually balance it. Where a function has several returns, a `break`, or anything that can throw, count the paths out — that count is what the manual release has to be correct on, and it is usually larger than it looks.

2. **Reach for a ready-made owner before writing anything.** An exclusive-ownership smart pointer is the default and covers most cases; `PAT_use_unique_ptr_for_exclusive_ownership` owns the choice, and moving up to shared ownership requires being able to name the second owner.

3. **Create it through the make function, not a bare allocation.** `PAT_prefer_make_functions_to_direct_new` owns why the allocation and the ownership transfer must not be two separable steps.

4. **Price shared ownership if you are about to reach for it.** *Gate.* Reference counting is not free, and this is the point to find that out rather than after profiling. `PAT_price_shared_ownership_before_choosing_it` owns the cost account, and it also owns the rule that additional owners are constructed from an existing owner rather than from the raw pointer again.

5. **Branch — when no ready-made owner fits, write the class.** A resource with a non-standard release, a paired acquire/release protocol, or a handle that is not a pointer needs its own manager. `PAT_manage_resources_with_raii_objects` owns the shape: acquire in the constructor, release in the destructor.

6. *Gate.* **A resource-managing class is not usable until copying has a defined meaning.** The compiler-generated copy will almost always mishandle the resource — double release, or two owners believing they are one. `PAT_choose_raii_copying_behavior_deliberately` owns the choice among prohibiting, reference counting, deep copying, and transferring. Once chosen, delegate the implementation to `AP_write_copy_control_for_a_resource_owning_class`; do not hand-roll it here.

7. **Give clients the raw resource where foreign interfaces demand it.** C APIs and older libraries will not take the wrapper. `PAT_provide_access_to_raw_resource_in_raii_class` owns the choice between an explicit accessor and an implicit conversion, and that choice trades safety against convenience rather than being free.

8. **Check the constructor's own acquisitions.** A constructor that acquires two things can throw between them, and a destructor never runs for an object that never finished constructing. `PAT_give_every_constructor_resource_a_self_releasing_owner` owns this case, which the class-level destructor cannot cover.

9. **Remove the manual release, then re-read every exit path.** Delete the release call the owner now performs. Where any manual release survives — a legacy path, an array — `PAT_match_new_and_delete_forms` owns getting the form right, because a mismatch is undefined behavior rather than a leak.

10. **Completion check.** Every acquisition in the scope has an owner; no exit path performs or skips a manual release; the ownership model is readable from the declaration; and if a class was written, copying either works or does not compile.

## Notes
The reason this is a protocol rather than a single rule is the branch at step 5 and the gate at step 6. Most resources never reach either — a ready-made owner takes them and the work is three steps. The cost of the flow is paid only by resources that genuinely need a bespoke manager, and that is exactly where an unordered set of rules produces a class that compiles, releases correctly on the happy path, and double-frees the first time someone copies it.

Ownership is a design decision the type system can carry, which is why step 2 comes before step 5. Writing a manager first and discovering afterwards that an exclusive-ownership pointer would have done is common and wasteful.
