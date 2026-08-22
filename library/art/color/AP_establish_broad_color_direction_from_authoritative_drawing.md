---
object_id: AP_establish_broad_color_direction_from_authoritative_drawing
object_type: ap
name: Establish Broad Color Direction From an Authoritative Drawing
library_path:
- art
- color
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- color
- registered_successor
- color_direction
- palette
- gamut
- illumination
- value_structure
- color_rough
cross_links:
- rel: related_to
  target_object_id: PAT_develop_scene_through_registered_successors
- rel: supports
  target_object_id: PAT_choose_color_strategy_to_fit_subject_purpose_and_viewing_context
- rel: supports
  target_object_id: PAT_preserve_value_structure_when_translating_tone_into_color
- rel: supports
  target_object_id: PAT_define_and_enforce_picture_gamut
- rel: supports
  target_object_id: PAT_unify_palette_with_shared_color_influence
- rel: supports
  target_object_id: PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum
- rel: related_to
  target_object_id: DRILL_audition_one_subject_across_small_color_roughs
- rel: related_to
  target_object_id: AP_develop_approved_drawing_into_coherent_color_image
reference:
  source_title: PASS Art visible Color ratification synthesis
  author: MaDin + GPT
confidence: high
references: []
variants: []
---

# Establish Broad Color Direction From an Authoritative Drawing

## Objective
Turn an exact authoritative Drawing into a deliberately broad Color-direction artifact whose picture-level palette, gamut, light/value organization, dominant Color families, warm/cool structure, and major chroma hierarchy are clear enough to approve before detailed Color development, while preserving the inherited Drawing lockset and withholding downstream material and surface finish.

## Steps / Flow
1. **Pass the authoritative-Drawing gate.** Begin from an approved PASS Drawing or an exact user-supplied drawing explicitly designated as the visual authority. Register it with `PAT_develop_scene_through_registered_successors`. Freeze camera, crop, composition, pose, perspective, placement, major proportions and design/form, scene inventory, important overlaps/contacts, and other ratified Drawing decisions. If the requested native operation requires edit/reference continuity, confirm that this exact Drawing is actually accessible; otherwise fail closed rather than regenerate a near-match.
2. **Separate locked appearance constraints from open Color decisions.** Preserve any already-authoritative lighting intent, tonal hierarchy, required local colors, story/brand palette, narrative Color constraints, or other ratified appearance decisions. Do not reopen them merely because Color development has begun. If the desired Color direction requires structural redesign, return to the Drawing owner.
3. **Decide whether Color Search is genuinely open.** If the user has already specified or approved the Color direction, skip auditioning and build one broad Color-direction artifact. If several materially different Color strategies remain open, use the comparison logic of `DRILL_audition_one_subject_across_small_color_roughs`: generate roughly four to six cheap whole-picture alternatives while keeping Drawing, crop, scene inventory, and normally the major value organization fixed.
4. **Keep Color Search about Color, not composition.** Candidate roughs may vary picture-level hue families, temperature organization, palette/gamut, Color key, dominant/subordinate relationships, and broad chroma placement. They may not move the camera, recompose the image, redesign poses or silhouettes, replace scene inventory, or use structural change to make one palette appear stronger.
5. **Resolve or inherit illumination before detailed Color.** Use `PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum` when illumination remains open; otherwise preserve the accepted lighting intent. The broad Color artifact must already make the dominant light environment believable enough that later local Color can be developed causally rather than patched object by object.
6. **Protect the large value read.** Apply `PAT_preserve_value_structure_when_translating_tone_into_color`. Hue and chroma may enrich the picture, but they must not collapse the accepted large light, middle, and dark families. If the Color rough only works when the major value structure is lost, it has failed this operation.
7. **Establish picture-level strategy, gamut, and unity.** Coordinate `PAT_choose_color_strategy_to_fit_subject_purpose_and_viewing_context`, `PAT_define_and_enforce_picture_gamut`, and `PAT_unify_palette_with_shared_color_influence`. The image should already read as one Color environment or designed scheme at reduced size rather than as separately attractive local objects.
8. **Set broad chroma and temperature hierarchy without finishing it.** Establish where Color is strongest or quietest, how warm/cool families organize the picture, and which Color masses dominate or recede. Leave local reflected Color, material-specific optical nuance, atmospheric microvariation, edge polish, texture, and small accents for the successor unless one is essential to communicate the broad decision.
9. **Pass the approval-boundary check.** A valid Color-direction artifact preserves the Drawing; keeps accepted appearance constraints; reads coherently at reduced size; has an intentional palette/gamut; preserves the large value structure; communicates a stable illumination/color environment; and makes the major Color hierarchy understandable without detailed rendering. When Search was used, one actual visible candidate must be selected/approved before successor work.
10. **Stop at broad direction.** Do not continue automatically into local Color development or medium-specific finish. Surface the current broad Color artifact for approval/revision/rejection. Its purpose is to make the expensive downstream Color solution safe to build, not to look maximally finished.

### Productive Image Contract
- **Artifact form:** one broad whole-picture Color-direction treatment of the exact authoritative Drawing; when Search is genuinely open, approximately four to six cheap whole-picture Color alternatives may be surfaced for selection.
- **Preserve:** exact Drawing camera, crop, composition, pose, perspective, placement, proportions, major form/design, scene inventory, important overlaps/contacts, approved leading/path geometry, and already-ratified lighting/value/local-color/story constraints.
- **Establish:** picture-level Color strategy, broad palette/gamut, dominant/subordinate Color families, broad warm/cool organization, major Color masses, large value preservation, stable illumination intent, and major chroma hierarchy.
- **Withhold:** detailed material rendering, texture, micro-reflection, tiny local Color variation, small atmospheric effects, micro-edge treatment, incidental accents, and polish not needed to judge the whole-picture direction.
- **Forbidden:** recomposition, camera/crop redesign, pose redesign, perspective rewrite, major silhouette/design replacement, scene-inventory replacement, or structural repair disguised as Color exploration.
- **Stop:** when the broad Color solution can be approved on whole-picture relationships without relying on downstream finish.

## Notes
This is the first productive operation of the approval-gated Color thread, but `stage_binding: 0 design` is generic PASS refinement metadata, not a declaration of Color Stage 0. The operation is intentionally broad because the user should approve costly-to-replace picture-level Color commitments before local appearance detail accumulates.

When a contact sheet is the only host-supported way to show Color alternatives, selection may establish canonical Color identity but does not by itself prove that the chosen panel is independently accessible for native successor editing. Prefer separate images; otherwise use exact deterministic extraction/re-upload when available. Never regenerate an approximate isolated copy merely to manufacture a predecessor.
