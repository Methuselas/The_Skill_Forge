---
object_id: PAT_rebuild_walking_gait_around_changed_support_and_limb_clearance_constraints
object_type: pattern
name: Rebuild Walking Gait Around Changed Support and Limb Clearance Constraints
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
foundation_object_id: PAT_design_walk_from_character_state_and_attitude
tags:
- animation
- walk
- locomotion
- support
- asymmetry
- limb_clearance
- cane
- crutch
- walker
cross_links:
- rel: related_to
  target_object_id: PAT_track_weight_support_and_transfer_through_every_pose
- rel: related_to
  target_object_id: PAT_design_pose_against_center_of_gravity
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Rebuild Walking Gait Around Changed Support and Limb Clearance Constraints

## Pattern Rule
**IF** injury, restriction, weakness, or a walking aid changes which limb can support, swing, or clear the ground normally
**THEN** solve the actual support and clearance constraint, then let the gait become asymmetrical or discontinuous as required

## Do
- Identify exactly what the affected limb can no longer do: bend enough for clearance, accept full weight, push off, or swing through the ordinary path.
- Create clearance by changing the body as well as the limb when needed: swing a restricted leg laterally, raise the supporting heel, lift or tilt the pelvis, or shorten the step.
- Let left and right timing, spacing, and vertical travel become genuinely unequal when only one side is restricted.
- Treat a cane, crutch, or walker as a real support contact when the figure loads it; shift body weight into it rather than using it as a prop that slides beside an otherwise normal gait.
- For two-crutch or walker locomotion, build the sequence from actual support exchange: establish the aid, transfer weight, advance the body or legs, then recover the aid for the next support.
- Preserve the character's objective and confidence on top of the mechanical solution rather than using one generic "limp" symbol.

## Don't
- Do not add a limp to an otherwise unchanged symmetrical walk without explaining the changed support mechanics.
- Do not keep a restricted knee or ankle moving through a normal clearance path it can no longer achieve.
- Do not let a loaded cane, crutch, or walker remain visually weightless.

## Checklist
- Every altered step can be explained by support, clearance, or propulsion.
- Asymmetry appears in timing and spacing when the constraint is unilateral.
- Walking aids visibly receive and release weight.
- The resulting gait remains mechanically coherent even with the costume and aid removed from view.

## Notes
A constrained gait is most convincing when it grows from a specific mechanical limitation. Webster's examples show several possible compensations for the same broad problem, so the animator should diagnose what cannot happen normally and rebuild the support cycle around that restriction instead of relying on a stock limp.
