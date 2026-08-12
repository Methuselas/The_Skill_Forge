# PASS — Doctrine

status: active
owner: docs/domains/spec
last_reviewed: 2026-08-02
supersedes: PASS_v20.6_ABSOLUTE_SPEC_FLAT.md (doctrine portion)

Read this before running PASS. It is short on purpose. The enforceable rules live
in `PASS_SCHEMA.md` and in the validator; this file is the part a human needs to
understand.

---

## What PASS is

PASS converts source material into reusable skill objects.

When a person wants to learn a craft, they read a book. They don't skim it and
they don't summarize it. They absorb every usable technique, rule of thumb,
shortcut, warning, and exercise, and turn it into something they can *do*.

PASS makes a model do the same thing. Given source material a human would learn
from, extract every piece of knowledge that enhances a skillset. The domain does
not matter — programming, cooking, drawing, writing, music, mathematics, game
design. When you find something usable, extract it. What you end up with is a
library of reusable skills that make you better at the craft, not merely informed
about it.

**Read like a learner, extract like a craftsman, store like a library.**

PASS is not summarization. It is not note-taking. It is not a book report. It is
not an inventory of what the source contains.

## Why a library — refinement, not remediation

The model already has broad latent capability; it can usually do the thing. What
it lacks is *reliable retrieval of the right move at the right moment*. That is the
difference between a student who could pass and one who studied: same underlying
ability, but the second took notes, highlighted the traps, and drilled until the
correct technique surfaces consistently under pressure.

A skill card is that study note. It says **when** to reach for a skill (the IF),
**why** it works (the Notes), and **how** to execute it (the Do and Checklist); a
drill is the practice rep that turns recognition into reflex. The library exists to
make an existing capability *dependable*, not to teach from zero. This is
refinement.

## Balance: assistance, not replacement

The PASS runtime is external practice memory. It preserves the notes, examples,
corrections, and exercises that a practitioner would otherwise have to remember
perfectly after every interruption. Before a non-trivial task, the model studies
the relevant part of that cabinet the way a person reviews notes before a
practical exam.

The library does **not** replace the model's broad capability. The model still
supplies recognition, invention, subject knowledge, analogy, and adaptation to
the present request. the selected domain skill protects the centerline of execution: it recalls
the grounded procedure, known traps, stage boundaries, and checks that keep that
capability from drifting into a familiar failure.

Authority is therefore scoped:

- the user's intent and active project constraints define the job;
- an applicable grounded skill governs the craft decision it actually covers;
- the model's prior supplies context, invention, and reasonable action where the
  library is silent;
- a card does not control decisions outside its IF clause merely because it was
  retrieved.

Both extremes are failures. Ignoring the library repeats preventable mistakes.
Letting the library dominate every decision turns a support structure into a cage.
A successful use combines disciplined recall with flexible judgment.

Humility is part of the method. A fluent result is not proof that the work is
correct. Known weaknesses are reasons to prepare, inspect, and practise—not
reasons to crop, omit, hide, or otherwise route around a required part of the
work. When an attempt fails, diagnose the failure, preserve what worked, and use
the relevant Pattern, AP, or Drill to improve the next attempt.

## References and examples follow the medium

A useful library keeps the kind of precedent that helps the craft being performed:

- visual art benefits from staged drawings and spatial construction studies that
  are themselves real drawings, not merely labeled infographics;
- software work benefits from working implementations, interface examples, tests,
  failure cases, and before/after designs;
- writing benefits from dialogue formats, structural samples, revision pairs, and
  examples of voice or pacing in use;
- teaching benefits from demonstrations, exercise progressions, and assessment
  examples.

These are study aids, not templates to copy. Retrieve a small, relevant set,
observe what it proves, then adapt the lesson to the current task. The purpose is
to reduce blind retries by making prior successful practice available before the
next attempt.

It is also why grounding is non-negotiable. A wrong note is worse than no note: a
student who highlighted the wrong sentence confidently writes the wrong answer,
because they "studied it." Ungrounded cards do not merely fail to help — they make
the model more wrong while feeling more sure. That is precisely the failure the
fail-closed rule and the grounding gate (`PASS_GROUNDING.md`) exist to prevent, and
why a skim is not a shortcut but active damage.

## The three object types

Everything extracted becomes exactly one of three things. There is no fourth type.
Inventing one is not creativity; it is failure.

**Pattern** — a decision rule. IF this situation, THEN this action, ELSE this
fallback, with source-derived DOs and DON'Ts. The reusable craft knowledge that
improves the work every time it is applied.

**Drill** — a short repeatable training exercise. What you do to practise, or
assign when teaching someone.

**AP (Action Protocol)** — a repeatable staged workflow that produces work at
defined levels of refinement.

Material that does not fit is transformed into one of the three, attached inside
an existing object's notes or variants, recorded as context in the ledger, or
rejected.

## The stage scaffold

APs and every object's `stage_binding` use one scaffold, unchanged across domains:

