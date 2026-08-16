---
object_id: PAT_define_image_story_job_before_visualizing
object_type: pattern
name: Define the Image's Story Job Before Visualizing
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
- storytelling
- illustration
- narrative
- communication
- suspense
- image_text
cross_links:
- rel: related_to
  target_object_id: PAT_choose_viewpoint_to_strengthen_story_effect
- rel: related_to
  target_object_id: AP_build_comic_page_from_assigned_beats_to_pencils
- rel: related_to
  target_object_id: AP_design_comic_cover_from_editorial_brief_to_pencils
reference:
  source_title: Creative Illustration
  author: Andrew Loomis
confidence: high
references: []
variants:
- variant_id: VAR_loomis_use_illustration_as_entry_point_to_surrounding_message
  variant_name: Use the Illustration as an Entry Point to the Surrounding Message
  variant_basis: context
  difference_from_foundation: For image-and-message layouts, treats the picture as a gateway that attracts attention, makes
    enough of the promise or situation visible to create relevance, and directs curiosity into the remaining copy, product,
    or communication rather than satisfying the viewer entirely inside the image.
  when_to_use: Use when the illustration is one component of a larger communication and success depends on moving the viewer
    from the picture into adjacent text, product information, or another required unit.
  when_not_to_use: Do not force this route when the image is meant to stand alone, when surrounding text is optional, or when
    the illustration itself must carry the complete message.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_use_cover_as_experience_promise_not_contents_inventory
  variant_name: Use the Cover as an Experience Promise Rather Than a Contents Inventory
  variant_basis: context
  difference_from_foundation: Specializes the story-job decision for covers and jackets by making the image promise the work's
    subject, mood, tension, character, question, or reward without trying to summarize every important event or fact inside.
  when_to_use: Use when a cover must create accurate curiosity and communicate what kind of experience the work offers before
    the audience enters it.
  when_not_to_use: Do not use a misleading tease, spoil the work merely to make the cover dramatic, or force a summary when
    direct identification or another communication job is more important.
  absorbed_from_object_id: none
- variant_id: VAR_dahlig_scale_emotional_cue_redundancy_to_desired_explicitness
  variant_name: Scale Emotional Cue Redundancy to the Desired Explicitness
  variant_basis: emphasis
  difference_from_foundation: 'Treats the number of reinforcing emotional channels as an adjustable design variable: a direct
    read can align face, body, viewpoint, color treatment, and narrative evidence, while an ambiguous read can leave some
    channels unstated or partially contradictory.'
  when_to_use: Use when deciding how plainly or subtly the image should communicate its emotional job before rendering begins.
  when_not_to_use: Do not maximize every cue by default or create ambiguity accidentally; choose the degree of redundancy
    to fit the intended reading.
  absorbed_from_object_id: none
---

# Define the Image's Story Job Before Visualizing

## Pattern Rule
**IF** an illustration works with a story, brief, caption, page, sequence, or other surrounding communication
**THEN** decide what information the image itself must carry, reinforce, or deliberately withhold before choosing the scene and composition
**ELSE** let the picture carry the full communication when it must stand alone.

## Do
- State the picture's communication job before thumbnailing: carry the idea substantially by itself, reinforce or advance accompanying information, or create a deliberate information gap that makes the viewer continue.
- Identify what the audience must understand immediately and what can remain unresolved.
- Preserve suspense when the surrounding story depends on a later reveal; choose a moment that creates expectation rather than prematurely illustrating the answer.
- Let staging, viewpoint, gesture, expression, and environment serve the chosen information boundary.
- Recheck the picture against its actual context. A strong standalone image can still be the wrong illustration if it repeats, contradicts, or spoils what surrounds it.

## Don't
- Do not assume the image should summarize every fact available in the story or brief.
- Do not reveal the outcome merely because it produces the most spectacular scene when the narrative depends on uncertainty.
- Do not make the picture so withholding that the intended situation, characters, or stakes become unintelligible.
- Do not judge the illustration only as an isolated composition when its real job depends on adjacent text, sequence, or display context.

## Checklist
- The image has a named communication job.
- Essential immediate information is visible without unnecessary explanation.
- Any withheld information is withheld deliberately and supports the intended narrative effect.
- The selected scene does not accidentally spoil a later reveal.
- The picture and its surrounding communication divide the work intentionally rather than redundantly.

## Notes
Loomis distinguishes illustrations that largely carry their own message, illustrations that support accompanying words, and illustrations that intentionally leave enough unanswered to draw the reader onward. The portable lesson is not tied to magazine publishing: before visualizing, decide how much narrative labor the image should perform and how much should remain outside the frame. A technically excellent image can fail its assignment by telling too much, too little, or the wrong part of the story.

`VAR_loomis_use_illustration_as_entry_point_to_surrounding_message` specializes the story-job decision for mixed layouts: the image can attract and clarify enough of the promise to make the viewer continue into adjacent copy, product, or message instead of becoming a self-contained diversion from the rest of the communication.

`VAR_loomis_use_cover_as_experience_promise_not_contents_inventory` treats the image as an accurate promise of the work's experience rather than a literal inventory of its contents.

`VAR_dahlig_scale_emotional_cue_redundancy_to_desired_explicitness` adds an explicitness control to story planning. Reinforce the emotion through multiple channels for a forceful read, or deliberately reduce that redundancy when the image should leave more inference to the viewer.
