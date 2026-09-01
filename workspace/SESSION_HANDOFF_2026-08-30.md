# Handoff — SkillForge, software-engineering lane, 2026-08-30

**Repo:** `D:\Repos\SkillForge` — clean, in sync with `origin/main`, suite green.
**Read first:** `CLAUDE.md` (hard rules), then `.claude/skills/software-engineering/SKILL.md` (the lane's entrypoint, including the write barrier and the memory section).

This is a state handoff for continuing the work, not a sterile one. It carries context deliberately.

---

## 1. Verified state

| package | objects |
|---|---|
| software-engineering | 608 |
| art | 547 |
| writing | 269 |
| game-design | 18 |
| metaskills | 5 |

`memory.py validate` → 4 stores, 27 entries, 77 events. Suite → 113 tests OK, ~225s. Nothing unpushed.

Untracked in `workspace/`, deliberately: `GAME_DESIGN_SOURCE_FIX_HANDOFF.md`, `REVIEW_PROTOCOL_RUN_HANDOFF.md`, `REVIEW_PROTOCOL_RUN_2_HANDOFF.md`, `REVIEW_PROTOCOL_RUN_2_REPORT.md`, `REVIEW_PROTOCOL_RUN_3_HANDOFF.md`, and this file.

---

## 2. Query memory before doing anything productive

Do not skip this and do not read the entries out of this document — they are the system of record and restating them here would create a second copy that rots.

```bash
python PASS/tools/memory.py query --domain software-engineering --cues "review this code" --cues "count"
```

Fourteen active entries, one monitoring, two resolved. The ones most likely to fire during ordinary work:

- `SE_MEM_009`, `SE_MEM_012` — how measurements of a codebase go wrong. Between them they cover a wrong search pattern, a correct pattern over the wrong region, a correct number with an invented cause, and a keyword scan mistaken for a result. All four happened here.
- `SE_MEM_011` — the shapes a card takes when it fails against a language it was not written from, and the cheap reading sweep that finds three of the four. Read its boundary: the sweep cannot find a condition that is merely narrow.
- `SE_MEM_010` — this runtime stops one sentence before the conclusion when a check asks what an exercise revealed. Confirmed against checks it did not author.
- `SE_MEM_002` — do not report an inconsistency before asking whether it follows a structural line. Fired correctly twice today.
- `SE_MEM_015` (resolved) — which toolchains are available and how to invoke them. Section 4 below repeats only the invocations, because those are environment facts rather than observations.

**No open review items.** `SE_EV_0035` has since been consolidated, and nothing is awaiting consolidation. Two entries have been added since this file was written; they are in the store and are deliberately not described here.

---

## 3. What the productive loop turned out to be

Most of the day went into the library checking itself: card-against-card sweeps, drill grading, schema work. That found real things and it has a ceiling, because an internal sweep can only surface *disagreement*, and a card wrong in the same way as its neighbours reads as consistent to all of them.

The loop that kept producing is `AP_review_code_you_did_not_write` run against a slice of a real codebase, taking both of its outputs seriously — the defect list *and* step 8, which asks what the reading showed about the guidance. Four runs, four productive. Between them they produced two new cards, four widened cards, and a set of confirmed defects in code nobody here wrote.

Two things make it work:

- **Step 8 must be asked for explicitly.** The review's attention is on the code, and the guidance findings do not appear unless the step is run. It has a gate in front of it now: settle whether the code is *right* before classifying it, because a defect mistaken for practice will widen a card until it endorses the defect.
- **Reproduce rather than argue.** Section 4. Several findings changed character entirely once compiled.

The protocol is at `library/software-engineering/core/code-quality/AP_review_code_you_did_not_write.md`. Read it before running it; it has eight steps and two gates.

---

## 4. You can compile and run things

This is the biggest capability change and it is not discoverable from the repo.

**Python** — `python` on PATH (3.12).

**Go** — `D:\tools\go\bin\go.exe` (1.27). Not on PATH. For a scratch program set `GOCACHE` and `GOPATH` to temporary paths and `go mod init scratch` first.

**Rust** — `D:\tools\rustup\toolchains\stable-x86_64-pc-windows-msvc\bin\rustc.exe` (1.98). Use that path, **not** the launcher in `D:\tools\cargo\bin`, which needs `RUSTUP_HOME` and `CARGO_HOME` set because the install is not in the default location.

**C / C++** — MSVC is present and `vcvars64.bat` is broken on this machine. Write this batch beside your source and run it:

```bat
@echo off
set "MSVC=C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools\VC\Tools\MSVC\14.50.35717"
set "SDK=C:\Program Files (x86)\Windows Kits\10"
set "V=10.0.26100.0"
set "INCLUDE=%MSVC%\include;%SDK%\Include\%V%\ucrt;%SDK%\Include\%V%\um;%SDK%\Include\%V%\shared"
set "LIB=%MSVC%\lib\x64;%SDK%\Lib\%V%\ucrt\x64;%SDK%\Lib\%V%\um\x64"
cd /d "%~dp0"
"%MSVC%\bin\Hostx64\x64\cl.exe" /EHsc /std:c++17 /nologo /W4 yourfile.cpp
```

The batch sometimes claims it cannot find the produced `.exe` when the build actually succeeded — run the executable directly afterwards instead of believing that message.

Corpora are under `workspace/sources/` (untracked, present): `C/AROS-master`, `Cpp/extracted/` (warzone2100, DevilutionX, endless-sky, freeorion, gemrb, wesnoth), `Go/prometheus`, `Python/pydantic`, `Rust/ripgrep`.

**Already reviewed, pick something else:** `endless-sky/source/Account.{h,cpp}` (twice), `freeorion/Empire/ResearchQueue.{h,cpp}`, `pydantic/_internal/_utils.py`.

---

## 5. Open work, in the order I would take it

Four of the five below have closed since this file was written. They are kept rather than deleted
because what each one turned into is the useful part, and a list that only shows what is left
hides where the answers came from.

**a. Consolidate `SE_EV_0035` into an entry. — DONE.** It is `SE_MEM_016`, and it has since been
cited by a second event. Read it from the store rather than from here.

**b. Run the protocol again, on a fresh slice. — DONE, and worth repeating.** Run 2 took a Go
concurrency component and produced five findings and a step-8 gap that has since been carded. A
third run is set up in `workspace/REVIEW_PROTOCOL_RUN_3_HANDOFF.md`, with run 2's report held in a
separate file so it cannot be read by accident. That separation is the point: this handoff's own
predecessor leaked its findings into the file the next run had to open.

**c. The rewritten drill checks have never been run against. — DONE.** Three were taken blind and
graded: nine of fifteen bullets, with the closing bullet failing in all three. The finding is
`SE_MEM_017`, and it points at the Instructions rather than the checks. Still outstanding underneath
it: a second, *independent* sitting, since the first was graded by the runtime that produced the
answers.

**d. The art lane's 119 drill keys are untouched.** Median 64 words, 5 at strength, 30 carrying
neither discriminating mechanism. `workspace/ART_DRILL_SUCCESS_CHECK_HANDOFF.md` is written and
ready for that project; it is not this lane's work. Deferred by the user, not forgotten.

**e. Game-design source fix. — CLOSED.** The repo side was already fixed; the source side has since
been corrected in that project, including the three cross-links section 2 of its handoff left as a
content judgment. Nothing is pending here. `workspace/GAME_DESIGN_SOURCE_FIX_HANDOFF.md` is worth
keeping only for its sections 3 and 4 — export the lane and nothing else, and run the duplicate-id
scan before producing an archive — which are standing rules for every future drop rather than
one-time repairs.

---

## 6. Operational things that cost time here

- **Gate the suite on its exit status.** `python -m unittest ... && git commit` — not a newline, not `;`. A red suite was stepped over three times today and once reached `origin`. Fix forward rather than rewriting pushed history.
- **Two sessions share this working tree**, and drops from other projects have arrived as whole-repo archives. One overwrote this lane's memory store with a stale copy and silently deleted two events; nothing in the tooling can detect that, because the append tool verifies its write against the file rather than against what another tree is about to commit. The tell was an entry citing events that no longer existed. Run `memory.py review` after any external drop. The same shape turned up inside the tooling and has since been closed there: `memory.py compact --entry` takes the entry's *complete* evidence list, which reads like "add these", and it used to overwrite silently because its readback compared the result against what was passed. It now refuses to drop a citation unless `--replace` says so. The archive case is still undetectable and still wants the manual check.
- **Long content breaks bash heredocs** in this environment. Write the script to a file and run the file.
- **YAML in `skill_memory.yaml` gets reflowed** by the memory tool, so multi-line anchors in a regex will not match. Use `\s+` between words or anchor on a short unique fragment.
- **cwd resets to the repo root** between some tool calls. Use absolute paths.
- **Never paste memory text into a card.** `tests/test_memory.py` enforces it and caught exactly that once today. It also bans the word *page* anywhere in an entry, because that is how a source reference reads when one leaks in.
