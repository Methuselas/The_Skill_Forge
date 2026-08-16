---
object_id: PAT_program_to_a_templates_implicit_interface
object_type: pattern
name: Program to a Template's Implicit Interface
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- generic_programming
- compile_time_polymorphism
cross_links:
- rel: related_to
  target_object_id: PAT_adapt_rules_to_active_cpp_sublanguage
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Program to a Template's Implicit Interface

## Pattern Rule
**IF** you are writing or using a function or class template
**THEN** reason about its type parameters through the implicit interface — the set of expressions that must compile — rather than explicit function signatures, because template constraints are checked during compilation by instantiation.

## Do
- Identify the valid expressions a template requires of a parameter — a size() call, an operator!= comparison, copy construction — and treat that expression set as the interface the type must satisfy.
- Rely on compile-time polymorphism: which functions run is settled during instantiation and overload resolution, not at runtime.
- Allow for operator overloading and implicit conversions when judging validity; a return value need only support the expression it appears in, possibly after a conversion.

## Don't
- Don't assume a parameter needs an exact signature, such as an integral-returning size() or a specific operator>; it only needs expressions that compile, which is looser than an explicit interface.

## Checklist
- What set of expressions must compile for this template to instantiate — that is its implicit interface?
- Is the behavior resolved during compilation (instantiation and overloading) rather than at runtime?
- Am I over-constraining by thinking in signatures instead of valid expressions?

## Notes
Classes have explicit interfaces (signatures) and runtime polymorphism (virtuals); templates have implicit interfaces (valid expressions) and compile-time polymorphism (instantiation). In the doProcessing template, T need not offer an integral size() or a defined operator>; it need only make the expressions compile, which overloading and conversions can satisfy in surprising ways. This is the shift from Object-Oriented C++ into Template C++ (the sublanguage rule from Item 1): same rigor, different interface model.
