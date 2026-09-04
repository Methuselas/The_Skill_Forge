---
object_id: PAT_build_complex_storyboard_choreography_on_performed_action_foundation
object_type: pattern
name: Build Complex Storyboard Choreography on a Performed Action Foundation
library_path:
- art
- storyboarding
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
- storyboarding
- choreography
- action
- fight
- dance
- reference
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_create_task_specific_reference_when_available_material_misses_required_action
- rel: related_to
  target_object_id: PAT_translate_live_action_reference_into_story_readable_animation_extremes
- rel: related_to
  target_object_id: PAT_stage_interacting_characters_as_one_action_reaction_system
- rel: supports
  target_object_id: AP_develop_storyboard_sequence_in_progressive_directing_passes
reference:
  source_title: The Art of Storyboard
  author: Don Bluth
confidence: high
references: []
variants: []
---

# Build Complex Storyboard Choreography on a Performed Action Foundation

## Pattern Rule
**IF** a fight, dance, stunt exchange, or other multi-body action is too interdependent to invent reliably as isolated storyboard poses
**THEN** solve a coherent movement performance or reference foundation first, then direct that action into storyboard shots
**ELSE** board the simpler action directly when its mechanics and interaction are already trustworthy.

## Do
- Establish the underlying action as one coherent event before fragmenting it into shots.
- Rehearse or choreograph with performers who understand the movement when specialist physical knowledge is needed.
- Capture the performed action, or assemble suitable motion reference into a continuous action foundation, before deciding the final storyboard coverage.
- Preserve causal interaction: an attack creates a response, the response creates a counter, contact changes position, recovery creates the next opportunity, and each participant gives the other something physically possible to react to.
- After the movement works, direct it for the board: choose camera position, shot scale, cut points, emphasis, omission, compression, and staging according to story clarity rather than the reference camera.
- Emphasize the moment that proves whether an action succeeds, fails, misses, connects, reverses, or changes the advantage.
- Redesign the action for the target characters, proportions, environment, and animation style instead of copying the performers literally.
- Use `PAT_create_task_specific_reference_when_available_material_misses_required_action` when the choreography needs evidence you do not already have.
- Use `PAT_translate_live_action_reference_into_story_readable_animation_extremes` downstream when the reference must be transformed into target-character animation poses.

## Don't
- Do not invent complex choreography as a chain of disconnected "cool shots" whose bodies cannot plausibly connect.
- Do not let isolated impact poses replace the motion that makes those impacts believable.
- Do not inherit the rehearsal camera merely because that is where the performance was recorded.
- Do not treat the performer's anatomy, timing, range, or physical ability as the target character's literal motion.
- Do not let elaborate reference capture replace the dramatic objective of the fight, dance, or stunt sequence.
- Do not require performed reference for ordinary actions whose mechanics are already clear enough to board directly.

## Checklist
- The underlying choreography works as a continuous action before shot fragmentation.
- Each participant's action creates a readable physical opportunity or constraint for the next response.
- The storyboard camera is chosen for story and clarity rather than inherited from the reference setup.
- Important successes, failures, misses, contacts, recoveries, and reversals are visually provable in the selected beats.
- The target characters and environment reshape the reference rather than merely reproducing it.
- No board beat exists only because it looked impressive in reference while contributing nothing to the dramatic action.

## Notes
For a difficult fight or dance, choreograph and record the interdependent motion before translating it into storyboard sketches. The durable lesson is the order of operations: establish trustworthy action first, then decide how the audience should see it. This Pattern owns that storyboard-stage bridge from performed choreography into shot design. It does not replace the general reference-capture or animation-reference owners, which govern obtaining evidence and remapping it into final animated performance.
