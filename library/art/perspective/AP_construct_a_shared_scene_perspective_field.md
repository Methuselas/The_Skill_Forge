---
object_id: AP_construct_a_shared_scene_perspective_field
object_type: ap
name: Construct a Shared Scene Perspective Field
library_path:
- art
- perspective
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- perspective
- scene
- construction
- workflow
cross_links:
- rel: supports
  target_object_id: PAT_establish_eye_level_and_vanishing_directions
- rel: supports
  target_object_id: PAT_choose_convergence_from_view_and_orientation
reference:
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
confidence: high
references: []
variants:
- variant_id: VAR_lock_scene_with_minimal_underlay
  variant_name: Lock POV and Large Volumes With a Minimal Underlay
  variant_basis: method_sequence
  difference_from_foundation: 'Adds an optional hybrid path: use a simple 3D, photographic, or generated underlay only to
    lock POV, field impression, grid, and large proportions, then return to drawing.'
  when_to_use: Use when perspective setup is consuming design time or many camera variants must be tested.
  when_not_to_use: Do not overmodel the final design or make software a prerequisite.
  absorbed_from_object_id: none
- variant_id: VAR_hogarth_calibrate_shared_scene_from_trusted_figure
  variant_name: Calibrate the Shared Scene From a Trusted Figure
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a figure-first entry route: use known body landmarks, ground contacts, and body planes
    from one correctly constructed figure to seed relative scale and direction before extending the shared scene field to
    objects and additional figures.'
  when_to_use: Use when the figure is the primary designed subject and the environment must inherit believable scale and viewpoint
    from it.
  when_not_to_use: Do not let an uncertain figure override formal eye level, vanishing behavior, or independent perspective
    checks; the shared field becomes authority once solved.
  absorbed_from_object_id: PAT_build_shared_scene_perspective_from_figure
---

# Construct a Shared Scene Perspective Field

## Objective
Build one coherent perspective field that can govern figures, objects, and environment, then load only the precision constructions the scene actually needs.

## Steps / Flow
**Entry Conditions**
- The scene viewpoint is not yet locked, or multiple objects/figures must share one convincing spatial world.
- The task benefits from explicit perspective construction rather than purely observational copying.

**Persistent Invariants**
- One observer/view relationship governs the scene.
- Horizontal-world vanishing directions share one eye-level line.
- Objects that share a real direction share the corresponding vanishing behavior.
- Scale and repeated spacing are constructed on the solved field, not guessed independently.
- Optional technical geometry is loaded only when it answers a concrete placement problem.

**Flow**
1. **Set the view.** Decide what the observer sees and establish eye level.
2. **Solve dominant directions.** Group the scene's main parallel directions and assign their vanishing behavior from orientation.
3. **Block the scene.** Use box masses, a trusted figure, or both to establish large placements and shared scale.
4. **Check distortion.** If edge regions become implausibly stretched, correct vanishing spacing or crop before continuing.
5. **Specialize only as needed.** Load height/width transfer, plane subdivision, inclined planes, or round-solid construction only where the scene asks for them.
6. **Validate the field.** Check that major objects, figures, and planes still agree before detail and rendering obscure construction errors.

**Failure / Rollback Rules**
- If several objects require different vanishing destinations for what should be the same real direction, return to dominant-direction setup.
- If equal-scale subjects drift with depth, return to height/width guides.
- If edge distortion grows while the center is sound, adjust vanishing spacing/crop rather than patching objects locally.
- If a specialized construction becomes more complicated than the visual problem, roll back to the simplest sufficient guide.

**Completion Criteria**
- The viewer can infer one coherent eye level and spatial field.
- Major direction families converge consistently.
- Figures and objects preserve believable relative scale across depth.
- Any slopes, circles, repeats, or measured designs inherit the same field.
- The scene is ready for downstream drawing/rendering without perspective correction being hidden by detail.
- If several locally plausible parts refuse to coexist spatially, suspect viewpoint drift from solving them one at a time; re-anchor the whole scene to one eye level and dominant perspective field before correcting individual parts.

## Notes
This AP is intentionally equation-light. D'Amelio's geometric theory is retained as cause, but the working procedure is visual construction: establish, project, check, and only measure when necessary.

`VAR_hogarth_calibrate_shared_scene_from_trusted_figure` adds a figure-first calibration route: one sound figure may seed scene scale and direction, but formal perspective still validates the field and takes over as the common authority.

`VAR_lock_scene_with_minimal_underlay` remains a bounded variant under the conditions recorded in its variant metadata.

A large observed scene can drift into a composite of subtly different viewpoints when the gaze is re-aimed for each local object. Treat local correctness that fails to coexist globally as a cue to restore one shared view field before patching individual forms.
