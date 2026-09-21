# SkillForge Agent Kit

Keeps several AI agents (Claude, Codex, local models, or several sessions of one) from stepping on each other when they work in the same project. A lead creates bounded tasks; workers claim them atomically; every task holds the files and named resources it will change until it is closed, so two agents never edit the same thing at once.

[Download SkillForge-Agent-Kit.zip](SkillForge-Agent-Kit.zip)

| | |
|---|---|
| Skill name | `skillforge-agent-kit` |
| Built from | PASS `1.0.0-beta.73` |
| Domain cards | 0 Patterns, 0 Action Protocols, 0 Drills |
| Modules | `agent-kit/coordination` |
| Also bundled | the `metaskills` baseline every release carries |
| Helpers | `scripts/skillforge_runtime.py`, `library/agent-kit/coordination/runtime/agentkit.py` |
| ZIP | `SkillForge-Agent-Kit.zip`, 92,237 bytes |
| SHA-256 | `db69ba7870666bcae49ef70cc25d84b331c4af1f01ca5bb6dc2ae5afa5ba71dc` |

## What it covers

- Lead and worker roles, task specs with goal, scope, non-scope, dependencies, required capabilities, verification and required evidence.
- Atomic claims, path and resource scopes held until close, leases renewed by heartbeat, and short holds on shared processes such as a running editor or a build.
- Attribution of each task's commits and changes, even when several agents share one checkout; flags edits nobody claimed.
- Named reviewers, review verdicts, rework, notes on any open task, stale-spec detection, and a generated status board.

This release ships the coordination runtime (`agentkit.py`, standard-library Python) and its README; the protocol cards are not written yet, so its knowledge beyond the runtime README is the shared `metaskills` baseline.

## Install

The ZIP holds one folder, `SkillForge_Agent_Kit/`, with `SKILL.md` at its root. Keep that
folder whole: its library, helpers and license files belong together.

- **Claude Code:** extract it so the skill sits at `.claude/skills/skillforge-agent-kit/SKILL.md`
  in a project, or `~/.claude/skills/skillforge-agent-kit/SKILL.md` for every project.
- **Codex:** extract it to `.agents/skills/skillforge-agent-kit/` in the repository.
- **Claude.ai, ChatGPT and other Agent Skills hosts:** upload the ZIP as a skill.
- **Anything else:** extract it and start from its `SKILL.md`.

## Use

Install it in the project the agents share (both folders below if Claude and Codex work there), then add one line to that project's `AGENTS.md` / `CLAUDE.md`: *register and claim through the Agent Kit skill before changing files*. Each agent then runs:

```text
python <skill-folder>/library/agent-kit/coordination/runtime/agentkit.py --help
```

Read `library/agent-kit/coordination/runtime/README.md` in the release for the lead and worker loops. Task state lives in the project (`.git/agent-kit/state.db`), never in the skill.

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
