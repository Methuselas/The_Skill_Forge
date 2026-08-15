# Authoring workspace — private, local-only state

Nothing under this directory except this file is tracked in Git. It is the
factory; the repository publishes the product and a receipt proving the product
matches what was accepted.

```
workspace/
  authoring/          <- private, local only (this directory)
    sources/            books and PDFs, staged locally
    ledger/             REGISTRY.md, SOURCE.md, UNITS.md, unit receipts
    renders/            page-image cache for visual grounding
    handoffs/           inter-agent handoff notes
  provenance/         <- PUBLIC: one compact receipt per source
    <source_id>.json
```

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

The tools detect which they are in. `validate.py` reads the ledger when it is
present and the published receipts when it is not; the release gate does the same.
No flag is needed.

## Recreating this locally

Create the directories as you need them — Git does not track empty directories and
nothing needs to exist before you start:

```
workspace/authoring/sources/
workspace/authoring/ledger/
workspace/authoring/renders/
```

Stage a book into place, then work normally:

```bash
python PASS/tools/preflight_pdf.py "D:/Sources/<path>/<book>.pdf"
```

Copy rather than move the file, so the original remains the evidentiary source and
the staged copy is only the working payload.

After attesting a source, republish its public receipt:

```bash
python PASS/tools/publish_provenance.py --all
python PASS/tools/publish_provenance.py --check    # CI-friendly staleness check
```

A receipt is stale until you do, and a stale or missing receipt fails the release
gate rather than shipping unverified.
