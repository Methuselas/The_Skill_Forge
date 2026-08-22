---
object_id: PAT_create_depth_sequence_with_overlap
object_type: pattern
name: Create a Depth Sequence With Overlap
library_path:
- art
- foundations
- form-construction
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- overlap
- depth
- interposition
- form_construction
cross_links: []
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants:
- variant_id: VAR_hogarth_sequence_foreshortened_figure_with_partial_forms
  variant_name: Sequence a Foreshortened Figure With Partial Forms
  variant_basis: source
  difference_from_foundation: Hogarth applies the general interposition decision to a tipped human figure, emphasizing that
    each visible fragment of an obscured limb or torso mass must retain enough identity, direction, volume, and attachment
    for the viewer to complete the hidden member mentally.
  when_to_use: Use when a foreshortened or self-overlapping figure needs an especially explicit near-to-far ordering through
    limbs and torso masses.
  when_not_to_use: Do not force extra occlusion when the intended pose is already spatially clear or when another depth cue
    carries the relationship more cleanly.
  absorbed_from_object_id: none
---

# Create a Depth Sequence With Overlap

## Pattern Rule
**IF** two or more forms occupy different depths and their order is unclear
**THEN** let nearer forms interpose over farther forms so partial visibility establishes a readable near-to-far sequence
**ELSE** keep forms complete when they genuinely occupy similar depth or when another spatial cue already carries the relationship sufficiently

## Do
- Let the nearer form interrupt or cover the farther form at a boundary that agrees with the intended spatial order.
- Preserve enough of each obscured form's direction, volume, identity, and attachment that the hidden continuation can still be inferred.
- Use overlap together with scale, convergence, atmospheric reduction, or other depth cues when one cue alone leaves the space weak.
- Check that repeated overlaps form one consistent sequence rather than a set of local tricks that contradict one another.

## Don't
- Show every form in full and expect contour alone to produce the same recession.
- Cut a hidden form so abruptly that it reads as detached, pasted on, or amputated from its parent structure.
- Add more overlap merely to make the picture feel "deeper" when the resulting order becomes ambiguous.
- Use overlap to hide unresolved placement or attachment errors.

## Checklist
- A viewer can identify which major forms are nearer and which are farther without labels.
- Partial forms still imply believable complete forms behind the occluders.
- The overlap order agrees with the rest of the perspective and scale evidence.
- Removing the overlap would noticeably weaken the intended depth relationship.

## Notes
Dodson presents overlap as one of several general depth cues and demonstrates it with non-figure subjects as well as ordinary scenes. This genericizes the earlier Hogarth figure-specific owner: the reusable decision is interposition itself, while Hogarth's foreshortened-figure treatment remains a bounded variant.
Variants retained in this canonical object: `VAR_hogarth_sequence_foreshortened_figure_with_partial_forms`.
