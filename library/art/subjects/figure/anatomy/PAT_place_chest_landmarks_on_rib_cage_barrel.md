---
object_id: PAT_place_chest_landmarks_on_rib_cage_barrel
object_type: pattern
name: Place Chest Landmarks on the Rib-Cage Barrel
library_path:
- art
- subjects
- figure
- anatomy
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: PAT_design_surface_anatomy_as_microgesture_on_parent_forms
tags:
- figure_drawing
- chest_anatomy
- landmark_placement
- surface_form
cross_links:
- rel: related_to
  target_object_id: PAT_orient_rib_cage_with_curved_openings
reference:
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
confidence: high
references: []
variants:
- variant_id: VAR_zarins_build_breast_as_deformable_mass_over_pectoralis
  variant_name: Build Breast Tissue as a Deformable Mass Over the Pectoral Wall
  variant_basis: method_sequence
  difference_from_foundation: 'Extends chest-landmark placement into volumetric tissue behavior: separate the breast mass
    from the pectoralis and rib-cage wall beneath it, establish its attachment to that wall, then redistribute the mass with
    gravity and body orientation rather than preserving a pasted sphere. Across pose changes, treat the same breast as approximately
    conserving its tissue volume while its profile, lower border, projection, and weight distribution change.'
  when_to_use: Use when breasts are correctly placed on the chest but still look like rigid hemispheres, when the torso changes
    orientation, or when reclining/side-lying poses require the mass to respond to gravity.
  when_not_to_use: Do not freeze Zarins's youthful-shape tips into a universal ideal or literal physics law. Age, size, tissue
    composition, support, pregnancy/lactation history, motion, clothing, and individual anatomy can change both attachment
    and deformation; use the actual reference/design as authority.
  absorbed_from_object_id: none
---

# Place Chest Landmarks on the Rib-Cage Barrel

## Pattern Rule
**IF** pectoral, nipple, or breast landmarks must be placed on a front or three-quarter torso
**THEN** project paired approximately forty-five-degree paths from the neck-pit region over the rib-cage surface, place the landmarks on those paths, and then shape the tissue to the body and view
**ELSE** reorient the barrel before placing surface anatomy

## Do
- Wrap each guide over the chest volume so its apparent angle changes with the torso rather than staying flat on the page.
- In a full front view, allow the paired forms to point outward; in a three-quarter view, expect one to appear more frontal and the other more profile.
- Retain the structural placement while adjusting visible tissue for age, body mass, muscular support, gravity, and the intended character.

## Don't
- Paste two identical circles onto the chest or aim both forms directly at the viewer.
- Use surface tissue to redefine a rib cage whose volume and facing direction are still unclear.

## Checklist
- The neck pit, paired chest landmarks, and torso centerline belong to the same barrel.
- The left and right forms follow the chest curvature rather than mirroring as flat symbols.
- A body-type variation changes tissue behavior without losing the underlying placement scaffold.

## Notes
The forty-five-degree construction is a legacy average-body heuristic, not a promise that every finished chest has the same surface shape. Its durable value is positional: secondary tissue sits on a primary barrel and responds to that barrel, the view, and gravity.

`VAR_zarins_build_breast_as_deformable_mass_over_pectoralis` retains **Build Breast Tissue as a Deformable Mass Over the Pectoral Wall** as a bounded alternative; use it only under the conditions recorded in the variant metadata.
