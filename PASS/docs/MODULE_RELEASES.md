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

## Skillset Memory in a release

A release ships the memory store of every domain it bundles, and no other. The
domain is the top-level package name of a selected module, so `art/composition`
and `art/subjects/animals` both mean `memory/art/`. Stores land at
`memory/<domain>/` in the release root — beside `library/`, never inside it.
Packaging memory must not turn an observation into a card (`ARCHITECTURE.md`
contract 20).

Memory is not a build dependency. A domain with no store contributes nothing,
and a build with `memory/` deleted entirely succeeds and declares
`memory_domains: []`. `--memory` overrides the tree the stores are read from;
it receives the same output protection as `--library`.

Shipped memory files are written read-only, and the ZIP carries both the POSIX
mode and the DOS read-only attribute so either extractor preserves it. The
release is a reader of the record, not its persistence target: new events belong
to the library that owns the store. Read-only is a statement of that contract,
not a security boundary — a consumer who clears the bit only forks a copy that
no longer travels back.

`RELEASE_MANIFEST.json` records the shipped domains in `memory_domains`, and
`check` rejects a declared domain whose store is missing, a packaged domain the
manifest does not declare, and a memory domain with no matching packaged library
package.

## Quality gate

A normal release build fails closed unless all of these pass:

1. PASS schema and relationship validation;
2. visual-reference asset verification;
3. local asset resolution;
4. portability scan;
5. Skillset Memory validation, when the release ships a store.

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
repository are refused even with that flag. Explicit external library, memory, and
recipe paths receive the same ancestor/descendant protection. Builds occur in a temporary
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
