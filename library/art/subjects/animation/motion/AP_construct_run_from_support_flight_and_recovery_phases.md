---
object_id: AP_construct_run_from_support_flight_and_recovery_phases
object_type: ap
name: Construct Run From Support Flight And Recovery Phases
library_path:
- art
- subjects
- animation
- motion
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- run
- locomotion
- flight
cross_links:
- rel: supports
  target_object_id: PAT_separate_timing_from_spacing_when_designing_motion
- rel: supports
  target_object_id: PAT_track_weight_support_and_transfer_through_every_pose
- rel: supports
  target_object_id: PAT_stage_contact_before_deformation_to_strengthen_impact
- rel: supports
  target_object_id: PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support
- rel: supports
  target_object_id: PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation
- rel: supports
  target_object_id: PAT_articulate_foot_roll_to_control_stride_weight_and_character
- rel: supports
  target_object_id: PAT_transition_sprint_startup_from_forward_drive_into_steady_running_posture
- rel: supports
  target_object_id: PAT_preserve_support_logic_while_distorting_locomotion_design
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Construct Run From Support Flight And Recovery Phases

## Objective
Construct a run around support/contact, compression and push-off, a true airborne phase, recovery, and the next contact.

## Steps / Flow
1. Apply `PAT_separate_timing_from_spacing_when_designing_motion` while placing successive contacts: choose stride length, contact timing, travel, and speed class as distinct controls instead of shortening the whole cycle indiscriminately.
2. Apply `PAT_track_weight_support_and_transfer_through_every_pose` at the run/walk gate. At a true run contact, the previous support has already released; if both feet remain grounded through the transition, return to the gait choice.
3. Apply `PAT_stage_contact_before_deformation_to_strengthen_impact` and `PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support`: let the landing foot arrive first, then let the support leg and body compress as impact is accepted.
4. Continue `PAT_track_weight_support_and_transfer_through_every_pose`, using `PAT_articulate_foot_roll_to_control_stride_weight_and_character` where the foot's contact and release need explicit control, so the support redirects the mass into push-off and extension.
5. Apply `PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation` to the unsupported phase: keep both feet off the ground and organize pose change around a coherent center-of-mass arc.
6. Use push -> suspension -> first contact -> squash -> passing -> extension as a diagnostic sequence when the cycle's mechanics are unclear, without treating those labels as a fixed timing formula.
7. Coordinate body lean, reach of the incoming foot, and recovery of the trailing leg with speed. When a sprint begins from rest, apply `PAT_transition_sprint_startup_from_forward_drive_into_steady_running_posture` instead of copying the steady cycle into acceleration.
8. For faster runs and sprinting, increase whole-body drive and opposing arm action as needed; for sustained running or jogging, reduce stride, vertical excursion, limb lift, and arm amplitude when the observed gait supports it. Apply `PAT_preserve_support_logic_while_distorting_locomotion_design` whenever stylization pushes the poses away from ordinary mechanics.
9. For very young or uncertain runners, retain the support audit from `PAT_track_weight_support_and_transfer_through_every_pose`: shorter steps, very brief suspension, higher step frequency, and arms held outward may be more convincing when balance overrides efficient adult coordination.
10. Recover the limbs for the next landing and repeat at the chosen cadence.

**Completion check**
- The flight phase is unmistakable.
- Successive contacts establish a coherent stride and travel rate.
- Contact does not retain a second planted foot long enough to read as a walk.
- The mass trajectory, body lean, contact geometry, vertical excursion, arm drive, and foot recovery agree with the run’s speed and character.
- Landing contact and subsequent compression read as related but distinct events rather than one undifferentiated pose.

## Notes
Treat walk/run comparison as a structural check rather than a fixed pose recipe: a run is distinguished by true release into unsupported flight, and the contact relationship between landing foot, trailing leg, and advancing mass changes with speed. The named phase breakdown is likewise a diagnostic scaffold, not a universal frame chart. Character proportions, terrain, acceleration, age, balance demands, and style can change the exact geometry.
