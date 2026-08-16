---
object_id: PAT_name_unexplained_values
object_type: pattern
name: Give Unexplained Values a Name
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- constants
- readability
- magic_numbers
- single_source_of_truth
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_readable
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_draw_the_line_at_zero_and_one
  variant_name: Draw the Line at Zero and One Rather Than at Obviousness
  variant_basis: method_sequence
  difference_from_foundation: The foundation names a value when its meaning is not obvious, which leaves the author judging their own code's obviousness. This variant removes the judgment and replaces it with a bright line — the only literals that belong in the body of a program are 0 and 1, used for incrementing, decrementing, and starting at the first element; every other literal gets a name. It goes further and treats safe-looking literals as the priority target, on the grounds that the author is the worst-placed person to rule on obviousness. A loop running 1 to 12 over monthly profit is probably iterating months, and probably is the problem — the repair ladder runs from the literal, to a named constant, to a named loop index, to an enumerated type whose members are the months themselves, and only the last leaves no doubt. It adds an active search rather than waiting for review, sweeping the source for the digits 2 through 9. And it adds a consistency requirement the foundation does not state — a value represented by a named constant in one place and a literal in another is worse than either alone, because changing the constant looks complete and silently is not.
  when_to_use: Use where the cost of a missed literal is high or the code will outlive its author's memory — the bright line takes the argument about obviousness off the table, and the sweep finds literals that no reviewer would think to question. It is also the right stance when the value is one everyone knows, since a well-known value is exactly the one nobody double-checks.
  when_not_to_use: Do not apply the sweep mechanically to code where digits carry no domain meaning — array indices, bit positions, and the arithmetic inside a small well-named helper are cases where the literal is already local and named by its surroundings. The foundation's judgment is the better tool when naming would add a layer without adding information.
  absorbed_from_object_id: none
---

# Give Unexplained Values a Name

## Pattern Rule
**IF** the code contains a hard-coded value — a conversion coefficient, a tunable parameter, a template — whose meaning is not obvious
**THEN** give it a name, by placing it in a well-named constant or returning it from a well-named function, so a reader learns both what the value is and what it means.

## Do
- Name the constant for its meaning: replace the bare `907.1847` and `0.44704` in a kinetic-energy calculation with `KILOGRAMS_PER_US_TON` and `METERS_PER_SECOND_PER_MPH`.
- Or name it through a function — a provider function returning the coefficient, or better a helper that performs the conversion (`usTonsToKilograms(mass)`) so callers never see the value at all.
- If other code might reuse the value or conversion, put it in a shared public utility rather than hiding it in one class.

## Don't
- Don't inline an unexplained literal; an engineer swapping `getMassUsTon()` for `getMassKg()` will not know the stray `907.1847` must also go, and silently returns wrong energy.
- Don't assume the reader shares your domain knowledge — the kinetic-energy coefficients are meaningless to anyone who does not already know the formula.

## Checklist
- Does every hard-coded value convey its meaning through a name?
- Would someone modifying nearby code see that a related constant must change too?
- Could this value or conversion be reused, and if so is it placed where others can find it?

## Notes
The kinetic-energy example shows the failure mode precisely: because `907.1847` is an unnamed tons-to-kilograms factor, an engineer switching the mass unit leaves it in and breaks the calculation without realizing. Naming the value — as a constant, a provider function, or a conversion helper — costs almost nothing and makes both the value's identity and the consequences of changing surrounding code visible. This is a readability concern about legitimate constants, distinct from using an in-band magic value to signal an error.

`VAR_draw_the_line_at_zero_and_one` disagrees with the foundation about who decides. Long names a value when its meaning is not obvious; McConnell answers that the author is the worst-placed person to rule on obviousness and draws a line instead — only 0 and 1 belong in the body of a program, and everything else gets a name whether or not it seems to need one. His demonstration is a loop from 1 to 12 over monthly figures, which is *probably* iterating months, and the word probably is the argument. He escalates it through a named constant, then a named loop index, then an enumerated type running January to December, and only the last removes the doubt entirely. Two additions travel with the stance and are worth taking even if the bright line is not: sweep the source for the digits 2 through 9 rather than waiting for a reviewer to notice, and never let one value appear as a named constant in one place and a literal in another — that mixture is worse than consistent literals, because changing the constant then looks like a complete edit and is not.

