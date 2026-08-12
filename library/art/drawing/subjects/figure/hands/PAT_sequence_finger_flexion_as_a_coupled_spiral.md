---
object_id: PAT_sequence_finger_flexion_as_a_coupled_spiral
object_type: pattern
name: Sequence Finger Flexion as a Coupled Spiral
library_path:
- art
- drawing
- subjects
- figure
- hands
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: PAT_construct_hand_from_palm_wedge_and_digit_chain
tags:
- hand
- fingers
- fist
- biomechanics
cross_links:
- rel: related_to
  target_object_id: PAT_construct_hand_from_palm_wedge_and_digit_chain
reference:
  source_id: burne_hogarth_drawing_dynamic_hands
  source_title: Drawing Dynamic Hands
  author: Burne Hogarth
  publish_date: '1977'
  media_type: book
  locator: ch05, printed pp. 77-81
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_bridgman_wrist_flexion_limits_finger_closure
  variant_name: Let Wrist Flexion Constrain Finger Closure
  variant_basis: method_sequence
  source_id: george_bridgman_constructive_anatomy
  source_title: Constructive Anatomy
  locator: u02, physical pp. 19-20
  difference_from_foundation: 'Adds a wrist-to-finger coupling check to the existing staged flexion model: as the wrist folds strongly toward the palm, the extensor system is drawn taut across the dorsal wrist, so full finger closure becomes mechanically incompatible with extreme wrist flexion.'
  when_to_use: Use when designing a fist, grasp, claw, or compressed hand pose with a strongly flexed wrist and the fingers appear able to close more than the carrying wrist position permits.
  when_not_to_use: Do not turn the source's endpoint demonstration into a universal numeric angle law; use it as a coupled movement constraint and judge the actual pose.
  absorbed_from_object_id: none
- variant_id: VAR_bridgman_hundred_hands_stage_digit_curl_from_knuckle_outward
  variant_name: Stage Each Digit Curl From the Knuckle Outward
  variant_basis: method_sequence
  source_id: george_bridgman_book_of_a_hundred_hands
  source_title: The Book of a Hundred Hands
  locator: u00, physical pp. 13 and 118; printed pp. 17 and 122
  difference_from_foundation: 'Adds a within-digit construction order to the existing across-finger coupled sequence: start a curling finger at the metacarpophalangeal knuckle, then articulate the successive joints outward toward the tip, while the foundation still controls how neighboring fingers recruit and stagger across the hand.'
  when_to_use: Use when one bent finger looks kinked, disconnected, or as if its distal joints were posed independently of its base, especially inside a fist, hook, or partial grasp.
  when_not_to_use: Do not treat the sequence as a literal universal timing law; real/reference motion can flex several joints together or isolate a distal joint, and the source-specific order is best used as a construction and diagnosis scaffold.
  absorbed_from_object_id: none
---

# Sequence Finger Flexion as a Coupled Spiral

## Pattern Rule
**IF** several fingers are closing toward the palm or opening from a fist
**THEN** stage them as a coupled, graduated sequence rather than four identical hinges moving together: closure begins on the little-finger side and recruits neighboring fingers toward the index, while opening reverses the overall sequence
**ELSE** preserve whatever independent digit action the pose actually requires

## Do
- Let the little-finger side lead early fist closure.
- Build the closing fingertips toward the palm hollow as a converging spiral.
- Let neighboring digits be visibly related instead of posing every finger as an isolated mechanism.
- Treat the index as later in closure and the thumb as the final enclosing/opposing member.
- Reverse the overall sequence when designing the fist opening.

## Don't
- Curl all four long fingers by the same amount at the same instant.
- Infer that no finger can ever move independently.
- Turn the staged fist example into an unsupported universal ranking for every hand action.

## Checklist
If the closing hand looks like four cloned finger animations attached to a palm, restore the staggered sequence and spiral.

## Notes
Finger closure reads more naturally when the digit group shares a staggered directional relationship while preserving any intentional independent action.

`VAR_bridgman_wrist_flexion_limits_finger_closure` retains **Let Wrist Flexion Constrain Finger Closure** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_bridgman_hundred_hands_stage_digit_curl_from_knuckle_outward` retains **Stage Each Digit Curl From the Knuckle Outward** as a bounded alternative; use it only under the conditions recorded in the variant metadata.
