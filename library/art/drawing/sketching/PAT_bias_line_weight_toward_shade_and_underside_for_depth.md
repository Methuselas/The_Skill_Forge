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
  difference_from_foundation: 'Assigns hierarchy from edge role rather than primarily from lighting: emphasize important ground/contact edges and free separating edges with open space behind them, keep interior or descriptive edges lighter, and allow receding construction to lose weight with depth. When distinct spatial planes must separate clearly in line art, step contour weight down from foreground to middle ground to background instead of outlining every plane equally.'
  when_to_use: Use for quick line drawings where spatial separation must read clearly before or without a committed lighting scheme, especially when foreground, middle-ground, and background planes otherwise collapse together.
  when_not_to_use: Do not let spatial-role weighting contradict a strong established light hierarchy or turn every silhouette
    into one uniformly heavy outline.
  absorbed_from_object_id: none
- variant_id: VAR_martin_anchor_line_weight_to_primary_light_and_scene_continuity
  variant_name: Anchor Line Weight to Primary Light and Scene Continuity
  variant_basis: context
  difference_from_foundation: Uses the primary light as the stable backbone of the contour-weight system when multiple lights or sequential panels complicate the drawing; secondary light modifies highlights and local details without overturning the main shade-side hierarchy, and the chosen logic persists through a continuous scene unless a deliberate dramatic break is intended.
  when_to_use: Use when an inked figure, face, or object has more than one source or appears across several panels and line weight needs a consistent causal lighting basis.
  when_not_to_use: Do not force physical continuity when the image intentionally changes lighting for dramatic effect, and do not let the primary-light shorthand override a clearly designed local value pattern.
  absorbed_from_object_id: none
---

# Bias Line Weight Toward Shade and Underside for Depth

## Pattern Rule
**IF** a mostly linear drawing or ink pass needs stronger depth and form separation before or without full tonal rendering
**THEN** increase line weight selectively along boundaries that fall on the shaded side or underside of the form, keeping light-facing boundaries comparatively lighter so the line hierarchy agrees with the chosen illumination
**ELSE** keep a more even descriptive line when lighting is intentionally neutral, diagrammatic, or not yet established

## Do
- Establish the light direction first so heavier boundaries follow a cause instead of becoming decorative accents.
- Strengthen lower edges and shade-side contour passages enough to suggest weight and turning without converting the entire silhouette into one heavy outline.
- Keep construction and light-facing edges lighter where they only need to locate form.
- Keep equivalent weight classes internally consistent enough that one isolated passage does not imply a different light or hierarchy by accident.
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

`VAR_olofsson_assign_line_weight_by_spatial_edge_role` is the non-lighting branch. A line can gain weight because it marks contact with the ground or a free edge separating the object from open space, while interior descriptive edges stay lighter. When several depth planes need separation, foreground contours may carry more weight than middle-ground contours and background contours may be finer still, provided this spatial hierarchy does not contradict an established light hierarchy.

`VAR_martin_anchor_line_weight_to_primary_light_and_scene_continuity` keeps one primary light as the causal anchor when secondary sources or sequential panels would otherwise make contour weight drift. The same head or form can reverse its heavy/light contour logic under a genuinely different source direction; the weight is evidence of the chosen light, not a fixed anatomy formula.
