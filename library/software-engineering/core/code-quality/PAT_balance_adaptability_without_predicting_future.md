---
object_id: PAT_balance_adaptability_without_predicting_future
object_type: pattern
name: Make Code Adaptable Without Predicting Specific Changes
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- adaptability
- code_quality
- over_engineering
- requirements_change
cross_links: []
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u01, pp. 9-10
  evidence_type: text
confidence: high
references: []
variants: []
---

# Make Code Adaptable Without Predicting Specific Changes

## Pattern Rule
**IF** you know a piece of code's requirements will change but not exactly how, and you must decide how much adaptability to build in
**THEN** aim for a point between two failure extremes — apply generally-applicable adaptability techniques that do not require knowing the specific future change.
**ELSE** for a small, run-once-then-throw-away utility, put no effort into adaptability at all.

## Do
- Recognize the cost of over-preparing (scenario A): days or weeks mapping speculative futures, deliberating every minutia, shipping a year late, and usually guessing the future wrong anyway.
- Recognize the cost of under-preparing (scenario B): brittle assumptions baked in everywhere and subproblems bundled into inseparable chunks, so a small requirement change forces throwing everything away and rewriting.
- Choose where on the spectrum to sit based on the specific project and the culture of the organization — there is no single optimal point.

## Don't
- Don't try to predict exactly how requirements will evolve and pre-engineer support for every branch you imagine.
- Don't swing the other way and ignore that requirements *will* evolve just because you cannot predict how.

## Checklist
- Are subproblems kept separable, or bundled into one inseparable chunk?
- Would a small but likely requirement change force a rewrite rather than a local edit?
- Did you add adaptability machinery for a specific future nobody has asked for?

## Notes
Long presents two extreme scenarios — exhaustively engineering for predicted change versus ignoring change entirely — and shows both lose to a competitor, one by shipping a year late and one by needing repeated three-month rewrites. The durable lesson is that adaptability is achievable without prophecy: general techniques (developed through the rest of the book) keep code flexible without committing to guesses about which change will actually arrive.
