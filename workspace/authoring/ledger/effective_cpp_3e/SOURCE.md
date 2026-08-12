# Effective C++, Third Edition

source_id:    effective_cpp_3e
title:        "Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs"
author:       Scott Meyers
publish_date: 2005
media_type:   PDF
payload_path: sources/effective_cpp_3e/Effective_Cpp_3rd_Edition.pdf
sha256:       4f983195c37c2276fc247ecc25ded5541573a317e37361f6a497fc7944f50679
pdf_page_offset: 21
added:        2026-07-31
status:       complete
closed:       2026-08-01

## Unit scheme

One source-native chapter per unit (9 chapters, 55 Items). Each chapter groups a
run of self-contained "Item" essays, and each Item carries its own "Things to
Remember" box — the author's atomic teachable scope. A chapter is the smallest
grouping that reads twice comfortably while still yielding a coherent cluster of
related skills, matching the chapter-per-unit cadence proven on
`gcbc_think_like_swe` (~11 objects/unit). A dense chapter may be read in Item
passes but remains one ledger unit unless it proves too large to ground in one
read, in which case the split is recorded here.

Page numbers in locators are the book's printed page numbers. PDF page = book
page + 21 (Ch.1 "Item 1" begins on book p.11 = PDF p.32; the Introduction's
book p.1 = PDF p.22).

## Summary

Reconciled 2026-08-01. All 9 chapter units processed (0 empty, 0 blocked).

- **Units:** 9 processed / 0 empty / 0 blocked.
- **Objects added:** 80 — 64 patterns, 16 drills, 0 APs.
- **Variants absorbed:** 2, both into `gcbc_think_like_swe` foundations —
  `VAR_cpp_warnings_implementation_dependent` into
  `PAT_treat_compiler_warnings_as_potential_bugs` (u09, Item 53), and
  `VAR_cpp_know_standard_library_and_tr1` into `PAT_reuse_before_reinventing`
  (u09, Items 54-55).
- **Objects replaced:** 0.
- **Candidates rejected:** 2 explicit `reject` rows in u09 — the standard
  library / TR1 component inventory (Item 54) and the Boost overview (Item 55),
  both reference/awareness material rather than transferable skills. Pre-C++11
  successors (`= delete`, `std::unique_ptr`/`std::shared_ptr`, move semantics,
  `std::function`/`std::bind`, modern trait names) were deliberately left for
  *Effective Modern C++* to absorb as variants/replacements rather than invented
  here.

### Per-unit object counts

| unit | chapter | patterns | drills | total |
|---|---|---|---|---|
| u01 | Accustoming Yourself to C++ | 10 | 2 | 12 |
| u02 | Constructors, Destructors, Assignment Operators | 9 | 2 | 11 |
| u03 | Resource Management | 5 | 2 | 7 |
| u04 | Designs and Declarations | 8 | 2 | 10 |
| u05 | Implementations | 8 | 2 | 10 |
| u06 | Inheritance and Object-Oriented Design | 10 | 2 | 12 |
| u07 | Templates and Generic Programming | 8 | 2 | 10 |
| u08 | Customizing new and delete | 6 | 2 | 8 |
| u09 | Miscellany | 0 | 0 | 0 (2 variants absorbed, 2 rejects) |
| **total** | | **64** | **16** | **80** |

### Library placement

All 80 objects live in the `software-engineering` package under a new
`languages/cpp/` lane, across topics: foundations, preprocessor,
const-correctness, initialization, copy-control, destructors, construction,
resource-management, memory-management, interface-design, parameter-passing,
encapsulation, operators, swap, inheritance, virtual-functions, templates,
traits, and metaprogramming. Many cards specialize or cross-link to the
language-agnostic gcbc foundations (immutability, hard-to-misuse, encapsulation,
error-handling, composition, reuse), and Ch.9 added two C++ variants directly
into gcbc foundations.

### Retirement

Payload moved to `trash/sources/effective_cpp_3e/` on 2026-08-01 at the user's
request (local cleanup; `sources/` and `trash/` are gitignored). The SHA-256
above remains the source identity and the REGISTRY duplicate guard, so the
source will not be reprocessed regardless of file location. The book was removed
from the curated `sources/Programming/C++/` shelf; its `READING-ORDER.md` still
lists it, so re-download or restore from trash if the shelf copy is wanted back.

