---
object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
object_type: pattern
name: Evaluate Mechanics by the Decisions and Agency They Create
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
- mechanics
- agency
- decisions
- resolution
cross_links:
- rel: related_to
  target_object_id: PAT_match_practiced_behavior_to_the_intended_outcome
- rel: related_to
  target_object_id: PAT_match_the_cost_of_failure_to_the_players_prior_investment
- rel: related_to
  target_object_id: PAT_build_complete_resolution_procedures_incrementally
- rel: related_to
  target_object_id: DRILL_profile_serial_resolution_latency
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Evaluate Mechanics by the Decisions and Agency They Create

## Pattern Rule
**IF** a mechanic is being evaluated or compared
**THEN** inspect what meaningful decisions the player can make before, during, and after resolution, and determine how much outcome control comes from skill, strategy, chance, or adjudication
**ELSE** do not judge the mechanic only by whether its arithmetic or procedure resolves correctly.

## Do
- Separate the mechanic’s calculation from the decisions that feed it and the choices that follow its result.
- Identify where players can spend resources, accept risk, change position, push a result, or otherwise influence an outcome.
- Check whether the intended game wants high player control, high uncertainty, facilitator judgment, or a deliberate mixture.
- For adverse outcomes, examine whether players can understand why the result occurred and regard the procedure as legitimate even when they dislike it.
- Measure execution cost in time, lookup, arithmetic, physical handling or counting, explanation, state tracking, and attention, then compare that burden with the meaningful decisions, consequences, simulation value, genre experience, or clarity the mechanic purchases.
- Measure where and how often that cost is paid. Complexity attached to an optional capability a player chooses can be worthwhile even when it is substantial; the same burden inserted into every ordinary action can become recurring friction.
- Classify complexity by cadence and operator context: common-path runtime, character creation, advancement, and downtime, preparation, or construction. Equal procedure length does not imply equal experiential cost when one is paid every attack and another is paid rarely as an expressive activity.
- Test omissions as well as additions. A low-frequency procedure can be worth adding when it creates durable strategic, ownership, identity, or construction decisions whose value exceeds its operating burden.
- Separate decision complexity from operator complexity. Record which parts ask players to choose and which parts mainly perform arithmetic, lookup, translation, dependency propagation, state maintenance, or entity bookkeeping.
- Stress-test conditional mechanics under realistic concurrent activation. Several individually cheap rules can become expensive when one situation activates them together or when they all modify the same shared resource or derived value.
- When players can alter a bad result, make the intervention a decision through scarcity, opportunity cost, added risk, or another meaningful consequence rather than an automatic extra step.
- Evaluate attention displacement: check whether executing the mechanic reinforces the intended activity or becomes a competing activity that players focus on for its own sake.
- During playtests, observe both operational correctness and experiential fit: whether players understand the mechanic, how long it actually takes, what they attend to while using it, whether they accept its outcomes as legitimate, and whether their behavior matches the experience the mechanic was meant to create.
- Separate a tester's observation from the tester's proposed repair. Preserve reports such as confusion, drag, dominance, or lack of choice as evidence, but treat suggested fixes as new design hypotheses that must be diagnosed against the intended experience and surrounding system.
- Treat every revision as unvalidated until the changed behavior and its nearby dependencies have been retested; the first mechanic is not always the right one, and the first fix is not always the right one either.

- Evaluate repeated procedures at table scale as well as action scale. When actors resolve serially, measure how per-resolution work multiplies across a representative round and how long each participant goes without a meaningful decision.
- Count persistent-state cost after the visible resolution. A result that creates bleeding, stun, timers, penalties, follow-up checks, recovery records, or other obligations leaves operator work behind even when the initial roll is finished.
- When a table or lookup replaces arithmetic, prose exceptions, or improvisation, compare the work it compresses with retrieval distance, lookup frequency, interpretation steps, branch depth, and the future state its result creates rather than treating tables as inherently efficient or inefficient.

- Separate purposeful character-facing friction from operator-facing friction. Preserve scarcity, uncertainty, injury, delay, or other hardship when the difficulty is itself part of the intended decisions; compress lookup, repeated translation, bookkeeping, or calculation that does not create equivalent play.
- When a procedure scales with simulated units such as bullets, targets, components, or actors, compare that scaling with the number of meaningful decisions it produces; a one-decision action that multiplies operator work per physical unit is a high-frequency warning sign.
- Treat a nominally specialist procedure as common-path complexity when the genre or expected play makes it frequent; a separate section heading does not buy a larger runtime budget.

