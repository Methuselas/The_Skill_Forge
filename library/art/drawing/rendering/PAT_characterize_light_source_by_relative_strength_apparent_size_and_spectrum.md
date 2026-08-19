---
object_id: PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum
object_type: pattern
name: Characterize a Light Source by Relative Strength, Apparent Size, and Spectrum
library_path:
- art
- drawing
- rendering
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- lighting
- light_source
- spectrum
- source_size
- falloff
cross_links:
- rel: related_to
  target_object_id: PAT_design_lighting_to_serve_subject_mood_and_visual_intent
- rel: supports
  target_object_id: PAT_resolve_visible_color_from_local_color_light_and_reflection
- rel: supports
  target_object_id: PAT_control_edge_hardness_from_form_light_and_focus
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_gurney_decompose_clear_day_into_sun_skylight_and_bounce
  variant_name: Decompose Clear Day Into Sun, Skylight, and Bounce
  variant_basis: context
  difference_from_foundation: Treats clear daylight as a dominant direct sun plus broad blue-sky fill and local
    reflected bounce instead of one generic daylight source.
  when_to_use: Use for clear outdoor daylight where direct sun, sky exposure, and ground or nearby reflection all
    materially affect the shadow family.
  when_not_to_use: Do not force a blue-sky/warm-ground split when cloud, haze, colored surroundings, or another
    environment changes those secondary sources.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_model_overcast_as_large_diffuse_sky_source
  variant_name: Model Overcast as a Large Diffuse Sky Source
  variant_basis: context
  difference_from_foundation: Treats a cloud-covered sky as a very broad source that compresses light-shadow contrast,
    softens directional evidence, and favors large color shapes.
  when_to_use: Use when cloud cover broadly diffuses the sun and the scene lacks crisp direct-sun cast shadows.
  when_not_to_use: Do not use for partly cloudy conditions where distinct sun patches still survive.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_model_window_daylight_as_aperture_plus_exterior_bounce
  variant_name: Model Window Daylight as Aperture Plus Exterior Bounce
  variant_basis: context
  difference_from_foundation: Treats a window or open door as an aperture admitting cool sky-dominant daylight plus
    possible upward light reflected from exterior ground or surroundings.
  when_to_use: Use for interiors where daylight enters through a bounded opening and exterior surfaces materially
    alter the fill color.
  when_not_to_use: Do not assume every window is cool or every ceiling receives warm bounce; inspect or design the
    actual exterior sources.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_apply_inverse_square_falloff_to_local_point_source
  variant_name: Apply Inverse-Square Falloff to a Local Point Source
  variant_basis: constraint
  difference_from_foundation: Uses the physical point-source baseline that illumination weakens rapidly with distance,
    approximately to one quarter at twice the distance and one ninth at three times the distance.
  when_to_use: Use for compact nearby emitters such as candles, bare bulbs, or small lamps when distance variation
    across the subject is large enough to matter.
  when_not_to_use: Do not apply the point-source law literally to broad area lights, distant sun, or scenes where
    exposure/compression intentionally remaps the physical ratio.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_model_golden_hour_as_warm_weakened_sun_plus_rich_sky_fill
  variant_name: Model Golden Hour as Warm Weakened Sun Plus Rich Sky Fill
  variant_basis: context
  difference_from_foundation: Treats low-angle sun as a weaker, substantially warmer key while the sky remains a
    rich cool secondary source, producing strong but causally motivated warm/cool separation.
  when_to_use: Use near dawn or dusk when the long atmospheric path has reddened and weakened direct sunlight while
    skylight still fills shadows.
  when_not_to_use: Do not invent identical blue shadows in every golden-hour scene; actual sky, ground, cloud, and
    surrounding bounce still determine the fill.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_model_partly_cloudy_day_as_sun_patches_under_cloud_fill
  variant_name: Model Partly Cloudy Day as Sun Patches Under Cloud Fill
  variant_basis: context
  difference_from_foundation: Treats partly cloudy conditions as direct sunlight surviving in moving patches while
    cloud-shadow regions receive a mixture of open-sky and diffuse cloud illumination, with softer cloud-shadow
    boundaries than hard local occluders.
  when_to_use: Use when clouds intermittently block the sun but do not create a fully overcast sky.
  when_not_to_use: Do not model the scene as either clear sun everywhere or uniform overcast, and do not use arbitrary
    hard spotlight patches unrelated to the cloud field.
  absorbed_from_object_id: none
