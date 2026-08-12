---
object_id: PAT_orient_rib_cage_with_curved_openings
object_type: pattern
name: Orient the Rib Cage With Curved Openings
library_path:
- art
- drawing
- subjects
- figure
- construction
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
- figure_drawing
- torso_construction
- rib_cage
- viewpoint
cross_links:
- rel: supports
  target_object_id: PAT_build_gesture_into_clear_masses
reference:
  source_id: burne_hogarth_dynamic_figure_drawing_ocr
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
  publish_date: 1970
  media_type: book
  evidence_type: mixed
  locator: ch01, printed pp. 12-17
confidence: high
references: []
variants:
- variant_id: VAR_hampton_use_landmarks_to_turn_major_masses
  variant_name: Use Landmarks to Turn the Major Masses
  variant_basis: method_sequence
  source_id: michael_hampton_figure_drawing_design_and_invention
  source_title: 'Figure Drawing: Design and Invention'
  locator: u01, printed pp. 29-36
  difference_from_foundation: 'Adds Hampton''s landmark-first perspective check to rib-cage orientation: place the stable skeletal points and symmetry line before committing to box planes; as the mass turns, the symmetry line favors the near-facing side and the opposite side plane becomes more visible. The landmarks generate the perspective scaffold instead of being pasted onto it afterward.'
  when_to_use: Use when the rib cage or pelvis is technically blocked but its turn is ambiguous, or when landmarks and perspective planes disagree.
  when_not_to_use: Do not force every torso into a literal box or treat Hampton's C/S symmetry-line shorthand as an invariant anatomical law; use landmarks to verify the chosen mass construction.
  absorbed_from_object_id: none
---

# Orient the Rib Cage With Curved Openings

## Pattern Rule
**IF** the upper torso must read as a solid mass from a specific angle
**THEN** block it as a barrel whose collarbone depression, diaphragm arch, and centerline curve consistently around the chosen view
**ELSE** simplify the torso to a single barrel and correct its opening curves before adding shoulders or anatomy

## Do
- Treat the rib cage as the largest single body mass and let it control the scale of nearby head and shoulder forms.
- Open the top and bottom as curved passages around the volume, not as flat horizontal cuts.
- In a high or low angle, use overlap and the swelling front-to-back curve to decide whether chest, back, neck, or head is dominant.

## Don't
- Use a flat oval or box that gives no evidence of front-to-back depth.
- Draw upper and lower arcs that imply different tilts on the same barrel.

## Checklist
- The two opening curves and centerline describe one compatible orientation.
- The chest can be read as an upview, downview, or level view without surface anatomy.
- Attached head and shoulders are subordinate to the rib-cage volume rather than enlarging it arbitrarily.

## Notes
The upper collarbone depression and lower diaphragm arch behave like cross-sections through a rounded volume. They are construction evidence: when their curvature disagrees, the torso cannot occupy one coherent space.

`VAR_hampton_use_landmarks_to_turn_major_masses` retains **Use Landmarks to Turn the Major Masses** as a bounded alternative; use it only under the conditions recorded in the variant metadata.
