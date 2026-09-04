---
object_id: PAT_compare_related_animal_types_with_proportion_boxes
object_type: pattern
name: Compare Related Animal Types With Proportion Boxes
library_path:
- art
- subjects
- animals
- construction
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_establish_animal_type_from_proportional_ensemble
tags:
- animal_drawing
- proportion
- conformation
- comparative_anatomy
- horse
- pig
- warthog
- dog
- canine
- breed
cross_links:
- rel: related_to
  target_object_id: PAT_transport_proportional_landmarks_across_views
- rel: related_to
  target_object_id: PAT_block_quadruped_from_dorsal_axis_and_three_body_masses
reference:
  source_title: The Art of Animal Drawing
  author: Ken Hultgren
confidence: high
references: []
variants:
- variant_id: VAR_hultgren_compare_warthog_to_domestic_pig_from_shared_frame_and_diagnostic_landmarks
  variant_name: Compare Warthog and Domestic Pig From a Shared Frame and Diagnostic Landmarks
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a related-type comparison route that starts from a shared skeletal/body frame instead
    of matched proportion boxes: Hultgren treats the warthog as structurally close to the domestic pig, then separates it
    with a longer nose, more erect ears, a dorsal hair ridge, and view-dependent silhouette checks such as the pig-like rear
    view.'
  when_to_use: Use when two closely related animal types share enough construction that rebuilding each from scratch hides
    the useful differences; first establish the common frame, then isolate the few landmarks that actually distinguish the
    intended type.
  when_not_to_use: Do not promote Hultgren's listed warthog traits into exhaustive or fixed species diagnostics. Age, sex,
    individual variation, viewpoint, and the actual reference can change how strongly each landmark appears.
  absorbed_from_object_id: none
- variant_id: VAR_hultgren_compare_dog_breeds_by_resizing_shared_skeleton_parts
  variant_name: Compare Dog Breeds by Resizing Parts of a Shared Skeleton
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Hultgren''s dog-breed comparison route: keep the simplified canine skeleton as the common
    topology, then change the relative lengths and bulk of its parts to establish breed conformation before coat or facial
    finish. His opening contrast is a long-backed, short-legged dachshund against the shorter, squarer English bull, with
    later pages extending the same study across greyhound, cocker, Great Dane, and collie types.'
  when_to_use: Use when several dog breeds keep collapsing into one generic canine and the useful distinction lies in relative
    segment length, trunk proportion, chest mass, or limb scale more than in markings or grooming.
  when_not_to_use: Do not treat Hultgren's stylized examples as breed-standard measurements or force every individual into
    one historical type drawing; preserve the shared canine organization, then set the actual proportions from the intended
    dog or reference.
  absorbed_from_object_id: none
- variant_id: VAR_bammes_compare_representative_types_by_shared_design_and_function
  variant_name: Compare Representative Animal Types by Shared Design and Functional Specialization
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Bammes''s broader comparative-anatomy route: begin from a structural design shared across
    representative animal types, then compare how proportion, pivotal points, skull/limb emphasis, and front-versus-rear organization
    change with the animal''s functional demands. This contrasts types by shared plan plus specialization rather than by enclosing
    them in matched proportion boxes.'
  when_to_use: Use when an unfamiliar animal is either being copied as a disconnected silhouette or being forced into one
    generic mammal template; compare it with a few structurally informative types to identify what stays common and which
    relationships actually change.
  when_not_to_use: Do not turn one representative example or Bammes's functional explanation into an exhaustive species law.
    Use the comparison to generate structural questions, then check the actual animal, age, pose, and reference.
  absorbed_from_object_id: none
---

# Compare Related Animal Types With Proportion Boxes

## Pattern Rule
**IF** two related animal types, ages, or breeds keep collapsing into the same generic construction
**THEN** place them in comparable height-width boxes, carry a small set of shared structural landmarks across those boxes, and compare the relative lengths, heights, widths, and mass emphasis before adding surface traits
**ELSE** rely on direct observation when only one subject is being studied and no comparative distinction is needed.

## Do
- Use the same measurement questions for every comparison: overall height and length, shoulder and rear height, trunk depth, neck and head proportion, limb length, and front-versus-rear width.
- Keep the landmarks structural rather than decorative so the comparison survives when coat, mane, feathers, or stripes are removed.
- Compare related examples side by side, such as draft versus saddle horses, a colt against an adult, or zebra versus horse proportion.
- Let age or type change the whole proportional ensemble rather than resizing one isolated feature.
- Treat named traits as observations to test against the actual subject or reference, not as fixed biological constants.

## Don't
- Use one horse mannequin and identify type only by mane, feathering, stripe pattern, or other surface symbols.
- Change the scale of the entire animal and call that a proportion difference.
- Compare different views with unrelated boxes and then infer proportion from foreshortening artifacts.
- Promote one stylized example into a universal breed, age, or species rule without checking the subject being drawn.

## Checklist
- The compared animals remain distinguishable when reduced to boxes, body masses, and landmark lines.
- Differences can be described as relationships such as longer, higher, wider, shorter, or more massive rather than only as surface labels.
- The same viewpoint and comparable measurement scheme are used before proportions are judged.
- Removing texture and decorative traits does not erase the intended type distinction.

## Notes
Use enclosing boxes to compare related animal types through overall size and conformation, leg and body length, rear height, head and hoof size, and width relationships. The comparison method transfers; broad type claims do not become universal anatomy.

`VAR_hultgren_compare_warthog_to_domestic_pig_from_shared_frame_and_diagnostic_landmarks` adds a shared-frame transfer: when related types share most of the structure, establish that common frame first and spend the comparison on the few landmarks that separate them instead of forcing every distinction through a proportion box.

`VAR_hultgren_compare_dog_breeds_by_resizing_shared_skeleton_parts` adds the canine transfer: hold one simplified canine skeletal organization constant and compare breeds by redistributing relative length, height, and mass across that frame before surface coat or facial traits. The historical breed drawings are examples to test against the actual subject, not fixed standards.

`VAR_bammes_compare_representative_types_by_shared_design_and_function` adds a wider comparative-anatomy route: hold the shared structural plan in mind, then ask how proportion, pivotal points, limb emphasis, and other framework relationships specialize across representative types. It is more transferable than a matched-box comparison, but also easier to overgeneralize, so the actual animal remains the final check.
