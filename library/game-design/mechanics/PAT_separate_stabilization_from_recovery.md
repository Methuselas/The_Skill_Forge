---
object_id: PAT_separate_stabilization_from_recovery
object_type: pattern
name: Separate Stabilization from Recovery
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
- injury
- recovery
- time
- medicine
- persistent-state
cross_links:
- rel: related_to
  target_object_id: PAT_match_the_cost_of_failure_to_the_players_prior_investment
- rel: related_to
  target_object_id: PAT_use_time_to_structure_opportunity
- rel: related_to
  target_object_id: PAT_use_maintenance_to_trade_present_effort_for_future_reliability
reference:
  source_title: Cyberpunk 2020 (2.0.2.0 Version)
  author: Mike Pondsmith and R. Talsorian Games contributors
confidence: high
references: []
variants: []
---

# Separate Stabilization from Recovery

## Pattern Rule
**IF** an injury, breakdown, or other deteriorating state is supposed to create consequences beyond the immediate scene
**THEN** let emergency intervention stop worsening or preserve the asset without automatically erasing the damage, then resolve recovery through its own time, resource, access, and participation decisions
**ELSE** collapse stabilization and recovery when persistent aftermath is not part of the intended experience.

## Do
- Give immediate responders a broadly accessible way to prevent catastrophic loss when specialist absence would otherwise hard-lock the group.
- Let specialists improve long-term outcomes, recovery rate, replacement options, restoration quality, or access to advanced treatment rather than monopolizing basic survival.
- Make recovery time collide with jobs, deadlines, obligations, finances, threats, or other campaign pressures when time is meant to matter.
- Allow money or rare resources to buy **campaign time** when accelerated recovery is a meaningful economic choice.
- Preserve injuries or damaged components that ordinary healing cannot erase when replacement or redesign should become a later character/asset decision.
- Check persistent character consequence against player participation; a coherent month-long recovery can still be bad play if one player has no meaningful decisions.

## Don't
- Treat one successful emergency roll as full restoration when persistent injury is part of the promised danger.
- Require repeated daily resolution when the only meaningful decision is treatment choice and elapsed time.
- Make a healer or repair specialist mandatory for basic survival unless that hard dependency is intentional and supported by party construction.
- Defend long recovery solely as realism without showing what decisions the time pressure creates.

## Checklist
- Stabilization and restoration answer different questions.
- Emergency success preserves rather than deletes the underlying consequence.
- Long-term recovery has at least one meaningful time, access, resource, or build implication.
- Specialist competence improves outcomes without making basic emergency response impossible for everyone else unless intentionally designed.
- Player-level TBMD during long recovery has been considered explicitly.

## Notes
Persistent consequence is strongest when it creates stages: stop the loss, treat the damage, recover capability, then replace or adapt if necessary. This architecture lets violence or failure remain part of the campaign economy without requiring exhaustive medical or maintenance simulation. Time becomes a resource, and advanced services become meaningful because they change when the character or asset can re-enter play rather than merely erasing a number.
