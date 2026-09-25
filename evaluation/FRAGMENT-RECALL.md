# Fragment recall: acceptance and comparison plan

[Design](../design/FRAGMENT-RECALL.md) · [Handoff contract](../implementation/FRAGMENT-RECALL-CONTRACT.md) · [Requirement catalogue](../implementation/REQUIREMENTS.md)

## Status and reporting

These are specified acceptance scenarios, not executed tests or reported passes. FR-M and FR-B are supplemental scenario labels, not new requirement identifiers. Keep I01–I21 and the existing 45 requirement rows unchanged. Record exact design, implementation, provider, question-template, retrieval-policy, and evaluator revisions with each result. Preserve earlier failures under their original criteria.

The target is a graph of persona-authored fragments and conditional connections, indexed candidate discovery, optional Jev-style semantic assessment, and a checked bounded context. There is no mandatory tree, function category, or permanent link weight. Same-call authorship still excludes a separate generative memory writer, but permits a separately charged selector.

## Existing requirement mapping

| Existing requirements | Refinement covered | Supplemental cases |
|---|---|---|
| PER-01–PER-03, PER-05 | Coherent identity, supplied seed provenance, character-conditioned fragments, and one authoring role. | FR-M01–FR-M02, FR-M17; FR-B03 |
| MEM-01–MEM-02 | Distinct evidence and interpretation, conditional links, correction, and exact fragment revisions. | FR-M02–FR-M07, FR-M15; FR-B04 |
| MEM-03–MEM-04 | Owner-scoped discovery, direct and delegated selection, protected context, and exact inclusion. | FR-M03–FR-M06, FR-M10–FR-M12; FR-B01–FR-B02 |
| MEM-05, EVD-05 | Useful transfer and honest stage-specific evidence rather than fragment counts. | FR-M16, FR-M20; FR-B01–FR-B06 |
| COL-01–COL-04, SOC-03 | Directional social memory, actual contact usefulness, and no invented commitment or global reputation. | FR-M18; FR-B05 |
| GOV-01–GOV-04, UX-02 | Processing permission, bounded costs, non-disclosure, stopping, and no hidden retry loop. | FR-M06, FR-M12–FR-M15, FR-M19 |
| SYS-01–SYS-04, ACT-03–ACT-04 | Atomic updates, auxiliary versus primary authority, freshness, restart, and no effect replay. | FR-M07–FR-M09, FR-M13–FR-M16 |
| UX-01, OSS-01 | Readable graph inspection, exact recall explanations, and versioned release claims. | FR-M20; all reports |

These refinements do not enable proposed society, physical, or cross-host extensions. The [fragment-persona scenarios](FRAGMENT-PERSONA.md) remain applicable with their current graph-based wording.

## Mechanism scenarios

| Case | Setup and required observation |
|---|---|
| FR-M01 — No imposed hierarchy | Create fragments with several connections, a cycle, and an isolated node. Navigation and recall work without root, parent, or functional category. A pinned character node is not used as a graph root. |
| FR-M02 — Same-call authorship | One ordinary response does work and creates or revises fragment text, retrieval descriptions, conditions, and future attention. No extra generative writer runs. No-change is valid; a result not yet received cannot be cited as observed. |
| FR-M03 — Whole-index discovery | Place old relevant material outside the active neighborhood among many recent distractors. Direct search and exact entity lookup find it. Candidate bounds and any incomplete search are visible. |
| FR-M04 — Conditional meanings | Exercise direct fact match, no match, missing information, outdated interpretation, and invalid expression. A semantic answer cannot override a failed hard prerequisite. An unknown case is not a satisfied rule. |
| FR-M05 — Unexpected event and new work | Deliver a reply from a known participant that the prior handoff did not predict. Current events seed retrieval. A new work uses its own brief and does not inherit another work's private focus. |
| FR-M06 — Before-provider privacy | Deny remote processing for a locally readable fragment and for current situation text. Neither is sent to Jev. A permitted local path remains possible. Denied source access cannot be bypassed by cards, links, hidden counts, or fallback. |
| FR-M07 — Atomic update and replay | Create connected fragments and future selection, then inject an invalid source or reference. Commit all valid changes or none. Exact retries preserve the same receipt without duplicate graph writes. |
| FR-M08 — Two roles, one primary authority | Run auxiliary selection while a primary decision or another work stream exists. The selector cannot acquire action authority, supersede the primary call, or become a fragment author. Independent personas retain isolation and concurrency. |
| FR-M09 — Snapshot race | Change a fragment, condition, recall policy, current character, source permission, or cancellation during selection. Recheck before main admission. Optional stale candidates have dispositions; mandatory conflicts block or rebuild within the bound. |
| FR-M10 — Direct choice and delegation | Without delegation, search matches remain cards. With an authorized recall plan, eligible full fragments can enter the next request. Disabled, expired, preview-only, and operator-bootstrap choices retain their distinct meanings. |
| FR-M11 — Exact final context | Inspect actual provider-bound text and digests. The chosen full versions, character, qualifications, and current observations are present. A card-only receipt cannot count as full inclusion, and selection cannot retroactively change the previous call. |
| FR-M12 — Full-request pressure | Increase text, qualifiers, media, instructions, and output reserve. Necessary context remains present or admission blocks. A high candidate count does not override token limits; no silent full-text-to-title downgrade occurs. |
| FR-M13 — Batch contract failure | Return missing or extra question IDs, wrong answer types, malformed options, invalid distributions, partial output, or a wrong model. The initial profile rejects the incomplete semantic batch and uses only its declared fallback. No failed candidate is invented as irrelevant. |
| FR-M14 — Bounded costs and failures | Trigger timeout, quota, unknown usage, stale attempts, and restart. Reserve before dispatch, retain actual or uncertain spend, enforce one batch per attempt and the episode-wide bound, and never replay an outside effect. |
| FR-M15 — Index and cache invalidation | Edit text and descriptions, revoke a source, change a question template, and move a model alias. Exact validity checks prevent stale disclosure and cross-version cache reuse. New fragments remain discoverable during bounded index lag. |
| FR-M16 — Receipts are not benefits | Record offered, selected, included, applied, and outcome-assessed stages separately. Repeated selection never silently becomes a permanent weight, belief, or correctness claim. |
| FR-M17 — Character lock and voice boundary | Lock current self-fragments and traits while allowing ordinary graph development. Neither substitute fields nor selector output mutate identity. Test misleading conflicting prose behavior separately; metadata alone cannot prove voice fidelity. |
| FR-M18 — Social evidence | Supply one report, a repeated copy, a verified later contribution, a decline, and nonresponse. Preserve origins and uncertainty. Recall cannot create expertise, consent, a blacklist, or a commitment. |
| FR-M19 — Diversity without unsafe revival | Sample eligible new or underexposed candidates using recorded seeds. Exclude revoked or discredited advice as current instruction. A required correction is included independently of random sampling. |
| FR-M20 — Inspectable interface | Open connected fragments, exact text versions, conditions, recall routes, model-used status, omissions, and usage. The interface invents neither categories nor selector rationales. Retention and visibility remain enforced. |

