---
object_id: PAT_match_failure_to_scope_of_recoverability
object_type: pattern
name: Isolate Failures at the Right Scope of Recoverability
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
- robustness
- monitoring
- architecture
cross_links:
- rel: related_to
  target_object_id: PAT_fail_loudly_and_signal_unrecoverable_errors_implicitly
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Isolate Failures at the Right Scope of Recoverability

## Pattern Rule
**IF** an error is unrecoverable within a narrow scope but the program has a wider scope that can absorb it — such as a server handling independent requests
**THEN** catch it at that isolating boundary instead of crashing the whole program, but log the details, monitor error rates, and alert engineers so the failure is still noticed.

## Do
- Place the catch where the scopes divide: a single bad request can fail its own handler without taking down the server, because requests are independent events.
- Resolve the robustness-versus-loudness dichotomy with logging plus monitoring plus alerting, so you get both a running program and errors that do not vanish.
- Reserve catch-all-and-log for a handful of places — very high-level entry points or genuinely independent, noncritical branches.

## Don't
- Don't apply broad catch-and-log in low-level, critical, or non-independent code; there it hides errors and lets the software carry on doing the wrong thing.
- Don't treat "caught so it didn't crash" as done — an error caught but never logged, monitored, or alerted on is an error nobody will ever fix.

## Checklist
- Is the catch boundary at a scope that can genuinely continue without this unit?
- Are caught errors logged with enough detail to debug, and is their rate monitored and alerted?
- Is this catch-all confined to high-level or independent code rather than critical low-level logic?

## Notes
Long's server example shows recoverability as a property of scope: a programming error may be unrecoverable for one request yet recoverable for the server as a whole, so crashing everything would be wrong. The resolution to the robustness/loudness tension is not silence but observability — log, monitor, alert. He cautions that this catch-all technique belongs in very few places; used carelessly it becomes exactly the error-hiding the next pattern warns against. Server frameworks usually provide this request isolation, so you rarely write the try/catch yourself.
