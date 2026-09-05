---
object_id: PAT_dont_hide_errors
object_type: pattern
name: Don't Hide Errors Behind Default or Silent Results
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
- avoid_surprises
- magic_values
- robustness
cross_links:
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
- rel: related_to
  target_object_id: AP_decide_how_to_signal_and_handle_an_error
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Don't Hide Errors Behind Default or Silent Results

## Pattern Rule
**IF** you are tempted to swallow an error to keep the code simple — return a default value, an empty collection, do nothing, or catch-and-ignore
**THEN** don't; signal the error instead, because hiding it denies recoverable handling, conceals programming bugs, and leaves the caller assuming success while the software limps into corruption.
**ELSE** discard it deliberately and visibly in the two cases where signalling costs more than it buys — the call cannot fail by its own documented contract, or the failure happened while unwinding an operation that has already failed — and in the second case make sure the original failure is what still reaches the caller.

## Do
- See through each disguise: returning `0.0` for a failed balance lookup makes an error indistinguishable from a genuine zero balance; returning an empty invoice list on a store failure tells an auditor the customer owes nothing.
- Recognize "doing nothing" as hiding too: an `addItem()` that silently returns on a currency mismatch leaves the caller believing the item was added.
- If you must catch, still surface it — an exception caught and only logged is barely better, because the caller still assumes the email was sent when it was not.
- Where an interface reports a failure it documents as impossible, discard it in a form a reader can see, and let the documented contract be the reason. Some interfaces carry a failure channel because a general shape demanded one, not because this implementation can use it. Writing a handler there adds a branch that cannot run, that no test can reach, and that every later reader has to evaluate before dismissing — while a visible discard says the contract was read and the conclusion was drawn.
- Where the failure arrives during cleanup of an operation that has already failed, keep the first failure and do not let the second replace it. Unwinding runs precisely when things have gone wrong, so its own failures are both likely and less informative — the rollback that could not complete is a consequence of the condition the caller actually needs to hear about. Report the cleanup failure somewhere it can be read later if it matters, and return the original.
- Distinguish these two from the disguises above by asking who benefits. Every case in the Don't list withholds something the caller needed; these two withhold something no caller can use, or protect something the caller needs from being buried by it.

## Don't
- Don't return a default or empty value for an error case; defaults break fail-fast and fail-loud by letting the system carry on with wrong data that manifests weirdly later.
- Don't log sensitive data while "handling" an error — an exception may carry a user's email address subject to data-handling policies.

## Checklist
- Can a caller distinguish this return value from a legitimate normal result?
- If the operation failed, does the caller find out, or assume it succeeded?
- Does any catch block swallow or merely log an error the caller needed to know about?
- If this failure is being discarded, is it because the contract says it cannot happen,
  or because handling it looked inconvenient?
- On a cleanup path, does the failure that started the unwinding still reach the caller
  unchanged, rather than being replaced by one raised while cleaning up?

## Notes
The rule is written absolutely because the failure it addresses is a failure of nerve, and
qualifying it invites the reader to find themselves in the exception. The two cases below
are worth stating anyway, because a reader who has met them and found the card silent
concludes the card was written by somebody who had not, and discounts the rest of it.

Neither case is a weakening. The test that separates them from every disguise above is
whether a caller loses information. Returning zero for a failed lookup, an empty list for
an unavailable store, or nothing at all for a rejected item each withhold something the
caller needed and had no other way to learn. A failure that its own interface documents as
impossible carries nothing to withhold, and handling it produces a branch no test can
reach and every reader must still read. A failure raised while unwinding a failed operation
is the more important of the two, because there the mistake runs the other way: the second
failure arrives later, so it is the one that survives if you let it, and the caller ends up
holding a report about a rollback instead of the condition that made rollback necessary.
Signalling it faithfully is what hides the thing that mattered. The discipline is to record
the second where it can be recovered and let the first be the answer.

Long walks through the disguises one by one — default value, empty list (a null-object variant), doing nothing, suppressing an exception, catching and only logging — and shows each produces a caller that proceeds as if all is well: unpaid invoices vanish, balances read zero, emails silently fail. Hiding errors has real-world consequences, and the fix is always to signal. The default-value and null-object forms get fuller treatment as magic values elsewhere; here the durable rule is simply that an error must never be dressed up as a success.
