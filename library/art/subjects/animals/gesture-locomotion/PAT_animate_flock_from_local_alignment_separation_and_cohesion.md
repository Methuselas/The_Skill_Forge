---
object_id: PAT_animate_flock_from_local_alignment_separation_and_cohesion
object_type: pattern
name: Animate a Flock From Local Alignment, Separation, and Cohesion
library_path:
- art
- subjects
- animals
- gesture-locomotion
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_track_animal_motion_through_moving_pivots_and_overlapping_arcs
tags:
- animal_drawing
- bird
- flock
- group_motion
- alignment
- separation
- cohesion
- formation
- animation
cross_links:
- rel: related_to
  target_object_id: PAT_select_bird_flight_mode_by_available_source_of_lift_and_propulsion
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Animate a Flock From Local Alignment, Separation, and Cohesion

## Pattern Rule
**IF** many birds must read as one responsive flock without moving as a rigid formation or requiring a visible leader
**THEN** let each bird maintain spacing, align with nearby neighbors, and stay connected to the local group, with small response delays allowing directional changes to propagate through the flock

## Do
- Use separation to keep neighboring birds from crowding or colliding.
- Use alignment so local neighbors tend toward compatible headings and motion.
- Use cohesion so individuals remain associated with the group instead of dispersing randomly.
- Offset reactions slightly so a turn or speed change travels through the flock as a wave rather than occurring everywhere on the same frame.
- For formal migration formations, preserve relative position and coordinate flap/glide changes when synchronized behavior improves the formation's efficiency.

## Don't
- Do not rotate or translate the entire flock as one rigid graphic shape.
- Do not require every bird to copy a single leader when the action is meant to read as distributed flocking.
- Do not randomize every trajectory independently and expect the result to retain flock identity.
- Do not synchronize every local correction perfectly unless the shot is deliberately showing a formal coordinated formation.

## Checklist
- Neighbor spacing is maintained without making a visible grid.
- Local headings are related but not mechanically identical.
- The group remains cohesive through turns and speed changes.
- Directional changes propagate with believable delay.
- Formal formations, when used, have a reason for tighter positional and timing control.

## Notes
Webster reduces flocking to alignment, separation, and cohesion and notes that group turns can emerge from delayed local imitation rather than a leader commanding the entire flock. Formation flying is a more constrained case in which position and synchronized flap/glide timing can become part of the efficiency strategy.
