---
schema_version: vNext-draft.1
object_id: PAT_render_material_from_optical_response
object_type: pattern
name: Render Material From Optical Response
library_path:
- art
- drawing
- rendering
status: candidate
confidence: high
tags:
- material
- reflection
- transparency
- texture
scope:
  role: foundation
  axis: method
  foundation_object_id: null
bindings:
  development_stages: []
  execution_profiles:
  - direct_dream
  - staged
  - teaching
capabilities:
  provides:
  - art.drawing.rendering.render_material_from_optical_response
  requires: []
  optional:
  - art.drawing.rendering.prepare_construction_for_rendering
  excludes: []
context:
  residency: transient
  priority: 68
  load_when:
  - geometry and lighting already read but the surface still does not communicate what material it is made from
  unload_when:
  - the material reads from a small set of coherent reflection, transparency, value, and texture cues
relations:
- rel: supports
  target_object_id: PAT_consolidate_resolved_form_with_tone
grounding:
  mode: source_led
  evidence:
  - evidence_id: gill_pp68_71_reflection_absorption
    kind: source
    source_id: robert_w_gill_basic_rendering
    locator: printed pp. 68-71 (physical PDF pp. 71-74)
    evidence_type: mixed
    note: Gill makes reflected-light efficiency, base value, and surface behavior central to what the observer sees, while acknowledging practical materials depart from ideal black/white cases.
  - evidence_id: gill_pp95_117_form_before_material
    kind: source
    source_id: robert_w_gill_basic_rendering
    locator: printed pp. 95-117 (physical PDF pp. 98-120)
    evidence_type: mixed
    note: The cylinder/cone/sphere chapters separate form identity from later material-specific reflection and show reflected-light exceptions changing local values without changing underlying form.
  - evidence_id: gill_pp118_130_glass
    kind: source
    source_id: robert_w_gill_basic_rendering
    locator: printed pp. 118-130 (physical PDF pp. 121-133)
    evidence_type: mixed
    note: Glass is treated through visual penetration, reflection, background, and viewing angle; Gill recommends using the minimum evidence needed to communicate a transparent highly reflective material.
  - evidence_id: gill_pp131_137_water
    kind: source
    source_id: robert_w_gill_basic_rendering
    locator: printed pp. 131-137 (physical PDF pp. 134-140)
    evidence_type: mixed
    note: Water shifts between transparency and mirror-like reflection according to view angle, depth, bottom reflectance, and surface disturbance, with roughness fragmenting reflected images.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Render Material From Optical Response

## Pattern Rule
**IF** the form already reads but the material does not **THEN** identify the small set of optical cues that distinguish that surface—base value, reflection strength, transparency or opacity, surface roughness/texture, and environmental reflections—and add those cues without sacrificing the underlying light-and-form structure.

## Do
- Establish the object's shape and light/shade structure first; material cues should modify a readable form rather than create the form from scratch.
- Ask what the surface sends back toward the viewer: broad diffuse value, sharp reflected shapes, transmitted/background information, broken texture, or some mixture.
- Use the environment and background as part of the material description when the surface is reflective or transparent.
- For glass, prioritize visual penetration plus reflected highlights/shapes; at some angles the viewer mainly sees through it, at grazing angles reflection can dominate.
- For smooth water, decide whether the current view favors transparency or mirror-like reflection; as the surface becomes disturbed, break and fragment the reflected image according to the surface movement.
- Use only enough texture to identify the material at the intended scale; keep high-frequency marks subordinate to the large form and light pattern.

## Don't
- Replace form construction with texture symbols or surface noise.
- Assume one canned highlight proves “glass,” “metal,” “water,” or “leather” regardless of viewpoint and surroundings.
- Copy Gill's ideal white-reflects-all / black-absorbs-all diagrams as literal material physics; use them only as a historical simplification of relative reflectance.
- Render every material cue at equal strength when only two or three cues are needed to communicate the surface.

## Checklist
- The object remains legible as a volume when texture marks are removed.
- The material response is consistent with the light, viewer, and nearby environment.
- Transparent or reflective surfaces include believable information from what lies behind or around them.
- Surface detail supports rather than competes with the main tonal and spatial hierarchy.

## Notes
Gill's glass and water chapters are kept as variants of one broader decision rather than separate foundations: the renderer decides which optical evidence is carrying the material under the current conditions. This preserves his practical observation while avoiding his more idealized reflection/absorption explanations as universal physics.
