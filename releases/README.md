# SkillForge Releases

Each release records the PASS factory version it was built from as
`pass_version`; these skillsets do not yet carry independent product versions.
Each release passed the PASS version-contract, schema, reference, asset,
portability, memory, and release-integrity checks before its ZIP was written.

| Release | PASS build | Size | SHA-256 |
|---|---|---:|---|
| [SkillForge Art](SkillForge-Art.zip) | `1.0.0-beta.6`, [`60b60ae`](https://github.com/Methuselas/PASS/commit/60b60ae), 2026-09-11 | 25,072,603 bytes | `4481447147ec96ef0a81140bcdb5f7c927b34bb3103c8620cec0fc5ff93a7c32` |
| [SkillForge Game Design](SkillForge-Game-Design.zip) | `1.0.0-beta.6`, [`60b60ae`](https://github.com/Methuselas/PASS/commit/60b60ae), 2026-09-11 | 570,040 bytes | `86524da0931e6ccdce1ded75cf68df448fab3618b1cadca37ff340bf1209876` |
| [SkillForge Software Engineering](SkillForge-Software-Engineering.zip) | `1.0.0-beta.19`, [`6bee6b3`](https://github.com/Methuselas/PASS/commit/6bee6b3), 2026-09-13 | 1,965,536 bytes | `e29d6e53d8d1831aed0aca5ac87a29648d8a875959a73dcda95b22cc449046ed` |
| [SkillForge Writing](SkillForge-Writing.zip) | `1.0.0-beta.6`, [`60b60ae`](https://github.com/Methuselas/PASS/commit/60b60ae), 2026-09-11 | 986,269 bytes | `4005eb0333c7d56bc0ec2e96406def3fe6337ca572712b57aba5107bf6b749d9` |

Install or upload a ZIP as one skill. To inspect it manually, extract it and
begin with the root `SKILL.md` inside the archive.

These files are generated products. Make changes in PASS, rebuild, verify, and
replace the corresponding ZIP rather than editing an extracted release here.
