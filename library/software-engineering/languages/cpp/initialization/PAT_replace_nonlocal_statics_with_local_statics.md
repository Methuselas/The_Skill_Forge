---
object_id: PAT_replace_nonlocal_statics_with_local_statics
object_type: pattern
name: Replace Non-local static Objects with Function-Local statics
library_path:
- software-engineering
- languages
- cpp
- initialization
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- initialization
- static_objects
- singleton
cross_links:
- rel: related_to
  target_object_id: PAT_initialize_members_with_init_list
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Replace Non-local static Objects with Function-Local statics

## Pattern Rule
**IF** one non-local static object's initialization uses another non-local static defined in a different translation unit
**THEN** move each object into its own function that returns a reference to a function-local static, and have clients call the functions — because the relative initialization order of non-local statics across translation units is undefined.

## Do
- Convert `extern FileSystem tfs;` into `FileSystem& tfs() { static FileSystem fs; return fs; }` and have callers use `tfs()` instead of `tfs`.
- Lean on C++'s guarantee that a function-local static is initialized the first time control reaches its definition, so the referenced object always exists by the time it is used.

## Don't
- Don't leave a cross-translation-unit static dependency to chance: a `tempDir` whose constructor calls `tfs.numDisks()` may run before `tfs` is constructed, which is undefined and varies by platform.
- Don't assume this is thread-safe — the first-use initialization of a local static can race, so trigger each function during single-threaded startup.
- Don't take this as a fix for destruction order. It pins down when each object is built and leaves teardown on the reverse of that — so of two objects converted this way, the one built first is destroyed last, and if it is the one the other reports to during its own teardown, the reference handed back names an object that is already gone.

## Checklist
- Does any non-local static depend on another defined in a different translation unit?
- Is each such object now reached through a function returning a local-static reference?
- Are those functions invoked during single-threaded startup to head off initialization races?
- Does any of these objects get used during another's teardown, and if so is it guaranteed to still be alive then?

## Notes
This is the "static initialization order fiasco": the standard leaves the cross-translation-unit ordering undefined, and finding a correct order is unsolvable in general once implicit template instantiations enter. The fix converts non-local statics into local statics, whose initialization order C++ *does* pin down — first use. Aficionados will recognize this as the reference-returning core of the Singleton pattern.

The threading caveat that used to attach to this no longer holds and should not be carried forward. Initialization of a function-local static has been required to be thread-safe since C++11 — a thread arriving while another is still initializing blocks until that finishes — so warming the functions up on a single thread at startup is no longer necessary. It remains necessary on a pre-C++11 toolchain, and on compilers offering a switch to disable the guard, which some do for embedded targets where the guard's cost is unwanted.

First use also decides *whether* the object is built at all, which is a second reason to prefer this form over a static data member. A static at class or namespace scope is constructed whether or not the program ever touches it; a function-local one that no execution reaches is never constructed. What you pay for that is a check on entry to see whether construction has already happened.

The fiasco this solves is an initialization one, and converting to local statics leaves the mirror-image problem untouched: teardown runs in reverse order of construction, so a dependency that was safe going up is inverted coming down. Where two of these use each other at all, the one needed late has to be exempted from that order deliberately — `PAT_design_shutdown_for_process_lifetime_objects` owns that decision. The failure is quiet, because the storage outlives the object seated in it and a call against the remains often appears to work.
