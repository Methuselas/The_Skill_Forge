---
object_id: PAT_ask_whether_the_problem_grows_with_the_machine
object_type: pattern
name: Ask Whether the Problem Grows With the Machine
library_path:
- software-engineering
- core
- performance
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- performance
- scalability
- measurement
- concurrency
- estimation
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_decide_if_the_problem_is_worth_parallelizing
- rel: related_to
  target_object_id: PAT_derive_the_parallelism_from_work_and_span
- rel: related_to
  target_object_id: PAT_name_the_performance_metric_before_you_optimize
- rel: related_to
  target_object_id: PAT_reproduce_the_real_context_before_believing_a_microbenchmark
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Ask Whether the Problem Grows With the Machine

## Pattern Rule
**IF** you are predicting what more processors will buy, or reporting what they bought
**THEN** settle first whether the problem size is held fixed while the machine grows, or grows along with it — because these are different questions with different ceilings, and the famous limit on speedup applies to only one of them
**ELSE** where the program will run one problem size on one machine forever, neither model is needed and a measurement of that case is the whole answer.

## Do
- Name the question before quoting any number. *Same problem, finished sooner* and *bigger problem, finished in the same time* are both legitimate goals and they are not the same goal. The first holds the input fixed and adds processors; the second grows the input alongside the processors. Nearly every disagreement about whether something "scales" is these two being compared to each other.
- Keep the fixed-size ceiling and its scope together. Whatever fraction of a *fixed* problem must run sequentially does set a hard limit on speedup that no number of processors overcomes. That result is correct and it is routinely quoted as though it were unconditional, which it is not — it is a statement about holding the problem still.
- Turn the question around for the growing case, because the arithmetic changes completely. Instead of asking how much faster a parallel machine runs a fixed problem, ask how long a single processor would need for the problem the parallel machine actually solves. Now the sequential portion is a fraction of the *parallel* run rather than of the total work, and speedup rises very nearly in proportion to the processors added.
- Read the two views as explaining the same data rather than contradicting each other. Real programs routinely exceed the fixed-size ceiling, and that is not evidence the law is wrong — it is evidence that people running large machines are solving larger problems, which is a question the fixed-size model was never asking.
- Expect the sequential fraction to shrink on its own as the problem grows, and check whether it does. Startup, configuration, input parsing, and a final combining step are often close to constant while the parallel work rises with the input — so a program that looks limited at small scale can be nearly unlimited at large scale, and the way to find out is to measure at more than one size.
- State the baseline every speedup is measured against, since the number means nothing without it. One core of the same machine, one machine of a cluster, and the best known sequential algorithm are three different denominators, and the last is the honest one — a parallel algorithm run on one processor is usually slower than the sequential algorithm it replaced, so using it as the baseline inflates every figure that follows.
- Be careful reporting efficiency on mixed hardware, where the processor count is not a number anyone agrees on. An accelerator has thousands of small cores; whether to count them all, whether to count the host that feeds it, and what to use as the single-processor time are all open. Where the platform is heterogeneous, reporting speedup against a stated baseline is more honest than an efficiency figure whose denominator was chosen by the author.

## Don't
- Don't quote a fixed-size ceiling at a workload that grows. It is the most common misuse of the result and it talks people out of parallelizing things that would have scaled nearly linearly in the regime they actually run in.
- Don't present a growing-problem measurement as though the problem had been held fixed. The number will be much better and it answers a different question; a reader who assumes the fixed-size regime will conclude the sequential fraction is smaller than it is.
- Don't measure at one size and extrapolate. Which regime you are in is not visible from a single point, and the sequential fraction that dominates at small input can be irrelevant at large input.
- Don't use the parallel code on one processor as the sequential baseline. It carries the decomposition, the coordination, and often a worse algorithm, so the comparison flatters the parallel version by exactly the overhead you were trying to measure.
- Don't let "it scales" pass without the qualifier. The claim is meaningless until it says which quantity was held fixed, against what baseline, and over what range of sizes was actually tried.

## Checklist
- Is the problem size fixed while processors increase, or growing with them?
- Which of the two ceilings applies to the case this program will actually run in?
- What is the baseline for every speedup figure quoted here?
- Has this been measured at more than one problem size?
- Does the sequential portion stay constant as the input grows, or grow with it?
- On mixed hardware, what number is being used as the processor count, and does the reader know?

## Notes
The two models are usually presented as a dispute and are better understood as a pair of questions. Holding the problem fixed and adding processors is the right frame when the work is what it is — a fixed simulation, a fixed dataset, a deadline on a known input — and there the sequential fraction really is a wall. Growing the problem with the machine is the right frame when more capacity means more ambition, which is the usual reason anyone buys a bigger machine, and there the wall is largely an artifact of the question.

The practical consequence is that the fixed-size limit gets quoted in situations it does not govern, and it is discouraging in exactly the wrong direction. A team told that ten percent sequential code caps them at tenfold speedup may abandon work that would have scaled almost linearly, because in their actual regime the sequential ten percent was measured on a small input and shrinks to almost nothing on a large one. The correction is not to distrust the arithmetic but to check which question it answered.

The baseline problem deserves its own attention because it is where most reported speedups quietly lose their meaning. Comparing a parallel program on many processors against the same parallel program on one is comparing against something nobody would ever run, and it credits the parallel version with removing overhead it introduced. The comparison that means something is against the best sequential solution available, which is often a different algorithm entirely — and choosing it as the baseline is what makes the resulting number a claim about the problem rather than about the code.
