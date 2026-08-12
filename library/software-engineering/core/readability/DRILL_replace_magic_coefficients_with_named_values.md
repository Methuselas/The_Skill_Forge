---
object_id: DRILL_replace_magic_coefficients_with_named_values
object_type: drill
name: Replace Magic Coefficients With Named Constants or Functions
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
- refactoring
- magic_numbers
cross_links:
- rel: teaches
  target_object_id: PAT_name_unexplained_values
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u05, pp. 124-128
  evidence_type: text
confidence: high
target_skill: naming hard-coded values so their meaning and change-impact are visible
references: []
variants: []
---

# Replace Magic Coefficients With Named Constants or Functions

## Practice Task
Take a calculation full of unexplained numeric literals and rewrite it so every value's meaning is named, then confirm a related change is now obvious.

## Target Skill
Naming hard-coded values via constants and functions to make meaning and change-impact visible.

## Setup
No special setup required.

## Instructions
1. Start from a calculation with bare coefficients — for example kinetic energy using `907.1847` to convert US tons to kilograms and `0.44704` to convert MPH to meters per second.
2. Identify what each literal means and where the same assumption might be encoded elsewhere.
3. Rewrite once using well-named constants (`KILOGRAMS_PER_US_TON`, `METERS_PER_SECOND_PER_MPH`) placed near the code that uses them.
4. Rewrite again using functions — a provider function returning the coefficient, and a conversion helper (`usTonsToKilograms`) that hides the value entirely — and compare which reads best.
5. Simulate a related change (switch the mass input from tons to kilograms) and check that the named version makes the now-wrong conversion obvious.

## Success Check
- No unexplained numeric literal remains in the calculation.
- Each named value states its meaning at the point of use.
- The simulated unit change makes the obsolete conversion visibly wrong.

## Common Failures
- Naming the constant but placing it far from where it is used, so the change-impact is still hidden.
- Leaving one literal inline because it "seemed obvious," reintroducing the trap.

## Notes
This drills the kinetic-energy example, whose whole point is the broken modification: an unnamed `907.1847` survives a unit change and silently corrupts the result. Naming values — as constants, provider functions, or conversion helpers — costs little and turns an invisible dependency into an obvious one, which is what protects the next engineer who edits nearby code.
