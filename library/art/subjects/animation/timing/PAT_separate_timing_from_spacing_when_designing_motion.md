---
object_id: PAT_separate_timing_from_spacing_when_designing_motion
object_type: pattern
name: Separate Timing From Spacing When Designing Motion
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
- timing
- spacing
- motion
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Separate Timing From Spacing When Designing Motion

## Pattern Rule
**IF** an action has fixed endpoints but its duration and positional spacing still need independent control
**THEN** Treat duration/event placement and positional distribution as independent controls so the same endpoints can produce different motion character

## Do
- Set when important events occur.
- Then choose how the positions are distributed between them.
- Compare alternate spacing profiles without changing total duration.

## Don't
- Do not use “timing” as a vague label that hides spacing decisions.

## Checklist
- Timing and spacing can each be changed without accidentally changing the other.

## Notes
