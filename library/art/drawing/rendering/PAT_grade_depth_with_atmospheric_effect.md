---
object_id: PAT_grade_depth_with_atmospheric_effect
object_type: pattern
name: Grade Depth With Atmospheric Effect
library_path:
- art
- drawing
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
  source_id: robert_w_gill_basic_rendering
  source_title: 'Basic Rendering: Effective Drawing for Designers, Artists and Illustrators'
  author: Robert W. Gill
  publish_date: '1991'
  media_type: book
  locator: u00, printed pp. 25-31 (physical PDF pp. 28-34)
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_dodson_shift_texture_mark_vocabulary_with_distance
  variant_name: Shift Texture Mark Vocabulary With Distance
  variant_basis: method_sequence
  source_id: bert_dodson_keys_to_drawing
  source_title: Keys to Drawing
  locator: u06, physical pp. 169-170
  difference_from_foundation: "Adds Dodson's perceptual-scale route: as repeated surface detail recedes, change the kind of mark used to represent it rather than merely shrinking the foreground stroke. Move from individual articulation to grouped texture, broader pattern, and finally near-omission as distance removes resolvable events."
  when_to_use: Use when grass, foliage, crowds, windows, scales, fur, roof tiles, or other repeated detail extends through substantial depth and literal miniaturization would make the far field noisy or false.
  when_not_to_use: Do not change mark vocabulary so abruptly that equivalent surfaces stop belonging to the same material family, and do not use simplification to repair incorrect scale or perspective.
  absorbed_from_object_id: none
---

# Grade Depth With Atmospheric Effect

## Pattern Rule
**IF** a rendered scene must separate near from far beyond line perspective alone **THEN** reduce contrast, value separation, edge clarity, and fine detail as distance increases, applying the depth grade consistently to objects, ground, and cast shadows rather than fading only selected elements.

## Do
- Establish the strongest readable value separation in the foreground or nearest important zone, then progressively compress that separation with distance.
- Let distant darks move toward the surrounding middle values and distant lights lose some local brilliance so far forms become less contrasty than near ones.
- Apply the same near-to-far logic to ground planes, repeated structures, cast shadows, and background forms that occupy the same atmosphere.
- Use the effect as a depth layer after the perspective field and major lighting relationships are already coherent.
- Preserve important light-versus-shade relationships while reducing their contrast as they recede; atmosphere should soften a solved form, not erase its structure arbitrarily.

## Don't
- Fade distant objects while leaving their cast shadows or ground contacts equally black and crisp.
- Treat atmospheric depth as a background-only fog effect when middle-ground forms should also participate.
- Use contrast loss to repair wrong scale, convergence, overlap, or object placement.
- Import Gill's simplified particle explanation as a complete physical theory of atmospheric scattering; keep the card at the observable rendering level.

## Checklist
- Near forms have more value separation and edge/detail clarity than equivalent far forms.
- Ground, shadows, and objects agree about which zones are near and far.
- The scene still reads structurally if the atmospheric grade is mentally removed.
- Distant forms are quieter without becoming unrelated flat cutouts.

## Notes
Gill calls this “atmospheric effect” and repeatedly treats it as part of the same spatial evidence system as convergence, diminution, foreshortening, light, shadow, and overlap. The durable extraction is the near-to-far loss of contrast and clarity, not the book's period-specific account of why the air produces it.

`VAR_dodson_shift_texture_mark_vocabulary_with_distance` adds a perceptual-scale rendering route: let foreground articulation collapse into grouped texture, broader pattern, and eventual omission as distance removes resolvable surface events instead of miniaturizing one mark indefinitely.
