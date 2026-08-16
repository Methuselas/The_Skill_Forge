---
object_id: PAT_understand_the_routine_before_the_compiler_sees_it
object_type: pattern
name: Understand the Routine Before the Compiler Sees It
library_path:
- software-engineering
- core
- working-practice
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- verification
- desk_checking
- debugging
- compiler
- self_review
cross_links:
- rel: related_to
  target_object_id: AP_build_a_routine_from_intent_level_pseudocode
- rel: related_to
  target_object_id: PAT_treat_compiler_warnings_as_potential_bugs
- rel: related_to
  target_object_id: PAT_externalize_intermediate_state_when_tracing
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Understand the Routine Before the Compiler Sees It

## Pattern Rule
**IF** you have just finished writing a routine and are reaching for the compiler, the test run, or the debugger to find out whether it works
**THEN** read it through first — execute every path in your head, including the endpoints and each exception condition — and submit it to the tool only once you already believe it is correct.
**ELSE** when a further reading is genuinely teaching you nothing, run it and treat the report as confirmation of a judgment you already made rather than as the judgment itself.

## Do
- Execute the nominal paths, the endpoints, and every exception condition by hand. Do it alone first — desk checking — then with at least one other person, which becomes a walk-through or an inspection depending on how formally you run it.
- Suspect your own work before anything else's. Roughly five percent of errors were found to be hardware, compiler, or operating-system errors, and the figure has only fallen since; you are responsible for the other ninety-five.
- Know why every line is there and why it is needed. Nothing is right merely because it appears to work, and if you cannot say why it works, it very likely does not — you just have not found out yet.
- Turn the warning level up to the pickiest setting available and eliminate the cause of each message rather than the message. Bring in validators for what the compiler cannot check, including code that is never compiled at all.
- Once it does compile, step every line under the debugger and confirm each one executes the way you expected — not merely that the routine produced the right answer.
- Redesign a routine that is unusually buggy instead of patching it. A routine that is buggy at this stage tends to stay buggy, and rewriting it from a fresh design is the move that actually ends the sequence of defects.

## Don't
- Don't let the first run start a stopwatch. Once it has, the pull is toward getting it right with just one more attempt, and that pressure produces exactly the hasty, error-prone changes that make the whole thing take longer.
- Don't substitute a feeling about the code for an understanding of it. The recognizable symptom is suspecting the toolchain or the hardware — that is the boundary between hobbyist and professional practice, and it has nothing to do with experience.
- Don't stop at a routine that works. Working is the precondition for the check, not the result of it.
- Don't accept recurring warnings as background. They do one of two things, both bad: they camouflage the messages that matter, or they simply become an irritation you have trained yourself past. Rewriting the code to remove the underlying problem is usually safer and less painful than living with either.

## Checklist
- Have you executed every path by hand, including each exception condition?
- Can you account for every line — what it does and why it is needed?
- If it already works, do you know why it works?
- Has anyone else read it, or heard you talk through it?
- Are you changing code because you found a cause, or because you want a message to go away?

## Notes
The counterintuitive part is the ordering, and it survives the change in tooling that seems to have made it obsolete. The original argument had a component about compile cost that no longer applies — compiling is effectively free now, and the advice to delay it reads at first as a relic of slower machines. But the mechanism named was never the machine. It was the internal clock that starts when you first hand work to something that answers back, and the sequence of increasingly hasty edits that clock produces. A feedback loop that returns in under a second makes that pressure stronger, not weaker, because each hasty edit is now cheap enough to make without deciding to.

What the discipline protects is the difference between a routine that passes and a routine you understand. Those come apart quietly. Adjusting code until the tool stops complaining terminates on a green result whether or not anyone knows why it is green, and the knowledge that was supposed to be built during construction never gets built. The check described here is what makes the green result mean something.

The five-percent figure earns its place by removing the escape hatch rather than by being a statistic. The temptation under a confusing failure is to suspect the layer below, and the number settles that argument before it starts.
