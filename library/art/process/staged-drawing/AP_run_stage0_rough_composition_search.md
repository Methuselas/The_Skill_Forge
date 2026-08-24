---
object_id: AP_run_stage0_rough_composition_search
object_type: ap
name: Run Stage 0 Rough Composition Search
library_path:
- art
- process
- staged-drawing
stage_binding: 0 design
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: AP_progress_artifact_through_ratified_steps
tags:
- stage_0
- composition_search
- thumbnails
- approval
- information_ceiling
cross_links:
- rel: related_to
  target_object_id: AP_alternate_search_and_control_cycles
- rel: supports
  target_object_id: AP_gate_staged_visual_work_by_approval
- rel: related_to
  target_object_id: AP_prepare_artifact_only_image_generation_handoff
- rel: related_to
  target_object_id: PAT_explore_stage0_with_thumbnail_set
- rel: related_to
  target_object_id: PAT_backcast_stage0_from_stage4_visual_proposition
- rel: related_to
  target_object_id: PAT_calibrate_stage_information_density_against_precedent
- rel: related_to
  target_object_id: PAT_track_force_continuity_through_action
- rel: related_to
  target_object_id: PAT_design_pose_against_center_of_gravity
reference:
  source_title: Guided Stage Revision Debugging and Stage Mechanics Review
  author: MaDin + GPT
confidence: high
references:
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage0_canonical_composition.png
  caption: 'Canonical Broken Gate Stage 0 composition root: low-information rough
    locks the low three-quarter camera, courier/spear diagonal, wagon anchor, gate
    framing, pursuer arrangement, road depth path, and major negative spaces without
    finished surface rendering.'
  derived_from: guided Broken Gate canonical Drawing precedent run, accepted Stage
    0
  origin: first_party_source
  review: passed
variants: []
---

# Run Stage 0 Rough Composition Search

## Objective
Produce a cheap, rough picture proposition that lets the user judge the intended finished image's composition before structural development begins, while keeping creative Search broad and preventing the assistant from selecting or advancing a candidate on the user's behalf.

## Steps / Flow
1. **Enter only while the picture proposition is unresolved.** Preserve the user's brief, reference-lock requirements, and any camera/crop constraints already fixed. If the user has already supplied an approved composition, do not reopen Stage 0 unless they ask to redesign it.
2. **Choose the Stage 0 search form and bind the global candidate budget in controller state.** For an open composition, use `PAT_explore_stage0_with_thumbnail_set`; for a fixed direction, make one rough control thumbnail. Open Search produces **four to six candidate images total for the entire search cycle**, normally four unless the brief benefits from additional camera/action exploration. Every candidate is one independent image artifact created by its own native image invocation. **One native image call = one Stage 0 candidate.** Do not use a host multi-output option for Stage 0 even when one is available. The controller alone tracks the global total, candidate identifiers, diversity bookkeeping, invalid-slot retries, and user-selection gate. **Contact sheets, production sheets, grids, and any image containing multiple composition candidates are forbidden.** Use the single universal Stage 0 low-information ceiling and `PAT_calibrate_stage_information_density_against_precedent` to keep every result cheap enough to reject.
3. **Search the picture, not the rendering.** Explore camera/viewpoint, framing, subject scale/placement, dominant gesture/action, large shape and negative-space arrangement, depth path, hierarchy, and only the broadest value/light idea. Require structural divergence across alternatives: each candidate should materially change several coarse descriptors such as action family, camera height/side/roll/distance, torso orientation, support surface, primary diagonal, subject scale/crop, foreground relation, or depth path. Cosmetic pose edits inside the same underlying shot do not count as Search.
4. **Gate semantic action requirements at gesture scale.** When the brief says acrobatic, dynamic, weightless, forceful, or another action quality, test that quality before detail: the action line, torso/pelvis relationship, limb asymmetry, center-of-mass/support condition, silhouette, foreshortening, and chosen moment must communicate it even with costume, weapon detail, lighting, and environment finish removed. Use the existing gesture/force patterns where relevant.
5. **Compile one productive image through the artifact-only handoff per native call.** Use `AP_prepare_artifact_only_image_generation_handoff` and the singular Productive Image Contract below. Keep the global search count, candidate index, Search terminology, approval logic, and future calls on the controller side. Do not narrate the staged workflow immediately before generation, and do not add later-resolution visual requirements merely because the golden-truth pack contains them.
6. **Keep alternatives neutral.** Identify candidates clearly in conversation or by simple marks only when needed, but do not star, rank, frame as “best,” call one a root, or visually develop one unless the user explicitly asks for a recommendation. Assistant preference never creates approval.
7. **Classify rejection and retire the correct family.** A bounded correction such as a missing limb or fixed prop may produce another Stage 0 revision while preserving the viable composition. Composition/camera rejection retires that picture family. Pose/action-family rejection retires the coarse action solution. Information-density rejection keeps the picture decision open but lowers the artifact back to the universal Stage 0 ceiling. Broad critiques such as “same image again,” “none of these work,” “too flat,” or “not dynamic enough” reopen Search with the critique carried forward and with matching coarse descriptors treated as dead until the user explicitly resurrects them.
8. **Ratify only from explicit user selection.** In visible interactive staged work, a Stage 0 root does not exist until the user unambiguously approves/selects a candidate. Rejected candidates remain ineligible unless the user explicitly resurrects one.
9. **Return the bounded Stage 0 candidate set and stop for ratification.** When Search is open, return **four to six genuinely different rough candidate images total, one candidate per image**. Never satisfy the count by putting several candidates inside one canvas, and never start a second full candidate batch after the first. If a surfaced candidate is invalid, mark that candidate invalid and retry only that missing slot at the same ceiling; an invalid image never becomes a root or a reason to multiply the whole search set. When the direction is already narrow, one rough control thumbnail may be enough. After selection, the exact selected candidate image is the Stage 0 root and must pass the exact-predecessor accessibility gate before any continuity-dependent Stage 1 generation. In all cases, stop after the current Stage 0 candidate set and await explicit user selection, revision, or rejection.
10. **Use the Stage 0 handoff prompt.** End the turn with explicit next actions such as: “Select the thumbnail you like, with any revisions you may have, or reject them and I'll start over.” If there is only one control thumbnail, adapt the wording from “thumbnail” to “direction,” but keep selection, revision, and rejection all visible.

