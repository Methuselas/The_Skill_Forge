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
  target_object_id: PAT_track_weight_support_and_transfer_through_every_pose
- rel: supports
  target_object_id: PAT_stage_contact_before_deformation_to_strengthen_impact
- rel: supports
  target_object_id: PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support
- rel: supports
  target_object_id: PAT_balance_primary_motion_with_counteraction
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
1. Establish successive contact positions early enough to define stride length, travel, and the intended speed class; treat stride length and stride frequency as separate speed controls rather than shortening the whole cycle indiscriminately.
2. Use `PAT_track_weight_support_and_transfer_through_every_pose` to verify the support state. At a true run contact, confirm that the previous support has already released; if both feet remain grounded through the transition, the action is drifting toward a walk.
3. Use `PAT_stage_contact_before_deformation_to_strengthen_impact` to separate first contact from the following load-absorption phase: let the landing foot arrive, then let the support leg and body compress as impact is accepted.
4. Use `PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support` while the support leg redirects the mass into push-off and extension.
5. Create a flight phase with both feet off the ground; allow the body to reach a higher or more extended portion of its path during unsupported flight when that fits the run.
6. Use push -> suspension -> first contact -> squash -> passing -> extension as a diagnostic sequence when the cycle's mechanics are unclear, without treating those labels as a fixed timing formula.
7. Coordinate body lean, reach of the incoming foot, and recovery of the trailing leg with speed rather than merely shortening the duration of a generic run.
8. Use `PAT_balance_primary_motion_with_counteraction` when increasing whole-body drive and opposing arm action for faster runs and sprinting. For sustained running or jogging, reduce stride, vertical excursion, limb lift, and arm amplitude when the observed gait supports it.
9. For very young or uncertain runners, allow balance needs to override efficient adult coordination: shorter steps, very brief suspension, higher step frequency, and arms held outward may be more convincing than a clean adult sprint pattern.
10. Recover the limbs for the next landing and repeat at the chosen cadence.

**Completion check**
- The flight phase is unmistakable.
- Successive contacts establish a coherent stride and travel rate.
- Contact does not retain a second planted foot long enough to read as a walk.
- The mass trajectory, body lean, contact geometry, vertical excursion, arm drive, and foot recovery agree with the run’s speed and character.
- Landing contact and subsequent compression read as related but distinct events rather than one undifferentiated pose.

## Notes
Blair's walk/run comparison is most useful as a structural check rather than a fixed pose recipe: a run is distinguished by true release into unsupported flight, and the contact relationship between landing foot, trailing leg, and advancing mass changes with speed. Webster's phase breakdown is likewise a diagnostic scaffold, not a universal frame chart. Character proportions, terrain, acceleration, age, balance demands, and style can change the exact geometry.
