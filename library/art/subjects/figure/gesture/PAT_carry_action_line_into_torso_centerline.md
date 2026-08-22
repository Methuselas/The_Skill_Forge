---
object_id: PAT_carry_action_line_into_torso_centerline
object_type: pattern
name: Carry the Action Line Into the Torso Centerline
library_path:
- art
- subjects
- figure
- gesture
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
- figure_drawing
- action_line
- torso_centerline
- gesture
cross_links:
- rel: supports
  target_object_id: AP_notate_a_figure_in_structural_order
- rel: related_to
  target_object_id: PAT_join_rib_cage_and_pelvis_through_flexible_waist
reference:
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
confidence: high
references: []
variants:
- variant_id: VAR_hampton_design_gesture_with_asymmetry_and_visual_timing
  variant_name: Design Gesture With Asymmetry and Visual Timing
  variant_basis: emphasis
  difference_from_foundation: 'Adds a compositional line-design layer to the governing action: offset the apexes of neighboring
    curves instead of mirroring them, and use repeated curves selectively to slow the eye around complex intersections while
    longer asymmetrical sweeps accelerate it along forms.'
  when_to_use: Use when the pose is structurally plausible but feels snowman-like, parallel, evenly paced, or visually static.
  when_not_to_use: Do not ban symmetry when the story calls for stability, power, immobility, or deliberate frontal organization;
    timing is a design choice, not an anatomy law.
  absorbed_from_object_id: none
---

# Carry the Action Line Into the Torso Centerline

## Pattern Rule
**IF** an accepted Step 1 action line is becoming a Stage 2 torso
**THEN** preserve that line as the torso centerline and construct the rib-cage barrel and pelvic wedge around it so their direction, opposition, and connection all serve one continuous action
**ELSE** return to Step 1 when the action line is unclear or cannot support the intended torso masses

## Do
- Let the centerline determine the allowable bend, tilt, turn, and spiral before adding dependent forms.
- Use the line across both torso masses to compare their facing directions and the transition through the waist.
- Permit a deliberate correction to the Step 1 line when the block exposes a real structural error, then carry that correction back into the underlying framework.
- Check every later limb and head choice as a response to the governing torso action.

## Don't
- Place two unrelated torso masses and add a centerline afterward merely to connect them.
- Treat the centerline as a decorative surface stripe that reports form without governing it.
- Let an extreme arm, leg, or head direction contradict the established action unless the opposing force is structurally supported.
- Discard the Step 1 flow and invent a new Stage 2 pose without acknowledging the redesign.

## Checklist
- The Stage 2 centerline can be traced back to the accepted Step 1 action line.
- Rib cage, pelvis, and waist transition read as one compound action rather than stacked parts.
- Limb directions either continue, oppose, balance, or redirect the centerline coherently.
- Reducing the torso back to one line preserves the intended gesture.

## Notes
The centerline is the figure's Wu Sao: it protects the directional logic of the action. Once established, the attached forms have a limited family of believable curves and directions. This is especially important in exaggerated or comic-art poses, where strong distortion still needs one readable governing flow.

`VAR_hampton_design_gesture_with_asymmetry_and_visual_timing` retains **Design Gesture With Asymmetry and Visual Timing** as a bounded alternative; use it only under the conditions recorded in the variant metadata.
