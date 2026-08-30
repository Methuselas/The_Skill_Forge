---
object_id: DRILL_implement_nonthrowing_swap_for_pimpl
object_type: drill
name: Implement an Efficient Non-throwing swap for a Pimpl Type
target_skill: Wiring up member swap, namespace non-member swap, and a std::swap specialization
library_path:
- software-engineering
- languages
- cpp
- swap
stage_binding: 3 rough
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- swap
- pimpl
- exception_safety
cross_links:
- rel: related_to
  target_object_id: PAT_support_nonthrowing_swap
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Implement an Efficient Non-throwing swap for a Pimpl Type

## Practice Task
Given a `Widget` that holds a pointer to a `WidgetImpl` (the pimpl idiom), give it an efficient, non-throwing swap wired up correctly.

## Target Skill
Providing a member swap, a namespace non-member swap, and a std::swap specialization, and calling swap correctly.

## Setup
No special setup required.

## Instructions
- Add a public member swap that exchanges the two internal pointers and cannot throw.
- Add a non-member swap in Widget's namespace that calls the member.
- For this non-template class, totally specialize std::swap to call the member.
- Write a client that does `using std::swap;` then calls swap unqualified, and confirm the Widget-specific version is chosen.

## Success Check
- The member swap is confirmed to exchange only the pointers, checked by observing that the pointed-to data was never touched.
- The no-throw property is argued from what the member actually does, and the run states what would break it. A swap of anything that allocates is not this technique and will not hold the guarantee callers depend on.
- Both call forms are exercised and each shown to reach the fast version, with the unqualified call written exactly as clients write it. The whole technique turns on the lookup, so a qualified-only test skips the case being taught.
- The run says why the non-member in the class's own namespace is what makes the unqualified call work, rather than treating the several overloads as ceremony to be copied.
- The total specialization of the standard template is checked as legal here because this is a non-template class, and the run states what the answer would be for a class template instead, since that is exactly where the technique changes.

## Common Failures
- Adding an overload or a partial specialization of swap inside namespace std.
- Qualifying the call as std::swap and losing argument-dependent lookup to the type-specific version.

## Notes
This drills Item 25: the three-part setup plus the unqualified-call convention is what makes the fast, non-throwing swap reachable in every context, including code that wrongly qualifies the call.
