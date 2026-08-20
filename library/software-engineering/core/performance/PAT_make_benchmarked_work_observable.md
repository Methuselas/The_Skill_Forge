---
object_id: PAT_make_benchmarked_work_observable
object_type: pattern
name: Make the Benchmarked Work Observable
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
- benchmarking
- measurement
- compilers
- optimization
cross_links:
- rel: related_to
  target_object_id: PAT_reproduce_the_real_context_before_believing_a_microbenchmark
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: prerequisite_for
  target_object_id: AP_locate_a_performance_bottleneck_by_measurement
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Make the Benchmarked Work Observable

## Pattern Rule
**IF** you are timing a code fragment whose result the surrounding benchmark never uses
**THEN** route the result somewhere the language counts as observable before you believe any number the benchmark prints, because an optimizer is entitled to delete work nobody can detect
**ELSE** where the fragment already writes to a file, performs I/O, or mutates state the caller reads afterwards, it is anchored and needs nothing added.

## Do
- Recognize the symptom before you chase the wrong explanation. A fragment that reports zero time, or a time that does not grow when you raise the iteration count from one to thousands, has not been measured — it has been removed. Stepping through it in a debugger and finding the lines missing confirms it.
- Know what the language actually promises to preserve, because that list is short and execution time is not on it. Reads and writes of volatile objects happen as written and in order, data written to files at termination is as if the program ran as written, and prompts reach interactive devices before the program waits for input. Everything else may be rearranged or dropped, and running under a debugger is not observable behaviour either.
- Anchor the result with the tool your benchmark library provides, and prefer it. A wrapper such as Google Benchmark's `DoNotOptimize` marks the value as used without switching off optimization inside the expression, which is exactly the split you want: the fragment is compiled the way production would compile it and is merely forbidden to disappear.
- Assign into a volatile sink where no such wrapper is at hand. Writing each result to a `volatile` variable forces the calls to happen and to happen in order, while leaving the compiler free to generate the best code for the work itself.
- Put the timed function in its own compilation unit and turn off whole-program optimization. Otherwise the optimizer can see that every call returns the same value and keep only the first, and no amount of sinking the result will stop it.
- Take the fixture's setup out of the timed region rather than subtracting it afterwards. Allocating and filling the inputs is not the thing being measured, and a benchmark loop that measures only its own body reports a number that means one execution.

## Don't
- Don't sink successive results into the same non-volatile variable and print it at the end. Only the last write survives; the compiler drops every earlier call, and the run that was optimized away reports a spectacular improvement over the one that was not.
- Don't read a suspiciously fast result as a fast implementation. When two versions differ by an order of magnitude and the slower one is the one you expected to be slower, the first hypothesis is that the faster one did not run.
- Don't reach for a global "disable optimizations" flag to stop the deletion. An unoptimized build measures code that will never ship, and the comparison it produces is between two programs nobody runs.
- Don't assume the anchor is permanent. A newer optimizer can see through a construct that held last year, so a benchmark result that jumps after a toolchain upgrade deserves the deletion check again before it is interpreted as a performance change.

## Checklist
- Does the reported time scale roughly linearly when you multiply the iteration count?
- Is every iteration's result anchored, rather than only the final one?
- Is the function under test compiled separately from the benchmark, with whole-program optimization off?
- Is the build otherwise optimized exactly as production is?
- Does the timed region exclude input setup and teardown?

## Notes
The rule that governs this is the as-if rule: the compiled program must show the same observable behaviour as the source executed line by line, and it is otherwise unconstrained. Read as a benchmark author, that sentence says a measurement is only defended to the extent it participates in observable behaviour — the compiler is not being clever or hostile, it is doing exactly what it is licensed to do, and a benchmark that measures nothing is the author's bug.

Anchoring the result is a narrower instrument than it first appears, and the narrowness is the point. It does not suppress optimization of the code under test; it removes exactly one option, deleting the call. That keeps the fragment compiled as production would compile it, which is the only version whose timing is worth having.

This trap is the reason a micro-benchmark's first plausible-looking number should be treated as unverified. Confirming that the work happened is a separate question from confirming that the measured context resembles the real one, and both have to be answered before a number is evidence.
