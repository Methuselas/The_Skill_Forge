---
object_id: PAT_do_not_create_a_thread_for_every_task
object_type: pattern
name: Size the Thread Count to the Hardware, Not to the Work
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
- threading
- design
- performance
- scalability
cross_links:
- rel: related_to
  target_object_id: PAT_match_the_problem_to_a_known_coordination_shape
- rel: related_to
  target_object_id: PAT_decide_if_the_problem_is_worth_parallelizing
- rel: related_to
  target_object_id: PAT_check_for_memory_saturation_before_adding_threads
- rel: prerequisite_for
  target_object_id: PAT_let_idle_workers_take_work_rather_than_busy_ones_hand_it_out
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Size the Thread Count to the Hardware, Not to the Work

## Pattern Rule
**IF** you are deciding how a program will get its independent work onto multiple processors
**THEN** create a number of threads determined by the cores available and feed tasks to them, rather than creating a thread per unit of work
**ELSE** where the program has a handful of long-lived activities that each map to one thread for the program's lifetime, a thread apiece is the right structure and there is nothing to pool.

## Do
- Separate the two counts in your design vocabulary. How many tasks the program has is a property of the problem and can be enormous; how many threads should exist is a property of the machine and is small. Conflating them is what produces the thread-per-task design.
- Price thread creation before relying on it. Starting and joining threads costs enough that it shows up plainly in measurements — parallel standard algorithms that start and join threads on each call are slower than the sequential version on short sequences for that reason alone, and it is the same cost paid explicitly by a thread-per-task program.
- Carry rough magnitudes for both costs, since the design decision usually turns on them. A thread's default stack reserves on the order of one to two megabytes depending on the platform, so the count is bounded by address space long before it is bounded by anything else. Creating and joining a thread that does nothing has been measured at roughly fifteen microseconds on one Linux desktop and roughly forty-five on one Windows laptop — tens of thousands per second, not millions, and that is the floor beneath any work the thread actually does.
- Separate the two questions such a facility is asked to answer, because the answers differ. As a way to saturate many cores with compute, an asynchronous-call facility disappoints: implementations either provide limited parallelism or run each call on its own thread, and neither is what a throughput-bound program needs. As a way to *manage* tasks, it is a considerable improvement on raw threads — it carries return values back to the caller, propagates exceptions instead of terminating the program when one escapes, and leaves oversubscription and load balancing to a runtime that can see the machine. Which of those you need decides whether it is the right tool.
- Weigh what raw threads make you responsible for before choosing them: exhaustion when the system will not create another, oversubscription when more are runnable than there are cores, distributing work between them, and adapting all of that to the next platform. A task-based facility is worth its limits partly because it takes those on.
- Expect the raw thread interface to be too low-level in both directions. It costs too much for fine-grained work, and it exposes too little to build a scheduler on, since most of the attributes that would let you control placement and priority are platform-specific.
- Invert this rule on hardware where a thread's context lives on-chip. A graphics processor keeps every thread's registers resident, so switching between groups of threads costs nothing, and the scheduler covers memory latency by running another group whenever one stalls. There, oversubscription is the *mechanism* rather than the waste: you deliberately launch far more threads than there are cores, because having spare groups ready is what keeps the memory pipeline covered. The rule above is a consequence of context switching being expensive, and it holds exactly as far as that premise does.
- Invert it again where the runtime schedules tasks in user space onto a small pool of system threads, because there the same premise fails for the same reason. A task in such a runtime is not a system thread: its stack starts at a couple of kilobytes and grows on demand rather than reserving megabytes up front, and switching between tasks is a handful of instructions rather than a trip through the kernel, so the two costs this rule is built on drop by three or four orders of magnitude. One task per unit of work is then the correct structure, and hundreds of thousands of them is an ordinary number rather than a design error.
- Notice that the rule's own advice is what makes that safe, and that it is being followed rather than abandoned. The separation between a task count set by the problem and a thread count set by the machine still holds exactly; the runtime is simply the thing performing it, mapping any number of tasks onto a pool it sizes from the cores it can see. What changes is whose job it is. The practical consequence is that building your own pool on top of such a runtime adds a second scheduler above one that already works, which costs throughput and obscures where work is queued.
- Establish which of the two you are on before applying any of this, since the vocabulary hides it. Both are commonly called threads, and the word is the same in a language whose threads are system threads and in one whose threads are scheduled by its own runtime. The question to ask is what a task costs to create and what a switch between two of them costs, and both are documented or measurable in an afternoon; guessing from the name is what produces a pool nobody needed or a hundred thousand system threads nobody can schedule.
- Set the count from cores, adjusted by measurement. Simultaneous multi-threading presents more logical processors than physical cores and the gain from the extra ones varies from substantial to nothing, so whether to count them is a question the program answers by being run both ways.

## Don't
- Don't assume the operating system will absorb the excess. Very few can schedule threads in the millions with any efficiency, and a design that assumes otherwise is portable to almost nowhere.
- Don't judge the design on a small input. Thread-per-task looks fine at ten tasks and collapses at a hundred thousand, which is usually the size that matters and rarely the size that gets tested first.
- Don't add threads to a program that is already limited by something shared. More threads against a saturated memory bus, or against a guarded region everything passes through, add overhead and no throughput.
- Don't write your own scheduler as the first response. It is a substantial component with its own failure modes, and a library pool or a parallel algorithm covers most of what a program actually needs.

## Checklist
- How many tasks will this create at realistic input sizes, and how many threads?
- What does a thread cost to start on the target platform, relative to the work one task does?
- Where do tasks queue up, and what happens when they arrive faster than they are consumed?
- Is the thread count derived from the hardware, or from the shape of the input?
- Does a context switch on this hardware actually cost anything, or is the premise behind the rule absent here?
- Has the count been varied and measured, including with and without the logical cores?

## Notes
The appeal of thread-per-task is that it makes the code read the way the problem is described — here is an independent piece of work, here is a thread for it. That correspondence is genuinely valuable, and the way to keep it is a task abstraction over a fixed pool, so the code still says "this is an independent task" while the runtime decides where it runs.

Two costs sit behind the rule, and they are different. Creation and joining is a per-thread cost, paid up front, which is what makes fine-grained tasks lose. Oversubscription is a running cost: threads beyond the available processors do not add capacity, they timeslice, so the work is the same and the context switching is extra.

The exception worth keeping in view is a thread that mostly waits. Threads blocked on input, on the network, or on a user are not consuming a processor, so the count that matters is how many are runnable rather than how many exist. That is a different design from the compute-bound case and the reason a rule stated as "one thread per core" needs the qualifier.
