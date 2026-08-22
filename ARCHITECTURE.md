# SkillForge Architecture Contract

SkillForge is a workspace for manufacturing portable, self-contained AI skillsets.
The repo is optional infrastructure; the release is the product.

## The guiding test

For every component, ask:

> Does PASS need this in order to execute or validate the finished skill card?

If no, it is not a mandatory part of PASS.

> Does another agent or domain need this in order to create cards in its own lane?

If no, it does not become shared infrastructure.

> Will the runtime still have this source?

If no, the runtime does not depend on it.

## Contract

1. PASS is a portable authoring skill.
2. Finished releases are self-contained.
3. Released skills never depend on SkillForge.
4. Clean chats/Projects are first-class environments; a repo is optional. A card
   authored in a chat project and one authored in a checkout use the same schema
   and validate the same way.
5. **A card is source-independent.** It carries no source id, locator, page,
   hash, receipt, or attestation, and it must execute after the work it was
   learned from is gone.
6. **Skill domains are independent.** `art`, `writing`, and `software-engineering`
   are authored, validated, and built without one another. They share a library,
   not an authoring process.
7. Cards may reference cards in their own domain, plus the shared `metaskills`
   package. Any other cross-package edge is a domain coupling and fails.
8. Every SkillForge release includes `metaskills`.
9. Duplicate guarding is domain-local. Card IDs are unique library-wide.
10. Skill-required tools live with that skill; workspace-only tools stay in the
    workspace.
11. No global registry or index without demonstrated functional need, and never
    one that creates cross-domain authoring coupling.
12. Hard prerequisites survive folder boundaries and fail closed if unresolved.
13. Adding a module or language must not require modifying unrelated siblings.
14. Generated output is not canonical source.
15. Python may accelerate PASS but must not be the only place its methodology
    exists.
16. Temporary scratch state is disposable. Deleting it must never invalidate the
    library.
17. Art may use formal human-guided teaching; autonomous domains may be
    agent-authored. The repo must not force either mode.
18. The current staged-drawing process is frozen until explicitly streamlined
    later.
19. **Patterns own reusable decisions; APs own goal-directed orchestration; Drills
    own repeatable practice or evaluation.** The resolver may resolve routing and
    audit completion deterministically when invoked, but it must not hide domain
    action logic inside scripts, and nothing may describe it as enforcing what
    only the model and host can actually do.

## Knowledge and action composition

PASS has one knowledge vocabulary with three roles, not three competing stores of
the same information:

```text
Pattern  -> what decision to make
AP       -> how to apply decisions together to complete an action
Drill    -> how to practise or evaluate those capabilities
```

An AP is allowed to be synthesized from accepted Patterns after the sources that
taught those Patterns are gone. That does not weaken source grounding: the AP may
only coordinate canonical knowledge that already exists, and it remains
source-independent like every other card. Practice results may reveal that an AP
is missing, but one run's history does not become the AP's content.

For productive requests, semantic retrieval should prefer the closest applicable
AP and let that protocol activate its Pattern owners. When no AP exists, ad-hoc
Pattern composition is a valid runtime fallback and an authoring signal, not a new
architectural subsystem. No AP registry or separate workflow database is needed.

## The Skill Forge boundary

**PASS is the workbench; Skill Forge is the repository of finished skillsets.**
A validated card is not a skillset. `library/` holds domain knowledge being
matured; a skillset is the mature assembled product built from it. Do not
describe Skill Forge as "where finished cards go" — that collapses the two
layers. As of 2026-08-16 no lane has crossed the threshold.

### Foundations ship as their own package

`build_release.py` currently resolves a recipe's reference closure by
**inclusion**: the C++ recipe names only `software-engineering/languages/cpp`,
and the build pulls in every `core` card those cards reference. Nothing dangles,
so contract item 12 holds — but it holds by copying. That release ships 80 C++
cards and 251 core cards, and every future language skill would carry its own
copy of the same 251.

The intended shape is that a **core or foundational subtree becomes its own
distributable package**, and dependent skills declare it as a prerequisite
rather than absorbing it:

```text
Software Engineering Core          Art Foundation
        ↑                                ↑
   Python · C++ · JS               Figure Drawing · …
```

Two reasons, both practical: a foundation duplicated into every sibling
consumes each one's package-size budget, and a foundation that ships once can be
updated once.

Express the dependency by extending the existing recipe or module manifest. Do
not build a dependency database. A build must still prove the full transitive
closure plus `metaskills` resolves before publishing — declaring a prerequisite
replaces duplication, not verification.

This is runtime/distribution metadata about finished packages. It is not retired
authoring bureaucracy, and the prohibition below does not cover it.

### Maturity is declared by the user, never inferred

A domain is ready to build when **its reading list is complete and the user says
so.** Both halves matter: the reading list is the scope, and the call is a
human's.

No agent may declare a domain mature. Nothing measurable supports the judgment —
card count least of all, since a mature library correctly declines most of what
it reads, so output slows exactly as readiness arrives. An agent seeing a run
produce few cards is looking at the same signal a saturated domain and a badly
read source both produce.

Until the user says otherwise, treat every build as a development artifact.

## What this architecture must not grow back

Prefer deletion over abstraction; plain files over state machinery;
self-contained cards over reconstructed provenance.

Do not reintroduce an authoring ledger, a provenance graph or database, a source
manifest system, source staging, page receipts, quality attestations, source
projections, state sidecars, a synchronization protocol, a universal meta-domain,
a shared Teaching lane, a migration framework, or a mandatory session-state
object.

Retired 2026-08-15. See `docs/CLEANUP_2026-08-15.md`.
