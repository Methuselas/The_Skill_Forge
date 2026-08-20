---
object_id: PAT_choose_between_auto_and_decltype_auto
object_type: pattern
name: Choose Between auto and decltype(auto)
library_path:
- software-engineering
- languages
- cpp
- type-deduction
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- type_deduction
- auto
- templates
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_auto_for_local_variables
- rel: related_to
  target_object_id: PAT_force_the_deduced_type_with_an_explicit_cast
- rel: related_to
  target_object_id: PAT_return_by_value_when_returning_new_object
- rel: related_to
  target_object_id: PAT_prefer_pass_by_reference_to_const
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Choose Between auto and decltype(auto)

## Pattern Rule
**IF** you are letting a type be deduced and it matters whether the result is a copy or refers to the original
**THEN** use `auto` when you want a copy and `decltype(auto)` when the reference and const qualification of the initializing expression must survive
**ELSE** where the expression yields a value rather than a reference to anything, the two agree and the plain `auto` is the one to write.

## Do
- Hold the one rule that explains most surprises: plain `auto` follows template deduction, which discards reference-ness always and top-level const for by-value deduction. `auto myWidget = cw;` where `cw` is a `const Widget&` gives a `Widget` — a copy, modifiable. `decltype(auto) myWidget = cw;` gives a `const Widget&`.
- Reach for `decltype(auto)` on a function whose return type must be whatever the underlying expression returns. A wrapper returning `c[i]` declared `auto` returns `int` where `c[i]` returned `int&`, so assigning through the call does not compile; declared `decltype(auto)`, it returns the reference and the wrapper is transparent.
- Treat any extra parentheses around a returned name as a change of type, not of formatting. `decltype` on a name gives the declared type; on any other lvalue expression of type `T` it gives `T&`. So `return x;` deduces `int` while `return (x);` deduces `int&` — and in a function that means returning a reference to a local.
- Remember that reference-ness is preserved when an array or function name is bound to a reference and lost otherwise. Passed by value, an array name decays to a pointer and its size is gone; bound to a reference parameter, the deduced type is the full array type including its extent, which is how a compile-time array-size function is written.
- Verify a deduced type rather than assuming it, when it matters. Instantiating an undefined class template with the type produces an error message that names it exactly; a dedicated type-index library prints it accurately at run time.

## Don't
- Don't trust an IDE's type display or a run-time `typeid` name for anything subtle. Both routinely drop const and reference qualification, so the two properties that decide this choice are the two most likely to be missing from what the tool shows you.
- Don't use `decltype(auto)` casually because it seems more precise. It preserves whatever the expression yields, including references to things that are about to be destroyed, and the failure is a dangling reference rather than a compile error.
- Don't expect a plain `auto` parameter or return type to keep an argument's constness. By-value deduction drops const, so a copy of a const object is not const — which is correct, since the copy is a separate object, and surprising the first time it matters.
- Don't reason about universal references as though they were rvalue references. A parameter declared `T&&` in a deduced context deduces `T` as an lvalue reference when the argument is an lvalue — the only situation in which `T` is deduced to be a reference at all.

## Checklist
- Should this name refer to the initializer, or hold a copy of it?
- If this is a function return type, does a caller need to assign through the result?
- Are there parentheses around the expression in a `decltype(auto)` return statement?
- Could the expression's referent be destroyed before the deduced reference is used?
- If the deduced type is in doubt, has it been printed by a tool that preserves const and reference qualification?

## Notes
The reason these two spellings exist is that deduction has to serve two different intentions, and one keyword cannot. Most of the time a declaration wants a value it owns, and dropping references and const is exactly right. Occasionally a declaration — most often a return type on a forwarding wrapper — needs to be transparent, passing through whatever the wrapped expression produced. `decltype(auto)` is that second intention made available in the places `auto` already worked.

The parenthesis rule is the one to commit to memory, because it is the only case in ordinary code where whitespace-adjacent syntax changes semantics this severely. It follows from `decltype`'s definition rather than being a special case: names report their declared type, and other lvalue expressions report an lvalue reference. Wrapping a name in parentheses stops it being a name.

Underneath both is a single set of deduction rules with three cases, and knowing them removes most of the surprise from both keywords: by-reference and by-pointer parameters keep the argument's const and drop its reference-ness; by-value parameters drop both; and a `T&&` parameter in a deduced context behaves differently for lvalue and rvalue arguments than any other reference does. The tools listed above help, but they report what happened rather than explaining it.
