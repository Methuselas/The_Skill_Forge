---
object_id: PAT_describe_data_by_meaning_when_it_leaves_the_machine
object_type: pattern
name: Describe Data by Meaning When It Leaves the Machine
library_path:
- software-engineering
- core
- data-types
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- data_types
- portability
- interfaces
- distributed
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_separate_buffer_ownership_from_message_delivery
- rel: related_to
  target_object_id: PAT_convey_usage_through_names_and_types
- rel: related_to
  target_object_id: PAT_single_source_of_truth_for_logic
- rel: related_to
  target_object_id: PAT_price_a_dependency_by_the_cost_of_change
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Describe Data by Meaning When It Leaves the Machine

## Pattern Rule
**IF** data is about to leave the process that created it — across a network, into a file, into shared storage, or to another program
**THEN** describe it by what each field *is* rather than by how many bytes it occupies, so the reader can reconstruct meaning rather than reproduce a layout
**ELSE** where producer and reader are the same build of the same program on the same machine and the data never outlives that process, the layout is the meaning and there is nothing to translate.

## Do
- Separate the two things a description can capture, because only one of them travels. A size says how much storage to move. A type says what the bytes mean — which end the significant byte is at, how wide the value is, where the fields begin. A reader given only sizes has to already agree with you about all of that, and agreement is what you cannot assume once the data leaves.
- Enumerate what can differ, because the list is longer than the obvious entry. Byte order is the one everybody names. Width is the second — the same declared integer is not the same size everywhere. And the third, most easily missed, is that the compiler inserts padding between fields to satisfy alignment, so two builds can disagree about a structure's layout **on the same processor** if they were compiled with different settings.
- Take that third point as the reason "we control both ends" is a weaker argument than it sounds. Same architecture does not mean same layout, so a scheme that copies a structure's raw bytes is depending on build flags matching — a coupling nobody records, nothing checks, and a compiler upgrade can break.
- Write it in the portable form even where no translation will occur. Where both ends genuinely match, describing fields by type costs nothing at run time and the code never has to change when a new platform, a new compiler, or a new consumer appears. The alternative is correct today and is a rewrite the first time either end moves.
- Keep the description in one place and derive both directions from it. A writer and a reader that each independently know the format are two sources of truth that drift, and the failure is a corrupted round trip rather than a compile error.
- Send a structure as one described unit rather than field by field. Decomposing it into a series of primitive transfers breaks the encapsulation for no gain and pays the per-transfer cost repeatedly; describing the whole aggregate once keeps both the structure and the efficiency.
- Decide what happens when the two ends disagree about the shape itself, not just its layout. Fields get added; readers meet data written by newer or older writers. A format with no version and no rule for unknown fields will eventually be read by something that does not share its assumptions, and the failure will be silent.

## Don't
- Don't ship a structure as an opaque block of bytes because it works. It is the fastest thing to write, it passes every test on the machine that wrote it, and it encodes your compiler's padding decisions into a wire format. What breaks it is not exotic — a different architecture, a different compiler, or the same compiler with different flags.
- Don't treat a matching total size as evidence the layouts agree. Two structures can occupy the same number of bytes with fields at different offsets, so the check that seems like it would catch this does not.
- Don't rely on a comment to carry the format. The description has to be something both ends execute, not something both ends were told; a note beside the writer does not constrain the reader and stops being true silently.
- Don't defer the versioning question to the first incompatibility. By then there is data in flight, data at rest, and readers you do not control, and the change that was a design decision has become a migration.
- Don't confuse this with efficiency. Describing data by meaning is not about making it smaller — a self-describing format is usually larger — it is about the reader being able to read it at all.

## Checklist
- Does anything outside this build ever read this data?
- Is each field described by what it is, or by how many bytes it takes?
- Could padding or alignment differ between the writer and any reader, including a future build of this program?
- Do the writing and reading sides derive their format from one definition?
- What happens when a reader meets data written by a different version?
- Does the data outlive the process that wrote it?

## Notes
The instinct this corrects is a good one applied past its boundary. Inside a program, a structure's layout *is* its representation, and treating memory as bytes is exactly right — it is fast, direct, and there is no second opinion about what the bytes mean. The moment the data crosses to something that was compiled separately, that shared understanding stops being automatic and becomes an assumption, and the code carries no record that it was ever made.

Alignment padding deserves the emphasis it gets here because it defeats the usual reassurance. Most people reach for raw byte copying after checking that both ends run the same architecture, which handles byte order and width and feels like enough. It is not: the compiler decides where fields sit, that decision depends on settings, and two builds of the same source on the same processor can lay a structure out differently. The coupling is to a build configuration rather than to a machine, and build configurations change without anyone thinking of it as a format change.

The versioning question belongs here rather than in a later conversation, because the answer constrains the format. A format designed with no notion of a version can be given one later only by breaking every existing reader; a format that reserves the question from the start pays a small cost forever and can evolve. Which of those you want is a real choice, and it is decided — deliberately or not — at the moment the first byte is written.
