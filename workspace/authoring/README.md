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

`art/training-notes/` is tracked — the one exception to this directory being
scratch. Everything else here is yours and disposable.

Those notes record corrections given during guided teaching runs: where a
source's method was bounded, where a literal reading would have produced a wrong
card, where a technique turned out to be one option rather than a law. Some of
that judgment reached the cards; the reasoning behind it did not, because a card
carries the decision and not the argument that shaped it.

They are **not canonical**. No tool reads them, no build includes them, no card
depends on them, and deleting them cannot invalidate the library. They are also
not retired, so they do not belong in `archive/`.

They are practice history — the class of knowledge that sits between a finished
card and a practitioner's own memory, described in `PASS/docs/PASS_RUN.md` §5.

**This is a holding position, not a home.** They are tracked here only because
the practice-memory layer does not exist yet, and untracked they would live on
one machine and vanish with it. When that layer is designed, these move into it
or are superseded by it, and this exception and the `.gitignore` line that
carves it out both go away. Nothing should be built that depends on them
staying.

Do not promote their contents into cards wholesale. An observation from a
teaching run is evidence, not a Pattern; the buffer rule in §5 applies.

## Historical local state

If you have a `ledger/`, `renders/`, `handoffs/`, or `sources/` directory here from
before the cleanup, it is inert. Nothing reads it, no validator looks for it, and
no build consults it. Delete it whenever you like.

`sources/` was partly tracked in Git until 2026-08-15, for a set of first-party
guided art renders. It was untracked because nothing read it and 15 of its 17
tracked images were byte-identical duplicates of assets already shipped under
`library/art/.../assets/`. The shipped images and their review sidecars are the
canonical copies, and that is what `verify_references.py` checks.
