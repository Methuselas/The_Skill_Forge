---
object_id: PAT_crop_decisively_to_reshape_figure_ground_relationships
object_type: pattern
name: Crop Decisively to Reshape Figure-Ground Relationships
library_path:
- art
- drawing
- composition
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- composition
- framing
- cropping
- figure_ground
- intimacy
cross_links:
- rel: related_to
  target_object_id: PAT_resolve_unintended_tangencies_with_overlap_or_separation
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants:
- variant_id: VAR_mogilevtsev_keep_revisable_frame_with_outer_margin
  variant_name: Keep a Revisable Frame With Outer Margin
  variant_basis: method_sequence
  difference_from_foundation: "Adds Mogilevtsev's reversible paper-framing method: when the intended aspect ratio is known but exact placement is still unsettled, draw the working format inside a larger sheet and keep usable margin beyond it so the frame can shift or expand after the figure is tested. This turns crop preview into an explicit nondestructive construction rather than committing the physical paper edge immediately."
  when_to_use: Use when a long study has a known general format but figure placement, movement, or surrounding space may still require adjustment before the final drawing or transfer is fixed.
  when_not_to_use: Do not keep reopening the frame after the composition is approved, and do not violate required trim, bleed, fixed-output dimensions, or other final-format constraints; digitally, use an equivalent nondestructive crop rather than manufacturing unnecessary canvas margin.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_leave_sacrificial_crop_margin_for_downstream_formatting
  variant_name: Leave Sacrificial Crop Margin for Downstream Formatting
  variant_basis: constraint
  difference_from_foundation: Preserves expendable image area around a stable compositional core when later production may legitimately place the same artwork into different borders, mats, aspect ratios, or crops. Unlike a revisable working frame, the extra margin is retained for downstream format flexibility after the core composition is already resolved.
  when_to_use: Use when the final crop is not controlled by the artist and the same image may need to survive multiple known or plausible output formats.
  when_not_to_use: Do not leave vague excess space when the final format is fixed, and do not let optional crop margin weaken the designed central hierarchy.
  absorbed_from_object_id: none
---
# Crop Decisively to Reshape Figure-Ground Relationships

## Pattern Rule
**IF** the frame is still open and a tighter or more selective crop would improve intimacy, abstraction, subject dominance, or the surrounding negative shapes
**THEN** treat the page edge as an active compositional boundary and choose deliberate cuts that create useful new figure-ground relationships
**ELSE** keep the subject more complete when identification, comparison, environment, or technical context requires the missing information

## Do
- Preview more than one crop before committing when the composition is still open.
- Judge what the frame creates, not only what it removes: every cut changes the remaining positive and negative shapes.
- Use closer crops deliberately to increase intimacy, scale, or abstraction.
- Let forms cross the frame decisively when partial visibility is the intended design.
- Recheck critical joints, facial features, contacts, and strong tangencies before finalizing the crop.

## Don't
- Treat accidental truncation as intentional cropping after the fact.
- Cut exactly through a critical junction simply because the object no longer fits.
- Leave a tiny sliver of form at the frame when a decisive inclusion or exclusion would read better.
- Assume every composition needs a crop; complete containment can be the stronger choice.

## Checklist
- The crop improves a specific compositional goal rather than merely making the subject larger.
- Frame-edge cuts look deliberate.
- New negative shapes created by the crop are useful rather than awkward leftovers.
- Required story, structural, or technical information survives the framing choice.

## Notes
Dodson treats the frame as part of the design. A crop can alter the viewer's distance, break one broad ground into more useful shapes, or turn a familiar subject into a more abstract pattern. His specific "crop and float" advice is retained as a source heuristic rather than a universal rule; the durable decision is intentional frame-edge design.

`VAR_mogilevtsev_keep_revisable_frame_with_outer_margin` adds Mogilevtsev's paper-study method for delaying final frame commitment: draw the intended format inside a larger field, keep usable outer margin, test the figure, and shift or expand the inner frame before the long drawing is locked.

`VAR_loomis_leave_sacrificial_crop_margin_for_downstream_formatting` covers a different boundary: after the compositional core is resolved, retain expendable outer image area when later production may need to fit the work into several legitimate formats.
