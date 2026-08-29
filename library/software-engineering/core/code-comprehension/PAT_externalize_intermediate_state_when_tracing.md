---
object_id: PAT_externalize_intermediate_state_when_tracing
object_type: pattern
name: Externalize Intermediate State When Tracing Code
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_comprehension
- tracing
- working_memory
- debugging
cross_links:
- rel: related_to
  target_object_id: PAT_diagnose_source_of_code_confusion
- rel: related_to
  target_object_id: AP_build_a_mental_model_of_unfamiliar_code
- rel: related_to
  target_object_id: AP_find_a_defect_by_hypothesis_not_by_guessing
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants:
- variant_id: VAR_hermans_choose_a_constrained_model_to_focus_retrieval
  variant_name: Pick a Model Whose Constraints Do the Focusing
  variant_basis: method_sequence
  difference_from_foundation: The foundation externalizes intermediate state to stop working memory from having to store an execution while also processing it, and the trace is shaped by the code being traced. This variant treats the choice of notation as the active ingredient — pick a model whose constraints exclude most of the problem, because being unable to express the irrelevant parts is what directs long-term memory toward the relevant memories. A state diagram can only show values of variables and an entity relationship diagram can only show classes and their relationships, and that inability is the benefit rather than a limitation to work around.
  when_to_use: Use when the difficulty is deciding what to attend to rather than holding too many values — architectural or design questions, or a codebase too large to hold in working memory at all, where the useful move is mapping it on a whiteboard under a notation that admits only one kind of element. Also use when the model has to be shown to someone else, since a constrained notation makes relationships visible that are otherwise hidden in the code.
  when_not_to_use: Do not swap in a constrained notation when you need exactly the values a line-by-line trace produces; a diagram that cannot express intermediate state is the wrong tool for a calculation you are stepping through. It is also the wrong move when you do not yet know which kind of element matters, because choosing the constraint prematurely hides the thing you were looking for.
  absorbed_from_object_id: none
---

# Externalize Intermediate State When Tracing Code

## Pattern Rule
**IF** mentally executing code requires tracking more changing values and operations than you can reliably hold at once
**THEN** write each relevant intermediate value beside its line or in a trace table and advance the execution one step at a time.

## Do
- Record a variable immediately after the statement that changes it, so the state and the responsible operation stay adjacent.
- Keep only values that influence the behavior under investigation; use the written trace to free working memory for deciding what the next operation means.
- Treat the urge to scribble down values as evidence that the trace has exceeded working-memory capacity, not as a failure that more concentration will fix.

## Don't
- Don't recompute an earlier value from memory every time a later line needs it; repeated reconstruction consumes the same capacity needed to understand the control flow.
- Don't turn the trace into an indiscriminate dump of every symbol, because irrelevant state recreates the overload on paper.

## Checklist
- Does every recorded state change point to the exact line that produced it?
- Can I resume the trace after an interruption without reconstructing prior values?
- Does the table contain enough state to explain the behavior but omit values unrelated to the question?

## Notes
The BASIC conversion example remains difficult even when its keywords and operations are visible. Hermans annotates the listing with successive values and recommends a pen-and-paper or tabular trace when the small execution steps no longer fit in working memory. The move changes the job of working memory from storing the entire execution to processing one transition at a time.

`VAR_hermans_choose_a_constrained_model_to_focus_retrieval` retains **Pick a Model Whose Constraints Do the Focusing** as an alternative route to the same relief. Chapter 6 revisits externalization from the direction of the notation rather than the load: a model's constraints are what make it useful, because a state diagram can only carry variable values and an entity relationship diagram can only carry classes and their relationships, and that restriction forces attention onto one aspect of the problem and helps long-term memory surface the memories that bear on it. The chapter's own analogy is a child adding 3+5 on a number line, where the notation does the focusing; the programming case is mapping an architecture on a whiteboard because a large codebase will not fit in working memory at all. Reach for it when the problem is deciding what to attend to, and not when you need the specific intermediate values a step-by-step trace exists to produce.
