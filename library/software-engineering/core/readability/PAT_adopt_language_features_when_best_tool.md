---
object_id: PAT_adopt_language_features_when_best_tool
object_type: pattern
name: Adopt a Language Feature Only When It Is the Best Tool
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- language_features
- readability
- judgment
- maintainability
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_readable
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u05, pp. 133-135
  evidence_type: text
confidence: high
references: []
variants: []
---

# Adopt a Language Feature Only When It Is the Best Tool

## Pattern Rule
**IF** you are tempted to use a new or shiny language feature
**THEN** use it only when it is genuinely the best tool for this job — it improves the code, and the engineers who will maintain it are familiar enough with it — not merely because it is new.

## Do
- Use a feature where it clearly improves the code: a Java stream with a filter replaces a verbose for-loop-and-new-list with succinct, readable code, and leans on a tested language construct rather than hand-rolled logic.
- Weigh team familiarity: if a small codebase's maintainers do not know streams, a marginal readability gain may not be worth the confusion they cause.
- Match the feature to the task — `map.get(key)` is the right tool for a map lookup, not a stream that filters every entry.

## Don't
- Don't reach for a feature just because it is shiny; be honest about whether it is really the best fit here.
- Don't misapply a versatile feature where a simpler call is clearer and faster — filtering a map's entry set to find one key is both less readable and less efficient than a direct lookup.

## Checklist
- Does the feature make this specific code more readable or robust?
- Are the people who will maintain this code familiar enough with the feature?
- Is there a simpler, more direct construct that fits the task better?

## Notes
Long's paired examples set the boundary: streams shine for filtering a list but are absurd for a map lookup that `map.get()` does directly and efficiently. The decision has two axes — does the feature improve this code, and is it familiar to the maintainers — and a genuine improvement can still be the wrong call if it is marginal and the team does not know the feature. Language designers add features for good reasons, but excitement is not a reason to use one.
