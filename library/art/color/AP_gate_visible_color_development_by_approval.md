---
object_id: AP_gate_visible_color_development_by_approval
object_type: ap
name: Gate Visible Color Development by Approval
library_path:
- art
- color
stage_binding: 0 design
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: AP_progress_artifact_through_ratified_steps
tags:
- color
- approval_gate
- ratification
- registered_successor
- continuity
- rollback
cross_links:
- rel: related_to
  target_object_id: AP_progress_artifact_through_ratified_steps
- rel: related_to
  target_object_id: AP_establish_broad_color_direction_from_authoritative_drawing
- rel: related_to
  target_object_id: AP_develop_approved_color_direction_to_color_completion
- rel: related_to
  target_object_id: AP_develop_approved_drawing_into_coherent_color_image
- rel: related_to
  target_object_id: DRILL_audition_one_subject_across_small_color_roughs
- rel: related_to
  target_object_id: PAT_develop_scene_through_registered_successors
- rel: related_to
  target_object_id: AP_prepare_artifact_only_image_generation_handoff
reference:
  source_title: PASS Art visible Color ratification synthesis
  author: MaDin + GPT
confidence: high
references: []
variants: []
---

# Gate Visible Color Development by Approval

## Objective
Run explicit approval-gated Color production as the Color-domain adapter for `AP_progress_artifact_through_ratified_steps`, allowing exactly two mandatory visible Color operations—Broad Color Direction, then Color Development / Completion—while preserving the exact authoritative Drawing, registering each approved Color predecessor, and preventing rejection, revision, or terminal approval from silently advancing into another operation or medium.

## Steps / Flow
1. **Enter only for an explicit approval-gated Color request.** Use this AP when the user asks to develop Color visibly through approvals from an authoritative Drawing or explicitly requests staged/stepwise Color. Ordinary direct Color remains owned by `AP_develop_approved_drawing_into_coherent_color_image`; do not make every Color request staged merely because this adapter exists.
2. **Delegate universal ratification mechanics upward.** `AP_progress_artifact_through_ratified_steps` remains authoritative for explicit approval, rejection, same-operation revision, Search/Control, inherited locksets, rollback, exactly-one advancement, and terminal closure. This AP supplies only the Color-owned thread and Color-specific legality; do not duplicate a second generic staged controller inside Color.
3. **Use the Color thread exactly as authored.** The ordered productive operations are: `AP_establish_broad_color_direction_from_authoritative_drawing` → `AP_develop_approved_color_direction_to_color_completion`. These are named Color operations, not Color Stage 0–4 and not an extension of Drawing's numbered thread.
4. **Resolve the authoritative Drawing before the first Color artifact.** Accept an approved PASS Drawing or an exact user-supplied drawing explicitly designated as authoritative. Freeze its Drawing lockset. If the native Color operation depends on edit/reference continuity, confirm that the exact canonical Drawing is actually accessible to the image tool; canonical identity without native accessibility is insufficient.
5. **Make Broad Color Direction the only legal first Color operation.** With no approved Color-direction artifact, only `AP_establish_broad_color_direction_from_authoritative_drawing` may produce a visible Color artifact. If several Color strategies genuinely remain open, that AP may use the Search reasoning of `DRILL_audition_one_subject_across_small_color_roughs`; the Search remains inside this operation and must collapse to one approved canonical Color-direction artifact before development begins.
6. **Require user-originated approval to ratify Color direction.** Assistant ranking, recommendation, praise, silence, or a request for improvement never approves the current Color artifact. Local revisions remain in Broad Color Direction. Broad rejection reopens Search inside Broad Color Direction with the critique preserved. A selected/approved candidate becomes the sole canonical Color-direction predecessor; rejected and unselected candidates lose productive authority unless the user explicitly resurrects them.
7. **Interpret contextual continuation as exactly one Color transition.** At the Broad Color Direction gate, `Continue`, `Next`, or `Commit and Continue` means approve the actual current Color-direction artifact, freeze the Color decisions owned there, and authorize exactly one successor: `AP_develop_approved_color_direction_to_color_completion`. It does not authorize multiple images, a fresh recoloring from the Drawing, or automatic Paint/Ink/Manga execution.
8. **Require the exact approved Color artifact for the second operation.** Apply `PAT_develop_scene_through_registered_successors`. Once Broad Color Direction is approved, the required productive predecessor is that exact approved Color artifact, not the original Drawing and not prose describing the palette. When exact edit/reference continuity is required but the artifact is unavailable, fail closed and recover/request the exact artifact. A re-upload restores the same canonical predecessor and lockset without new approval.
9. **Carry two inherited locksets into Color Development.** Preserve the Drawing lockset and the approved broad-Color lockset. The second operation may increase resolution, causal variation, material response, atmosphere, chroma nuance, and hierarchy within those commitments; it may not silently replace the approved picture structure or global Color direction.
10. **Route failures to the productive owner.** Structural/camera/composition/pose/perspective/major-design failure rolls back to Drawing. Wrong global palette, major Color strategy, major warm/cool organization, major Color/value relationship, dominant Color family, or broad chroma hierarchy rolls back to Broad Color Direction. Local Color, reflected Color, material appearance, atmosphere, chroma refinement, edge hierarchy, and focal integration remain in Color Development / Completion while consuming Rendering knowledge as needed.
11. **Use the artifact-only native handoff for every productive Color call.** Immediately before native image generation, use `AP_prepare_artifact_only_image_generation_handoff`. Keep approval logic, operation names, Search/Control, rollback, and future-step vocabulary on the PASS side. The image tool should receive only the currently legal Color artifact contract, inherited visual authorities, permitted changes, withheld information, and stop condition.
12. **Stop at the terminal Color gate.** When `AP_develop_approved_color_direction_to_color_completion` passes its completion check, legal outcomes are final Color approval, same-operation Color-development revision, rollback to Broad Color Direction when its commitments must change, or an explicit user request for another downstream medium. A bare terminal `Continue` does not invent Painting, Ink, Manga/B&W, watercolor, or any other successor. The Color thread closes.

## Notes
This AP is a domain adapter, not a universal controller and not a claim of hidden runtime state. The generic metaskill owns how ratification works; Color owns what the Color thread is. The number of visible operations belongs to the domain rather than to Drawing's historical 0–4 sequence.

The compact Color chain is **authoritative Drawing → Broad Color Direction → Color Development / Completion**. Every arrow that depends on native edit/reference continuity requires both known canonical identity and actual access to the exact predecessor. Loss of access never authorizes visual reinterpretation.
