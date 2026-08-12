---
object_id: PAT_fail_loudly_and_signal_unrecoverable_errors_implicitly
object_type: pattern
name: Fail Loudly and Signal Unrecoverable Errors Implicitly
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
- fail_loudly
- error_handling
- unchecked_exceptions
- robustness
cross_links:
- rel: related_to
  target_object_id: PAT_fail_fast_near_error_source
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u04, pp. 73-74, 92
  evidence_type: text
confidence: high
references: []
variants: []
---

# Fail Loudly and Signal Unrecoverable Errors Implicitly

## Pattern Rule
**IF** an error occurs that there is no realistic way to recover from — almost always a programming bug
**THEN** fail loudly with an implicit technique that exits the scope of irrecoverability — an unchecked exception, a panic, or a check/assertion — so engineers notice, without burdening every caller up the chain with handling it.

## Do
- Make it impossible to miss: crash by throwing, or where crashing is too blunt, log-and-monitor-and-alert so the error still reaches the team.
- Prefer an implicit technique here precisely because there is nothing sensible a caller could do but pass the error on; forcing acknowledgment at every layer would be noise.
- Rely on the loud exit producing a stack trace or line number that points engineers at where the error occurred.

## Don't
- Don't force callers to catch or declare an unrecoverable error up a long call chain — that is handling ceremony for something none of them can act on.
- Don't let an unrecoverable error fail quietly; a silent programming bug can corrupt data for months before anyone notices.

## Checklist
- Is there genuinely no way for any caller to recover, making this a programming error?
- Does the failure make itself noticed — a crash, or logging with monitoring and alerting?
- Are you avoiding needless handling ceremony for an error nobody can act on?

## Notes
This is the deliberate mirror of the explicit-signaling advice: explicit for recoverable errors, implicit for unrecoverable ones. Long's reasoning is that when no caller can do anything useful, an explicit technique only clutters every layer with pass-through handling, so an unchecked exception, panic, check, or assertion — which fail loudly and unwind to the scope boundary — is the right tool. It combines fail-fast (surface at the source) with fail-loud (guarantee it is noticed) for the class of errors that are bugs to be fixed rather than conditions to be handled.
