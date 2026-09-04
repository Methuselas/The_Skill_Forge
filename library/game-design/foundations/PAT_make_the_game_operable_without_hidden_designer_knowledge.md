---
object_id: PAT_make_the_game_operable_without_hidden_designer_knowledge
object_type: pattern
name: Make the Game Operable Without Hidden Designer Knowledge
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
- usability
- rules
- assumptions
- onboarding
cross_links:
- rel: related_to
  target_object_id: PAT_define_the_intended_player_before_designing_for_them
- rel: related_to
  target_object_id: PAT_spend_worldbuilding_detail_where_it_changes_play
- rel: related_to
  target_object_id: PAT_scale_npc_and_adversary_detail_to_their_role_in_play
- rel: related_to
  target_object_id: PAT_build_complete_resolution_procedures_incrementally
- rel: related_to
  target_object_id: PAT_structure_adventure_narratives_with_milestones_plot_beats_and_player_agency
- rel: related_to
  target_object_id: PAT_layer_adventure_information_by_how_players_can_access_it
- rel: related_to
  target_object_id: PAT_account_for_the_intended_play_environment_before_freezing_the_design
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants:
- variant_id: game_design_variant_use_a_sample_adventure_as_an_executable_reference_implementation
  variant_name: Use a Sample Adventure as an Executable Reference Implementation
  variant_basis: context
  difference_from_foundation: When a game expects new referees to run play or create their own adventures, pair the construction grammar with at least one representative adventure that can be run directly and that demonstrates how rules, setting assumptions, encounter structures, information, and referee procedures compose in practice.
  when_to_use: The game expects inexperienced or downstream referees to learn how its abstract rules and authoring guidance become actual playable material.
  when_not_to_use: The sample would substitute for explicit construction guidance, teach an atypical edge case as though it were the normal form, or require users to reverse-engineer hidden assumptions from the example.
  absorbed_from_object_id: none
---

# Make the Game Operable Without Hidden Designer Knowledge

## Pattern Rule
**IF** players, facilitators, testers, or implementers will use the game without the designer present
**THEN** make the assumptions, rules, expectations, and required information explicit enough for the intended user to operate the game independently
**ELSE** temporary explanatory debt is acceptable in an internal prototype only when it is tracked as unfinished design rather than mistaken for a complete rule.

## Do
- Watch for moments where the designer answers a question from memory instead of from the game’s written or implemented interface.
- Test with people who were not present during design so missing assumptions become visible.
- During at least one handoff playtest, remain silent when players or another facilitator encounter a rules question long enough to see whether the written game lets them recover; record any designer explanation required to continue as missing or unclear design information.
- At completed-game stage, include at least one referee or facilitator who did not learn the game directly from the designer. Treat any designer intervention as test contamination that must be recorded even when intervention is necessary to keep play moving.
- When an unfamiliar referee hesitates, distinguish intentionally delegated referee judgment from ordinary unfamiliarity that the documentation can resolve and from information that is actually missing and can only be supplied by hidden designer knowledge.
- Distinguish an intentionally adjudicated open space from a rule whose missing logic is being supplied unconsciously by the creator.
- Treat delegation as healthy only when the user receives explicit authority plus enough boundaries, reusable categories, examples, baselines, or other calibration to make the delegated decision without reverse-engineering the designer.
- Distinguish local fictional rulings from high-value authoring or construction tasks the game expects users to perform repeatedly or campaign-centrally; the latter need an explicit grammar when stock examples and modification rules are insufficient.
- Rewrite rules around the decision the user must make, including inputs, outputs, and exceptional states that matter to play.
- For multi-step resolution, state the trigger, sequence, branch conditions, state changes, resource-spend timing, precedence, return points, and termination conditions needed to execute the procedure without the designer supplying missing order from memory.
- When a setting is meant to support referee, modder, or downstream expansion, communicate the underlying setting grammar firmly enough that new material can be extended coherently without requiring hidden designer intent.
- For every content type the game expects downstream creators to author, expose the construction grammar — required fields, constraints, scaling guidance, templates, and examples — rather than providing only finished examples or modification rules.
- When adventure creation is an expected downstream task, pair that grammar with a representative runnable adventure so intended rules, information, encounter structure, and referee procedures can be seen operating together rather than only described in isolation.
- When an adventure contains required milestones, supported scope boundaries, triggered plot beats, or forced transitions, expose those structures to the referee and state the tools available for moving play toward them rather than requiring the referee to guess which parts of the plot are mandatory.
- In prepared adventures, clearly distinguish player-facing description from referee-only truth, and state the perception, question, action, trigger, or resolution condition under which concealed information becomes available.
- Treat the rulebook, reference document, or equivalent rules surface as part of the game’s operating interface: organize prerequisite concepts before they are needed or provide clear navigation to them, and make frequently consulted procedures, modifiers, tables, exceptions, and definitions cheap to retrieve during play.
- Distinguish learning architecture from reference architecture. A simplified onboarding procedure can be useful, but clearly identify when it is a teaching model rather than an incomplete presentation of the exact full procedure.
- Give a new facilitator a clearly sufficient first-campaign configuration: identify the rules that are required, the modules that can be ignored safely, and the concrete situations that should trigger adding optional detail later. When the configuration surface is large, encode that curation in a preset, campaign template, or equivalent package rather than making the novice reconstruct it from the full catalog.
- Treat optionality as a knowledge-cost question as well as a dependency claim. If users must understand a module before they can know whether omitting it is safe, include that evaluation burden in onboarding design instead of pretending the optional label removes it.
- Use information hierarchy deliberately — headings, spacing, tables, boxes, indexes, cross-references, summaries, and other navigational signals — to reduce search and interpretation cost rather than merely making the artifact visually distinctive.
- Put usability ahead of visual style. Preserve thematic presentation only while the text remains readable and the rules remain reliably retrievable; simplify ornamental treatment when it interferes with operation.

