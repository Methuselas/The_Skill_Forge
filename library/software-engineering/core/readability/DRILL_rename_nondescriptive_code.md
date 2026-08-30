---
object_id: DRILL_rename_nondescriptive_code
object_type: drill
name: Rename Nondescriptive Code and Drop the Redundant Comments
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- readability
- refactoring
- comments
cross_links:
- rel: teaches
  target_object_id: PAT_use_descriptive_names
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: replacing cryptic names with descriptive ones and removing comments they made necessary
references: []
variants: []
---

# Rename Nondescriptive Code and Drop the Redundant Comments

## Practice Task
Take a snippet with single-letter names propped up by comments, rename everything descriptively, and delete the comments the names made unnecessary.

## Target Skill
Turning cryptic, comment-dependent code into self-explanatory code through naming.

## Setup
No special setup required.

## Instructions
1. Start from code with opaque names — a `class T` holding `pns` and `s`, with a function `f(n)` and a free function `s(ts, n)` — and comments explaining each.
2. Read it cold and note every place you had to consult a comment or the class body to understand a name.
3. Rename each class, function, variable, and parameter for the concept it represents (team, player names, score, contains-player, team-score-for-player).
4. Remove each comment that now merely restates a name, keeping only any that document genuine usage.
5. Re-read a call site in isolation and confirm it is clear without opening the class.

## Success Check
- The places where a comment or the class body had to be consulted are written down before renaming, and each is matched afterwards to the name that removed the need. A rename with no recorded confusion behind it is a preference rather than a finding.
- At least one name is judged with the code out of sight and accepted, or the absence of such a name is stated. Names read in place are judged with context the next reader will not have, which is the failure this step exists to catch.
- The call site is re-read cold and what it now says is written out. If understanding it still requires knowing the class's contents, the naming is unfinished regardless of how the names look in isolation.
- Every deleted comment is accounted for as a restatement of a name, and every surviving comment has the information it carries named. A comment kept in case it is useful is what this bullet catches.
- The result is checked for the opposite error — a name long enough that callers will abbreviate it, or specific enough that the next requirement makes it wrong.

## Common Failures
- Renaming but leaving the now-redundant comments, keeping the clutter and the sync burden.
- Half-descriptive names that still need a comment to be understood.

## Notes
This is Long's `T`-to-`Team` transformation as practice. The habit it builds is to reach for a better name before reaching for a comment, and to delete comments that a good name has made redundant so the code carries its own explanation.
