---
object_id: PAT_choose_index_types_the_compiler_can_assume_do_not_wrap
object_type: pattern
name: Choose Index Types the Compiler Can Assume Do Not Wrap
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
- loops
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_treat_undefined_behavior_as_a_whole_program_assumption
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: PAT_optimize_for_what_the_compiler_can_prove
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Choose Index Types the Compiler Can Assume Do Not Wrap

## Pattern Rule
**IF** you are declaring the index or counter of a loop that will run hot
**THEN** use a signed type, or an unsigned type as wide as the machine's registers, so the compiler is free to assume the increment cannot wrap and can use the cheapest instruction for it
**ELSE** where you are relying on wraparound as part of the algorithm — hashing, checksums, ring buffers — an unsigned type is required and the cost is the price of the semantics you asked for.

## Do
- Know why the types differ, since nothing in the source suggests they should. Signed overflow is undefined, so the compiler may assume it never happens and emit a plain add. Unsigned overflow is defined to wrap, so on a 64-bit machine a 32-bit unsigned increment must produce a wrapped 32-bit result — which the natural add instruction does not do, forcing a slower substitute.
- Take the sizes that are safe. Signed integers of any width are fine. Unsigned integers the width of the machine's registers are fine, because the register-width add already has the required semantics. It is specifically narrow unsigned arithmetic on a wider machine that pays.
- Give the compiler a bound if you must keep the narrow unsigned type. Comparing the index against a known length lets it deduce that the counter cannot reach its maximum, which restores most of the gain — though the comparison itself costs a little, leaving this slightly behind the signed version.
- Verify in the generated code rather than by reasoning, because the difference is a single instruction. The fast form shows an add; the slow one shows an address-computation instruction being used to do arithmetic.
- Treat this as the reason to prefer signed loop variables by default. The rule is easy to apply everywhere, costs nothing where it does not matter, and removes a trap that is invisible at the source level.

## Don't
- Don't assume that an index which is never negative should therefore be unsigned. The reasoning is sound about the values and wrong about the code generated: on the substring comparison that opened this book, switching the index from unsigned to signed was the change that made the whole sort several times faster.
- Don't look for the cause of such a difference in the C++ source. Two loops differing only in the declared type of a counter are the same algorithm doing the same work, and the explanation exists only in what the compiler is permitted to assume.
- Don't conclude from this that undefined behaviour is a tool to invoke deliberately. What you are choosing is a type whose overflow the compiler need not implement — not a program that overflows. An index that actually wraps is undefined and the program is then ill-formed regardless of how well it ran.
- Don't generalize the specific instruction sequences. Which instruction is fast for which type is a property of one architecture, and the durable content is that the assumption differs by signedness, not the names of the instructions.

## Checklist
- Are the hot loop's counters signed, or unsigned at register width?
- If a narrow unsigned type is required, is the loop bounded by a comparison the compiler can use?
- Does the generated code show a plain add for the increment?
- Is wraparound part of the algorithm here, or merely impossible?
- Could this index actually reach its type's maximum for any legal input?

## Notes
This is the answer to a demonstration set up much earlier: an "obvious" optimization that removed work made a comparison loop more than twice as slow, while a change with no effect on any computed value made it faster than the original. Both surprises come from the same place — the compiler is not optimizing the arithmetic you wrote, it is optimizing under the assumptions your types give it.

The general lesson is larger than the specific rule and worth carrying forward. Performance can depend on a declaration that changes nothing about what the program computes, so the source is not a reliable guide to the cost of a hot loop, and a difference that has no explanation at the source level has one at the level of what the compiler was permitted to assume.

It also shows the practical value of the undefined-behaviour rules to code that never invokes them. Signed overflow being undefined is what makes plain integer arithmetic fast; a program that stays inside its types collects that benefit without ever encountering the hazard.
