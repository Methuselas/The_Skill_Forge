---
object_id: PAT_locate_a_learner_on_the_neo_piagetian_stages
object_type: pattern
name: Work Out Which Stage a Learner Is At Before Choosing How to Help
library_path:
- software-engineering
- core
- working-practice
stage_binding: 0 design
lane_fit: teach
foundation_role: foundation
routing_class: teaching
specialization_axis: none
foundation_object_id: none
tags:
- onboarding
- teaching
- mental_model
- working_practice
cross_links:
- rel: related_to
  target_object_id: PAT_account_for_the_curse_of_expertise_when_onboarding
- rel: related_to
  target_object_id: PAT_teach_along_a_semantic_wave
- rel: related_to
  target_object_id: DRILL_trace_a_state_table_for_calculation_heavy_code
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u13, pp. 207-211
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Work Out Which Stage a Learner Is At Before Choosing How to Help

## Pattern Rule
**IF** you are helping someone who is new to a language, codebase or paradigm
**THEN** establish which of the four neo-Piagetian stages they are operating at *for this material*, because the help that works at one stage is actively unhelpful at another.

## Do
- Test with tracing. A **sensorimotor** programmer cannot correctly trace a program — they have an incoherent model of execution. For them, explaining general principles away from the code does not land: someone stepping through database code is not helped by how the database is configured elsewhere. They need the execution model first.
- Recognise the **preoperational** stage by guessing. These programmers can trace small pieces and that is their *only* route to reasoning about code; they find it hard to explain what the same code means, and they reason inductively from a few traces. Expect them to seem erratic — a guess that is spot on, then five minutes later something unreasonable.
- Withhold diagrams until **concrete operational**. Lister found diagrams support thinking only from that stage; a preoperational programmer is focused on the code itself and will not benefit from being handed a picture.
- Use flashcards to move someone out of preoperational, by expanding their code vocabulary.
- At **concrete operational**, watch for overcommitment to a first strategy — the junior who spends a full day retrying a fix rather than stepping back to ask whether the approach is right. Reflection on one's own strategy is the formal-operational capability they do not have yet.
- Treat the stage as specific to the material, not to the person. Someone can be formal operational in Java and sensorimotor in Python, or formal in one codebase and lower in another.

## Don't
- Don't read the preoperational stage as lack of effort or ability. It is a necessary stage on the way to the next one, and it is the point at which onboarders most often conclude the newcomer is not smart or not trying.
- Don't assume a stage, once reached, is held. Learners temporarily fall back when meeting something new — someone who reads Python functions fluently may need to trace a few calls when first shown variadic functions with `*args` before reading them comfortably again.
- Don't offer the same support to everyone in a cohort. Diagrams that unlock one person will be noise to another in the same room.

## Checklist
- Can this person trace this code correctly, and can they say what it means?
- Are they reasoning from traces, or from recognising what they see?
- Is the help I am about to give one that works at their stage?

## Notes
Neo-Piagetism adapts Piaget's four developmental stages, and the adaptation is the useful part: the levels are domain-specific rather than general, so they describe a person's relationship with particular material rather than the person. Lister's work is what maps them onto programming.

Figure 13.1 shows all four applied to a three-line variable swap, and the progression is legible in what each programmer produces. The sensorimotor and preoperational programmers both say they do not know what it does; the difference is that the preoperational one has a trace table. The concrete operational programmer narrates the mechanism — z becomes y, y becomes x, x becomes z. The formal operational one states the meaning: the values of x and y are swapped.

The practical payoff is negative as much as positive. Three of the interventions in this chapter — general principles, diagrams, and unguided exploration — each fail at a specific stage, and knowing which is what stops a well-intentioned onboarder from adding load while believing they are removing it.
