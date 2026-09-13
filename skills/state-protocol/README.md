# SkillForge State Protocol

SkillForge State Protocol gives local models, project-based assistants, and
multi-agent repositories compact continuity without treating chat transcripts
or a search index as memory. Markdown is canonical, generated indexes are
disposable, and the model remains responsible for semantic judgment.

[Download the current release](../../releases/SkillForge-State-Protocol.zip) ·
[Release details and checksum](../../releases/README.md)

## Use it for

- resuming work after a model loses or exhausts its context window;
- maintaining compact project state in append-only continuity packets;
- storing consented user preferences separately and only for the active skill;
- coordinating several models or agents without mixing unrelated workstreams;
- crawling and searching a user-controlled local Markdown store.

## Operating profiles

**Portable Manual** works in project libraries and other hosts without Python or
a writable local filesystem. At a material boundary, the model writes a uniquely
named, complete Markdown snapshot. Quick questions and unchanged sessions can
remain ephemeral.

**Local Store** uses the bundled standard-library Python tool. It can initialize,
resume, search, propose, commit, checkpoint, crawl, and validate a store. Project
state and per-user, per-skill adaptation use separate roots and separate
disposable SQLite indexes.

**Multi-Model** gives each coherent body of work a stable `project_id` and
`workstream_id`; `created_by` records the current contributor without making the
model's identity the namespace. Separate worktrees or checkouts are still
required when agents could collide on the same source files.

## Why snapshots have unique names

Project libraries commonly preserve every newly created file and rename
collisions. State Protocol therefore never relies on replacing `memory.md`.
Packets use a sequence, timestamp, and unique suffix, for example:

```text
SP__my-project__main__r000042__20260912T214500Z__7c2a.md
```

Sequence numbers describe continuity lineage; they are not Semantic Versions.
The protocol schema and the SkillForge release are versioned separately.

## Install

Install or upload the ZIP as one skill. For a manual project-library workflow,
make its `SKILL.md` and relevant references available to the model. For local
automation, extract the archive and use the tool under
`library/state-protocol/local/tools/` with Python 3; it has no third-party
dependencies.

## Memory boundaries

State Protocol deliberately separates three things:

- project continuity: what one workstream is doing;
- user skill adaptation: how one user wants an activated skill applied;
- PASS Skillset Memory: empirical evidence about how a skill performed.

None overrides the others. A crawler retrieves candidate records; it does not
decide what is true, authoritative, or relevant.
