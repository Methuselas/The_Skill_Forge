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
| [Agent Kit](skills/agent-kit/) | Coordinating several AI agents in one project | `1.0.0-beta.144` | 92,966 | `cd6303bba5b0fc5e6eed41216e7f8fc228c4b69fc2f3f6abca85bb0118022c9f` |
| [Art](skills/art/) | Drawing, painting, comics and illustration craft | `1.0.0-beta.144` | 9,304,235 | `a9f620da6f69c91af7df8c48015fe8a5b34acba08e66a1cba811146dae1e9b77` |
| [Game Design](skills/game-design/) | Mechanics, characters, adversaries, adventures, worlds | `1.0.0-beta.144` | 556,892 | `08b555303c8e4aea93545232f36778d629b7765741fbe909f289798b0ee360c8` |
| [Software Engineering](skills/software-engineering/) | Design, implementation, review, testing, AI systems, C++, Rust, Unreal | `1.0.0-beta.144` | 3,303,499 | `8fec0e8b0cb5154da3f0ddcfe478de8c0ff3c650f08fed8f68bd50b77c2b88a0` |
| [Writing](skills/writing/) | Fiction, poetry, nonfiction, essays, career documents | `1.0.0-beta.144` | 960,891 | `22dd6aefd7254303ba0fb44b1d5ba0ead6b6b3001e8ae53fc8178e14e714c5d2` |

## Model tools

Not built by PASS; each carries its own version.

| Tool | What it is for | Version | Size (bytes) | SHA-256 |
|---|---|---|---:|---|
| [Bionic Memory](models/bionic/) | Persistent cross-session memory for AI agents | v2 | 5,732 | `0c954bbfc27b53bdb9af1e7954b03152e30cd0529b3247cbc5ca4a1176d51519` |
