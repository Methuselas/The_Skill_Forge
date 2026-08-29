---
object_id: PAT_write_boolean_expressions_to_be_read_not_decoded
object_type: pattern
name: Write Boolean Expressions to Be Read, Not Decoded
library_path:
- software-engineering
- core
- control-flow
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- boolean_expressions
- control_flow
- readability
- evaluation_order
cross_links:
- rel: related_to
  target_object_id: PAT_name_a_boolean_for_the_condition_it_asserts
- rel: related_to
  target_object_id: PAT_count_a_routines_decision_points
- rel: related_to
  target_object_id: PAT_bound_an_arithmetic_expression_before_trusting_it
- rel: related_to
  target_object_id: AP_shape_a_multi_way_decision
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Write Boolean Expressions to Be Read, Not Decoded

## Pattern Rule
**IF** you are writing a condition with more than one term, a negation, or a range test
**THEN** shape it so a reader can take it at face value without applying the language's precedence rules, mentally removing negations, or working out which end of a range is which.
**ELSE** where the condition resists every one of these and still reads badly, that is the signal to name its parts or move it into a function rather than to keep rearranging it.

## Do
- State the condition positively and let the branches follow. A test on a not-status with the real work in its alternative branch inverts more easily than it reads — flip the test and swap the two branches. Where flipping is awkward, changing the variable to one whose name means the opposite achieves the same thing, so a status-is-fine flag becomes an error-was-detected flag.
- Reach for De Morgan's transformation when a negation cannot be flipped away. A test on not-this or not-that is the same as a negation of this-and-that, and the mechanical rule is to negate each operand, swap the `and` with the `or`, and negate the whole. That converts a scattered pair of negations into one, which is the form people parse correctly.
- Put range tests in number-line order. Write the lower bound, then the value, then the upper bound, so that a test for being inside a range reads with the bounds at the ends and the value in the middle, and a test for being outside it puts the value at both ends. That maps directly onto a picture of the range; the same test written with both comparisons pointing the same way gives the reader nothing to visualize.
- Parenthesize fully rather than relying on precedence. Extra parentheses cost nothing, and they remove a demand on a reader who may be moving between languages with different rules. When a chain of comparisons could group more than one way, the parentheses are also what tell the compiler which one you meant.
- Compare implicitly only when the value really is a truth value. A test on a not-done flag is a boolean test and reads best bare. A number, a character, or a pointer is not, and comparing each explicitly against zero, the null terminator, or null says which of zero's several meanings this code is using.

## Don't
- Don't stack negations. A reader untangling a not-short string of non-positives is doing work that rearranging the expression would have removed, and the error rate on that work is high.
- Don't let correctness rest on evaluation order without knowing your language's rule. A guard testing that a denominator is non-zero before dividing by it is safe only where evaluation stops at the first false term and only in that order — reverse the two terms and the same expression divides by zero. Languages differ, and some offer both a short-circuiting and a fully-evaluating operator that look nearly identical, so the guard silently stops guarding if the wrong one is used. Where the ordering is load-bearing, nested tests state the dependency instead of assuming it.
- Don't evaluate a term that will be invalid when the guard fails. A loop condition that checks an index against a limit and then indexes with it will read past the end on the final pass in any language that evaluates both terms, and it is sloppy even where it happens to be safe.
- Don't accept an unbalanced expression on inspection. Walking the line left to right, counting up at each opening parenthesis and down at each closing one, should reach zero exactly once — at the very end. Hitting zero early means a parenthesis is missing before that point.

## Checklist
- Is every negation necessary, or would flipping the test and its branches remove one?
- Do range tests read in number-line order?
- Is the expression fully parenthesized, and does the count return to zero only at the end?
- Are truth values compared implicitly and everything else compared explicitly?
- If evaluation stopped partway, or did not, would this expression still be correct?

## Notes
These are five separate guidelines with one thing in common — each removes a step the reader would otherwise have to perform before knowing what the condition means. Precedence rules, double negations, and range comparisons pointing the same direction are all decodable, and that is the problem: they are work, they are done under time pressure, and they are done wrong at a rate that a few extra characters would have avoided.

One conflict is worth knowing about because the source raises it rather than hiding it. Stating conditions positively sometimes collides with putting the case you normally expect in the main branch, and there is no rule that resolves it — you weigh which reading matters more here and decide. That is an honest gap rather than an oversight, and it is worth recognizing when you hit it, because the temptation is to assume you have misunderstood one of the two guidelines.

The number-line ordering is the smallest of these and the one most worth adopting as a habit, because it costs nothing at the moment of writing and pays at every later reading. A test with its bounds at the ends and its value in the middle can be checked against a mental picture in about a second. The same test with both comparisons written in the same direction has to be evaluated term by term, and the reader who does that quickly is the one who mistakes an inside test for an outside one.
