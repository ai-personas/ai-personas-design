# Observable system contracts

[Implementation guide](README.md) · [Requirements](REQUIREMENTS.md) · [Acceptance scenarios](../evaluation/ACCEPTANCE.md)

These contracts define what cooperating parts of an implementation must guarantee. They are not database tables, interface syntax, or a mandatory workflow. Small work may combine several records, provided the meanings and evidence remain distinct.

## Information that must remain recoverable

| Conceptual record | Minimum meaning to preserve |
|---|---|
| Persona | Stable identity, provenance, lifecycle, character revisions, current participation, inference configuration, and owned references. |
| Environment | Membership, resources, workspace, available capabilities, access boundaries, and presentation context. |
| Mandate | Original request, accepted interpretation, required outcomes, constraints, criteria, questions, assumptions, authority, resources, and closure terms. |
| Participation and funded episode | One persona's work context, distinct from the shared funding and authority envelope. |
| Perspective | Author, situation, agenda or relationship subject, evidence, interpretation, and limitations. |
| Work entry | Attributed observation, proposal, question, decision, assumption, or finding with a current disposition. |
| Agreement | Exact terms, scope, endorsers, dissent, permissions, and revision or exit conditions. |
| Commitment | Offer, actual acceptance, owner, outcome, terms, dependencies, allowance, evidence, and closure or handoff. |
| Fragment | Owner, content, selection trigger, source type and evidence, applicability, counterevidence, revisions, visibility, retention, and later use. |
| Capability | Provenance, descriptor or version, environment, required access, lifecycle, actual operation evidence, and limits. |
| Birth and invitation | Motivating work, creation provenance, authorized seed, bounded orientation, invitation preview, membership response, and contribution offer. |
| Artifact and submission | Exact content, producing action, source versions, assembly membership, criteria, conditions, access, and limitations. |
| Assessment | Claim, exact criteria and evidence, accepted reviewer, policy, conflicts, observations and reasoning, optional citation snapshots with capture stage, verdict, limitations, and separately derived applicability. |
| Grant and allocation | Principal, actor, permitted scope and effects, expiry or revocation, ceilings, reservations, actual usage, and uncertain exposure. |
| Action and event | Stable request identity, actor, work, relevant observed versions, accepted intent, status, outputs, causality, and delivery state. |
| Release | Exact mandate, criteria, assumptions, assembly, reviews, blockers, current authority, delivered scope, and acceptance where required. |

Material records identify their source or author, scope, version, visibility, and relevant causal relationships. A link can mean derived from, tests, blocks, supersedes, contradicts, or endorses. A link alone does not establish that the asserted domain relationship is correct or complete.

## Need intake and continuation

**Inputs:** original human request, source identity, supplied material, available permissions and allowance, addressed participants.

**Accepted result:** a recoverable initial mandate and an offer of participation. The system records explicit continuation acceptance before showing that responsibility as owned. Required outcomes each show accepted ownership or a gap.

**Failure behavior:** unavailable or declining participants produce awaiting, declined, or unowned states. The system does not substitute a profession roster. Scope changes preserve the original request and require the relevant authority. Unknown facts remain questions or conditional assumptions.

**Visible evidence:** original and current mandate versions, actual acceptance, outcome coverage, unresolved questions, and the authority for material changes.

## Agreements and responsibility transfer

**Inputs:** proposed terms, scope, intended participants, relevant outcomes, dependencies, resources, and conditions.

**Accepted result:** only actual endorsements bind the identified participants. Commitment acceptance is separate from membership. Handoff changes ownership only when the receiver accepts the exact responsibility or an authorized disposition explicitly replaces it.

**Failure behavior:** stale terms conflict; declines remain declines; missing receivers leave responsibility or a visible handoff gap. Acknowledgment of a finding does not resolve it. Compaction and pagination cannot hide applicable unresolved blockers.

**Visible evidence:** offers, accepted versions, objections, owners, dependencies, findings, transfers, and final dispositions.

## Identity creation and onboarding

**Inputs:** authorized sponsor or proposer, causal work, observed contribution need, root population and resource limits, permitted inference capability, and shareable seed references.

