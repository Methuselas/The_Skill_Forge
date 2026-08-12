# Gottfried Bammes — The Artist's Guide to Animal Anatomy — Source Record

source_id: gottfried_bammes_artist_guide_to_animal_anatomy
title: The Artist's Guide to Animal Anatomy
author: Gottfried Bammes
publish_date: 2004
media_type: PDF
payload_path: sources/animal_anatomy/gottfried_bammes_artist_guide_to_animal_anatomy/The_Artists_Guide_to_Animal_Anatomy.pdf
pdf_page_offset: -2
sha256: 57ad055fadae85e1c15f85af1cc5803155354a3a143554503ef92b92bc96e26d
added: 2026-08-10
status: in-progress
commit_state: staged
text_layer: usable
visual: true
visual_access: renderer
page_images_path: none
page_count: 143 physical PDF pages

## Edition and locator note

This payload is the 2004 Dover edition, an unabridged republication of the 1994 English translation of *Die Gestalt des Tieres*. The main instructional text runs from printed p. 7 through printed p. 143. Across that body, physical PDF pagination is consistently two pages earlier than printed pagination, so `pdf_page_offset: -2` maps printed receipt pages to physical PDF pages.

Preflight on 2026-08-10 reported a usable text layer on 143/143 physical pages and working CropBox rendering through `/usr/bin/pdftoppm`. Because this is an anatomy/drawing source, every processed unit pairs per-page text extraction with rendered page inspection even when a given unit is prose-heavy.

## Unit scheme and deep-PASS routing

This source is intentionally split more finely than Hultgren. Bammes builds a cumulative method across explicit numbered subsections, and several chapters are dense enough that a whole-chapter unit would be too large to read twice and ground cheaply. The default unit is therefore one numbered subsection. Two exceptions avoid artificial overlap: 1.1 and 1.2 share printed p. 9 and are combined; the Chapter 9 opener on printed p. 134 is combined with 9.1.

- u01 — Introduction — printed pp. 7-8; physical pp. 5-6
- u02 — 1.1 Deciding on specific impressional qualities + 1.2 Anatomical knowledge used to pinpoint essence — printed pp. 9-10; physical pp. 7-8
- u03 — 1.3 Understanding the structural design of an animal — printed pp. 11-14; physical pp. 9-12
- u04 — 1.4 Deciding on a viewing angle — printed pp. 15-16; physical pp. 13-14
- u05 — 2. Body cover textures — printed pp. 17-22; physical pp. 15-20
- u06 — 3.1 Proportion: a distinctive feature of animal form — printed pp. 23-26 through the text immediately before §3.2; physical pp. 21-24
- u07 — 3.2 Establishing proportion: a practical guide — printed pp. 26-29 from the §3.2 heading through the text immediately before §3.3; physical pp. 24-27
- u08 — 3.3 Practical work on proportion — printed pp. 29-32 from the §3.3 heading; physical pp. 27-30
- u09 — 4.1 Modes of standing, sitting and lying — prose printed pp. 33-34 / physical pp. 31-32, plus supporting figs. 34-37 printed pp. 35-36 / physical pp. 33-34
- u10 — 4.2 Modes of locomotive movement — printed pp. 35-40; physical pp. 33-38; shared pp. 35-36 also carry the visual spill of figs. 34-37 from §4.1
- u11 — 4.3 Exercises in repose and motion — printed pp. 41-46; physical pp. 39-44
- u12 — 4.4 Freedom, improvisation, experiment — printed pp. 47-48; physical pp. 45-46
- u13 — 5.1 Hindleg: drawing the construction of the skeleton — printed pp. 49-54; physical pp. 47-52
- u14 — 5.2 Hindleg: the musculature — printed pp. 55-56; physical pp. 53-54
- u15 — 5.3 Hindleg: constructional studies and visualization — printed pp. 57-64; physical pp. 55-62
- u16 — 6.1 Foreleg: shoulder and foreleg of specialized runners — printed pp. 65-68; physical pp. 63-66
- u17 — 6.2 Foreleg: musculature in specialized runners — printed pp. 69-70; physical pp. 67-68
- u18 — 6.3 Whole foreleg of a runner: analysis and drawing from imagination — printed pp. 71-79; physical pp. 69-77
- u19 — 6.4 Shoulder and foreleg of carnivores — printed pp. 80-83; physical pp. 78-81
- u20 — 6.5 Carnivore foreleg: basic disposition of the musculature — printed pp. 84-86; physical pp. 82-84
- u21 — 6.6 Carnivore foreleg: constructional approach combined with visualization — instructional prose and figs. 93-98 on printed pp. 87-92; physical pp. 85-90; printed p. 92 also begins fig. 99, which is supporting evidence for u22 rather than u21
- u22 — 6.7 Special shape of the shoulder girdle in primates — supporting fig. 99 on printed pp. 92-93 / physical pp. 90-91 plus §6.7 prose and fig. 100 on printed p. 94 / physical p. 92
- u23 — 7.1 Vertebral column as a structure creating form — printed pp. 95-101; physical pp. 93-99
- u24 — 7.2 Thorax as a plastic core — printed pp. 102-104; physical pp. 100-102
- u25 — 7.3 Skeleton of the whole trunk — printed p. 105; physical p. 103
- u26 — 7.4 Disposition of the pure trunk muscles — printed pp. 106-107; physical pp. 104-105
- u27 — 7.5 Graphic aids to depicting the body — printed pp. 108-112; physical pp. 106-110
- u28 — 8.1 Types of skull structures — printed pp. 113-118; physical pp. 111-116
- u29 — 8.2 Drawing the skull constructionally — printed pp. 119-121; physical pp. 117-119
- u30 — 8.3 Head and shapes of its soft parts — printed pp. 122-129; physical pp. 120-127
- u31 — 8.4 Drawing the head as a whole — printed pp. 130-133; physical pp. 128-131
- u32 — 9. Coming to terms with the whole animal figure + 9.1 Drawings as built designs — printed pp. 134-135; physical pp. 132-133
- u33 — 9.2 Sketching — printed pp. 136-137; physical pp. 134-135
- u34 — 9.3 Free play — printed pp. 138-143; physical pp. 136-141

