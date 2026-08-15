---
object_id: AP_teach_craft_from_orientation_to_generation
object_type: ap
name: Teach Craft From Orientation to Generation
library_path:
- teaching
- learning-design
stage_binding: 0 design
lane_fit: teach
foundation_role: foundation
routing_class: teaching
specialization_axis: none
foundation_object_id: none
tags:
- teaching
- curriculum_design
- worked_examples
- generative_practice
- vocabulary
- transfer
cross_links:
- rel: related_to
  target_object_id: PAT_match_models_to_learner_output_scale
- rel: related_to
  target_object_id: PAT_shrink_practice_scope_to_preserve_revision
reference:
  source_id: david_starkey_creative_writing_four_genres_in_brief_3e
  source_title: 'Creative Writing: Four Genres in Brief, Third Edition'
  author: David Starkey
  publish_date: '2017'
  media_type: PDF
  locator: u001, physical pp. 12-14
  evidence_type: text
confidence: medium
references: []
variants:
- variant_id: VAR_starkey_teach_writing_genre_with_kick_starts_and_anthology
  variant_name: Teach a Writing Genre With Kick-Starts and Anthology
  variant_basis: context
  source_id: david_starkey_creative_writing_four_genres_in_brief_3e
  source_title: 'Creative Writing: Four Genres in Brief, Third Edition'
  locator: u001, physical pp. 12-14
  difference_from_foundation: 'Applies the general sequence to a writing genre: sketch the genre parameters, analyze three concise literary models by craft element, summarize how each element can be used, introduce terms at first use, provide genre-specific kick-starts, and follow with a short anthology spanning traditional and experimental work.'
  when_to_use: Use when learners need to move from recognizing a writing genre to producing a bounded draft while seeing more than one legitimate style within the form.
  when_not_to_use: Do not force genre terminology, literary-model analysis, or an anthology stage onto a non-writing craft whose examples and generation routes work differently.
  absorbed_from_object_id: none
---

# Teach Craft From Orientation to Generation

## Objective
Design a compact craft-learning unit that moves learners from recognizing the target form, through seeing its decisions in complete models, to generating and reviewing a viable attempt of their own.

## Steps / Flow
**Entry Conditions**
- The target craft or form and available teaching time are known.
- The expected learner artifact has a bounded, revisable scope.
- A small set of complete models can be studied within that scope.

**Persistent Invariants**
- Analysis must end in an action the learner can attempt.
- Models must be strong enough to study and small enough to inspect closely.
- Vocabulary supports recognition; it does not replace making decisions in an artifact.
- Generative exercises open more than one path into practice without prescribing one finished result.

**Flow**
1. **Orient the craft.** Sketch the form’s broad parameters and connect them to abilities learners already have, including relevant similarities and differences with familiar work.
2. **Establish a compact model set.** Choose a few complete examples at the learner assignment’s scale. Include enough variation to prevent one example from masquerading as the only valid route.
3. **Study models for decisions.** Identify how each example handles the craft’s governing elements rather than treating the example as content to recall.
4. **Translate each element into use.** After discussing an element, state the practical choice it gives the learner, the effect it can create, and a boundary or failure mode.
5. **Surface working vocabulary.** Introduce key terms at first meaningful use and retain a compact reference learners can revisit during practice.
6. **Open generation.** Offer several short starting routes suited to the craft so a blocked learner can begin from different stimuli, constraints, or subproblems.
7. **Return to varied examples.** Use additional models after the first attempt to deepen possibilities, challenge the learner’s first default, and provide material for comparison and revision.

**Failure / Rollback Rules**
- If a model consumes the session but cannot be inspected closely, replace it with a smaller complete example.
- If learners can name elements but cannot apply them, rewrite each element summary as a concrete choice and consequence.
- If starting exercises yield copies of one model, widen the model set or vary the entry routes.
- If production leaves no time for response and revision, reduce artifact scope before adding more instruction.

**Completion Criteria**
- Learners can describe the target form’s working parameters without treating them as one rigid formula.
- Each model contributes at least one identifiable move that can be attempted.
- Key terms are attached to decisions visible in the examples.
- Learners have multiple viable starting routes and enough time to produce a bounded attempt.
- The model set exposes more than one legitimate way to work within the craft.

## Notes
Starkey describes this sequence through writing instruction, but its learner decision travels: orient the form, study compact complete models, translate observations into usable moves, support recognition with vocabulary, open generation, then compare against a broader range. The writing-context route is retained as `VAR_starkey_teach_writing_genre_with_kick_starts_and_anthology`; it specializes the model set into literary works, the working vocabulary into genre elements, the starting routes into kick-starts, and the later comparison set into a short anthology spanning established and experimental writing.
