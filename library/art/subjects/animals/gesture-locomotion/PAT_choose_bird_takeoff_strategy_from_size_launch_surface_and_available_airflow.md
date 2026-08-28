---
object_id: PAT_choose_bird_takeoff_strategy_from_size_launch_surface_and_available_airflow
object_type: pattern
name: Choose Bird Takeoff Strategy From Size, Launch Surface, and Available Airflow
library_path:
- art
- subjects
- animals
- gesture-locomotion
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_select_bird_flight_mode_by_available_source_of_lift_and_propulsion
tags:
- animal_drawing
- bird
- flight
- takeoff
- launch
- airflow
- running
- jumping
- water
cross_links:
- rel: related_to
  target_object_id: PAT_match_bird_wing_planform_to_flight_performance_tradeoffs
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Choose Bird Takeoff Strategy From Size, Launch Surface, and Available Airflow

## Pattern Rule
**IF** a bird must transition from support into flight
**THEN** choose a launch that builds enough airflow over the wings for that bird's size and situation, using a jump, drop, run, water taxi, headwind, or combination rather than defaulting to one universal leap-and-flap takeoff

## Do
- Let small light birds jump directly into a strong initial wingbeat when their mass and wing loading permit it.
- Use a drop or outward push from a perch or elevated edge when open space can supply immediate relative airflow.
- Give larger birds a running or water-surface acceleration phase when they need more forward speed before the wings can support their weight.
- Face the bird into useful wind when environmental airflow can reduce the amount of self-generated launch speed required.
- Coordinate leg thrust, body pitch, and first wingbeats so support is relinquished only when the bird has a plausible airborne solution.

## Don't
- Do not launch every bird vertically from flat ground with identical timing.
- Do not ignore the friction and support limits of water, land, branch, or cliff launch surfaces.
- Do not remove ground support before the wings or environmental airflow can plausibly carry the body.

## Checklist
- The launch strategy fits the bird's apparent size and wing loading.
- The support surface meaningfully affects the takeoff.
- Airflow is gained before or as the bird loses support.
- Leg, body, and wing actions cooperate instead of occurring as unrelated gestures.

## Notes
Webster's takeoff examples all solve the same requirement—obtain enough airflow for lift—but do so differently according to scale, launch surface, and wind. The reusable decision is therefore not a fixed pose sequence but the way the bird creates or acquires the airflow needed to become airborne.