Local helper checks are not execution of these mechanisms. A green documentation build or successful SVG render proves neither runtime admission nor model behavior.

## Behavioral comparisons

### FR-B01 — Candidate discovery before selection

With a fixed context allowance, grow a private authorized archive containing old relevant fragments, isolated nodes, changed descriptions, paraphrased needs, exact participant references, and distractors. Measure whether the needed candidate and its qualification bundle enter the shortlist before evaluating Jev. Report recall, latency, index cost, hidden-data exclusions, and bound exhaustion separately. Failure to discover a candidate is not charged to the selector as a semantic mistake.

### FR-B02 — Does the selector improve the context?

Compare the same indexed candidate pool under deterministic selection and Jev-assisted selection. Also assess shortlist quality with an independent reference selection; the reference is an evaluation instrument, not another production LLM call. Hold the persona, task, tools, total resources, and main model fixed. Measure contextual precision, missed relevant fragments, qualifier coverage, redundancy, downstream task quality, and total latency and cost. Better relevance labels with worse work are not success.

Evaluate insufficient-information cases, negation, implicit situations, misleading candidate descriptions, and self-promoting instructions inside fragments. Keep these candidates inside the privacy boundary. Tune thresholds on development tasks and report held-out results; do not transfer thresholds between different model revisions, primitives, or question wording without re-evaluation.

### FR-B03 — Character in authored fragments and actions

Use matched starting profiles, name swaps, character-withheld controls, and neutral-wording controls. Inspect what the primary persona writes and actually does: questions, checking, consultation, challenge, and stopping. Test that mandatory facts can lead different characters to the same appropriate choice. Jev must not suppress useful corrections merely because they conflict with a preferred approach. Repeat with the selector disabled to isolate selector effects from character prompting.

### FR-B04 — Qualified transfer and correction

Run a learned task followed by held-out related tasks under retained, properly withheld, and fresh-persona conditions. Audit equivalent information in other fragments, conditions, descriptions, self-summaries, host files, messages, caches, and indexes. Include a once-useful method that now fails and an attractive but incorrect rule. Observe narrowing, correction, or rejection rather than automatic reinforcement of familiarity. State the actual intervention when removing a focal lesson also removes descendants or derivative information.

### FR-B05 — Learning useful social recall

Different synthetic peers provide distinct inspectable contributions without profession labels or a prescribed contact roster. Later needs test whether a persona recalls a useful exchange, communicates appropriately, and recognizes the limits of prior help. Include a familiar peer who declines or gives wrong advice. Measure contribution usefulness and outcomes, not name mentions, automatic agreement, popularity, or constant sociability. Keep private accounts distinct from shared agreements.

### FR-B06 — Longitudinal growth and economics

Compare an initial persona with a developing fragment graph over a task sequence and later held-out work. Fix total resources, not just the number of main calls. Include selector input and output, failed attempts, indexing, embeddings, tools, and larger same-call fragment completions. Report cost per completed task, p50/p95 latency, context growth, repeated errors, useful generalization, and variation across runs. Test low-budget and provider-unavailable conditions as well as the best path.

## Experimental discipline and release gates

Predeclare tasks, seeds, candidate order handling, repetition counts, character controls, outcome rubrics, and leakage checks. Preserve the applicable minimum repetitions in the existing development acceptance rules. Treat the 24-candidate, 48-question example as a tunable local profile, not a product claim or provider capability.

Record actual returned model versions. A moving alias, unavailable revision pinning, or uncontrolled sampling limits causal conclusions. Cross-model changes preserve identity but do not inherit earlier behavior claims. Preserve adverse and inconclusive results.

Release reporting separates documentation validation, compiled mechanisms, tested transport, recall performance, character behavior, social continuity, and independently assessed work improvement. No current scenario establishes human feelings, consciousness, or universal expertise. An operator may enable the optional selector only within an approved processing and resource policy; a promising experiment cannot widen authority by itself.