**Accepted result:** one identity, creation provenance, initialization reservation, restricted orientation context, and initial notification are accepted coherently. The newcomer can inspect the exact invitation preview before deciding on membership and then on the offered commitment.

**Failure behavior:** duplicate requests do not duplicate births; concurrent requests cannot exceed remaining capacity; seed revocation is checked at use. Initialization failure has bounded retries. Declining membership neither creates a replacement nor erases spent resources or birth counts.

**Visible evidence:** created, oriented, joined, and committed are separate milestones. A useful contribution is assessed later, not inferred from a biography.

## Context and decision ownership

**Inputs:** an authorized stimulus, persona identity, current work and authority, required obligations and findings, permitted selected history, inference capability, and available allowance.

**Accepted result:** one current decision authority acts for one persona at a time. The decision receives its mandatory current core plus the historical material actually included. Independent personas and bounded jobs may proceed concurrently.

**Failure behavior:** old or competing holders cannot commit as the same persona; unsupported input, refusal, malformed response, timeout, and context overflow are explicit. Historical selection can shrink, but current constraints, cancellations, and obligations cannot disappear. Inability to fit the required core causes a visible block.

**Visible evidence:** identity and work context, input-version references, actual included material, inference configuration, concise decision summary, accepted or rejected actions, and usage. Do not require disclosure of private chain-of-thought.

## Persona-owned organization and capability choice

**Inputs:** the current mandate, permitted work and participant discovery, actual capability evidence, individual context, proposals, and existing grants and commitments.

