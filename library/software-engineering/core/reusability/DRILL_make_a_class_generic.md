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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
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
- The limitation is demonstrated first: the second need is written as code and shown not to compile against the original. That it could not be reused is the premise of the exercise rather than a result of it.
- No concrete element type remains, verified by searching the class for the original type's name and reporting the count. A field converted while a parameter or a return type was missed still compiles for the original type and fails only for the second one.
- Both instantiations are compiled and their members exercised. Instantiating and never calling leaves most of the class uninstantiated, so the check passes without having checked anything.
- The empty-versus-null case is decided explicitly and the decision recorded: either the element type is constrained so the sentinel cannot collide, or a separate emptiness query exists. Considering it and moving on satisfies the older wording and leaves the ambiguity exactly where it was.
- The cost of parameterizing is named — the definition must now be visible to every user, and errors arrive at instantiation rather than at the definition, reported against code the user did not write.

## Common Failures
- Replacing the type in some places but leaving a hard-coded occurrence that defeats the generalization.
- Overlooking that a nullable element type collides with a null empty-signal.

## Notes
This drills Long's `RandomizedQueue` generalization from a string-only queue to one parameterized by a type placeholder. The habit is to notice when a class references a type it does not truly care about, and to lift that type to a placeholder so one implementation serves every element type.
