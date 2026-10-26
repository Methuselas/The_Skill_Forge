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
| [Agent Kit](skills/agent-kit/) | Coordinating several AI agents in one project | `1.0.0-beta.101` | 92,102 | `0ed52ed7f217ec302d57eab8f82eb6d40d2896d0f66e658660d6bd44614faee8` |
| [Art](skills/art/) | Drawing, painting, comics and illustration craft | `1.0.0-beta.101` | 9,317,295 | `523db9af42cd75d0ff8f1b4a45eb137794d96f6298e67cb62a61f1e97d445b86` |
| [Game Design](skills/game-design/) | Mechanics, characters, adversaries, adventures, worlds | `1.0.0-beta.101` | 582,842 | `6e12432849626392983571efe43bb5349c881e42403c17bbd985c87e1a4a3c89` |
| [Software Engineering](skills/software-engineering/) | Design, implementation, review, testing, AI systems, C++, Rust, Unreal | `1.0.0-beta.141` | 3,226,614 | `2548973d15ac5bfc807ae24f0fb3b3e26f5f7d81ce18469b91187bac238b838a` |
| [Writing](skills/writing/) | Fiction, poetry, nonfiction, essays, career documents | `1.0.0-beta.101` | 995,586 | `dbd548477a784127312938e878b3adb05e2ce62531b4adca32a79375263cac19` |

## Model tools

Not built by PASS; each carries its own version.

| Tool | What it is for | Version | Size (bytes) | SHA-256 |
|---|---|---|---:|---|
| [Bionic Memory](models/bionic/) | Persistent cross-session memory for AI agents | v2 | 5,732 | `0c954bbfc27b53bdb9af1e7954b03152e30cd0529b3247cbc5ca4a1176d51519` |
