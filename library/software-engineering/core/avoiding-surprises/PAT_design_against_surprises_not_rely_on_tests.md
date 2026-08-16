---
object_id: PAT_design_against_surprises_not_rely_on_tests
object_type: pattern
name: Design Against Surprises Rather Than Relying on Tests to Catch Them
library_path:
- software-engineering
- core
- avoiding-surprises
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- avoid_surprises
- testing
- api_design
- mocks
cross_links:
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: medium
references: []
variants: []
---

# Design Against Surprises Rather Than Relying on Tests to Catch Them

## Pattern Rule
**IF** you are tempted to leave code that could surprise a caller because tests should catch any resulting problems
**THEN** don't rely on tests for this — design the surprise out, because the failures happen in other engineers' code and tests you do not control.

## Do
- Remember you control your own tests but not your callers': another engineer may not test the corner case that exposes your surprising behavior, especially for rare or large-input scenarios.
- Prefer removing the surprise at the contract level (explicit returns, honest names, required inputs) over trusting a test to notice it downstream.

## Don't
- Don't count on mocks to reveal a surprise; an engineer who misunderstands your code will program a mock to behave the way they wrongly think it does, so the bug never surfaces in their tests.
- Don't assume testing covers effects that are hard to test — multithreading bugs from hidden side effects appear only at scale and with low probability.

## Checklist
- Would catching this issue depend on someone else testing a corner case they may not think of?
- Could a mock of your code encode the wrong assumption and pass anyway?
- Is the surprising behavior something tests are known to miss, like a concurrency effect?

## Notes
Long closes the chapter by rebutting "just test it": testing is essential but does not substitute for unsurprising code, because avoiding surprises is about the correctness of the code other engineers build on yours. Three gaps make tests an unreliable backstop here — callers test less diligently, mocks bake in the caller's mistaken mental model, and some effects (concurrency) evade tests almost by nature. The same reasoning carries into making code hard to misuse in chapter 7.
