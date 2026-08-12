---
schema_version: vNext-draft.1
object_id: PAT_grade_depth_with_atmospheric_effect
object_type: pattern
name: Grade Depth With Atmospheric Effect
library_path:
- art
- drawing
- rendering
status: candidate
confidence: high
tags:
- atmosphere
- depth
- value
- contrast
scope:
  role: specialization
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
  - art.drawing.rendering.grade_depth_with_atmospheric_effect
  requires: []
  optional:
  - art.drawing.perspective.construct_shared_scene_field
  excludes: []
context:
  residency: transient
  priority: 72
  load_when:
  - a rendered scene needs stronger near-to-far separation, especially across objects, ground, cast shadows, or repeated forms
  unload_when:
  - the intended depth hierarchy reads without keeping the atmospheric instructions resident
relations:
- rel: supports
  target_object_id: AP_construct_a_shared_scene_perspective_field
grounding:
  mode: source_led
  evidence:
  - evidence_id: gill_pp25_31_atmosphere
    kind: source
    source_id: robert_w_gill_basic_rendering
    locator: printed pp. 25-31 (physical PDF pp. 28-34)
    evidence_type: mixed
    note: Gill demonstrates identical forms at increasing distances losing value separation and contrast, with foreground contrasts strongest and distant forms progressively neutralized.
  - evidence_id: gill_pp83_86_global_atmosphere
    kind: source
    source_id: robert_w_gill_basic_rendering
    locator: printed pp. 83-86 (physical PDF pp. 86-89)
    evidence_type: mixed
    note: Gill applies the same depth grading to the object, ground plane, and cast shadow, warning that selective atmospheric treatment creates contradictory spatial evidence.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Grade Depth With Atmospheric Effect

## Pattern Rule
**IF** a rendered scene must separate near from far beyond line perspective alone **THEN** reduce contrast, value separation, edge clarity, and fine detail as distance increases, applying the depth grade consistently to objects, ground, and cast shadows rather than fading only selected elements.

## Do
- Establish the strongest readable value separation in the foreground or nearest important zone, then progressively compress that separation with distance.
- Let distant darks move toward the surrounding middle values and distant lights lose some local brilliance so far forms become less contrasty than near ones.
- Apply the same near-to-far logic to ground planes, repeated structures, cast shadows, and background forms that occupy the same atmosphere.
- Use the effect as a depth layer after the perspective field and major lighting relationships are already coherent.
- Preserve important light-versus-shade relationships while reducing their contrast as they recede; atmosphere should soften a solved form, not erase its structure arbitrarily.

## Don't
- Fade distant objects while leaving their cast shadows or ground contacts equally black and crisp.
- Treat atmospheric depth as a background-only fog effect when middle-ground forms should also participate.
- Use contrast loss to repair wrong scale, convergence, overlap, or object placement.
- Import Gill's simplified particle explanation as a complete physical theory of atmospheric scattering; keep the card at the observable rendering level.

## Checklist
- Near forms have more value separation and edge/detail clarity than equivalent far forms.
- Ground, shadows, and objects agree about which zones are near and far.
- The scene still reads structurally if the atmospheric grade is mentally removed.
- Distant forms are quieter without becoming unrelated flat cutouts.

## Notes
Gill calls this “atmospheric effect” and repeatedly treats it as part of the same spatial evidence system as convergence, diminution, foreshortening, light, shadow, and overlap. The durable extraction is the near-to-far loss of contrast and clarity, not the book's period-specific account of why the air produces it.
