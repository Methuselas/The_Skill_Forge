# Review protocol — run 3

**Protocol:** `library/software-engineering/core/code-quality/AP_review_code_you_did_not_write.md`
**Slice:** `workspace/sources/Rust/ripgrep/crates/cli/src/process.rs` (316 lines), plus its
in-tree consumers `crates/cli/src/decompress.rs`, `crates/core/search.rs`,
`crates/core/flags/hiargs.rs`.
**Why this slice:** I wanted a published library crate whose consumers live outside the tree,
and took the first file in the 200–500 line band that owns a resource and has a public
interface — chosen from a `wc -l` listing before reading any of it.

Run 2's report was not opened until this file was written.

## Environment check

| Check | Result |
|---|---|
| `validate.py` | PASS, **1447** objects |
| `memory.py validate` | PASS, 4 stores, **27** entries, **77** events |
| `unittest discover` | **OK, 113 tests, 226.0s** |

All green. The counts are above the handoff's (1446 / 26 / 76 / 110 tests); the handoff
anticipated this and said to trust the store. `HEAD` is `2367b2e` and the working tree has no
modified tracked files — only untracked `workspace/*.md` handoffs — so tree and history agree.

## Memory

```
python PASS/tools/memory.py query --domain software-engineering \
  --cues "review this code" --cues "unfamiliar" \
  --cues "resource ownership" --cues "child process" --cues "deadlock" --cues "library crate"
```

Returned `SE_MEM_016` and `SE_MEM_002`. Both applied, and both changed the output.

---

# Code findings

Ranked by what the defect can break. Findings 1–3 were reproduced by compiling and running
code; transcripts are at the end.

### 1. The builder's default is the opposite of its documented default, and the undocumented one deadlocks

**Where:** `process.rs:83-86` (`#[derive(..., Default)] struct CommandReaderBuilder { async_stderr: bool }`),
`process.rs:90-92` (`new()` → `default()`), against the doc at `process.rs:131`
("This is enabled by default") and `process.rs:146-149`.

`bool::default()` is `false`, so `CommandReaderBuilder::new()` — and therefore the public
`CommandReader::new()` — produces `async_stderr == false`. That selects `StderrReader::sync`
at `process.rs:115`, the branch the crate's own doc at `process.rs:126-129` describes as the one where
"it is possible for the process to fill up the stderr buffer and deadlock." The documented
default and the derived default are opposites, and no compiler check spans the two.

**What it can break:** liveness, permanently. A child that writes more than one pipe buffer to
stderr before its stdout is drained hangs the parent forever. There is no error, no timeout and
no output — the process simply stops. The cause is a `#[derive]` attribute; the symptom is a
hang inside an unrelated caller's read loop, which is about as far apart as cause and symptom get.

**Reachability, traced outward.** This is the step SE_MEM_016 exists for, and it changed the
finding's rank rather than confirming it:

- `crates/core/search.rs:56` — `command_builder.async_stderr(true)`, explicit.
- `crates/core/search.rs:74` — `decomp_builder.async_stderr(true)`, explicit.
- `crates/core/flags/hiargs.rs:1375` — `grep::cli::CommandReader::new(&mut cmd)`, **not**
  compensated. This is `hostname()`, which runs a user-supplied binary
  (`--hostname-bin`) and reads its stdout. A binary noisy on stderr hangs ripgrep here.
- `DecompressionReaderBuilder` (`decompress.rs:196-206`) derives `Default` and delegates, so
  `DecompressionReader::new(path)` inherits the same wrong default for anyone outside the tree.

So ripgrep is *mostly* protected, and protected only because two call sites happen to set the
flag by hand. Every external consumer of `grep-cli` that follows the documentation gets the
deadlocking path. That asymmetry is the finding: the compensation is in the callers, not in the
library, and the callers outside this tree cannot be inspected.

Note that the two sites that do compensate are evidence *against* reading this as intentional —
if `sync` were the intended default, the two internal high-volume users would not both need to
override it.

**Threshold measured on this machine:** no deadlock at 65,536 bytes of stderr; deadlock at
131,072 and above.

### 2. A zero-length read is treated as end-of-stream, silently discarding the child's output

**Where:** `process.rs:254-268`, `impl io::Read for CommandReader::read`.

```rust
let nread = stdout.read(buf)?;
if nread == 0 {
    self.eof = true;
    self.close().map(|_| 0)
}
```

