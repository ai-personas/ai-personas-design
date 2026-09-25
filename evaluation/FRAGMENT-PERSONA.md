# Fragment-persona acceptance and requirement mapping

[Design target](../design/FRAGMENT-PERSONA.md) · [Requirement index](../implementation/REQUIREMENTS.md) · [Acceptance catalogue](ACCEPTANCE.md)

## Status and interpretation

These are specified acceptance cases, not reported passes. FP-M and FP-B identifiers are supplemental scenario labels, not new requirement identifiers. Existing invariants I01–I21 and the existing 45 requirement rows remain unchanged. The exact design, implementation, provider, configuration, and evaluator revisions must accompany any result.

The design target makes authored fragments the cognitive representation of the persona, combines work and fragment authorship in ordinary decisions, and adds explicit conditional next-context selection. A passing storage, transport, or retrieval test does not establish a particular voice, useful social behavior, or improved work.

## Requirement traceability

| Existing requirements | Refinement being tested | Supplemental cases |
|---|---|---|
| PER-01–PER-03, PER-05 | Truthful seed provenance, coherent current self-model, versioned identity, and voice-conditioned authorship without fictional experience. | FP-M01–FP-M03; FP-B01, FP-B07 |
| MEM-01–MEM-02 | Distinct observation and interpretation, same-call authorship, evidence timing, revision, organization, and correction. | FP-M03–FP-M07; FP-B02–FP-B04 |
| MEM-03–MEM-04 | Explicit and delegated selection, event-triggered recall, work isolation, required context, and honest pressure handling. | FP-M08–FP-M12; FP-B05 |
| MEM-05, EVD-05 | Assessed transfer and mature work, not fragment volume or a favorable narrative. | FP-B02–FP-B05, FP-B07 |
| COL-01–COL-04, SOC-03 | Directional relationships, source-specific contribution evidence, independent judgment, and agreement distinct from personal interpretation. | FP-M13; FP-B03–FP-B04, FP-B06 |
| PER-04, GOV-01–GOV-04 | Authorship and spending boundaries, lifecycle, authorized activity, and no implicit extra inference. | FP-M02–FP-M03, FP-M12, FP-M15 |
| SYS-01–SYS-04, ACT-03–ACT-04 | Atomic adoption, current decision authority, restart, and observation-bound effects. | FP-M04–FP-M07, FP-M14–FP-M15 |
| UX-01–UX-02, OSS-01 | Inspectable context and development, private derivatives, and versioned truthful evidence claims. | FP-M10–FP-M12, FP-M16; all behavioral reports |

## Mechanism acceptance

