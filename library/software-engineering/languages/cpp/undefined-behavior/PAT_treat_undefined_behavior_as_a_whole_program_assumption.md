---
object_id: PAT_treat_undefined_behavior_as_a_whole_program_assumption
object_type: pattern
name: Treat Undefined Behavior as a Whole-Program Assumption
library_path:
- software-engineering
- languages
- cpp
- undefined-behavior
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- undefined_behavior
- optimization
- correctness
- compilers
cross_links:
- rel: related_to
  target_object_id: PAT_optimize_for_what_the_compiler_can_prove
- rel: related_to
  target_object_id: PAT_choose_index_types_the_compiler_can_assume_do_not_wrap
- rel: related_to
  target_object_id: PAT_treat_floating_point_arithmetic_as_approximate
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Treat Undefined Behavior as a Whole-Program Assumption

## Pattern Rule
**IF** you are reasoning about what a construct the standard calls undefined will actually do
**THEN** stop reasoning about the construct and start reasoning about the program, because the compiler is entitled to assume the construct never executes and to optimize everything around it on that basis
**ELSE** where the standard calls the behaviour implementation-defined or unspecified, reasoning about the outcomes is legitimate — those categories promise a set of possible results, and this one promises nothing.

## Do
- Keep the three categories apart, because the whole error lives in conflating them. Implementation-defined behaviour must be documented by the implementation. Unspecified behaviour has a range of permitted outcomes that need not be documented. Undefined behaviour places no requirement on the program at all — not a choice among outcomes, no requirement.
- Follow the reasoning the optimizer actually performs, forward and backward. It assumes the program is well defined, deduces what must therefore be true, and optimizes on that. If a statement would be undefined for large inputs, then large inputs do not occur — so a preceding branch that only fires for large inputs is dead code and its output disappears. If a statement is undefined for every input, it is never executed, so its function is never called, and the conditions leading there are false.
- Expect the deduction to run past the offending line in both directions. A function that dereferences a pointer and then tests it for null has the test removed — and so does one that tests first and dereferences afterwards, because either the pointer was non-null and the test was redundant, or it was null and nothing is required of the program.
- Take real divergence between compilers as the evidence it is. A program with an infinite loop hung under one compiler and, under another at the same optimization level, printed the text after the loop and exited cleanly. Both are correct.
- Run the sanitizer in your regular testing. Compilers ship an undefined-behaviour sanitizer that reports these situations at run time with the file, line, and the actual values involved. It costs run time, which is why it is a testing tool rather than a build setting.
- Keep the danger the right size. The compiler emits machine instructions; it cannot make your program do anything you could not have written in assembly yourself. The value of the folklore about arbitrary catastrophe is that it stops people reasoning about outcomes — the accurate statement is that the code you get is unrelated to the code you expected.

## Don't
- Don't argue about which of two plausible results an undefined expression produces. Choosing between them is what the *unspecified* category means; treating undefined behaviour that way is the mistake this card exists to prevent.
- Don't conclude a construct is safe because it currently works. The next compiler version reasons more aggressively than this one, and these deductions have grown steadily more thorough with each release.
- Don't expect the damage to be confined to the line that caused it. The standard withdraws its requirements from the entire program, and the optimizer's deductions propagate outward from the assumption.
- Don't assume the hardware's behaviour is what you will get. Signed overflow on a processor that wraps silently still permits the compiler to emit code containing no addition at all — a function returning whether `i + 1 > i` compiles to loading the constant true.

## Checklist
- Is the construct undefined, or merely implementation-defined or unspecified?
- What would the compiler be entitled to conclude if it assumed this never executes?
- Which code before and after this point could that conclusion eliminate?
- Does this build pass under the undefined-behaviour sanitizer?
- Is any part of your reasoning of the form "the hardware will just do X"?

## Notes
Why the standard leaves anything undefined rather than merely implementation-defined is worth understanding, because it makes the rule feel less arbitrary. The infinite-loop case is the clearest: fusing two identical loops into one is a valuable transformation and is only valid if the first loop terminates, and proving termination in general is not decidable. So the language assumes every loop terminates, which necessarily makes a non-terminating one undefined. Much of the rest of the list has the same shape — a useful optimization requires an assumption, and the cases violating it are placed outside the language rather than given a defined cost.

That framing also explains what a programmer gets in return, which is easy to miss when undefined behaviour is presented purely as a hazard. Nearly every entry on the list corresponds to an optimization the compiler can perform on ordinary correct code. The cost is borne entirely by programs that were already wrong.

Two of these are common enough to recognize on sight. Signed integer arithmetic is undefined on overflow, so the compiler may treat adding a positive number as strictly increasing. And dereferencing a pointer asserts that it is non-null from that point backwards, so null checks around a dereference are removable — the situation arising most often where someone has added checks in some places and not others.