## Shared transition-page note

Printed pp. 26 and 29 each contain the end of one numbered subsection and the beginning of the next. The unit boundaries therefore follow the subsection headings rather than assigning the whole physical page to only one unit: u06/u07 share printed p. 26 and u07/u08 share printed p. 29. Receipt notes on those pages are scoped to the text and figures belonging to the named subsection.

A second layout spill occurs at the start of §4.2: printed p. 35 begins the §4.2 prose but also carries figs. 34-35, which visually complete §4.1's reduced-support analysis; printed p. 36 carries figs. 36-37, which visually complete §4.1's lying/repose examples even though the footer is already Section 4.2. u09 therefore reads those figures as supporting evidence while u10 owns the §4.2 prose on the same pages. The shared pages are not double-counted as new doctrine.


A third transition spill occurs between §§6.6 and 6.7. Printed p. 92 finishes fig. 98 for §6.6 and begins fig. 99, titled as the special shoulder/forelimb form of the ape; printed p. 93 is entirely the continuation of fig. 99, while the §6.7 prose heading appears on printed p. 94 and explicitly explains fig. 99. u21 therefore owns §6.6 through fig. 98, while u22 owns fig. 99 on printed pp. 92-93 together with the §6.7 prose/fig. 100 on printed p. 94. The shared p. 92 is not double-counted as new doctrine.

## Source posture

This is a deep comparative-anatomy PASS source. Strong candidates are expected in functional construction, proportion, support and locomotion, limb specialization, scapular/shoulder mechanics, trunk construction, skull/head design, visualization, and deliberate practice. Anatomy facts do not earn cards merely for being true. Broad biological or teleological claims are kept source-scoped unless the book supplies a drawing-relevant construction decision and enough evidence to support it.

Hultgren is already canonical and is treated as prior ownership. Where Bammes reaches the same learner decision with a different method, sequence, or tradeoff, retain a variant rather than cloning a card. Where Bammes establishes a more general animal-anatomy foundation, new ownership is allowed and later source reconciliation may relink narrower Hultgren specializations.
