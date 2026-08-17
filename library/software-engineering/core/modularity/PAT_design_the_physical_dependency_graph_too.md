---
object_id: PAT_design_the_physical_dependency_graph_too
object_type: pattern
name: Design the File and Library Dependencies, Not Only the Class Ones
library_path:
- software-engineering
- core
- modularity
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- coupling
- modularity
- build_structure
- dependencies
cross_links:
- rel: related_to
  target_object_id: PAT_design_modular_interfaces
- rel: related_to
  target_object_id: PAT_make_classes_care_about_themselves
reference:
  source_title: The Pragmatic Programmer
  author: Andrew Hunt & David Thomas
confidence: high
references: []
variants: []
---

# Design the File and Library Dependencies, Not Only the Class Ones

## Pattern Rule
**IF** you are settling how a growing system is split up, and you have already decided which module depends on which
**THEN** decide the arrangement into files, directories, and libraries at the same time and keep that arrangement's dependency graph free of cycles, because rebuild time and test isolation are set by that second graph and not by the logical one.

## Do
- Read the physical symptoms as design feedback rather than as build-system trouble: a link command for one unit test longer than the test program itself, a "simple" change to one module propagating through modules unrelated to it, and developers unwilling to change code because they cannot tell what it might affect.
- Ask what a file actually needs from a type before depending on its full definition. A class holding another type by value forces every user to pull in that type's whole declaration; holding it by pointer or reference, with only a forward declaration, means the internals can change without rebuilding anything downstream.
- Check that one unit test can be built against a small part of the system. When the test drags in the rest of the system as support code, the physical arrangement is already wrong, whatever the class diagram says.
- Do the physical layout in tandem with the logical design, not after it, because the two constrain each other and only one of them can be fixed cheaply later.

## Don't
- Don't assume a clean class design buys you a clean build. Two classes with a tidy logical interface can still sit in files that each drag in the other's world.
- Don't leave a cycle among files, directories, or libraries to be untangled later. Undoing cyclic physical dependencies across a large body of code is extremely difficult, which is why this is done early or effectively not at all.
- Don't treat a build measured in hours as an infrastructure problem to solve with hardware when its cause is the dependency structure.

## Checklist
- Can you name the set of files a change to this one forces a rebuild of?
- Is there any cycle among the files, directories, or libraries?
- Can a single unit test be built without pulling in the whole system?
- Does this file need the full definition of that type, or only its name?

## Notes
There are two dependency graphs over the same code and they are not the same graph. The logical one records who calls whom and is what a design discussion is usually about. The physical one records what must be rebuilt, relinked, and shipped together, and it is the one that sets how long a build takes and whether a piece can be tested on its own. A design can score well on the first and badly on the second — the classes talk through narrow interfaces, and the files still include each other's entire worlds.

The asymmetry is what makes this worth deciding early. Logical coupling can be loosened a piece at a time: move a method, introduce an interface, and the rest of the system carries on. A cycle in the physical graph cannot be broken a piece at a time, because every candidate first step needs one of the other files to have moved already. On a large system this is the difference between a refactor and a rewrite, so the physical arrangement has to be designed alongside the logical one rather than falling out of it.

The three symptoms are worth memorising because they show up long before anyone connects them to design. The overlong link line and the whole-system unit test are the direct measurement. The third — people who will not touch a piece of code — is the one usually blamed on caution or on team culture, when it is a rational response to a dependency graph nobody can hold in their head.
