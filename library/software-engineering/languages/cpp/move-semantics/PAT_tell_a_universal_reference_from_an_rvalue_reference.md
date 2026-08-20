---
object_id: PAT_tell_a_universal_reference_from_an_rvalue_reference
object_type: pattern
name: Tell a Universal Reference From an Rvalue Reference
library_path:
- software-engineering
- languages
- cpp
- move-semantics
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- move_semantics
- templates
- type_deduction
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_choose_between_auto_and_decltype_auto
- rel: related_to
  target_object_id: PAT_avoid_overloading_on_universal_references
- rel: related_to
  target_object_id: PAT_return_by_value_when_returning_new_object
- rel: related_to
  target_object_id: PAT_understand_special_member_generation
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Tell a Universal Reference From an Rvalue Reference

## Pattern Rule
**IF** you are holding a parameter declared with a double ampersand and deciding what to do with it
**THEN** determine first whether it is a universal reference or a true rvalue reference, because the answer decides which cast to apply — an unconditional one to rvalue references, a conditional one to universal references
**ELSE** where the parameter is an ordinary lvalue reference or a value, neither cast belongs there and applying one is how a caller's object gets silently emptied.

## Do
- Apply the test, which is narrow. A parameter is a universal reference only if its declared form is precisely `T&&` for a deduced `T`, or the object is declared `auto&&`. Anything else — a const qualifier in the way, a nested type, a member of a class template whose parameter was fixed when the object was created — is an ordinary rvalue reference, whatever it looks like.
- Remember what each cast actually is, because the names mislead. Neither moves nor forwards anything, and neither generates any run-time instructions. One is an unconditional cast to an rvalue; the other performs the same cast only when its argument was bound to an rvalue. A better name for the first would have been an rvalue cast.
- Cast on the last use of the parameter and not before. A cast to rvalue tells everything downstream that the object may be plundered, so any later read of it is reading whatever the plundering left.
- Apply the same rule to values being returned by a function that returns by value: unconditional cast for an rvalue reference parameter, conditional cast for a universal reference one.
- Understand why the deduction produces this behaviour, since it makes the rest predictable. When an lvalue is passed to a deduced `T&&`, `T` is deduced as an lvalue reference, producing a reference to a reference — which collapses. The collapse rule is one line: if either reference is an lvalue reference the result is an lvalue reference, otherwise it is an rvalue reference. That happens during template instantiation, `auto` deduction, alias and typedef formation, and `decltype`.

## Don't
- Don't cast a local object to an rvalue on the way out of a function that returns by value. The compiler was entitled to construct that local directly in the caller's storage, and the cast forbids it — you have asked for a move where no work at all was going to happen.
- Don't move from a const object and expect a move. The move constructor takes a non-const rvalue reference and cannot bind it; the copy constructor takes a reference to const, which can. So the cast succeeds, the copy runs, and the code is correct and exactly as slow as before — which is why a parameter you intend to move from must not be const.
- Don't expect forwarding to be perfect. Braced initializers cannot be deduced, a literal zero or the null macro forwards as an integer rather than a null pointer, declaration-only static const members can fail to link, overloaded function names and template names give the compiler no single type to deduce, and bitfields cannot be bound to a reference at all.
- Don't apply either cast to a parameter you will use again. The object is left in a valid but unspecified state, and nothing in the code marks the point after which reading it is meaningless.

## Checklist
- Is the declared form exactly a double ampersand on a deduced type, with no const and no nesting?
- Is the cast being applied at the last use of the parameter?
- Is anything being moved from that is declared const?
- Is a local being cast on return where the compiler could have elided the copy entirely?
- If forwarding fails to compile, is the argument one of the kinds that cannot be forwarded?

## Notes
The two names are the source of most of the confusion, and replacing them mentally with what they do removes it: both are casts, one unconditional and one conditional, and neither emits an instruction. What follows the cast — an actual move, a copy, or nothing — is decided by overload resolution on the result, which is why a cast on a const object quietly selects the copy constructor and why a cast on a return value can suppress an optimization rather than enable one.

The narrowness of the universal-reference form is worth over-learning, because near misses are common and behave completely differently. A const-qualified double ampersand is an rvalue reference. A double ampersand on a member of a class template, where the template argument was fixed when the object was created, is an rvalue reference — no deduction happens at the call. Only a deduced type in exactly that form binds both lvalues and rvalues.

Reference collapsing is presented as an obscure rule and is really the mechanism that makes the whole feature work. A universal reference binding an lvalue produces a reference to a reference, which the language forbids as a written type and permits as a deduced one; collapsing resolves it, and the direction of the collapse — lvalue wins — is exactly what preserves the caller's lvalue-ness through the forwarding call.
