#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
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

from paths import default_library_root, repo_root_from_tool

FM_RE = re.compile(r"\A---\r?\n(?P<front>.*?)\r?\n---\r?\n(?P<body>.*)\Z", re.S)
FORBIDDEN = {
    ".git", ".agents", ".claude", "__pycache__", ".pytest_cache",
    "workspace", "sources", "ledger", "ledgers", "worklogs", "trash",
    "tmp", "build", "dist",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


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
        required_object_ids: set[str] = set()

        # A materialized release must contain a complete object graph. Follow every
        # outgoing canonical relationship, not only foundations. Otherwise a soft
        # related_to/supports/teaches edge can become a dangling link after export.
        for object_id in list(included_ids):
            data = by_id[object_id][1]
            foundation = data.get("foundation_object_id")
            if foundation and foundation != "none":
                required_object_ids.add(str(foundation))
            for link in data.get("cross_links") or []:
                if isinstance(link, dict) and link.get("target_object_id"):
                    required_object_ids.add(str(link["target_object_id"]))

        # prerequisite_for points from prerequisite source -> dependent target, so
        # include the prerequisite object when its dependent is already selected.
        for source_id, (_path, data) in by_id.items():
            for link in data.get("cross_links") or []:
                if isinstance(link, dict) and link.get("rel") == "prerequisite_for":
                    if link.get("target_object_id") in included_ids:
                        required_object_ids.add(source_id)

        for required_id in sorted(required_object_ids):
            if required_id not in by_id:
                raise ValueError(f"missing related object: {required_id}")
            module = owner.get(required_id)
            if not module:
                raise ValueError(f"{required_id}: related object has no module")
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


def run_gate(script: Path, args: list[str]) -> None:
    result = subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True)
    if result.returncode:
        detail = (result.stdout + "\n" + result.stderr).strip()
        raise ValueError(f"quality gate failed ({script.name}):\n{detail}")


