---
object_id: PAT_factor_parameter_independent_code_from_templates
object_type: pattern
name: Factor Parameter-Independent Code Out of Templates
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
- code_bloat
- efficiency
cross_links:
- rel: related_to
  target_object_id: PAT_use_private_inheritance_judiciously
- rel: related_to
  target_object_id: PAT_limit_inlining_to_small_hot_functions
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u07, pp. 212-217
  evidence_type: text
confidence: high
references: []
variants: []
---

# Factor Parameter-Independent Code Out of Templates

## Pattern Rule
**IF** a template instantiates code that does not actually depend on all of its parameters (such as a non-type size parameter)
**THEN** factor that code into a less-parameterized place — a base class templatized only on the varying type, or function parameters and data members instead of non-type parameters — to avoid code bloat from repeated instantiations.

## Do
- Move size-independent logic into a base class templatized only on the element type, and have each sized derived class make inline calls into it (SquareMatrix delegating to SquareMatrixBase).
- Replace a non-type template parameter with a function parameter or a data member so one function body serves many sizes.
- Cut type-parameter bloat by having strongly-typed instantiations share one underlying implementation — pointer templates delegating to a void-pointer version.

## Don't
- Don't leave code that differs only by a constant inside the template; each instantiation duplicates it, as a 5-by-5 and a 10-by-10 invert do.
- Don't inline the shared base function, or you reinstate the duplication you just factored out.

## Checklist
- Does any code in this template not depend on all of its parameters?
- Can a non-type parameter become a function parameter or a data member?
- Is the shared implementation non-inline and reused across instantiations?

## Notes
Template replication is implicit: one source copy, but many instantiated bodies. The SquareMatrix invert example bloats because size is a non-type parameter, so each size gets its own copy; moving invert into a base templatized only on the element type (reached by private inheritance) shares one body. Trade-offs are real — the size-specific version can optimize a compile-time constant the shared version cannot, and a stored data pointer adds size — so measure before deciding.
