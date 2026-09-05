---
object_id: PAT_model_daytime_sky_from_solar_glare_and_horizon_glow
object_type: pattern
name: Model Daytime Sky From Solar Glare and Horizon Glow
library_path:
- art
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- rendering
- sky
- atmosphere
- solar_glare
- horizon_glow
- color_gradation
cross_links:
- rel: related_to
  target_object_id: PAT_design_color_gradation_across_hue_value_and_chroma
- rel: related_to
  target_object_id: PAT_grade_depth_with_atmospheric_effect
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_gurney_build_sunset_from_low_sun_air_layers_cloud_height_and_earth_shadow
  variant_name: Build Sunset From Low Sun, Air Layers, Cloud Height, and Earth Shadow
  variant_basis: context
  difference_from_foundation: 'Constructs sunset as a layered illumination problem: long-path warm solar light, cloud altitude, solar direction, and the rising antisolar earth shadow replace a generic orange vertical gradient.'
  when_to_use: Use for sunrise/sunset scenes where the sky and cloud layers need believable directional color structure.
  when_not_to_use: Do not distribute equal orange across the whole sky or ignore cloud altitude and the antisolar side.
  absorbed_from_object_id: none
references: []
---

# Model Daytime Sky From Solar Glare and Horizon Glow

## Pattern Rule
**IF** a clear daytime sky must be rendered as a coherent color field
**THEN** combine solar glare as a function of angular distance from the sun with horizon glow as a function of elevation, allowing hue, value, and chroma to vary across both dimensions instead of using one fixed vertical blue gradient
**ELSE** let cloud, haze, or another atmospheric condition define the dominant sky model.

## Do
- Near the sun, allow the sky to become lighter, warmer, and less purely blue.
- Away from the sun, allow the blue to deepen and strengthen where the atmosphere supports it.
- Toward the horizon, generally lighten and weaken the blue because the view travels through more air.
- Place the deepest blue relative to the sun's position rather than permanently fixing it at the zenith.
- Modify the baseline for haze, cloud cover, time of day, altitude, and atmospheric loading.

## Don't
- Paint a sky as one top-to-bottom gradient regardless of solar direction.
- Make the horizon glow equally strong in every weather condition.
- Treat a clear-sky baseline as a universal recipe for clouded or smoky skies.

## Checklist
- The sky changes both with elevation and with angular distance from the sun.
- The deepest and warmest regions make sense relative to solar direction.
- Atmospheric conditions modify rather than contradict the baseline logic.

## Notes
A clear sky is a two-dimensional color field. Solar glare and horizon glow overlap, which explains why the strongest blue is not simply 'at the top' and why sky gradients often change hue, value, and chroma simultaneously.

`VAR_gurney_build_sunset_from_low_sun_air_layers_cloud_height_and_earth_shadow` Constructs sunset as a layered illumination problem: long-path warm solar light, cloud altitude, solar direction, and the rising antisolar earth shadow replace a generic orange vertical gradient. Use it when for sunrise/sunset scenes where the sky and cloud layers need believable directional color structure Avoid it when distribute equal orange across the whole sky or ignore cloud altitude and the antisolar side .
