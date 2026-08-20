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
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants:
- variant_id: pass_by_value_then_move
  variant_name: Take By Value and Move From the Parameter
  variant_basis: constraint
  difference_from_foundation: Where the function's job requires it to keep its own
    copy of the argument, the parameter is taken by value and moved from, instead of
    taken by reference-to-const and copied inside.
  when_to_use: The function or constructor must store or destructively use the argument,
    and the type is cheap to move. One signature then serves both lvalue arguments
    (copied into the parameter, then moved) and rvalue arguments (moved twice), where
    the reference form would need a second overload taking an rvalue reference.
  when_not_to_use: The type is expensive to move or has no move operations, in which
    case the pattern performs two copies instead of one. Also unsuitable where the
    function only reads the argument, which is the foundation's case.
  absorbed_from_object_id: none
---

# Prefer Pass-by-Reference-to-const to Pass-by-Value

## Pattern Rule
**IF** a function parameter is of a user-defined type
**THEN** pass it by reference-to-const, which skips the copy-constructor and destructor calls that pass-by-value incurs and avoids slicing a derived argument down to its base.

## Do
- Declare the parameter as a reference to const, so no new object is constructed and the caller is still protected from modification.
- Pass built-in types, and STL iterators and function objects, by value instead — they are cheap to copy and designed for it.

## Don't
- Don't assume a small user-defined type is cheap by value; a small object can hold a pointer to a lot of data, its copy constructor can be costly, and its size can grow in a later release.
- Don't pass a derived object by value through a base-type parameter — the base copy constructor slices off the derived part and later virtual calls resolve to the base.

## Checklist
- Is this a user-defined-type parameter passed by reference-to-const rather than by value?
- Could passing by value slice a derived argument here?
- Is this one of the exceptions — built-in, iterator, function object — where by-value is right?

## Notes
Passing a `Student` by value fired one Student, one Person, and four string copy constructors (and as many destructors); reference-to-const fires none. It also prevents slicing: a `WindowWithScrollBars` passed by value into a `Window` parameter loses its derived behavior and calls the base display(). The exceptions — built-ins, STL iterators, and function objects — are exactly the sublanguages where by-value is the convention (Item 1).

The rule above answers the case where the function only reads its argument, which is the
common one. Where the function's job is to *keep* a copy — a constructor storing a member,
or a function that consumes its argument destructively — passing by value is not the
inefficiency it looks like, and the variant `pass_by_value_then_move` covers it. The parameter
is taken by value and moved into its destination. An lvalue argument is copied into the
parameter and then moved, which costs the same one copy as taking a reference and copying
inside; an rvalue argument is moved twice and never copied at all. One signature therefore
handles both, where the reference-to-const form needs a second overload taking an rvalue
reference — and with several parameters each needing this, the overload count doubles per
parameter.

Two conditions bound that variant. The type must be cheap to move: for a type with no move
operations, or one whose move is as expensive as its copy, the pattern performs two copies
where the reference form performed one. And the parameter is left in a moved-from state, so
nothing in the function body may use it after the move — a rule the compiler does not enforce.
