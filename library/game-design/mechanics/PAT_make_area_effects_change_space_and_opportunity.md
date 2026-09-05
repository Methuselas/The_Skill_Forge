---
object_id: PAT_make_area_effects_change_space_and_opportunity
object_type: pattern
name: Make Area Effects Change Space and Opportunity
library_path:
- game-design
- mechanics
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- combat
- area-effects
- movement
- tactics
- control
cross_links:
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: related_to
  target_object_id: PAT_calibrate_encounters_to_their_purpose_challenge_and_response_space
- rel: related_to
  target_object_id: PAT_use_time_to_structure_opportunity
reference:
  source_title: Cyberpunk 2020 (2.0.2.0 Version)
  author: Mike Pondsmith and R. Talsorian Games contributors
confidence: high
references: []
variants: []
---

# Make Area Effects Change Space and Opportunity

## Pattern Rule
**IF** an area attack, suppression effect, hazard, zone, or field is meant to justify additional tactical procedure
**THEN** make it change routes, positions, timing, exposure, coordination, or available actions for characters inside or near the affected space
**ELSE** treat it as a simpler damage/effect calculation when the area does not create a different decision environment.

## Do
- Let the effect create hazardous or privileged space that characters may avoid, cross, contest, wait out, reinforce, or neutralize.
- Tie resolution to the decision that activates the danger when possible; a hazardous zone need not make repeated rolls until someone enters, remains in, or interacts with it.
- Reward coordination when multiple effects overlap or shape routes in ways players can intentionally exploit.
- Make the geometry legible enough that players can plan rather than discover the effect only after committing.
- Compare the added procedure against the new movement and positioning decisions it creates.

## Don't
- Add an area-fire subsystem that only multiplies damage while leaving movement and positioning unchanged.
- Resolve every possible target in the zone when only characters who choose to interact with the zone need immediate processing.
- Hide the effective area so completely that players cannot make informed route or timing decisions unless uncertainty is itself the intended challenge.

## Checklist
- The area changes at least one route, position, timing, exposure, or coordination decision.
- Characters can choose among multiple responses to the zone.
- Resolution activates at a clear interaction trigger rather than through unconditional repeated upkeep when possible.
- The extra operator work is lower than or proportional to the additional tactical decisions produced.
- Removing the spatial consequence would materially reduce the purpose of the subsystem.

## Notes
Area effects earn complexity most clearly when they reshape the opportunity map. Suppressive fire, fire, gas, magical zones, overwatch, alarms, and environmental hazards can all create terrain-like state. The important output is not only damage; it is a changed set of safe, risky, delayed, or coordinated choices.
