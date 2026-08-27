---
object_id: PAT_design_drapery_from_tension_points_and_forces
object_type: pattern
name: Design Drapery From Tension Points and Forces
library_path:
- art
- subjects
- figure
- anatomy
stage_binding: 3 rough
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- figure_drawing
- drapery
- folds
- tension
cross_links:
- rel: related_to
  target_object_id: PAT_carry_action_line_into_torso_centerline
- rel: related_to
  target_object_id: PAT_lace_separated_forms_with_valid_interconnections
- rel: related_to
  target_object_id: PAT_project_form_curves_from_camera_view
- rel: related_to
  target_object_id: PAT_render_material_from_optical_response
reference:
  source_title: 'Figure Drawing: Design and Invention'
  author: Michael Hampton
confidence: high
references: []
variants:
- variant_id: VAR_loomis_separate_garment_construction_from_body_driven_folds
  variant_name: Separate Garment Construction From Body-Driven Folds
  variant_basis: method_sequence
  difference_from_foundation: 'Deepens Hampton''s causal drapery Pattern by separating two sources of cloth behavior: folds
    created by the underlying body and tension points, and folds or flatness created by the garment''s own cut, seams, darts,
    gathers, bias, pleats, and intended fit. Reconstruct the figure first, then interpret only the cloth events justified
    by either source.'
  when_to_use: Use when clothing looks generically wrinkled, when fitted garments ignore seam logic, or when loose cloth fails
    to react to the body beneath it.
  when_not_to_use: Do not turn costume drawing into tailoring notation or draw every seam/button; retain only garment-construction
    information that materially changes fit, drape, or silhouette.
  absorbed_from_object_id: none
- variant_id: VAR_mattesi_read_clothing_as_evidence_of_body_action_and_form
  variant_name: Read Clothing as Evidence of Body Action and Form
  variant_basis: method_sequence
  difference_from_foundation: 'Uses the garment as diagnostic evidence for the body beneath it: solve the body action and form first, then read stretch/compression pairs, suspension and lock points, and constructed garment landmarks as clues to hidden volume, turn, foreshortening, and joint direction. Simplify wrinkle information after those cues have served the pose.'
  when_to_use: Use when clothing is obscuring the figure, when hidden body direction must be inferred from garment behavior, or when a clothed pose needs clearer evidence of underlying action and volume.
  when_not_to_use: Do not treat every seam, pocket, cuff, or wrinkle as equally important; retain only garment evidence that materially clarifies action, form, material, fit, or silhouette.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_stage_costume_practice_from_isolated_figure_to_scene_context
  variant_name: Stage Costume Practice From Isolated Figure to Scene Context
  variant_basis: method_sequence
  difference_from_foundation: 'Uses problem-scope sequencing as a costume-study method: first suppress most environmental
    complexity and solve the clothed figure as body plus garment under one coherent light, then deliberately reintroduce room,
    furniture, accessories, and scene context so scale, perspective, occlusion, and environmental lighting are tested after
    the garment/body relationship is controllable.'
  when_to_use: Use when costume or drapery study is being overloaded by background, perspective, lighting, and environmental
    information before the garment/body relationship itself can be diagnosed reliably.
  when_not_to_use: Do not treat background suppression as a final-image rule; graduate back into scene context because environment
    can alter cast shadows, reflected light, occlusion, silhouette, scale, and composition.
  absorbed_from_object_id: none
---

# Design Drapery From Tension Points and Forces

## Pattern Rule
**IF** fabric is being designed over or around a figure **THEN** identify where it is supported, pinched, suspended, twisted, compressed, or externally driven; route folds from those causes through gravity and host-form perspective; then simplify so the figure remains primary.

## Do
- Treat structural landmarks as potential tension points.
- Let gravity provide the default tendency unless motion, suspension, wind, or another force overrides it.
- Combine fold families when causes combine.
- Separate cloth variables instead of collapsing them into one heavy/light axis: weight and thickness influence hanging mass, sag, fold scale, and sense of load, while stiffness or hardness influences fold break, angularity, radius, and how abruptly direction changes; yielding and surface slickness can modify those responses further.
- Treat textile identity as two coupled systems: mechanical drape behavior (weight, stiffness, thickness, yielding, crease sharpness, fold scale/frequency) and optical surface behavior (sheen, roughness, reflection structure, highlight softness, absorption, and visible surface texture).
- Solve the causal fold structure first, then render the material response so fold behavior and surface appearance tell the same material story under the chosen light.
- Use specific reference when an exact textile must be identified; do not infer fibre identity from one cue such as sheen or fold softness alone.
- Carry gesture, asymmetry, overlap, hard/soft, and squash/stretch into the fabric.
- In animation or sequential work, treat the body as the primary action and the garment as subordinate secondary action: let changing cloth shapes follow from changing support points, body motion, gravity, momentum, and garment construction.
- Preserve causal continuity from state to state so a fold, flare, drag, or settling shape can be explained by what the body and cloth were doing immediately before it.

## Don't
- Do not draw folds as independent zigzags without a cause.
- Do not give every fold equal emphasis.
- Do not let garment detail obscure the pose.
- Do not let clothing appear to act independently from the body or physical forces when its changing shape should be a reaction to the primary action.

## Checklist
- The result shows the intended structural or functional change without contradicting the surrounding construction.
- In a sequence, changing drapery can be traced back to changing body action, support, gravity, momentum, or garment construction rather than frame-by-frame decorative wrinkle invention.
- Garment motion supports the primary acting body instead of competing with it as an unrelated action.

## Notes
Drapery becomes intelligible when folds are traced back to support, pull, compression, and release instead of copied as independent zigzags. In sequential work, the same causal rule extends through time: the body supplies the primary action and the garment reacts as secondary action, so cloth changes should remain explainable from the changing body, supports, gravity, momentum, and garment construction. Fabric behavior also depends on the cloth itself: under comparable forces, weight and stiffness change how broadly or frequently those folds can form. Textile identity is strongest when this mechanical behavior agrees with the cloth's optical response—such as sheen, roughness, reflection structure, highlight softness, and absorption—rather than when either fold mechanics or surface rendering is treated in isolation. Weight, thickness, stiffness or hardness, yielding, and surface slickness are related but not interchangeable: judge them from the actual wrinkle and hanging behavior instead of assuming, for example, that heavy cloth must also be rigid or that thin cloth must be soft. General optical causality remains owned by `PAT_render_material_from_optical_response`; this Pattern owns how that material evidence stays consistent with garment and drape mechanics.

`VAR_loomis_separate_garment_construction_from_body_driven_folds` retains **Separate Garment Construction From Body-Driven Folds** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_mattesi_read_clothing_as_evidence_of_body_action_and_form` reverses the usual reading direction once the garment is understood: use stretch/compression, hang points, openings, cuffs, waistbands, seams, pockets, straps, and other constructed landmarks as evidence of the body's hidden action and volume, then delete wrinkle information that does not help the pose, material, or form read.

`VAR_loomis_stage_costume_practice_from_isolated_figure_to_scene_context` adds a training progression: isolate the clothed figure long enough to diagnose body/garment relationships, then restore rooms, furniture, accessories, and environmental lighting so costume skill is tested inside real scene constraints rather than remaining an isolated-study trick.
