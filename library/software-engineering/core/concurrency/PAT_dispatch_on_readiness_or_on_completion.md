---
object_id: PAT_dispatch_on_readiness_or_on_completion
object_type: pattern
name: Dispatch on Readiness or on Completion
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- concurrency
- design
- patterns
- io
- event_handling
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_give_a_shared_object_its_own_thread_instead_of_a_lock
- rel: related_to
  target_object_id: PAT_keep_thread_aware_code_away_from_thread_ignorant_code
- rel: related_to
  target_object_id: PAT_do_not_create_a_thread_for_every_task
- rel: related_to
  target_object_id: PAT_plan_the_shutdown_early
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Dispatch on Readiness or on Completion

## Pattern Rule
**IF** you are building something that serves many event sources at once — connections, files, devices, user input — and must decide how one loop will attend to all of them
**THEN** choose deliberately between waiting for a source to become *ready* and then performing the operation yourself, and *initiating* the operation up front and being called back when it has finished, because the two put the transfer of data on different sides of the wait and everything else follows from that
**ELSE** where the program serves one source, or where each source can afford a thread that blocks on it, a blocking call per source is the direct expression and neither loop earns its complexity.

## Do
- Locate the wait, since that is the whole distinction. Waiting on readiness means the loop learns a source *can* be operated on and the handler then does the reading or writing itself, synchronously, on the loop's thread. Waiting on completion means the operation was already begun and the loop learns it *has been done*, so the handler receives a result rather than an opportunity.
- Register handlers against sources and let the loop call them, rather than asking each source in turn whether it has anything. The flow of control inverts — you no longer call the framework, it calls you — and that inversion is the price of admission for either arrangement.
- Keep every handler in a readiness loop short. The handler runs on the loop's own thread, so for as long as it runs nothing else is attended to, and one slow handler is indistinguishable from a hung server.
- Hand long work off across a queue when a handler cannot be short. Accept the event on the loop that must not block, put it on a queue, and let a separate pool of threads that may block do the actual work. Two layers with different blocking rules and a queue between them is the standard resolution, and it is what keeps the accepting side responsive while the processing side stays ordinary blocking code that anyone can read.
- Copy across that boundary, or pass something immutable. The layers run on different threads with no shared lock between them, and the queue is only a decoupling device if what crosses it is not still being modified behind it.
- Prefer completion where the platform performs the operation for you and readiness where it does not. Completion-based dispatch is only a win when something below you is genuinely doing the transfer while your thread is elsewhere; emulating it over a readiness primitive re-adds the thread you were trying to save.
- Keep the buffers and the request context alive from initiation until the completion arrives, in a completion design. Nothing on the stack at the point of initiation is still there when the result comes back, and this is the defect that arrangement produces most reliably.
- Expect the wait itself to be a platform facility, and expect it to differ. Whichever you choose, the loop's core is a call that blocks until one of many sources has something to say, that call is supplied by the operating system, and its capabilities and limits vary enough between platforms to be worth confirming rather than assuming.
- Say which arrangement you built, in the code. A reader who assumes the wrong one will write a handler that blocks in a loop that cannot afford it.

## Don't
- Don't perform the operation in a completion handler. Its job is to process a result that already exists; starting fresh blocking work there puts the wait back on the dispatching thread and gives up the arrangement's only advantage.
- Don't let handlers hold state that assumes they run in submission order. Neither arrangement promises it, and completion-based dispatch in particular reorders freely because the durations differ.
- Don't choose completion for the debuggability of a smaller thread count. It separates initiation from result in both time and place, which is precisely what makes a failure hard to attribute — the stack at the point of failure contains the loop and the handler, and nothing about who asked.
- Don't leave the loop's exit unconsidered. Handlers registered against sources that are closing, and completions still to arrive for operations already begun, are the two ways a shutdown wedges, and both are easier to design for than to retrofit.
- Don't add threads to a readiness loop as the first fix for a slow handler. The loop is single-threaded by design and much of its value is that handlers need no guarding; the queue-and-worker-layer split preserves that property, and threading the loop itself destroys it.

## Checklist
- At the moment the loop wakes, does the handler still have to perform the operation, or is it holding a result?
- What is the longest a single handler can run, and what is not being served while it does?
- Where is the boundary between what must not block and what may, and what crosses it?
- For work initiated and completed at different times, what keeps its buffers and context alive in between?
- Which platform facility supplies the wait, and what are its limits on the number of sources?
- How does the loop stop, and what happens to registered sources and outstanding operations?

## Notes
Stated as two named arrangements these look like alternative frameworks to adopt. Stated as a question — on which side of the wait does the data actually move — they are one decision, and it is a decision every multi-source program makes whether or not anyone writes it down. Getting it wrong is not usually a wrong framework; it is a handler written in the style of the other arrangement, which is why naming which one is in force matters more than which one was chosen.

The single-threaded readiness loop is often described as a limitation and is closer to the opposite. Because handlers run one at a time on one thread, handler code needs no locking, and the hardest class of defect is absent from the part of the system with the most application logic in it. That property is what the two-layer split exists to preserve: the reason to move long work to a pool of blocking threads is not merely that the loop would stall, it is that the alternative — making the loop concurrent — would put guarding back into every handler.

Completion-based dispatch is the arrangement whose costs arrive last. It reads well, it needs the fewest threads, and it holds up until something fails and there is no stack that connects the failure to its origin, or until a buffer is reused while an operation still refers to it. These are not implementation slips so much as the recurring bill for separating initiation from completion, and they are worth pricing at design time rather than paying at diagnosis time.
