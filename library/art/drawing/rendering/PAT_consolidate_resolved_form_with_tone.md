---
object_id: PAT_consolidate_resolved_form_with_tone
object_type: pattern
name: Consolidate Resolved Form With Tone
library_path:
- art
- drawing
- rendering
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- tone
- value
- light_shadow
- form_unity
cross_links:
- rel: related_to
  target_object_id: AP_prepare_construction_for_rendering
- rel: related_to
  target_object_id: PAT_concentrate_contrast_and_accents_at_focal_area
reference:
  source_id: bert_dodson_keys_to_drawing
  source_title: Keys to Drawing
  author: Bert Dodson
  publish_date: 1985
  media_type: PDF
  locator: u04, physical pp. 103-128
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_dodson_map_light_and_shadow_before_modeling
  variant_name: Map Light and Shadow Before Modeling
  variant_basis: method_sequence
  source_id: bert_dodson_keys_to_drawing
  source_title: Keys to Drawing
  locator: u04, physical pp. 103-107
  difference_from_foundation: Dodson starts by reducing the subject to decisive light
    and dark territories, even temporarily imposing a clear border across ambiguous
    transitions, then models and softens those boundaries only after the large value
    pattern reads.
  when_to_use: Use when subtle local shading is fragmenting the picture or making
    it difficult to judge the large light/shadow organization.
  when_not_to_use: Do not freeze the first map into a rigid formula; actual surface
    turning, local value, light quality, and later edge decisions can soften or revise
    the initial division.
  absorbed_from_object_id: none
- variant_id: VAR_hogarth_fuse_resolved_figure_as_one_tonal_mass
  variant_name: Fuse a Resolved Figure as One Tonal Mass
  variant_basis: emphasis
  source_id: burne_hogarth_dynamic_figure_drawing_ocr
  source_title: Dynamic Figure Drawing
  locator: ch03, printed pp. 99-104
  difference_from_foundation: Preserves Hogarth's figure-specific use of continuous
    tone gradation to reunify overlap-separated body parts after their construction
    is already solved, allowing selected contour boundaries to soften or disappear
    while the figure remains one mass.
  when_to_use: Use on a structurally resolved figure whose overlapping parts read
    as disconnected pieces and can be fused by a coherent tonal mass.
  when_not_to_use: Do not use tone to conceal unresolved anatomy, attachment, or contradictory
    overlaps; in finished physical lighting, the chosen light still governs the value
    pattern.
  absorbed_from_object_id: PAT_consolidate_resolved_form_with_tone
- variant_id: VAR_use_physical_light_and_material_response
  variant_name: Use Physical Light and Material Response for Final Rendering
  variant_basis: method_sequence
  source_id: robert_w_gill_basic_rendering
  source_title: Basic Rendering
  locator: selected lighting/material chapters
  difference_from_foundation: Keeps sculptural tone for form study but makes final
    rendering respect chosen light/shadow geometry first, with material, reflected
    light, transparency, and texture applied afterward.
  when_to_use: Use when moving from structural tone study into physically motivated
    scene rendering.
  when_not_to_use: Do not preserve an attractive tonal grouping if it contradicts
    the intentionally chosen scene light unless the result is explicitly a study.
  absorbed_from_object_id: none
- variant_id: VAR_hampton_match_value_edge_timing_to_plane_change
  variant_name: Match Value and Edge Timing to the Rate of Plane Change
  variant_basis: method_sequence
  source_id: michael_hampton_figure_drawing_design_and_invention
  source_title: 'Figure Drawing: Design and Invention'
  locator: u09, printed pp. 232-234
  difference_from_foundation: 'Adds Hampton''s form-to-value translation: classify
    a surface turn by the speed of its plane change—slow like a sphere, quicker like
    a cylinder, abrupt like a box—and let value transition and edge softness/hardness
    reflect that rate.'
  when_to_use: Use after line, planes, and major volumes are resolved and light/shadow
    must clarify the same surfaces.
  when_not_to_use: Do not invent value changes that contradict the chosen light or
    established form.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_keep_cloth_modeling_inside_material_value_family
  variant_name: Keep Cloth Modeling Inside the Material Value Family
  variant_basis: emphasis
  source_id: andrew_loomis_figure_drawing_for_all_its_worth
  source_title: Figure Drawing for All It's Worth
  locator: u12, printed pp. 189-194
  difference_from_foundation: 'Adds Loomis''s garment-value restraint to resolved-form
    tone: model folds and planes strongly enough to describe structure, but keep light
    and dark changes subordinate to the garment''s local material/color value so cloth
    does not fragment into unrelated high-contrast patches.'
  when_to_use: Use when drapery is structurally correct but overmodeling breaks the
    garment into noisy isolated lights and shadows.
  when_not_to_use: Do not flatten legitimate strong cast shadows or material-specific
    contrast when the actual lighting requires them; the rule is about preserving
    material unity, not suppressing physical illumination.
  absorbed_from_object_id: none
