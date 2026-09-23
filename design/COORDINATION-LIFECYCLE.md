# Emergence, coordination, and lifecycle boundaries

[Design index](README.md) · [Identity](01-personas-and-identity.md) · [Work and cooperation](03-work-and-cooperation.md) · [Evaluation](../evaluation/README.md)

This is a normative clarification of the existing persona, cooperation, recovery, and resource rules. It adds no requirement family, profession registry, coordinator service, fixed team size, or compulsory workflow. The 21 invariants, 45 requirements, and existing acceptance identifiers remain the coverage framework.

The motivating abstract Lean review used design revision `2a685b8b5a666812960f726df4594aea5ad8d52b`. Its proof draft was not successfully compiled. This clarification reports neither a machine-checked proof nor implementation conformance, useful emergence, or product acceptance. The rules below are self-contained and do not require that draft or an earlier conversation.

## Separate three emergence claims

| Claim | Required distinction |
|---|---|
| The protocol permits different organizations. | The same admission rules can represent different accepted divisions of work and a one-person path, where authority and capabilities allow them. This is a structural property, not observed behavior. |
| Personas actually choose and revise the organization. | Attributed decisions and observations, together with inspection of the actual core policy, prompts, configuration, and adapters, distinguish participant choices from a hidden task script. Merely exhibiting multiple permitted traces does not establish this. |
| The resulting cooperation is useful. | Actual contributions, evidence-led changes, appropriate checks, and comparable total-resource outcomes establish a scoped benefit. Team size, variation, agreement, or a successful protocol handoff does not establish it. |

The system must not force distinct choices when the evidence supports the same method. Reused procedures and temporary specialization remain permitted, revisable work content. A one-person result need not recruit a second participant to satisfy an emergence test. None of these claims allows scope, permission, privacy, resource, or review boundaries to be negotiated away.

## Responsibility binds exact accepted terms

A current responsibility must be supported by authenticated acceptance of the particular commitment and its applicable terms, or by an already accepted delegation that covers that responsibility. Preserve the accepting identity, commitment identity, work scope, exact terms or accepted delegation envelope, and the attributable acceptance event. A name, membership flag, invitation, caller-supplied receipt, or acceptance of a different commitment is insufficient.

Material amendments outside the accepted terms or delegation require new acceptance before the changed responsibility is attributed. An amendment already permitted by the accepted envelope records that basis and its exact revision; this rule does not require renegotiating every permitted detail. Prior acceptance stays historical rather than silently attaching to changed terms. Acceptance does not create an execution grant or override current revocation.

A handoff offer leaves the existing responsibility in place. Transfer occurs only when the receiver accepts the exact responsibility under current eligibility and authority, or when an explicitly authorized disposition replaces the obligation. Acceptance and ownership change must be one coherent transition against the current commitment version. Competing handoffs, cancellation, and relevant lifecycle changes cannot each commit from the same stale view. A declined, inaccessible, or outdated offer leaves an accountable owner or an explicit authorized gap, not an invented successor.

These rules apply per commitment. An outcome may have several accepted commitments, and continuation may be shared or partitioned. A simple proof model with one owner per job must not become a product-wide prohibition on joint work. Existing responsibilities and historical transfers remain inspectable under their access and retention rules.

## Lifecycle changes preserve accountability

Creation, bounded orientation, membership acceptance, and commitment acceptance remain separate milestones. Limited orientation may use only currently permitted seed material and invitation previews. A retry returns the original creation identity and initialization; it does not rerandomize a persona, duplicate funding, or start replacement births after a decline.

Lifecycle, membership, quarantine, model configuration, and accepted obligations have distinct meanings even when stored together. Active does not mean continuously invoking inference. Completing or closing a task does not automatically retire the persona. A pause, model change, membership removal, retirement, or reactivation must not erase accepted work, pending effects, actual spending, uncertain exposure, or applicable birth counters.

