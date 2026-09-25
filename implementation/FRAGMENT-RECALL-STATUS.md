# Fragment recall implementation status

Review date: 2026-09-25.
Normative baseline: `f8a8566fb8d71469ac7b53da08bee1d491956000`.
Runtime base reviewed: `ai-personas/ai-personas@8fdcd396b9bd64058c7717b97159125bc2ee9bcb`.
Corrective follow-up pushed: `33a3bd2dfc078cf1aeaa1c277c899476b8017b8e`
on `rewrite/design-first`.

This ledger records implementation and validation separately. It does not amend
or relax the [recall contract](FRAGMENT-RECALL-CONTRACT.md), the
[fragment-persona design](../design/FRAGMENT-PERSONA.md), or their acceptance gates.
A pushed patch is not an executed test, and a retrieval hit is not learning benefit.

## Implemented source and accompanying corrective follow-up

The Rust request compiler has an owner-scoped metadata index and bounded
traversal of existing memory-node `related` links. Candidates are previews, not
automatically selected full fragments. Current access, exact fragment versions
and graph-only traversal paths are checked before admission. Character inclusion
remains mandatory under the existing profile contract.

The follow-up changes rank metadata matches before the database shortlist,
exclude already-offered/stale/duplicate entries from that shortlist, and use
query-local scores rather than cross-owner corpus statistics. Matching uses the
existing FTS5 tokenizer. Database work is not constant-time, permission filtering
can underfill the bounded list, and search remains nonexhaustive.

Graph cards receive exact `@memory` node aliases. Pressure projection removes
aliases for omitted optional cards while keeping aliases for still-explicit
selections. Alias admission rejects stale or unoffered nodes; a historical
reference does not itself constitute an offered card. The primary response
still chooses whether to select a preview for a later full-context request.
No additional selection model is dispatched by these changes.

The code workflow is pinned to the reviewed normative design revision rather
than the older pre-update design input. It records literal SQL checks and focused
Rust recall checks separately, without removing the broader build, API or UI gates.
The source report is `reviews/fragment-recall-followup-2026-09-25.md` in the runtime
repository; its machine-readable SQL evidence is adjacent to that report.

## Validation evidence

| Layer | Evidence actually available |
|---|---|
| Source integrity | Original runtime/reference/workflow files matched their GitHub blob hashes before editing. |
| Literal database statements | 35 tests executed successfully against SQL extracted from the Rust source, using SQLite 3.46.1. |
| Python and workflow syntax | Python syntax compilation and YAML parsing completed. This is not GitHub workflow execution. |
| New Rust regressions | 17 added and wired into the recall module, including request/alias/explicit-selection round trips. Not compiled or executed. |
| Existing Rust and integration suite | No local run. Previous workflow `36191987796`, including retried job `108266865992`, failed before steps. |
| Live provider transport and behavior | No live Jev, character comparison, social-usefulness or work-improvement run. |

The test round trip covers request compilation and reference/continuity contracts,
not the full production funding/admission path. A new commit's workflow outcome
must be checked at that exact commit. The pre-step failures do not establish a
compiler error or a specific billing/account cause.

## Open implementation and release gates

| Gate | Required work before closure |
|---|---|
| Canonical graph, without mandatory hierarchy | Replace legacy tree storage/API/view assumptions; keep stable owner/version identities and existing retention protections. |
| Conditional connections | Add same-call authored connection revisions, bounded checkable expressions, separate match/no-match/unknown states and inaccessible/invalid dispositions. |
| Current fragment-based self-model | Designate exact ordinary self-fragments under one authoritative profile revision; preserve seed provenance, self-authorship policy and decision freshness without a competing narrative. |
| Optional pre-call Jev | Integrate a distinct read-only preparation lane with operator-approved deployment, disclosure permission, bounded episodes, reservation/settlement, cancellation and separation from primary decision authority. |
| Semantic validation, cache and fallback | Validate complete typed batches; bind reuse to exact owner/situation/policy/candidate/connection/template/model/scope; recheck current permissions and retain uncertain spending. |
| Delegated packing | Implement explicit recall delegation, exact full-fragment inclusion, correction/prerequisite bundle closure and omission handling under protected-core budgets. |
| Executed mechanism gates | Compile the complete private checkout; run focused and all-target Rust checks plus contract/browser gates; report formatting/lint separately. |
| Behavioral and cost gates | Run controlled deterministic-versus-selector, character-continuity, social-learning and retained-versus-withheld-learning comparisons with leakage controls and actual cost/latency evidence. |

**No row in this open-gate table is closed by the ranking/reference follow-up.**
In particular, a working native TypeSafe adapter is not a completed pre-call recall
integration, and the existing explicit-selection path is not delegated selection.

Use [recall acceptance](../evaluation/FRAGMENT-RECALL.md) and
[fragment-persona acceptance](../evaluation/FRAGMENT-PERSONA.md) as the release basis.
Do not enable an auxiliary provider or claim persona maturity merely because
SQL checks pass or a branch update succeeds.
