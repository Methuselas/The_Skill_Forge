---
object_id: PAT_beware_assumptions_avoid_or_enforce
object_type: pattern
name: Avoid Unnecessary Assumptions and Enforce Necessary Ones
library_path:
- software-engineering
- core
- reusability
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- assumptions
- reusability
- checks
- fail_fast
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_reusable_and_generalizable
- rel: related_to
  target_object_id: PAT_enforce_contracts_at_runtime_with_checks
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Avoid Unnecessary Assumptions and Enforce Necessary Ones

## Pattern Rule
**IF** a piece of code bakes in an assumption about its inputs or data
**THEN** remove the assumption where it is unnecessary, and where it is genuinely required, enforce it and name the code so callers opt in knowingly.

## Do
- Drop an assumption that only saves a little work: a `getAllImages` that assumes exactly one image section becomes more reusable by scanning all sections, at the cost of a few extra loop iterations.
- When an assumption is necessary for a use case, enforce it with a check or assertion so a broken assumption fails fast rather than silently returning a wrong result.
- Signal the assumption in the name: rename `getImageSection` to `getOnlyImageSection`, so callers who do not want that assumption avoid the function.

## Don't
- Don't leave an assumption unenforced and only mentioned in a comment; a caller reusing the code will not notice, and a violation passes silently instead of failing.
- Don't reflexively assert; if the data comes from a user or an external system, a broken assumption is recoverable, so use an explicit error-signaling technique rather than a crash.

## Checklist
- Is this assumption actually needed, or can the code handle the general case cheaply?
- If needed, is it enforced so a violation fails fast, and named so callers opt in?
- Given the data's source, is an assertion or an explicit error the right enforcement?

## Notes
Assumptions are a hidden reuse tax: they make code fragile in exactly the situations a future caller will hit. Long's article example shows the ladder — remove the one-image-section assumption when you can, and when a single-section template genuinely requires it, enforce it with an assertion and rename to `getOnlyImageSection`. The enforcement choice tracks recoverability from chapter 4: an assertion for an internally generated article (a programming error), an explicit signal when the article comes from outside and a caller may want to recover.
