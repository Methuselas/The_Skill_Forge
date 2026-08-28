---
object_id: PAT_select_bird_flight_mode_by_available_source_of_lift_and_propulsion
object_type: pattern
name: Select Bird Flight Mode by Available Source of Lift and Propulsion
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
foundation_object_id: PAT_read_animal_locomotion_as_a_functional_performance_tradeoff
tags:
- animal_drawing
- bird
- flight
- powered_flight
- gliding
- soaring
- hovering
- lift
- propulsion
cross_links:
- rel: related_to
  target_object_id: PAT_animate_flapping_bird_flight_from_power_recovery_and_body_response
- rel: related_to
  target_object_id: PAT_match_bird_wing_planform_to_flight_performance_tradeoffs
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Select Bird Flight Mode by Available Source of Lift and Propulsion

## Pattern Rule
**IF** a bird's flight action is being planned
**THEN** identify whether lift and forward motion come primarily from active wingbeats, existing forward airflow, rising external air, or a hovering solution, and animate that mode's distinct energy source instead of treating all airborne motion as generic flapping

## Do
- Use powered flight when the bird must actively supply repeated thrust and lift with wingbeats.
- Use gliding when existing airspeed can support the bird with held wings while forward speed is gradually traded away.
- Use soaring when external rising air supplies enough lift that the bird can remain aloft with comparatively small corrective wing movements.
- For hovering, identify the actual mechanism: very rapid repeated wing action can generate lift in still air, while some birds can face into a headwind and use the moving air with small corrections.
- Mix modes when the bird's behavior and energy economy call for it, such as powered beats alternating with glide phases.

## Don't
- Do not animate gliding or soaring as powered flight with the wingbeats merely omitted.
- Do not make hovering mechanically identical across species that use different airflow strategies.
- Do not change flight mode without changing where the sustaining lift or propulsion is coming from.

## Checklist
- The source of lift and propulsion is identifiable from the action.
- Wing motion and body attitude fit the chosen mode.
- Mode changes correspond to a change in energy source or flight problem.
- Hovering remains spatially controlled without pretending the bird has no force requirement.

## Notes
Webster describes powered flight, gliding, soaring, and hovering as distinct flight gaits. Their visible differences follow from where lift and thrust come from. A hummingbird creates the needed airflow through rapid wing motion; a kestrel can hover into a wind and use the external airflow instead.
