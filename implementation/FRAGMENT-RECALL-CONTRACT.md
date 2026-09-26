# Fragment recall: responsibility and handoff contract

[Design](../design/FRAGMENT-RECALL.md) · [Persona graph](../design/FRAGMENT-PERSONA.md) · [Requirements](REQUIREMENTS.md) · [Acceptance](../evaluation/FRAGMENT-RECALL.md)

## Status and scope

This normative handoff contract refines the existing identity, memory, inference, information, and resource contracts. It adds no work planner, profession registry, mandatory fragment category, or additional generative author. Where the earlier contracts require a tree or disallow every auxiliary selection model, this contract and the current design replace those restrictions. Authority and evidence invariants remain unchanged.

An auxiliary selector is a read-only context-preparation operation. Its result cannot execute a work action or become a primary persona decision. The contract specifies behavior and failures, not request payloads, implementation code, or a storage migration.

## 1. Persistent information and ownership

| Information | Responsibility and invariant |
|---|---|
| Persona identity and creation | Stable identity and immutable provenance survive model and work changes. |
| Current character designation | One authoritative profile revision binds exact ordinary self-fragments and current traits. It is not a graph root. |
| Fragment revision | Full authored text, retrieval description, evidence, applicability, and limits belong to an exact owner and version. |
| Connection revision | Source and target, authored situation, scope, permitted selection mode, and validity are explicit. A score is not required. |
| Recall delegation | The persona's authorized intention describes the source scope, selection mode, limits, and lifetime of prospective recall. |
| Situation snapshot | Actual observations and the current authored focus are separately attributable. A prior intention cannot override new facts. |
| Selector receipt | Exact input digests, candidate references, question template, returned model, assessments, usage, and disposition are auditable. |
| Context manifest | Exact full fragments, previews, required qualifiers, selection origins, omissions, and provider-bound payload digest are distinguishable. |

Retrieval descriptions, edges, and cached results follow source restrictions. Deriving a short description does not create a less-private copy. Ordinary views must not independently edit a second competing persona narrative.

## 2. Authoring handoff

The primary persona response may propose work actions and graph changes together. New fragments and connection targets can use local handles within the transaction; existing edits bind received exact versions. The runtime validates ownership, received evidence, source ancestry, current character policy, bounds, and decision authority before committing changes and future selection together.

No fragment is required merely to fill a category. Intentional no-change and deferral remain valid. Retain/revise labels do not prove writes. Invalid changes leave the prior valid graph and plan intact. Independently valid actions retain their original admitted context; no action may use an uncommitted fragment as authority or evidence. Accepted self-model changes preserve the fresh-decision boundary.

A fragment authored before an effect settles may contain a plan, not a result. Future evidence cannot be cited retroactively. A substantive revision reconsiders its retrieval description and affected connection conditions. Earlier use evidence stays tied to earlier bytes. Retirement preserves the minimal permitted disposition; incoming edges cannot resurrect old content.

## 3. Preparation handoff

Preparation binds the persona, current work, current recall policy, important observations, and active fragment versions. Candidate discovery applies current owner and scope filters before model-facing material or visibility-sensitive counts are exposed. Exact sender, work, tool, and artifact bindings supplement authored natural-language focus. A new work has no inherited private handoff.

The candidate packet states its exact versions, discovery route, authored description, applicable condition, material limitations, and enough permitted content for the question. Node, edge, candidate, traversal, token, and byte bounds are separately enforced. Search reports when those bounds prevent completeness. Disconnected nodes have direct retrieval entry points. No public or foreign fragment is treated as owned memory merely because it is semantically similar.

Required correction and prerequisite relations are checked independently of ordinary association traversal. Expansion limits cannot turn a method without its essential qualification into a complete usable procedure. Cross-work reuse and destination processing each need their own permission checks.

## 4. Dispatching the optional selector

Enablement requires an operator-approved deployment, processing permissions, finite allowance, timeout, fallback mode, and approved model configuration. A persona's recall delegation chooses what may be selected; it does not create money or data-export permission. The bootstrap path has explicit operator attribution.

A validated context-preparation attempt makes at most one selector batch. Episode-wide attempts and spending also have finite bounds so repeated stale snapshots cannot create an unbounded loop. Reserve exposure before any remote request. Record uncertain spend rather than assuming a timeout was free. No credentials or hidden provider configuration enter persona fragments.

The selector receives only approved text and questions. It may assess semantic relevance and uncertain situation fit; arithmetic, exact identity, permission, and expiry decisions remain in the runtime. Each candidate question contains its actual meaning, not only an identifier. Questions are independent; no answer is assumed to become another question's input in the same batch.

Validate the returned model, answer identifiers, types, option sets, finite distributions, and reported usage under the adapter contract. Missing, duplicate, extra, malformed, or partial answers must have a declared failure disposition. The initial target rejects the semantic batch as incomplete rather than pretending missing candidates scored poorly. Selection returns no executable action and authors no fragment.

## 5. Selection and packing handoff

