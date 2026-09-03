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
- Define `Person`'s destructor in the implementation file, and say why it cannot be implicitly generated in the header when the pointee is incomplete.
- Replace definition includes in the header with forward declarations where possible, and include declaration-only headers for the types used in the interface. Justify every include that remains as declaration-only or as a type the interface uses by value, and record any you kept only because removing it broke the build.
- Change `PersonImpl`, run the build, and record what actually rebuilt.
- Name the costs — one indirection per call, one allocation per object, and a forwarding function per member to keep in step — and state what the forwarding silently removed: inlining across the boundary, and any member that used to be usable in a constant expression.

## Success Check
- Every include remaining in the header is justified as declaration-only, or as a type the interface uses by value. An include kept because removing it broke the build is the coupling this drill removes, and it is recorded rather than tolerated.
- The recompilation claim is tested rather than asserted: the implementation is changed, the build is run, and what actually rebuilt is recorded. Build systems differ enough that this has to be observed on the one in use.
- The destructor is accounted for. A class holding a smart pointer to an incomplete type will not compile with an implicitly generated destructor, so the run says where the destructor is defined and why it must live in the implementation file.
- The costs are named — one indirection per call, one allocation per object, and a forwarding function per member to keep in step. A run concluding only that compilation coupling fell has priced one side of the trade.
- What the forwarding silently removed is stated: inlining across the boundary, and any member that used to be usable in a constant expression.

## Common Failures
- Leaving definition includes in the header that reintroduce the dependency.
- Forward-declaring a standard-library type such as string instead of including its header.

## Notes
This drills Item 31: the pimpl pointer plus forward declarations move the implementation types out of the header, so client code depends only on the interface.
