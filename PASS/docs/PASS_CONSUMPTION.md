# PASS — Consumption Contract (using the library, not just building it)

status: active
owner: docs/domains/spec
last_reviewed: 2026-08-04

Everything else in PASS governs **extraction** — how a source becomes grounded
skill objects. This governs **use**: how a focused domain skill draws on those
objects. The two are separate contracts with separate failure modes. Extraction
fails by fabricating. Consumption fails either by ignoring the library and
improvising from priors, or by letting retrieved notes control decisions they were
never meant to govern.

The host first selects a focused `SKILL.md`, such as `visual-art` or
`software-engineering`. That skill loads its category master index, then retrieves
a bounded set of PASS objects. There is no universal consumer skill and no domain
routing hidden inside PASS itself.

A domain may add its own execution checks: the visual-art skill, for example, owns intent
routing, stage authorization, freeze records, and post-artifact inspection. Those
rules do not apply to software engineering or PASS authoring.

Retrieval is evidence of consultation, not proof of correct execution. A loaded
card still must be evaluated against its `IF` clause and applied only at the
learner decision and stage it governs.

---

## The scoped golden-truth rule

**On any non-trivial task, check the library for a matching skillset before doing
the work. An applicable grounded skill is authoritative for the craft decision it
actually covers. It does not replace the user's intent, active project rules,
subject knowledge, invention, or judgment outside its IF clause.**

This scope is the balance:

1. The user's request and active project constraints define the job.
2. A matching grounded card governs the learner decision named by its IF/THEN.
3. The model's prior supplies recognition, invention, analogy, adaptation, and
   reasonable action where the library is silent.
4. Retrieval is not permission to apply a card outside its decision moment.

A matching card may not be silently ignored merely because the model's default
answer feels easier. Equally, a card may not be stretched into total authority
merely because it is present in context. The selected domain skill protects the centerline of execution; it does not replace the performer.

If no skill matches, say so and fall back to your own reasoning. A silent fallback
that *looks* like it used a skill is the consumption version of a skim.

## Treat the task as a practical exam

Before acting, perform a bounded study pass:

1. **Restate the craft problem.** Identify the actual decision, artifact, and
   required result rather than matching the whole prompt verbatim.
2. **Retrieve the relevant APs, Patterns, and Drills.** Load foundations first and
   keep the bundle small enough to use deliberately.
3. **Name the known risks.** Notice the parts where the model, the medium, or the
   current task commonly fails. Do not confuse confidence with competence.
4. **Study the useful precedents.** Inspect the medium-appropriate references,
   worked examples, formats, tests, or corrections that backstop the task.
5. **Execute in stage order.** Let APs organize the work, Patterns guide local
   decisions, and Drills repair weak execution.
6. **Inspect before repeating.** Diagnose the visible or testable failure, preserve
   what worked, and make the next attempt answer that diagnosis rather than simply
   generating another variation.

This preflight is not ceremony. It is how prior practice becomes available before
an expensive attempt instead of after several preventable failures.

## Select by task — load the relevant subset, not the library

You do not use every skill for every job. Debugging work does not pull
random-number-generation skills; inking a comic panel does not pull every art
card; revising dialogue does not load every writing source. Match the task to a
package and topic path (and tags), retrieve that skillset, and load only it.

Retrieval is bounded, the same way extraction's placement step is: pull the
handful of skills whose IF clauses plausibly match the situation, not everything
under a package. Loading too much is both wasteful and a way to let irrelevant
notes crowd out judgment.

## Foundations first, in stage order — never start at step 3

A person drawing a figure does not begin at step 3. They thumbnail the intent,
lay a skeleton, block it with simple solids, tighten, then finalize. A person
writing code does not begin at the special case. The model works the same way:

1. **Foundations before specializations.** Within a selected skillset, load and
   apply the foundation skills before their specializations. `foundation_role`,
   `foundation_object_id`, and `prerequisite_for` links encode this order; honor
   it. A specialization applied without its foundation is a step-3 start.
2. **The universal stage scaffold is the spine.** Run work through
   `0 design → 1 skeleton → 2 block → 3 rough → 4 final` (the mandatory
   `metaskills/iterative-construction` AP). Each skill's `stage_binding` says where
   it belongs in that arc; apply it at its stage, not before.
3. **Visual art returns to its centerline after a produce route.** A turn routed
   as discussion or inspection does not enter production merely because art words
   are present. After a valid produce route, the activated `art` package loads
   `PAT_return_to_art_centerline` before drawing, painting, design, or rendering
   cards. The latest approved artifact and its compact freeze
   record are the controlling pair for the next registered pass; when none exists,
   establish Stage 0.

