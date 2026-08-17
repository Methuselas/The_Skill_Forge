---
object_id: PAT_stage_product_instruction_sequence_with_consistent_state_and_action_cues
object_type: pattern
name: Stage Product Instruction Sequence With Consistent State and Action Cues
library_path:
- art
- drawing
- sketching
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- sketching
- instructions
- sequence
- motion
- product_use
cross_links:
- rel: related_to
  target_object_id: PAT_interpolate_rigid_part_pose_along_motion_path
reference:
  source_title: Sketching the Basics
  author: Koos Eissen and Roselien Steur
confidence: high
references: []
variants: []
---

# Stage Product Instruction Sequence With Consistent State and Action Cues

## Pattern Rule
**IF** a product action, assembly, or transformation must be understood across several drawings
**THEN** preserve product identity and state continuity across frames while making each action legible with an informative view and movement cue
**ELSE** use a single explanatory view when the action has no meaningful intermediate state

## Do
- Make every frame visibly related to the preceding and following state through stable proportions, defining features, and consistent rendering conventions.
- Choose the viewpoint that best explains each action; keep the camera fixed only when a fixed view remains clear throughout the sequence.
- Vary view or scale modestly when it improves legibility without making the product appear to change identity.
- Build an action arrow from the actual movement: locate start and end, add a midpoint or curved path when needed, then design the arrow around that trajectory.
- Arrange the frames in the reading order expected by the intended audience and make the sequence direction visually obvious.

## Don't
- Do not let a changing camera make one product look like several unrelated designs.
- Do not use decorative arrows whose direction or curvature contradicts the mechanism being explained.
- Do not freeze a poor viewpoint across every frame merely for consistency.
- Do not assume one universal left-to-right sequence when the audience or format uses another reading order.

## Checklist
- Each frame can be recognized as the same product in a new state.
- The changed state or action is obvious without relying on prose to repair ambiguous geometry.
- Arrow paths agree with the part's actual movement.
- Camera changes improve explanation and do not break continuity.
- The page order makes the first, next, and final state unambiguous.

## Notes
Instructional sequences have two competing needs: continuity and local clarity. Keeping everything identical can hide an action that needs another view, while changing every view can destroy the reader's mental model of the object. Preserve the stable identity cues, then spend viewpoint changes only where they make the action easier to reconstruct.
