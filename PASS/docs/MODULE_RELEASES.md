# Module and Release Composition

A source module owns coherent reusable knowledge and declares only local direct
requirements in `MODULE.yaml`. A named release recipe selects its entry module(s).
`build_release.py` always adds `metaskills`, recursively resolves module and object
prerequisites, runs the release quality gates, then materializes the complete
closure under `library/` inside the release.

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
3. content-addressed grounding attestations for every source used by the selected
   dependency closure;
4. local asset resolution;
5. portability scan.

Grounding attestations bind the exact source ledger and exact cards to either a
live source verification or an explicitly accepted canonical archive. This lets
third-party source books remain outside Git while preventing a modified or
ungrounded library from silently publishing. Any card or grounding-ledger change
invalidates its source attestation until it is reviewed and re-attested.

`--unsafe-skip-quality-gates` exists only for composition fixtures/tests. A release
built that way is marked unsafe and intentionally fails `build_release.py check`.

## Output safety

The builder never recursively deletes an existing directory by default. Existing
outputs require `--replace`, and protected repository/library/authoring paths are
refused even with that flag. Builds occur in a temporary sibling directory and are
moved into place only after validation succeeds.

ZIP output remains opt-in.
