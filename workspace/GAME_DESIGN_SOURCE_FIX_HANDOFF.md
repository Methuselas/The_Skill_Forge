# Handoff — Fix the game-design source to match the repo

**For:** the Game Design project chat
**Why:** the archive that produced the last drop contains a defect that broke the whole SkillForge repo. It has been fixed in the repo. Your source still has it, so the next archive will reintroduce it unless you make the identical change.

There are two separate items. The first is the defect. The second is how the archive is exported, which caused a different and worse problem.

---

## 1. The defect: two cards share one `object_id`

Two files in `library/game-design/foundations/` both declared:

```yaml
object_id: PAT_match_practiced_behavior_to_the_intended_outcome
```

They are genuinely different cards — different names, different bodies, 61 lines and 59 lines. It reads as a rename that stopped before the front matter: the file was renamed and retitled and its `object_id` was left behind.

### What it cost

One duplicate id fails `PASS/tools/validate.py`. Every release build, index check, domain-independence test and memory-portability test runs the validator first, so that single line produced **24 test failures** and blocked every release recipe. The other four packages — software-engineering, writing, art, metaskills — validated cleanly the whole time. The repo was one line from green.

This is worth knowing for its own sake: a duplicate `object_id` is not a local problem. Card ids are unique library-wide, so one collision inside one lane takes down every lane's build.

### The exact fix

**File:** `library/game-design/foundations/PAT_align_repeated_and_rewarded_behavior_with_intended_outcomes.md`

**Change one line in the front matter:**

```diff
-object_id: PAT_match_practiced_behavior_to_the_intended_outcome
+object_id: PAT_align_repeated_and_rewarded_behavior_with_intended_outcomes
```

Nothing else in that file changes. The `name:` field already reads `Align Repeated and Rewarded Behavior with Intended Outcomes`, and the filename already matches, so the new id is the one both were already implying.

**Do not touch** `library/game-design/foundations/PAT_match_practiced_behavior_to_the_intended_outcome.md`. Its id was the correct one all along.

### Then regenerate the indexes

Two index files were stale in the drop. They are generated artifacts and must never be hand-edited:

```bash
python PASS/tools/build_index.py
```

That rewrote `library/game-design/INDEX.md` and `library/game-design/foundations/INDEX.md`.

### Verify

```bash
python PASS/tools/validate.py --package game-design    # expect: PASS: 18 object(s)
python PASS/tools/validate.py                          # expect: PASS: 1444 object(s)
python -m unittest discover -s tests -p "test_*.py"    # expect: OK, 110 tests
```

---

## 2. Left for you to decide: three cross-links

Three cards point at the id that was duplicated:

```
characters/PAT_balance_character_roles_by_consequential_contribution.md:25
foundations/PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create.md:21
foundations/PAT_translate_genre_into_play_requirements.md:23
```

All three read:

```yaml
target_object_id: PAT_match_practiced_behavior_to_the_intended_outcome
```

While the id was duplicated, those links were ambiguous. After the fix they resolve unambiguously to **`PAT_match_practiced_behavior_to_the_intended_outcome`** — the "match practiced behaviour" card.

**This validates and was left as-is deliberately.** If any of those three meant to point at the *align* card instead, repoint it to `PAT_align_repeated_and_rewarded_behavior_with_intended_outcomes`. That is a judgement about game-design content, not about the defect, and guessing would turn a working link into a wrong one.

Check each one and decide. If all three meant the match card, nothing more to do.

---

## 3. The bigger problem: the archive is a whole-repo snapshot

This one matters more than the defect.

The drop archive did not contain only the game-design lane. It contained the whole repository tree, including `memory/software-engineering/`. Merging it therefore **overwrote another lane's memory store with a stale copy**, silently deleting two entries that had been written and committed in between. They were recoverable from git history, but nothing in the tooling could have detected the loss: the memory tool verifies each write by reading the file back, which confirms the write against the file and not against what another tree is about to commit over it.

The tell was indirect — a memory entry citing two events that no longer existed. Without that cross-reference the deletion would have gone unnoticed.

### What to change

**Export only the lane.** An archive from this project should contain:

```
library/game-design/**
memory/game-design/**
```

and nothing else. No `library/art`, no `library/software-engineering`, no `library/writing`, no `memory/` for any other domain, no `PASS/`, no `tests/`, no root files such as `CLAUDE.md`, `AGENTS.md` or `ARCHITECTURE.md`. Those are shared and are edited by other lanes between drops, so shipping them means shipping whatever state they were in when this project's copy was taken.

This mirrors how the art lane's drops already have to be handled: merge additively, never sync, never let a drop replace a file the drop does not own.

**If a whole-tree archive cannot be avoided**, then before merging, extract only the two paths above from it and leave everything else in the archive untouched.

---

## 4. Checklist before producing the next archive

- [ ] `object_id` in every card matches its filename, and no two cards anywhere share one.
- [ ] `python PASS/tools/build_index.py` has been run and the indexes are current.
- [ ] `python PASS/tools/validate.py` reports PASS for the whole library, not only for `--package game-design`.
- [ ] The archive contains `library/game-design/**` and `memory/game-design/**` and nothing outside them.
- [ ] No generated `INDEX.md` was hand-edited.

The first item is the one that bit this time, and it is worth a mechanical check rather than an eye. This finds every collision in the library in one pass:

```python
import glob, io, re, collections, os
ids = collections.defaultdict(list)
for f in glob.glob("library/**/*.md", recursive=True):
    m = re.search(r"^object_id:\s*(\S+)", io.open(f, encoding="utf-8", errors="replace").read(), re.M)
    if m:
        ids[m.group(1)].append(os.path.relpath(f, "library").replace("\\", "/"))
for k, v in ids.items():
    if len(v) > 1:
        print(k)
        for p in v:
            print("   ", p)
```

Silence means clean.
