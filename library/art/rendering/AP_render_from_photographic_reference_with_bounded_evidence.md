---
object_id: AP_render_from_photographic_reference_with_bounded_evidence
object_type: ap
name: Render From Photographic Reference With Bounded Evidence
library_path:
- art
- rendering
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- photographic_reference
- reference_authority
- camera_artifacts
- evidence
- synthesis
cross_links:
- rel: supports
  target_object_id: PAT_synthesize_visual_concepts_from_diverse_source_types
- rel: supports
  target_object_id: PAT_choose_rendering_technique_from_visual_intent_subject_and_constraints
- rel: related_to
  target_object_id: AP_diagnose_and_recover_failing_observed_rendering
reference:
  source_title: 'Alla Prima II: Everything I Know About Painting—and More'
  author: Richard Schmid
confidence: high
references: []
variants: []
---

# Render From Photographic Reference With Bounded Evidence

## Objective
Use photographic reference as channel-specific evidence for a designed rendering without inheriting unsupported camera artifacts, false precision, or a single photograph's accidental composition and hierarchy.

## Steps / Flow
1. **Choose the legal entry contract before granting the photograph authority.** If no approved Drawing predecessor exists, use **root entry** and decide composition, mood, degree of literal fidelity, and the result the image must communicate. If an approved Drawing predecessor exists, use **registered-successor entry**: inherit its camera, crop, composition, perspective, placement, major form/design, scene inventory, and important overlap/contact decisions as locked. The photograph may then inform legal appearance decisions, but it may not silently replace the accepted Drawing. An explicitly owning root/alternate workflow may begin without manufacturing Finished Pencils first.
2. **Audit the photograph by information channel.** Judge drawing, perspective, transient action, local detail, value extremes, hue/chroma/temperature, edge hierarchy, atmosphere, and emphasis separately rather than classifying the whole image as simply reliable or unreliable.
3. **Mark likely reference-loss zones.** Look for clipped highlights, crushed darks, uniform sharpness, flattened atmosphere, camera distortion, frozen microdetail, and other places where the camera may have discarded or exaggerated useful information.
4. **Assign supplementary evidence by job.** Use `PAT_synthesize_visual_concepts_from_diverse_source_types` to give additional views, life/color studies, factual structure, alternate exposures, or other accepted evidence specific authority instead of averaging all references indiscriminately.
5. **Use photographic restructuring only where the entry contract permits it.** In root entry, crop, simplify, reorganize, and selectively depart from the photograph when the active pictorial target permits it. In registered-successor entry, preserve the approved Drawing's camera/crop/composition/structure; simplify or reinterpret photographic evidence only within that inherited picture. If the accepted Drawing itself must change, roll back to the owning Drawing AP.
6. **Normalize multiple references before integration.** Reconcile camera, light, scale, and viewpoint differences before combining information that must coexist in one scene.
7. **Choose the handling mode deliberately.** When seeking a live/direct look from static reference, use the accepted live-equivalent constraint variant so unlimited access does not automatically produce uniform detail and overfinish.
8. **Render with channel-specific trust.** Use the photograph confidently where its evidence is strong; where evidence is weak, lower specificity or use the stronger supplemental owner instead of inventing false precision.
9. **Reject unintended camera artifacts before finalization.** Check clipped whites, dead darks, everywhere-focus, uniform detail density, photographic edge patterns, lens distortion, and missing atmospheric/color variation. Route each failure to its owning Pattern or recovery AP.
10. **Complete by the intended picture.** The result is finished when it satisfies the declared image goal using the photograph as bounded evidence, not when every recorded photographic detail has been copied.

## Notes
Different references may legitimately own different channels: one photograph can be strongest for structure, another exposure for values, a life study for color/atmosphere, and another angle for hidden construction. Missing evidence should reduce specificity rather than invite confident invention. Root authority and registered-successor authority are distinct: the former may establish/reorganize the intended picture; the latter must preserve the inherited Drawing lockset and use reference as bounded downstream evidence.
