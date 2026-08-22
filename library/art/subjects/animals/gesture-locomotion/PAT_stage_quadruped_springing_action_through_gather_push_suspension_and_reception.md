---
object_id: PAT_stage_quadruped_springing_action_through_gather_push_suspension_and_reception
object_type: pattern
name: Stage Quadruped Springing Action Through Gather, Push, Suspension, and Reception
library_path:
- art
- subjects
- animals
- gesture-locomotion
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_read_quadruped_locomotion_from_support_swing_and_suspension_phases
tags:
- animal_drawing
- quadruped
- locomotion
- jump
- leap
- sprint
- spring
- push_off
- suspension
- landing
- compression
- extension
cross_links:
- rel: related_to
  target_object_id: PAT_stage_animal_impact_as_deformation_reversal_and_recovery
- rel: related_to
  target_object_id: PAT_map_animal_pose_as_vertebral_and_limb_direction_framework
- rel: related_to
  target_object_id: PAT_distinguish_quadruped_forequarter_suspension_from_hindquarter_drive
reference:
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
confidence: high
references: []
variants: []
---

# Stage Quadruped Springing Action Through Gather, Push, Suspension, and Reception

## Pattern Rule
**IF** a quadruped jump, leap, bound, or full-speed spring looks like one static body with the legs merely rearranged around it
**THEN** stage the whole event through a gathered/preloaded configuration, propulsive extension, a suspended travel phase, and a receiving/contact phase, allowing the trunk, neck, forelimbs, and hindlimbs to reorganize according to the species and action rather than all reaching maximum extension at once
**ELSE** use the ordinary gait-contact Pattern when the action does not contain a clear springing or airborne event.

## Do
- Establish the gathered or compressed setup first when the reference shows it: propulsive limb joints close, the body lowers or bunches, and non-supporting limbs prepare for the launch rather than posing independently.
- Let push-off change the **whole framework**, not only the rear feet; the major body direction and relevant joint chains should visibly lengthen or redirect as the animal leaves support.
- Treat the suspension phase as an intermediate whole-body configuration with its own limb organization, not as a frozen maximum-stretch icon.
- Prepare the forequarter for the next receiving contact, then let the visible joint response agree with the animal and phase; Bammes's horse, dog, and cat examples receive load differently.
- Bring the hindlimbs forward or fold them for recovery when the reference shows the next support being prepared.
- Let vertebral and neck motion participate only to the degree supported by the species and reference; Bammes shows strong spinal flexion/extension in the dog and cat examples and a different organization in the horse jump.

## Don't
- Do not give horse, dog, and cat the same spinal flexibility, limb timing, or landing mechanics merely because all three leave the ground.
- Do not make every limb fully extend at the same instant; propulsion, suspension, reaching, reception, and recovery overlap differently.
- Do not stretch or compress the actual limb segment lengths to create the feeling of spring.
- Do not treat Bammes's "tension spring" or centrifugal-force language as literal universal biomechanics; preserve the observable pose sequence and species-specific structure.
- Do not use the landing pose without accounting for the gathered and suspended phases that produced it when the task is to show motion rather than a single contact instant.

## Checklist
- The action has a readable gathered/preload phase when appropriate.
- Push-off reorganizes the body and limb framework rather than only changing foot position.
- A suspension phase is distinct from both takeoff and landing.
- The receiving contact prepares for and visibly responds to body travel.
- Hindlimb recovery points toward the next support relationship instead of ending the sequence arbitrarily.
- Species-specific spine, neck, and limb behavior is checked against reference.

## Notes
On printed pp. 39-40 Bammes compares three springing actions: a dog moving full tilt, a horse jumping, and a cat springing from a crouch. Their exact mechanics differ, but all three are presented as **phase changes of the whole articulated animal** rather than as decorative leg positions. The reusable art decision is therefore to stage gather, propulsion, airborne travel, and reception as connected structural states, while refusing to turn any one species' sequence into a universal jump formula.

This Pattern begins before the impact-focused Hultgren Pattern and overlaps it at reception. Use `PAT_stage_animal_impact_as_deformation_reversal_and_recovery` when the drawing problem is specifically shock, rebound, or post-contact recovery.
