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
- rel: related_to
  target_object_id: PAT_classify_error_recoverability_by_caller
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
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
- Match the reach of the exit to what you own, because the techniques above are not interchangeable in how far they go. Throwing leaves the current scope and runs destructors and cleanup handlers on the way out; a panic, an assertion, or a call that ends the process leaves every scope at once and runs none of them. Both are loud. Only the first is available to code that does not own the process it is running in.

## Don't
- Don't force callers to catch or declare an unrecoverable error up a long call chain — that is handling ceremony for something none of them can act on.
- Don't let an unrecoverable error fail quietly; a silent programming bug can corrupt data for months before anyone notices.
- Don't end the process from a component whose host has to survive it. A library, a container, a plugin, or anything else invoked by code you did not write is not entitled to decide that the program stops — that decision belongs to whoever owns the entry point. The consequence is severe and lands far from the cause: one bad index in one request takes down every other request in the process, no destructor or cleanup handler anywhere runs, buffered output is lost, and the component's error path can never be tested, because asserting on it takes the test runner with it.
- Don't read "unrecoverable here" as "unrecoverable anywhere." The scope you cannot recover in is usually much smaller than the program, and a component that cannot know its call sites is exactly the one with no standing to judge. `PAT_classify_error_recoverability_by_caller` owns that judgement and reaches the opposite answer for reusable code — where the two cards seem to disagree on a piece of code, it is because this one was read as licensing a process exit, which it does not.

## Checklist
- Is there genuinely no way for any caller to recover, making this a programming error?
- Does the failure make itself noticed — a crash, or logging with monitoring and alerting?
- Are you avoiding needless handling ceremony for an error nobody can act on?
- Does this code own the process it runs in? If it does not, does the technique chosen still leave the host standing?
- Does the technique run destructors and cleanup on the way out, or skip them?

## Notes
This is the deliberate mirror of the explicit-signaling advice: explicit for recoverable errors, implicit for unrecoverable ones. Long's reasoning is that when no caller can do anything useful, an explicit technique only clutters every layer with pass-through handling, so an unchecked exception, panic, check, or assertion — which fail loudly and unwind to the scope boundary — is the right tool. It combines fail-fast (surface at the source) with fail-loud (guarantee it is noticed) for the class of errors that are bugs to be fixed rather than conditions to be handled.

The phrase "exits the scope of irrecoverability" is carrying most of the rule and is the easiest thing here to read past, because the techniques listed beside it do not all reach the same distance. That scope is not a property of the error; it is a property of who owns the running program. For code at the entry point the scope of irrecoverability and the process are the same thing, and ending the process is the honest response. For a component invoked by callers it has never seen, the largest scope it is entitled to leave is the call — and reaching for a technique that ends the program is not a louder version of the same decision but a different decision, made on behalf of somebody who was never asked.

What makes this worth stating rather than leaving implicit is that the wrong version passes every other test on this card. It is loud, it is impossible to miss, it burdens no caller with handling ceremony, and it does not fail quietly. A reviewer checking this card's Do list and Don't list against a library that terminates on bad input will find nothing wrong, which is why the distinction has to be named here rather than left to be caught by the card that owns recoverability.
