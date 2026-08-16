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
- State a base operation or invariant that the derived class cannot honor: a list allows duplicates a Set must reject, or `makeBigger` changes a rectangle's width independently of height, which a square cannot allow.
- Confirm the substitutability test fails: the derived object is not usable everywhere the base is.
- Remodel with composition: give `Set` a private `list` member and forward member/insert/remove/size to it, exposing only the Set interface.
- Verify the new type enforces its own contract (no duplicates) rather than inheriting the base's.

## Success Check
- The false is-a is identified by a concrete broken operation or invariant.
- The remodeled type holds the other as a member and exposes only its own interface.
- The contract that inheritance violated now holds.

## Common Failures
- Keeping public inheritance because the base has convenient functions to reuse.
- Exposing the contained object's full interface instead of only the new type's.

## Notes
This drills Items 32 and 38: the reuse temptation is real, but is-a demands substitutability, and Set-on-list fails it — composition with delegation is the fix.
