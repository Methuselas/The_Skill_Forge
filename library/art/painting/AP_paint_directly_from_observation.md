---
object_id: AP_paint_directly_from_observation
object_type: ap
name: Paint Directly From Observation
library_path:
- art
- painting
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: AP_plan_and_build_work_from_thumbnail_to_final
tags:
- painting
- direct_painting
- alla_prima
- observation
- block_in
- continuity
cross_links:
- rel: supports
  target_object_id: PAT_preflight_observed_rendering_for_constraints_and_failure_points
- rel: supports
  target_object_id: PAT_choose_block_in_strategy_by_visual_priority_and_subject_complexity
- rel: supports
  target_object_id: PAT_build_loose_surface_from_precise_visual_decisions
- rel: supports
  target_object_id: PAT_calibrate_observed_proportion_with_relational_sighting
- rel: supports
  target_object_id: PAT_design_whole_picture_as_interlocking_shape_pattern
- rel: supports
  target_object_id: PAT_control_edge_hardness_from_form_light_and_focus
- rel: supports
  target_object_id: PAT_choose_painted_edge_method_from_blending_color_steps_and_surface_state
- rel: supports
  target_object_id: PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum
- rel: supports
  target_object_id: PAT_resolve_visible_color_from_local_color_light_and_reflection
- rel: supports
  target_object_id: PAT_unify_palette_with_shared_color_influence
- rel: supports
  target_object_id: PAT_choose_color_strategy_to_fit_subject_purpose_and_viewing_context
- rel: related_to
  target_object_id: AP_diagnose_and_recover_failing_observed_rendering
- rel: supports
  target_object_id: PAT_map_observed_subject_as_interlocking_positive_and_negative_shapes
- rel: supports
  target_object_id: PAT_select_observed_evidence_to_serve_expressive_intent
- rel: supports
  target_object_id: PAT_sequence_paint_body_from_thin_to_thicker_as_passages_resolve
reference:
  source_title: 'Alla Prima II: Everything I Know About Painting—and More'
  author: Richard Schmid
confidence: high
references: []
variants: []
---

# Paint Directly From Observation

## Objective
Complete a direct observational painting by turning a live visual target into a sequence of trustworthy painted relationships while protecting the composition, value/light key, structural anchors, color harmony, edge hierarchy, and strength of the accepted start.

## Steps / Flow
1. **Enter with a pictorial target.** State what the painting is meant to convey and keep that target active without making it rigid. When the available observed facts compete for equal attention, apply `PAT_select_observed_evidence_to_serve_expressive_intent` so selection serves that target without sacrificing required structural truth. If a genuinely better idea appears, re-baseline deliberately rather than drifting unnoticed.
2. **Select the picture before technical work.** Apply `PAT_design_whole_picture_as_interlocking_shape_pattern` at this decision. Choose viewpoint, crop, arrangement where controllable, large interlocking shape pattern, focal hierarchy, and major directional flow. A composition that would require avoidable downstream repair does not pass this gate.
3. **Preflight the live conditions.** Apply `PAT_preflight_observed_rendering_for_constraints_and_failure_points` at this decision. Check subject stability, light, available time, viewpoint, difficult passages, and the intended handling route. Rescope when the conditions cannot support the planned result.
4. **Choose a start that protects the dominant risk.** Delegate to `PAT_choose_block_in_strategy_by_visual_priority_and_subject_complexity`. When named parts or internal assumptions bias placement, use `PAT_map_observed_subject_as_interlocking_positive_and_negative_shapes` as an independent shape check. Do not leave the searching phase until enough correct relationships exist that the intended direction can be clearly read.
5. **Protect the strength of the accepted start.** Apply `PAT_build_loose_surface_from_precise_visual_decisions` at this decision. Identify the large shape pattern, parent value families, color/light key, important edge organization, and compositional movement that make the start work. Later development may improve them but must not silently destroy them.
6. **Verify anchors before dependent development.** Apply `PAT_calibrate_observed_proportion_with_relational_sighting` at this decision. When drawing sensitivity warrants it, use relational sighting and trusted visible anchors before later shapes are allowed to depend on them.
7. **Establish the light and value organization.** Apply `PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum` at this decision. Characterize the dominant illumination and significant secondary/reflected influences. When value organization materially carries the picture, do not let local subdivision become authoritative until the major families survive a simplified whole-source read.
8. **Accumulate trustworthy passages at an accuracy-controlled pace.** Let placement, shape, value, color, and edge determine speed. When the chosen paint medium has meaningful body and uncertain passages may need revision, apply `PAT_sequence_paint_body_from_thin_to_thicker_as_passages_resolve` so physical commitment rises with certainty. A locally resolved passage may become a comparison field only after it is trustworthy enough to support later decisions.
9. **Build color relationally under the active illumination.** Apply `PAT_resolve_visible_color_from_local_color_light_and_reflection`, `PAT_unify_palette_with_shared_color_influence`, and `PAT_choose_color_strategy_to_fit_subject_purpose_and_viewing_context` at this decision. Let local color, light, reflection, and the accepted field govern each important patch. If the painter deliberately departs from observation, explicitly switch from literal matching to an internally coherent pictorial color strategy.
10. **Maintain an edge hierarchy.** Apply `PAT_control_edge_hardness_from_form_light_and_focus` and `PAT_choose_painted_edge_method_from_blending_color_steps_and_surface_state` at this decision. Before final accents become authoritative, rank the whole image's important edges. Place or reserve the strongest edge according to certainty and focal need; locally correct hard edges still fail if they destroy the intended hierarchy.
11. **Interrupt failure instead of painting through it.** Invoke `AP_diagnose_and_recover_failing_observed_rendering` whenever a significant supposedly resolved passage stops being trustworthy.
12. **Handle changing light deliberately.** If live illumination materially changes, either re-baseline the light model and reconcile dependent color or preserve the established key and stop/rescope; do not drift gradually between incompatible light states.
13. **Allow selective completion.** The painting does not need equal finish everywhere. Stop when the active pictorial statement is made and additional paint would no longer strengthen it.

## Notes
Direct painting is treated here as controlled visual comparison, not as a mandatory one-session recipe or a fixed block-in method. Painting-specific Patterns own wet-state handling and paint body; general Rendering and Observation Patterns continue to own the visual decisions themselves.
