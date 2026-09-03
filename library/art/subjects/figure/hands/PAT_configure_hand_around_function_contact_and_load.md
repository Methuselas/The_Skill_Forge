---
object_id: PAT_configure_hand_around_function_contact_and_load
object_type: pattern
name: Configure the Hand Around Function, Contact, and Load
library_path:
- art
- subjects
- figure
- hands
stage_binding: 3 rough
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: PAT_construct_hand_from_palm_wedge_and_digit_chain
tags:
- hand
- function
- contact
- load
cross_links:
- rel: related_to
  target_object_id: PAT_construct_hand_from_palm_wedge_and_digit_chain
- rel: related_to
  target_object_id: PAT_orient_thumb_by_opposition_and_rotation
- rel: related_to
  target_object_id: PAT_reveal_hand_structure_through_surface_stress
reference:
  source_title: Drawing Dynamic Hands
  author: Burne Hogarth
confidence: high
references: []
variants:
- variant_id: VAR_dynamic_hands_ch11_object_constraint_and_reference_fidelity
  variant_name: Let the Instrument Constrain the Hand
  variant_basis: method_sequence
  difference_from_foundation: Extends the function/contact/load rule into occupation-specific drawing by establishing the
    tool or instrument first when it constrains the action, then solving an explicit contact chain from object axis through
    palm orientation, thumb opposition, active digits, support digits, palm contact, wrist axis, and forearm before final
    contour. It also calls for stronger reference fidelity for unfamiliar operations than for familiar actions.
  when_to_use: Use when a hand is working with a rigid instrument, tool, machine, or specialized procedure whose geometry
    or technique restricts plausible hand placement.
  when_not_to_use: Do not over-constrain free expressive hand actions or use occupational reference as a substitute for the
    underlying palm/digit construction.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_pre_shape_hand_to_object_contour_before_grasp
  variant_name: Pre-Shape the Hand to the Object Before Contact
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Loomis''s anticipatory-grasp study: inspect the object''s contour first, then watch how
    the hand begins matching that contour just before contact so the grasp is designed as an approach into contact rather
    than a generic pose pasted onto the object afterward.'
  when_to_use: Use when drawing a hand about to pick up, catch, cup, or close around a known object and the fingers need a
    believable pre-contact configuration.
  when_not_to_use: Do not force the final grip shape onto the hand too early when the action is still distant from contact,
    and do not replace the underlying palm/digit construction with contour tracing.
  absorbed_from_object_id: none
- variant_id: VAR_bridgman_hundred_hands_rest_on_ulnar_heel
  variant_name: Seat a Resting Hand on the Ulnar Heel
  variant_basis: context
  difference_from_foundation: 'Specializes the function/contact/load rule for passive support: when a relaxed hand simply
    rests on a plane, establish the little-finger-side heel/pisiform as the primary contact, let the thenar mass accept secondary
    thumb-side pressure, and preserve some natural digit arch instead of flattening the whole palm and fingers equally.'
  when_to_use: Use for relaxed or lightly supported hands resting on a table, floor, body, or other broad plane when the contact
    pattern needs to feel weighted without becoming an active brace or grip.
  when_not_to_use: Do not force this contact map onto pushing, bracing, gripping, injured, highly rotated, or reference-specific
    hands; actual task and observed pressure distribution override the passive-rest default.
  absorbed_from_object_id: none
---

# Configure the Hand Around Function, Contact, and Load

## Pattern Rule
**IF** the hand is performing a task, contacting an object, or carrying load
**THEN** let the required function determine the hand's configuration: align the palm and digits to the force direction, choose which surfaces bear contact, and let the fingers/thumb adapt around the external shape or support demand
**ELSE** do not invent arbitrary tension or grip behavior just to make the hand look active

## Do
- Identify what the hand is doing before choosing the final finger pose.
- Distinguish striking/prying actions from hooking, pinching, supporting, cupping, bracing, or digging by their different contact surfaces and force directions.
- Let a held or contained object govern the local contour where the hand must wrap around it.
- For a rigid instrument, solve the contact chain before contour: object axis → palm orientation → thumb opposition → active digit or digits → support-digit wrap → palm contact → wrist axis → forearm. Keep every visible digit traceable to one base even when several fingers compress around the same grip.
- In support actions, spread or brace the digits so the load path reads from contact points through palm and wrist.
- In precision actions, reduce contact to the digits actually needed and keep unnecessary fingers from competing with the task.
- Use surface-stress cues only where the functional load would actually reveal them.

## Don't
- Pose the fingers first and assign a function afterward.
- Make every grip a fist.
- Fuse the support fingers into an undifferentiated mitten around a rigid grip when their roots, knuckles, or separate contact roles should remain readable.
- Ignore the shape or stiffness of the contacted object.
- Add equal tension to every finger regardless of which digits carry the force.
- Treat a supporting hand and a grasping hand as the same mechanical problem.

## Checklist
- The task or function is identifiable from the hand configuration without relying on a label.
- A contacted object's axis, shape, and stiffness visibly constrain palm and digit placement.
- Active and support digits have distinct contact roles where the task requires them.
- Every visible digit traces to one plausible root even when several compress around the same object.
- Contact points create a coherent force path through palm, wrist, and forearm.
- The hand appears mechanically engaged with the object or support rather than merely posed around it.

## Notes
The hand should inherit its pose from what it is doing: contact, load, object shape, and intended action constrain the configuration before decorative gesture does.

The `VAR_dynamic_hands_ch11_object_constraint_and_reference_fidelity` variant adds an occupation-specific order of operations: establish the constraining instrument or procedure first, then map object axis, palm facing, thumb opposition, active and support digits, palm contact, wrist axis, and forearm before final contour. Increase reference fidelity as the action becomes less familiar or more technically constrained.

`VAR_dynamic_hands_ch11_object_constraint_and_reference_fidelity` retains **Let the Instrument Constrain the Hand** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_loomis_pre_shape_hand_to_object_contour_before_grasp` retains **Pre-Shape the Hand to the Object Before Contact** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_bridgman_hundred_hands_rest_on_ulnar_heel` retains **Seat a Resting Hand on the Ulnar Heel** as a bounded alternative; use it only under the conditions recorded in the variant metadata.
