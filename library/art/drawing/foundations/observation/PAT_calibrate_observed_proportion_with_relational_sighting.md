---
object_id: PAT_calibrate_observed_proportion_with_relational_sighting
object_type: pattern
name: Calibrate Observed Proportion With Relational Sighting
library_path:
- art
- drawing
- foundations
- observation
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- observation
- measurement
- proportion
- sighting
- placement
cross_links:
- rel: related_to
  target_object_id: PAT_map_observed_subject_as_interlocking_positive_and_negative_shapes
- rel: related_to
  target_object_id: PAT_use_perceptual_wrongness_as_inspection_trigger
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants:
- variant_id: VAR_loomis_center_out_live_figure_survey
  variant_name: Center-Out Live-Figure Survey
  variant_basis: method_sequence
  difference_from_foundation: Applies relational sighting to a standing live figure by fixing overall height and width, establishing a center and major divisions, then expanding outward through horizontal levels, vertical plumbs, and sighted angle continuations.
  when_to_use: Use when an observed figure needs accurate Stage 1 placement without reducing the pose to traced contour fragments.
  when_not_to_use: Do not impose the live-model survey as a mandatory invention workflow when no reference is being copied.
  absorbed_from_object_id: PAT_calibrate_observed_proportion_with_relational_sighting
- variant_id: VAR_loomis_switch_reclining_measurement_to_pose_specific_relations
  variant_name: Switch Reclining Measurement to Pose-Specific Relations
  variant_basis: method_sequence
  difference_from_foundation: When perspective compresses the body so severely that normal head-count standards stop being informative, retain overall height/width, center/quarter checks, and local comparative distances that belong to the observed pose itself.
  when_to_use: Use for reclining or strongly foreshortened observed figures whose projected proportions no longer resemble an upright head-unit chart.
  when_not_to_use: Do not abandon structural proportion entirely; switch from canonical upright ratios to pose-specific projected relationships, not from measurement to guesswork.
  absorbed_from_object_id: none
- variant_id: VAR_vilppu_crosscheck_3d_construction_with_2d_shape_survey
  variant_name: Cross-Check 3D Construction With a 2D Shape Survey
  variant_basis: method_sequence
  difference_from_foundation: Alternates volumetric analysis with flat observational checks using height/width, verticals, horizontals, diagonals, arcs, and positive/negative shapes; disagreement exposes placement or proportion drift.
  when_to_use: Use when a volumetrically convincing drawing no longer matches the observed pose, or when a measured silhouette has become flat and structurally unconvincing.
  when_not_to_use: Do not choose 2-D or 3-D as a permanent winner; the variant exists to cross-check both readings.
  absorbed_from_object_id: none
- variant_id: VAR_bammes_reorient_reclining_figure_with_longitudinal_and_cross_axes
  variant_name: Reorient a Reclining Figure With Longitudinal and Cross Axes
  variant_basis: method_sequence
  difference_from_foundation: Uses the projected body mid-axis and a small set of transverse stations through major structural levels to organize a reclining body in depth before inserting core masses and limbs.
  when_to_use: Use for lying or strongly foreshortened figures from life or fixed reference when the body is hard to orient as one coherent spatial object.
  when_not_to_use: Do not turn every minor joint into an equal measuring station; keep only axes that materially clarify depth.
  absorbed_from_object_id: none
- variant_id: VAR_dodson_draw_by_eye_then_measure_and_correct
  variant_name: Draw by Eye, Then Measure and Correct
  variant_basis: method_sequence
  difference_from_foundation: Begins with an observational estimate, then uses sighting to diagnose and restate proportion before returning to the eye; measuring becomes a calibration pass rather than a substitute for seeing.
  when_to_use: Use when excessive premeasurement makes observational drawing rigid, or when the eye needs objective checks after a first placement.
  when_not_to_use: Do not postpone all measurement until the end when a known high-sensitivity relationship is already drifting.
  absorbed_from_object_id: none
- variant_id: VAR_dodson_increase_check_density_when_tolerance_is_small
  variant_name: Increase Check Density When Tolerance Is Small
  variant_basis: emphasis
  difference_from_foundation: Concentrates more plumb, level, midpoint, and comparative checks where small errors strongly affect likeness or compressed foreshortened relationships, while allowing looser checking where tolerance is larger.
  when_to_use: Use for portrait likeness, tight feature spacing, severe foreshortening, or other relationships where a small error materially changes the read.
  when_not_to_use: Do not survey every low-sensitivity passage with equal intensity when the task benefits from spontaneity or broader observation.
  absorbed_from_object_id: none
