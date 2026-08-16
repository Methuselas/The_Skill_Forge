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

## Two boundaries this contract does not yet draw

Both are Skill Forge concerns, not PASS concerns. Neither blocks authoring, and
neither should be built speculatively — they are recorded so they are not
rediscovered as surprises.

**PASS is the workbench; Skill Forge is the repository of finished skillsets.**
A validated card is not a skillset. `library/` holds domain knowledge being
matured; a skillset is the mature assembled product built from it. Do not
describe Skill Forge as "where finished cards go" — that collapses the two
layers. As of 2026-08-16 no lane has crossed the threshold, so every skillset
question below is still hypothetical.

### 1. Prerequisite skills are duplicated, not declared

`build_release.py` resolves a recipe's reference closure by **inclusion**: the
C++ recipe names only `software-engineering/languages/cpp`, and the build
correctly pulls in every `core` card that the C++ cards reference. Nothing
dangles, so contract item 12 holds today.

It holds by copying. The C++ release ships 80 C++ cards and 251 core cards —
core outruns the skill it supports by roughly three to one. Every future
language skill would carry its own copy of the same 251.

That is fine until package-size limits force a mature domain to split into
several distributable skills, at which point the closure needs to be **declared**
rather than duplicated: `Figure Drawing` requires `Art Foundation`; a language
skill requires `Software Engineering Core`. Prefer extending the existing recipe
or module manifest to express that. Do not build a dependency database.

This is runtime/distribution metadata about finished packages. It is not retired
authoring bureaucracy, and the prohibition below does not cover it.

### 2. The maturity threshold is undefined

Nothing currently answers "when is a domain finished enough to build into a
skillset?" Card count does not answer it: a mature library correctly declines
most of what it reads, so growth slows precisely as a domain becomes ready.
Until the question is answered, treat every build as a development artifact.

## What this architecture must not grow back

Prefer deletion over abstraction; plain files over state machinery;
self-contained cards over reconstructed provenance.

Do not reintroduce an authoring ledger, a provenance graph or database, a source
manifest system, source staging, page receipts, quality attestations, source
projections, state sidecars, a synchronization protocol, a universal meta-domain,
a shared Teaching lane, a migration framework, or a mandatory session-state
object.

Retired 2026-08-15. See `docs/CLEANUP_2026-08-15.md`.
