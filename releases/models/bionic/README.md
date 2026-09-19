# Bionic Memory

Persistent cross-session memory for AI agents. Local Markdown files, zero dependencies beyond Python 3.8+, works with any Agent Skills–compatible host.

## The Problem

AI agents start every session with amnesia. They forget your preferences, your project context, the corrections you gave them last time. You end up repeating yourself, or worse — the agent confidently contradicts something you established previously.

Bionic Memory gives agents a durable memory that survives across sessions, stored as simple Markdown files on your machine.

## How It Works

Memory lives in `~/.bionic-memory/memory/`:

- **Global** (`global/`) — for regular chats
- **Project-scoped** (`Project/<folder>/`) — per-workspace context

Each memory entry is one Markdown file with front matter. The `memory.py` CLI tool manages entries, enforces structure, and automatically rebuilds the index after every change so it can never drift out of sync.

## Quick Start

```bash
# See what's in memory
python memory.py index

# Read specific entries
python memory.py read user-terse feedback-honesty

# Add a new entry
python memory.py write user-preference-dark-mode --type user \
  --description "Prefers dark mode UIs across all tools." \
  --body "Always use dark themes when suggesting tools or writing docs."

# Update an existing entry (same name replaces it)
python memory.py write user-terse --type user \
  --description "Prefers terse, technical responses." \
  --body "Direct answers. No verbosity. Lead with the result."

# Delete entries
python memory.py delete stale-entry

# Manually rebuild the index
python memory.py rebuild
```

For project-scoped memory, add `--project <workspace-path>` to any command:

```bash
python memory.py index --project /path/to/my/repo
```

## Commands

| Command | What it does |
|---|---|
| `index` | Print the memory index (one line per entry) |
| `read NAME [NAME ...]` | Print up to 8 entries in full |
| `write NAME --type TYPE --description TEXT [--body TEXT \| --body-file FILE]` | Create or replace an entry |
| `delete NAME [NAME ...]` | Remove entries |
| `rebuild` | Rebuild the index from entry files |

### Write options

- `--type` — one of: `user`, `project`, `feedback`, `reference`
- `--description` — one-line summary shown in the index (max 200 chars)
- `--body` or `--body-file` — the entry content (max 4000 chars; one fact per entry)
- `--confidence` — `provisional` (default) or `strong`
- `--author` — who wrote the entry

## Entry Types

| Type | Use for |
|---|---|
| `user` | Who the user is, how they work, stable preferences |
| `project` | Current work, decisions, goals, blockers |
| `feedback` | Corrections, confirmed approaches, "do X not Y" |
| `reference` | Pointers to external resources, docs, tools |

## Design Principles

- **One fact per entry.** If it needs two paragraphs, it's probably two entries.
- **The index is derived, never authoritative.** It's rebuilt from the entry files after every operation.
- **Small models can use it.** The CLI protocol is three commands: `index` → `read` → `write`. No complex file editing required.
- **The user is always right.** If the user contradicts a memory entry, the user wins. Update the entry.
- **No sensitive data unless asked.** Don't store health, religion, politics, or identity unless the user explicitly wants that remembered.

## Rules the Tool Enforces

- Entry names: lowercase words joined by hyphens (e.g., `user-terse`)
- Body size: max 4000 characters
- Read size: max 8 entries per call
- Type must be one of the four defined types
- Index is rebuilt automatically — you can't leave it stale

## File Format

Each entry is a Markdown file with YAML front matter:

```markdown
---
name: user-terse
description: Prefers terse, technical responses. No verbosity.
type: user
confidence: strong
modified: 2026-09-13T14:00:00Z
---

Prefers terse, technical, direct responses. Dislikes verbosity and salesy language.

**Why:** Verbosity burns context tokens and the user's patience.

**How to apply:** Lead with the answer. One paragraph unless depth is asked for.
```

Richer entries (feedback, decisions) should include **Why** and **How to apply** when those would matter in a future session. Cross-reference other entries with `[[entry-name]]`.

## As an Agent Skill

Bionic Memory ships as an Agent Skills–compatible skill with a `SKILL.md` that instructs the agent on when and how to use it. Install it like any other skill, and the agent will:

1. Load relevant memory at session start
2. Use it as background context
3. Write new entries when durable state changes
4. Consolidate stale entries at natural boundaries

The skill includes an 8B compatibility mode: for small models (8B, 16k context), the protocol collapses to `index` → read at most 3 entries → use them → write one entry if needed. No consolidation, no complexity.

## Requirements

- Python 3.8+
- Standard library only (no pip installs)

## License

MIT
