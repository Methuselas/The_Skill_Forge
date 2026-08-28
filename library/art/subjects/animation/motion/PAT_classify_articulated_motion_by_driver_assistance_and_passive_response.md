---
object_id: PAT_classify_articulated_motion_by_driver_assistance_and_passive_response
object_type: pattern
name: Classify Articulated Motion by Driver Assistance and Passive Response
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
foundation_object_id: PAT_track_force_continuity_through_action
tags:
- animation
- primary_action
- secondary_action
- tertiary_action
- articulation
- causality
- follow_through
cross_links:
- rel: related_to
  target_object_id: PAT_carry_secondary_parts_through_overlap_follow_through_and_drag
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Classify Articulated Motion by Driver Assistance and Passive Response
## Pattern Rule
**IF** many parts of an articulated subject move at once and their relative importance is unclear
**THEN** classify each movement by causal contribution: primary motion drives the current action, secondary motion assists or improves it without driving it, and tertiary motion is a passive consequence of primary or secondary movement

## Do
- Identify the current driver from what actually accomplishes the action, not from which part moves the farthest on screen.
- Allow the primary driver to migrate during a compound action; legs, arms, spine, or another region may take over at different phases.
- Treat assisting counteractions, balancing motions, or efficiency-improving motions as secondary when the action can still occur without them.
- Treat hair, loose garments, tails, floppy ears, hanging props, and similar passively carried structures as tertiary when they do not help accomplish the main task.
- Reclassify by action context rather than assigning a permanent class to a body part.

## Don't
- Do not assume the visually largest motion is primary.
- Do not classify an arm, tail, head, or other region permanently; its causal role can change with the task.
- Do not confuse this causal hierarchy with conventional terminology that may call passively carried parts "secondary action" in a broader sense.

## Checklist
- The primary driver can be named for each major phase.
- Secondary motion improves the action without being necessary to initiate it.
- Tertiary motion is traceable to movement elsewhere in the subject or to external forces.
- Role changes across the action remain mechanically coherent.

## Notes
The classification is causal rather than anatomical or visual. An arm can drive a sweep, assist a run, or hang passively in different contexts. Likewise, a dramatically flapping coat tail can remain tertiary because it contributes nothing to the action that caused it.
