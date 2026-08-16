---
object_id: PAT_return_outcome_and_enforce_return_check
object_type: pattern
name: Return an Outcome and Enforce That Callers Check It
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
- outcome_type
- error_handling
- compiler_enforcement
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_explicit_error_signaling_for_recoverable_errors
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Return an Outcome and Enforce That Callers Check It

## Pattern Rule
**IF** a function performs an action rather than producing a value, and that action can fail
**THEN** return an outcome value indicating success or failure, and mark the function so that ignoring the return value produces a compiler warning — otherwise the outcome is too easy to overlook.

## Do
- Choose the outcome shape to fit: a Boolean when there are two states, an enum when there are more than two or when true/false would be unclear, a whole class when detailed information is needed.
- Enforce the check with the language's mechanism — `@CheckReturnValue` in Java, `MustUseReturnValue` in C#, `[[nodiscard]]` in C++ — so a caller who drops the return gets a warning at compile time.
- Handle it at the call site with a plain if-else that branches on success and failure, as with `sendMessage()` returning true when sent and false when the channel is closed.

## Don't
- Don't ship an unmarked outcome return; a caller can silently ignore it and tell the user the message was sent when it was not, which quietly downgrades this from an explicit technique to an implicit one.
- Don't overload true/false when the meaning is not obvious from context; reach for an enum or class so the outcome reads clearly.

## Checklist
- Does the function return an outcome the caller can branch on?
- Is the function marked so that ignoring the return raises a compiler warning?
- Is the outcome shape (Boolean, enum, class) matched to the number and clarity of states?

## Notes
An outcome return type is only as explicit as the enforcement behind it: without a return-value-check annotation, Long shows a caller writing `sendMessage(...)` on its own line and then reporting success regardless. The `@CheckReturnValue` family closes that gap by turning an ignored return into a visible compiler warning, which is what earns the outcome type its place among the explicit techniques. It is the technique of choice when the function does something rather than computing a value to return.
