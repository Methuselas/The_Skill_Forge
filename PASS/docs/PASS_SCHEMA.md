# PASS — Object Schema (closed contract)

status: active
owner: docs/domains/spec
last_reviewed: 2026-08-15
supersedes: PASS_v20.6_ABSOLUTE_SPEC_FLAT.md §1, §2, §5, §7

The three schemas below are closed contracts, not examples. A file containing
useful extraction that does not match its schema is salvageable material, not an
exported PASS object.

**Every rule in this file that can be checked mechanically is checked by the
validator** (`tools/validate.py`, see `docs/domains/tooling/`). Rules are written
here once so the validator has a specification; they are not enforced by asking a
model to remember them.

---

## 1. Common frontmatter

Every object begins at byte 0 with `---`. No prose, blank lines, or code fences
before it. Exactly one frontmatter block per file.

```yaml
object_id:            stable id; may be numbered or source-prefixed
object_type:          pattern | drill | ap
name:                 human-readable skill name (see §5)
library_path:         list of 2+ path segments; first is the package
stage_binding:        0 design | 1 skeleton | 2 block | 3 rough | 4 final
lane_fit:             teach | skill | both | teaching_foundation
foundation_role:      foundation | specialization
routing_class:        general | specialized | teaching
specialization_axis:  none | language | tool | framework | medium | style |
                      genre | tradition | source | method | domain
foundation_object_id: object_id | none
tags:                 list of strings
cross_links:          list of { rel, target_object_id }
reference:            map, see below
confidence:           low | medium | high
references:           list, see below (empty list valid except for visual cards)
variants:             list, see §4 (empty list valid)
```

`drill` adds exactly one key: `target_skill`.

`reference` contains exactly these keys:

```yaml
reference:
  source_id:      id of the source in the source ledger
  source_title:   title
  author:         author | Unknown
  publish_date:   date | Unknown
  media_type:     format only, one or two words
  locator:        unit + page/chapter/panel this came from
  evidence_type:  text | image | mixed
```

`references` records original teaching images for visual cards:

```yaml
references:
  - image_path: library/art/drawing/subjects/figure/hands/assets/hand_rod_ball_wedge.png
    caption: Hand masses reduced to a rod forearm, palm wedge, and finger/thumb blocks.
    derived_from: u04 p.72 figure
    origin: generated | first_party_source
    review: passed
```

### Hard rules

- **Extra keys are invalid. Missing keys are invalid. Renamed keys are invalid.**
  No `id` for `object_id`. No `type` for `object_type`. No key containing "guard".
  No custom key for domain metadata, warnings, or safety annotations. The schema
  is closed.
- `source_id` lives only inside `reference`, never at root.
- `library_path` is the single source of truth for placement. Its first segment
  is the installable package; every remaining segment is a navigation topic.
  It must have at least two non-empty lowercase segments and exactly match the
  object's directory below `library/`. `category` and `subcategory` are invalid.
- `media_type` describes format (`PDF`, `book`, `video`, `course`, `archive`,
  `image_set`), not subject matter. Subject goes in `library_path`/`tags`.
- `evidence_type` is exactly `text`, `image`, or `mixed`. No compound values.
- `lane_fit` describes teaching vs execution. It is orthogonal to domain,
  package ownership, and execution mode; it is not a stage or a role.
- `lane_fit: teach` or `both` does not by itself move an object into the
  top-level `teaching` package. Domain-specific teaching knowledge remains in
  its domain. Cross-domain instructional foundations belong under
  `library/teaching/` and continue to use `pattern`, `drill`, or `ap`.
- `routing_class: general` requires `specialization_axis: none`.
  `routing_class: specialized` requires an axis other than `none`.
- **Default to `foundation` / `general` / `none`.** Mark `specialization` only when
  the pattern's IF/THEN cannot be stated without a language-, tool-, framework-,
  medium-, style-, genre-, tradition-, method-, or domain-specific constraint.
  Context-flavoured implementation detail in `Do`/`Don't` does not make a pattern
  a specialization — the test is the rule, not the prose. See
  `docs/domains/spec/decisions.md` 2026-07-30.
- `foundation_role: specialization` with `foundation_object_id: none` is **legal**:
  the portable foundation has not been extracted yet. Genericization is deferred
  until the library holds a grounded related route to reconcile with it.