- If a product is presented as a complete playable core, keep every common-path procedure executable from that core surface. Supplements may broaden options or deepen detail, but do not make a required attack, spell, recovery, or other ordinary branch depend on an undisclosed external book or module.
- At a frequent branch point, provide the next destination where the user needs it: name the required table, section, procedure, or equivalent interface target and keep high-frequency dependencies physically or digitally close enough that ordinary play does not require memorizing the document graph.
- Test novice retrieval separately from veteran retrieval. Experienced users may cache table locations, abbreviations, and dependency paths in memory; treat that expertise as an interface optimization they learned, not as proof that a first-time user can find the same material efficiently.

## Don't
- Treat “it is obvious” as evidence that another player will infer the same rule.
- Use designer availability as a permanent support mechanism for unclear procedures.
- Rescue an independent handoff test with unwritten explanations and still count the resulting execution as proof that the published artifact is self-sufficient.
- Hide required knowledge in scattered examples when the user needs it to execute a core interaction.
- Treat a catalog of stock examples as a substitute for creation rules when users are expected to make new instances of that content.
- Call unsupported extrapolation healthy referee freedom when a campaign-central creation or calibration task is expected but the artifact supplies neither a usable construction grammar nor enough baselines to perform it consistently.
- Leave interactions such as “before armor,” “after damage,” “when hit,” or “when injured” to table intuition when different ordering would change the result.
- Hide a required adventure milestone behind prose, imply that every route is supported when the scenario has a real boundary, or expect the referee to invent coercion on the fly because the intended transition was never documented.
- Mix player-safe description and hidden referee information so closely that a downstream referee must infer what can be revealed or when a secret becomes accessible.
- Treat a rule as adequately documented merely because the correct text exists somewhere in the book if intended users cannot reliably locate it when play requires it.
- Present a teaching simplification as though later rules merely add detail when the full procedure actually changes sequencing, information, permissions, or other behavior the learner must relearn.
- Require a new referee to survey the entire rules corpus before running a competent first campaign merely to discover which options are safe to omit.
- Present a toolkit without a recommended starting configuration when the intended user is expected to configure many interdependent modules before play.
- Let decorative style, dense page furniture, or thematic presentation reduce legibility or make high-frequency information slower to recover.

- Call a product complete when its common-path procedures require an unbundled book, hidden module, or external reference merely to reach an ordinary result.
- Use cross-references that only name a destination after the user has already had to search for the branch or infer which product contains it.
- Treat veteran table-location memory or habitual shortcuts as evidence that the published interface is self-explanatory for novices.

## Checklist
- A new user can begin and resolve core play without asking what the designer meant.
- Rules that rely on judgment say who exercises that judgment and what boundaries apply.
- Delegated judgment has enough categorical rails, examples, baselines, or calibration that an intended user can make a ruling without reconstructing hidden designer assumptions.
- Campaign-central creation or construction tasks expected of users have an explicit grammar rather than only stock examples or upgrade rules.
- Playtests record repeated clarification questions as design defects to investigate.
- A handoff or designer-silence test has shown that intended users can recover from ordinary rules questions without the designer supplying unwritten intent.
- At least one completed-game handoff has been run by a referee or facilitator who learned the game from the artifact rather than from the designer, and every designer intervention required to continue was logged.
- Handoff observations distinguish intentional adjudication space, recoverable unfamiliarity, and genuinely missing information.
- Internal prototypes clearly mark unresolved or temporarily explained behavior.
- Open setting space has stable anchors and boundaries from which a downstream creator can infer what belongs and what consequences a new addition should have.
- For each content category users are expected to extend, a new user can construct a novel instance without reverse-engineering unstated assumptions from published examples.
- If the game expects referees to create adventures, at least one representative sample can be run directly and visibly demonstrates how the documented construction grammar composes into play.
- For a prepared adventure, the referee can identify required milestones, optional or conditional beats, supported scope boundaries, and any transition tools the design expects them to use.
- Player-facing description, referee-only truth, and concealed-information access conditions are separated clearly enough that a referee can reveal information without reverse-engineering author intent.
- A new user can execute each core multi-step resolution from trigger to termination and determine when resources are spent, branches are entered, and conflicting effects take precedence.
- The book or rules interface presents prerequisite concepts in a usable order or supplies navigation that lets the reader recover missing prerequisites without already knowing the game.
- High-frequency rules and reference material can be found quickly enough that retrieval does not become a recurring source of avoidable play friction.
- If onboarding uses a simplified procedure, the artifact tells the learner what is simplified and provides a clear transition to the full procedure instead of hiding a later behavioral replacement.
- A first-time facilitator can identify a sufficient playable rules path without already possessing expert knowledge of the full system, and a large modular game provides at least one ready-to-run preset or equivalent configuration when a plain list of optional rules would still require expert curation.
- Optional modules state enough about dependencies and activation triggers that the facilitator can omit them intentionally and add them later without reconstructing the entire rules architecture.
- Visual hierarchy is consistent enough that intended users can distinguish chapters, sections, rules, examples, tables, warnings, and reference material without decoding a new presentation grammar on each page.
- The artifact remains readable and operable even after ornamental style is evaluated separately from personal aesthetic preference.