- variant_id: VAR_vilppu_model_form_with_viewer_facing_tone_before_direct_light
  variant_name: Model Form With Viewer-Facing Tone Before Direct Light
  variant_basis: method_sequence
  source_id: glenn_vilppu_basic_figure_drawing
  source_title: 'Drawing Manual: Basic Figure Drawing'
  locator: u10, physical pp. 137-147
  difference_from_foundation: 'Adds Vilppu''s analytic modeling-tone study mode to
    resolved-form tone: temporarily treat the viewer as the light source, keep planes
    facing the viewer light, darken surfaces as they turn away, soften receding contours,
    and use value to push sides back so the volume can be studied independently of
    a literal scene light.'
  when_to_use: Use as a form-study or diagnostic when line construction is understood
    but the artist needs to test whether value alone can explain the orientation and
    turning of simple or anatomical masses.
  when_not_to_use: Do not mistake this viewer-centered modeling tone for physical
    illumination in a finished scene; once a direct light is specified, actual light
    geometry and material response govern.
  absorbed_from_object_id: none
- variant_id: VAR_vilppu_separate_core_and_cast_shadow_by_cause
  variant_name: Separate Core and Cast Shadow by Cause
  variant_basis: method_sequence
  source_id: glenn_vilppu_basic_figure_drawing
  source_title: 'Drawing Manual: Basic Figure Drawing'
  locator: u11, physical pp. 149-155
  difference_from_foundation: 'Adds Vilppu''s compact diagnostic to physical lighting:
    identify core shadow as a form-turning event between direct and reflected light,
    and cast shadow as light blocked by another form. Let the core edge inherit the
    sharpness of the surface turn, while the cast-shadow edge is sharpest near the
    occluder and softens with separation.'
  when_to_use: Use when a tonal drawing has plausible dark shapes but the shadow edges
    do not explain whether the form is turning or another object is blocking the light.
  when_not_to_use: Do not force every core or cast edge into one fixed softness; actual
    source size, geometry, material, reflected light, and scene conditions still govern.
  absorbed_from_object_id: none
