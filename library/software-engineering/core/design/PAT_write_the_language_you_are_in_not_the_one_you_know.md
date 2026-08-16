---
object_id: PAT_write_the_language_you_are_in_not_the_one_you_know
object_type: pattern
name: Check You Are Not Writing Your Previous Language in New Syntax
library_path:
- software-engineering
- core
- design
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- language_choice
- idiom
- transfer
- design
- code_review
cross_links:
- rel: related_to
  target_object_id: PAT_program_into_the_language_not_in_it
- rel: related_to
  target_object_id: PAT_adopt_language_features_when_best_tool
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Check You Are Not Writing Your Previous Language in New Syntax

## Pattern Rule
**IF** you are writing in a language you know less well than one you know deeply
**THEN** inspect the result for constructs you reached for because your stronger language has them, and for capabilities of the current language you have not touched at all — code that compiles is not evidence that it is written in this language.

## Do
- Read your own output asking which language it was really written in. The failure is invisible from inside because every individual line is valid; it shows only in aggregate, as a shape belonging somewhere else.
- Look specifically for imported bad habits. The reported pattern is programmers stretching the new language to emulate the *worst* features of the old one — reaching for gotos and global data in a language that offers better — rather than importing its best.
- Inventory what you have not used. A language's distinguishing capabilities going entirely untouched across a whole component is the stronger signal, and it is the easier one to check.
- Treat the vocabulary as the constraint it is. The words a language gives you for expressing a thought shape how you express it and may determine which thoughts you form at all, so a construct you have no name for is one you will not reach for unprompted.
- Spend the familiarity where it pays. Three or more years in a language is worth roughly 30 percent productivity over equivalent engineers new to it, which is the size of the gap you are working against when you write in an unfamiliar one.

## Don't
- Don't take compiling, passing tests, and reviewing cleanly as evidence you have used the language. Disguised code satisfies all three.
- Don't conclude the language is deficient before checking whether you have looked for its facility. The judgment that a language cannot do something is unreliable from inside a stronger language's habits.
- Don't fix this by importing idioms wholesale either. A construct still has to be the best tool for the job at hand, not merely native to the language.

## Checklist
- If this file were shown without its extension, which language would a reader guess it was written by someone fluent in?
- Which capabilities of this language does the component not use at all, and is that a decision or an absence?
- Are there constructs here that exist because your other language would have needed them?
- Did you check whether a facility exists before working around its supposed absence?

## Notes
The mechanism is a linguistic one, and McConnell borrows it deliberately: the Sapir-Whorf hypothesis holds that the ability to think a thought depends on having words that express it, and that without the words you may not be able to formulate the thought at all. Applied to programming, the vocabulary a language supplies determines how thoughts get expressed and plausibly determines which get expressed. That is why the failure is not laziness — the missing constructs are not being rejected, they are not being generated.

The documented case is a team writing a new system in C++ from Fortran backgrounds, producing code that compiled as C++ while being Fortran underneath: emulating Fortran's weakest features and leaving C++'s object-oriented capabilities untouched. The pattern has been reported across the industry for decades, so it is a structural consequence of moving between languages rather than a story about one team.

The counterpart failure sits next door and needs the opposite correction. Reaching for a language feature because it is new and impressive is over-adoption; this is under-adoption caused by a prior habit. Both are cured by asking the same question — is this construct the right tool here — but only after you have noticed there was a choice.
