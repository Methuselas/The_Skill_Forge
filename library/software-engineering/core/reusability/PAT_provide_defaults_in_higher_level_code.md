---
object_id: PAT_provide_defaults_in_higher_level_code
object_type: pattern
name: Provide Default Values in Higher-Level Code
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
- default_values
- reusability
- layers_of_abstraction
- dependency_injection
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_reusable_and_generalizable
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u09, pp. 252-257
  evidence_type: text
confidence: high
references: []
variants: []
---

# Provide Default Values in Higher-Level Code

## Pattern Rule
**IF** a low-level component could substitute a default when a value is absent
**THEN** have it report the absence (return null or an optional) and let higher-level code supply the default, rather than baking the default into the low-level code.

## Do
- Return absence from the low level: a settings class with no user-chosen font should return null, not silently return Arial.
- Make defaulting its own subproblem solved higher up: a dedicated defaults provider plus a settings layer that chooses between the user value and the default keeps that decision reconfigurable, ideally via dependency injection.
- Use the language's null-coalescing operator where available to keep the "user value or default" choice concise.

## Don't
- Don't hard-code a default deep in low-level code; every layer above then inherits the assumption that this default is sensible, and the lower the level, the more code that assumption constrains.
- Don't force one default on all callers when different reuses of the code may need different defaults.

## Checklist
- Does a low-level component decide a default that higher layers should own?
- Is absence reported upward so callers can each choose their own default?
- Is the defaulting logic reconfigurable rather than fixed at the lowest level?

## Notes
A default value is an assumption about every layer above, and the deeper it sits, the more code it silently binds. Long's `UserDocumentSettings` returning Arial is the trap: reusing that code inherits Arial whether it suits or not. Returning null and lifting the default into a `DocumentSettings` layer (with the provider injected) turns defaulting into a distinct, reconfigurable subproblem, so each caller picks its own — the reusability-focused counterpart to the earlier warnings against default and magic return values.
