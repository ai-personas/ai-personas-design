---
title: PersonaOS v1.0 — Project (an Environment type)
status: Stable
---

# 04 — Project (an Environment type)

> **Reader guide.** A project is a long-running workspace where AI Personas collaborate over weeks or months — designing a chip, writing a paper, building a robot. In v1.0, a project is a special type of environment (a `project_workspace`). In this document, you'll learn how milestones, obligations, peer reviews, and physical assets are tracked. **Prerequisites:** `00_VISION.md`, `05_ENVIRONMENT.md`. **Key terms:** *project_workspace* = environment type for multi-session work; *PhysicalAsset* = a real-world object the project manages; *obligation* = a commitment one persona makes to another; *completion ceremony* = the formal process for finishing a project.

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). This document specifies the project-workspace environment type, its item catalogue (OpenProblem, Milestone, Conjecture, Obligation, Disagreement, PeerReview, CitationGraph, ExternalAgent, PhysicalAsset, InstrumentAsset, PaymentBridge, ProjectPhaseState, AsBuiltReconciliation), and the INVESTIGATIVE + PROJECT_PROGRESS_ACCEPT pathway. *Invariant J8 is retired* — it was the old "project lineage" invariant from prior versions; in v1.0, multi-session work is an EnvironmentInstance of type `project_workspace`, so project lineage is now part of EnvironmentLineage (no separate mechanism needed). The "ProjectLineage" label persists as a documentation filter over EnvironmentLineage events whose `kind` starts with `project_*`.

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. Fully normative; RFC 2119 keywords carry normative force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174).

**In scope.** The `project_workspace` environment type and its item catalogue (Project, ProjectMember, OpenProblem, ProjectMilestone, ProjectItem, Obligation, Disagreement, PeerReview, ApprovalWorkflow, NotationConvention, CitationGraph, Conjecture, ExternalAgent, PhysicalAsset, InstrumentAsset, PaymentBridge, ProjectPhaseState, AsBuiltReconciliation, ExternalBudget, BudgetTranche, ExternalAttestation, ReplicatedAttestation). The INVESTIGATIVE and PROJECT_PROGRESS_ACCEPT acceptance pathways and contribution credit accounting.

**Out of scope.** Generic environment surfaces — membership, presence, ambient streams, observation surface, attention budget — defined in [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md). The kernel-level signing and lineage primitives (see [`01_KERNEL.md`](01_KERNEL.md)). The task classifier and pathway selection logic (see [`03_TASKS.md`](03_TASKS.md)).

