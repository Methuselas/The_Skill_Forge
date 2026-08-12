---
object_id: PAT_make_critical_inputs_required
object_type: pattern
name: Make Critical Inputs Required Rather Than Silently No-Op
library_path:
- software-engineering
- core
- avoiding-surprises
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- avoid_surprises
- api_design
- hard_to_misuse
- required_parameters
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_hard_to_misuse
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u06, pp. 158-162
  evidence_type: text
confidence: high
references: []
variants: []
---

# Make Critical Inputs Required Rather Than Silently No-Op

## Pattern Rule
**IF** a parameter is critical — the function cannot do what its name promises without it
**THEN** make it required (non-nullable) so the function is impossible to call without it, rather than accepting a null and silently doing nothing when it is absent.

## Do
- Take the critical value as non-nullable: a `displayLegalDisclaimer(String legalText)` that cannot accept null is guaranteed to actually display a disclaimer whenever it is called.
- Push the absent-value decision to the caller, who then must confront it — `ensureLegalCompliance` has to check for a missing translation and signal failure, returning a checked Boolean instead of pretending compliance.

## Don't
- Don't accept a nullable critical parameter and return early when it is null; a `displayLegalDisclaimer(null)` that quietly does nothing makes callers believe the disclaimer always shows, risking legal non-compliance.
- Don't trade the caller's clarity for a few saved lines; sparing callers a null check by absorbing it invisibly is a bad bargain when it hides a critical no-op.

## Checklist
- Can the function fulfill its named promise without this parameter?
- If the parameter is absent, does the function silently do nothing?
- Are callers forced to handle the missing-value case rather than being misled?

## Notes
This is a misleading-function failure: the unmistakable contract (the name) says one thing while a nullable-and-no-op body does another. Long's legal-disclaimer example shows the stakes — a signup flow that "always" shows a disclaimer sometimes shows nothing, breaking the law, because a null translation makes the call a no-op. Making the critical input required moves the absent-value handling into the open at the call site, echoing chapter 5's point that a few extra caller lines are cheap against a surprising bug.
