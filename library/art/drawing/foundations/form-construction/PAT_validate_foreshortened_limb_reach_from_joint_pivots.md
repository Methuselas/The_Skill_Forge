---
object_id: PAT_validate_foreshortened_limb_reach_from_joint_pivots
object_type: pattern
name: Validate Foreshortened Limb Reach From Joint Pivots
library_path:
- art
- drawing
- foundations
- form-construction
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- figure_drawing
- foreshortening
- joint_reach
- proportion
cross_links:
- rel: related_to
  target_object_id: PAT_preserve_articulated_limb_chain
- rel: related_to
  target_object_id: PAT_hold_member_identity_with_constant_width
reference:
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
confidence: high
references: []
variants: []
---

# Validate Foreshortened Limb Reach From Joint Pivots

## Pattern Rule
**IF** a foreshortened arm or leg looks too long, too short, disconnected, or otherwise uncertain in depth
**THEN** preserve the designed length of each limb segment, treat its carrying joint as the pivot, and test whether the next joint or terminal form can plausibly occupy the chosen endpoint before anatomy is developed
**ELSE** keep the ordinary articulated-chain and proportion checks when the projected length already reads clearly

## Do
- Establish the parent socket or joint, the next joint, and the terminal form as one traceable chain before refining contour.
- Use the same figure's designed segment length as the reach constraint; apparent screen-space length may compress radically without the physical member changing identity.
- For a two-segment limb, solve the first endpoint from its parent pivot, then solve the second from the intermediate joint.
- Use a temporary ellipse or arc when visual judgment needs help; use part-to-part contact or alignment checks when the pose naturally supplies them.
- Coordinate the reach check with width and taper control so projected length and member identity agree.

## Don't
- Stretch or shrink a limb segment merely to make a difficult pose fit the silhouette.
- Turn the ellipse, arc, or triangle scaffold into compulsory visible construction when the relationship is already clear.
- Treat the pivot as an isolated dot divorced from the moving body structure that carries it.
- Preserve a neat guide when it produces a less believable articulated figure.

## Checklist
- Every distal endpoint is reachable from its parent joint without silently changing the designed member length.
- The socket-to-joint-to-terminal order remains continuous through overlap and foreshortening.
- Width, taper, and projected length describe the same member rather than competing solutions.
- Removing the temporary guide leaves the limb structurally convincing.

## Notes
Chapter 5 is retained as a local reach diagnostic rather than a compulsory geometry system. The arc is temporary evidence for legal articulation; the accepted pose, segment identity, and carrying body structure remain authoritative.
