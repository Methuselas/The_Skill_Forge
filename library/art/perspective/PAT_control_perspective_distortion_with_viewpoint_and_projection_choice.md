---
object_id: PAT_control_perspective_distortion_with_viewpoint_and_projection_choice
object_type: pattern
name: Control Perspective Distortion With Viewpoint and Projection Choice
library_path:
- art
- perspective
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- perspective
- distortion
- viewpoint
- projection
cross_links:
- rel: related_to
  target_object_id: PAT_validate_three_point_viewpoint_geometry
reference:
  source_title: 'Viewpoints: Mathematical Perspective and Fractal Geometry in Art'
  author: Marc Frantz and Annalisa Crannell
confidence: high
references: []
variants:
- variant_id: VAR_rectilinear_viewpoint_match
  variant_name: Rectilinear Viewpoint Match
  variant_basis: method_sequence
  difference_from_foundation: Recover or derive the viewing target and viewing distance before changing local objects. Reframe,
    crop, move the station point, spread vanishing points consistently, enlarge the support, or cluster important content
    nearer the viewing target.
  when_to_use: The intended image is a conventional flat-plane perspective and apparent distortion may be caused by viewing
    or framing mismatch.
  when_not_to_use: Do not use this as a substitute for correcting an actually inconsistent perspective construction; first
    distinguish construction error from viewing/framing mismatch.
  absorbed_from_object_id: none
- variant_id: VAR_extreme_field_projection_swap
  variant_name: Extreme-Field Projection Swap
  variant_basis: method_sequence
  difference_from_foundation: Consider a curvilinear or spherical projection rather than forcing one rectilinear grid to carry
    the entire field. Preserve the same scene directions and viewpoint logic while changing the projection surface/model.
  when_to_use: One compact image must cover a close, very tall, very wide, or near-immersive field that would demand an impractically
    close station point or very large flat support.
  when_not_to_use: Do not switch projection models for an ordinary field that a practical rectilinear viewpoint can carry
    cleanly.
  absorbed_from_object_id: none
- variant_id: VAR_one_look_edge_distortion_diagnostic
  variant_name: Use the One-Look Edge Diagnostic
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a quick production check: compare a major form near the frame edge with equivalent forms
    nearer the center; conspicuous edge stretch is a signal to move/reframe/crop before local correction.'
  when_to_use: Use for fast diagnosis before invoking exact station geometry.
  when_not_to_use: Do not promote Gill's fixed 60-degree cone as universal project law.
  absorbed_from_object_id: none
---

# Control Perspective Distortion With Viewpoint and Projection Choice

## Pattern Rule
**IF** perspective looks stretched, pinched, unnaturally rapid, implausibly flat, or makes the subject read at a misleading apparent size **THEN** first determine whether the construction is wrong or whether a valid construction is being viewed/framed from the wrong station relationship; correct the field globally through viewpoint, framing/support scale, or projection choice before repairing individual objects.

## Do
- Recover or establish the viewing target and viewing distance when the view is exact enough to justify it.
- Treat vanishing-point spacing as one consequence of the viewpoint geometry, not as the only distortion control.
- Check the subject's apparent scale as well as edge stretch: stronger convergence from a closer or more aggressive viewpoint can make the same product read as larger or more imposing even when its local proportions remain coherent.
- When a flat-plane image is valid but requires an implausibly close station point, move the viewpoint back and rebuild the field, crop/reframe, enlarge the support, or cluster key content nearer the viewing target.
- For a close skyscraper or other very large angular field, distinguish a mathematically valid rectilinear image from a practical display problem: the flat image may need to be physically huge to be experienced from a comfortable distance.
- When the intended compact image must preserve a much wider directional field than a practical flat-plane setup can carry, switch deliberately to a curvilinear/spherical projection rather than locally bending objects inside a rectilinear field.
- Keep prior Norling/Gill production checks: compare equivalent forms near the center and edges, and prefer a global reframe over local compensations.

## Don't
- Assume that edge distortion proves the perspective construction itself is mathematically wrong; test the implied station point first.
- Treat 50° or 60° as a universal mathematical cutoff. The audited source does not establish a single fixed cone-of-vision threshold.
- Add fake extra vanishing points to a face that is parallel to a flat picture plane merely to imitate the sensation of looking up and down a nearby skyscraper.
- Mix rectilinear and curvilinear rules accidentally inside the same field.
- Repair each object separately after the camera/viewfield has already become inconsistent.

## Checklist
- The implied station point/viewing distance is known or at least directionally plausible for the intended presentation.
- Equivalent objects do not change perspective logic merely because they approach the frame edge.
- Important content sits in a usable relation to the viewing target unless deliberate edge stress is intended.
- The chosen convergence does not accidentally make the subject read materially larger or smaller than the intended product-scale impression.
- A close tall/wide scene has an explicit decision: larger support/reframe versus alternate projection.
- The chosen projection model is consistent across the full scene.
- No fixed numeric COV rule is being mistaken for a theorem.

## Notes
This Pattern supersedes the earlier D'Amelio VP-spacing-only card. *Viewpoints* resolves the key ambiguity: rectilinear perspective can remain geometrically exact at an extreme field, but only from its implied station point and support geometry. Eissen and Steur add a useful design-sketch diagnostic: convergence changes perceived product scale as well as shape, so a technically consistent view can still communicate the wrong size impression. Practical distortion control therefore depends on the intended viewer/display as well as the vanishing geometry. Spherical/curvilinear projection is a deliberate alternate model for compact extreme fields, not a local correction applied after the fact.

`VAR_rectilinear_viewpoint_match` remains a bounded variant under the conditions recorded in its variant metadata.

`VAR_extreme_field_projection_swap` remains a bounded variant under the conditions recorded in its variant metadata.

`VAR_one_look_edge_distortion_diagnostic` remains a bounded variant under the conditions recorded in its variant metadata.

- Use camera distance and lens/projection behavior narratively: a close wide setup exaggerates near/far size differences and depth, while a distant long setup compresses apparent depth and relative scale.
- At very low viewpoints, treat ground contacts and actual ground-plane spacing as critical depth evidence; apparent gaps higher in the frame can be misleading.
