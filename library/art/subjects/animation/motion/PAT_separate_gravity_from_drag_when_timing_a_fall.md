---
object_id: PAT_separate_gravity_from_drag_when_timing_a_fall
object_type: pattern
name: Separate Gravity From Drag When Timing a Fall
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
foundation_object_id: PAT_show_mass_through_resistance_to_acceleration_and_direction_change
tags:
- animation
- gravity
- drag
- falling
- air_resistance
- weight
- physics
cross_links:
- rel: related_to
  target_object_id: PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Separate Gravity From Drag When Timing a Fall
## Pattern Rule
**IF** two unsupported objects seem to require different falling speeds because one looks heavier
**THEN** keep gravitational acceleration conceptually separate from resistance: under the same gravity, mass alone does not make the heavier object fall faster, so use drag, shape, area, medium, and related resistance to justify visible differences in descent
**ELSE** when resistance is negligible, let differently massive objects share the same basic gravitational acceleration and show mass through other responses.

## Do
- Use exposed area, shape, orientation, flexible surfaces, and the surrounding medium to decide how strongly drag alters a fall.
- Show heavier or lighter mass through inertia, force response, stopping distance, impact, deformation, and recovery rather than automatically changing downward acceleration.
- Preserve the same gravitational tendency when comparing objects in the same environment unless another force explains the difference.

## Don't
- Do not encode "heavier means faster falling" as a default timing rule.
- Do not ignore resistance when a feather, cloth, leaf, broad surface, or similar form visibly interacts with air or fluid.
- Do not use realistic physics more precisely than the intended animation requires; the result still has to serve the chosen motion fidelity.

## Checklist
- Any difference in falling rate has a named force or resistance mechanism.
- Mass is readable without requiring a false gravity rule.
- The fall remains consistent with the environment and medium.
- Stylization, if present, is intentional rather than accidental physics drift.

## Notes
Objects of different mass fall at the same rate in a vacuum; familiar differences such as a feather descending more slowly than a compact heavy object arise from resistance. For animation, the practical value is diagnostic: gravity establishes the shared downward tendency while drag and other forces explain why shapes may depart from that baseline.
