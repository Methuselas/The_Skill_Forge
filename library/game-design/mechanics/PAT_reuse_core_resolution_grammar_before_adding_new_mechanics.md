---
object_id: PAT_reuse_core_resolution_grammar_before_adding_new_mechanics
object_type: pattern
name: Reuse Core Resolution Grammar Before Adding New Mechanics
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
- mechanics
- architecture
- resolution
- refactoring
cross_links:
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: related_to
  target_object_id: PAT_use_the_defining_affordances_of_an_adopted_game_system
- rel: related_to
  target_object_id: PAT_build_complete_resolution_procedures_incrementally
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Reuse Core Resolution Grammar Before Adding New Mechanics

## Pattern Rule
**IF** a new task, conflict, or gameplay domain needs resolution similar to situations the game already handles
**THEN** first express it through the existing mechanical primitives and vocabulary; extend or refactor those primitives when recurring gaps appear, and create a separate subsystem only when the activity needs a different decision structure or experience that the core grammar cannot express cleanly
**ELSE** when the activity genuinely requires different play, define the subsystem and its interfaces deliberately rather than treating it as an isolated exception.

## Do
- Map the new situation onto the existing inputs, uncertainty, consequences, and state changes before inventing a new procedure.
- Ask whether the requirement poses a genuinely new rules question or merely a new fictional instance of a question the game already answers. Add new machinery more readily for the former; require stronger justification for replacing the latter.
- When a proposed replacement mainly translates information the current grammar already expresses directly, identify the decision, clarity, pacing, uncertainty profile, or other meaningful play benefit that the translation purchases before adopting it.
- After choosing or extending the mechanical grammar, treat the complete sequencing of those mechanics as a separate design responsibility; shared primitives do not by themselves define trigger order, branches, precedence, or termination.
- Separate a change in entity detail or fictional context from a change in resolution logic; different data does not automatically require different rules.
- Prefer a reusable extension when one small addition broadens the current grammar across several related cases.
- Treat repeated adapters, exception chains, or bespoke conversions as evidence that the underlying mechanic may need refactoring.
- Treat genre supplements and specialized subsystems as possible laboratories for general mechanics: when a local solution repeatedly transfers beyond its original domain, promote the underlying concept into shared grammar, then revisit the originating subsystem for duplicate infrastructure that can be removed without erasing its distinctive play experience.
- When a specialized subsystem is justified, define how play enters it, what decisions it adds, how it resolves, and how its results return to the rest of the game.
- Carry the established resolution grammar into downtime and extended tasks when the underlying uncertainty is the same; a longer fictional duration does not by itself justify a new mechanic.
- When time pressure changes an existing task, first express the pressure through the game’s existing difficulty, modifier, target-number, dice-pool, assistance, quality, or consequence grammar.
- Use intuitive semantic difficulty categories when useful, but give each category a consistent mechanical translation so fictional adjudication can remain flexible without making resolution arbitrary.

## Don't
- Add a dedicated mechanic merely because the fiction presents a situation the first draft did not name explicitly.
- Preserve a weak core mechanic by surrounding it with patches that each solve only one new case.
- Force every activity through one generic check when doing so erases decisions or an experience the game is specifically built to support.
- Confuse broad mechanical coverage with enumerating a separate rule for every conceivable action.
- Create a bespoke “rushed task” rule when the normal difficulty grammar already expresses the increased demand.
- Let a named difficulty such as Easy, Hard, or Very Hard drift to a different mechanical meaning from one skill or scene to another unless the game explicitly defines that distinction.
- Replace a familiar core resolution language merely to make the rules look more unified when the existing grammar already answers the same question efficiently.
- Add a lookup or translation layer around a value the player already understands unless the new layer creates a meaningful difference in play.
- Assume that reusing the same dice, modifiers, or damage vocabulary automatically produces a complete working resolution procedure.

## Checklist
- At least one unforeseen but ordinary situation can be resolved through the established grammar without a new rule.
- Recurring edge cases are handled by a reusable extension or refactor rather than an expanding exception list.
- Any separate subsystem names the distinctive decisions or experience that justify its additional procedure.
- The subsystem's inputs and outputs connect cleanly to the rest of the game.
- Removing a proposed bespoke rule does not leave a case that the existing grammar already resolves adequately.
- A pressured version of an ordinary task can be expressed through established difficulty or consequence language before a new time-specific procedure is considered.
- If semantic difficulty labels are used, equivalent labels translate consistently across the skills and actions that share the same resolution grammar.
- A proposed replacement of an established resolution grammar has been compared against the current procedure on representative situations, including the migration or relearning cost created by the change.
- Any added translation layer can name what meaningful play it creates beyond restating information the existing grammar already communicates.

## Notes
Coherent mechanics achieve coverage through generalization: a small vocabulary can absorb many different fictional situations while preserving recognizable play. Consistency does not require one mechanic for literally everything. A tactical subsystem, vehicle procedure, magic system, or other specialized structure may earn its place when it creates meaningful decisions that a generic resolution cannot preserve economically. The important design move is to test the existing grammar first and treat repeated patches as a refactoring signal rather than normal growth. Mature systems may also discover better core grammar inside successful genre-specific extensions: once a local mechanic proves broadly reusable, generalize the concept, then re-audit the original subsystem to see whether shared grammar can replace duplicated machinery while preserving the experience that justified the subsystem in the first place. A new mechanic is easiest to justify when it answers a question the game could not previously express; replacing the established answer to an already-solved question carries a higher burden because it can impose migration cost without adding agency. This applies across time scales as well as fictional domains: combat, downtime, repairs, training, and other extended activities should reuse familiar resolution language when they ask the same underlying question. Semantic labels such as Trivial, Easy, Hard, Very Hard, or Impossible can provide an open-ended interface between fiction and rules; the referee may judge which label fits a situation, while the mechanic attached to that label remains stable. The label may translate into a modifier, target number, multiplier, dice-pool change, advantage state, or another method—the implementation is a design choice, not a universal prescription. This Pattern owns the choice to apply, extend, refactor, or replace the game’s mechanical grammar; **Build Complete Resolution Procedures Incrementally** owns how selected mechanics are dependency-ordered and integrated into an executable action.
