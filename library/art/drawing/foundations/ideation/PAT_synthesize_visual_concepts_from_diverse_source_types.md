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
  difference_from_foundation: Uses a photograph either to study a specific visual relationship or as material to transform
    and combine, rather than allowing one photograph to become the automatic final answer.
  when_to_use: Use when photography captures inaccessible, fleeting, complex, or reference-rich information that can support
    observation or ideation.
  when_not_to_use: Do not let tracing, one-photo dependence, or mismatched camera/light information replace construction and
    drawing judgment when the task requires independent adaptation.
  absorbed_from_object_id: none
- variant_id: VAR_use_memcaps_as_accumulated_project_experience_source
  variant_name: Use Memcaps as Accumulated Project Experience Source
  variant_basis: context
  difference_from_foundation: Adapts Dodson's personal-experience source route to AI systems that possess durable, provenance-bearing
    project memory. Prior teachings, corrections, failures, successful outcomes, and judgments preserved in memcaps can be
    retrieved as learned project experience rather than fabricated as lived human experience.
  when_to_use: Use when a relevant memcap or other durable project-memory record actually exists and can supply prior lessons,
    failure modes, corrections, or successful precedents for the current visual problem.
  when_not_to_use: Do not invent memories, personal history, emotions, or prior lessons that are absent from the record; without
    a memcap, use current sources and user-provided context instead.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_normalize_reference_camera_and_light_before_synthesis
  variant_name: Normalize Reference Camera and Light Before Synthesis
  variant_basis: method_sequence
  difference_from_foundation: Establishes the target viewpoint, eye level, value arrangement, and lighting logic before synthesis;
    when reference acquisition is controllable, captures new material to match that target upstream, then rebuilds any remaining
    mixed photographs, clippings, studies, or underlays into the same camera and illumination system.
  when_to_use: Use when combining multiple visual references whose eye levels, perspective, scale cues, value structures,
    or light sources may conflict, especially when some reference can be staged or photographed specifically for the designed
    rough.
  when_not_to_use: Do not spend time normalizing a single authoritative reference when the task is direct observation or faithful
    study of that one setup.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_triangulate_portrait_identity_across_multiple_references
  variant_name: Triangulate Portrait Identity Across Multiple References
  variant_basis: method_sequence
  difference_from_foundation: Uses several imperfect portrait references to infer the recurring structural identity of one
    subject before rebuilding that identity through a single chosen head construction, camera, and lighting system.
  when_to_use: Use when no single photograph cleanly reveals a person's stable character forms, especially when references
    vary in expression, camera, age, or lighting.
  when_not_to_use: Do not average away genuine asymmetry, age-specific traits, or distinctive forms merely because they vary
    across sources; and do not multiply references when one authoritative setup already supplies the required likeness.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_design_action_before_acquiring_pose_reference
  variant_name: Design Action Before Acquiring Pose Reference
  variant_basis: method_sequence
  difference_from_foundation: Designs the intended action, interaction, and broad pose first with cheap gesture or skeleton
    sketches, then acquires model or photographic reference to make that chosen conception convincing instead of letting available
    reference originate the composition.
  when_to_use: Use when a narrative pose, multi-figure interaction, or dramatic action must serve a preselected story beat
    and camera rather than whatever pose happens to be easiest to photograph.
  when_not_to_use: Do not ignore useful accidental discoveries from a model session, and do not predesign away the observational
    task when the assignment is direct life study; the rule is to keep reference subordinate to an intentional conception
    when illustration is being staged.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_use_applied_realism_to_fortify_invention
  variant_name: Use Applied Realism to Fortify Invention
  variant_basis: method_sequence
  difference_from_foundation: 'Connects invention and factual study in either direction: start from an invented or stylized
    proposition and research only the missing facts needed to make it convincing, or study real structure/behavior first,
    internalize the useful facts, and later recombine them freely in invention rather than treating reference fidelity as
    the goal.'
  when_to_use: Use when imaginative, stylized, fictional, caricatured, or abstract subject matter needs factual credibility
    without surrendering the intended design, or when deliberate study is being banked for later imaginative use.
  when_not_to_use: Do not use selective omission as an excuse for accidental anatomy, perspective, material, or lighting errors;
    and do not suppress relevant evidence when the task is faithful observation, documentation, or technical study.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_mine_precedent_for_general_problem_then_redesign_solution
  variant_name: Mine Precedent for the General Problem, Then Redesign the Solution
  variant_basis: method_sequence
  difference_from_foundation: Uses an earlier image to identify a broad recurring problem, relationship, audience appeal,
    or subject situation while deliberately discarding the donor image's specific composition and pictorial solution before
    rebuilding from the current brief.
  when_to_use: Use when precedent is valuable as an idea stimulus but the current work needs an original construction rather
    than a close visual paraphrase.
  when_not_to_use: Do not treat this as permission to reproduce protected or distinctive expression; actual reuse still follows
    the applicable rights and permissions context.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_translate_photo_reference_through_drawn_study_before_final
  variant_name: Translate Photo Reference Through a Drawn Study Before Final
  variant_basis: method_sequence
  difference_from_foundation: Inserts an interpretive drawing between photographic evidence and final execution so the artist
    selects, simplifies, and restates useful information before the polished photograph can become the aesthetic target.
  when_to_use: Use when a highly finished photograph is beginning to dictate slickness, literal detail, or surface treatment
    beyond the limited facts the final illustration actually needs.
  when_not_to_use: Do not add an intermediate study mechanically when the photograph is already being used narrowly and the
    extra pass would not improve selection or interpretation.
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

