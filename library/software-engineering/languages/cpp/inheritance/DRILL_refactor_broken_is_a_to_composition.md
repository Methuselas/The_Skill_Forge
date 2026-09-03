---
object_id: DRILL_refactor_broken_is_a_to_composition
object_type: drill
name: Refactor a Broken Is-A Hierarchy to Composition
target_skill: Detecting a false is-a and remodeling it with composition
library_path:
- software-engineering
- languages
- cpp
- inheritance
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- inheritance
- composition
- refactoring
cross_links:
- rel: related_to
  target_object_id: PAT_model_has_a_with_composition
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Refactor a Broken Is-A Hierarchy to Composition

## Practice Task
Given a `Set` publicly inheriting from `list` (or a `Square` publicly inheriting from `Rectangle`), show why the is-a fails and remodel it.

## Target Skill
Testing an inheritance link for true substitutability and replacing a false is-a with composition.

## Setup
No special setup required.

## Instructions
- Write, as code that compiles against the inheritance version, a base operation or invariant the derived class cannot honor: a list allows duplicates a Set must reject, or `makeBigger` changes a rectangle's width independently of height, which a square cannot allow. Run it and record the wrong result.
- Fail substitutability in practice: pass the derived object where the base is expected and observe the breakage.
- Remodel with composition: give `Set` a private `list` member and forward member/insert/remove/size to it, exposing only the Set interface. Enumerate the forwarded members with a reason for each, and name any member deliberately not forwarded.
- List the new type's public surface and confirm the base's interface is absent from it.
- Exercise the new type's own contract against the case that broke before and show it holds.

## Success Check
- The broken operation is written as code that compiles against the inheritance version and produces a wrong result when run. A stated invariant violation is the argument; the failing call is the evidence.
- Substitutability is failed in practice, by passing the derived object where the base is expected and observing the breakage rather than reasoning about the relationship.
- After remodelling, the base's interface is confirmed absent from the new type's public surface by listing that surface. A composition forwarding everything has reproduced the inheritance with more typing.
- The forwarded members are enumerated with a reason each, and any member deliberately not forwarded is named. That omission is what composition bought.
- The new type's own contract is exercised against the case that broke before and shown to hold.

## Common Failures
- Keeping public inheritance because the base has convenient functions to reuse.
- Exposing the contained object's full interface instead of only the new type's.

## Notes
This drills Items 32 and 38: the reuse temptation is real, but is-a demands substitutability, and Set-on-list fails it — composition with delegation is the fix.
