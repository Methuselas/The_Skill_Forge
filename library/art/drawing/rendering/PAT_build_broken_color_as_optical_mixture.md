---
object_id: PAT_build_broken_color_as_optical_mixture
object_type: pattern
name: Build Broken Color as Optical Mixture
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
- color
- broken_color
- optical_mixture
- mark_scale
cross_links:
- rel: related_to
  target_object_id: PAT_unify_palette_with_shared_color_influence
- rel: related_to
  target_object_id: PAT_match_rendering_complexity_to_reproduction_process
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_schmid_preserve_dry_medium_crispness_with_broken_color_before_overblending
  variant_name: Preserve Dry-Medium Crispness With Broken Color Before Overblending
  variant_basis: medium
  difference_from_foundation: Uses adjacent color notes and fewer blending interventions when repeated rubbing or smoothing would collapse a dry or particulate medium into generic smoothness, preserving a crisp granular surface while holding the large value/color family.
  when_to_use: Use with pastel or analogous dry media when broken adjacency can create the needed color integration without destroying the medium-specific surface.
  when_not_to_use: Do not preserve broken texture when the passage needs a truly smooth continuous transition or when the marks become noisy at the target scale.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_preserve_intra_stroke_color_variation_with_partial_wet_mixing
  variant_name: Preserve Intra-Stroke Color Variation With Partial Wet Mixing
  variant_basis: medium
  difference_from_foundation: Leaves controlled partial mixing within a wet stroke so closely related color striations and scintillation remain inside the mark instead of homogenizing every mixture before application.
  when_to_use: Use in larger paint-like passages where slight internal color variation adds life without breaking the parent value/color family.
  when_not_to_use: Do not use where precise drawing, tiny shapes, uniform local color, or clean graphic separation requires a fully controlled mixture.
  absorbed_from_object_id: none
references: []
---
# Build Broken Color as Optical Mixture

## Pattern Rule
**IF** a passage needs color vibration without losing its large value and color-family read
**THEN** place adjacent, visibly separate notes whose combined effect fuses at normal viewing distance, controlling their average value, hue family, chroma, and mark scale rather than premixing the passage into one uniform color
**ELSE** premix or simplify when the viewing scale cannot preserve useful separation between notes.

## Do
- Choose neighboring notes that differ enough to remain lively up close but still average into the intended mass from the target viewing distance.
- Preserve the passage's large value structure; optical mixture is not permission to let small bright notes destroy the value family.
- Vary note size and spacing with the final reproduction or display scale so the intended vibration survives instead of collapsing into noise.
- Compare the passage both close and reduced: close view should reveal distinct notes, while normal view should recover one coherent color mass.
- Use surrounding muted or related notes to keep the vibration subordinate to the picture's hierarchy.

## Don't
- Scatter unrelated hues randomly and call the result broken color.
- Let the technique fragment form boundaries or lighting logic that need to read as one mass.
- Miniaturize marks below the output's useful resolution and expect optical mixing to remain visible.

## Checklist
- The passage reads as one intended value/color family at normal viewing size.
- Separate notes remain perceptible at closer inspection without becoming accidental confetti.
- The effect survives the expected reproduction or display scale.

## Notes
Broken color is a controlled optical mixture: separate marks retain local vibration while the eye integrates them into a larger color statement. Its success depends as much on mark scale and aggregate value as on hue choice.

`VAR_schmid_preserve_dry_medium_crispness_with_broken_color_before_overblending` protects the granular/broken surface of dry media when smoothing would destroy useful color vibration. `VAR_schmid_preserve_intra_stroke_color_variation_with_partial_wet_mixing` applies the same optical principle inside a wet mark by leaving controlled pigment variation rather than homogenizing every stroke.
