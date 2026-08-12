#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any

import yaml

from paths import default_ledger_root, default_library_root, repo_root_from_tool
from quality_attestation import all_source_object_hashes, verify_attestation

FM_RE = re.compile(r"\A---\r?\n(?P<front>.*?)\r?\n---\r?\n(?P<body>.*)\Z", re.S)
FORBIDDEN = {
    ".git", ".agents", ".claude", "__pycache__", ".pytest_cache",
    "workspace", "sources", "ledger", "ledgers", "worklogs", "trash",
    "tmp", "build", "dist",
}


def read_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected mapping")
    return data


def discover(library: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    result: dict[str, tuple[Path, dict[str, Any]]] = {}
    for path in library.rglob("MODULE.yaml"):
        data = read_yaml(path)
        name = data.get("name")
        if not isinstance(name, str) or not name:
            raise ValueError(f"{path}: module name missing")
        if name in result:
            raise ValueError(f"duplicate module name: {name}")
        expected = path.parent.relative_to(library).as_posix()
        if name != expected:
            raise ValueError(f"{path}: module name/path mismatch: {name} != {expected}")
        result[name] = (path.parent, data)
    return result


def object_index(library: Path, modules: dict[str, tuple[Path, dict[str, Any]]]):
    by_id: dict[str, tuple[Path, dict[str, Any]]] = {}
    owner: dict[str, str] = {}
    module_dirs = sorted(
        ((path, name) for name, (path, _data) in modules.items()),
        key=lambda item: len(item[0].parts),
        reverse=True,
    )
    for path in library.rglob("*.md"):
        raw = path.read_text(encoding="utf-8")
        match = FM_RE.match(raw)
        if not match:
            continue
        data = yaml.safe_load(match.group("front"))
        if not isinstance(data, dict) or not data.get("object_id"):
            continue
        object_id = data["object_id"]
        if object_id in by_id:
            raise ValueError(f"duplicate object_id: {object_id}")
        by_id[object_id] = (path, data)
        for module_dir, name in module_dirs:
            try:
                path.relative_to(module_dir)
                owner[object_id] = name
                break
            except ValueError:
                pass
    return by_id, owner


def resolve(entry, modules, by_id, owner):
    selected: set[str] = set()
    visiting: set[str] = set()

    def add_module(name: str) -> None:
        if name in selected:
            return
        if name in visiting:
            raise ValueError(f"module dependency cycle at {name}")
        if name not in modules:
            raise ValueError(f"missing module: {name}")
        visiting.add(name)
        for required in modules[name][1].get("requires") or []:
            add_module(required)
        visiting.remove(name)
        selected.add(name)

    add_module("metaskills")
    for name in entry:
        add_module(name)

    changed = True
    while changed:
        changed = False
        included_ids = {object_id for object_id, module in owner.items() if module in selected}
        for object_id in list(included_ids):
            data = by_id[object_id][1]
            foundation = data.get("foundation_object_id")
            if foundation and foundation != "none":
                if foundation not in by_id:
                    raise ValueError(f"{object_id}: missing foundation object {foundation}")
                module = owner.get(foundation)
                if not module:
                    raise ValueError(f"{object_id}: foundation object has no module: {foundation}")
                before = len(selected)
                add_module(module)
                changed |= len(selected) != before
        # prerequisite_for points from prerequisite source -> dependent target.
        for source_id, (_path, data) in by_id.items():
            for link in data.get("cross_links") or []:
                if isinstance(link, dict) and link.get("rel") == "prerequisite_for":
                    target = link.get("target_object_id")
                    if target in included_ids:
                        module = owner.get(source_id)
                        if not module:
                            raise ValueError(f"{source_id}: prerequisite has no module")
                        before = len(selected)
                        add_module(module)
                        changed |= len(selected) != before
    return selected


def included_objects(selected: set[str], by_id, owner):
    return {
        object_id: (path, data)
        for object_id, (path, data) in by_id.items()
        if owner.get(object_id) in selected
    }


def source_ids_for(objects) -> set[str]:
    result: set[str] = set()
    for _object_id, (_path, data) in objects.items():
        reference = data.get("reference")
        source_id = reference.get("source_id") if isinstance(reference, dict) else None
        if source_id:
            result.add(str(source_id))
    return result


def run_gate(script: Path, args: list[str]) -> None:
    result = subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True)
    if result.returncode:
        detail = (result.stdout + "\n" + result.stderr).strip()
        raise ValueError(f"quality gate failed ({script.name}):\n{detail}")