| Stage | Meaning |
|---|---|
| `0 design` | The seed. A design doc, a one-line app idea, a paragraph character description, a list of ingredients. |
| `1 skeleton` | Barest viable start. Stick figure with ovals. Function signature, empty body. Mise en place. |
| `2 block` | Solid shapes. Limbs as cylinders. You can tell what it is. |
| `3 rough` | Definition visible but unclean. Compiles but needs refactoring. Plated, not garnished. |
| `4 final` | Keep what works, cut what doesn't. Clean, tested, weighted, finished. |

## Teaching is a route, not a type

A source sometimes teaches you *how to teach* something — a good explanation, a
clever progression, an effective exercise order. That is worth keeping, but it is
still a pattern, drill, or AP. It carries `lane_fit: teach` or
`teaching_foundation` and `routing_class: teaching`. It never becomes its own
object type.

## What happens between extractions

**Variants.** Two patterns teaching the same skill different ways are not
duplicates. Keep both inside one object — different situations call for different
approaches.

**Sources are evidence, not exclusive authority.** A source demonstrates one
grounded route through a craft problem; it does not prove that route is the only
sound one. When another source reaches the same learner decision, seek the
different method, sequence, constraint, or tradeoff it contributes. Preserve a
grounded alternative when it changes a practitioner's choice. Do not invent an
alternative that no source supports.

**Replacement.** A genuinely superior pattern replaces an inferior one. Not
merely different — better.

**Genericization.** A skill learned from a narrow source that applies broadly gets
the source-specific detail stripped and stored as the foundation, with the narrow
version kept as a variant beneath it. A C++ design pattern that works in Java. A
French knife technique that works in Japanese cuisine.

## One relationship model across every skill family

Packages may contain different crafts: writing is not drawing, and drawing is
not software development. Their internal knowledge relationships are still the
same:

- A **foundation** states the portable learner decision for a topic.
- A **variant** stays inside that foundation when the decision is the same but a
  source supplies a different method, sequence, emphasis, or tradeoff.
- A **specialization** becomes its own object when the IF/THEN itself requires a
  language, tool, framework, medium, style, genre, tradition, method, or domain
  constraint. It links back to its foundation when one exists.
- **Tags** are the cross-cutting retrieval keys: they name contexts such as
  `python`, `manga`, `life_drawing`, `robot_design`, `tank`, `resume_writing`,
  and `technical_writing`. Tags connect related routes even when navigation paths
  differ.

The folder tree is navigation, not a second ontology. A package may expose
readable lanes such as `foundations`, `languages`, `media`, `styles`, or
`domains` when they help a learner browse a large skill family. Those lanes
never replace the foundation/variant/specialization relationship in frontmatter,
and they are never source or book buckets.

For example, a shared vehicle-construction foundation can serve cars and tanks;
a tank card is a specialization when its rule needs tracks, a turret, armour
layers, or terrain use. Likewise, figure construction can be shared by comics,
manga, life drawing, and mechanical figures, while the context-specific method
or constraint determines whether it is a variant or specialization. The same
test applies to resume writing and technical writing, or to Python and another
language.

**Merging.** Running PASS on a new source merges into the existing library.
Variants attach, superior patterns replace, duplicates are dropped, indexes
rebuild. The library improves with every source.

## The contract

- Learn from the source like a human learner.
- Extract reusable skill objects only. Never summarize the source.
- Every extraction is a pattern, drill, or AP.
- Preserve variants. Replace inferior with superior. Genericize what travels.
- Treat each source as one route worth learning, never as proof that its route is
  the only one.
- Every object must be usable **without** the original source in hand.
- Favor thoroughness. Extract more, not less. Do not quietly reduce density.
- **Fail closed.** If the source cannot actually be read, stop and say so. Never
  emit objects that look grounded but are not.

That last rule is the one that has actually bitten. On 2026-03-04 a run produced
structured, authoritative-looking output for a book it had not read, and kept
going after its inputs had expired. Structured output is not evidence of
grounding. An object whose locator cannot be checked against a processed unit is
not an object.

## Why the process is per-unit

The old spec grew to 4,644 lines, most of it prohibitions against template-
stamping: banned Do sentences, banned ELSE clauses, IF-uniqueness rules,
anti-recycling rules, four documented generations of the model inventing a new
wrapper as soon as the old one was banned.

The cause was never insufficient prohibition. It was pressure. Asking for the
whole book at once means grounding each object is expensive and stamping a shape
is cheap, so shapes win. Ban the shapes and new shapes appear.

PASS now processes **one unit at a time** — normally a chapter. A unit fits in
context with room left to think, which makes real grounding the cheap path. The
prohibitions that remain are enforced by a validator instead of by asking a model
to remember them.

If you find yourself wanting to add a new banned-template rule, first check
whether the unit was too large.

## Ownership boundary

PASS owns extraction and conceptual placement. Anything downstream consumes
placed objects; it does not relocate them or redefine where they belong.

Placement is `library_path` in the object's own frontmatter. Its first segment
is the installable package; later segments are the topic path. The folder tree
and every index are **generated** from that. Focused domain skills load their own
category indexes and package-declared bootstraps. Moving a skill means editing its
path list, never hand-editing an index.
