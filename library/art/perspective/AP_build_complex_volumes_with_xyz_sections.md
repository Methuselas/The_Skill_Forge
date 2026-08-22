---
object_id: AP_build_complex_volumes_with_xyz_sections
object_type: ap
name: Build Complex Volumes With X-Y-Z Sections
library_path:
- art
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
  source_title: 'How to Draw: Drawing and Sketching Objects and Environments from Your Imagination'
  author: Scott Robertson with Thomas Bertling
confidence: high
references: []
variants:
- variant_id: VAR_zarins_slice_torso_at_anatomical_landmark_levels
  variant_name: Slice the Torso at Anatomical Landmark Levels
  variant_basis: method_sequence
  difference_from_foundation: 'Specializes the committed X-Y-Z section workflow for organic human form: take horizontal sections
    through meaningful torso levels such as shoulder/chest, lower rib cage, waist, iliac-crest/hip, and pelvic regions, and
    let each section record the actual front-back and side-side distribution of the anatomy. The sections may be lobed, asymmetric,
    or sharply changing rather than ideal ellipses; connect them to recover the torso''s planar transitions and outer envelope.'
  when_to_use: Use when the torso silhouette is plausible but its depth distribution is guessed, when front/side studies disagree,
    or when a planar blockout needs proof that its corners correspond to one continuous organic volume.
  when_not_to_use: Do not cover a finished figure with equal-spaced slices or force Zarins's sample male/female section shapes
    onto another body. Add sections only at levels where changing anatomy or viewpoint needs clarification, and derive their
    shapes from the actual design/reference.
  absorbed_from_object_id: none
- variant_id: VAR_zarins_connect_leg_sections_with_anatomical_rails
  variant_name: Connect Leg Sections With Anatomical Rails
  variant_basis: method_sequence
  difference_from_foundation: 'Extends section-based volume construction from the torso into a tapered articulated limb: place
    cross-sections where the thigh, knee, calf, shin, and ankle materially change shape, then connect those sections with
    longitudinal anatomical rails instead of stacking independent round segments. Zarins''s examples use persistent bony/surface
    routes such as the medial tibial surface and long traversing muscle paths; the sartorius can act as a visible thigh plane
    separator when the pose/body supports it. The resulting rails may drift diagonally across successive sections, producing
    asymmetric planes and torsion through the leg.'
  when_to_use: Use when a leg has believable silhouette but feels cylindrical, segmented, or impossible to rotate mentally;
    especially useful when front/side views disagree about where the major plane changes belong.
  when_not_to_use: Do not cover the finished leg with equal-spaced contour rings, force the sartorius or tibial rail to be
    visible in every body, or copy Zarins's sample section shapes as universal anatomy. Sections and rails are temporary construction
    evidence derived from the actual pose, build, and viewpoint.
  absorbed_from_object_id: none
- variant_id: VAR_eissen_solve_cylindrical_junctions_with_projected_cross_sections
  variant_name: Solve Cylindrical Junctions With Projected Cross-Sections
  variant_basis: method_sequence
  difference_from_foundation: Solves a tube-to-cylinder junction by projecting decisive incoming cross-sections onto the host
    cylinder, then uses the host cylinder's ellipse direction to build an optional curved square or rectangular bounding patch
    around the junction. The saddle-like connection should remain coherently inside that width/height envelope instead of
    being guessed as an asymmetric blend.
  when_to_use: Use when one cylindrical or tubular product part enters, intersects, or blends into another and the visible
    junction contour is difficult to invent consistently from silhouette alone.
  when_not_to_use: Do not multiply sections after the junction is already unambiguous, and do not assume every cylindrical
    intersection is an exact ellipse when diameters, angles, offsets, or transition geometry differ.
  absorbed_from_object_id: none
- variant_id: VAR_eissen_construct_curved_tubes_with_sections_and_rails
  variant_name: Construct Curved Tubes With Sections and Longitudinal Rails
  variant_basis: method_sequence
  difference_from_foundation: 'Specializes section construction for a tube that bends through space: establish the tube''s
    curvature or center path, place a few circular cross-sections perpendicular to that changing path, choose corresponding
    points on successive sections, and connect those points as longitudinal rails before resolving the outer contour. The
    rails make the surface flow through the bend instead of leaving each cross-section as an isolated ring.'
  when_to_use: Use for bent handles, hoses, pipework, tubular frames, and similar forms whose changing direction makes a single
    silhouette or two endpoint ellipses insufficient to control the volume.
  when_not_to_use: Do not stack evenly spaced rings over an already clear tube, and do not let a rail jump between unrelated
    points on successive sections; sections and rails must describe one continuous surface around the actual bend.
  absorbed_from_object_id: none
- variant_id: VAR_eissen_control_changing_product_rounding_with_sparse_sections
  variant_name: Control Changing Product Rounding With Sparse Sections and Seams
  variant_basis: method_sequence
  difference_from_foundation: 'Specializes section construction for product-body rounding that changes along a surface rather
    than following one constant-radius turn: establish the major parent surfaces, place sectional slices only where the rounding
    materially changes, and connect those checkpoints with longitudinal transition lines, seams, or structural ribs that naturally
    follow the form before selecting the outer contour.'
  when_to_use: Use when a product body has compound, tapered, or changing rounding whose surface turn cannot be inferred reliably
    from the endpoints alone, especially when a seam or rib can double as a readable construction rail.
  when_not_to_use: Do not cover a simple constant fillet with contour rings, invent seams that the design does not support,
    or treat every visible seam as proof of a geometric section. Use only the slices and rails needed to solve the changing
    transition.
  absorbed_from_object_id: none
