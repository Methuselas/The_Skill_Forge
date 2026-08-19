# SkillForge Runtime Kernel

The runtime kernel is SkillForge's deterministic routing and completion
centerline. It makes lane and execution-mode routing, declared metaskill
activation, risk checks, and completion requirements deterministic without moving
semantic craft judgment or task orchestration out of the knowledge cards.

## Boundary

**Scripts decide deterministic routing and when checks must happen. APs organize
the craft action. Patterns supply the decisions. Drills supply practice. The model
makes semantic judgments. Verification checks what happened.**

Metaskills are therefore **script-dependent, not script-owned**. `RUNTIME.yaml`
files declare activation conditions, while the AP/Pattern/Drill cards remain the
source of meaning and method. The kernel must not become a hidden domain workflow
engine.

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

Normal visual-generation requests default here. The final image is produced
without exposing Stage 0–3 artifacts or approval gates, but earlier-stage craft
knowledge remains active as constraints. Direct Render is not naive Stage 4.
Post-render verification is still mandatory.

### Staged Production

Training, drills, debugging, explicit process requests, or an explicit Staged
override externalize Stage 0 → 1 → 2 → 3 → 4. Stage artifacts, approval gates,
parentage/commitment checks, rollback, and final verification are required.

Difficulty alone does not silently change modes. An unusually difficult Direct
Render may accumulate more risk checks, but it remains Direct unless the user or
profile routing selects Staged Production.

## Risk checks

Profiles may add task-specific checks such as camera consistency, digit count,
weight/support, or articulated attachment chains. Python requires that those
checks be performed and recorded. It never decides whether the pose, anatomy,
composition, prose, or code is correct.

## Runtime CLI

Canonical authoring example:

```bash
python PASS/runtime/skillforge_runtime.py \
  --profile PASS/runtime/profiles/art.yaml \
  --library library \
  resolve --request "Draw a figure pointing toward the camera"
```

Portable releases vendor the same canonical kernel as
`scripts/skillforge_runtime.py` and the selected profile as
`runtime/profile.yaml`. `doctor` validates the profile/manifests; `verify`
fails closed when required completion/risk checks are absent.

## Release packaging

The canonical kernel has one source of truth. Release builds vendor a tiny copy
into each self-contained skill rather than assuming one installed skill can
import executable code from another.

Deployment constraints are separate from runtime semantics and authoring health.
Target-specific package-size policies live under
`PASS/runtime/deployment_profiles/` and are enforced only at the release boundary.
