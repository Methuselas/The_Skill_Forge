---
object_id: PAT_grade_depth_with_atmospheric_effect
object_type: pattern
name: Grade Depth With Illuminated Atmospheric Effect
library_path:
- art
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- atmosphere
- depth
- value
- contrast
cross_links:
- rel: supports
  target_object_id: AP_construct_a_shared_scene_perspective_field
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
references: []
variants:
- variant_id: VAR_dodson_shift_texture_mark_vocabulary_with_distance
  variant_name: Shift Texture Mark Vocabulary With Distance
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Dodson''s perceptual-scale route: as repeated surface detail recedes, change the kind
    of mark used to represent it rather than merely shrinking the foreground stroke. Move from individual articulation to
    grouped texture, broader pattern, and finally near-omission as distance removes resolvable events.'
  when_to_use: Use when grass, foliage, crowds, windows, scales, fur, roof tiles, or other repeated detail extends through
    substantial depth and literal miniaturization would make the far field noisy or false.
  when_not_to_use: Do not change mark vocabulary so abruptly that equivalent surfaces stop belonging to the same material
    family, and do not use simplification to repair incorrect scale or perspective.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_shift_receding_colors_toward_atmospheric_influence
  variant_name: Shift Receding Colors Toward Atmospheric Influence
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a color-specific atmospheric-depth route: as forms recede, let their hue and chroma participate
    increasingly in the prevailing atmospheric influence while the existing near-to-far losses of contrast, edge clarity,
    and detail continue to operate.'
  when_to_use: Use when a colored scene needs stronger atmospheric integration across depth, especially in blue-sky distance,
    gray weather, haze, mist, or another clearly dominant air/light condition.
  when_not_to_use: Do not apply one canned cool shift to every scene; use the actual or designed atmospheric influence, and
    do not let color drift erase material identity or contradict the established light.
  absorbed_from_object_id: none
- variant_id: VAR_vilppu_use_atmospheric_contrast_as_local_depth_design
  variant_name: Use Atmospheric Contrast as Local Depth Design
  variant_basis: emphasis
  difference_from_foundation: 'Adds Vilppu''s figurative use of atmospheric perspective as a controlled design device: reduce
    contrast, detail, and edge clarity on receding or subordinate passages—even across relatively small depth changes—while
    keeping nearer or action-critical forms sharper, so overlapping masses separate and the main action reads more strongly.'
  when_to_use: Use when a figure's near/far organization is technically correct but visually crowded, or when atmospheric
    edge/value control can strengthen the action without changing the underlying construction.
  when_not_to_use: Do not apply arbitrary haze that contradicts the intended scene, material, lighting, or focal hierarchy;
    when physical atmospheric perspective matters, actual distance and medium conditions still govern.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_reverse_atmospheric_perspective_in_warm_near_sun_glare
  variant_name: Reverse Atmospheric Perspective in Warm Near-Sun Glare
  variant_basis: context
  difference_from_foundation: Handles the uncommon case where low-sun light scattered through mist, dust, or moist air overwhelms
    the usual blue veil so distant forms grow warmer rather than cooler with recession.
  when_to_use: Use when looking toward a low warm sun through enough participating atmosphere for orange/red scattered light
    to dominate the depth field.
  when_not_to_use: Do not generalize this exception into a default warm-distance rule; ordinary blue-sky haze often behaves
    differently.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_compress_depth_through_dense_fog_mist_smoke_or_dust
  variant_name: Compress Depth Through Dense Fog, Mist, Smoke, or Dust
  variant_basis: context
  difference_from_foundation: Accelerates contrast/chroma loss in dense suspended media and changes the lighting model when
    the medium becomes thick enough to diffuse or block direct sun; low mist with clear sun above remains a different condition.
  when_to_use: Use when dense participating media materially controls visibility, contrast, and illumination across depth.
  when_not_to_use: Do not treat all fog as uniform overcast; shallow mist under clear sun can retain direct light on forms
    while strongly brightening the surrounding shadow field.
  absorbed_from_object_id: none
---

# Grade Depth With Illuminated Atmospheric Effect

## Pattern Rule
**IF** a scene must separate depth through intervening air
**THEN** treat atmospheric perspective as viewing forms through illuminated air whose effect grows with optical distance and particle/moisture load, compressing contrast and chroma while shifting visible color toward the prevailing atmospheric illumination
**ELSE** keep depth cues geometric and local when intervening atmosphere is negligible.