- variant_id: VAR_vilppu_use_atmospheric_contrast_as_local_depth_design
  variant_name: Use Atmospheric Contrast as Local Depth Design
  variant_basis: emphasis
  source_id: glenn_vilppu_basic_figure_drawing
  source_title: 'Drawing Manual: Basic Figure Drawing'
  locator: u12, physical pp. 161-165
  difference_from_foundation: 'Adds Vilppu''s figurative use of atmospheric perspective
    as a controlled design device: reduce contrast, detail, and edge clarity on receding
    or subordinate passages—even across relatively small depth changes—while keeping
    nearer or action-critical forms sharper, so overlapping masses separate and the
    main action reads more strongly.'
  when_to_use: Use when a figure's near/far organization is technically correct but
    visually crowded, or when atmospheric edge/value control can strengthen the action
    without changing the underlying construction.
  when_not_to_use: Do not apply arbitrary haze that contradicts the intended scene,
    material, lighting, or focal hierarchy; when physical atmospheric perspective
    matters, actual distance and medium conditions still govern.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_model_head_as_single_light_plane_value_study
  variant_name: Model the Head as a Single-Light Plane Value Study
  variant_basis: method_sequence
  source_id: andrew_loomis_drawing_the_head_and_hands
  source_title: Drawing the Head and Hands
  locator: u03, physical pp. 57-61
  difference_from_foundation: 'Adds Loomis''s head-specific analytic tone sequence:
    start from an already constructed plane head, use one strong light, simplify the
    result into broad light/halftone/form-shadow/cast-shadow shapes, keep the underlying
    plane readable as edges soften, and postpone wrinkles or fine surface detail until
    the plane/value statement works.'
  when_to_use: Use when learning or diagnosing head tone and complex lighting is making
    it difficult to tell whether the planes themselves are understood.
  when_not_to_use: Do not turn the one-light study setup into a universal final-lighting
    rule, and do not preserve teaching-block facets when the observed head turns more
    softly.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_turn_planes_with_stroke_direction_before_value_change
  variant_name: Turn Planes With Stroke Direction Before Increasing Value Contrast
  variant_basis: emphasis
  source_id: andrew_loomis_drawing_the_head_and_hands
  source_title: Drawing the Head and Hands
  locator: u03, physical pp. 57 and 61
  difference_from_foundation: 'Adds Loomis''s mark-direction alternative for line-dominant
    modeling: let pencil, pen, or hatch strokes follow the facing direction of a plane,
    and change their direction as the plane turns so solidity can increase without
    requiring a large value jump between adjacent surfaces.'
  when_to_use: Use in pencil, pen, charcoal, or other stroke-based studies when plane
    orientation should read clearly but the value design needs to stay restrained.
  when_not_to_use: Do not use mechanically parallel or decorative hatching that ignores
    the form, and do not let stroke direction contradict the chosen light, material,
    or actual surface turn.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_separate_front_and_rim_light_roles_on_head
  variant_name: Separate Front and Rim Light Roles on the Head
  variant_basis: emphasis
  source_id: andrew_loomis_drawing_the_head_and_hands
  source_title: Drawing the Head and Hands
  locator: u06, physical p. 99
  difference_from_foundation: 'Adds Loomis''s controlled two-light portrait-study
    route: combine front illumination with back or rear-top illumination, but assign
    the lights to different visible surface roles so the same head plane is not broken
    into competing crisscross shadow patterns. The second light is used as a separating
    or rim/back accent while the primary light keeps the facial value structure coherent.'
  when_to_use: Use for a designed head study or illustration when a front key needs
    extra separation from the background and a restrained back/rear-top accent can
    clarify silhouette without fragmenting the facial planes.
  when_not_to_use: Do not treat this as a universal rule of physical lighting. Real
    scenes can have overlapping multiple lights on the same surface; when realistic
    illumination is the goal, actual source geometry and material response govern.
    Avoid the method when the extra light makes the head harder rather than easier
    to read.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_gate_tone_on_age_and_expression_read_in_outline
  variant_name: Gate Tone on Age and Expression Reading in Outline
  variant_basis: method_sequence
  source_id: andrew_loomis_drawing_the_head_and_hands
  source_title: Drawing the Head and Hands
  locator: u07, physical p. 111
  difference_from_foundation: 'Adds Loomis''s child-head staging gate before modeling:
    keep the head in outline until the intended age and expression already read, because
    subsequent tone can strengthen the forms that are present but cannot reliably
    rescue an age or expression that was structurally wrong in the linear statement.'
  when_to_use: Use when a school-age or other child portrait is tempting you to shade
    early even though the age, expression, silhouette, or feature placement is still
    uncertain; use the line-only state as a cheap diagnostic before committing to
    modeling.
  when_not_to_use: 'Do not make outline a mandatory style or deny that value can participate
    in design from the beginning in a value-first workflow. This is a Loomis sequencing
    alternative for line-led head studies: if the chosen process establishes age and
    expression through value masses rather than contour, apply the same gate to that
    earlier structure instead.'
  absorbed_from_object_id: none
