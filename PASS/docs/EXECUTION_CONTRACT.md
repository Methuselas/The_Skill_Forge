# SkillForge Execution Contract

This document defines the **execution contract** SkillForge declares: which
execution mode and lane a request resolves to, which metaskills activate, which
risk checks apply, and what completion requires. It is a contract, not a kernel.

## What actually executes what

SkillForge has three layers, and confusing them is the failure this document
exists to prevent.

| Layer | Owns | Can enforce |
|---|---|---|
| **Cards and profiles** | What behavior SkillForge asks for | Nothing — they are declarative |
| **`skillforge_runtime.py`** | Deterministic resolution and auditing, *when invoked* | Only what is explicitly routed through it |
| **The host** (ChatGPT, Claude Code, …) | Model behavior, native tools, image generation, conversation state | Everything that actually happens |

`skillforge_runtime.py` is a repository-side resolver and contract auditor. It
runs only when something calls it, keeps no state between calls, and cannot
observe, intercept, or block a model or host action. A test proving the profile
declares a Stage 4 AP does not prove the host will execute Stage 4 through it.

Everything below is therefore either **declared** by a profile, **resolved** by
the script, or **honored** by the model and host. Where a behavior depends on
model compliance, this document says so rather than implying machinery.

## Boundary

**Profiles declare deterministic routing and which checks apply. The resolver
reports that declaration on request. APs organize the craft action. Patterns
supply the decisions. Drills supply practice. The model makes semantic judgments
and is responsible for honoring the contract. Verification checks what happened.**

Metaskills are therefore **contract-declared, not script-owned**. `RUNTIME.yaml`
files declare activation conditions, while the AP/Pattern/Drill cards remain the
source of meaning and method. The contract must not become a hidden domain
workflow engine, and the resolver must not be mistaken for one.

## Semantic action routing

For a productive user request, the model resolves knowledge **AP-first** inside
the active domain:

```text
request -> applicable AP -> Pattern owners -> applicable variants
```

The AP supplies semantic control flow: dependency order, gates, branches, recovery,
continuity checks, and stopping. Patterns remain the owners of the individual
decisions, so improving a Pattern automatically improves every AP that uses it.

If no adequate AP exists, the model may assemble an ad-hoc Pattern chain and still
complete the request. Runtime does not silently manufacture a canonical AP. The
missing orchestration is an **AP coverage gap** that may be taken to a later PASS
authoring audit.

AP-first is independent of execution mode. **Direct Render** may execute an AP
internally without exposing intermediate artifacts. **Staged Production** may
externalize the same or another AP's gates where the mode contract requires it.

## Orthogonal teach lane

Profiles resolve a `lane` independently from execution `mode`. `skill` is the
default lane. Explicit teaching, coaching, learning-design, or assessment intent
selects `teach`. A request can therefore resolve as Art + teach lane + Direct
Render, or Art + teach lane + Staged Production; choosing the teach lane does not
silently redefine the execution mode.

The lane is card-level semantics only. It selects how the domain's own cards are
applied; it does not route into a separate Teaching package, and no domain
depends on one. Resolution activates `metaskills` and the release's own domain
modules. (The shared Teaching lane was retired 2026-08-15.)

## Art execution modes

### Stage-informed Direct Render

Normal visual-generation requests default here. The requested artifact is produced
without exposing intermediate approval gates, but earlier craft knowledge remains
active as constraints. For universal Drawing, Stage 4 means **Finished Pencils**.
If the requested artifact is Ink, Color, Paint, Manga/B&W finish, or another
downstream medium, the skill routes from the internally solved Drawing lockset
into the closest applicable downstream AP (or an honest Pattern-chain fallback when
AP coverage is incomplete) rather than redefining Drawing Stage 4. Direct Render is
not a naive last-stage jump. Post-render verification is still mandatory.

### Staged Production

Training, drills, debugging, explicit process requests, or an explicit Staged
override externalize the universal Drawing sequence:

```text
Stage 0 Search / Composition
→ Stage 1 Framework / Scene Skeleton
→ Stage 2 Complete Minimum Mass
→ Stage 3 Specific Rough / Developed Pencils
→ Stage 4 Finished Pencils
```

Stage artifacts, approval gates, parentage/commitment checks, rollback, and final
verification are required. Ink, Color, Paint, Manga/B&W finish, and other
medium-specific workflows are downstream APs rather than permissions inside Drawing
Stage 4.

