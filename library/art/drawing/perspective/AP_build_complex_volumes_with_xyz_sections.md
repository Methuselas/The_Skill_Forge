---
object_id: AP_build_complex_volumes_with_xyz_sections
object_type: ap
name: Build Complex Volumes With X-Y-Z Sections
library_path:
- art
- drawing
- perspective
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- perspective
- sections
- volume
- workflow
cross_links:
- rel: supports
  target_object_id: AP_construct_a_shared_scene_perspective_field
- rel: supports
  target_object_id: PAT_project_curves_onto_sectioned_surfaces
reference:
  source_id: scott_robertson_how_to_draw
  source_title: 'How to Draw: Drawing and Sketching Objects and Environments from Your Imagination'
  author: Scott Robertson with Thomas Bertling
  publish_date: '2013'
  media_type: book
  locator: u00, printed pp. 82-89 (physical PDF pp. 80-87)
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_zarins_slice_torso_at_anatomical_landmark_levels
  variant_name: Slice the Torso at Anatomical Landmark Levels
  variant_basis: method_sequence
  source_id: uldis_zarins_anatomy_for_sculptors
  source_title: 'Anatomy for Sculptors: Understanding the Human Figure'
  locator: u01, physical pp. 21-24
  difference_from_foundation: 'Specializes the committed X-Y-Z section workflow for organic human form: take horizontal sections through meaningful torso levels such as shoulder/chest, lower rib cage, waist, iliac-crest/hip, and pelvic regions, and let each section record the actual front-back and side-side distribution of the anatomy. The sections may be lobed, asymmetric, or sharply changing rather than ideal ellipses; connect them to recover the torso''s planar transitions and outer envelope.'
  when_to_use: Use when the torso silhouette is plausible but its depth distribution is guessed, when front/side studies disagree, or when a planar blockout needs proof that its corners correspond to one continuous organic volume.
  when_not_to_use: Do not cover a finished figure with equal-spaced slices or force Zarins's sample male/female section shapes onto another body. Add sections only at levels where changing anatomy or viewpoint needs clarification, and derive their shapes from the actual design/reference.
  absorbed_from_object_id: none
- variant_id: VAR_zarins_connect_leg_sections_with_anatomical_rails
  variant_name: Connect Leg Sections With Anatomical Rails
  variant_basis: method_sequence
  source_id: uldis_zarins_anatomy_for_sculptors
  source_title: 'Anatomy for Sculptors: Understanding the Human Figure'
  locator: u06, physical pp. 193-215, especially pp. 198, 206, 215
  difference_from_foundation: 'Extends section-based volume construction from the torso into a tapered articulated limb: place cross-sections where the thigh, knee, calf, shin, and ankle materially change shape, then connect those sections with longitudinal anatomical rails instead of stacking independent round segments. Zarins''s examples use persistent bony/surface routes such as the medial tibial surface and long traversing muscle paths; the sartorius can act as a visible thigh plane separator when the pose/body supports it. The resulting rails may drift diagonally across successive sections, producing asymmetric planes and torsion through the leg.'
  when_to_use: Use when a leg has believable silhouette but feels cylindrical, segmented, or impossible to rotate mentally; especially useful when front/side views disagree about where the major plane changes belong.
  when_not_to_use: Do not cover the finished leg with equal-spaced contour rings, force the sartorius or tibial rail to be visible in every body, or copy Zarins's sample section shapes as universal anatomy. Sections and rails are temporary construction evidence derived from the actual pose, build, and viewpoint.
  absorbed_from_object_id: none
---

# Build Complex Volumes With X-Y-Z Sections

## Objective
Construct a complex invented volume from readable side/top/front information and cross-sections so the form is built from the inside out instead of being guessed from its final silhouette.

## Steps / Flow


## Notes
Robertson calls X-Y-Z section drawing the core skill for complex volumes. The letters are an orientation vocabulary, not an algebra requirement: think **longitudinal profile + perpendicular profile + cross-sections**, each living on a perspective plane. The construction is intentionally suited to imagined vehicles, products, architecture, and machines, but the method itself is domain-portable.

`VAR_zarins_slice_torso_at_anatomical_landmark_levels` retains **Slice the Torso at Anatomical Landmark Levels** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_zarins_connect_leg_sections_with_anatomical_rails` retains **Connect Leg Sections With Anatomical Rails** as a bounded alternative; use it only under the conditions recorded in the variant metadata.
