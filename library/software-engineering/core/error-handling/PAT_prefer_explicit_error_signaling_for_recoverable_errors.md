---
object_id: PAT_prefer_explicit_error_signaling_for_recoverable_errors
object_type: pattern
name: Prefer Explicit Signaling for Recoverable Errors
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
- checked_exceptions
- api_design
- team_conventions
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_unmistakable_over_small_print
- rel: related_to
  target_object_id: PAT_return_result_type_to_convey_error_cause
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u04, pp. 79-98
  evidence_type: text
confidence: high
references: []
variants: []
---

# Prefer Explicit Signaling for Recoverable Errors

## Pattern Rule
**IF** an error is one a caller might want to recover from
**THEN** signal it with an explicit technique — a checked exception, a nullable or optional return under null safety, a result type, or an enforced outcome type — so the error sits in the unmistakable part of the contract, rather than an implicit technique the caller can be oblivious to.

## Do
- Sort techniques by contract visibility: explicit ones (checked exception, nullable/optional/result/outcome return) force awareness; implicit ones (unchecked exception, magic value, promise/future) leave the caller free to miss the error.
- Favor explicit because doing the wrong thing then requires active effort and shows up as a blatant transgression a reviewer can catch, whereas with an unchecked exception the wrong thing — no handling — happens silently by default.
- Weigh the honest counterarguments: unchecked exceptions can concentrate handling in a few high layers and spare intermediate code, and heavy explicit handling can tempt engineers to cut corners like hiding an `IOException`.
- Above all, agree a single philosophy across the team; mixed error-handling conventions across interacting code are worse than either choice alone.

## Don't
- Don't rely on undocumented unchecked exceptions for recoverable errors; they rarely get documented, turning "which can this throw?" into a whack-a-mole that ends in a catch-all that hides real bugs.
- Don't reach for `catch (Exception)` to end the whack-a-mole; it buries unrecoverable programming errors and makes the software fail silently and weirdly.

## Checklist
- Is the error a caller could act on carried by an explicit, contract-visible channel?
- If someone fails to handle it, is that omission blatant in review rather than invisible?
- Has the team agreed one error-signaling philosophy that this code follows?

## Notes
This is the chapter's central and admittedly divisive decision, and Long's stated opinion: use explicit techniques for recoverable errors. The `TemperatureLogger`/`DiskDataStore` example shows both sides — a checked `IOException` forces a visible change at every call site (which tempts hiding), while an unchecked one lets an unhandled error slip past a reviewer unnoticed. His decisive argument is that explicit signaling makes the wrong thing require effort and become obvious, and undocumented unchecked exceptions cause the outages he has seen; the standard-exception-type tactic mitigates whack-a-mole but blurs distinct error causes. The specific explicit techniques — result, outcome, nullable — are their own patterns; this one governs the choice between the explicit and implicit families.
