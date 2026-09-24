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
| [Agent Kit](skills/agent-kit/) | Coordinating several AI agents in one project | `1.0.0-beta.84` | 92,983 | `e12f06cf8025f3ca3cf38b660c4a9606077afa1dee42ef24e761d8ac42aa992b` |
| [Art](skills/art/) | Drawing, painting, comics and illustration craft | `1.0.0-beta.84` | 9,323,995 | `c2896d2828240d243a739f0f8005e256b4806b385696a94fbdcc2dc6e197f1be` |
| [Game Design](skills/game-design/) | Mechanics, characters, adversaries, adventures, worlds | `1.0.0-beta.84` | 584,945 | `508cd83979cb39c487546733f7cdaf9345a6ba6d15745efc7c840ea8015fc1da` |
| [Software Engineering](skills/software-engineering/) | Design, implementation, review, testing, C++, Unreal | `1.0.0-beta.84` | 2,603,294 | `5f50db4437aa05d633e84ba37f98dcb42a82d000e17a796e0b4e54b2ba5dda34` |
| [Writing](skills/writing/) | Fiction, poetry, nonfiction, essays, career documents | `1.0.0-beta.84` | 998,835 | `4eda7179cad68ba112bbf420b1315d0a003d0fed66f211c2c793697170ffc505` |

## Model tools

Not built by PASS; each carries its own version.

| Tool | What it is for | Version | Size (bytes) | SHA-256 |
|---|---|---|---:|---|
| [Bionic Memory](models/bionic/) | Persistent cross-session memory for AI agents | v2 | 5,732 | `0c954bbfc27b53bdb9af1e7954b03152e30cd0529b3247cbc5ca4a1176d51519` |
