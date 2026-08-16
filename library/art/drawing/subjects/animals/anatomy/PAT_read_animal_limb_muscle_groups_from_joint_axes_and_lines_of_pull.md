---
object_id: PAT_read_animal_limb_muscle_groups_from_joint_axes_and_lines_of_pull
object_type: pattern
name: Read Animal Limb Muscle Groups From Joint Axes and Lines of Pull
library_path:
- art
- drawing
- subjects
- animals
- anatomy
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animal_drawing
- animal_anatomy
- mammal
- limb
- musculature
- functional_anatomy
- joint_axis
- line_of_pull
- flexor
- extensor
- multi_joint
- comparative_anatomy
cross_links:
- rel: foundation_of
  target_object_id: PAT_read_hindleg_muscle_groups_from_joint_axes_and_lines_of_pull
- rel: foundation_of
  target_object_id: PAT_shape_specialized_runner_foreleg_from_functional_muscle_and_skeletal_masses
- rel: foundation_of
  target_object_id: PAT_shape_carnivore_foreleg_from_joint_axes_and_paw_control_muscle_mass
- rel: related_to
  target_object_id: PAT_rebuild_animal_limb_joint_form_from_articulation_and_axis
- rel: related_to
  target_object_id: PAT_taper_mammal_limb_mass_from_proximal_muscle_to_distal_tendon
- rel: related_to
  target_object_id: PAT_carry_form_flow_through_joint_transitions
reference:
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
confidence: high
references: []
variants: []
---

# Read Animal Limb Muscle Groups From Joint Axes and Lines of Pull

## Pattern Rule
**IF** an animal limb is being built from memorized muscle names or copied surface bulges without a clear mechanical relation to the articulated skeleton
**THEN** keep the relevant joint axes visible, group the major muscles by which axes their lines of pull cross, account for groups that span more than one joint, and use those functional groups to organize the large soft-tissue masses before resolving individual muscles
**ELSE** keep the anatomy abbreviated when the major functional masses already agree with the pose, species, and underlying joint chain.

## Do
- Start from the articulated limb and its current joint axes. The skeleton supplies the moving framework that gives every muscle group a meaningful route.
- Trace a major group's line of pull across each joint it actually spans before assigning an action. Use the specific joint geometry rather than a memorized front/back slogan.
- Keep multi-joint groups intact when they cross more than one axis. One continuous group can contribute different actions at different joints and should not be broken into unrelated local lumps.
- Reduce named muscles into a few functional complexes first. Bammes uses this simplification in both hindleg and runner-foreleg studies so the large rhythm and mass organization can be understood before anatomical inventory.
- Convert the grouped functions into visible construction only after the axes are secure: decide where the limb gains depth, where masses overlap, and where tendon or skeleton becomes more dominant.
- Recheck the arrangement against the animal being studied. Comparative anatomy changes proportions, attachments, muscle amount, and distal specialization even when the functional reading method remains useful.

## Don't
- Do not turn "in front of an axis" or "behind an axis" into a universal flexor/extensor sign rule. The relevant joint, axis orientation, and line of pull determine the action.
- Do not memorize an exact horse muscle map and stamp it onto carnivores, primates, or other mammals.
- Do not inventory every named muscle before the functional groups and skeletal axes are readable.
- Do not infer a precise contraction state, hidden attachment, or force magnitude from an outer contour that the reference does not support.
- Do not let soft-tissue masses conceal an uncertain joint chain; correct the articulated framework first.

## Checklist
- Every major limb mass can be related to one or more joint axes rather than floating between bones.
- Multi-joint groups remain mechanically continuous across the joints they span.
- Functional groupings explain the large visible mass pattern before individual muscle names are needed.
- Species differences are allowed to change the arrangement instead of being forced into one model.
- The limb can still be simplified back to its joint chain and major functional masses without losing the pose.

## Notes
Bammes first establishes this method in the hindleg on printed p. 55, grouping muscle complexes by the joint cross-axes and lines of pull they span. Section 6.2 independently repeats the same learner decision in the runner foreleg: the shoulder, elbow, carpal, and digital groups are read in relation to moving axes, and several groups cross more than one joint.

That repetition earns a broader owner. The portable skill is not a horse atlas map; it is a way to **organize limb anatomy from mechanics outward**. `PAT_read_hindleg_muscle_groups_from_joint_axes_and_lines_of_pull` remains as the hindleg specialization because it preserves the specific hip, knee, tarsal, rump, and Achilles examples that this general Pattern should not carry. `PAT_shape_specialized_runner_foreleg_from_functional_muscle_and_skeletal_masses` preserves the runner foreleg's distinctive plastic consequences.
