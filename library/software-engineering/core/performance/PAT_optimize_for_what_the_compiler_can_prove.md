---
object_id: PAT_optimize_for_what_the_compiler_can_prove
object_type: pattern
name: Optimize for What the Compiler Can Prove
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
- compilers
- optimization
- tuning
- design
cross_links:
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: PAT_read_a_profile_as_a_statement_about_machine_code
- rel: related_to
  target_object_id: PAT_ask_whether_the_hot_code_can_run_less_often
- rel: related_to
  target_object_id: PAT_avoid_global_state_inject_shared_state
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Optimize for What the Compiler Can Prove

## Pattern Rule
**IF** the compiler is not performing an optimization on hot code that you can see would be valid
**THEN** work out which scenario would make it invalid — not in your program, but in any program this fragment could legally appear in — and then find a way to rule that scenario out in the code itself
**ELSE** where no such scenario exists and the optimization still does not happen, the limit is the compiler's analysis budget rather than its knowledge, and shrinking the fragment is the lever.

## Do
- Start from the right question. The compiler may transform your program only if it can prove the result is identical for *every* possible input and state, so the useful question is never "is this true?" but "could this fail to be true in some program the compiler must also support?"
- Look first at the three things that block most optimizations. A function whose body is not visible could do anything the language permits, so nothing can be assumed across the call. Global and otherwise widely reachable state can be modified by any of those invisible functions. And a long, complicated fragment exhausts the analysis budget — compilers stop rather than let compile times explode.
- Count what a called function can reach, not what it is passed. A function that does not receive your object as an argument can still reach it if the object is global, is a class member with member or friend functions in play, or has had a reference to it stored somewhere. Only when nothing outside can name the object does its stability become provable.
- Prefer facts the compiler gets for free over facts it must derive. Marking a value constant is checked by the syntax rules whether or not the optimizer has budget left, so the guarantee is always available; the same fact left to be discovered by analysis may or may not be found.
- Settle small "does this cost anything" arguments by diffing the generated code rather than benchmarking. Where the difference would be far too small to measure reliably, identical machine code from both versions is a stronger answer than any timing — a redundant null test ahead of an inlined function that tests again compiles to exactly the same instructions as the version without it.
- Shape a hot loop so the hardware's parallel form is provable, since vectorizing one is the same permission question in its sharpest form. The compiler may issue one instruction across several elements only if it can establish that the iterations do not depend on each other, that the number of them is known before the loop is entered, and that the elements sit contiguously — scattered access turns one wide load into several narrow ones and gives most of the benefit back. A call the compiler cannot see into, a nested loop, or any locking or atomic operation in the body each end the analysis on their own.
- Treat good structure as the cheap route to good optimization. Small functions with clear boundaries, few global interactions, and short bodies are easier for the compiler to analyze for exactly the reasons they are easier to read; the overlap is not a coincidence.

## Don't
- Don't assume a fact you have documented is a fact the compiler has. A descriptive function name, a comment, and in most cases an assertion just before the code are all invisible to the optimizer — some compilers derive a constraint from an assertion at the highest settings, most do not.
- Don't reason from your own program's behaviour. That a global is never modified there, or that two arguments are never the same object, is a property of your calls rather than of the function being compiled, and the compiler has to compile the function.
- Don't add redundant checks that a visible function already performs. Where the callee is inlined, the compiler removes the duplicate; where it is not, the outer check earns its place by avoiding the call, and the inner one is a cost the compiler cannot remove because it cannot see every caller.
- Don't take "the compiler will get rid of it anyway" as a reason to avoid a local variable. The variable may well disappear from the generated code while the guarantee its presence expressed is kept and used.
- Don't count on the widening happening because the loop looks simple. Whether a given loop vectorized is a question for the generated code or the compiler's own report, not for inspection — and the answer moves between compilers, between versions of one compiler, and between the instruction sets of one processor family.
- Don't go looking for these opportunities across the whole program. They pay only where a profile has already shown the code matters, and finding them costs attention that is better spent where the time is.

## Checklist
- What legal scenario would make this optimization change the program's behaviour?
- Which functions in this fragment are visible to the compiler, and which are opaque?
- Can anything the fragment calls reach the state you are relying on being stable?
- Is that stability expressed in a form the language checks, or left to be inferred?
- Have you compared the generated code for the two versions before arguing about the cost?

## Notes
The gap this closes is between two kinds of knowledge that feel identical from inside a program. The author knows that a container's size never changes across a call, that two pointers never overlap, that a flag is fixed for the run. The compiler knows only what the code establishes for all possible executions. Nearly every "why didn't it optimize that?" reduces to a fact of the first kind being mistaken for one of the second.

The unoptimized baseline is worth knowing because it sets the scale of what the compiler is contributing. A program built with optimization disabled commonly runs an order of magnitude slower than the same source fully optimized — so this is not a matter of recovering a few percent, it is about not obstructing the single largest performance mechanism available.

Two of the three blockers pull against each other, which is why this is a judgment rather than a rule. Making function bodies visible enlarges the region the compiler can reason about, and it also enlarges the region the compiler must reason about within a finite budget. There is no setting that maximizes both; what resolves it in practice is that the fragments where it matters are few and known from measurement.
