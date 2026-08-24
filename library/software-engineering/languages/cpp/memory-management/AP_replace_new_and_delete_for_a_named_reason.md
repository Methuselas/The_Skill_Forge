---
object_id: AP_replace_new_and_delete_for_a_named_reason
object_type: ap
name: Replace new and delete for a Named Reason
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- allocation
- operator_new
- new_handler
cross_links:
- rel: supports
  target_object_id: PAT_replace_new_delete_only_with_clear_reason
- rel: supports
  target_object_id: PAT_reach_for_a_custom_allocator_only_for_what_it_can_buy
- rel: supports
  target_object_id: PAT_follow_new_delete_conventions
- rel: supports
  target_object_id: PAT_dont_hide_standard_new_forms
- rel: supports
  target_object_id: PAT_pair_placement_new_with_placement_delete
- rel: supports
  target_object_id: PAT_write_a_well_behaved_new_handler
- rel: supports
  target_object_id: PAT_provide_class_specific_new_handler_via_crtp
- rel: related_to
  target_object_id: PAT_match_new_and_delete_forms
- rel: related_to
  target_object_id: AP_tune_a_measured_bottleneck
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted C++ sources
confidence: high
references: []
variants: []
---

# Replace new and delete for a Named Reason

## Objective
Substitute your own allocation functions for the compiler's, at global or class scope, and leave behind a set that satisfies every obligation the language places on them — not only the one the replacement was written for. Success is a replacement that serves its stated purpose and that no client can trip over by allocating an array, allocating zero bytes, using a placement form, or being derived from.

## Steps / Flow

1. *Gate.* **Name the reason, or stop.** `PAT_replace_new_delete_only_with_clear_reason` owns the admissible list — detecting usage errors, speed, statistics, space overhead, alignment, clustering. If the reason is "allocation looked slow," it is not yet a reason; `AP_tune_a_measured_bottleneck` owns turning that into a measurement first. Most attempts should end here, and ending here is a success of the protocol rather than a failure of it.

2. **Check whether a container allocator is the smaller answer.** Where the need is confined to one container rather than a type, `PAT_reach_for_a_custom_allocator_only_for_what_it_can_buy` owns the shorter list of what that route actually delivers, and it avoids everything below.

3. **Decide the scope: global, or one class.** Global replacement affects every allocation in the program including the library's; class-specific replacement affects one type and everything derived from it. The obligations in steps 4 to 7 apply to both, but the blast radius of getting them wrong does not.

4. **Meet the conventions the language expects.** `PAT_follow_new_delete_conventions` owns the three that are easiest to omit: the loop that calls the new-handler rather than failing immediately, returning something valid for a zero-byte request, and forwarding a wrong-sized request to the global version rather than serving it from a class-specific pool sized for the base.

5. *Gate.* **Re-expose the standard forms your declaration just hid.** Declaring any allocation function in a class hides all the global ones — normal, placement, and nothrow — so clients who never asked for your allocator stop compiling. `PAT_dont_hide_standard_new_forms` owns the repair, typically a base class carrying the standard forms plus a using declaration.

6. **Pair every extra-parameter form with its matching release.** `PAT_pair_placement_new_with_placement_delete` owns this, and the cost of skipping it is silent: the constructor throws, no matching release exists, and the allocation leaks with nothing to indicate it. Keep the ordinary release form alongside.

7. **Branch — for allocation-failure behavior specific to this class.** `PAT_write_a_well_behaved_new_handler` owns what a handler must do to avoid an endless retry, and `PAT_provide_class_specific_new_handler_via_crtp` owns the mixin that gives one class its own handler without disturbing the global one.

8. **Verify against the forms nobody wrote a test for.** Allocate an array, allocate zero bytes, allocate an object of a derived class larger than the base, throw from a constructor after a placement form, and allocate through a client path that uses no custom form at all.

9. **Completion check.** The stated reason is measurably served; every standard form still compiles for clients; every extra-parameter form has its counterpart; failure behavior terminates; and a derived class does not receive base-sized memory.

## Notes
This protocol is mostly a gate followed by a conformance walk, and that is the shape the problem has. The decision to replace allocation is rare and reversible; the obligations that come with it are numerous, unenforced by the compiler, and individually invisible when omitted. An unordered set of the same rules reliably produces a replacement that serves its purpose and breaks a client six months later on the one form nobody exercised.

Step 5 deserves emphasis because it is a compile-time failure in *client* code rather than in the code being written, which puts it outside the author's normal feedback loop entirely.

The matching-form rule for ordinary allocation and release sits outside this flow: it applies to everyone, not only to those replacing the functions, which is why it is adjacent here rather than owned.
