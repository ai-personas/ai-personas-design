# Fragment-persona acceptance and requirement mapping

[Persona network](../design/FRAGMENT-PERSONA.md) · [Recall acceptance](FRAGMENT-RECALL.md) · [Requirement index](../implementation/REQUIREMENTS.md)

## Status and revision meaning

These are specified cases, not reported passes. Existing FP-M01–FP-M16 and FP-B01–FP-B07 identifiers are retained. Their tree-specific setup is replaced by graph-based setup, and the no-extra-authoring-call rule now explicitly distinguishes optional semantic selection from generative memory writing. Earlier evaluation outcomes keep their original evaluator revision; this edit does not retroactively change a pass or failure.

The graph has no canonical root, required parent, function grouping, or automatic weight reinforcement. Current self-fragments are consistently included by policy, not made graph ancestors. Fragment interpretation, event evidence, selector assessment, actual inclusion, and demonstrated benefit remain different claims.

## Requirement traceability

| Existing requirements | Refinement | Cases |
|---|---|---|
| PER-01–PER-03, PER-05 | Provenance, current self-model, character-conditioned authorship, and model-independent identity. | FP-M01–FP-M03; FP-B01, FP-B07 |
| MEM-01–MEM-02 | Observation versus interpretation, same-call authoring, connection conditions, correction, and exact revisions. | FP-M03–FP-M07; FP-B02–FP-B04 |
| MEM-03–MEM-04 | Direct and delegated recall, event entry points, work isolation, and required context. | FP-M08–FP-M12; FP-B05 |
| MEM-05, EVD-05 | Assessed transfer instead of volume or favorable self-description. | FP-B02–FP-B05, FP-B07 |
| COL-01–COL-04, SOC-03 | Directional social memory, independent judgment, and actual acceptance. | FP-M13; FP-B03–FP-B04, FP-B06 |
| PER-04, GOV-01–GOV-04 | Authorship controls, lifecycle, bounded activity, and visible selector costs. | FP-M02–FP-M03, FP-M12, FP-M15 |
| SYS-01–SYS-04, ACT-03–ACT-04 | Atomic adoption, current authority, restart, and observation-bound effects. | FP-M04–FP-M07, FP-M14–FP-M15 |
| UX-01–UX-02, OSS-01 | Private derivatives, readable inspection, and versioned claims. | FP-M10–FP-M12, FP-M16; all reports |

## Mechanism acceptance

| Case | Required observation |
|---|---|
| FP-M01 — Bootstrap and self-model | Supplied and generated starting profiles retain provenance and explicit zero traits. The first ordinary work call can author self-fragments without another writer. Current character and historical seed are distinct. |
| FP-M02 — Locked and evolving self | Test self-authorship on and off. Protected self-fragments and traits cannot be edited through another label. Ordinary methods and relationships may change. Accepted identity changes fence stale dependent actions. |
| FP-M03 — One combined decision | Count actual primary and auxiliary dispatches separately. Work and graph authorship use one primary response. No hidden reflection or relationship writer exists. No-change is valid. Optional selectors have explicit permission and accounting. |
| FP-M04 — Evidence timing | Sending a message or requesting a check can produce a tentative intention, not a claimed future result. Only received observations can support the subsequent interpretation. |
| FP-M05 — Atomic graph and selection | Create several connected fragments, a correction relation, and future selection without parents or categories. One invalid reference rolls back the whole change set and preserves independent work's original context. |
| FP-M06 — Consolidation and correction | Generalize episodes while preserving limitations and evidence. Retire obsolete interpretations with coherent incoming-link dispositions. Exact historical versions remain attributable. |
| FP-M07 — Concurrent work and replay | Competing primary writers cannot silently overwrite persona state. Auxiliary selection is not primary authority. Exact retries return original receipts without duplicate fragments or effects. |
| FP-M08 — Explicit selection versus delegation | A discovery match stays a preview without an applicable delegation. Valid bounded delegation can supply full text. Expiry, disablement, preview-only choices, and bootstrap attribution remain explicit. |
| FP-M09 — Unexpected event recall | A real reply from a known participant seeds relevant recall in the next ordinary request. No extra generative retrieval planner runs. Record whether an optional selector contributed. |
| FP-M10 — Cross-work boundaries | New work has its own handoff and event entry points. Only permitted reusable material crosses over; old private focus, withheld fragments, and other owners' cards do not leak through indexes or caches. |
| FP-M11 — Recall channels and invalidation | Test exact references, entity lookup, labeled text search, conditional graph traversal, and optional semantic assessment. Revocation invalidates descriptions, edges, cached results, and derived indexes before disclosure. |
| FP-M12 — Whole-request budget | Current character, necessary observations, selected full text, and essential exceptions survive or admission blocks explicitly. Selector and primary exposure are both accounted for. |
| FP-M13 — Social interpretation is not authority | Distinguish reports, copied claims, later demonstrated help, decline, and nonresponse. Do not invent global expertise, commitment, consent, or a punitive reputation from a fragment. |
| FP-M14 — Injection and stale adoption | A fragment or message cannot broaden access, rewrite locked character, or turn a recall condition into executable effects. Current permissions and versions are rechecked after selection. |
| FP-M15 — Stopping and cost | Deferred opportunities do not cause idle model calls. Optional exploration, selector attempts, and recovery remain bounded. Failures and uncertain usage are not silently free. |
| FP-M16 — Inspectable evidence | Show the actual graph, condition and version, direct/delegated/preview origins, committed changes, provider-bound inclusion, and assessed outcomes. No invented selector explanation or private reasoning archive is required. |

