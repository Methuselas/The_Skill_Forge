---
object_id: AP_prepare_construction_for_rendering
object_type: ap
name: Prepare a Construction Drawing for Rendering
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
  - rendering
  - lighting
  - shade
  - shadow
cross_links:
  - rel: supports
    target_object_id: AP_construct_cast_shadows_in_perspective
  - rel: supports
    target_object_id: PAT_consolidate_resolved_form_with_tone
reference:
  source_title: 'Basic Rendering: Effective Drawing for Designers, Artists and Illustrators'
  author: Robert W. Gill
confidence: high
references: []
variants: []
---

# Prepare a Construction Drawing for Rendering

## Objective
Convert a structurally solved drawing into a clean, light-aware rendering base before tone, texture, or polish begins.

## Steps / Flow
1. **Lock the construction.** Verify the perspective, major volumes, overlaps, and supporting planes. Do not let rendering become a substitute for unresolved structure.
2. **Choose the light.** Establish the light source or dominant light direction **and its quality** in relation to the object and viewer before assigning values; note whether the dominant illumination is direct, diffuse, backlit, underlit, or otherwise distinctive enough to change the shadow/edge pattern.
3. **Construct the cast-shadow shapes.** Use the chosen light direction and the scene geometry to locate where opaque forms block light on receiving surfaces.
4. **Identify the light/shade separation.** Mark the form boundary where surfaces turn out of direct light. On curved forms treat this as a transition/terminator region rather than automatically drawing a hard contour.
5. **Name the regions correctly.** Keep form shade separate from cast shadow; reflected light may modify either later, but it does not change which condition produced it.
6. **Check the shadow-form relationship.** The cast-shadow boundary should be consistent with the light-facing separation of the form and with any receiver changes already solved in perspective.
7. **Transfer only the solved drawing.** Move the clean object contours, necessary internal edges, shadow shapes, and useful light/shade guides to the final layer/surface; leave construction clutter behind.
8. **Begin rendering only now.** Introduce values and material response on top of this clean base, preserving the perspective and lighting commitments beneath it.

## Notes
