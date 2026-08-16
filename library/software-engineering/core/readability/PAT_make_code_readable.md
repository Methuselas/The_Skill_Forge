---
object_id: PAT_make_code_readable
object_type: pattern
name: Write Code That Reads Like a Well-Structured Recipe
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- readability
- naming
- code_structure
- comprehension
cross_links:
- rel: related_to
  target_object_id: DRILL_diagnose_and_rewrite_unreadable_procedure
- rel: related_to
  target_object_id: PAT_use_beacons_to_test_code_hypotheses
- rel: prerequisite_for
  target_object_id: PAT_use_descriptive_names
- rel: prerequisite_for
  target_object_id: PAT_comment_why_not_what
- rel: prerequisite_for
  target_object_id: PAT_favor_readability_over_brevity
- rel: prerequisite_for
  target_object_id: PAT_follow_a_consistent_coding_style
- rel: prerequisite_for
  target_object_id: PAT_minimize_nesting_with_early_returns
- rel: prerequisite_for
  target_object_id: PAT_use_named_arguments_for_readable_calls
- rel: prerequisite_for
  target_object_id: PAT_replace_primitives_with_descriptive_types
- rel: prerequisite_for
  target_object_id: PAT_name_unexplained_values
- rel: prerequisite_for
  target_object_id: PAT_use_anonymous_functions_only_when_small
- rel: prerequisite_for
  target_object_id: PAT_adopt_language_features_when_best_tool
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Write Code That Reads Like a Well-Structured Recipe

## Pattern Rule
**IF** another engineer — or future you — will need to read this code to review, debug, or extend it
**THEN** structure it so a reader can quickly answer what it does, how it does it, what inputs or state it needs, and what it produces, the way a good recipe has a title, ordered steps, named ingredients, and information placed where it is used.

## Do
- Give the code an up-front "title" through clear naming and entry points, so a reader learns what it is about without reading the whole thing.
- Present logic as discrete steps or subproblems instead of one undifferentiated wall.
- Name things for their role — "the bowl with melted butter and chocolate," not "A."
- Keep related information together: put a quantity next to its ingredient, and state a precondition (preheat the oven) where it matters, not stranded at the end.
- Reach for an established design pattern where one genuinely fits and the maintainers know it, or can be told it is there. A reader who recognises the pattern takes in its collaborating parts as one structure instead of rebuilding them line by line.
- Plant beacons on purpose. Meaningful names, operators, and control structures are simple ones; combinations such as paired left and right fields, or a complete loop header, are compound ones that let a reader form and test a hypothesis about the data structure or algorithm before reading the details.

## Don't
- Don't force readers to decipher vague single-letter labels or reconstruct meaning from an unstructured block of text.
- Don't separate a critical instruction from where it is needed, leaving it discovered too late to act on.

## Checklist
- Can a skim-reader state the subject, the result, and the required inputs without decoding?
- Is every vague label replaced by a name describing the thing's role?
- Does each precondition and quantity sit where it is used?

## Notes

Long demonstrates poor readability with a brownie recipe rewritten as one wall of text: no title, vague labels ("A," "B," "C"), unstructured steps, and the oven-preheat instruction buried at the end. He maps each defect to a code equivalent — a reader struggles to see what the code does, how, what it needs, and what it returns. This is the "readable" pillar's foundation; chapter 5 specializes it into descriptive names, comment use, nesting depth, and named arguments. The paired drill runs the recipe rewrite as practice.

Both of the last two Do items come from the chunking research (The Programmer's Brain, ch. 2), and both carry the same limit: they work on what the reader already holds, so neither is free. A design pattern the team does not know is indirection rather than a chunk, and a pattern forced onto a problem it does not fit costs more than the maintenance task earns. A beacon that is redundant, misleading, or inconsistent with the behaviour it advertises is worse than none, because a reader who tests a hypothesis against it draws the wrong conclusion with confidence. The reader-side counterpart is `PAT_use_beacons_to_test_code_hypotheses`; this card is the writer's half of the same mechanism.
