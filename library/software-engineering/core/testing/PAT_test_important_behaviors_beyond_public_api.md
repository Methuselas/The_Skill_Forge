---
object_id: PAT_test_important_behaviors_beyond_public_api
object_type: pattern
name: Test Every Important Behavior, Even Beyond the Public API
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
- public_api
- side_effects
- important_behaviors
cross_links:
- rel: related_to
  target_object_id: PAT_keep_tests_agnostic_to_implementation
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u10, pp. 274-278
  evidence_type: text
confidence: high
references: []
variants: []
---

# Test Every Important Behavior, Even Beyond the Public API

## Pattern Rule
**IF** an important behavior cannot be triggered or verified through what you consider the public API — it needs a dependency set up, or produces a side effect to check
**THEN** still test it, straying beyond the public API to set up dependencies and verify side effects, but only when there is genuinely no alternative.

## Do
- Set up the non-public dependencies a behavior needs: just as testing a vending machine requires plugging it in, filling water, and adding beans, testing code may require configuring or simulating a server or database.
- Verify important side effects that customers never see but that matter — a smart machine notifying a technician when beans run low, or code not re-calling a server on repeat requests.
- Separate the behavior you care about from the mechanism: test that repeat requests are not sent, not that a cache exists, since the cache is a means to that end.

## Don't
- Don't cite "test only the public API" as an excuse to leave an important behavior untested just because it sits outside a narrow API definition.
- Don't drift into testing implementation details while reaching for these behaviors; leave the public API only when no alternative exists, and never assert on how (the water heater) instead of what (the coffee).

## Checklist
- Is any important behavior currently untested because it is awkward to reach through the public API?
- When you verify a side effect, are you checking the outcome that matters, not the mechanism?
- Have you strayed from the public API only where there was truly no alternative?

## Notes
"Test only the public API" is a strong default but a subjective one, and Long has seen it misused to justify skipping real behaviors. The vending-machine analogy separates three categories — public-API interactions, non-public setup and side effects that still need testing, and pure implementation details that do not. The `AddressBook` example lands it: the caching is an implementation detail, but "does not re-hit the server on repeats" is an important behavior worth testing even though it lives outside the lookup API.
