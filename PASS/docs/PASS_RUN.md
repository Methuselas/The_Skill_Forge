# PASS — Run Procedure (per unit)

status: active
owner: docs/domains/corpus
last_reviewed: 2026-07-30
supersedes: PASS_v20.6_ABSOLUTE_SPEC_FLAT.md §3, §4, §10, §11

This is the operating procedure for an assistant running PASS in this repo.

Read `PASS_DOCTRINE.md` and `PASS_SCHEMA.md` first. One run processes **one
unit**. Not one book. If you are tempted to do two, don't — the whole design
depends on a unit being small enough that grounding each object is cheap.

---

## 0. Why one unit

A source-native chapter is the default unit, but a numbered lesson, section, or
bounded section range is valid when it is the smallest instructional scope that
can be read twice and still ground a coherent skill. State that choice in
`SOURCE.md`; do not combine unrelated units merely because they are adjacent.

State lives in files, not in the conversation. That means a run can stop at any
point and the next run continues from the ledger rather than from memory. There
are no `Continue [Y/N]` gates any more; there is a ledger row and a commit.

---

## 1. Preflight, then admit the source

**A source is only admitted through `ledger/REGISTRY.md`.** Never create a
`source_id` or a `ledger/` folder without checking the registry first.

For a PDF, run readiness preflight **before hashing it**:

```text
python tools/preflight_pdf.py "sources/<file>.pdf"
python tools/preflight_pdf.py "sources/<art-book>.pdf" --visual --vision-capable --page-images "sources/<pages>.zip"
```

Preflight identifies a missing or sparse text layer as `NEEDS_OCR`. Stop without
adding a registry row, OCR the PDF, then preflight and hash the final payload.
OCR rewrites the file and therefore changes its SHA-256; hashing first would
admit an identity that the readable payload no longer has. For `visual: true`
sources, preflight also requires a vision-capable model and usable page access
through either a working renderer or a verified page-numbered image directory or
ZIP. Record its reported `text_layer` and selected `visual_access` in `SOURCE.md`.
Inspect any reported `weak_physical_pages` visually; use page-image evidence for
instructional pages whose prose OCR missed.

Once preflight passes:

```
1. Hash the file:  sha256sum "sources/<file>"
                   Get-FileHash "sources\<file>" -Algorithm SHA256
2. Search ledger/REGISTRY.md for that hash.
```

| Registry says | Do this |
|---|---|
| hash present | **STOP.** Already processed. Report its row. Do not re-read the book. |
| title matches, hash differs because an admitted scan was OCR-updated | Verify the page count plus first/middle/last content against the admitted payload. If pagination and content are unchanged, update that source's hash and OCR metadata in one reviewed commit; do not create a false sibling edition. |
| title matches, hash differs | Different edition. New `source_id`; cross-note the sibling id in both `SOURCE.md` files. |
| no match | New source: add a `queued` row, then create `ledger/<source_id>/`. |

Filenames and titles are typed by humans and get changed. The hash is the only
part of this guard that cannot drift, so it is the part that decides. Record the
exact repo-relative `payload_path` in `SOURCE.md`; sources may be grouped under
`sources/` by collection rather than by `source_id`.

## 2. Claim the unit

```
1. Read ledger/<source_id>/UNITS.md
2. Take the first unit whose status is `queued` by default. An explicit user
   selection may choose a different queued unit; record that selection in the
   unit's notes.
3. Set it to `in-progress`, commit that alone
```

If every unit is `processed`, `empty`, or `blocked`, the source is finished — run
the source-level reconciliation in §8 and stop.

## 3. Read the unit — fail closed

Read the actual unit text. Not the table of contents, not the chapter title, not
your prior knowledge of the subject.

**Default to lean text extraction.** For text sources — most coding, math, and
writing books — extract the unit over a page range with `pdftotext` rather than
loading rendered pages or a whole-document reader:

```text
pdftotext -f <first-physical-page> -l <last-physical-page> "<file>.pdf" -
```

It is the token-cheapest way to actually read, and it avoids the context bloat
that forces mid-run compaction (a smaller-window run that reads pages natively can
burn a large share of its budget just compacting to stay alive). Use
`pdftotext -layout` when code alignment, tables, or columns matter — plain
extraction wraps lines and interleaves inline comments, so verify code-heavy
excerpts against `-layout` output before quoting them. Reserve page rendering
(`tools/render_pdf.py`) for `visual: true` sources and for units where layout
carries meaning text cannot (see below). If `pdftotext` returns empty or garbled
text, the page has no usable text layer — render/OCR it or mark the unit
`blocked`; never guess from a bad extraction.

