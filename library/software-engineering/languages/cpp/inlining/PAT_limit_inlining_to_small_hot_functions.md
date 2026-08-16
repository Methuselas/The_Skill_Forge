---
object_id: PAT_limit_inlining_to_small_hot_functions
object_type: pattern
name: Limit Inlining to Small, Frequently Called Functions
library_path:
- software-engineering
- languages
- cpp
- inlining
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- inlining
- performance
- build
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_inline_functions_to_macro_functions
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Limit Inlining to Small, Frequently Called Functions

## Pattern Rule
**IF** you are deciding whether to declare a function inline
**THEN** reserve inline for small, frequently called functions, because inline is only a request and overusing it causes code bloat, harder debugging, and forced client recompiles.

## Do
- Inline trivial, hot functions such as a one-line accessor; start by inlining almost nothing and add it later as a deliberate, measured optimization.
- Keep inline off library functions whose bodies may change, so clients can relink instead of recompiling.

## Don't
- Don't declare a function template inline merely because it lives in a header; template placement and the inlining decision are independent.
- Don't assume constructors and destructors are good inline candidates; compilers inject base-class and member construction and destruction code into them, so they are far larger than they look.

## Checklist
- Is this function small and called often enough to justify inlining?
- Am I inlining a template only because it is defined in a header?
- Could inlining this library function force every client to recompile whenever it changes?

## Notes
inline is a request the compiler may ignore, and it rarely inlines loops, recursion, or virtual calls. The costs are code bloat (worse instruction-cache behavior), debuggers that cannot step into an absent function, and binary fragility: a change to an inline library function forces clients to recompile, not just relink. Constructors and destructors hide generated construction/destruction code, so they inline larger than they appear. Follow the 80-20 rule and inline only the small, hot functions that matter.