A direct choice, a delegated rule match, a semantic recommendation, and an exploratory preview are different origins. A failed hard prerequisite cannot be overruled by a semantic answer. Unknown applicability remains visible; an explicitly permitted candidate path can still expose an unknown case as a preview, not a satisfied rule.

The runtime applies the declared selection policy to valid results. Independent candidate scores do not guarantee a useful set: deduplicate, preserve needed qualification bundles, and cover the current need within the budget. The selection policy may use transient relevance ordering, never a hidden global persona value or reputation score. Random exploration is bounded, seeded, eligible, and does not displace mandatory information.

Full text is fetched at exact versions. The final request protects current character, constraints, obligations, cancellations, and critical observations. Valid explicit full selections cannot silently become titles. Necessary content that cannot fit triggers the existing bounded maintenance or an explicit block. A selector never switches the primary model or grants a larger allowance to force a fit.

Ordinary requests should bound repeated settled history before reaching a model's context ceiling. Any projection identifies omitted details and how to recover their exact receipts. It preserves explicit selections, recent and unread observations, adverse facts and unresolved effects. This is a request projection, not authored learning or evidence that an omitted result was inspected. A later pressure pass preserves earlier omission references. Discovery must not disappear merely because old successful output is verbose.

A lookup is not adoption of a belief. A full-context receipt is not evidence that the LLM applied the fragment. A selected fragment's correctness and later benefit require separate observations and assessment.

## 6. Freshness and authority between calls

Selection is advisory work on a snapshot, not a new primary decision authority. It must neither displace an already admitted primary call nor let two primary writers update the same persona concurrently. Independent personas and isolated jobs retain their existing concurrency.

Revalidate relevant work, cancellation, persona character, source policy, fragment, connection, and recall-plan versions after selection and before main-call admission. A changed mandatory reference requires rebuilding or blocking. An optional stale recommendation may be omitted with a visible disposition; do not silently follow it to different bytes. An unrelated change need not invalidate an otherwise unchanged snapshot.

If the snapshot is stale, use the declared bounded fallback or a separately budgeted future preparation attempt. No paid automatic loop occurs merely because another write keeps changing the graph. Already spent selector usage remains charged even when no main call follows. A timeout or restart does not automatically replay an uncertain provider call or an outside work effect.

## 7. Cache and index integrity

Cache assessments by exact owner, situation, candidate and connection versions, recall-policy revision, question template, model version, and relevant processing scope. Candidate-set identity is also included where a question compares candidates. Authorization is rechecked even on a cache hit. A moving model alias cannot establish cross-version cache equivalence.

An index is a candidate finder, not the source of current truth. Current-store access and revision checks fence every returned candidate before disclosure. Fragment edits and invalidations require a transactional index-update marker or equivalent reliable reconciliation. A bounded recent-write path can make new fragments discoverable during index lag. Revoked and erased sources invalidate descriptions, derived vectors, cached results, and selection eligibility.

No cache response is treated as current provider receipt. Reuse is labeled with its original assessment version and current validity check. Retention restrictions apply to model-facing packets and receipts; do not retain raw reasoning or an unnecessary second archive of private prompt text.

## 8. Failure and fallback dispositions

| Situation | Required behavior |
|---|---|
| Selector disabled or no useful candidates | Skip it. Compile valid existing context without a fabricated assessment. |
| Candidate cannot be sent to selector | Exclude from that provider request. A permitted local path remains possible. |
| Timeout, quota, invalid output, or exhausted allowance | Preserve actual usage; use only the configured deterministic fallback or block. |
| Required source revoked | Do not disclose or use it through a cached result, description, or substitute summary. |
| Optional selected version changed | Omit with a disposition or rebuild within the episode bound; do not silently substitute. |
| Character, work authority, or cancellation changed | Recheck main-call admission and stop fresh actions where required. |
| Mandatory core does not fit | Bounded maintenance or explicit block, never silent truncation. |
| Graph update fails | Keep prior graph and next-context plan; provide a repairable receipt. |
| Retrieval repeats without useful progress | Surface the repetition and respect the ordinary continuation and stopping limits. |

A failure disposition must not leak inaccessible identifiers, source text, or hidden counts. A deterministic fallback is not recorded as Jev approval. Deferred recall does not schedule another model call by itself.

## 9. Operator evidence and release gates

The interface offers a connected-fragment view and search, exact current character, authored connection situations, permission controls, and per-decision recall origins. It distinguishes observed events, personal interpretation, candidate relevance, actual inclusion, use, and assessed benefit. Human-visible explanations are composed from known receipt fields, not a new model's invented rationale.

Implementation readiness requires passing the applicable [recall scenarios](../evaluation/FRAGMENT-RECALL.md) and [fragment-persona scenarios](../evaluation/FRAGMENT-PERSONA.md) at exact revisions. Mechanism execution, provider transport, character behavior, social usefulness, and outcome improvement are separate statuses. No wording in this contract converts an unrun acceptance case into a passed feature.
