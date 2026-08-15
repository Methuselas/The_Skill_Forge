---
object_id: PAT_read_quadruped_locomotion_from_support_swing_and_suspension_phases
object_type: pattern
name: Read Quadruped Locomotion From Support, Swing, and Suspension Phases
library_path:
- art
- drawing
- subjects
- animals
- gesture-locomotion
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_track_animal_motion_through_moving_pivots_and_overlapping_arcs
tags:
- animal_drawing
- quadruped
- locomotion
- gait
- contact_sequence
- support
- swing
- suspension
- weight_shift
- animation
cross_links:
- rel: related_to
  target_object_id: PAT_design_pose_against_center_of_gravity
- rel: related_to
  target_object_id: PAT_distinguish_quadruped_forequarter_suspension_from_hindquarter_drive
- rel: related_to
  target_object_id: PAT_use_frame_sequence_reference_to_study_fast_action
reference:
  source_id: gottfried_bammes_artist_guide_to_animal_anatomy
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
  publish_date: '2004'
  media_type: PDF
  locator: u10, printed pp. 35, 37-39; physical pp. 33, 35-37
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Read Quadruped Locomotion From Support, Swing, and Suspension Phases

## Pattern Rule
**IF** a quadruped walk, trot, gallop, amble, or related gait has plausible-looking limbs but no coherent sense of how support is handed from one contact to the next
**THEN** strip the sequence to actual ground contacts, swinging/recovering limbs, the support line or area under the body, and any suspension phase, then check that those roles change continuously from one phase to the next before restoring contour and anatomy
**ELSE** use the simpler moving-pivot analysis when exact contact timing is not important to the drawing.

## Do
- Mark which feet are actually touching the ground before judging the pose from limb spread or silhouette.
- Separate supporting or bracing limbs from swinging/recovering limbs; a foot approaching the ground is not yet a support simply because it is low.
- Draw the support relationship under each phase—single contact, diagonal pair, same-side pair, three contacts, or no contact—so the body's placement can be checked against what is carrying it.
- Treat suspension as a phase with no ground contact, not as a generic symbol for speed; compare the phases immediately before and after it.
- Read a gait as a **sequence of changing support relationships** rather than a memorized row of leg shapes.
- Confirm exact phase order from species- and gait-specific reference when accuracy matters; Bammes's horse diagrams are a structural analysis method, not a universal timing chart for all quadrupeds.

## Don't
- Do not infer support from whichever hoof or paw is visually nearest the ground.
- Do not copy the six horse-walk phases onto another species without checking its actual gait.
- Do not assume that every fast gait must contain the same kind or duration of suspension.
- Do not hard-code Bammes's species list for ambling or his statement that locomotor thrust always comes from behind as universal animal mechanics.
- Do not let the torso remain mechanically unchanged while the support geometry beneath it changes from phase to phase.

## Checklist
- Every phase identifies the current ground contacts.
- Swinging/recovering limbs are distinguishable from weight-bearing contacts.
- The support line or area changes coherently with the feet on the ground.
- Suspension, when present, sits between plausible departure and reception phases.
- Adjacent phases preserve one animal's proportions and articulated joint chains.
- Exact gait timing is verified from appropriate reference rather than inferred from this representative horse sequence alone.

## Notes
Bammes's figs. 38-40 reduce horse walking, trotting, and galloping to a contact diagram beneath each pose. Solid contacts, swinging feet, the standing surface, and the gravity-line relationship make the phase logic readable even before surface anatomy is considered. The transferable decision is to diagnose locomotion from **support sequence plus swing/recovery and suspension**, not to memorize Bammes's horse phase silhouettes or his broader species claims.

This Pattern generalizes the support-role reading already present in Hultgren's horse-specific gait Pattern. The Hultgren object remains useful for horse study, but it now specializes this broader quadruped locomotion foundation.
