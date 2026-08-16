---
object_id: PAT_synthesize_visual_concepts_from_diverse_source_types
object_type: pattern
name: Synthesize Visual Concepts from Diverse Source Types
library_path:
- art
- drawing
- foundations
- ideation
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- ideation
- reference
- synthesis
- research
- memory
- concept_design
cross_links:
- rel: related_to
  target_object_id: PAT_generate_novel_options_by_combining_distant_concepts
- rel: related_to
  target_object_id: AP_alternate_search_and_control_cycles
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants:
- variant_id: VAR_dodson_use_photography_as_bounded_study_or_creative_departure
  variant_name: Use Photography as Bounded Study or Creative Departure
  variant_basis: constraint
  difference_from_foundation: Uses a photograph either to study a specific visual relationship or as material to transform and combine, rather than allowing one photograph to become the automatic final answer.
  when_to_use: Use when photography captures inaccessible, fleeting, complex, or reference-rich information that can support observation or ideation.
  when_not_to_use: Do not let tracing, one-photo dependence, or mismatched camera/light information replace construction and drawing judgment when the task requires independent adaptation.
  absorbed_from_object_id: none
- variant_id: VAR_use_memcaps_as_accumulated_project_experience_source
  variant_name: Use Memcaps as Accumulated Project Experience Source
  variant_basis: context
  difference_from_foundation: Adapts Dodson's personal-experience source route to AI systems that possess durable, provenance-bearing project memory. Prior teachings, corrections, failures, successful outcomes, and judgments preserved in memcaps can be retrieved as learned project experience rather than fabricated as lived human experience.
  when_to_use: Use when a relevant memcap or other durable project-memory record actually exists and can supply prior lessons, failure modes, corrections, or successful precedents for the current visual problem.
  when_not_to_use: Do not invent memories, personal history, emotions, or prior lessons that are absent from the record; without a memcap, use current sources and user-provided context instead.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_normalize_reference_camera_and_light_before_synthesis
  variant_name: Normalize Reference Camera and Light Before Synthesis
  variant_basis: method_sequence
  difference_from_foundation: Treats photographs, clippings, studies, or underlays as information to be rebuilt into one chosen viewpoint and one lighting logic instead of accepting each source's camera and illumination unchanged.
  when_to_use: Use when combining multiple visual references whose eye levels, perspective, scale cues, or light sources may conflict.
  when_not_to_use: Do not spend time normalizing a single authoritative reference when the task is direct observation or faithful study of that one setup.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_triangulate_portrait_identity_across_multiple_references
  variant_name: Triangulate Portrait Identity Across Multiple References
  variant_basis: method_sequence
  difference_from_foundation: Uses several imperfect portrait references to infer the recurring structural identity of one subject before rebuilding that identity through a single chosen head construction, camera, and lighting system.
  when_to_use: Use when no single photograph cleanly reveals a person's stable character forms, especially when references vary in expression, camera, age, or lighting.
  when_not_to_use: Do not average away genuine asymmetry, age-specific traits, or distinctive forms merely because they vary across sources; and do not multiply references when one authoritative setup already supplies the required likeness.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_use_applied_realism_to_fortify_invention
  variant_name: Use Applied Realism to Fortify Invention
  variant_basis: method_sequence
  difference_from_foundation: Starts from an invented or stylized creative proposition and recruits only the real-world structural, material, lighting, environmental, or behavioral evidence needed to make that proposition convincing, rather than treating reference fidelity as the goal.
  when_to_use: Use when imaginative, stylized, fictional, caricatured, or abstract subject matter needs factual credibility without surrendering the intended design.
  when_not_to_use: Do not use selective omission as an excuse for accidental anatomy, perspective, material, or lighting errors; and do not suppress relevant evidence when the task is faithful observation, documentation, or technical study.
  absorbed_from_object_id: none
---

# Synthesize Visual Concepts from Diverse Source Types

## Pattern Rule
**IF** one reference family is too narrow to solve the visual problem or the design needs a richer internal logic
**THEN** extract useful relationships, forms, mechanisms, moods, symbols, or mark behaviors from several source types and recombine them into the active drawing
**ELSE** keep the source set narrow when one authoritative reference already contains the information the task requires.

## Do
- Define what information is missing before collecting sources.
- Use different source families for different jobs: observation for appearance, anatomy for structure, motion reference for action, historical/art sources for visual language, literature or music for mood and conceptual cues, objects for mechanisms or materials, and user-provided experience for narrative specificity.
- Extract transferable attributes instead of copying whole source images into one collage.
- Reconstruct the result through the active drawing foundations so borrowed parts behave as one design.
- Track provenance for source-specific claims and for memory-derived lessons.
- Recheck the synthesized result as a whole; more references do not automatically create a coherent design.

## Don't
- Ask one reference to solve structure, mood, costume, anatomy, lighting, and style when it only supports one of those jobs.
- Accumulate references without deciding what each contributes.
- Paste donor parts together without reconciling scale, perspective, mechanics, material, or action.
- Claim AI lived experience. Use preserved project memory only when it exists and is attributable.

## Checklist
- Each major source has a defined contribution.
- The final concept is reconstructed rather than merely collaged.
- Conflicting source information has been resolved intentionally.
- Memory-derived lessons can be traced to an actual durable record.
- The result has one coherent visual and mechanical logic.

## Notes
Dodson explicitly draws from visual and nonvisual sources and treats photography as either study material or a point of creative departure. Guided teaching adds a critical AI boundary: a human artist can draw from lived memory; an AI can only use durable prior experience when it has actually been preserved. Dynamic Figure Drawing memcaps demonstrate the useful form of that experience: they retain teaching corrections, failure patterns, and successful interpretations that can later inform a new problem without pretending the AI lived the original event.

`VAR_dodson_use_photography_as_bounded_study_or_creative_departure` keeps photography either a focused observation source or a transformable ideation source rather than the automatic endpoint.

`VAR_use_memcaps_as_accumulated_project_experience_source` permits prior project experience only when durable memory actually exists and its provenance can be checked.

`VAR_loomis_normalize_reference_camera_and_light_before_synthesis` adds a reconstruction pass for mixed visual references: choose the target viewpoint and lighting logic first, then rebuild useful information from each source so conflicting eye levels and illumination do not survive into the final scene.

`VAR_loomis_triangulate_portrait_identity_across_multiple_references` adds a likeness-specific synthesis pass: collect several views, identify recurring skull/face proportions and feature spacing that persist across source accidents, separate those stable traits from expression/camera/light artifacts, then rebuild the subject through one coherent target construction. This differs from the u01 normalization variant because the thing being reconciled is subject identity rather than camera and illumination.


`VAR_loomis_use_applied_realism_to_fortify_invention` adds Loomis's closing **applied realism** workflow: begin with the creative proposition, identify which facts must be true for it to convince, gather only the evidence needed for those jobs, reconstruct that evidence through the invented design, and subordinate literal information that does not strengthen the idea. It is a credibility pass for invention, not a demand that imaginative work become literal realism.

This is especially important for future creature and character design. A hybrid organism can draw structural evidence from several donor anatomies, motion evidence from another source, and narrative/design cues from still others, but shared construction and FORCE foundations must reconcile those inputs into one functioning body.
