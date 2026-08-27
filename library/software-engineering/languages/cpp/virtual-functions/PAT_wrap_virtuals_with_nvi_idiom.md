---
object_id: PAT_wrap_virtuals_with_nvi_idiom
object_type: pattern
name: Wrap Virtual Functions with the Non-Virtual Interface Idiom
library_path:
- software-engineering
- languages
- cpp
- virtual-functions
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- virtual_functions
- nvi
- template_method
cross_links:
- rel: related_to
  target_object_id: PAT_externalize_varying_behavior_with_strategy
- rel: related_to
  target_object_id: PAT_never_redefine_inherited_default_parameter
- rel: related_to
  target_object_id: PAT_dont_call_unknown_code_while_holding_a_lock
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Wrap Virtual Functions with the Non-Virtual Interface Idiom

## Pattern Rule
**IF** you want customizable behavior but also control over the context in which it runs
**THEN** expose a public non-virtual function that calls a private (or protected) virtual doing the real work — the non-virtual interface idiom, a form of Template Method.

## Do
- Give clients a public non-virtual wrapper (healthValue) that calls a private virtual (doHealthValue), so derived classes customize the how while the base fixes the when.
- Put shared setup and teardown in the wrapper — check invariants and preconditions before the call, verify postconditions after — so every derived implementation runs in the right context.
- Bracket the call with a lock only where every override is in your own component and its locking is something you can see and keep seeing. Where an override may be supplied by a caller, the virtual is unknown code: take the value before the lock, or release before the dispatch.
- Make the virtual protected instead of private when derived overrides must call the base version.

## Don't
- Don't let clients call the varying virtual directly; you then lose the guaranteed before-and-after context the wrapper provides.
- Don't assume a private virtual cannot be overridden — derived classes may redefine a private virtual (the how) even though they cannot call it (the when); that separation is the point.
- Don't treat the wrapper as a safe place to hold a mutex merely because the base owns the when. Controlling when the call happens is not the same as knowing what the callee does, and a published customization point is exactly the case where you cannot know.

## Checklist
- Is the varying behavior a non-public virtual, wrapped by a public non-virtual function?
- Does the wrapper own the setup/teardown context around the virtual call?
- If base versions must be invoked by overrides, is the virtual protected rather than private?
- If the wrapper takes a lock, can every override that will ever run under it be seen from inside this component?

## Notes
NVI splits two independent concerns: redefining a virtual says how something is done, calling it says when. The wrapper reserves the when for the base class, so it can bracket the call with invariant checks and pre/postcondition verification that direct virtual calls cannot guarantee. This is why virtual functions can — and this school argues should — usually be private; make them protected only when overrides must chain to the base.

One qualification the usual presentation of the idiom omits. The wrapper's control over context is often justified by its ability to hold a mutex across the call, and that justification holds only for a closed override set. `PAT_dont_call_unknown_code_while_holding_a_lock` states the boundary: code that is yours, in the same component, whose locking you can see and keep seeing, is as safe as the rest of the critical section — and an override written outside it is not. Wrapping the virtual does not move it across that line, because who calls the virtual is a different question from who wrote it. The invariant and pre/postcondition bracketing survives on both sides of the line, and is the part of the wrapper's context that never depends on the answer.
