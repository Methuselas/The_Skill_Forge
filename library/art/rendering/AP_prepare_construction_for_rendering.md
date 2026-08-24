---
object_id: AP_prepare_construction_for_rendering
object_type: ap
name: Prepare a Construction Drawing for Rendering
library_path:
- art
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- rendering
- lighting
- shade
- shadow
cross_links:
- rel: supports
  target_object_id: AP_construct_cast_shadows_in_perspective
- rel: supports
  target_object_id: PAT_consolidate_resolved_form_with_tone
- rel: supports
  target_object_id: PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum
reference:
  source_title: 'Basic Rendering: Effective Drawing for Designers, Artists and Illustrators'
  author: Robert W. Gill
confidence: high
references: []
variants: []
---

# Prepare a Construction Drawing for Rendering

## Objective
Convert a trustworthy construction into a clean downstream appearance base whose form, perspective, light model, form-shade logic, and required cast shadows agree before later appearance or medium-specific development begins. When an approved Drawing predecessor exists, inherit its accepted lockset rather than reopening solved Drawing decisions.

## Steps / Flow
1. **Pass the construction-entry and predecessor gate.** Enter only when perspective, major volumes, attachments/overlaps, support relationships, and important hidden continuations are trustworthy enough for downstream appearance work. If an approved Drawing predecessor exists, inherit its camera, crop, composition, pose, perspective, placement, major form/design, scene inventory, and important overlap/contact decisions as locked. If no approved Drawing predecessor exists, a legitimate root or alternate-entry workflow may still supply trustworthy construction without manufacturing Finished Pencils first. If downstream appearance work would have to choose unresolved structure, return to the construction owner instead of using tone as camouflage.
2. **Establish the light model.** Use `PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum` to define enough of the dominant source—direction, relative size/quality, spectral tendency where relevant, and important secondary/reflected influences—to predict the intended form/shadow behavior.
3. **Map the form-light separation.** Identify which surfaces face the source and where they turn out of direct light. On curved forms treat the terminator as a form-dependent transition rather than automatically converting it into a hard contour.
4. **Delegate significant geometric cast shadows when needed.** When important opaque forms cast structurally meaningful shadows onto known receivers, invoke `AP_construct_cast_shadows_in_perspective`, then return with the solved shadow geometry. Under very diffuse light or when cast shadows are not structurally important, do not invoke the subordinate AP mechanically.
5. **Keep causes distinct.** Name form shade, cast shadow, occlusion, and reflected-light effects according to what produces them. Reflected light may modify appearance later, but it does not change whether a region is form shade or cast shadow.
6. **Pass the causal-consistency gate.** Check that terminators, form shade, cast-shadow direction/shape, receiver changes, and accepted geometry all agree with the same light model. A visually attractive shadow that implies an impossible source or receiver fails.
7. **Route failures to the correct owner.** If the lighting/shadow map exposes an impossible form, return to construction rather than distorting the light to hide it. If construction remains sound but a shadow or light relation is wrong, repair the light/shadow decision without reopening the object.
8. **Pass the transfer gate.** Apply `PAT_consolidate_resolved_form_with_tone` at this decision. Identify exactly which information must survive into the rendering base: visible structural contours, necessary internal boundaries, important form-light guides, and required cast-shadow geometry. Remove scaffolding whose diagnostic job is finished.
9. **Build the clean rendering base.** Transfer only the solved information while preserving registration to the accepted construction. Cleanup may simplify marks; it may not move the structure or rewrite the light.
10. **Hand off only after verification.** Pass the clean base to the applicable downstream appearance or medium workflow only when it still reproduces the trusted form and predicts a coherent light/shadow system. Rendering owners may develop shared appearance relationships such as light, value, visible color, material response, atmosphere, and edges within their scope; the selected downstream medium AP owns medium-specific finish and completion.

## Notes
Persistent invariants are **STRUCTURE**, **LIGHT**, **CAUSE**, and **TRANSFER**. Downstream appearance interpretation may enrich accepted structure but may not relocate or silently redesign it; local values must belong to one active light model; shadow categories remain tied to their causes; and cleanup must preserve every piece of construction evidence the next appearance decisions actually need.

Completion is a clean structural/light base whose perspective/form, light model, form-shade logic, and required cast shadows agree without construction clutter that the next workflow would have to interpret around. This AP prepares a handoff; it does not universally own material appearance, color orchestration, or medium-specific finish. If a downstream workflow discovers a genuine upstream structural defect, roll back to the owning construction/Drawing AP rather than repairing it covertly downstream.
