---
object_id: PAT_state_the_problem_before_the_solution
object_type: pattern
name: Write Down the Problem in Terms That Name No Solution
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- problem_definition
- requirements
- design
- scope
cross_links:
- rel: related_to
  target_object_id: PAT_choose_a_problem_representation_before_solving
- rel: related_to
  target_object_id: AP_assess_construction_prerequisites_before_building
reference:
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u03, pp. 36-38
  evidence_type: text
confidence: high
references: []
variants: []
---

# Write Down the Problem in Terms That Name No Solution

## Pattern Rule
**IF** you are handed a request and about to start work on it
**THEN** restate it as what is wrong, in the requester's own vocabulary, with no mechanism named — and if you cannot, you have been handed someone's solution and do not yet know the problem.
**ELSE** when the thing that is wrong genuinely is the machinery — compile times too slow, tools buggy — state it in computer terms, because there the computer is the problem.

## Do
- Apply the sounds-like test. "We can't keep up with orders for the Gigatron" sounds like a problem. "We need to optimize our automated data-entry system to keep up with orders for the Gigatron" sounds like a solution, and smuggles in both the diagnosis and the fix.
- Keep it short. One or two pages is the size; this is not the requirements document, it is the thing requirements work then investigates in depth.
- Write it from the user's point of view and in the user's language, not in technical computer terms. A statement the requester would not recognize as their own problem has drifted.
- Ask whether the answer has to be software at all. Needing an annual profit figure when quarterly reports already exist can mean paying a programmer to write and debug a report generator, or paying someone one minute with a calculator to add up four numbers.
- Check the restatement back with whoever asked. The failure this catches is invisible from inside your own head, because a solution restated as a problem still reads as sensible.

## Don't
- Don't accept a request phrased as a mechanism and start implementing the mechanism. The penalty is double-barrelled: you waste the effort solving the wrong problem, and the right problem stays unsolved.
- Don't let the programmer mindset pick the solution before the problem is stated. Being fluent at building the thing is exactly what makes the unnecessary version of it feel like the obvious next step.
- Don't skip this because the request seems small and obvious. Cheap requests are where a smuggled solution goes unexamined.

## Checklist
- Read your statement aloud: does it sound like a complaint, or like a plan?
- Does it name any technology, component, or technique? If so, cut it and see whether the statement still says what is wrong.
- Would the person who asked recognize this as their problem in their words?
- Have you established that a program is the right kind of answer, rather than assumed it?
- Is the whole thing short enough that nobody needs to summarize it?

## Notes
The trap here is efficient-looking. A request arrives already shaped as a task — optimize this, add that, migrate the other — and shaped tasks are pleasant to accept because they can be started immediately. But a request shaped as a task has already had somebody's diagnosis compiled into it, and that diagnosis is invisible once the wording is adopted. Reversing it back into a problem statement is what exposes the assumption for checking.

This sits before requirements work rather than replacing it. The problem definition says what is wrong; requirements are the detailed investigation of that problem and the first step toward a solution. Getting the order wrong means the detailed investigation inherits an unexamined premise and then elaborates it thoroughly, which is worse than not investigating at all — you end up with precise, well-specified, confidently wrong scope.

The exception is worth holding onto because it is narrow rather than general. When the problem genuinely lives in the machinery — a build that takes too long, a debugger that lies — stating it in computer terms is correct, because there the user *is* a programmer and the machinery *is* the domain. That does not license restating an ordinary business problem in technical terms on the grounds that programmers will read it.
