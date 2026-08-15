# Authoring workspace — private, local-only state

This is the factory. The repository publishes the product and a receipt proving
the product matches what was accepted; the working records that produced it stay
here, on your machine.

```
workspace/
  authoring/            <- private, local only (this directory)
    sources/              books and PDFs, staged locally      GITIGNORED*
    ledger/               REGISTRY, SOURCE, UNITS, receipts   GITIGNORED
    renders/              page-image cache for grounding      GITIGNORED
    handoffs/             inter-agent handoff notes           GITIGNORED
    README.md             this file                           tracked
  provenance/           <- PUBLIC: one compact receipt per source
    <source_id>.json                                          tracked
```

**\* One deliberate exception.** A small set of first-party images under
`sources/` *is* tracked: the guided art process sheets and renders that shipped
visual references were generated from. `verify_references.py` compares each
shipped reference against those renders to prove originality, so they have to
travel with the repo or the check cannot run publicly. `.gitignore` whitelists
them by name; every third-party book remains excluded. If you add a first-party
source whose renders back a shipped reference, whitelist it the same way.

## Why the ledger is not published

The ledger is needed **operationally** and not **publicly**. During authoring it
supplies the duplicate guard, the unit queue, grounding receipts, Teaching-lane
receipts, every rejected candidate and the reasoning behind it, and the state that
makes a run resumable and fail-closed. Those are internal working records. A
visitor to the repository does not need the page-level extraction decisions or the
list of candidates that were considered and dropped.

What a visitor *does* need is the ability to check that the shipped library has not
drifted from the grounding that was accepted. That is what
`workspace/provenance/<source_id>.json` provides. Each receipt carries the
attestation — `source_payload_sha256`, `ledger_tree_sha256`, `grounding_basis`,
`approved_by`, the source-projection hash of every card citing the source, and the
attestation signature — plus the three ledger facts the library checks need:
processed unit ids, whether the source is visual, and whether its images are
first-party.

`ledger_tree_sha256` is what makes the omission safe rather than merely convenient.
The public receipt names the exact private authoring record that was approved, so
the ledger can be produced later and checked against what was published.

## Two levels of validation

| | public checkout | authoring checkout |
|---|---|---|
| library schema, module closure, reference assets | yes | yes |
| provenance attestations, source-projection hashes | yes | yes |
| release portability | yes | yes |
| REGISTRY ↔ SOURCE/UNITS agreement (rule 25) | — | yes |
| unit status, candidate accounting, Teaching-lane receipts (rules 21, 24) | — | yes |
| live grounding against the real payloads | — | yes |

The tools detect which they are in — `validate.py`, `verify_references.py`,
`quality_attestation.py verify` and the release gate all read the ledger when it is
present and the published receipts when it is not. No flag is needed.

A clean public clone validates itself with:

```bash
python PASS/tools/validate.py                          # schema, closure, rule 13
python PASS/tools/verify_references.py                 # shipped reference images
python PASS/tools/quality_attestation.py verify --all  # provenance receipts
python PASS/tools/build_release.py build workspace/release-recipes/<recipe>.yaml <out>
```

None of those need the private ledger. Fail-closed still holds: a source with no
receipt fails rule 13 rather than passing unverified, an unclassifiable source
fails the reference gate rather than being waved through, and a tampered receipt
fails its signature check.

## Recreating this locally

Create the directories as you need them — Git does not track empty directories and
nothing needs to exist before you start:

```
workspace/authoring/sources/
workspace/authoring/ledger/
workspace/authoring/renders/
```

Stage a book into place with one command — it hashes, runs the duplicate guard,
preflights, copies, and scaffolds `SOURCE.md`:

```bash
python PASS/tools/stage_source.py "D:/Sources/Programming/Practice/<book>.pdf"
```

It copies rather than moves, so the original stays the evidentiary source and the
staged file is only the working payload.

After a fresh checkout every payload is missing, because `sources/` is gitignored.
Re-staging a book whose hash is already in the ledger is recognised as a re-attach:
the payload is restored to its recorded `payload_path` and `SOURCE.md` is left
alone, so `verify_grounding.py` works again immediately. Point it at the same book
and it will tell you there is nothing to do.

After attesting a source, republish its public receipt:

```bash
python PASS/tools/publish_provenance.py --all
python PASS/tools/publish_provenance.py --check    # CI-friendly staleness check
```

A receipt is stale until you do, and a stale or missing receipt fails the release
gate rather than shipping unverified.
