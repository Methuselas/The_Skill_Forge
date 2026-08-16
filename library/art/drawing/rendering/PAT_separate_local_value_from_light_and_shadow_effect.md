---
object_id: PAT_separate_local_value_from_light_and_shadow_effect
object_type: pattern
name: Separate Local Value From Light and Shadow Effect
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
- local_value
- illumination
- light_shadow
- value
cross_links:
- rel: related_to
  target_object_id: PAT_consolidate_resolved_form_with_tone
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants:
- variant_id: VAR_loomis_compress_observed_values_into_pencil_safe_four_band_range
  variant_name: Compress Observed Values Into a Pencil-Safe Four-Band Range
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Loomis''s medium-aware pencil compression: when the observed dynamic range is broader
    than pencil can comfortably reproduce, preserve the ordering of local values and illumination while mapping the subject
    into a small controlled set of value families - paper white for extreme lights, very delicate gray for modeled light,
    middle gray for halftone, and dark gray/black for shadow and the deepest accents.'
  when_to_use: Use when a pencil rendering is becoming muddy because too many closely spaced observed grays are being copied
    literally, or when a broad value structure must stay readable despite the medium's practical range.
  when_not_to_use: Do not treat four bands as a universal tonal law or force subtle subjects into four equal steps. Use more
    or fewer groups when the medium, subject, or intended finish needs them, and preserve local-value ordering so intrinsically
    dark materials do not become falsely light merely because they are illuminated.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_shift_neighbor_local_values_as_relational_group
  variant_name: Shift Neighboring Local Values as a Relational Group
  variant_basis: method_sequence
  difference_from_foundation: Loomis makes the local-value comparison operational by holding the approximate difference between
    neighboring materials while a shared illumination change raises or lowers the group. PASS preserves this as a relational
    check rather than Loomis's absolute claim that the difference remains constant under every possible light.
  when_to_use: Use when two neighboring materials are drifting independently during a lighting change and their established
    local-value ordering or separation needs to remain legible as one illumination family moves lighter or darker.
  when_not_to_use: Do not lock the numerical difference mechanically when different materials, colored illumination, specularity,
    translucency, exposure, or other optical effects legitimately change the apparent separation. Preserve the relationship
    only as far as the observed or designed light supports it.
  absorbed_from_object_id: none
- variant_id: VAR_vandijk_compress_exposure_without_collapsing_material_light_states
  variant_name: Compress Exposure Without Collapsing Material-by-Light States
  variant_basis: constraint
  difference_from_foundation: Allows the value range to be compressed away from literal camera-like exposure when necessary
    to keep important combinations of material and illumination readable as distinct states.
  when_to_use: Use when extreme brightness or darkness would merge materially important states such as lit snow, shadowed
    snow, lit rock, and shadowed rock into an unreadable value collapse.
  when_not_to_use: Do not flatten the lighting arbitrarily; preserve the relational logic of light, material, and distance
    while remapping the range only as much as readability requires.
  absorbed_from_object_id: none
---

# Separate Local Value From Light and Shadow Effect

## Pattern Rule
**IF** the visible value of a surface is being judged from what the object is known to be rather than from the current illumination
**THEN** distinguish the surface's local value from the light/shadow effect acting on it, then judge the final visible value as the interaction of both
**ELSE** keep the simpler value grouping when local-value differences are negligible for the task

## Do
- Compare neighboring materials under the same light before assuming their lights or shadows should match.
- Let a dark local-value object remain part of a darker family even when illuminated, and let a light local-value object become substantially darker when turned away from strong light.
- Use direct observation to override symbolic labels such as “white snow,” “light skin,” or “black hair” when the actual value relationships differ.
- Recheck the whole value range after changing the lighting because illumination can cause previously separate local-value shapes to merge or separate.

## Don't
- Assign a fixed tone from the object's name or remembered color.
- Confuse a surface being intrinsically dark with that surface being in shadow.
- Lighten every nominally white object until it breaks the observed or designed value pattern.

## Checklist
- You can state which major value differences come from material/local value and which come from illumination.
- Nominally light materials can become dark when the light requires it.
- The visible value pattern reads coherently without relying on object-name assumptions.

## Notes
Dodson's snow, skin, hair, and mixed-material examples make local value and illumination separate inputs to one observed value pattern. The practical purpose is not terminology for its own sake; it prevents “known color” from overruling what the light actually makes visible. `VAR_loomis_compress_observed_values_into_pencil_safe_four_band_range` adds a pencil-specific compression pass: reduce an overbroad observed range to a few controlled value families while preserving the material/light hierarchy, treating Loomis's four bands as a practical simplification rather than a fixed tonal law. `VAR_loomis_shift_neighbor_local_values_as_relational_group` adds a bounded relational check: under a shared illumination change, move neighboring local values together enough to preserve their established ordering and approximate separation, but release that constraint when material or optical behavior genuinely changes the relationship.

`VAR_vandijk_compress_exposure_without_collapsing_material_light_states` permits bounded exposure compression when literal brightness would collapse important material-by-light distinctions. Keep the relationships believable, including distance effects, while preserving the separations the scene needs to read.
