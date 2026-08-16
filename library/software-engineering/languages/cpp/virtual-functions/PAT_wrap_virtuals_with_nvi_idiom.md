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
- Put shared setup and teardown in the wrapper — lock a mutex, check invariants and preconditions before the call, verify postconditions after — so every derived implementation runs in the right context.
- Make the virtual protected instead of private when derived overrides must call the base version.

## Don't
- Don't let clients call the varying virtual directly; you then lose the guaranteed before-and-after context the wrapper provides.
- Don't assume a private virtual cannot be overridden — derived classes may redefine a private virtual (the how) even though they cannot call it (the when); that separation is the point.

## Checklist
- Is the varying behavior a non-public virtual, wrapped by a public non-virtual function?
- Does the wrapper own the setup/teardown context around the virtual call?
- If base versions must be invoked by overrides, is the virtual protected rather than private?

## Notes
NVI splits two independent concerns: redefining a virtual says how something is done, calling it says when. The wrapper reserves the when for the base class, so it can bracket the call with mutex locks, invariant checks, and pre/postcondition verification that direct virtual calls cannot guarantee. This is why virtual functions can — and this school argues should — usually be private; make them protected only when overrides must chain to the base.
