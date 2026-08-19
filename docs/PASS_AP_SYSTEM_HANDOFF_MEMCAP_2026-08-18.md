# PASS — ACTION PROTOCOL SYSTEM HANDOFF MEMCAP
**Date:** 2026-08-18  
**Scope:** Global PASS architecture / runtime / authoring doctrine  
**Purpose:** Preserve the clarified role of Action Protocols (APs) so future repo work does not regress to Pattern-first orchestration.

---

# WHY THE AP SYSTEM WAS CORRECTED

A runtime landscape test exposed a structural problem in PASS.

The Art library already contained strong Patterns for:

- composition;
- value grouping;
- lighting;
- color;
- atmospheric depth;
- materials;
- edges;
- painterly mark decisions.

The generated landscape nevertheless skipped important intermediate structural work. The mountain had a strong silhouette and broad light/shadow organization, but weak meso-scale terrain structure and overly flat warm/cool color families.

The important diagnosis was:

**the knowledge largely existed, but it was not being ordered, gated, and verified as one complete action.**

This exposed a teaching/architecture deficiency around Action Protocols.

The old practical interpretation had drifted toward:

> AP = another kind of staged knowledge object.

The corrected interpretation is:

> **AP = the model applying accepted Patterns, in a deliberate control flow, to accomplish a complete action.**

That distinction is now canonical PASS doctrine.

---

# CANONICAL THREE-OBJECT MODEL

PASS still has exactly three canonical object types.

## Pattern

A **Pattern** owns a reusable decision primitive.

Conceptually:

> IF this situation is present, THEN make this decision / take this local action, ELSE use the fallback.

Patterns own craft knowledge.

Examples:

- how to choose edge hardness;
- how to preserve value structure while changing color;
- how to diagnose a contract mismatch;
- how to choose a viewpoint;
- how to isolate a defect hypothesis.

A Pattern is not responsible for coordinating an entire user-level action.

## Drill

A **Drill** owns repeatable practice or evaluation.

It exists to make one or more capabilities more reliable through:

- deliberate repetition;
- comparison;
- testing;
- constrained studies;
- diagnostic reps.

Drills are the training/evaluation layer.

## AP — Action Protocol

An **AP** is a goal-directed application of accepted Patterns that accomplishes a complete action.

An AP owns **control flow**, including:

- entry state;
- intended result;
- dependency order;
- invariants that must remain true;
- gates that permit or block progress;
- branches;
- recovery routes;
- continuity across stages;
- completion / stopping conditions.

An AP does **not** become a second owner of the Pattern knowledge it coordinates.

The compact architecture is:

```text
Pattern  -> what decision to make
AP       -> how to apply decisions together to complete an action
Drill    -> how to practise or evaluate those capabilities
```

---

# ACTION-FIRST RUNTIME RETRIEVAL

For a productive user request, the normal semantic retrieval order is now:

```text
requested action
      ↓
closest applicable AP
      ↓
required Pattern owners
      ↓
applicable variants
```

Example:

```text
paint a landscape
      ↓
landscape-painting AP
      ↓
composition / form / value / color / atmosphere / material / edge Patterns
      ↓
medium- or subject-specific variants
```

The AP controls **when** a Pattern becomes actionable.

Patterns still control the actual local decision.

Drills are loaded only when practice, calibration, recovery, or evaluation is needed.

---

# WHEN NO AP EXISTS

The runtime is still allowed to act.

If there is no suitable AP:

1. assemble a bounded ad-hoc chain of relevant Patterns;
2. complete the action as well as possible;
3. recognize internally that this is an **AP coverage gap**.

An ad-hoc Pattern bundle is not proof that the skillset already has adequate procedural coverage.

Repeated or consequential ad-hoc chains are candidates for AP synthesis.

Do **not** invent a new workflow registry, AP database, or fourth PASS object type. The existing library relationships remain the dependency system.

---

# AP SYNTHESIS IS A SEPARATE AUTHORING MOVE

Normal source ingestion naturally produces many Patterns because books and sources frequently teach local decisions one at a time.

PASS must therefore **not wait for one source to explicitly teach every useful AP**.

An AP may be synthesized from already accepted canonical Patterns after the original sources are gone.

That remains source-grounded because:

- the AP may only orchestrate accepted canon;
- it does not invent missing craft knowledge;
- it remains source-independent like other finished PASS cards.

## Trigger an AP synthesis audit when:

- a book or subcategory closes and the accepted library now supports a recurring user-level action;
- repeated work keeps assembling the same ad-hoc Pattern chain;
- an execution test shows that the necessary Pattern knowledge existed but was omitted, mistimed, or destroyed by later work;
- an existing AP no longer coordinates the strongest current owners.

## AP synthesis procedure

1. **Name the action and result.**  
   Use a real user-level verb:
   - paint the landscape;
   - revise the essay;
   - debug the service;
   - construct the cast shadow.

2. **Check for an existing AP.**  
   Refine the existing owner when it already owns the action.

