---
object_id: PAT_read_a_profile_as_a_statement_about_machine_code
object_type: pattern
name: Read a Profile as a Statement About Machine Code
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
- profiling
- measurement
- compilers
- diagnosis
cross_links:
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: PAT_reproduce_the_real_context_before_believing_a_microbenchmark
- rel: prerequisite_for
  target_object_id: AP_locate_a_performance_bottleneck_by_measurement
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Read a Profile as a Statement About Machine Code

## Pattern Rule
**IF** you are attributing time to a function or a source line from a profiler's report
**THEN** read the report as a statement about the instructions the compiler emitted, and reconcile it with the source rather than reading it as source-level truth
**ELSE** where a single function dominates so completely that the attribution question does not change the answer, take the obvious reading and move on.

## Do
- Build with optimization and debug information at the same time. Debug information is what maps instruction addresses back to source lines, and optimization is what makes the profiled program the same program that ships — profiling an unoptimized build measures code nobody runs, however much easier it is to read.
- Expect inlining to move the time somewhere you did not write it. One profiler will still name the inlined function and attribute time to the lines where its body was written; another will show the time in the caller, as if the sort routine and `main` had grown expensive on their own. Both are describing the same binary.
- Treat a source line that appears more than once in an annotated listing as evidence of scheduling, not of a duplicate. The instructions generated from one line are frequently spread across the function by the optimizer, and the profiler shows the line beside each cluster.
- Check the sample count before believing a percentage. Time-based sampling needs enough samples in a function for its share to mean anything — a few dozen per function you intend to trust — and a short run collects nowhere near that.
- Take the whole-program counter run first when you want to know what kind of limit you are against. Instruction count, cycles, branches and branch misses, cache references and misses across the entire run tell you which resource is the problem; they do not tell you where, which is what the sampled profile is for.
- Drop to the disassembly when the source-level attribution stops making sense. Locating the compare-and-jump pair that implements a loop condition is what turns "18% is spent somewhere in these two lines" into a specific claim about which operation costs it.
- Pick the tool for the question rather than looking for one that answers everything. Interpreter-based profilers slow the program heavily, instrumented ones require a special build and assume the instrumented code performs like the original, and hardware-counter sampling is nearly free but only tells you where the program counter was.

## Don't
- Don't compare a profiled run's total time against an unprofiled one and treat the difference as a finding. Collecting a profile slows the program; the relative breakdown is what survives, not the absolute duration.
- Don't stop at the function name when the function has several callers. Which call chain pays for the cost is a separate question from which function spends it, and the call graph is what answers it — a function taking 58% of the run may owe two thirds of that to one of its two callers.
- Don't profile the whole program at full detail and expect the data to interpret itself. The recommended order is coarse first, then focused reruns on the interesting part; the exhaustive profile is usually too much information rather than too little.
- Don't expect the profiler's line-level report to survive heavy optimization intact. There is no way to undo inlining, reordering, and code motion in the report, so detailed profile reading is a skill that improves with the platform's assembly language, not a feature the tool provides.

## Checklist
- Was the profiled binary built optimized, with debug information?
- How many samples landed in the function you are about to act on?
- Could this function have been inlined into, or out of, where the report places it?
- Do you know which caller the cost belongs to, or only which function?
- If the counters say cache misses or branch misses dominate, does the code you are looking at explain that?

## Notes
Profiling exists to answer the question benchmarking cannot: where does the time go in code nobody instrumented. That is its whole advantage, and the cost of it is that the answer arrives in the compiler's coordinate system rather than the author's.

Sampling is worth understanding as a mechanism rather than a black box, because the mechanism explains both the accuracy and the failure. The profiler interrupts the program at an interval, records where the program counter is and what the hardware counters read, and infers time from sample proportion. Sample more often and you learn more and perturb more; sample less and a cheap function can hide entirely. Nothing about it guarantees a function with three samples is really three percent of anything.

Modern CPUs carry a limited number of hardware counters — often around eight — each configurable to count one of many event types, and the available events differ by processor and by hypervisor. This is why two machines can give different counter sets for the same program, and why a counter-based finding should name the machine it came from.

One preparation step is easy to forget and quietly invalidates comparisons: variable clock speed. Power management moves the frequency during the run, so measurements taken before and after a change are not on the same scale unless scaling is disabled.
