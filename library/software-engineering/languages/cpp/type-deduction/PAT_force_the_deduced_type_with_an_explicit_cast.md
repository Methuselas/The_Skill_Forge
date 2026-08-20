---
object_id: PAT_force_the_deduced_type_with_an_explicit_cast
object_type: pattern
name: Force the Deduced Type With an Explicit Cast
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
- proxy_types
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_auto_for_local_variables
- rel: related_to
  target_object_id: PAT_choose_between_auto_and_decltype_auto
- rel: related_to
  target_object_id: PAT_treat_undefined_behavior_as_a_whole_program_assumption
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Force the Deduced Type With an Explicit Cast

## Pattern Rule
**IF** `auto` deduces a type you did not intend — typically because the initializer yields a proxy object rather than the value it stands for
**THEN** keep `auto` and cast the initializer to the type you want deduced, rather than falling back to naming the type
**ELSE** where the deduced type is the one you wanted, no cast belongs there; this idiom announces a deliberate difference and should not appear where there is none.

## Do
- Recognize the shape of the failure, because it compiles and then misbehaves at run time. Indexing a `std::vector` of `bool` returns that specialization's nested `reference` type, not a `bool`, since the container packs its elements one bit each and C++ has no reference to a bit. Assign that to a named `bool` and the implicit conversion happens immediately and correctly; assign it to `auto` and you have stored the proxy.
- Follow why storing the proxy is undefined rather than merely surprising. Where the container was a temporary — the return value of a function — the proxy holds a pointer into it plus a bit offset. The temporary dies at the end of the statement, and the variable now holds a dangling pointer that will be dereferenced on first use.
- Write the cast on the initializer, not on the variable — a `static_cast` to `bool` wrapped around the whole indexing expression. The proxy is still produced, the conversion it was designed to perform still runs while its referent is alive, and `auto` deduces the converted type.
- Look for proxies in the signature when the documentation does not warn you. Knowing that `operator[]` on a container of `T` normally returns `T&` makes any other return type a signal, and proxies are usually returned from functions clients are expected to call, so they show up in headers even when they are meant to be invisible.
- Expect them beyond the standard library. Numeric libraries using expression templates return objects encoding the whole expression — an addition of four matrices may yield a nest of sum-node types, converting implicitly to the result — and those objects are built to live no longer than the statement.
- Use the same idiom to make a deliberate narrowing visible. Declaring the variable `auto` and applying a `static_cast` to `float` around the call says the precision reduction was intended, in a way that declaring the variable `float` does not, and the same applies to a floating-point expression you mean to store as an integer.

## Don't
- Don't abandon `auto` when it deduces the wrong type. `auto` is not the fault; it deduced exactly what the expression produced. What is needed is a different expression, not a different declaration style.
- Don't hold an invisible proxy in a variable at all. These types are designed on the assumption that they do not outlive the full expression that created them, so declaring a variable of one violates the assumption the library was built on — undefined behaviour is one possible consequence and not the only one.
- Don't rely on a C-style cast or on assigning through an intermediate to get the same effect. The point is that the conversion is visible and the intent is stated; a named cast does that and the alternatives do not.
- Don't scatter the idiom where the types already agree. It reads as a warning that something unusual is happening, and it is only useful while that remains true.

## Checklist
- Does the initializing expression return the type it appears to, or a stand-in for it?
- Is the object the proxy refers to still alive after this statement?
- Is the cast applied to the initializer rather than to the declared variable?
- Where a narrowing conversion is intended, does the code say so?
- Have you checked the header for a return type that is not the conventional one?

## Notes
Proxy classes are not a defect and the library is not misbehaving; they exist to make something work that the language cannot express directly — a reference to a bit, or an arithmetic expression that has not been evaluated yet. What makes them hazardous with `auto` is that some are meant to be seen and some are not. Smart pointers are proxies and advertise it; the `bool` vector's nested reference type and its `std::bitset` counterpart are built to be invisible, and invisibility is exactly what defeats a feature that deduces what is actually there.

The general lesson generalizes past `auto`, which is why the idiom has a second use. Any place where the type of an expression and the type you want to work with differ is a place where the difference should be written down. Before `auto`, the declaration carried that information incidentally; with `auto`, stating it becomes a deliberate act, and the code is clearer for having to make it.

In practice these are most often discovered through a compilation error that makes no sense or a unit test that fails for no visible reason. That is worth knowing so the diagnosis comes faster: when a value obtained through `auto` behaves as though it is not the value you asked for, the first hypothesis is that it is not.
