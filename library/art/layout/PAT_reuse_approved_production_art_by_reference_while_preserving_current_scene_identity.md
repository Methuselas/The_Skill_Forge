---
object_id: PAT_reuse_approved_production_art_by_reference_while_preserving_current_scene_identity
object_type: pattern
name: Reuse Approved Production Art By Reference While Preserving Current Scene Identity
library_path:
- art
- layout
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- layout
- animation
- reuse
- provenance
- production
- assets
cross_links:
- rel: related_to
  target_object_id: AP_package_approved_layout_into_executable_scene_plan
- rel: related_to
  target_object_id: PAT_decompose_animation_scene_into_registered_level_stack_for_independent_control
reference:
  source_title: The Art of Layout and Storyboarding
  author: Mark T. Byrne
confidence: high
references: []
variants: []
---

# Reuse Approved Production Art By Reference While Preserving Current Scene Identity

## Pattern Rule
**IF** an approved background, overlay, cycle, expression set, pose, or other expensive production asset already satisfies the current scene's need
**THEN** reuse it by explicit reference, copy, or instance while preserving both the asset's provenance and the current scene's own identity and bookkeeping.

## Do
- Search for approved compatible material before rebuilding expensive art from scratch.
- Reuse the authoritative asset itself or a controlled derivative rather than recreating it by eye.
- Record where the reused material came from so another artist can trace its source and approval state.
- Keep the current scene/sequence identity on the current package even when the underlying asset originated elsewhere.
- Preserve the source asset's spatial, style, and production constraints unless the current shot explicitly requires an approved adaptation.
- Prefer copies, instances, links, or reference systems that let production find the asset without hunting for one physical original.

## Don't
- Do not silently relabel an old asset as if it were newly authored for the current scene.
- Do not let the source scene's numbering replace the current scene's identity.
- Do not reuse material merely because it exists when it conflicts with camera, geography, style, action, or production requirements.
- Do not make downstream artists search manually for an undocumented original.

## Checklist
- The reused asset is genuinely compatible with the current shot.
- Its source and approval provenance are recoverable.
- The current scene retains its own identity and notes.
- Reuse saves work without introducing continuity or spatial errors.
- A downstream artist can retrieve the correct asset without guesswork.

## Notes
Byrne's stock-art system is physical and studio-specific, but the underlying rule remains current: reuse authoritative production assets while separating source provenance from current-scene ownership and numbering.
