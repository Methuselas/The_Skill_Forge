---
object_id: PAT_integrate_shoulder_mass_with_rib_cage
object_type: pattern
name: Integrate the Shoulder Mass With the Rib Cage
library_path:
- art
- foundations
- form-construction
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- figure_drawing
- shoulder
- rib_cage
- arm_attachment
cross_links:
- rel: related_to
  target_object_id: PAT_preserve_articulated_limb_chain
reference:
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
confidence: high
references: []
variants:
- variant_id: VAR_hampton_block_shoulder_girdle_as_independent_perspective_bridge
  variant_name: Block the Shoulder Girdle as an Independent Perspective Bridge
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Hampton''s explicit shoulder-girdle scaffold to the existing shoulder integration Pattern:
    treat clavicle and scapula together as a flexible perspectival unit resting on the rib cage, with its own tilt and top/side/front
    plane relationships, so the arm is attached through a movable bridge rather than directly to the torso shell.'
  when_to_use: Use when the arm is structurally attached but the shoulder perspective feels vague, when the two shoulders
    do not belong to the same turn/tilt, or when scapular/clavicular motion is hard to organize in 3-D.
  when_not_to_use: Do not preserve a literal football-pad block in the finished figure; it is a temporary spatial organizer
    for the actual clavicle, scapula, deltoid, chest, and back forms.
  absorbed_from_object_id: none
---

# Integrate the Shoulder Mass With the Rib Cage

## Pattern Rule
**IF** an arm position changes the upper torso silhouette
**THEN** use the deltoid as the broad transition between arm and rib cage, merging it into the chest when the arm lowers and lifting it away when the arm raises
**ELSE** recheck the shoulder socket and arm direction before refining the torso edge

## Do
- Treat the chest and shoulders as a compound form whose visible shape responds to arm elevation.
- Let humerus elevation propagate through the shoulder girdle: coordinate the scapular and clavicular response with the deltoid transition so a large arm sweep does not hinge from a frozen socket.
- Let a lowered shoulder broaden and wedge the upper torso; let a raised shoulder reveal more of the barrel.
- Keep the arm chain anchored through the shoulder transition rather than attaching a cylinder directly to the chest edge.

## Don't
- Reuse one shoulder cap and torso outline for every arm position.
- Draw a gap between deltoid and chest that makes the arm look detached.

## Checklist
- The shoulder silhouette changes when the arm changes elevation.
- The deltoid belongs simultaneously to the arm chain and the chest-and-shoulder mass.
- The rib-cage barrel remains readable beneath the changing transition.
- The shoulder girdle visibly answers a major arm elevation instead of remaining mechanically fixed.

## Notes
The source treats the deltoids as arm muscles that become part of the upper torso because they mediate attachment. This prevents the common mannequin error of bolting a limb cylinder to a fixed chest shell.

`VAR_hampton_block_shoulder_girdle_as_independent_perspective_bridge` retains **Block the Shoulder Girdle as an Independent Perspective Bridge** as a bounded alternative; use it only under the conditions recorded in the variant metadata.
