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
variants:
- variant_id: VAR_cognition_design_patterns_as_chunks
  variant_name: Use Known Design Patterns as Comprehension Chunks
  variant_basis: emphasis
  difference_from_foundation: Makes familiar design patterns an explicit readability device because a maintainer who recognizes the pattern can process its collaborating parts as one semantic chunk instead of reconstructing them line by line.
  when_to_use: A design problem has a fitting established pattern and the intended maintainers know the pattern or its presence can be made explicit.
  when_not_to_use: The pattern is unfamiliar to the team, does not fit the problem, or adds more indirection than the maintenance task earns.
  absorbed_from_object_id: none
- variant_id: VAR_cognition_semantic_beacons
  variant_name: Plant Simple and Compound Semantic Beacons
  variant_basis: emphasis
  difference_from_foundation: Treats meaningful names, operators, control structures, comments, and cooperating code elements as deliberate signals that let a reader form and test a high-level hypothesis about the data structure or algorithm.
  when_to_use: Writing or revising code whose purpose is difficult to infer quickly from a local reading.
  when_not_to_use: A proposed signal would be redundant, misleading, or inconsistent with the behavior it is meant to reveal.
  absorbed_from_object_id: none
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

## Don't
- Don't force readers to decipher vague single-letter labels or reconstruct meaning from an unstructured block of text.
- Don't separate a critical instruction from where it is needed, leaving it discovered too late to act on.

## Checklist
- Can a skim-reader state the subject, the result, and the required inputs without decoding?
- Is every vague label replaced by a name describing the thing's role?
- Does each precondition and quantity sit where it is used?

## Notes

Long demonstrates poor readability with a brownie recipe rewritten as one wall of text: no title, vague labels ("A," "B," "C"), unstructured steps, and the oven-preheat instruction buried at the end. He maps each defect to a code equivalent — a reader struggles to see what the code does, how, what it needs, and what it returns. This is the "readable" pillar's foundation; chapter 5 specializes it into descriptive names, comment use, nesting depth, and named arguments. The paired drill runs the recipe rewrite as practice.

Variant `VAR_cognition_design_patterns_as_chunks` (The Programmer's Brain, Chapter 2) adds a pattern-literacy route: when a fitting design pattern is familiar to the maintainer or explicitly identified, its participants can be processed as one known structure rather than rediscovered line by line. Use it only when the pattern fits and the audience can recognize it; an unfamiliar or gratuitous pattern adds indirection instead of reducing cognitive load.

Variant `VAR_cognition_semantic_beacons` (The Programmer's Brain, Chapter 2) adds a signaling route. Meaningful names and operators are simple beacons, while combinations such as paired left/right fields or a complete loop header become compound beacons that reveal a data structure or operation. Use these signals to support a correct high-level hypothesis, but do not add redundant or misleading cues merely to make code look explanatory.
