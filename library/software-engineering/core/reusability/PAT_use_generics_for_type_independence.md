---
object_id: PAT_use_generics_for_type_independence
object_type: pattern
name: Use Generics for Type-Independent Subproblems
library_path:
- software-engineering
- core
- reusability
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- generics
- reusability
- generalization
- types
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_reusable_and_generalizable
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u09, pp. 259-262
  evidence_type: text
confidence: high
references: []
variants: []
---

# Use Generics for Type-Independent Subproblems

## Pattern Rule
**IF** a class solves a subproblem that does not actually care about the specific type it stores or references
**THEN** write it with a generic type placeholder instead of hard-coding a concrete type, so the same code generalizes to any type.

## Do
- Replace the hard-coded type with a placeholder: a randomized queue written against a fixed string type only serves word games, but declared with a placeholder T it stores anything.
- Reach for generics when you notice the code references another type it does not really care about — it is usually little extra work for a large gain in generality.
- Let each caller pick the concrete type at use: one team stores strings for a word game, another stores pictures for a near-identical picture game, from the same class.

## Don't
- Don't hard-code a concrete type into a fundamentally type-agnostic container; a near-identical subproblem elsewhere then cannot reuse your solution and must reimplement it.
- Don't ignore the nullable-return edge: if the container returns null to mean empty, storing nullable elements makes empty indistinguishable from a null element, so add a has-next check if that case matters.

## Checklist
- Does this class truly depend on the specific type it holds, or would any type do?
- Could a near-identical subproblem for a different type reuse this code unchanged?
- If the type placeholder can be nullable, is "empty" still distinguishable from a null element?

## Notes
Generics turn a one-type solution into a whole family of reuses for almost no cost. Long's `RandomizedQueue` hard-coded to strings serves only the word game, yet the same add-and-remove-random logic is exactly what a picture game needs; a type placeholder generalizes it to both. The pattern completes the reusability pillar's theme — spot the fundamental, type-agnostic subproblem and write it once for every type — with the nullable-element caveat as the one edge to watch.
