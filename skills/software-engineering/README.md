# SkillForge Software Engineering

SkillForge Software Engineering is an implementation and review skillset for
models working in real repositories. It emphasizes contracts, call-site
evidence, maintainable changes, explicit failure behavior, and verification
against the requested outcome.

[Download the current release](../../releases/SkillForge-Software-Engineering.zip) ·
[Release details and checksum](../../releases/README.md)

## Use it for

- software design, implementation, debugging, and refactoring;
- code review, readability, modularity, contracts, and error handling;
- test design, boundary analysis, and completion verification;
- repository-scale maintenance and architectural decisions;
- C++ engineering through the currently bundled language module.

The core engineering library is broadly applicable. C++ is the present
language-specific package; additional languages can be released later without
changing the core contract.

## How it works

Before productive code changes, the skill requires the model to inspect the
actual declarations and call sites, name the invariant and failure signal,
state its input assumptions, and match the repository's existing conventions.
It then retrieves a bounded set of Action Procedures and Patterns rather than
preloading the whole library.

## Install

Install or upload the ZIP as one skill. If the host expects a directory, extract
the archive and point it at the extracted `SkillForge_Software_Engineering`
folder. The entry point is `SKILL.md`.

Python is optional. The helpers resolve the execution contract, verify recorded
completion checks, and administer blind Drills; they do not edit code or judge
the result.

## Persistence boundary

The release may include a read-only snapshot of Software Engineering Skillset
Memory. It records empirical test evidence, never overrides canonical cards,
and is separate from project continuity. Rebuilds and changes originate in
PASS.
