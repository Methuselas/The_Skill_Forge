---
object_id: PAT_derive_character_capabilities_from_expected_play
object_type: pattern
name: Derive Character Capabilities from Expected Play
library_path:
- game-design
- characters
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- characters
- abilities
- roles
- gameplay
cross_links:
- rel: related_to
  target_object_id: PAT_translate_genre_into_play_requirements
- rel: related_to
  target_object_id: PAT_define_the_intended_player_before_designing_for_them
- rel: related_to
  target_object_id: PAT_balance_character_roles_by_consequential_contribution
- rel: related_to
  target_object_id: PAT_price_character_options_by_mechanical_leverage_and_constraint
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Derive Character Capabilities from Expected Play

## Pattern Rule
**IF** a game is defining the traits, abilities, skills, classes, playbooks, templates, or other structures used to create player characters
**THEN** derive those structures from the significant actions and challenges the characters are expected to face in actual play
**ELSE** when an inherited character framework is being used, remove or reinterpret fields that do not support the intended experience before adding new ones.

## Do
- List the most exciting and recurring things player characters are expected to do before deciding which attributes or skills exist.
- Use genre and setting to determine which capabilities deserve mechanical distinction and which terms make those distinctions understandable to players.
- Narrow the near-infinite set of human traits to qualities that change gameplay or meaningfully shape the player experience.
- Let classes or playbooks package recognizable roles when that helps creation and communication, but allow classless structures when direct trait and ability selection better fits the design.
- Make character options mechanically consequential enough that choosing them changes how the character acts, solves problems, or participates in the game's important situations.
- Choose capability granularity deliberately. Broad packages reduce creation and retrieval burden but can bundle competencies that players reasonably want separated; granular skills increase concept precision but also increase acquisition, lookup, and character-management cost.
- When one narrow capability is too specific and its parent attribute or package is too broad, consider a priced thematic bundle that improves a coherent middle-sized family without collapsing unrelated concepts into the same purchase.
- Use editable templates, archetypes, or recommended packages when an open construction system can otherwise overwhelm new players or let them accidentally omit capabilities required for the role they intend to play. Keep role scaffolds distinct from mandatory ontological packages such as species or body-state traits.
- If templates, lenses, packages, or reusable trait groups can compose, define duplicate, precedence, conflict, and merge behavior instead of leaving combination semantics to the user.
- Use numeric capability levels only when adjacent values create distinctions the game repeatedly cares about; use coarse proficiency states when the meaningful questions are categorical and extra numeric resolution would mostly create advancement or dependency overhead.
- Decide whether specialization should be soft or permission-based. Cost, efficiency, access, packaging, and hard exclusion all create different character philosophies even when the resulting skill list looks similar.
- When increased expertise is supposed to feel like greater fluency rather than only greater reliability, let advancement change appropriate operating requirements such as time, ritual, energy, restrictions, or available applications instead of limiting every improvement to a larger success probability.
- Separate an ability's mechanical effect from its fictional source when several origins can produce the same capability. Reuse the effect grammar where practical and attach source-specific access, counters, limitations, costs, or advancement only where the fiction requires them.
- Separate advancement price, advancement permission, and fictional cause. Let price measure the persistent mechanical value of the new state, permission state whether that change is currently available, and fictional cause explain how the character actually acquires it.
- Track training, exposure, teachers, downtime, or other causal evidence only at the resolution the campaign values; causal advancement should not require the facilitator to audit every hour or action merely to prove a believable change occurred.

## Don't
- Begin with a traditional attribute or skill list and search afterward for reasons each field should matter.
- Model every plausible human capability simply because a detailed character could possess it.
- Create a class whose title sounds appropriate to the genre but whose abilities rarely matter in the adventures the game actually produces.
- Create a new tracked field or mechanical distinction when its play value does not justify the extra state it adds to the character model.
- Split a broad capability into many narrow skills without checking whether the increased concept precision is worth the build and retrieval burden.
- Use numeric skill progression for a capability whose actual play questions are mostly broad proficiency categories.
- Treat an editable role template as a hard permission boundary merely because it is a convenient onboarding scaffold.
- Force players toward a broad parent trait merely because buying the intended family of narrow capabilities separately is economically inefficient.
- Harden a soft specialization framework into permanent role or permission boundaries merely because named archetypes are easier to present.
- Duplicate mechanically identical capabilities into separate subsystems solely because their fictional sources differ when source tags, limitations, counters, or access rules would preserve the distinction more economically.
- Make expertise progression numerically larger at every step when the intended fantasy is specifically about becoming faster, cheaper, subtler, more controlled, or less constrained.
- Let point expenditure alone create a social, institutional, technological, or learned state when the fiction must first make that state possible.
- Require exhaustive training or exposure logs when a coarser causal record would preserve the same believable advancement.

## Checklist
- Every major character field can be connected to an expected action, challenge, role, or recurring decision.
- Important adventure activities have character capabilities capable of differentiating how PCs approach them.
- A mechanically elaborate option appears often enough, or matters strongly enough, to justify its representation cost.
- Class or role labels correspond to differences in actual play rather than cosmetic naming alone.
- Traditional elements retained from another RPG architecture have a current purpose in this game.
- The chosen skill or capability granularity matches how often the game needs those competencies to differ in play.
- When a middle-sized aptitude bundle exists, its price has been compared with both representative individual capabilities and the broader parent trait.
- If open character construction is difficult to enter safely, at least one editable role template or equivalent scaffold produces a competent starting character without requiring the novice to understand the entire option catalog.
- Composable templates or packages state how duplicate requirements, leveled traits, contradictory traits, and optional variation are merged.
- The capability's granularity matches the questions play actually asks: numeric levels are retained where adjacent values matter, while categorical states are used where they preserve the meaningful distinctions more economically.
- Any hard role, class, profession, or permission boundary names the design benefit that cannot be achieved as cleanly through softer cost or efficiency incentives.
- Advancement produces the intended form of mastery: if fictional expertise should change how the capability is performed, at least one non-probability improvement expresses that change.
- Capabilities that share an effect but differ in origin reuse common mechanics where possible while preserving any source-specific counters, permissions, costs, or identity that actually changes play.
- Advancement tests identify price, permission, and fictional cause separately, and the facilitator can verify the cause without maintaining more training-history detail than the campaign actually values.

## Notes
Character architecture should be derived from what the game expects characters to do, not from an attempt to model every trait a person could possess. Classes can package broad roles, while classless systems can expose capabilities directly; either approach works when the represented choices change play. Templates can provide a third layer: an editable, competence-preserving interface over open construction rather than a hard permission system. Their usefulness depends on composition rules when several packages can stack. Granularity is another axis rather than a quality ladder: a compact package or categorical proficiency can be easier to learn and operate, while narrower numeric competencies can express character concepts more precisely. When the useful concept sits between those extremes, an intermediate thematic bundle can preserve differentiation without making a broad parent trait the obvious economic purchase. Specialization can likewise be soft, through different costs or efficiencies, or hard, through permission boundaries; changing between those forms changes the character model even if many individual skills remain recognizable. A capability on the sheet also advertises competence, so an elaborate option that rarely matters can become a false promise even when its individual rule is sound. Advancement has a similar separation problem: what a change costs, whether it is currently available, and what causes it in the fiction are different design questions and should not be forced into one rule or one bookkeeping burden.