If the unit cannot be read — file missing, extraction garbled, pages are images
with no usable text and you cannot inspect them — set the unit to `blocked` with
the reason, commit, and **stop**. Do not emit objects.

This is the rule that the 2026-03-04 failure violated. Output that looks
structured and authoritative is not evidence that anything was read. If you did
not read it, say so.

As you read, collect the unit's **reading receipt** — verbatim quotes spread
across its pages (or page-image references for image-only pages). This is nearly free
while the extracted text is in front of you, and it is what `verify_grounding.py`
checks in §7. A run that cannot produce spread-out verbatim quotes did not read
the unit. See `PASS_GROUNDING.md`.

For units where layout carries meaning — tables, diagrams, figures, stat blocks,
worked examples, panel sequences, score notation — text extraction alone is not
"read." Inspect the rendered pages, or mark the unit `blocked` on visual
inspection and say which pages.

For an art book, pair the OCR text for each page with that page's image. Read the
prose from extraction and inspect the art from the image; do not spend vision
tokens rereading the same prose from a raster. Scan every page in the bounded
unit at overview resolution, then inspect candidate-bearing pages at full
resolution. A full-page render is still required when layout, sequencing, or the
relationship between text and figure carries the lesson. Source-provided page
images are preferred when they are cleaner than a render and their first,
middle, and last page mapping has been visually confirmed.

### Visual access is infrastructure

A `visual: true` source requires a vision-capable model. If the active model
cannot inspect images, stop: page extraction alone cannot recover an art book's
instruction. It also requires either a working PDF renderer or a verified,
page-aligned image set. A missing visual path is a tooling gap, not permission to
skip visual evidence.

When rendering, use the project helper and record the exact renderer executable
and pages inspected in the worklog:

The helper is `tools/render_pdf.py`:

```text
python tools/render_pdf.py "sources/<file>.pdf" --pages <first>-<last> --output-prefix <output-dir>/<prefix>
```

It renders the visible PDF CropBox to PNG at 150 DPI by default, verifies that
every requested page was written, and reports the executable and exact Poppler command used. Record the
wrapper invocation, resolved renderer, and inspected page range in the unit
ledger or worklog. Set `PASS_PDFTOPPM` or use `--renderer` when Poppler is not
available on `PATH`. Use a fresh output prefix for each render; the helper
refuses existing expected page files so a stale image cannot satisfy a new review.
Use `--media-box` only when material outside the CropBox is intentionally part of
the source; the default avoids blank scanner margins that waste visual context.

A page-image directory or ZIP may substitute for the renderer only when
`preflight_pdf.py` verifies a contiguous one-to-one page count and decodable
first, middle, and last images. The assistant must then visually confirm those
three mappings against the PDF before trusting the sequence. Receipt rows use
`image:` locators as documented in `PASS_GROUNDING.md`.

### Domain evidence checks

Run the smallest check that tests the source's claim rather than merely the card
shape. For a mathematical factorization, expand selected final factors back to
their starting expressions and record the spot-check in the worklog. Do not add
a schema field for domain evidence; the unit ledger and worklog carry it.

### When visual inspection is unavailable

For a source that is **not** marked `visual: true`, there is a third case between
"read" and "blocked": the renderer is unavailable,
but the unit may not contain anything visual to miss. **You may proceed — but only
on proxy evidence you actually have, never on the absence of something you could
not look at.**

```
WRONG: "This chapter has no diagrams whose meaning is lost without rendering."
       (asserts absence of the thing you just said you cannot see)

RIGHT: "Renderer unavailable. Extracted text for pp. X-Y contains no `Figure`
        captions, no `Table` captions, and no in-text figure references.
        Proceeding on text and code, which extracted cleanly."
```

Text extraction preserves captions and cross-references even when it cannot render
the image, so their absence is a checkable fact. Record the proxy in the unit
ledger. If captions *are* present and you cannot view them, that unit is
`blocked` on visual inspection — name the pages.

## 4. Extract candidates

Work through the unit like a learner. Every reusable skill becomes a candidate
pattern, drill, or AP.

For each candidate, write down before anything else:

