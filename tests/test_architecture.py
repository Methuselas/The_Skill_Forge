from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "PASS/tools/build_release.py"
TOOLS = ROOT / "PASS/tools"
sys.path.insert(0, str(TOOLS))
from quality_attestation import all_source_object_hashes, verify_attestation  # noqa: E402


def run(*args: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(BUILDER), *map(str, args)],
        text=True,
        capture_output=True,
        cwd=ROOT,
    )


class SkillForgeArchitectureTests(unittest.TestCase):
    def test_named_release_composition_and_agent_skill_metadata(self) -> None:
        for recipe in sorted((ROOT / "workspace/release-recipes").glob("*.yaml")):
            with self.subTest(recipe=recipe.name), tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp) / "release"
                result = run("build", recipe, out, "--unsafe-skip-quality-gates")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue((out / "library/metaskills/MODULE.yaml").is_file())
                skill = (out / "SKILL.md").read_text(encoding="utf-8")
                self.assertTrue(skill.startswith("---\n"))
                front = yaml.safe_load(skill.split("---\n", 2)[1])
                self.assertTrue(front.get("name"))
                self.assertTrue(front.get("description"))

    def test_real_release_runs_all_quality_gates_and_resolves_assets(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "release"
            result = run("build", ROOT / "workspace/release-recipes/Animal_Anatomy.yaml", out)
            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = json.loads((out / "RELEASE_MANIFEST.json").read_text(encoding="utf-8"))
            gates = manifest["quality_gates"]
            self.assertEqual(gates["schema_validation"], "passed")
            self.assertEqual(gates["visual_reference_verification"], "passed")
            self.assertEqual(gates["grounding_attestations"], "passed")
            self.assertEqual(run("check", out).returncode, 0)

    def test_cpp_excludes_art(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "release"
            result = run(
                "build", ROOT / "workspace/release-recipes/CPP_Development.yaml", out,
                "--unsafe-skip-quality-gates",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = json.loads((out / "RELEASE_MANIFEST.json").read_text(encoding="utf-8"))
            self.assertIn("software-engineering/core", manifest["modules"])
            self.assertFalse(any(name.startswith("art/") for name in manifest["modules"]))

    def test_missing_module_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            recipe = Path(tmp) / "bad.yaml"
            recipe.write_text("name: bad\nmodules: [does/not/exist]\n", encoding="utf-8")
            result = run("build", recipe, Path(tmp) / "out", "--unsafe-skip-quality-gates")
            self.assertNotEqual(result.returncode, 0)

    def test_release_check_detects_missing_declared_asset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "release"
            result = run(
                "build", ROOT / "workspace/release-recipes/Animal_Anatomy.yaml", out,
                "--unsafe-skip-quality-gates",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            declared = next(out.rglob("precedent_stage1_observatory_hybrid_construction.png"))
            declared.unlink()
            check = run("check", out)
            self.assertNotEqual(check.returncode, 0)
            self.assertIn("missing image_path", check.stderr)

    def test_changed_card_invalidates_grounding_attestation(self) -> None:
        library = ROOT / "library"
        ledger = ROOT / "workspace/authoring/ledger"
        all_objects = all_source_object_hashes(library)
        source_id = "effective_cpp_3e"
        current = dict(all_objects[source_id])
        self.assertEqual(verify_attestation(source_id, library, ledger, current), [])
        card = next(iter(current))
        current[card] = "0" * 64
        failures = verify_attestation(source_id, library, ledger, current)
        self.assertTrue(any("changed after attestation" in failure for failure in failures))

    def test_replace_refuses_repository_root(self) -> None:
        result = run(
            "build", ROOT / "workspace/release-recipes/Animal_Anatomy.yaml", ROOT,
            "--replace", "--unsafe-skip-quality-gates",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("protected output path", result.stderr)
        self.assertTrue((ROOT / ".git").is_dir())

    def test_repo_agent_skill_discovery_folders_are_present(self) -> None:
        for host in (".agents", ".claude"):
            for skill in ("pass-authoring", "software-engineering", "visual-art"):
                path = ROOT / host / "skills" / skill / "SKILL.md"
                self.assertTrue(path.is_file(), path)
                front = yaml.safe_load(path.read_text(encoding="utf-8").split("---\n", 2)[1])
                self.assertEqual(front.get("name"), skill)
                self.assertTrue(front.get("description"))

    def test_pass_dependency_manifest_exists(self) -> None:
        requirements = (ROOT / "PASS/requirements.txt").read_text(encoding="utf-8")
        for dependency in ("PyYAML", "Pillow", "pypdfium2"):
            self.assertIn(dependency, requirements)


if __name__ == "__main__":
    unittest.main()