- variant_id: VAR_eissen_curve_surface_by_offsetting_sections_from_flat_datum
  variant_name: Curve a Surface by Offsetting Sections From a Flat Datum
  variant_basis: method_sequence
  difference_from_foundation: 'Starts from a broad flat reference plane rather than an already volumetric shell: place decisive
    sectional locations on that datum, raise or lower selected section profiles relative to the original plane, then connect
    those displaced profiles into the new curved surface while retaining enough of the datum to make the deformation legible.
    The reference plane turns shallow, irregular curvature into a controlled offset problem instead of a guessed silhouette.'
  when_to_use: Use for shallow shells, trays, pads, covers, and broad product surfaces whose form is easier to understand
    as a deformation of an original plane than as a stack of primitive solids.
  when_not_to_use: Do not force strongly volumetric or deeply undercut forms into a flat-datum method, and do not add evenly
    spaced sections when only a few transition locations determine the curvature.
  absorbed_from_object_id: none
---

# Build Complex Volumes With X-Y-Z Sections

## Objective
Construct a complex invented or observed volume from trustworthy governing views, cross-sections, and surface routes so the form is solved from the inside out and remains coherent when the final silhouette is derived.

## Steps / Flow
1. **Choose the entry frame.** If the object belongs to a scene whose perspective field is not yet trustworthy, delegate that bounded sub-action to `AP_construct_a_shared_scene_perspective_field` before section construction begins. For an isolated design object, establish only the local orientation/axis framework needed to keep its views and sections mutually coherent.
2. **State the purpose of the section network.** Decide whether sections are being used to construct an uncertain volume, diagnose changing curvature, optimize a transition, or explain a solved form. Do not add technical scaffolding without an unresolved spatial job.
3. **Establish the governing information.** Lock the side, top, front, longitudinal, centerline, or other decisive profiles that define the volume's orientation and major extents.
4. **Pass the profile-agreement gate.** Before sections proliferate, verify that the governing views can plausibly describe one object. If front/top/side or longitudinal information disagrees about extents, orientation, symmetry, or major turns, repair that disagreement now rather than formalizing it with more slices.
5. **Place only structurally meaningful cross-sections.** Add slices where the form materially changes. Prefer meaningful transition levels and directions over arbitrary equal spacing; sections are commonly perpendicular to the dominant form or surface direction when that best describes the volume.
6. **Use a decisive section when one governs the form.** For a symmetrical or section-led volume, solve that key section first and build outward from it rather than guessing an exterior envelope and repairing it later. When the section itself should be symmetric but drifts, control it inside a perspective square/rectangle or matched construction scaffold.
7. **Pass the section-coherence gate.** Each section must live on a coherent plane, preserve correspondence with the governing profiles, and transition plausibly toward neighboring slices. Repair an isolated bad section locally; if many sections demand increasingly distorted fixes, roll back to the governing profiles or perspective frame.
8. **Connect corresponding points into surface routes.** Use longitudinal rails, contours, seams, centerlines, or other meaningful paths so the sections describe one continuous surface rather than independent rings.
9. **Pass the rail/surface-continuity gate.** Corresponding rails may bend, taper, and twist, but they may not silently swap roles, kink without a structural cause, or cross in ways that imply an impossible envelope. When continuity fails across many rails, return to the earliest section/profile decision that caused it.
10. **Add late sections only where ambiguity remains.** Use additional slices to resolve a specific contour, curvature transition, hidden relationship, or junction. Omit them when the network already predicts the form clearly.
11. **Derive the visible form from the internal solution.** Resolve the final contour and important surface routes from the accepted network, then remove construction evidence that no longer helps.
12. **Complete when the network has done its job.** Stop when the visible contour and major surface flow can be derived from the accepted profiles/sections, important hidden relationships remain coherent, and further sections would add notation rather than reduce uncertainty.

## Notes
Persistent invariants are **FRAME**, **CORRESPONDENCE**, **CONTINUITY**, and **PURPOSE**. The governing orientation may not drift while later slices are added; corresponding points must remain corresponding; all sections and rails must belong to one continuous volume; and every construction mark must answer a real spatial question.

Robertson's X-Y-Z vocabulary is an orientation framework rather than an algebra requirement: think longitudinal profile + perpendicular profile + cross-sections. Organic and product variants may use asymmetric, lobed, tapered, or changing sections when the actual form requires them. The protocol does not reward dense section grids; it rewards a section network whose internal evidence predicts the same object from every useful view.

`VAR_zarins_slice_torso_at_anatomical_landmark_levels` retains the anatomical-landmark torso-section specialization.

`VAR_zarins_connect_leg_sections_with_anatomical_rails` retains the articulated-limb section-and-rail specialization.

`VAR_eissen_solve_cylindrical_junctions_with_projected_cross_sections` retains the projected cylindrical-junction specialization.

`VAR_eissen_construct_curved_tubes_with_sections_and_rails` retains the curved-tube section-and-rail specialization.

`VAR_eissen_control_changing_product_rounding_with_sparse_sections` retains the sparse-section changing-rounding specialization.

`VAR_eissen_curve_surface_by_offsetting_sections_from_flat_datum` retains the flat-datum offset-surface specialization.
