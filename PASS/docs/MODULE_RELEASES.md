# Module and Release Composition

A source module owns coherent reusable knowledge and declares only local direct
requirements in `MODULE.yaml`. A named release recipe selects its entry module(s).
`build_release.py` always adds `metaskills`, recursively resolves module and object
prerequisites, runs the release quality gates, then materializes the complete
closure under `library/` inside the release.

A domain release packages that domain without loading any other. Closure follows
module and object prerequisites inside the domain, plus the shared `metaskills`
package. It never requires closure across another skill domain.

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
2. visual-reference asset verification;
3. local asset resolution;
4. portability scan.

Every gate runs against the materialized release closure, so a release is
publishable on the strength of the cards it actually ships and a defect in an
unrelated skill family cannot block an independent release.

A release build never resolves research provenance. It cannot fail because a
source PDF is missing, an attestation is stale, a ledger is absent, or another
domain was not inspected — none of those exist. Retired 2026-08-15.

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
