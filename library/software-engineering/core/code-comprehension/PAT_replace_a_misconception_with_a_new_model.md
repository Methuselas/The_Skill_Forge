---
object_id: PAT_replace_a_misconception_with_a_new_model
object_type: pattern
name: Replace a Misconception Rather Than Correcting It
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 3 rough
lane_fit: teach
foundation_role: foundation
routing_class: teaching
specialization_axis: none
foundation_object_id: none
tags:
- misconceptions
- mental_model
- teaching
- onboarding
cross_links:
- rel: related_to
  target_object_id: PAT_recognize_a_misconception_by_its_three_marks
- rel: related_to
  target_object_id: PAT_guard_against_an_outdated_mental_model_under_load
- rel: related_to
  target_object_id: PAT_choose_explanatory_metaphors_by_audience_schemata
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Replace a Misconception Rather Than Correcting It

## Pattern Rule
**IF** you are trying to clear a misconception, in yourself or in someone you are teaching
**THEN** supply a replacement model of the concept rather than a correction of the belief, because a misconception is held too confidently to be dislodged by being contradicted.

## Do
- Rebuild the concept, not the claim. Telling a novice that a variable can be changed does not work; they need a new understanding of what a variable *is*, which is what the literature calls conceptual change.
- Budget for it being slower than ordinary learning. Regular learning adds to an existing schema; conceptual change alters knowledge already in the long-term memory, and that difference is why misconceptions linger.
- Separate the fact from the practice when planning the work. Learning that Python is dynamically typed is a one-line fact; learning to stop reaching for types when making decisions in code is the conceptual change, and only the second one takes time.
- Name what has to be unlearned explicitly when moving between languages — some syntax, such as always declaring variable types, and some practices, such as relying on those types.

## Don't
- Don't expect being shown the flaw to be sufficient. Simply being presented with information about why your thinking is wrong often does not help, or does not help enough, and repeating the correction more firmly does not change that.
- Don't treat a cleared misconception as gone. What changes is which model gets retrieved, not whether the old one still exists, so the same belief can resurface later.
- Don't mistake fluent recall of the correct answer for conceptual change; someone can state the right rule and still reason from the old model under pressure.

## Checklist
- Am I offering a replacement understanding, or just contradicting the current one?
- Have I distinguished the fact to be learned from the practice that has to be relearned?
- What would this person have to stop doing, not merely start knowing?

## Notes
Conceptual change is the term for an existing conception being fundamentally changed, replaced, or assimilated by new knowledge. Hermans is precise that this — the change in existing knowledge rather than the addition of new knowledge to a schema — is what distinguishes it from other learning, and it is the reason the effort cannot be shortcut.

The practical consequence for anyone moving between languages is that a significant share of the work is unlearning rather than learning, and that share is invisible on a syllabus. It is also why the pattern is lane-tagged for teaching: the same asymmetry governs onboarding someone onto a codebase whose conventions contradict their previous one.

This pairs with the outdated-model pattern from chapter 6 rather than duplicating it. That one is about detecting an old model surfacing while you read; this one is about what it takes to change which model is there to surface.
