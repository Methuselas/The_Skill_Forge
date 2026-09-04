---
object_id: PAT_reanchor_straight_ahead_animation_with_registration_drawings
object_type: pattern
name: Reanchor Straight-Ahead Animation With Registration Drawings
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
foundation_object_id: PAT_preserve_solid_flexible_zone_hierarchy_through_character_motion
tags:
- animation
- straight_ahead
- registration
- construction
- scale
- continuity
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Reanchor Straight-Ahead Animation With Registration Drawings

## Pattern Rule
**IF** successive straight-ahead drawings can accumulate small proportion, construction, attachment, or scale errors
**THEN** compare the developing passage against periodic registered anchor drawings and correct local drift before it propagates through later states

## Do
- Establish trustworthy construction and scale anchors before the straight-ahead passage begins.
- Insert or select comparison drawings at meaningful changes of direction, force, contact, or staging rather than at an arbitrary fixed interval.
- Register the current drawing against both the nearest trusted anchor and the intended motion path.
- Compare stable masses, attachment points, characteristic proportions, and overall scale before surface detail.
- Correct the earliest drawing where drift becomes visible, then propagate the repaired structure forward.
- Preserve intended squash, stretch, perspective change, and flexible deformation while removing unintended cumulative change.

## Don't
- Do not compare only each drawing with its immediate predecessor; a chain of locally plausible errors can still drift far from the model.
- Do not force expressive deformation back to neutral proportions when the change is intentional and volume remains coherent.
- Do not repair late symptoms while leaving the earlier drift point unchanged.
- Do not use registration to flatten the motion path or eliminate controlled variation.

## Checklist
- Stable masses and characteristic proportions return consistently across the passage.
- Overall scale does not shrink or grow without an intended spatial cause.
- Attachments remain continuous through flexible or overlapping motion.
- The earliest drift point was repaired before downstream drawings were accepted.

## Notes
Registration provides a long-range comparison that adjacent-frame checking cannot. This Pattern owns cumulative structural-drift control; it does not decide which systems should be animated straight ahead or replace motion-path and timing decisions.
