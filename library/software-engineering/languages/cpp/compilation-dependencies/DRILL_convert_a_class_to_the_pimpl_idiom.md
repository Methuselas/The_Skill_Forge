---
object_id: DRILL_convert_a_class_to_the_pimpl_idiom
object_type: drill
name: Convert a Class to the Pimpl Idiom
target_skill: Decoupling a class interface from its implementation with a Handle class
library_path:
- software-engineering
- languages
- cpp
- compilation-dependencies
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- compilation_dependencies
- pimpl
- refactoring
cross_links:
- rel: related_to
  target_object_id: PAT_minimize_compilation_dependencies
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Convert a Class to the Pimpl Idiom

## Practice Task
Given a `Person` class whose header includes date.h and address.h and stores those members directly, convert it to a Handle class using the pimpl idiom.

## Target Skill
Replacing dependencies on definitions with dependencies on declarations by hiding data behind an implementation pointer.

## Setup
No special setup required.

## Instructions
- Move the data members into a forward-declared `PersonImpl` class defined in a separate file.
- Give `Person` a single smart pointer to `PersonImpl` and forward each member function to it.
- Replace definition includes in the header with forward declarations where possible, and include declaration-only headers for the types used in the interface.
- Confirm that changing `PersonImpl` no longer forces clients of `Person` to recompile.

## Success Check
- `Person`'s header depends on declarations, not definitions, of its implementation types.
- A change to the implementation requires clients only to relink, not recompile.

## Common Failures
- Leaving definition includes in the header that reintroduce the dependency.
- Forward-declaring a standard-library type such as string instead of including its header.

## Notes
This drills Item 31: the pimpl pointer plus forward declarations move the implementation types out of the header, so client code depends only on the interface.
