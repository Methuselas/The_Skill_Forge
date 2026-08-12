---
object_id: PAT_design_for_testability
object_type: pattern
name: Design for Testability While You Write
library_path:
- software-engineering
- core
- testing
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- testability
- testing
- modularity
- design
cross_links:
- rel: related_to
  target_object_id: PAT_design_modular_interfaces
- rel: prerequisite_for
  target_object_id: PAT_structure_tests_arrange_act_assert
- rel: prerequisite_for
  target_object_id: PAT_tests_fail_only_when_code_broken
- rel: prerequisite_for
  target_object_id: PAT_keep_tests_agnostic_to_implementation
- rel: prerequisite_for
  target_object_id: PAT_write_well_explained_test_failures
- rel: prerequisite_for
  target_object_id: PAT_keep_unit_tests_fast_to_run
- rel: prerequisite_for
  target_object_id: PAT_test_important_behaviors_beyond_public_api
- rel: prerequisite_for
  target_object_id: PAT_use_test_double_only_when_needed
- rel: prerequisite_for
  target_object_id: PAT_prefer_fakes_over_mocks_and_stubs
- rel: prerequisite_for
  target_object_id: PAT_pick_and_choose_testing_philosophies
- rel: prerequisite_for
  target_object_id: PAT_test_behaviors_not_functions
- rel: prerequisite_for
  target_object_id: PAT_dont_expose_privates_for_testing
- rel: prerequisite_for
  target_object_id: PAT_split_code_to_make_it_testable
- rel: prerequisite_for
  target_object_id: PAT_test_one_behavior_per_case
- rel: prerequisite_for
  target_object_id: PAT_use_shared_test_setup_carefully
- rel: prerequisite_for
  target_object_id: PAT_use_appropriate_assertion_matchers
- rel: prerequisite_for
  target_object_id: PAT_inject_dependencies_for_testability
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u01, pp. 18-21
  evidence_type: text
confidence: high
references: []
variants: []
---

# Design for Testability While You Write

## Pattern Rule
**IF** you are writing code that will later need to be verified — which is essentially all non-throwaway code
**THEN** continually ask "how will we test this?" as you write, and shape the code as a distinct unit that can be run and asserted on in isolation, rather than only inside the full system.

## Do
- Make the unit runnable outside its heavy context: an emergency-braking module you can feed a prerecorded video of a pedestrian beats one you can only test by driving a real car at a real person.
- Lean on modular structure, because testability tracks modularity — the same interface boundaries that make code modular let you cheaply exercise thousands of scenarios.
- Distinguish the two halves of the pillar: "make code testable" (a property of the real code) and "test it properly" (writing the tests) are related but separate obligations.

## Don't
- Don't treat testing as an afterthought bolted on at the end; code that was not built to be testable can become impossible to test properly.
- Don't build a unit that can only be exercised through an expensive, risky, whole-system setup when a smaller boundary would do.

## Checklist
- Can this unit be run and asserted on outside the full system?
- Did you ask "how will I test this?" before considering the code finished?
- Are the scenarios you need to cover cheap and safe to set up?

## Notes
The car braking system is the anchor: as an inseparable whole it can only be tested by building a car, renting a track, and endangering a person; as a distinct module it takes a recorded video and checks the output signal, making thousands of scenarios cheap and safe. Long ties testability to modularity and warns against treating tests as an afterthought, noting some engineers write tests first (TDD). This is the "testable" pillar's foundation; chapters 10 and 11 specialize it into unit-testing principles and practices.
