---
object_id: DRILL_make_a_class_generic
object_type: drill
name: Make a Type-Specific Class Generic
library_path:
- software-engineering
- core
- reusability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- generics
- reusability
- generalization
- refactoring
cross_links:
- rel: teaches
  target_object_id: PAT_use_generics_for_type_independence
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u09, pp. 260-262
  evidence_type: text
confidence: high
target_skill: replacing a hard-coded element type with a generic placeholder
references: []
variants: []
---

# Make a Type-Specific Class Generic

## Practice Task
Take a container class hard-coded to one element type and rewrite it with a generic placeholder, then use it with two different types.

## Target Skill
Replacing a hard-coded element type with a generic type placeholder to generalize a container.

## Setup
No special setup required.

## Instructions
1. Start from a container hard-coded to one type — a randomized queue that stores only strings.
2. Confirm the limitation: a near-identical need for a different type (pictures instead of words) cannot reuse it.
3. Introduce a type placeholder on the class and replace every hard-coded occurrence of the element type with that placeholder, in fields, parameters, and return types.
4. Instantiate the class with two different concrete types and confirm both work from the same code.
5. Check the nullable edge: if the container returns null to signal empty, decide whether storing nullable elements needs a separate has-next check.

## Success Check
- No concrete element type remains hard-coded in the class.
- The same class stores two different types at two call sites.
- The empty-versus-null-element ambiguity is considered and handled if relevant.

## Common Failures
- Replacing the type in some places but leaving a hard-coded occurrence that defeats the generalization.
- Overlooking that a nullable element type collides with a null empty-signal.

## Notes
This drills Long's `RandomizedQueue` generalization from a string-only queue to one parameterized by a type placeholder. The habit is to notice when a class references a type it does not truly care about, and to lift that type to a placeholder so one implementation serves every element type.
