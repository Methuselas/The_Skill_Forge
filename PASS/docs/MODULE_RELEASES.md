# Module and Release Composition

A source module owns coherent reusable knowledge and declares only local direct requirements in `MODULE.yaml`. A named release recipe selects its entry module(s). `build_release.py` always adds `metaskills`, recursively resolves module requirements and object prerequisites, then copies the complete closure into the release. Missing prerequisites or cycles fail the build. The final release contains no external module links. ZIP output is opt-in.
