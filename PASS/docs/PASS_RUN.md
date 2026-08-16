# PASS — Run Procedure (authoring loop)

status: active
owner: docs/domains/corpus
last_reviewed: 2026-08-15

This is the operating procedure for an assistant authoring PASS cards.

Read `PASS_DOCTRINE.md` and `PASS_SCHEMA.md` first.

The whole loop is:

```text
READ SOURCE → UNDERSTAND → COMPARE AGAINST YOUR DOMAIN
           → CREATE / UPDATE CARD → VALIDATE → ADD TO THE LIBRARY
```

Nothing else is mandatory. You may keep scratch notes while you work; they are
yours, they are disposable, and nothing in PASS reads them.

---

## 0. Scope: one domain, a readable chunk at a time

You author in **one** skill domain per run — `art`, `writing`, or
`software-engineering`. You do not need to read, synchronize with, or modify any
other domain to do it. Domains meet in the library, not during authoring.

Work through a chunk of source small enough to read twice and still ground a
coherent skill: a chapter, a numbered lesson, a bounded section range. Reading
twice is the point — the second pass is what turns a summary into extraction.

The source can live anywhere the authoring environment provides it: a local
folder, a chat project's uploaded files, your own library. PASS does not care and
does not track it. If the source disappears tomorrow, the cards remain.

---

## 1. Read the source — fail closed

Read the actual material. Not the table of contents, not the chapter title, not
your prior knowledge of the subject.

If you cannot read it — file missing, extraction garbled, pages are images you
cannot inspect — **stop and say so**. Do not emit cards.

Output that looks structured and authoritative is not evidence that anything was
read. A run that skims and stamps the schema shape produces cards that are
well-formed and worthless. If you did not read it, say so.

### When you cannot see the images

For material with figures you cannot view, you may proceed — but only on evidence
you actually have, never on the absence of something you could not look at.

```
WRONG: "This chapter has no diagrams whose meaning is lost without rendering."
       (asserts absence of the thing you just said you cannot see)

RIGHT: "Cannot view figures. The extracted text for this chapter contains no
        figure captions and no in-text figure references. Proceeding on the
        prose, which read cleanly."
```

Captions and cross-references survive text extraction even when images do not, so
their absence is a checkable fact. If captions *are* present and you cannot view
them, that material is not readable — say which pages and stop.

---

## 2. Extract candidates

Work through the material like a learner. Every reusable skill becomes a
candidate pattern, drill, or AP.

For each candidate, write down — for yourself, before anything else — **what the
source specifically says, shows, warns about, or exercises.** That note is what
makes the body sections writable. If you cannot produce it, the candidate is not
extraction; drop it.

Extract generously. A dense chapter yielding fifteen candidates is normal. Do not
reduce density to save effort.

Two tests decide whether a candidate is worth keeping:

- **The master test.** Could this have been written knowing only the name, the IF
  clause, and the THEN clause, without reading the source? Then it is filler.
- **The value test.** Does it change what the model would do by default, or flag a
  trap it would otherwise fall into? Extract hardest where the source *corrects* a
  common default; lightest where it merely confirms one.

---

## 3. Second read

Re-read the same material against your candidate list. This is cheap now.

```
- recover skills the first read missed
- strengthen candidates whose grounding is thin
- split candidates that merged two distinct skills
- drop candidates that turned out to be source facts, not transferable skills
```

### Decision-versus-method check

For every candidate that may overlap an existing card, name three things:

1. the **learner decision** or outcome the source teaches;
2. the **method, policy, or constraint** the source uses to reach it;
3. the observable **tradeoff** that changes when that method is chosen.

One source excerpt may legitimately produce two candidates: it can teach a new
decision **and** supply an alternative method for an existing one. Split those
claims before placement — shared grounding does not make them duplicates.

This is a learning check, not a taxonomy exercise. Keep the alternative a
practitioner needs to recognize and choose.

---

## 4. Place each candidate against your own domain

**Never merge "the library." Merge one candidate against its neighbours.**

Duplicate guarding is **domain-local**: Art checks Art, Writing checks Writing,
Software Engineering checks Software Engineering. Do not run a cross-domain
semantic search. The one global rule is that card IDs are unique library-wide.

For each surviving candidate:

```
1. Retrieve cards in your domain that could collide:
   same topic or `library_path` prefix, the corresponding foundation or
   specialization route, overlapping tags, similar name.
   Aim for ~5. If retrieval returns 40, tighten the query.
2. Read them.
3. Decide exactly one disposition:

   new       no existing card teaches this skill    -> write a new card
   variant   same skill, different approach         -> absorb into the
                                                       foundation's variants
   replace   genuinely superior to an existing card -> supersede it
   reject    adds nothing durable                   -> drop it, write nothing
```

`variant` and `replace` are different. Different-but-valid is a variant. Better is
a replacement. "Newer" is not "better."

Do not reject a candidate merely because it shares a construct, tag, or code
listing with an existing card.

If the skill is broader than the source that taught it, store the portable version
as the foundation and keep the source-specific form as a variant beneath it. If
the rule itself needs a language, tool, framework, medium, style, genre, tradition,
method, or domain constraint, write a specialization and link it to the foundation
when one exists. Use tags to retrieve across these routes; never create a
source-named folder.

### Variants belong to their owner

A variant lives inside the card it varies. It carries no source, no locator, and
no owner in another domain, and it is executable straight from the owning card.
When a variant updates an existing card, **the finished owner file is the
canonical result.**

---

## 5. Write, validate, add

```
1. Write or update card files per PASS_SCHEMA.md
2. Run the gates:
     python PASS/tools/validate.py                    # card shape and integrity
     python PASS/tools/verify_references.py           # visual references, if any
3. Fix every failure. A failing card does not ship.
4. Regenerate navigation: `python PASS/tools/build_index.py`
5. Commit
```

Never widen the schema to accommodate a card. A card that disagrees with its
template is the card's bug.

A chunk that yielded nothing is a real result. Say so and move on.

---

## Two authoring environments, one card

PASS validates the **cards**, not the environment that produced them.

**Repo-native:**

```text
repo checkout + source material
  -> author cards -> validate -> commit
```

**Chat project:**

```text
current skill archive / relevant library files + source material
  -> author cards -> validate -> export finished files -> land in repo later
```

The resulting cards are identical in structure and validate the same way. Nothing
in the loop assumes a persistent checkout, Git write access, long-lived workspace
state, or access to any source you read earlier.

---

## Cost model

Spend capability where it earns it:

| Step | Who |
|---|---|
| §1–§3 read, extract, second read | strongest model available — this is the product |
| §4 disposition against ~5 neighbours | mid-tier is plausible; small context, bounded judgment |
| §5 validate | code, no model |

Downgrading §1–§3 reproduces the template-stamping failure the doctrine describes,
because stamping a shape is what a model does when grounding is beyond its reach.
Downgrading §5 to a model is paying for something a script does perfectly.
