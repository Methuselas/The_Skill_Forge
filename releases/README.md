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
| [Agent Kit](skills/agent-kit/) | Coordinating several AI agents in one project | `1.0.0-beta.60` | 80,615 | `114f290318a75edfa512245672275dcc5541a696a1933bca8b5e7ffd3a14d0f0` |
| [Art](skills/art/) | Drawing, painting, comics and illustration craft | `1.0.0-beta.60` | 9,323,867 | `6119d9bb94bae034eb7664b67e57b0dc90dd311f54bc8094e97cc938800ce017` |
| [Game Design](skills/game-design/) | Mechanics, characters, adversaries, adventures, worlds | `1.0.0-beta.60` | 576,527 | `80d414cbd4cd75622f985401849da2b74d1fe99e018f77d8e9df02404370c407` |
| [Software Engineering](skills/software-engineering/) | Design, implementation, review, testing, C++, Unreal | `1.0.0-beta.60` | 2,156,551 | `6e4bfb3ca1d2c450d7f2efed532e95e02884bd3998a062018e677214b01439c5` |
| [Writing](skills/writing/) | Fiction, poetry, nonfiction, essays, career documents | `1.0.0-beta.60` | 993,642 | `16c0bfeaedd8ee3729ae66bebd9c730a69784697d6bc84b55712e4444e5da248` |

## Model tools

Not built by PASS; each carries its own version.

| Tool | What it is for | Version | Size (bytes) | SHA-256 |
|---|---|---|---:|---|
| [Bionic Memory](models/bionic/) | Persistent cross-session memory for AI agents | v2 | 5,732 | `0c954bbfc27b53bdb9af1e7954b03152e30cd0529b3247cbc5ca4a1176d51519` |