Starting from foundations in stage order stops the model from producing
confident, detailed output that is structurally wrong — the code equivalent of a
beautifully rendered hand with six fingers.

## APs guide; Patterns check; Drills strengthen

The object types have different use-time roles:

- An **AP** organizes a repeatable section or workflow. A top-level AP may delegate
  to subordinate APs when the task has distinct construction problems.
- A **Pattern** governs a local decision at the moment its IF clause becomes true.
  It is not a universal instruction merely because it was retrieved.
- A **Drill** develops or restores a weak capability. Invoke it when inspection
  reveals a recurring failure, not as decoration around finished work.

This prevents a universal AP from becoming a chain of every possibly related
rule. The AP establishes order; the relevant local skill enters when the work
reaches it.

## References and examples follow the medium

Study the kind of precedent that actually helps the current craft:

- **Visual art:** staged drawings, construction studies, and spatial diagrams
  embedded in real drawings. When a visual card carries a reviewed first-party
  image, work against it rather than the text alone. A card may still ship with
  `references: []`; then the text is useful guidance, but producing the visual
  result still requires an image-capable model.
- **Software:** working implementations, interface shapes, tests, failure cases,
  and before/after designs. Use them to verify behavior and architecture, not to
  copy a solution whose constraints do not match.
- **Writing:** dialogue formats, scene structures, voice samples, revision pairs,
  and before/after edits. Use them to recover form and judgment without flattening
  the new work into imitation.
- **Teaching:** demonstrations, exercise sequences, model answers, and assessment
  examples that show what progression and success look like.

A reference is a backstop, not a command. It can show stage density, continuity,
format, or a successful decision while leaving the current subject and expression
to the model and user.

## Do not turn a limitation into an escape route

Known weaknesses require support, practice, and inspection. They do not justify
silently avoiding a required part of the task.

Examples include cropping or obscuring difficult hands and feet without a
compositional reason, omitting tests around fragile code, avoiding dialogue in a
scene that depends on it, or simplifying away a requirement merely because it is
hard. A legitimate design choice is allowed; repeated convenience that evades the
stated task is a failure signal.

When a required part remains unresolved, either solve it through the relevant
skill route or report the limitation honestly. Do not hide it with polish.

## Use-time guardrails

Consumption needs its own gate, parallel to the fail-closed reading rule that
governs extraction (`PASS_RUN.md` §2.1):

- **Intent before execution.** Route the current turn as discuss, inspect,
  produce, or ambiguous before a craft pipeline. Only produce may enter visual
  generation, and a persistent no-image lock still wins.
- **Prerequisite enforcement.** A specialization does not load until its
  foundation is loaded.
- **IF-match.** Apply a skill only when its IF clause actually matches the
  situation, not because it was retrieved.
- **Scoped authority.** A card governs its learner decision, not the whole task.
- **Confidence surfaced.** A `low`/`medium`-confidence skill is applied as such,
  not trusted like a `high` one.
- **Self-contained application.** A card carries everything needed to apply it.
  If applying it would require consulting a source document, the card is
  incomplete — fix the card rather than reaching for the book.
- **Reference-aware loading.** Surface useful reviewed references when present;
  surface their absence for visual execution rather than pretending text alone is
  equivalent.
- **Avoidance check.** Before finalizing, verify that difficult required elements
  were not silently cropped, omitted, hidden, or simplified away.
- **Diagnosis-led revision.** Preserve successful structure and revise the named
  failure instead of regenerating the whole artifact without a reason. For staged
  visual work, route the failure to the first stage where that property became
  decidable, re-ratify it there, and propagate forward.
- **Two-carrier continuity.** Pass the exact image for geometry and the compact
  freeze record for commitments. Do not require a later model to infer count,
  attachment, occlusion, or intent from pixels alone.
- **Post-artifact parentage.** Authorization is not proof that the image tool used
  the supplied parent. Record the actual parent and operation mode, then inspect
  every inherited freeze before claiming continuity.

## Ceiling — enforce what can be enforced

Every rule here is one a model can rationalize past, exactly like "don't skim."
Durable checks should therefore be implemented by the domain that needs them.
A release loader or consumer can enforce bounded retrieval, foundations-first ordering, and coverage reporting. The visual-art skill may additionally block
continuation without an approved predecessor, verified edit target, and complete
freeze record. A software skill may rely instead on compilation, tests, and code
review.

No utility can guarantee humility, good judgment, or honest inspection after a
bundle enters context. Loading a card is not applying it, and applying a card
mechanically is not understanding it. Treat any unenforced rule as a known gap,
not a solved one.
