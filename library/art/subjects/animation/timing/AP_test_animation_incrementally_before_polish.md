---
object_id: AP_test_animation_incrementally_before_polish
object_type: ap
name: Test Animation Incrementally Before Polish
library_path:
- art
- subjects
- animation
- timing
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- testing
- roughs
- workflow
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Test Animation Incrementally Before Polish

## Objective
Validate motion repeatedly while it is cheap to change, moving from structural tests to rough passes before cleanup or finish.

## Steps / Flow
1. Test story keys.
2. Test extremes and breakdowns.
3. Test rough primary action.
4. Test added secondary/tertiary motion.
5. Only polish after timing, spacing, path, and performance survive playback.

**Completion check**
- Major motion errors are found before cleanup.
- Polish never serves as the first motion test.

## Notes
- Keep early animation rough while solving timing, spacing, path, performance, and continuity. Rough states are for discovering motion; cleanup is for preserving a motion solution that already works.
- At sequence scale, test storyboards and animatics before detailed animation so editing, geography, duration, and staging problems are corrected at their cheapest representation.
