# Handoff — Run the review protocol against real code

**Repo:** `D:\Repos\SkillForge`
**Task:** execute `AP_review_code_you_did_not_write` against one slice of a real codebase, and report both of its outputs.

This is a measurement, not a chore. An earlier run of this protocol was made by the same person who last amended it, which is the weakest form that evidence can take. The point of this run is that you are not that person. Everything below is mechanics; there is deliberately nothing here about what any previous run found, and you should not go looking.

---

## 1. Read the protocol first

```
library/software-engineering/core/code-quality/AP_review_code_you_did_not_write.md
```

Read it in full before starting, including the Notes. It has an entry state, eight steps, two gates and a completion check. Follow it as written rather than reviewing the way you normally would — what is being tested is the protocol, not your taste.

Step 8 is the part most likely to be skipped, because everything before it is about the code and step 8 is about the guidance you judged the code with. Do not skip it.

## 2. Query memory before you start

The lane's skill entrypoint asks for this, and it is part of what is being exercised:

```bash
python PASS/tools/memory.py query --domain software-engineering --cues "review this code" --cues "unfamiliar"
```

Add cues drawn from whatever you end up looking at. What comes back is an observation carrying a stated confidence, not an instruction — read it as something that might apply, and say in your report whether any of it actually did.

## 3. Choose your own slice, freely

Corpora are on disk under `workspace/sources/` (untracked, large, already present):

```
C/AROS-master              an AmigaOS reimplementation, systems C
Cpp/extracted/             six game codebases: warzone2100, DevilutionX, endless-sky,
                           freeorion, gemrb, wesnoth
Go/prometheus              monitoring server
Python/pydantic            validation library
Rust/ripgrep               search tool, library crates with published consumers
```

Pick **one slice you have not read**: a single class, module, or file of roughly 200 to 500 lines, plus its header or interface if it has one. Choose it freely rather than hunting for somewhere you suspect is weak — how the slice was chosen changes what step 8 returns, and a freely chosen one is the honest measurement.

Say in your report which slice you chose and why, in one line.

## 4. You can compile and run things

This matters more than it sounds. A finding you have executed is a different kind of claim from one you have argued, and several of the protocol's outputs are worth turning into a small reproduction.

**Python** — on PATH: `python` (3.12).

**Go** — `D:\tools\go\bin\go.exe` (1.27). Not on PATH; call it by full path. For a scratch program set `GOCACHE` and `GOPATH` somewhere temporary and `go mod init scratch` first.

**Rust** — `D:\tools\rustup\toolchains\stable-x86_64-pc-windows-msvc\bin\rustc.exe` (1.98). Use that path rather than the launcher under `D:\tools\cargo\bin`, which needs `RUSTUP_HOME` and `CARGO_HOME` set because the install is not in the default location.

**C and C++** — MSVC is present but `vcvars64.bat` is broken on this machine, so set the paths yourself. This batch file works; put it beside your source and run it:

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

The batch sometimes reports it cannot find the produced `.exe` even when the build succeeded; run the executable directly afterwards rather than trusting that message.

Where you reproduce something, transcribe the actual output into the report rather than describing it.

## 5. Do not consult these

The run is only worth something if the slice and the findings are yours.

- **This repo's recent commit messages and its `training_history.jsonl`** describe what other runs produced. Do not read them before you have formed your own findings. Afterwards is fine and probably interesting.
- **Any other chat.** Start from the protocol and the code.

Memory *entries* retrieved through `memory.py query` are fine and are part of the exercise — they are written as general observations rather than as a record of what a particular run found.

## 6. Report

Two outputs, kept separate, exactly as the protocol's completion check asks.

**Code findings.** Ranked by what the defect can break, not by how easily you found it. Each names the defect, where it is, and what it can break. Include the families you examined and found acceptable, including the ones that produced nothing — a list of six defects and nothing else cannot be distinguished from a review that stopped after six.

**Guidance findings.** What the reading showed about the library you judged the code with. Each entry sorted into one of the protocol's three outcomes, and each naming either the object id that covers it or the search you ran that came back empty. Do not skip the gate that comes before the sorting.

Also report, in a line each:

- whether anything memory returned actually applied
- whether any candidate finding you were about to report was dropped, and what stopped it
- whether step 8 produced anything, or genuinely produced nothing

A run that returns no guidance findings is a real result and should be reported as one. It is not a failed run and it should not be padded.

## 7. Environment check before you start

```bash
python PASS/tools/validate.py                        # expect PASS across the library
python PASS/tools/memory.py validate                 # expect PASS across 4 stores
python -m unittest discover -s tests -p "test_*.py"  # expect OK, 110 tests, ~220s
```

If any of those is already failing, say so and stop — a broken tree is somebody else's problem arriving in the middle of yours, and working through it will contaminate the run.

Do not commit anything. Report; the repair decisions come after.
