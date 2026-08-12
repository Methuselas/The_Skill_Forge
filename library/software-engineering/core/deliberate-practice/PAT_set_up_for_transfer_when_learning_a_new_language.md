---
object_id: PAT_set_up_for_transfer_when_learning_a_new_language
object_type: pattern
name: Arrange the Conditions That Make Prior Knowledge Transfer
library_path:
- software-engineering
- core
- deliberate-practice
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- transfer
- learning
- deliberate_practice
- onboarding
cross_links:
- rel: related_to
  target_object_id: DRILL_elaborate_a_new_concept_against_known_ones
- rel: prerequisite_for
  target_object_id: PAT_expect_negative_transfer_between_similar_languages
- rel: related_to
  target_object_id: DRILL_compare_a_new_language_against_a_known_one
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u07, pp. 111-117
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Arrange the Conditions That Make Prior Knowledge Transfer

## Pattern Rule
**IF** you are about to learn a new programming language, framework, or library
**THEN** deliberately arrange the conditions that make your existing knowledge reachable, because useful knowledge does not transfer automatically and the factors that govern whether it does are partly under your control.

## Do
- Name the commonalities before you start. Being told that knowing one language will help with another makes you look for the similarities actively, and that looking is what produces the transfer — Hermans calls this the critical-attributes factor.
- Keep the context stable where you cheaply can. Transfer between two languages is more likely when you write both in the same IDE, which is a concrete argument for one editor across languages rather than a per-language toolchain.
- Lean on the areas you have genuinely mastered. An expert in one language carries more strategies, chunks, and models into the next than a novice does, so transfer scales with how well the source knowledge is held rather than merely with having met it.
- Run elaboration at the moment you meet the new concept. Explicitly relating it to what you already know is what raises the odds that the long-term memory search turns something up.
- When the goal is to broaden how you think rather than to ship, pick a language fundamentally unlike the ones you have. Moving from one nearby language to another is a false broadening — the book's image is going from "country music" to "Western music."

## Don't
- Don't assume expertise carries. Studies of chess found proficient players no better at remembering numbers or shapes and no better at related puzzles like the Tower of London, and Salomon's 1987 overview found the same for programming education — children acquired programming skills that did not transfer to other cognitive domains.
- Don't trust a strong feeling of similarity. Association is a real factor and an unreliable one: Java and JavaScript sound alike and are conceptually not much alike, so the felt connection can be stronger than the actual one.
- Don't let seeing yourself as an expert stop you doing beginner work. The frustration is real and the beginner activities — flashcards for syntax, deliberate comparison — are still the ones that work.

## Checklist
- What specific prior knowledge am I expecting to carry, and have I written it down before starting?
- Is anything about my environment gratuitously different from where the source knowledge lives?
- Am I relying on a similarity I have checked, or one that merely feels strong?

## Notes
Hermans splits the phenomenon in two. *Transfer during learning* is what happens when existing knowledge makes learning something new easier — figure 7.1 traces it, with new information arriving through sensory memory and the STM into working memory while the LTM is searched in parallel and any related material is fed into working memory alongside it. *Transfer of learning* is applying what you know in an unfamiliar situation, which is what cognitive scientists usually mean by the bare word "transfer," and which ranges from unconscious (closing the button on new trousers) to deliberate ("I indent loop bodies in Python — does JavaScript need that too?").

Six factors govern how much transfer occurs: mastery, similarity, context, critical attributes, association, and emotions. Three of them — context, critical attributes, and to a degree mastery — are things you can arrange in advance, which is what makes this a pattern rather than an observation. Emotions and association mostly matter as distortions to watch for.

The pessimistic half of the chapter is load-bearing rather than discouraging. Far transfer, between genuinely distant domains, is unlikely to happen spontaneously, so expect to learn substantial new syntax and new strategies before regaining your previous level. Practices shift too: much of what you know about reuse and abstraction in JavaScript has to be reconsidered in SQL.