### Productive Image Contract
- **Artifact form:** one full-frame loose composition sketch containing exactly one rough picture proposition. No additional composition, panel division, title, caption, note, legend, checkmark, ranking/preference marker, later-resolution panel, or presentation-board layout.
- **Preserve:** the user's subject/story requirements and only the character identity constraints that remain visible at this low resolution. Do not solve later surface design merely because the references make it known.
- **Show:** one readable camera/action/composition proposition using gestural figure shapes, silhouette, large environment masses, simple perspective/depth cues, foreground/midground/background relationships, and at most a few broad value families.
- **Novelty constraint:** avoid any explicitly excluded coarse composition descriptors supplied with this image task. Make the proposition materially distinct through several coarse picture decisions such as action family, camera height/side/roll/distance, torso orientation, support/contact surface, primary diagonal, subject scale/crop, foreground relationship, silhouette family, or depth path.
- **Action gate:** when a semantic action quality is required, it must survive as gesture and silhouette alone. A proposition that becomes “dynamic” only after adding a gun, neon, motion effects, dramatic lighting, or costume detail fails.
- **Identity visibility:** preserve body plan/proportion, broad hair mass, silhouette-critical armor/gear shapes, and major equipment masses only where needed for recognition at thumbnail scale. Low detail never licenses redesign.
- **Withhold:** resolved facial features, finger anatomy, hair strands, costume seams/emblems, detailed armor construction, polished anatomy, finished hands or weapons, surface materials, texture, glow/reflection effects, atmospheric rendering, detailed signage, polished lighting, and final environment description.
- **Forbid:** any additional composition proposition on the canvas, process-board/presentation framing, an in-image preference marker, or developed descriptive rendering beyond this rough composition sketch.
- **Global ceiling:** the image remains inexpensive and disposable. Sketchy linework over a developed illustration still exceeds the ceiling.
- **Stop:** when this one proposition can be judged on composition, action, camera, silhouette, depth, and broad value grouping without needing local detail.

## Notes
Stage 0 is a rough idea, not a miniature final. It should show enough of the basic composition to let the viewer imagine how the finished image could work while leaving construction, mass, detailed form, materials, texture, and polish unresolved.

When the host always surfaces generated images immediately, an invalid over-rendered or multi-step artifact cannot be hidden after the fact. Mark it invalid, do not treat it as a legitimate Stage 0 revision or anchor, and retry the same step.
