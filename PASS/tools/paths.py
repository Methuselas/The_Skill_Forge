from __future__ import annotations

from pathlib import Path


def repo_root_from_tool() -> Path:
    """Return the repository root when PASS lives at <repo>/PASS/tools.

    This is only a convenience default. PASS remains portable: callers can always
    supply an explicit --library path when it is used outside SkillForge.
    """
    return Path(__file__).resolve().parents[2]


def default_library_root() -> Path:
    cwd = Path.cwd()
    for candidate in (cwd / "library", repo_root_from_tool() / "library"):
        if candidate.exists():
            return candidate
    # Return the most conventional candidate so argparse help/errors stay useful.
    return cwd / "library"


def default_memory_root() -> Path:
    """Return the memory tree root, mirroring default_library_root().

    Memory is domain-scoped empirical state that sits beside the library rather
    than inside it: the library holds canon, and the validator that reads it is
    documented to read nothing else.
    """
    cwd = Path.cwd()
    for candidate in (cwd / "memory", repo_root_from_tool() / "memory"):
        if candidate.exists():
            return candidate
    return cwd / "memory"
