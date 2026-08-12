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
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u04, pp. 106-112
  evidence_type: text
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
- Swapping two Widgets exchanges only the internal pointers, not the underlying data.
- Both an unqualified swap and a qualified std::swap call reach the fast version.

## Common Failures
- Adding an overload or a partial specialization of swap inside namespace std.
- Qualifying the call as std::swap and losing argument-dependent lookup to the type-specific version.

## Notes
This drills Item 25: the three-part setup plus the unqualified-call convention is what makes the fast, non-throwing swap reachable in every context, including code that wrongly qualifies the call.