```
- what the source specifically says, shows, warns about, or exercises
- the locator (page range / section) it came from
```

That grounding note is what makes the body sections writable. If you cannot
produce it, the candidate is not extraction — drop it.

Extract generously. A dense chapter yielding fifteen candidates is normal. Do not
reduce density to save effort.

**State the candidate count explicitly in the unit ledger.** New or revised
ledgers use `ledger_format: 2` plus `candidate_count: N`; the validator compares
that value with the disposition rows. Every candidate raised here must appear in
exactly one row, so a declared count of 11 against 10 rows is an incomplete run
rather than a discrepancy hidden in prose.

## 5. Second read

Re-read the same unit against your candidate list. This is cheap now — the unit is
small.

```
- recover skills the first read missed
- strengthen candidates whose grounding is thin
- split candidates that merged two distinct skills
- drop candidates that turned out to be source facts, not transferable skills
```

The old spec's mandatory double-read over the whole book is what this replaces.

### Decision-versus-method recovery check

For every candidate that may overlap an existing skill, name three things during
the second read and record them in the v2 ledger if the candidate becomes a
variant:

1. the **learner decision** or outcome the source teaches;
2. the **method, policy, or constraint** the source uses to reach it; and
3. the observable tradeoff that changes when that method is chosen.

The row's `object_id` names the foundation; `variant_basis` identifies the kind
of contrast. `learner_decision`, `method_or_policy`, and `tradeoff` are required
fields, not prose hidden in `note`.

One source excerpt may legitimately produce two candidates. It can teach a new
decision **and** supply an alternative method for an existing decision. Split
those claims before placement; shared grounding does not make them duplicates.
For example, an API example can simultaneously teach what kind of result a
caller needs and whether safety checks happen on every call or through a separate
route.

This is a learning check, not a taxonomy exercise. The library should retain the
alternative a practitioner needs to recognize and choose, rather than merely
recording that two sources used the same syntax or keyword.

## 6. Place each candidate against the library

**Never merge "the archive." Merge one candidate against its neighbours.**

For each surviving candidate:

```
1. Retrieve existing objects that could collide:
   same topic or `library_path` prefix, the corresponding foundation or
   specialization route, overlapping tags, similar name.
   Aim for ~5 candidates. If retrieval returns 40, tighten the query.
2. Read those objects.
3. Run the recovery check before choosing a disposition:

   - Same learner decision, different valid method, policy, sequence, or
     constraint -> `variant`.
   - A distinct learner decision plus a different method for an existing one ->
     split into a `new` candidate and a `variant` candidate, even when both come
     from the same source example.
   - No distinct decision and no differing durable method -> `reject`.

   Do not reject a candidate merely because it shares a construct, tag, or code
   listing with an existing card.
4. Decide exactly one disposition for each resulting candidate:

   new       no existing object teaches this skill        -> write a new object
   variant   same skill, different approach               -> absorb into the
                                                             foundation's variants
   replace   genuinely superior to an existing object     -> supersede it, record
                                                             the replaced id
   reject    adds nothing durable                         -> ledger only, no file
```

`variant` and `replace` are different. Different-but-valid is a variant. Better is
a replacement. "Newer" is not "better."

If the skill is broader than the source that taught it, store the portable version
as the foundation and keep the source-specific form as a variant beneath it.
If the rule itself needs a language, tool, framework, medium, style, genre,
tradition, method, or domain constraint, write a specialization instead and link
it to the foundation when available. Use tags to retrieve the context across
these routes; do not create a source-named folder.

## 7. Write, validate, commit

```
1. Write or update object files per PASS_SCHEMA.md
2. Append one disposition row per candidate to the unit's ledger
3. Write the unit's `## Reading receipt` block (see PASS_GROUNDING.md)
4. Set the unit to `processed` (or `empty` if it genuinely yielded nothing)
5. Run BOTH gates:
     python tools/validate.py                              # card shape
     python tools/verify_grounding.py --source <source_id> # actually read
6. Fix every failure. A failing object does not ship; an unverified receipt
   means the unit is not `processed`.
