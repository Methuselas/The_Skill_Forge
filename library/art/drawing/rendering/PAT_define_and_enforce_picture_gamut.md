---
object_id: PAT_define_and_enforce_picture_gamut
object_type: pattern
name: Define and Enforce a Picture Gamut
library_path:
- art
- drawing
- rendering
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- color
- gamut
- palette
- color_strategy
- constraint
cross_links:
- rel: related_to
  target_object_id: PAT_trade_chroma_against_value_within_available_gamut
- rel: related_to
  target_object_id: PAT_choose_color_strategy_to_fit_subject_purpose_and_viewing_context
- rel: related_to
  target_object_id: PAT_unify_palette_with_shared_color_influence
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_gurney_audition_picture_gamuts_by_moving_a_mask
  variant_name: Audition Picture Gamuts by Moving a Mask
  variant_basis: method_sequence
  difference_from_foundation: Holds a chosen gamut shape or relationship constant while shifting or rotating it
    through hue space to compare whole-picture alternatives before execution.
  when_to_use: Use when the image needs a controlled palette but several overall hue biases could serve the same
    structural relationship.
  when_not_to_use: Do not confuse the audition diagram with the final picture; select by the image consequences,
    not by geometric elegance.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_prepare_value_strings_from_selected_gamut_colors
  variant_name: Prepare Value Strings From Selected Gamut Colors
  variant_basis: method_sequence
  difference_from_foundation: Pre-resolves a small number of useful value steps for principal gamut families so
    detailed execution starts from controlled color/value anchors rather than continuous improvisation.
  when_to_use: Use when a picture has stable major color families and premixed value steps would improve consistency
    across repeated passages or changing light planes.
  when_not_to_use: Do not force a fixed number of steps or prevent needed interpolation; the strings are anchors
    inside the gamut, not a mandatory swatch grid.
  absorbed_from_object_id: none
references: []
---

# Define and Enforce a Picture Gamut

## Pattern Rule
**IF** a picture needs deliberate color unity stronger than ad hoc palette restraint
**THEN** define an intentional region of allowed color relationships, choose boundary colors as subjective primaries, identify the gamut's relational neutral, and enforce that gamut during execution before importing any outside accent
**ELSE** use a broader palette when the subject or purpose genuinely requires unrestricted color variety.

## Do
- Choose boundary colors that define the intended extremes of the picture rather than defaulting to historical primary colors.
- Treat mixtures and intermediate notes inside the chosen region as available and outside regions as deliberately excluded.
- Identify the subjective neutral created by the gamut; it may be chromatic rather than physically achromatic.
- Expect mixtures between extreme parents to move inward toward lower chroma and budget that saturation cost when planning accents.
- Shape, rotate, widen, narrow, or shift the gamut before production to compare alternate schemes.
- Search the selected gamut boundary for a stronger accent before violating the approved constraint.

## Don't
- Confuse a chosen picture gamut with the medium's physical reproduction gamut.
- Keep out-of-gamut colors conveniently active during execution if the point of the constraint is to prevent drift.
- Assume an objective gray will read neutral inside a strongly biased gamut.

## Checklist
- The palette's boundary colors and relational neutral are explicit.
- Most picture colors can be explained as positions or mixtures inside the chosen gamut.
- Accents strengthen the image without quietly dissolving the constraint.

## Notes
A picture gamut is an intentional design subset of the colors a medium could physically produce. Its value is not the diagram itself but the discipline of choosing, auditioning, and then enforcing a coherent field of color relationships.

`VAR_gurney_audition_picture_gamuts_by_moving_a_mask` Holds a chosen gamut shape or relationship constant while shifting or rotating it through hue space to compare whole-picture alternatives before execution. Use it when when the image needs a controlled palette but several overall hue biases could serve the same structural relationship Avoid it when confuse the audition diagram with the final picture; select by the image consequences, not by geometric elegance .

`VAR_gurney_prepare_value_strings_from_selected_gamut_colors` Pre-resolves a small number of useful value steps for principal gamut families so detailed execution starts from controlled color/value anchors rather than continuous improvisation. Use it when when a picture has stable major color families and premixed value steps would improve consistency across repeated passages or changing light planes Avoid it when force a fixed number of steps or prevent needed interpolation; the strings are anchors inside the gamut, not a mandatory swatch grid .
