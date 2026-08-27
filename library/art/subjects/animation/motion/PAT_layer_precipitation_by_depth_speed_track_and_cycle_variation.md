---
object_id: PAT_layer_precipitation_by_depth_speed_track_and_cycle_variation
object_type: pattern
name: Layer Precipitation By Depth Speed Track And Cycle Variation
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
foundation_object_id: PAT_anchor_stylized_motion_in_observed_mass_mechanics
tags:
- animation
- effects
- rain
- snow
- precipitation
- depth
cross_links:
- rel: related_to
  target_object_id: PAT_repeat_with_variation_to_balance_coherence_and_interest
- rel: related_to
  target_object_id: PAT_grade_depth_with_atmospheric_effect
reference:
  source_title: Timing for Animation
  author: Harold Whitaker and John Halas
confidence: high
references: []
variants: []
---

# Layer Precipitation By Depth Speed Track And Cycle Variation

## Pattern Rule
**IF** rain, snow, or similar particle fields must read as precipitation occupying depth rather than as one flat repeated overlay
**THEN** separate the field into depth layers, vary apparent particle size, speed, trajectory, and cycle phase by layer, and preserve enough directional continuity that individual tracks read as motion instead of flicker
**ELSE** use a simpler single-layer graphic effect when the shot is intentionally flat or too brief for depth differentiation to matter

## Do
- Divide precipitation into foreground, middle, and distant layers when the scene needs spatial depth.
- Change apparent particle scale and screen-space speed with depth instead of moving every streak or flake at one identical rate.
- Keep successive positions aligned along a readable track so fast rain or drifting snow does not appear as disconnected random marks.
- Stagger births, impacts, and disappearances so the whole field does not reset on one frame.
- Use longer, phase-offset, or different-length cycles across layers when repeated tracks would otherwise become visible.
- Match trajectory character to the phenomenon: rain can use faster directional streaks, while gentle snow can follow slower wavy or drifting paths.
- When wind increases, bias trajectories and introduce gusts or eddies through the paths rather than merely rotating an unchanged flat particle sheet.

## Don't
- Do not give near and far precipitation identical particle size, speed, and density when depth should be visible.
- Do not let particles teleport between unrelated positions from frame to frame.
- Do not align repeated cycles so all layers reset together unless a deliberately mechanical effect is intended.
- Do not preserve the same track character for gentle snow, driving rain, and windblown precipitation when their motion cues need to differ.

## Checklist
- Foreground and background precipitation differ in a way that reinforces depth.
- Individual motion tracks remain directionally continuous enough to read as falling or drifting matter.
- Cycle lengths or phases do not expose an obvious synchronized reset.
- Particle appearance and disappearance are staggered.
- Wind, if present, alters the actual path behavior rather than only the graphic slant.

## Notes
Precipitation is easiest to read when it is treated as many related tracks distributed through depth. Layering permits different apparent scales and rates, while staggered or unequal cycles prevent the field from revealing its repetition. Fixed frame counts are not the durable rule; the useful test is whether the trajectories, depth separation, and repeat structure remain convincing at the intended shot scale and playback rate.
