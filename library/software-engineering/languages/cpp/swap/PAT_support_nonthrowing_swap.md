---
object_id: PAT_support_nonthrowing_swap
object_type: pattern
name: Support a Non-throwing swap for Pimpl-style Types
library_path:
- software-engineering
- languages
- cpp
- swap
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- swap
- exception_safety
- pimpl
cross_links:
- rel: related_to
  target_object_id: PAT_handle_self_assignment_in_copy_assignment
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Support a Non-throwing swap for Pimpl-style Types

## Pattern Rule
**IF** the default std::swap would be inefficient for your type — typically a pimpl type holding a pointer to its real data
**THEN** provide a fast, non-throwing swap: a public swap member that exchanges the internals, a non-member swap in your type's namespace that calls it, and, for a class, a total specialization of std::swap that also calls it.

## Do
- Write a public member swap that exchanges the internal pointers and never throws.
- Add a non-member swap in the same namespace that calls the member, so argument-dependent lookup finds it.
- For a non-template class, also totally specialize std::swap to call the member, so even a qualified std::swap call gets the fast version.
- When you call swap yourself, write `using std::swap;` and then call swap unqualified, so the best version is chosen.

## Don't
- Don't add a new overload or a partial specialization of swap inside namespace std; totally specializing an existing template there is allowed, but adding to std is undefined behavior.
- Don't let the member swap throw — the strong exception-safety guarantee in other code depends on it.

## Checklist
- Is there a non-throwing member swap that exchanges only the internals?
- Is there a non-member swap in the type's namespace that calls the member?
- For a class, is std::swap totally specialized (not overloaded, not partially specialized)?
- Do my own swap calls use an unqualified swap after `using std::swap;`?

## Notes
The default swap copies three whole objects, which is wasteful for a pimpl type where swapping the internal pointers suffices. The full recipe is: a non-throwing member swap; a namespace-level non-member swap that calls it (found by argument-dependent lookup); and, for non-template classes, a total specialization of std::swap that also calls it — because some misguided code writes `std::swap` qualified and would otherwise miss your version. You may totally specialize std templates but must never add new templates to std. The non-throwing guarantee on the member matters because exception-safe code relies on it.
