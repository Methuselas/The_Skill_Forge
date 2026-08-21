---
object_id: PAT_stop_a_thread_by_asking_it_rather_than_killing_it
object_type: pattern
name: Stop a Thread by Asking It, Rather Than Killing It
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- threading
- lifecycle
- cancellation
cross_links:
- rel: related_to
  target_object_id: PAT_make_threads_unjoinable_on_every_path
- rel: related_to
  target_object_id: PAT_plan_the_shutdown_early
- rel: related_to
  target_object_id: PAT_wait_on_a_predicate_not_on_a_notification
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Stop a Thread by Asking It, Rather Than Killing It

## Pattern Rule
**IF** long-running work needs to be able to end early — a shutdown, a cancelled request, a search whose answer arrived from elsewhere
**THEN** pass the work a token it can check, and signal a request through the matching source, because a thread cannot be safely terminated from outside and the only workable cancellation is one the work cooperates with
**ELSE** where the work is short and bounded, waiting for it to finish is simpler than any cancellation protocol and there is nothing to arrange.

## Do
- Know why the forcible option does not exist, since that is what makes the cooperative one non-negotiable rather than stylistic. A thread stopped at an arbitrary point may be halfway through updating something, leaving the program's state undefined; and it may be holding a mutex, in which case stopping it deadlocks everything that later wants that mutex.
- Separate the three roles the mechanism gives you: a source that issues the request, tokens that observe it, and callbacks that fire when it is issued. They share one stop state, and the tokens are cheap to copy.
- Hand the token to whatever is doing the work, not to a particular kind of thread. It reaches a plain thread, a joining thread, an asynchronously launched task, or a worker driven through a promise equally well — which makes this a general signalling mechanism rather than a feature of one thread type.
- Poll the token at points where stopping is safe, which is the design work this pushes onto you and is the point. The work chooses where it can be interrupted, so it is never interrupted while an invariant is broken.
- Wait on a condition variable in its interruptible form when the work can block. The overload taking a stop token returns on either a notification or a stop request and tells you which, so a waiting thread is not a thread that has stopped listening.

## Don't
- Don't expect the request to affect work that has already finished. Signalling after completion does nothing and the registered callback does not run, so a protocol that assumes every request is observed will silently skip the cases where it arrived late.
- Don't expect it to affect work that never checks. The token is a flag; a loop that does not poll it runs to completion regardless, and a destructor that requests a stop before joining will then wait for exactly as long as it would have anyway.
- Don't leave the ordering to chance for work that is already executing. The request has to happen before the work polls the token or registers its callback, so a request issued after joining is a request issued after everything that could observe it.

## Checklist
- Does the work have points where stopping would leave state consistent, and does it poll there?
- Does every entity that might need stopping hold a token?
- Can the work block, and if so does it block in a form that a stop request can end?
- Is the request issued while the work could still be running, rather than after joining it?
- Does anything assume a request is always observed?

## Notes
The three states a piece of work can be in when the request arrives are the part worth carrying, because they are what turns a cancellation feature into a protocol you have to design. Not yet started means the token reports the request and any callback runs. Already executing means it depends on the race between the request and the poll. Already finished means the request has no effect at all. Only the first is unconditional.

This is why the joining thread's destructor requests a stop before it joins rather than only joining. A destructor that just waits will wait indefinitely on a thread looping until told otherwise; requesting first supplies the signal the loop is waiting for. That only helps for work written to check, which is the same requirement stated from the other end.

The design pressure this creates is healthy and worth naming. Being unable to stop work from outside forces the work to declare where it is safe to stop, and those points are exactly the ones where its invariants hold. A cancellation mechanism that did not require this would let callers interrupt at points the author never considered.
