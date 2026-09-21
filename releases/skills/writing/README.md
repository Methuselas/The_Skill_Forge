# SkillForge Writing

Craft knowledge for fiction, poetry, creative nonfiction and life writing, college admission essays and career documents: drafting, structure, viewpoint, voice, dialogue, imagery, revision, feedback and submission.

[Download SkillForge-Writing.zip](SkillForge-Writing.zip)

| | |
|---|---|
| Skill name | `skillforge-writing` |
| Built from | PASS `1.0.0-beta.73` |
| Domain cards | 195 Patterns, 31 Action Protocols, 92 Drills |
| Modules | `writing/adventure-modules`, `writing/career-documents`, `writing/college-admission-essays`, `writing/creative-nonfiction`, `writing/fiction`, `writing/foundations`, `writing/poetry` |
| Also bundled | the `metaskills` baseline every release carries |
| Skillset Memory | `memory/writing/` (read-only) |
| Helpers | `scripts/skillforge_runtime.py`, `scripts/skillforge_drill.py` (blind Drills) |
| ZIP | `SkillForge-Writing.zip`, 989,221 bytes |
| SHA-256 | `131732df024abe36442aff80fce82d264d1962f62307c53f659dc6e2009c5d04` |

## What it covers

- Foundations shared by every form.
- Fiction, poetry and creative nonfiction.
- College admission essays and career documents.
- Adventure-module writing for tabletop games.

## Install

The ZIP holds one folder, `SkillForge_Writing/`, with `SKILL.md` at its root. Keep that
folder whole: its library, helpers and license files belong together.

- **Claude Code:** extract it so the skill sits at `.claude/skills/skillforge-writing/SKILL.md`
  in a project, or `~/.claude/skills/skillforge-writing/SKILL.md` for every project.
- **Codex:** extract it to `.agents/skills/skillforge-writing/` in the repository.
- **Claude.ai, ChatGPT and other Agent Skills hosts:** upload the ZIP as a skill.
- **Anything else:** extract it and start from its `SKILL.md`.

## Use

Ask for drafting, revision, critique or practice in any of these forms.

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