def run_quality_gates(library: Path, ledger: Path, selected_sources: set[str]) -> dict[str, Any]:
    tool_dir = Path(__file__).resolve().parent
    run_gate(tool_dir / "validate.py", ["--library", str(library), "--ledger", str(ledger)])
    run_gate(tool_dir / "verify_references.py", ["--library", str(library), "--ledger", str(ledger)])
    problems: list[str] = []
    all_objects = all_source_object_hashes(library)
    for source_id in sorted(selected_sources):
        problems.extend(verify_attestation(source_id, library, ledger, all_objects.get(source_id, {})))
    if problems:
        raise ValueError("quality attestation gate failed:\n" + "\n".join(problems))
    return {
        "schema_validation": "passed",
        "visual_reference_verification": "passed",
        "grounding_attestations": "passed",
        "sources": sorted(selected_sources),
    }


def scan_tree(path: Path) -> list[str]:
    problems: list[str] = []
    for item in path.rglob("*"):
        rel = item.relative_to(path)
        if any(part in FORBIDDEN for part in rel.parts):
            problems.append(f"forbidden path: {rel}")
        if item.is_symlink():
            problems.append(f"symlink: {rel}")
        if item.is_file() and item.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".py", ".txt"}:
            text = item.read_text(encoding="utf-8", errors="ignore")
            if "/mnt/data/" in text or re.search(r"(?m)(?:^|[\s`\"'])\.\./", text):
                problems.append(f"external path reference: {rel}")
            if "SkillForge_Base" in text:
                problems.append(f"factory dependency reference: {rel}")
    return sorted(set(problems))


def asset_problems(path: Path) -> list[str]:
    problems: list[str] = []
    for card in path.rglob("*.md"):
        raw = card.read_text(encoding="utf-8", errors="strict")
        match = FM_RE.match(raw)
        if not match:
            continue
        data = yaml.safe_load(match.group("front"))
        if not isinstance(data, dict):
            continue
        for reference in data.get("references") or []:
            if not isinstance(reference, dict) or not reference.get("image_path"):
                continue
            declared = Path(str(reference["image_path"]))
            if declared.is_absolute() or ".." in declared.parts:
                problems.append(f"{card.relative_to(path)}: unsafe image_path {declared}")
                continue
            if not (path / declared).is_file():
                problems.append(f"{card.relative_to(path)}: missing image_path {declared}")
    return problems


def skill_metadata_problem(path: Path) -> list[str]:
    skill = path / "SKILL.md"
    if not skill.is_file():
        return ["missing SKILL.md"]
    match = FM_RE.match(skill.read_text(encoding="utf-8"))
    if not match:
        return ["SKILL.md lacks YAML frontmatter"]
    data = yaml.safe_load(match.group("front"))
    if not isinstance(data, dict):
        return ["SKILL.md frontmatter is not a mapping"]
    problems = []
    if not isinstance(data.get("name"), str) or not data["name"].strip():
        problems.append("SKILL.md frontmatter missing name")
    if not isinstance(data.get("description"), str) or not data["description"].strip():
        problems.append("SKILL.md frontmatter missing description")
    return problems


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("release name cannot be converted to a skill name")
    return slug


