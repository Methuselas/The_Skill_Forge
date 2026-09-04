---
object_id: PAT_construct_reflections_across_arbitrary_planes
object_type: pattern
name: Construct Reflections Across Arbitrary Planar Mirrors
library_path:
- art
- perspective
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- perspective
- reflection
- mirror
- oblique
cross_links: []
reference:
  source_title: 'Perspective: A Guide for Artists, Architects and Designers'
  author: Gwen White
confidence: high
references: []
variants: []
---

# Construct Reflections Across Arbitrary Planar Mirrors

## Pattern Rule
**IF** a planar reflecting surface is not necessarily level, **THEN** treat the reflection as real geometry mirrored across that plane: establish the mirror plane, reflect controlling points/directions using equal incidence and reflection, derive the reflected direction families, and then project the reflected geometry through the same camera/view field.

## Do
- Establish the mirror plane before drawing the reflected object: its trace/direction and, when tipped, its plane orientation matter.
- Use a small plan and/or elevation when the reflected direction is not obvious; reflect rays/directions so the angle of incidence equals the angle of reflection.
- Use source-to-mirror contact points as anchors where structural lines meet the mirror plane.
- Preserve equal perpendicular source/image distance across a level mirror or calm-water plane; this is the simple branch already captured by Norling.
- For vertical or tipped mirrors, derive the reflected direction family from the mirror geometry rather than reusing the source object's vanishing point automatically.
- Once the reflected geometry is defined in space, construct it with ordinary perspective/oblique-perspective methods and measuring points as needed.
- Validate with both position and direction: a reflected point must be located correctly across the mirror, and reflected parallel edges must converge according to their reflected world direction.
- For curved or circular forms, mirror the three-dimensional geometry across the reflection plane and reproject it from the same camera; allow reflected ellipses to change apparent openness and projected proportion as their mirrored spatial positions change.

## Don't
- Flip the visible silhouette in screen space and assume the result is a valid perspective reflection.
- Give every mirror reflection the source object's original vanishing points; that is only safe in specific symmetric/level cases.
- Treat the mirror as decoration after the reflected object has already been guessed.
- Use the advanced tipped-mirror construction when a simple calm-water equal-distance reflection is sufficient.

## Checklist
- The mirror plane has a coherent orientation in the scene.
- Source and reflected constructions satisfy equal incidence/reflection in the plan/elevation used to derive them.
- Contact points on the mirror remain fixed between source and reflected geometry.
- Reflected parallel families share their own correct vanishing destinations.
- The level-plane branch collapses cleanly to equal perpendicular distances across the reflecting plane.

## Notes
This Pattern subsumes the earlier level-plane reflection owner. The simple level reflection remains a fast branch inside the general planar case.

**Boundaries**
This Pattern covers flat mirrors and calm planar water. Curved mirrors, rippled water, refractive surfaces, and lens effects require different optics and are outside these planar constructions.

A reflection is not a screen-space copy of the visible silhouette. Curved forms make the error obvious: a mirrored circle may project as an ellipse with a different apparent openness because the reflected geometry occupies a different spatial position relative to the same camera. Contact points on the mirror plane remain useful anchors, but the reflected form must be reprojected.