3. **Retrieve the Pattern owners.**  
   Keep each reusable decision in its Pattern.

4. **Order by dependency, not source order.**  
   Ask what must become trustworthy before later decisions can safely depend on it.

5. **Add invariants and gates.**  
   Define what must survive and what evidence permits progress.

6. **Add branches and recovery routes.**  
   Route failure back to the Pattern that owns the decision instead of allowing damage to propagate.

7. **Define completion.**  
   State what verification or stopping condition makes the action complete.

8. **Use only real existing dependencies.**  
   Do not create a parallel AP dependency framework.

9. **Present the AP delta for approval** like any other canonical PASS mutation.

Practice history may reveal that orchestration is missing, but one failed or successful attempt must not be copied literally into canon. The resulting AP must generalize.

---

# AP QUALITY TEST

An AP should add real ordering value.

A useful AP should answer questions such as:

- What has to happen first?
- What cannot safely happen yet?
- What must remain intact while later work is added?
- What condition means the current phase is trustworthy?
- If this check fails, where do we return?
- Which Pattern owns that correction?
- When is the action actually finished?

If an unordered list of the same Patterns would work just as well, the AP probably is not adding enough orchestration value.

APs should not become giant restatements of every linked Pattern.

---

# RELATIONSHIP TO THE UNIVERSAL STAGE SCAFFOLD

The universal stage vocabulary remains:

```text
0 design
1 skeleton
2 block
3 rough
4 final
```

This scaffold is **not** the universal control flow for every action.

The corrected rule is:

> **The applicable AP owns task control flow.**

`stage_binding` remains useful for describing where an object normally enters or operates, but a debugging AP, revision AP, diagnosis AP, or research AP should not be forced through an artificial `0 → 4` ritual.

An AP may:

- stay inside one stage;
- cross several stages;
- use all five;
- use none of them as explicit user-visible phases.

For Art, the existing staged production system remains frozen unless the user explicitly opens that work. The AP correction does not rename, merge, or rewrite the Art Stages.

---

# FAILURE ATTRIBUTION — DO THIS BEFORE WRITING NEW CARDS

A bad result does not automatically mean the Pattern library lacks knowledge.

Use this taxonomy:

```text
knowledge       the skillset lacks the decision principle
orchestration   the principles exist, but no adequate AP orders/gates them
retrieval       the correct canon exists but was not brought into the attempt
application     the correct canon was retrieved but executed incorrectly
continuity      a later step destroyed an earlier correct decision
reference       the source/reference was insufficient or misread
tool            the execution system could not perform the intended operation
interface       the instruction passed to the execution system was ambiguous
```

Canonical implications:

- **knowledge failure** → possible Pattern / Pattern refinement;
- **orchestration failure** → possible AP / AP refinement;
- **repeatable training deficiency** → possible Drill;
- retrieval/application/continuity/reference/tool/interface failures → execution problems first, not excuses to bloat the library.

Use the buffer:

```text
attempt
  ↓
observation
  ↓
repeated evidence
  ↓
possible canonical refinement
```

Never convert one bad attempt directly into permanent doctrine.

---

# WHY THIS MATTERS ACROSS DOMAINS

This correction is global.

## Art

A finished landscape may require Patterns for:

- intent;
- composition;
- structure;
- value;
- color;
- atmosphere;
- material;
- texture;
- edges;
- final hierarchy.

The AP decides their dependency order and prevents premature finishing.

## Software Engineering

A debugging action may need:

- reproduction;
- evidence capture;
- hypothesis formation;
- isolation;
- controlled experiment;
- root-cause confirmation;
- repair;
- regression verification.

Those local decisions can remain Patterns while an AP controls the investigation.

## Writing

A revision action may coordinate:

- intent;
- structure;
- argument;
- evidence;
- paragraph function;
- clarity;
- voice;
- consistency.

## Research / Teaching / Other future lanes

The same rule holds:

**Patterns contain expertise. APs conduct it. Drills strengthen it.**

---

# ART-SPECIFIC ORIGIN OF THE CORRECTION

The AP architecture change came directly from a post-Schmid landscape test.

The main failure was not lack of Art knowledge.

The runtime successfully produced:

- strong composition;
- clear focal hierarchy;
- coherent large value masses;
- atmospheric depth;
- painterly handling.

But it skipped too quickly from:

```text
large mass
   ↓
finished painterly surface
```

without sufficiently protecting:

```text
large mass
   ↓
meso-scale structural breakup
   ↓
internal color variation
   ↓
selective texture / finish
```

The landscape therefore became the first clear **post-Schmid AP-coverage failure case**.

A future Art AP audit should begin with a candidate action similar to:

`AP_render_landscape_to_finished_painting`

Do **not** automatically land that object from this memcap. First audit existing Art AP ownership and current Patterns, then propose the actual AP delta.

Likely gates worth testing include:

