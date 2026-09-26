# Fragment recall implementation status

Review date: 2026-09-26. Normative baseline: `a736120a7d440c0603443528221e99f9ce2b298d`.
Runtime update starts from `ai-personas/ai-personas@9b351fd83f3d13ea24a0f34592a23b5ce7049ff2`.
Production UI update starts from `ai-personas/ai-personas-ui@23811d6fedffd16fb80d7b191fd23911bf7eeccc`.

This ledger separates implemented mechanisms from behavioral acceptance. The
[handoff contract](FRAGMENT-RECALL-CONTRACT.md), [fragment-persona design](../design/FRAGMENT-PERSONA.md),
and [recall acceptance](../evaluation/FRAGMENT-RECALL.md) remain normative.
Exact code revisions, private execution records and validation commands belong
in the runtime repository's `reviews/fragment-implementation-2026-09-26.md`.
Local changes are not a published deployment or a successful hosted workflow.

## Implemented mechanisms

| Requirement | Implementation boundary |
|---|---|
| Canonical graph | Owner-scoped, rootless navigation uses exact nodes and fragments, directed incoming/outgoing connections, cycles, private search and visible pagination. Parent fields and tree controls are removed. The storage/API contract changes without a migration. |
| Authored connections | The primary continuity transaction authors conditions, explanations, relation, target, scope, expiry and full/preview treatment together. Bounded finite predicates distinguish match, no-match, unknown, invalid and inaccessible states. |
| Current self-model | An explicit designation binds ordinary self-fragments and the derived profile projection under one attributed revision. The starting seed remains provenance. Self-authorship and fresh-decision checks apply to protected revisions; ordinary learning remains available. Bootstrap character can be explicitly preserved until designated. |
| Pre-call selector | An optional read-only preparation batch precedes primary admission. Per-work operator processing permission, source export checks, exact model pricing, finite attempts, request limits and transactional reservations are required. The auxiliary result has no primary writer authority. |
| Accounting and control | Every dispatched attempt is accounted, including cancellation, stale results, invalid output and uncertain transport. Failure follows the declared deterministic/block policy. The saved Jev connection also has an editable node-wide USD ceiling in Funding → Settings; edits and key replacement retain spending. |
| Exact reuse | Complete typed batches bind owner, work, profile, deployment generation, policy, observations, conditions, source and target versions, delegation, template and model. Permission changes invalidate reuse. Moving aliases and restarts do not reuse prior assessments. |
| Qualification packing | Direct and delegated full selections carry required correction/prerequisite closure. Missing or excessive bundles are omitted as a whole or block required selection. Explicit selections, self-context and required core remain protected. |
| Operator inspection | The production UI uses graph cards and directed conditions, shows authoritative self-model projection and selection evidence, and exposes recall processing controls and Jev spending limits. Generated contracts come from the Rust runtime. |

No auxiliary call authors fragments, creates consent, changes character, or
turns retrieval into proof of usefulness. A configured API key alone grants
neither processing permission nor work funding.

## Validation and remaining release gates

Focused transaction, compiler, selector, cancellation, cache, budget and browser
checks have executed locally. The complete runtime/API suite and final generated
contract checks are recorded separately in the private review. SQL helper tests
remain supplemental evidence, not substitutes for runtime tests. Formatting,
lint and hosted CI must be reported separately from executed local tests.

A bounded live pilot has now exercised character, retained/withheld/fresh
learning, social interpretation and deterministic-versus-Jev selection. Its
private report preserves failures, uncertain spending, actual model usage,
selection provenance and limitations. It does not establish general character
differentiation, social benefit, maturity or broad work/cost improvement.

Remaining acceptance work is broader, repeated, controlled evaluation: blinded
character judgments, actual social exchanges and executed useful work, additional
failure/quality cases, and cost/latency comparisons with adequate sampling.
Synthetic fixture qualification tests and one live pilot do not close those
behavioral gates. Coordinated publication/deployment and hosted CI are also
separate from this local implementation.

The obsolete tree address has been removed. Use [graph navigation](../design/MEMORY-GRAPH.md).
