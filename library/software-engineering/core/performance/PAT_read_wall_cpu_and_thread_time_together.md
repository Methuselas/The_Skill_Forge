---
object_id: PAT_read_wall_cpu_and_thread_time_together
object_type: pattern
name: Read Wall, CPU, and Thread Time Together
library_path:
- software-engineering
- core
- performance
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- measurement
- benchmarking
- diagnosis
- concurrency
cross_links:
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: PAT_name_the_performance_metric_before_you_optimize
- rel: prerequisite_for
  target_object_id: AP_locate_a_performance_bottleneck_by_measurement
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Read Wall, CPU, and Thread Time Together

## Pattern Rule
**IF** you are putting timers around a section of code to find out how it behaves
**THEN** record elapsed time, process CPU time, and calling-thread CPU time from the same pair of points, because the gaps between the three say what the code was doing and no single one of them does
**ELSE** where you only need to confirm a change moved the number the user feels, elapsed time alone answers that — the three-clock read is for diagnosis, not for the verdict.

## Do
- Learn the four readings by their shape. All three roughly equal means the section computed non-stop on one thread and the CPU was fully loaded. CPU far below elapsed means the section spent its time waiting rather than computing. Process CPU high with thread CPU near zero means other threads did the work while this one blocked. Process CPU at a multiple of elapsed means that many threads computed at once — two threads doing a second of work in 0.53 seconds of elapsed time is the shape of concurrency that is actually paying.
- Read a low CPU-to-elapsed ratio as a question, not an answer. A section that is blocked on a socket, a file, or a user shows the same shape as one running on an overloaded machine and the same shape as one thrashing in swap, and those need different responses.
- Invert the goal for interactive code. A program servicing user requests wants CPU time as far below elapsed time as it can get, because that ratio is the evidence it is not burning the machine while idle; the same reading in a compute path would be a fault.
- Reach past the portable clock when you need CPU time. Language-level clocks typically expose elapsed time only, so process and thread CPU time come from a system call — on POSIX, `clock_gettime` with `CLOCK_PROCESS_CPUTIME_ID` and `CLOCK_THREAD_CPUTIME_ID` alongside `CLOCK_REALTIME`.
- Report counts next to the times. Timers can carry anything you decide to record — how many times the function ran, how long the average input was — and that context is usually what makes the times interpretable.
- Subtract like units before combining them when the clock returns seconds and nanoseconds separately. Take the difference of the seconds, then add the difference of the sub-second parts; combining first and subtracting afterwards throws away significant digits between two large numbers.

## Don't
- Don't conclude "this section is slow" from elapsed time alone. Elapsed time counts the seconds a thread spent asleep exactly the same as the seconds it spent computing.
- Don't measure a thread's own clock and report it as the program's cost. A thread that dispatches work and waits on the result reads near zero while the program is at full load, which reads as a fast section that is doing nothing of the kind.
- Don't scatter timers through the code to find out where the time goes. Timer calls cost enough to slow the program and distort the very measurement, and covering unknown territory this way means instrumenting hundreds of functions blind — that is what a profiler is for.
- Don't trust any of the three on a machine whose clock speed is moving. Power-saving and frequency scaling vary the rate the work is done at, so disable them before a measurement you intend to compare against another.

## Checklist
- Do you have all three readings from the same pair of points, or only one?
- If CPU time came in well under elapsed time, do you know which of blocking, contention, and paging caused it?
- For a threaded section, does process CPU time exceed elapsed time by roughly the number of threads you expected to be working?
- Is the machine's frequency scaling disabled for this run?
- Does the section carry the counts you would need to interpret an odd result later?

## Notes
The three clocks are cheap to record together and awkward to add later, which is the practical argument for taking all of them the first time. The reason to want them is that the interesting failures are all mismatches: the program that looks busy and is waiting, the thread that looks idle and is the whole program, the parallel section that turns out to be running one thread's worth of work.

Instrumenting by hand has a boundary worth naming, because it decides when to stop and reach for a different tool. Timers answer any question you thought to ask and no question you did not — if the timer is not there, the answer does not exist until the code is changed and rerun. That makes benchmarking excellent for code you own and are actively working on, and useless as a way to explore an unfamiliar or inherited codebase.

The habit that pays here is instrumenting major sections in advance rather than in response to a problem. Code written with its own timing hooks can answer the coarse question immediately the next time performance is in doubt, and there will be a next time.
