---
object_id: DRILL_build_full_tonal_drawing_from_value_sketch_and_relational_checks
object_type: drill
name: Build a Full Tonal Drawing From a Value Sketch and Relational Checks
library_path:
- art
- drawing
- rendering
stage_binding: 4 final
lane_fit: teach
foundation_role: specialization
routing_class: teaching
specialization_axis: method
foundation_object_id: PAT_consolidate_resolved_form_with_tone
tags:
- rendering
- value_sketch
- tonal_range
- relational_check
- general_to_specific
cross_links:
- rel: teaches
  target_object_id: PAT_consolidate_resolved_form_with_tone
- rel: related_to
  target_object_id: PAT_separate_local_value_from_light_and_shadow_effect
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
target_skill: organizing a full tonal drawing from a stable large-value plan while keeping later local modeling subordinate
  to whole-image value relationships
variants:
- variant_id: VAR_guptill_bracket_observed_values_with_neutral_extreme_anchors
  variant_name: Bracket Observed Values With Neutral Extreme Anchors
  variant_basis: method_sequence
  difference_from_foundation: Before committing the tonal range, compare suspected lights and darks against neutral white
    and black anchors, or equivalent reference patches, so observed value is judged relationally rather than inferred from
    the object name.
  when_to_use: Use when local-color labels such as white, black, or gray are biasing value judgment under unusual illumination.
  when_not_to_use: Do not force every scene to contain literal paper white or absolute black; the anchors calibrate observation
    and can then be compressed to the intended output range.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_low_pass_source_without_softening_output
  variant_name: Low-Pass the Source Without Softening the Output
  variant_basis: method_sequence
  difference_from_foundation: Uses progressive source simplification only to discover mergers and hierarchy, then reopens
    the source to judge actual value/color and inspects the output at full clarity rather than hiding errors with the same
    low-pass treatment.
  when_to_use: Use when local detail is obscuring the major value organization or edge grouping during a tonal study.
  when_not_to_use: Do not copy the artificially darkened/desaturated squinted appearance and do not soften the output to make
    structural errors disappear.
  absorbed_from_object_id: none
---
# Build a Full Tonal Drawing From a Value Sketch and Relational Checks

## Practice Task
Make one small value sketch that reduces a subject to three or four major tones, then use it to build a larger full tonal drawing without allowing any local area to outrun the overall value range.

## Target Skill
Controlling a complex tonal rendering from large value organization to subtle modeling through repeated whole-image comparison.

## Setup
Choose a subject with a readable light pattern. Use a viewfinder if helpful. Work small for the value sketch and larger for the final drawing.

## Instructions
1. Squint at the subject and identify the few largest light, middle, and dark territories.
2. Make a small value sketch that fixes only those large relationships; omit texture and minor modeling.
3. Transfer the large placement to the full drawing and establish the overall lightest useful light and darkest useful dark before polishing any local passage.
4. Develop secondary tones gradually across the whole image. Repeatedly step back and ask relational questions such as “which is lighter?” and “which is darker?” rather than naming isolated values.
5. When one area becomes highly finished while neighboring value families are still undecided, stop and bring the rest of the drawing to the same level of tonal resolution.
6. Finish only after the large pattern still agrees with the value sketch and the finer modeling improves rather than fragments it.

## Success Check
- The small value sketch and final drawing share the same dominant light/dark organization.
- No local passage depends on a value range that contradicts the rest of the image.
- Subtle modeling can be removed mentally without destroying the large tonal read.

## Common Failures
- Rendering one attractive area to completion before the overall range exists.
- Copying local tones independently instead of comparing them across the whole subject.
- Letting the value sketch become so detailed that it no longer serves as a large-pattern control.

## Notes
Dodson's method uses squinting, a small value plan, and repeated relational comparison to keep a long tonal drawing coherent. The exercise is subject-general and is meant to train value judgment, not prescribe one rendering medium.

`VAR_guptill_bracket_observed_values_with_neutral_extreme_anchors` uses neutral light and dark anchors to break local-color naming bias before the working value range is committed.

`VAR_schmid_low_pass_source_without_softening_output` uses source simplification to reveal broad value and edge organization, then returns to a clear view for output inspection. Simplification is an analysis aid, not a blur pass for hiding incorrect drawing or transitions.

`VAR_schmid_low_pass_source_without_softening_output` follows a two-view loop: low-pass the source to identify hierarchy and mergers, reopen the source for actual value/color judgment, and inspect the drawing at full clarity. Never low-pass the output to conceal mistakes.
