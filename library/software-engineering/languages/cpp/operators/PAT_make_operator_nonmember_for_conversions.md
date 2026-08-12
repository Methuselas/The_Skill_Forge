---
object_id: PAT_make_operator_nonmember_for_conversions
object_type: pattern
name: Make a Function Non-member When All Arguments Need Conversion
library_path:
- software-engineering
- languages
- cpp
- operators
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- operators
- type_conversion
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_non_member_non_friend_functions
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u04, pp. 102-105
  evidence_type: text
confidence: high
references: []
variants: []
---

# Make a Function Non-member When All Arguments Need Conversion

## Pattern Rule
**IF** an operator or function must allow implicit type conversion on every argument, including the left operand — as in mixed-mode arithmetic like `2 * oneHalf`
**THEN** make it a non-member function, because the implicit receiver argument of a member function is never eligible for implicit conversion.

## Do
- Implement the operator as a non-member taking all operands as parameters, so the compiler may convert any of them (turning the int 2 into a Rational).
- Keep it a non-member non-friend when the public interface suffices; the opposite of a member is a non-member, not a friend.

## Don't
- Don't leave such an operator a member: `oneHalf * 2` compiles but `2 * oneHalf` does not, because the receiver — the int 2 — cannot be converted to the class type.

## Checklist
- Does this operator need conversions on the left operand as well as the right?
- Is it a non-member so every operand is eligible for conversion?
- Did I avoid making it a friend when the public interface was enough?

## Notes
Only parameters in the parameter list are eligible for implicit conversion; the object a member function is invoked on (the receiver) never is. So a member `Rational::operator*` supports `oneHalf * 2` but not `2 * oneHalf`, breaking commutativity for mixed-mode arithmetic. Making operator* a non-member puts both operands in the parameter list, so the constructor-based int-to-Rational conversion applies to either. And since it needs only the public interface here, it should be a plain non-member, not a friend.
