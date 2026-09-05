---
object_id: PAT_design_modular_interfaces
object_type: pattern
name: Compose Modules With Few Well-Defined Interfaces
library_path:
- software-engineering
- core
- modularity
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- modularity
- interfaces
- coupling
- adaptability
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_reusable_and_generalizable
- rel: prerequisite_for
  target_object_id: PAT_use_dependency_injection
- rel: prerequisite_for
  target_object_id: PAT_depend_on_interfaces_not_concrete_classes
- rel: prerequisite_for
  target_object_id: PAT_prefer_composition_over_inheritance
- rel: prerequisite_for
  target_object_id: PAT_make_classes_care_about_themselves
- rel: prerequisite_for
  target_object_id: PAT_encapsulate_related_data_together
- rel: prerequisite_for
  target_object_id: PAT_dont_leak_implementation_details_in_return_types
- rel: prerequisite_for
  target_object_id: PAT_dont_leak_implementation_details_in_exceptions
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Compose Modules With Few Well-Defined Interfaces

## Pattern Rule
**IF** you are structuring code that a future requirement change may need to reconfigure or replace in parts
**THEN** break it into self-contained modules whose interactions with each neighbor happen in a single place through a well-defined interface with as few points of interaction as possible.

## Do
- Favor the "single peg and hole" interface — one clean point of interaction — over the "twenty interwoven threads" interface that entangles a component with the rest of the system.
- Confine the interaction between two adjacent modules to one location, so changing one piece of functionality does not require edits scattered all over the place.

## Don't
- Don't stitch functionality together so that swapping one part (a new hand that now needs fingers) means cutting many connections and re-stitching new ones, damaging the surrounding work.
- Don't spread the coupling between two modules across many scattered call sites where a single interface would do.

## Checklist
- Can you replace one module without touching the others?
- Is each inter-module interaction confined to one well-defined interface?
- If a new requirement lands on one component, does the change stay contained to it?

## Notes
The two toys make the cost concrete: the modular toy swaps a hand at a single peg-and-hole; the stitched toy needs twenty threads cut and re-sewn, with collateral damage, and the same laborious work again to undo it. Long ties modularity to adaptability and comprehension — well-defined, few-point interfaces localize change and make code easier to reason about. This is the "modular" pillar's foundation; it specializes into layers of abstraction and concrete techniques like dependency injection and interface-based dependencies.
