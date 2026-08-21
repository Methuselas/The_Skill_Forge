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
- Weigh what inlining buys the optimizer, not just what it saves on the call. Removing the call sequence is the smallest benefit. The larger one is that the compiler can then see what the function does *not* do — that it touches no globals, changes no arguments — and so is free to optimize across what was previously an opaque call. A destructor loop over a container of a trivially destructible type disappears entirely when the element's destructor is visible, and costs one call per element when it is defined in another translation unit.
- Give the compiler a call site with only one possible target when you want an indirect call inlined. Passing a function to an algorithm by name leaves the target a runtime pointer value that many instantiations could share; wrapping the same call in a lambda gives the instantiation a unique type, so there is exactly one target and inlining becomes straightforward — an extra layer of indirection in the source that removes one in the object code.

## Don't
- Don't declare a function template inline merely because it lives in a header; template placement and the inlining decision are independent.
- Don't assume constructors and destructors are good inline candidates; compilers inject base-class and member construction and destruction code into them, so they are far larger than they look.

## Checklist
- Is this function small and called often enough to justify inlining?
- Am I inlining a template only because it is defined in a header?
- Could inlining this library function force every client to recompile whenever it changes?

## Notes
inline is a request the compiler may ignore, and it rarely inlines loops, recursion, or virtual calls. The costs are code bloat (worse instruction-cache behavior), debuggers that cannot step into an absent function, and binary fragility: a change to an inline library function forces clients to recompile, not just relink. Constructors and destructors hide generated construction/destruction code, so they inline larger than they appear. Follow the 80-20 rule and inline only the small, hot functions that matter.

The reason inlining matters to the optimizer more than to the call sequence is worth holding
onto, because it explains which non-inlined calls are expensive. Most compiler optimizations
operate within a region of code with one entry and one exit, and a call the compiler cannot
see into ends that region: everything reachable must be assumed modified, every value held
in a register must be assumed stale. Inlining enlarges the region. It also produces a copy of
the body specialized to this call site, where facts that do not hold for the function in general
may hold here — which is a second source of gains that has nothing to do with call overhead.

That cuts both ways and is the reason the guidance above is a limit rather than an
encouragement. A larger region is also more code for the optimizer to analyze within a finite
budget, so inlining everything degrades optimization as surely as inlining nothing. The
resolution is the one this card already states: a small number of small, hot functions.

Virtual functions deserve a specific mention because the request is not merely ignored there —
it can cost you something. Compilers commonly decide which object file holds a class's dispatch
table by a rule keyed to the first non-inline, non-pure virtual function the class defines. A class
whose virtual functions are all declared inline gives that rule nothing to key on, and
implementations following it may then emit a copy of the table in every object file that uses
the class. On a large system that is a great many copies of something there was supposed to be
one of, which is a reason to leave virtual functions out of line beyond the fact that they were
not going to be inlined anyway.
