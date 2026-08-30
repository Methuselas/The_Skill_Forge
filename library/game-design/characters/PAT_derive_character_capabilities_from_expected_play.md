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

## Don't
- Begin with a traditional attribute or skill list and search afterward for reasons each field should matter.
- Model every plausible human capability simply because a detailed character could possess it.
- Create a class whose title sounds appropriate to the genre but whose abilities rarely matter in the adventures the game actually produces.
- Create a new tracked field or mechanical distinction when its play value does not justify the extra state it adds to the character model.

## Checklist
- Every major character field can be connected to an expected action, challenge, role, or recurring decision.
- Important adventure activities have character capabilities capable of differentiating how PCs approach them.
- A mechanically elaborate option appears often enough, or matters strongly enough, to justify its representation cost.
- Class or role labels correspond to differences in actual play rather than cosmetic naming alone.
- Traditional elements retained from another RPG architecture have a current purpose in this game.

## Notes
Character architecture should be derived from what the game expects characters to do, not from an attempt to model every trait a person could possess. Classes can package broad roles, while classless systems can expose capabilities directly; either approach works when the represented choices change play. A capability on the sheet also advertises competence, so an elaborate option that rarely matters can become a false promise even when its individual rule is sound.
