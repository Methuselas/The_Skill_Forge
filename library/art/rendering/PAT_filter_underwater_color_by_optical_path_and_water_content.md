---
object_id: PAT_filter_underwater_color_by_optical_path_and_water_content
object_type: pattern
name: Filter Underwater Color by Optical Path and Water Content
library_path:
- art
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- underwater
- water
- color
- atmosphere
- optical_path
cross_links:
- rel: related_to
  target_object_id: PAT_model_water_surface_from_view_angle_reflection_transmission_and_wave_distortion
- rel: related_to
  target_object_id: PAT_grade_depth_with_atmospheric_effect
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants: []
references: []
---

# Filter Underwater Color by Optical Path and Water Content

## Pattern Rule
**IF** forms are viewed through a meaningful thickness of water
**THEN** grade color, contrast, and visibility by the total optical path through the water and by what the water contains, allowing longer paths to lose warm wavelengths and approach the prevailing water color
**ELSE** preserve fuller local color in shallow or exceptionally clear short-path conditions.

## Do
- Treat horizontal and vertical water paths consistently; what matters is total distance through the medium, not depth alone.
- Let longer clear-water paths progressively suppress warm color, compress contrast, and bias forms toward blue-green where the water supports it.
- Shift the prevailing color and visibility for silt, clay, algae, or other suspended content instead of applying a universal cyan overlay.
- Allow a nearby artificial source to restore warmer color only within the limited path where its light can still reach and return.
- Combine this underwater filter with surface reflection/transmission when the viewer looks through a water surface.

## Don't
- Use fixed depth thresholds as universal laws independent of clarity and water content.
- Apply the same blue cast to muddy, algae-rich, clear, or shallow water.
- Restore full warm local color at long range without a plausible local source.

## Checklist
- Color loss follows optical path length and water properties.
- Contrast and detail diminish consistently with the same medium.
- Local artificial light affects only the region its path can plausibly support.

## Notes
Underwater color behaves like a volumetric filter. The robust rule is path length plus medium content; exact distances vary too much with clarity and composition to serve as universal thresholds.