`std::io::Read::read`'s contract states that a zero-length `buf` may return `Ok(0)` and that this
**does not** indicate EOF. `CommandReader` does not distinguish the two: a caller passing an empty
slice sets `self.eof = true`, runs `close()` (which drops stdout and reaps the child), and leaves
the reader permanently at EOF. All subsequent reads return `Ok(0)` via the `None` arm at line 257.

**What it can break:** silent data loss with no error anywhere. Executed: a child producing 28
bytes on stdout yields the empty string, and `BufReader::with_capacity(0, rdr).lines()` — which
reaches this through ordinary `std` code with no empty slice anywhere in user code — collects
zero lines from three. A caller sees a successful read of an empty stream and cannot tell it from
a genuinely empty one. Worse than a truncation that errors, because there is nothing to notice.

Rank is below finding 1 only because the caller shape is uncommon, not because the consequence is
smaller — a wrong empty answer that reports success is in some ways worse than a hang.

### 3. `is_empty()` and `Display` disagree about what "empty stderr" means, defeating the suppression they serve

**Where:** `CommandError::is_empty` at `process.rs:33-38` (untrimmed `bytes.is_empty()`) versus
`Display` at `process.rs:49` (`msg.trim().is_empty()`), meeting in `close()` at `process.rs:238`.

`close()` suppresses an anticipated broken-pipe failure with `if !self.eof && err.is_empty()`.
`is_empty()` is a strict zero-byte test. `Display` treats whitespace-only stderr as empty and
prints `<stderr is empty>`. A child that emits a single newline to stderr — routine — therefore
fails the suppression and produces an error whose entire rendered text is `<stderr is empty>`.

**What it can break:** a spurious, uninformative, user-visible error on any partial read of a
subprocess-backed stream. Under `rg -z`, a search that stops early (`-m`, `--quiet`, a closed
pipe) partially reads the decompressor, which then exits nonzero; if it wrote a trailing newline
to stderr, the user gets an error message that says nothing. Executed end-to-end through the real
`close()`: `close() -> Err("<stderr is empty>")`.

The two functions are 200 lines apart in one file and neither refers to the other. Whichever
definition is right, they should be the same one.

### 4. `CommandError` exposes no error source and flattens to `ErrorKind::Other`

**Where:** `process.rs:41` (`impl std::error::Error for CommandError {}`, empty) and
`process.rs:76` (`io::Error::new(io::ErrorKind::Other, cmderr)`).

`source()` defaults to `None`, so the inner `io::Error` of the `Io` variant is unreachable by
chain-walking. The `Stderr` variant becomes `ErrorKind::Other`, which no consumer can match on.

**What it can break:** external consumers cannot programmatically distinguish a spawn failure
from a child-reported failure, and error-chain reporters print one line where two were available.
Contained and non-corrupting, hence the rank. `From<CommandError> for io::Error` does preserve
the `Io` variant losslessly (`process.rs:74`), which limits the damage.

### 5. The async stderr thread is never joined on the success path

**Where:** `process.rs:227-228`. When `child.wait()` reports success, `close()` returns without
calling `self.stderr.read_to_end()`, so the `Async` variant's `JoinHandle` is dropped rather than
joined and the thread is detached.

**What it can break:** little, which is why it is last. The child has already exited, so the pipe
closes and the thread terminates on its own; the `CommandError` it built is dropped. The cost is
that the whole of a successful child's stderr is read onto the heap and discarded, and the thread
briefly outlives the reader that owns it. Read, not executed.

## Families examined and found acceptable

Listed so this can be told from a review that stopped at five.

- **Should the type exist at all (step 2).** No wholesale-replacement finding. `std` offers
  `Command::output()` (buffers everything, not streaming) and raw `spawn()` (no stderr capture on
  failure); nothing in `std` provides streaming stdout with stderr held for the failure case. The
  type earns its place, so nothing below is conditional.
- **Ownership and lifetime.** `CommandReader` owns the `Child`, its two pipes, and possibly a
  thread. `build()` takes both pipes at `process.rs:113-115`, so ownership is unambiguous and no
  handle is left in the `Child`. Correct.
- **Copy/clone control.** `CommandReaderBuilder` derives `Clone` (plain config); `CommandReader`
  does not (owns a process). The distinction is made correctly and deliberately.
