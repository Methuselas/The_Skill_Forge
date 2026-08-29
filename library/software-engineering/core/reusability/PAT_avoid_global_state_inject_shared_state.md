---
object_id: PAT_avoid_global_state_inject_shared_state
object_type: pattern
name: Avoid Global State; Dependency-Inject Shared State
library_path:
- software-engineering
- core
- reusability
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- global_state
- reusability
- dependency_injection
- encapsulation
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_reusable_and_generalizable
- rel: related_to
  target_object_id: PAT_use_dependency_injection
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_contain_a_global_behind_access_routines
  variant_name: Contain a Global Behind Access Routines When You Cannot Remove It
  variant_basis: method_sequence
  difference_from_foundation: The foundation removes the global — hold the state in instances and inject them — which is the right answer when it is available. This variant is the containment route for when it is not, in a language without the machinery, in a codebase too large to convert, or for state that genuinely is program-wide. Hide the data inside a class, keep a single instance of it, expose routines to read and change it, and require every other part of the program to go through them. A naming convention makes the requirement enforceable by review where the language cannot enforce it — mark global data with a prefix and forbid any code but its own access routines from touching a name carrying that prefix. Package each global with the class it actually belongs to rather than tipping all of them into one accessor barrel, which otherwise trades the problems of global data for none of the benefits of information hiding. What this buys is a single point of control, one place to put the validity checks every caller would otherwise have to remember, and freedom to change the representation later. What it does not buy is the foundation's benefit — the state is still one shared copy, so two independent uses still collide, and reuse is still blocked.
  when_to_use: Use when the state is genuinely program-wide, such as a mode the whole program runs in or a table every routine consults, and when injection is unavailable rather than merely inconvenient. It also earns its place as a migration step, since a global reached only through routines can later become instance state without touching any call site. A development-only checkout scheme over the routines — refusing a second acquisition while one is outstanding — is a cheap way to surface unexpected sharing during construction, provided it is replaced with something gentler before production.
  when_not_to_use: Do not reach for it while injection is still on the table; wrapping is containment and not a fix, and a wrapped global is still a global. Do not use a global to hold intermediate results of a calculation — compute into a local and assign the final value once, or every reader between the first write and the last sees a value that was never meant to be observed. And do not evade the rule by pouring every variable into one large object passed to every routine; that satisfies the letter of avoiding globals, produces none of the encapsulation, and is harder to reason about than the globals it replaced.
  absorbed_from_object_id: none
---

# Avoid Global State; Dependency-Inject Shared State

## Pattern Rule
**IF** several parts of a program need to share some state
**THEN** hold that state in a value created once per use and handed to the code that shares it — an instance of a class injected where needed, or, where the language has no classes, a structure allocated per use and passed explicitly as a parameter — rather than storing it in global (static) state that every part of the program shares.

## Do
- Make the state instance-scoped: change a `ShoppingBasket` from static variables and functions to an instantiable class where each instance has its own distinct contents.
- Inject the instance into exactly the classes meant to share it, so you control which code shares one basket and which uses a separate one.
- Use separate instances to make reuse safe: one basket for normal products and one for fresh products never interfere, and each view widget shows only its own basket.
- In a language without classes, the same shape is a structure created per use and passed as a parameter to everything that touches it — the context-parameter form that a file handle, a database connection, or a library base already takes. What matters is not the construct but that the state is created per use and reaches the code by being handed to it. A global reachable by name fails that test whatever the language, and passing a pointer to a single global one passes the syntax and fails the intent.

## Don't
- Don't put shared state in a global variable to make it convenient to reach; two features using the same global basket silently pollute each other's contents.
- Don't assume "only one of these will ever exist at a time"; that assumption is exactly what breaks when the code is reused, making global-state code essentially impossible to reuse safely.

## Checklist
- Is the shared state static/global, so every caller sees the same single copy?
- Can two independent uses of this code run without interfering through shared state?
- Is the state injected so you control precisely which code shares which instance?

## Notes
Global state encodes a particularly costly assumption — that a single shared copy is always what everyone wants — and Long's `ShoppingBasket` shows it collapsing the moment two parts of the app need independent baskets. Converting the static class to instance state plus dependency injection makes each basket self-contained and reuse safe. This is why the chapter treats global state as best avoided in most scenarios, and it leans directly on the dependency-injection technique from chapter 8.

`VAR_contain_a_global_behind_access_routines` covers the case this card does not — the global you cannot remove. Hide the data in a class, keep one instance, expose routines to read and write it, and require everything else to go through them; where the language cannot enforce that, a prefix convention on global names plus a rule that only their own access routines may touch them makes it reviewable. The honest accounting is that this is containment rather than repair. It gives you one place to change the representation, one place to put the checks each caller would otherwise have to remember, and a path to converting the global into instance state later without touching call sites — but the state remains a single shared copy, so the foundation's actual benefit, two independent uses that cannot collide, is not available.

Two failure modes McConnell names are worth carrying whether or not you take the variant, because neither is obvious. The first is aliasing: pass a global as an argument to a routine that also reads it directly, and one variable now has two names inside that routine, so a parameter set to zero and a global computed from it five lines later both read as the same value and the routine's output makes no sense. The second is initialization order — in languages where the order across separate files is undefined, one global initialized from another that lives in a different file has no reliable value, and the workaround for it is intricate enough to serve as an argument against the arrangement that required it. He also warns against the disguised version, in which every variable is poured into one large object and passed to every routine; that avoids the word global while keeping all of its costs and acquiring none of encapsulation's benefits.
