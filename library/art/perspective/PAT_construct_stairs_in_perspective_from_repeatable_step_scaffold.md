---
object_id: PAT_construct_stairs_in_perspective_from_repeatable_step_scaffold
object_type: pattern
name: Construct Stairs In Perspective From Repeatable Step Scaffold
library_path:
- art
- perspective
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- perspective
- stairs
- repeated_spacing
- environment
- construction
cross_links:
- rel: related_to
  target_object_id: PAT_construct_inclined_planes_from_base_vanishing_directions
- rel: related_to
  target_object_id: PAT_measure_subdivide_and_repeat_on_perspective_planes
reference:
  source_title: The Art of Layout and Storyboarding
  author: Mark T. Byrne
confidence: high
references: []
variants: []
---

# Construct Stairs In Perspective From Repeatable Step Scaffold

## Pattern Rule
**IF** a staircase must remain convincing through depth, hidden portions, or a changing view
**THEN** solve one trustworthy step inside a perspective scaffold and propagate the tread/riser relationship geometrically instead of guessing each step independently.

## Do
- Establish the scene perspective and the stair run before detailing individual steps.
- For a straight stair, solve one tread depth and riser height, then use the run's perspective and an auxiliary inclined direction to locate the succeeding steps.
- Continue the full construction where steps become hidden or cross the horizon so the visible portions inherit correct spacing rather than drifting.
- For a spiral stair, establish an outer cylindrical scaffold, divide its base into repeatable radial segments, advance the step height through those divisions, and preserve hidden rear construction.
- Add an inner cylindrical scaffold when the stair needs a controlled inner tread edge.
- Apply material and decorative treatment only after the repeated stair geometry is stable.

## Don't
- Do not stack individually eyeballed steps and expect their height and depth to remain consistent through recession.
- Do not stop constructing a step at the horizon or at an occlusion when the hidden geometry is needed to locate later steps.
- Do not treat a spiral stair as a flat fan pasted into a cylinder.
- Do not force every stair into one fixed tread/riser proportion; solve the intended design first, then propagate it consistently.

## Checklist
- One coherent perspective field governs the stair and surrounding environment.
- Tread depth and riser height change through depth without cumulative drift.
- Hidden or rear steps can be reconstructed from the same scaffold as visible steps.
- Spiral stairs follow a cylindrical parent structure rather than an arbitrary 2D spiral.
- Material detail does not conceal unresolved stair geometry.

## Notes
The durable operation is to solve the repeating step relationship once inside a trustworthy parent scaffold, then propagate it through the scene geometry. Byrne demonstrates both straight and spiral stair constructions; the exact paper-and-ruler procedure is optional, while the repeatable scaffold is the transferable decision.
