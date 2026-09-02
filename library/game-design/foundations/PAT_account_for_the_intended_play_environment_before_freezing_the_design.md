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
- rel: related_to
  target_object_id: PAT_calibrate_encounters_to_their_purpose_challenge_and_response_space
- rel: related_to
  target_object_id: PAT_cover_required_production_functions_with_explicit_ownership
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
- When software can remove arithmetic, lookup, timers, derived-value propagation, or other maintenance that is not itself intended play, automate that work while keeping an inspectable explanation of the inputs and causes behind player-facing results.
- Test whether controls, components, physical space, network assumptions, or platform conventions change the cost of executing a mechanic.
- Treat required components as part of the operating cost: acquisition, availability, handling, table space, and platform support should be justified by what those components contribute to play.
- Treat remote and local play as different environments when information flow, components, or social cues materially change.
- Revisit environment assumptions before manufacturing, implementation, or content production makes changes expensive.
- Treat the rules-delivery format as part of the operating environment when it changes retrieval or readability. Print books, searchable PDFs, small phone screens, VTT references, and other digital surfaces can impose different navigation, display, and cross-reference costs even when they contain identical rules.
- Validate the actual presentation formats the game intends to support rather than assuming that a layout or reference structure proven in one medium transfers without friction to another.
- When physical components are mandatory, test not only their table-use burden but whether they are practical to source, manufacture, package, replace, and deliver for the intended audience and release scale.
- Treat production cost, availability, shipping burden, and replacement difficulty as part of a mandatory component's operating burden; if a component materially increases price or production complexity, require a correspondingly meaningful play benefit.
- Consider simpler substitute components when the intended mechanical experience survives the substitution, and recheck unusual component requirements whenever release format or production resources change.
- In completed-game playtests, state the kind of play and content being tested so participant behavior is not being measured against expectations the test never established.
- Use safety and table-management procedures appropriate to the content, intended audience, and test environment; an unmanaged or misrepresented environment can contaminate the behavioral evidence being attributed to the game.

## Don't
- Assume a mechanic that is easy with software is equally usable when tracked by people at a table.
- Preserve manual bookkeeping in a digital implementation merely because the tabletop version required humans to perform it, or hide automated modifier/state changes so completely that players cannot understand why the outcome changed.
- Preserve a physical interaction in a digital adaptation when its value came from tactile or spatial affordances that no longer exist.
- Add platform compromises for hypothetical audiences that are outside the project’s real requirements.
- Assume that a book layout, table, spread, or navigation structure remains equally usable when moved unchanged to a different screen size or delivery format.
- Require an expensive or difficult-to-source component merely because it is distinctive; its play value must justify both use-time and production-time burden.
- Assume that self-publishing requires a traditional bulk print run; digital distribution and print-on-demand can change inventory and fulfillment risk substantially.
- Treat confusion or disengagement caused by undisclosed test expectations, inappropriate table conditions, or missing participant-support procedures as clean evidence about the game's mechanics.

## Checklist
- Every core interaction has been exercised in the intended environment.
- Required components, controls, tracking, and information visibility are practical for that environment.
- Any unusual or numerous required components are used enough, and contribute enough, to justify being mandatory.
- Automation does not conceal complexity that still creates poor decisions or feedback.
- Automated calculations and state propagation can be inspected at the level needed to understand why a result, modifier, or capability changed without requiring the player to reproduce the computation manually.
- The design has a deliberate answer for any environment it chooses not to support.
- Each intended rules-delivery format has been checked for legibility, navigation, and retrieval cost in the conditions where users will actually consult it.
- Mandatory physical components remain feasible to source, manufacture or obtain on demand, package, deliver, and replace at the intended release scale.
- The chosen release format does not impose component cost or logistics disproportionate to the play value those components provide.
- Completed-game tests establish what kind of experience and content are being tested and use table procedures appropriate to that environment.
- Test notes can distinguish friction produced by the game from friction produced by the conditions under which the test was run.

## Notes
The medium through which players execute rules changes which mechanics are viable. Technology may remove bookkeeping or expose new interactions, while physical components can create affordances software does not. Required components therefore carry acquisition, availability, handling, space, platform, production, and delivery costs in addition to their mechanical function. Automation also changes the economics of complexity: a lookup-heavy or state-heavy procedure that burdens humans may be cheap for software to execute, though automation does not excuse poor player-facing decisions or feedback. Environment is therefore part of the constraint set before a mechanic is considered finished. Chapter 19 extends that constraint beyond components and controls to the rules artifact itself: identical content can have different operating costs in a printed spread, searchable PDF, phone-sized display, or VTT reference surface. Supporting a medium therefore means validating the information interface in that medium, not merely exporting the same pages into it. Publication extends the same reasoning into acquisition: if the game requires a component, somebody ultimately has to obtain it. Digital distribution and print-on-demand can reduce the need for creator-held inventory, while custom components may still create manufacturing, packaging, replacement, and price burdens that must pay rent in play. The social and procedural conditions of a playtest are part of that environment as well. Expectations, content framing, and appropriate safety or table-management procedures help ensure that observed behavior is evidence about the game rather than an artifact of a poorly controlled test session.
