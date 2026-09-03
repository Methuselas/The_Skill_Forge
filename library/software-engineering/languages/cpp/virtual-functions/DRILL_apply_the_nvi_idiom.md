---
object_id: DRILL_apply_the_nvi_idiom
object_type: drill
name: Apply the Non-Virtual Interface Idiom
target_skill: Wrapping a public virtual in a non-virtual function with controlled context
library_path:
- software-engineering
- languages
- cpp
- virtual-functions
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- virtual_functions
- nvi
- template_method
cross_links:
- rel: related_to
  target_object_id: PAT_wrap_virtuals_with_nvi_idiom
- rel: related_to
  target_object_id: PAT_dont_call_unknown_code_while_holding_a_lock
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Apply the Non-Virtual Interface Idiom

## Practice Task
Given a class with a public virtual `healthValue`, convert it to the non-virtual interface idiom so the base controls the context around the call.

## Target Skill
Turning a public virtual into a public non-virtual wrapper around a non-public virtual.

## Setup
No special setup required.

## Instructions
- Make `healthValue` a public non-virtual function and add a private virtual `doHealthValue` that does the real work.
- Have the wrapper call the private virtual, adding before-work (check invariants and preconditions) and after-work (verify postconditions).
- Decide whether the wrapper may also hold a lock across the dispatch, and write down which case you are in: it may where every override lives in this component and its locking is visible to you, and it may not where an override could be supplied by a caller. Where it does hold one, enumerate every override that can run under it.
- Override `doHealthValue` in a derived class and observe the wrapper's before-work and after-work running around it.
- Attempt both wrong forms — a client calling the virtual, a derived class overriding the wrapper — and record the compiler's rejections.
- Decide the virtual's access level against whether overrides call the base version, stating the reason rather than taking the default.
- Name what the idiom costs — an extra function per customization point and a pair of names to keep aligned.

## Success Check
- Clients can call only the wrapper and derived classes can override only the virtual, checked by attempting both wrong forms and recording the compiler's rejections.
- The wrapper's before-work and after-work are observed running around an override supplied by a derived class, rather than concluded from how the code is arranged.
- If the wrapper holds a lock across the dispatch, every override that can run under it is enumerated and each one is inside this component; if any could come from a caller, the lock is outside the dispatch instead. An unanswered question here is a deadlock that appears only once somebody else supplies an override.
- The virtual's access level is decided against whether overrides call the base version, with the reason stated rather than the default taken.
- The run names what the idiom costs — an extra function per customization point and a pair of names to keep aligned — so it is priced rather than adopted wholesale.

## Common Failures
- Leaving the virtual public, so clients bypass the wrapper's context.
- Assuming a private virtual cannot be overridden — it can; only calling it is restricted.
- Locking a mutex in the wrapper without asking where the overrides come from. The wrapper fixes when the virtual runs, not what it does, and an override supplied from outside the component can take locks of its own.

## Notes
This drills Item 35's NVI idiom (a Template Method form): derived classes control how via the private virtual, the base controls when via the wrapper.
