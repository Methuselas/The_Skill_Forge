---
object_id: PAT_build_loose_surface_from_precise_visual_decisions
object_type: pattern
name: Build a Loose Surface From Precise Visual Decisions
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
- looseness
- precision
- mark_making
- brushwork
- decision_control
cross_links:
- rel: related_to
  target_object_id: PAT_control_edge_hardness_from_form_light_and_focus
- rel: related_to
  target_object_id: PAT_select_observed_evidence_to_serve_expressive_intent
reference:
  source_title: 'Alla Prima: Everything I Know About Painting'
  author: Richard Schmid
confidence: high
references: []
variants:
- variant_id: VAR_schmid_accumulate_direct_painting_from_resolved_patch_to_resolved_patch
  variant_name: Accumulate Direct Painting From Resolved Patch to Resolved Patch
  variant_basis: method_sequence
  difference_from_foundation: After minimal placement, establish one trustworthy visual patch and compare the next patch against what is already resolved, building outward through verified relationships instead of scattering speculative marks across the image.
  when_to_use: Use in direct or finish-as-you-go rendering when each retained passage should be credible enough that the work could stop early without the resolved region reading only as unfinished block-in.
  when_not_to_use: Do not force local finish when the task still requires broad searching, major compositional relocation, or a deliberately global block-in before any passage is resolved.
  absorbed_from_object_id: none
---
# Build a Loose Surface From Precise Visual Decisions

## Pattern Rule
**IF** the intended finish should look free, economical, spontaneous, or boldly handled
**THEN** make each surviving mark answer a deliberate visual job while keeping the number of marks and corrections low; let looseness describe the surface character, not the quality of the decisions
**ELSE** use a more explicit or tightly controlled surface when the assignment requires sustained detail, technical description, or a different finish language.

## Do
- Before retaining an important mark, check its place, shape and size, color, value, and edge character against the current image logic.
- Prefer one sure mark that carries several jobs over a cluster of hesitant corrections that merely approximates the same passage.
- Keep checking new marks against already trusted relationships so local freedom accumulates on a stable visual structure.
- Let broad, broken, dry, fluid, or otherwise conspicuous handling follow form, light, material, and emphasis instead of becoming uniform decorative noise.
- Stop developing a passage once added handling no longer improves the intended statement.

## Don't
- Do not equate speed, randomness, or visible brush texture with looseness.
- Do not leave avoidable placement, value, color, or edge errors merely because the surface is meant to look spontaneous.
- Do not polish every passage to the same degree; selective completion can carry more authority than equal finish everywhere.

## Checklist
- Important marks have a clear placement, shape/size, color, value, and edge job.
- The surface feels economical without depending on obvious errors or uncontrolled daubing.
- Painterly or gestural marks reinforce form, material, light, or hierarchy rather than functioning as a generic style filter.
- The image could stop at its present level of completion without the resolved passages needing explanation to read as intentional.

## Notes
Loose appearance and precise control are complementary. A surface can remain broad, broken, or visibly handled while the underlying decisions stay exact enough to support the picture. The practical test is not whether the hand or renderer moved quickly, but whether the retained marks are purposeful and relationally correct.

`VAR_schmid_accumulate_direct_painting_from_resolved_patch_to_resolved_patch` specializes this into a direct-painting sequence: resolve one useful patch, use it as a trusted comparison anchor, and extend the picture through connected accurate relationships rather than through scattered trial marks.
