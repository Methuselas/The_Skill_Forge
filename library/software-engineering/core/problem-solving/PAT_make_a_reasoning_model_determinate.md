---
object_id: PAT_make_a_reasoning_model_determinate
object_type: pattern
name: Add Detail Until the Model Admits One Reading
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- problem_solving
- models
- working_memory
- reasoning
cross_links:
- rel: related_to
  target_object_id: PAT_choose_a_problem_representation_before_solving
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Add Detail Until the Model Admits One Reading

## Pattern Rule
**IF** the model you are reasoning from is consistent with more than one arrangement of the real system
**THEN** add detail until only one arrangement fits, because reasoning accuracy tracks how tightly the model pins the situation down, not how elegant or general it is.

## Do
- Test a model by asking what else it would also be true of; if you can describe a second, materially different system that satisfies every statement in your model, the model is still indeterminate.
- Pin down the relations that constrain layout or ordering, not just the ones that name participants — "the plate is between the spoon and the fork" fixes an arrangement that "the fork is to the left of the spoon" leaves open.
- Spend the extra effort on complex or unfamiliar code specifically. That is where an accurate model takes work and also where it pays, since simple code can usually be modeled without deliberate effort.
- Prefer a concrete instance over an abstract sketch when you are about to answer a specific question about the system.

## Don't
- Don't mistake a model you can state quickly for a model you can reason from; the fast, underspecified version is exactly the one that produces confident wrong answers.
- Don't add detail indiscriminately — the goal is to remove rival interpretations, so detail that does not eliminate an alternative is just load.
- Don't treat an indeterminate model as harmless because nothing has gone wrong yet; the cost shows up as an error rate, not as an immediate failure.

## Checklist
- Can I draw a second arrangement that satisfies everything my model asserts?
- Which specific statement would rule that second arrangement out, and do I know it to be true?
- Am I about to answer a question this model was never detailed enough to settle?

## Notes
Johnson-Laird's table-setting experiment is the evidence, and its second half is the part that matters here. Participants heard descriptions of a place setting, did unrelated tasks, and then ranked four candidate descriptions. Some had received determinate descriptions matching exactly one arrangement; others received indeterminate ones matching several. The determinate group chose correctly 88% of the time against 58% for the indeterminate group — a gap large enough that Hermans draws the direct programming conclusion that "the more details a mental model has, the easier it is to reason about the system at hand and to answer questions about the system correctly."

The two settings the descriptions had to distinguish are worth picturing: the two arrangements differ only in where the plate sits relative to the fork and spoon, which is precisely the distinction an indeterminate description fails to carry.

The same experiment separately establishes that people build a model at all rather than storing sentences — participants ranked descriptions they had never heard, but which could be inferred from the layout, nearly as highly as the ones they had actually been given.
