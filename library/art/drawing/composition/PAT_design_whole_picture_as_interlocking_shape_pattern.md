---
object_id: PAT_design_whole_picture_as_interlocking_shape_pattern
object_type: pattern
name: Design the Whole Picture as an Interlocking Shape Pattern
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
- figure_ground
- shape_design
- value_pattern
- unity
cross_links:
- rel: related_to
  target_object_id: PAT_map_observed_subject_as_interlocking_positive_and_negative_shapes
- rel: related_to
  target_object_id: PAT_repeat_with_variation_to_balance_coherence_and_interest
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants:
- variant_id: VAR_dodson_merge_same_value_shapes_across_object_boundaries
  variant_name: Merge Same-Value Shapes Across Object Boundaries
  variant_basis: emphasis
  difference_from_foundation: Allows nearby light, midtone, or dark regions to join into a larger compositional shape even when they belong to different objects, local values, or shadow types, so the whole design can gain unity at the cost of some local separation.
  when_to_use: Use when several adjacent regions are close enough in value that tying them together strengthens the larger pattern, silhouette, or focal organization.
  when_not_to_use: Do not merge across boundaries that must remain clear for the subject to read, for technical description, or for a material/light relationship the viewer needs to understand.
  absorbed_from_object_id: none
- variant_id: VAR_dodson_reduce_scene_to_nonobject_shape_language
  variant_name: Reduce the Scene to Non-Object Shape Language
  variant_basis: method_sequence
  difference_from_foundation: Temporarily suppresses object labels by squinting and summarizing the view as a few large value/shape masses, then returns to the subject once the whole pattern is visible.
  when_to_use: Use when named-object thinking or local detail is preventing the artist from judging the overall figure-ground and value pattern.
  when_not_to_use: Do not remain so abstract that required identity, structure, or narrative information is lost; this is a way to reveal the whole, not a replacement for the subject.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_generate_composition_from_informal_subdivision_armature
  variant_name: Generate Composition from an Informal Subdivision Armature
  variant_basis: method_sequence
  difference_from_foundation: "Loomis turns whole-picture shape design into a generative start procedure: divide the format unequally, cross it with a major diagonal, extend horizontals or perpendiculars through selected intersections, recursively subdivide chosen spaces, and let the resulting abstract armature suggest placements, contours, spacing, or even subject ideas. The scaffold is temporary and should disappear once the picture organizes itself."
  when_to_use: "Use at Stage 0 when the blank frame is producing generic placement, when subject elements will not lock into one picture, or when an abstract structural prompt could generate less habitual arrangements."
  when_not_to_use: "Do not preserve the construction grid mechanically, treat Loomis's preferred unequal divisions as universal laws, or force a subject to obey an armature after the actual picture demands a better relationship. The scaffold is a search device, not a correctness formula."
  absorbed_from_object_id: none
- variant_id: VAR_loomis_generate_subject_arrangement_from_abstract_mass_pattern
  variant_name: Generate Subject Arrangement from an Abstract Mass Pattern
  variant_basis: method_sequence
  difference_from_foundation: Begins with an abstract arrangement of major light, middle, and dark masses before the literal subject placement is fixed, then lets those masses suggest figure placement, garments, shadows, windows, accessories, grouping, or lighting relationships that can be translated into a coherent scene.
  when_to_use: Use when object-first staging keeps producing predictable arrangements, when a story scene lacks a strong large-scale value design, or when an abstract mass proposition could generate less habitual subject placement.
  when_not_to_use: Do not force essential anatomy, perspective, narrative facts, or spatial logic to obey an arbitrary blot pattern after the actual scene demands correction; the mass pattern is a generative scaffold, not a correctness law.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_build_tonal_plan_around_one_dominant_value_family
  variant_name: Build a Tonal Plan Around One Dominant Value Family
  variant_basis: emphasis
  difference_from_foundation: "Adds Loomis's tonal-pattern emphasis to whole-picture shape design: simplify the scene into a few broad value families, identify or choose the family that will occupy the greatest area, then organize the remaining values as subordinate and accent masses against that dominant field before restoring modeling and detail."
  when_to_use: "Use when a picture contains many scattered value patches, when a broad sky/floor/interior/shadow field could unify the design, or when thumbnail planning needs a simple tonal statement that survives at small size."
  when_not_to_use: "Do not force every picture into one overwhelmingly dominant family when the intended design depends on a more even, mosaic, or deliberately fragmented distribution. Loomis's named tonal plans are planning aids, not universal laws."
  absorbed_from_object_id: none
---

# Design the Whole Picture as an Interlocking Shape Pattern

## Pattern Rule
**IF** a drawing is being designed as a composition rather than merely assembled object by object
**THEN** judge subject, background, positive/negative space, and light/dark regions as one interlocking pattern whose shared boundaries and larger masses must work together
**ELSE** preserve straightforward descriptive separation when the task prioritizes neutral observation, diagrammatic clarity, or technical explanation over compositional integration

## Do
- Reduce the picture to its largest positive, negative, light, dark, and middle-value masses before polishing local passages.
- Judge boundaries twice: once for what they describe locally and again for what shape relationship they create in the whole sheet.
- Let subject and background solve one another instead of treating the background as leftover space.
- Merge compatible value regions when a larger connected shape gives the picture more unity or directional clarity.
- Return from abstract pattern to structural and descriptive information before necessary identity disappears.

## Don't
- Finish one object beautifully while ignoring the shape problems it creates around the rest of the frame.
- Assume every object boundary needs equal contrast or explicit separation.
- Confuse observational positive/negative checking with composition: the same shared boundaries can verify accuracy in observation and be deliberately redesigned in composition.
- Merge shapes only because they are close in value if the lost boundary carries essential spatial, anatomical, or narrative information.

## Checklist
- The subject and ground read as one organized picture rather than independent cutouts.
- Large value/shape groups remain intelligible at thumbnail size or through squinting.
- Shared boundaries help both local description and the whole composition.
- Any merged boundary is intentional and does not destroy information the image needs.

## Notes
Dodson's Chapter 7 shifts positive/negative shape from an observational checking device into a whole-picture design principle. The existing observation foundation remains the owner of using shared positive/negative boundaries to verify what was seen; this Pattern owns how those same kinds of boundaries are organized deliberately across the final picture.

`VAR_dodson_merge_same_value_shapes_across_object_boundaries` carries forward the same-value merging introduced in the light chapter and gives it its full composition rationale: value groups may cross object and shadow categories when the larger design benefits.

`VAR_dodson_reduce_scene_to_nonobject_shape_language` is a temporary abstraction route for seeing the pattern without being trapped by object names. It should lead back to the subject, not erase the subject.

`VAR_loomis_generate_composition_from_informal_subdivision_armature` adds a Stage 0 generative route: build a disposable unequal line scaffold, let its intersections and spaces suggest the arrangement, then erase the scaffold once the subject and picture relationships can stand on their own. Loomis's particular anti-equality rules are retained as variation prompts rather than universal composition laws.


`VAR_loomis_generate_subject_arrangement_from_abstract_mass_pattern` reverses the usual object-to-pattern sequence: establish a compelling abstract mass arrangement first, then discover which subject elements can inhabit those masses without losing story or structure. It is generative abstraction, unlike `VAR_dodson_reduce_scene_to_nonobject_shape_language`, which abstracts an already observed or conceived scene to reveal its existing whole-picture pattern.

`VAR_loomis_build_tonal_plan_around_one_dominant_value_family` adds a tonal-design branch: choose a dominant broad value family, organize subordinate and accent masses against it, and restore local modeling only after the large tonal pattern holds together.
