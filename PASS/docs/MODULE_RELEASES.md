# Module and Release Composition

A source module owns coherent reusable knowledge and declares only local direct
requirements in `MODULE.yaml`. A named release recipe selects its entry module(s).
`build_release.py` always adds `metaskills`, recursively resolves module and object
prerequisites, runs the release quality gates, then materializes the complete
closure under `library/` inside the release.

The top-level `teaching` package is conditional. A teaching-capable release
selects it explicitly in the recipe; the builder never treats it like mandatory
`metaskills`. The runtime can then combine the release's domain modules with
Teaching foundations when `lane: teach` is resolved, while ordinary `skill`
requests leave those Teaching objects inactive.

The release preserves canonical `library/...` paths. This is deliberate: trained
cards may contain local asset paths such as `library/art/.../assets/foo.png`, and
those paths must continue to resolve after export without rewriting card content.
Missing assets fail the build and `check` command.

Every release root is an Agent Skills-compatible directory. `SKILL.md` contains
required YAML `name` and `description` metadata followed by the consumer
instructions. The same release can be uploaded/installed where Agent Skills are
supported or used directly as an archived/context package.

## Quality gate

A normal release build fails closed unless all of these pass:

1. PASS schema and relationship validation;
2. visual-reference/provenance verification;
3. content-addressed grounding attestations for every primary or variant source used by the selected
   dependency closure;
4. local asset resolution;
5. portability scan.

Schema and visual-reference gates run against the materialized release closure,
so a defect in an unrelated skill family does not block an independent release.
Grounding attestations bind each source to every canonical card where it appears, whether as the
primary reference or an absorbed variant. The card hash is source-scoped: unrelated variants from
other sources are removed from the fingerprint, while the base card and that source's own variants
remain bound. This prevents a newly absorbed variant from falsely staling the owner source while
still invalidating the variant source when its method/prose changes. A base-rule change stales the
owner and attached variants because their meaning depends on the same canonical decision.

Attestations also bind the exact source ledger to either a live source verification or an explicitly
accepted canonical archive. This lets third-party source books remain outside Git while preventing a
modified or ungrounded source contribution from silently publishing.

`--unsafe-skip-quality-gates` exists only for composition fixtures/tests. A release
built that way is marked unsafe and intentionally fails `build_release.py check`.

## Output safety

The builder never recursively deletes an existing directory by default. Existing
outputs require `--replace`, and release outputs inside or above the factory
repository are refused even with that flag. Explicit external library and recipe
paths receive the same ancestor/descendant protection. Builds occur in a temporary
sibling directory and are moved into place only after validation succeeds.

ZIP output remains opt-in.

Each release manifest records a SHA-256 digest for every shipped file other than
the manifest itself. `build_release.py check` rejects missing, changed, or
unexpected files, missing or undeclared modules, unresolved packaged object
relationships, and stale quality-gate state. ZIP targets use the same canonical
path protection as release directories and must use a `.zip` extension.

Release closure follows every outgoing canonical `cross_links` target and the
reverse side of `prerequisite_for` edges, in addition to module requirements and
`foundation_object_id`. This keeps the packaged object graph self-contained;
soft relationships such as `related_to`, `supports`, and `teaches` may not turn
into dangling links merely because their target lives in another module.
