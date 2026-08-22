# Tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

Both suites run from that one command. Keep it that way — a test file outside
this directory is a test nobody runs.

## What each suite can prove

**`test_architecture.py` — repository invariants.** The library validates, cards
are self-contained, domains stay isolated, rule leads stay in sync between
`CLAUDE.md` and `AGENTS.md`, releases ship their prerequisite closure.

**`test_skillforge_runtime.py` — resolver behavior.** Profiles parse; a given
request string resolves to a given mode and lane; declared risk checks are
reported; every card reference in every profile resolves to a real `object_id`;
the completion audit reports what a record omits.

## What no suite here can prove

Nothing in this directory touches a live host. These behaviors depend on the
model and the host honoring the contract, and only regression testing an actually
installed skill can show whether they held:

- Skill auto-loading, and whether the resolver is invoked at all
- Mode Lock persisting across turns
- Stage Lock — a ratified stage staying authoritative
- Visual Lock — later work developing the predecessor rather than reinterpreting it
- Exact-predecessor availability to the native image tool
- One approval producing exactly one transition
- No silent fallback to Direct generation while staged

A test asserting that `art.yaml` names a Stage 4 AP proves the YAML says so. It
does not prove any host will execute Stage 4 through it. Tests named
`test_art_profile_declares_*` are that kind: declaration checks, not behavior
checks. Do not cite them as evidence of host behavior.

Release structure (files ship, references survive materialization, packages stay
portable) is proved by `PASS/tools/build_release.py` at build and check time, not
here.
