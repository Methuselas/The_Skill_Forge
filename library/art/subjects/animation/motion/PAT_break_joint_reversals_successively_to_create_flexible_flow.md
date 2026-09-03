---
object_id: PAT_break_joint_reversals_successively_to_create_flexible_flow
object_type: pattern
name: Break Joint Reversals Successively To Create Flexible Flow
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
- joints
- flexibility
- overlap
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Break Joint Reversals Successively To Create Flexible Flow

## Pattern Rule
**IF** a flexible articulated chain changes direction and would look rigid if every joint reversed at once
**THEN** Pass a reversal successively through an articulated chain instead of reversing every joint simultaneously

## Do
- Choose where the directional change begins.
- Let neighboring segments continue briefly while the first segment reverses.
- Propagate the reversal through the chain.
- Allow controlled anatomical exaggeration when it improves the moving flow.

## Don't
- Do not snap an entire chain from one pose to the opposite pose on one shared clock.

## Checklist
- The reversal travels through the chain and creates flexible flow.

## Notes

Let the initiating force determine the propagation order; the delay need not be evenly spaced from joint to joint. Track segment length and attachment through the reversal so flexibility comes from phase difference rather than stretching the chain accidentally.
