---
object_id: PAT_declare_template_converting_operators_as_friends
object_type: pattern
name: Declare Type-Converting Template Operators as Friends Inside the Class
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- operators
- type_conversion
cross_links:
- rel: related_to
  target_object_id: PAT_make_operator_nonmember_for_conversions
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Declare Type-Converting Template Operators as Friends Inside the Class

## Pattern Rule
**IF** a class template needs a non-member operator that allows implicit conversions on all of its arguments (mixed-mode arithmetic on a numeric class template)
**THEN** declare, and usually define, that operator as a friend inside the class template, because template argument deduction never applies implicit conversions, so a separate function template would not be found.

## Do
- Declare the operator as a friend inside the class template, so it is instantiated as a concrete function when the class is instantiated — a real function, eligible for implicit conversions on its arguments.
- Define the friend in place, or have it call a helper template defined outside the class, since a function you declare you must also define.

## Don't
- Don't leave the operator as a standalone function template and expect mixed-mode calls to work; deduction sees a plain int where the class type is needed and will not convert it, so the call does not compile.

## Checklist
- Does this operator need conversions on every operand, for a class template?
- Is it declared as a friend inside the class template so it becomes a concrete instantiated function?
- Is the friend actually defined, in place or via a helper, not merely declared?

## Notes
Item 24's non-member operator fails once Rational becomes a template: argument deduction refuses implicit conversions, so a plain int argument cannot be deduced to the class type. Declaring the operator a friend inside the class template sidesteps deduction — the concrete operator is generated when the class instantiates, and as a real (non-template) function it can use the class's converting constructor. Here friendship is for automatic instantiation, not private access; keep the body thin by delegating to an outside helper template.
