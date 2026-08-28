---
object_id: PAT_prefer_pass_by_reference_to_const
object_type: pattern
name: Prefer Pass-by-Reference-to-const to Pass-by-Value
library_path:
- software-engineering
- languages
- cpp
- parameter-passing
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- parameter_passing
- efficiency
- slicing
cross_links:
- rel: related_to
  target_object_id: PAT_adapt_rules_to_active_cpp_sublanguage
- rel: related_to
  target_object_id: PAT_return_by_value_when_returning_new_object
- rel: related_to
  target_object_id: PAT_pass_by_value_only_when_all_four_conditions_hold
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Prefer Pass-by-Reference-to-const to Pass-by-Value

## Pattern Rule
**IF** you are deciding how a function that only reads its argument should take a parameter
**THEN** pass a user-defined type by reference-to-const, which skips the copy-constructor and destructor calls that pass-by-value incurs and avoids slicing a derived argument down to its base — and pass a built-in, an STL iterator, or a function object by value, because those are cheap to copy and designed for it
**ELSE** where the function's job is to keep a copy of what it is given, passing by value can be right for reasons this rule does not cover; `PAT_pass_by_value_only_when_all_four_conditions_hold` owns that decision.

## Do
- Declare the parameter as a reference to const, so no new object is constructed and the caller is still protected from modification.
- Pass built-in types, and STL iterators and function objects, by value instead — they are cheap to copy and designed for it.

## Don't
- Don't assume a small user-defined type is cheap by value; a small object can hold a pointer to a lot of data, its copy constructor can be costly, and its size can grow in a later release.
- Don't pass a derived object by value through a base-type parameter — the base copy constructor slices off the derived part and later virtual calls resolve to the base.
- Don't take a built-in by reference-to-const on the reasoning that a reference is always the cheaper way to pass something. A reference is the size of a pointer or larger, so nothing is saved on a type that fits in a register; the callee must load through it at each use rather than keeping the value in one; and because the reference is to const it binds to a temporary whenever the argument's type does not match exactly, so an index arriving as a different integer type materialises one on every call. This is the mirror image of the mistake the rule above prevents, and it is easy to reach by applying that rule past the types it was written for.

## Checklist
- Is this a user-defined-type parameter passed by reference-to-const rather than by value?
- Is this a built-in taken by reference-to-const, which is the rule applied past the types it covers?
- Could passing by value slice a derived argument here?
- Is this one of the exceptions — built-in, iterator, function object — where by-value is right?

## Notes
Passing a `Student` by value fired one Student, one Person, and four string copy constructors (and as many destructors); reference-to-const fires none. It also prevents slicing: a `WindowWithScrollBars` passed by value into a `Window` parameter loses its derived behavior and calls the base display(). The exceptions — built-ins, STL iterators, and function objects — are exactly the sublanguages where by-value is the convention (Item 1).

The rule above answers the case where the function only reads its argument, which is the
common one. Where the function's job is to *keep* a copy — a constructor storing a member, or
a function that consumes its argument destructively — passing by value stops being the
inefficiency it looks like, because one signature then serves lvalues and rvalues without a
second overload taking an rvalue reference. That is a decision with four qualifying conditions
and two ways to go wrong, and it has its own card rather than living here as a footnote.

One consequence of the const on that reference is worth knowing, because it is where a
surprising share of unnoticed temporaries come from. When the argument's type does not match
the parameter's, a const reference parameter will happily bind to a temporary conjured up to
make the call work, so passing a character array where a string is expected constructs and
destroys a string on every call. A reference to non-const will not do this — the language forbids
it, because modifying such a temporary would change something the caller never sees — which
means the same mismatch that compiles silently in the const case is a diagnostic in the other.
The two places temporaries arise are exactly this and returning an object by value; learning to
notice both is more useful than any individual fix for them.
