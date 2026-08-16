# Skill Author Guide

This guide defines how portable SkillForge source modules become self-contained releases.

## 1. Define a clean module boundary

A module owns one coherent body of source knowledge. Organize by what the knowledge is and who owns it, not by book title, historical path, agent, or shipping accident.

Examples:

- `software-engineering/core`
- `software-engineering/languages/cpp`
- `art/drawing/perspective`
- `art/drawing/subjects/figure/anatomy`
- `art/drawing/subjects/animals/anatomy`

The folder tree is navigation, not a second ontology. Moving two related skills into different folders must not erase their relationship.

Do not create empty future taxonomy merely because a domain may exist later. Add a new subject, style, medium, or variant structure when trained/authored knowledge actually requires it.

## 2. Source modules are not release boundaries

Modules may be reused during authoring. A release is a materialized product.

Conceptually:

```text
software-engineering/core
        +
software-engineering/languages/cpp
        +
metaskills
        ↓
C++ Development
```

A recipient receives the complete result. They do not resolve SkillForge dependencies separately.

## 3. Metaskills are mandatory

Every released SkillForge skillset includes `metaskills` automatically. The release recipe must not depend on a human remembering to add it.

`metaskills` is the universal catch-all process baseline shared by all skillsets. Domain-specific modules extend it; they do not replace it.

## 4. Declare prerequisites explicitly

A prerequisite is a hard dependency, not a browsing suggestion.

Prerequisites may cross folders and domains. For example, an animal skill may depend on a figure-construction, anatomy, perspective, or process skill if the trained knowledge requires it.

Rules:

- declare the prerequisite in the authored relationship metadata;
- do not rely on folder adjacency;
- resolve prerequisites recursively;
- include the module that owns every required prerequisite in the final release;
- fail export if any hard prerequisite cannot be found;
- reject dependency cycles.

If object A is required before object B can be applied correctly, a release containing B must also contain A, regardless of where A lives.

## 5. Keep module metadata local

Use the smallest local module description that is sufficient to identify the module and its direct module requirements. Do not introduce a global registry merely to discover modules that can already declare themselves locally.

A module may conceptually declare:

```yaml
name: software-engineering/languages/cpp
requires:
  - software-engineering/core
```

Release composition then combines local module requirements with object-level prerequisite closure.

## 6. Named releases select intent, not every ingredient

A named release recipe should identify the requested product and its entry module or modules, for example:

```yaml
name: Animal Anatomy
modules:
  - art/drawing/subjects/animals/anatomy
```

The recipe is not a hand-maintained duplicate of the prerequisite graph. PASS calculates the closure.

When a prerequisite changes, fix the relationship at its source rather than editing a giant release ingredient list.

## 7. Preserve the authoring mode

Not every skill is learned the same way.

**Autonomous authoring** is appropriate when agents can reliably derive the skill from the supplied sources and validation rules.

**Human-guided teaching** is required when durable skill behavior depends on interpretation, correction, taste, or a teacher-developed method. In that mode, the conversation is part of the training process even though raw chat transcripts are not automatically release material.

Do not flatten a formally taught skill back into "what the book says" during maintenance.

## 8. Release requirements

Every release must:

- contain `metaskills`;
- contain every hard prerequisite and required module locally;
- contain all runtime instructions/resources/tools it actually needs;
- work without SkillForge present;
- use only local references inside the release;
- preserve the authored skill relationships needed by the consumer;
- exclude unrelated skill families.

A release must not contain workspace-only material such as:

- `.git`;
- agent coordination or ownership files;
- authoring scratch notes;
- source PDFs, books, or other study material;
- build caches;
- repo importers;
- unrelated modules;
- absolute or repo-relative external dependencies.

## 9. Portability test

Before calling a release complete:

1. materialize it outside the SkillForge tree;
2. verify all local references resolve;
3. verify `metaskills` and prerequisite closure are present;
4. verify no workspace/source paths remain;
5. test it in a clean chat/Project when the platform permits;
6. confirm deleting the SkillForge workspace would not break the release.

The workspace manufactures skillsets. The release must not need the factory after export.

## Release quality gates

Publishing is gated, not just copying. The builder validates schema and
relationships, visual-reference assets, asset paths, and portability before a
release can pass.

Every gate runs against the packaged release tree, so a release is publishable on
the strength of the cards it actually ships. A build never resolves research
provenance: it cannot fail because a source book is missing, a receipt is stale,
or another domain was not inspected. Those checks were retired 2026-08-15.

Finished releases preserve the canonical `library/...` layout so authored local
asset paths stay valid.
