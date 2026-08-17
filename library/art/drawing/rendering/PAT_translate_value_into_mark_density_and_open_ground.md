---
object_id: PAT_translate_value_into_mark_density_and_open_ground
object_type: pattern
name: Translate Value Into Mark Density and Open Ground
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
- line
- value
- hatching
- mark_density
- negative_space
- tonal_design
cross_links:
- rel: related_to
  target_object_id: PAT_consolidate_resolved_form_with_tone
- rel: related_to
  target_object_id: PAT_control_edge_hardness_from_form_light_and_focus
reference:
  source_title: Creative Illustration
  author: Andrew Loomis
confidence: high
references: []
variants:
- variant_id: VAR_guptill_outline_then_add_selective_tone_for_economy
  variant_name: Outline, Then Add Selective Tone for Economy
  variant_basis: method_sequence
  difference_from_foundation: 'Uses a line-first hybrid economy: establish form and selected material evidence with line,
    preserve open ground as much of the light family, then add only the gray and black tone needed to organize the darker
    value structure.'
  when_to_use: Use when a sketch should retain linear clarity and speed while gaining enough tonal structure to read form,
    material, and hierarchy.
  when_not_to_use: Do not use sparse selective tone when the task requires continuous modeling, subtle atmosphere, or full
    documentary value description.
  absorbed_from_object_id: none
---
# Translate Value Into Mark Density and Open Ground

## Pattern Rule
**IF** a line-led rendering needs tonal hierarchy without continuous-tone fill
**THEN** translate each intended value into a controlled relationship between marks and exposed ground, calibrating spacing, weight, density, and crossings before committing to the final passage while keeping mark direction subordinate to form and material
**ELSE** use a continuous-tone or mass-based method when discrete marks would fight the intended finish.

## Do
- Decide the large light/halftone/shadow or black/gray/white organization before worrying about attractive stroke handling.
- Make a small value ladder or test patch when the tool/support combination is unfamiliar, so you know how much exposed ground produces each practical value.
- Darken primarily by changing the ratio of mark to open ground: closer spacing, heavier marks, additional crossings, or broader mark families can lower the apparent value.
- Preserve untouched or lightly marked ground deliberately in lighter passages instead of filling everything and trying to recover light later.
- Let stroke direction reinforce turning planes, surface flow, or the material logic already solved by the drawing.
- Recheck the passage at reduced size. The intended value should survive after individual marks stop reading as separate strokes.
- Vary stroke length and direction enough to prevent conspicuous white gaps or mechanical striping while preserving the intended aggregate value, form direction, and material read.
- When repeated physical detail falls below the drawing's useful resolution, reduce the number of rendered repetitions and preserve the aggregate value, directional rhythm, and material identity instead of miniaturizing every event.

## Don't
- Do not pile on random hatching until a passage happens to look dark enough.
- Do not let decorative stroke rhythm override the required value grouping.
- Do not assume one numeric spacing recipe transfers between pens, pencils, brushes, papers, screens, or digital brushes; recalibrate when mark behavior changes.
- Do not use dense mark texture to conceal unresolved construction or lighting.
- Do not confuse this Pattern with a requirement to hatch every shadow; solid masses, washes, or continuous tone may be better for a given finish.
- Do not let many short broken strokes create a spotty field of accidental white holes, or let equal-length equal-direction strokes turn a tonal passage into mechanical texture.
- Do not draw every shingle, slate, brick, or other repeated unit when literal repetition would make a small or foreshortened passage too dark, busy, or spotty.

## Checklist
- The target value structure is decided before local mark decoration.
- Darker passages contain a controlled increase in mark-to-ground ratio rather than arbitrary clutter.
- Lighter passages preserve enough open ground to remain visibly distinct.
- Mark direction supports the depicted form or material.
- A small-scale check preserves the intended light/dark grouping.
- The method has been recalibrated when the tool or support materially changes the mark behavior.
- Repeated detail is sampled at a frequency the image scale can support, and the simplified pattern still preserves the intended value and material read.

## Notes
Loomis describes pen value as the amount of light paper showing through a network of dark lines and recommends making a scale of pen values for reference. The adjacent procedure pages reinforce planning the black/gray/white mass arrangement and important passages before final execution. PASS abstracts that medium-specific demonstration into a general line-rendering capability: value is controlled through the designed ratio of marks to exposed ground, while the exact behavior of pen, brush, paper, scratchboard, Craftint, and other physical media remains deferred to the future Materials / Media curriculum.

`VAR_guptill_outline_then_add_selective_tone_for_economy` keeps a line-led sketch open by preserving light ground and adding only the decisive darker tone needed for form and hierarchy.

At small representation scales, physical repetition count and rendered mark count should diverge. A roof may contain many more courses than the drawing can carry cleanly; sampling fewer repetitions can preserve the same broad darkness and surface rhythm more truthfully than literal micro-detail that collapses into noise.
