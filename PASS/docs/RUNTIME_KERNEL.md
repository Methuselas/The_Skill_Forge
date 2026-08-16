# SkillForge Runtime Kernel

The runtime kernel is SkillForge's procedural centerline. It makes lane and
execution-mode routing, knowledge activation, gates, and completion requirements
deterministic without moving semantic craft judgment out of the knowledge cards.

## Boundary

**Scripts decide when thinking must happen. Skills teach how to think about it.
The model makes the judgment. Verification checks what happened.**

Metaskills are therefore **script-dependent, not script-owned**. `RUNTIME.yaml`
files declare activation conditions, while the AP/Pattern/Drill cards remain the
source of meaning and method.

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