- variant_id: VAR_hogarth_concentrate_accents_at_structurally_decisive_points
  variant_name: Concentrate Accents at Structurally Decisive Points
  variant_basis: emphasis
  source_id: burne_hogarth_drawing_the_human_head
  source_title: Drawing the Human Head
  locator: u06, physical pp. 148-152
  difference_from_foundation: 'Adds the gallery''s sparse-rendering alternative: allow
    broad masses, hair, atmosphere, or minor planes to remain tentative or softly
    stated, then spend the darkest line, sharpest edge, clearest highlight, or most
    definite mark at the few points where structure and identity become decisive.
    Hogarth reads this economy in Degas, Forain, Whistler, Redon, and related examples.'
  when_to_use: Use when a head study should stay loose, atmospheric, sketch-like,
    or economical while still reading as a specific solid head rather than an unresolved
    blur.
  when_not_to_use: Do not scatter accents uniformly or use a few dark marks to fake
    structure that was never solved. The accents clarify an already understood mass/plane
    organization; they do not substitute for it.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_freeze_changing_light_with_plane_value_key
  variant_name: Freeze Changing Light With a Plane-Value Key
  variant_basis: method_sequence
  source_id: andrew_loomis_successful_drawing
  source_title: Successful Drawing
  locator: u04, physical p. 85
  difference_from_foundation: 'Adds Loomis''s field workflow for unstable illumination: when the observed light changes faster than a finished drawing can be made, capture one chosen moment as a quick broad-plane key, classifying the major surfaces as light, halftone, or shadow, then use that snapshot as the fixed lighting reference for later development rather than chasing subsequent changes.'
  when_to_use: Use when drawing from life under moving sunlight or another changing source and the long rendering needs to preserve one coherent light state across time.
  when_not_to_use: Do not treat the key as infallible or keep following later illumination after choosing the preserved state; verify the broad plane read before committing, because a mistaken first classification can fossilize the error through the finish.
  absorbed_from_object_id: none

- variant_id: VAR_mogilevtsev_model_portrait_detail_from_light_shadow_boundary_and_planes
  variant_name: Model Portrait Detail From the Light-Shadow Boundary and Planes
  variant_basis: method_sequence
  source_id: vladimir_mogilevtsev_fundamentals_of_drawing
  source_title: Fundamentals of Drawing
  locator: u04, physical PDF pp. 22-30
  difference_from_foundation: >-
    Adds Mogilevtsev's portrait-detail modeling sequence after feature placement is resolved: re-establish the major plane structure, analyze the light/shade boundary, mass the shadow broadly without overworking it, then develop halftone and light while changing edge/tangency and contrast as the surface orientation changes. Recheck the local passage against the whole head before increasing finish.
  when_to_use: Use when facial features are correctly placed but local rendering is becoming patchy, symbolic, or disconnected from the larger head planes and tonal relationships.
  when_not_to_use: Do not turn the source's claim that the chiaroscuro boundary follows major plane intersections into a universal lighting law. Treat that alignment as an academic analysis heuristic; the literal terminator is governed by actual light direction and continuous surface curvature.
  absorbed_from_object_id: none

- variant_id: VAR_loomis_shift_whole_picture_value_key_while_preserving_internal_relations
  variant_name: Shift the Whole Picture Value Key While Preserving Internal Relations
  variant_basis: method_sequence
  source_id: andrew_loomis_creative_illustration
  source_title: Creative Illustration
  locator: u06, physical PDF pp. 77-80; printed pp. 85-88
  difference_from_foundation: "Adds Loomis's key-manipulation route: remap the picture broadly upward or downward in the available value range while preserving enough internal light/dark ordering and separation that the subject remains coherent. This lets the artist compare high-, middle-, and low-key conceptions without redesigning every relationship independently."
  when_to_use: "Use during tonal planning when the large value relationships are readable but the overall picture feels too light, too dark, too flat, or emotionally mismatched and you want to test a different key while retaining the subject's internal organization."
  when_not_to_use: "Do not preserve numeric intervals mechanically when lighting, material response, exposure limits, or focal emphasis require compression or selective change. The invariant is relational coherence, not identical measured value spacing."
  absorbed_from_object_id: none
- variant_id: VAR_loomis_break_uniform_tonal_fields_without_losing_value_family
  variant_name: Break Uniform Tonal Fields Without Losing the Value Family
  variant_basis: emphasis
  source_id: andrew_loomis_creative_illustration
  source_title: Creative Illustration
  locator: u07, physical PDF p. 100; printed p. 108
  difference_from_foundation: "Adds Loomis's anti-flatness diagnostic inside an already correct large tonal mass: introduce restrained internal modulation, small accents, or local variation so a mechanically smooth field gains vitality while the broad value family and picture hierarchy remain intact."
  when_to_use: "Use when a large tone is correctly grouped but reads pasted-on, tinny, dead, or mechanically even and a small amount of internal variation can restore life without changing the large value design."
  when_not_to_use: "Do not break every quiet field with texture or noise, and do not scatter accents until one coherent mass becomes many unrelated patches. Flatness may be intentionally graphic, atmospheric, or structurally useful; preserve it when it serves the picture."
  absorbed_from_object_id: none
