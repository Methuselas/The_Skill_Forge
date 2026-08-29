---
object_id: PAT_classify_error_recoverability_by_caller
object_type: pattern
name: Classify Error Recoverability From the Caller's Position
library_path:
- software-engineering
- core
- error-handling
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- error_handling
- recoverability
- api_design
- abstraction
cross_links:
- rel: related_to
  target_object_id: PAT_make_callers_aware_of_recoverable_errors
- rel: prerequisite_for
  target_object_id: PAT_make_callers_aware_of_recoverable_errors
- rel: prerequisite_for
  target_object_id: PAT_fail_fast_near_error_source
- rel: prerequisite_for
  target_object_id: PAT_match_failure_to_scope_of_recoverability
- rel: prerequisite_for
  target_object_id: PAT_dont_hide_errors
- rel: prerequisite_for
  target_object_id: PAT_prefer_explicit_error_signaling_for_recoverable_errors
- rel: prerequisite_for
  target_object_id: PAT_fail_loudly_and_signal_unrecoverable_errors_implicitly
- rel: prerequisite_for
  target_object_id: PAT_return_result_type_to_convey_error_cause
- rel: prerequisite_for
  target_object_id: PAT_return_outcome_and_enforce_return_check
- rel: prerequisite_for
  target_object_id: PAT_signal_async_errors_with_promise_of_result
- rel: prerequisite_for
  target_object_id: PAT_prefer_null_safety_or_optionals
- rel: prerequisite_for
  target_object_id: PAT_treat_compiler_warnings_as_potential_bugs
- rel: related_to
  target_object_id: AP_decide_how_to_signal_and_handle_an_error
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Classify Error Recoverability From the Caller's Position

## Pattern Rule
**IF** an error can occur in a function and you must decide whether to treat it as recoverable or fatal
**THEN** recognize the answer is context-dependent and usually only the caller knows, so as the function's author assume an error caused by supplied input is one a caller may want to recover from — unless the contract makes the input obviously invalid and trivially checkable before the call.

## Do
- Distinguish the two classes: errors from something external (invalid user input, network down, corrupt file) are usually recoverable by the system as a whole; errors from a programming mistake (missing bundled resource, invalid hard-coded argument, missing initialization) usually are not.
- Read recoverability off the call site: `PhoneNumber.parse("01234typo56789")` with a hard-coded literal is an unrecoverable programming error, while `PhoneNumber.parse(userInput)` is recoverable and deserves a friendly UI message.
- Default to "caller might want to recover" whenever you lack complete knowledge of every call site, or there is any chance the code will be reused later.

## Don't
- Don't assume an input error is a fatal programming error just because it is obvious to you; the invalidity may be buried in small print the caller never read.
- Don't decide recoverability at the low level where the error is detected — that layer is often not the one that knows how it should be handled.

## Checklist
- Could this error arise from external input rather than a programming mistake?
- Do you actually know every caller and the origin of every value they pass?
- If reused tomorrow, would your recoverable/unrecoverable assumption still hold?

## Notes
Long's phone-number example makes recoverability a property of context rather than of the error itself: the same `parse` failure is fatal from a hard-coded typo and recoverable from user input. Because a function author rarely controls all callers, the safe default is to treat input-caused errors as potentially recoverable and signal them, reserving "unrecoverable" for cases where the contract makes the invalidity obvious and the caller can cheaply check it first — a negative list index being the archetype.
