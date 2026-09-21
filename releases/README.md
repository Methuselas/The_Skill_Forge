# SkillForge Releases

Every release has its own folder with its ZIP and a README describing what it
contains, how to install it, and how to verify it. The ZIPs are generated
products: change them in [PASS](https://github.com/Methuselas/PASS), rebuild,
verify, and replace the ZIP here rather than editing an extracted release.

## Skills

Built and validated in PASS. Each one records the PASS version it was built from
as `pass_version` and passed the version-contract, schema, reference, asset,
portability, memory and release-integrity checks before its ZIP was written.

| Skill | What it is for | PASS build | Size (bytes) | SHA-256 |
|---|---|---|---:|---|
| [Agent Kit](skills/agent-kit/) | Coordinating several AI agents in one project | `1.0.0-beta.73` | 92,237 | `db69ba7870666bcae49ef70cc25d84b331c4af1f01ca5bb6dc2ae5afa5ba71dc` |
| [Art](skills/art/) | Drawing, painting, comics and illustration craft | `1.0.0-beta.73` | 9,307,715 | `cc5fc74eb606aaffc41a43977196ab49bfe3e515b045ed1b3963bb39af4a821b` |
| [Game Design](skills/game-design/) | Mechanics, characters, adversaries, adventures, worlds | `1.0.0-beta.73` | 579,949 | `dc8345563e051498ffcef15219f8339f16deb6d11cf905f4ea32cfc3e7753d62` |
| [Software Engineering](skills/software-engineering/) | Design, implementation, review, testing, C++, Unreal | `1.0.0-beta.73` | 2,367,141 | `3855bc84e6dd7641dfcf0e5e2ea58ba2079e0160008dc40375472939babb545f` |
| [Writing](skills/writing/) | Fiction, poetry, nonfiction, essays, career documents | `1.0.0-beta.73` | 989,221 | `131732df024abe36442aff80fce82d264d1962f62307c53f659dc6e2009c5d04` |

## Model tools

Not built by PASS; each carries its own version.

| Tool | What it is for | Version | Size (bytes) | SHA-256 |
|---|---|---|---:|---|
| [Bionic Memory](models/bionic/) | Persistent cross-session memory for AI agents | v2 | 5,732 | `0c954bbfc27b53bdb9af1e7954b03152e30cd0529b3247cbc5ca4a1176d51519` |
