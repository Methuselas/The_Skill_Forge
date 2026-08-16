---
object_id: PAT_prefer_fakes_over_mocks_and_stubs
object_type: pattern
name: Prefer Fakes Over Mocks and Stubs
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
- fakes
- mocks
- stubs
cross_links:
- rel: related_to
  target_object_id: PAT_use_test_double_only_when_needed
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Prefer Fakes Over Mocks and Stubs

## Pattern Rule
**IF** you have decided a test needs a test double
**THEN** prefer a fake — a simplified but contract-faithful implementation — over a mock or a stub, using mocks and stubs only as a last resort when no real dependency or fake is available.

## Do
- Understand the three doubles: a mock records and verifies the calls made to a dependency (good for checking a side effect happened), a stub returns predefined values (good for feeding inputs), and a fake is a working alternative implementation that stores state internally.
- Choose a fake because it enforces the real contract: a fake bank account that throws on a negative debit, and rounds a returned balance the way the real one does, catches bugs a mock or stub silently passes.
- Have the dependency's owning team maintain the fake, so its contract stays identical to the real implementation as that changes.

## Don't
- Don't rely on mocks or stubs where realism matters; you re-encode your own possibly-wrong assumptions into them, so a mock verifying a negative debit "works" makes a passing test a tautology while the real code is broken.
- Don't verify interactions that are implementation details; a mock asserting `debit` or `credit` was called breaks when the code is refactored to a single `transfer`, whereas a fake checking the final balance survives.

## Checklist
- If you need a double, does a fake exist or could you write one for a dependency you own?
- Does the double enforce the real contract, or could it pass while the real code fails?
- Are you asserting on end state (fake) rather than on which internal calls were made (mock)?

## Notes
Mocks and stubs carry two failure modes Long demonstrates: unrealistic tests, where a mock configured to accept a negative debit hides that the real account rejects it, and tight coupling, where verifying `debit`/`credit` calls breaks on a refactor to `transfer`. A fake avoids both by faithfully implementing the contract and letting tests assert on resulting state. This is the classicist (Detroit) school over the mockist (London) school — real dependency first, then a fake, with mocks and stubs a last resort — which the author adopted after mock-heavy tests proved unrealistic and hard to refactor.