**Accepted result:** participants can discover, communicate, propose, accept or decline, revise, and hand off work through the existing records and transitions. Plans and reusable methods are versioned work content; only accepted commitments bind participants. The [organization rules](../design/03-work-and-cooperation.md#how-organization-emerges) define this boundary under I03, not a new service or domain schema.

**Failure behavior:** unavailable affordances, declined offers, uncovered outputs, and missing capabilities remain explicit. Neither a domain keyword nor an embedded orchestration prompt may silently allocate professions, choose a fixed solution pipeline, or manufacture a replacement. General scheduling may enforce accepted prerequisites, but cannot bypass the pending-action decision barrier. Safeguards and mandatory criteria remain enforceable even when a group proposes an exception.

**Visible evidence:** the permitted information actually used, concise proposal and revision reasons, accepted responsibility, capability choices and actual results, ownership gaps, and subsequent evidence-led changes. An implementation must make relevant routing and orchestration configuration auditable by authorized evaluators without exposing secrets or private reasoning. A polished transcript alone does not establish that organization was unscripted.

## Actions and observations

**Inputs:** actor, causal work, stable request identity and content, relevant versions, intended effect, capability, current grant, reservation, output expectation, and uncertainty or cancellation rules.

**Accepted result:** authority checks, resource reservations, accepted intent, related state changes, and required notifications form one coherent transition. Durable intent exists before dispatch. Result receipts identify actual status and exact outputs.

**Failure behavior:** the same request and content resumes the same admitted operation; changed content under the same identity conflicts. A pending operation suppresses the unobserved remainder of its decision. Later actions require a fresh decision informed by observed results. Failures preserve diagnostics; ambiguous external effects remain unknown until reconciled.

**Visible evidence:** proposed, admitted, running, completed, failed, stop requested, canceled to the observed extent, and effect unknown remain distinguishable. Completed execution does not prove a correct result.

## Authority and resource accounting

**Inputs:** controlling grant, current actor and work scope, exact effect or permitted envelope, applicable ceilings, outstanding reservations, and known or uncertain usage.

**Accepted result:** no child grant exceeds its parent, and no action spends capacity already reserved elsewhere. Transfers conserve the root. Initialization, descendants, retries, compaction, review, and finishing all remain within the controlling allowance.

**Failure behavior:** insufficient capacity or expired permission rejects the new admission. Unknown usage stays exposed rather than being refunded. Ordinary work cannot use protected closeout capacity without authorized reallocation. Revocation stops new affected admissions and initiates stopping, while late receipts remain available.

**Visible evidence:** controlling authority, scope, allocation, protected closeout, consumed resources, uncertainty, reservations, transfers, and the precise stopping state. When inference ends, mechanical reporting remains possible.

## Shared writing and change impact

**Inputs:** proposed artifact adoption, the prior version observed by the author, exact candidate versions, declared dependencies, and current write authority.

**Accepted result:** one coherent current version or assembly is adopted. Competing alternatives remain inspectable. The system exposes relevant evidence as stale or pending before displaying a changed result with any current acceptance claim.

**Failure behavior:** a stale author cannot overwrite newer accepted work. Partial adoption cannot present an inconsistent assembly as coordinated. Uncertain dependency coverage triggers conservative wider revalidation rather than a fabricated unaffected result.

**Visible evidence:** prior and new versions, alternatives, conflicts, affected claims, notification of owners, and fresh applicability decisions.

## Review and release

**Inputs:** exact submission, mandate and criteria, assumptions, assembly, accepted funded reviewer, independence policy, observations and reasoning, optional additional citations, findings, and authority. Completed host commands are not a universal prerequisite.

**Accepted result:** an assessment records the reviewing persona's explained judgment, exact evidence and limitations without using citation kind, count or success as a quality score. A release binds one coherent current state: qualifying reviews, resolved or legitimately disposed blockers, exact scope, and current permission. An empty additional-citation list does not omit the review or authorize automatic release.

**Failure behavior:** missing review, unavailable evidence, changed inputs or cited snapshots, unresolved mandatory blockers, or stale authority prevent the corresponding release claim. Check snapshot identity at the first binding and subsequent use; a pending receipt becoming terminal is a change, not permission to retrofit the old verdict. If a relevant change occurs before release, reconsider; if release occurs first, retain that historical release and create a new candidate. Never transfer acceptance silently. Unknown or malformed snapshot versions fail closed; older bindings retain their documented compatibility rules without fabricated observation history.

**Visible evidence:** persona assessment, receipt states, snapshot capture stage, current applicability, human acceptance, and outside validation are separate. A recording-time fingerprint is not proof of earlier request inclusion, attention or comprehension. Non-command observations carry the same source restrictions as execution evidence. Limited or partial delivery states identify what the original need still lacks. The [judgment and integrity boundary](../design/06-evidence-and-completion.md#persona-judgment-and-mechanical-integrity) defines the distinction; its [snapshot limits](../design/06-evidence-and-completion.md#what-a-citation-snapshot-establishes) must remain visible in implementation claims.

## Durable delivery, waiting, and restart

Accepted state and its required notification must not diverge after a restart. Delivery may repeat, but recipients recognize the same event without duplicating its effect. Access-filtered views must not leak private counts or relationships.

A wait records its condition against current durable state. Whether the result arrives before or after waiting is registered, the participant remains ready or durably notified. Receiving, including, acknowledging, resolving, and accepting are separate stages.

Restore accepted records, pending effects, reservations, unresolved findings, canceled authority, and undelivered events. Do not invent replacement founders, new funding, successful outside effects, or erased obligations. A current view identifies its recoverable point in history; stale or incomplete views disclose that limit.

Import and rollback preserve provenance and uncertainty. Unknown external bindings remain unknown. Read-only exchange must not automatically activate a remote persona or duplicate authority. Cross-host exclusive activation requires a separate evaluated contract.

## Privacy, correction, and retention

Every read path and derivative follows the same underlying access rules, including search, summaries, thumbnails, relationship views, error messages, exports, seed material, and backups. Revoked or discredited sources require an explicit disposition for affected memories and future use.

Retaining provenance does not require retaining sensitive payloads forever. Keep minimal historical accountability consistent with the deployment's retention decision. State the limits of deletion for copies outside the system's control. Import must not automatically execute content or reveal protected evaluator material.

## Boundary of these guarantees

The system can enforce attribution, permission, conserved resources, unchanged bytes, current references, and required recorded transitions. Those checks do not establish optimal planning, genuine expertise, complete stakeholder representation, or technical truth.

Map each implementation component to the applicable [requirements](REQUIREMENTS.md), demonstrate the [acceptance scenarios](../evaluation/ACCEPTANCE.md), and publish the particular boundaries actually tested.

The first-release memory graph and combined decision contract are defined in [Persona-authored memory navigation](../design/MEMORY-TREE.md). Every learned fragment belongs to a stable private node; old storage and continuity bundles are not migration inputs.
