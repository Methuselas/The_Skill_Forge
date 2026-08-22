---
object_id: PAT_map_observed_subject_as_interlocking_positive_and_negative_shapes
object_type: pattern
name: Map an Observed Subject as Interlocking Positive and Negative Shapes
library_path:
- art
- foundations
- observation
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- observation
- positive_shape
- negative_shape
- placement
- proportion
cross_links: []
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants:
- variant_id: VAR_schmid_reduce_observed_scene_to_flat_color_value_edge_shapes
  variant_name: Reduce an Observed Scene to Flat Color, Value, and Edge Shapes
  variant_basis: emphasis
  difference_from_foundation: Extends flat-shape observation from contour and negative-space checking to the entire visible
    field, reading named objects temporarily as adjoining two-dimensional shapes defined by placement, shape/size, color or
    value, and edge character.
  when_to_use: Use when semantic knowledge of objects is causing the model to paint what things are supposed to look like
    instead of the particular light/color pattern actually observed.
  when_not_to_use: Do not discard structural knowledge permanently; return to form, anatomy, perspective, or material understanding
    when it helps interpret ambiguous evidence without overruling clear observation.
  absorbed_from_object_id: none
---
# Map an Observed Subject as Interlocking Positive and Negative Shapes

## Pattern Rule
**IF** an observed subject is difficult to place accurately because named parts or internal structure are biasing the drawing
**THEN** alternate between the subject's positive shapes and the adjacent or trapped negative shapes so shared boundaries provide independent placement checks
**ELSE** keep the structural construction primary when observational matching is not the task

## Do
- Begin with large enclosing or combined shapes before subdividing into smaller openings.
- Use trapped spaces between limbs, furniture bars, features, or other parts to test the same contour from the opposite side.
- Compare a three-dimensional construction against the two-dimensional shape map when one reading begins to drift.

## Don't
- Do not turn negative-space drawing into contour tracing without structural awareness.
- Do not solve every tiny gap before the major enclosing relationships are stable.

## Checklist
- Important boundaries agree when read from both the positive and negative side.
- Large shapes are placed before small trapped spaces are refined.
- A mismatch between 2-D shape and 3-D construction is investigated rather than ignored.

## Notes
Because a positive member and the space beside it share the same boundary, Dodson uses negative shapes as an alternate description of the subject. The method is portable across figures, animals, objects, vehicles, architecture, and creatures.

`VAR_schmid_reduce_observed_scene_to_flat_color_value_edge_shapes` broadens the flat-shape read to the whole visual field: temporarily suppress object names and compare adjoining shapes by placement, size, color/value, and edge before restoring structural interpretation where it helps.
