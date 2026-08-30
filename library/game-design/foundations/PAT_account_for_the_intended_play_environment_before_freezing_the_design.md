---
object_id: PAT_account_for_the_intended_play_environment_before_freezing_the_design
object_type: pattern
name: Account for the Intended Play Environment Before Freezing the Design
library_path:
- game-design
- foundations
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- medium
- controls
- components
- environment
cross_links:
- rel: related_to
  target_object_id: PAT_choose_a_game_foundation_by_the_experience_it_must_support
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Account for the Intended Play Environment Before Freezing the Design

## Pattern Rule
**IF** a game is expected to operate through a particular physical, digital, remote, local, or hybrid environment
**THEN** test its core interactions against that environment’s affordances and limitations before locking the design
**ELSE** do not compromise the core experience merely to support a delivery environment the project does not need.

## Do
- Identify what the environment can automate, display, conceal, track, manipulate, or communicate reliably.
- Test whether controls, components, physical space, network assumptions, or platform conventions change the cost of executing a mechanic.
- Treat remote and local play as different environments when information flow, components, or social cues materially change.
- Revisit environment assumptions before manufacturing, implementation, or content production makes changes expensive.

## Don't
- Assume a mechanic that is easy with software is equally usable when tracked by people at a table.
- Preserve a physical interaction in a digital adaptation when its value came from tactile or spatial affordances that no longer exist.
- Add platform compromises for hypothetical audiences that are outside the project’s real requirements.

## Checklist
- Every core interaction has been exercised in the intended environment.
- Required components, controls, tracking, and information visibility are practical for that environment.
- Automation does not conceal complexity that still creates poor decisions or feedback.
- The design has a deliberate answer for any environment it chooses not to support.

## Notes
The medium through which players execute rules changes which mechanics are viable. Technology may remove bookkeeping or expose new interactions, while physical components can create affordances software does not. Environment is therefore part of the constraint set before a mechanic is considered finished.
