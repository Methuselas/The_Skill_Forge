"""Deterministic contracts for Skillset Memory.

The two that matter most, and the reason this suite exists:

    an invalid run never counts as evidence about a capability
    a write is not persisted until the target is reopened and confirmed

Everything else here guards a boundary that was expensive to learn: memory does
not become canon by being copied into it, temporary state does not become
memory, authoring actions are not training events, and an entry that defers its
content to a conversation is not portable.

What this suite cannot prove is listed in tests/README.md: nothing here touches a
live host, so it cannot show that memory was actually consulted during a real
task. It can only show that the tooling reports honestly what it retrieved.
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
MEMORY = ROOT / "memory"
LIBRARY = ROOT / "library"
TOOL = ROOT / "PASS/tools/memory.py"
SCHEMA_DOC = ROOT / "PASS/docs/MEMORY_SCHEMA.md"

VALID_ENTRY = {
    "id": "TST_MEM_001",
    "scope_type": "topic",
    "scope_id": "example_topic",
    "type": "recurring_failure",
    "evidence_class": "stochastic_performance",
    "observation": "A specific, factual thing that was seen during a real run.",
    "confidence": "provisional",
    "status": "active",
}
VALID_EVENT = {
    "event_id": "TST_EV_0001",
    "date": "2026-08-22",
    "task": "Produce a finished render under competing load",
    "validity": "valid",
}
INVALID_EVENT = {
    "event_id": "TST_EV_0002",
    "date": "2026-08-22",
    "task": "Tighten an accepted artifact without redesign",
    "validity": "invalid",
    "invalid_reason": "exact_edit_source_unavailable",
}


def run_tool(*args: object, memory: Path | None = None) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(TOOL), *map(str, args)]
    if memory is not None:
        command += ["--memory", str(memory)]
    return subprocess.run(command, capture_output=True, text=True, cwd=ROOT)


class MemoryStoreFixture(unittest.TestCase):
    """A disposable memory tree, so no test mutates the shipped store."""

    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="pass-memory-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.domain = self.tmp / "art"
        self.domain.mkdir(parents=True)

    def write(self, entries: list[dict], events: list[dict]) -> None:
        (self.domain / "skill_memory.yaml").write_text(
            yaml.safe_dump(
                {"memory_schema_version": 1, "skillset": "art", "memory_version": 1, "entries": entries},
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        (self.domain / "training_history.jsonl").write_text(
            "".join(json.dumps(event, sort_keys=True) + "\n" for event in events),
            encoding="utf-8",
        )

    def validate(self) -> subprocess.CompletedProcess[str]:
        return run_tool("validate", "--domain", "art", memory=self.tmp)


class AdmissibilityContract(MemoryStoreFixture):
    """An invalid run may be remembered. It may never count."""

    def test_entry_citing_an_invalid_event_is_rejected(self) -> None:
        entry = dict(VALID_ENTRY, evidence_count=1, evidence_events=["TST_EV_0002"])
        self.write([entry], [VALID_EVENT, INVALID_EVENT])
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("cites invalid event", result.stdout)

    def test_entry_citing_a_valid_event_is_accepted(self) -> None:
        entry = dict(VALID_ENTRY, evidence_count=1, evidence_events=["TST_EV_0001"])
        self.write([entry], [VALID_EVENT, INVALID_EVENT])
        self.assertEqual(self.validate().returncode, 0)

    def test_invalid_events_are_kept_rather_than_discarded(self) -> None:
        """The invalid run is the evidence that a tool or controller needs work."""
        self.write([VALID_ENTRY], [VALID_EVENT, INVALID_EVENT])
        self.assertEqual(self.validate().returncode, 0)
        lines = (self.domain / "training_history.jsonl").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2)

    def test_evidence_count_must_match_cited_events(self) -> None:
        entry = dict(VALID_ENTRY, evidence_count=7, evidence_events=["TST_EV_0001"])
        self.write([entry], [VALID_EVENT])
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("does not match", result.stdout)

    def test_compact_refuses_to_link_an_invalid_event(self) -> None:
        self.write([VALID_ENTRY], [VALID_EVENT, INVALID_EVENT])
        result = run_tool(
            "compact", "--domain", "art", "--entry", "TST_MEM_001",
            "--events", "TST_EV_0002", memory=self.tmp,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("refusing invalid event", result.stderr)

    def test_compact_links_valid_evidence_and_confirms_it(self) -> None:
        self.write([VALID_ENTRY], [VALID_EVENT])
        result = run_tool(
            "compact", "--domain", "art", "--entry", "TST_MEM_001",
            "--events", "TST_EV_0001", memory=self.tmp,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        stored = yaml.safe_load((self.domain / "skill_memory.yaml").read_text(encoding="utf-8"))
        self.assertEqual(stored["entries"][0]["evidence_events"], ["TST_EV_0001"])
        self.assertEqual(stored["entries"][0]["evidence_count"], 1)


class PersistenceContract(MemoryStoreFixture):
    """Reported written is not verified written."""

    def test_append_confirms_the_write_by_reading_it_back(self) -> None:
        self.write([], [])
        result = run_tool(
            "append", "--domain", "art", "--task", "Render a figure under competing load",
            memory=self.tmp,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("confirmed it on readback", result.stdout)
        events = [json.loads(line) for line in (self.domain / "training_history.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["validity"], "valid")

    def test_append_refuses_an_authoring_action(self) -> None:
        """Authoring a card is not exercising a capability."""
        self.write([], [])
        result = run_tool(
            "append", "--domain", "art", "--task", "Authored a Drill and committed it",
            memory=self.tmp,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("authoring action", result.stderr)
        self.assertEqual((self.domain / "training_history.jsonl").read_text(encoding="utf-8"), "")

    def test_append_requires_a_reason_for_an_invalid_run(self) -> None:
        self.write([], [])
        result = run_tool(
            "append", "--domain", "art", "--task", "Attempt a local edit",
            "--validity", "invalid", memory=self.tmp,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid_reason is required", result.stderr)

    def test_append_fails_when_the_readback_cannot_find_the_event(self) -> None:
        """The readback is the contract, not the success message.

        Driven in-process because the point is the failure path: if the write is
        reported and the target does not contain it, append must refuse to claim
        persistence. A subprocess test that only checks the happy path would
        still pass with the readback deleted.
        """
        sys.path.insert(0, str(ROOT / "PASS/tools"))
        self.addCleanup(sys.path.remove, str(ROOT / "PASS/tools"))
        import memory as memory_tool

        self.write([], [])
        original = memory_tool.load_events
        # Simulate a target that accepts the write but does not contain it.
        memory_tool.load_events = lambda domain_dir: ([], [])
        self.addCleanup(setattr, memory_tool, "load_events", original)

        ok, problems = memory_tool.append_event(self.domain, dict(VALID_EVENT))
        self.assertFalse(ok)
        self.assertTrue(any("readback failed" in problem for problem in problems), problems)

    def test_append_refuses_a_duplicate_event_id(self) -> None:
        self.write([], [VALID_EVENT])
        result = run_tool(
            "append", "--domain", "art",
            "--json", json.dumps(dict(VALID_EVENT, task="A different task")),
            memory=self.tmp,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("already exists", result.stderr)


class SchemaContract(MemoryStoreFixture):
    """Closed vocabularies stay closed; the schema is never widened for an entry."""

    def test_unknown_vocabulary_value_is_rejected(self) -> None:
        self.write([dict(VALID_ENTRY, confidence="quite_sure")], [])
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("closed vocabulary", result.stdout)

    def test_unknown_key_is_rejected(self) -> None:
        self.write([dict(VALID_ENTRY, vibe="strong")], [])
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("unknown key", result.stdout)

    def test_missing_required_key_is_rejected(self) -> None:
        entry = dict(VALID_ENTRY)
        del entry["evidence_class"]
        self.write([entry], [])
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing required keys", result.stdout)

    def test_duplicate_entry_id_is_rejected(self) -> None:
        self.write([VALID_ENTRY, dict(VALID_ENTRY)], [])
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate entry id", result.stdout)

    def test_superseded_status_requires_a_successor(self) -> None:
        self.write([dict(VALID_ENTRY, status="superseded")], [])
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("requires superseded_by", result.stdout)

    def test_unknown_evidence_origin_is_rejected(self) -> None:
        self.write([dict(VALID_ENTRY, evidence_origin=["vibes"])], [])
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("evidence_origin", result.stdout)

    def test_human_teaching_is_a_recognized_evidence_origin(self) -> None:
        """Teaching is not user preference and must not be filed as feedback."""
        self.write([dict(VALID_ENTRY, evidence_origin=["human_teaching"])], [])
        self.assertEqual(self.validate().returncode, 0)


class TemporaryStateFirewall(MemoryStoreFixture):
    """Nothing becomes memory except a generalized empirical observation."""

    def test_session_state_keys_are_rejected(self) -> None:
        for key in ("current_stage", "candidate_id", "session_id", "next_unit", "parent_gen_id"):
            with self.subTest(key=key):
                self.write([dict(VALID_ENTRY, **{key: "whatever"})], [])
                result = self.validate()
                self.assertEqual(result.returncode, 1)
                self.assertIn("forbidden key", result.stdout)

    def test_retired_provenance_keys_are_rejected(self) -> None:
        for key in ("source_id", "page", "receipt", "attestation", "ledger"):
            with self.subTest(key=key):
                self.write([dict(VALID_ENTRY, **{key: "whatever"})], [])
                result = self.validate()
                self.assertEqual(result.returncode, 1)
                self.assertIn("forbidden key", result.stdout)

    def test_observation_deferring_to_a_conversation_is_rejected(self) -> None:
        entry = dict(VALID_ENTRY, observation="Hands were weak; see the earlier chat for details.")
        self.write([entry], [])
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("must stand alone", result.stdout)


class RetrievalContract(MemoryStoreFixture):
    """Retrieval is bounded, and it reports what it actually returned."""

    def test_query_returns_only_matching_entries(self) -> None:
        entries = [
            dict(VALID_ENTRY, id="TST_MEM_001", scope_id="hands", retrieval_cues=["hand", "grip"]),
            dict(VALID_ENTRY, id="TST_MEM_002", scope_id="landscape", retrieval_cues=["terrain"]),
        ]
        self.write(entries, [])
        result = run_tool("query", "--domain", "art", "--cues", "hand", memory=self.tmp)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("retrieved: TST_MEM_001", result.stdout)
        self.assertNotIn("TST_MEM_002", result.stdout)

    def test_query_respects_the_limit(self) -> None:
        entries = [
            dict(VALID_ENTRY, id=f"TST_MEM_{n:03d}", retrieval_cues=["shared"])
            for n in range(1, 6)
        ]
        self.write(entries, [])
        result = run_tool("query", "--domain", "art", "--cues", "shared", "--limit", "2", memory=self.tmp)
        receipt = [line for line in result.stdout.splitlines() if line.startswith("retrieved:")][0]
        self.assertEqual(len(receipt.split(":")[1].split(",")), 2)

    def test_resolved_entries_stop_being_retrieved(self) -> None:
        entries = [
            dict(VALID_ENTRY, id="TST_MEM_001", status="resolved", retrieval_cues=["hand"]),
            dict(VALID_ENTRY, id="TST_MEM_002", status="active", retrieval_cues=["hand"]),
        ]
        self.write(entries, [])
        result = run_tool("query", "--domain", "art", "--cues", "hand", memory=self.tmp)
        self.assertIn("retrieved: TST_MEM_002", result.stdout)

    def test_query_reports_an_empty_retrieval_honestly(self) -> None:
        self.write([dict(VALID_ENTRY, retrieval_cues=["hand"])], [])
        result = run_tool("query", "--domain", "art", "--cues", "unrelated", memory=self.tmp)
        self.assertIn("retrieved: (none)", result.stdout)


class ShippedStore(unittest.TestCase):
    """The memory that actually ships in this repository."""

    def test_shipped_memory_validates(self) -> None:
        result = run_tool("validate")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_every_domain_with_memory_is_a_real_library_package(self) -> None:
        for domain_dir in MEMORY.iterdir():
            if domain_dir.is_dir() and (domain_dir / "skill_memory.yaml").is_file():
                self.assertTrue(
                    (LIBRARY / domain_dir.name).is_dir(),
                    f"memory/{domain_dir.name} has no matching library package",
                )

    def test_memory_is_not_inlined_into_canon(self) -> None:
        """An entry that must apply every turn earns promotion, not a paste.

        Copying memory into an always-loaded file creates a second write site and
        lets the retrieval path decay unobserved. This checks the paste directly:
        no eight-word run from any observation may appear in a card or a skill
        entrypoint, and no entry id may appear there either.
        """
        canon_texts: list[tuple[str, str]] = []
        for path in LIBRARY.rglob("*.md"):
            canon_texts.append((path.as_posix(), path.read_text(encoding="utf-8")))
        for folder in (ROOT / ".claude", ROOT / ".agents"):
            for path in folder.rglob("*.md") if folder.is_dir() else []:
                canon_texts.append((path.as_posix(), path.read_text(encoding="utf-8")))

        normalized = [(label, " ".join(text.lower().split())) for label, text in canon_texts]

        for domain_dir in MEMORY.iterdir():
            store = domain_dir / "skill_memory.yaml"
            if not store.is_file():
                continue
            data = yaml.safe_load(store.read_text(encoding="utf-8")) or {}
            for entry in data.get("entries") or []:
                entry_id = str(entry.get("id", ""))
                for label, text in normalized:
                    self.assertNotIn(
                        entry_id.lower(), text,
                        f"memory id {entry_id} appears in canon at {label}",
                    )
                words = " ".join(str(entry.get("observation", "")).lower().split()).split()
                shingles = {" ".join(words[i:i + 8]) for i in range(max(0, len(words) - 7))}
                for shingle in shingles:
                    for label, text in normalized:
                        self.assertNotIn(
                            shingle, text,
                            f"memory observation from {entry_id} appears verbatim in canon at {label}",
                        )

    def test_memory_carries_no_practice_history_into_cards(self) -> None:
        """CLAUDE.md rule 15, checked from the other side."""
        for path in LIBRARY.rglob("*.md"):
            text = path.read_text(encoding="utf-8").lower()
            for marker in ("skill_memory", "training_history", "memory_schema_version"):
                self.assertNotIn(marker, text, f"{path.as_posix()} references the memory store")


class Portability(unittest.TestCase):
    """Cold portability: the lesson survives without the repository around it."""

    def test_memory_validates_and_retrieves_with_nothing_but_itself(self) -> None:
        tmp = Path(tempfile.mkdtemp(prefix="pass-memory-portable-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        shutil.copytree(MEMORY, tmp / "memory")

        validated = run_tool("validate", memory=tmp / "memory")
        self.assertEqual(validated.returncode, 0, validated.stdout + validated.stderr)

        queried = run_tool("query", "--cues", "hand", memory=tmp / "memory")
        self.assertEqual(queried.returncode, 0, queried.stderr)
        self.assertNotIn("retrieved: (none)", queried.stdout)

    def test_deleting_memory_does_not_invalidate_the_library(self) -> None:
        """The test that keeps memory from becoming the retired machinery.

        Canon does not depend on the empirical record of using it, exactly as it
        does not depend on the sources it was learned from. If this ever fails,
        memory has become a runtime dependency and ARCHITECTURE.md item 20 is
        broken.
        """
        tmp = Path(tempfile.mkdtemp(prefix="pass-no-memory-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        shutil.copytree(LIBRARY, tmp / "library")
        result = subprocess.run(
            [sys.executable, str(ROOT / "PASS/tools/validate.py"), "--library", str(tmp / "library")],
            capture_output=True, text=True, cwd=ROOT,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse((tmp / "memory").exists())

    def test_no_entry_depends_on_a_conversation_or_a_source(self) -> None:
        for domain_dir in MEMORY.iterdir():
            store = domain_dir / "skill_memory.yaml"
            if not store.is_file():
                continue
            text = store.read_text(encoding="utf-8").lower()
            for phrase in ("see the chat", "see the conversation", "see the transcript", "source_id", "page "):
                self.assertNotIn(phrase, text, f"{store.as_posix()} depends on {phrase!r}")


class ToolingBoundary(unittest.TestCase):
    """The memory tool reads memory. It does not grow a ledger."""

    def test_tool_takes_no_source_ledger_or_provenance_arguments(self) -> None:
        help_text = run_tool("--help").stdout + run_tool("validate", "--help").stdout
        for banned in ("--source", "--ledger", "--provenance", "--receipt", "--manifest"):
            self.assertNotIn(banned, help_text)

    def test_card_validator_still_reads_only_the_library(self) -> None:
        """Memory must not have been bolted onto the card validator."""
        validator = (ROOT / "PASS/tools/validate.py").read_text(encoding="utf-8")
        for marker in ("skill_memory", "training_history", "memory."):
            self.assertNotIn(marker, validator)

    def test_schema_document_exists_and_declares_the_invariants(self) -> None:
        text = SCHEMA_DOC.read_text(encoding="utf-8")
        for required in (
            "never increment",
            "Presence is not consultation",
            "authoritative writable working state",
            "reopens and contains the expected state",
        ):
            self.assertIn(required, text, f"MEMORY_SCHEMA.md is missing: {required}")


if __name__ == "__main__":
    unittest.main()
