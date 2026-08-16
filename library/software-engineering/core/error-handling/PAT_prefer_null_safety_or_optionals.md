---
object_id: PAT_prefer_null_safety_or_optionals
object_type: pattern
name: Signal Absent Values With Null Safety or Optionals
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
- null_safety
- optionals
- types
- error_prevention
cross_links: []
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_error_signal
  variant_name: Nullable Return as an Explicit Error Signal
  variant_basis: context
  difference_from_foundation: Applies the nullable/optional return specifically to signal that a function could not produce a result (an error), not merely that a value is optional. Under null safety this is an explicit signal because the caller is forced to handle the null before use.
  when_to_use: When a function can fail but the caller does not need to know why — the mere fact that no value could be produced is enough, as in a square-root function returning null for a negative input.
  when_not_to_use: When the caller needs the reason for the failure; null carries no error detail, so reach for a result type instead. Also weak where the language lacks null safety and the return can be silently dereferenced.
  absorbed_from_object_id: none
---

# Signal Absent Values With Null Safety or Optionals

## Pattern Rule
**IF** a variable, parameter, or return value can legitimately be absent
**THEN** make the absence explicit and compiler-enforced — mark the type nullable under a null-safety regime so it cannot be used without a null check, or use an optional type where the language lacks null safety.

## Do
- Default everything to non-nullable and opt specific things into nullability: under the book's convention a `?` suffix (`Element?`) marks a type that can be null and the compiler blocks use until it is checked.
- Where null safety is unavailable, reach for an optional type (`Optional`, Rust's `Option`, C++'s equivalent) and return `Optional.empty()` instead of a bare null.
- Turn on null safety if your language supports or can retrofit it (newer languages by default, opt-in in recent C#, retrofittable in Java).

## Don't
- Don't return a bare, unmarked null that callers can dereference without checking — that is the road to `NullPointerException`, `NullReferenceException`, and "cannot read property of null."
- Don't over-correct into banning absence entirely; forbidding all nulls forces awkward code gymnastics when absence is a real, useful concept.

## Checklist
- Is every value that can be absent marked so the compiler forces a check before use?
- Where null safety is absent, is an optional type used instead of a raw null?
- Have you avoided both unchecked nulls and a blanket no-nulls rule?

## Notes
This establishes the book's pseudocode convention and a durable typing habit. Long frames nulls as straddling a dichotomy — genuinely useful for representing absence, genuinely dangerous because engineers forget to check them — and resolves it with compiler-enforced null safety or optionals rather than either raw nulls or an absolutist ban. It is the foundation that later error-signaling techniques, such as nullable and optional return types, build on when a function may be unable to produce a result.

The absorbed variant (VAR_error_signal) applies the same nullable/optional return as an explicit error signal: when a function cannot produce a result, returning null under null safety forces the caller to acknowledge the failure before using the value, which makes it an explicit technique. Its limit is that null conveys no reason for the failure, so a result type is preferable when the caller needs error detail — Long shows this with a square-root function that returns null for a negative input and needs a comment to explain what the null means.
