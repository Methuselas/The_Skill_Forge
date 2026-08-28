---
object_id: PAT_register_character_occlusion_with_shared_matchline_or_overlay
object_type: pattern
name: Register Character Occlusion With Shared Matchline Or Overlay
library_path:
- art
- layout
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
- layout
- animation
- occlusion
- matchline
- overlay
- registration
cross_links:
- rel: related_to
  target_object_id: PAT_pose_out_approved_storyboard_action_into_layout_without_reauthoring_scene
- rel: related_to
  target_object_id: PAT_protect_critical_content_from_physical_production_boundaries
reference:
  source_title: The Art of Layout and Storyboarding
  author: Mark T. Byrne
confidence: high
references: []
variants: []
---

# Register Character Occlusion With Shared Matchline Or Overlay

## Pattern Rule
**IF** separately produced character or effects artwork must pass behind a background prop or environmental element
**THEN** establish one shared occlusion boundary, or separate the covering element as an overlay, so every department resolves the hide/reveal edge against the same geometry.

## Do
- Mark the exact boundary where the moving artwork becomes hidden when Background and Animation must meet on the same edge.
- Use the same registered boundary in layout, cleanup/animation, effects, and background production so the composite does not jiggle along the occlusion edge.
- Use an overlay when separating the covering object is cleaner or more reusable than tracing the same boundary into every moving drawing.
- Keep the boundary tied to the layout's perspective and final prop geometry.
- Omit hidden drawing detail below the boundary when it serves no downstream need.
- Label or otherwise identify the boundary clearly enough that another department can find and use it without inference.

## Don't
- Do not let each department independently guess where the character disappears behind the prop.
- Do not place a match boundary on an approximate or still-changing prop edge.
- Do not spend production time finishing fully hidden areas unless another requirement needs them.
- Do not preserve historical red-pencil symbols or letter codes as if they were the essential rule; preserve the shared-registration operation.

## Checklist
- All participating layers use the same occlusion edge.
- The edge is defined from final-enough layout geometry.
- The moving subject disappears and reappears without visible edge jitter.
- An overlay is used when it simplifies the handoff or reuse.
- Hidden work is not developed beyond what production actually needs.

## Notes
Byrne describes traditional match or registration lines marked on the layout and traced by downstream artists, with overlays as an alternative. The durable production principle is one shared occlusion boundary across separately produced layers.
