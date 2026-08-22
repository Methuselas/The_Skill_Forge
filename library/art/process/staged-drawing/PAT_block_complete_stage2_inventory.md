---
object_id: PAT_block_complete_stage2_inventory
object_type: pattern
name: Block the Complete Stage 2 Inventory
library_path:
- art
- process
- staged-drawing
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: AP_draw_a_figure_through_onion_skinned_stages
tags:
- stage_2
- blocking
- complete_inventory
- minimum_mass
- no_rendering
cross_links:
- rel: supports
  target_object_id: AP_build_stage2_complete_mass_block
- rel: related_to
  target_object_id: PAT_build_gesture_into_clear_masses
- rel: related_to
  target_object_id: AP_notate_a_figure_in_structural_order
- rel: prerequisite_for
  target_object_id: PAT_commit_stage3_form_realization
reference:
  source_title: Guided Stage 1–3 Artist Discretion, Mass Completion, and Commitment Review
  author: MaDin + GPT
confidence: high
references:
- image_path: library/art/process/staged-drawing/assets/precedent_stage2_observatory_complete_mass_block.png
  caption: 'Approved Stage 2 observatory block-in: every intended Stage 3 subject is present at minimum solid form, the Stage
    1 layout remains intact, and the drawing avoids lighting, texture, and decorative rendering.'
  derived_from: guided observatory Stage 2 review and human approval
  origin: first_party_source
  review: passed
variants: []
---

# Block the Complete Stage 2 Inventory

## Pattern Rule
**IF** an approved Stage 1 plan is entering Stage 2
**THEN** expand its anchors into the minimum connected solid masses needed to contain every subject, object, effect, and structural feature intended for Stage 3 while preserving the approved Stage 0 picture proposition and Stage 1 construction
**ELSE** do not invent missing Stage 3 content later and call it refinement

## Do
- Treat Stage 2 as the building phase. Convert Stage 1 notation into connected volume without redesigning the composition.
- In visible staged mode, carry both anchors: `ROOT = approved Stage 0` and `IMMEDIATE = approved Stage 1`. Label new attempts `S2-r1`, `S2-r2`, and so on.
- Include every major element that must exist in Stage 3 at its minimum block level. A later figure, building, vehicle, effect, prop, attachment, support, or major design feature needs a Stage 2 mass or structural placeholder.
- Build figures in **Torso → Legs → Arms → Head** order unless a justified support-specific exception applies.
- Expand environmental notation directly: boxes gain thickness, circles become spheres, rectangles become tubes/cabinets, tripod lines gain support volume, cylinders gain overlap and end orientation.
- Preserve Stage 1 centers, axes, proportions, contacts, horizon, perspective relationships, overlap order, and negative spaces, and preserve Stage 0 camera, crop, major subject scale/placement, hierarchy, and composition.
- Use draw-through, cross-contours, taper, joint interlock, overlap, foreshortening, and support to make the masses readable.
- Use only minimal tone when line alone cannot explain overlap, turning plane, contact, or difficult depth. Treat that tone as structural notation, not illumination.
- Allow optional 2A primary-mass and 2B correction passes when useful, but do not turn them into mandatory public gates unless requested.

## Don't
- Do not add a Stage 3 element for the first time after Stage 2 has been approved.
- Do not migrate, multiply, replace, rescale, or repurpose approved major subjects while giving them volume.
- Do not add anatomy, facial identity, costume folds, hair rendering, materials, texture, dramatic lighting, cast shadows, atmosphere, decorative hatching, or polished surface design.
- Do not repair a Stage 0 composition/scale/placement failure or Stage 1 pose/proportion/perspective failure silently. Return to the owning approved stage and rebuild.

## Checklist
- Every intended Stage 3 major element already exists as a readable Stage 2 mass or structural block.
- The Stage 1 plan can be recovered by reducing masses to anchors and primitives.
- Camera, crop, subject scale/placement, perspective, overlaps, hierarchy, and negative spaces remain consistent with the approved lineage visible in the conversation.
- Shading is absent except for a necessary structural accent.
- Stage 3 can begin without inventing, relocating, or rescaling a major block.
- The result reads more like complete minimum mass than like a grayscale illustration.

## Notes
Stage 1 says how the approved picture is constructed. Stage 2 states what solid forms exist there. Stage 3 decides what those forms specifically become.

The governing rule is: **if it will be a major Stage 3 element, it must already exist in Stage 2 at the minimum block level.**
