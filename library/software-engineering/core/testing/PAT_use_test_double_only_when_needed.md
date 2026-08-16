---
object_id: PAT_use_test_double_only_when_needed
object_type: pattern
name: Use a Test Double Only When a Real Dependency Won't Do
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
- test_doubles
- dependencies
- determinism
cross_links:
- rel: related_to
  target_object_id: PAT_use_dependency_injection
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Use a Test Double Only When a Real Dependency Won't Do

## Pattern Rule
**IF** you are deciding whether to use a real dependency or a test double in a test
**THEN** prefer the real dependency, and reach for a test double only when the real one is genuinely infeasible — painful to set up, causes real-world side effects, or behaves indeterministically.

## Do
- Substitute a double when a dependency drags in a mountain of sub-dependency setup that would couple the test to implementation details and make it fragile.
- Substitute a double to protect the outside world when the real dependency has real consequences — testing a payment against a real bank account would move real money.
- Substitute a double to protect the test from the outside world when a real dependency is indeterministic, such as a bank balance that drifts with interest and fees and would make the test flaky.

## Don't
- Don't reach for a double by default; injecting a double always risks a test that diverges from real behavior, so use one only where the real dependency cannot be.
- Don't assume a double is always simpler — configuring one can sometimes be more work than using the real thing, so weigh it case by case.

## Checklist
- Is there a concrete reason the real dependency cannot be used here?
- Does the dependency cause real-world side effects or behave nondeterministically?
- Would using the real dependency keep the test more realistic at acceptable cost?

## Notes
Dependency injection is what makes this choice possible — a dependency supplied from outside can be a real one or a double. Long frames three legitimate reasons to substitute a double: simplifying an unwieldy setup, protecting real systems from the test, and protecting the test from a flaky outside world. The default remains the real dependency; the next pattern covers which kind of double to choose when one is warranted.
