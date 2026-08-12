---
object_id: PAT_precede_nested_dependent_types_with_typename
object_type: pattern
name: Precede Nested Dependent Type Names with typename
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- typename
- dependent_names
cross_links:
- rel: related_to
  target_object_id: PAT_program_to_a_templates_implicit_interface
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u07, pp. 203-207
  evidence_type: text
confidence: high
references: []
variants: []
---

# Precede Nested Dependent Type Names with typename

## Pattern Rule
**IF** you refer to a nested dependent type name inside a template — a type nested in something that depends on a template parameter, such as C::const_iterator
**THEN** precede it with the keyword typename, because the compiler otherwise assumes a nested dependent name is not a type.

## Do
- Write typename before the nested dependent type when declaring a variable of it, so the parser reads it as a type rather than a value.
- Pair it with typedef for long traits names (typedef typename ... value_type value_type;) so you write the full name only once.

## Don't
- Don't put typename on a non-dependent name or on the template parameter itself (the C in a const C& parameter); typename is only for nested dependent type names.
- Don't use typename in a base class list or a member initialization list, even for a nested dependent type name — it is disallowed in those two positions.

## Checklist
- Is this a type nested inside something dependent on a template parameter, and is it preceded by typename?
- Am I wrongly adding typename to a non-dependent name or in a base-class-list or init-list position?
- Have I used typedef typename to avoid repeating a long nested dependent type name?

## Notes
Until the template parameter is known, the parser cannot tell whether C::const_iterator names a type or a static member being multiplied, so C++ assumes not-a-type by default; typename overrides that. The rule has one irksome exception — a base class list and a member initialization list forbid typename on the same names that otherwise require it. The typedef typename juxtaposition looks odd but follows directly from the rule.