- **Idempotence of `close()`.** Holds. `self.child.stdout.take()` at `process.rs:222` is both the
  action and the flag, so every call after the first returns `Ok(())` at line 223. Verified by
  execution — `Drop` after an explicit `close()` is a no-op.
- **Double-call of `StderrReader::read_to_end`.** The `expect` at `process.rs:300` is
  unreachable: `read_to_end` is called only from `close()`'s failure arm, and `close()` cannot
  reach that arm twice because of the `take()` guard above. Cleared.
- **Panic inside `Drop`.** `Drop` calls `close()`, which can reach two `expect`s. Both are
  effectively unreachable (the one above; and `stderr_to_command_error` at `process.rs:310-316`
  has no panicking path short of allocation failure, which aborts rather than unwinds). No
  double-panic abort risk. Cleared.
- **`unwrap()` on `child.stderr.take()`** at `process.rs:113,115`. Justified — `.stderr(piped())`
  is set three lines above on the same builder. Cleared.
- **Inherited stdin.** `build()` deliberately does not override stdin and says so at
  `process.rs:98-99`; `hiargs.rs:1374` sets `Stdio::null()` itself. Documented, not a defect.
- **Unbounded stderr buffering.** The entire stderr is read onto the heap
  (`process.rs:311-313`), disclosed at `process.rs:148-149`. A hostile child can exhaust parent
  memory. Accepted, documented limitation rather than a finding — flagged here because it is a
  real bound that a consumer choosing this crate should know about.
- **Error-signalling consistency.** Examined and *deliberately not reported* — see the dropped
  candidate below.

## Step 6 — conflicts surfaced rather than resolved

**One, and it is about the protocol rather than the code.** Step 8's gate and its `unowned`
outcome give opposite readings of the same observation.

Finding 1 exists because nothing in the library says that a language-synthesized default is a
decision nobody made. That is a genuine, demonstrable gap in coverage, and step 8's `unowned`
outcome is where a gap belongs. But the gate says every step 8 entry must first be shown *sound*,
because "a defect mistaken for practice will widen a card until it endorses the defect" — and this
arrived as a defect, not as a technique the code used well. The gate therefore routes it to the
code findings, where there is nowhere to record that no card covers it, and the observation is lost.

I have not resolved this. Both readings are defensible: the gate is protecting against laundering
a defect into canon, and the `unowned` outcome is the only place the library learns about its own
blind spots. The distinction that might settle it is that the gate guards against *widening an
existing card to endorse a defect*, whereas this would *author a new card that forbids the
defect* — those are not the same risk. I have recorded it below as unowned and marked it, rather
than picking silently.

---

# Guidance findings

