---
object_id: PAT_price_virtual_dispatch_against_the_real_alternative
object_type: pattern
name: Price Virtual Dispatch Against the Real Alternative
library_path:
- software-engineering
- languages
- cpp
- virtual-functions
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- virtual_functions
- performance
- inlining
- design
cross_links:
- rel: related_to
  target_object_id: PAT_match_virtualness_to_inherited_interface
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: PAT_optimize_for_what_the_compiler_can_prove
- rel: related_to
  target_object_id: PAT_limit_inlining_to_small_hot_functions
- rel: related_to
  target_object_id: AP_design_a_customization_point
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Price Virtual Dispatch Against the Real Alternative

## Pattern Rule
**IF** someone proposes avoiding a virtual function on performance grounds
**THEN** establish what the non-virtual replacement would actually be, and compare against that — which is usually another form of runtime dispatch, not a direct call
**ELSE** where the type genuinely is known at compile time, the comparison against a direct call is the right one, and what it costs is mostly the lost inlining rather than the indirection.

## Do
- Separate the two costs, because they differ by orders of magnitude. The dispatch itself is an extra pointer load and an indirect jump — call machinery roughly twice as expensive as a direct call, and rarely more than ten to fifteen percent of a simple function's total time. Not being inlinable is the other cost, and it is the one that matters.
- Follow what the lost inlining takes with it. A one-line accessor compiles to an instruction or none when inlined; out of line it pays the full call sequence. Worse, an opaque call forces the compiler to assume the callee may touch any reachable state, so optimizations around the call site are given up too — which is how the gap reaches orders of magnitude in the bad case.
- Notice when the question is malformed. If the target is known at compile time, you would not have written a virtual call; if it is only known at run time, a direct call was never available. The honest comparison is against the dispatch mechanism you would write instead.
- Rank the runtime alternatives before assuming yours is faster. A chain of conditionals or a switch on a type tag is generally slower once there are more than two cases, and the fastest general answer is a table of function pointers indexed by a runtime value — which is precisely what the compiler generates for a virtual call.
- Let the compiler remove the dispatch where it can prove the type. When the concrete type is deducible at the call site, the call is converted to a direct one and becomes inlinable again — so keeping types visible where it matters is more productive than avoiding virtual functions.
- Reserve the whole question for measured hot paths. Dispatch cost shows up where a very small function is called very many times; anywhere else the machinery is a small fraction of the work being dispatched to.

## Don't
- Don't quote a figure for what a virtual call costs. Every quantified answer — twice as slow, fifteen percent, negligible, orders of magnitude, and even faster than the alternative — is correct in some context, and the context is what decides.
- Don't replace virtual dispatch with a hand-built function-pointer table and expect a gain. You have reimplemented what the compiler was already doing, with the same loss of inlining and none of the type checking.
- Don't devirtualize by adding a type tag and a switch. It is more code, usually slower past two cases, and it moves a correctness property the compiler was enforcing into a conditional somebody has to maintain.
- Don't choose a design around this cost without a profile. The design consequences of avoiding polymorphism are large and permanent; the performance difference is frequently unmeasurable.

## Checklist
- What would the non-virtual version of this call actually be?
- Is the function small enough that call machinery is a significant fraction of it?
- Could the compiler determine the concrete type here, making the call direct?
- How many times per unit of work does this dispatch happen?
- Does a profile attribute meaningful time to this call site at all?

## Notes
This settles a question that gets asked constantly and answered badly. The reason no single number is right is that the measured cost depends on the size of the function being called, whether the caller could otherwise have inlined it, what the surrounding code loses by having an opaque call in the middle of it, and the state of the caches — which is why a survey of plausible answers can contain a hundredfold spread with every entry defensible.

The framing that makes the decision tractable is to stop treating virtual dispatch as an overhead added to a call, and treat it as one implementation of runtime selection. Every program that must choose behaviour at run time pays for the choice somewhere; the language feature exists because the compiler's implementation of that choice is a good one and is checked for consistency in a way a hand-rolled table is not.

Where the cost is genuinely worth attention is a small virtual function called in a tight loop — an accessor, a comparison, a one-line hook — because the ratio of call machinery to real work is at its worst and the lost inlining removes the optimization that would have made it free. That is a narrow, recognizable situation rather than a general property of polymorphic design.

It helps to know which of the related features charge what, because they are usually discussed as one lump and they are not. Virtual functions cost per-class table space, one hidden pointer inside every object, and the loss of inlining. Multiple inheritance adds to the first two — more hidden pointers, extra tables, slightly more work locating them — and takes nothing further from inlining. Virtual bases often add another pointer per object and sometimes none, depending on how the implementation avoids replicating the shared base. Run-time type identification costs one more table entry per class plus the type object itself and leaves object size alone. Of these, only the per-object costs scale with how many objects exist, which is why they are the ones that matter on small, numerous objects and are close to irrelevant on large ones.
