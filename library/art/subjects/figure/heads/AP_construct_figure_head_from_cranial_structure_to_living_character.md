---
object_id: AP_construct_figure_head_from_cranial_structure_to_living_character
object_type: ap
name: Construct a Figure Head From Cranial Structure to Living Character
library_path:
- art
- subjects
- figure
- heads
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- figure_drawing
- head_construction
- portrait
- character_design
- likeness
- expression
cross_links:
- rel: supports
  target_object_id: PAT_construct_head_from_cranial_ball_and_facial_wedge
- rel: supports
  target_object_id: PAT_design_surface_anatomy_as_microgesture_on_parent_forms
- rel: supports
  target_object_id: PAT_resolve_head_and_neck_last_from_context
- rel: related_to
  target_object_id: AP_notate_a_figure_in_structural_order
reference:
  source_title: PASS Art canonical synthesis
  author: Multiple accepted sources
confidence: high
references: []
variants: []
---

# Construct a Figure Head From Cranial Structure to Living Character

## Objective
Construct, rotate, individualize, and develop a human or humanoid figure head from a coherent cranial/facial structure into a living character while preserving viewpoint, large proportion, identity, and attachment to the figure when present. Increase specificity only when the current drawing stage permits it.

## Steps / Flow
1. **Enter with the head's job and context already understood.** Determine whether the task is a head study, portrait/likeness, invented character head, or a head embedded in a whole figure. If the head belongs to a figure whose body action or neck attachment is not yet trustworthy, return to the figure owner first. In whole-figure work, `PAT_resolve_head_and_neck_last_from_context` may establish the permitted direction and narrative/gaze requirement before detailed head development begins.
2. **Build the Stage-2 cranial/facial structure.** Apply `PAT_construct_head_from_cranial_ball_and_facial_wedge`. Establish one shared three-dimensional head system: cranial mass, facial projection/wedge, jaw relationship, centerline, brow/feature tracks, and the turn/tilt required by the view. Do not begin from separately drawn eyes, nose, mouth, hair, or expression.
3. **Use the lightest structural variant that solves the actual problem.** When the turn or tilt drifts, use `VAR_bridgman_block_head_inside_perspective_cage` or the applicable Hogarth rotation/plane variants. When feature placement drifts on a sound head block, use `VAR_loomis_construct_feature_placement_from_divided_cranial_ball`. When the head reads too round or mask-like, use the applicable planar/skull-boundary variants. These are conditional tools under the same head-construction decision, not a checklist to load all at once.
4. **Preserve identity in the large structure before local features.** For likeness, type, age, or character design, use only the applicable variants beneath `PAT_construct_head_from_cranial_ball_and_facial_wedge`: global proportion before features, cranial-envelope variation, age progression, structural exaggeration, or observed whole-to-part portrait blocking. Large head shape, cranial/facial balance, jaw projection, and feature-spacing system must carry the intended person or character before detail.
5. **Pass the Stage-2 head gate.** The head must survive reduction to simple masses: turn and tilt are unambiguous; paired features will belong to one perspective; cranial width/depth and facial projection are coherent; the jaw belongs to the same skull; and any neck/body attachment remains plausible. Do not use hair, wrinkles, eyelashes, costume, or rendering to rescue a weak head block.
6. **Develop living features at Stage 3 without abandoning their supports.** Use the applicable feature-development variants under `PAT_construct_head_from_cranial_ball_and_facial_wedge`, including support-to-cover construction for complex features, linked spherical eyes when needed, and bone-first/flesh-second character analysis. Features may become specific only after their parent skull and facial masses are stable.
7. **Treat hair as a head mass before strand information.** When hair materially changes silhouette or character, use `VAR_loomis_block_hair_as_large_mass_before_strands`. Keep the hairstyle attached to the skull and subordinate individual strand information to the accepted head volume and stage ceiling.
8. **Resolve expression, age, and surface anatomy as deformation of one living head.** When wrinkles, folds, creases, or other local surface anatomy materially carry expression, age, compression, or character, apply `PAT_design_surface_anatomy_as_microgesture_on_parent_forms`. Surface marks must wrap and deform the accepted cranial/facial forms rather than becoming independent symbols. Use age/type variants only when supported by the subject; do not average every head toward one canon.
9. **Check character continuity before finish.** Rotate mentally or compare against trusted views/reference when available. The same head type must survive turn, tilt, expression, and local feature refinement. If likeness or character identity changes because a feature was solved independently, return to the structural owner rather than polishing the drift.
10. **Stop at the requested resolution.** A construction study may correctly end at Stage 2; a developed head may end at Stage 3. If the caller requires finished Drawing Stage 4, return the structurally resolved head to that Drawing workflow rather than converting this AP into Rendering, Color, Paint, or another downstream medium.

## Notes
Figure-head construction is a reusable sub-action within Figure Drawing, portraiture, character design, comics, storyboards, and other Art workflows. The AP owns the general structural-to-living sequence; age, head type, likeness, feature, and stylistic methods remain bounded variants or downstream specializations so they stay available without becoming default noise.

A whole-figure workflow may establish only a simple head block when that is all the current stage needs. A prominent portrait-level head can delegate here and return to the parent figure without changing the body's accepted action, camera, or stage ceiling.
