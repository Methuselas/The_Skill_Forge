---
object_id: PAT_scale_visual_information_to_viewing_time_and_display_context
object_type: pattern
name: Scale Visual Information to Viewing Time and Display Context
library_path:
- art
- composition
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- composition
- readability
- viewing_distance
- display
- simplification
- illustration
cross_links:
- rel: related_to
  target_object_id: PAT_define_image_story_job_before_visualizing
- rel: related_to
  target_object_id: PAT_design_vignette_as_open_composition_with_page_space
reference:
  source_title: Creative Illustration
  author: Andrew Loomis
confidence: high
references: []
variants:
- variant_id: VAR_loomis_reduce_glance_read_display_to_one_dominant_unit_and_minimal_message
  variant_name: Reduce a Glance-Read Display to One Dominant Unit and Minimal Message
  variant_basis: constraint
  difference_from_foundation: Specializes the general viewing-context rule for extreme short-read or distance-read displays
    by reducing competing information, favoring one dominant visual unit, simplifying broad value and silhouette relationships,
    and keeping wording to what can survive the actual attention window.
  when_to_use: Use for posters, signs, billboards, venue graphics, or other displays that must communicate quickly or from
    substantial distance.
  when_not_to_use: Do not apply a fixed historical word count or viewing-time formula, and do not strip information that the
    real audience can comfortably inspect at close range or over sustained viewing.
  absorbed_from_object_id: none
- variant_id: VAR_bluth_make_brief_storyboard_images_read_at_a_glance
  variant_name: Make Brief Storyboard Images Read at a Glance
  variant_basis: context
  difference_from_foundation: Specializes the viewing-context rule for storyboard images that will be seen only briefly by
    simplifying each sketch around one immediately legible action or message, separating important silhouettes, suppressing
    competing detail or movement, and concentrating visual emphasis where the viewer must look first.
  when_to_use: Use when a storyboard or animatic image has a short viewing interval and must communicate its main action,
    relationship, or story information almost immediately.
  when_not_to_use: Do not force every storyboard panel into the same simplicity, do not preserve a fixed historical duration
    formula, and do not mechanically transfer this constraint to comics or other media where the viewer controls inspection time.
  absorbed_from_object_id: none
- variant_id: VAR_stanchfield_scale_animation_acting_to_final_viewing_distance
  variant_name: Scale Animation Acting to Final Viewing Distance
  variant_basis: context
  difference_from_foundation: Specializes the viewing-context rule for animated acting by judging whether the pose, silhouette,
    directional relationships, weight shift, and primary action still communicate at the character's actual shot size, then
    amplifying or reducing gesture information only as much as that viewing condition requires.
  when_to_use: Use when an acting choice reads at drawing-board or zoomed-in scale but may disappear in a long shot, small
    reproduction, distant presentation, or other reduced viewing condition.
  when_not_to_use: Do not turn this into a universal command to overact. Preserve subtle acting when the shot scale and story
    support it, and do not exaggerate beyond character, mechanics, or emotional intent merely to make motion larger.
  absorbed_from_object_id: none
---

# Scale Visual Information to Viewing Time and Display Context

## Pattern Rule
**IF** an image will be encountered under a specific viewing time, distance, size, medium, or repeat-exposure condition
**THEN** tune its information density, contrast hierarchy, narrative complexity, and persistence to what that viewing condition can actually support
**ELSE** use the intended final presentation as the default context rather than designing only for a close working view.

## Do
- Estimate whether the image must read in a glance, rewards extended looking, or will be seen repeatedly over a long period.
- Simplify large relationships when distance, small reproduction, or short attention time will erase fine distinctions.
- Allow richer secondary information when the viewing condition genuinely supports sustained inspection.
- Test whether the central idea survives at the actual output size and likely viewing distance.
- Consider repeat exposure: distinguish short-lived intensity that works for a brief encounter from long-lived visual tension that may become tiring when displayed continuously.
- Test the image inside its competitive visual surround when it will appear among many other assertive designs; basic identity and hierarchy must survive the neighboring field, not just a neutral workspace.
- Remove information that does not improve the intended read under the real presentation conditions.

## Don't
- Do not assume more detail produces more communication when the viewer cannot perceive or process it in time.
- Do not simplify every format equally; a close-read page and a glance-read poster solve different information problems.
- Do not design only at zoomed-in working size when the final will be seen much smaller or farther away.
- Do not use suspense or visual strain that depends on novelty when the image must remain comfortable under repeated exposure.

## Checklist
- The likely viewing time, size, and distance are known or reasonably estimated.
- The main idea survives at final scale.
- Secondary information is appropriate to the amount of attention available.
- Nothing essential depends on detail that disappears in the real viewing condition.
- Repeat exposure has been considered when the image will remain on display, especially whether unresolved tension stays rewarding rather than exhausting.
- When competition matters, the primary identifier or image hierarchy survives among representative neighboring designs.

## Notes
Loomis contrasts image types that receive prolonged attention with formats that must communicate quickly at a distance, then asks whether an idea reads in the available time, survives its medium, and can lose anything else without damage. His calendar discussion adds a persistence test: an effect that is effective once may become stale or irritating when seen every day. The durable rule is to design for the actual viewing condition rather than for the drawing board alone. Cover and jacket work adds a competitive-context check: a design that succeeds against a neutral workspace can disappear once surrounded by equally assertive neighbors. Loomis's poster material supplies the extreme short-read case retained in `VAR_loomis_reduce_glance_read_display_to_one_dominant_unit_and_minimal_message`; his calendar discussion reinforces the opposite persistence test, where an effect that succeeds for one glance may become tiring under months of repeated exposure. Bluth applies the rule to brief storyboard images by requiring the main action or message to read quickly before the next sketch replaces it. Bluth extends the same viewing-time rule to fast storyboard images: when a sketch will be visible only briefly, its principal action and message must survive almost immediately through clear silhouette, separation, and focal emphasis. `VAR_bluth_make_brief_storyboard_images_read_at_a_glance` preserves that storyboard-specific application without turning his example timing into a universal duration rule. Stanchfield's “playing to the balcony” application extends the same rule to animated acting: test the performance at the actual character size and viewing distance, strengthen broad pose and action information when subtle acting would disappear, and retain small acting when the shot can support it. `VAR_stanchfield_scale_animation_acting_to_final_viewing_distance` captures that calibration without treating larger acting as automatically better.
