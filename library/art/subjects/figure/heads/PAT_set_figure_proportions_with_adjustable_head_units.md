---
object_id: PAT_set_figure_proportions_with_adjustable_head_units
object_type: pattern
name: Set Figure Proportions With Adjustable Head Units
library_path:
- art
- subjects
- figure
- heads
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- figure_drawing
- proportion
- design
- measurement
cross_links:
- rel: related_to
  target_object_id: PAT_choose_stage1_construction_by_readability
reference:
  source_title: Figure Drawing for All It's Worth
  author: Andrew Loomis
confidence: high
references: []
variants:
- variant_id: VAR_bammes_build_age_and_body_type_from_proportional_ensemble
  variant_name: Build Age and Body Type From a Proportional Ensemble
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Bammes''s anti-schema body-type rule to adjustable head-unit proportion: do not encode
    female, child, adolescent, or young-adult form with one isolated symbol or a single canon. Coordinate head scale, torso-to-leg
    relation, shoulder/hip widths, limb proportions, joint prominence, muscle development, and soft-tissue distribution so
    the whole body carries the intended type.'
  when_to_use: Use when designing or observing figures whose age, developmental stage, sex-linked body structure, or individual
    build must read from the body before costume or facial detail.
  when_not_to_use: Do not treat Bammes's measured averages as diagnostic truths about a real person or force one developmental
    timetable onto every individual; use them as drawing references and compare against the actual model or design.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_check_head_age_against_body_context
  variant_name: Check Head Age Against the Body Context
  variant_basis: context
  difference_from_foundation: 'Adds Loomis''s crop-context warning to age proportion: a school-age or early-adolescent head
    can look more mature in a head-and-shoulders view because the head approaches adult size before the rest of the body does.
    When the age read matters in a figure, compare the head against the body''s still-developing scale and proportions instead
    of judging maturity from the isolated face alone.'
  when_to_use: Use when a cropped reference, portrait study, or nearly adult-looking child head is making the developmental
    stage ambiguous and a full-body reference or designed body is available for comparison.
  when_not_to_use: Do not infer a precise biological age from head-to-body proportion or override the actual individual. In
    a true head-only portrait, preserve the observed head and treat the missing body context as uncertainty rather than inventing
    it.
  absorbed_from_object_id: none
- variant_id: VAR_hda_u04_use_eight_three_quarter_head_heroic_scaffold
  variant_name: Use an Eight-and-Three-Quarter-Head Heroic Scaffold
  variant_basis: context
  difference_from_foundation: 'Adds Hogarth''s internally linked eight-and-three-quarter-head alternative as one deliberately
    elongated heroic/athletic design scaffold. Keep its own landmark system coherent—roughly three heads from shoulder line
    to pubic arch in front, three and one-half to the buttock base in back, two and three-quarter heads from collarbone attachment
    to wrist plus a three-quarter-head hand, and four heads from greater trochanter to high inner ankle—rather than mixing
    isolated ratios from unrelated canons. PASS bounds the source''s dated claim of a universal contemporary ideal: this is
    a design option, not average anatomy.'
  when_to_use: Use when designing a deliberately long-limbed heroic or athletic figure, or when studying Hogarth's proportion
    system as one coherent alternative before adapting it to a specific character.
  when_not_to_use: Do not treat eight and three-quarter heads, the source's cross-body alignments, or its twentieth-century
    ideal language as a biological norm, demographic truth, or substitute for measuring an observed individual. Choose another
    scaffold or follow the reference when the intended body differs.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_exaggerate_head_body_ratio_for_comic_character
  variant_name: Exaggerate Head-to-Body Ratio for Comic Character Design
  variant_basis: context
  difference_from_foundation: Adds a comic-character context in which head-to-body ratio is deliberately pushed far outside
    realistic figure canons while the torso, joints, limb reach, and action remain internally coherent. The ratio is treated
    as a design variable for character variety, not as anatomy.
  when_to_use: Use when designing humorous, chibi-like, caricatured, or otherwise stylized figures whose personality depends
    partly on the relative scale of head and body.
  when_not_to_use: Do not apply the exaggerated ratio as a biological average or let the large/small head excuse broken balance,
    attachment, reach, or pose mechanics.
  absorbed_from_object_id: none
---

# Set Figure Proportions With Adjustable Head Units

## Pattern Rule
**IF** a figure needs a repeatable proportional design **THEN** choose a head-unit standard appropriate to the intended figure, establish the major vertical relationships from that shared unit, and preserve those relationships as the pose is constructed in perspective.

## Do
- Treat the head as a convenient relational unit, not a biological constant.
- Choose the proportional standard deliberately for the intended character/design.
- Carry the scaffold into the mannikin and perspective construction.

## Don't
- Do not canonize one ideal height for every body.
- Do not let measurement flatten gesture or override purposeful variation.

## Checklist
- The result shows the intended structural or functional change without contradicting the surrounding construction.

## Notes
Treat head-unit canons as adjustable scaffolds for checking large figure relationships, not as biological averages or fixed ideals.

`VAR_bammes_build_age_and_body_type_from_proportional_ensemble` retains **Build Age and Body Type From a Proportional Ensemble** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_loomis_check_head_age_against_body_context` retains **Check Head Age Against the Body Context** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_hda_u04_use_eight_three_quarter_head_heroic_scaffold` retains **Use an Eight-and-Three-Quarter-Head Heroic Scaffold** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_loomis_exaggerate_head_body_ratio_for_comic_character` bounds Loomis's extreme head/body shifts to stylized character design. Push the ratio deliberately for variety while preserving the articulated body's internal relationships; do not reinterpret the exaggeration as human proportion doctrine.
