---
object_id: PAT_define_completion_against_a_living_game_design_document
object_type: pattern
name: Define Completion Against a Living Game Design Document
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
- scope
- completion
- gdd
- iteration
cross_links:
- rel: related_to
  target_object_id: PAT_define_the_intended_player_before_designing_for_them
- rel: related_to
  target_object_id: PAT_make_the_game_operable_without_hidden_designer_knowledge
- rel: related_to
  target_object_id: AP_run_an_evidence_driven_playtest_revision_cycle
- rel: related_to
  target_object_id: PAT_cover_required_production_functions_with_explicit_ownership
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Define Completion Against a Living Game Design Document

## Pattern Rule
**IF** a game contains multiple interacting systems, content domains, interfaces, or production requirements
**THEN** maintain a living game design document or equivalent specification that identifies the intended experience, required fundamentals, dependencies, scope, and completion criteria for the current version, and measure design completion against that specification
**ELSE** use a lighter checklist or specification as long as the required fundamentals and completion conditions are still explicit.

## Do
- Define the intended game's fundamentals before they disappear into scattered notes, disconnected documents, or hidden designer memory.
- Include enough specification to establish, as appropriate, the intended player and experience, genre or world requirements, core activity or play structure, resolution systems, player capabilities, progression or resources, adversaries or challenges, required components and interfaces, major content domains, dependencies among systems, and production or release requirements that belong to the intended version.
- Distinguish required fundamentals for the current version from desirable additions, experiments, expansions, stretch goals, and backlog ideas.
- Keep the GDD living: revise the specification when evidence shows that the design itself should change.
- When a fundamental changes, trace the dependencies that must be reconsidered rather than treating the edit as isolated.
- Define what counts as complete for each fundamental instead of relying on vague states such as "mostly done."
- Treat the design as complete when every required fundamental for the current version is specified, implemented or documented, integrated with its dependencies, and testable as part of the whole.
- Treat release readiness as a later gate that can additionally require playtesting, regression testing, independent operability, editing, production, and delivery validation.
- Once the defined fundamentals are complete, classify new ideas honestly as revisions, enhancements, expansions, optional modules, or next-version work rather than automatically reopening the current design.
- Preserve recoverable versions of both the game and its design document through major revisions.
- Use the defined scope to distinguish a missing fundamental from a merely absent feature. A game can be complete without supporting every activity its setting could conceivably contain.
- Treat a module as genuinely optional only when removing it leaves the defined base game complete and executable; optionality is a dependency claim, not just a label.
- When the current version exposes a player-facing capability whose required procedure is deferred to future work, either supply enough support now to make the capability usable or classify it explicitly as a future hook rather than completed current-version functionality.

## Don't
- Treat the GDD as an immutable prophecy that cannot change after development begins.
- Treat the GDD as a novel or speculative encyclopedia full of features the current game may never need.
- Allow fundamental requirements to remain only in the creator's head.
- Add new "fundamentals" indefinitely merely because another idea occurred during development.
- Confuse time already invested in a feature with its importance to the intended game.
- Continue implementing dependent material when a known foundational defect makes that work predictably disposable.
- Let local polishing prevent progress toward a testable whole.
- Refuse necessary foundational redesign merely because a draft is not yet complete.
- Declare the design unfinished merely because further improvement is possible.
- Declare a product release-ready merely because all design-document boxes are checked.
- Treat player requests for additional systems as proof that the current version was incomplete when those systems were outside its defined fundamentals.
- Call a module optional when the base game becomes incomplete, unbalanced, or non-executable after that module is removed.
- Present an announced future subsystem as current completed support when users can select or depend on the feature before its required procedure exists.

## Checklist
- The current version has an explicit scope and intended experience.
- Every required fundamental is named somewhere recoverable rather than existing only in designer memory.
- Each fundamental has a concrete completion condition.
- Dependencies among major systems are visible enough that a foundational change can be traced.
- Optional, expansion, and next-version ideas are distinguishable from current-version requirements.
- All current-version fundamentals are specified, implemented or documented, integrated, and testable as a whole before the design is called complete.
- Release readiness is evaluated separately from design completeness.
- Major revisions preserve recoverable prior states of both implementation and specification.
- The project can explain why an absent feature is either a missing fundamental or intentionally outside the current version's scope.
- Every module labeled optional can be removed while the defined base game still executes its promised experience.
- Every future-facing hook is distinguishable from current functionality, and no current required capability depends on an unpublished or undefined procedure.
- The design-completion gate is explicit: fundamentals defined -> fundamentals implemented -> dependencies integrated -> whole testable.
- The release-readiness gate is separate: design complete + required validation and production gates.

## Notes
Completeness is measured against the defined scope of the current version, not against every feature the game could conceivably support. A complete game can later gain expansions without retroactively becoming an incomplete original game. Optional modules follow the same logic at a smaller scale: removing an option should leave the defined base experience intact, while a feature that depends on future rules is a roadmap hook rather than current completed functionality.

*Star Frontiers: Alpha Dawn* is a useful example. It supplied a complete science-fiction roleplaying game for planetary adventure even though player characters could not yet pilot or operate starships as a full subsystem. *Knight Hawks* later expanded the product line into starship design, spaceship skills, space movement, combat, and campaign play. The later expansion added desirable scope; its existence does not mean *Alpha Dawn* lacked a complete original design.

Do not let "finish the draft before editing" become a ban on necessary redesign. The useful distinction is between foundational correction and premature polishing. Fix architecture that is known to be wrong; do not spend endless effort perfecting isolated fragments while required fundamentals remain missing.

Finish the specification. Finish the fundamentals. Validate the whole. Then stop calling optional improvement unfinished design.
