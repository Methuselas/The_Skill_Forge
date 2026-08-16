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

## Do
- See through each disguise: returning `0.0` for a failed balance lookup makes an error indistinguishable from a genuine zero balance; returning an empty invoice list on a store failure tells an auditor the customer owes nothing.
- Recognize "doing nothing" as hiding too: an `addItem()` that silently returns on a currency mismatch leaves the caller believing the item was added.
- If you must catch, still surface it — an exception caught and only logged is barely better, because the caller still assumes the email was sent when it was not.

## Don't
- Don't return a default or empty value for an error case; defaults break fail-fast and fail-loud by letting the system carry on with wrong data that manifests weirdly later.
- Don't log sensitive data while "handling" an error — an exception may carry a user's email address subject to data-handling policies.

## Checklist
- Can a caller distinguish this return value from a legitimate normal result?
- If the operation failed, does the caller find out, or assume it succeeded?
- Does any catch block swallow or merely log an error the caller needed to know about?

## Notes
Long walks through the disguises one by one — default value, empty list (a null-object variant), doing nothing, suppressing an exception, catching and only logging — and shows each produces a caller that proceeds as if all is well: unpaid invoices vanish, balances read zero, emails silently fail. Hiding errors has real-world consequences, and the fix is always to signal. The default-value and null-object forms get fuller treatment as magic values in chapter 6; here the durable rule is simply that an error must never be dressed up as a success.