- variant_id: VAR_mogilevtsev_run_pre_detail_portrait_landmark_axis_audit
  variant_name: Run a Pre-Detail Portrait Landmark-Axis Audit
  variant_basis: method_sequence
  difference_from_foundation: >-
    Places a dense portrait-specific relational audit at the transition from a resolved sketch into feature modeling: restore the facial centerline, lay transverse guides through sensitive landmarks, compare paired placements, then cross-check head bend with ear/feature relations and facial angle before committing to local detail.
  when_to_use: Use when an observed portrait sketch is about to enter expensive feature modeling and small placement drift could damage likeness or head attitude.
  when_not_to_use: Do not preserve the guide network as a mandatory finish or apply the same check density to a freer drawing whose low-sensitivity passages benefit from spontaneity.
  absorbed_from_object_id: none
- variant_id: VAR_mogilevtsev_run_pre_detail_figure_axis_and_support_audit
  variant_name: Run a Pre-Detail Figure Axis-and-Support Audit
  variant_basis: method_sequence
  difference_from_foundation: >-
    Adds Mogilevtsev's figure-specific audit at the sketch-to-detail transition: identify the actual stationary support, use the source's one-leg suprasternal plumb as a quick steadiness and head/shoulder relation check, restore the body centerline, then lay only the major perspective-aware axes through head, torso, pelvis, and knees before rechecking symmetry and proportion.
  when_to_use: Use when an observed long-figure sketch is about to enter expensive local modeling and balance, orientation, or large proportional drift may still be hiding beneath a plausible surface sketch.
  when_not_to_use: Do not treat the suprasternal-notch-to-foot plumb as a universal center-of-gravity law; dynamic, two-leg, seated, braced, suspended, or externally supported poses require their actual support mechanics, and the guide network should be dropped once the large audit has done its job.
  absorbed_from_object_id: none
---

# Calibrate Observed Proportion With Relational Sighting

## Pattern Rule
**IF** an observed subject must be placed or proportioned accurately without replacing looking with a fixed formula
**THEN** establish large shape and placement, test midpoint or major divisions, then use plumb, level, and comparative measurements as relational checks against the subject before returning to visual judgment
**ELSE** use freer construction when exact observational correspondence is not the task

## Do
- Regard proportions as relationships among parts and between parts and the whole rather than as isolated dimensions.
- Use the midpoint early to solve a large proportional division and to prevent the drawing from running out of page or floating at the wrong scale.
- Hold the sighting tool at a consistent arm length and viewpoint so repeated comparisons mean the same thing.
- Use vertical and horizontal alignments to locate several landmarks from one relationship and to clarify the action of a pose.
- Let any useful span become a temporary comparative unit; keep that measurement as a ratio within the subject rather than transferring its physical size directly to the page.

## Don't
- Do not assume a canonical proportion chart describes the current projection of a slouched, reclining, or foreshortened subject.
- Do not let measurement overpower the drawing process; pepper the work with checks where they answer a real uncertainty.
- Do not use inconsistent eye position, elbow bend, or pencil distance and then treat the readings as objective.
- Do not preserve a measured relation that still looks wrong without rechecking the anchors and viewpoint.

## Checklist
- Overall placement and midpoint are plausible before small relationships are measured.
- Important landmarks can be checked by more than one relation: plumb, level, midpoint, angle, or comparative span.
- The chosen measurement density matches the sensitivity of the task.
- The eye gets the final chance to judge the correction after measuring.

## Notes
Dodson frames sighting as objective calibration added to an already developing eye. The procedure is deliberately mixed with gesture, restatement, blind observation, erasing, and other drawing behavior rather than treated as a rigid step-by-step system. `VAR_loomis_center_out_live_figure_survey` retains the original figure-specific Loomis route. `VAR_loomis_switch_reclining_measurement_to_pose_specific_relations` handles severe projected compression. `VAR_vilppu_crosscheck_3d_construction_with_2d_shape_survey` alternates volumetric and flat checks. `VAR_bammes_reorient_reclining_figure_with_longitudinal_and_cross_axes` uses a depth-oriented axis scaffold. `VAR_dodson_draw_by_eye_then_measure_and_correct` makes search precede calibration, `VAR_dodson_increase_check_density_when_tolerance_is_small` concentrates verification where small errors matter most, `VAR_mogilevtsev_run_pre_detail_portrait_landmark_axis_audit` inserts a portrait-specific relational audit immediately before local feature modeling, and `VAR_mogilevtsev_run_pre_detail_figure_axis_and_support_audit` adds the corresponding figure-stage audit while bounding the source's one-leg support plumb as a context-specific diagnostic rather than a universal balance law.
