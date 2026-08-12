from __future__ import annotations

from pathlib import Path


def _first_existing(candidates: list[Path], kind: str) -> Path:
    for path in candidates:
        if path.exists():
            return path
    # Return the most conventional candidate so argparse help/errors stay useful.
    return candidates[0]


def repo_root_from_tool() -> Path:
    """Return the repository root when PASS lives at <repo>/PASS/tools.

    This is only a convenience default. PASS remains portable: callers can always
    supply explicit --library/--ledger paths when it is used outside SkillForge.
    """
    return Path(__file__).resolve().parents[2]


def default_library_root() -> Path:
    cwd = Path.cwd()
    repo = repo_root_from_tool()
    return _first_existing(
        [cwd / "library", repo / "library"],
        "library",
    )


def default_ledger_root() -> Path:
    cwd = Path.cwd()
    repo = repo_root_from_tool()
    return _first_existing(
        [
            cwd / "workspace" / "authoring" / "ledger",
            cwd / "ledger",
            repo / "workspace" / "authoring" / "ledger",
            repo / "ledger",
        ],
        "ledger",
    )
