# Art Empirical Pressure Test

This directory holds resumable repository-side evidence that tests the current
Art library against real human artwork. It is test infrastructure, not Art canon
and not release content.

## Boundaries

- `library/art/` remains the only canonical Art knowledge source.
- External artwork is read-only and is not copied into this repository.
- Findings may nominate likely owners, but they do not mutate cards.
- A confirmed failure is unfinished until an approved repair has a generalized
  regression.
- Finished artwork proves outcomes more strongly than process. AP and Drill
  process claims require process evidence or an honest host-test designation.
- Repository tests do not prove installed-host selection, routing, or image-model
  behavior.
- Cataloguing or reading artwork is not a Skillset Memory training event.

## Files

- `manifest.jsonl` accounts for every Art Pattern, Drill, AP, and embedded
  Variant. Generated card metadata is refreshed from the library while progress
  fields are preserved.
- `coverage.json` summarizes inventory, status, and high-centrality Art targets.
- `fixture_manifest.yaml` describes the user-supplied evidence pool and records
  selected fixtures only when they enter a bounded batch.
- `state.yaml` records the pressure-test phase and next authorized action. It is
  project test state, not PASS authoring state, and never ships.
- `findings/`, `regressions/`, `rubrics/`, `host_tests/`, and `reports/` hold
  bounded artifacts as they are created.

## Commands

```bash
python tests/art_pressure/tools/build_inventory.py
python tests/art_pressure/tools/build_inventory.py --check
python -m unittest discover -s tests -p "test_*.py"
```

The inventory tool does not open or depend on the external comics collection.
A clean clone can verify object accounting without possessing the evidence pool.
