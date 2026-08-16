# Authoring workspace — your local scratch space

Nothing in PASS reads this directory.

`library/` holds the finished cards. That is the whole system of record. There is
no authoring state to maintain beside it: no ledger, no source registry, no unit
queue, no reading receipts, no provenance records, no attestations. All of that
was retired on 2026-08-15 (see `docs/CLEANUP_2026-08-15.md`).

Keep whatever working notes help you while you study a source. They are yours,
they are disposable, and **deleting all of them cannot invalidate the library.**

```
workspace/
  authoring/            <- local scratch, ignored by every tool (this directory)
  release-recipes/      <- named products                          tracked
```

## Where source material goes

Wherever you like. A local folder, a chat project's uploaded files, a drive, your
own library. PASS does not track, copy, hash, or register source files, and no
card records which one it came from.

A card must be valid and executable after the source is gone. Delete every
research PDF and the library still validates and still builds:

```bash
python PASS/tools/validate.py
python PASS/tools/verify_references.py
python PASS/tools/build_release.py build workspace/release-recipes/<recipe>.yaml <out>
```

## Training notes

Guided-teaching notes (for example `art/training-notes/`) live here as local
scratch. They are raw material for authoring skill cards later, not repository
content, and no tool reads them. Keep them as long as they are useful to you.

## Historical local state

If you have a `ledger/`, `renders/`, `handoffs/`, or `sources/` directory here from
before the cleanup, it is inert. Nothing reads it, no validator looks for it, and
no build consults it. Delete it whenever you like.

`sources/` was partly tracked in Git until 2026-08-15, for a set of first-party
guided art renders. It was untracked because nothing read it and 15 of its 17
tracked images were byte-identical duplicates of assets already shipped under
`library/art/.../assets/`. The shipped images and their review sidecars are the
canonical copies, and that is what `verify_references.py` checks.
