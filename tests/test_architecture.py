from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "workspace/authoring/ledger"
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
            self.assertTrue(manifest["files_sha256"])
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
            self.assertFalse(any(name == "teaching" or name.startswith("teaching/") for name in manifest["modules"]))

    def test_teaching_capable_release_opts_in_explicitly(self) -> None:
        recipe = yaml.safe_load(
            (ROOT / "workspace/release-recipes/Dynamic_Figure_Drawing.yaml").read_text(encoding="utf-8")
        )
        self.assertIn("teaching", recipe["modules"])

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

    def test_release_check_detects_changed_card(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "release"
            result = run(
                "build", ROOT / "workspace/release-recipes/CPP_Development.yaml", out,
                "--unsafe-skip-quality-gates",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            card = next((out / "library/software-engineering/languages/cpp").rglob("PAT_*.md"))
            card.write_text(card.read_text(encoding="utf-8") + "\nmutation\n", encoding="utf-8")
            check = run("check", out)
            self.assertNotEqual(check.returncode, 0)
            self.assertIn("changed release file", check.stderr)

    def test_release_check_detects_deleted_module(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "release"
            result = run(
                "build", ROOT / "workspace/release-recipes/CPP_Development.yaml", out,
                "--unsafe-skip-quality-gates",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            shutil.rmtree(out / "library/software-engineering/languages/cpp")
            check = run("check", out)
            self.assertNotEqual(check.returncode, 0)
            self.assertIn("missing declared module", check.stderr)

    def test_zip_output_refuses_canonical_library(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            zip_out = ROOT / "library/do-not-overwrite.zip"
            result = run(
                "build", ROOT / "workspace/release-recipes/CPP_Development.yaml",
                Path(tmp) / "release", "--zip", zip_out,
                "--unsafe-skip-quality-gates",
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("zip output path inside or above the repository", result.stderr)
            self.assertFalse(zip_out.exists())

    def test_cpp_quality_gates_ignore_invalid_unrelated_art(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            copied_library = Path(tmp) / "library"
            shutil.copytree(ROOT / "library", copied_library)
            art_card = next((copied_library / "art").rglob("PAT_*.md"))
            text = art_card.read_text(encoding="utf-8")
            art_card.write_text(text.replace("confidence: high", "confidence: invalid", 1), encoding="utf-8")
            out = Path(tmp) / "release"
            result = run(
                "build", ROOT / "workspace/release-recipes/CPP_Development.yaml", out,
                "--library", copied_library,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(run("check", out).returncode, 0)

    def test_public_checkout_validates_without_the_ledger(self) -> None:
        """The ledger is private; a public checkout must still validate itself.

        Library checks are answered from workspace/provenance/<source_id>.json
        instead of the ledger. Only software-engineering and metaskills are
        exercised, because those are the packages whose sources are fully attested.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "library", root / "library")
            shutil.copytree(ROOT / "workspace/provenance", root / "workspace/provenance")
            for package in ("art", "writing", "teaching"):
                shutil.rmtree(root / "library" / package, ignore_errors=True)
            self.assertFalse((root / "workspace/authoring/ledger").exists())
            result = subprocess.run(
                [
                    sys.executable, str(TOOLS / "validate.py"),
                    "--library", str(root / "library"),
                    "--ledger", str(root / "workspace/authoring/ledger"),
                    "--provenance", str(root / "workspace/provenance"),
                ],
                text=True, capture_output=True, cwd=ROOT,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_public_validation_refuses_a_source_with_no_receipt(self) -> None:
        """Fail-closed still holds publicly: no receipt means no verification."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "library", root / "library")
            shutil.copytree(ROOT / "workspace/provenance", root / "workspace/provenance")
            for package in ("art", "writing", "teaching"):
                shutil.rmtree(root / "library" / package, ignore_errors=True)
            (root / "workspace/provenance/code_complete_2e.json").unlink()
            result = subprocess.run(
                [
                    sys.executable, str(TOOLS / "validate.py"),
                    "--library", str(root / "library"),
                    "--ledger", str(root / "workspace/authoring/ledger"),
                    "--provenance", str(root / "workspace/provenance"),
                ],
                text=True, capture_output=True, cwd=ROOT,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("rule 13", result.stdout)

    def test_published_provenance_receipts_are_current(self) -> None:
        """A stale receipt would publish a claim the ledger no longer supports."""
        result = subprocess.run(
            [sys.executable, str(TOOLS / "publish_provenance.py"), "--all", "--check"],
            text=True, capture_output=True, cwd=ROOT,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_release_still_fails_when_a_shipped_card_drifts(self) -> None:
        """Scoping the attestation gate to shipped cards must not disarm it.

        The counterpart to test_cpp_quality_gates_ignore_invalid_unrelated_art:
        corrupting a card the C++ release *does* contain has to fail the build.
        """
        with tempfile.TemporaryDirectory() as tmp:
            copied_library = Path(tmp) / "library"
            shutil.copytree(ROOT / "library", copied_library)
            shipped = copied_library / "software-engineering/languages/cpp"
            card = next(path for path in sorted(shipped.rglob("PAT_*.md")))
            text = card.read_text(encoding="utf-8")
            self.assertIn("## Notes", text)
            card.write_text(text + "\n\nDrifted after attestation.\n", encoding="utf-8")
            result = run(
                "build", ROOT / "workspace/release-recipes/CPP_Development.yaml",
                Path(tmp) / "release", "--library", copied_library,
            )
            self.assertNotEqual(result.returncode, 0, "drifted shipped card must fail the gate")
            self.assertIn("changed after attestation", result.stdout + result.stderr)

    def test_metaskill_from_another_domain_does_not_couple_releases(self) -> None:
        """A universally-included metaskill cites its origin source; that citation
        must not drag the origin's unrelated cards into an unrelated release."""
        library = ROOT / "library"
        metaskill_sources = {
            source_id
            for source_id, cards in all_source_object_hashes(library).items()
            if any(path.startswith("metaskills/") for path in cards)
        }
        self.assertTrue(metaskill_sources, "expected metaskills to carry provenance")
        for source_id in metaskill_sources:
            cards = all_source_object_hashes(library)[source_id]
            shipped = {path for path in cards if path.startswith("metaskills/")}
            drifted = dict(cards)
            for path in cards:
                if path not in shipped:
                    drifted[path] = "0" * 64
            self.assertEqual(
                verify_attestation(source_id, library, LEDGER, drifted, scope_paths=shipped),
                [],
                f"{source_id}: non-shipped card drift must not fail a metaskill-only release",
            )

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

    def test_release_output_refuses_any_repository_subdirectory(self) -> None:
        target = ROOT / "do-not-create-release"
        result = run(
            "build", ROOT / "workspace/release-recipes/CPP_Development.yaml", target,
            "--unsafe-skip-quality-gates",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("inside or above the repository", result.stderr)
        self.assertFalse(target.exists())

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