Gate applied before sorting: each technique below was checked for correctness first, and one
candidate failed and was moved into the code findings (see #3).

**Owned — 4.** Recognition, recorded as a count with ids:

| Technique in the code | Covering object |
|---|---|
| `Option::take` as the closed-flag, so closedness is derived from whether the resource is still held rather than from a second `bool` (`process.rs:222`) | `PAT_single_source_of_truth_for_data` |
| Explicit `close()` that returns the error, plus `Drop` as a last line of defence that can only log (`process.rs:246-252`) | `PAT_give_every_acquired_resource_one_named_owner` |
| Deriving `Clone` on the config builder but not on the resource-owning reader | `PAT_choose_raii_copying_behavior_deliberately` |
| A crate error type carrying the failure cause as a variant, with lossless `From` back to `io::Error` (`process.rs:65-80`) | `PAT_return_result_type_to_convey_error_cause` |

**Owned but coarser than the practice — 1.**

*Concurrent draining of two blocking streams from one peer.* The `async` branch
(`process.rs:280-284`) gives stderr its own thread so neither the parent nor the child can be
blocked by the other's unread buffer. Verified sound by execution: the async case drains 1,048,576
bytes and completes while the sync case hangs.

`PAT_break_one_of_deadlocks_four_conditions` covers the diagnosis and points the right way — its
"Don't count only the resources you named … anything else limited in number that cannot be
shared" reaches a pipe buffer, and "Attack the exclusivity first" is the correct strategy here.
Where it stops short is the remedy. All three of its worked remedies — a global acquisition
order, release-and-retry, and a request mechanism — assume the contending parties are threads
inside your design that can choose *when* to acquire. Here the other party is a separate process
you do not control and cannot instruct, the contended resource is buffer space in a stream you are
already holding open, and the only available move is to remove the exclusivity by giving each
stream its own consumer. That instance is absent from the card, and its absence is what makes the
card readable as correct while leaving a reviewer of this code with no rule to apply. Direction
right, resolution short — the outcome the protocol warns is easiest to miss.

**Unowned — 1, flagged under the step 6 conflict above.**

*A default the language synthesizes is a decision nobody made, and where the type's intended
default lives only in prose, nothing will ever report the disagreement.* The situation is
present: `#[derive(Default)]` on a config struct whose intended default is stated in a doc
comment, with no code path connecting the two.

Searches run, all empty in `core`:

- `grep -rli "synthesi"` — matches only `source_title: PASS software-engineering canonical synthesis` reference fields. No card discusses language-synthesized members outside the cpp lane.
- `grep -rli "documented default"`, `"default is documented"`, `"doc comment"` — no matches anywhere in `software-engineering` or `metaskills`.
- `grep -rli "implicit default"` — one match, `PAT_signal_async_errors_with_promise_of_result`, unrelated.
- `grep -rli "compiler-generated"` — matches only cpp copy-control and RAII cards.

Nearest cards, all read in full rather than by title:

- `PAT_state_a_types_default_in_one_place` — closest by name and does not cover it. Its Pattern
  Rule enumerates the sites as "a member initializer, a reset or clear path, a factory … or the
  condition under which a writer omits a field" — every one a code site, and its failure mode is
  drift *between* code sites that all execute. Here there is exactly one code site (the derive)
  and one prose site, and the derive was never written by anyone. The card's repairs — assign a
  freshly constructed instance, test the round trip — do not reach it.
- `PAT_prefer_unmistakable_over_small_print` — directionally relevant and about a different
  thing: where to put a contract term that binds the *caller*. It would say the `async_stderr`
  guarantee should not live in a doc comment. It does not address a default the type supplies to
  *itself*, and its concern is the caller not reading the small print rather than the small print
  being false.
- `PAT_make_the_default_value_mean_invalid` — about reserving the zero slot of an enumerated type
  for an invalid member. There is no invalid member to reserve when both values of a config
  `bool` are legal.
- `PAT_choose_raii_copying_behavior_deliberately` — the same *shape* ("decide explicitly, because
  the compiler-generated one usually mishandles it"), but it is a cpp-lane card scoped to copy
  control, and rules 2/3 keep a `core` card from reaching it. The core-level generalization is
  what is absent.

---

# The three required lines

**Did memory apply?** Yes, both entries, and both changed the output. `SE_MEM_016` sent me past
the file boundary to the call sites before ranking; that trace is what produced finding 1's actual
severity — that ripgrep is protected only by two hand-written `async_stderr(true)` calls while
`hostname()` and every external consumer are not. Without it I would have had a documentation
inconsistency rather than a reachable deadlock. `SE_MEM_002` killed a candidate (below). Worth
noting for that entry's boundary clause, which says it is untested where the slice is a library
crate with consumers outside the tree: on this slice the outward trace stayed bounded and cheap —
four call sites, all found by one grep — because the *in-tree* consumers were enough to establish
reachability. The unbounded part (consumers outside the tree) did not need tracing, since their
existence, not their contents, is what makes the finding.

**Was a candidate dropped?** Yes, one. This file signals errors two ways — `CommandError` from
`build()`/`new()`, `io::Error` from `read()`/`close()` — and I was moving to report the split as an
inconsistency. `SE_MEM_002` says to check whether the inconsistency falls along a line or scatters.
It falls along a line exactly: the `io::Result` surface is where the type implements
`std::io::Read`, whose signature it does not control. Reporting it would have been wrong, and the
entry is what stopped it.

**Did step 8 produce anything?** Yes — one owned-but-coarser item, one unowned item, four owned,
and one conflict about step 8's own structure. Note that the slice was chosen freely rather than
aimed at thin coverage, and the protocol predicts a low unowned share from such a slice; one
unowned item out of six is consistent with that rather than evidence the library is thin here.

---

# Reproductions

Compiled with `rustc 1.98.0`, no crate dependencies. Sources in the session scratchpad
(`rustscratch/repro.rs`, `repro2.rs`, `repro3.rs`). `repro2.rs` contains `process.rs` copied
verbatim, with only `log::warn!` → `eprintln!` and `pub(crate)` → `pub` so it builds against
`std` alone; the transcripts below are its actual output.

### Finding 1 — `repro.rs`

```
process.rs:131 documents async_stderr: "This is enabled by default."
CommandReaderBuilder::new().async_stderr == false

child writes 1048576 bytes to stderr before writing stdout

async_stderr = false  (what CommandReader::new() actually gives)
  -> DEADLOCK: no progress in 10s (child blocked writing stderr, parent blocked reading stdout)

async_stderr = true   (what the docs promise)
  -> OK: read "hello from stdout" from stdout; child exited true; stderr drained: 1048576 bytes
```

Threshold scan (`repro3.rs`, same program parameterized by stderr volume):

```
   4096 bytes -> OK        32768 bytes -> OK        131072 bytes -> DEADLOCK
   8192 bytes -> OK        65536 bytes -> OK        262144 bytes -> DEADLOCK
  16384 bytes -> OK                                 524288 bytes -> DEADLOCK
```

### Findings 2 and 3 — `repro2.rs`, driving the verbatim code with real child processes

```
=== Case A: zero-length read treated as EOF ===
std::io::Read::read contract: "If buf has a length of zero, then this
call may return Ok(0), which does not indicate EOF."

  rdr.read(&mut []) -> Ok(0)   [child produced 28 bytes]
  subsequent read_to_string  -> ""
  => the stream is now permanently EOF; the child was closed.

  BufReader::with_capacity(0, rdr).fill_buf() -> 0 bytes
  .lines() collected                          -> []
  => three lines of real output silently became zero, with no error.

=== Case B: is_empty() and Display disagree on "empty stderr" ===
  stderr bytes = "\n"
  CommandError::is_empty() -> false   (close() suppression needs true)
  Display renders          -> "<stderr is empty>"

  partial read of 4 bytes (eof flag stays false)
  close() -> Err("<stderr is empty>")
```

Nothing was committed and nothing was written to `memory/`.

---

# Comparison with run 2 (read only after the above was written)

Run 2 took `prometheus tsdb/isolation.go` — Go, in-process, lock-based. Run 3 took Rust, a
published library crate, cross-process pipes. Independent slices, independent languages,
independent failure domains. Four things came out the same:

1. **The same two memory entries fired**, and were used the same way: `SE_MEM_016` to trace
   outward before ranking, `SE_MEM_002` to kill an inconsistency candidate that turned out to
   follow a layer boundary. Neither run saw the other's report.
2. **The same step 8 shape**: one unowned, one owned-but-coarser, four owned. Both slices were
   chosen freely and both produced the low unowned share the protocol predicts.
3. **The same card came back owned-but-coarser** —
   `PAT_break_one_of_deadlocks_four_conditions` — from two runs that could hardly have approached
   it more differently. Run 2 found its *convention-siting* clause underspecified; run 3 found its
   *remedy list* missing the case where the contended resource is buffer space in a stream and the
   other party is a process you cannot instruct. Different clauses, same verdict: right in
   direction, short on resolution.
4. **Both runs' top finding was produced by the outward trace, not by the file.** Run 2's came
   from `head_append.go`; run 3's from `hiargs.rs` and `search.rs`. In both cases the file alone
   supported a weaker claim.

That third point seems the most useful of the four. One run finding a card coarse is an opinion;
two independent runs finding the same card coarse at two different clauses is a measurement, and
it is the kind of evidence the handoff's open repair #2 was waiting on. Repair #2 appears to have
landed already — the card now carries the "Put that convention where an acquisition site will hit
it" bullet, which is precisely what run 2 asked for — so run 3's observation is a *second,
separate* shortfall in the same card rather than a restatement of the first.

One boundary clause was tested rather than assumed. `SE_MEM_016` records that it is "untested
where the slice is a library entry point or a published interface whose consumers are outside the
tree, and there the same instruction could licence an unbounded trace rather than a short one."
Run 3 was deliberately that case. The trace did **not** run away: it terminated in one grep and
four call sites, because establishing reachability only needed the in-tree consumers, and the
out-of-tree consumers mattered for their *existence* rather than their contents. That is one
observation on the untested edge, not a repeat of the two events already cited, and it points the
opposite way from the risk the boundary anticipated.

I have not written it to `memory/`. Whether it is admissible — one run, one runtime, and the same
"graded by the runtime that produced it" objection the handoff raises about `SE_EV_0036` —
is a decision, and the handoff says decisions come after the report.
