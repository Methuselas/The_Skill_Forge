---
object_id: PAT_bias_line_weight_toward_shade_and_underside_for_depth
object_type: pattern
name: Bias Line Weight Toward Shade and Underside for Depth
library_path:
- art
- drawing
- sketching
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- sketching
- line_weight
- form
- lighting
- depth
cross_links:
- rel: related_to
  target_object_id: PAT_design_lighting_to_serve_subject_mood_and_visual_intent
reference:
  source_title: 'Sketching: Drawing Techniques for Product Designers'
  author: Koos Eissen and Roselien Steur
confidence: high
references: []
variants:
- variant_id: VAR_olofsson_assign_line_weight_by_spatial_edge_role
  variant_name: Assign Line Weight by Spatial Edge Role
  variant_basis: emphasis
  difference_from_foundation: 'Assigns hierarchy from edge role rather than primarily from lighting: emphasize important ground/contact
    edges and free separating edges with open space behind them, keep interior or descriptive edges lighter, and allow receding
    construction to lose weight with depth.'
  when_to_use: Use for quick product drawings where spatial separation must read clearly before or without a committed lighting
    scheme.
  when_not_to_use: Do not let spatial-role weighting contradict a strong established light hierarchy or turn every silhouette
    into one uniformly heavy outline.
  absorbed_from_object_id: none
---

# Bias Line Weight Toward Shade and Underside for Depth

## Pattern Rule
**IF** a mostly linear product sketch needs stronger depth and form separation before full tonal rendering
**THEN** increase line weight selectively along boundaries that fall on the shaded side or underside of the form, keeping light-facing boundaries comparatively lighter so the line hierarchy agrees with the chosen illumination
**ELSE** keep a more even descriptive line when lighting is intentionally neutral, diagrammatic, or not yet established

## Do
- Establish the light direction first so heavier boundaries follow a cause instead of becoming decorative accents.
- Strengthen lower edges and shade-side contour passages enough to suggest weight and turning without converting the entire silhouette into one heavy outline.
- Keep construction and light-facing edges lighter where they only need to locate form.
- Recheck the line-only sketch from a distance before adding tone; the heavier passages should already help the object sit in space.

## Don't
- Do not thicken every outer contour equally; uniform bold outlining flattens the lighting cue this method depends on.
- Do not place heavy accents on the light-facing side merely because an edge feels important.
- Do not use line weight to conceal unresolved construction, proportions, or perspective.

## Checklist
- The heaviest descriptive lines cluster plausibly toward shaded or lower-facing boundaries.
- Light-facing edges remain available as lighter lines instead of being swallowed by one continuous outline.
- The object reads as more solid before any large tone fields are added.
- The line hierarchy remains subordinate to the actual form and chosen light direction.

## Notes
A product sketch can begin describing light before marker or pencil shading is applied. Selective weight on the shaded side and underside turns line thickness into a compact form cue: the same object can feel more grounded and dimensional while the drawing is still mostly linear. The useful constraint is causal placement. Heavier line is not a generic emphasis device here; it is a shorthand for the side of the form that turns away from the descriptive light.

`VAR_olofsson_assign_line_weight_by_spatial_edge_role` is the non-lighting branch. A line can gain weight because it marks contact with the ground or a free edge separating the object from open space, while interior descriptive edges stay lighter. Use it when spatial organization needs to read before a full light setup exists.
