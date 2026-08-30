# PASS — Object Schema (closed contract)

status: active
owner: docs/domains/spec
last_reviewed: 2026-08-18

The three schemas below are closed contracts, not examples. A file containing
useful extraction that does not match its schema is salvageable material, not an
exported PASS object.

**Every rule in this file that can be checked mechanically is checked by the
validator** (`PASS/tools/validate.py`). Rules are written here once so the
validator has a specification; they are not enforced by asking a model to
remember them.

The validator reads the library and nothing else. It never looks for a source
document, a page, a reading receipt, or any record of the session that produced
a card.

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
lane_fit:             teach | skill | both
foundation_role:      foundation | specialization
routing_class:        general | specialized | teaching
specialization_axis:  none | language | tool | framework | medium | style |
                      genre | tradition | source | method | domain
foundation_object_id: object_id | none
tags:                 list of strings
cross_links:          list of { rel, target_object_id }
reference:            map, optional attribution — see below
confidence:           low | medium | high
references:           list, see below (empty list always valid)
variants:             list, see §4 (empty list valid)
```

`drill` adds exactly one key: `target_skill`.

`reference` is **optional courtesy attribution** and holds at most these keys:

```yaml
reference:
  source_title:   title of the work the knowledge was learned from
  author:         author
```

It names a book so credit stays visible. It is not resolved, fetched, or checked
against anything, and no validator or release build reads it. A card with no
`reference` at all is fully valid.

`references` records original teaching images for visual cards:

```yaml
references:
  - image_path: library/art/subjects/figure/hands/assets/hand_rod_ball_wedge.png
    caption: Hand masses reduced to a rod forearm, palm wedge, and finger/thumb blocks.
    derived_from: what the image demonstrates
    origin: generated | first_party_source
    review: passed
```

### Hard rules

- **Extra keys are invalid. Missing keys are invalid. Renamed keys are invalid.**
  No `id` for `object_id`. No `type` for `object_type`. No key containing "guard".
  No custom key for domain metadata, warnings, or safety annotations. The schema
  is closed.
- `library_path` is the single source of truth for placement. Its first segment
  is the installable package; every remaining segment is a navigation topic.
  It must have at least two non-empty lowercase segments and exactly match the
  object's directory below `library/`. `category` and `subcategory` are invalid.
- **No card may carry source identity.** `source_id`, `locator`, page numbers,
  page ranges, source hashes, and `evidence_type` are invalid anywhere in a card —
  at root, inside `reference`, or inside a variant. A finished card must stay
  valid and executable after the work it was learned from is gone.
- `lane_fit` describes teaching vs execution. It is orthogonal to domain,
  package ownership, and execution mode; it is not a stage or a role.
- `lane_fit: teach` or `both` marks a card as instructional **within its own
  domain**. It does not route the card anywhere else and does not require any
  Teaching package to exist. (`teaching_foundation` was retired 2026-08-15 along
  with the shared Teaching lane.)
- **A card may reference other cards in its own package**, plus the shared
  `metaskills` package that every release bundles. A `cross_links` target or
  `foundation_object_id` in any other package is a domain coupling and fails.
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
  `supports`, `related_to`, `teaches`, `skill_pair`.
- Every `target_object_id` must resolve to an object in the library. Dangling
  links fail. `cross_links: []` is always valid.
- **No unreplaced `<angle_bracket>` tokens anywhere.** `provisional` is never
  valid in an exported object.
- `references` is a list. Each item contains exactly `image_path`, `caption`,
  `derived_from`, `origin`, and `review`. `origin` is `generated` or
  `first_party_source`; `reproduced` and every other value are invalid.
  `review` is `pending` or `passed`, but only `passed` ships.
- Any card MAY ship with `references: []`. An image is included only when it
  genuinely illustrates the card's move; it is never manufactured to satisfy a
  gate. References that ARE present are fully validated by the rules below.
- Every `image_path` is repo-relative, exists, and stays under that card's own
  topic directory. Its `<image>.meta.json` sidecar records the generator model,
  generation date, and a completed review record. `tools/verify_references.py`
  checks that the image exists and carries a passed review before release.

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

`Success Check` is a closed list of conditions a reader other than the runner can
check after the fact. The section as a whole has to be able to fail; one that any
completed attempt satisfies is the bug rather than the drill. Three requirements
make it able to fail:

- **The property under test may not serve as its own evidence.** Where a drill
  turns on a test that would fail, an interference that would occur, or a change
  that would leave something intact, the check requires that it was run, produced,
  or applied. A prediction recorded in place of an observation reads as complete
  and establishes nothing.
- **At least one bullet excludes a named plausible near-miss** that would otherwise
  satisfy the section. The working form is to state the cheap answer and say what
  it demonstrates, rather than to describe the correct answer more emphatically.
- **Where the drill ends in a choice, the check asks for the reason rather than
  the selection**, so the run produces a defensible decision instead of a
  preference.

A bullet requiring an output the work alone does not produce satisfies the second
requirement by a different mechanism — a name that would have been accepted had it
been read in place, a model not previously made explicit, a rejected candidate with
the observation that disqualified it. These resist fabrication because performing
the exercise does not hand them over.

Length is not the contract and is a poor proxy for it. A compressed check can
discriminate better than a long one, and padding a section that already
discriminates dilutes the bullets doing the work. Register belongs to the package:
a procedural lane and a critical lane phrase the same requirement differently and
both are correct.

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

The three headings are deliberately broad; AP control-flow semantics live inside
them rather than by widening the schema:

- `Objective` names the complete user-level action and the result that counts as
  success.
- `Steps / Flow` owns orchestration. It must make the entry state clear, order
  dependent decisions, activate or point to the relevant Pattern owners, preserve
  important invariants, state advance gates, include branches/recovery when the
  action can fail in materially different ways, and end in a completion check.
  These may be bold labels, list items, or prose inside the section; they are not
  extra H2 headings.
- `Notes` explains scope, tradeoffs, and bounded exceptions. It must not duplicate
  the full rules of the Patterns the AP coordinates.

An AP may call subordinate APs where a genuine reusable sub-action already has an
owner. It must not create a second dependency mechanism: use `foundation_object_id`
and `cross_links` for real object relationships.

For an AP, `stage_binding` indicates the stage where the protocol is normally
entered or primarily operates. The AP may traverse later or earlier stages when
its action genuinely requires that flow.

### AP value test

> If the same set of Patterns were handed to the model as an unordered bag, would
> the action still be performed just as reliably?

If yes, the AP adds no orchestration value. If ordering, gating, branching,
continuity, or stopping materially changes reliability, the AP earns its place.

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

Encode the source for practice. The finished card is the durable artifact; the
work it came from is not a runtime dependency.

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
own route. A variant belongs to its owner card and is executable from it: it
carries no source, no locator, and no owner in another domain.

```yaml
variants:
  - variant_id: <stable id>
    variant_name: <name>
    variant_basis: method_sequence | emphasis | medium | style | source |
                   constraint | context
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
library/art/subjects/figure/construction/
```

The library tree is organized from object ownership and `library_path`. Indexes, when used, are optional generated navigation aids rather than canonical dependency state. Moving a skill means changing `library_path`, moving the file, and regenerating any derived navigation.
