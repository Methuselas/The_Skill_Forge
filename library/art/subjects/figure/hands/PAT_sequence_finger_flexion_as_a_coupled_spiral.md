---
object_id: PAT_sequence_finger_flexion_as_a_coupled_spiral
object_type: pattern
name: Sequence Finger Flexion as a Coupled Spiral
library_path:
- art
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
  source_title: Drawing Dynamic Hands
  author: Burne Hogarth
confidence: high
references: []
variants:
- variant_id: VAR_bridgman_wrist_flexion_limits_finger_closure
  variant_name: Let Wrist Flexion Constrain Finger Closure
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a wrist-to-finger coupling check to the existing staged flexion model: as the wrist folds
    strongly toward the palm, the extensor system is drawn taut across the dorsal wrist, so full finger closure becomes mechanically
    incompatible with extreme wrist flexion.'
  when_to_use: Use when designing a fist, grasp, claw, or compressed hand pose with a strongly flexed wrist and the fingers
    appear able to close more than the carrying wrist position permits.
  when_not_to_use: Do not turn the source's endpoint demonstration into a universal numeric angle law; use it as a coupled
    movement constraint and judge the actual pose.
  absorbed_from_object_id: none
- variant_id: VAR_bridgman_hundred_hands_stage_digit_curl_from_knuckle_outward
  variant_name: Stage Each Digit Curl From the Knuckle Outward
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a within-digit construction order to the existing across-finger coupled sequence: start
    a curling finger at the metacarpophalangeal knuckle, then articulate the successive joints outward toward the tip, while
    the foundation still controls how neighboring fingers recruit and stagger across the hand.'
  when_to_use: Use when one bent finger looks kinked, disconnected, or as if its distal joints were posed independently of
    its base, especially inside a fist, hook, or partial grasp.
  when_not_to_use: Do not treat the sequence as a literal universal timing law; real/reference motion can flex several joints
    together or isolate a distal joint, and the source-specific order is best used as a construction and diagnosis scaffold.
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
- After posing the local chains, check the four-finger group against the thumb and wrist as one mechanism; if the combined flexion pattern produces contradictory crossings, implausible relative fingertip placement, or an obviously strained read, revise the group rather than preserving each finger independently.
- When a finger curls deeply toward or behind the palm, preserve its root-to-tip joint chain and distal/nail plane where that plane is needed to explain orientation; hide the chain by overlap rather than driving it through the palm mass or detaching it from the hand.

## Don't
- Curl all four long fingers by the same amount at the same instant.
- Infer that no finger can ever move independently.
- Turn the staged fist example into an unsupported universal ranking for every hand action.

## Checklist
- Neighboring long fingers show a readable staggered flexion order instead of identical simultaneous closure.
- The closing or opening group follows a coherent spiral or fan behavior rather than four isolated hinge actions.
- Every required curling digit traces continuously from one palm root through its joints to its tip.
- Hidden digit paths pass plausibly behind the palm or neighboring forms rather than through them or detaching from the hand.
- The long-finger group, thumb where present, palm, and wrist coexist as one mechanically attainable hand configuration.

## Notes
Finger closure reads more naturally when the digit group shares a staggered directional relationship while preserving any intentional independent action.

`VAR_bridgman_wrist_flexion_limits_finger_closure` retains **Let Wrist Flexion Constrain Finger Closure** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_bridgman_hundred_hands_stage_digit_curl_from_knuckle_outward` retains **Stage Each Digit Curl From the Knuckle Outward** as a bounded alternative; use it only under the conditions recorded in the variant metadata.
