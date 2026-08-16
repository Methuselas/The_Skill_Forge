---
object_id: PAT_bound_an_arithmetic_expression_before_trusting_it
object_type: pattern
name: Bound an Arithmetic Expression Before You Trust It
library_path:
- software-engineering
- core
- data-types
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- integers
- overflow
- numbers
- type_conversion
cross_links:
- rel: related_to
  target_object_id: PAT_treat_floating_point_arithmetic_as_approximate
- rel: related_to
  target_object_id: PAT_treat_compiler_warnings_as_potential_bugs
- rel: related_to
  target_object_id: PAT_understand_the_routine_before_the_compiler_sees_it
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Bound an Arithmetic Expression Before You Trust It

## Pattern Rule
**IF** you are writing an expression that divides, multiplies, accumulates, or mixes numeric types
**THEN** work out the largest and smallest value each term can take — including the values that only exist part-way through — and confirm the chosen types hold all of them.
**ELSE** when a term's range genuinely cannot be bounded, add a runtime check at that point rather than assuming the type is wide enough.

## Do
- Estimate each term's maximum before choosing the type. If one factor tops out at 200 and the other at 25, the product reaches 5,000 and a 32-bit integer is ample; at 200,000 and 100,000 the product reaches 20,000,000,000 and it is not, so the type has to change before the code is written rather than after it misbehaves.
- Bound the intermediates separately, because they are where this actually bites. A product-then-divide such as one million times one million divided by one million needs to hold a million million part-way through, and in 32-bit integers it does not — the expression returns −727 rather than 1,000,000, and every value in it looks reasonable.
- Watch for truncation the moment integers meet division. Seven divided by ten is zero in integer arithmetic, and that zero propagates: ten times the quantity seven-over-ten is zero, where multiplying first and dividing last gives seven. Reordering so divisions happen last is usually the whole fix.
- Ask at every division symbol whether the denominator can reach zero, and write the guard where it can.
- Make every type conversion explicit at the point it happens, so a reader can see it and so the conversion performed is the one you chose. Different compilers convert differently, and an implicit conversion is a decision made by whoever built the toolchain.
- Convert deliberately rather than comparing across types. A comparison between a floating-point value and an integer makes the compiler pick a type, convert one side, and round before it answers, and the result is close to unpredictable.

## Don't
- Don't check only the value the expression produces. A final result well inside the type's range says nothing about what happened in the middle, and the middle is not visible in the answer.
- Don't reason about today's inputs alone. A quantity that will never exceed five thousand is fine; one expected to grow steadily for several years has to be sized for where it is going, not where it starts.
- Don't assume integer division rounds the way you expect. What it does with the remainder varies between languages — toward zero, toward negative infinity, to the nearest integer — so an expression relying on the behaviour is relying on the language rather than on arithmetic.
- Don't let a warning about mixed numeric types pass. It is the toolchain reporting this exact class of defect before it runs, and every programmer has eventually spent an afternoon on a bug the compiler had been describing all along.

## Checklist
- What is the largest value each term in this expression can take?
- What is the largest value reached at any point during evaluation, not just at the end?
- Is any division here integer division, and is that what you meant?
- Can any denominator be zero?
- Are all the operands the same type, and if not, where exactly does the conversion happen and who chose it?

## Notes
What makes this class of defect distinctive is that nothing reports it. An overflow does not raise, a truncating division does not warn, and an implicit conversion is by definition the compiler doing what it was designed to do. The wrong answer arrives in the same shape as the right one, and it is often plausible — that is why the discipline has to run before execution rather than after, and why it belongs with reading code rather than with testing it.

The intermediate-result case is the one worth memorising, because it defeats the obvious defence. Someone who has been bitten by overflow checks the result against the type's range, finds it comfortable, and moves on. The expression still fails, because the evaluation passed through a value the type could not hold and the damage was done before the final division brought the magnitude back down. The general form is that a type has to accommodate the whole evaluation, not the answer.

None of this argues for defensive arithmetic everywhere. The ranges of the common integer types are small in number and easy to keep at hand, most expressions are obviously safe once the terms are bounded, and the check takes seconds. The cost is only paid where it is needed, which is what makes it worth doing every time rather than after something has already gone wrong.
