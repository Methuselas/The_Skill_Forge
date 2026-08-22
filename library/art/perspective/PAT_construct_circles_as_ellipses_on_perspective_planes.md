---
object_id: PAT_construct_circles_as_ellipses_on_perspective_planes
object_type: pattern
name: Construct Circles as Ellipses on Perspective Planes
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
- circle
- ellipse
- center
cross_links:
- rel: related_to
  target_object_id: PAT_turn_cylinder_end_curves_with_depth
reference:
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
confidence: high
references: []
variants:
- variant_id: VAR_eissen_derive_perspective_frame_from_established_ellipse
  variant_name: Derive a Perspective Frame From an Established Ellipse
  variant_basis: method_sequence
  difference_from_foundation: 'Reverses the usual square-to-circle construction for fast product sketching: begin from an
    already established ellipse, choose the relevant axial/world direction through it, infer the corresponding tangent relationships,
    and use those tangencies to recover an enclosing perspective frame around the ellipse. The ellipse major/minor axes remain
    its own orientation reference; different chosen object directions can produce different valid tangent frames around the
    same ellipse.'
  when_to_use: Use when an ellipse or cylindrical feature is already the dominant established element and the surrounding
    block, plane, or product structure needs to be built from it.
  when_not_to_use: Do not use the tangent estimate as a metrological substitute for exact square-to-circle construction when
    precision matters, and avoid relying on it when the ellipse is so flat that the tangent directions are visually unstable.
  absorbed_from_object_id: none
---

# Construct Circles as Ellipses on Perspective Planes

## Pattern Rule
**IF** a real circle lies on a plane turned away from the picture plane, **THEN** construct its enclosing square in perspective, use the square to locate the circle's true projected center and tangency structure, and draw the visible circle as an ellipse fitted to that plane.

## Do
- Start from a perspective square or rectangle that contains the circle.
- Use the square's diagonals to locate the projected center of the real circle.
- Use the plane's center and edge relationships to place opposite points and tangencies before refining the ellipse.
- Make the ellipse flatter as the circular plane turns farther from a face-on view.
- Keep the major and minor ellipse directions perpendicular in the visible ellipse while distinguishing that geometric ellipse center from the projected center needed for construction.

## Don't
- Bisect the real circle in perspective by simply using the visible ellipse's widest midpoint.
- Freehand an ellipse whose orientation disagrees with the plane carrying it.
- Let the circle float independently of the square or plane perspective.

## Checklist
- The ellipse belongs to the same plane as its enclosing perspective square.
- Opposite structural points correspond through the square's true projected center.
- The amount of ellipse compression agrees with the plane's turn.
- The construction can support a cylinder or cone without shifting the circle afterward.

## Notes
The important D'Amelio delta beyond the existing figure-cylinder card is that the visually centered ellipse is not always the correct metrological center of the original circle in perspective.

**Boundaries**
This Pattern is about projected circles on planes. Organic cross-contours may use looser ellipse cues when exact circle-center construction is unnecessary.

`VAR_eissen_derive_perspective_frame_from_established_ellipse` preserves Eissen and Steur's complementary product-sketch route: when the ellipse exists first, recover a useful surrounding perspective frame from chosen direction and tangent relationships rather than rebuilding the ellipse from a square. Keep it as an estimation method, especially because very flat ellipses make tangent recovery unreliable.