## Notes
A private game can survive because its creator silently supplies missing intent. A transferable game cannot depend on that invisible subsystem. Independent use is therefore a test of whether the design actually contains the rules the designer believes it contains. The same test applies to extensible settings: define the grammar more firmly than every possible instance so that deliberate negative space becomes bounded possibility rather than missing content. A game can be playable from stock content yet still be incomplete for downstream authorship if it shows finished examples without teaching how to build a new one; examples demonstrate a grammar, but they do not replace it. The same is true of resolution procedures: a designer may understand the intended order of Dodge, damage, armor, resistance, interruption, or resource spending while the written rules expose only the component mechanics. Hidden sequencing is still hidden designer knowledge. A useful handoff test is to watch another group encounter uncertainty without immediately rescuing them: if the designer must provide the missing rule, precedence, interpretation, or recovery path for play to continue, that information is not yet actually carried by the game.

`game_design_variant_use_a_sample_adventure_as_an_executable_reference_implementation` applies this principle specifically to adventure onboarding. A sample adventure can function as an executable reference implementation: it shows how abstract rules, setting assumptions, encounter structures, information, and referee procedures compose into actual play while also reducing the cost of a first session. The example remains evidence of the grammar rather than a substitute for it. If users are expected to author new adventures, they should be able to do so from explicit guidance instead of reverse-engineering unstated design intent from the sample. This variant is supported by Martin Buinicki's *Designing TTRPGs For Dummies*, Chapter 14, which treats an included adventure as both an onboarding tool and a model for later adventure creation. Chapter 15 extends the same operability requirement into narrative execution: if a scenario depends on specific milestones, scope limits, beat triggers, or transition pressures, the referee needs those requirements exposed explicitly. Otherwise the adventure may be fully understandable to its author while forcing a downstream referee to reconstruct the intended plot from hidden assumptions. Chapter 16 extends this operability test to information presentation: a referee must be able to tell what is safe to present immediately, what remains hidden, and what condition grants access to it. Learning and lookup are related but distinct interface jobs. Optionality creates a third interface job: curation. A large toolkit is not automatically accessible merely because each extra rule can be omitted; the facilitator still needs enough information to choose a playable subset. A strong onboarding path therefore supplies a sufficient default configuration and clear expansion triggers, allowing mastery to grow through play instead of requiring mastery before play. Progressive disclosure can reduce onboarding burden, while mature reference use may benefit from consolidation, indexes, summaries, and direct retrieval. When introductory rules intentionally simplify a full procedure, the simplification should be labeled so later differences do not masquerade as mere added detail. Chapter 19 extends the same principle to information architecture and layout. A rulebook is not merely prose that contains correct rules; it is one of the interfaces through which those rules are learned, recovered, and executed. Search time, page flipping, unclear hierarchy, distant exceptions, and unreadable presentation therefore create real operating cost. Different RPGs and different editions can use radically different visual styles while preserving the same basic information grammar. Style may establish identity, but usability is the requirement: if the intended user cannot read or retrieve the content reliably, the interface has failed regardless of how attractive it is. Completed-game handoff testing extends this principle from individual rules questions to the whole artifact: the strongest evidence comes from a referee who has not been trained by the designer. If the designer must step in, the session can continue, but the intervention is evidence about the artifact rather than invisible assistance that should be ignored.

Healthy delegation is not the same as omission. A compact game can leave local fictional interpretation to a referee when authority is explicit and the surrounding mechanics provide a bounded vocabulary for judgment. The same defense does not apply when the game makes a construction, calibration, or authorship task central to play but expects users to infer its grammar from finished examples. In that case, an expert may be able to reverse-engineer the missing procedure, but the artifact is still depending on knowledge it did not teach.