Retirement requires a recorded disposition for every open obligation: an accepted handoff, authorized cancellation, or explicit blocked disposition where the existing lifecycle policy permits it. A blocked obligation remains unresolved, attributable to its existing responsibility, and visible with its condition and escalation route or missing responsible party. Recording a block neither invents a human or peer's acceptance nor establishes completion. A retired persona cannot execute that work merely because it remains its historical or blocked owner.

Quarantine is an independent restriction. Reactivation requires a new authorized lifecycle decision; it does not by itself clear quarantine, renew grants, restore revoked membership, replenish resources, or authorize replay of old operations. Ordinary work resumes only after the applicable recovery, membership, authority, and funding conditions hold. A transition that changes relevant eligibility must invalidate affected in-flight decision authority before another operation is admitted. Late receipts remain available for evidence and accounting without restoring authority.

Continuing identity and the original starting-state reference survive permitted changes and restoration. This is not a requirement to retain sensitive payloads forever: erasure preserves an honest minimal provenance disposition under the retention policy, not invented replacement seed values. Restoration must not activate a second independent host or bypass the separately gated cross-host activation boundary. Historical source privacy and the existing execution trust boundary remain unchanged.

## Progress guarantees need explicit assumptions

Being discoverable, being considered by a scheduler, receiving a funded decision opportunity, accepting work, and achieving a checked outcome are different events. A fairness claim must identify which event it guarantees and under what operating conditions.

For eventual consideration, declare continued scheduler progress, recovery assumptions, opportunity identity and queue-mutation rules, and how long the relevant eligibility persists. A fixed finite queue with a persistent cursor is one possible model, not a mandated implementation. A deployment with concurrent insertion, deletion, or restart must demonstrate the corresponding progress argument; repeatedly returning to an unchanged ineligible prefix is not sufficient. Conditions outside the guarantee remain visible rather than being reported as timely consideration.

Consideration does not guarantee admission. Current permission, expiry, available resources, and foreground priority across the shared resource root still apply. Nor does an admitted opportunity guarantee voluntary acceptance: every offered participant may decline. Finite allowances, meaningful waits, and honest unowned or blocked dispositions must therefore remain available. Repeated offers, reminders, or replacement births must not turn lack of acceptance into an unbounded inference loop.

A stronger claim of eventual accepted coordination needs explicit assumptions about responsive participants and admissible opportunities. A claim of eventual completion additionally needs assumptions about feasible work, available capabilities, dependencies, external observations, and sufficient authorized resources. The design does not assume those conclusions merely because scheduling is fair.

A cycle in which each commitment requires another's final output must be exposed. Participants may accept bounded provisional inputs and compatibility checks, revise dependencies within authority, or stop with an honest block. Provisional execution does not satisfy final dependencies or prove convergence. Any progress theorem that assumes acyclic final dependencies must identify that restriction rather than claim coverage of all permitted cooperative work.

## Verification obligations

A formalization must identify its state, initial conditions, admitted transitions, and the precise meaning of acceptance, authority, lifecycle, ownership, evidence, and resources. Show invariant preservation for each transition and for arbitrary finite reachable histories; establish non-vacuous legal histories as well. Do not obtain a purported preservation result solely by admitting transitions whose postcondition is already the entire desired invariant.

| Obligation | Proof or implementation boundary to make explicit |
|---|---|
| Every current responsibility has applicable acceptance. | Authenticate acceptance or accepted delegation for the exact commitment and terms; an uninterpreted acceptance predicate is a trusted assumption, not an implemented consent protocol. |
| Handoff and amendment preserve accountability. | Validate current terms, owner, eligible receiver, and authority atomically; reject stale races while retaining prior history and unresolved gaps. |
| Lifecycle changes preserve identity and obligations. | Separate immutable provenance references from retained payloads, blocked work from completion, and quarantine from ordinary lifecycle. Verify stale-decision fencing and recovery. |
| Coordination is representable without a mandatory team ritual. | Include alternative divisions under the same core rules, a one-founder trace with no additional birth, and an all-decline trace. These witnesses do not establish useful or unscripted behavior. |
| Scheduling makes the claimed progress. | State temporal and environmental assumptions, cover the supported mutable queue and restart semantics, and distinguish consideration from admission, acceptance, and successful completion. |
| Starts and retries preserve the controlling allowance. | Use authoritative work-to-episode lineage and shared-root admission; distinguish pre-admission rollback from settlement after admission or possible dispatch. |

