---
object_id: PAT_inbetween_motion_along_arcs_revealed_by_neighboring_frames
object_type: pattern
name: Inbetween Motion Along Arcs Revealed by Neighboring Frames
library_path:
- art
- subjects
- animation
- inbetweening
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_synthesize_temporal_movement_into_rhythmic_visual_pattern
tags:
- animation
- inbetweening
- arcs
- motion_path
- continuity
- neighboring_frames
cross_links:
- rel: related_to
  target_object_id: PAT_construct_difficult_inbetween_from_basic_shapes_before_details
- rel: related_to
  target_object_id: PAT_carry_secondary_parts_through_overlap_follow_through_and_drag
- rel: related_to
  target_object_id: PAT_track_animal_motion_through_moving_pivots_and_overlapping_arcs
reference:
  source_title: Drawn to Life, Volume One
  author: Walt Stanchfield
confidence: high
references: []
variants: []
---

# Inbetween Motion Along Arcs Revealed by Neighboring Frames

## Pattern Rule
**IF** the direct midpoint between two animation drawings would make a moving form snap, kink, or travel on an uncertain path
**THEN** inspect a wider run of neighboring states, infer the continuing motion path from those states, and place the inbetween on that path rather than averaging only the two nearest positions
**ELSE** use direct interpolation when the sequence actually establishes a straight path

## Do
- Track the same feature, mass, joint, or attachment through several surrounding drawings when the path cannot be read confidently from the immediate endpoints.
- Use the wider sequence to distinguish a true straight translation from an arc that only appears straight when two samples are viewed in isolation.
- Place intermediate positions so the moving form progresses smoothly along the recovered path while preserving its attachment and structural identity.
- Recheck the completed inbetweens against more than one neighboring drawing so a locally plausible midpoint does not create a sequence-level hitch.
- Treat the path as part of the action design; if an extreme or breakdown already establishes a directional turn, preserve that turn through the intermediate states.

## Don't
- Do not assume the geometric midpoint of two drawings is the correct motion midpoint when the action before and after them bends the path.
- Do not straighten a curved action merely because only the nearest pair of frames was compared.
- Do not redraw the moving part on an attractive arc that is unsupported by the surrounding action.
- Do not preserve the path while allowing the form's attachment, volume, or articulation to drift between states.

## Checklist
- More than the immediate endpoint pair was inspected when the path was ambiguous.
- The chosen path agrees with the directional trend of the surrounding sequence.
- Intermediate states progress smoothly without a visible kink or sudden lateral jump.
- The same form remains structurally continuous while moving along the path.
- A straight interpolation is used only when the wider sequence supports straight travel.

## Notes
Two drawings can conceal the real path of an action. A wider set of states may reveal that the apparent midpoint belongs on a continuing arc, and placing it on the straight chord between the nearest endpoints can make the motion jerk. The reliable decision is therefore sequence-based: recover the path first, then place the missing state on it.

- Check the trajectory through all important positions, not only the local neighbor pair. Organic action commonly follows arcs or compound arcs, while deliberate straight/angular travel remains valid when it serves power or design.
- The failure is accidental deviation from the intended path, not failure to make every movement circular.
