---
object_id: AP_construct_cast_shadows_in_perspective
object_type: ap
name: Construct Cast Shadows in Perspective
library_path:
- art
- drawing
- perspective
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- perspective
- shadow
- light
- projection
cross_links: []
reference:
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
confidence: high
references: []
variants:
- variant_id: VAR_reconstruct_shadows_across_complex_receivers
  variant_name: Reconstruct Shadows Across Changing Receivers
  variant_basis: method_sequence
  difference_from_foundation: 'Absorbs Norling''s receiver-turn checkpoint and extends it to inclined, multi-plane, and curved receivers: keep the same light ray but reconstruct each intersection on the new receiving geometry.'
  when_to_use: Use when a cast shadow crosses a wall, incline, curved form, or other receiver break.
  when_not_to_use: Do not continue a shadow as one flat screen-space contour across changing receiver geometry.
  absorbed_from_object_id: none
- variant_id: VAR_link_cast_shadow_to_terminator_and_depth_grade
  variant_name: Link Cast Shadow to Terminator and Depth Grade
  variant_basis: method_sequence
  difference_from_foundation: Connects solved cast-shadow geometry to the form's light/shade separation, then hands distant contrast weakening to the atmosphere/rendering system.
  when_to_use: Use when carrying a perspective shadow solution into a rendered scene.
  when_not_to_use: Do not let atmospheric weakening alter the geometric receiver intersections already solved.
  absorbed_from_object_id: none
---

# Construct Cast Shadows in Perspective

## Objective
Project cast shadows so the light direction, receiving plane, object position, and scene perspective all agree.

## Steps / Flow
**Entry Conditions**
- A cast shadow must be placed constructively rather than guessed from value alone.
- The receiving plane and the object's placement are sufficiently established to support projection.

**Persistent Invariants**
- Shade is the unlit side of the form; cast shadow is the region on another surface from which the light is blocked.
- The shade boundary supplies the points that cast the shadow.
- Sunlight is treated as parallel rays; a nearby point light uses rays diverging from the source.
- Shadow construction must remain consistent with the receiving plane's perspective.

**Flow**
1. **Classify the light.** Use the parallel-sun branch or the local-point-source branch.
2. **Find the shade boundary.** Identify the object's edge or line separating light-facing and turned-away surfaces.
3. **Solve the receiving-plane direction.** Establish how shadow-bearing lines travel across that plane.
4. **Parallel sunlight branch.** Keep the light rays parallel in space. When oblique to the picture plane, use the light-ray vanishing point and the shadow-direction vanishing point in their corresponding perspective relationship.
5. **Local point-source branch.** Draw rays from the actual light source through the relevant shade-boundary points; use the source's projection onto the plane to establish the shadow direction for upright forms.
6. **Intersect constructions.** The intersections locate exact cast-shadow points; connect them in the order supplied by the casting boundary.
7. **Validate.** Confirm that a lower sun gives longer projected shadows and a higher sun shorter ones in the book's construction, and that local-light shadows fan consistently from the source.

**Failure / Rollback Rules**
- If the shadow direction contradicts the receiving plane, re-solve that plane before moving the shadow.
- If sunlight rays diverge, return to the parallel-light branch.
- If a point-source shadow behaves as parallel sunlight, return to source projection and ray intersections.
- If the casting boundary is wrong, repair the shade line before adjusting the shadow contour.

**Completion Criteria**
- Shadow points can be traced back to valid casting points and light rays.
- The shadow lies on the receiving plane rather than floating over it.
- Parallel and point-source lights produce visibly different but internally coherent projection behavior.
- The cast shadow supports, rather than contradicts, the scene's established depth field.

## Notes
D'Amelio's chapter is geometric, but the operational question is simple: identify what blocks the light, establish how the rays travel, and solve where those rays meet the receiving surface.

Variants retained in this canonical object: `VAR_reconstruct_shadows_across_complex_receivers`, `VAR_link_cast_shadow_to_terminator_and_depth_grade`.
