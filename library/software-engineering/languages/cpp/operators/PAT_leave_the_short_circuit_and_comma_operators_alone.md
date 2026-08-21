---
object_id: PAT_leave_the_short_circuit_and_comma_operators_alone
object_type: pattern
name: Leave the Short-Circuit and Comma Operators Alone
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
- avoiding_surprises
- evaluation_order
cross_links:
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Leave the Short-Circuit and Comma Operators Alone

## Pattern Rule
**IF** you are considering overloading logical and, logical or, or the comma operator for one of your types
**THEN** don't, because overloading turns the construct into a function call, and a call evaluates all of its arguments — which is exactly the guarantee the built-in spellings exist to provide
**ELSE** where you want the reading these spellings suggest, give the operation an ordinary name, so that nobody reads into it a promise it cannot keep.

## Do
- Trace what the expression turns into once overloaded, since the substitution is invisible at the call site. What reads as two operands joined by a symbol becomes a call taking both of them, as a member function with one argument or a free function with two.
- Take seriously how much working code depends on the built-in behavior. Testing a pointer against null and dereferencing it in the same condition is correct only because the second operand goes unevaluated when the first fails, and that shape appears everywhere.
- Reserve the comma operator for reading rather than writing. Programmers meet it in the update clause of a loop advancing two variables at once, where only an expression is legal and two statements are not, and that is close to the whole of its defensible use.

## Don't
- Don't conclude the objection lapsed when the ordering rules tightened. It is true that the operands of these overloaded operators are now sequenced the way the built-in versions sequence them, so the evaluation-order half of the classic argument no longer holds — but the decisive half is untouched: a call evaluates both operands whatever the order, so the skipping is gone.
- Don't treat the ability to overload an operator as a reason for doing it. The point of operator overloading is that programs read more clearly, and no caller can read these three correctly once the semantics have changed quietly underneath a familiar spelling.

## Checklist
- Does any class here overload logical and, logical or, or comma?
- If so, is there code anywhere that depends on the right operand being skipped?
- Would a named function express the same operation without implying a guarantee it cannot honor?

## Notes
What separates these three from the other overloadable operators is that their built-in meanings are not only about results — they are about which subexpressions run at all. An overload can reproduce a result; it cannot reproduce a decision not to evaluate something, because by the time the function body begins, both operands have already been evaluated.

The set of operators that cannot be overloaded at all — member selection, scope resolution, the conditional operator, sizeof, typeid, and the named casts — is worth knowing next to this, because it marks where the language judged the same hazard severe enough to settle centrally instead of leaving to taste. These three sit just on the permitted side of that line.

Meyers rested the original case on two grounds: unspecified operand order and lost short-circuiting. The language has since fixed the first. Keeping the conclusion while discarding the obsolete half of its support is the point — the rule survives, but citing evaluation order as the reason for it is now simply wrong.
