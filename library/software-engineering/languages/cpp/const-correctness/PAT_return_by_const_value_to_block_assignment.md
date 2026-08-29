---
object_id: PAT_return_by_const_value_to_block_assignment
object_type: pattern
name: Return by const Value to Block Accidental Assignment
library_path:
- software-engineering
- languages
- cpp
- const-correctness
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- const
- operator_overloading
- interface_design
cross_links:
- rel: related_to
  target_object_id: PAT_apply_const_to_lock_invariants
- rel: related_to
  target_object_id: AP_make_a_class_const_correct
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Return by const Value to Block Accidental Assignment

## Pattern Rule
**IF** you are declaring an operator or function that returns a user-defined value clients have no business assigning into
**THEN** return it by `const` value, so that `(a * b) = c` and the typo `if (a * b = c)` fail to compile.

## Do
- Declare `const Rational operator*(const Rational& lhs, const Rational& rhs);` so the product of two numbers cannot be assigned to.
- Use the const return to give your type the same protection a built-in already has, where assigning to the result of an arithmetic expression is flatly illegal.

## Don't
- Don't return a non-const value from such an operator; one `=`-for-`==` slip then silently compiles into an assignment onto a temporary and a bug that reads like a comparison.

## Checklist
- Could a caller accidentally assign into this return value?
- Would that same mistake be illegal for a built-in type — and does my type now behave consistently with the built-ins?

## Notes
A hallmark of good user-defined types is that they avoid gratuitous incompatibilities with the built-ins. Letting clients assign to `a * b` is exactly such an incompatibility, and it is usually reached by accident — a stray `=` inside an `if`. A `const` return value closes the door for the small cost of the keyword, which is why it is the right default for value-returning operators.
