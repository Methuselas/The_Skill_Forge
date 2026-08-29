---
object_id: PAT_split_code_to_make_it_testable
object_type: pattern
name: Split Code Into Smaller Units to Make It Testable
library_path:
- software-engineering
- core
- testing
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- unit_testing
- modularity
- public_api
- refactoring
cross_links:
- rel: related_to
  target_object_id: PAT_size_classes_by_pillars_not_lines
- rel: related_to
  target_object_id: AP_write_a_unit_test_suite
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Split Code Into Smaller Units to Make It Testable

## Pattern Rule
**IF** testing all of a unit's behaviors through its public API feels daunting because that unit does too much
**THEN** split the complicated subproblem into its own unit — a class, or a separate translation unit with its own header — so it can be tested directly through its own public API, rather than exposing a private function to reach it.

## Do
- Read the urge to make a private function visible as a signal the class is doing too much: when a credit-rating check grows complex with error cases, that complexity belongs in its own unit.
- Extract the subproblem into a dedicated class (a credit-rating checker) that the original class depends on, so each class exposes a testable public API of its own.
- Let the extraction simplify the original class too, since it no longer holds the nuts-and-bolts logic for the subproblem.

## Don't
- Don't reach for "visible only for testing" because testing through the public API seems hard; the difficulty is a symptom of a class that should be split.
- Don't leave a sprawling class and try to test its tangled internals; the real fix is thinner layers, each independently testable.

## Checklist
- Is the reason testing-via-public-API feels hard that the class is doing too much?
- Could the awkward-to-test logic become its own class with its own public API?
- After splitting, can each unit be tested through its own surface without exposing internals?

## Notes
When testing through the public API genuinely feels infeasible, Long identifies the deeper cause: the class is doing too much, which is exactly when engineers resort to exposing privates. Extracting the complex subproblem — moving credit-rating logic into a `CreditRatingChecker` — gives it a public API that is straightforward to test and simplifies the original class. This is chapter 2's class-sizing and layering advice arriving through the door of testability.
