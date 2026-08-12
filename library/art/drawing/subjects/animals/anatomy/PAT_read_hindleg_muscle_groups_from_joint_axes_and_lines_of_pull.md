---
object_id: PAT_read_hindleg_muscle_groups_from_joint_axes_and_lines_of_pull
object_type: pattern
name: Read Hindleg Muscle Groups From Joint Axes and Lines of Pull
library_path:
- art
- drawing
- subjects
- animals
- anatomy
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_read_animal_limb_muscle_groups_from_joint_axes_and_lines_of_pull
tags:
- animal_drawing
- animal_anatomy
- mammal
- hindleg
- musculature
- functional_anatomy
- joint_axis
- line_of_pull
- flexor
- extensor
cross_links:
- rel: related_to
  target_object_id: PAT_construct_mammal_hindleg_from_pelvic_anchor_and_joint_chain
- rel: related_to
  target_object_id: PAT_change_hindleg_joint_form_with_flexion_and_axis
- rel: related_to
  target_object_id: PAT_distinguish_quadruped_forequarter_suspension_from_hindquarter_drive
- rel: related_to
  target_object_id: PAT_carry_form_flow_through_joint_transitions
reference:
  source_id: gottfried_bammes_artist_guide_to_animal_anatomy
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
  publish_date: '2004'
  media_type: PDF
  locator: u14, printed p. 55; physical p. 53
  evidence_type: text
confidence: high
references: []
variants: []
---

# Read Hindleg Muscle Groups From Joint Axes and Lines of Pull

## Pattern Rule
**IF** an animal hindleg is being built from named muscle lumps or copied surface bulges without a clear relation to the skeleton
**THEN** keep the joint cross-axes visible in the construction, trace the major muscle groups by the side of each relevant axis that their line of pull crosses, note when one group spans more than one joint, and use those functional groups to organize the front and back masses before resolving individual muscles
**ELSE** keep the lighter skeletal construction when the major functional masses already agree with the pose and species.

## Do
- Start from the articulated hindleg chain and its joint axes; Bammes treats the skeleton as the priority framework that gives muscle function and form a place to act.
- Group muscles by what they do across a joint rather than by memorizing every named muscle. On the hindleg, the source distinguishes hip-moving groups, knee extensors, tarsal and digital groups, and multi-joint rump or Achilles-related groups.
- Follow the actual line of pull across the **specific joint** before assigning flexion or extension. A group can cross one axis or several, so its action cannot be inferred from one contour label alone.
- Let the grouped flexor/extensor volumes help explain the leg's front-to-back depth. Bammes notes that these masses tend to occupy the front and rear contours more strongly than the side-to-side width.
- Recheck the arrangement against the animal being studied. Bammes explicitly warns that his functional diagrams are simplified and that comparable species may differ in which muscle groups are present or where they originate.

## Don't
- Do not turn "in front of the axis = extension, behind = flexion" into a universal sign rule for every joint. Bammes's own hindleg examples assign different actions at the hip, knee, tarsus, and digits; the relevant joint and line of pull decide the action.
- Do not inventory individual muscle names before the large functional groups and skeletal axes are clear.
- Do not assume a horse grouping can be stamped unchanged onto cows, dogs, cats, or other mammals; the source explicitly notes genus-level differences.
- Do not infer a precise contraction state or hidden attachment from a static outer contour when the source or reference does not support it.
- Do not let muscle masses obscure an uncertain joint chain; correct the skeleton before developing the soft forms.

## Checklist
- Each major hindleg mass can be related to one or more joint axes instead of floating between bones.
- A multi-joint group is not accidentally treated as if it acted only on the nearest joint.
- Front/back muscle volumes support the visible contour without replacing the underlying skeleton.
- The arrangement is allowed to change with species rather than being forced into one horse diagram.
- The drawing can still be simplified to functional masses without needing every muscle name.

## Notes
Bammes frames the living hindleg as a structural dialogue between hard skeletal forms and variable muscle forms. On printed p. 55 he reduces the musculature to functional complexes and explains them by their relation to joint cross-axes and lines of pull. He then immediately qualifies the diagrams as **general and simplified**, noting that the actual arrangement differs between animal forms.

This card now sits beneath `PAT_read_animal_limb_muscle_groups_from_joint_axes_and_lines_of_pull`, the broader owner earned when §6.2 independently repeats the same axis-and-line-of-pull logic in the runner foreleg. The hindleg specialization remains useful because it preserves Bammes's specific hip, knee, tarsal, rump, Achilles, and distal-foot examples while the general owner keeps the method portable across limbs.