---

# Consolidate Resolved Form With Tone

## Pattern Rule
**IF** structurally solved forms still read as fragmented pieces or the large value organization is unclear
**THEN** establish a coherent large light/dark or tonal mass over the resolved construction, then model secondary transitions so value strengthens the same form, depth, and hierarchy rather than replacing them
**ELSE** keep the drawing line-led when tone is not needed for the task

## Do
- Start from the largest value relationships and compare them across the whole subject before polishing local passages.
- Let tone unify forms that already have correct attachment, overlap, and volume.
- Allow selected contour boundaries to soften, break, or disappear when adjacent value relationships still explain the form.
- Distinguish study-mode modeling tone from a finished lighting statement; once scene light is specified, values must answer to that light unless an expressive composition deliberately bends it.

## Don't
- Use darkening to hide an unclear attachment, wrong perspective, contradictory overlap, or unresolved joint.
- Shade every part independently until the subject becomes a collection of separately modeled pieces.
- Treat one teaching value map as a universal formula for every light, material, or subject.

## Checklist
- The largest value pattern reads before small modeling is added.
- Tone makes the subject more coherent without moving the solved construction.
- Lost or softened edges remain understandable through adjacent planes and values.
- A finished rendering's value pattern agrees with the intended light, material, and compositional purpose.

## Notes
`VAR_loomis_freeze_changing_light_with_plane_value_key` adds Loomis's unstable-light field route: capture one chosen light state as a quick broad-plane L/H/S key, then develop against that fixed key instead of chasing later changes.

Dodson supplies the subject-general value organization: map large light/dark relationships first, then refine them. The original Hogarth figure card is retained as a bounded variant for fusing overlap-separated body masses. Earlier Gill, Hampton, Vilppu, and Loomis variants remain attached because they describe distinct rendering conditions rather than separate ownership.

`VAR_dodson_map_light_and_shadow_before_modeling` retains **Map Light and Shadow Before Modeling** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_hogarth_fuse_resolved_figure_as_one_tonal_mass` retains **Fuse a Resolved Figure as One Tonal Mass** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_use_physical_light_and_material_response` retains **Use Physical Light and Material Response for Final Rendering** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_hampton_match_value_edge_timing_to_plane_change` retains **Match Value and Edge Timing to the Rate of Plane Change** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_loomis_keep_cloth_modeling_inside_material_value_family` retains **Keep Cloth Modeling Inside the Material Value Family** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_vilppu_model_form_with_viewer_facing_tone_before_direct_light` retains **Model Form With Viewer-Facing Tone Before Direct Light** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_vilppu_separate_core_and_cast_shadow_by_cause` retains **Separate Core and Cast Shadow by Cause** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_vilppu_use_atmospheric_contrast_as_local_depth_design` retains **Use Atmospheric Contrast as Local Depth Design** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_loomis_model_head_as_single_light_plane_value_study` retains **Model the Head as a Single-Light Plane Value Study** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_loomis_turn_planes_with_stroke_direction_before_value_change` retains **Turn Planes With Stroke Direction Before Increasing Value Contrast** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_loomis_separate_front_and_rim_light_roles_on_head` retains **Separate Front and Rim Light Roles on the Head** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_loomis_gate_tone_on_age_and_expression_read_in_outline` retains **Gate Tone on Age and Expression Reading in Outline** as a bounded alternative under the conditions recorded in the variant metadata.

`VAR_hogarth_concentrate_accents_at_structurally_decisive_points` retains **Concentrate Accents at Structurally Decisive Points** as a bounded alternative under the conditions recorded in the variant metadata.
`VAR_mogilevtsev_model_portrait_detail_from_light_shadow_boundary_and_planes` retains **Model Portrait Detail From the Light-Shadow Boundary and Planes** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_loomis_shift_whole_picture_value_key_while_preserving_internal_relations` adds Loomis's whole-picture key-remapping route: shift the picture broadly lighter or darker while preserving enough internal value ordering to keep the subject coherent, then judge whether the new key better serves the intended picture.

`VAR_loomis_break_uniform_tonal_fields_without_losing_value_family` adds a local vitality check after the broad mass is already correct: break mechanical smoothness with restrained modulation or accents while keeping the field inside one coherent value family.

