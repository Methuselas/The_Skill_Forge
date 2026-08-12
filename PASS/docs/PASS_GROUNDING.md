# PASS — Grounding Verification (the anti-skim gate)

status: active
owner: docs/domains/tooling
last_reviewed: 2026-07-31

Read this with `PASS_RUN.md`. It closes the one hole `tools/validate.py` cannot:
validate.py proves a card is well-*formed*; it cannot prove the source was
*read*. This gate does.

---

## The failure it prevents

The 2026-03-04 incident and the 2026-07 art runs share one shape: a run that did
not actually read the source still produced structured, authoritative-looking
cards, with locators pointing at a unit it merely *declared* `processed`.
Shape validation passed. The output was ungrounded.

Telling a model "don't skim" does not work — it rationalizes past the rule, the
same way it invents a new template as soon as the old one is banned. The doctrine
already learned this: **prohibitions are enforced by a validator, not by asking a
model to remember them.** Grounding is now enforced the same way.

## The rule

**Every `processed` unit must carry a `## Reading receipt` block in its
`ledger/<source_id>/units/<unit_id>.md`, and `tools/verify_grounding.py` must pass
for the source before the unit's objects ship.**

A receipt is verbatim evidence, re-checked against the real payload:

```markdown
## Reading receipt

| page | evidence |
|---|---|
| 5  | "Good code is obviously not the only ingredient that goes into making good software" |
| 12 | "We'll start with a high-level description of each pillar" |
| 21 | "by the end of this book we will only have scratched the surface of what there is to know about software testing" |
```

- **Pages** are the source's own printed page numbers (the same space object
  locators use). `SOURCE.md` carries `pdf_page_offset:` so the tool can convert to
  physical PDF pages for extraction. Constant offset only; if a source has none,
  set the offset so receipt pages are physical pages.
- **Text pages** cite a verbatim quote of at least 6 words. The tool re-extracts
  that exact page and confirms the quote is present (whitespace/punctuation
  normalized, but no fuzzy matching). You cannot fabricate a quote from a page you
  never extracted.
- **Image-only pages** (figure-drawing plates, scanned diagrams) have no text to
  quote. Cite a render or a source-provided page image, and the tool confirms the
  image exists and decodes:

  ```markdown
  | 45 | render: tmp/render/gcbc/p45.png | observed: rib-cage barrel tilts back over the pelvic wedge |
  | 46 | image: sources/Art/book-pages.zip::pages/page_046.jpg | observed: the gesture line precedes mass blocking |
  ```

  This forces the page-image step a skim skips. The tool cannot judge the
  `observed:` note, but it can prove a decodable image was available; the note is
  for human review.

## Visual sources — captions are not the figures

Mark a source `visual: true` in `SOURCE.md` when its skills live in the images
(figure drawing, anatomy, diagrams, worked plates). A visual source has text too —
captions, instruction paragraphs — and a skim can quote *those* while never
looking at a single drawing. That is exactly how the art runs faked their cards.

So for a `visual: true` source, quotes do not count toward coverage: each
processed unit must carry verified **page-image rows** (`render:` for generated
renders or `image:` for source-provided page images), enough to cover the unit
and spread across it. You cannot mark a figure-drawing chapter `processed` by
quoting captions.

This requires a vision-capable model plus either a working PDF rasterizer
(`pdftoppm` / Poppler) or a preflighted page-image directory or ZIP whose page
mapping was visually confirmed. A direct `image:` locator is repo-relative. A ZIP
locator uses `archive.zip::exact/member/path.jpg`; spaces are allowed. If neither
page path is available, a visual source cannot be grounded — which is the
correct outcome, not a reason to fall back to captions.

## Shipped visual references

Grounding renders are evidence, not deliverables. A visual card instead ships an
original teaching image through its `references:` frontmatter. Generate it from
the card's construction instruction while studying the source page image;
never crop, trace, or lightly edit the source plate. `tools/generate_reference.py`
writes the image provenance sidecar, and `tools/verify_references.py` is the
release gate: it requires a recorded claim review and rejects an image too
similar to any source render. See `PASS_SCHEMA.md` §1 for the closed field shape.

### First-party visual sources

When the source rights holder explicitly records `rights: first_party` in
`SOURCE.md`, a card may instead ship a reviewed source image as
`origin: first_party_source`. Its sidecar must record that provenance and the
review gate confirms the rights declaration before allowing the similarity that
would otherwise fail. This exception is authorization-specific; never infer it
from a file's location or an assistant's past involvement.

## Coverage — you must read the whole unit

The tool rejects receipts that cluster on the opening pages:

- at least `ceil(page_span / 8)` rows (floor of 2), and
- the cited pages must span at least half the unit's page range.

So a 20-page chapter needs 3+ quotes spread across ≥10 of its pages. Quoting only
page 1 fails — that is what reading the first paragraph and extrapolating looks
like.

## Where it runs in the procedure

`PASS_RUN.md` §3 (read) and §7 (write/validate/commit) now require:

1. When you read the unit, collect the receipt quotes *as you go*. This is nearly
   free for an honest run — you already have the extracted text open.
2. Write the `## Reading receipt` block into the unit ledger before writing
   objects.
3. In §7, run **all three** gates and fix every failure before committing:

   ```bash
   python tools/validate.py                              # card shape
   python tools/verify_grounding.py --source <source_id> # actually read
   python tools/verify_references.py                     # visual references, if any
   ```

A unit whose receipt does not verify is not `processed`. Its objects do not ship.

## Ceiling — what this does and does not prove

Be honest about the boundary:

- It **does** make the cheap cheat — skim, then fabricate grounded-looking cards —
  mechanically fail. That is the cheat that has actually bitten, twice.
- It **does not** prove comprehension, good judgment, or that the *right* skills
  were extracted. A run could quote real pages and still write weak cards. Those
  failures are caught by the second read, disposition review, and card-quality
  rules, not by this gate.
- For image sources it proves a decodable page image was available, not that the
  figure was understood. Visual grounding still needs the domain-evidence check in
  `PASS_RUN.md` §3.

The gate raises the floor from "output that looks grounded" to "output backed by
verified source evidence." It is a necessary condition for shipping, not a
sufficient one for quality.