Difficulty alone does not silently change modes. An unusually difficult Direct
Render may accumulate more risk checks, but it remains Direct unless the user or
profile routing selects Staged Production.

### Registered-successor source-access gate

*Model- and host-dependent. No script observes an image call, so nothing here is
mechanically enforced. It is a contract the skill must honor, and only live
host regression testing can show whether it held.*

For any staged successor or local revision that requires image edit/reference
continuity, the contract requires two separate truths: the canonical predecessor
is known **and** the exact canonical artifact is actually available to the native
image tool as an edit/reference source. If exact access is unavailable, fail closed.
Recover or request a re-upload of that same artifact rather than reconstructing from
prose, substituting another stage/rejected image, or generating a near-match. A
re-upload restores access to the same canonical predecessor and inherited lockset
without new approval.

**Loss of edit-target access does not authorize visual reinterpretation.**

## Risk checks

Profiles may add task-specific checks such as camera consistency, digit count,
weight/support, or articulated attachment chains. The profile declares which
checks a request activates, and the resolver reports that list on request.

For staged Art, a risk rule may also declare `checks_by_stage`. This is a
**resolution compatibility rule**, not permission to ignore risk. A low-information
stage verifies the same underlying concern at the visual resolution it legally
owns: Stage 0 can verify gross contact/action intent without inventing fingers;
Stage 1 can verify hand blocks and attachment chains without finished digits;
Stage 2 can verify palm/contact masses; Stage 3-4 may require full visible digit
and topology checks. The consuming staged controller must pass the actual current
Drawing stage to the resolver after Stage 0. A fresh staged resolution defaults
to Stage 0 because no later stage is legal before approval.

Performing the selected checks is the skill's obligation; recording them is the
skill's obligation; `verify` audits the record afterward if someone runs it. Python
never decides whether the pose, anatomy, composition, prose, or code is correct,
and it cannot tell whether a check was genuinely performed or merely written down.

A profile may therefore require **evidence records** in addition to boolean checks.
This does not give Python vision. It prevents a lossy aggregate assertion such as
`all visible hands valid: true` from satisfying a contract that requires each
visible instance to be enumerated and inspected. For full hand-topology checks,
Art requires one record per materially visible hand, a declared visible-hand count
matching the number of records, local/enlarged inspection, root tracing, and an
expected-versus-observed topology count. `uncertain`, insufficient evidence, a
missing instance record, or a count mismatch leaves completion unresolved.

Accordingly, `verify` reports `completion_record_complete` separately from
`artifact_visually_validated`. The latter is always false in this repository-side
helper because the helper never receives or inspects the artifact. A complete
evidence record is stronger caller-supplied evidence, not independent visual proof.

## Resolver CLI

Canonical authoring example:

```bash
python PASS/runtime/skillforge_runtime.py \
  --profile PASS/runtime/profiles/art.yaml \
  --library library \
  resolve --request "Draw a figure pointing toward the camera"
```

For a continuing staged Drawing thread, supply the controller's current stage so
stage-aware risk checks resolve at the legal information ceiling:

```bash
python PASS/runtime/skillforge_runtime.py \
  --profile PASS/runtime/profiles/art.yaml \
  --library library \
  resolve --mode staged --stage 2 --request "Continue the approved mass-block successor"
```

Portable releases vendor the same canonical resolver as
`scripts/skillforge_runtime.py` and the selected profile as
`runtime/profile.yaml`. `doctor` validates the profile and manifests, including
that every card reference in the profile resolves to a real `object_id`. `verify`
audits a completion record its caller supplies and exits 2 when required
completion or risk checks are absent from that record — useful in CI, and no
obstacle whatsoever to a model that never writes the record.

Nothing invokes any of this automatically. A host that never runs the resolver
still gets the full library; it just does not get the deterministic resolution.

## Release packaging

The canonical resolver has one source of truth. Release builds vendor a tiny copy
into each self-contained skill rather than assuming one installed skill can
import executable code from another.

Deployment constraints are separate from execution semantics and authoring health.
A recipe may name a `deployment_profile`, and `build_release.py` then reads
`PASS/runtime/deployment_profiles/<name>.yaml` to check package size at the
release boundary. **That directory does not currently exist and no recipe names a
profile** — it is an available extension point, not active policy. A recipe naming
one before the file is added fails the build with a clear error.
