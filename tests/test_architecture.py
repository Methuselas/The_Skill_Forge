"""Architecture tests for the simplified PASS / SkillForge system.

These encode the invariants the 2026-08-15 cleanup restored: a finished skill
library is valid on its own, each domain stands alone, and nothing here needs a
source PDF, an authoring ledger, a workspace, or a provenance receipt.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "library"
BUILDER = ROOT / "PASS/tools/build_release.py"
VALIDATOR = ROOT / "PASS/tools/validate.py"
RECIPES = ROOT / "workspace/release-recipes"
DOMAINS = ("art", "writing", "software-engineering")
RETIRED_STATE = ("workspace", "sources", "ledger", "provenance", "renders", "tmp")


def run(*args: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(BUILDER), *map(str, args)],
        text=True, capture_output=True, cwd=ROOT,
    )


def validate(*args: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), *map(str, args)],
        text=True, capture_output=True, cwd=ROOT,
    )


def cards(library: Path) -> list[Path]:
    return [
        path for path in library.rglob("*.md")
        if path.name not in {"README.md", "INDEX.md"}
    ]


def frontmatter(card: Path) -> dict:
    raw = card.read_text(encoding="utf-8")
    return yaml.safe_load(raw.split("---\n", 2)[1])


def isolated_library() -> tempfile.TemporaryDirectory:
    """A checkout containing the library and tools and nothing else.

    Everything the retired architecture used to require — source payloads, the
    authoring ledger, workspace state, provenance receipts — is simply absent.
    """
    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name)
    shutil.copytree(LIBRARY, root / "library")
    shutil.copytree(ROOT / "PASS", root / "PASS", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(RECIPES, root / "recipes")
    return tmp


class SourceAndStateIndependenceTests(unittest.TestCase):
    """1-3, 12: the library is valid with no research state of any kind."""

    def test_library_validates_with_no_sources_ledger_or_workspace(self) -> None:
        with isolated_library() as tmp:
            root = Path(tmp)
            for name in RETIRED_STATE:
                self.assertFalse((root / name).exists(), f"{name} leaked into a clean checkout")
            result = subprocess.run(
                [sys.executable, str(root / "PASS/tools/validate.py"), "--library", str(root / "library")],
                text=True, capture_output=True, cwd=root,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("PASS:", result.stdout)

    def test_release_builds_with_no_sources_ledger_or_workspace(self) -> None:
        # The builder refuses to write inside its own checkout, so the release
        # lands in a separate directory outside the isolated tree.
        with isolated_library() as tmp, tempfile.TemporaryDirectory() as dest:
            root = Path(tmp)
            out = Path(dest) / "release"
            result = subprocess.run(
                [
                    sys.executable, str(root / "PASS/tools/build_release.py"), "build",
                    str(root / "recipes/CPP_Development.yaml"), str(out),
                    "--library", str(root / "library"),
                ],
                text=True, capture_output=True, cwd=root,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            gates = json.loads((out / "RELEASE_MANIFEST.json").read_text(encoding="utf-8"))["quality_gates"]
            self.assertEqual(gates["schema_validation"], "passed")
            self.assertEqual(gates["visual_reference_verification"], "passed")

    def test_deleting_temporary_research_state_does_not_change_validity(self) -> None:
        before = validate("--library", str(LIBRARY))
        with isolated_library() as tmp:
            root = Path(tmp)
            after = subprocess.run(
                [sys.executable, str(root / "PASS/tools/validate.py"), "--library", str(root / "library")],
                text=True, capture_output=True, cwd=root,
            )
        self.assertEqual(before.returncode, 0, before.stdout)
        self.assertEqual(before.stdout.strip(), after.stdout.strip())


class DomainIndependenceTests(unittest.TestCase):
    """4-7, 10: each domain validates, builds, and links on its own."""

    def test_each_domain_validates_independently(self) -> None:
        for domain in DOMAINS:
            with self.subTest(domain=domain):
                result = validate("--library", str(LIBRARY), "--package", domain)
                self.assertEqual(result.returncode, 0, result.stdout)

    def test_no_card_depends_on_another_domain(self) -> None:
        owner = {}
        for card in cards(LIBRARY):
            data = frontmatter(card)
            if data.get("object_id"):
                owner[data["object_id"]] = card.relative_to(LIBRARY).parts[0]
        for card in cards(LIBRARY):
            data = frontmatter(card)
            if not data.get("object_id"):
                continue
            package = card.relative_to(LIBRARY).parts[0]
            targets = [link["target_object_id"] for link in data.get("cross_links") or []]
            foundation = data.get("foundation_object_id")
            if foundation and foundation != "none":
                targets.append(foundation)
            for target in targets:
                # `metaskills` is a shared foundation every release bundles, not a
                # peer domain. Any other cross-package edge couples two lanes.
                self.assertIn(
                    owner.get(target), {package, "metaskills"},
                    f"{data['object_id']} ({package}) depends on {target} ({owner.get(target)})",
                )

    def test_domain_release_excludes_unrelated_domains(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "release"
            self.assertEqual(run("build", RECIPES / "CPP_Development.yaml", out).returncode, 0)
            modules = json.loads((out / "RELEASE_MANIFEST.json").read_text(encoding="utf-8"))["modules"]
            self.assertIn("software-engineering/languages/cpp", modules)
            for foreign in ("art", "writing", "teaching"):
                self.assertFalse(
                    any(name == foreign or name.startswith(f"{foreign}/") for name in modules),
                    f"C++ release pulled in {foreign}",
                )

    def test_teaching_is_not_required_by_any_domain(self) -> None:
        self.assertFalse((LIBRARY / "teaching").exists(), "teaching is quarantined out of library/")
        for recipe in sorted(RECIPES.glob("*.yaml")):
            modules = yaml.safe_load(recipe.read_text(encoding="utf-8"))["modules"]
            with self.subTest(recipe=recipe.name):
                self.assertFalse(any(str(name).startswith("teaching") for name in modules))
        for domain in DOMAINS:
            with self.subTest(domain=domain):
                self.assertEqual(validate("--library", str(LIBRARY), "--package", domain).returncode, 0)


class CardContractTests(unittest.TestCase):
    """8, 9: identity and variants hold without any source record."""

    def test_card_ids_are_globally_unique(self) -> None:
        seen: dict[str, Path] = {}
        for card in cards(LIBRARY):
            data = frontmatter(card)
            object_id = data.get("object_id")
            if not object_id:
                continue
            self.assertNotIn(object_id, seen, f"{object_id} duplicated in {card} and {seen.get(object_id)}")
            seen[object_id] = card
        self.assertGreater(len(seen), 0)

    def test_variants_resolve_to_their_owner_card(self) -> None:
        found = 0
        for card in cards(LIBRARY):
            data = frontmatter(card)
            notes = card.read_text(encoding="utf-8").split("## Notes", 1)[-1]
            for variant in data.get("variants") or []:
                found += 1
                # A variant is executable through the card it lives in: no source,
                # no locator, no owner in another domain.
                self.assertEqual(set(variant), {
                    "variant_id", "variant_name", "variant_basis",
                    "difference_from_foundation", "when_to_use", "when_not_to_use",
                    "absorbed_from_object_id",
                }, f"{card}: variant carries retired fields")
                self.assertIn(variant["variant_id"], notes)
        self.assertGreater(found, 0, "corpus has no variants to check")

    def test_no_card_carries_retired_source_provenance(self) -> None:
        retired = {"source_id", "locator", "page", "page_range", "source_hash", "evidence_type"}
        for card in cards(LIBRARY):
            data = frontmatter(card)
            with self.subTest(card=card.name):
                self.assertFalse(retired & set(data), f"{card}: retired root key")
                reference = data.get("reference")
                if reference is not None:
                    self.assertTrue(
                        set(reference) <= {"source_title", "author"},
                        f"{card}: reference carries retired provenance fields",
                    )


class ReleaseIntegrityTests(unittest.TestCase):
    """11: releases package knowledge; the remaining gates are real."""

    def test_every_recipe_builds_and_checks(self) -> None:
        for recipe in sorted(RECIPES.glob("*.yaml")):
            with self.subTest(recipe=recipe.name), tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp) / "release"
                result = run("build", recipe, out)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue((out / "library/metaskills/MODULE.yaml").is_file())
                front = yaml.safe_load((out / "SKILL.md").read_text(encoding="utf-8").split("---\n", 2)[1])
                self.assertTrue(front.get("name") and front.get("description"))
                self.assertEqual(run("check", out).returncode, 0)

    def test_release_check_detects_a_changed_card(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "release"
            self.assertEqual(run("build", RECIPES / "CPP_Development.yaml", out).returncode, 0)
            card = next((out / "library/software-engineering/languages/cpp").rglob("PAT_*.md"))
            card.write_text(card.read_text(encoding="utf-8") + "\nmutation\n", encoding="utf-8")
            check = run("check", out)
            self.assertNotEqual(check.returncode, 0)
            self.assertIn("changed release file", check.stderr)

    def test_release_check_detects_a_missing_declared_asset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "release"
            self.assertEqual(run("build", RECIPES / "Animal_Anatomy.yaml", out).returncode, 0)
            next(out.rglob("precedent_stage1_observatory_hybrid_construction.png")).unlink()
            check = run("check", out)
            self.assertNotEqual(check.returncode, 0)
            self.assertIn("missing image_path", check.stderr)

    def test_release_check_detects_a_deleted_module(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "release"
            self.assertEqual(run("build", RECIPES / "CPP_Development.yaml", out).returncode, 0)
            shutil.rmtree(out / "library/software-engineering/languages/cpp")
            check = run("check", out)
            self.assertNotEqual(check.returncode, 0)
            self.assertIn("missing declared module", check.stderr)

    def test_missing_module_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            recipe = Path(tmp) / "bad.yaml"
            recipe.write_text("name: bad\nmodules: [does/not/exist]\n", encoding="utf-8")
            self.assertNotEqual(run("build", recipe, Path(tmp) / "out").returncode, 0)

    def test_output_refuses_the_repository(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            zip_out = ROOT / "library/do-not-overwrite.zip"
            result = run("build", RECIPES / "CPP_Development.yaml", Path(tmp) / "release", "--zip", zip_out)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("zip output path inside or above the repository", result.stderr)
            self.assertFalse(zip_out.exists())
            self.assertNotEqual(run("build", RECIPES / "CPP_Development.yaml", ROOT / "sub").returncode, 0)


class ValidatorScopeTests(unittest.TestCase):
    """The validator checks cards, and refuses to grow research-history checks."""

    def test_validator_rejects_a_cross_domain_dependency(self) -> None:
        with isolated_library() as tmp:
            root = Path(tmp)
            # Point a Writing card at a C++ card: a coupling the validator must catch.
            card = next((root / "library/writing").rglob("PAT_*.md"))
            _, front, body = card.read_text(encoding="utf-8").split("---\n", 2)
            data = yaml.safe_load(front)
            data["cross_links"] = [
                {"rel": "related_to", "target_object_id": "PAT_wrap_virtuals_with_nvi_idiom"}
            ]
            card.write_text(
                "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n" + body,
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(root / "PASS/tools/validate.py"), "--library", str(root / "library")],
                text=True, capture_output=True, cwd=root,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("rule 26", result.stdout)

    def test_validator_takes_no_ledger_or_provenance_arguments(self) -> None:
        result = validate("--help")
        self.assertEqual(result.returncode, 0)
        for retired in ("--ledger", "--provenance", "--scope-ledger-to-library"):
            self.assertNotIn(retired, result.stdout)

    def test_indexes_are_generated_and_current(self) -> None:
        # Indexes are derived navigation. A stale one silently hides cards from
        # any agent that follows a skill's documented load order.
        result = subprocess.run(
            [sys.executable, str(ROOT / "PASS/tools/build_index.py"), "--check"],
            text=True, capture_output=True, cwd=ROOT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_every_index_lists_the_cards_beside_it(self) -> None:
        for index in sorted(LIBRARY.rglob("INDEX.md")):
            listed = set(re.findall(r"\(((?:PAT|DRILL|AP)_[a-z0-9_]+\.md)\)", index.read_text(encoding="utf-8")))
            beside = {p.name for p in index.parent.glob("*.md") if p.name not in {"INDEX.md", "README.md"}}
            with self.subTest(index=index.relative_to(LIBRARY).as_posix()):
                self.assertEqual(beside - listed, set(), "cards missing from their own index")

    def test_no_tool_imports_retired_provenance_modules(self) -> None:
        retired = ("provenance", "quality_attestation", "source_provenance", "stage_source", "verify_grounding")
        for tool in sorted((ROOT / "PASS/tools").glob("*.py")):
            text = tool.read_text(encoding="utf-8")
            for name in retired:
                with self.subTest(tool=tool.name, module=name):
                    self.assertNotIn(f"import {name}", text)
                    self.assertNotIn(f"from {name}", text)


class RepositoryShapeTests(unittest.TestCase):
    def test_repo_agent_skill_discovery_folders_are_present(self) -> None:
        for folder in (".claude/skills", ".agents/skills"):
            self.assertTrue((ROOT / folder).is_dir(), folder)

    def test_pass_dependency_manifest_exists(self) -> None:
        self.assertTrue((ROOT / "PASS/requirements.txt").is_file())

    def test_agent_instruction_files_carry_the_same_hard_rules(self) -> None:
        # CLAUDE.md and AGENTS.md state the same contract for different agents.
        # Two copies drift, so every load-bearing rule must appear in both.
        required = {
            "source independence": ("source is gone", "source_id"),
            "one domain per run": ("one domain",),
            "shared metaskills only": ("metaskills",),
            "no rebuilding retired state": ("ledger", "provenance", "attestation"),
            "archive is inert": ("archive/",),
            "art stages frozen": ("Art Stages", "staged-drawing", "Stages"),
        }
        for name in ("CLAUDE.md", "AGENTS.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            for rule, needles in required.items():
                with self.subTest(file=name, rule=rule):
                    self.assertTrue(
                        any(needle.lower() in text.lower() for needle in needles),
                        f"{name} does not state the '{rule}' rule",
                    )

    def test_retired_authoring_infrastructure_is_gone(self) -> None:
        for path in (
            "PASS/tools/provenance.py",
            "PASS/tools/source_provenance.py",
            "PASS/tools/quality_attestation.py",
            "PASS/tools/publish_provenance.py",
            "PASS/tools/stage_source.py",
            "PASS/tools/verify_grounding.py",
            "PASS/tools/preflight_pdf.py",
            "PASS/tools/render_pdf.py",
            "PASS/tools/cleanup_authoring_cache.py",
            "PASS/docs/PASS_LEDGER.md",
            "PASS/docs/PASS_GROUNDING.md",
            "PASS/templates/SOURCE_TEMPLATE.md",
            "PASS/templates/UNITS_TEMPLATE.md",
            "PASS/templates/UNIT_LEDGER_TEMPLATE.md",
            "workspace/provenance",
        ):
            with self.subTest(path=path):
                self.assertFalse((ROOT / path).exists(), f"{path} survived the cleanup")


if __name__ == "__main__":
    unittest.main()
