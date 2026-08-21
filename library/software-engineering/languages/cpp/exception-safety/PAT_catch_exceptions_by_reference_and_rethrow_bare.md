---
object_id: PAT_catch_exceptions_by_reference_and_rethrow_bare
object_type: pattern
name: Catch Exceptions by Reference and Rethrow With a Bare Throw
library_path:
- software-engineering
- languages
- cpp
- exception-safety
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- exception_safety
- error_handling
- slicing
- polymorphism
cross_links:
- rel: related_to
  target_object_id: PAT_offer_an_exception_safety_guarantee
- rel: related_to
  target_object_id: PAT_never_let_exceptions_leave_a_destructor
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Catch Exceptions by Reference and Rethrow With a Bare Throw

## Pattern Rule
**IF** you are writing a handler and must decide how the exception object arrives, and whether to let it continue outward
**THEN** take it by reference — by reference to const where the handler does not modify it — and when passing the same exception onward, use the operand-less form rather than naming the caught object
**ELSE** where you are deliberately substituting a different exception for the one you caught, throwing a named object is the point, and the type change is intended rather than accidental.

## Do
- Order the handlers most-derived first. Matching is first-fit in source order, unlike virtual dispatch, which is best-fit — so a base-class handler written above a derived-class handler for the same try block silently makes the second one unreachable.
- Expect fewer conversions than a function call would apply. Only two kinds are considered: from derived to accessible base, and from any pointer type to a pointer to void. Nothing else — an integer thrown will sail straight past a handler taking a floating-point value, which is a match a function call would have made.
- Reach for reference to const by default and plain reference only when the handler genuinely alters the object. Either works; the language permits a thrown object to bind to a non-const reference even though it is a temporary, which an ordinary function parameter would not.

## Don't
- Don't catch by pointer. The handler is then obliged to decide whether to release what it received, and the answer depends on whether the thrower allocated it — static storage means releasing is undefined, heap storage means not releasing leaks, and no handler can tell which it got. The standard's own exception types are objects rather than pointers anyway, so this style cannot even cover them.
- Don't catch by value. A derived exception caught as its base has the derived part sliced away, so the object in the handler is a base object: its added members are gone and calls to its virtual functions resolve to the base versions, which is almost never the diagnostic you wanted. It also costs a second copy on top of the one throwing always makes.
- Don't propagate by naming the caught object. That throws a fresh exception of the caught object's static type, so a derived exception caught through a base reference is quietly demoted to the base on its way out; the operand-less form passes along what was actually thrown, and costs no copy.

## Checklist
- Does any handler here take a pointer, and if so, who is supposed to release it?
- Does any handler take a value, and could the thrown object be of a derived type?
- Within one try block, does any base-class handler precede a handler for a class derived from it?
- Does every rethrow of the caught exception use the operand-less form?

## Notes
The behavior that makes catch-by-value wrong is the same one that makes exceptions safe: a thrown object is always copied, and the copy is made using the copy constructor of its *static* type. That is why throwing through a base-class reference to a derived object throws a base object — the compiler consults the declared type, not what the reference actually refers to.

That copy also fixes the accounting. Catching by reference still costs one copy, because throwing made it; catching by value costs two, because the handler copies the temporary again. There is no arrangement that costs none, which is part of why exceptions are expensive relative to returning.

The distinction between the two rethrow spellings is easy to lose because both are correct code and neither warns. The difference only appears when the caught type is a base of what was thrown, and its symptom is a handler further out receiving a less specific exception than the one that actually occurred.
