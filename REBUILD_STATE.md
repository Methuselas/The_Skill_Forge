# Rebuild State

- Phase 1 Architecture contract: complete
- Phase 2 Portable PASS package: complete
- Phase 3 Module -> release composition: complete
- Phase 4 Workspace cleanup: complete
- Phase 5 Software Engineering core + C++ split: complete
- Phase 6 Art u27 reconciliation and subject reorganization: complete
- Phase 7 Hard export boundary: complete
- Phase 8 Local portability tests: complete; clean ChatGPT platform acceptance remains external/pending
- Phase 9 Human documentation: complete
- Phase 10 Fresh Git baseline: complete
- Phase 11 Architecture reset — source, ledger, and domain decoupling: complete (2026-08-15)

Stages are frozen until explicitly streamlined later.

## Phase 11 — architecture reset (2026-08-15)

The authoring infrastructure that had accumulated around sources was removed
rather than improved. Cards no longer carry source identity; validation and
release builds read only the library; the three skill domains are independent;
Teaching left the shared pipeline and is quarantined under `archive/`.

Full record: `docs/CLEANUP_2026-08-15.md`. Contract: `ARCHITECTURE.md`.