For each theorem, record the exact design and model revisions, property, assumptions, exclusions, and mapped requirement identifiers. A formal result also records the pinned proof toolchain and dependencies, actual compiler outcome, and the axioms or other trusted mechanisms used. An uncompiled source file, an unchecked proof placeholder, a bounded Python model, and a kernel-checked theorem must be reported as different evidence. State any remaining unproved obligations rather than treating a successful build alone as complete coverage.

A proof about an abstract model does not prove that an implementation supplies authentic receipts, durable state, atomic transitions, current access checks, or the modeled scheduling behavior. Map concrete operations and recovery paths to the model and provide refinement evidence or explicitly narrower implementation tests. Missing correspondence stays an open assurance gap. Behavioral comparisons, privacy and security assurance, domain truth, and cross-host exclusivity are not inherited from a protocol theorem.

## Acceptance refinements under existing identifiers

These are specified refinements of the existing catalogue, not new numbered requirements or reported passes. Mechanical success, behavioral benefit, and complete delivery remain separate outcomes.

| Existing gates | Situation and required observation |
|---|---|
| M01, M05, M06, M18 | Repeat creation, decline membership, and race births for remaining capacity. Preserve one creation receipt and seed, separate onboarding milestones, current preview access, and bounded charges; no automatic replacement or invented commitment. |
| M02, M03, M06, M19 | Offer a handoff, decline it, change terms, replay acceptance from another commitment, and race two receivers or a revocation. Only a current accepted transfer or authorized disposition changes responsibility; rejected transitions preserve accountable work. Also test a change genuinely covered by an already accepted delegation. |
| M03, M16, X02 | Retire after an accepted handoff; separately retire with an authorized visible blocked disposition. Preserve identity and unresolved effects, keep the blocked obligation unresolved, and prevent retired or quarantined execution. Where X02 applies, exercise the institutional exit case as well. |
| M03, M15, M16, B10 | Change the model, pause, quarantine, restart, and explicitly reactivate. Preserve provenance and obligations, reject old decision authority, and recheck current membership and grants. Mechanical continuity alone does not pass B10's behavioral assessment. |
| B01–B04, B08, B12 | Compare permitted alternative divisions, one-founder work without birth, and declined offers. Inspect actual policy and attributed choices; do not treat the abstract ability to express alternatives as a behavioral pass. |
| B05, B07, B09 | Trace a peer's evidence to an actual revision and fresh assessment; compare relevant retained experience with matched withheld experience. Messages, receipt links, and memory inclusion alone are insufficient evidence of benefit. |
| M22 | Create a final-only dependency cycle. Expose the deadlock; use only expressly accepted bounded provisional work or an honest stop. Unresolved final compatibility still blocks full acceptance. |
| M04, M25, M26 | Place eligible work beyond future or paused entries, mutate the queue, and restart. Demonstrate the declared consideration guarantee and durable wake behavior without promising admission during expired funding, shared-root foreground demand, or universal refusal. |
| M04, M07, M23, M25 | Fail immediately before admission and after possible dispatch; add a late collaborator and retry. Apply the [failed-start boundary](EXPLORATION-ACCOUNTING.md#failed-starts-and-admitted-attempts), preserve real charges and unknown exposure, and prevent a fresh per-participant allowance or reuse of protected finishing capacity. |

The primary requirement families are PER-01/PER-04/PER-05, NED-02, COL-01–COL-06, GOV-01–GOV-04, SYS-01–SYS-04, and the existing evidence and privacy requirements. The [requirement index](../implementation/REQUIREMENTS.md) remains authoritative for identifiers; the [evaluation method](../evaluation/README.md) governs behavioral and public claims.
