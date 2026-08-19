---
object_id: PAT_select_observed_evidence_to_serve_expressive_intent
object_type: pattern
name: Select Observed Evidence to Serve Expressive Intent
library_path:
- art
- drawing
- foundations
- observation
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- observation
- selection
- representation
- expressive_intent
- visual_hierarchy
- reference
cross_links:
- rel: related_to
  target_object_id: PAT_define_study_target_before_choosing_scope_medium_and_detail
- rel: foundation_of
  target_object_id: PAT_select_one_dominant_quality_for_animal_study
reference:
  source_title: Composition
  author: Arthur Wesley Dow
confidence: high
references: []
variants:
- variant_id: VAR_dow_force_selection_with_two_value_brush_constraint
  variant_name: Force Selection With a Two-Value Brush Constraint
  variant_basis: constraint
  difference_from_foundation: Restricts an observational study to two major values and a small number of decisive marks so the artist must choose which evidence carries form, texture, character, and complexity instead of recording every visible fact.
  when_to_use: Use when observation is becoming indiscriminate, when broad structure is being buried by local description, or when the study specifically needs to train selection and economy.
  when_not_to_use: Do not keep the two-value limit when subtle modeling, documentary accuracy, or a broader value range is essential to the assignment.
  absorbed_from_object_id: none
- variant_id: VAR_guptill_recompose_secondary_reference_elements_with_plausible_changes
  variant_name: Recompose Secondary Reference Elements With Plausible Changes
  variant_basis: constraint
  difference_from_foundation: Permits omission, relocation, size/value adjustment, or integration of secondary reference elements when their literal placement damages unity, provided the main subject remains truthful and the altered condition stays visually plausible.
  when_to_use: Use when an otherwise useful reference contains a distracting secondary tree, boat, shadow, accessory, or similar element that steals attention or fractures the composition.
  when_not_to_use: Do not alter primary identity, architecture, action, or other facts the assignment requires to remain documentary; this is selective recomposition, not arbitrary falsification.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_previsualize_result_as_painted_relationships
  variant_name: Previsualize the Result as Painted Relationships
  variant_basis: method_sequence
  difference_from_foundation: Translates a general urge to paint a subject into a rough pictorial target—broad shapes, color/value relations, edge character, focal emphasis, and intended degree of completion—before execution begins.
  when_to_use: Use when liking the subject is not enough to guide selection, emphasis, or stopping decisions during direct or observational rendering.
  when_not_to_use: Do not demand a fully detailed mental image before work begins; the target only needs enough visual specificity to guide major choices.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_choose_dominant_visual_element_and_subordinate_the_rest
  variant_name: Choose a Dominant Visual Element and Subordinate the Rest
  variant_basis: emphasis
  difference_from_foundation: Chooses whether color, value, drawing/form, design, or a small combination carries the main attraction, then keeps the other visual elements accurate enough to support it without developing all of them to equal intensity.
  when_to_use: Use when several attractive visual elements compete for equal emphasis or when an intangible aim must be translated into the concrete element that actually produces it.
  when_not_to_use: Do not weaken a supporting element below the level required for convincing structure, likeness, or the assignment.
  absorbed_from_object_id: none
---
# Select Observed Evidence to Serve Expressive Intent

## Pattern Rule
**IF** a representational drawing or painting is using nature or reference and the available facts compete for equal descriptive attention
**THEN** identify what the representation must express or accomplish, then select and emphasize the observed evidence that serves that purpose while preserving the structural truth and likeness the task requires
**ELSE** let neutral documentation or exact accuracy remain primary when faithful description is itself the job

## Do
- Name the representational purpose before deciding which observed facts deserve the strongest treatment: character, emotion, shape harmony, spatial relation, story, decorative fit, or another concrete job.
- Preserve the proportions, construction, identity, and spatial facts that the subject needs to remain convincing even when secondary information is simplified.
- Let line, mass, value, edge, surface, or detail become selective evidence rather than giving every visible fact the same descriptive weight.
- Compare possible selections against the whole image: an observation is useful when emphasizing it strengthens the intended statement without creating a larger structural error.
- When the assignment shifts toward documentation, likeness, or technical description, restore the level of literal evidence that the new purpose requires.
- Use the intended visual statement as a completion test: once added information no longer improves what the picture is meant to say, stop rather than increasing detail merely to make the surface look uniformly finished.

## Don't
- Do not treat expressive selection as permission for careless anatomy, perspective, proportion, or identity.
- Do not copy every available fact merely because it is visible in the reference.
- Do not substitute a stereotype or preconceived symbol for evidence actually present in the subject.
- Do not suppress facts that are essential to the assignment simply because they complicate the composition.
- Do not falsify an observed element merely because it is difficult to render; change or omit secondary evidence only when the declared pictorial purpose justifies the alteration and the result remains plausible.

## Checklist
- The purpose of the representation can be stated before refinement.
- The most emphasized observations directly support that purpose.
- Simplified or omitted information is secondary to the required likeness, structure, or story.
- The subject remains convincing after selective emphasis is applied.
- A more documentary assignment would trigger a consciously different balance between selection and literal accuracy.

## Notes
Observation supplies more information than most images need at equal strength. The transferable decision is therefore selective rather than anti-accuracy: determine what the representation is for, choose evidence accordingly, and keep enough structural truth that selection improves expression instead of excusing bad drawing. Exactness can still be the dominant criterion when documentation or likeness is the actual purpose.

`VAR_dow_force_selection_with_two_value_brush_constraint` turns that selection problem into a hard observational constraint: with only two values and a few decisive marks available, the learner must decide which facts actually carry the subject instead of recording everything visible. Restore a broader value range when the assignment depends on subtle modeling or documentation.

`VAR_guptill_recompose_secondary_reference_elements_with_plausible_changes` permits bounded changes to secondary reference elements when unity improves and the required primary truth remains intact.

`VAR_schmid_previsualize_result_as_painted_relationships` establishes a rough pictorial target before execution, while `VAR_schmid_choose_dominant_visual_element_and_subordinate_the_rest` decides which visual element carries the main attraction. For selective recomposition, difficulty alone is not a design reason: `VAR_guptill_recompose_secondary_reference_elements_with_plausible_changes` remains bounded by the picture's declared purpose and by the plausibility of the altered result.
