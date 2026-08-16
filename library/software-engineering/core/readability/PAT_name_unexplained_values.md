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
variants: []
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
