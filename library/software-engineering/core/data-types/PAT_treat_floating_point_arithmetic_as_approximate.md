---
object_id: PAT_treat_floating_point_arithmetic_as_approximate
object_type: pattern
name: Treat Floating-Point Arithmetic as Approximate
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
- floating_point
- numbers
- rounding
- precision
cross_links:
- rel: related_to
  target_object_id: PAT_bound_an_arithmetic_expression_before_trusting_it
- rel: related_to
  target_object_id: PAT_use_dedicated_types_over_general_ones
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Treat Floating-Point Arithmetic as Approximate

## Pattern Rule
**IF** a value is held in a floating-point type and you are about to compare it, accumulate it, or trust its last digits
**THEN** work with it as an approximation — compare within a tolerance, control the order of operations, and move to an exact representation when the domain demands exactness.
**ELSE** when the quantity must balance to the last unit, stop using floating point for it rather than trying to make floating point behave.

## Do
- Replace equality with a closeness test. Write an `Equals` helper that returns true when the absolute difference is under an accepted delta, and compare through it. Two routes to the same number do not reliably produce the same bits — adding 0.1 ten times rarely reaches 1.0.
- Scale the tolerance to the values when the range is wide. A hard-coded delta is fine only while the magnitudes it judges stay in a narrow band; otherwise compute it from the size of the two numbers being compared.
- Sum from the smallest term upward. Adding numbers of very different sizes loses the small ones entirely — in 32-bit floating point, 1,000,000.00 plus 0.1 comes back as 1,000,000.00, and 5,000,000.02 minus 5,000,000.01 comes back as 0.0. Sorting ascending before summing does not remove the round-off but it minimizes it, and the same applies to summing a series backwards from its smallest term.
- Move money off floating point. Track cents in integers and dollars as multiples of 100 cents, or use a decimal or currency type where the language provides one. Wrap the representation in a class so callers work in dollars and cents while the integer arithmetic stays hidden.
- Reach for more precision only as a first resort, not the fix. Going from single to double precision buys digits and postpones the problem; it does not make the arithmetic exact.

## Don't
- Don't compare two floating-point values with `==` because they were computed from the same inputs. The failure is not in the values but in the paths — a loop accumulating 0.1 passes through 0.30000000000000004 and 0.7999999999999999 on its way to 0.9999999999999999, and every intermediate is slightly wrong in a way the printed result may not show.
- Don't assume seven or fifteen digits of accuracy is the same as exact. A 32-bit representation of one third comes out as 0.33333330, which is accurate enough for most purposes and inaccurate enough to trip you occasionally — and the occasional case is the one that ships.
- Don't leave the accumulated error uncontrolled just because each individual operation looks harmless. Ordering is the cheapest lever available and costs nothing at runtime.

## Checklist
- Does any comparison of these values use exact equality?
- If a tolerance is used, does it still make sense at the largest and smallest magnitudes this code sees?
- Are values of very different sizes being added, and if so in what order?
- Is this quantity one that has to balance exactly, and if so why is it in a floating-point type?
- Would a reader know from the type that this value is approximate?

## Notes
The root cause is worth holding in one sentence, because every guideline here follows from it: many fractional decimal numbers have no exact representation in the ones and zeros a digital computer has to work with. Nonterminating values like one third or one seventh get approximately seven or fifteen digits, and the error is small, real, and cumulative. Nothing in the language warns you, because nothing has gone wrong by the language's standards.

The trap that catches people who already know all this is the printed result. A loop that lands on 0.9999999999999999 will often display as 1, so the value looks right in a debugger and in a log and fails only in a comparison. That is why the repair is a habit about comparisons rather than a habit about checking values — the check that would catch it is the one that is failing.

The money case deserves the separate treatment it gets here. Dollars-and-cents in floating point is a normal-looking choice that is wrong for a reason that has nothing to do with precision in the abstract: the quantity has to balance, and approximate arithmetic cannot be made to balance by adding digits. Switching to integer cents is a roll-your-own version of what a decimal type does for you, and it is effective on both speed and accuracy — the cost is remembering that the fractional part is now yours to manage, which is exactly what a small wrapper class exists to absorb.