The [recall suite](FRAGMENT-RECALL.md) adds detailed shortlist, batching, auxiliary-role, cache, privacy, and failure cases. Documentation checks cannot substitute for these runtime tests.

### Compact preservation across the first decision — FP-M05, FP-M10, FP-M12

Exercise the first compact response, not only a response after run-local state is already populated. Give a new participation permitted, explicitly designated identity anchors, ordinary records, selected receipts and a handoff. Separately test an invitation with already-selected owned seed fragments before it has a materialized graph plan. A preserve/null choice must retain the effective selection supplied to that decision, including the owned fragments and their required qualifications; absent run-local fields must not be mistaken for an explicit empty choice.

Test replacement and preservation independently for records, receipts, full memory selection, handoff and retrieval query. Explicit empty arrays or strings clear the corresponding choice. An existing work-local selection, including an empty one, overrides identity defaults. Unscoped historical context and another participation's private focus are not inherited. Preserving full identity anchors must not silently authorize identity-level recall delegation, navigation or a self-model change in the new work. Membership and funding remain unchanged.

Reopen the durable store between the first and second decisions and inspect the actual provider-bound context as well as the committed selection. A preserved but now missing, unreadable, stale or unreceived required reference must fail visibly and atomically under the existing rules; it must not be silently dropped to make the response succeed. An explicit valid replacement can repair the selection. Confirm that preservation creates no new fragment, observation, provider call or automatic acceptance.

For a paired efficiency check, hold the task, model, evidence, permissions and stopping rubric fixed. Compare compact preservation with explicitly restating the same valid choices. Require equivalent supplied evidence and delivered outcomes, and count all primary, repair, rediscovery and authorized selector usage. A smaller prompt caused by accidentally losing an anchor is a correctness failure, not an efficiency gain. Store-transaction tests, compiler tests and live task/token results remain separately reported evidence; this specification reports no executed pass.

## Behavioral acceptance

### FP-B01 — Character in fragments and actions

Vary declared character under matched tasks, observations, tools, and budget. Use name-swap, self-model-withheld, and neutral-wording controls. Assess authored meaning and actual checking, consultation, challenge, and stopping, not trait mentions. Test locked-character conflicts in ordinary prose. Different personas may appropriately choose the same action when evidence is decisive.

### FP-B02 — Later procedural transfer

Compare retained relevant fragments, genuinely withheld equivalent information, and fresh personas on held-out related tasks. Freeze model and total resources. Check leakage through descriptions, connection conditions, self-summaries, files, caches, and peer messages. Inspect actual recall and application before crediting an outcome to memory.

### FP-B03 — Learning whom to consult

Use distinct synthetic peers with inspectable contributions but no prescribed professions. Later tasks test useful contact choice, focused questions, and scoped interpretations. Include wrong advice, unavailability, and decline. A familiar name or universal expert label does not demonstrate social learning.

### FP-B04 — Harmful memory and social correction

Provide an attractive inapplicable method, an overconfident relationship interpretation, and copied claims from one source. Supply a consequential contradiction. Observe qualification, revision, or rejection and improved later use, rather than automatic reinforcement of a selected fragment.

### FP-B05 — Retrieval under memory growth

Grow an ungrouped graph with a fixed prompt budget, old relevant nodes, new distractors, conditions, exceptions, and isolated material. Compare deterministic recall with optional semantic selection. Measure candidate recall, full inclusion, qualification coverage, duplication, latency, compute, and downstream work separately.

### FP-B06 — Small-society continuity

Run bounded shared activities with actual offers, acceptance, messages, disagreement, handoffs, and departure. Inspect each persona's private authored interpretations and deliberately shared practices. Believable interaction, useful delivery, legitimate acceptance, and human consent remain distinct. No global private-memory merge or hidden coordinator is introduced.

### FP-B07 — Longitudinal maturity and model changes

Compare fixed initial and fragment-developing personas over a task sequence and held-out work, accounting for all primary, selector, retrieval, and tool costs. Record useful generalization, repeated mistakes, recovery, consultation cost, and context growth. Repeat under declared model configurations. More fragments, higher confidence, or changed traits are not maturity by themselves.

## Reporting and release gates

Predeclare rubrics, tasks, seeds, isolation, and repetitions, retaining applicable minima from the existing development acceptance rules. Report variation, failures, and limits on model revision pinning. Voice, selection quality, mechanism execution, provider receipt, social behavior, and independent work improvement are separate claims. The supplemental identifiers do not expand the 45 active requirements or authorize a deployment.