def write_skill(path: Path, skill_name: str, display_name: str, description: str, modules: list[str]) -> None:
    front = yaml.safe_dump(
        {"name": skill_name, "description": description},
        sort_keys=False,
        default_flow_style=False,
    ).strip()
    body = (
        f"# {display_name}\n\n"
        "This is a self-contained SkillForge release. Load `library/metaskills` as the "
        "universal four-stage process baseline, then use only the bundled domain modules "
        "relevant to the task. Hard prerequisites have already been materialized locally. "
        "Source citations are provenance, not runtime dependencies.\n\n"
        "## Bundled modules\n\n"
        + "".join(f"- `library/{module}`\n" for module in modules)
    )
    (path / "SKILL.md").write_text(f"---\n{front}\n---\n\n{body}", encoding="utf-8")


def protected_output(outdir: Path, library: Path, recipe: Path) -> str | None:
    outdir = outdir.resolve()
    library = library.resolve()
    recipe = recipe.resolve()
    repo = library.parent.resolve()
    protected = {
        repo,
        library,
        recipe.parent,
        repo / "PASS",
        repo / "tests",
        repo / "workspace" / "authoring",
        repo / ".git",
    }
    if outdir in protected:
        return f"refusing protected output path: {outdir}"
    # Never allow an output path that contains the repository/library/recipe,
    # or an output nested inside canonical source/authoring areas.
    if repo.is_relative_to(outdir) or library.is_relative_to(outdir) or recipe.is_relative_to(outdir):
        return f"refusing output path that is an ancestor of canonical content: {outdir}"
    if (
        outdir.is_relative_to(library)
        or outdir.is_relative_to(repo / "PASS")
        or outdir.is_relative_to(repo / "workspace" / "authoring")
        or outdir.is_relative_to(recipe.parent)
        or outdir.is_relative_to(repo / ".git")
    ):
        return f"refusing output path inside canonical content: {outdir}"
    return None


