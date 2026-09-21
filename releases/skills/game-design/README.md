# SkillForge Game Design

Craft knowledge for designing and revising games: mechanics, characters, adversaries, adventures and playable worlds, with Drills for practising and playtesting the decisions.

[Download SkillForge-Game-Design.zip](SkillForge-Game-Design.zip)

| | |
|---|---|
| Skill name | `skillforge-game-design` |
| Built from | PASS `1.0.0-beta.75` |
| Domain cards | 158 Patterns, 9 Action Protocols, 14 Drills |
| Modules | `game-design/adventures`, `game-design/adversaries`, `game-design/characters`, `game-design/foundations`, `game-design/mechanics`, `game-design/worldbuilding` |
| Also bundled | the `metaskills` baseline every release carries |
| Skillset Memory | `memory/game-design/` (read-only) |
| Helpers | `scripts/skillforge_runtime.py`, `scripts/skillforge_drill.py` (blind Drills) |
| ZIP | `SkillForge-Game-Design.zip`, 579,950 bytes |
| SHA-256 | `caeaafd3e3da92821e03a251cf8362f48f4c195e86e420d162267c578ee3b18e` |

## What it covers

- Foundations of play and mechanics design.
- Characters and adversaries.
- Adventure structure and worldbuilding for playable settings.

## Install

The ZIP holds one folder, `SkillForge_Game_Design/`, with `SKILL.md` at its root. Keep that
folder whole: its library, helpers and license files belong together.

- **Claude Code:** extract it so the skill sits at `.claude/skills/skillforge-game-design/SKILL.md`
  in a project, or `~/.claude/skills/skillforge-game-design/SKILL.md` for every project.
- **Codex:** extract it to `.agents/skills/skillforge-game-design/` in the repository.
- **Claude.ai, ChatGPT and other Agent Skills hosts:** upload the ZIP as a skill.
- **Anything else:** extract it and start from its `SKILL.md`.

## Use

Ask for mechanics, encounter, character, adventure or world design, critique, or a playtest plan.

Nothing needs preloading: the skill starts from `SKILL.md` and retrieves only the
cards a task needs. Python is optional except where a helper above is used.

## Verify

Compare the ZIP's SHA-256 with the table above. With Python available, run
`python scripts/skillforge_runtime.py doctor` inside the extracted folder.

## License

Python helpers are AGPL-3.0-or-later; instructions, knowledge, profiles, memory
and assets are CC-BY-SA-4.0. The release carries `LICENSE.md`, `NOTICE.md`,
`TRADEMARKS.md` and both license texts. Built and validated in
[PASS](https://github.com/Methuselas/PASS); change it there, never here.
