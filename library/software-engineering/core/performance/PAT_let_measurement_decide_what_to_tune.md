---
object_id: PAT_let_measurement_decide_what_to_tune
object_type: pattern
name: Let Measurement Decide What to Tune, Never Intuition
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
- optimization
- measurement
- premature_optimization
cross_links:
- rel: prerequisite_for
  target_object_id: PAT_weaken_a_memory_order_only_against_a_measurement
- rel: related_to
  target_object_id: PAT_choose_the_level_before_tuning_the_code
- rel: related_to
  target_object_id: PAT_make_code_readable
- rel: prerequisite_for
  target_object_id: AP_tune_a_measured_bottleneck
- rel: related_to
  target_object_id: AP_build_a_pool_for_a_hot_allocation
- rel: related_to
  target_object_id: AP_locate_a_performance_bottleneck_by_measurement
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Let Measurement Decide What to Tune, Never Intuition

## Pattern Rule
**IF** you believe a piece of code is a performance problem, or that a change would make it faster
**THEN** treat that belief as a hypothesis with a poor track record and measure before acting on it and again after
**ELSE** where measuring genuinely costs more than the change is worth, the honest conclusion is that the change is not worth making — not that you may guess.

## Do
- Start from the distribution, because it is more extreme than anyone expects. Twenty percent of a program's routines consume eighty percent of its execution time, and under four percent of a program typically accounts for over half its run time. One thousand-line program spent eighty percent of its time in a five-line square-root routine.
- Wait until the program is correct and complete. You cannot identify a bottleneck in a program that does not yet work, so optimizing as you go means spending about ninety-six percent of the effort on code that never needed it — and leaving little for the four percent that does.
- Discount your own experience here specifically. It was formed on some other machine, language, compiler, or library, and every one of those changes the answer. A hand conversion of matrix indexing to pointer arithmetic, expected to remove ten thousand multiplications, produced no improvement at any matrix size, because the compiler's optimizer had been doing it already.
- Expect most attempts to fail, and plan the work around that. Across one aggressive tuning effort, at least two-thirds of the optimizations tried did not work and some doubled the run time; more than half of attempted tunings typically produce negligible or negative improvement.
- Measure precisely enough for the answer to mean something. Use the CPU clock ticks allocated to your program rather than the time of day, so a context switch to another program is not charged to your routine, and factor out measurement and startup overhead so neither version is unfairly penalized.
- Write straightforward code to help the optimizer, not to defeat it. Optimizing compilers do better on straightforward code than on clever code, so fooling with loop indexes can cost more in lost compiler optimization than the trick returns.
- Use the profiler as the admission gate, not only as an instrument. If a tuning matters enough to haul out the profiling machinery and measure it, it probably matters enough to allow — and if it does not, it does not matter enough to spend readability on either. That single test resolves most arguments about whether an optimization is worth it, because it makes the person proposing the change pay for it in effort before the code pays for it in clarity.

## Don't
- Don't believe that fewer lines of high-level code means faster or smaller machine code. Ten straight assignments initializing an array measured at least sixty percent faster than the two-line loop doing the same job. There is no predictable relationship between source line count and a program's size or speed.
- Don't say an operation is *probably* faster. There is no room for probably: the answer changes with the language, the compiler, the compiler version, the library, the library version, the processor, and the memory on the machine.
- Don't forget that a tuning commits you to re-measuring it forever. Every compiler upgrade, library version, and platform change can turn a hand optimization into a pessimization, and one that is never reprofiled will eventually be one.
- Don't accept a speed argument over a correctness argument. It is hardly ever true that a program needs to be fast before it needs to be right — a program that does not have to work can be made to run instantly.
- Don't tune something because tuning it is satisfying. Taking a routine from twenty microseconds to two feels like defying physics and carries real cachet among programmers, and neither is a reason.
- Don't assume that strictly less work means less time on the same machine. Deleting a provably unnecessary comparison from the inner loop of a string compare — same compiler, same hardware, same data — more than doubled its run time, and switching the loop index from an unsigned to a signed integer, a change with no effect on the values computed, made it faster than the original. Unpredictability is not only a property of moving between platforms; it lives inside one binary on one machine.

## Checklist
- Have you profiled, or are you working from a belief about where the time goes?
- Is the program complete and correct yet?
- Did you measure the effect of the change, not just make it?
- What is the plan for re-measuring this optimization after the next toolchain upgrade?
- If this change turns out to buy nothing, will you take it back out?

## Notes
The strongest sentence in this material is the one about what you can be certain of: the only result of an optimization you can usually count on without measuring is that you have made the code harder to read. The rest is a gamble, and the phrasing that follows is the operational test — if it is not worth measuring to know it is more efficient, it is not worth sacrificing clarity for a performance gamble.

Premature optimization's real defect is lack of perspective rather than wasted cycles. Three things go wrong at once. You cannot find the bottlenecks yet, so effort lands almost everywhere except where it would pay. In the rare case where you do find one, you overkill it and let others become critical, which lowers performance overall. And attention goes to algorithm analysis and arcane argument while correctness, information hiding, and readability become secondary — which is the expensive trade, because performance is easier to improve later than those are. Post hoc performance work touches under five percent of a program's code. The choice is between doing performance work on five percent of the code and readability work on a hundred percent of it.

There is a genuine exception and it is narrow. For a minority of projects — smaller than most people think, and shrinking — speed or size is a major concern, and those risks must be addressed by up-front design rather than by later tuning. Even there the answer is not to optimize as you go but to specify size and speed goals per feature and work to them, which keeps the perspective that ad hoc early optimization destroys.

The evidence for "measure or do not bother" is stronger than a principle usually gets, because the companion technique catalogue is effectively a controlled demonstration of its own unreliability. Nearly every technique in it backfired in at least one language. Reordering a case statement so the most frequent branch is tested first — advice that is analytically obvious — measured 7% faster in Visual Basic, exactly 0% in Java, and 18% *slower* in C#. Unrolling a loop returned 34% in C++ and 27% worse in Python. A second strength reduction on a polynomial evaluation, which should have been strictly cheaper, was 94% worse. Two languages that share case-statement syntax produced opposite verdicts on case versus if-then-else, one dramatically faster and the other dramatically slower, with no explanation available. The catalogue is best read not as a list of things to do but as the reason the rule exists.

Worse, the unpredictability is increasing rather than decreasing with experience. McConnell's own retrospective a decade after his first edition reports that the effect of any specific optimization had become *less* predictable, not more, as languages, compilers, versions, libraries, and settings multiplied. Accumulated familiarity with a technique is therefore not evidence about what it will do in your build.

Two cautions about the anecdotes and tables in this material. The measured ratios come from compilers and machines of the early 2000s, so their specific figures are historical, and the durable content is the shape rather than the number — the concentration of run time in a small fraction of code, the size of the gap between interpreted and compiled execution, the fact that arithmetic operations sit near each other while transcendental functions and system calls do not. And every one of those was obtained by measuring, which is the point being made rather than a detail of how it was made.
