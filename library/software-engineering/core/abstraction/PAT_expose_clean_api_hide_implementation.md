---
object_id: PAT_expose_clean_api_hide_implementation
object_type: pattern
name: Expose a Clean API and Hide Implementation Details
library_path:
- software-engineering
- core
- abstraction
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- api_design
- abstraction
- encapsulation
- implementation_details
cross_links:
- rel: related_to
  target_object_id: PAT_dont_widen_api_for_reuse_or_testing
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Expose a Clean API and Hide Implementation Details

## Pattern Rule
**IF** you are writing or modifying a class, interface, or function that other code will call
**THEN** treat it as exposing a mini-API: publish only the concepts callers need — public functions, their names, parameters, return types, and any required call order — and keep everything else as an implementation detail.

## Do
- Sort each aspect deliberately: the class name, public documentation, and public function signatures are API; private functions and variables, what the class depends on, and the code inside any function (even a public one) are implementation details.
- Use "does this leak into the API?" as a fast layer-cleanliness check — if something that should be internal appears in an input parameter, return type, or public function, the layer is not as distinct as it should be.

## Don't
- Don't expose a public function or type whose presence forces callers to understand how the subproblem is solved internally.
- Don't treat "it's all my code" as license to ignore the API boundary; the boundary is what lets the layer be understood and swapped without reading its internals.

## Checklist
- Can a caller use this code correctly from its public names, types, and documentation alone?
- Does any implementation detail appear in a parameter, return type, or public function?
- Is the required call order (if any) stated as part of the API?

## Notes
Long borrows the service term "API" for in-process code: just as a service hides its implementation behind an interface callers program against, a class or function exposes a small surface and hides the rest. The value is a precise, succinct way to talk about the layer of abstraction a piece of code provides, and a concrete leak test for whether the layer is clean. This underpins the later warning against widening the API merely to enable reuse or testing.
