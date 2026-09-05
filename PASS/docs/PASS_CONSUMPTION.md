# PASS — Consumption Contract (using the library, not just building it)

status: active
owner: docs/domains/spec
last_reviewed: 2026-09-05

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
2. **Resolve the closest applicable AP first.** Let that action protocol pull in
   the Pattern owners and variants its flow actually reaches. If no adequate AP
   exists, assemble a bounded ad-hoc Pattern chain and treat the missing
   orchestration as an AP-coverage gap rather than pretending the task already has
   a protocol. Load Drills only when practice or evaluation is actually needed.
3. **Name the known risks.** Notice the parts where the model, the medium, or the
   current task commonly fails. Do not confuse confidence with competence.
4. **Study the useful precedents.** Inspect the medium-appropriate references,
   worked examples, formats, tests, or corrections that backstop the task.
5. **Execute in protocol order.** Let the AP organize dependencies, gates,
   branches, continuity, and stopping; let Patterns govern the local decisions
   reached by that flow. Use the universal stage scaffold where the action really
   has refinement stages, not as a substitute for the AP's own control logic.
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

## Foundations first; let the action protocol own the order

A specialization still cannot safely run without the foundations it depends on,
but **foundation order and action order are different questions**. The model uses
both:

1. **Foundations before specializations.** Within a selected skillset, load and
   apply the foundation skills before their specializations. `foundation_role`,
   `foundation_object_id`, and `prerequisite_for` links encode this dependency;
   honor it.
2. **The applicable AP owns task control flow.** Its dependency order, gates,
   branches, recovery, and completion decide when each Pattern becomes actionable.
   Do not replace a debugging, revision, diagnosis, or other action with a generic
   five-stage ritual merely because all cards have `stage_binding`.
3. **Use the universal stage scaffold where refinement is genuinely part of the
   action.** `0 design → 1 skeleton → 2 block → 3 rough → 4 final` remains the
   shared vocabulary for refinement state. An AP may traverse some or all of it,
   or remain inside one stage. In Art, Direct Render keeps earlier-stage decisions
   active internally while Staged Production externalizes the approved stage flow.
4. **Visual art returns to its centerline after a produce route.** A turn routed
   as discussion or inspection does not enter production merely because art words
   are present. After a valid produce route, the activated `art` package loads
   `PAT_return_to_art_centerline` before drawing, painting, design, or rendering
   cards. The latest approved artifact and its compact freeze record are the
   controlling pair for the next registered pass; when none exists, establish
   Stage 0 when the selected Art mode requires an external staged predecessor.

The point is not to begin with "step 3." It is to make every later decision depend
on trustworthy earlier ones **without confusing one universal refinement scaffold
for every possible action protocol**.

## APs guide; Patterns check; Drills strengthen

The object types have different use-time roles:

- An **AP** organizes a complete user-level action. It owns the action's control
  flow and may delegate a genuine reusable sub-action to another AP. It should
  activate Patterns as their decision moments arrive rather than copying their
  knowledge into one giant card.
- A **Pattern** governs a local decision at the moment its IF clause becomes true.
  It is not a universal instruction merely because it was retrieved.
- A **Drill** develops or restores a weak capability. Invoke it when inspection
  reveals a recurring failure, not as decoration around finished work.

This prevents an AP from becoming a dump of every possibly related rule. The AP
establishes the **necessary chain**; the relevant local Pattern enters when the
flow reaches its decision moment. If an unordered bundle would work equally well,
the AP is not adding orchestration value.

## Taking a drill

**Administer it blind.** A drill read whole scores recognition, and returns clean
passes that mean nothing. Give the taker the card truncated at a chosen point,
have the answer written to a file, and only then reveal the rest and score against
it. Freeze the answer before anything further is opened — a hash of the file,
recorded — so the score is against what was actually produced rather than against
what got tidied once the key was visible. Keep the taker out of the library for
the duration: the owning cards hold the answers, and a search for the drill's own
name reaches them.

Where the card is cut decides what is being measured:

- **Before `## Instructions`** — the taker holds the Practice Task and Setup and
  nothing else. This measures whether the capability produces the required moves
  unprompted.
- **Before `## Success Check`** — the taker works to the Instructions but never
  sees the bullets that grade them. This measures execution against instruction,
  and lets the Success Check grade as a check the taker could not have written
  toward.

Neither cut is the correct one; they answer different questions, and a sitting
should say which it used. Have someone other than the taker score it where that is
possible, and where it is not, record that the runner and the grader were the same
reader — the result is still usable, but it is weaker evidence about the
capability than it looks.

**A described result is not a produced one.** A drill's Instructions ask the
taker to execute, observe, record, mark, or exercise something, and those verbs
are the drill. Where a bullet names one, produce what it names — compile it, run
it, mark the code, attempt the construction that should be impossible — and keep
the machine's own output as the answer. Prose asserting that the result would
have held does not satisfy the bullet.

State this to whoever takes the drill, in those words, before they start. It is
the difference between a sitting that carries out the Instructions and one that
narrates them, and the narrated sitting looks like a pass: it is fluent, it is
usually correct about what *would* happen, and it fails exactly the bullets that
asked for evidence. The Instructions already ask for the artifact; the reminder is
what gets them followed.

**Drills may be chained** — several taken at once against a single shared artifact
that must satisfy all of their Instructions simultaneously. Chaining does not
weaken the individual results, and the collisions are the point: two drills'
decisions meeting in one artifact expose constraints neither drill states, and
the second drill is what makes the first one's easy answer wrong. A drill about
copying and a drill about caching, sharing one class, yield a rule about
invalidating the cache on assignment that neither card contains. A drill taken
alone has nothing to collide with, so it cannot reach that class of finding at
all. Chain when the point is to find defects; take singly when the point is to
score one capability.

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
- **AP-first action routing.** For a productive request, resolve the closest
  applicable AP before collecting local Patterns. If none exists, make the ad-hoc
  fallback explicit to the skill's own reasoning and do not treat it as canonical
  coverage.
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
- **Produced, not described.** An Instruction bullet that asks for execution,
  observation, or a recorded rejection is answered with the machine's output, not
  with an account of it.
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
A release loader or consumer can enforce bounded retrieval, AP-first action
selection where declared, foundations-first dependency ordering, and coverage
reporting. The visual-art skill may additionally block
continuation without an approved predecessor, verified edit target, and complete
freeze record. A software skill may rely instead on compilation, tests, and code
review.

No utility can guarantee humility, good judgment, or honest inspection after a
bundle enters context. Loading a card is not applying it, and applying a card
mechanically is not understanding it. Treat any unenforced rule as a known gap,
not a solved one.
