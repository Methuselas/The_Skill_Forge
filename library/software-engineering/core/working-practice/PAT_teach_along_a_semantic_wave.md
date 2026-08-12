---
object_id: PAT_teach_along_a_semantic_wave
object_type: pattern
name: Explain a Concept as a Wave — Abstract, Concrete, Abstract Again
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
- explanation
- memory
cross_links:
- rel: related_to
  target_object_id: PAT_locate_a_learner_on_the_neo_piagetian_stages
- rel: related_to
  target_object_id: DRILL_elaborate_a_new_concept_against_known_ones
- rel: related_to
  target_object_id: PAT_choose_explanatory_metaphors_by_audience_schemata
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u13, pp. 211-213
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Explain a Concept as a Wave — Abstract, Concrete, Abstract Again

## Pattern Rule
**IF** you are explaining a concept to someone meeting it for the first time
**THEN** run the explanation through all three positions — what it is for, then the concrete detail, then back up to the general form — because an explanation that stops at either end leaves the concept unusable.

## Do
- Start at the top with what the concept is for and why it is worth knowing. A variadic function is useful because it lets you pass as many arguments as the situation requires.
- **Unpack** downward into the specifics. In Python a `*` marks it, and the arguments arrive as a list — so there are not really multiple arguments, there is one argument holding all of them as elements.
- **Repack** back upward, stepping away from the details until the learner is comfortable with the general shape again. This is the step that gets skipped and the one that does the storing.
- Support repacking explicitly by asking what the new concept has in common with things the learner already knows. The integration into long-term memory is relational — "C++ supports variadic functions, Erlang does not" is what repacking produces.
- Give the learner both registers. Experts naturally talk in generic, abstract terms, and novices need the abstract *and* the concrete, not a choice between them.

## Don't
- Don't **high flatline** — staying abstract throughout. A newcomer can learn that Python has variadic functions and why they are useful and, never having seen the syntax, still have everything left to learn.
- Don't **low flatline** — opening with the details. "You make a variadic function with a `*` and Python sees the arguments as one list" means little to someone who does not yet know when to want one.
- Don't run a **downward escalator** — descending correctly from abstract to concrete and then moving on without repacking. You have shown the why and the how and left no time to integrate either.
- Don't assume the descent alone is the teaching. Two of the three antipatterns are failures of the return trip or of never leaving the top; only one is about the detail itself.

## Checklist
- Did I say what this is for before saying how it works?
- Did I come back up, or did I stop at the syntax?
- Have I asked what this reminds them of?

## Notes
The semantic wave is Karl Maton's, and figure 13.2 draws it as a curve descending from abstract into concrete and rising again, with the two transitions labelled unpacking and repacking.

Figure 13.3 is worth looking at because it explains a name the prose leaves opaque. Each of the three antipatterns is drawn as a red overlay on the correct black wave: a flat red line along the top for high flatlining, a flat red line along the bottom for low flatlining, and — for the third — a series of red strokes each descending from abstract to concrete without returning. That is why it is "downward escalator**s**", plural: the failure is not one missed repacking but a rhythm of them, concept after concept dropped to the concrete and abandoned there. The plural is invisible in the text.

This pairs with the stage pattern rather than duplicating it. That one decides what kind of help a learner can use; this one shapes any individual explanation once you have decided to give one.
