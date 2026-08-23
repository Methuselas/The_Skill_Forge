---
object_id: PAT_give_every_operation_one_instant_where_it_takes_effect
object_type: pattern
name: Give Every Operation One Instant Where It Takes Effect
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
- correctness
- design
- data_structures
- review
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_specify_a_concurrent_object_as_a_sequential_object_plus_a_correctness_condition
- rel: related_to
  target_object_id: PAT_make_every_concurrent_operation_a_complete_transaction
- rel: related_to
  target_object_id: PAT_publish_shared_data_through_one_atomic_handle
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
- rel: prerequisite_for
  target_object_id: DRILL_name_the_committing_step_on_every_path
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Give Every Operation One Instant Where It Takes Effect

## Pattern Rule
**IF** you are building or reviewing a shared object whose operations are meant to appear atomic, and there is no lock held across each whole operation to make that obvious
**THEN** identify, for every operation and every path through it, the single step at which that operation becomes visible to everyone else — and treat an operation for which you cannot name one as unfinished design rather than as code to test harder
**ELSE** where each operation runs entirely inside one critical section, any point within it serves and the requirement is already met; naming it is documentation rather than design work.

## Do
- Look for one step, not a region. The step is where the effect becomes observable to other operations — typically a single write or read-modify-write on the shared state — and the useful test is that an observer checking just before it sees an object where the operation has not happened, and just after it sees one where it has completed.
- Do this per path, not per operation. The same operation frequently takes effect at different steps depending on outcome: a removal that finds something takes effect when it detaches it, while the same removal finding nothing takes effect earlier, at the read that established emptiness. Both are correct and they are different instants.
- Accept a step that is a read as readily as one that is a write. An operation that changes nothing still has to take effect somewhere, and for a query the moment it read the state it reports is exactly that moment. Operations that observe are not exempt from having a position in the order.
- Use the exercise as a design constraint rather than a proof obligation. An operation whose effect leaks out gradually — several fields updated in turn, each visible to somebody — has no such instant, and that absence is the defect. Restructuring so that one step publishes everything, often by putting the whole change behind a single pointer or a single flag, is the usual fix and is easier than arguing the gradual version is safe.
- Watch for the instant that falls outside the operation's own execution, and treat it as a warning. Designs exist where an operation is completed by another thread helping it along, so its effect happens at a step that thread executed; these are legitimate and considerably harder to reason about, and knowing you are in one is worth more than the elegance of the construction.
- Write the step down next to the code. It is one line, it is what the whole safety argument rests on, and it is invisible in the source — a reader who cannot find it cannot check any change they make against it.
- Recheck it after every change to the operation. Adding a fast path, reordering two statements, or hoisting a read all move it, and the change that moves it is rarely the change that looks dangerous.
- Handle an operation that cannot be satisfied when it is called by finding the instant it is *fulfilled*, which may be much later and caused by somebody else. A removal from an empty structure that waits rather than failing takes effect when an insertion supplies it, so its committing step sits in the inserting thread's execution — the operation's interval simply extends until then. An operation like this has no committing step inside its own code at all, and looking for one is how the design gets mistaken for broken.
- Ask the same question of an operation that fails or throws. An operation that aborts still either happened or did not, and saying which — and at what step it was decided — is part of the contract.

## Don't
- Don't accept "the lock makes it atomic" once the lock has been narrowed. Fine-grained schemes hold different locks over different parts of an operation, so the operation is no longer inside one critical section and the instant has to be found rather than assumed.
- Don't let two candidate steps stand. If an operation could plausibly be said to take effect at either of two points, then there is an interval where it has partly happened, and some other operation can be scheduled inside it.
- Don't confuse the instant with the operation's return. A value can be computed and the effect committed well before the caller gets an answer, and it is the commit that orders the operation against everything else.
- Don't skip this for an operation that only reads. That is exactly where a missing instant hides, because nothing is being modified and the operation looks harmless — while it can still return a view of the object that no single moment of its history ever held.
- Don't treat the absence of a nameable instant as something testing can settle. It means executions exist that the object's own specification does not explain; the failure is rare by construction and will not be produced on demand.

## Checklist
- For each operation and each path through it, which single step commits its effect?
- Does an observer immediately before that step see the object as though the operation never started?
- Is the step ever executed by a thread other than the one that called the operation?
- For read-only operations, at which step was the returned view taken?
- Is the step recorded anywhere a later reader will find it?
- After the last change to this operation, did the step move?

## Notes
The reason this technique is worth having as a habit is that it converts a question about all possible interleavings into a question about one line of code. Arguing directly that no schedule can break an object means reasoning about an unbounded set; naming the committing step and showing the object is consistent on both sides of it discharges the same obligation locally. That change of scale is what makes non-locking designs reviewable at all.

The diagnostic value tends to exceed the proof value. Most of the time, hunting for the step either finds it immediately or reveals that the operation does not have one — and the second outcome is the useful one, because an effect that becomes visible in stages is a defect that testing is poorly equipped to find. The design response is nearly always the same: arrange for one step to publish the whole change, which is the same move as putting the change behind a single handle everyone reads.

Two subtleties recur often enough to expect them. The first is that one operation usually has several committing steps, one per outcome, and reviewers who look for a single answer per method miss the empty-case path — which is where the interesting bugs are. The second is that the step need not belong to the thread that called the operation; helping schemes, where a thread finishes work another started, are the standard way to obtain stronger progress guarantees, and they relocate the instant into another thread's execution. Neither is a problem, and both are things to notice deliberately rather than discover later.
