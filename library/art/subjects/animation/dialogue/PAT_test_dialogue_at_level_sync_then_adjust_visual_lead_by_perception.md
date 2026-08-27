---
object_id: PAT_test_dialogue_at_level_sync_then_adjust_visual_lead_by_perception
object_type: pattern
name: Test Dialogue At Level Sync Then Adjust Visual Lead By Perception
library_path:
- art
- subjects
- animation
- dialogue
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- dialogue
- sync
- timing
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Test Dialogue At Level Sync Then Adjust Visual Lead By Perception

## Pattern Rule
**IF** lip sync is technically aligned but the visible mouth action does not perceptually feel synchronized
**THEN** Start dialogue animation at logical sound sync, then test and adjust small visual leads only when perception improves

## Do
- Build a level-sync version first.
- Test the actual character and performance.
- Advance the mouth or picture by a small amount only if it reads better.
- Keep the chosen offset local to the performance rather than a universal rule.

## Don't
- Do not assume every dialogue shot must lead sound by a fixed frame count.

## Checklist
- The mouth feels synchronized perceptually, not merely numerically.

## Notes
