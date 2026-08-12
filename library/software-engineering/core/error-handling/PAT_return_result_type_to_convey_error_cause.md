---
object_id: PAT_return_result_type_to_convey_error_cause
object_type: pattern
name: Return a Result Type to Convey the Error's Cause
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
- result_type
- error_handling
- api_design
- factory_function
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_explicit_error_signaling_for_recoverable_errors
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u04, pp. 85-87
  evidence_type: text
confidence: high
references: []
variants: []
---

# Return a Result Type to Convey the Error's Cause

## Pattern Rule
**IF** a function can fail and the caller needs to know not just that a value could not be produced but why
**THEN** return a result type that holds either a value or an error, so the return type itself makes the possible error explicit and carries the failure detail.

## Do
- Build the type to hold exactly one of value or error: a private constructor plus static `ofValue()` and `ofError()` factories prevents an instance that has both or neither, and a `hasError()` gate tells the caller which it holds.
- Make the caller's usage clear — check `hasError()` first, then `getValue()` on success or `getError()` for the encapsulated detail, such as the erroneous number that caused the failure.
- Lean on built-in support where it exists — Swift, Rust, and F# provide result types with cleaner syntax and transform helpers like Rust's `and_then` — and take those as models for a hand-rolled version.

## Don't
- Don't reach for a result type when the caller needs no reason for the failure; a nullable return is simpler there, and the result type's benefit is the error detail.
- Don't assume a hand-rolled result type is self-explanatory; if a colleague does not know to call `hasError()` before `getValue()`, the safety is lost, so keep its usage conventional.

## Checklist
- Does the return type itself reveal that an error is possible?
- Can the value and error states never both be present or both absent?
- Does the caller get actionable detail about why the failure happened?

## Notes
The result type answers the one thing a bare null or optional cannot: the reason for failure. Long's worked `getSquareRoot` returns a `Result` of value-or-`NegativeNumberError`, the error object carrying the offending number for debugging and a UI message. The private-constructor-plus-factories construction is what guarantees the invariant of exactly-one-of, and pointing at the mature Rust and Swift implementations signals that real result types add ergonomic transform helpers on top of this core.
