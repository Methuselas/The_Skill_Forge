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
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Make the Game Operable Without Hidden Designer Knowledge

## Pattern Rule
**IF** players, facilitators, testers, or implementers will use the game without the designer present
**THEN** make the assumptions, rules, expectations, and required information explicit enough for the intended user to operate the game independently
**ELSE** temporary explanatory debt is acceptable in an internal prototype only when it is tracked as unfinished design rather than mistaken for a complete rule.

## Do
- Watch for moments where the designer answers a question from memory instead of from the game’s written or implemented interface.
- Test with people who were not present during design so missing assumptions become visible.
- Distinguish an intentionally adjudicated open space from a rule whose missing logic is being supplied unconsciously by the creator.
- Rewrite rules around the decision the user must make, including inputs, outputs, and exceptional states that matter to play.
- When a setting is meant to support referee, modder, or downstream expansion, communicate the underlying setting grammar firmly enough that new material can be extended coherently without requiring hidden designer intent.

## Don't
- Treat “it is obvious” as evidence that another player will infer the same rule.
- Use designer availability as a permanent support mechanism for unclear procedures.
- Hide required knowledge in scattered examples when the user needs it to execute a core interaction.

## Checklist
- A new user can begin and resolve core play without asking what the designer meant.
- Rules that rely on judgment say who exercises that judgment and what boundaries apply.
- Playtests record repeated clarification questions as design defects to investigate.
- Internal prototypes clearly mark unresolved or temporarily explained behavior.
- Open setting space has stable anchors and boundaries from which a downstream creator can infer what belongs and what consequences a new addition should have.

## Notes
A private game can survive because its creator silently supplies missing intent. A transferable game cannot depend on that invisible subsystem. Independent use is therefore a test of whether the design actually contains the rules the designer believes it contains. The same test applies to extensible settings: define the grammar more firmly than every possible instance so that deliberate negative space becomes bounded possibility rather than missing content.
