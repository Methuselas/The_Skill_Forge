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
| [Agent Kit](skills/agent-kit/) | Coordinating several AI agents in one project | `1.0.0-beta.75` | 92,235 | `ef217f474477fca494432d49e15c43079384457ef377c6d337098cfc7f155e6e` |
| [Art](skills/art/) | Drawing, painting, comics and illustration craft | `1.0.0-beta.75` | 9,307,715 | `24a0aa0cd941dfff1af82262e46875cd5e1f69bfa312cd56a72690daa55fd1c1` |
| [Game Design](skills/game-design/) | Mechanics, characters, adversaries, adventures, worlds | `1.0.0-beta.75` | 579,950 | `caeaafd3e3da92821e03a251cf8362f48f4c195e86e420d162267c578ee3b18e` |
| [Software Engineering](skills/software-engineering/) | Design, implementation, review, testing, C++, Unreal | `1.0.0-beta.75` | 2,365,273 | `ce4265668f59a4ecf7e7759823484acb05464a759c2cb44f6312defe545c29e5` |
| [Writing](skills/writing/) | Fiction, poetry, nonfiction, essays, career documents | `1.0.0-beta.75` | 989,222 | `f1f99d520dc0296bdac398fd8b151ee65ee8a94ce1eede4cf3c01e19e01a3198` |

## Model tools

Not built by PASS; each carries its own version.

| Tool | What it is for | Version | Size (bytes) | SHA-256 |
|---|---|---|---:|---|
| [Bionic Memory](models/bionic/) | Persistent cross-session memory for AI agents | v2 | 5,732 | `0c954bbfc27b53bdb9af1e7954b03152e30cd0529b3247cbc5ca4a1176d51519` |