`VAR_loomis_normalize_reference_camera_and_light_before_synthesis` adds both an upstream acquisition strategy and a reconstruction pass: establish the target rough, viewpoint, eye level, value structure, and lighting logic first; when you control the shoot, stage new reference to match those decisions before capture; then rebuild useful information from any remaining mixed sources so conflicting camera and illumination do not survive into the final scene.

`VAR_loomis_triangulate_portrait_identity_across_multiple_references` adds a likeness-specific synthesis pass: collect several views, identify recurring skull/face proportions and feature spacing that persist across source accidents, separate those stable traits from expression/camera/light artifacts, then rebuild the subject through one coherent target construction. This differs from the u01 normalization variant because the thing being reconciled is subject identity rather than camera and illumination.



`VAR_loomis_design_action_before_acquiring_pose_reference` adds Loomis's story-staging sequence: invent the action in tiny cheap drawings, settle the interaction and broad pose, then direct or collect reference around that conception. The model or camera supplies convincing facts to a designed scene; it does not become the automatic author of the scene.

`VAR_loomis_use_applied_realism_to_fortify_invention` preserves both directions of Loomis's applied-realism logic. One route is **conception → identify missing facts → research → rebuild**, where an invented proposition recruits only the evidence needed to convince. The other is **study fact → internalize structure or behavior → invent from understanding**, where observation becomes reusable knowledge rather than a picture to copy. Both routes treat realism as support for invention, not a demand that imaginative work become literal.

This is especially important for future creature and character design. A hybrid organism can draw structural evidence from several donor anatomies, motion evidence from another source, and narrative/design cues from still others, but shared construction and FORCE foundations must reconcile those inputs into one functioning body.

`VAR_loomis_mine_precedent_for_general_problem_then_redesign_solution` separates the reusable problem from a donor image's particular answer. Extract the broad situation, relationship, or appeal that made the precedent useful, discard its specific composition, and rebuild the new concept from the present assignment and design logic.

`VAR_loomis_translate_photo_reference_through_drawn_study_before_final` adds a translation buffer: photograph -> interpretive study -> final. The study becomes the immediate authority for selection and design, while the photograph remains evidence instead of silently setting the final work's finish and surface language.
