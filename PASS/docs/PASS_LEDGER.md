# PASS — Ledger Formats

status: active
owner: docs/domains/corpus
last_reviewed: 2026-07-30
supersedes: PASS_v20.6_ABSOLUTE_SPEC_FLAT.md §6, PASS_LEDGER_SCHEMA.md (v1.0)

The ledger is what makes a run resumable and what makes fail-closed checkable.
It is plain markdown so it reviews in a diff.

---

## Layout

```
sources/                  the books themselves — GITIGNORED, never committed
  <collection>/<file>     optional human-facing grouping; active only

trash/sources/            retired source payload; never committed
  <source_id>/<file>

ledger/                   the run record — tracked
  <source_id>/
    SOURCE.md             what this source is
    UNITS.md              one row per unit, with status
    units/
      <unit_id>.md        dispositions for that unit

library/                  the product — tracked
  <package>/<topic-path...>/
    PAT_*.md  DRILL_*.md  AP_*.md
  INDEX.md                generated — do not hand-edit
```

`library/` paths are derived from each object's `library_path` frontmatter. Its
first segment is the package and all remaining segments are its topic path.
`ledger/` is the run record. `sources/` holds active payload and is
gitignored for copyright and repo-size reasons — see `sources/README.md`.

The SHA-256 is the source identity. `SOURCE.md` records the current
repo-relative `payload_path`, so a move to trash does not sever the local link.

---

## REGISTRY.md — the duplicate guard

`ledger/REGISTRY.md` is the single place that answers "have I already read this
book?" One row per source. Nothing else answers that question, because
`SOURCE.md` only knows about itself — to consult it you must already know the
`source_id`, which is exactly what you don't know when a book reappears under a
different filename.

```markdown
| source_id | title | author | sha256 (first 12) | status | units | objects | closed |
|---|---|---|---|---|---|---|---|
| cpp_pl_4e | The C++ Programming Language, 4th ed. | Stroustrup | 9f2c1a4b8e07 | complete | 44/44 | 312 | 2026-08-02 |
| ppp_2e | Programming: Principles and Practice, 2nd ed. | Stroustrup | 3d7e9902fa11 | in-progress | 6/27 | 41 | |
| gaddis_9e | Starting Out with C++, 9th ed. | Gaddis | b1049cc3de52 | low-yield | 5/18 | 3 | 2026-08-04 |
```

`status`: `queued` · `in-progress` · `complete` · `low-yield` · `abandoned`

`low-yield` means the source was closed early because it stopped producing new
objects, variants, or replacements. It is a legitimate outcome, not a failure, and
recording it stops the book being reopened hopefully.

### The rule: hash before you create

**Before creating a `source_id` or a `ledger/` folder, hash the file and search
the registry for that hash.**

```bash
sha256sum "sources/<file>"                       # git bash
```
```powershell
Get-FileHash "sources\<file>" -Algorithm SHA256  # powershell
```

| Registry says | Do this |
|---|---|
| hash already present | **Stop.** Already processed. Read its row. Do not re-read the book. |
| title matches, hash differs | Different edition — different pagination, so different locators. New `source_id`; note the sibling id in both `SOURCE.md` files. |
| no match | New source. Add the row with `status: queued`, then scaffold `ledger/<source_id>/`. |

The hash is the only part of this that does not depend on somebody remembering
something. Filenames get changed, titles get typed differently, folders get
copied — content does not. Key the guard on content.

### Keeping it honest

The registry is a derived summary; `UNITS.md` files are the ground truth for
counts. If they disagree, the ledger wins and the registry row is stale. Anything
that closes a unit updates both.

### Retiring a closed source

After reconciliation, move the payload to
`trash/sources/<source_id>/<original filename>`. This is required local cleanup,
not deletion: the payload remains available for recovery but leaves the active
source queue. Update `SOURCE.md` with its new `payload_path`, retirement date,
and final registry status. Do not retire a source that has a queued or
in-progress unit.

## SOURCE.md

```markdown
# <source_title>

source_id:    <stable id>
title:        <title>
author:       <author | Unknown>
publish_date: <date | Unknown>
media_type:   <PDF | book | video | course | archive | image_set>
payload_path: <repo-relative active or trash path>
sha256:       <hash of the source file>
added:        YYYY-MM-DD
status:       in-progress | complete | abandoned
text_layer:   usable | mixed | none
visual:       true | false
visual_access: renderer | page_images | both | none
page_images_path: <repo-relative directory or ZIP | none>

## Unit scheme

How this source was divided, and why (chapters, sections, a dense chapter split in
two, three thin chapters batched). Stated once so a later run divides the same way.

## Summary

Filled in at reconciliation:
units processed / empty / blocked · objects added · variants absorbed ·
objects replaced · candidates rejected
```

