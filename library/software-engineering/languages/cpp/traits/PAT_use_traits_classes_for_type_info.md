---
object_id: PAT_use_traits_classes_for_type_info
object_type: pattern
name: Use Traits Classes for Compile-Time Type Information
library_path:
- software-engineering
- languages
- cpp
- traits
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- traits
- templates
- compile_time
cross_links:
- rel: related_to
  target_object_id: PAT_use_template_metaprogramming
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants:
- variant_id: VAR_branch_inside_one_function_with_if_constexpr
  variant_name: Branch Inside One Function With a Compile-Time If
  variant_basis: method_sequence
  difference_from_foundation: The foundation obtains its compile-time if/else by splitting the work across overloaded workers and letting overload resolution choose between them, with a trait supplying the tag that selects one. This variant keeps the work in a single function and writes the if/else literally, with the condition being a compile-time boolean rather than a tag. The mechanism that makes it safe is that the branch not taken is not instantiated, so a branch may contain an expression that would be ill-formed for the types that do not reach it — dereferencing the parameter in the branch selected only for pointers is the standard case. That is the same property the overload set was buying, obtained without the indirection — no tag type, no worker overloads, and no master function whose only job is to pass the trait along. The trade is that the whole decision now sits inside one body, which reads well for a two-way branch on one property and poorly once the conditions multiply or the branches diverge in length.
  when_to_use: Use where the variation is a small number of alternatives selected by a property expressible as a compile-time boolean, and where the alternative bodies are short enough to read together. It is the better choice when the overload set would exist only to carry the dispatch and each worker would be called from exactly one place, since that indirection is pure ceremony. It also keeps a function's logic legible in one place for a reader who would otherwise have to assemble it from several overloads and a tag hierarchy.
  when_not_to_use: Do not use it where the trait must compute a type rather than answer a question — selecting how a parameter is taken or naming a container's element type is not a branch and has no if/else form. Prefer the foundation where the alternatives are numerous, where they are long enough that one function stops being readable, or where the workers are genuinely reusable and called from more than one master. It is also unavailable where the variation must be extensible by other authors, since an overload set can be added to from outside while a chain of compile-time branches inside one function cannot.
  absorbed_from_object_id: none
---

# Use Traits Classes for Compile-Time Type Information

## Pattern Rule
**IF** you need behavior that depends on properties of a type, and it must work for built-in types too
**THEN** put the information in a traits class — a template with specializations, including one for pointers — and dispatch on it with overloaded worker functions, giving a compile-time if/else on types.

## Do
- Define a traits template exposing the information (an iterator's category), supplied by a nested typedef for user-defined types and by a pointer specialization for built-ins.
- Dispatch by writing overloaded worker functions that each take a different traits tag, plus a master function that passes the trait so overload resolution picks the right worker during compilation.
- Use a trait to compute a *type* as well as to answer a question. Selecting how a parameter should be taken, stripping a qualifier, or picking a container's element type are all decisions generic code cannot make by hand, because the category of the type is exactly what it does not know.

## Don't
- Don't branch on the type at runtime with a typeid if/else; it wastes runtime, bloats the executable, and can force code that is invalid for some types to be compiled.
- Don't nest the information only inside the type; that fails for built-ins like pointers, so keep the traits external to the type.

## Checklist
- Is the type information exposed by a traits template with a specialization for pointers?
- Is dispatch done by overloaded workers selected by a traits tag rather than a runtime typeid test?
- Does the design work for built-in types as well as user-defined ones?
- Where the trait yields a type rather than a flag, does that type stay legal for every argument the template accepts, including one that is already a reference or already qualified?

## Notes
advance wants iterator arithmetic for random-access iterators and stepping otherwise — a decision about a type. Traits make that decision at compile time: iterator_traits exposes an iterator_category (via a nested typedef, and a pointer specialization for built-ins), and overloaded doAdvance workers tagged by category let overload resolution choose. The tag structs inherit (forward is-a input), so a worker written for the base tag also serves the derived category. This is the compile-time if/else that runtime typeid cannot match.

`VAR_branch_inside_one_function_with_if_constexpr` reaches the same compile-time if/else by writing it as an if/else. Where the foundation splits the work into tagged workers and lets overload resolution pick one, the variant keeps a single function and branches on a compile-time boolean, relying on the fact that the untaken branch is never instantiated — which is what permits a branch to dereference a parameter when it is only selected for pointers. Note what that does to this card's second Don't: the objection to a runtime `typeid` if/else was partly that it forces code invalid for some types to be compiled, and the compile-time branch supplies the readable if/else shape without reintroducing that problem. Use it for a small number of short alternatives selected by one property, where an overload set would exist purely to carry the dispatch. Keep the foundation where the trait computes a type rather than answering a question, where the alternatives are many or long, or where other authors must be able to extend the set — an overload set is open to additions from outside and a chain of branches inside one function is not.

The same mechanism computes types, and that use is easy to miss because it does not look like a decision. Generic code cannot write `const T&` for every parameter and be right — a scalar is cheaper taken by value, and a type that is already a reference cannot take another one — so the parameter form is derived from the type's category rather than chosen. Traits that strip a qualifier, or select between two candidate types on a compile-time condition, are the same move: the answer is a type, and the code asking for it does not know enough to write that type down.