7. Regenerate indexes
8. Commit: one unit, one commit
```

A unit that yielded nothing is a real result. Mark it `empty` and move on — an
unrecorded empty unit gets re-run forever.

Never widen the schema to accommodate a card. A card that disagrees with its
template is the card's bug.

## 8. Source reconciliation

When every unit of a source is closed:

**Publish-boundary invariant:** source closure is not complete while any retained skill exists only in a staging, intake, migration, or candidate tree. Before setting the registry row to `complete`, reconcile every retained standalone object into `library/` and every retained variant into its canonical owner there. Source-reading evidence may be archived under `ledger/<source_id>/evidence/`; rejected or superseded drafts may remain only as clearly noncanonical evidence. Never leave a second active skill corpus beside `library/`.

```
- resolve cross_links that pointed at candidates later rejected or absorbed
- reconcile source-prefixed object_ids into semantic filenames
- regenerate indexes
- append a source summary to `SOURCE.md`:
  units processed / empty / blocked, objects added, variants absorbed,
  objects replaced, candidates rejected
- update the source's row in `ledger/REGISTRY.md`: final status, unit count,
  object count, closed date
- move the payload to `trash/sources/<source_id>/<original filename>`; update
  `SOURCE.md` with the trash `payload_path`, retirement date, and final status
- commit
```

---

## Cost model

Spend capability where it earns it:

| Step | Who |
|---|---|
| §3–§5 read, extract, second read | strongest model available — this is the product |
| §6 disposition against ~5 neighbours | mid-tier is plausible; small context, bounded judgment |
| §7 validate, index, ledger integrity | code, no model |

Downgrading §3–§5 reproduces the template-stamping failure the doctrine describes,
because stamping a shape is what a model does when grounding is beyond its reach.
Downgrading §7 to a model is just paying for something a script does perfectly.

## What was removed, and why

| Removed | Because |
|---|---|
| `Continue [Y/N]` phase gates and the state machine | state is files and commits now, not transcript position |
| Whole-book double-read | replaced by a per-unit second read that is affordable |
| Index patch files, subcategory/category patches | indexes are generated from frontmatter |
| Zip bundle packaging | the repo is the archive |
| Four generations of banned-template catalogues | validator rules, plus a unit size that removes the incentive |
| Same-turn bypass prohibitions | there is no turn to bypass |

---

## First run — the minimum path

The validator and index generator now exist. This retained checklist is an
illustrative minimum path; where it conflicts with sections 1-8, sections 1-8
control. The tools enforce exported-object shape and navigation, but they do not
replace source reading, visual inspection, second-read grounding, or domain
evidence checks.

Pick one book and run one source-native unit. Not a whole book.

```
1. Put the file anywhere under sources/ and record its repo-relative payload path.
2. Hash it. Check ledger/REGISTRY.md. Add a `queued` row.        (§1)
3. Create ledger/<source_id>/SOURCE.md — title, author, sha256,
   and the unit scheme you chose. Include the repo-relative `payload_path`.
4. Create ledger/<source_id>/UNITS.md — one row per chapter from
   the book's own table of contents, all `queued`.
5. Pick the chapter. Set it `in-progress`. Commit.               (§2)
6. Read it. If you cannot, mark `blocked` and stop.              (§3)
7. Extract candidates, each with a grounding note + page range.  (§4)
8. Second read of the same chapter.                              (§5)
9. library/ is empty on a first run, so every candidate is `new`
   — no retrieval step yet.                                      (§6)
10. Write the objects. Write ledger/<source_id>/units/<unit>.md
    with one row per candidate. Mark the unit `processed`.        (§7)
11. Check each object against docs/PASS_SCHEMA.md by hand,
    and say in the worklog that the check was manual.
12. Commit.
```

Then stop and look at what came out. The questions worth answering before running
a second chapter:

- Does a body section fail the master test — could it have been written without
  reading the chapter?
- Is the `Do` section saying something different from the `THEN`, or restating it?
- Do the objects read like a practitioner wrote them, or like a schema was filled?
- How long did the chapter take, and how many objects came out?

That last number is what tells you whether the unit size is right. If a chapter
produced two thin objects, the unit was probably too big to hold attention. If it
produced twenty solid ones, the size is working.

**The tier experiment:** run the same chapter twice, once with a strong model and
once with a cheap one, into scratch folders rather than `library/`. Read them side
by side. That answers the cost question with evidence in an afternoon, and it is
the cheapest experiment available.

Record the outcome in `docs/domains/corpus/worklog.md` either way — including if it
goes badly. A first run that fails is the most useful data the project can get, and
an unrecorded failure gets repeated.
