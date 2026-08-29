---
object_id: PAT_fail_fast_near_error_source
object_type: pattern
name: Fail Fast So Errors Surface Near Their Source
library_path:
- software-engineering
- core
- error-handling
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- fail_fast
- error_handling
- debugging
- robustness
cross_links:
- rel: related_to
  target_object_id: PAT_enforce_contracts_at_runtime_with_checks
- rel: related_to
  target_object_id: AP_decide_how_to_signal_and_handle_an_error
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Fail Fast So Errors Surface Near Their Source

## Pattern Rule
**IF** an error condition is detected, such as a function receiving an invalid argument
**THEN** signal it immediately, as close to the real source as possible, rather than letting execution carry on until the bad state causes a failure somewhere far away later.

## Do
- Throw at the entry point: reject an invalid input the moment the function is called, so a stack trace points at the exact line, instead of surfacing three classes away with no trail back.
- Value fast failure for both error classes — it gives a recoverable error the best chance of graceful recovery and an unrecoverable one the best chance of quick diagnosis.

## Don't
- Don't let code limp on past a detected error; a delayed failure can mean saving corrupted data to a database and only noticing months later, after real data is destroyed.
- Don't scatter invalid data forward through several callers, forcing an engineer to work backward across the codebase to find where it actually went wrong.

## Checklist
- Does an invalid input fail at the function boundary, not deep in downstream logic?
- Would a stack trace from the failure point at or near the true source?
- Can bad state propagate silently before anything complains?

## Notes
The truffle-dog analogy anchors it: a dog that barks the instant it finds a truffle is far more useful than one that wanders ten meters first, just as code that barks at the real source of a bug beats code that barks somewhere distant. Long pairs fail-fast (surface near the source) with fail-loud (make sure it is noticed); this pattern is the location half, and it is the same instinct behind runtime contract checks that reject bad inputs up front.