def build(
    recipe: Path,
    outdir: Path,
    zip_out: Path | None = None,
    library: Path | None = None,
    ledger: Path | None = None,
    *,
    replace: bool = False,
    unsafe_skip_quality_gates: bool = False,
):
    lib = (library or default_library_root()).resolve()
    led = (ledger or default_ledger_root()).resolve()
    recipe = recipe.resolve(); outdir = outdir.resolve()
    if not lib.is_dir():
        raise ValueError(f"library root not found: {lib}; pass --library")
    if not led.is_dir() and not unsafe_skip_quality_gates:
        raise ValueError(f"ledger root not found: {led}; pass --ledger")
    danger = protected_output(outdir, lib, recipe)
    if danger:
        raise ValueError(danger)
    if outdir.exists() and not replace:
        raise ValueError(f"output already exists: {outdir}; use --replace after checking the path")
    if zip_out:
        zip_out = zip_out.resolve()
        if zip_out == outdir or zip_out.is_relative_to(outdir):
            raise ValueError("zip output must be outside the release directory")
        if zip_out.exists() and not replace:
            raise ValueError(f"zip output already exists: {zip_out}; use --replace after checking the path")

    modules = discover(lib)
    by_id, owner = object_index(lib, modules)
    spec = read_yaml(recipe)
    entries = spec.get("modules") or []
    if not entries:
        raise ValueError("release recipe has no modules")
    selected = resolve(entries, modules, by_id, owner)
    objects = included_objects(selected, by_id, owner)
    selected_sources = source_ids_for(objects)
    quality = (
        {"status": "UNSAFE_SKIPPED"}
        if unsafe_skip_quality_gates
        else run_quality_gates(lib, led, selected_sources)
    )

    display_name = str(spec.get("name") or recipe.stem)
    skill_name = str(spec.get("skill_name") or slugify(display_name))
    description = str(spec.get("description") or f"Use for tasks requiring the {display_name} SkillForge skillset.")

    outdir.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{outdir.name}.build-", dir=outdir.parent))
    try:
        (staging / "library").mkdir(parents=True)
        selected_roots = {modules[name][0].resolve() for name in selected}

        def ignore_nested_modules(current, names):
            cur = Path(current).resolve()
            ignored = []
            for item in names:
                child = (cur / item).resolve()
                if child != cur and child in selected_roots:
                    ignored.append(item)
            return ignored

        # Preserve canonical library-relative paths so card image_path references
        # remain valid in the release without rewriting trained content.
        for name in sorted(selected, key=lambda n: len(modules[n][0].parts)):
            src = modules[name][0]
            dst = staging / "library" / name
            shutil.copytree(src, dst, dirs_exist_ok=True, ignore=ignore_nested_modules)

        manifest = {
            "name": display_name,
            "skill_name": skill_name,
            "description": description,
            "modules": sorted(selected),
            "quality_gates": quality,
        }
        (staging / "RELEASE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        write_skill(staging, skill_name, display_name, description, manifest["modules"])

        problems = scan_tree(staging) + asset_problems(staging) + skill_metadata_problem(staging)
        if problems:
            raise ValueError("release portability check failed:\n" + "\n".join(sorted(set(problems))))

        if outdir.exists():
            # Safe only because protected_output() already rejected canonical paths.
            shutil.rmtree(outdir)
        staging.rename(outdir)
        staging = None  # type: ignore[assignment]

        if zip_out:
            zip_out = zip_out.resolve()
            zip_out.parent.mkdir(parents=True, exist_ok=True)
            if zip_out.exists():
                zip_out.unlink()
            with zipfile.ZipFile(zip_out, "w", zipfile.ZIP_DEFLATED) as archive:
                for path in sorted(outdir.rglob("*")):
                    if path.is_file():
                        archive.write(path, Path(outdir.name) / path.relative_to(outdir))
        return manifest
    finally:
        if staging is not None and staging.exists():
            shutil.rmtree(staging, ignore_errors=True)


def check(path: Path) -> None:
    problems = scan_tree(path) + asset_problems(path) + skill_metadata_problem(path)
    manifest_path = path / "RELEASE_MANIFEST.json"
    if not manifest_path.is_file():
        problems.append("missing RELEASE_MANIFEST.json")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            gates = manifest.get("quality_gates", {})
            if gates.get("status") == "UNSAFE_SKIPPED":
                problems.append("release was built with quality gates skipped")
            else:
                for gate in ("schema_validation", "visual_reference_verification", "grounding_attestations"):
                    if gates.get(gate) != "passed":
                        problems.append(f"release manifest does not record passed {gate}")
        except json.JSONDecodeError:
            problems.append("invalid RELEASE_MANIFEST.json")
    if not (path / "library" / "metaskills" / "MODULE.yaml").is_file():
        problems.append("missing mandatory metaskills")
    if problems:
        raise ValueError("\n".join(sorted(set(problems))))


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    build_parser = sub.add_parser("build")
    build_parser.add_argument("recipe", type=Path)
    build_parser.add_argument("outdir", type=Path)
    build_parser.add_argument("--library", type=Path, default=default_library_root())
    build_parser.add_argument("--ledger", type=Path, default=default_ledger_root())
    build_parser.add_argument("--zip", dest="zip_out", type=Path)
    build_parser.add_argument("--replace", action="store_true", help="replace an existing safe output path")
    build_parser.add_argument(
        "--unsafe-skip-quality-gates",
        action="store_true",
        help="composition-fixture/testing only; the resulting directory fails `check` and must not be published",
    )
    check_parser = sub.add_parser("check")
    check_parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        if args.cmd == "build":
            manifest = build(
                args.recipe, args.outdir, args.zip_out, args.library, args.ledger,
                replace=args.replace,
                unsafe_skip_quality_gates=args.unsafe_skip_quality_gates,
            )
            print(json.dumps(manifest, indent=2))
        else:
            check(args.path.resolve())
            print("PASS: portable Agent Skill release")
    except Exception as exc:  # noqa: BLE001 - CLI must fail closed with context
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