references: []
---

# Characterize a Light Source by Relative Strength, Apparent Size, and Spectrum

## Pattern Rule
**IF** a light source must be rendered, compared, or combined with other sources
**THEN** characterize its relative strength at the subject, apparent angular size from the subject, and spectral/color output before assigning shadows, edge softness, color bias, or hierarchy
**ELSE** use a simpler lighting description when those variables are visually negligible.

## Do
- Compare source strength at the receiving surface rather than by bulb name, wattage, or apparent brightness alone.
- Judge hardness from how large the luminous source appears from the subject's position; apparent size, not physical size by itself, governs penumbra breadth.
- Treat source spectrum as a color-availability constraint: uneven spectral output can strengthen some color families while weakening others.
- Judge color under the illuminant that will actually light or display the subject; a material match made under one source can shift in hue, value, or chroma under another source even when the nominal local color is unchanged.
- Separate primary and secondary sources so their effects can be combined causally instead of painted as one undifferentiated tint.
- Re-evaluate the source model when distance, diffusion, cloud cover, aperture geometry, or surrounding bounce changes.

## Don't
- Equate a physically large but distant source with a soft source automatically.
- Treat every warm or cool light as a uniform color overlay independent of spectrum and receiving material.
- Judge multiple sources by absolute labels instead of their relative contribution at the subject.

## Checklist
- Each important source has a stated relative strength, apparent size, and color/spectral character.
- Shadow softness and color shifts follow those source properties.
- Critical color judgments have been checked under the intended viewing illuminant when source spectrum differs materially.
- Secondary sources remain subordinate or competitive according to their actual contribution.

## Notes
Source description becomes operational when it predicts consequences. Strength mainly controls contribution and hierarchy; apparent size controls edge softness; spectrum controls which color responses the source can support. Distance and environment can modify all three.

`VAR_gurney_model_golden_hour_as_warm_weakened_sun_plus_rich_sky_fill` Treats low-angle sun as a weaker, substantially warmer key while the sky remains a rich cool secondary source, producing strong but causally motivated warm/cool separation.

`VAR_gurney_model_partly_cloudy_day_as_sun_patches_under_cloud_fill` Treats partly cloudy conditions as direct sunlight surviving in moving patches while cloud-shadow regions receive a mixture of open-sky and diffuse cloud illumination, with softer cloud-shadow boundaries than hard local occluders.

`VAR_gurney_decompose_clear_day_into_sun_skylight_and_bounce` Treats clear daylight as a dominant direct sun plus broad blue-sky fill and local reflected bounce instead of one generic daylight source. Use it when for clear outdoor daylight where direct sun, sky exposure, and ground or nearby reflection all materially affect the shadow family Avoid it when force a blue-sky/warm-ground split when cloud, haze, colored surroundings, or another environment changes those secondary sources .

`VAR_gurney_model_overcast_as_large_diffuse_sky_source` Treats a cloud-covered sky as a very broad source that compresses light-shadow contrast, softens directional evidence, and favors large color shapes. Use it when when cloud cover broadly diffuses the sun and the scene lacks crisp direct-sun cast shadows Avoid it when use for partly cloudy conditions where distinct sun patches still survive .

`VAR_gurney_model_window_daylight_as_aperture_plus_exterior_bounce` Treats a window or open door as an aperture admitting cool sky-dominant daylight plus possible upward light reflected from exterior ground or surroundings. Use it when for interiors where daylight enters through a bounded opening and exterior surfaces materially alter the fill color Avoid it when assume every window is cool or every ceiling receives warm bounce; inspect or design the actual exterior sources .

`VAR_gurney_apply_inverse_square_falloff_to_local_point_source` Uses the physical point-source baseline that illumination weakens rapidly with distance, approximately to one quarter at twice the distance and one ninth at three times the distance. Use it when for compact nearby emitters such as candles, bare bulbs, or small lamps when distance variation across the subject is large enough to matter Avoid it when apply the point-source law literally to broad area lights, distant sun, or scenes where exposure/compression intentionally remaps the physical ratio .
