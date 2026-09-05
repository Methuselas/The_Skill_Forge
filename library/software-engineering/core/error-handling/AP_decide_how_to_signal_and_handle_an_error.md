---
object_id: AP_decide_how_to_signal_and_handle_an_error
object_type: ap
name: Decide How to Signal and Handle an Error
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
- error_handling
- recoverability
- api_design
- decision_process
cross_links:
- rel: supports
  target_object_id: PAT_classify_error_recoverability_by_caller
- rel: supports
  target_object_id: PAT_prefer_explicit_error_signaling_for_recoverable_errors
- rel: supports
  target_object_id: PAT_dont_hide_errors
- rel: supports
  target_object_id: PAT_fail_fast_near_error_source
- rel: supports
  target_object_id: PAT_fail_loudly_and_signal_unrecoverable_errors_implicitly
- rel: supports
  target_object_id: PAT_match_failure_to_scope_of_recoverability
- rel: supports
  target_object_id: PAT_make_callers_aware_of_recoverable_errors
- rel: supports
  target_object_id: PAT_treat_compiler_warnings_as_potential_bugs
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Decide How to Signal and Handle an Error

## Objective
Given a specific error that a piece of code can raise, arrive at a signaling and handling choice that surfaces the error to whoever can act on it and never hides it.

## Steps / Flow
1. **Judge recoverability from the call sites.** Determine whether the error is recoverable — usually caller-dependent, so default to "a caller might want to recover" whenever you cannot see every call site or the code might be reused, reserving "unrecoverable" for obvious programming errors the caller could cheaply prevent. That judgement is `PAT_classify_error_recoverability_by_caller`.
2. **Fail fast either way.** Signal the error as near its real source as possible so it surfaces with a usable stack trace and cannot propagate bad state into a distant, dangerous failure. `PAT_fail_fast_near_error_source` owns how near the source is near enough.
3. **For an unrecoverable error, fail loudly and implicitly.** Use an unchecked exception, panic, check, or assertion that exits the scope of irrecoverability, and make sure it is noticed by crashing or by logging with monitoring and alerting, without burdening every caller with handling it. `PAT_fail_loudly_and_signal_unrecoverable_errors_implicitly` owns this branch.
4. **For a recoverable error, signal explicitly.** Put the error in the unmistakable contract with a checked exception, a nullable or optional return, a result type when the caller needs the reason, or an outcome type enforced so ignoring it warns at compile time; make the caller aware the error can happen. `PAT_prefer_explicit_error_signaling_for_recoverable_errors` owns the signalling choice, and `PAT_make_callers_aware_of_recoverable_errors` owns what the caller is told.
5. **Set the isolation scope.** If a wider scope can absorb the failure, catch at that boundary rather than crashing the whole program — but only in high-level or genuinely independent code, and always with logging, monitoring, and alerting. The scope decision is `PAT_match_failure_to_scope_of_recoverability`.
6. **Never hide the error, and heed the compiler.** Reject default values, empty collections, silent returns, and swallowed exceptions; and treat any compiler warning the change raises as a possible bug to fix or explicitly suppress with a reason. `PAT_dont_hide_errors` and `PAT_treat_compiler_warnings_as_potential_bugs` own the two halves of this.

## Notes
This threads the separate decisions into one pass: recoverability first, because it drives everything; fail-fast always; then the explicit-for-recoverable, implicit-for-unrecoverable split; scope isolation for robustness; and the two backstops — never hide, and respect warnings. Long is candid that the recoverable-error choice is contested and that the most important thing is a team-wide agreed philosophy, so step 4 should follow whatever convention the team has settled on. The individual techniques and the don't-hide rule are their own patterns; this procedure is the order in which to apply them.
