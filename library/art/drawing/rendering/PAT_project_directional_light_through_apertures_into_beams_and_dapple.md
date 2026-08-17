---
object_id: PAT_project_directional_light_through_apertures_into_beams_and_dapple
object_type: pattern
name: Project Directional Light Through Apertures Into Beams and Dapple
library_path:
- art
- drawing
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- lighting
- sunbeams
- dappled_light
- aperture
- projection
cross_links:
- rel: related_to
  target_object_id: PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_gurney_reveal_sunbeams_in_participating_atmosphere
  variant_name: Reveal Sunbeams in Participating Atmosphere
  variant_basis: context
  difference_from_foundation: Makes a light beam visible only when suspended particles or moisture scatter enough
    light toward the viewer, with visibility strengthened by a darker surround and a view sufficiently toward the
    source.
  when_to_use: Use for dust, mist, smoke, or haze where a directional source passes through an aperture or obstruction
    and the atmosphere itself can reveal the light volume.
  when_not_to_use: Do not draw a visible beam in perfectly clear air or ignore the source/aperture geometry.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_project_dappled_sun_disks_through_small_openings
  variant_name: Project Dappled Sun Disks Through Small Openings
  variant_basis: context
  difference_from_foundation: Treats sufficiently small leaf gaps as pinhole projectors of the solar disk, producing
    spots whose shape follows receiver orientation and whose size/softness grows with canopy-to-receiver distance.
  when_to_use: Use when directional sun passes through many small foliage gaps and distinct dappled spots are visible
    on a receiver.
  when_not_to_use: Do not make every leaf-shaped opening produce a leaf-shaped light spot or keep all spots equally
    sharp regardless of distance.
  absorbed_from_object_id: none
references: []
---

# Project Directional Light Through Apertures Into Beams and Dapple

## Pattern Rule
**IF** strong directional light passes through openings in an occluder
**THEN** solve the source-to-aperture-to-receiver geometry first, keeping distant-sun rays parallel in world space while perspective and receiver orientation determine the visible beam or projected light pattern
**ELSE** use broad source illumination without aperture projection.

## Do
- Establish source direction before drawing openings, beams, or light spots.
- Let aperture shape influence the projected volume while allowing small openings to behave more like image-forming pinholes.
- Increase projection size and softness as aperture-to-receiver distance grows.
- Distinguish visible light volume in atmosphere from a bright patch projected onto a surface.
- Apply receiver perspective and orientation to the projected shape.

## Don't
- Make parallel sunlight physically fan out in world space because the visible beams converge in perspective.
- Copy opening silhouettes mechanically onto receivers at every scale.
- Add beams or dapples without a plausible occluder and source.

## Checklist
- Source direction, aperture position, and receiver agree geometrically.
- Projection scale/softness changes with distance.
- Visible beams and surface dapples are distinguished by their optical cause.

## Notes
Beams and dapple share one projection logic. The difference is what reveals the light: participating atmosphere makes the volume visible, while a receiver makes the projected patch visible.

`VAR_gurney_reveal_sunbeams_in_participating_atmosphere` Makes a light beam visible only when suspended particles or moisture scatter enough light toward the viewer, with visibility strengthened by a darker surround and a view sufficiently toward the source. Use it when for dust, mist, smoke, or haze where a directional source passes through an aperture or obstruction and the atmosphere itself can reveal the light volume Avoid it when draw a visible beam in perfectly clear air or ignore the source/aperture geometry .

`VAR_gurney_project_dappled_sun_disks_through_small_openings` Treats sufficiently small leaf gaps as pinhole projectors of the solar disk, producing spots whose shape follows receiver orientation and whose size/softness grows with canopy-to-receiver distance. Use it when when directional sun passes through many small foliage gaps and distinct dappled spots are visible on a receiver Avoid it when make every leaf-shaped opening produce a leaf-shaped light spot or keep all spots equally sharp regardless of distance .