## Do
- Establish the strongest readable value separation in the foreground or nearest important zone, then progressively compress that separation with distance.
- Let distant darks move toward the surrounding middle values and distant lights lose some local brilliance so far forms become less contrasty than near ones.
- Apply the same near-to-far logic to ground planes, repeated structures, cast shadows, and background forms that occupy the same atmosphere.
- Use the effect as a depth layer after the perspective field and major lighting relationships are already coherent.
- Preserve important light-versus-shade relationships while reducing their contrast as they recede; atmosphere should soften a solved form, not erase its structure arbitrarily.
- Let distant darks lighten and take on atmospheric/sky influence early, while illuminated surfaces lose chroma and approach the prevailing atmospheric color.
- Compress light-shadow contrast with distance until very distant forms can merge toward a common quiet silhouette without erasing the larger structure.
- Distinguish a quiet atmospheric silhouette from a hard backlit cutout: if backlighting turns a distant form into a crisp, high-contrast shape that visually advances, restore enough atmospheric influence, internal shadow variation, edge softness, or surrounding value integration to preserve the intended distance read.
- Treat the atmosphere itself as illuminated volume: a shaded parcel of air can appear darker or differently colored than adjacent sunlit haze even at similar geometric distance.
- Allow bright white objects to behave differently from dark objects instead of forcing every material through one identical cool-and-lighten recipe.
- Increase the effect for haze, moisture, dust, smoke, smog, or other particles that shorten the distance over which full contrast and chroma survive.

## Don't
- Fade distant objects while leaving their cast shadows or ground contacts equally black and crisp.
- Treat atmospheric depth as a background-only fog effect when middle-ground forms should also participate.
- Use contrast loss to repair wrong scale, convergence, overlap, or object placement.
- Import a simplified particle explanation as a complete physical theory of atmospheric scattering; keep the card at the observable rendering level.
- Do not preserve the old blanket rule that every receding color must become cooler; near-sun glare, warm haze, smoke, and other illumination states can reverse the hue shift.
- Do not assume every distant silhouette automatically reads as distant; a hard, high-contrast backlit cutout can visually advance and fight the atmospheric hierarchy.

## Checklist
- Near forms have more value separation and edge/detail clarity than equivalent far forms.
- Ground, shadows, and objects agree about which zones are near and far.
- The scene still reads structurally if the atmospheric grade is mentally removed.
- Distant forms are quieter without becoming unrelated flat cutouts or unintended high-contrast backlit cutouts that jump forward.

## Notes
Atmospheric effect belongs to the same spatial evidence system as convergence, diminution, foreshortening, light, shadow, and overlap. Its durable visual basis is the near-to-far loss of contrast and clarity, not a period-specific physical account of why the air produces it.

`VAR_dodson_shift_texture_mark_vocabulary_with_distance` adds a perceptual-scale rendering route: let foreground articulation collapse into grouped texture, broader pattern, and eventual omission as distance removes resolvable surface events instead of miniaturizing one mark indefinitely. `VAR_loomis_shift_receding_colors_toward_atmospheric_influence` adds the color counterpart: distant hues and chroma increasingly participate in the prevailing atmospheric influence rather than retaining foreground color separation unchanged.

`VAR_vilppu_use_atmospheric_contrast_as_local_depth_design` retains **Use Atmospheric Contrast as Local Depth Design** as a bounded emphasis route: deliberately use atmospheric contrast, edge, and detail reduction even across relatively small figurative depth when it clarifies overlap and spatial separation.

This owner extends a simple near-to-far contrast fade into a model of **illuminated intervening air**. Distance still matters, but so do atmospheric content and whether the air itself is in sun, shade, warm glare, or another light field. A distant form may simplify toward silhouette through atmosphere, but hard backlighting can turn that silhouette into a high-contrast cutout that appears to advance. Preserve enough atmospheric integration for the intended depth read.

`VAR_gurney_reverse_atmospheric_perspective_in_warm_near_sun_glare` Handles the uncommon case where low-sun light scattered through mist, dust, or moist air overwhelms the usual blue veil so distant forms grow warmer rather than cooler with recession.

`VAR_gurney_compress_depth_through_dense_fog_mist_smoke_or_dust` Accelerates contrast/chroma loss in dense suspended media and changes the lighting model when the medium becomes thick enough to diffuse or block direct sun; low mist with clear sun above remains a different condition.