- do not advance from broad block-in while major natural forms have silhouette and light/shadow but no characteristic meso-scale structure;
- before finalization, check that major value families contain intentional hue/chroma/temperature variation rather than collapsing into one warm/cool swatch;
- atmospheric reduction should remove microtexture before it erases characteristic meso-scale form;
- visible painterly marks should perform a form, material, light, edge, or color job rather than merely signal “painterly style.”

These are **audit hypotheses**, not automatically canonical language.

---

# CURRENT ART STATE

Richard Schmid — *Alla Prima: Everything I Know About Painting* is complete.

Post-Schmid Art state:

- **345 Art objects**
- 218 Patterns
- 110 Drills
- 17 APs

The Schmid pass contributed **10 net-new Art objects** plus variants/refinements across Rendering, Color, Observation, Composition, Mark-making, and medium-specific execution.

The reconstructed post-Schmid library is already included in the current combined archive.

The proposed next source is:

**Richard Schmid — *Alla Prima II***

The user has the source and plans to upload it later.

Because *Alla Prima II* is an expanded/revised edition of the completed Schmid source, treat it as a **high-intensity collision/refinement source**, not greenfield ingestion. Preflight before authoring.

---

# CURRENT SOFTWARE STATE

Software Engineering was added to the combined repo after the AP doctrine correction.

Current Software state:

- **386 Software Engineering objects**
- 307 Patterns
- 63 Drills
- 16 APs

The Software cards were not rewritten during the merge.

Claude is currently working on the code side and may perform the Software AP audit/rework.

Therefore:

- do **not** independently mutate Software APs unless explicitly asked;
- use the new global AP doctrine when reviewing them;
- expect some existing APs to contain procedural knowledge that may need to remain as control flow or move back to Pattern ownership;
- prefer refinement over parallel replacement workflows.

---

# CANONICAL FILES UPDATED FOR THE AP CORRECTION

The AP correction was applied globally across the repo documentation/runtime contract.

Relevant files include:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `ARCHITECTURE.md`
4. `PASS/SKILL.md`
5. `PASS/docs/PASS_DOCTRINE.md`
6. `PASS/docs/PASS_RUN.md`
7. `PASS/docs/PASS_SCHEMA.md`
8. `PASS/docs/PASS_CONSUMPTION.md`
9. `PASS/docs/RUNTIME_KERNEL.md`

Treat the repo versions as canonical over this memcap if the two ever diverge.

This memcap exists to preserve intent and explain why those rules changed.

---

# IMPORTANT AUTHORING GUARDRAILS

- Do not convert large numbers of Patterns into APs merely to balance counts.
- Low AP count is only a signal to inspect action coverage.
- APs should remain substantially fewer than Patterns.
- Do not make an AP a source-summary or chapter-order object.
- Do not duplicate Pattern DOs/DON'Ts inside an AP.
- Do not create a separate AP registry/database.
- Do not force every task through `0 → 4`.
- Do not use one runtime failure as automatic evidence for a new Pattern.
- Do not treat an ad-hoc Pattern chain as equivalent to a mature AP.
- Do not require one source to teach the complete AP.
- Do not infer missing craft knowledge during AP synthesis.
- Do not mutate Art Stages as part of this correction.

---

# FIRST ACTIONS AFTER HANDOFF

When this memcap is used in a future chat or agent session:

1. Load the actual current repo.
2. Read the canonical PASS files in normal order.
3. Confirm the AP doctrine still matches:
   - Pattern = decision;
   - AP = goal-directed orchestration;
   - Drill = practice/evaluation.
4. Validate the repo before mutating anything.
5. For **Art**, perform an AP coverage audit before manufacturing new Pattern fixes from generation failures.
6. Start that audit with high-value complete actions, using the landscape test as the first known orchestration-gap case.
7. For **Software**, defer to Claude's code/AP work unless the user explicitly routes that work here.
8. When *Alla Prima II* is supplied, preflight it against the **345-Art post-Schmid library** before extraction.
9. Continue using the cheapest honest disposition:
   - refinement;
   - variant;
   - new object;
   - replacement;
   - reject/no-extract.
10. Generate new archives only when explicitly requested.

---

# CURRENT HANDOFF STATE

- PASS AP architecture correction: **LANDED**
- AP canonical meaning: **goal-directed Pattern orchestration**
- Runtime retrieval direction: **AP-first for productive actions**
- AP synthesis procedure: **canonical**
- Failure attribution taxonomy: **canonical**
- Universal stage scaffold: **retained, no longer mistaken for universal task control flow**
- Art Stages: **frozen / unchanged**
- Art: **345 objects**
- Software Engineering: **386 objects**
- Shared metaskills: **4**
- Total PASS objects: **735**
- Indexes: **85 current**
- Visual references: **OK**
- Post-Schmid reconstruction: **complete**
- Art AP coverage audit: **not yet performed**
- Software AP audit: **deferred / likely Claude**
- Next Schmid source: **Alla Prima II, pending upload**
- Current combined repo archive: `SkillForge_Art_Schmid_AP_Rework_With_Software_2026-08-18.zip`
