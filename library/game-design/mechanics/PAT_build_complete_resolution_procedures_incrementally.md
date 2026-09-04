---
object_id: PAT_build_complete_resolution_procedures_incrementally
object_type: pattern
name: Build Complete Resolution Procedures Incrementally
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
- resolution
- procedures
- integration
cross_links:
- rel: related_to
  target_object_id: PAT_reuse_core_resolution_grammar_before_adding_new_mechanics
- rel: related_to
  target_object_id: PAT_make_the_game_operable_without_hidden_designer_knowledge
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: related_to
  target_object_id: PAT_invoke_resolution_only_for_meaningful_uncertainty
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Build Complete Resolution Procedures Incrementally

## Pattern Rule
**IF** an action requires multiple mechanics, conditional branches, or state changes to resolve completely
**THEN** begin with the smallest dependency-ordered procedure that can carry the action from trigger to final state, validate that baseline, and add mechanics one at a time at the point where their required inputs already exist, retesting the complete affected procedure after every addition
**ELSE** when one mechanic already resolves the action completely, do not add procedural stages merely to make the system appear more detailed.

## Do
- Define the procedure's trigger, required inputs, initial state, terminal state, and minimum successful path before adding optional detail.
- Put each mechanic after the information or state it depends on has been produced; dependency order is part of the design, not only presentation.
- Test a new mechanic both in isolation and inside every affected path of the larger procedure.
- After each addition, execute the full procedure from declaration through termination and verify that state, resources, modifiers, and consequences remain coherent.
- When a new mechanic breaks a previously working procedure, first inspect the mechanic itself, its insertion point, and its interaction with existing mechanics before adding an exception or patch.
- Make branches explicit when different conditions call different mechanics; specialized protection, defenses, weapon properties, or scale rules need not run on every action when they are only conditionally relevant.
- Keep the common path cheap and gate deeper consequence machinery behind the state transitions that actually require it, then test a plausible situation in which several gated branches become active together.
- Once the procedure works, remove or bypass one stage at a time and retest; retain complexity when its loss removes intended decisions, consequences, information, pacing, or genre effect.
- Refactor the underlying procedure when repeated additions require precedence exceptions, adapters, or contradictory state assumptions.
- When runtime stages repeatedly reconstruct the same stable property of an attack, item, actor, or effect, test whether that property should become explicit entity data consumed by the shared procedure instead; promote only properties that multiple real procedures repeatedly need.

- Precompute invariant runtime work into the published procedure or data. If every execution adds the same constant, converts the same stable property, or repeats the same deterministic translation, shift that work into target values, tables, entity data, or another static representation unless doing it live creates a meaningful choice or visible information.
- After the immediate result is known, trace what the procedure leaves behind. Treat timers, bleeding, stun, penalties, follow-up checks, healing records, or other persistent outputs as part of the complete procedure when they create future mandatory work.

## Don't
- Design a large stack of interdependent mechanics and postpone integration testing until the entire subsystem is assembled.
- Insert a mechanic before the values, state, or choices it needs have been established.
- Treat a mechanic that works alone as proof that it will compose correctly with the rest of the procedure.
- Patch every new collision with another exception while preserving a procedure whose underlying order no longer makes sense.
- Leave trigger timing, precedence, resource expenditure, branch conditions, or termination implicit when multiple mechanics can interact.
- Force optional or specialized stages through every execution when the action can bypass them cleanly.
- Assume conditional branches cannot create overload merely because each one is skipped most of the time; overlapping triggers can make several low-frequency procedures run at once.

## Checklist
- The smallest complete baseline can be executed from trigger to final state without relying on mechanics that have not yet been defined.
- Every added mechanic has a named insertion point and the inputs it requires already exist at that point.
- The complete affected procedure was retested after the most recent addition rather than only the new mechanic being tested alone.
- A failure introduced by a new mechanic can be classified as a mechanic failure, insertion/order failure, or interaction failure before another rule is added.
- Branches say what condition enters them, what state they change, and where control returns or terminates.
- The most common execution path avoids consequence checks that cannot affect its result, and at least one realistic multi-trigger state has been executed when conditional branches can overlap.
- Resource spending and state changes occur at explicit points that remain coherent if the action is interrupted, resisted, or fails.
- Removing a retained stage demonstrably removes an intended decision, consequence, information channel, pacing effect, or genre function.
- Repeated exceptions trigger a refactor decision rather than indefinite rule accretion.
- A stable property that several procedures repeatedly derive has been considered for explicit, inspectable entity state, and descriptive facts that do not materially affect play have not been promoted into unnecessary statistics.

- Universal deterministic arithmetic and translations have been checked for precomputation so users are not repeatedly performing work the design can do once.
- The procedure map includes persistent state and later mandatory updates created by the result, not only the point where the initial roll or lookup ends.

## Notes
A mechanic performs an operation; a resolution procedure composes mechanics into an executable action. Combat makes this distinction easy to see: an attack check, Dodge, damage roll, armor reduction, resistance test, and injury rule can each work independently while their ordering and interaction still fail as a whole. Build the minimum complete chain first — for example, attack -> hit or miss -> damage — then insert defense, resistance, armor, criticals, locations, or other mechanics only after the simpler procedure works. The same method applies to repair, crafting, training, spellcasting, hacking, social actions, travel, and other multi-step resolution. Procedure refactoring can also move stable repeated distinctions out of high-frequency runtime work and into the data model: if several actions continually rediscover the same penetration class, size category, or other durable property, record it once when doing so gives the common procedure a stable input. This is not a mandate to stat every descriptive fact; first-class state earns its cost when actual play repeatedly consumes it. Chapter 12 of *Designing TTRPGs For Dummies* supplies the combat-domain components and repeatedly encourages reuse rather than a rule for every conceivable attack; the incremental construction and integration method is practitioner synthesis from comparing those components across working RPG systems.
