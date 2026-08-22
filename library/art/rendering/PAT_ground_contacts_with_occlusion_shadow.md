---
object_id: PAT_ground_contacts_with_occlusion_shadow
object_type: pattern
name: Ground Contacts With Occlusion Shadow
library_path:
- art
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- occlusion
- contact_shadow
- depth
- grounding
cross_links:
- rel: related_to
  target_object_id: PAT_model_matte_form_from_primary_light_and_secondary_fill
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants: []
references: []
---

# Ground Contacts With Occlusion Shadow

## Pattern Rule
**IF** two surfaces touch or approach closely enough that surrounding illumination cannot reach the gap
**THEN** place the darkest compact occlusion accent where light access is most restricted, then release it as the gap opens
**ELSE** avoid inventing a contact-darkening band when the geometry remains exposed to light.

## Do
- Concentrate the darkest occlusion near true contact, tight folds, crevices, and inside corners.
- Let the dark soften or lighten as separation increases and more environmental light can enter.
- Keep occlusion distinct from a directional cast shadow; it follows restricted light access, not a projected silhouette.
- Use the contact accent sparingly enough that it grounds rather than outlines the form.

## Don't
- Draw a uniform black contour around every overlap or object-ground junction.
- Extend a contact shadow far from the contact without a cast-shadow cause.
- Ignore local material and environment when they visibly lift or soften the junction.

## Checklist
- The darkest contact accents occur where surrounding light is most blocked.
- Occlusion weakens as the geometry opens.
- Contacts feel grounded without acquiring artificial outlines.

## Notes
Occlusion shadow is a compact visibility-of-light problem. It is strongest where the environment has the least access to a gap, which makes it a useful but easily overused grounding cue.
