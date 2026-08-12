---
object_id: PAT_design_a_class_as_type
object_type: pattern
name: Design a Class as You Would Design a Type
library_path:
- software-engineering
- languages
- cpp
- interface-design
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- class_design
- type_design
- invariants
cross_links:
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
- rel: related_to
  target_object_id: PAT_define_your_code_contract_explicitly
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u04, pp. 84-86
  evidence_type: text
confidence: high
references: []
variants: []
---

# Design a Class as You Would Design a Type

## Pattern Rule
**IF** you are about to define a new class
**THEN** treat it as designing a new type and work through the full set of type-design questions before fixing the declaration, because a class defines a type and deserves the care language designers give the built-in types.

## Do
- Decide how objects are created and destroyed, and how initialization differs from assignment — this shapes the constructors, destructor, and assignment operators.
- Define the legal values and invariants the members must maintain, and where you will check them.
- Settle inheritance fit (virtual or not, and whether others may derive), the allowed conversions, which operators and functions belong, what to disallow, and who gets access.

## Don't
- Don't start writing members before deciding what pass-by-value means for the type, what "undeclared interface" guarantees it makes (performance, exception safety, resource use), and whether you truly need a new type rather than a non-member function.

## Checklist
- Have I decided creation and destruction, initialization versus assignment, and copy/pass-by-value semantics?
- What are the type's invariants, and where are they enforced?
- Does it fit an inheritance graph, what conversions are allowed, and what should be disallowed or kept private?

## Notes
Defining a class is defining a type, so the same care language designers spend on int and double applies. Meyers frames it as a checklist of unavoidable questions: creation/destruction, init-versus-assignment, pass-by-value meaning (the copy constructor), legal values and invariants, inheritance fit, conversions, which functions are members, what to disallow, access, the undeclared performance/exception/resource guarantees, generality (maybe a template), and whether a new type is even warranted. Answering them up front prevents a poorly planned class that cannot be given natural syntax or efficient implementation later.
