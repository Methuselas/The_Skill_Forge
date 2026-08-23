---
object_id: PAT_prefer_a_task_to_a_thread_when_work_returns_something
object_type: pattern
name: Prefer a Task to a Thread When Work Returns Something
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
- tasks
- error_handling
- threading
cross_links:
- rel: related_to
  target_object_id: PAT_specify_the_launch_policy_when_asynchrony_is_required
- rel: related_to
  target_object_id: PAT_make_threads_unjoinable_on_every_path
- rel: related_to
  target_object_id: PAT_match_the_problem_to_a_known_coordination_shape
- rel: prerequisite_for
  target_object_id: PAT_specify_the_launch_policy_when_asynchrony_is_required
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Prefer a Task to a Thread When Work Returns Something

## Pattern Rule
**IF** work is to run concurrently and the caller needs its result, or needs to learn that it failed
**THEN** express it as a task rather than as a thread, because the channel between the two endpoints already carries the value, the failure, and the readiness — none of which a thread carries and all of which you would otherwise build
**ELSE** where the work returns nothing, reports nothing, and you need to manage the thread of execution itself — its lifetime, its identity, its detachment — a thread is the object you actually want.

## Do
- Weigh the two on what they give you rather than on which is more primitive. A thread hands results back through a shared variable that you must declare, protect, and synchronize; a task hands them back through a channel that is protected for you, so a task must not have a mutex added to it.
- Treat the difference in failure behaviour as the decisive one, because it is not a matter of convenience. An exception escaping a thread's callable does not merely end that thread — it terminates the creator and the whole process. The same exception from a task is stored in the shared state and rethrown when the result is retrieved, which puts it in front of code positioned to handle it.
- Set the failure explicitly when driving the channel by hand. Catching everything in the worker and setting the current exception on the promise is the idiom, and it turns any failure into a value the other endpoint receives.
- Retrieve the result exactly once. A second retrieval through the same future is undefined; where several parties need the value, convert the future to its shareable form and let each hold one.
- Notice that a task does not oblige you to create a thread at all. Whether one is created is a separate decision, expressed by the launch policy, and forgetting to make it deliberately is its own hazard.

## Don't
- Don't return results through a shared variable and a join. It works, and it requires you to declare the variable, arrange its synchronization, decide where it lives, and invent a separate channel for reporting failure — all of which arrive together with the task.
- Don't let an exception escape a thread's callable. There is no mechanism to catch it outside that thread, so the outcome is termination of the entire program regardless of what the creator would have done with it.
- Don't call the retrieval a second time on a plain future. It compiles and it is undefined, and the failure appears only on the path where two parties both wanted the answer.

## Checklist
- Does the caller need a value back, or only for the work to have happened?
- If a shared variable is carrying the result, what protects it and what reports failure?
- Can the work throw, and if so where would that exception surface?
- Is the result retrieved more than once, and is the future the shareable kind if so?
- Has the launch policy been chosen, or left to the default?

## Notes
The vocabulary is worth taking literally, because it explains the design. The two ends are a promise and a future: one endpoint undertakes to supply a result, the other collects it, and the two need not be in the same thread or exist at the same moment. What flows between them is not restricted to values — a notification with no payload and an exception are both ordinary things to send.

The exception asymmetry is the part that should change behaviour. It is easy to read "the thread terminates" as a local consequence and it is not local: the standard's response to an exception leaving a thread's callable is to end the program. Any design where concurrent work can fail and the caller is expected to cope has to route that failure somewhere, and the task's channel is already that route.

The obligation to create a thread being optional is a real difference rather than an implementation detail, and it is what makes tasks composable in ways threads are not. It also means the question "will this actually run concurrently?" has a separate answer that has to be given deliberately.
