---
object_id: PAT_measure_live_figure_with_center_out_visual_survey
object_type: pattern
name: Measure a Live Figure With a Center-Out Visual Survey
library_path:
- art
- drawing
- subjects
- figure
- construction
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- figure_drawing
- observation
- measurement
- live_model
cross_links:
- rel: related_to
  target_object_id: PAT_choose_stage1_construction_by_readability
- rel: related_to
  target_object_id: PAT_set_figure_proportions_with_adjustable_head_units
reference:
  source_id: andrew_loomis_figure_drawing_for_all_its_worth
  source_title: Figure Drawing for All It's Worth
  author: Andrew Loomis
  publish_date: Unknown
  media_type: PDF
  locator: u04, printed pp. 82-89
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_loomis_switch_reclining_measurement_to_pose_specific_relations
  variant_name: Switch Reclining Measurement to Pose-Specific Relations
  variant_basis: method_sequence
  source_id: andrew_loomis_figure_drawing_for_all_its_worth
  source_title: Figure Drawing for All It's Worth
  locator: u10, printed pp. 159-165
  difference_from_foundation: 'Adds Loomis''s reclining-figure exception to both ideal head-unit proportion and live-model survey: when perspective compresses the body so severely that normal head-count standards stop being informative, retain overall height/width, center/quarter checks, and local comparative distances that belong to the observed pose itself.'
  when_to_use: Use for reclining or strongly foreshortened observed figures whose projected proportions no longer resemble an upright head-unit chart.
  when_not_to_use: Do not abandon structural proportion entirely; the switch is from canonical upright ratios to pose-specific projected relationships, not from measurement to guesswork.
  absorbed_from_object_id: none
- variant_id: VAR_vilppu_crosscheck_3d_construction_with_2d_shape_survey
  variant_name: Cross-Check 3D Construction With a 2D Shape Survey
  variant_basis: method_sequence
  source_id: glenn_vilppu_basic_figure_drawing
  source_title: 'Drawing Manual: Basic Figure Drawing'
  locator: u09, physical pp. 123-136
  difference_from_foundation: 'Adds Vilppu''s explicit alternation between volumetric analysis and flat observational checks: construct the figure as 3-D forms, then verify placement with 2-D height/width, verticals, horizontals, diagonals, arcs, and positive/negative shapes; use disagreement between the two readings to expose placement or proportion drift.'
  when_to_use: Use when a figure is volumetrically convincing but no longer matches the observed pose, or when a carefully measured silhouette has become flat and structurally unconvincing.
  when_not_to_use: Do not reduce the drawing to mechanical copying or abandon 3-D understanding once the flat survey matches; Vilppu's point is to combine both modes, not choose one permanently.
  absorbed_from_object_id: none
- variant_id: VAR_bammes_reorient_reclining_figure_with_longitudinal_and_cross_axes
  variant_name: Reorient a Reclining Figure With Longitudinal and Cross Axes
  variant_basis: method_sequence
  source_id: gottfried_bammes_wir_zeichnen_den_menschen
  source_title: 'Wir zeichnen den Menschen: Eine Grundlegung'
  locator: u08, printed pp. 290-297
  difference_from_foundation: 'Adds Bammes''s spatial setup for reclining observation: when the body''s usual upright orientation no longer helps, first mark the projected body mid-axis and a small set of transverse stations through major structural levels such as the shoulder girdle, lower rib cage/abdominal fold, pelvis/pubic level, knee, and foot. Let perspective compress the intervals that recede and open the nearer ones; only then insert the head, rib-cage, pelvic cores, and simplified limbs. This turns the unfamiliar horizontal pose into a depth-organized scaffold before local contour or anatomy.'
  when_to_use: Use for lying or strongly foreshortened figures from life or fixed reference when the body is hard to orient as one coherent spatial object.
  when_not_to_use: Do not turn every minor joint into an equal measuring station or cover a simple view with unnecessary cross-lines. Keep only the axes that materially clarify depth, and use freer construction for invented poses that do not require observational surveying.
  absorbed_from_object_id: none
---

# Measure a Live Figure With a Center-Out Visual Survey

## Pattern Rule
**IF** an observed figure must be placed accurately from life or a fixed reference
**THEN** establish the overall height and width, locate a reliable center and major divisions, and work outward by checking horizontal levels, vertical plumbs, and sighted angle continuations against already-known points
**ELSE** use freer construction when exact observational placement is not the task

## Do
- Fix top, bottom, overall width, and a central reference before chasing small landmarks.
- Compare where important points fall directly across from or beneath one another.
- Extend difficult angles until they intersect a known level or plumb relationship.
- Recheck from known points as the drawing expands rather than accumulating unverified local measurements.
- Let the survey support the mannikin and mass construction instead of replacing structural understanding.

## Don't
- Do not duplicate the model by measuring every contour fragment independently.
- Do not measure with a changing arm length or inconsistent viewing setup.
- Do not let one mistaken anchor propagate unchecked through the whole figure.
- Do not apply this observational procedure as a mandatory invention workflow when no model/reference is being copied.

## Checklist
- Overall height/width and major divisions agree before details.
- Several important landmarks can be verified by both level/plumb and angular relationships.
- The resulting figure can still be reduced to a coherent Stage 1 construction rather than a traced contour map.

## Notes
Loomis calls this an “intelligent measurement” procedure rather than mere duplication. Its strength is relational redundancy: points are located from multiple known alignments, so observational accuracy can be checked while the figure remains structurally understood.

`VAR_loomis_switch_reclining_measurement_to_pose_specific_relations` retains **Switch Reclining Measurement to Pose-Specific Relations** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_vilppu_crosscheck_3d_construction_with_2d_shape_survey` retains **Cross-Check 3D Construction With a 2D Shape Survey** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_bammes_reorient_reclining_figure_with_longitudinal_and_cross_axes` retains **Reorient a Reclining Figure With Longitudinal and Cross Axes** as a bounded alternative; use it only under the conditions recorded in the variant metadata.
