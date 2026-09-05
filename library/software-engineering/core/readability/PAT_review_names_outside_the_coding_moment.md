---
object_id: PAT_review_names_outside_the_coding_moment
object_type: pattern
name: Judge Names When You Are Not the One Solving the Problem
library_path:
- software-engineering
- core
- readability
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- code_review
- cognitive_load
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_separate_intrinsic_from_extraneous_load
- rel: related_to
  target_object_id: PAT_use_descriptive_names
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Judge Names When You Are Not the One Solving the Problem

## Pattern Rule
**IF** you want good names in a codebase
**THEN** schedule the naming judgement for a moment when you are not also solving the problem, because the point at which names are created is the point at which you have least capacity to choose them well.

## Do
- Treat a placeholder written mid-problem as expected rather than as a lapse. Working memory is at capacity building and using a mental model, so picking an easy name is the brain doing exactly what it should — Hermans's framing is that it makes sense from a cognitive perspective to avoid exceeding capacity.
- Come back to names in code review, which is a moment with spare capacity and a reader's perspective at once.
- Accept that the meaning often is not available yet. Sometimes what the thing actually is only becomes clear later in the programming process, so an early name was not merely rushed — it was premature.
- Extract the names from the code before judging them, so you are evaluating names rather than re-reading the logic.

## Don't
- Don't try to fix this by resolving to concentrate harder while coding. The cause is capacity, not diligence, and adding a naming decision to a full working memory competes with the problem you are there to solve.
- Don't leave the placeholders permanently either. The pattern moves the decision, it does not remove it, and `foo` shipped is a naming failure regardless of why it happened.
- Don't rely on names being raised organically in review. Allamanis found naming remarks in about one in four code reviews, which means three in four pass without any — a checklist is what makes it systematic.

## Checklist
- Was this name chosen while I was mid-problem, and has anything since clarified what the thing is?
- Am I judging the name with the code in front of me, or the name on its own?
- Does our review process direct attention at names explicitly, or only incidentally?

## Notes
The argument is a straight application of cognitive load to a practice question. Naming is hard in the abstract — Feitelson's experiment with almost 350 subjects found the median probability of two developers picking the same name for one of 47 objects was only 7% — and it is hardest precisely when done during problem solving.

The practical consequence is a scheduling one rather than a technique. Hermans is explicit that coding is not a great moment to think about names, and that reflecting on naming quality is better done outside the coding process, with code review named as the good moment. That is what makes this separable from the patterns about what a good name looks like: those tell you how to judge, this tells you when you are able to.
