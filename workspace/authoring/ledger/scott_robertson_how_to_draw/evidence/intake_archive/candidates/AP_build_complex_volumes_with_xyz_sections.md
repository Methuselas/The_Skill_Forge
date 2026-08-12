---
schema_version: vNext-draft.1
object_id: AP_build_complex_volumes_with_xyz_sections
object_type: ap
name: Build Complex Volumes With X-Y-Z Sections
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- sections
- volume
- workflow
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
  - art.drawing.perspective.build_complex_volumes_with_xyz_sections
  requires:
  - art.drawing.perspective.construct_shared_scene_field
  - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
  optional:
  - art.drawing.perspective.rotate_grids_preserve_unit_scale
  - art.drawing.perspective.construct_projected_circles
  - art.drawing.perspective.project_curves_onto_sectioned_surfaces
  excludes: []
context:
  residency: phase
  priority: 94
  load_when:
  - an invented vehicle, machine, product, architecture element, or other complex volume must be constructed from controllable profiles instead of guessed as one outer silhouette
  unload_when:
  - the section network and tangent silhouette define one coherent volume ready for specific detail
relations:
- rel: supports
  target_object_id: AP_construct_a_shared_scene_perspective_field
- rel: orchestrates
  target_object_id: PAT_project_curves_onto_sectioned_surfaces
grounding:
  mode: source_led
  evidence:
  - evidence_id: robertson_pp82_89_xyz
    kind: source
    source_id: scott_robertson_how_to_draw
    locator: printed pp. 82-89 (physical PDF pp. 80-87)
    evidence_type: mixed
    note: Robertson plans with simpler orthographic/draft views, transfers a profile through a proportioned bounding rectangle, then builds the volume from Y centerline, Z/top width, mirrored profiles, X cross-sections, and a silhouette tangent to the section network.
  - evidence_id: robertson_pp90_103_xyz_extension
    kind: source
    source_id: scott_robertson_how_to_draw
    locator: printed pp. 90-103 (physical PDF pp. 88-101)
    evidence_type: mixed
    note: The chapter extends the section method into cuts, fillets, surface details, temporary construction planes, contour/overlap decisions, and more complex sculpted transitions.
  derivations:
  - derivation_id: xyz_volume_ap_synthesis
    kind: synthesis
    inputs:
    - robertson_pp82_89_xyz
    - robertson_pp90_103_xyz_extension
    note: Condenses Robertson's core section-drawing curriculum into one volume-building workflow while keeping subject-specific vehicle/product examples out of the foundation.
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
  - state_id: plan_profile
    objective: Establish the clearest draft/profile view and its controlling proportions before perspective compression is introduced.
    requires: []
    optional: []
    warmup_capabilities:
    - activation.art.drawing.perspective.construction_line_aiming_warmup
    release_on_exit: []
    checkpoint: true
    transitions:
    - transfer_profiles
  - state_id: transfer_profiles
    objective: Transfer the longitudinal and width/top profiles onto compatible perspective planes.
    requires:
    - art.drawing.perspective.construct_shared_scene_field
    optional:
    - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - build_sections
  - state_id: build_sections
    objective: Add and mirror cross-sections until the volume can be read from the inside out.
    requires: []
    optional:
    - art.drawing.perspective.construct_projected_circles
    warmup_capabilities:
    - activation.art.drawing.perspective.ellipse_axis_warmup
    release_on_exit: []
    checkpoint: true
    transitions:
    - close_silhouette
  - state_id: close_silhouette
    objective: Draw the outer silhouette tangent to the solved section network and resolve disagreements before detail.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - modify_surface
  - state_id: modify_surface
    objective: Add cuts, fillets, graphics, and design curves through the established section system as needed.
    requires: []
    optional:
    - art.drawing.perspective.project_curves_onto_sectioned_surfaces
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions: []
---

# Build Complex Volumes With X-Y-Z Sections

## Objective
Construct a complex invented volume from readable side/top/front information and cross-sections so the form is built from the inside out instead of being guessed from its final silhouette.

## Steps / Flow
1. **Plan before perspective.** Draw the view you understand most clearly as a simple side, top, or front draft. Establish the important proportions there without fighting foreshortening.
2. **Transfer the controlling profile.** Put the draft profile inside a simple divisible bounding rectangle, mark meaningful intersections, reproduce that rectangle on the perspective grid, and transfer the profile point by point when the view is too foreshortened to trust by eye.
3. **Establish one longitudinal plane.** Use the Y-style center plane for the main centerline/profile. Keep attention on that one plane until its curve and proportions are coherent.
4. **Establish width/top information.** Add the perpendicular Z-style plane or top view that controls width and the object's support footprint, then mirror it when symmetry is intended.
5. **Slice the object.** Add X-style cross-sections at useful grid locations. Every section must meet the already established center/top information at compatible points; start with the sections that reveal the most shape.
6. **Mirror and extend sections as needed.** Use perspective mirroring rather than independently redrawing the far side. Insert more sections only where the changing form cannot yet be inferred safely.
7. **Draw the outside silhouette last.** Let the silhouette run tangent to the solved cross-sections; do not force the sections to match a prematurely designed outline.
8. **Modify the solved volume.** Add cuts, radii, surface changes, graphics, or intersection curves by projecting them through the section system instead of painting them onto the shell.
9. **Validate the form from several directions.** A side profile, top/width logic, cross-sections, and outer contour should describe the same object; if one disagrees, fix the controlling section before adding detail.

## Notes
Robertson calls X-Y-Z section drawing the core skill for complex volumes. The letters are an orientation vocabulary, not an algebra requirement: think **longitudinal profile + perpendicular profile + cross-sections**, each living on a perspective plane. The construction is intentionally suited to imagined vehicles, products, architecture, and machines, but the method itself is domain-portable.