def run_quality_gates(release_library: Path) -> dict[str, Any]:
    """Gate the packaged library on what it contains, not on how it was authored.

    Both gates run against the staged release tree, so a release is publishable
    on the strength of the cards it actually ships.
    """
    tool_dir = Path(__file__).resolve().parent
    run_gate(tool_dir / "validate.py", ["--library", str(release_library)])
    run_gate(tool_dir / "verify_references.py", ["--library", str(release_library)])
    return {
        "schema_validation": "passed",
        "visual_reference_verification": "passed",
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


def release_file_hashes(path: Path) -> dict[str, str]:
    """Hash every shipped file except the manifest that stores the hashes."""
    manifest_path = path / "RELEASE_MANIFEST.json"
    return {
        item.relative_to(path).as_posix(): sha256_file(item)
        for item in sorted(path.rglob("*"))
        if item.is_file() and item != manifest_path
    }


def release_graph_problems(library: Path) -> list[str]:
    """Check that a packaged library contains every relationship target."""
    try:
        modules = discover(library)
        by_id, owner = object_index(library, modules)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [f"invalid packaged library: {exc}"]

    problems: list[str] = []
    for name, (_module_path, data) in modules.items():
        requires = data.get("requires") or []
        if not isinstance(requires, list):
            problems.append(f"module {name}: requires must be a list")
            continue
        for required in requires:
            if required not in modules:
                problems.append(f"module {name}: missing required module {required}")

    known_ids = set(by_id)
    for object_id, (_card_path, data) in by_id.items():
        if object_id not in owner:
            problems.append(f"{object_id}: object has no packaged module")
        foundation = data.get("foundation_object_id")
        if foundation and foundation != "none" and foundation not in known_ids:
            problems.append(f"{object_id}: missing foundation object {foundation}")
        for link in data.get("cross_links") or []:
            if not isinstance(link, dict):
                continue
            target = link.get("target_object_id")
            if target and target not in known_ids:
                problems.append(f"{object_id}: unresolved cross_link target {target}")
    return sorted(set(problems))


def manifest_problems(path: Path, manifest: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    expected_hashes = manifest.get("files_sha256")
    if not isinstance(expected_hashes, dict) or not all(
        isinstance(name, str) and isinstance(digest, str)
        for name, digest in expected_hashes.items()
    ):
        problems.append("release manifest lacks valid files_sha256")
    else:
        actual_hashes = release_file_hashes(path)
        for name in sorted(set(expected_hashes) - set(actual_hashes)):
            problems.append(f"missing release file: {name}")
        for name in sorted(set(actual_hashes) - set(expected_hashes)):
            problems.append(f"unexpected release file: {name}")
        for name in sorted(set(expected_hashes) & set(actual_hashes)):
            if expected_hashes[name] != actual_hashes[name]:
                problems.append(f"changed release file: {name}")

    declared = manifest.get("modules")
    if not isinstance(declared, list) or not all(isinstance(name, str) for name in declared):
        problems.append("release manifest lacks a valid modules list")
    else:
        try:
            actual = set(discover(path / "library"))
        except (OSError, ValueError, yaml.YAMLError) as exc:
            problems.append(f"invalid packaged modules: {exc}")
        else:
            for name in sorted(set(declared) - actual):
                problems.append(f"missing declared module: {name}")
            for name in sorted(actual - set(declared)):
                problems.append(f"undeclared packaged module: {name}")
    return problems


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("release name cannot be converted to a skill name")
    return slug


def write_skill(
    path: Path,
    skill_name: str,
    display_name: str,
    description: str,
    modules: list[str],
    runtime_profile: str,
) -> None:
    front = yaml.safe_dump(
        {"name": skill_name, "description": description},
        sort_keys=False,
        default_flow_style=False,
    ).strip()
    body = (
        f"# {display_name}\n\n"
        "This is a self-contained SkillForge release.\n\n"
        f"`runtime/profile.yaml` (profile `{runtime_profile}`) is this release's "
        "**execution contract**. It declares the execution modes, routing, risk checks, "
        "and completion requirements this skill is expected to honor. Read it and honor "
        "it: resolve the execution mode before productive work, apply the activated "
        "metaskills, perform the risk checks the contract names for the request, and "
        "satisfy the completion requirements before declaring a task complete. That "
        "responsibility is yours — nothing in this package can check it for you.\n\n"
        "`scripts/skillforge_runtime.py` is an **optional deterministic helper** for "
        "hosts that can execute Python. It holds no state, runs only when invoked, and "
        "cannot observe or block anything you do:\n\n"
        "- `doctor` checks that the bundled profile and library are internally consistent.\n"
        "- `resolve --request <user request>` returns the contract for a request as JSON, "
        "so mode and check selection are deterministic instead of re-derived each time.\n"
        "- `verify` audits a completion record you write, and reports which required "
        "checks it does not contain.\n\n"
        "Where Python is unavailable, apply the contract in `runtime/profile.yaml` "
        "directly. The release is complete without it.\n\n"
        "The semantic craft knowledge lives in `library/`. Python resolves and reports; "
        "it does not sequence stages, gate approvals, or enforce the contract. Hard "
        "prerequisites have already been materialized locally. Each card is "
        "self-contained: it needs no source document to execute.\n\n"
        "## Bundled modules\n\n"
        + "".join(f"- `library/{module}`\n" for module in modules)
    )
    (path / "SKILL.md").write_text(f"---\n{front}\n---\n\n{body}", encoding="utf-8")


def runtime_root() -> Path:
    return repo_root_from_tool().resolve() / "PASS" / "runtime"


def vendor_runtime(staging: Path, runtime_profile: str, deployment_profile: str | None) -> None:
    root = runtime_root()
    resolver = root / "skillforge_runtime.py"
    profile = root / "profiles" / f"{runtime_profile}.yaml"
    if not resolver.is_file():
        raise ValueError(f"SkillForge resolver not found: {resolver}")
    if not profile.is_file():
        raise ValueError(f"runtime profile not found: {profile}")
    (staging / "scripts").mkdir(parents=True, exist_ok=True)
    (staging / "runtime").mkdir(parents=True, exist_ok=True)
    shutil.copy2(resolver, staging / "scripts" / "skillforge_runtime.py")
    shutil.copy2(profile, staging / "runtime" / "profile.yaml")
    if deployment_profile:
        source = root / "deployment_profiles" / f"{deployment_profile}.yaml"
        if not source.is_file():
            raise ValueError(f"deployment profile not found: {source}")
        shutil.copy2(source, staging / "runtime" / "deployment_profile.yaml")


def write_zip_from_tree(tree: Path, zip_path: Path, root_name: str) -> None:
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for item in sorted(tree.rglob("*")):
            if item.is_file():
                archive.write(item, Path(root_name) / item.relative_to(tree))


def deployment_size_result(tree: Path, profile_path: Path, root_name: str) -> dict[str, Any]:
    profile = read_yaml(profile_path)
    max_bytes = profile.get("max_package_bytes")
    if not isinstance(max_bytes, int) or max_bytes <= 0:
        raise ValueError(f"{profile_path}: max_package_bytes must be a positive integer")
    warn_at = profile.get("warn_at_bytes")
    if warn_at is not None and (not isinstance(warn_at, int) or warn_at <= 0 or warn_at >= max_bytes):
        raise ValueError(f"{profile_path}: warn_at_bytes must be positive and below max_package_bytes")
    policy = str(profile.get("size_policy") or "hard")
    with tempfile.TemporaryDirectory(prefix="skillforge-size-") as tmp:
        package = Path(tmp) / "release.zip"
        write_zip_from_tree(tree, package, root_name)
        package_bytes = package.stat().st_size
    if package_bytes > max_bytes:
        status = "FAIL" if policy == "hard" else "WARN"
    elif isinstance(warn_at, int) and package_bytes >= warn_at:
        status = "WARN"
    else:
        status = "PASS"
    return {
        "target": str(profile.get("target") or profile_path.stem),
        "status": status,
        "package_bytes": package_bytes,
        "max_package_bytes": max_bytes,
        "size_policy": policy,
    }


def runtime_release_problems(path: Path) -> list[str]:
    resolver = path / "scripts" / "skillforge_runtime.py"
    profile = path / "runtime" / "profile.yaml"
    if not resolver.is_file():
        return ["missing vendored SkillForge resolver"]
    if not profile.is_file():
        return ["missing vendored SkillForge runtime profile"]
    result = subprocess.run(
        [sys.executable, str(resolver), "--profile", str(profile), "--library", str(path / "library"), "doctor"],
        text=True, capture_output=True,
    )
    if result.returncode:
        detail = (result.stdout + "\n" + result.stderr).strip()
        return [f"runtime doctor failed: {detail}"]
    return []


def protected_output(outdir: Path, library: Path, recipe: Path) -> str | None:
    outdir = outdir.resolve()
    library = library.resolve()
    recipe = recipe.resolve()
    repo = repo_root_from_tool().resolve()
    protected = {
        repo,
        library,
        recipe.parent,
    }
    if outdir in protected:
        return f"refusing protected output path: {outdir}"
    # Never allow output inside or above the factory repository. There is no
    # designated in-repo release area, so treating the entire tree as canonical
    # avoids an incomplete allow/deny list becoming a deletion primitive.
    if repo.is_relative_to(outdir) or outdir.is_relative_to(repo):
        return f"refusing output path inside or above the repository: {outdir}"
    # Explicit library/recipe arguments may live outside the factory repo and
    # must receive the same ancestor/descendant protection.
    if library.is_relative_to(outdir) or recipe.is_relative_to(outdir):
        return f"refusing output path that is an ancestor of canonical content: {outdir}"
    if outdir.is_relative_to(library) or outdir.is_relative_to(recipe.parent):
        return f"refusing output path inside canonical content: {outdir}"
    return None


def build(
    recipe: Path,
    outdir: Path,
    zip_out: Path | None = None,
    library: Path | None = None,
    *,
    replace: bool = False,
    unsafe_skip_quality_gates: bool = False,
):
    lib = (library or default_library_root()).resolve()
    recipe = recipe.resolve(); outdir = outdir.resolve()
    if not lib.is_dir():
        raise ValueError(f"library root not found: {lib}; pass --library")
    danger = protected_output(outdir, lib, recipe)
    if danger:
        raise ValueError(danger)
    if outdir.exists() and not replace:
        raise ValueError(f"output already exists: {outdir}; use --replace after checking the path")
    if zip_out:
        zip_out = zip_out.resolve()
        if zip_out.suffix.lower() != ".zip":
            raise ValueError("zip output must use a .zip extension")
        danger = protected_output(zip_out, lib, recipe)
        if danger:
            raise ValueError(danger.replace("output path", "zip output path"))
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
    display_name = str(spec.get("name") or recipe.stem)
    skill_name = str(spec.get("skill_name") or slugify(display_name))
    description = str(spec.get("description") or f"Use for tasks requiring the {display_name} SkillForge skillset.")
    runtime_profile = str(spec.get("runtime_profile") or "generic")
    deployment_profile = spec.get("deployment_profile")
    if deployment_profile is not None:
        deployment_profile = str(deployment_profile)

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

        vendor_runtime(staging, runtime_profile, deployment_profile)

        quality = (
            {"status": "UNSAFE_SKIPPED"}
            if unsafe_skip_quality_gates
            else run_quality_gates(staging / "library")
        )

        manifest = {
            "schema_version": 1,
            "name": display_name,
            "skill_name": skill_name,
            "description": description,
            "modules": sorted(selected),
            "runtime_profile": runtime_profile,
            "deployment_profile": deployment_profile,
            "quality_gates": quality,
        }
        write_skill(staging, skill_name, display_name, description, manifest["modules"], runtime_profile)
        manifest["files_sha256"] = release_file_hashes(staging)
        (staging / "RELEASE_MANIFEST.json").write_text(
            json.dumps(manifest, indent=2) + "\n",
            encoding="utf-8",
        )

        problems = (
            scan_tree(staging)
            + asset_problems(staging)
            + skill_metadata_problem(staging)
            + release_graph_problems(staging / "library")
            + manifest_problems(staging, manifest)
            + runtime_release_problems(staging)
        )
        if problems:
            raise ValueError("release portability check failed:\n" + "\n".join(sorted(set(problems))))

        size_result = None
        deployment_file = staging / "runtime" / "deployment_profile.yaml"
        if deployment_file.is_file():
            size_result = deployment_size_result(staging, deployment_file, outdir.name)
            if size_result["status"] == "FAIL":
                raise ValueError(
                    "deployment package size gate failed: "
                    f"{size_result['package_bytes']} > {size_result['max_package_bytes']} bytes "
                    f"for target {size_result['target']}"
                )

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
            write_zip_from_tree(outdir, zip_out, outdir.name)
        result_manifest = dict(manifest)
        if size_result is not None:
            result_manifest["deployment_size"] = size_result
        return result_manifest
    finally:
        if staging is not None and staging.exists():
            shutil.rmtree(staging, ignore_errors=True)


def check(path: Path) -> None:
    problems = (
        scan_tree(path)
        + asset_problems(path)
        + skill_metadata_problem(path)
        + release_graph_problems(path / "library")
        + runtime_release_problems(path)
    )
    manifest_path = path / "RELEASE_MANIFEST.json"
    if not manifest_path.is_file():
        problems.append("missing RELEASE_MANIFEST.json")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if not isinstance(manifest, dict):
                raise ValueError("release manifest is not a JSON object")
            problems.extend(manifest_problems(path, manifest))
            gates = manifest.get("quality_gates", {})
            if gates.get("status") == "UNSAFE_SKIPPED":
                problems.append("release was built with quality gates skipped")
            else:
                for gate in ("schema_validation", "visual_reference_verification"):
                    if gates.get(gate) != "passed":
                        problems.append(f"release manifest does not record passed {gate}")
        except (json.JSONDecodeError, ValueError) as exc:
            problems.append(f"invalid RELEASE_MANIFEST.json: {exc}")
    if not (path / "library" / "metaskills" / "MODULE.yaml").is_file():
        problems.append("missing mandatory metaskills")
    deployment_file = path / "runtime" / "deployment_profile.yaml"
    if deployment_file.is_file():
        try:
            size = deployment_size_result(path, deployment_file, path.name)
            if size["status"] == "FAIL":
                problems.append(
                    f"deployment package exceeds {size['target']} limit: "
                    f"{size['package_bytes']} > {size['max_package_bytes']} bytes"
                )
        except (OSError, ValueError, yaml.YAMLError) as exc:
            problems.append(f"invalid deployment profile: {exc}")
    if problems:
        raise ValueError("\n".join(sorted(set(problems))))


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    build_parser = sub.add_parser("build")
    build_parser.add_argument("recipe", type=Path)
    build_parser.add_argument("outdir", type=Path)
    build_parser.add_argument("--library", type=Path, default=default_library_root())
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
                args.recipe, args.outdir, args.zip_out, args.library,
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
