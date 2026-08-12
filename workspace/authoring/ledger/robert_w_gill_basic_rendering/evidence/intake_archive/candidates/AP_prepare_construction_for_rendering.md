---
schema_version: vNext-draft.1
object_id: AP_prepare_construction_for_rendering
object_type: ap
name: Prepare a Construction Drawing for Rendering
library_path:
- art
- drawing
- rendering
status: candidate
confidence: high
tags:
- rendering
- lighting
- shade
- shadow
scope:
  role: specialization
  axis: workflow
  foundation_object_id: null
bindings:
  development_stages: []
  execution_profiles:
  - direct_dream
  - staged
  - teaching
capabilities:
  provides:
  - art.drawing.rendering.prepare_construction_for_rendering
  requires: []
  optional:
  - art.drawing.perspective.construct_cast_shadows
  - art.drawing.perspective.construct_shared_scene_field
  excludes: []
context:
  residency: transient
  priority: 76
  load_when:
  - a perspective or structural drawing is ready to become a rendered image and lighting decisions need to be made explicit before value or material work
  unload_when:
  - the clean rendering base has perspective, light direction, cast-shadow shapes, and light-versus-shade regions resolved
relations:
- rel: supports
  target_object_id: AP_construct_cast_shadows_in_perspective
- rel: supports
  target_object_id: PAT_consolidate_resolved_form_with_tone
grounding:
  mode: source_led
  evidence:
  - evidence_id: gill_pp52_57_shade_shadow
    kind: source
    source_id: robert_w_gill_basic_rendering
    locator: printed pp. 52-57 (physical PDF pp. 55-60)
    evidence_type: mixed
    note: Gill distinguishes shade from cast shadow and connects both to the chosen light source and reflected-light conditions.
  - evidence_id: gill_pp76_80_drawing_prep
    kind: source
    source_id: robert_w_gill_basic_rendering
    locator: printed pp. 76-80 (physical PDF pp. 79-83)
    evidence_type: mixed
    note: Gill requires cast-shadow shapes and the line of separation to be identified before rendering, then transfers the solved construction to a clean final surface.
  - evidence_id: gill_pp160_162_exercises
    kind: source
    source_id: robert_w_gill_basic_rendering
    locator: printed pp. 160-162 (physical PDF pp. 163-165)
    evidence_type: mixed
    note: 'The skill-building sequence repeats the order: accurate perspective, chosen light, constructed shadow shapes, identified separation line/light/shade, then rendering.'
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  execution_profiles:
    supported:
    - direct_dream
    - staged
    - teaching
    preferred: staged
  commitment_ledger:
    enabled: true
    persist_across_swaps: true
  states:
  - state_id: lock_construction
    objective: Confirm the perspective and structural drawing before lighting is asked to explain it.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - choose_light
  - state_id: choose_light
    objective: Fix a light direction/source relationship for the rendering.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - map_shadow
  - state_id: map_shadow
    objective: Construct cast-shadow shapes and identify the light/shade separation on the forms.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - transfer_clean
  - state_id: transfer_clean
    objective: Move only the solved information needed for rendering onto the final working layer or surface.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions: []
---

# Prepare a Construction Drawing for Rendering

## Objective
Convert a structurally solved drawing into a clean, light-aware rendering base before tone, texture, or polish begins.

## Steps / Flow
1. **Lock the construction.** Verify the perspective, major volumes, overlaps, and supporting planes. Do not let rendering become a substitute for unresolved structure.
2. **Choose the light.** Establish the light source or dominant light direction in relation to the object and viewer before assigning values.
3. **Construct the cast-shadow shapes.** Use the chosen light direction and the scene geometry to locate where opaque forms block light on receiving surfaces.
4. **Identify the light/shade separation.** Mark the form boundary where surfaces turn out of direct light. On curved forms treat this as a transition/terminator region rather than automatically drawing a hard contour.
5. **Name the regions correctly.** Keep form shade separate from cast shadow; reflected light may modify either later, but it does not change which condition produced it.
6. **Check the shadow-form relationship.** The cast-shadow boundary should be consistent with the light-facing separation of the form and with any receiver changes already solved in perspective.
7. **Transfer only the solved drawing.** Move the clean object contours, necessary internal edges, shadow shapes, and useful light/shade guides to the final layer/surface; leave construction clutter behind.
8. **Begin rendering only now.** Introduce values and material response on top of this clean base, preserving the perspective and lighting commitments beneath it.

## Notes
Gill's strongest contribution here is procedural separation: construction, light direction, cast-shadow geometry, and light/shade regions are solved before finish work. His exact “basic tonal pattern” is more conditional than the book sometimes implies, so this AP does not hard-code one universal ranking of top plane, side plane, shade, and shadow values.
