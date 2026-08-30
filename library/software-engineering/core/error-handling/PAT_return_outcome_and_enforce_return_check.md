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
**THEN** return an outcome value indicating success or failure, and arrange that ignoring the return produces a compiler warning — by marking the function, or by returning a type that already carries the obligation — otherwise the outcome is too easy to overlook.

## Do
- Choose the outcome shape to fit: a Boolean when there are two states, an enum when there are more than two or when true/false would be unclear, a whole class when detailed information is needed.
- Enforce the check with the language's mechanism — `@CheckReturnValue` in Java, `MustUseReturnValue` in C#, `[[nodiscard]]` in C++ — so a caller who drops the return gets a warning at compile time.
- Ask whether the obligation belongs on the type rather than on each function, because in some languages it already does. Where the standard outcome type is itself declared must-use, every function returning it is enforced with no annotation anywhere, and adding one per function is noise that also implies the unmarked functions are exempt. Prefer that arrangement wherever the language offers it: an annotation can be forgotten on the next function somebody writes, a type cannot.
- Handle it at the call site with a plain if-else that branches on success and failure, as with `sendMessage()` returning true when sent and false when the channel is closed.

## Don't
- Don't ship an unmarked outcome return; a caller can silently ignore it and tell the user the message was sent when it was not, which quietly downgrades this from an explicit technique to an implicit one.
- Don't overload true/false when the meaning is not obvious from context; reach for an enum or class so the outcome reads clearly.

## Checklist
- Does the function return an outcome the caller can branch on?
- Is the function marked so that ignoring the return raises a compiler warning — or does the
  type it returns already carry that obligation, making a mark redundant?
- Is the outcome shape (Boolean, enum, class) matched to the number and clarity of states?

## Notes
An outcome return type is only as explicit as the enforcement behind it: without a return-value-check annotation, Long shows a caller writing `sendMessage(...)` on its own line and then reporting success regardless. The `@CheckReturnValue` family closes that gap by turning an ignored return into a visible compiler warning, which is what earns the outcome type its place among the explicit techniques. It is the technique of choice when the function does something rather than computing a value to return.

Where the enforcement lives is worth separating from whether it exists. The annotation families above attach the obligation to a function, which means it is applied one function at a time and can be omitted on the next one; a language that declares its standard outcome type must-use attaches the obligation to the type instead, and then every function returning that type is covered by construction. The visible consequence is that a codebase in such a language shows no annotations at all while being more strictly enforced than one covered in them — the absence is the mechanism working, not the rule going unapplied. Reading it the other way and adding per-function marks is worse than redundant, because a marked subset invites the inference that the unmarked functions were deliberately exempted.