- `cross_links[].rel` is one of `foundation_of`, `variant_of`, `prerequisite_for`,
  `supports`, `related_to`, `teaches`, `skill_pair`, `teaching_foundation_for`.
- Every `target_object_id` must resolve to an object in the library. Dangling
  links fail. `cross_links: []` is always valid.
- **No unreplaced `<angle_bracket>` tokens anywhere.** `Unknown` is allowed only
  for `reference.author` and `reference.publish_date`. `provisional` is never
  valid in an exported object.
- **`locator` must name a unit the source ledger marks `processed`.** An object
  whose locator points at an unprocessed unit is a fail-closed violation, not a
  formatting problem.
- `references` is a list. Each item contains exactly `image_path`, `caption`,
  `derived_from`, `origin`, and `review`. `origin` is `generated` or
  `first_party_source`. The latter is valid only when the card's `SOURCE.md`
  declares `rights: first_party`; `reproduced` and every other value are invalid.
  `review` is `pending` or `passed`, but only `passed` ships.
- A card from a source marked `visual: true` MAY ship with `references: []` — as a
  text extraction from a visual source. A reference is included only when a
  first-party image genuinely illustrates the card's move; it is never manufactured
  to satisfy a gate. (Retired 2026-08-01: the former rule required at least one
  reference for such cards. It was dropped when generated teaching references were
  removed from the corpus — requiring a reference would have forced generated ones
  back. See `docs/domains/spec/decisions.md`.) References that ARE present are still
  fully validated by the rules below.
- Every `image_path` is repo-relative, exists, and stays under that card's own
  topic directory. Its `<image>.meta.json` sidecar records the generator model,
  generation date, source renders studied, and a completed review record.
  `tools/verify_references.py` validates the image, its review, and its
  dissimilarity from the source render before release.
- A `first_party_source` reference remains subject to claim review and provenance,
  but is intentionally exempt from the generated-image similarity failure. This
  exception applies only to source material the rights holder explicitly marks
  first-party; it never authorizes reuse from a third-party visual source.

---

## 2. Body contracts

### Pattern

```markdown
# <name, matching frontmatter exactly>

## Pattern Rule
**IF** <the specific decision moment>
**THEN** <the specific action>
**ELSE** <specific fallback — optional>

## Do
- <source-derived positive action>

## Don't
- <source-derived failure mode>

## Checklist
- <observable verification>

## Notes
<synthesized prose context>
```

### Drill

```markdown
# <name>

## Practice Task
## Target Skill
## Setup
## Instructions
## Success Check
## Common Failures
## Notes
```

`Setup` may be exactly `No special setup required.`

### AP

```markdown
# <name>

## Objective
## Steps / Flow
## Notes
```

Headings must appear in the order given, with no substitutes and no extras. Any
heading containing "Guard" is invalid as a body section. So are `## Canon`,
`## Purpose`, `## Source Evidence`, `## Validation`, `## PASS Accounting`.

---

## 3. Body quality rules

These exist because the model's cheapest way to fill a required section is to
stamp a shape. Per-unit extraction removes most of that pressure; these rules
catch the remainder.

### The master test

> Could this body section be produced knowing only the name, the IF clause, and
> the THEN clause — without having read the source?

If yes, it is filler. If it required knowing what the source specifically said,
demonstrated, warned about, or exercised, it is extraction.

### The value test — does the card change the default?

The master test asks whether a section required the source. A second test asks
whether the card is worth keeping at all: **does it change what the model would do
by default, or flag a trap it would otherwise fall into?** The model already has
broad latent capability (see `PASS_DOCTRINE.md`, "refinement, not remediation"), so
a card that only restates what it already produces reliably is a highlighted
sentence it already knew — true, but low value. Extract hardest where the source
*corrects a common default* — the `Don't` section, the failure mode, the
counterintuitive warning — and lightest where it merely *confirms* one. A good card
earns its place by shifting behavior, not by being correct.

### Each section adds new information

| Section | Must add |
|---|---|
| Pattern Rule | the situation (IF) and the action (THEN) |
| Do | implementation *how* details not in the THEN — from worked examples |
| Don't | failure modes and misconceptions — from the source's warnings |
| Checklist | verification steps — from test cases or expected outputs |
| Notes | context — motivation, prerequisites, what misconception it addresses |

A section that restates another section in different words is padding.

### Mechanically enforced (validator)