`sha256` matters: if the file changes, previously processed units may no longer
correspond to the same pages.

`payload_path` is operational metadata, not identity. Update it when the local
payload is moved to trash; never use a path or filename as a duplicate guard.

For PDFs, `text_layer` records the preflight result. `visual_access` records how
an image-dependent source will be inspected; `page_images_path` is required when
that route includes `page_images`. These are run-readiness facts, not object
schema fields. Run preflight before admission because OCR changes the payload
hash. Existing admitted payloads are never silently OCR-replaced: a changed hash
must be reviewed as a source-identity change before more units are processed.

---

## UNITS.md

One row per unit. This is the work queue.

```markdown
| unit_id | label | locator | status | objects | notes |
|---|---|---|---|---|---|
| u01 | Ch.1 The Basics | pp. 1-24 | processed | 7 | |
| u02 | Ch.2 Types | pp. 25-58 | processed | 11 | split from one dense chapter |
| u03 | Ch.3 Front matter | pp. i-xii | empty | 0 | preface, no teachable skill |
| u04 | Ch.4 Figures | pp. 59-80 | blocked | 0 | pages are scans, no text layer |
| u05 | Ch.5 Templates | pp. 81-120 | queued | | |
```

Status values:

| Status | Meaning |
|---|---|
| `queued` | not yet attempted |
| `in-progress` | claimed by a run; set before reading, so a crash is visible |
| `processed` | read and extracted; objects written |
| `empty` | read, genuinely nothing transferable. A real result. |
| `blocked` | could not be read. Reason required. No objects emitted. |

**A locator in an exported object must name a unit whose status is `processed`.**
That is the mechanical form of fail-closed, and the validator checks it.

---

## units/&lt;unit_id&gt;.md

One row per candidate, including the ones that did not ship. Rejections are the
most valuable rows here — they stop the next run from re-litigating the same
material.

New or revised unit ledgers use `ledger_format: 2` and a machine-checkable
candidate count:

```markdown
ledger_format: 2
candidate_count: 5
```

The count must equal the number of disposition rows. A v2 candidate table uses
these columns:

```markdown
| candidate | type | disposition | object_id | grounding | learner_decision | variant_basis | method_or_policy | tradeoff | note |
|---|---|---|---|---|---|---|---|---|---|
```

For a `variant` row, `object_id` names the foundation and `learner_decision`,
`variant_basis`, `method_or_policy`, and `tradeoff` are required. Older ledgers
remain readable during migration; a ledger becomes v2 whenever its unit is
revised.

```markdown
# u02 — Ch.2 Types

read:        2026-07-29
second_read: 2026-07-29
ledger_format: 2
candidate_count: 5

| candidate | type | disposition | object_id | grounding | learner_decision | variant_basis | method_or_policy | tradeoff | note |
|---|---|---|---|---|---|---|---|---|---|
| Prevent object slicing | pattern | new | PAT_prevent_object_slicing | pp. 31-33 worked example | | | | | |
| Copy ctor allocates storage | pattern | variant | PAT_value_semantics_copy | pp. 34-36 | Choose a copy-storage policy | method_sequence | Allocate before copying element state | Trades an up-front allocation for independent value ownership | absorbed as v_02 |
| Use const accessors | pattern | replace | PAT_const_correct_accessor | pp. 40-41 | | | | | supersedes PAT_const_usage_basic |
| RAII practice exercise | drill | new | DRILL_raii_scope_pairing | ex. 2.7 | | | | | |
| Templates exist | — | reject | — | p. 44 | | | | | source fact, not a transferable skill |
```

Dispositions: `new`, `variant`, `replace`, `reject`.

`grounding` names what in the source supports it — a page range plus what is there
(worked example, warning, exercise, table). A row with no grounding is a row that
should have been rejected.

For a `variant` row, the structured fields record the foundation, decision,
method, and concrete source-versus-foundation tradeoff. A source example may
also ground a separate `new` candidate; give each learning claim its own row
rather than discarding the alternative as duplicate evidence.

---

## Accounting rule

Every candidate raised in §3 of the run procedure appears in exactly one row with
exactly one disposition. Candidates do not vanish silently.

If the count of rows does not match the count of candidates raised, the run is
incomplete — say so rather than quietly closing the unit.
