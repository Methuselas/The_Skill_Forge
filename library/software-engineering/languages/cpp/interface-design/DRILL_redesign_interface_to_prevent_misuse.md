---
object_id: DRILL_redesign_interface_to_prevent_misuse
object_type: drill
name: Redesign an Error-Prone Interface So Misuse Won't Compile
target_skill: Using types, value constraints, and ownership to make an interface hard to misuse
library_path:
- software-engineering
- languages
- cpp
- interface-design
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- interface_design
- type_safety
- hard_to_misuse
cross_links:
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u04, pp. 78-83
  evidence_type: text
confidence: high
references: []
variants: []
---

# Redesign an Error-Prone Interface So Misuse Won't Compile

## Practice Task
Given a `Date(int month, int day, int year)` constructor, redesign it so wrong-order and out-of-range arguments cannot compile.

## Target Skill
Preventing client mistakes with distinct types, constrained values, and removed bookkeeping.

## Setup
No special setup required.

## Instructions
- List the client mistakes the current signature allows: swapped month/day, and out-of-range values.
- Introduce distinct Day, Month, and Year types so the compiler rejects wrong-kind or wrong-order arguments.
- Constrain Month to its valid values, using predefined Month objects rather than a raw int or an enum.
- Consider whether an associated factory should return a smart pointer to remove a release obligation.

## Success Check
- `Date(30, 3, 1995)` no longer compiles, while `Date(Month(3), Day(30), Year(1995))` does.
- An invalid month value cannot be constructed.

## Common Failures
- Using an enum for the month, which is still usable as an int, instead of a constrained type.
- Leaving the argument order unenforced so a swap still compiles.

## Notes
This drills Item 18: the type system is the tool that turns runtime mistakes into compile errors, and consistency plus removed bookkeeping do the rest.
