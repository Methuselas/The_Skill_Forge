# SkillForge Software Engineering

Engineering judgment for design, implementation, review, refactoring and testing, written language-agnostically in `core` with C++ and Unreal Engine modules on top. Includes the Code Apprenticeship runner for studying real human-written code.

[Download SkillForge-Software-Engineering.zip](SkillForge-Software-Engineering.zip)

| | |
|---|---|
| Skill name | `skillforge-software-engineering` |
| Built from | PASS `1.0.0-beta.60` |
| Domain cards | 570 Patterns, 39 Action Protocols, 78 Drills |
| Modules | `software-engineering/core`, `software-engineering/languages/cpp`, `software-engineering/unreal-engine` |
| Also bundled | the `metaskills` baseline every release carries |
| Skillset Memory | `memory/software-engineering/` (read-only) |
| Helpers | `scripts/skillforge_runtime.py`, `scripts/skillforge_drill.py` (blind Drills), `scripts/skillforge_code_study.py` (Code Apprenticeship) |
| ZIP | `SkillForge-Software-Engineering.zip`, 2,156,551 bytes |
| SHA-256 | `6e4bfb3ca1d2c450d7f2efed532e95e02884bd3998a062018e677214b01439c5` |

## What it covers

- Contracts, error handling, readability, modularity, testing, concurrency and maintainability (core).
- Modern C++ practice (languages/cpp).
- Unreal Engine editor tooling: modules, modes, command routing, selections, transactions, menus and verified asset edits (unreal-engine).
- Blind Drill administration and Code Apprenticeship study of real code.

## Install

The ZIP holds one folder, `SkillForge_Software_Engineering/`, with `SKILL.md` at its root. Keep that
folder whole: its library, helpers and license files belong together.

- **Claude Code:** extract it so the skill sits at `.claude/skills/skillforge-software-engineering/SKILL.md`
  in a project, or `~/.claude/skills/skillforge-software-engineering/SKILL.md` for every project.
- **Codex:** extract it to `.agents/skills/skillforge-software-engineering/` in the repository.
- **Claude.ai, ChatGPT and other Agent Skills hosts:** upload the ZIP as a skill.
- **Anything else:** extract it and start from its `SKILL.md`.

## Use

Ask for design, implementation, review, refactoring, testing, C++ or Unreal editor help; the skill routes to the few cards the task needs.

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
