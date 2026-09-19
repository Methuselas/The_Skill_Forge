# SkillForge Art

Visual-art craft knowledge for drawing, painting, comics and illustration work: execution, critique and teaching, organized as reusable decisions (Patterns), ordered procedures (Action Protocols) and deliberate practice (Drills).

[Download SkillForge-Art.zip](SkillForge-Art.zip)

| | |
|---|---|
| Skill name | `skillforge-art` |
| Built from | PASS `1.0.0-beta.49` |
| Domain cards | 415 Patterns, 60 Action Protocols, 119 Drills |
| Modules | `art/color`, `art/comics`, `art/comics/covers`, `art/comics/inking`, `art/comics/page-construction`, `art/composition`, `art/drawing/rendering`, `art/drawing/sketching`, `art/foundations/form-construction`, `art/foundations/gesture-force`, `art/foundations/ideation`, `art/foundations/mark-making`, `art/foundations/observation`, `art/foundations/temporal-movement`, `art/foundations/visual-centerline`, `art/layout`, `art/painting`, `art/perspective`, `art/process`, `art/process/staged-drawing`, `art/publication-design`, `art/rendering`, `art/storyboarding`, `art/subjects/animals`, `art/subjects/animals/gesture-locomotion`, `art/subjects/animation`, `art/subjects/figure`, `art/subjects/figure/anatomy`, `art/subjects/figure/construction`, `art/subjects/figure/gesture`, `art/subjects/figure/hands`, `art/subjects/figure/heads` |
| Also bundled | the `metaskills` baseline every release carries |
| Skillset Memory | `memory/art/` (read-only) |
| Helpers | `scripts/skillforge_runtime.py`, `scripts/skillforge_drill.py` (blind Drills) |
| ZIP | `SkillForge-Art.zip`, 9,310,904 bytes |
| SHA-256 | `9a76ee788ae302be22f1e1d3d7d668100335fa1f3b8b455a810f43876824bb64` |

## What it covers

- Foundations: form construction, gesture and force, observation, mark-making, ideation, visual centerline, movement over time.
- Figure (anatomy, construction, gesture, heads, hands), animals, and animation subjects.
- Composition, perspective, color, painting, rendering, sketching, layout and publication design.
- Comics (covers, inking, page construction), storyboarding, and a staged drawing process.

## Install

The ZIP holds one folder, `SkillForge_Art/`, with `SKILL.md` at its root. Keep that
folder whole: its library, helpers and license files belong together.

- **Claude Code:** extract it so the skill sits at `.claude/skills/skillforge-art/SKILL.md`
  in a project, or `~/.claude/skills/skillforge-art/SKILL.md` for every project.
- **Codex:** extract it to `.agents/skills/skillforge-art/` in the repository.
- **Claude.ai, ChatGPT and other Agent Skills hosts:** upload the ZIP as a skill.
- **Anything else:** extract it and start from its `SKILL.md`.

## Use

Ask for drawing, critique, rendering, composition, perspective, figure or comics help; the skill routes to the few cards the task needs.

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
