---
object_id: PAT_calibrate_product_redesign_with_reference_underlay
object_type: pattern
name: Calibrate Product Redesign With a Reference Underlay
library_path:
- art
- drawing
- sketching
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- sketching
- underlay
- proportion
- scale
- redesign
- ergonomics
cross_links: []
reference:
  source_title: 'Sketching: Drawing Techniques for Product Designers'
  author: Koos Eissen and Roselien Steur
confidence: high
references: []
variants:
- variant_id: VAR_eissen_reopen_cad_design_decisions_with_model_underlay
  variant_name: Reopen Design Decisions With a 3D Model Underlay
  variant_basis: method_sequence
  difference_from_foundation: Uses a rough CAD/3D rendering or screenshot as temporary underlay geometry so the designer can
    sketch over an already modeled proposal, explore alternative details and surface decisions, then feed promising sketch
    changes back into another 3D pass. The useful loop can run 2D sketch -> rough 3D model/render -> 2D refinement -> 3D again,
    postponing expensive final surfacing until important lines and surfaces are resolved.
  when_to_use: Use during iterative product development when a 3D model exists but the design still needs fast hand-drawn
    exploration without rebuilding the full geometry for every alternative.
  when_not_to_use: Do not treat the render as authority that freezes the design, and do not use sketch-over to conceal geometry
    that must be corrected in the actual model before downstream engineering or presentation.
  absorbed_from_object_id: none
- variant_id: VAR_eissen_overlay_prototype_photos_for_ergonomic_review
  variant_name: Overlay Prototype Photos for Ergonomic Review
  variant_basis: context
  difference_from_foundation: Uses a photograph of a technical prototype as the underlay so a designer can sketch over visible
    user-product relationships such as grip envelope, hand clearance, control reach, contact zones, and placement of user-contact
    surfaces while still redesigning the product around those observations.
  when_to_use: Use when a physical prototype already exposes ergonomic relationships that should be inspected or revised without
    rebuilding the entire product geometry before each sketch iteration.
  when_not_to_use: Do not treat one photograph as proof of hidden clearances, forces, comfort, or motion that the camera does
    not show, and do not let prototype geometry become a fixed design authority when the sketch is meant to improve it.
  absorbed_from_object_id: none
---

# Calibrate Product Redesign With a Reference Underlay

## Pattern Rule
**IF** a redesign sketch must stay credible against an existing product's size, proportion, silhouette, or human-use scale
**THEN** place a matching reference image of the existing product, prototype, or physical model beneath the drawing at a useful scale, use it to calibrate the large dimensions and interaction anchors, then draw the new design freely over that scaffold instead of tracing the reference as the answer
**ELSE** sketch without an underlay when the task has no fixed reference geometry or scale relationship worth preserving

## Do
- Choose a reference view that exposes the proportions and interaction relationships the redesign actually needs to preserve or compare.
- Scale the underlay deliberately before drawing. Use life size when hand size, grip, reach, or another direct ergonomic relationship needs to be judged against the body.
- Read the reference first as a size-and-proportion scaffold: overall envelope, major masses, centerlines, attachment zones, and human-contact regions.
- When a physical prototype or model exposes useful wireframe, sectional, seam, or structural relationships, trace those explanatory relationships as calibration evidence instead of reducing the underlay to its outer silhouette alone.
- Let the redesign depart from the reference once those anchors are established; use the calibrated starting condition to support invention rather than to suppress it.
- Recheck the new silhouette and component placement against the underlay whenever free sketching begins to drift away from the intended physical scale.
- When several design variants must be compared fairly, reuse one calibrated underlay to hold viewpoint, scale, perspective, and major proportion anchors constant while the actual design differences change.

## Don't
- Do not trace the source contour so literally that the old design determines the new one.
- Do not assume a photograph is automatically useful at whatever size it arrives; an uncalibrated image can preserve the wrong physical relationships just as confidently as a guessed sketch.
- Do not use a single view as proof of hidden depth, transitions, or ergonomics that the image does not actually reveal.

## Checklist
- The underlay matches the viewpoint needed for the redesign decision.
- Overall size and the major proportional landmarks can be compared directly against the new sketch.
- Human-contact features are checked at a meaningful physical scale when ergonomics matter.
- The new design visibly departs where invention requires it instead of becoming a traced copy.
- Removing the underlay leaves a coherent sketch whose scale and proportions still read as intentional.

## Notes
An underlay is most useful as a calibration device, not as a drawing to be copied. A photograph or existing product image can stabilize size, volume, and proportion early enough that the designer is free to search for a new form without repeatedly rebuilding those relationships from guesswork. For hand-held products, life-size setup is especially useful because hand size and grip can be judged directly rather than imagined abstractly.

`VAR_eissen_reopen_cad_design_decisions_with_model_underlay` extends the same underlay logic into an iterative CAD loop: use the model as temporary geometry, sketch alternatives over it, and return useful decisions to the model. The model stabilizes viewpoint and volume; it does not become a veto on redesign.

`VAR_eissen_overlay_prototype_photos_for_ergonomic_review` uses a prototype photograph as an ergonomic inspection surface: sketch over the visible grip, reach, clearance, and contact relationships while treating anything outside the camera evidence as unresolved rather than assumed.
A photographed physical model can also function as an analytical underlay when its construction exposes the logic of the surface. Trace the structural or sectional relationships that clarify the shape, then use those relationships as a starting scaffold for redesign or rendering; the goal is to extract useful form evidence, not to preserve the model as final geometry.

A shared underlay can also function as an experimental control. If viewpoint, scale, perspective, and major proportion anchors stay fixed across alternatives, differences in the page are more likely to come from the designs themselves rather than from presentation drift.
