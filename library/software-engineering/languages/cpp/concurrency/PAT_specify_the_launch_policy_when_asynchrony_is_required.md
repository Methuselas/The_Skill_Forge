---
object_id: PAT_specify_the_launch_policy_when_asynchrony_is_required
object_type: pattern
name: Specify the Launch Policy When Asynchrony Is Required
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
- api_design
- avoiding_surprises
cross_links:
- rel: related_to
  target_object_id: PAT_do_not_create_a_thread_for_every_task
- rel: related_to
  target_object_id: PAT_make_threads_unjoinable_on_every_path
- rel: related_to
  target_object_id: PAT_define_your_code_contract_explicitly
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Specify the Launch Policy When Asynchrony Is Required

## Pattern Rule
**IF** you are launching a task asynchronously and the program depends on it actually running concurrently, or on it running at all
**THEN** state the asynchronous launch policy explicitly, because the default permits the implementation to defer the task instead
**ELSE** where you only need the result eventually and do not care when the work happens, the default is what you want — it lets the runtime avoid oversubscription by deferring.

## Do
- Know what the default actually permits: either asynchronous execution on another thread, or deferred execution, where the function does not run until the result is requested. Both are conforming, the choice is the implementation's, and it is most likely to defer exactly when the machine is loaded — which is when concurrency mattered most.
- Take "may run later" and "may never run" as the same statement. A deferred task runs only when its result is requested; if the program never requests it, the function never executes. Any work whose value is in the side effects rather than the result can therefore silently not happen.
- Distrust thread-local storage across the boundary. A deferred task runs on whichever thread requests the result, so thread-local reads and writes inside it land somewhere that cannot be predicted from the launch site.
- Recognize the polling loop this breaks, because it looks correct and hangs forever. A loop that waits on the result with a timeout and continues until the status is no longer "not ready" never terminates for a deferred task: the wait returns the deferred status immediately and forever, and the loop never asks for the result that would cause the work to run.
- Ask whether the task is deferred before entering any timeout-based loop, if you must use the default. There is no direct query for it; the way to find out is to wait with a zero timeout and check whether the status comes back deferred.
- Use the default deliberately where it earns its keep. Letting the implementation decide is how oversubscription and load balancing get handled for you, and giving that up is the cost of demanding a thread.

## Don't
- Don't read the default as "asynchronous unless there is a good reason." It is "asynchronous or not, at the implementation's discretion," and code written against the first reading is correct only by luck of scheduling.
- Don't demand asynchronous launch reflexively either. It forces a thread whether or not the machine has capacity, which reintroduces the oversubscription that the task-based facility exists to manage.
- Don't rely on the side effects of a task whose result nobody reads. Under the default that work may never happen; if the side effects are the point, the result has to be requested or the policy stated.
- Don't debug a hanging timeout loop by increasing the timeout. The status is not going to change, and the length of the wait is not what is wrong.

## Checklist
- Does the program depend on this task running on another thread?
- Does it depend on the task running at all, for its side effects?
- Does the task touch thread-local state?
- Is there a wait-with-timeout loop anywhere on this future?
- If the default policy is being used, is that a decision about oversubscription rather than an omission?

## Notes
The reason the default is permissive is sound and worth stating, because it explains when to leave it alone. Deciding between running now on another thread and running later on this one is exactly the scheduling judgment that a task-based facility exists to make, and it needs runtime information the caller does not have. The default gives it that latitude. What the default cannot know is that your program requires concurrency for its correctness rather than its speed.

The three consequences are easy to treat as separate curiosities and they are one consequence seen from three sides: the task may not be running on another thread. Thread-local access is unpredictable because there is no other thread; the timeout loop hangs because there is nothing in progress to time out; and the work may never happen because deferral means the function is a stored call waiting for someone to ask.

That last case deserves the sharpest attention, because it is the one that produces no symptom at all. A task launched for its side effects, under the default policy, whose result is never requested, is a function that does not run — and there is nothing in the code, the profile, or the output to indicate that anything was supposed to.
