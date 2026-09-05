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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
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
- Design the contract and the code that checks the contract as one job. A written precondition and postcondition are already a test plan: the precondition says to pass something that violates it and confirm rejection, and to pass the value sitting exactly on it and confirm acceptance; the postcondition says what to assert about the result across the legal range.
- Write those tests before the implementation when you can, for the reason that survives whatever you think of test-first as a methodology — it makes you use the interface before you are committed to it, and an interface that is awkward to call is cheapest to change while nothing calls it yet.

## Don't
- Don't treat testing as an afterthought bolted on at the end; code that was not built to be testable can become impossible to test properly.
- Don't build a unit that can only be exercised through an expensive, risky, whole-system setup when a smaller boundary would do.
- Don't assume a passing suite means the contract was right. Tests written against a stated contract check two things at once — whether the code meets the contract, and whether the contract says what its author believed it said — and only the second one catches a unit that correctly implements the wrong promise.

## Checklist
- Can this unit be run and asserted on outside the full system?
- Did you ask "how will I test this?" before considering the code finished?
- Are the scenarios you need to cover cheap and safe to set up?
- Is there a stated contract here that the test cases can be read off, or are the cases being invented?

## Notes
Deriving the cases from a contract is what turns "we tested it" into something with a defined edge. The usual alternative is throwing a few plausible values at the code and calling it tested, which stops wherever confidence runs out rather than wherever the promises do. A contract that says an argument must be non-negative and that the result squared must come within a small fraction of the argument names its own cases: the rejected negative, the accepted zero at the boundary, and a spread of legal values checked against the tolerance. Nothing had to be invented, and the coverage question has an answer.

The second-order benefit is the one worth remembering, because it catches a class of failure that a correct implementation cannot. Writing the tests forces the contract to be stated precisely enough to be executable, and that is where an author discovers their own contract does not mean what they thought — a boundary they had not decided, an error case they had assumed away, a promise they cannot actually keep. Code that faithfully implements a wrong contract passes every test derived from it and fails in production, so the moment the contract itself gets examined is the moment that risk is addressed.

The car braking system is the anchor: as an inseparable whole it can only be tested by building a car, renting a track, and endangering a person; as a distinct module it takes a recorded video and checks the output signal, making thousands of scenarios cheap and safe. Long ties testability to modularity and warns against treating tests as an afterthought, noting some engineers write tests first (TDD). This is the "testable" pillar's foundation; it specializes into unit-testing principles and practices.
