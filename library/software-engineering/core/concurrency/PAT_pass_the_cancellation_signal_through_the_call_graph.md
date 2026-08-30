---
object_id: PAT_pass_the_cancellation_signal_through_the_call_graph
object_type: pattern
name: Hand Every Wait the Signal That Cancels It
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- cancellation
- lifecycle
- interfaces
- timeouts
cross_links:
- rel: related_to
  target_object_id: PAT_plan_the_shutdown_early
- rel: related_to
  target_object_id: PAT_block_with_a_deadline_before_polling_on_an_interval
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
- rel: related_to
  target_object_id: PAT_dont_hide_errors
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted sources
confidence: medium
references: []
variants: []
---

# Hand Every Wait the Signal That Cancels It

## Pattern Rule
**IF** an operation can block, or can run long enough that something outside it may need it to stop before it finishes
**THEN** pass a cancellation signal into it as an explicit parameter, and have every wait inside it stand ready for that signal as well as for the thing it is waiting on
**ELSE** where an operation is bounded and short enough that nothing will ever want to interrupt it, leave the parameter off rather than threading it everywhere for symmetry — but record that as a decision, because the same reasoning is what a reader will apply to the next function, and it stops being true as soon as the operation grows a wait.

## Do
- Make the signal a parameter rather than something the operation reaches for. Ambient state can express that everything should stop and cannot express that this one request should, which is the case that actually arises — a caller abandoning one query, a client that disconnected, a retry superseded by a newer attempt. The parameter is what carries that distinction, and it is not recoverable later by putting a flag somewhere convenient.
- Derive a child signal from the parent whenever an operation starts sub-work, so cancelling anything cancels everything beneath it. That property is the whole reason the mechanism scales: the caller cancels the one thing it knows about, and work it has never heard of and could not name stops as a consequence.
- Express a deadline through the same object as a cancellation, because a timeout is a cancellation with a clock attached, and splitting them produces two mechanisms that each cover half the waits. An operation already standing ready for cancellation needs no further work to respect a deadline; one that treats them as separate honours whichever it was written for and hangs on the other.
- Accept the signal in every function that can block, including ones deep enough that nobody expects to cancel them. The chain is only as responsive as its least responsive wait, so a single leaf that ignores it turns a prompt stop into a hang — and it does so intermittently, because the hang appears only when cancellation arrives while that particular wait is the one in progress.
- Keep it a request rather than a kill. The operation notices, stops what it is doing, and returns through its normal exits, so locks are released, buffers are returned, and partial work is dealt with by the code that understands it. What makes this the safe form is exactly that nothing is destroyed from outside while it holds something.
- Report a cancelled operation as cancelled and not as a failure. A caller that cannot tell them apart will retry work that was deliberately abandoned and will raise alarms about a system doing what it was told, so the distinction has to survive all the way out — which means the layers in between must pass it through rather than flattening it into a generic error.
- Let the signal live for the operation and no longer. It describes one unit of work, so a copy kept in a long-lived structure either goes stale and cancels nothing, or outlives its operation and cancels something unrelated.

## Don't
- Don't substitute a process-wide flag. It answers the shutdown question and no other, and the moment a second reason to stop something appears there is nowhere to put it.
- Don't skip a leaf because it is fast. Fast is a claim about the common case, and the wait that hangs is the one that was slow for a reason nobody predicted.
- Don't log the cancellation at every level it passes through. It is one event, and reporting it at each frame turns an ordinary shutdown into a page of apparent errors, which trains readers to ignore the log.
- Don't reach for terminating the worker instead. That stops the code from outside at a point of somebody else's choosing, which is how held locks, half-written buffers, and unreleased resources outlive the thing that was using them.

## Checklist
- Does every function here that can block accept the signal, including the deepest ones?
- Does cancelling this operation stop the work it started, without having to name that work?
- Is a deadline carried by the same mechanism as a cancellation, or by a separate one?
- Can a caller tell a cancelled operation from a failed one, at the outermost layer?
- Is the signal held anywhere that outlives the operation it describes?
- If cancellation arrives at the worst moment, does anything get destroyed rather than unwound?

## Notes
This belongs at the point of designing an interface rather than at the point of building a shutdown, because it changes signatures, and signatures are cheap to decide and expensive to revise. A codebase that threads cancellation from the start carries an extra parameter on most of its functions and gains one uniform answer to a question that otherwise has to be solved separately at every wait. One that adds it later has to revisit every blocking call in the system — the same retrofit cost that makes an unplanned shutdown expensive, arriving through a different door. The parameter reads as noise until the first time something has to stop promptly, and then it is the only thing that makes that possible.

Passing it explicitly rather than reaching for it is what buys the property that matters, and the property is compositional. A caller holds a signal for the work it initiated, anything that work starts derives from it, and cancelling the top cancels a subtree whose shape the canceller does not know and could not enumerate. No arrangement of ambient state reproduces that, because ambient state has one scope while the requirement has as many scopes as there are operations in flight. It is also why the signal must not be stored: it describes one operation's lifetime, and a structure that keeps one has confused a property of a request with a property of the thing serving requests.

The distinction between cancelled and failed is the part most often lost, and it is lost in the middle rather than at either end. The layer that cancels knows, and the layer that was cancelled knows; every layer in between sees something that is not success and has a generic way of describing that, so the information is flattened by code that had no opinion about it. What follows is a retry of work somebody deliberately stopped, or an alert about a component behaving correctly, and both get diagnosed as concurrency problems when they are reporting problems. Deciding early that cancellation is its own outcome, distinct from failure, is what keeps it intact across the layers that do not care.
