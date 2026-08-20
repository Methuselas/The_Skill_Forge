---
object_id: PAT_prefer_auto_for_local_variables
object_type: pattern
name: Prefer auto for Local Variables
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
- initialization
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_postpone_variable_definitions
- rel: related_to
  target_object_id: PAT_declare_and_initialize_at_first_use
- rel: related_to
  target_object_id: PAT_force_the_deduced_type_with_an_explicit_cast
- rel: related_to
  target_object_id: PAT_choose_between_auto_and_decltype_auto
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Prefer auto for Local Variables

## Pattern Rule
**IF** you are declaring a local variable whose type is determined by its initializer
**THEN** declare it `auto` rather than naming the type, so the variable cannot be left uninitialized and cannot silently differ from the expression that initializes it
**ELSE** where writing the type genuinely makes the code clearer to a reader, or where you want a type *different* from the initializer's, name it — `auto` is an option and not a mandate.

## Do
- Take the forced initialization as the first benefit, because it removes a category of bug rather than a symptom. A variable declared `auto` with no initializer does not compile, so the rule about initializing at the point of declaration stops being a discipline and becomes structural.
- Use it wherever the type is unpleasant to write but obvious in meaning. The type of the value an iterator points at has to be spelled as a nested `value_type` reached through an iterator-traits template; `auto` says the same thing and is right by construction.
- Use it for anything whose type cannot be written at all. A lambda's closure type is known only to the compiler, and the alternative — storing the closure in a `std::function` — is a different thing with real costs: fixed size regardless of the closure, a possible heap allocation when the closure does not fit, restricted inlining, and an indirect call.
- Let it close the gap between the type you assumed and the type that is actually there. Writing `unsigned sz = v.size()` compiles everywhere and is correct only where `size_type` happens to be 32 bits — it is a portability bug that appears when the code moves to a 64-bit target. `auto sz = v.size()` cannot be wrong.
- Watch for the same mismatch silently copying in a range-based loop. Iterating a map with a reference-to-const pair of string and int binds to a temporary, because the element type has a *const* key — so every iteration constructs and destroys a copy, and taking the address of the loop variable yields a pointer to the temporary rather than into the container. `const auto&` binds to the element.
- Count the refactoring benefit as real. Change a function's return type from `int` to `long` and every `auto` call site follows on the next compile; every explicitly typed call site has to be found.

## Don't
- Don't initialize an `auto` variable with braces unless you want a `std::initializer_list`. This is the single point where `auto` deduction differs from template deduction: `auto x{27}` and `auto x = {27}` both declare a `std::initializer_list` of int, not an `int`. It is the standard accident of the uniform-initialization habit, and it is why some developers brace only where they must.
- Don't expect that rule inside a deduced return type or a lambda parameter. Those use *template* deduction, where a braced initializer deduces nothing at all — so a function returning `{ 1, 2, 3 }` does not compile.
- Don't assume the deduced type is the one the expression appears to produce. Where the initializer yields an invisible proxy, `auto` deduces the proxy, which is a separate decision with its own remedy.
- Don't read the loss of a visible type name as a loss of information. Knowing that something is a container, a counter, or a smart pointer is usually enough, and with a well-chosen variable name it is already on the page.

## Checklist
- Could this variable be left uninitialized as written?
- Is the declared type exactly what the initializer produces, including const and reference qualification?
- In a range-based loop over an associative container, does the loop variable's type match the element type?
- Would a change to the initializer's type require editing this declaration?
- Is the initializer braced, and did you want a `std::initializer_list`?

## Notes
The two failure modes this prevents are worth separating because they fail differently. An uninitialized variable is a defect that may or may not manifest. A type mismatch between a declaration and its initializer is silent and legal — the compiler inserts a conversion, and the result is a portability difference, an unwanted copy, or a reference bound to a temporary. `auto` removes the second class entirely, because there is nothing for the initializer to be converted *to*.

The readability objection deserves a straight answer rather than a dismissal. Losing the ability to read a type off the declaration is a real cost, and it is smaller than it feels: type inference is long established in statically typed languages, large codebases are built in them, and the abstract fact that something is a smart pointer is usually what a reader needs. Where the exact type genuinely carries the meaning, write it.

There is a subtlety in what `auto` deduces that this card takes for granted and the deduction rules make precise: a plain `auto` copies, dropping reference and top-level const from the initializer. That is usually what a local variable should do, and where it is not — where the point is to alias the initializer exactly — the deduction has to be told so explicitly.
