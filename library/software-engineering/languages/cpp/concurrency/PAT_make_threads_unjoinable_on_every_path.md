---
object_id: PAT_make_threads_unjoinable_on_every_path
object_type: pattern
name: Make Threads Unjoinable on Every Path
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- threading
- resource_management
- lifecycle
cross_links:
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: PAT_plan_the_shutdown_early
- rel: related_to
  target_object_id: PAT_do_not_create_a_thread_for_every_task
- rel: related_to
  target_object_id: PAT_specify_the_launch_policy_when_asynchrony_is_required
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Make Threads Unjoinable on Every Path

## Pattern Rule
**IF** a thread object exists in a scope that can be left by an early return, a break, or an exception
**THEN** guarantee it has been joined or detached before the scope ends, on every path, by giving that responsibility to an object whose destructor performs it
**ELSE** where the thread object is destroyed immediately after a join that cannot be skipped, the guarantee already holds and no wrapper is needed.

## Do
- Take the consequence seriously, because it is the harshest in the language's concurrency support: destroying a thread object that is still joinable terminates the program. Not undefined behaviour, not a leak — termination.
- Understand why that was chosen, since it explains why no gentler default is coming. The two alternatives were both judged worse. An implicit join makes the destructor wait for a thread whose work is no longer wanted, producing a performance anomaly at a point in the code that contains no clue about it. An implicit detach severs the connection while the thread keeps running and keeps referring to the enclosing scope's variables, which is undefined behaviour that appears to work.
- Wrap the thread in a type whose destructor joins or detaches according to a policy chosen at construction. That converts "every path out of this function" from a review obligation into a property of the type, which is the same move as any other resource.
- Choose the policy deliberately rather than defaulting to join. Joining is safe and can block; detaching does not block and leaves a running thread referring to memory that is about to disappear. The right answer depends on whether the work is still wanted when the scope ends, which is a question about the program rather than the thread.
- Declare thread data members last. Members are destroyed in reverse order of declaration, so a thread declared last is destroyed first — while the members its function may still be using are all intact.
- Expect the same surprise from the other direction with futures. A future's destructor usually just destroys its members, but the last one referring to the shared state of a task launched asynchronously blocks until that task finishes. A destructor that sometimes blocks and sometimes does not is worth knowing about before it appears in a profile.

## Don't
- Don't rely on reaching a join at the end of the function. An exception thrown between the thread's creation and that call skips it, and the destructor then terminates the program — which is the failure mode this rule exists to prevent.
- Don't detach to make the termination go away. It compiles, it stops the crash, and it replaces a loud failure with a thread that outlives the objects it refers to.
- Don't assume a thread that has finished its work is unjoinable. Joinability is about whether the object still corresponds to a thread of execution, not about whether that thread is still running; a completed thread's object is joinable until joined or detached.
- Don't treat this as a special case unrelated to other resources. A thread is a resource acquired in a scope, and the reason to hand it to an object with a destructor is the reason that applies to every other resource.

## Checklist
- Can this scope be left by an early return, a break, or an exception after the thread is created?
- Is the join or detach performed by a destructor rather than by a statement?
- Was the join-or-detach policy chosen, or inherited from whatever the wrapper does by default?
- Are thread members declared after the members their functions use?
- Does any future here refer to an asynchronously launched task whose destructor may block?

## Notes
The termination behaviour reads as harshness and is better understood as the committee declining to choose between two silent failures. Both alternatives hide something: one hides a wait, the other hides a dangling reference. Termination hides nothing, and it puts the decision back where it belongs — with the person who created the thread and knows whether its work is still wanted.

The declaration-order point is small and worth keeping, because it is invisible until it fails. Members are destroyed in reverse declaration order, so a thread declared first is destroyed last, after everything its function might be touching has already gone. Declaring it last inverts that, and costs nothing.

The future's blocking destructor belongs beside this rather than in a separate discussion, because both are the same category of surprise: an object whose destruction does something substantial and conditional. In both cases the fix is not to avoid the facility but to know which objects have destructors that wait, and to place them where waiting is acceptable.