- **No THEN recycling.** The first `Do` item may not restate or paraphrase the
  THEN clause. `Notes` may not open with a restatement of it.
- **Cross-object sentence reuse.** If any `Do`, `Don't`, `Checklist`, or `Notes`
  sentence — after stripping the object name, IF clause, and THEN clause —
  appears in more than **3** objects, every object containing it fails.
- **IF uniqueness.** If the same IF clause appears in more than 3 patterns, all of
  them fail. A shared IF means it names a domain category rather than a decision
  moment.
- **ELSE uniqueness.** Same threshold. A shared ELSE is a template wrapper.
- **No duplicate items** within one object, including case-only differences.
- **Object name may not appear in body text** outside the H1. Partial fragments
  that are also domain terms (`vector`, `const`, `fond`) are fine; the ban is on
  the full name inserted as filler.
- **No raw source dumps in Notes.** OCR fragments, slide-header sequences, and
  assembled `author + locator + keywords + fragment` strings are not synthesis.

The last one has a signature worth recognizing:

```
Langtangen presents this around pp. 189-190 with operator, reading, array,
values; the nearby material shows reading array values:
```

That is mechanical assembly. A human writes: *"The source shows how const member
functions protect objects passed by const reference from accidental modification.
Without const-qualified accessors, passing by const reference would block all
member calls."*

### Source independence

An object must be usable without the original source. These phrasings are invalid
in a body: `see page`, `as shown in the diagram`, `as shown above`, `copy the
example above`, `study the figure`, `repeat the exercise from the source`, `use
the pictured pose`, `refer to the illustration`.

Reference the source for provenance. Encode the source for practice.

### Practitioner voice

Write in the working language of the craft: direct verbs (draw, block, cut, test,
refactor, season, shade, tune, measure), concrete nouns (rib cage, pointer,
invariant, pan fond, chord tone, knife edge), and checks a practitioner can run
immediately. Avoid `source-derived rationale`, `visual evidence`, `artifact
quality`, and similar scholarly filler.

---

## 4. Variants

Variants live **inside** the foundation object, not as separate files. A separate
file is allowed only when a variant is promoted to a true specialization with its
own route.

```yaml
variants:
  - variant_id: <stable id>
    variant_name: <name>
    variant_basis: method_sequence | emphasis | medium | style | source |
                   constraint | context
    source_id: <source_id>
    source_title: <title>
    locator: <unit/page>
    difference_from_foundation: <concrete difference>
    when_to_use: <when useful>
    when_not_to_use: <when poor fit>
    absorbed_from_object_id: <object_id | none>
```

If `variants` is populated, `## Notes` must describe each absorbed variant in
prose — what it changes, when to use it, its `variant_id`. Populated YAML with no
mention in Notes means invisible variants, and fails.

---

## 5. Names and filenames

`name` and the H1 are human-readable semantic skill names. `object_id` may be
encoded or numbered.

Valid names describe a craft move: `Type-Rich Interface Design`,
`Prevent Object Slicing`, `Figure Drawing Torso Mass Compression`,
`Factoring Trinomials With Non-Unit Leading Coefficient`.

Invalid: numeric or ID-like (`104`, `pattern_104`), source fragments, chapter
headings, OCR fragments, or names ending in generic filler (`… Decision Rule`)
when the rest is not a concrete move. At least two alphabetic words unless the
skill has a conventional one-word name.

Filenames carry a type prefix and a slugified semantic name:

```
PAT_<slug>.md      PAT_prevent_object_slicing.md
DRILL_<slug>.md    DRILL_replace_manual_memory_with_raii.md
AP_<slug>.md       AP_refactor_resource_owner_to_raii.md
```

Truncated sentence fragments (`PAT_cs_are_destroyed_when_a_string_is.md`) and
ID-only names (`pat_cpp_047.md`) are invalid as final filenames.

---

## 6. Placement, packages, and indexes

`library_path` in frontmatter is the single source of truth for placement. Its
first segment names the installable package; later segments form the topic path.
For example:

```yaml
library_path: [art, drawing, subjects, figure, construction]
```

belongs at:

```text
library/art/drawing/subjects/figure/construction/
```

The library tree is organized from object ownership and `library_path`. Indexes, when used, are optional generated navigation aids rather than canonical dependency state. Moving a skill means changing `library_path`, moving the file, and regenerating any derived navigation.
