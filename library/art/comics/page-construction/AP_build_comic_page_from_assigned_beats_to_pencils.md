---
object_id: AP_build_comic_page_from_assigned_beats_to_pencils
object_type: ap
name: Build a Comic Page From Assigned Beats to Pencils
library_path:
- art
- comics
- page-construction
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: AP_plan_and_build_work_from_thumbnail_to_final
tags:
- comics
- page_layout
- sequential_art
- penciling
- staging
- action_flow
cross_links:
- rel: related_to
  target_object_id: AP_plan_and_build_work_from_thumbnail_to_final
- rel: supports
  target_object_id: PAT_choose_viewpoint_to_strengthen_story_effect
- rel: supports
  target_object_id: PAT_repeat_with_variation_to_balance_coherence_and_interest
- rel: related_to
  target_object_id: AP_stage_story_scene_from_big_idea_to_camera_rough
- rel: related_to
  target_object_id: AP_resolve_temporal_movement_for_pose_or_sequence
reference:
  source_title: How to Draw Comics the Marvel Way
  author: Stan Lee and John Buscema
confidence: high
references: []
variants: []
---

# Build a Comic Page From Assigned Beats to Pencils

## Objective
Carry a page whose panel beats are already assigned from a whole-page action skeleton into coherent finished pencils while preserving beat order, continuity, page-level readability, and lockstep development so no polished panel hides a broken sequence.

## Steps / Flow
1. **Enter only after the page beats are assigned.** The ordered events and page boundary must already exist, and the intended action or event of each beat must be stateable. Full script breakdown, page-turn design, lettering, and balloon flow remain outside this AP unless another owner supplies them.
2. **Stage 1 — build the entire page skeleton at once.** Establish panel arrangement and rough every panel with action centerlines, simple figures, directional cues, state changes, and only enough environment to understand placement. When two or more assigned beats depict phases of one continuing physical action, delegate the bounded phase-selection/continuity problem to `AP_resolve_temporal_movement_for_pose_or_sequence` in sequence mode, then preserve those returned state changes inside the assigned panel beats. No panel may outrun the page into expensive finish.
3. **Pass the page-skeleton gate.** Before advancing, the whole page must make clear what happens in each panel, who is where, what changes between panels, the direction of important action, and how one panel hands the reader to the next without relying on anatomy or finish.
4. **Delegate difficult local staging only when necessary.** Apply `PAT_choose_viewpoint_to_strengthen_story_effect` at this decision. If one assigned beat is clear but its camera/action staging remains unresolved, call `AP_stage_story_scene_from_big_idea_to_camera_rough` as a bounded sub-action. When it returns, reinsert the result into the page and reject it if the locally strong camera breaks continuity, sequence, or page rhythm.
5. **Stage 2 — build masses across the whole page.** Convert skeleton figures and settings into simple spatial forms while preserving action, contacts, orientation, and panel-to-panel state. Draw through only where hidden structure is needed to prove attachment, overlap, foreshortening, or placement.
6. **Pass the mass gate.** Every panel's figures and major setting masses must agree with the Stage-1 skeleton before anatomy, costume, or detail becomes authoritative. A correct local volume that changes the page action or continuity fails.
7. **Stage 3 — flesh out the whole page in lockstep.** Develop anatomy, costume, props, and environment from the accepted masses while preserving the page's action centerlines, changing states, and spatial relationships.
8. **Pass the page-design gate.** Apply `PAT_repeat_with_variation_to_balance_coherence_and_interest` at this decision. Judge each panel as design inside the page. Variation in scale, camera, and composition should serve sequence clarity and emphasis rather than merely avoid repetition; the page must still read as one sequence rather than a set of unrelated illustrations.
9. **Recover at the earliest broken dependency.** Unclear event or handoff returns to the page skeleton; continuity/orientation failure returns to the whole-page skeleton; valid staging with bad volume/foreshortening returns to Stage 2; local anatomy/costume failure returns to Stage 3. Late polish does not justify page-wide local patching when an earlier page decision is wrong.
10. **Complete the pencil handoff.** The finished page must communicate the same beat sequence that worked in the skeleton, keep characters/props/orientation coherent across panels, preserve useful variation without sacrificing clarity, and remain ready for downstream finishing without redesigning the page.

## Notes
Persistent invariants are **BEATS**, **CONTINUITY**, **LOCKSTEP**, **HANDOFF**, and **PAGE**. This AP deliberately begins after panel beats are assigned; deeper pacing, lettering, page turns, and script breakdown remain future or separate owners rather than being inferred into this workflow.
