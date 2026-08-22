---
object_id: PAT_carry_form_flow_through_joint_transitions
object_type: pattern
name: Carry Form Flow Through Joint Transitions
library_path:
- art
- foundations
- form-construction
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- figure_drawing
- joint_connection
- anatomy
- form_flow
cross_links:
- rel: related_to
  target_object_id: PAT_preserve_articulated_limb_chain
- rel: related_to
  target_object_id: PAT_integrate_shoulder_mass_with_rib_cage
reference:
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
confidence: high
references: []
variants:
- variant_id: VAR_bridgman_elbow_masses_from_opposed_condyles
  variant_name: Organize Elbow Flow From Opposed Condylar Masses
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Bridgman''s elbow-specific routing to the general joint-transition rule: build the inner
    flexor-pronator mass from the medial condyle and the outer extensor-supinator mass from the lateral side, leaving the
    cubital fossa between them; let the thumb-side supinator wedge and little-finger-side ulna route carry those masses down
    the forearm.'
  when_to_use: Use when the elbow reads as a generic hinge bead or the forearm masses do not explain how the upper arm transitions
    into thumb-side and little-finger-side structure.
  when_not_to_use: Do not expose every named muscle or condyle equally; preserve only the masses and landmarks the view and
    action actually reveal.
  absorbed_from_object_id: none
- variant_id: VAR_bridgman_build_knee_as_beveled_block_with_patellar_apex
  variant_name: Build the Knee as a Beveled Block With a Patellar Apex
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Bridgman''s knee-specific block to the general joint-transition rule: conceive the knee
    as a roughly square mass beveled toward the front, hollowed behind, with the patella riding at the apex of the angle between
    thigh and leg while the back is organized by paired hamstring/calf tendons around the popliteal hollow.'
  when_to_use: Use when the knee reads as a round bead, when the patella floats independently of the thigh-leg angle, or when
    the back of the knee lacks a believable transition.
  when_not_to_use: Do not force a literal square outline or expose every tendon; the block is an internal organizing model
    whose visible planes change with view and flexion.
  absorbed_from_object_id: none
- variant_id: VAR_vilppu_use_joint_landmarks_as_directional_cross_axes
  variant_name: Use Joint Landmarks as Directional Cross-Axes
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Vilppu''s landmark-as-orientation use to joint transitions: treat paired bony points at
    the elbow, knee, ankle, and shoulder region as a cross-axis or terminal plane that reveals how the adjoining limb cylinder
    is facing in space. The landmark relationship is used to orient the form, not merely to decorate anatomy.'
  when_to_use: Use when a limb cylinder or joint is structurally present but its facing direction is ambiguous, especially
    around bent elbows, knees, ankles, or shoulder-girdle turns.
  when_not_to_use: Do not expose every landmark equally or force textbook symmetry where perspective, flexion, soft tissue,
    or individual anatomy obscures one point; use only the landmarks the view actually supports.
  absorbed_from_object_id: none
- variant_id: VAR_bammes_construct_knee_from_rolling_joint_mechanics
  variant_name: Construct Knee Form From Rolling Joint Mechanics
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Bammes''s mechanical flexion model to the existing knee transition: establish the distal
    femur as a clear cuboid/roller-like form before rounding it, then let flexion open the knee relationship and roll the
    femoral condylar mass relative to the tibial platform while the patella remains integrated into the quadriceps-patellar-ligament
    chain rather than floating as a separate disk.'
  when_to_use: Use when a bent knee looks like two cylinders joined by a bead, when the patella floats independently of the
    thigh-leg angle, or when flexion does not materially change the front/back knee volumes.
  when_not_to_use: Do not expose a literal mechanical gap or roller in the finished anatomy; cartilage, fat, tendon, capsule,
    muscle, skin, and viewpoint determine the visible surface. Use the mechanism to organize the form, not to draw an engineering
    diagram.
  absorbed_from_object_id: none
---

# Carry Form Flow Through Joint Transitions

## Pattern Rule
**IF** a joint or attachment region makes the connected members look as though they stop and restart
**THEN** treat that region as part of the whole chain and let its bone, tendon, muscle, skin, and contour changes receive and redirect the flow of both adjoining masses
**ELSE** keep the transition understated when the connected system already reads without an explicit route

## Do
- Let the knee combine patella, condyles, tendons, thigh, shin, and calf into one changing leg rather than a separate hinge block.
- Let the deltoid belong visually to both arm and torso, with passages into trapezius, scapular ridge, chest, triceps, and elbow as the view exposes them.
- Let the hip carry the leg into the pelvic and buttock masses, and let the elbow organize upper- and lower-arm forms around its bony projection.
- Join head and torso through the visible sternomastoid, trapezius, neck-funnel, and implied spinal routes appropriate to the camera.

## Don't
- Insert a generic connector between two otherwise unrelated cylinders.
- Preserve every anatomical passage equally when only one or two are visible or useful in the chosen view.
- Force a line through a joint that contradicts the actual body or its pose merely to create a stronger depth effect.

## Checklist
- The joint changes direction without severing the parent member.
- The forms entering and leaving the region share a believable structural relationship.
- The visible transition changes with pose and camera while the underlying connected system remains intact.

## Notes
The chapter's knee, shoulder, elbow, hip, and neck studies are local demonstrations of a larger fact: the human figure is one connected system. A joint is not a punctuation mark between independent pieces. It is a region where the whole system changes direction, tension, visibility, and surface organization.

`VAR_bridgman_elbow_masses_from_opposed_condyles` retains **Organize Elbow Flow From Opposed Condylar Masses** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_bridgman_build_knee_as_beveled_block_with_patellar_apex` retains **Build the Knee as a Beveled Block With a Patellar Apex** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_vilppu_use_joint_landmarks_as_directional_cross_axes` retains **Use Joint Landmarks as Directional Cross-Axes** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_bammes_construct_knee_from_rolling_joint_mechanics` retains **Construct Knee Form From Rolling Joint Mechanics** as a bounded alternative; use it only under the conditions recorded in the variant metadata.