## Don't
- Equate more choices with more meaningful agency when the options do not materially alter outcomes.
- Treat randomness as automatically hostile to agency; uncertainty can support an experience when players can make consequential decisions around it.
- Call a resolution fair merely because its probabilities are mathematically consistent.
- Treat extra precision, realism, or procedural detail as self-justifying when it adds more operating burden than useful play.
- Compare two mechanics only by their raw rule count or arithmetic difficulty while ignoring whether one cost is opt-in and local and the other is mandatory and high-frequency.
- Equate fewer rules with better design when removing or omitting a procedure also removes high-value decisions at a cadence where the added complexity would be affordable.
- Assume that a rule is cheap merely because it is optional, conditional, or event-gated; measure the cost of discovering whether it applies and the cost when several such rules become relevant at once.
- Count automated arithmetic or hidden state changes as meaningful player complexity when the player still has to understand or choose around them; automation can remove operator burden without removing the need for causal feedback.
- Spread a specialized layer across baseline play merely because it is enjoyable in the optional domain where it was first tested.
- Let a second-chance mechanic routinely erase undesirable results without asking the player to spend, risk, or choose anything meaningful.
- Assume an entertaining subgame automatically supports the RPG; a fun procedure can still pull attention away from the experience the surrounding game is trying to create.
- Implement a tester's proposed fix merely because the reported symptom is real; accurate observation does not guarantee accurate diagnosis or repair.
- Treat a revision as validated because it sounds cleaner on paper without running the changed behavior again.

- Remove character-facing friction merely because it makes the game inconvenient when that inconvenience is the pressure players are meant to manage.
- Call a redesign simpler without checking whether equivalent complexity moved into another common or genre-frequent procedure.

## Checklist
- The mechanic’s meaningful decision points can be named.
- The sources of outcome control and uncertainty are explicit.
- Player choices can change consequences in ways appropriate to the intended experience.
- Failure can be explained through the procedure rather than feeling arbitrary or hidden.
- The mechanic's execution time, lookup burden, arithmetic, physical handling or counting, explanation, and tracked state have been observed or estimated against what the procedure contributes to play.
- The evaluation records which users pay the mechanic's complexity, whether they opted into it, and how often the cost recurs during normal play.
- The evaluation distinguishes common-path runtime, creation, advancement, and downtime or construction costs instead of treating all complexity as one budget.
- Any omitted or proposed procedure has been checked for the meaningful strategic or expressive decisions it would add or remove at its actual cadence.
- The evaluation distinguishes meaningful decisions from arithmetic, lookup, translation, state maintenance, and representation work that could be simplified or automated without erasing those decisions.
- At least one plausible stacked state has been checked when multiple conditional mechanics can overlap, including any downstream changes caused through shared resources or derived values.
- Any second-chance rule preserves uncertainty by attaching a meaningful choice, cost, risk, or scarcity to intervention.
- The mechanic's own entertainment and attention demands support rather than displace the intended play experience.
- Playtest evidence distinguishes a mechanic that merely executes correctly from one whose observed table behavior also supports the intended experience.
- Feedback records preserve the observed symptom separately from any suggested cause or fix.
- Revised mechanics have been retested rather than accepted solely from design reasoning.

- A representative full-round test has checked whether individually tolerable resolutions become long participant downtime when repeated across all actors.
- The evaluation records any persistent state created by a resolution and the later reminders, updates, or recovery work that state requires.
- Any table-driven procedure identifies what logic the table compresses and what retrieval, interpretation, branch, or state-maintenance cost the lookup introduces.

## Notes
A mechanic has experiential work beyond producing an answer. The distribution of control shapes how players relate to success and failure, while the procedure itself consumes table time and attention. Complexity earns its place when that operating cost buys meaningful decisions, useful consequences, simulation value, genre experience, or clarity for the intended audience. A detailed simulation can therefore be coherent yet still overtax human operators when many individually sensible mechanics must be maintained simultaneously. Shared primitives reduce fragmentation, but they can also increase interaction density because several modules may feed the same resources and derived values. Evaluate the common path, the stacked path, and the amount of work that is genuine play rather than bookkeeping. Placement matters as much as amount: a dense construction system can be enjoyable when players choose to engage it for new capabilities, while a smaller procedure can feel expensive when it interrupts every familiar action. A mechanically correct procedure can still be a poor fit when its execution burden overwhelms what the players gain from it, and an entertaining procedure can still be the wrong fit when it becomes a competing activity that displaces the intended play. Second chances follow the same rule: they are strongest when a bad result becomes a resource or risk decision rather than an automatic erasure of failure. Playtesting should therefore test more than mathematical or procedural validity. A mechanic can produce the correct answer and still be the wrong mechanic if players misunderstand it, spend disproportionate time operating it, focus on the procedure instead of the intended activity, or consistently make decisions unlike those the design was meant to encourage. Feedback adds another separation: an observed symptom is evidence about the game, while a proposed cause or repair is a hypothesis. Preserve the first, diagnose before accepting the second, and retest every revision because the first fix can fail just as readily as the first mechanic.

Complexity cadence changes what a design can afford. A moderately involved procedure used once during downtime may be strategically expressive and inexpensive in table-time terms, while the same number of operations repeated for every ordinary action can dominate the session. Simplification should therefore test both sides of the trade: what operating work disappears and what decisions disappear with it. A missing procedure can be a design defect when its low-frequency complexity would have supported campaign-central ownership, construction, or strategic expression.
