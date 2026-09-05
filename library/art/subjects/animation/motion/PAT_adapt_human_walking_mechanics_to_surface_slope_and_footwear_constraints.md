---
object_id: PAT_adapt_human_walking_mechanics_to_surface_slope_and_footwear_constraints
object_type: pattern
name: Adapt Human Walking Mechanics to Surface Slope and Footwear Constraints
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
- terrain
- slope
- footwear
- contact
- balance
cross_links:
- rel: related_to
  target_object_id: PAT_articulate_foot_roll_to_control_stride_weight_and_character
- rel: related_to
  target_object_id: PAT_track_weight_support_and_transfer_through_every_pose
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Adapt Human Walking Mechanics to Surface Slope and Footwear Constraints

## Pattern Rule
**IF** the walking surface, slope, resistance, or footwear changes how safely and efficiently the foot can contact, clear, or push against the ground
**THEN** rebuild the gait around the new contact problem instead of preserving a normal flat-ground walk and merely changing its timing

## Do
- On slippery ground, shorten the stride and use more cautious, flatter contact when a strong heel-first roll would increase the chance of slipping.
- In deep mud, snow, or another resisting surface, increase foot clearance and extract the foot more vertically before advancing it rather than dragging an ordinary swing path through the resistance.
- On an uphill slope, shorten and reorganize the stride, pitch the body into the climb as needed, and allow sufficiently steep terrain to recruit the hands and transition toward scrambling.
- On a downhill slope, shorten the step, manage the body's forward fall, and change orientation or recruit hand support when straightforward walking can no longer preserve stability.
- Let restrictive, unstable, or unusual footwear alter available ankle/foot articulation, clearance, contact confidence, and stride rather than leaving the lower-body mechanics unchanged.
- Recheck the support point, center-of-mass travel, and ground reaction after every terrain-driven change.

## Don't
- Do not keep the same foot roll, stride length, and swing path on every surface.
- Do not represent mud, snow, ice, or steep grade only with slower timing while the support mechanics remain unchanged.
- Do not force an ordinary walk to continue after the terrain has made another support strategy mechanically more appropriate.

## Checklist
- Foot clearance and contact fit the surface.
- Stride length and body pitch fit the slope or resistance.
- Any use of the hands or change of orientation follows from a real stability problem.
- Footwear restrictions are visible in the gait rather than only in the costume drawing.

## Notes
Changing terrain changes the locomotion problem. Webster's examples show that believable adaptation appears in contact geometry, clearance, stride, body pitch, and support strategy—not just in speed. The animator should solve the new ground interaction first, then restore character and timing on top of that solution.
