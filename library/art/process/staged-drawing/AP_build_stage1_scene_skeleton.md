---
object_id: AP_build_stage1_scene_skeleton
object_type: ap
name: Build the Stage 1 Scene Skeleton
library_path:
- art
- process
- staged-drawing
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: AP_progress_artifact_through_ratified_steps
tags:
- stage_1
- scene_skeleton
- structural_layout
- perspective
- continuity
cross_links:
- rel: supports
  target_object_id: PAT_develop_scene_through_registered_successors
- rel: supports
  target_object_id: AP_gate_staged_visual_work_by_approval
- rel: related_to
  target_object_id: AP_prepare_artifact_only_image_generation_handoff
- rel: supports
  target_object_id: PAT_choose_stage1_construction_by_readability
- rel: related_to
  target_object_id: AP_notate_a_figure_in_structural_order
- rel: prerequisite_for
  target_object_id: AP_build_stage2_complete_mass_block
- rel: supports
  target_object_id: PAT_recover_view_field_from_existing_image
- rel: supports
  target_object_id: PAT_preserve_articulated_limb_chain
reference:
  source_title: Guided Stage Revision Debugging and Stage Mechanics Review
  author: MaDin + GPT
confidence: high
references:
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage1_canonical_scene_skeleton.png
  caption: 'Canonical Broken Gate Stage 1 scene-wide skeleton: the exact accepted
    Stage 0 picture is carried forward as sparse figure gesture/skeleton construction
    plus scene perspective, axes, planes, and object scaffolds.'
  derived_from: guided Broken Gate canonical Drawing precedent run, accepted Stage
    1
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/debug/broken_gate_debug_stage1_mannequin_mass_leakage_INVALID.png
  caption: 'INVALID / NON-CANONICAL Stage 1 negative precedent: the scene scaffold
    is structural but humanoids leak Stage 2 mass through cylindrical limbs, solid
    torso volumes, and mannequin joints.'
  derived_from: guided Broken Gate Stage 1 rejection and correction
  origin: first_party_source
  review: passed
variants: []
---

# Build the Stage 1 Scene Skeleton

## Objective
Translate an approved Stage 0 picture proposition into the simplest scene-wide structural scaffold that locates and connects every important subject and environment element without changing the composition or jumping ahead into mass, anatomy, lighting, texture, or rendering.

## Steps / Flow
1. **Enter only from an approved picture proposition.** Use the actual approved Stage 0 image in the conversation as the composition authority. If no Stage 0 root has been approved in interactive staged mode, return to Stage 0 rather than constructing a preferred option.
2. **Register the exact approved picture as the productive predecessor.** Apply `PAT_develop_scene_through_registered_successors`. When the host exposes image editing/reference continuity, use that actual accepted image as the source rather than independently regenerating the scene from the verbal brief. Register every important figure, weapon, prop, architecture element, and environment anchor that must survive.
3. **Switch from picture Search to structural Control.** Preserve camera, crop, major subject apparent scale/placement, dominant action, large negative spaces, hierarchy, scene inventory, and story read. Search is allowed only inside unresolved structural questions that do not recompose the picture.
4. **Lay down the scene framework first.** Apply `PAT_choose_stage1_construction_by_readability` at this decision. Apply `PAT_recover_view_field_from_existing_image` at this decision. Establish horizon/eye level and perspective directions where relevant, then place skeletal axes, centerlines, contact points, support lines, object orientation lines, simple enclosing planes/boxes, and other sparse construction needed to locate every important scene object.
5. **Skeletonize all scene participants, not only the hero.** For articulated figures, animals, wings, fins, or invented appendages, apply `PAT_preserve_articulated_limb_chain` at the chain decision so each member remains continuous from parent socket through joints to terminal form. Figures receive action lines, torso/pelvis orientation, limbs/joints, head placement, and contact chains. Architecture, vehicles, props, pipes, signs, terrain, weapons, and other objects receive their simplest axes, planar frames, boxes, centerlines, or attachment scaffolds sufficient to preserve placement and perspective.
6. **Compile the productive image through the artifact-only handoff.** Use `AP_prepare_artifact_only_image_generation_handoff` and the Productive Image Contract below. The primary artwork itself must use the structural vocabulary; do not demonstrate structure in side examples around a more developed central image.
7. **Check the whole scene against Stage 0.** Compare camera, crop, subject scale/placement, major silhouette trajectory, negative spaces, environment arrangement, and depth path. If the better structural solution would materially recompose the picture, rollback to Stage 0 instead of silently improving it here.
8. **Revise only structural defects at this step.** Missing joints, bad attachments, inconsistent perspective, weak contacts, or incomplete scene scaffolding remain Stage 1 problems. A user rejection of the composition is a Stage 0 restart, not a Stage 1 refinement.
9. **Complete when Stage 2 can be built without guessing.** The result should read as a coherent scene-wide skeleton even with all shading, texture, and surface detail removed. Stop at that point and return control to the staged controller.
10. **Use the Stage 1 handoff prompt.** End with explicit next actions such as: “Approve this structure to continue, tell me any structural revisions you want, or reject it and we'll return to the appropriate earlier stage.” Keep the language structural so Stage 1 does not imply permission to repaint or redesign.
### Productive Image Contract
- **Artifact form:** one full-frame sparse structural drawing of the selected composition. No title, captions, notes, legends, inset examples, side demonstrations, or alternate versions.
- **Preserve:** camera, crop, dominant action, subject placement/apparent scale, depth arrangement, major negative spaces, and environment placement from the selected composition.
- **Figure vocabulary:** action line; head egg/ball; ribcage primitive; pelvis wedge/primitive; shoulder and hip axes; limb centerlines; joint markers; crude hand/foot blocks; support/contact chains; weapon axis plus a simple placeholder block where needed.
- **Environment vocabulary:** horizon and perspective guides; wall/ground planes; object axes; centerlines; boxes; simple frames; attachment points; single-line cables/pipes; other minimum location scaffolds.
- **Identity visibility:** preserve proportion, broad hair mass, shoulder/gear silhouette, and other structure-scale anchors. Known surface design remains withheld.
- **Withhold:** eyes, nose/lips, rendered face, hair strands, costume seams, emblems, armor surface detailing, musculature, fabric folds, finished hands, detailed weapon surfaces, shaded volumes, value design, color, lighting, glow, reflections, materials, texture, atmospheric effects, finished signage, and decorative architecture.
- **Global ceiling:** every important region uses the same sparse structural vocabulary. If removing the construction marks would leave a recognizable developed illustration, the artifact is too advanced.
- **Stop:** when every important scene element is structurally located and connected well enough for solid forms to be added without guessing.

## Notes
Stage 1 answers **where everything is and how it is structurally connected**. It is intentionally less impressive than a rough render. Its value is that every later mass can be built from an explicit scaffold rather than invented during rendering.
