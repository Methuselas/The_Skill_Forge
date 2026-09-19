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
| [Agent Kit](skills/agent-kit/) | Coordinating several AI agents in one project | `1.0.0-beta.59` | 79,983 | `c4c6729aee5848c59134fa28940d6115cc94bba43c8c71b03a3bf7cff31c74bd` |
| [Art](skills/art/) | Drawing, painting, comics and illustration craft | `1.0.0-beta.49` | 9,310,904 | `9a76ee788ae302be22f1e1d3d7d668100335fa1f3b8b455a810f43876824bb64` |
| [Game Design](skills/game-design/) | Mechanics, characters, adversaries, adventures, worlds | `1.0.0-beta.49` | 572,519 | `7001ca5646e6000def047a0f7e38e4b25be4105018fec998f91ed06ad1c99870` |
| [Software Engineering](skills/software-engineering/) | Design, implementation, review, testing, C++ | `1.0.0-beta.49` | 2,092,842 | `868f713c90546d509d758df736687d288717d9ed638b2730d307ad1490589a03` |
| [Writing](skills/writing/) | Fiction, poetry, nonfiction, essays, career documents | `1.0.0-beta.49` | 985,506 | `448ce4d7dccccea74422555dd9b9778e453fc89a8882483778f550cb1772941b` |

## Model tools

Not built by PASS; each carries its own version.

| Tool | What it is for | Version | Size (bytes) | SHA-256 |
|---|---|---|---:|---|
| [Bionic Memory](models/bionic/) | Persistent cross-session memory for AI agents | v2 | 5,732 | `0c954bbfc27b53bdb9af1e7954b03152e30cd0529b3247cbc5ca4a1176d51519` |