| Case | Setup and required observation |
|---|---|
| FP-M01 — Bootstrap and self-model | Start with supplied prose and explicit traits, and separately with the existing generated-character path. Preserve origins and zero values. The first work decision can use the bootstrap or author self fragments without an additional profile-writing call. Current and historical state are not competing instructions. |
| FP-M02 — Locked and evolving self | Test self-authorship enabled and disabled. Locked self-fragment pointers and traits cannot be edited through another field. Ordinary methods and relationships can still change. Accepted identity edits appear in the next request and fence stale dependent actions. Test conflicting prose behavior separately under FP-B01. |
| FP-M03 — One combined decision | Count actual provider dispatches while work, conversation, review, and maintenance produce changes. There is no hidden reflection, relationship author, or query planner. A no-change disposition is valid and does not create a fabricated lesson. Malformed or failed responses are not successful development. |
| FP-M04 — Evidence timing | A call sends a message or proposes an experiment while writing a tentative fragment. That fragment cannot cite the future reply or result. Only the next received observation can support the corresponding revision. A failed or uncertain effect is not interpreted as observed success. |
| FP-M05 — Atomic graph and selection | Create a parent, child, related link, and next selection together; then inject one invalid source, reference, or selection. The valid case is present in the very next request. The invalid case commits none of those changes, preserves prior selection, and does not corrupt independently valid work. |
| FP-M06 — Consolidation and correction | Merge examples into a generalized method while preserving evidence and exceptions. Retire or move children and incoming links coherently. A corrected or unavailable fragment cannot continue as an unqualified instruction; historical authorship remains unchanged. |
| FP-M07 — Concurrent work and replay | Admit two competing persona decisions around the same fragment revision. Only the current authority can adopt its changes. Restart and retry return the original receipt without duplicate fragments or external effects. Independent personas and already isolated jobs retain concurrency. |
| FP-M08 — Explicit selection versus delegation | With no delegated selector, a search match remains a preview. With an explicitly authored bounded selector, eligible full text can be supplied and is labeled delegated. Disabling, expiry, version changes, and a selector that requests previews only are respected. |
| FP-M09 — Unexpected event recall | Author a standing relationship selector, then deliver an unexpected permitted reply from a known participant. The very next ordinary request includes the allowed relationship fragment, selected using the actual sender identity rather than guessed reply content. There is no retrieval-planning model dispatch. |
| FP-M10 — Cross-work boundaries | Start a new work. Its handoff is empty and navigation starts at root; only permitted standing choices and eligible personal material can cross over. Private previous-work cues, withheld fragments, source-restricted procedures, and other owners' cards cannot appear through plans, graph links, or caches. |
| FP-M11 — Recall channels and invalidation | Exercise exact IDs, participant anchors, explicit whole-word search, separate lexical recall, graph neighbors, and optional local embeddings when enabled. Record the channel and exact versions. Revoke a source and confirm invalidation across descriptions, plans, index entries, embeddings, and cached results before disclosure. |
| FP-M12 — Whole-request budget | Increase self-model, selected text, qualifiers, observations, and output reservation until pressure occurs. Required content is preserved or admission blocks explicitly. A selected method cannot lose a material exception while remaining labeled complete. No silent full-text-to-card downgrade or runtime-authored summary is allowed. |
| FP-M13 — Social interpretation is not authority | Supply a peer claim, a repeated copy from a second peer, a real later contribution, a decline, and nonresponse. Preserve distinct origins. No universal expertise, consent, commitment, punishment, or global reputation is fabricated from the relationship fragment. |
| FP-M14 — Injection and stale adoption | A received message or fragment asks to change identity, broaden a selector to private data, or bypass grants. It remains attributed content, not controlling authority. Changed source permissions or current self-model revisions are rechecked before dependent action admission. |
| FP-M15 — Stopping and cost | End a task with deferred opportunities, unanswered questions, pending effects, and optional exploration disabled. No new model call is created merely to keep the persona alive, fill a fragment category, or reflect. Optional local retrieval compute and any separately authorized activity retain their own visible accounting. |
| FP-M16 — Inspectable evidence | The interface distinguishes proposed and committed changes; cards and full text; direct and delegated selection; admitted and dispatched payload; use and independently assessed benefit. Opening an account of a relationship shows its attributable evidence and limitations without exposing another persona's private state. |

At each transport boundary, inspect what was actually supplied to the model, not only the pre-dispatch object. Record exact fragment versions, self-model revision, selector version, event bindings, source permissions, and any omission. Do not retain a raw chain-of-thought archive to satisfy this check.

## Behavioral acceptance

### FP-B01 — Character in fragments and actions

Give matched personas the same observation, task, tools, and budget while varying declared starting character. Include name-swap, self-model-withheld, and matched neutral-wording controls. Assess the actual fragment text and subsequent questions, checks, collaboration, and stopping choices. The rubric should describe understandable tendencies without demanding a stereotype or arbitrary difference on every trial.

Check that numerical traits are not merely recited, source quotations are not rewritten as firsthand experience, and a strong task constraint can produce the same correct choice across characters. Test whether a locked self-model is respected when an ordinary fragment contains contradictory character instructions. Report failures rather than claiming that protected metadata guarantees semantic behavior.

### FP-B02 — Later procedural transfer

Use held-out tasks that benefit from an abstraction but differ from the original task. Compare retained relevant fragments, the same persona state with the relevant information withheld, and a fresh persona with matching seed and model. Freeze tools, resources, task information, environments, and assessment rules. Inspect whether the right procedure was retrieved, adapted, and used before assessing correctness, cost, or repeated errors.

