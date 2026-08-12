# SkillForge Architecture Contract

SkillForge is a workspace for manufacturing portable, self-contained AI skillsets. The repo is optional infrastructure; the release is the product.

1. PASS is a portable authoring skill.
2. Finished releases are self-contained.
3. Released skills never depend on SkillForge.
4. Clean chats/Projects are first-class environments; a repo is optional.
5. Skill-required tools live with that skill; workspace-only tools stay in the workspace.
6. No global registry or index without demonstrated functional need.
7. Source modules may compose; release dependency closure is materialized locally.
8. Every SkillForge release includes `metaskills`.
9. Hard prerequisites survive folder boundaries and fail closed if unresolved.
10. Adding a module or language must not require modifying unrelated siblings.
11. Generated output is not canonical source.
12. Python may accelerate PASS but must not be the only place its methodology exists.
13. Art may use formal human-guided teaching; autonomous domains may be agent-authored. The repo must not force either mode.
14. The current staged-drawing process is frozen until explicitly streamlined later.
15. No memcap architecture is assumed until one is intentionally designed.
