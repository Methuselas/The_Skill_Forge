# Eval — does the write barrier change produced code?

status: v1
created: 2026-08-29

## The question

The software-engineering skill gained a **write barrier** on 2026-08-28: seven
numbered steps to run before writing or changing code, with a fail-closed rule.
It was tested once, by hand, on one unit, by a run that knew it was being tested.
That is an anecdote, not a measurement.

This eval asks the same question with repetition and a baseline:

> Does the barrier change the code that comes out, or is it text that sits in the
> entrypoint and is skimmed?

## Design

Two arms, identical in every respect except one paragraph of instruction.

| arm | what it is told |
|---|---|
| `with` | Load the `software-engineering` skill and follow its write barrier. |
| `without` | Implement it well. No mention of the skill or the barrier. |

Both arms get the same task, the same header, and the same prohibition on reading
the reference implementation. **The baseline is not crippled** — it is told to do
a good job. If a careful implementer reaches the same answer unaided, the barrier
adds nothing, and that is a real result rather than a failed eval.

Each arm runs N times. Results are reported as mean ± stddev per assertion, with
the delta between arms, because a single run of either arm proves nothing.

## The task

Implement `src/gateway.cpp` from `src/gateway.h`, in the warzone2100 corpus at
`workspace/sources/Cpp/extracted/warzone2100-master/`.

The unit was chosen because **the header under-specifies behaviour that only the
call sites reveal**. `gwNewGateway` normalises its coordinates smallest-first and
clamps them to the map edge. The header says none of this. A comment at
`src/gamestate_serialize.cpp:3219` says it outright, and the ownership of the raw
`GATEWAY *` pointers in `GATEWAY_LIST` is answerable from how `gwShutDown` is
used across nine call sites.

That makes barrier step 1 — *read the declarations and call sites, not the names* —
directly measurable: an arm that runs it finds the reorder and the clamp, and an
arm that does not writes plain insertion.

## Assertions

Graded mechanically against the produced file by `grade.py`. Each is objectively
checkable; none asks whether the code is "good".

| id | assertion | barrier step it tests |
|---|---|---|
| `A1_ownership` | Something deletes the heap-allocated gateways on shutdown | 1, 2 |
| `A2_reorder` | Coordinates are normalised so the smaller comes first | **1** |
| `A3_clamp` | Coordinates are clamped to the map bounds | **1** |
| `A4_read_callsites` | The run's own notes cite a call site or the reorder/clamp comment | **1** |
| `A5_invariant` | At least one assertion or explicit invariant check is present | 2 |
| `A6_house_idiom` | Uses the declared `GATEWAY_LIST` rather than substituting a container | 5 |

`A2` and `A3` are the substantive discriminators: they are facts obtainable only
from outside the header. `A4` is direct evidence the mechanism ran.

## Honest limits — read before quoting a result

* **Mechanical grading measures mechanical things.** These assertions test
  barrier steps 1, 2 and 5 well. Step 4, about state crossing a decomposition
  seam, has no objective check and is not graded here. A good score is not a
  claim that the barrier works in general.
* **One unit.** A barrier that helps on a C header with hidden call-site
  behaviour may do nothing on a task with no such behaviour to find.
* **Small N.** v1 runs three per arm. Three is enough to see a large effect and
  not enough to see a small one. If the arms overlap within one standard
  deviation, the honest reading is "no effect detected", not "no effect".
* **The grader is regex-based**, so it can be fooled by code that mentions a
  concept without doing it. Spot-check the produced files before believing a
  number.
* **Author is the grader.** The assertions were written by the same runtime the
  eval measures, after reading the reference implementation. That is a real
  conflict; the mitigation is that every assertion is checkable by a third party
  against the produced file.

## Running it

```bash
# 1. launch N agents per arm, each writing to runs/<iteration>/<arm>/run<i>/
# 2. grade every produced file
python workspace/evals/barrier_gateway/grade.py runs/iteration-1

# 3. aggregate to mean +/- stddev with the delta
python workspace/evals/barrier_gateway/aggregate.py runs/iteration-1
```

## In-flight state (2026-08-29)

Iteration 1 was launched with three agents per arm and may not have completed.
The run directories under `runs/iteration-1/` are committed empty on purpose, so
a later session can see the intended shape.

To pick this up cold:

1. Check `runs/iteration-1/*/run*/` for `gateway.cpp` and `notes.md`. Any run
   missing both never finished and should be relaunched, not graded.
2. Relaunch missing runs with the prompt in `prompt_with.md` or
   `prompt_without.md`, substituting `<COMMON>` from `prompt_common.md` and
   `<OUTDIR>` with that run's directory.
3. Grade, then aggregate. Do not report a delta without the standard deviations
   beside it.

The two arms must stay identical apart from their final paragraph. If a prompt is
edited, the previous iteration's numbers are no longer comparable and the
iteration directory should be abandoned rather than mixed.

## Harness defect found on iteration 1

The "you may not open `src/gateway.cpp`" rule is not sufficient. A repo-wide grep
for a symbol echoed three lines of that file into one run's context before it
thought to exclude the path. The run disclosed this itself, unprompted, and
recorded it in its notes.

Fix the prompt before iteration 2: ban reading the reference file **and** any
search whose output can quote it, and require the exclusion flag on every
tree-wide search. A run that reports such a leak should be marked
`contaminated: true` in its grade rather than silently kept or silently dropped —
its own claim that the leaked lines "only confirmed" existing conclusions is the
run assessing its own contamination, which is not evidence.

## Iteration 1 outcome: material good, instrument not

All six runs completed and their outputs are committed. **No result should be
quoted from them yet — the grader is not trustworthy.**

Three regex defects were found by spot-checking, exactly as the limits section
above said to do:

* `A1` looked for `delete` and missed `free()`, failing a run that released
  correctly.
* `A3` missed `std::max<int>(...)` because the pattern assumed no explicit
  template argument — a false negative.
* `A3` also matched a validating `ASSERT_OR_RETURN(..., x1 < width ...)` as if it
  were a clamp — a false positive. Validation rejects bad input; a clamp assigns.
  The first version of this eval therefore reported a 67-point separation on its
  headline assertion that was an artifact in both directions.

After repairing those, `A3` reported failure for every run while the same pattern
matches the text when tested directly against the file. So at least one further
defect remains in `grade.py` and it has not been found.

Four of six assertions sat at 100% in both arms, including the one meant to be
direct evidence the mechanism ran. An assertion that never discriminates measures
nothing, which is a design fault in the assertion rather than a finding about the
arms.

**Before iteration 2:** fix and unit-test `grade.py` against known-good and
known-bad fixtures before grading anything, and replace the four ceiling
assertions. The six implementations already on disk are a free fixture set for
that work — no agents needed.
