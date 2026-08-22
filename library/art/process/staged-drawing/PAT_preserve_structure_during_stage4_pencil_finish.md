---
object_id: PAT_preserve_structure_during_stage4_pencil_finish
object_type: pattern
name: Preserve Structure During Stage 4 Pencil Finish
library_path:
- art
- process
- staged-drawing
stage_binding: 4 final
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
- stage_4
- finished_pencils
- visual_continuity
- drift_control
- line_hierarchy
cross_links:
- rel: supports
  target_object_id: AP_finish_stage4_as_finished_pencils
- rel: supports
  target_object_id: AP_gate_staged_visual_work_by_approval
- rel: related_to
  target_object_id: PAT_preserve_articulated_limb_chain
- rel: related_to
  target_object_id: PAT_commit_stage3_form_realization
reference:
  source_title: Guided Broken Gate Canonical Drawing Precedent Run
  author: MaDin + GPT
confidence: high
references:
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage4_canonical_finished_pencils.png
  caption: 'Canonical Broken Gate Stage 4 finished pencils: the FIRST accepted Stage
    4 artifact closes the Drawing AP by cleaning, resolving, and integrating the Stage
    3 drawing in pencil. Minor accepted limitation: finish is slightly soft/uniformly
    busy.'
  derived_from: guided Broken Gate canonical Drawing precedent run, first accepted
    Stage 4
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/debug/broken_gate_debug_stage4_edit_target_near_regeneration_INVALID.png
  caption: 'INVALID / NON-CANONICAL Stage 4 debugging precedent: a local tightening
    request lacked reliable access to the exact accepted predecessor and produced
    a near-reconstruction with no material targeted improvement; it must not replace
    the first accepted Stage 4.'
  derived_from: guided Broken Gate Stage 4 edit-target failure review
  origin: first_party_source
  review: passed
variants: []
---
# Preserve Structure During Stage 4 Pencil Finish

## Pattern Rule
**IF** an approved Stage 3 drawing is being completed as Stage 4
**THEN** use the exact approved Stage 3 artifact as the immediate visual anchor, preserve every Stage 0–3 commitment, and add only finished-pencil information
**ELSE** return to the earliest unresolved drawing stage or fail closed when the exact predecessor cannot be accessed

## Do
- Carry `ROOT = approved Stage 0` and `IMMEDIATE = approved Stage 3`; Stage 4 owns finish, not a new composition or design solution.
- Treat canonical identity and tool accessibility as separate checks. If a registered-successor edit requires the predecessor and the exact accepted image is not exposed to the native image tool, stop and recover/re-upload that exact artifact. A re-upload restores access to the same canonical predecessor and inherited lockset; it does not create a new composition or require new approval.
- Finish in pencil: clean construction residue, resolve contours, organize line hierarchy, clarify already-established anatomy/clothing/gear, resolve hands/feet/prop contacts, refine folds/overlaps, clean architecture/props, and use controlled graphite hatching/value to clarify form and depth.
- Protect focal hierarchy. Give the lead subject and functional contacts the tightest pencil resolution; suppress line noise and tertiary chatter in subordinate/distant regions.
- Inspect articulated chains after finishing: parent mass → joint → member → endpoint. Check hands, feet, head/neck, prop contacts, weapons, wings, tails, and any other functional endpoints relevant to the drawing.
- Compare the finished pencils against both anchors at reduced scale. Distinguish global drift from local pencil defects; global drift returns upstream, while a local Stage 4 defect may be revised only when the exact canonical Stage 4 predecessor is accessible.

## Don't
- Do not enlarge/reposition subjects, change camera/crop, alter major negative spaces, modify perspective/path geometry, or add major inventory for a more dramatic drawing.
- Do not use line finish, clothing, darkness, rubble, or texture to hide an impossible structural chain.
- Do not introduce color, paint, final material rendering, atmospheric color, ink, manga tones, or another medium's finish.
- Do not regenerate from the original prose when an accepted visual predecessor exists.
- Do not substitute a rejected artifact or a visually similar reconstruction when exact-source access is unavailable.
- Do not claim edit lineage or parentage the host did not actually expose.

## Checklist
- Exact approved Stage 3 predecessor identified.
- Exact predecessor is actually available to the native image tool when the requested operation requires edit/reference continuity.
- The finished drawing still reads as the same approved picture before local detail is examined.
- Camera, crop, subject scale/placement, major negative spaces, inventory, path geometry, overlaps, contacts, and hierarchy remain consistent.
- Functional articulated chains remain plausible and attached.
- Pencil hierarchy is deliberate: focal contours resolve tightly; secondary regions are quieter.
- No downstream medium appears.
- No tool-level lineage claim exceeds what the host exposes.

## Notes
Stage 4 is the terminal drawing operation: **Finished Pencils**. It is not the terminal operation of Art as a whole. Ink, Color, Paint, Manga/B&W finish, and other medium-specific workflows inherit the completed Drawing lockset later.

The Broken Gate tightening failure establishes a hard rule: **loss of edit-target access does not authorize visual reinterpretation.**