Audit equivalent information in self summaries, related fragments, handoffs, files, conversation, tool caches, and peer messages. Withholding one record while leaving its content elsewhere is not a clean ablation. When descendant removal changes more than the focal fragment, state the actual intervention. Uncontrolled leakage makes the result diagnostic rather than causal.

### FP-B03 — Learning whom to consult

Use a sequence in which different synthetic peers make distinct, inspectable contributions on overlapping problems. Later tasks should test whether the persona recalls a useful contact, supplies appropriate context, understands the scope of previous help, and still seeks alternatives when relevant. No profession labels or prescribed contact roster are included in the task prompt.

Measure consultation usefulness and outcome, not merely whether a familiar name was mentioned. Include a previously useful peer who declines, is unavailable, or provides incorrect advice. A credible social memory should update its scoped interpretation rather than impose a universal blacklist or keep trusting the old account automatically.

### FP-B04 — Harmful memory and social correction

Seed an attractive but inapplicable method, an overconfident relationship interpretation, and a claim repeated by several peers from one origin. Supply a consequential contradiction. Assess whether the persona questions the interpretation, preserves the evidence distinction, revises or stops using the faulty prompt part, and avoids passing the old error into later tasks.

The target is evidence-responsive individuality, not permanent agreeableness, cynicism, or group conformity. A fragment that is repeatedly reused without reassessment is not counted as mature merely because its wording stays consistent.

### FP-B05 — Retrieval under realistic memory growth

Grow the authorized fragment archive while keeping the request budget fixed. Include old relevant methods, newer distractors, paraphrased needs, relevant relationships, critical exceptions, and unexpected events. Compare tree-and-explicit-selection baseline with the proposed nonsemantic context compiler; test local semantic indexing separately when available.

Report candidate recall, full-fragment inclusion, qualifier coverage, contextual precision, duplicate share, retrieval latency and compute, and task outcome as separate measures. A better retrieval score with worse work is not a successful maturity claim. Include first-call-on-new-work usefulness, and test that a stale next-context plan does not displace critical new input. Do not claim a search is exhaustive when an internal bound prevented that.

### FP-B06 — Small-society continuity

Run bounded shared activities with several distinct personas and actual message, contribution, agreement, decline, and handoff events. Observe whether individual relationship fragments and shared practices develop from those events, whether disagreement remains attributable, and whether coordination survives one participant leaving. There is no global merged private memory or hidden task-solving director.

Distinguish successful delivery, believable interaction, legitimate acceptance, and mutual contact preference. A scripted event or evaluator hint must be labeled. These exercises do not authorize a real institution, establish human consent, or prove general human-equivalent life.

### FP-B07 — Longitudinal maturity and model changes

Compare a fixed initial persona with an otherwise matched fragment-developing persona across a task sequence and later held-out work. Account for all prompt and completion tokens, failed calls, retrieval compute, and tools; the same number of model calls does not imply equal resources. Track useful generalization, repeated mistakes, uncertainty calibration under a specified rubric, recovery, consultation cost, and retained-context growth.

Repeat under declared model configurations. A model change preserves identity but may change performance and voice; report that separately. Do not award maturity for increasing fragment count, trait drift, self-praise, or a longer answer. A smaller, better-qualified prompt network may be a better outcome.

## Reporting and release gates

Predeclare tasks, model configurations, repetitions, isolation rules, qualitative rubrics, and outcome measures. Retain existing minimum repetitions where the development acceptance rules already apply. Report variation and uncertainty rather than a single favorable trace. When model revision pinning or reproducible sampling is unavailable, disclose it and narrow causal conclusions.

Report mechanism execution, transport verification, voice behavior, retrieval behavior, social behavior, and task improvement separately. Retain failures under their original criteria. Evaluation activity may use independent human or task-specific assessment; it is not inserted as an additional production reflection call.

A design publication establishes the intended contract only. An implementation may claim the mechanism after its exact tests pass. Useful learning and maturity require the corresponding controlled behavioral results. No test in this document establishes consciousness, human feelings, or universal competence.