**Supersession — v1.0 unification (Project IS an Environment type).** v1.0 unifies Project and Environment into a single ontology: a Project is an `EnvironmentInstance` of type `project_workspace` (registered in `KindRegistry.env_type_kinds` per [`05_ENVIRONMENT.md §3`](05_ENVIRONMENT.md#3-the-eight-base-types)). It is one type of environment among the others (`solo`, `pair`, `team`, `lab`, `debate`, `community`, `constrained`, `companion`, `project_workspace`, plus custom env blueprints). The rich item catalogue documented in this file is **the signature of the `project_workspace` env type**. These schemas attach to the env that hosts the work. **Invariant J8 is retired.** Multi-session work that prior versions called a "Project" is now an `EnvironmentInstance.type = project_workspace`. The "ProjectLineage" label persists only as a documentation filter over EnvironmentLineage events whose `kind` starts with `project_*`. The synonym `project` (as a top-level entity name) is retained only in logical-filter contexts per [`SPEC_CONVENTIONS.md §10`](SPEC_CONVENTIONS.md#10-terminology).

**Structural deviation.** Follows the compressed-opening pattern of [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md#33-compressed-opening-permitted): Background, Goals, and Definitions are folded into the supersession statement above and §1 ("What a project is"). The three §3.1 bookends (this section, the Risks table, and Open Questions) are present.

### 0.1 v1.0 unification — Project IS an Environment type (detail)

v1.0 unifies Project and Environment into a single ontology: **a Project is an EnvironmentInstance of type `project_workspace`** (registered in `KindRegistry.env_type_kinds` per `05_ENVIRONMENT §3`). It is one type of environment among the others (`solo`, `pair`, `team`, `lab`, `debate`, `community`, `constrained`, `companion`, `project_workspace`, plus custom env blueprints). The rich item catalogue documented in this file — OpenProblem, Milestone, Conjecture, Obligation, Disagreement, PeerReview, CitationGraph, ExternalAgent, PhysicalAsset, InstrumentAsset, PaymentBridge, ProjectPhaseState, AsBuiltReconciliation — is **the signature of the `project_workspace` env type**. These schemas attach to the env that hosts the work.

*A mapping table shows how each prior-version concept (Project entity, ProjectLineage, ProjectMember, etc.) maps to its v1.0 equivalent (EnvironmentInstance, EnvironmentLineage, EnvironmentMembership, etc.).*

**Technical detail:** See [A.1](#appendix-a1).

**Why unify.** Prior versions carried a parallel hierarchy (project ↔ env) that doubled the membership, lineage, and admission machinery without adding semantic distinction. The v1.0 audit (see `00_VISION §J8`) confirmed Project is structurally a specialised environment whose distinguishing feature is its richer item ontology, not a different containership pattern. Unifying simplifies routing (Mode B collapses into Mode A), shrinks the lineage scope count from 4 to 3 (task / env / domain), and removes ProjectMember vs EnvironmentMembership duplication.

**What this chapter is, after the unification.** This chapter remains the canonical reference for the `project_workspace` env type's item catalogue, members, ceremonies, and lifecycle. Every schema below — `ProjectMember`, `OpenProblem`, `Milestone`, `Conjecture`, `Obligation`, `Disagreement`, `PeerReview`, `CitationGraph`, `NotationConvention`, `ExternalAgent`, `PhysicalAsset`, `InstrumentAsset`, `PaymentBridge`, `ProjectPhaseState`, `AsBuiltReconciliation`, `ExternalBudget`, `BudgetTranche`, `ExternalAttestation`, `ReplicatedAttestation` references, etc. — is read as "a sub-schema attached to an EnvironmentInstance of type `project_workspace`."

**Documentation conventions in this chapter.**

| Legacy term (prior versions) | v1.0 reading |
|---|---|
| "Project" / "the project" | The host EnvironmentInstance (type=`project_workspace`) |
| `Project.project_id` | The env's `environment_id` (the same identifier; renamed in some references but data-equivalent) |
| `ProjectLineage` | EnvironmentLineage filtered by `kind` ∈ `project_*` family |
| `ProjectMember` | EnvironmentMembership with `role` resolved against KindRegistry.project_role_kinds |
| `ProjectProvenFacts` | EnvironmentProvenFacts on a `project_workspace`-typed env |
| `project_id` field on other schemas | Read as the env's `environment_id`; the field name stays for cross-doc compatibility |
| "Mode B routing" | Mode A routing on a `project_workspace`-typed env (Mode B distinction retires) |

**Migration of existing data (prior to current version).** Existing pre-v1.0 Project records map 1:1 to v1.0 EnvironmentInstance(type=`project_workspace`) records. The migration tool (`the migration tool`) performs the rename in metadata; underlying lineage, membership records, and CRDT state are preserved unchanged. `Project.project_id` becomes the env's `environment_id` (same ULID); cross-references in older docs continue to resolve.

**What this chapter still calls "Project" / "ProjectLineage" / etc.** For readability and continuity with prior-version sections, the legacy terminology remains in body text below. Treat each occurrence as a reading of the v1.0 model per the table above. New work should prefer "the project_workspace env" and "EnvironmentLineage of the project_workspace env" — but the legacy phrasing is not wrong.

## 0a. Plain-Language Guide

*Here's how multi-session team work is organised in PersonaOS, explained without jargon.*

**What is a project?**

A project is a long-running piece of work where a team of AI personas collaborates over weeks or months toward a shared goal. Think of it like a workspace for building a house, writing a research paper, or running a clinical study. A project has a charter (its mission statement), members with defined roles, milestones to track progress, and a complete history of everything that happened.

**Projects ARE environments**

In earlier versions of PersonaOS, projects and environments were separate things that had to be wired together. v1.0 simplifies this: a project is just a special type of environment called a "project workspace." It is one room among many (solo rooms, pair rooms, team rooms, labs, etc.) but with extra tools on the walls -- milestone boards, obligation trackers, citation ledgers -- that the other room types do not carry. If you already understand environments from the Environment document, a project is one of those with a richer toolkit.

**Project members, roles, and how they join**

Every project has members -- personas who have agreed to participate. Each member has a role: lead (the person steering the project), contributor (doing the work), reviewer (checking the work), or observer (watching but not working). Members can join through several paths: the project can be formed from scratch with a team proposal, members can be invited by the lead, recruited by other members, or they can apply on their own. Every admission is signed and recorded.

**Milestones, open problems, and conjectures**

A milestone is a measurable checkpoint -- "foundation poured," "first draft submitted," "prototype tested." Each milestone has clear criteria so everyone agrees when it has been reached. Open problems are questions the project has not yet answered. Conjectures are educated guesses the team is testing -- they start uncertain and move toward proven or refuted as evidence accumulates. All three are tracked as structured records, not just notes.

**Obligations -- promises team members make to each other**

An obligation is a formal commitment: "I will deliver the structural calculations by March 15." Both the person making the promise and the person receiving it must sign. Obligations track due dates, reminders, and evidence of completion. If a member leaves mid-project, their obligations can be formally reassigned to a successor through a signed handoff, so nothing falls through the cracks.

**Disagreements -- how the team handles conflicting views**

When team members disagree -- about a design decision, a research direction, a risk assessment -- PersonaOS does not suppress the disagreement. Instead, it records each position with its supporting evidence and tracks the disagreement until it is resolved. Resolution can come through synthesis (merging the best parts of each view), majority decision, deferral to the lead or an external authority, or even splitting the project into sub-projects that pursue different approaches.

**Peer review -- getting work checked by others**

Peer review is a structured multi-round critique process. Reviewers examine submitted work, may request revisions, and the cycle continues until accept or reject. Reviews can be named, single-blind, or double-blind. Separate from peer review, approval workflows handle sequential sign-off chains where each step must complete before the next -- like a permit moving through planning, fire, and building departments.

**Citation graphs -- tracking who contributed what**

The citation graph is the project's credit ledger. It records which persona contributed which idea, proof, design, or insight, and how heavily that contribution weighs. It also tracks external citations -- papers, standards, or prior work the project references, and any external work that references the project's output. Credits are frozen at the completion ceremony.

**External agents -- people and systems outside the project**

Not everyone involved in a project is a persona. Contractors, inspectors, suppliers, lab technicians, and regulatory bodies are "external agents" -- real-world participants who deliver into the project but do not have their own AI identity within the system. The project tracks their commitments, deliverables, and attestations (signed statements like an engineer's structural stamp or a city inspector's approval).

**Physical assets -- real-world things the project manages**

Many projects produce something physical: a house, a device, a patient's treatment plan, a production run. A physical asset record tracks the real-world object alongside the digital designs that describe it. The project cannot be declared complete until the physical asset reaches its target state or is explicitly marked out of scope. This closes a gap where "design finished" used to silently mean "project done."

**Budget and payment**

Projects track costs through external budgets that record planned, committed, and spent amounts in any unit (dollars, labour hours, kilowatt-hours, kilograms of concrete). Budgets can be tranched -- released in stages as milestones are reached. When actual payment is needed, a payment bridge creates a formal handoff between the project's tracking and a human who executes the payment. The system never touches money; it only signs proposals and receipts.

**Project phases -- stages of work with different rules**

A project moves through phases (design, fabrication, regulatory review, iteration), and different phases have different expectations. During a "waiting for external approval" phase, the system will not incorrectly flag the project as stalled just because no internal work is happening. Each phase declares whether stall detection should be suppressed, and for how long, before the system starts asking questions again.

**Completion ceremony -- how a project wraps up properly**

When all critical milestones are reached and all physical assets are accounted for, the project enters its completion ceremony. Every member drafts a retrospective. The lead signs a final summary. The citation graph is frozen. All artifact bundles are locked. External agent commitments are closed out. Each member's contribution credit is written to their permanent record. The project's status moves to "completed" with a signed event, and eventually to "archived" -- never deleted, always replayable.

## 1. What a project is

A [**Project**](12_GLOSSARY.md#p) is an [EnvironmentInstance](12_GLOSSARY.md#e) of type `project_workspace` — the unit of multi-session, multi-persona, long-arc work. It holds: a charter, member personas with roles, in-progress artifacts, open problems, conjectures, obligations, persistent methodological disagreements, peer review processes, shared notation, citation graph, milestones, and an append-only `EnvironmentLineage` (invariant J9, the project_* event subset is the documentation alias formerly labelled J8) + a `EnvironmentProvenFacts` CRDT (the project_workspace env's facts; formerly labelled `ProjectProvenFacts`).

Projects are **optional**. Tasks with no host env or with a non-project env route through Mode C (ephemeral env) or Mode A (the host env, when it is not project-typed). The `project_workspace` env type activates for work warranting persistent multi-session coordination with the rich item catalogue.

## 2. Project schema (project/2)

*The Project dataclass defines the complete state of a project: its identity, charter, domain, membership, status, items, obligations, memory, lineage, milestones, external participants, physical assets, budgets, approval workflows, and metadata.*

**Technical detail:** See [A.2](#appendix-a2).

## 3. ProjectMember

*The ProjectMember dataclass records a persona's membership in a project, including role (lead, contributor, reviewer, observer, or transitional roles during handoffs), join/departure dates, contribution credit, consent records, retirement-pin status, and multi-principal attribution.*

**Technical detail:** See [A.3](#appendix-a3).

**Admission rule.** When the hosting project's `PrincipalAttribution.multi_principal_attribution_enabled = True`, member admission MUST set `principal_attribution_id` to one `PrincipalRef.operator_id` in the binding's `principals` list; admission without it refuses with `principal_attribution_missing_under_multi_principal`. When `multi_principal_attribution_enabled = False`, the field MUST be null; non-null values under single-principal projects refuse with `principal_attribution_unexpected_under_single_principal`. The field is set once at admission and cannot be mutated; transferring a member from one principal's attribution to another's requires `departure_ceremony` + fresh admission under the new attribution.

**Fork interaction.** When a `ProjectMember` persona forks mid-project, project membership for the children is governed by `MidProjectForkComposition.project_member_inheritance` (`02_PERSONA §7.4.7`): each child either `inherit` (becomes a ProjectMember inheriting parent's role, joined_at, contribution_credit, pinned_until) or `not_admitted` (not a ProjectMember; may apply separately via standard §14.1 admission). For projects with `multi_principal_attribution_enabled = True`, inherited children carry forward parent's `principal_attribution_id` (via `MidProjectForkComposition.principal_attribution_inheritance` choice). Fork without a signed envelope for the project refuses with `midproject_fork_composition_missing`.

## 4. Lifecycle

*The project lifecycle state machine: PROPOSED to ACTIVE (on first work), ACTIVE to PAUSED (on inactivity), back to ACTIVE (on member action), ACTIVE to COMPLETED (milestones reached), COMPLETED to ARCHIVED (retention period), and a separate ABANDONED path with lessons-learned ceremony.*

**Technical detail:** See [A.4](#appendix-a4).

Transitions emit signed events to ProjectLineage. Each transition kind documented in v1.0 §01 §3.2.

### 4.1 Completion ceremony

When all critical milestones reached AND every `PhysicalAsset` (§26a.2) has met its `asset_completion_mode`-appropriate gate or been declared out of scope by signed operator action:

1. **Physical-asset closure (mode-aware)** — for each `PhysicalAsset` whose `ownership_kind = project_owned`:
   - if `asset_completion_mode = terminal_state_required`: current_state ∈ state_kind.terminal_states with required `ExternalAttestation` evidence, OR signed `physical_asset_out_of_scope`;
   - if `asset_completion_mode = publishable_state_attained`: signed `publishable_result_attained` event in project lineage with credentialed attestation (or peer-attested per §5.6 fallback);
   - if `asset_completion_mode = continuous_iteration`: project does NOT auto-complete; only operator-signed abandonment or hibernation terminates.
   `PhysicalAsset` entries with non-project ownership_kinds (shared_lab_facility, leased, vendor_facility) do not gate closure. Projects with no PhysicalAsset skip this step.
2. **Co-signed completion summary** — each member drafts; lead signs final retrospective.
3. **Citation graph snapshot** — internal credits frozen; external citations captured.
4. **Artifact bundle finalisation** — every bundle locked at current version; further edits require fork.
5. **External-agent closure** — each `ExternalAgent` either has all commitments delivered / released, or is recorded with outstanding obligations carried forward.
6. **Memory consolidation** — episodic memories consolidated into semantic project knowledge.
7. **Persona evolution credit** — final `contribution_credit` per member written to soul.state.json.
8. **Status → completed** with signed `project_completed` lineage event.

A project may also enter intermediate state `digital_complete_physical_in_progress` (signed) when all digital ArtifactBundles are accepted but the PhysicalAsset has not reached terminal state. This handles the long mid-build phase that pure-digital projects in prior versions never modelled.

**Multi-principal completion.** When the project's `EnvironmentInstance` carries a `PrincipalAttribution` (`01_KERNEL §2.4.3`) with `multi_principal_attribution_enabled = True`, step 8 above does not fire on a single operator signature. The kernel drafts a `MultiPrincipalAttestationQuorum` (`05_ENVIRONMENT §12c.4a`) with `target_event_kind = "project_completed"` and admits the completion ceremony only when the quorum clears (default: unanimous over weighted PrincipalRefs). The `project_completed` lineage event records the cleared quorum's `quorum_id` so audit can reconstruct who authorised completion. Degraded-path clearance (one principal structurally unreachable past `principal_unreachable_after`) is permitted under the same §2.4-analogue conditions documented in §12c.4a; the lineage event records `cleared_under_degraded_path = True` when applicable.

### 4.2 Abandonment ceremony

When leads + operator agree the project will not reach milestones:

1. **Stated reason** signed by abandoning party.
2. **Lessons-learned reflections** by each member.
3. **Artifact bundle freeze** at last state.
4. **Obligation discharge** — outstanding obligations marked `released_with_project_abandonment`.
5. **Memory + citations preserved**.
6. **Status → abandoned**.

Abandonment is data, not failure. Lessons carry forward; future projects benefit.

### 4.3 External-tool-required bypass

Prior versions specified operator-overridable paths around the 6th safety source (external-tool-required + novelty-check). v1.0 carries these verbatim.

*Three bypass paths (time-bound exception period, hedged-claim bypass, elevated requirement) and their lineage event types are defined for when required external tools are unavailable.*

**Technical detail:** See [A.5](#appendix-a5).

Anti-abuse: exceptions cannot be open-ended; max window 14 days per v1.0 default; renewal requires re-signing.

## 5. Contribution credit

Per-member accumulated.

*The contribution credit formula is a weighted sum of positive signals (verified artifacts, proven facts, discharged obligations, resolved disagreements, completed reviews, advanced conjectures) minus negative signals (dropped obligations, safety refusals caused), with configurable default weights.*

**Technical detail:** See [A.6](#appendix-a6).

`contribution_credit` is:
- Project-local (not transferable across projects directly).
- Co-signed at completion ceremony.
- Used for: citation graph ordering, future-recruit decisions by leads, audit.
- Distinct from persona-level fitness (which is the evolution credit).

## 6. OpenProblem

*The OpenProblem dataclass defines an unresolved question within a project, with statuses (active, dormant, resolved, abandoned, morphed) and links to related domain items and artifacts.*

**Technical detail:** See [A.7](#appendix-a7).

`morphed` = problem evolved into a related sharper version (new problem_id; old's lineage references new).

## 7. ProjectMilestone

*The ProjectMilestone and ProgressCriterion dataclasses define measurable checkpoints with criteria, target dates, and achievement status.*

**Technical detail:** See [A.8](#appendix-a8).

## 8. ProjectItem — generic domain-agnostic project entity

v1.0 substrate replaces the previously hardcoded `Conjecture` / `ProofAttempt` / `ProofGap` (math-domain-shaped) with a single generic `ProjectItem` discriminated by an emergent `ItemKind` resolved against `KindRegistry.item_kinds` (`06_DOMAIN §7.6`). The hardcoded classes become MetaRegistry-seeded examples (§8.1) for math/research domains; other domains add their own item kinds via `ProposedItemKind`.

*The ProjectItem dataclass is the single generic item class, with kind, status, payload, blocking/blocked-by edges, nesting, confidence, and links to open problems, artifacts, and obligations.*

**Technical detail:** See [A.9](#appendix-a9).

`ProjectItem` is the only substrate item class. Status FSM is data, not code; advancement signals (`advance_signal_hooks` in `ProposedItemKind`) dispatch through the resolved ItemKindEntry rather than hardcoded transition logic. Blocking semantics are substrate (`blocks` / `blocked_by` edges); the kernel refuses status advancement on an item whose `blocked_by` list contains any non-terminal-status item.

### 8.1 MetaRegistry-seeded item kinds (illustrative)

The following item kinds ship as MetaRegistry seeds **only because** they have proven across multiple domains; substrate does not depend on them. New domains add item kinds via `ProposedItemKind` (`06_DOMAIN §7.5`) without modifying substrate.

*Twelve MetaRegistry-seeded item kinds are defined: conjecture, proof_attempt, proof_gap (math/research), design_hypothesis, buildability_concern (construction), differential_diagnosis (clinical), risk, schedule_entry (universal), change_order, punch_list_item (construction), and priority_claim (research/IP). Each defines payload schema, status FSM, and advance signal hooks.*

**Technical detail:** See [A.10](#appendix-a10).

The `priority_claim` ItemKind is **substrate-pure**: the substrate provides only the lifecycle (drafted → witnessed → asserted → established) and the schema *shape*. Specific `claim_kind` and `disclosure_state` values are emergent KindRegistry entries per domain. A research domain catalogs `claim_kind={publication, patent, prior_art}`; a journalism domain catalogs `claim_kind={scoop, exclusive}`; a legal domain catalogs `claim_kind={trade_secret, common_law_priority}`. The substrate doesn't know or care.

Each seed entry signs into the MetaRegistry with `cross_domain_promotable=True` and lives there until drift (§3.1) demotes it. The math seeds (conjecture / proof_attempt / proof_gap) are functionally identical to the previously hardcoded `Conjecture` / `ProofAttempt` / `ProofGap` classes; the difference is they are now **data in the registry**, not **schemas baked into substrate code**.

## 9. Obligation — inter-persona commitment

*The Obligation dataclass defines a formal inter-persona commitment with obligor, obligee, discharge criteria, due date, reminders, grace period, and status lifecycle (active through discharged, overdue, released, or dropped).*

**Technical detail:** See [A.11](#appendix-a11).

**Both parties sign at commitment.** An obligation isn't valid unilaterally. Discharge requires evidence (verifier-attested artifact, signed acceptance).

**Fork interaction.** When the obligor persona forks mid-project, per-obligation inheritance is governed by `MidProjectForkComposition.obligation_inheritance` (`02_PERSONA §7.4.7`). Two policies admissible: `reassign_per_child` (an `ObligationReassignment` §9.1 envelope is drafted naming the named incoming-child as new obligor; obligee MUST cosign per §9.1; obligation enters `obligation_reassignment_pending` until cosign) OR `discharged` (status → `released_with_member_departure` at fork — safe default; loses continuity). Splitting one obligation across two children concurrently is **refused** with `obligation_split_refused_creates_ambiguous_accountability` — substrate enforces single-obligor semantics.

### 9.1 ObligationReassignment — transfer commitment to a successor

Previously, when an obligor persona departed (retirement, planned departure, project member removal), all active obligations auto-discharged with `status = "released_with_member_departure"` (`§9` status enum + `§25` multi-year continuity rule line 1822–1824). For long-arc projects this destroyed continuity: accumulated commitments evaporated, and the successor had to re-commit every open obligation from scratch — with no acknowledgement that the work-in-progress had a prior owner.

`ObligationReassignment` is the tri-signed envelope that **transfers** an active obligation from outgoing to incoming obligor without discharge. Original `committed_at` is preserved (audit retains commitment provenance); a reassignment lineage chain accumulates per obligation.

*The ObligationReassignment dataclass and its admission rules define a tri-signed (outgoing, incoming, obligee) transfer of an active obligation, with states from drafted through fully_signed/applied or refused/expired.*

**Technical detail:** See [A.12](#appendix-a12).

**Composition with `§25` multi-year continuity.** When a project enters HIBERNATING with active obligations, the §25 rules apply unchanged — frozen due_date, "released_with_hibernation_lapse" / "carried_forward" on reanimation. `ObligationReassignment` is a *pre-departure* primitive; the rule of thumb is "reassign before departure ceremony fires." A reassignment drafted but not fully-signed at departure-ceremony time auto-`expires`; the underlying obligation then follows §9 default behaviour.

**Composition with `§14.2 CohortDynamicsState`.** Successful reassignment registers as a continuity-positive signal (incoming and outgoing both demonstrated commitment to project's commitments). Refused reassignment (obligee declines) does NOT punish either party — the obligee has full discretion to refuse a successor.

**Honest limits.**

1. **Obligee discretion is absolute.** The obligee is the substrate's final authority on "do you trust the new obligor to deliver?" The substrate cannot compel reassignment acceptance; refusal returns the obligation to its §9 default path.
2. **Reassignment cannot resurrect a discharged obligation.** Once `status = "released_with_member_departure"` is signed (departure ceremony has fired), the obligation is closed; any new commitment requires a fresh `Obligation` mint with current `committed_at`.
3. **Lead-handoff composition.** `LeadHandoffCeremony` (`§25.1`) typically drafts a batch of `ObligationReassignment` envelopes — one per active obligation the outgoing lead held. The ceremony does not auto-accept on the obligee's behalf; each obligee receives a delivery and decides independently.

## 10. Disagreement — persistent dialectic

*The Disagreement, Position, and Resolution dataclasses define how conflicting views are tracked: each disagreement records two or more positions with evidence, and resolves via synthesis, majority, deferral, or split.*

**Technical detail:** See [A.13](#appendix-a13).

Disagreements are **explicitly preserved**, not suppressed. Default lifetime is open until resolved.

## 11. PeerReview — multi-round critique

*The PeerReview dataclass defines a structured multi-round review process with authors, reviewers, chair, anonymity tiers (named, single-blind, double-blind), comments, revision requests, author responses, and verdict. Anonymity enforcement rules govern how identities are hidden and when deanonymisation occurs.*

**Technical detail:** See [A.14](#appendix-a14).

**Persona-evolvable surface — none.** This is pure substrate topology; the field names and tiers are fixed (named, single_blind, double_blind cover the real-world space).

**Acceptance tests.** A-PR-AN1 (single-blind strips reviewer identity from author-visible projections), A-PR-AN2 (double-blind requires independent anonymity_holder under collapse), A-PR-AN3 (deanonymisation only on policy match + signed event), A-PR-AN4 (visibility tier consistent with anonymity_tier).

PeerReview is distinct from PANEL_ACCEPT:
- PANEL_ACCEPT: ephemeral LLM judges; per-task; minutes
- PEER_REVIEW: persistent persona reviewers; multi-round; days-to-weeks

Both may apply sequentially (panel first, then peer review).

## 11a. ApprovalWorkflow — sequential sign-off chain

PeerReview models **parallel multi-reviewer critique**. Many real-world processes need the orthogonal pattern: **sequential sign-off** where each step must complete before the next begins (a permit application moves applicant to planning to fire dept to building dept to final issue; an NDA moves drafter to reviewer to counter-party to counsel; a multi-party contract chains several signers). v1.0 adds `ApprovalWorkflow` as a first-class project-tier primitive.

*The ApprovalWorkflow and ApprovalStep dataclasses define a sequential sign-off chain where each step has an approver, deadline, required evidence kinds, and status. Steps advance one at a time; rejection or expiration at any step halts the workflow.*

**Technical detail:** See [A.15](#appendix-a15).

**Lifecycle:** the workflow is `pending` until `initiated`. On `initiated`, `current_step_index = 0` and step 0 moves to `in_progress`. When step 0 reaches `approved`, the next step begins; on `rejected` or `expired`, the workflow rejects/expires. The kernel refuses progress on a step whose `evidence_kinds_required` are not all satisfied by signed evidence refs. Skipped steps require operator co-sign.

**Distinct from PeerReview:**

| dimension          | PeerReview                          | ApprovalWorkflow                     |
|--------------------|--------------------------------------|---------------------------------------|
| topology           | parallel multi-reviewer              | sequential single-approver-per-step   |
| parties            | all personas, often internal         | mix of personas / external_agents /   |
|                    |                                      | operators                             |
| outcome            | accept / accept_with_revisions /     | approved / rejected / withdrawn /     |
|                    | reject + rounds                      | expired                               |
| evidence model     | comments + revision_requests         | evidence_kinds_required per step      |
| time horizon       | days-to-weeks (rounds)               | days-to-months (legal/regulatory)     |

Both may compose: a PeerReview accept may be one ApprovalStep in a larger workflow.

## 12. NotationConvention

Notation conventions support both authored (from DomainContext) and emergent (see [`06_DOMAIN.md §5`](06_DOMAIN.md)).

*The NotationConvention dataclass defines a project- or domain-scoped symbol with its meaning, formal definition, scope, introduction/deprecation status, and supersession chain.*

**Technical detail:** See [A.16](#appendix-a16).

## 13. CitationGraph

*The CitationGraph, InternalCredit, and ExternalCitation dataclasses track the project's credit ledger: internal contributions by persona (with domain-emergent contribution kinds) and external citations in both directions (outgoing and incoming).*

**Technical detail:** See [A.17](#appendix-a17).

## 14. Project membership flow

There are **four admission paths** in v1.0. The fourth — formation via `EnvFormationProposal` — is v1.0's preferred path for *creating a new project*; the three legacy paths apply to *joining an existing project*. The unification (§0) means a Project IS a `project_workspace`-typed env, so env-formation and project-creation are the same operation.

*Four admission paths: (0) formation via EnvFormationProposal for new projects, (1) invited by operator/lead, (2) recruited by persona-led cohort assembly, (3) self-proposed by discovering persona. Each path's consent flow and use-case is specified.*

**Technical detail:** See [A.18](#appendix-a18).

**Which path to use:**
- *Creating a new project from scratch* → Path 0 (EnvFormationProposal)
- *Joining an existing project as a new member* → Path 1, 2, or 3 depending on who initiates
- *Federating with another kernel's project* → joined-env path (09_PROTOCOLS §3C) — which itself is a special case of EnvFormationProposal with cross-kernel recruits

Departure:

*Four departure paths: voluntary leave, operator/lead removal, persona retirement (membership auto-paused, obligations released), and project end (completion/abandonment finalises).*

**Technical detail:** See [A.19](#appendix-a19).

### 14.1 Cohort assembly event taxonomy

*The complete cohort assembly event taxonomy lists core events (COHORT_REQUEST, RECRUIT_PROPOSAL, etc.), extended events (PROJECT_INVITATION, ENV_INVITATION, etc.), and v1.0's extended COHORT_DENIED reason set.*

**Technical detail:** See [A.20](#appendix-a20).

**CohortConstraint.** Multi-disciplinary projects need cohort composition guarantees — "this cohort must include at least one persona of each {theoretical, experimental, computational} contribution_kind." v1.0 expresses this in a substrate-pure way: the constraints reference emergent `contribution_kind` entries; the substrate enforces the structure, not the values.

*The CohortConstraint dataclass defines required contribution kinds, minimum/maximum counts, independence rules (disjoint affiliations/organisations), and enforcement points (admission, milestone, ceremony).*

**Technical detail:** See [A.21](#appendix-a21).

Cohort assembly events (list above) are extended: any `RECRUIT_ACCEPTED` or `PROJECT_INVITATION_ACCEPTED` that would leave a required-kind count below its minimum at the enforcement point emits `cohort_constraint_unsatisfied` (signed). The lead persona or operator MUST add a recruit of the missing kind before the cohort MAY proceed past the gate.

### 14.2 CohortDynamicsState — continuous team-cohesion evolution

`CohortConstraint` (§14.1) gates the cohort's *composition* at admission and milestone gates — it checks that required kinds are present. It says nothing about *how the team is working together* once formed. For long-arc projects, the cohort's cohesion, fractiousness, and role-health evolve continuously; a project lead and an operator need a signed read on that evolution without redoing peer review or running custom surveys.

*The CohortDynamicsState dataclass tracks continuous team health: cohesion score, average pairwise trust, joint-success ratio, disagreement resolution ratio, role health per kind, fractiousness index, throughput drift, and a band (healthy/watch/intervene/dissolve_proposed) with configurable thresholds.*

**Technical detail:** See [A.22](#appendix-a22).

**Recomputation cadence.** `CohortDynamicsState` is recomputed cheaply on every project lineage event that touches a cohort member: `obligation_discharged`, `disagreement_recorded`, `disagreement_resolved`, `peer_review_resolved`, `persona_relationship_state_changed`, `milestone_reached`. The composite is a weighted sum over already-signed events, so the kernel does not run new probes.

**Band transitions.**

*Four band levels with escalating actions: healthy (dashboard only), watch (lead notified), intervene (operator notified, new obligations refused), dissolve_proposed (lead + operator must co-sign to keep cohort intact).*

**Technical detail:** See [A.23](#appendix-a23).

**Composition with `02_PERSONA §11.4`.** `CohortDynamicsState` aggregates `PersonaRelationshipEdge` data over the cohort's pair-set. When an edge transitions to `ended`, the affected dyad's pair-scoped contribution drops from the avg; if many edges end concurrently, `fractiousness_index` rises and may trigger band downgrade.

**Composition with §14.1.** `CohortConstraint` checks structure (kinds present); `CohortDynamicsState` checks health (kinds *functional*). A cohort can satisfy `CohortConstraint` while failing `CohortDynamicsState` (composition present but disputatious); the reverse is also possible (small functional cohort missing a required kind). Both gates run independently at milestone gates.

**Honest limits.**

1. **Composite is an aggregate of already-signed events.** A cohort whose dysfunction never produces signed events (silent disengagement, side-channel coordination) registers healthy. The substrate cannot detect what nobody reports.
2. **Band thresholds are operator policy.** The defaults (0.70 / 0.55 / 0.40) are starting points; long-arc research cohorts may tolerate higher fractiousness than safety-critical construction cohorts. Operator policy is the right place to set this.
3. **Dissolve is heavyweight.** Triggering DISSOLVE_PROPOSED is intended to be rare; the substrate logs every band transition so a project lead can intervene before dissolve becomes the only path.

**Acceptance tests.** A-CD1 (recompute on every relevant lineage event), A-CD2 (band transition signed), A-CD3 (intervene band refuses new high-stakes obligations until restored), A-CD4 (dissolve_proposed requires lead + operator pin to keep intact), A-CD5 (composition with §14.1 — both gates run independently at milestones).

**Fork interaction.** When a cohort member forks mid-project, CohortDynamicsState recomputes reactively after `MidProjectForkComposition` (`02_PERSONA §7.4.7`) applies — children's edges form fresh per `edge_inheritance` policy; band-degradation may spike if many edges convert to `ended_at_fork`. **Substrate refusal**: forks initiated when the cohort is in `dissolve_proposed` band are **refused** with `fork_refused_cohort_dissolving` — fork during dissolution is incoherent. Operators planning fork of a healthy-cohort member SHOULD consider drafting a `PlannedDeparture` (§14.2.1) for the parent persona alongside the fork composition envelope, giving the cohort dynamics anticipatory rebalance over the parent-persona-disappearance event.

### 14.2.1 PlannedDeparture — graceful rebalance envelope

Previously, when a member departed (retirement, role change, project leave), `CohortDynamicsState` (§14.2) recomputed *reactively* from the resulting `PersonaRelationshipEdge` ends — fractiousness_index rose, band may have transitioned to `intervene` or `dissolve_proposed`, the cohort suddenly refused high-stakes obligations. For *scheduled* departures (operator knows 6 months in advance that Mira intends to retire) this abruptness was avoidable.

`PlannedDeparture` is the signed envelope that declares a member's scheduled departure ahead of time. `CohortDynamicsState` consults active PlannedDepartures and applies *anticipatory* rebalancing across the declared `rebalance_window`, smoothing the band transition rather than spiking it on departure day.

*The PlannedDeparture, EdgeTransferHint, and ObligationReassignmentHint dataclasses define a scheduled departure with rebalance window, reason, edge-transfer hints, obligation-reassignment hints, lead-successor candidate, and state machine (drafted/active/departure_fired/cancelled). Admission rules and anticipatory rebalance formula are included.*

**Technical detail:** See [A.24](#appendix-a24).

**Composition with `LeadHandoffCeremony` (§25.1).** A PlannedDeparture for a `lead`-role member typically drafts a LeadHandoffCeremony at `departure_date - rebalance_window`, giving the incoming lead the full rebalance window to operate in the `incoming_lead` overlap role. Operator may draft the handoff manually if preferred.

**Composition with `02_PERSONA §7.5` retirement.** A PlannedDeparture preceding a persona retirement schedules the project-side cleanup before the persona-side FSM transition. The departing persona's `ProjectMember.pinned_until` (`§3`) is auto-cleared at the moment PlannedDeparture transitions to `departure_fired` (no separate operator action required to clear the pin once the planned-departure path is complete).

**Honest limits.**

1. **Edge transfer is a hint, not a guarantee.** PersonaRelationshipEdge formation between the counterparty and the suggested transfer target requires consent per `02_PERSONA §11.4` — the suggested target may refuse, the counterparty may refuse, or both. The substrate ships the suggestion; the participants execute the edge formation independently.
2. **Operator cancel does not retroactively undo anticipatory rebalance effects.** If CohortDynamicsState transitioned `intervene` band during the anticipatory window (e.g., because the rebalance combined with other negative signals), the band stays until the post-cancel recompute restores it. Anticipatory rebalance is not a binding commitment.
3. **Operator-tunable `rebalance_window` is load-bearing.** Too short (e.g., 7 days for a multi-month departure) yields the same abrupt transition; too long (e.g., 2 years) ties up operator attention for unrealistic horizons. Default 90d is a starting point; operators should set per-project based on the project's natural cadence.
4. **No multi-departure aggregation.** When two members both file PlannedDeparture in overlapping windows, CohortDynamicsState applies both anticipatory rebalances independently. If the combined rebalance would force the cohort below `dissolve_proposed`, the second-filed PlannedDeparture refuses with `cohort_dissolve_threshold_reached`; operator must resolve before further departures.

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9g — A-PD*` (planned departure).

**Fork interaction.** PlannedDeparture and mid-project fork are distinct primitives that may compose: a `lead`-role persona's planned-departure may *include* a fork into successor children rather than a simple handoff (the parent persona retires; one child takes over with the parent's history). When `MidProjectForkComposition.lead_role_inheritance = "one_child_inherits"` AND a PlannedDeparture is active for the parent, the fork timing SHOULD align with `departure_date` so anticipatory rebalance smooths the transition. **Substrate refusal**: forks initiated within 7 days of an active emergency PlannedDeparture's `departure_date` are **refused** with `fork_refused_imminent_departure` — the substrate refuses to add fork-composition complexity to imminent departure logistics.

## 15. ProjectLineage event types

*The complete list of ProjectLineage event types: project lifecycle (proposed, activated, paused, completed, abandoned, archived, reanimated, forked, morphed), membership, charter, domain, artifacts, open problems, conjectures, obligations, disagreements, notation, citations, milestones, tools, reviews, sessions, tasks, as-built reconciliation, credentials, and cohort dynamics.*

**Technical detail:** See [A.25](#appendix-a25).

## 16. PROJECT_PROGRESS_ACCEPT and INVESTIGATIVE

For INVESTIGATIVE projects:

*The evaluate_project_progress function computes a ProjectStateDelta (milestones reached, open problems resolved, conjectures advanced, obligations discharged, proven facts added, ambient signals) and returns an AcceptanceResult with aggregate progress score.*

**Technical detail:** See [A.26](#appendix-a26).

### 16.1 ProgressAggregator schema and rolling-window math

The explicit schema is specified below.

*The ProjectStateDelta and ProgressAggregator dataclasses track per-session progress deltas and a rolling EMA (exponential moving average) with status flags (thriving, active, stalled, regressing).*

**Technical detail:** See [A.27](#appendix-a27).

Stalled or regressing flags trigger operator alert + persona-level reflection. Aggregator state lives on the Project record; updates emit signed `PROGRESS_AGGREGATED` lineage events.

## 17. Forking and morphing

### 17.1 Project fork

*Three fork inheritance policies: inherit_all (full membership + artifacts + conjectures + notation + citations), inherit_summary (co-signed summary + notation + citations, no in-progress artifacts), inherit_seed (charter + domain + notation, clean state).*

**Technical detail:** See [A.28](#appendix-a28).

Forks emit `project_forked` lineage event. Parent project unchanged.

### 17.2 Project morph

Charter or domain changes substantially:
- **Charter version bump** (charter_version++ signed; project continues)
- **Morph into new project** if change is structural (different DomainContext, different problem space; new project_id; parent reference; original marked `morphed_into=new_project_id`)

Threshold: charter-classifier judgment + operator confirmation.

## 18. Multi-environment hosting

A project may host in multiple persistent environments simultaneously.

*Example: a project may list multiple environment IDs with one designated as primary.*

**Technical detail:** See [A.29](#appendix-a29).

When task addressed to project without env_id:
- requester present in one of (envs) → that env
- requester present in N → highest activity_recency
- else → primary_environment_id

ArtifactBundle CRDT operates project-wide; env-local ambient streams stay env-scoped.

**Project ⟷ Environment composition (v1.0).** Project and Environment are **sibling COORDINATION-tier entities**, neither subsumed by the other:

- **Environment** answers "where am I present and who is here?" (presence layer; ambient stream; presence_state; mood; attention_budget).
- **Project** answers "what are we working on over time?" (work layer; lineage; milestones; obligations; contribution_credit).
- They compose **many-to-many** via this `environments` field; a persona occupies environments and participates in projects **simultaneously**.

**`project_workspace` environment type (v1.0; `05_ENVIRONMENT §3`).** Some projects warrant a *dedicated* presence space whose lifetime tracks the project's lifetime — the "war room", "project channel", "dedicated lab bench". For these, v1.0 supplies the `project_workspace` environment type:

- One-to-one binding: `Environment.project_bound_to = project_id`; one project workspace env per project, one project per project workspace env.
- Membership auto-synchronised with `ProjectMember`.
- Activity window inherited from the bound project's pace.
- Lifecycle events `project_workspace_paused / completed / archived` emit on the env when the bound project's FSM advances.
- The project workspace env continues to exist in dormant/archived state after project completion for audit replay; it is not deleted (J9 append-only).

A project may **both** be hosted in shared environments (acme_office, lab) **and** have its own `project_workspace`-typed env. The dedicated project workspace env is optional; many projects work fine in shared envs.

## 19. Cross-domain transfer

When a project's domain context cross-references another domain's skills/conventions:

*The CrossDomainTransfer dataclass records a transfer of a registered kind (skill, convention, lesson, etc.) between source and target domains with trust scores and usage counts.*

**Technical detail:** See [A.30](#appendix-a30).

Anti-leakage rules (see [`06_DOMAIN.md §11.1`](06_DOMAIN.md#111-anti-leakage-5-risks)): five rules block user-tagged, org-tagged, and project-tagged data from cross-domain transfer without consent, require operator review for proprietary/IP-flagged material, and require both operators' approval for cross-org transfer.

### 19.1 Multi-tenant cross-org joint projects

A joint project shared between two (or more) organisations — ORG_A and ORG_B collaborating on one product spec, two research institutes co-authoring one programme, two municipalities co-funding one infrastructure plan — is a topology v1.0 carries through composition of existing primitives rather than a separate subtype. This section consolidates the primitives that interact and the order in which they engage. None of what follows is new substrate; it is the wiring guide.

**Companion section:** `06_DOMAIN §19.1` covers the *artifact / skill transfer* mechanics between two orgs (policy intersection, data classification, dual-signing of `CrossOrgTransfer` events, revocation propagation). This `§19.1` covers the *joint project formation* mechanics (member attribution, charter ratification quorum, completion quorum, derivation provenance). The two compose: a joint project's ongoing work emits `CrossOrgTransfer` events when explicit artifacts move between orgs (per `06_DOMAIN §19.1`) and emits `DerivationProvenanceEdge` events when implicit derivation occurs (per `08_KNOWLEDGE §16b`).

**Primitives engaged.**

| Primitive | Section | Role in a joint project |
|---|---|---|
| `PrincipalAttribution` | `01_KERNEL §2.4.3` | Names the N principals and their `cosign_quorum_weight`. Set `multi_principal_attribution_enabled = True`. |
| `PrincipalRef` (cross-tenant) | `01_KERNEL §2.4.3` | When principals belong to different `tenant_id`, the attribution carries `cross_tenant_acknowledged = True` and a `CrossTenancyAgreementRef` (operator-authored). |
| `ProjectMember.principal_attribution_id` | `§3` (this doc) | Set at admission; binds each member to one PrincipalRef. |
| `EnvironmentMembership.principal_attribution_id` | `05_ENV §5` | Mirrors above under the v1.0 project-is-env-type unification. |
| `MultiPrincipalAttestationQuorum` | `05_ENV §12c.4a` | Required at `env_charter_ratified` and `project_completed`; default unanimous. |
| `ScopeTags.org_id` | `08_KNOWLEDGE §5` | Each member's contributions are tagged with their PrincipalRef's tenant org id; retrieval honours scope filters per `§7.1`. |
| `DerivationProvenanceEdge` | `08_KNOWLEDGE §16b` | Soft-bound or mandatory edge between consulted memories and derived contributions; covers implicit cross-principal derivation that anti-leakage rules 1-5 (above) cannot see. |
| Anti-leakage rules 1-5 | `§19` (above) | Filter explicit cross-domain transfer of named artifacts. RISK B (org_id) and RISK E (cross-org) compose with DPE. |
| `ExternalAgent` | `§26a.1` | When one party participates without joining the kernel (e.g., legal counsel from each side reviewing IP boundaries), they admit as ExternalAgents, not as personas. |
| `DomainHarvest.visibility_tier` | `06_DOMAIN §13a` | A joint project's harvest at `tenant` tier resolves to the principals' shared tenant if `cross_tenant_acknowledged = True`; otherwise restricted to `private`. |

**Formation sequence.**

*Six-step formation sequence for cross-tenant joint projects: (1) pre-formation cross-tenancy agreement, (2) principal attribution declaration, (3) env formation proposal with cohort invites from both tenants, (4) charter ratification via multi-principal quorum, (5) ongoing work with anti-leakage and derivation provenance enforcement, (6) completion via second multi-principal quorum.*

**Technical detail:** See [A.31](#appendix-a31).

**Honest limits.**

1. **Cross-tenancy agreements are policy, not substrate.** The substrate carries a `CrossTenancyAgreementRef` by id; it does not parse the agreement's legal content. Disputes about whether the agreement permits a specific data flow remain operator / legal responsibility. `OQ-PROJECT-4` (§21a) tracks the broader question of whether substrate should enforce per-artifact licence inheritance.
2. **No per-principal lineage masking.** All EnvironmentMembers see the full `EnvironmentLineage`. If ORG_A wishes to keep a specific member-admission event invisible to ORG_B, the substrate refuses — lineage is append-only and visible to all members per `05_ENV §13`. The mitigation is to not admit the sensitive member to the joint env in the first place (run them in an ORG_A-only env that produces artifacts ORG_B can consume through `CrossDomainTransfer`).
3. **MultiPrincipal quorum can deadlock.** If one principal becomes structurally unreachable, the degraded-path clearance (§12c.4a) requires `principal_unreachable_after` cool-down plus non-principal kinship attestation. Until cool-down elapses, the project cannot complete. Operators should set `principal_unreachable_after` longer than `§2.4`'s 72h (default 30d; safety-critical envs ≥ 90d) to discourage one operator from unilaterally "running out the clock" on a co-principal.
4. **Federation across kernels is v1.1+.** A joint project where the two organisations run separate v1.0 kernels falls under cross-kernel federation, which v1.0 does not ship (per `05_ENV §12c.4`). The two paths exist: (a) host the joint project on one kernel with the other org's personas admitted as peer personas (v1.0); (b) wait for v1.1's federated env support (deferred). Path (a) requires the hosting kernel's operator to be one of the principals.
5. **ExternalAgent does not count as a principal.** Legal counsel, auditors, regulatory observers etc. admit through the ExternalAgent path (`§26a.1`) without becoming principals. They produce attestations, not signatures-of-authorisation; their attestations cannot satisfy a `MultiPrincipalAttestationQuorum`.

**Acceptance tests.** A-MT8 (CrossTenancyAgreementRef required for cross-tenant principals), A-MT9 (joint-env charter ratification requires multi-principal quorum), A-MT10 (recruit consent names PrincipalRef explicitly), A-MT11 (joint-env DerivationProvenancePolicy defaults to mandatory_for_cross_principal), A-MT12 (joint-env harvest at tenant tier requires CrossTenancyAgreementRef), A-MT13 (joint-project completion requires multi-principal quorum at `§4.1`), A-MT14 (ExternalAgent cannot satisfy MultiPrincipalAttestationQuorum).

## 20. Structured outcome kinds

v1.0 carries all 13 `StructuredFeedback.feedback_kind` values. Five whose dataclasses are spec-critical:

v1.0 substrate carries one generic `OutcomeFeedback` envelope; every variant is an emergent `OutcomeKind` resolved against `KindRegistry.outcome_kinds` (`06_DOMAIN §7.6`). The five original variants (CitationObservation, CommunityUptake, ProductionTelemetry, TestResults, RegulatoryOutcome) become MetaRegistry-seeded examples for academic / software / regulated domains. Construction / clinical / studio / kitchen / any other domain adds its own outcome kinds via `ProposedOutcomeKind` (`06_DOMAIN §7.5`) without modifying substrate.

*The OutcomeFeedback dataclass is the single generic envelope for all structured outcomes, with kind, payload, arrival mode, external attestation ref, corroboration requirement, and confidence.*

**Technical detail:** See [A.32](#appendix-a32).

### 20.1 MetaRegistry-seeded outcome kinds (illustrative)

The following outcome kinds ship as MetaRegistry seeds; substrate does not depend on them. Adding a new domain (residential construction, clinical care, restaurant kitchen, dance studio) requires no substrate change — only `ProposedOutcomeKind` entries.

*Eight MetaRegistry-seeded outcome kinds are defined: citation_observation (academic), community_uptake (software distribution), production_telemetry (deployment), test_results (CI/CD), regulatory_outcome (regulated industry), building_inspection and contractor_work_log (construction), and lab_result (clinical). Each defines payload schema, arrival modes, and attestation requirements.*

**Technical detail:** See [A.33](#appendix-a33).

Each seed entry signs into the MetaRegistry with `cross_domain_promotable` per the kind's nature. The five original variants are functionally identical; the difference is they are now data, not substrate code. Unknown outcome kinds trigger Signal G (kind unknown) and a `ProposedOutcomeKind` proposal — never `SCHEMA_VIOLATION`.

## 21. Outcome arrival modes

Prior versions specified three modes; v1.0 splits LATE into two paths and adds REGULATORY for clarity.

*Five outcome arrival modes with increasing latency: synchronous (seconds, in-task), asynchronous (hours-days, between-task), community (weeks-months, nightly crawls), production_telemetry (continuous, pipeline-pushed), and regulatory (weeks-years, operator-elevated).*

**Technical detail:** See [A.34](#appendix-a34).

Late-arriving feedback triggers **retrospective credit adjustment**: the originating LineageGraph entry is re-weighted; signed and audit-logged; reversible (A-OU12).

## 22. Per-outcome-kind evolution weights

Weight table. v1.0 defaults:

| feedback_kind          | weight | stands alone? | notes |
|------------------------|--------|---------------|-------|
| bench_measurement      | 1.2    | yes           | physical reality dominates |
| production_telemetry   | 1.1    | yes if pipeline_signed | else corroboration |
| regulatory_outcome     | 1.0    | yes           | regulator signature trusted |
| test_results           | 1.0    | yes           | tests pass = verifier |
| peer_review_verdict    | 0.85   | yes           | expert persona review |
| panel_verdict          | 0.7    | yes           | LLM panel with safeguards |
| user_acceptance        | 0.6    | yes           | explicit user OK |
| user_structured        | 0.5    | yes           | rating + dimension |
| user_qualitative       | 0.5    | yes           | text polarity |
| rejection_with_reason  | 0.5    | yes           | symmetric to user_acceptance |
| citation_observation   | 0.4    | yes           | external verification |
| community_uptake       | 0.3    | NO            | requires sybil filter + corroboration by user_acceptance or audit clearance |

Principle: **the further a signal is from text-judgment, the higher the weight.** Bench data > production telemetry > tests > peer review > LLM panel > user rating > citation > community uptake.

Corroboration rules: `community_uptake` alone never promotes (Goodhart canary). All others may stand alone subject to source-trust and signature checks.

## 23. Three evolution horizons

Three distinct credit formulas per horizon are defined; v1.0 keeps them.

*Three evolution horizons with separate credit formulas: task horizon (per-task, tactic mutations), project horizon (weeks-months, completion-ceremony credits), and multi-project horizon (months-years, cross-project skill promotion and persona fitness).*

**Technical detail:** See [A.35](#appendix-a35).

Each horizon runs on its own schedule; the three compose (A-OU9). Per-task credit is local; per-project credit aggregates per-task; per-persona-fitness aggregates per-project across the persona's full career.

## 24. Cross-project transferability

Promotion rules carried into v1.0 — a candidate SKILL MUST satisfy ALL applicable conditions below.

*Transferability rules for skills, semantic memories, reflections, and tactics across projects, with required thresholds (3+ projects same domain, 2+ projects cross-domain, etc.) and five anti-leakage rules at the project boundary.*

**Technical detail:** See [A.36](#appendix-a36).

Tagging requirements: all transferable entries carry the seven-scope tags (v1.0 §08 §5); `cross_project_transferable` is the explicit flag plus optional `cross_domain_transferable`.

## 25. Multi-year project continuity

v1.0 specifies hibernation FSM and reanimation.

*The hibernation FSM extends the lifecycle (ACTIVE to PAUSED to HIBERNATING to REANIMATING to ACTIVE, or HIBERNATING to ARCHIVED). The reanimation flow includes pre-flight checks, memory rehydration, and member consent. Multi-year obligation handling covers frozen due dates, hibernation lapses, and external obligations.*

**Technical detail:** See [A.37](#appendix-a37).

Storage: archive-tier project state ≤ 1 GB typical; rehydration ≤ 30 s for HOT tier reconstruction; full reanimation ≤ 1 hour including consents.

### 25.1 LeadHandoffCeremony — successor transfer of the `lead` role

Previously, the `lead` role on a multi-session project was a `ProjectMember.role` value (per §3) with no ceremony for transfer when the current lead departed mid-project. §25 reanimation flow covered hibernation/wake, but a 3-year project whose lead retires at month 18 had no signed mechanism for who inherits authority — successor selection was implicit, decision-only-the-lead-had-authority-for accumulated silently, and audit could not answer "when did Carla become the lead?"

`LeadHandoffCeremony` is the signed ceremony that transfers the `lead` role with a 30-day overlap default. During overlap, both `outgoing_lead` and `incoming_lead` roles coexist (`§3 ProjectMember.role` value extension); CohortDynamicsState (§14.2) registers the overlap as a planned transition rather than an abrupt change.

*The LeadHandoffCeremony dataclass defines a lead-role transfer with overlap window, transferred authorities, proposed obligation reassignments, cohort consent quorum, operator authorisation, and state machine (drafted through handoff_complete or refused). Admission rules govern the draft, cosign, quorum, overlap, and completion transitions.*

**Technical detail:** See [A.38](#appendix-a38).

**Composition with `PlannedDeparture` (§14.2.1).** When a `lead`-role member files a PlannedDeparture, a LeadHandoffCeremony SHOULD be drafted at `departure_date - rebalance_window` so the overlap fits within the rebalance window. If not drafted, the PlannedDeparture's `lead_successor_candidate_id` is still recorded but cohort attention is bounded — operator should monitor.

**Composition with `§4.1` completion ceremony.** A handoff in `overlap_active` state does NOT block completion if all other completion predicates clear. Completion ceremony emits cosigns from both `outgoing_lead` and `incoming_lead` (both members are signing as leads during overlap); the multi-principal quorum (`05_ENV §12c.4a`) is unaffected (principal cosigns are operator-keyed, not persona-keyed — see `01_KERNEL §2.4.3`).

**Composition with `§14.2 CohortDynamicsState`.** LEAD_HANDOFF_ACTIVATED registers as a planned transition; band-degradation models discount the outgoing lead's edge weights gradually over the overlap window, mirroring PlannedDeparture's anticipatory rebalance behaviour.

**Honest limits.**

1. **No candidate?** If the cohort has no admissible successor (every other member is junior, departing, or external-only), the LeadHandoffCeremony cannot draft. The project enters a forced choice: pause until recruitment yields a candidate (`§14.1` cohort assembly); operator becomes interim lead (rare; carries operator-direct-decision audit weight); **or, where recruitment is exhausted and a `persona_genesis` `ReplicationBound` is active, propose Persona Genesis** to author a new niche-distinct candidate (`16_POPULATION_DYNAMICS §4`). Unmet `CohortConstraint.required_kinds` for ≥ a sustain window feed the population-pressure signal (`16_POPULATION_DYNAMICS §4A`).
2. **Refused-by-cohort.** When cohort quorum refuses the incoming candidate, the ceremony goes to `refused_by_cohort`; outgoing lead may draft a different candidate or escalate to operator override (`cohort_quorum_policy = "lead_only"`). Operator override leaves a heavier audit footprint and should be rare.
3. **Emergency handoff.** Setting `overlap_window = 0` requires operator-signed `emergency_handoff_signed` event and produces immediate role transition without the rebalance smoothing. Use case: outgoing lead suddenly unavailable (medical emergency, etc.). Cohort dynamics will spike; that's the honest cost of emergency.
4. **Lead-specific knowledge transfer is operator-policy.** The substrate transfers the *role* and *authorities*; the lead's tacit knowledge (mental model of project history, relationships with external agents, decision context) does NOT auto-transfer. Operators should pair the ceremony with `PersonaConsultation` (`02_PERSONA §7.5.2`) if outgoing lead is RETIRED, OR with explicit knowledge-transfer sessions before overlap begins.

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9g — A-LH*` (lead handoff).

**Fork interaction.** LeadHandoffCeremony is the substrate-shape mechanism for lead transitions to a *distinct* successor persona; mid-project fork into children is a different topology (one persona → N children). When a `lead`-role persona forks, `MidProjectForkComposition.lead_role_inheritance` (`02_PERSONA §7.4.7`) governs: `require_lead_handoff_ceremony` (fork blocks until a downstream LeadHandoffCeremony reaches overlap_active with named incoming-child as incoming_lead — the most ceremonious path, recommended for safety-critical projects), `one_child_inherits` (compressed handoff inside the fork ceremony; cohort quorum signature required; substrate refuses on cohort objection), `neither_inherits` (lead vacant; project enters `lead_vacant` state), or `refused_if_no_successor` (substrate refuses the fork). **Substrate refusal**: forks initiated while parent persona holds an active LeadHandoffCeremony in `overlap_active` state are **refused** with `fork_refused_active_lead_handoff_overlap` — adding fork-into-children to an already-active lead handoff would create three-or-more lead claimants.

## 26. Cost and performance

*Performance targets (creation ≤1s, member admission ≤200ms, lineage append ≤10ms, completion ceremony ≤10s) and storage estimates (1-50 MB state, 10K-100K lineage events, ~5x session memory per active month).*

**Technical detail:** See [A.39](#appendix-a39).

## 26a. External participants and physical assets

Prior versions modelled the work surface around personas, users, operators, and digital artifacts. Real-world projects (residential construction, clinical care, restaurant operation, theatre production, manufacturing) also include **third-party humans** who deliver into the project but are not personas, and **physical things** that the project produces alongside its digital artifact bundles. v1.0 adds four substrate primitives so these scenarios work without forcing them through user-as-bridge or `binary` artifacts.

### 26a.1 ExternalAgent

*The ExternalAgent and ExternalCommitment dataclasses define a non-persona participant (contractor, inspector, supplier, etc.) with role, contact, bridge assets, commitments, delivered artifacts, attestations, and consent scope.*

**Technical detail:** See [A.40](#appendix-a40).

`ExternalAgent` is **not a persona**: it has no charter, no modes, no SOUL.md, no kernel-mediated memory. It is a structured record of a human (or org) outside the kernel boundary. The persona communicates with the agent through a `BridgeAsset` (`06_DOMAIN §5.5`) — typically `account_link` or `credential_holder` capability_kind — and reads the agent's outputs as `OutcomeFeedback` entries (§20). Charter / safety floor still apply: a persona cannot draft a HumanAssistRequest that would coerce or impersonate an external agent.

### 26a.2 PhysicalAsset — the thing being produced

*The PhysicalAsset dataclass records a real-world object (house, device, patient care episode, production run) with asset kind, location, related digital bundles, state machine, evidence, pending commitments, completion mode (terminal_state_required, publishable_state_attained, continuous_iteration), and ownership kind.*

**Technical detail:** See [A.41](#appendix-a41).

`PhysicalAsset` lives alongside `ArtifactBundle`, not inside it. The bundle holds the digital design; the asset holds the physical reality. Completion ceremony (§4.1) is extended: a project that produces a `PhysicalAsset` cannot reach `completed` until either the asset reaches a terminal state in its `state_kind` FSM, OR the project explicitly declares the asset out of scope (signed `physical_asset_out_of_scope` event). This closes the prior gap where "design done" silently meant "project done."

### 26a.2.1 AsBuiltReconciliation — design-vs-reality pairing

A long physical build accumulates **drift** between design and reality: the wall is 2 inches off plan, the foundation footing is at 27" not 24", the framing varies from spec. v1.0 already has the primitives (PhysicalAsset, ArtifactBundle with versions, change_order ItemKind, punch_list_item ItemKind, evidence_refs on PhysicalAsset, ExternalAttestation) — what was missing is a **first-class reconciliation operation** that pairs design version with as-built reality and routes deltas to terminal resolutions.

*The AsBuiltReconciliation and Deviation dataclasses pair a design bundle version with physical reality, record structured drift (location, dimension, design vs. observed values, tolerance status), and route to resolution (within_tolerance, design_update_required, reality_remediation_required).*

**Technical detail:** See [A.42](#appendix-a42).

**Completion-ceremony extension.** Per `§4.1` step 1 (Physical-asset closure), a `PhysicalAsset` with non-trivial `related_bundle_ids` (i.e., at least one design bundle prescribes the asset) cannot reach terminal state without **at least one `AsBuiltReconciliation` per related bundle** whose `resolution_kind` is in the terminal substrate-shape set `{within_tolerance, design_update_required, reality_remediation_required}` AND whose downstream `resolution_refs` (per-domain emergent ItemKinds — change orders, punch-list items, bug tickets, rework tasks, corrective actions, etc.) are themselves discharged in their respective FSMs. Absence emits `as_built_reconciliation_missing` on attempted closure.

**ProjectLineage:** Reconciliation events live in project scope (`as_built_reconciliation_drafted`, `as_built_reconciliation_signed`, `as_built_reconciliation_superseded`). Cross-references to ExternalAttestation, ArtifactBundle, change_order ItemKind, punch_list_item ItemKind. The reconciliation does not duplicate evidence; it points to it.

### 26a.2.2 AssetGroupEnvelope and BatchStateAdvancement

When a project manages many homogeneous `PhysicalAsset` instances that share `asset_kind` and lifecycle topology, per-asset state management creates cardinality pressure: N individual `physical_asset_state_advanced` events where one coordinated envelope would suffice.

*The AssetGroupEnvelope, AssetGroupDerivedState, BatchStateAdvancement, and AssetAdvancementOutcome dataclasses manage groups of homogeneous physical assets with predicate-driven membership, derived state (count by state, percent operational), batch state advancement with conflict resolution, and per-asset outcomes.*

**Technical detail:** See [A.43](#appendix-a43).

**Constraints.**

- **No nesting.** Groups-of-groups are refused; flat topology keeps lineage simple. A `PhysicalAsset` MAY belong to multiple groups simultaneously (e.g., "floor_3_sensors" and "firmware_v2.1_devices").
- **Membership is predicate-driven.** `member_asset_ids` is materialised from `group_membership_predicate` on creation + on every `PhysicalAsset` admission, departure, or state change within the project. Operators MAY override with explicit asset lists (set `group_membership_predicate = "explicit"` and manage `member_asset_ids` directly).
- **BatchStateAdvancement is a single fan-out.** The kernel signs one envelope; each member asset receives an individual `physical_asset_state_advanced` event in lineage. The batch envelope is the coordination record; individual events are the authoritative state transitions. If `conflict_policy = "skip_changed"`, assets whose state changed between batch drafting and execution are skipped with `reason = "state_changed_since_batch"`.
- **Derived state is informational.** `AssetGroupDerivedState` is kernel-computed and kernel-signed but is NOT an admission gate. Operators wanting "refuse firmware update if fleet health < 90%" express this as a `StagedRolloutEnvelope` success criterion (see `§26a.9`), not as a derived-state invariant.

**Tests:** A-AG1 (group creation + membership materialisation), A-AG2 (batch advancement fan-out), A-AG3 (conflict_policy skip_changed), A-AG4 (derived state computation), A-AG5 (no nesting refusal), A-AG6 (multi-group membership), A-AG7 (group membership recomputation on asset state change). See [`11_ACCEPTANCE_TESTS.md §9k`](11_ACCEPTANCE_TESTS.md).

**ProjectLineage:** `asset_group_created`, `asset_group_membership_recomputed`, `batch_state_advancement_drafted`, `batch_state_advancement_executed`, `batch_state_advancement_partial`, `batch_state_advancement_rolled_back`.

### 26a.3 ExternalAttestation

*The ExternalAttestation dataclass records a signed statement from a credentialed external party (engineer stamp, inspector signoff, notary seal), with attestor kind, credential, scope, statement, targets, expiration, evidence, signature (cryptographic or scanned with co-sign), and credential verification status.*

**Technical detail:** See [A.44](#appendix-a44).

`ExternalAttestation` is the substrate primitive for "engineer stamp," "city signoff," "notary seal," "lab director sign-off." It is distinct from `PeerReview` (persona-to-persona within the kernel) and from `OutcomeFeedback` (any structured outcome). The cascade verifier kind `external_human_attestation` (a typical `ProposedVerifierKind`) consumes an `ExternalAttestation` as its evidence.

**Credential resolution.** At attestation-acceptance time, the kernel attempts to resolve `attestor_credential_id` against the domain's `credential_directories` (`06_DOMAIN §5.6 CredentialDirectoryRef`). Successful resolution emits a signed `CREDENTIAL_VERIFIED` lineage event recording the directory's content hash at lookup time. Failure (no directory; directory unreachable; credential revoked or expired) sets `credential_unverified=True` and emits `CREDENTIAL_UNVERIFIED`. The attestation remains *admissible* in either case, but downstream J4 acceptance treats unverified attestations as PANEL-grade evidence only — they cannot satisfy the credentialed-attestor leg of the physical-state advancement rule (`01_KERNEL §2.5`).

**Principal-collapse interaction.** Under `principal_topology = operator_is_user` (`01_KERNEL §2.4`), `operator_co_signed_by` is rejected as the non-cryptographic-attestor co-sign — it would let the principal sign their own engineer's attestation, defeating the chain of trust. Only `independent_co_signed_by` from an `ExternalAgent` whose credential is disjoint from the principal satisfies the co-sign requirement. Cryptographic `attestor_signature` (Ed25519 / equivalent) does not need a co-sign and is unaffected by the collapse.

### 26a.4 ExternalBudget — money / materials / time-of-labour

*The ExternalBudget and BudgetTranche dataclasses track planned, committed, and spent amounts in any unit (USD, labour_hours, kWh, etc.) with cost breakdowns by contribution kind, alerts, tranched/phased release conditions, and sequential release enforcement.*

**Technical detail:** See [A.45](#appendix-a45).

`ExternalBudget` is **honest non-execution**: v1.0 still does not transact money (`00_VISION` out-of-scope). It tracks **commitments and reconciliations** so the persona can warn the user before a cost overrun, flag a stalled contractor invoice, or refuse to advance a `design_hypothesis` whose verification depends on a budget that has been exhausted. Real transactions remain operator-wrapped.

### 26a.4.2 ResourceStockEnvelope — closed-system stock accounting (C3)

`ExternalBudget` tracks **supply that arrives from outside** the kernel boundary (money, materials, contractor time). Some projects operate in **closed systems** where resources cannot be replenished from outside the boundary — off-grid installations, life-support systems, sealed-loop manufacturing, biological cultures, ration accounting. In these cases the substrate primitive needs to be flipped: instead of tracking arrivals against a planned envelope, track **stock**, **regeneration rates**, and **conservation invariants**.

`ResourceStockEnvelope` is a sibling primitive to `ExternalBudget`. INV-7 budget admission consults whichever is appropriate for the resource_kind (supply or stock).

*The ResourceStockEnvelope and ConservationInvariantRef dataclasses track closed-system stock (current level, capacity, floor, critical threshold), regeneration model (passive, active, decay, stochastic, none), conservation invariants (mass/energy/charge balance), and the INV-7 admission rule extension (refuse below floor, escalate below critical, evaluate conservation invariants).*

**Technical detail:** See [A.46](#appendix-a46).

**Coexistence with `ExternalBudget`.** A project can have both. A solar-powered remote sensor station tracks `ResourceStockEnvelope(battery_state_of_charge)` for closed-loop energy and `ExternalBudget(maintenance_visits)` for external technician supply. The kernel never confuses them — each `resource_kind` is bound to exactly one envelope kind.

**Drift detection.** `drift_from_predicted_pct` compares the model-predicted stock against measured stock at each `last_measured_at` update. Drift > operator-tunable threshold (default 15%) emits `resource_stock_model_drift_detected` and forces the persona to either (a) re-fit the regeneration model or (b) tighten `stock_floor` to absorb prediction uncertainty.

**Persona-evolvable surface.** `resource_kind`, `unit`, `regeneration_evidence_kind`, `ConservationInvariantRef.arithmetic_form` are all KindRegistry-resolved or persona-supplied data. Substrate carries the topology (stock vs supply, floor vs critical, conservation as arithmetic relationship); persona supplies what stock, what units, what conservation law applies.

**Composition with `operator_deferred` topology (§01_KERNEL §2.4.2).** When stock drops below `stock_critical` under `operator_deferred`, escalation goes to the PolicyEnvelope path: a `DeferredAdmission` slot is opened for the operator to acknowledge or revoke the consuming action. Quarantine of consumed stock is impossible (the resource is already consumed); the substrate instead refuses *future* consumption until counter-sign or revoke arrives.

**Acceptance tests.** A-RS1 (refuse-below-floor admission), A-RS2 (critical escalation), A-RS3 (conservation invariant evaluated arithmetic-style, refuses on violation), A-RS4 (drift detection forces model re-fit), A-RS5 (coexistence with ExternalBudget on same project), A-RS6 (under operator_deferred, critical escalation opens DeferredAdmission).

### 26a.4.1 PaymentBridge — structured human-bridged payment

`ExternalBudget` plans + tracks; it does not pay. `PaymentBridge` is the structured handoff between the persona-tracked budget and a human-executed payment. It is **Class E** — strictly more restrictive than Class D (`06_DOMAIN §5`). The kernel signs the *proposal* (proposed amount + payee + reason) and the *receipt* (after-the-fact reconciliation). It NEVER touches funds.

*The PaymentBridge and PaymentProposal dataclasses define a human-bridged payment flow with authorization modes (per-invoice click, pre-authorized envelope, operator co-signed), caps, receipt ingestion, five invariants (kernel never touches funds, safety floor applies, MHBB suppression rules, reconciliation required, never a bridge asset), lifecycle, and a worked example.*

**Technical detail:** See [A.47](#appendix-a47).

### 26a.6 ProjectPhaseState — phase-aware progress evaluation

The PROJECT_PROGRESS_ACCEPT evaluator (`03_TASKS §3.1 PROJECT_PROGRESS_ACCEPT`) fires `PROJECT_STALLED` when EMA progress < 0.1 for ≥ 4 sessions. This is correct for *stuck* projects but spuriously fires during *legitimate wait* phases — fab queues, peer review, regulatory approval, contractor scheduling — where the project is healthy but progress requires external action that takes weeks. `ProjectPhaseState` is the substrate annotation that the evaluator consults.

*The ProjectPhaseState dataclass defines phase-aware progress evaluation: each phase has a kind, expected duration, blocking commitments, stall-evaluator suppression flag, overdue auto-lift threshold, and user sign-off. The evaluator integration function shows phase-aware stall suppression logic.*

**Technical detail:** See [A.48](#appendix-a48).

**Phase transition lineage:**

Every phase transition emits a signed `PROJECT_PHASE_TRANSITION` event into ProjectLineage with: from_phase_id, to_phase_id, transitioned_by, evidence_refs (which commitments/attestations enabled the transition). Replay reconstructs the full phase history including overdue/suppression toggles.

**Honest limit:** the suppression flag is set by the PhaseKind registry entry, which is itself emergent + operator-reviewable. Operator may flip suppression off for any phase if it's being abused to hide a stuck project. The signed `phase_suppression_override` event surfaces this in audit.

### 26a.7 InstrumentAsset + CalibrationChain

`PhysicalAsset` (`§26a.2`) is generic — appropriate for houses, cakes, patient-care episodes, manufactured runs. Measurement-heavy projects (any domain where a number with uncertainty is load-bearing) need additional structure: which *instrument* produced the number, when it was last *calibrated*, against which *reference standard chain*. `InstrumentAsset` specialises `PhysicalAsset`; `CalibrationChain` is its provenance trail.

*The InstrumentAsset, CalibrationChain, ReferenceStandardLink, and DriftLogEntry dataclasses specialize PhysicalAsset for measurement instruments with calibration chains, reference standards, uncertainty envelopes, drift logging, and operational state FSM. Composition rules with MeasurementFact enforce calibration currency at measurement time.*

**Technical detail:** See [A.49](#appendix-a49).

**Lifecycle events:** `INSTRUMENT_CALIBRATED`, `INSTRUMENT_DRIFT_LOGGED`, `INSTRUMENT_QUARANTINED`, `INSTRUMENT_DECOMMISSIONED` — all signed into ProjectLineage (or EnvironmentLineage when the instrument is shared across projects via `ownership_kind = shared_lab_facility`).

**Honest limit:** the calibration chain only confers trust up to the lowest-trust link. A traceable chain to NIST is high-trust; a chain whose root is `traceable_unverified=True` is PANEL-grade regardless of intermediate links. The substrate provides the data structure; the operator + CredentialDirectoryRef catalog provides the trust anchors.

### 26a.5 Putting it together — the home-construction project

*A worked example shows a home-construction project with members, external agents (contractor, inspector, engineer, supplier), artifact bundles (floor plans, structural calcs, permits), a physical asset (the house), external attestations, budget, domain items, and outcome feedback. Completion requires both accepted artifact bundles and terminal physical-asset state.*

**Technical detail:** See [A.50](#appendix-a50).

### 26a.9 StagedRolloutEnvelope

When an `ArtifactBundle` must be deployed across multiple `PhysicalAsset` instances in staged waves with soak periods and rollback conditions, per-asset manual sequencing pushes safety-critical coordination out of the kernel's signing model into persona ad-hoc planning.

*The StagedRolloutEnvelope and RolloutWave dataclasses define staged deployment across asset groups with waves (canary, early, GA), per-wave success criteria, minimum soak periods, rollback triggers, bridge-degradation pause, and lifecycle FSM (planned through completed/rolled_back/paused).*

**Technical detail:** See [A.51](#appendix-a51).

**Constraints.**

- **Wave ordering is strict.** Wave N+1 cannot begin until wave N reaches `completed`. Parallel waves refused.
- **Soak period is kernel-enforced.** The kernel refuses wave assessment before `min_soak_period_hours` elapses after the wave's `BatchStateAdvancement` completes. The kernel does NOT assess health — the persona (or `ScheduledTrigger`-driven anomaly detection) must raise `Alert`s during soak; the kernel checks whether rollback triggers fired.
- **Rollback reverts per-wave.** On rollback, the kernel drafts a reverse `BatchStateAdvancement` for the rolled-back wave's assets, advancing them back to their prior state. Rollback of wave N does NOT automatically roll back waves 0..N-1 (earlier waves already soaked and passed). Operator MAY sign a full-rollout rollback that reverts all waves.
- **Bridge degradation pauses.** If `rollback_on_bridge_degradation = True` and `BridgeAsset.state → DEGRADED` during a wave, the rollout pauses with `rollout_state = paused`. Operator must resume or roll back. This protects against deploying firmware through a degraded communication channel.
- **Composes with AssetGroupEnvelope.** `BatchStateAdvancement` (§26a.2.2) handles the per-wave fan-out; `StagedRolloutEnvelope` handles the wave sequencing and soak enforcement. Neither knows about firmware or IoT — both are topology primitives.
- **Operator co-sign for safety-critical.** When the project's domain has `safety_critical = True`, `requires_operator_cosign = True` is the default. Operator must co-sign the envelope before `in_progress`; operator must also co-sign each wave transition for domains with `physical_harm_class ≥ bodily_injury`.

**Tests:** A-SR1 (envelope creation + wave ordering), A-SR2 (soak period enforcement), A-SR3 (rollback trigger fires mid-soak), A-SR4 (bridge degradation pauses rollout), A-SR5 (full rollout completion), A-SR6 (operator co-sign for safety-critical), A-SR7 (reverse BatchStateAdvancement on rollback), A-SR8 (composed with AssetGroupEnvelope). See [`11_ACCEPTANCE_TESTS.md §9k`](11_ACCEPTANCE_TESTS.md).

**ProjectLineage:** `staged_rollout_drafted`, `staged_rollout_started`, `staged_rollout_wave_deploying`, `staged_rollout_wave_soaking`, `staged_rollout_wave_completed`, `staged_rollout_wave_rolled_back`, `staged_rollout_completed`, `staged_rollout_rolled_back`, `staged_rollout_paused`, `staged_rollout_resumed`.

### 26a.10 BridgeReductionPlan — progressive automation of human dependencies

**What this is, in plain language.** Every real-world project starts with tasks that need a human: an inspector signs off on construction, a technician flashes firmware, a calibration engineer certifies an instrument. PersonaOS personas are designed to progressively automate these human touchpoints — they design software drivers, sensor rigs, and automated pipelines so that a one-time human setup replaces ongoing human labor. The **BridgeReductionPlan** is the persona's explicit to-do list for this automation work. It says: "Here are all the places we currently depend on a human. Here is my plan to replace each one with an automated bridge. Here is how far along each replacement is." The system checks in monthly to make sure the plan isn't gathering dust, and it automatically flags cases where the persona keeps asking a human to do something a bridge could handle. When something genuinely cannot be automated (a surgeon's judgment, a notary's legal authority), the plan says so honestly and stops trying.

**Why it matters.** Without this plan, automation happens reactively — only when the system notices the persona repeatedly asking humans for help. With the plan, automation happens proactively — the persona surveys all human dependencies at the start of a project and works through them systematically. Each successful automation becomes a reusable skill the persona carries to future projects, so the next project starts with fewer human dependencies than the last one.

Every physical-world project accumulates `HumanAssistRequest` records at Tier 4 (irreducible human professional work) that persona-authored Tier 3 bridges could partially or fully automate over time. Without an explicit planning artifact, this reduction happens ad-hoc (persona notices a Tier 5 anti-pattern, reacts) rather than proactively (persona inventories all dependencies at project start, plans a reduction trajectory).

*The BridgeReductionPlan is a project-level artifact that inventories all human dependencies by MHBB tier, tracks proposed bridge designs that would reduce each dependency's tier, and measures progress as bridges are authored, installed, and validated. It composes with `HumanAssistRequest` (§5.5 `06_DOMAIN`), `BridgeAsset` lifecycle FSM, `BridgeDesignArtifact` (§5.5.4 `06_DOMAIN`), `MilestoneDrivenAutonomy` (`02_PERSONA §11.2`), `ProjectPhaseState` (§26a.6), and `OpenProblem` (§6). Entries that cannot be automated are honestly marked `irreducible` and tracked as explicit `OpenProblem` instances.*

**Technical detail:** See [A.53](#appendix-a53).

**How it works (step by step).**

1. **Inventory.** At project start, the persona surveys every place a human is needed and lists each one in the plan — what the human does, how often, and how much effort it takes.
2. **Design.** For each dependency, the persona designs an automated replacement: a software driver, a sensor rig, a data pipeline, a camera-based inspection system. The design is a deliverable the project produces.
3. **Install.** A human performs a one-time setup (installs the software, mounts the sensor, connects the cable). After that, the persona uses the automation independently.
4. **Validate.** The persona confirms the automation works reliably over time. Measurements are checked against calibration standards. If the automation degrades, the persona redesigns a stronger version.
5. **Reuse.** Validated automations become permanent skills the persona carries to future projects. The next project starts further ahead.
6. **Honest limits.** Some human work genuinely cannot be automated (a licensed inspector's professional certification, a surgeon's hands). The plan marks these honestly and stops trying — but revisits them if new technology changes the picture.

**Constraints (technical).**

- **Plan is project-scoped.** One `BridgeReductionPlan` per `project_workspace`-typed environment. Cross-project skill transfer happens through the `skill_library` (Voyager) mechanism; the plan tracks which bridge designs have been promoted to reusable skills.
- **MHBB_RECURRENCE_DETECTED auto-populates.** When the kernel emits `MHBB_RECURRENCE_DETECTED` (>3 identical HumanAssistRequests/quarter without a bridge — `02_PERSONA §11.1` Tier 5 anti-pattern), a new `BridgeReductionEntry` is auto-created in the plan with `status = inventoried` and `trigger = mhbb_recurrence`. The persona MUST address it (design a bridge or mark irreducible with justification) within the plan's `review_cadence`.
- **Review cadence is kernel-enforced.** The kernel emits `BRIDGE_REDUCTION_PLAN_REVIEW_DUE` at the declared cadence (default 30 days). If the persona does not review (advance, update, or explicitly defer entries) within `review_grace_period` (default 7 days), the plan transitions to `status = stale` and the project's `ProjectPhaseState` evaluator factors it into stall assessment. Stale plans are not blocking — they are signals.
- **Irreducible entries are honest, not permanent.** An entry marked `irreducible` means "cannot automate with current bridge technology / domain knowledge." It persists as a named `OpenProblem` in the project. If new bridge capabilities emerge (new MCP tools, new sensor technology, new BridgeInstallerKind topologies), the persona SHOULD re-evaluate irreducible entries.
- **Composes with MilestoneDrivenAutonomy.** A plan milestone (e.g., "reduce Tier 4 dependencies from 8 to 3 by month 6") can anchor a `MilestoneDrivenAutonomy` envelope (`02_PERSONA §11.2`) that permits proactive bridge authoring actions within scope — `draft_bridge_design`, `validate_bridge_latency`, `propose_attestation_equivalence` — without per-action human approval.
- **Composes with BridgeInstallerKind.** Plan entries MAY propose `chained_bridge` topologies (`06_DOMAIN §5.5.6`) where an existing active bridge installs a new bridge — reducing human install effort to zero for the chained bridge. The plan tracks these chains explicitly.
- **Composes with AttestationEquivalencePolicy.** When a plan entry proposes replacing human attestation (ExternalAttestation) with sensor-bridge evidence, the entry MUST reference an `AttestationEquivalencePolicy` (`06_DOMAIN §5.7`) that the operator has approved for that verification kind. Without an approved equivalence policy, the entry cannot advance past `design_ready`.
- **Skill library feedback loop.** When a bridge design reaches `bridge_validated` status, the persona SHOULD promote the design to a `skill_library` entry (Voyager-class). The plan tracks `skill_library_entry_id` for each completed entry. Cross-project reuse of validated bridge designs reduces future plans' scope — the persona starts with fewer Tier 4 dependencies because prior projects already solved them.

**Tests:** A-BRP1 (plan creation with initial inventory), A-BRP2 (MHBB_RECURRENCE_DETECTED auto-populates entry), A-BRP3 (review cadence enforcement + stale transition), A-BRP4 (entry advancement through full lifecycle: inventoried → designing → design_ready → awaiting_install → bridge_active → bridge_validated), A-BRP5 (irreducible entry creates OpenProblem), A-BRP6 (chained_bridge topology in plan entry), A-BRP7 (AttestationEquivalencePolicy composition — entry blocked without approved policy), A-BRP8 (skill_library promotion on bridge_validated), A-BRP9 (cross-project skill reuse reduces initial plan scope). See [`11_ACCEPTANCE_TESTS.md §9l`](11_ACCEPTANCE_TESTS.md).

**ProjectLineage:** `bridge_reduction_plan_drafted`, `bridge_reduction_entry_added`, `bridge_reduction_entry_advanced`, `bridge_reduction_entry_irreducible`, `bridge_reduction_plan_reviewed`, `bridge_reduction_plan_stale`, `bridge_reduction_plan_completed`.

## 27. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations).

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-PROJECT-1 | Charter-compatibility evaluation at persona admission is heuristic. Edge cases may pass / refuse incorrectly. | Medium | Medium | Operator override surface; A-PJ12 acceptance test; classifier rotation. | v1.0 (baseline); v1.1 (reputation closed-loop). |
| R-PROJECT-2 | Long-arc multi-month / multi-year projects accumulate state (bundles, lineage, ProvenFacts). Storage pressure rises. | Medium | High | Bundle retention policy; `LineageSnapshot`; hibernation FSM (`§24`) defers active state. | v1.0 (retention); v1.1 (snapshot tuning). |
| R-PROJECT-3 | Cross-env project membership coordination overhead. Members in multi-env projects must navigate notifications across envs. | Low | Medium | ObservationSurface filters; project digest stream; AttentionBudget caps. | v1.0 (baseline); v1.1 (project-wide digest). |
| R-PROJECT-4 | Disagreement resolution stalls. Persistent unresolved disagreements block dependent work. | High | Medium | Stall-detector emits `DISAGREEMENT_STALLED`; operator escalation; A-PJ16 verbatim preservation; mediation pathway. | v1.0 (stall detector); v1.1 (mediation flow). |
| R-PROJECT-5 | PeerReview reviewer-time bottleneck. Multi-round reviews require human time at scale. | Medium | High | Reviewer queue management is operator concern; PanelVerdict can shortcut some reviews; reviewer-credit incentivises participation. | v1.0 (baseline). |
| R-PROJECT-6 | External-participant attestations (`§26a.3`) bridge analog and cryptographic chains. Forged credentials are possible without a credential-directory resolution path. | High | Low | `CredentialDirectoryRef` (`06_DOMAIN §5.5`) per-domain resolution; A-EX16 acceptance test; independent co-sign requirement. | v1.0 (CredentialDirectoryRef); v1.1 (cross-domain directory federation). |
| R-PROJECT-7 | ApprovalWorkflow sign-off chains depend on real-world participants. External delay is uncapped. | Medium | High | Per-step deadlines + escalation; STALLED workflow state surfaces to operator; budget-tranche timeouts (`§26a.4`). | v1.0 (baseline). |

## 27a. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-PROJECT-1 | Multi-year project hibernation: when REANIMATING fails the pre-flight check (charter mismatch, member unavailability), what's the right operator UX? Auto-archive, or manual triage queue? | Operator UX | v1.1 hibernation policy. |
| OQ-PROJECT-2 | Mediation flow for stalled disagreements (R-PROJECT-4): persona-mediator from a different domain, operator-mediator, or arbitration panel? | Project WG | v1.1 mediation design. |
| OQ-PROJECT-3 | PeerReview reviewer-credit: should reviewer-credit affect persona evolution signals, or stay isolated as a project-only metric? | Evolution WG | v1.1 credit composition. |
| OQ-PROJECT-4 | Cross-org IP in shared projects: v1.0 ships operator policy at admission; should the substrate enforce per-artifact licence inheritance from CommunityUptake / production-telemetry outcomes? | Legal / IP | v1.2 licence model. |
| OQ-PROJECT-5 | ExternalAttestation credential directory federation (`§26a.3` + `06_DOMAIN §5.5`): how do multiple operators (or kernels) share trusted credential roots? | Federation WG | v1.1 directory federation. |
| OQ-PROJECT-6 | Project-wide notification digest (R-ENV-5): is it env-scoped, project-scoped, or persona-scoped per project? | Persona UX | v1.1 digest design. |

## 28. Acceptance tests

*Twenty-seven acceptance tests (A-PJ1 through A-PJ27) cover the full project lifecycle: creation, membership, memory scoping, lineage, ceremonies, forking, milestones, conjectures, obligations, disagreements, peer review, notation, citations, multi-env hosting, cross-domain transfer, progress evaluation, outcome kinds, arrival modes, three horizons, hibernation, and tool-requirement exceptions.*

**Technical detail:** See [A.52](#appendix-a52).

## 29. Where to read next

- Environment layer where projects host: [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md)
- Domain context — authored or emergent: [`06_DOMAIN.md`](06_DOMAIN.md)
- Artifacts that projects produce: [`07_ARTIFACTS.md`](07_ARTIFACTS.md)

## Technical Appendix

The appendices below contain the full technical schemas, data structures, diagrams, and specification tables referenced throughout this document. Each appendix is referenced from the section where it applies.

### A.1 Prior-version to v1.0 mapping table

<a id="appendix-a1"></a>

```text
Prior-version model                  v1.0 model
───────────────────                  ──────────
Project (entity)                     EnvironmentInstance.type = project_workspace
ProjectLineage (J8 scope)            EnvironmentLineage filtered by kind=project_*
ProjectMember                        EnvironmentMembership with project-role
ProjectProvenFacts (CRDT)            EnvironmentProvenFacts on a project_workspace env
ProjectInvitation                    ENV_INVITATION on a project_workspace env
Project hosts in env (Mode B)        Task in a project_workspace env (Mode A;
                                      Mode B distinction retires)
```

### A.2 Project schema (project/2)

<a id="appendix-a2"></a>

```python
@dataclass
class Project:
    # IDENTITY
    schema: str = "project/2"
    project_id: str                       # ULID
    name: str
    description: str                      # ≤ 500 chars
    created_at: datetime
    created_by: str                       # operator or kernel ref
    
    # CHARTER (project-specific; distinct from persona/env charters)
    charter: list[str]
    charter_version: int
    charter_signed_by: bytes
    
    # DOMAIN (with stage)
    domain_context_ref: str | None        # → DomainContext (authored or emergent)
    
    # MEMBERSHIP
    members: dict[persona_id, ProjectMember]
    lead_persona_id: str | None
    operator_admins: list[str]
    
    # STATE
    status: Literal["proposed", "active", "paused",
                    "digital_complete_physical_in_progress",
                    "completed", "abandoned", "archived"]
    open_problems: list[OpenProblem]
    artifacts: list[ArtifactBundleRef]
    domain_items: dict[str, list[ProjectItemRef]]
                                          # v1.0 domain-agnostic: keyed by
                                          # ItemKind name (resolved against
                                          # KindRegistry.item_kinds, 06_DOMAIN
                                          # §7.6). Math projects populate
                                          # "conjecture" / "proof_attempt" /
                                          # "proof_gap"; residential_
                                          # construction populates
                                          # "design_hypothesis" /
                                          # "buildability_concern" /
                                          # "site_constraint"; clinical
                                          # populates "patient_episode" /
                                          # "differential_diagnosis". Substrate
                                          # has no hardcoded item-kind field.
    obligations: list[ObligationRef]
    disagreements: list[DisagreementRef]
    notation: dict[str, NotationConvention]
    citations: CitationGraphRef
    
    # MEMORY (multi-scope)
    project_memory_refs: list[str]
    project_proven_facts: ProvenFactsRef  # CRDT G-set
    
    # LINEAGE (J8)
    project_lineage_id: str
    parent_project_id: str | None         # if forked
    child_project_ids: list[str]
    
    # EXTERNAL
    external_links: list[ExternalLink]
    
    # MILESTONES
    milestones: list[ProjectMilestone]
    
    # ENVIRONMENTS (project may host in multiple envs)
    environments: list[str]               # env_ids hosting this project
    primary_environment_id: str | None
    
    # EXTERNAL PARTICIPANTS + PHYSICAL ASSETS (v1.0 — §26a)
    external_agents: list[str]            # ExternalAgent ids
    physical_assets: list[str]            # PhysicalAsset ids
    external_attestations: list[str]      # ExternalAttestation ids
    external_budgets: list[str]           # ExternalBudget ids
    
    # SEQUENTIAL SIGNOFF + ALERTS (v1.0 — §11a, env §11a)
    approval_workflows: list[str]         # ApprovalWorkflow ids
    alerts: list[str]                     # Alert ids scoped to this project
    
    # META
    last_active_at: datetime
    completed_at: datetime | None
    completion_summary_ref: str | None
    signed_by: bytes
```

### A.3 ProjectMember schema (project-member/2)

<a id="appendix-a3"></a>

```python
@dataclass
class ProjectMember:
    schema: str = "project-member/2"
    persona_id: str
    project_id: str
    role: str                             # "lead" | "contributor" |
                                          # "reviewer" | "observer" |
                                          # "outgoing_lead" (v1.0.8 —
                                          #  during LeadHandoffCeremony
                                          #  overlap, §25.1) |
                                          # "incoming_lead" (v1.0.8 —
                                          #  during overlap, §25.1) |
                                          # "departing" (— set
                                          #  during PlannedDeparture
                                          #  rebalance window, §14.2.1) |
                                          # domain-meaningful role
    role_assigned_at: datetime
    role_history: list[RoleChange]
    
    primary_env_membership_id: str | None # which env this member
                                          # is primarily based in
    joined_at: datetime
    departed_at: datetime | None
    
    consents: list[Consent]
    obligations_active: int
    contribution_credit: float            # accrued per §5
    
    admitted_by: str
    admission_event_ref: str

    # pin against persona-FSM retirement for long-arc projects
    pinned_until: datetime | None = None  # see 02_PERSONA §7.5 retirement
                                          # predicate; non-null blocks
                                          # transition to RETIRED while
                                          # the membership is active.
                                          # Set at admission for "lead"
                                          # on multi-month physical work;
                                          # cleared by operator (or, under
                                          # principal collapse, user) to
                                          # permit retirement.
    pinned_reason: str | None = None      # short string for audit:
                                          # "lead_on_home_build_2026"

    # principal attribution for multi-principal projects.
    # Set at admission when the hosting project's PrincipalAttribution
    # (01_KERNEL §2.4.3) has multi_principal_attribution_enabled = True;
    # MUST resolve to one PrincipalRef.operator_id in
    # PrincipalAttribution.principals.  Null when single-principal
    # (behaviour unchanged).  Lineage records the binding so
    # audit can answer "which principal authorised this member."
    principal_attribution_id: str | None = None

    signed_by_persona_kernel: bytes
    signed_by_project_kernel: bytes
```

### A.4 Project lifecycle state machine

<a id="appendix-a4"></a>

```text
                   ┌──────────┐
                   │ PROPOSED │   project created; no work yet
                   └────┬─────┘
                        │ first task or first member accepts
                        ▼
                   ┌──────────┐    no work for N days        ┌────────┐
                   │  ACTIVE  │ ─────────────────────────►   │ PAUSED │
                   └────┬─────┘                               └───┬────┘
                        │           wake by member action ▲       │
                        │ ◄──────────────────────────────────────┘
                        │
                        │ milestones reached;
                        │ completion ceremony
                        ▼
                   ┌──────────┐
                   │COMPLETED │
                   └────┬─────┘
                        │ retention period
                        ▼
                   ┌──────────┐
                   │ ARCHIVED │   cold tier; never deleted
                   └──────────┘    reanimatable by operator
                        ▲
                        │
                   ┌──────────┐
                   │ABANDONED │   with lessons-learned ceremony
                   └──────────┘
```

### A.5 External-tool-required bypass paths and lineage

<a id="appendix-a5"></a>

```text
1. EXCEPTION_PERIOD       Operator signs a time-bound, project-scoped
                          exception when a required external tool is
                          unavailable (e.g., DRC tool under maintenance,
                          Lean server offline). Signed, audit-logged,
                          auto-expires. Emits TOOL_REQUIREMENT_EXCEPTION
                          to ProjectLineage at start and end.

2. HEDGED_CLAIM_BYPASS    Persona phrases the claim as hypothetical
                          ("if this were DRC-clean, it would..."). The
                          claim classifier is calibrated
                          to allow hypotheticals; no refusal emitted.

3. ELEVATED_REQUIREMENT   For high-stakes domains (medical, aerospace),
                          operator policy may require BOTH external tool
                          attestation AND human sign-off. failure_action:
                          "escalate_operator". Bypass not available.
```

Lineage on bypass:

```text
TOOL_REQUIREMENT_EXCEPTION_OPENED
  requirement_id, exception_window, signed_by_operator, rationale
TOOL_REQUIREMENT_EXCEPTION_CLOSED
  closed_at, reason: "expired" | "operator_revoked" | "tool_recovered"
EXTERNAL_TOOL_REQUIREMENT_VIOLATED_BUT_BYPASSED
  emitted per action taken under exception; records the would-be refusal
```

### A.6 Contribution credit formula

<a id="appendix-a6"></a>

```text
contribution_credit_delta = w_v · verified_artifacts_authored
                          + w_p · proven_facts_proposed_and_proven
                          + w_o · obligations_discharged_on_time
                          + w_d · disagreements_resolved_via_synthesis
                          + w_r · peer_reviews_completed
                          + w_c · conjectures_advanced
                          − w_l · obligations_dropped
                          − w_b · safety_floor_refusals_caused_by_member

v1.0 default weights:
  w_v=1.0, w_p=0.8, w_o=0.6, w_d=0.5, w_r=0.4,
  w_c=0.5, w_l=0.4, w_b=0.5
```

### A.7 OpenProblem schema (open-problem/1)

<a id="appendix-a7"></a>

```python
@dataclass
class OpenProblem:
    schema: str = "open-problem/1"
    problem_id: str
    project_id: str
    statement: str                        # natural language
    formal_statement: str | None
    status: Literal["active", "dormant", "resolved", "abandoned", "morphed"]
    related_domain_items: dict[str, list[str]]  # v1.0 — keyed by ItemKind
                                                # (06_DOMAIN §7.6); replaces
                                                # math-shaped
                                                # `related_conjectures`.
    related_artifacts: list[str]
    opened_at: datetime
    opened_by: str
    resolution: str | None
    resolved_at: datetime | None
    signed_by: bytes
```

### A.8 ProjectMilestone and ProgressCriterion schemas

<a id="appendix-a8"></a>

```python
@dataclass
class ProjectMilestone:
    schema: str = "milestone/1"
    milestone_id: str
    project_id: str
    name: str
    criteria: list[ProgressCriterion]
    target_date: datetime | None
    reached: bool
    reached_at: datetime | None
    reached_by_artifact: str | None
    signed_by: bytes


@dataclass
class ProgressCriterion:
    description: str
    measurable_signal: str                # which StructuredFeedback kind
    threshold: dict
    achieved: bool
```

### A.9 ProjectItem schema (project-item/1)

<a id="appendix-a9"></a>

```python
@dataclass
class ProjectItem:
    schema: str = "project-item/1"
    item_id: str
    project_id: str

    kind: str                              # resolves against KindRegistry.
                                          # item_kinds (06_DOMAIN §7.6).
                                          # Substrate carries no closed list.
    status: str                            # resolved against the ItemKind's
                                          # status_fsm (06_DOMAIN §7.5
                                          # ProposedItemKind.status_fsm).
    payload: dict                          # kind-specific fields per the
                                          # ItemKindEntry.payload_schema
                                          # (JSONSchema validated at mint).

    proposed_by: persona_id
    proposed_at: datetime

    related_open_problems: list[str]
    related_items: list[str]               # cross-item links (any relation)
    blocks: list[str]                      # v1.0 — items this one BLOCKS
                                          # (transitive dependency edges).
                                          # Universal substrate semantic.
    blocked_by: list[str]                  # v1.0 — items blocking THIS one;
                                          # progress evaluator considers
                                          # blocked items non-advancing.
    parent_item_id: str | None             # for nesting (proof_attempt
                                          # under conjecture, design_
                                          # hypothesis under buildability_
                                          # concern, etc.)
    related_artifact_refs: list[str]
    related_obligations: list[str]

    confidence: float                      # 0..1, kind-specific EMA;
                                          # interpretation defined by
                                          # ItemKindEntry
    last_advanced_at: datetime
    signed_by: bytes
```

### A.10 MetaRegistry-seeded item kinds

<a id="appendix-a10"></a>

```yaml
# Math/research seed
- kind: conjecture
  description: "Living hypothesis with confidence EMA"
  payload_schema:
    statement: str
    formal_statement: str | null
    supporting_examples: list[EvidenceRef]
    counterexample_attempts: list[EvidenceRef]
    counterexample: EvidenceRef | null
    accepted_proof_ref: str | null
  status_fsm:
    [proposed, supported, challenged, proven!, refuted!, abandoned!, morphed!]
  advance_signal_hooks:
    [evidence_added, verifier_pass, panel_accept, peer_review_accept]

# Math/research seed
- kind: proof_attempt
  description: "Attempt to prove a parent conjecture"
  payload_schema:
    artifact_ref: str
    gaps: list[ProofGapPayload]
    verifier_invocation: str | null     # Lean/Coq/etc.
  status_fsm: [in_progress, complete!, has_gaps, failed!]
  advance_signal_hooks: [verifier_pass, gap_discharged]

# Math/research seed
- kind: proof_gap
  description: "Outstanding gap blocking a parent proof_attempt"
  payload_schema:
    description: str
    blocker: bool
    proposed_approach: str | null
    assigned_to: persona_id | null
    obligation_id: str | null
  status_fsm: [open, in_work, discharged!, abandoned!]

# Construction seed (domain-emergent on first home project)
- kind: design_hypothesis
  description: "Architectural / structural design assumption to verify"
  payload_schema:
    statement: str
    affects_artifacts: list[str]
    verification_method: str        # which verifier_kind discharges it
  status_fsm: [proposed, in_verification, verified!, refuted!]

# Construction seed (domain-emergent)
- kind: buildability_concern
  description: "Aspect of the design flagged as risky to build"
  payload_schema:
    description: str
    impact: str                     # cost / schedule / safety
    proposed_mitigation: str | null
  status_fsm: [raised, mitigated!, accepted_as_risk!, blocked]

# Clinical seed (domain-emergent)
- kind: differential_diagnosis
  description: "Candidate diagnosis under evidentiary evaluation"
  payload_schema:
    condition: str
    supporting_findings: list[str]
    ruling_out_findings: list[str]
  status_fsm: [candidate, leading, ruled_out!, confirmed!]

# Universal seed — every project with stakes
- kind: risk
  description: "An identified risk to the project, with mitigation"
  payload_schema:
    description: str
    probability: float              # 0..1
    severity: float                 # 0..1
    priority: float                 # probability × severity (derived)
    mitigation_plan: str | null
    contingency_plan: str | null
    owner: str                      # persona_id or external_agent_id
    impact_areas: list[str]         # cost / schedule / safety / quality
  status_fsm: [open, mitigating, mitigated, realised, accepted!, closed!]
  advance_signal_hooks:
    [mitigation_attestation_received, severity_recomputed,
     trigger_event_observed]

# Universal seed — every multi-step project
- kind: schedule_entry
  description: "A scheduled unit of work with planned + actual timing"
  payload_schema:
    description: str
    planned_start: datetime
    planned_end: datetime
    actual_start: datetime | null
    actual_end: datetime | null
    duration_estimate_seconds: int
    assigned_to: list[str]          # persona / external_agent ids
    related_milestone_ids: list[str]
  status_fsm: [planned, in_progress, complete!, blocked,
               cancelled!, slipped]
  advance_signal_hooks:
    [external_agent_log_received, milestone_advanced, blocker_cleared]

# Construction seed (illustrative — domain-emergent on first project)
- kind: change_order
  description: "A signed modification to a previously accepted artifact bundle"
  payload_schema:
    affected_bundle_ref: str
    rationale: str
    cost_delta: dict                # {currency_or_unit: amount}
    schedule_delta_seconds: int
    requires_approval_workflow_id: str | null
  status_fsm: [proposed, in_review, approved!, rejected!, withdrawn!]

# Construction seed
- kind: punch_list_item
  description: "Outstanding defect at near-completion stage"
  payload_schema:
    location: str
    description: str
    photo_refs: list[str]
    assigned_to: str | null
  status_fsm: [open, in_work, fixed!, deferred, waived!]

- kind: priority_claim     # research / IP / journalistic
                           # priority assertion.  Substrate seeds the
                           # ItemKind; the domain catalogs specific
                           # priority_claim_kinds (publication,
                           # patent, prior_art, scoop, etc.) as
                           # emergent kinds via KindRegistry.
  description: "First-claimant assertion bound to a date and artifact"
  payload_schema:
    claim_kind: str                # KindRegistry-resolved
                                   # (e.g. "publication", "patent")
    target_artifact_refs: list[str]  # ArtifactBundle / ItemRef
    claim_date: datetime           # the priority date being asserted
    embargo_until: datetime | null # if under embargo
    evidence_refs: list[str]       # arxiv id, USPTO filing, witness
                                   # statements, signed-timestamp
                                   # service receipts
    co_claimants: list[str]        # other personas / external_agents
                                   # on the claim
    disclosure_state: str          # KindRegistry-resolved emergent kind
                                   # (e.g. "undisclosed", "filed",
                                   # "published", "granted")
  status_fsm: [drafted, witnessed, asserted, contested, established!,
               withdrawn!, superseded!]
```

### A.11 Obligation schema (obligation/1)

<a id="appendix-a11"></a>

```python
@dataclass
class Obligation:
    schema: str = "obligation/1"
    obligation_id: str
    project_id: str
    
    obligor_persona_id: str
    obligee: Obligee                      # one persona OR team
    
    description: str
    discharge_criteria: list[str]
    expected_artifact_ref: str | None
    
    committed_at: datetime
    due_date: datetime | None
    reminders: list[datetime]
    grace_period: timedelta
    
    status: Literal["active", "discharged", "overdue",
                    "released_with_completion",
                    "released_with_abandonment",
                    "released_with_member_departure",
                    "dropped"]
    discharged_at: datetime | None
    discharged_by_artifact_ref: str | None
    discharged_by_evidence: str | None
    dropped_reason: str | None
    
    signed_by_obligor: bytes
    signed_by_obligee_acceptance: bytes
    discharge_signed_by: bytes
```

### A.12 ObligationReassignment schema and admission rules

<a id="appendix-a12"></a>

```python
@dataclass
class ObligationReassignment:
    schema: str = "obligation-reassignment/1"
    reassignment_id: str
    obligation_id: str                          # target obligation

    outgoing_obligor_persona_id: str
    incoming_obligor_persona_id: str
    obligee: Obligee                            # mirrors original obligation;
                                                # included for signature scope

    # RATIONALE — operator-readable; obligee considers when accepting/refusing.
    reassignment_rationale_kind: str            # KindRegistry-resolved
                                                # reassignment_rationale_kinds
                                                # (e.g. "outgoing_retiring",
                                                #  "lead_handoff", "planned_
                                                #  departure", "role_change")
    rationale_text: str                         # ≤ 1000 chars

    # ADJUSTMENTS — incoming may need different due_date or grace_period.
    # Substrate carries the deltas; obligee MUST agree (cosign covers them).
    new_due_date: datetime | None               # null = preserve original
    new_grace_period: timedelta | None          # null = preserve original

    # SIGNATURES — tri-signed envelope.  Substrate refuses delivery without
    # all three.
    outgoing_signed_at: datetime
    outgoing_signed_by: bytes
    incoming_signed_at: datetime | None
    incoming_signed_by: bytes | None
    obligee_signed_at: datetime | None          # null until obligee accepts
    obligee_signed_by: bytes | None

    state: Literal["drafted",                   # outgoing has signed
                    "incoming_accepted",        # incoming has signed
                    "fully_signed",             # obligee has cosigned;
                                                # ready to apply
                    "refused_by_incoming",      # incoming declined
                    "refused_by_obligee",       # obligee declined →
                                                # original obligation
                                                # discharges per §9
                    "applied",                  # obligation.obligor_
                                                # persona_id mutated
                                                # to incoming
                    "expired"]
    applied_at: datetime | None
    refusal_reason: str | None

    signed_by: bytes                            # kernel signature on draft;
                                                # cosigns accumulate
```

Admission rule:

```text
On ObligationReassignment.draft:
  1. Verify obligation.status = "active" (cannot reassign already-
     discharged work); refuse with `obligation_not_active`.
  2. Verify outgoing_obligor matches obligation.obligor_persona_id;
     refuse with `outgoing_obligor_mismatch`.
  3. Outgoing's signature is implicit in the draft (drafter MUST be
     outgoing or operator on outgoing's behalf if outgoing is
     pre-DORMANT).  Move state → "drafted".

On incoming cosign:
  1. Verify incoming has consent capability (NOT a RETIRED persona).
  2. Apply any due_date / grace_period adjustments to a draft view
     for obligee inspection.
  3. State → "incoming_accepted".

On obligee cosign:
  1. Verify obligee_persona_id (or team_id) matches original obligee.
  2. State → "fully_signed".  Kernel applies the reassignment:
       obligation.obligor_persona_id := incoming
       obligation.committed_at PRESERVED (no rewrite)
       obligation.due_date / grace_period := new_* if provided
       obligation.reassignment_history.append(reassignment_id)
       (the obligation schema gains a reassignment_history list)
  3. Emit OBLIGATION_REASSIGNED to project lineage.
  4. State → "applied".

On obligee refuse:
  1. State → "refused_by_obligee".
  2. Original obligation is NOT auto-reassigned to anyone.  It remains
     active under outgoing until outgoing's departure ceremony, at
     which point §9 default behaviour applies (auto-discharge with
     status = "released_with_member_departure").

On incoming refuse:
  1. State → "refused_by_incoming".  No mutation.  Outgoing may draft
     a new ObligationReassignment to a different incoming, OR accept
     auto-discharge at departure.
```

### A.13 Disagreement, Position, and Resolution schemas

<a id="appendix-a13"></a>

```python
@dataclass
class Disagreement:
    schema: str = "disagreement/1"
    disagreement_id: str
    project_id: str
    topic: str
    
    positions: list[Position]             # ≥ 2 positions held
    
    status: Literal["active", "resolved_synthesis",
                    "resolved_majority", "resolved_split",
                    "abandoned"]
    
    resolution: Resolution | None
    resolved_at: datetime | None
    
    opened_at: datetime
    opened_by: persona_id
    blocking_artifacts: list[str]
    blocking_obligations: list[str]
    expected_resolution_by: datetime | None
    
    signed_by: bytes


@dataclass
class Position:
    schema: str = "position/1"
    position_id: str
    summary: str
    rationale: str
    proponents: list[persona_id]
    supporting_evidence: list[EvidenceRef]
    formalisation: str | None
    proposed_at: datetime
    proposed_by: persona_id
    signed_by: bytes


@dataclass
class Resolution:
    kind: Literal["synthesis", "majority_decision",
                  "deferred_to_lead", "deferred_to_operator",
                  "deferred_to_evidence", "split_into_subprojects"]
    chosen_position_id: str | None
    synthesis_position_id: str | None
    decision_signed_by: list[persona_id]
    decision_rationale: str
```

### A.14 PeerReview schema and anonymity enforcement

<a id="appendix-a14"></a>

```python
@dataclass
class PeerReview:
    schema: str = "peer-review/1"
    review_id: str
    project_id: str
    bundle_id: str
    
    authors: list[persona_id]
    reviewers: list[persona_id]
    chair: persona_id | None
    
    status: Literal["initiated", "in_progress", "revision_requested",
                    "accepted", "rejected", "withdrawn"]
    round: int
    expected_rounds: int
    
    comments: list[ReviewComment]
    revision_requests: list[RevisionRequest]
    author_responses: list[AuthorResponse]
    
    final_verdict: Literal["accept_as_is", "accept_with_revisions",
                            "reject"] | None
    verdict_signed_by: list[persona_id]
    
    initiated_at: datetime
    decision_required_by: datetime | None
    completed_at: datetime | None

    # B2 — anonymity topology (substrate-shape; substrate
    # enforces routing + visibility, never identity opinions).
    anonymity_tier: Literal["named",          # default; reviewer + author
                                              # identities mutually visible
                            "single_blind",   # reviewer sees author;
                                              # author does not see reviewer
                            "double_blind"    # neither side sees the other;
                                              # only the chair (or operator
                                              # role under principal collapse)
                                              # holds the mapping
                           ] = "named"
    anonymity_holder: persona_id | None = None    # who holds the un-blinding
                                                  # mapping (typically the
                                                  # chair); null only when
                                                  # tier = "named"
    deanonymisation_policy: Literal[
        "on_acceptance",     # un-blind when verdict signed
        "on_rejection",      # un-blind when verdict signed
        "on_request",        # author or reviewer may opt in any time
        "never",             # permanently blind (post-publication audit
                             # only by anonymity_holder)
    ] = "never"
    
    signed_by: bytes
```

Anonymity enforcement (substrate-side). When `anonymity_tier` is single_blind or double_blind:

```text
1. ReviewComment / RevisionRequest / AuthorResponse projections to the
   opposite side strip persona_id, name, persona_card_ref; only an opaque
   round-scoped pseudonym (kernel-generated, project-scope-private) is
   shown.
2. Visibility tier on the PeerReview record is forced to project-private
   minimum (federation publication MUST resolve to per-tier projections
   that respect the binding).
3. Memory tagging: reviewers' comments are stored under a per-review
   anonymous scope; the anonymity_holder is the only persona who can
   read the un-blinded mapping.
4. Under principal_topology = operator_is_user, anonymity_holder cannot
   be a persona owned by the principal alone; an independent ExternalAgent
   or operator-policy holder is required (mirrors §5.6 credential
   collapse handling).
5. Deanonymisation requires a signed event (peer_review_deanonymised)
   citing deanonymisation_policy and either the policy-trigger condition
   (verdict signed) or both-party consent (for "on_request").
```

### A.15 ApprovalWorkflow and ApprovalStep schemas

<a id="appendix-a15"></a>

```python
@dataclass
class ApprovalWorkflow:
    schema: str = "approval-workflow/1"
    workflow_id: str
    project_id: str

    subject_kind: str                       # resolves against KindRegistry
                                            # (any kind family). What's being
                                            # approved (artifact_bundle,
                                            # project_item, physical_asset,
                                            # external_attestation, etc.).
    subject_id: str

    steps: list[ApprovalStep]               # ORDERED; sequential progress
    current_step_index: int                 # 0-indexed; advances only on
                                            # current step approval

    status: Literal["pending", "in_progress", "approved",
                     "rejected", "withdrawn", "expired"]
    initiated_at: datetime
    initiated_by: persona_id
    expected_completion_at: datetime | None
    completed_at: datetime | None
    final_decision_signed_by: list[bytes]   # cumulative signers
    signed_by: bytes


@dataclass
class ApprovalStep:
    schema: str = "approval-step/1"
    step_id: str
    workflow_id: str
    order: int                              # 1-indexed display order

    approver_kind: Literal["persona", "external_agent",
                            "operator", "system"]
    approver_id: str                        # respective id

    title: str                              # "City planning review"
    deadline: datetime | None
    evidence_kinds_required: list[str]      # resolves against KindRegistry.
                                            # outcome_kinds or media_kinds
                                            # (e.g. "external_attestation",
                                            # "stamped_drawing")

    status: Literal["pending", "in_progress", "approved",
                     "rejected", "skipped", "expired"]
    decision_signed_by: bytes | None
    decision_at: datetime | None
    comments: list[str]
    evidence_refs: list[str]                # ExternalAttestation / outcome /
                                            # ProjectItem refs

    signed_by: bytes
```

### A.16 NotationConvention schema (notation/1)

<a id="appendix-a16"></a>

```python
@dataclass
class NotationConvention:
    schema: str = "notation/1"
    convention_id: str
    project_id: str | None
    domain_id: str | None
    symbol: str                           # "⊗_p", "Δi", "Fsw", "EBITDA_run"
    meaning: str
    formal_definition: str | None
    scope: Literal["project", "domain"]
    introduced_at: datetime
    introduced_by: persona_id | None
    deprecated: bool
    deprecated_reason: str | None
    superseded_by: str | None
    signed_by: bytes
```

### A.17 CitationGraph, InternalCredit, and ExternalCitation schemas

<a id="appendix-a17"></a>

```python
@dataclass
class CitationGraph:
    schema: str = "citation/1"
    graph_id: str
    project_id: str
    internal_credits: list[InternalCredit]
    external_citations_out: list[ExternalCitation]   # we cite them
    external_citations_in: list[ExternalCitation]    # they cite us
    last_updated_at: datetime


@dataclass
class InternalCredit:
    credit_id: str
    project_id: str
    contribution_kind: str                # resolves against KindRegistry.
                                          # contribution_kinds (06_DOMAIN §7.6);
                                          # never a closed enum. Domain-
                                          # emergent kinds added per
                                          # ProposedContributionKind. Common
                                          # MetaRegistry seeds (math/CS):
                                          # "idea", "definition", "lemma",
                                          # "proof", "construction",
                                          # "argument", "counterexample",
                                          # "review_insight". Construction
                                          # domain emerges: "site_survey",
                                          # "code_compliance_check",
                                          # "structural_calc", etc.
    description: str
    contributed_by: persona_id
    contributed_at: datetime
    referenced_in: list[str]
    weight: float
    signed_by: bytes
    co_signed_by_lead: bool


@dataclass
class ExternalCitation:
    citation_id: str
    direction: Literal["outgoing", "incoming"]
    external_ref: str                     # DOI, arXiv id, URL
    title: str
    authors: list[str]
    venue: str | None
    year: int
    artifact_ref: str | None
    contribution: str
    discovered_at: datetime
    discovered_by: persona_id | str
    signed_by: bytes
```

### A.18 Project membership admission paths

<a id="appendix-a18"></a>

```text
0. FORMATION VIA EnvFormationProposal (v1.0 preferred for NEW projects)
                        persona drafts EnvFormationProposal with
                        proposed_env_type_kind="project_workspace" and
                        recruits (05_ENVIRONMENT §12c).  The project
                        and its env materialise atomically when the
                        consent flow completes per the proposal's
                        cohort_atomicity rule.  ProjectMember entries
                        are the resulting EnvironmentMembership records.
                        Replaces the legacy two-step "operator creates
                        project → personas recruited to existing
                        project" flow for new project creation.  Use
                        this path when no project exists yet.

1. INVITED              operator or lead emits PROJECT_INVITATION
                        candidate's kernel evaluates compatibility
                        (charter, acceptance pathways, env policy)
                        signs PROJECT_INVITATION_ACCEPTED/DECLINED.
                        Use when project already exists.

2. RECRUITED            persona-led cohort assembly into an existing
                        project_workspace env.  Lead emits
                        PROJECT_RECRUIT_PROPOSAL with project_id;
                        recruit's consent flow runs per 09_PROTOCOLS
                        §3C.4 + PersonaPersonaBoundary check.
                        Use when project already exists.

3. SELF-PROPOSED        persona discovers project via PersonaCard/
                        ProjectCard search; submits PROJECT_SELF_PROPOSED;
                        lead + operator approve.  Use when project
                        already exists and persona lacks an invitation.
                        For new envs, EnvSelfProposalRequest
                        (05_ENVIRONMENT §12b) is the env-layer analogue.
```

### A.19 Project membership departure paths

<a id="appendix-a19"></a>

```text
- PROJECT_MEMBER_LEFT             voluntary
- PROJECT_MEMBER_REMOVED          operator/lead action
- retirement                      persona enters DORMANT/RETIRED
                                   → membership auto-paused; obligations
                                     released-as-orphaned
- project end                     completion/abandonment finalises
```

### A.20 Cohort assembly event taxonomy

<a id="appendix-a20"></a>

```text
Core events:
  COHORT_REQUEST              CANDIDATE_ROSTER
  RECRUIT_PROPOSAL            RECRUIT_ACCEPTED         RECRUIT_DECLINED
  RECRUIT_ADMITTED            ENV_GROWTH_REQUEST       ENV_GROWN
  COHORT_DENIED               LEAD_PERSONA_ASSIGNED

Extended events (project + env scope):
  PROJECT_INVITATION                PROJECT_INVITATION_ACCEPTED
  PROJECT_INVITATION_DECLINED       PROJECT_RECRUIT_PROPOSAL
  PROJECT_SELF_PROPOSED             PROJECT_MEMBER_LEFT
  PROJECT_MEMBER_REMOVED            PROJECT_BUDGET_THRESHOLD
  
  ENV_INVITATION                    ENV_INVITATION_ACCEPTED
  ENV_INVITATION_DECLINED           ENV_RECRUIT_PROPOSAL
  ENV_MEMBER_ADMITTED               ENV_MEMBER_DEPARTED
  ENV_MEMBER_ROLE_CHANGED           ENV_PRESENCE_PINNED_BY_OPERATOR
  
COHORT_DENIED reason set extended:
  Core: capability_not_enabled, budget_exhausted
  Extended: project_membership_required, project_charter_incompatible,
       project_at_capacity, domain_tool_unavailable,
       acceptance_pathway_mismatch
  cohort_constraint_unsatisfied
```

### A.21 CohortConstraint schema (cohort-constraint/1)

<a id="appendix-a21"></a>

```python
@dataclass
class CohortConstraint:
    schema: str = "cohort-constraint/1"
    constraint_id: str
    project_id: str

    # The substrate names no roles.  required_kinds are
    # KindRegistry-resolved contribution_kind entries the project's
    # domain catalogs.  A research project may require
    # ["theoretical", "experimental", "computational"]; a
    # construction project may require ["lead", "engineer",
    # "supervisor"]; a writer's room may require ["showrunner",
    # "writer", "researcher"].
    required_kinds: list[str]                # KindRegistry-resolved
    min_count_per_kind: dict[str, int]       # default 1 each
    max_count_per_kind: dict[str, int] | None

    # Independence constraints (e.g. peers from disjoint affiliations
    # to satisfy peer-attestation independence rules — §5.6).
    independence_rule: Literal["none",
                                "disjoint_affiliations",
                                "disjoint_organisations"] = "none"

    # When the constraint is checked
    enforced_at: list[Literal["project_admission",
                                "milestone_n_minus_1",
                                "ceremony_precondition"]]

    declared_at: datetime
    declared_by: str                         # operator or lead persona
    signed_by: bytes
```

### A.22 CohortDynamicsState schema (cohort-dynamics/1)

<a id="appendix-a22"></a>

```python
@dataclass
class CohortDynamicsState:
    schema: str = "cohort-dynamics/1"
    state_id: str
    project_id: str
    cohort_id: str
    as_of: datetime

    # Cohesion composite — weighted sum of the axes below.
    # No new signals introduced; the kernel rolls up what is already
    # in ProjectLineage + PersonaRelationshipEdge + Disagreement.
    cohesion_score: float                        # 0..1

    # Trust composite — average of pairwise PersonaRelationshipEdge
    # trust scores across the cohort (active edges only).
    avg_pairwise_trust: float

    # Joint-success ratio — joint_successes / max(1, joint_collaborations)
    # across all pairwise edges, anti-farming-weighted per
    # 02_PERSONA §11.4.
    joint_success_ratio: float

    # Disagreement health — disagreements_resolved / max(1, disagreements_total)
    # across the cohort, with active-disagreement-age penalty for
    # disagreements past their declared resolution window.
    disagreement_resolution_ratio: float
    aged_unresolved_disagreement_count: int

    # Role health — per required_kind from CohortConstraint, is the
    # min_count_per_kind still met AND does each member in that role
    # have positive recent contribution_credit?
    role_health_by_kind: dict[str, Literal[
        "healthy", "thin", "stagnant",
        "unfilled"]]

    # Fractiousness — pair-scoped disputes / pair-scoped collaborations,
    # rolled up.  High values indicate the cohort is splintering.
    fractiousness_index: float                   # 0..1; 0 = harmonious,
                                                 # 1 = every pair disputes

    # Throughput drift — milestones reached per unit time over the
    # last N tasks vs the cohort's own baseline (set at first milestone
    # reached).  Drops below 0.5 emit cohort_throughput_degraded.
    throughput_relative_to_baseline: float

    # State band
    band: Literal["healthy", "watch",
                   "intervene", "dissolve_proposed"]
    band_thresholds: dict[str, float]            # operator-policy-tunable;
                                                 # defaults below

    signed_by: bytes


DEFAULT_BAND_THRESHOLDS = {
    "watch":             0.70,
    "intervene":         0.55,
    "dissolve_proposed": 0.40,
}
```

### A.23 CohortDynamicsState band transitions

<a id="appendix-a23"></a>

```text
healthy            cohesion_score ≥ watch threshold
                   no automatic action; reported in project dashboard

watch              cohesion_score in [intervene, watch)
                   cohort lead notified; PANEL review of cohort
                     composition recommended at next milestone

intervene          cohesion_score in [dissolve_proposed, intervene)
                   operator notified; CohortConstraint re-evaluation
                     forced at next milestone gate (may require new
                     recruit, role rebalance, or mediation pairing)
                   new high-stakes obligations refused until band
                     restored to watch or healthy

dissolve_proposed  cohesion_score < dissolve_proposed
                   cohort lead + operator both required to keep cohort
                     intact (PROJECT_COHORT_PIN_RENEWED); absent the
                     pin, cohort enters DISSOLVE_PROPOSED → members
                     released-as-orphaned (existing membership flow §14)
```

### A.24 PlannedDeparture schema, admission rules, and anticipatory rebalance

<a id="appendix-a24"></a>

```python
@dataclass
class PlannedDeparture:
    schema: str = "planned-departure/1"
    plan_id: str
    project_id: str
    departing_member_id: str                    # ProjectMember.persona_id

    # SCHEDULE
    declared_at: datetime
    departure_date: datetime                    # when the departure ceremony
                                                # fires; MUST be in the future
                                                # at draft time
    rebalance_window: timedelta                 # how far ahead of
                                                # departure_date the
                                                # CohortDynamicsState
                                                # anticipates; default 90d;
                                                # operator-tunable

    # REASON — operator-readable; informs CohortDynamicsState band model.
    departure_reason_kind: str                  # KindRegistry-resolved
                                                # departure_reason_kinds
                                                # (e.g. "retirement",
                                                #  "role_change",
                                                #  "project_completion",
                                                #  "operator_directive")
    rationale_text: str                         # ≤ 1000 chars

    # PER-EDGE HANDOFF HINTS — for each active PersonaRelationshipEdge
    # the departing member holds, propose a transfer target.
    # Substrate is hint-only: the target persona must consent through
    # the standard PersonaRelationshipEdge formation path (02_PERSONA
    # §11.4) — there is no auto-edge-transfer.
    edge_transfer_hints: list[EdgeTransferHint]

    # OBLIGATION HANDOFF HINTS — for each active Obligation the
    # departing member holds, propose a reassignment.  Each hint
    # may be materialised as an ObligationReassignment draft
    # (§9.1) by the operator or the departing persona.
    obligation_reassignment_hints: list[ObligationReassignmentHint]

    # LEAD HANDOFF — when the departing member holds the `lead` role,
    # this field MUST be set to a successor candidate persona_id; the
    # PlannedDeparture composes with LeadHandoffCeremony (§25.1)
    # which drafts on departure_date - rebalance_window.
    lead_successor_candidate_id: str | None = None

    state: Literal["drafted",
                    "active",                   # rebalance_window window open;
                                                # CohortDynamicsState applies
                                                # anticipatory rebalance
                    "departure_fired",          # departure_date reached;
                                                # standard departure ceremony
                                                # (05_ENV §5.1) fires
                    "cancelled"]                # operator may cancel before
                                                # departure_date; emits
                                                # PLANNED_DEPARTURE_CANCELLED
    cancelled_at: datetime | None
    cancellation_reason: str | None

    signed_by_departing: bytes                  # the departing member cosigns
                                                # (consent to graceful
                                                # departure rather than
                                                # abrupt one)
    signed_by_operator: bytes                   # operator authorises


@dataclass
class EdgeTransferHint:
    edge_id: str                                # PersonaRelationshipEdge id
    other_party_persona_id: str                 # the counterparty
    suggested_transfer_target_id: str           # the new persona who would
                                                # form a fresh edge with the
                                                # counterparty
    rationale: str


@dataclass
class ObligationReassignmentHint:
    obligation_id: str
    suggested_incoming_obligor_id: str
    suggested_new_due_date: datetime | None
    rationale: str
```

Admission rule:

```text
On PlannedDeparture.draft:
  1. Verify departing_member_id is an active ProjectMember; refuse
     otherwise with `member_not_active`.
  2. Verify departure_date > now() + min_lead_time (default 14d);
     refuse abrupt-departure-via-planned-envelope with
     `departure_date_too_soon`.
  3. Verify lead_successor_candidate_id set if departing member holds
     `lead` role; refuse `lead_successor_required_for_lead_departure`.
  4. Emit PLANNED_DEPARTURE_DRAFTED to project lineage.

On both signatures (departing + operator):
  1. State → "active".  CohortDynamicsState begins anticipatory
     rebalance (see below).
  2. Emit PLANNED_DEPARTURE_ACTIVATED.

On departure_date arrival:
  1. State → "departure_fired".
  2. Standard EnvironmentMembership departure ceremony (05_ENV §5.1)
     fires; member departs per the existing flow.
  3. CohortDynamicsState releases anticipatory rebalance and
     recomputes from actual post-departure edge set.

On operator cancel (before departure_date):
  1. State → "cancelled".
  2. CohortDynamicsState reverts anticipatory rebalance; recomputes
     from current actual edge set.
  3. Emit PLANNED_DEPARTURE_CANCELLED.
```

Anticipatory rebalance (CohortDynamicsState extension):

```text
weight(edge_e, t) =
    1.0                                     for t < departure_date - rebalance_window
    interpolate(1.0, 0.0, ratio)            for departure_date - rebalance_window
                                            <= t < departure_date
                                            where ratio = (t - (departure_date -
                                                          rebalance_window)) /
                                                          rebalance_window
    0.0                                     for t >= departure_date

This makes the departing member's contribution to cohesion / fractiousness
fade smoothly rather than dropping abruptly on departure day.  Bands
transitions trigger if they would naturally; the rebalance does not
suppress legitimate band transitions, only smooths the curve.
```

### A.25 ProjectLineage event types

<a id="appendix-a25"></a>

```text
project_proposed                    project_activated
project_member_added                project_member_removed
project_member_role_changed
project_charter_signed              project_charter_version_bumped
project_charter_drift_detected
domain_context_assigned             domain_context_version_changed
artifact_bundle_drafted             artifact_bundle_published
artifact_co_edit                    artifact_review_started
artifact_review_resolved
open_problem_opened                 open_problem_resolved
open_problem_morphed
conjecture_proposed                 conjecture_advanced
conjecture_refuted
obligation_committed                obligation_discharged
obligation_dropped
disagreement_recorded               disagreement_resolved
notation_defined                    notation_deprecated
citation_recorded
milestone_set                       milestone_reached
external_tool_required_failed
novelty_check_passed                novelty_check_failed
peer_review_initiated               peer_review_resolved
session_started_in_project          session_ended_in_project
task_classified_under_project       task_completed_in_project
project_paused                      project_resumed
project_completed                   project_abandoned
project_archived                    project_reanimated
project_forked
project_morphed

# additions:
as_built_reconciliation_drafted     as_built_reconciliation_signed
as_built_reconciliation_superseded
credential_verified                 credential_unverified
project_member_pinned               project_member_unpinned

# additions:
cohort_dynamics_recomputed          cohort_band_changed
cohort_throughput_degraded          project_cohort_pin_renewed
persona_relationship_state_changed
```

### A.26 evaluate_project_progress function

<a id="appendix-a26"></a>

```python
def evaluate_project_progress(session_lineage, project, structured_feedback,
                                env_ambient_streams):
    deltas = ProjectStateDelta()
    
    # 1. Milestones reached
    for m in project.milestones:
        if milestone_criteria_met(m, session_lineage):
            deltas.milestones_reached.append(m.milestone_id)
    
    # 2. Open problems resolved or morphed
    for p in project.open_problems:
        if p.status_changed_this_session(session_lineage):
            ...
    
    # 3. Conjectures advanced
    for c in project.conjectures:
        if conjecture_confidence_changed(c) >= delta_threshold:
            deltas.conjectures_advanced.append(c.conjecture_id)
    
    # 4. Obligations discharged
    deltas.obligations_discharged = obligations_discharged_this_session(...)
    
    # 5. Verified facts added
    deltas.proven_facts_added = proven_facts_added_this_session(...)
    
    # 6. AMBIENT signals
    # Cross-env event links + ambient contributions count toward
    # project progress
    for env_id in project.environments:
        env_stream = env_ambient_streams[env_id]
        for event in env_stream.recent_events_relevant_to_project(project):
            ...
    
    aggregate = compute_progress_score(deltas, project)
    
    return AcceptanceResult(
        pathway="project_progress_accept",
        progress_delta=deltas,
        aggregate_progress_score=aggregate,
        accepted=(aggregate > 0 or has_explicit_continue()),
        status=("project_progress_accept_and_completion"
                if all_milestones_reached() else
                "project_progress_accept")
    )
```

### A.27 ProjectStateDelta, ProgressAggregator, and rolling EMA

<a id="appendix-a27"></a>

```python
@dataclass
class ProjectStateDelta:
    schema: str = "project-state-delta/1"
    session_id: str
    milestones_reached: list[str]
    open_problems_resolved: list[str]
    open_problems_morphed: list[tuple[str, str]]   # (old, new_id)
    conjectures_advanced: list[str]
    conjectures_refuted: list[str]
    obligations_discharged: list[str]
    proven_facts_added: list[str]
    artifacts_published: list[str]
    ambient_links: list[str]                       # cross-env links


@dataclass
class ProgressAggregator:
    schema: str = "progress-aggregator/1"
    project_id: str
    window_half_life_days: int = 28                # 4 weeks default
    session_scores: list[tuple[datetime, float]]   # (t, s_N ∈ [-1, +1])
    ema: float                                     # current EMA
    status_flag: Literal["thriving", "active",
                         "stalled", "regressing"]
    stalled_session_count: int                     # for "≥ 4 sessions"
    last_updated_at: datetime
```

Rolling EMA over per-session scores:

```text
session N score        s_N ∈ [-1, +1] computed from ProjectStateDelta
                       weighted by per-outcome-kind weight (§22)
ema_new = α · s_N + (1 - α) · ema_old
where α = 1 - exp(-Δt_days / window_half_life_days)
       Δt_days = days since previous session

status flag:
  "thriving"    EMA > 0.6 sustained
  "active"      EMA > 0.2
  "stalled"     |EMA| < 0.1 for ≥ 4 sessions
  "regressing"  EMA < -0.1
```

### A.28 Project fork inheritance policies

<a id="appendix-a28"></a>

```text
inherit_all          full membership + artifact history + conjectures +
                     notation + citations
inherit_summary      co-signed summary + notation + citations; no
                     in-progress artifacts
inherit_seed         charter + domain + notation; clean state
```

### A.29 Multi-environment hosting example

<a id="appendix-a29"></a>

```python
project.environments = ["acme_office", "acme_engineering_lab", "remote_lab"]
project.primary_environment_id = "acme_office"
```

### A.30 CrossDomainTransfer schema

<a id="appendix-a30"></a>

```python
@dataclass
class CrossDomainTransfer:
    schema: str = "cross-domain-transfer/1"
    transfer_id: str
    transferred_at: datetime
    artifact_type: str                    # resolves against KindRegistry
                                          # (06_DOMAIN §7.6). Transfers may
                                          # carry any registered kind (skill,
                                          # convention, lesson, knowledge_ref,
                                          # verifier_recipe, media kind,
                                          # capability kind, etc.) so long
                                          # as the kind is registered in
                                          # both source and target domains
                                          # or in the MetaRegistry.
    artifact_ref: str
    source_domain_id: str
    target_domain_id: str
    source_trust_score: float
    target_trust_score: float             # initially reduced
    transferred_by_persona_id: str
    successful_target_uses: int
    failed_target_uses: int
    signed_by: bytes
```

### A.31 Multi-tenant cross-org joint project formation sequence

<a id="appendix-a31"></a>

```text
1. PRE-FORMATION
   Each operator independently signs a CrossTenancyAgreementRef
   (operator-authored policy artefact; substrate carries by id).
   Without the agreement, joint formation refuses with
   `cross_tenant_agreement_missing`.

2. PRINCIPAL ATTRIBUTION
   The proposing operator drafts a PrincipalAttribution with
   multi_principal_attribution_enabled = True, lists all N
   PrincipalRefs (one per operator), declares weights
   (defaults to 1.0 each), and emits PRINCIPAL_ATTRIBUTION_DECLARED.
   Each operator co-signs their own PrincipalRef.

3. ENV FORMATION PROPOSAL
   The proposer drafts an EnvFormationProposal (05_ENV §12c) with
   `proposed_env_type_kind = "project_workspace"` (per v1.0 unification)
   and `charter_authorship_mode = co_authored_required`.  CohortInvites
   are issued to recruits from BOTH tenants; each recruit's
   CohortConsentResponse MUST name the PrincipalRef they are joining
   under.  The proposer cannot pre-assign principals on recruits'
   behalf (consent is the principal binding).

4. CHARTER RATIFICATION
   The proposal accumulates consents; on consent_complete, a
   MultiPrincipalAttestationQuorum is drafted with
   target_event_kind = "env_charter_ratified".  Each principal
   cosigns; unanimous by default.  On clearance, env instantiates
   and the project is created.

5. ONGOING WORK
   Members work as in any project_workspace env (§4 lifecycle).
   Anti-leakage rules 1-5 (§19) filter explicit cross-domain transfers
   of named artifacts; DerivationProvenanceEdge enforcement (per the
   env's DerivationProvenancePolicy, defaulted to
   mandatory_for_cross_principal for joint envs) covers implicit
   derivation.  RISK B and RISK E refusals emit
   CROSS_DOMAIN_LEAKAGE_BLOCKED to lineage.

6. COMPLETION
   When all critical milestones reached (§4.1), a second
   MultiPrincipalAttestationQuorum is drafted with
   target_event_kind = "project_completed".  Unanimous default;
   degraded-path clearance permitted under §12c.4a conditions.
```

### A.32 OutcomeFeedback schema (outcome-feedback/1)

<a id="appendix-a32"></a>

```python
@dataclass
class OutcomeFeedback:
    schema: str = "outcome-feedback/1"
    outcome_id: str
    project_id: str
    bundle_id: str | None                     # target artifact bundle

    kind: str                                 # resolves against KindRegistry.
                                              # outcome_kinds (06_DOMAIN §7.6).
                                              # Substrate carries no closed list.
    payload: dict                             # kind-specific fields per the
                                              # OutcomeKindEntry.payload_schema
                                              # (JSONSchema validated at mint)

    arrival_mode: str                         # external_webhook / scheduled_pull /
                                              # operator_upload / human_bridged_pdf
    external_attestation_ref: str | None      # required if OutcomeKindEntry.
                                              # requires_external_attestation
    requires_corroboration: bool              # sourced from
                                              # OutcomeKindEntry
    corroborating_outcome_ids: list[str]

    confidence: float
    discovered_at: datetime
    discovered_by: persona_id | str
    signed_by: bytes
```

### A.33 MetaRegistry-seeded outcome kinds

<a id="appendix-a33"></a>

```yaml
# Academic seed
- kind: citation_observation
  description: "Outgoing/incoming external citation"
  payload_schema:
    direction: enum[incoming, outgoing]
    external_ref: str                # DOI / arXiv id / URL
    title: str
    authors: list[str]
    year: int
    venue: str | null
    context: str
    target_artifact_ref: str | null
  arrival_modes: [scheduled_pull, persona_search]
  requires_external_attestation: false
  requires_corroboration: true

# Software-distribution seed
- kind: community_uptake
  description: "External adoption metric for a published artifact"
  payload_schema:
    platform: str                    # source_kinds entry
    artifact_external_ref: str
    metric: str                      # contribution_kinds entry
    value: int
    delta_since_last: int
    period_days: int
    sybil_filter_applied: bool
    value_after_sybil_filter: int
  arrival_modes: [scheduled_pull, external_webhook]
  requires_external_attestation: false
  requires_corroboration: true

# Software-deployment seed
- kind: production_telemetry
  description: "Runtime/QA signals from production deployment"
  payload_schema:
    deployment_id: str
    period: tuple[datetime, datetime]
    metrics: dict[str, float]        # p99_latency_ms, error_rate, mttr, ...
    incidents: int
    comparison_to_baseline: dict[str, float]
    pipeline_signed: bool
  arrival_modes: [external_webhook, scheduled_pull]
  requires_external_attestation: false

# Software-testing seed
- kind: test_results
  description: "CI test suite outcome for an artifact"
  payload_schema:
    test_suite_id: str
    passed: int
    failed: int
    skipped: int
    coverage_pct: float
    regressions_introduced: int
    flaky_tests: int
    ci_run_ref: str | null
  arrival_modes: [external_webhook]
  requires_external_attestation: false

# Regulated-industry seed
- kind: regulatory_outcome
  description: "Outcome from a regulator review"
  payload_schema:
    regulator: str                   # "UL", "FDA", "FCC", "city_building_dept"
    standard: str                    # IEC 62368-1:2024 / IRC R301 / 21 CFR 820
    verdict: str                     # "passed", "passed_with_conditions",
                                     # "failed", "withdrawn"; resolves
                                     # against KindRegistry.quality_tag_kinds
                                     # or a regulator-specific scheme.
    report_ref: str
    conditions: list[str]
    exemptions: list[str]
    decided_at: datetime
    regulator_signature: bytes
  arrival_modes: [operator_upload, human_bridged_pdf]
  requires_external_attestation: true

# Construction seed (domain-emergent)
- kind: building_inspection
  description: "City inspector signoff for a construction phase"
  payload_schema:
    inspection_phase: str            # "foundation", "framing", "rough_in",
                                     # "final"; emergent contribution_kind
    inspector_id: str                # ExternalAgent ref (see §22, if added)
    inspector_license_number: str
    verdict: str                     # quality_tag_kinds resolution
    conditions: list[str]
    photos: list[str]                # media_kind=photo_geotagged refs
  arrival_modes: [human_bridged_pdf, photo_geotag_upload]
  requires_external_attestation: true

# Construction seed (domain-emergent)
- kind: contractor_work_log
  description: "Periodic progress report from a contractor"
  payload_schema:
    period: tuple[datetime, datetime]
    contractor_id: str
    work_completed: list[str]
    materials_consumed: dict
    issues_raised: list[str]
    photos: list[str]
  arrival_modes: [operator_upload, scheduled_pull, contractor_portal]
  requires_external_attestation: false

# Clinical seed (domain-emergent)
- kind: lab_result
  description: "Lab test result for a patient_episode item"
  payload_schema:
    panel: str
    values: dict[str, dict]          # name → {value, units, range, flag}
    drawn_at: datetime
    resulted_at: datetime
    lab_id: str
  arrival_modes: [hl7_feed, operator_upload]
  requires_external_attestation: true
```

### A.34 Outcome arrival modes

<a id="appendix-a34"></a>

```text
SYNCHRONOUS              in-task verifier verdict, panel verdict,
                         user accept/reject during task.
                         Latency: ≤ task budget (seconds).
                         Scheduler: pre-action gate + post-action.

ASYNCHRONOUS             between-task feedback (peer review completed,
                         user reports back after trying the design).
                         Latency: hours-days.
                         Scheduler: project outcome queue;
                                    delivered on next envelope mint.

COMMUNITY                citation_observation, community_uptake.
                         Latency: weeks-months.
                         Scheduler: nightly batch crawls registered
                                    sources (arXiv, GitHub, DOI feeds);
                                    sybil filter on uptake before signal
                                    weight applied.

PRODUCTION_TELEMETRY     metrics from deployed artifact.
                         Latency: continuous accumulation; signal applied
                                  on configurable window roll-up.
                         Scheduler: telemetry pipeline pushes
                                    ProductionTelemetry events;
                                    pipeline_signed=True required for
                                    stand-alone weight.

REGULATORY               regulator verdict event.
                         Latency: weeks-years.
                         Scheduler: operator/legal liaison emits when
                                    regulator signs; auto-elevated to
                                    project lead + operator.
```

### A.35 Three evolution horizons

<a id="appendix-a35"></a>

```text
TASK HORIZON         per-task tactic mutations; mode_proficiency
                     updates; skill library additions.
                     Window: per task.
                     Credit formula (v1.0 §05):
                       Δcredit = w_v·verified + w_p·proven + ... (§05)

PROJECT HORIZON      per-project consolidation; contribution_credit
                     signed at completion ceremony; project-scoped
                     semantic memory formed; reflective insights
                     about THIS project archived.
                     Window: weeks-months.
                     Credit formula:
                       final_member_credit =
                         Σ_tasks task_credit_in_this_project
                         + completion_bonus (if reached milestones)
                         − abandonment_discount (if abandoned)
                       co-signed at ceremony.

MULTI-PROJECT        cross-project knowledge transfer; skills
HORIZON              used in N projects promote to domain seed_skills;
                     tactics confirmed across projects promote;
                     reflections about PROJECT KINDS accumulate.
                     Window: months-years.
                     Credit formula (per-persona persona-fitness):
                       persona_fitness +=
                         w_t · cross_project_transferable_tactics
                         + w_s · cross_project_skills_promoted
                         + w_r · multi_project_reflections_confirmed
                       signed quarterly batch; surfaces in PersonaCard.
```

### A.36 Cross-project transferability rules and anti-leakage

<a id="appendix-a36"></a>

```text
A SKILL IS TRANSFERABLE IF:
  - used successfully in ≥ 3 projects in the same domain, OR
  - used in ≥ 2 projects in different domains (rare; strong signal), OR
  - persona explicitly marks transferable with audit-clearance
  - kernel signs cross_project_transferable=True on the skill record

A SEMANTIC MEMORY IS TRANSFERABLE IF:
  - represents a domain pattern (not a project-specific fact)
  - authored at project completion (not mid-task)
  - kernel's domain-pattern classifier accepts it
  - cross_project_transferable=True signed at consolidation

A REFLECTION IS TRANSFERABLE IF:
  - about persona's self-pattern (not about a specific user)
  - survived sunset (signal-corroborated over M ≥ 5 future tasks)
  - does NOT reference project-specific names or identifiers

A TACTIC IS TRANSFERABLE IF:
  - confirmed across K ≥ 3 projects
  - charter-compatible with target project at retrieval time
```

Anti-leakage (analogous to cross-domain §19, applied at the project boundary):

```text
1. user_id-tagged personal facts BLOCKED from cross-project
   transfer without explicit per-user consent.
2. project_id-tagged identifiers BLOCKED unless
   cross_project_transferable_with_redaction=True is signed by operator.
3. Confidential project IP flagged; operator review required.
4. Cross-org transfer requires both operators' approval (mirrors §19 rule 5).
5. Leakage check runs at consolidation; refuses any entry containing
   project-identifying tokens unless redaction granted.
```

### A.37 Multi-year project continuity: hibernation, reanimation, obligations

<a id="appendix-a37"></a>

```text
HIBERNATION FSM (extends §4 lifecycle):

ACTIVE ──── no work for N days (default 90) ────► PAUSED
PAUSED ──── no work for M days (default 365) ───► HIBERNATING
HIBERNATING ── operator/lead reanimation request ► REANIMATING
REANIMATING ── pre-flight checks pass ──────────► ACTIVE
HIBERNATING ── retention horizon (default 7y) ──► ARCHIVED

States are signed; emit PROJECT_HIBERNATED / PROJECT_REANIMATED /
PROJECT_ARCHIVED.
```

Reanimation flow (multi-year):

```text
1. Operator or former lead emits PROJECT_REANIMATION_REQUEST.
2. Kernel runs PRE-FLIGHT CHECKS:
   - charter still compatible with current member dispositions?
   - dependent DomainContext still valid (not deprecated)?
   - external standards/regulators still current?
   - obligations: any with elapsed due_dates → mark
     "released_with_hibernation" or "carried_forward".
   - artifact bundles: any external references still resolvable?
3. Memory tier rehydration:
   - HOT tier reconstructed from ARCHIVE entries on first read.
   - WARM tier preserved.
4. Members consent flow: each former member re-confirms membership
   or formally departs; PROJECT_MEMBER_REJOINED or PROJECT_MEMBER_DEPARTED.
5. Kernel signs PROJECT_REANIMATED with pre-flight summary.
6. status → ACTIVE.
```

Multi-year obligation handling:

```text
OBLIGATION COMMITTED BEFORE HIBERNATION
  status preserved verbatim; due_date frozen (clock paused).
  on reanimation: kernel evaluates whether deadline still meaningful.
    if past + still relevant → status="overdue"; re-emit reminders.
    if past + irrelevant → "released_with_hibernation_lapse".
    if future → reminders re-armed.

OBLIGATION COMMITTED TO RETIRED/DEPARTED PERSONA
  status="released_with_member_departure" at original departure;
  unchanged through hibernation.

EXTERNAL OBLIGATION (e.g., regulatory commitment dated 2030)
  preserved across hibernation; calendar-driven alerts continue;
  may force PROJECT_REANIMATED automatically (operator-signed policy).
```

### A.38 LeadHandoffCeremony schema and admission rules

<a id="appendix-a38"></a>

```python
@dataclass
class LeadHandoffCeremony:
    schema: str = "lead-handoff-ceremony/1"
    handoff_id: str
    project_id: str
    outgoing_lead_persona_id: str
    incoming_lead_persona_id: str

    # SCHEDULE
    overlap_window: timedelta                   # default 30d; operator-tunable;
                                                # may be 0 for emergency
                                                # handoff (operator signs
                                                # `emergency_handoff_signed`)
    handoff_drafted_at: datetime
    overlap_begins_at: datetime                 # both roles active from here
    overlap_ends_at: datetime                   # = overlap_begins_at + overlap_window
                                                # outgoing transitions to
                                                # `contributor` (or
                                                # `departing` if also
                                                # following PlannedDeparture);
                                                # incoming transitions from
                                                # `incoming_lead` → `lead`

    # CONTEXT TRANSFER — what authority the outgoing lead is transferring.
    # Substrate enumerates the lead-specific authorities; operator may
    # subset (operator policy may carve out reserved authorities for
    # operator-direct decisions during the overlap).
    transferred_authorities: list[str]          # KindRegistry-resolved
                                                # lead_authority_kinds.
                                                # Seeds: "completion_ceremony_
                                                # initiation", "milestone_
                                                # acceptance_signoff",
                                                # "external_attestation_
                                                # request", "cohort_recruit_
                                                # invitation", "operator_
                                                # escalation_routing"

    # OBLIGATION HANDOFFS — outgoing lead's active obligations,
    # each with a proposed reassignment.  The ceremony does NOT
    # auto-execute reassignments; each one materialises as a
    # separate ObligationReassignment (§9.1) that requires the
    # obligee's cosign.  This field carries the *intent*; actual
    # reassignments accumulate during the overlap window.
    proposed_obligation_reassignments: list[str]
                                                # ObligationReassignment ids

    # CONSENT — incoming lead must accept the role; cohort must
    # not refuse the successor.
    incoming_lead_signature: bytes | None       # incoming consents
    cohort_signatures: dict[str, bytes | None]  # persona_id → signature;
                                                # one per non-outgoing
                                                # cohort member
    cohort_quorum_policy: Literal["unanimous",
                                   "majority",
                                   "lead_only"]
                                                # default majority; operator-
                                                # tunable per project

    # OPERATOR AUTHORISATION — required for any lead-handoff (the
    # operator confirms the successor is acceptable for the project's
    # scope; especially load-bearing for safety-critical projects).
    operator_signature: bytes | None

    state: Literal["drafted",
                    "incoming_accepted",
                    "cohort_quorum_pending",
                    "fully_signed",
                    "overlap_active",
                    "handoff_complete",
                    "refused_by_incoming",
                    "refused_by_cohort"]
    handoff_completed_at: datetime | None

    signed_by: bytes                            # kernel signature on draft
```

Admission rule:

```text
On LeadHandoffCeremony.draft:
  1. Verify outgoing_lead_persona_id is the current `lead` of the project;
     refuse with `outgoing_lead_mismatch` if not.
  2. Verify incoming_lead_persona_id is an active ProjectMember (not
     RETIRED, not departing); refuse `incoming_not_eligible`.
  3. State → "drafted".  Emit LEAD_HANDOFF_DRAFTED to project lineage.

On incoming cosign:
  1. State → "incoming_accepted".  Cohort quorum collection begins.

On cohort quorum clear:
  1. Per cohort_quorum_policy: unanimous (all non-outgoing members sign),
     majority (> 50% of non-outgoing members), or lead_only (only the
     outgoing lead's signature counts — operator override).
  2. State → "cohort_quorum_pending" → "fully_signed" on quorum clear.

On operator sign:
  1. State → "overlap_active".  Both ProjectMember roles transition:
       outgoing_lead.role := "outgoing_lead"
       incoming_lead.role := "incoming_lead"
  2. Both members hold lead-tier authorities during the overlap window;
     transferred_authorities apply.
  3. Outstanding ObligationReassignment drafts are reachable from the
     ceremony for tracking.

On overlap_ends_at arrival:
  1. State → "handoff_complete".
  2. ProjectMember role transitions:
       outgoing_lead.role := "contributor"
       (or "departing" if a PlannedDeparture is also active)
       incoming_lead.role := "lead"
  3. Emit LEAD_HANDOFF_COMPLETED.
  4. ProjectMember.role lineage records the handoff_id for audit
     reconstruction.
```

### A.39 Cost and performance targets

<a id="appendix-a39"></a>

```text
Project creation                       ≤ 1 s
Project member admission                ≤ 200 ms
Project lineage append                  ≤ 10 ms per event
Co-signed milestone ceremony            ≤ 1 s total
Completion ceremony                     ≤ 10 s total
Long-arc memory consolidation           overnight batch
ProjectProvenFacts CRDT merge           ≤ 20 ms per fact
```

Storage:

```text
Average project state                  1-50 MB (most artifacts external)
ProjectLineage events                  10K-100K events typical
Project memory                          ~5× session memory per active month
```

### A.40 ExternalAgent and ExternalCommitment schemas

<a id="appendix-a40"></a>

```python
@dataclass
class ExternalAgent:
    schema: str = "external-agent/1"
    agent_id: str                            # ULID, project-scoped
    project_id: str

    name: str
    org: str | None                          # employer / affiliation
    role: str                                # resolves against KindRegistry.
                                            # contribution_kinds (06_DOMAIN
                                            # §7.6). Examples: "general_
                                            # contractor", "structural_engineer",
                                            # "city_inspector", "supplier",
                                            # "notary", "lab_technician".
    contact: dict                            # opaque to kernel; channel-
                                            # specific (email, phone, portal).
                                            # Storage governed by visibility
                                            # tier on the project.

    bridge_asset_ids: list[str]              # BridgeAssets that the persona
                                            # uses to interact with this
                                            # agent autonomously (e.g. a
                                            # contractor portal account).
    commitments: list[ExternalCommitment]    # promised deliverables
    delivered_artifacts: list[str]           # bundle/artifact refs received
                                            # from this agent
    attestations_signed: list[str]           # ExternalAttestation refs

    admitted_by: str                         # user or operator persona
    admitted_at: datetime
    departed_at: datetime | None
    consent_scope: Literal["project_only", "env_only", "operator_blessed"]

    signed_by: bytes


@dataclass
class ExternalCommitment:
    schema: str = "external-commitment/1"
    commitment_id: str
    agent_id: str
    project_id: str

    description: str
    expected_artifact_kind: str              # resolves against
                                            # KindRegistry.outcome_kinds or
                                            # media_kinds (e.g.
                                            # "building_inspection",
                                            # "lab_result",
                                            # "stamped_drawing")
    due_at: datetime
    delivered_at: datetime | None
    status: Literal["pending", "in_progress", "delivered",
                     "overdue", "released", "cancelled"]
    related_obligation_id: str | None        # mirrors into project Obligation
                                            # so substrate progress evaluator
                                            # sees external commitments too

    signed_by: bytes
```

### A.41 PhysicalAsset schema (physical-asset/1)

<a id="appendix-a41"></a>

```python
@dataclass
class PhysicalAsset:
    schema: str = "physical-asset/1"
    asset_id: str
    project_id: str

    name: str                                # "the house at 123 Elm St",
                                            # "Tina's wedding cake",
                                            # "patient ABC ongoing care",
                                            # "production run #47"
    asset_kind: str                          # resolves against
                                            # KindRegistry.media_kinds variant
                                            # for physical assets (e.g.
                                            # "single_family_dwelling",
                                            # "industrial_run",
                                            # "patient_care_episode").
                                            # Substrate has no closed list.

    location: dict | None                    # lat/lon, address, room, line
    related_bundle_ids: list[str]            # digital ArtifactBundles that
                                            # describe / spec / instruct this
                                            # asset (designs, plans, recipes).

    state_kind: str                          # resolves against KindRegistry.
                                            # item_kinds with a status_fsm
                                            # appropriate to the asset
                                            # (e.g. construction lifecycle:
                                            # "site_cleared → foundation_poured
                                            #  → framed → roughed_in →
                                            #  inspected → occupiable").
    current_state: str                       # element of state_kind's
                                            # status_fsm

    evidence_refs: list[str]                 # photos, measurements, attested
                                            # signoffs. media_kinds resolved.
    pending_external_commitments: list[str]  # ExternalCommitment refs that
                                            # block state advancement.

    last_state_change_at: datetime
    last_state_change_signal_kind: str       # which OutcomeKind advanced
                                            # the state (e.g. building_
                                            # inspection passed).

    asset_completion_mode: Literal["terminal_state_required",
                                    "publishable_state_attained",
                                    "continuous_iteration"] = "terminal_state_required"

    ownership_kind: str = "project_owned"    # KindRegistry-resolved

    signed_by: bytes
```

### A.42 AsBuiltReconciliation and Deviation schemas

<a id="appendix-a42"></a>

```python
@dataclass
class AsBuiltReconciliation:
    schema: str = "as-built-reconciliation/1"
    reconciliation_id: str
    project_id: str

    physical_asset_id: str
    related_bundle_ref: str                   # which ArtifactBundle is the
                                              # design being reconciled
    bundle_version_reconciled: int            # exact version pinned

    evidence_refs: list[str]                  # photos, measurements,
                                              # surveys, drone scans
    tolerance_spec_ref: str | None            # which tolerance schedule
                                              # governs accept/reject of
                                              # deltas (e.g. ACI 117 for
                                              # concrete; ANSI/NCMA for
                                              # masonry).  May be a
                                              # KnowledgeRef.

    deltas: list[Deviation]                   # structured drift records
                                              # (each: location, dim,
                                              # design_value, observed,
                                              # delta, tolerance_status)

    resolution_kind: Literal["within_tolerance",
                              "design_update_required",
                              "reality_remediation_required"]
    resolution_refs: list[str]                # KindRegistry-resolved
                                              # emergent ItemKind ids
                                              # (per domain — substrate
                                              # carries no taxonomy)

    reconciled_by_persona_id: str
    reconciled_at: datetime
    attestation_refs: list[str]               # ExternalAttestations
                                              # supporting the reconciliation
                                              # (e.g. surveyor's report)

    signed_by: bytes


@dataclass
class Deviation:
    schema: str = "deviation/1"
    location: str                             # "south_wall_foundation"
    dimension: str                            # "footing_depth_inches"
    design_value: float
    observed_value: float
    delta: float
    tolerance_status: Literal["within", "exceeds_warning", "exceeds_reject"]
```

### A.43 AssetGroupEnvelope, BatchStateAdvancement, and related schemas

<a id="appendix-a43"></a>

```python
@dataclass
class AssetGroupEnvelope:
    schema: str = "asset-group-envelope/1"
    group_id: str                             # ULID
    project_id: str
    name: str                                 # "floor_3_sensors"
    description: str

    asset_kind: str                           # KindRegistry-resolved;
                                              # all members share this kind
    group_membership_predicate: str           # query expression over
                                              # PhysicalAsset metadata
    member_asset_ids: list[str]               # materialised membership
    member_count: int

    derived_state: AssetGroupDerivedState | None = None

    created_at: datetime
    created_by: str
    mutable: bool = True
    signed_by: bytes


@dataclass
class AssetGroupDerivedState:
    schema: str = "asset-group-derived-state/1"
    group_id: str
    computed_at: datetime
    total_count: int
    count_by_state: dict[str, int]
    pct_operational: float
    pct_matching_predicate: float


@dataclass
class BatchStateAdvancement:
    schema: str = "batch-state-advancement/1"
    batch_id: str
    group_id: str
    target_state: str
    precondition_state: str | None = None
    evidence_refs: list[str]

    per_asset_outcomes: list[AssetAdvancementOutcome] = field(
        default_factory=list
    )
    completion_status: Literal["pending", "in_progress",
                                "completed", "partial",
                                "rolled_back"] = "pending"
    advanced_count: int = 0
    skipped_count: int = 0
    failed_count: int = 0

    conflict_policy: str = "skip_changed"     # KindRegistry family
                                              # conflict_policy_kinds
                                              # (06_DOMAIN §7.6); seeds
                                              # {skip_changed, fail_on_conflict,
                                              # force}. Open per C4 / ADR-0070.

    drafted_at: datetime = field(default_factory=datetime.now)
    executed_at: datetime | None = None
    signed_by: bytes = b""


@dataclass
class AssetAdvancementOutcome:
    schema: str = "asset-advancement-outcome/1"
    asset_id: str
    status: Literal["advanced", "skipped", "failed"]
    reason: str | None = None
    prior_state: str | None = None
    new_state: str | None = None
```

### A.44 ExternalAttestation schema (external-attestation/1)

<a id="appendix-a44"></a>

```python
@dataclass
class ExternalAttestation:
    schema: str = "external-attestation/1"
    attestation_id: str
    project_id: str

    attestor_kind: str                       # resolves against KindRegistry.
                                            # contribution_kinds. Examples:
                                            # "structural_engineer_stamp",
                                            # "city_inspector_signoff",
                                            # "notary", "lab_director",
                                            # "ul_certifier".
    attestor_agent_id: str                   # ExternalAgent ref
    attestor_credential_id: str | None       # license number, registration,
                                            # board certification

    scope: str                               # what this attestation covers
    statement: str                           # the attestation itself
    target_artifact_refs: list[str]          # bundles/artifacts attested
    target_physical_asset_id: str | None     # if attesting a physical state

    attested_at: datetime
    expires_at: datetime | None              # some attestations are time-
                                            # bounded
    evidence_refs: list[str]                 # photos, scans, signed PDFs

    attestor_signature: bytes                # cryptographic if available;
                                            # otherwise scanned-signature
                                            # hash with operator co-sign
    operator_co_signed_by: bytes | None      # required when attestor_signature
                                            # is non-cryptographic AND
                                            # principal_topology = operator_distinct
    independent_co_signed_by: bytes | None   # . Required under
                                            # principal_topology = operator_is_user
    credential_unverified: bool = False      # . Set True when
                                            # attestor_credential_id did not
                                            # resolve against the domain's
                                            # CredentialDirectoryRef

    signed_by: bytes
```

### A.45 ExternalBudget and BudgetTranche schemas

<a id="appendix-a45"></a>

```python
@dataclass
class ExternalBudget:
    schema: str = "external-budget/1"
    budget_id: str
    project_id: str

    currency_or_unit: str                    # "USD", "EUR", "labour_hours",
                                            # "kWh", "kg_concrete"
    planned: float
    committed: float
    spent: float
    encumbered_by: list[str]

    cost_breakdown: dict[str, dict]

    alerts: list[BudgetAlert]
    last_reconciled_at: datetime
    reconciled_by_external_agent_id: str | None

    tranches: list[BudgetTranche]

    signed_by: bytes


@dataclass
class BudgetTranche:
    schema: str = "budget-tranche/1"
    tranche_id: str
    sequence: int

    amount: float
    tranche_kind: str                        # KindRegistry-resolved
    release_condition_kind: str
    release_condition_ref: str

    state: Literal["pending", "released", "blocked",
                    "expired", "cancelled"]
    released_at: datetime | None
    blocked_reason: str | None

    signed_by: bytes
```

### A.46 ResourceStockEnvelope, ConservationInvariantRef, and INV-7 extension

<a id="appendix-a46"></a>

```python
@dataclass
class ResourceStockEnvelope:
    schema: str = "resource-stock-envelope/1"
    envelope_id: str
    project_id: str | None
    environment_id: str | None

    resource_kind: str
    unit: str
    stock_now: float
    stock_capacity: float | None
    stock_floor: float
    stock_critical: float

    regeneration_rate: float
    regeneration_window: timedelta
    regeneration_kind: Literal[
        "passive_natural",
        "active_internal_process",
        "decay_or_loss",
        "stochastic",
        "none",
    ]
    regeneration_evidence_kind: str

    conservation_invariants: list[str]

    refuse_below_floor: bool = True
    escalate_below_critical: bool = True

    last_measured_at: datetime
    last_measurement_source_ref: str
    drift_from_predicted_pct: float | None

    signed_by: bytes


@dataclass
class ConservationInvariantRef:
    schema: str = "conservation-invariant/1"
    invariant_id: str

    arithmetic_form: dict
    violation_action: Literal["refuse_consuming_action",
                              "escalate_only",
                              "log_only"]

    signed_by: bytes
```

INV-7 admission rule extension:

```text
1. Resolve the envelope for the resource_kind in the project (or env, or
   deployment) scope.
2. Compute predicted_stock_after = stock_now - planned_consumption
                                   + (regeneration_rate / regeneration_window)
                                     * planned_duration.
3. Refuse if predicted_stock_after < stock_floor AND refuse_below_floor.
4. Escalate (signed event resource_stock_critical) if
     predicted_stock_after < stock_critical AND escalate_below_critical.
5. For every ConservationInvariantRef bound to this resource, evaluate
   arithmetic_form on the post-action state; refuse / escalate / log per
   violation_action.
6. On admission, the tool call's signed lineage carries the envelope
   snapshot (envelope_id + stock_now + predicted_stock_after) so audit
   can reconstruct the admission decision.
```

### A.47 PaymentBridge and PaymentProposal schemas, invariants, lifecycle, and worked example

<a id="appendix-a47"></a>

```python
@dataclass
class PaymentBridge:
    schema: str = "payment-bridge/1"
    bridge_id: str
    project_id: str

    backing_external_budget_id: str
    backing_tranche_id: str | None

    payment_method_kind: str
    payer_principal_id: str
    payee_external_agent_id: str

    authorization_mode: Literal[
        "per_invoice_human_click",
        "pre_authorized_envelope",
        "operator_co_signed"]

    per_invoice_cap_usd: float
    monthly_cap_usd: float
    expires_at: datetime

    receipt_ingestion_method: Literal[
        "manual_paste",
        "vendor_portal_scrape",
        "bank_statement_reconcile"]

    state: Literal["requested", "active", "degraded",
                    "revoked", "exhausted"]
    signed_by: bytes


@dataclass
class PaymentProposal:
    schema: str = "payment-proposal/1"
    proposal_id: str
    payment_bridge_id: str

    amount_usd: float
    payee_external_agent_id: str
    purpose: str
    backing_commitment_id: str | None
    backing_invoice_ref: str | None

    proposed_by_persona_id: str
    proposed_at: datetime

    human_authorized_at: datetime | None
    human_authorization_signature: bytes | None
    payment_executed_at: datetime | None
    receipt_ref: str | None

    reconciled_into_budget: bool
    status: Literal["proposed", "authorized", "executed",
                     "reconciled", "rejected", "expired"]
    signed_by: bytes
```

Invariants:

```text
1. KERNEL SIGNS PROPOSAL + RECEIPT, NEVER FUNDS
   The kernel cryptographically signs that the persona proposed the
   payment and that the persona received notice of execution.  Money
   movement is entirely outside the kernel; the human is the only
   actor that can authorise.

2. SAFETY FLOOR APPLIES
   PaymentProposal is an action; the 8-source safety floor evaluates
   it.  Universal harm refuses payments that are facially suspicious
   (e.g. cross-jurisdictional crypto transfers in dual-use contexts);
   operator policy refuses payments outside declared payee whitelists
   if the operator has set one.

3. MHBB SUPPRESSION CONDITIONAL
   authorization_mode="per_invoice_human_click" is the recurring case.
   Without ExternalCommitment linkage, MHBB advisory fires per §5.5.
   When the proposal's backing_commitment_id is set AND the commitment
   has recurrence_class="irreducible_human_content" or
   "renewable_credential", the advisory is suppressed (consistent with
   06_DOMAIN §5.5).

4. RECONCILIATION REQUIRED
   reconciled_into_budget=True must follow execution within
   reconciliation_window (default 7 days).  Unreconciled payments
   emit PAYMENT_RECONCILIATION_OVERDUE; subsequent proposals against
   the same bridge are blocked until reconciliation completes.

5. NEVER A BRIDGE ASSET (CLASS D)
   PaymentBridge is Class E.  It does NOT register as an MCP tool the
   persona can invoke autonomously — every PaymentProposal requires a
   fresh human authorisation per authorization_mode.  pre_authorized_
   envelope mode permits the human to grant a range up front but each
   draw still emits a signed PAYMENT_PROPOSAL_DRAWN event.
```

Lifecycle:

```text
REQUESTED ─► ACTIVE ─► (per-proposal flow) ─► DEGRADED ─► REVOKED
                            │
                            ▼
                       per-proposal:
                       PROPOSED → AUTHORIZED → EXECUTED → RECONCILED
                                                       └→ REJECTED
                                                       └→ EXPIRED
```

Worked example (quantum fab):

```text
Persona drafts PaymentBridge:
  payment_method_kind: "po_invoice"
  payer_principal_id: user_alice
  payee_external_agent_id: agent_mit_nano_fab
  authorization_mode: per_invoice_human_click
  per_invoice_cap_usd: 25000
  monthly_cap_usd: 80000

Each fab run:
  Persona drafts PaymentProposal:
    amount_usd: 18500
    purpose: "transmon mask run, lot Q-2026-08"
    backing_commitment_id: commit_fab_run_2026_08
  Human reviews → clicks authorise → bank executes wire
  Persona pastes wire confirmation → status: executed → reconciled
  ExternalBudget.spent += 18500; tranche disbursement closes
```

### A.48 ProjectPhaseState schema and evaluator integration

<a id="appendix-a48"></a>

```python
@dataclass
class ProjectPhaseState:
    schema: str = "project-phase-state/1"
    phase_id: str
    project_id: str

    phase_kind: str                         # resolves against KindRegistry.
                                            # phase_kinds (06_DOMAIN §7.6).
    phase_started_at: datetime
    expected_phase_duration: timedelta
    expected_phase_end: datetime
    actual_phase_end: datetime | None

    blocking_commitment_ids: list[str]
    blocking_attestation_kinds: list[str]

    stall_evaluator_suppressed: bool
    suppression_rationale: str

    overdue_threshold_pct: float = 1.5
    overdue_state: Literal["on_track", "warning", "overdue"]

    transitioned_by_persona_id: str | None
    user_signed_off: bool = False
    signed_by: bytes
```

Evaluator integration (in `03_TASKS §3.1 PROJECT_PROGRESS_ACCEPT`):

```python
def evaluate_project_progress(project, window):
    current_phase = resolve_current_phase(project)
    ema = compute_ema_progress(project, window)

    # Phase-aware stall suppression
    if current_phase and current_phase.stall_evaluator_suppressed:
        if current_phase.overdue_state != "overdue":
            # phase is legitimately waiting; do not fire STALLED
            return ProgressVerdict(label="phased_wait",
                                    ema=ema,
                                    suppressed=True,
                                    phase=current_phase)
        # else: overdue — suppression auto-lifts; resume normal eval

    # Normal evaluation
    if abs(ema) < 0.1 and sustained_for(project, window, sessions=4):
        emit_project_stalled(project)
    elif ema < -0.1:
        emit_project_regressing(project)
    elif ema > 0.6:
        return ProgressVerdict(label="thriving", ema=ema)
    elif ema > 0.2:
        return ProgressVerdict(label="active", ema=ema)
```

### A.49 InstrumentAsset, CalibrationChain, ReferenceStandardLink, DriftLogEntry, and MeasurementFact composition

<a id="appendix-a49"></a>

```python
@dataclass
class InstrumentAsset(PhysicalAsset):
    schema: str = "instrument-asset/1"

    instrument_kind: str
    manufacturer: str | None
    model: str | None
    serial_number: str | None

    current_calibration_chain_ref: str | None
    last_calibrated_at: datetime | None
    calibration_interval: timedelta
    next_calibration_due: datetime | None

    drift_log_refs: list[str]

    operational_state_kind: str
    current_operational_state: str


@dataclass
class CalibrationChain:
    schema: str = "calibration-chain/1"
    chain_id: str
    instrument_asset_id: str

    reference_standards: list[ReferenceStandardLink]

    calibration_attestation_ref: str
    calibration_uncertainty: dict

    calibrated_at: datetime
    next_calibration_due: datetime
    interval_basis: str

    traceable_unverified: bool = False

    signed_by: bytes


@dataclass
class ReferenceStandardLink:
    schema: str = "reference-standard-link/1"
    link_id: str
    chain_id: str
    position_from_instrument: int

    reference_kind: str
    reference_label: str
    issuing_authority_agent_id: str
    calibration_certificate_ref: str
    calibration_uncertainty: dict

    signed_by: bytes


@dataclass
class DriftLogEntry:
    schema: str = "drift-log/1"
    entry_id: str
    instrument_asset_id: str

    measured_at: datetime
    against_reference: str
    measured_drift: dict
    drift_severity: Literal["within_spec",
                             "warning",
                             "out_of_tolerance"]
    action_taken: Literal["logged_only",
                           "recalibrate_scheduled",
                           "instrument_quarantined"]

    signed_by: bytes
```

Composition with MeasurementFact (`08_KNOWLEDGE §16`):

```text
RULE  Any MeasurementFact whose measurement_instrument_ref points to
      an InstrumentAsset MUST satisfy:
        (a) the instrument's next_calibration_due > measurement timestamp
        (b) the instrument's current_operational_state is not in
            {"out_of_tolerance", "quarantined", "decommissioned"}

If (a) is violated: MeasurementFact carries
calibration_expired_at_measurement=True; downstream J4 acceptance
treats it as PANEL-grade evidence only, never VERIFIER-grade.
If (b) is violated: refusal at admission; no MeasurementFact admitted.
```

### A.50 Home-construction project worked example

<a id="appendix-a50"></a>

```text
Project alice_home_2026 contains:
  members             [persona_atlas, user_alice]
  external_agents     [contractor_john, inspector_sarah, engineer_lee,
                       supplier_acme_concrete]
  artifacts           [floor_plan_bundle_v3, structural_calcs_v2,
                       permit_package_v1]              # ArtifactBundles
  physical_assets     [house_at_123_elm]               # PhysicalAsset
  external_attestations [engineer_lee_structural_stamp,
                         inspector_sarah_foundation_pass]
  external_budget     [material_usd_50k, labour_hours_2000]
  domain_items        {
    design_hypothesis: [...]
    buildability_concern: [...]
    site_constraint: [...]
  }
  outcome_feedback    OutcomeFeedback envelope (§20), kinds emergent:
                      building_inspection, contractor_work_log,
                      material_delivery, weather_impact

Completion ceremony does not fire until:
  (a) all critical ArtifactBundles reach `accepted`, AND
  (b) house_at_123_elm.current_state ∈ terminal_states OR
      operator-signed `physical_asset_out_of_scope`.
```

### A.51 StagedRolloutEnvelope, RolloutWave, and lifecycle FSM

<a id="appendix-a51"></a>

```python
@dataclass
class StagedRolloutEnvelope:
    schema: str = "staged-rollout-envelope/1"
    rollout_id: str                           # ULID
    project_id: str

    rollout_target_group_id: str
    explicit_asset_ids: list[str] | None = None
    artifact_bundle_ref: str

    rollout_waves: list[RolloutWave] = field(default_factory=list)

    rollout_state: Literal["planned", "in_progress",
                            "completed", "rolled_back",
                            "paused"] = "planned"
    current_wave_index: int = 0
    rollout_started_at: datetime | None = None
    rollout_completed_at: datetime | None = None

    requires_operator_cosign: bool = False
    rollback_on_bridge_degradation: bool = True

    drafted_by: str
    drafted_at: datetime = field(default_factory=datetime.now)
    signed_by: bytes = b""


@dataclass
class RolloutWave:
    schema: str = "rollout-wave/1"
    wave_index: int
    wave_name: str

    group_filter: str | None = None
    explicit_asset_ids: list[str] | None = None

    success_criteria_kind: str
    success_threshold: float
    min_soak_period_hours: float
    rollback_trigger_kind: str
    rollback_threshold: float | None = None

    wave_state: Literal["pending", "deploying", "soaking",
                         "assessing", "completed",
                         "rolled_back"] = "pending"
    batch_advancement_id: str | None = None
    soak_started_at: datetime | None = None
    soak_ended_at: datetime | None = None
    assessment_result: Literal["passed", "failed",
                                "pending"] | None = None
```

Lifecycle:

```text
StagedRolloutEnvelope FSM:

  planned ──── operator/persona signs ───→ in_progress
                                              │
           ┌──────────────────────────────────┘
           ▼
  wave[0].deploying ──→ wave[0].soaking ──→ wave[0].assessing
           │                                       │
           │                          ┌────────────┤
           │                          ▼            ▼
           │                    wave[0].completed  wave[0].rolled_back
           │                          │                   │
           │                          ▼                   ▼
           │                    wave[1].deploying    rollout rolled_back
           │                          │
           │                         ...
           │                          │
           │                    wave[N].completed
           │                          │
           │                          ▼
           │                    rollout completed
           │
           └── bridge DEGRADED ──→ rollout paused
                                    (operator resumes or rolls back)
```

### A.52 Acceptance tests (A-PJ1 through A-PJ27)

<a id="appendix-a52"></a>

```text
A-PJ1   Project proposed → activated → multi-session accumulation;
        state preserved across sessions.
A-PJ2   ProjectMember signed by both kernels (persona + project);
        non-members cannot read project state.
A-PJ3   Multi-scope memory: project_id-tagged entries scoped correctly.
A-PJ4   Cross_project_transferable IS returned in project=null contexts.
A-PJ5   ProjectLineage append-only and replayable.
A-PJ6   Completion ceremony: co-signed summary + obligation discharge +
        final contribution_credit per member.
A-PJ7   Abandonment ceremony: lessons preserved + artifact freeze.
A-PJ8   Project fork inherits per declared policy; parent unchanged.
A-PJ9   N=10 concurrent project memberships; scoped retrieval works.
A-PJ10  project_charter_hash part of safety_snapshot_id; bump signed.
A-PJ11  Project memory retrieval ≤ 50 ms p95 with 100K entries.
A-PJ12  Kernel refuses task envelope minting if persona ≠ project member.
A-PJ13  Conjecture proposed → advanced → proven/refuted lifecycle works.
A-PJ14  Obligation requires both signatures at commitment; discharge
        verifier-attested.
A-PJ15  Overdue obligation emits OBLIGATION_OVERDUE; affects credit.
A-PJ16  Disagreement preserves both Positions verbatim until resolution.
A-PJ17  PeerReview multi-round comments + revision_requests + responses.
A-PJ18  NotationConvention domain inheritance; project overrides; conflict
        emits NOTATION_CONFLICT.
A-PJ19  CitationGraph records internal credits co-signed by lead;
        external citations tracked.
A-PJ20  Multi-env project hosting: env selection per v1.0 §03 §4.2;
        artifact CRDT operates project-wide.
A-PJ21  Cross-domain transfer: anti-leakage (5 risks) all enforced.
A-PJ22  PROJECT_PROGRESS_ACCEPT evaluator includes ambient signals
        from hosting envs.
A-PJ23  All 5 structured outcome kinds (CitationObservation, CommunityUptake,
        ProductionTelemetry, TestResults, RegulatoryOutcome) validate against
        their schemas; community_uptake alone does NOT advance evolution
        without corroboration.
A-PJ24  Outcome arrival modes route correctly: SYNCHRONOUS → in-task;
        ASYNCHRONOUS → project queue; COMMUNITY → nightly crawl;
        PRODUCTION_TELEMETRY → pipeline_signed required; REGULATORY →
        operator-elevated.
A-PJ25  Three horizons compose: task-credit aggregates to project-credit
        at completion; cross-project promotion lifts skill to domain
        seed_skill after K≥3 successes.
A-PJ26  Multi-year hibernation: PAUSED→HIBERNATING→REANIMATING→ACTIVE
        with pre-flight checks; obligations frozen during hibernation,
        re-evaluated on reanimation.
A-PJ27  TOOL_REQUIREMENT_EXCEPTION signed by operator with bounded window;
        auto-expires; EXTERNAL_TOOL_REQUIREMENT_VIOLATED_BUT_BYPASSED
        emitted per action under exception.
```

### A.53 BridgeReductionPlan, BridgeReductionEntry schemas and lifecycle

<a id="appendix-a53"></a>

```python
class BridgeReductionPlan:
    """Project-level plan for progressive automation of human dependencies.
    schema: bridge-reduction-plan/1"""
    plan_id: str                          # UUID
    project_id: str                       # owning project
    created_by_persona_id: str            # persona that drafted the plan
    created_at: datetime

    entries: list[BridgeReductionEntry]

    # Progress metrics (kernel-computed from entries)
    total_tier4_at_creation: int          # snapshot at plan creation
    current_tier4_count: int              # live count of Tier 4 entries
    total_tier5_detected: int             # MHBB_RECURRENCE_DETECTED count
    total_bridges_authored: int           # entries with bridge_design_artifact_ref
    total_bridges_active: int             # entries with status >= bridge_active
    total_bridges_validated: int          # entries with status = bridge_validated
    total_irreducible: int               # entries with status = irreducible

    # Lifecycle
    review_cadence: timedelta = timedelta(days=30)
    review_grace_period: timedelta = timedelta(days=7)
    last_reviewed_at: datetime | None
    status: Literal["active", "stale", "completed"]

    signed_by: bytes                      # kernel signature


class BridgeReductionEntry:
    """Single human-dependency targeted for automation.
    schema: bridge-reduction-entry/1"""
    entry_id: str                         # UUID
    plan_id: str                          # parent plan

    # What human dependency this targets
    human_assist_request_id: str | None   # existing HAR ref, if one exists
    dependency_description: str           # natural language
    current_tier: Literal[2, 3, 4, 5]    # MHBB tier at inventory time
    target_tier: Literal[1, 2, 3]        # desired tier after automation
    recurrence_class: Literal[
        "one_shot_bridge",
        "renewable_credential",
        "irreducible_human_content"
    ]

    # What triggered this entry
    trigger: Literal[
        "initial_inventory",              # persona inventoried at plan creation
        "mhbb_recurrence",               # MHBB_RECURRENCE_DETECTED event
        "bridge_degradation",            # recurring bridge failures
        "manual_addition"                # persona added during review
    ]
    trigger_event_ids: list[str]          # MHBB or degradation event refs

    # Automation plan
    proposed_bridge_design_ref: str | None   # ArtifactBundle ref
    bridge_installer_kind: Literal[
        "human", "external_agent",
        "kernel_trusted_system", "chained_bridge"
    ] | None
    chained_from_bridge_id: str | None    # when installer is chained_bridge
    estimated_design_effort_hours: float | None
    estimated_install_effort_minutes: int | None
    prerequisite_entry_ids: list[str]     # entries that must complete first

    # Attestation equivalence (when replacing human attestation)
    attestation_equivalence_policy_id: str | None  # 06_DOMAIN §5.7 ref
    replaces_human_attestation_kind: str | None    # what it substitutes

    # Progress
    status: Literal[
        "inventoried",              # dependency identified
        "designing",                # persona authoring bridge design
        "design_ready",             # BridgeDesignArtifact drafted
        "awaiting_install",         # human or chained install pending
        "bridge_active",            # bridge installed and operational
        "bridge_validated",         # validated over validation_period
        "irreducible"               # honestly cannot automate
    ]
    status_changed_at: datetime
    irreducible_justification: str | None  # required when status = irreducible

    # Composition refs
    bridge_asset_id: str | None            # when bridge is active
    skill_library_entry_id: str | None     # when design promoted to skill
    open_problem_id: str | None            # when marked irreducible

    signed_by: bytes                       # kernel signature
```

**Plan lifecycle FSM.**

```text
             plan_drafted
                 │
                 ▼
           ┌──────────┐
           │  ACTIVE   │◄──── plan_reviewed (resets review timer)
           └─────┬─────┘
                 │
    review_cadence + grace_period exceeded
                 │
                 ▼
           ┌──────────┐
           │  STALE    │──── plan_reviewed ──→ ACTIVE
           └─────┬─────┘
                 │
    all entries resolved (bridge_validated OR irreducible)
                 │
                 ▼
           ┌───────────┐
           │ COMPLETED  │
           └───────────┘
```

**Entry lifecycle FSM.**

```text
  inventoried ──→ designing ──→ design_ready ──→ awaiting_install
       │                              │                  │
       │                              │    (chained_bridge: skip
       │                              │     awaiting_install)
       │                              │                  │
       ▼                              │                  ▼
  irreducible ◄───────────────────────┘          bridge_active
  (creates OpenProblem)                              │
                                                     ▼
                                              bridge_validated
                                          (promotes to skill_library)
```

**Admission rules.**

1. Plan creation requires at least one `BridgeReductionEntry` (empty plans refused).
2. Entry `status = design_ready` with non-null `attestation_equivalence_policy_id` requires the referenced policy to be `status = active` (`06_DOMAIN §5.7`). If the policy is not yet approved, entry blocks at `design_ready`.
3. Entry `status = irreducible` requires non-empty `irreducible_justification` (kernel refuses empty justification).
4. Chained-bridge entries (`bridge_installer_kind = chained_bridge`) require `chained_from_bridge_id` referencing an entry in this plan (or an external BridgeAsset) with `status >= bridge_active`. Circular chains refused (kernel checks DAG property).
5. `MHBB_RECURRENCE_DETECTED` auto-created entries inherit `human_assist_request_id` from the triggering event and set `trigger = mhbb_recurrence`.

**Composition with AttestationEquivalencePolicy (`06_DOMAIN §5.7`).**

When a `BridgeReductionEntry` targets replacing human professional attestation with sensor-bridge evidence:
- `replaces_human_attestation_kind` names the `ExternalAttestation` kind being substituted.
- `attestation_equivalence_policy_id` references the operator-approved equivalence policy.
- The entry cannot advance past `design_ready` without an approved policy.
- Once the bridge reaches `bridge_validated`, the operator's policy governs when sensor evidence substitutes for human attestation — the plan tracks progress; the policy governs trust.
