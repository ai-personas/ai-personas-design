# Why it keeps needing patches — structural review, 2026-09-04

Seven independent read-only audits over the code (142,128 lines under `src/personaos`), the design, the tests, and every run root on the host, commissioned after a week in which each live run produced a new fix and each fix was correct and local. This document answers the owner's question, records the evidence, and names the program that would end the series. It records decisions for nobody; the design owner decides.

## 1. The answer

The patches are not symptoms of missing design. The design states the right rules, most of them clearly and early: an absent or failed mechanism is a stated fact, never a silence (C-OP-14, 2026-08-18); a cursor handed out in a prompt must mean something when the persona hands it back (the blackboard lane's own docstring); no invented bounds (ADR-0110); an unreadable source is stated, never zeroed; a settle is a completing append, never a sweep. The patches are the signature of **rules that have no carrier in code**. Each rule lives in prose, a docstring, or a per-schema footnote, and the code offers hundreds of independent places to break it: 589 hand-built refusal dicts in 61 shapes, 22 prompt lanes that mint cursors by hand, 16 memo containers with 5 key schemes, 26 text-bounding functions in 5 units, 288 exact-shape checks, 61 hand-maintained JavaScript field lists, and 384 exception handlers that swallow an unreadable source into the zero of its type. A live run finds the next site where a hand-written dict, integer, or frozen set disagrees with the prose; the fix is another hand-written dict, integer, or frozen set, plus a test that pins the fix's text. The sibling site that was not exercised keeps the old behaviour, and the next run finds it.

Two numbers carry the whole argument. Of 225 fix items since 2026-08-28, **56 percent are statedness defects and 28 percent are two sites implementing one projection differently**, and both classes continued at the same rate after the rule for each was written, in new code by the same authors, in the same week. And this week's own fixes, written under the no-invented-bounds rule, added newest-8, newest-16, 64, 600 and 3600 as bare integers with no provenance: the class re-created itself inside its own remedy.

## 2. What the runs show

Signed lineage only, every root on this host.

| run | model | net calls | turns | execs | posts (refused) | lessons (deliberate) | names | births | caps built / invoked | inventory reads | artifacts | receipts | settle |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| e40c 09-02 | luna | 80 | 104 | 226 | 14 (0) | 81 (71) | 8 | 0 | 3 / 67 | 3 | 34 | 0 | operator stop |
| e40s 09-02 | luna, lone seed | 33 | 21 | 11 | 0 | 5 (3) | 1 | 1 | 2 / 3 | 1 | 0 | 0 | — |
| e45 09-02 | qwen | 111 | 88 | 12 | 13 (23) | 5 (5) | 6 | 0 | 2 / 0 | 0 | 0 | 0 | exhausted |
| e45b 09-02 | qwen, task 2 | 46 | 83 | 43 | 28 (41) | 8 (7) | 1 | 0 | 0 / 0 | 0 | 0 | 0 | exhausted |
| e46 09-02 | luna | 104 | 241 | 296 | 52 (2) | 155 (109) | 8 | 0 | 10 / 29 | 9 | 56 | 2 | exhausted |
| e48 09-02 | qwen | 103 | 50 | 10 | 12 (18) | 5 (1) | 5 | 0 | 2 / 0 | 0 | 0 | 0 | exhausted |
| e48b 09-02 | qwen, task 2 | 47 | 55 | 21 | 22 (0) | 5 (3) | 2 | 0 | 0 / 0 | 0 | 0 | 0 | exhausted |
| e49 09-03 | qwen | 106 | 130 | 32 | 123 (0) | 11 (9) | 5 | **1** | 1 / 0 | 0 | 0 | 0 | exhausted |
| e50 09-03 | luna | 89 | 968 | 164 | 29 (0) | 64 (54) | 8 | 0 | 2 / 23 | 8 | 29 | 0 | exhausted, 15 h late |

What a substrate rule moved, and held: refused posts on qwen went 23, 41, 18, then 0, 0, 0 once the schema declared its content member required. What a statedness fact moved: inventory reads went from zero on every run to 8 and 9 on luna once the acquisition surface was stated every turn; luna's cohort went from provisioning capabilities it never invoked to a shared verifier invoked 23 times by seven personas. What emerged unprompted: e49 admitted the first birth of any cohort run since early August. What did not move: receipts and mints are zero on every run but one; the independent audit of e50, the strongest run, met one of nine operator bars (the solid is watertight and byte-reproducible from source, everything else is a label); the cohort probed for FreeCAD, Blender, trimesh, numpy and scipy across eight inventory reads and attempted zero installs with zero denials. That last fact is the acquisition question answered: the path was open, stated, and unused, and it is a model limit, not a substrate constraint.

## 3. The anatomy of the fix log

225 fix items since 2026-08-28, one primary class each.

| class | items | share |
|---|---|---|
| B — two sites, one projection (writer vs reader, prompt lane vs read action, node vs UI, sibling lanes) | 64 | 28% |
| D — a silent state (no record when a mechanism failed or a run stopped) | 44 | 19% |
| I — a path that had never executed (no caller, never defined, never run to completion) | 33 | 15% |
| G — genuine new capability | 23 | 10% |
| A — a refusal stating a slug but not its recovery or members | 20 | 9% |
| C — an invented bound | 18 | 8% |
| H — a working mechanism stated nowhere a persona reads | 8 | 4% |
| F — a model-tier limit misread as substrate | 6 | 3% |
| S — soul iteration | 6 | 3% |
| E — an additive member breaking an exact-field reader | 5 | 2% |

A and D together are 64 items, the same size as B; together they are 56 percent of everything. Class I is a sibling of B: a second copy nobody ran. Class E is small in count and large in effect: every one of its five items was a blank member view or a deployment-wide refusal.

## 4. The six mechanisms that manufacture patches

### 4.1 A refusal is a convention, not a type

589 `ok: False` sites across 73 tools, in 61 distinct member sets; 361 are bare `{ok, error}`. Only 7 of 589 carry a code, a `retryable` boolean, a recovery, and a stage together. Eight different member names carry "the code". The member a persona needs most, whether to retry, is written by 22 handlers, defaulted to false by the node on the other 567, and carried to lineage by none. 478 of 589 (81 percent) reach lineage as nothing but a slug of their leading words. Six reach lineage as nothing at all. The one fix that named received and recognised members (e45) has 17 unfixed siblings, eight of which glue the names into prose after a colon so the slug rule deletes them by construction. The corpus test asserts only that a slug exists, which is the floor the owner is describing.

### 4.2 The cursor invariant lives in a docstring

Of 22 prompt-visible lanes that mint cursors, 3 have an accepting read action, 2 have an acceptor that can never validate (persona cards and brain fragments hash a different builder under a different namespace), 1 names an action whose schema refuses the argument, and 16 have no acceptor at all, two of them mandated by the design. Four cursor grammars coexist. Eight read actions still refuse a stale cursor with prose that projects to `{"ok": false, "code": "mcp_tool_refused"}` on the next turn: the word "cursor" does not survive. The fixed pending-communication lane is guaranteed stale across turns by its own carriage mark, and its recovery sentence asserts a cause ("records have been appended since") that was not the cause. The pager mints cursors for anyone, binds them to whatever rendering it is given, raises a bare `ValueError`, and does not know whether an acceptor exists.

### 4.3 Every cross-cutting concern is hand-implemented per lane

The monolith split (ADR-0112 cut 3b) moved definitions byte-identically, by name-family, so it relocated the duplicates without merging any. Verified lineage reads: 146 call sites, 106 fold a whole kind bucket per call with no memo, and 16 memo containers use 5 key schemes and 8 eviction rules across 8 files; the substrate's own kind-scoped primitive is used by 4 of them, and the export path's memo is still keyed on the whole environment generation, which the resume path's comment already says "made this memo miss every time". Text bounds: 17 Python functions in 12 files with 67 distinct limits and 9 JavaScript functions, in 5 units, 6 control-character policies and 3 rules for DEL; one live writer/reader disagreement stands today (the cognition writer keeps DEL and counts code points, the reader rejects DEL and counts UTF-16 units, and one bad character refuses the whole document). Exact shapes: 288 `set(x) != fields` checks, 120 of them against inline literal sets. Degraded reads: 430 stated, 384 swallowed silently into `{}`, `[]`, `None` or `0`; the member-view modules are 0 stated, 9 silent. The acquisition summary is folded twice per turn and discarded once; the settle fact is folded three times per parking append.

### 4.4 The UI contract turns every additive member into a two-language patch

61 hand-maintained JavaScript field lists verified by "sorted keys must equal this list", 4 hand-maintained Python shape tables, none generated from the other, one regex test covering one pair of about 24. This month every additive member cost a version bump plus edits in two languages plus a public cut, and every missed second edit became a silent blank. Two are live today: the **project view has been broken for 27 days** (a member was removed from the topology record on 2026-08-08; the UI still demands it and pins export/2; the error message tells the operator to republish with a version no node emits), and the **operator thinking drawer has been blank for 19 days** behind a `/2` pin against a `/3` emitter. Reproduced in-process: the next additive scorecard member drops the document back into the generic anonymous scan, which refuses the entire persona record because a counter name contains the token `record`. Exactness is not what carries the security property: the signature already covers every present member; the two real hazards, locator smuggling and content leaking on anonymous surfaces, are properties of a member, not of the set, and the codebase already enforces them member-wise where it works.

### 4.5 Observability is keyed to cause, and causes multiply faster than fixes

The e50 luna run: the provider hit its usage limit at 17:19Z on 09-03. From then until the settle at 08:32Z on 09-04 the run made zero persona-authored appends while writing 10,670 lineage records, 25 MB, and 4,190 content-store objects, 729 MB; after the settle, all eight prepaid learning wakes and all eight rewake fires were delivered into a provider the router knew was in cooldown. The mechanics: a 402 is classified correctly as quota exhaustion at one seam and then laundered into the retryable class at the next, because the swallow site propagates only two codes and the consumer has two arms; the manager's outbox replay has a 30-second backoff cap, no attempt cap, and never consults the router's cooldown, while the node's causal-delivery path got both from ADR-0109 — the fix landed on one of two retry paths; refused calls do not tick the budget, so the only clock that could stop the spin did not run; the liveness observer is fed paused rows only, and a run with a `running` shell registered as live is excluded three times over; and the provider's refusal text appears zero times in 12,653 lineage records and 5,907 content objects. The `/status` streak reads zero because refusals in cooldown never reach the increment and any unrelated success resets it. Every earlier silent-death fix stated one predicate at one site for one scope; three retry paths, two failure channels, two run states and N provider behaviours make every unenumerated combination silent by construction.

### 4.6 The tests protect the wrong layer

589 tests: 51 percent drive real code, but leaf code (ledgers, parsers, envelopes); 28 percent replace the collaborator with a hand copy of what the code expects (one fake lineage reader pasted across eight files, five files hand-building the dispatcher's reserved keyword arguments; fourteen tests execute no source logic at all); 18 percent assert that a literal is still present in a file. Zero tests execute JavaScript, boot a node and let a heartbeat run, read a recorded run root, hand a prompt lane's cursor to a read action, or call a handler through the real model-call lane. Every one of this month's nine incidents was a disagreement between two real parties, and no test puts two real parties in the same room. This week's fixes added tests at the same layer: pins and stubs, and one test whose expectations are the browser's rules re-typed by hand. Under that test, today's tree carries a divergence with the suite green: a lesson body of only Unicode whitespace or a byte-order mark is published as included and rejected by the reader, blanking the card.

## 5. The design side: rules without carriers

| rule the fixes keep re-applying | stated | enforced by | rating |
|---|---|---|---|
| a refusal states reason, members, recovery, truthful `retryable` | C-OP-14 (that a failure is stated, not which members); 09 §13 for two paged lanes | slug carriage helper; corpus test for slug existence; everything else per site | partial |
| one projection for prompt lane and read action | 09 §4.3; 09 §13 footnote; a docstring | two read-action tables; a test that pins one table's arguments; nothing pins projection equality | partial |
| no invented bounds | ADR-0110 standing rule + queued inventory | carrier family only; no bound registry, no provenance, no scan; 340 module-level numeric constants; ADR-0110's own queue still live at ≥8 sites | convention |
| additive members never break readers | 09 §12–13 implies free; C-OP-16 and the scanner mandate exact closed shape | 288 checks, 107 frozen sets, 61 JS lists; no test that every additive member is admitted by every closed reader; **two contradictory policies with no rule saying which applies where** | convention |
| unreadable is stated, never zeroed | C-OP-14; 10 §5 | scorecard dependency closure only; 430 stated vs 384 silent elsewhere | partial |
| a settle is a completing append, not a sweep | 03 §10; 10 §4.5; ADR-0112 | one predicate, one writer, one lock, three completing appends — each added after a live run failed to settle | mechanical for known sites, convention for completeness |

The design validates its criteria by manual walk and live run and says in so many words that suites are hygiene, not evidence (11 §4: "no criterion is supported by a test id"). The consequence is that no rule has an owner in code. 09 §13 is a registry by name and an accretion log by content: 89 percent of the 803 schema identifiers in code are not in it, its longest bullet holds ten dated "2026-09-0x" notes, and the version bumps it records manufacture dual-accept readers, which are two-site divergences by construction.

## 6. What would end the series

Six structural changes, ranked by the fix classes they remove. Every one states more and adjudicates nothing; none prices, ranks, coerces, or reads intent or domain words; the bound registry removes artificial constraints rather than adding any. Costs are the reviewers' estimates.

1. **One refusal type, registry-backed.** A single constructor `refuse(reason_code, *, stage, retryable, recovery, received=, recognized=, exception=)` whose field set is the allow-list the carriers read, and a corpus test over all lanes that refuses any `ok: False` not built by it. Removes class A and the refusal half of D (about 40 items) and makes "stated but not carried" unconstructible. Builder plus carriage plus ratchet about a day; codemod of 571 direct returns a day; `retryable` judgment on about 120 sites two to three days.
2. **One schema table generating both readers.** `public_schemas.py` = {schema: required, optional, bounds}, used by the emitters (assert the emitted set before signing), by the anonymous scan, and emitted as a generated JSON the UI reads or is tested against. Verifiers become signed-closed, verify-open, render-closed: unknown signed members are admitted as opaque bytes and never rendered or dereferenced; the locator rule moves to the producer, which refuses to sign what the scan would refuse; arrays of independently checkable rows degrade per element. Removes class E and the node/UI half of B; would have prevented five of this month's six contract failures. About 300 lines Python, 150 JavaScript, one parity test; two to three days.
3. **A cursor contract owned by the pager.** Sequence identity required (a rendering can never be the identity), one namespace registry (namespace → schema, read action, arguments) replacing the four tables, the pager refusing to mint a cursor for an unregistered namespace (it states a count, not an offer), one refusal shape returned never raised, and one parametrised test that walks the registry: mint, hand back, read, then again after the lane's state transition. Removes the paging half of B across 19 lanes and 8 refusal sites; +150 lines, −340 lines of hand-rolled parsers, about 25 call sites in 14 files.
4. **One verified-read-with-memo helper and one text-bound table.** Kind-scoped by default through the substrate's own generation primitive, never memoising an unreadable read; one table (schema, field, unit, limit, control policy, trim) generating the Python bounders and the JavaScript validators. Removes the memo and bound halves of B, which are the ones that recurred as "never hits" and "blank view". These two are merges of behaviours that differ, so they are the one place where choosing one behaviour is the change; stage one container and one family at a time.
5. **One progress observable for every run.** At the heartbeat, for every run in the registry and every paused row alike: when there is grant headroom, or live carriers, or pending deliveries in either registry, and no persona-authored append has landed for N beats, state `RUN_PROGRESS_STALL_OBSERVED` carrying seconds since the last such append, the unparked members and their dispositions, pending deliveries from both registries, the router's cooldown, streak and last refusal, the refused-turn count, and active call ages; deduped on transition and re-stated every M beats so "still stalled" is never silence. It wakes nobody. Two mechanical fixes fall out of the same evidence: honour the sink's own exhaustion classification for a 402 so replay is denied, and make every fire path consult the cooldown the router already knows. Together these remove class D's silent-death half; the observable is what ends it, the two fixes are the next patches.
6. **Tests that cross the seams.** A dispatch harness through the real model-call lane (covers the stamp, the receipt gate, and turns the refusal corpus into "call every tool with one invented argument"); a Python↔JavaScript contract test that loads the vendored script in Node and feeds it the real exporters' documents plus a property corpus (feasible today under a 15-line shim, and it found three divergences in one afternoon); producer→consumer round trips over real objects for every pointer pair and every exported document through the real scan; and an offline replay harness over a recorded run root with a fake clock for settle and liveness invariants, the only mechanism that reaches the silent-for-an-hour class.

Design documents that should change from prose to contract: 09 §13 becomes a machine-readable registry from which the closed sets, the scanner shapes, the UI lists and the read-action tables are generated or diffed, with one stated reader policy per record class and the run journal moved to 13; C-OP-14 gains a refusal record in 09 §13 that every refusal is; P-7 gains a bound registry with provenance ∈ {measured, declared, protocol-exact, absent}; 11 §4 keeps "tests are not evidence of usefulness" and drops "no criterion is supported by a test id", each criterion naming its guard or being marked convention; 03 §10 lists the completing appends as a closed set the code is pinned against; 14 records decisions and nothing else.

## 7. Defects this review found that are open today

Small, mechanical, and covered by the program above; listed so they are not lost.

- The project view: topology `status` removed on 2026-08-08, UI still requires it and pins export/2 (27 days).
- The operator thinking drawer: `/2` pin against a `/3` emitter (19 days).
- Unicode-whitespace-only and BOM-led lesson bodies: node includes, reader refuses, card blanks.
- The 402 laundered into the retryable class; the manager outbox never consulting the cooldown; refused calls never ticking the budget.
- The liveness observer fed paused rows only; its record carrying no provider member; dedupe by hash making an unchanged stall silent forever.
- The cognition writer keeping DEL and counting code points against a reader that rejects DEL and counts UTF-16 units.
- The export budget memo keyed on the whole environment generation.
- The scanner's next-member trap on the scorecard document.
- Six refusals reaching lineage as nothing; 17 argument-shape refusals not naming members, 8 of them gluing names into prose after a colon.
- A vendored release manifest declaring the wrong source commit; the repository's launch script serving a UI checkout with no member view.

## 8. A note on this week's own contribution

The reviewers found this week's fixes in the same pattern they were diagnosing: a text bound re-typed from the browser by hand rather than shared; a count computed after truncation; bare integers added under the rule that forbids them; and tests that pin the fix's literals. Every one of those was caught in review before it shipped, which is the process working; that they were written at all is the point of this document.
