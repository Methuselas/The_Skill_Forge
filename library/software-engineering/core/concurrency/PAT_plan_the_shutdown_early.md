---
object_id: PAT_plan_the_shutdown_early
object_type: pattern
name: Work Out How It Stops Before You Build How It Runs
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- threading
- lifecycle
- deadlock
- design
cross_links:
- rel: related_to
  target_object_id: PAT_break_one_of_deadlocks_four_conditions
- rel: related_to
  target_object_id: PAT_match_the_problem_to_a_known_coordination_shape
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
reference:
  source_title: 'Clean Code: A Handbook of Agile Software Craftsmanship'
  author: Robert C. Martin, with Brett L. Schuchert
confidence: high
references: []
variants: []
---

# Work Out How It Stops Before You Build How It Runs

## Pattern Rule
**IF** you are building something with several threads that will at some point need to stop cleanly rather than be killed
**THEN** design the stopping sequence at the same time as the running one and get it working early, because it fails in ways steady operation never exhibits and it will take longer than you expect
**ELSE** where the process can simply be terminated and everything it held is discarded safely, say so deliberately — that is a legitimate choice, and it is only legitimate when someone has checked it.

## Do
- Work out, for every thread, what wakes it up to be told to finish. A thread parked waiting on something that will never arrive cannot notice that it has been asked to stop, and that is the ordinary way an orderly stop hangs.
- Trace the ending in dependency order, not creation order. Where one thread supplies another, stopping the supplier first leaves the consumer waiting on something that has already gone — so the side that waits has to be released before, or at the same time as, the side it waits on.
- Give anything that waits a way out other than the arrival it is waiting for. A wait with no alternative exit is fine while the system runs forever and is exactly the thing that strands it on the way down.
- Decide what happens to work that is in flight. Finishing it, abandoning it, and persisting it for later are all defensible, and the failure is discovering at the last minute that nobody chose.
- Build and exercise it early rather than after the running path works. Retrofitting an exit into threads already written means revisiting every wait in the system, at the point where it is most expensive to change them.
- Set a bound on how long you are prepared to wait for a clean stop, and decide what you do when it expires. Waiting forever for a thread that will never finish is a hang, however orderly the intent.

## Don't
- Don't assume a system that runs correctly will stop correctly. Steady operation never exercises the ending, so the ending is entirely untested by everything you have done so far.
- Don't leave a parent waiting on children with no timeout. One child that cannot finish holds the whole thing open indefinitely, and from outside that is indistinguishable from a crash.
- Don't signal cooperating threads without regard to who waits on whom. Telling everything to stop at once is what leaves one side blocked on a partner that has already exited.
- Don't defer this to the end of the project. It is where the awkward interactions live, and the end is when there is least room to discover them.

## Checklist
- For each thread: what wakes it to receive the instruction to finish?
- Which threads wait on which others, and does the ending respect that order?
- Does every wait have an exit that does not depend on what it is waiting for?
- What happens to work that is partly done when the instruction arrives?
- How long will you wait, and what happens when that runs out?
- Has an orderly stop actually been run, or only reasoned about?

## Notes
The reason this earns separate attention is that stopping exercises a part of the design that running never touches. A system in steady operation has all its participants alive, so every wait eventually ends because the thing being waited for is still there to arrive. Ending removes participants one at a time, and every wait that depended on a departed participant becomes permanent. The design can therefore be entirely correct in operation and seize up reliably on the way down, and no amount of running it will reveal that.

The pairing case is the clearest illustration and the most common. Two threads cooperate, one supplying and one consuming. The instruction to stop reaches the supplier, which is between items and free to comply immediately, so it exits. The consumer is blocked waiting for the next item, and the item will never come — so it never returns to the point where it could notice it was asked to stop. It waits forever on a partner that no longer exists, and whatever is waiting for it waits forever too. Nothing failed, nothing errored, and the system will not exit.

Doing this early is a claim about cost rather than about tidiness. An exit path added at the end means revisiting every place a thread waits and giving each one an alternative way out, which is a change to the shape of code that has already been stabilised and, in threaded code, revalidated at considerable expense. Designed alongside the running path, the same requirement is nearly free: each wait gets its escape when it is written, by someone who at that moment holds the full picture of what it is waiting for and why.
