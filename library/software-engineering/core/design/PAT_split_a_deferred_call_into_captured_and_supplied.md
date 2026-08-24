---
object_id: PAT_split_a_deferred_call_into_captured_and_supplied
object_type: pattern
name: Split a Deferred Call Into Captured and Supplied
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- design
- deferred_execution
- callbacks
- lifetime
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_name_every_lambda_capture
- rel: related_to
  target_object_id: PAT_have_the_doer_record_the_undo
- rel: related_to
  target_object_id: PAT_keep_function_parameters_focused
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Split a Deferred Call Into Captured and Supplied

## Pattern Rule
**IF** you are storing a call to be made later — a queued task, a callback, an undo entry, a retry, a scheduled job
**THEN** divide its inputs deliberately into the ones captured when the call is created and the ones supplied when it is finally invoked, because that split is the design and everything else about the mechanism follows from it.

## Do
- Put an input in the captured half when it is known now and may not exist or may have changed later. Anything read from a scope that will have exited by invocation time belongs here, as a value rather than as a reference to it.
- Put an input in the supplied half when it is genuinely unknown at creation. Where the click position, the retry attempt, or the current clock is what the call is waiting for, capturing a stale one is worse than not having it.
- Say what the invoker must still provide, and keep that list as short as the work allows. Every supplied input is something the invoker has to know about the call, which is exactly the coupling storing the call was meant to remove.
- Count the lifetimes the captured half pins. A capture is a decision to keep something alive until the call runs or is discarded, and where that is expensive or unbounded, it argues for supplying the input instead.

## Don't
- Don't capture a reference to something whose scope will end first. This is the characteristic failure of deferred work and it usually appears to succeed, because the memory is often still readable and often still holds the old value.
- Don't capture the whole surrounding object to reach one field of it. That pins a lifetime far larger than the call needs and hides which field the call actually depends on.
- Don't push inputs into the supplied half to avoid thinking about lifetimes. Each one moves knowledge back into the invoker, and an invoker that must assemble half the call is not decoupled from it.
- Don't leave the split implicit and let the capture syntax decide it. A default that captures everything reachable answers this question by accident, and the answer it gives is usually the one with the largest lifetime and the least visible dependency.

## Checklist
- For each input, is it known now, and will it still be valid and correct when the call runs?
- What is the longest-lived thing this call keeps alive, and is that intended?
- What must the invoker know in order to invoke this, and is that list as short as it can be?
- If this call is discarded without ever running, does everything it captured get released?

## Notes
The reason to make this split explicitly is that it is the only decision a deferred call really has. Storing a call exists because the moment of assembling one is separated from the moment of making it; with that separation comes the question of what travels across the gap, and every other property — how large the stored call is, what it keeps alive, how much the invoker must know — is a consequence of the answer.

More captured means more independence. A call carrying everything it needs can be invoked by something that knows nothing about it, which is the whole point of storing calls rather than calling directly. The counterweight is lifetime: everything captured is held until the call runs or is thrown away, so independence is bought with retention and the balance is per case rather than general.

The failure is asymmetric and worth knowing before you choose. Capturing too much wastes memory and holds objects longer than necessary, which is visible in a profile and annoying. Capturing too little, or capturing a reference where a value was needed, produces a call that reads freed memory at invocation time — undefined, intermittent, and usually discovered a long way from the code that made the decision.
