---
object_id: PAT_make_callers_aware_of_recoverable_errors
object_type: pattern
name: Make Callers Aware of Errors They Might Want to Recover From
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
- avoid_surprises
- api_design
- abstraction
cross_links:
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
- rel: related_to
  target_object_id: PAT_prefer_explicit_error_signaling_for_recoverable_errors
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Make Callers Aware of Errors They Might Want to Recover From

## Pattern Rule
**IF** your code can produce an error a caller might want to recover from
**THEN** actively ensure the caller is made aware the error can happen, rather than leaving its possibility hidden — because the whole point of your abstraction is that callers are not experts in the problem it solves.

## Do
- Assume callers may not even know the error concept exists: a caller of `PhoneNumber.parse()` is shielded from the rules of phone-number validity, so they may not realize an "invalid number" error is possible or expect validation to happen there.
- Surface the possibility where the caller cannot miss it, which in practice means choosing an explicit signaling technique so the error sits in the unmistakable part of the contract.

## Don't
- Don't rely on the caller inferring that an error can occur; a shielded caller has no way to know beforehand that a specific call will fail.
- Don't leave the error unsurfaced and assume someone will write handling for it — unhandled surprises become user-visible bugs or failures in business-critical logic.

## Checklist
- Would a caller reading only your function's signature know this error can occur?
- Is the error's possibility carried by the contract, not just implied by the implementation?
- Have you assumed the caller shares your expertise in the problem being solved?

## Notes
This is the bridge between recoverability and signaling. Long stresses that an abstraction deliberately hides complexity, which means a caller often will not anticipate the very error the abstraction can raise. The author's obligation is therefore to make the error's possibility visible — the concrete "how" is the explicit-signaling decision in the following sections, and the failure it prevents is exactly the surprise the avoid-surprises pillar warns against.
