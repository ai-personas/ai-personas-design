---
title: PersonaOS v1.0 — Kernel
status: Stable
---

# 01 — Kernel

> **Reader guide.** The kernel is the trusted core of PersonaOS — the referee that checks every action before it happens. In this document, you'll learn what the kernel guarantees, how the eight safety checks work, how every action is signed and recorded, and how the cryptographic key hierarchy is structured. **Prerequisites:** `00_VISION.md`. **Key terms:** *kernel* = the trusted core that enforces all rules; *safety floor* = 8 layered safety checks (strictest wins); *lineage* = tamper-proof audit trail; *admission gate* = a checkpoint the kernel runs before allowing an action.

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). The kernel implements invariants J1, J2, J3, J4 from [`00_VISION.md §3`](00_VISION.md#3-invariants-j1j9) and INV-1…INV-10 from [`00_VISION.md §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10).

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. This document is **fully normative**: every MUST / MUST NOT / SHALL / REQUIRED keyword in ALL CAPS carries RFC 2119 / RFC 8174 force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174).

**In scope.** The kernel — the deterministic substrate that owns identity (J1), the eight-source safety floor (J3), three-scope append-only lineage (J2 task / J9 env / C1 domain), signing infrastructure (Ed25519 over canonical fields; three custody tiers; scope keys), schema validation (INV-10), sandbox execution, budget admission (INV-7), and OpenTelemetry observability. Also the verified-loop substrate that backs class-routed acceptance (J4) including round invariants INV_R1…INV_R11.

**Out of scope.** Persona internals (see [`02_PERSONA.md`](02_PERSONA.md)); task classification and acceptance pathway selection (see [`03_TASKS.md`](03_TASKS.md)); environment surfaces and presence (see [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md)); domain emergence and promotion (see [`06_DOMAIN.md`](06_DOMAIN.md)); the schema-version registry (see [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry)); the acceptance-test catalogue (see [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md)).

**Supersession.** Subsumes prior kernel design and lineage extensions; J8 retired (project lineage now a documentation filter over `project_workspace`-typed EnvironmentLineage — see [`04_PROJECT.md §0`](04_PROJECT.md#0-status--scope)).

**Structural deviation from `SPEC_CONVENTIONS.md §3.2`.** This document follows the compressed-opening pattern of [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md#33-compressed-opening-permitted): Background, Goals, and Definitions are folded into the body sections (§1 Purpose, §2-§13 mechanism specifications). Terminology cross-links to [`12_GLOSSARY.md`](12_GLOSSARY.md). The three §3.1 bookends (this section, [§12 Risks](#12-risks--known-limitations), [§13a Open questions](#13a-open-questions)) are present.

## 0a. Plain-Language Guide

*Here's how the trusted core of PersonaOS works, explained without jargon. If you read nothing else, read this section.*

**What is the kernel?**

Think of the PersonaOS kernel as a trusted referee at the centre of everything. Every AI Persona (called a "persona") must go through this referee before doing anything. The kernel does not do the creative work itself — personas do that. Its job is to make sure every action is safe, properly signed, and recorded. It owns identity (who is who), enforces the safety rules, signs every change with a digital signature so nothing can be tampered with, and keeps an unbreakable audit trail.

**The safety floor: eight layers of safety checks**

Before any persona can act, the kernel runs the action through eight separate safety checks — like eight security guards who each look for something different. Guard 1 checks for universal harms (things that are never acceptable, like coaching self-harm). Guard 2 checks the persona's founding principles. Guard 3 checks personal boundaries the user has set. Guard 4 enforces the operator's deployment-wide rules. Guard 5 checks domain-specific safety rules (e.g., electrical safety standards). Guard 6 verifies required external tools were called before certain claims. Guard 7 checks novelty claims against prior art. Guard 8 checks the rules of the specific environment. If any guard says no, the action is blocked. The strictest rule always wins.

**How actions get approved: the pre-action gate**

Every action follows the same path. The persona proposes it. The kernel runs all eight checks in parallel. If any check refuses, the action is blocked. If all pass, the action runs inside a secure sandbox (an isolated container that cannot damage the rest of the system). Afterwards, the kernel audits the result and records everything.

**Deployment profiles: who is in charge**

PersonaOS can be set up in different ways. In an enterprise, there is typically a separate operator (the company or admin) who sets the rules, and users who work within them. But sometimes one person is both.

**Principal collapse: when operator and user are the same person**

When one person plays both roles — say, a homeowner planning a renovation — the safety gate requiring a separate operator's approval becomes meaningless. The kernel substitutes a "degraded gate": a 72-hour cooling-off period, an independent third-party review, and a signed acknowledgement that you are approving your own work. This does not eliminate self-approval but prevents unconsidered snap decisions.

**Physical-state rules: extra safety when real things could get hurt**

When an action would affect the physical world in a domain where bodily injury is possible, the kernel requires two things: the design must have passed the full verification process, and an independent credentialed expert must have attested to the physical state. Neither alone is enough — both "the design looks good on paper" and "a qualified person checked the real thing" must hold.

**Safety classifier rotation: swapping out the guards**

Each safety check uses an AI classifier to make its decision. To prevent a persona from learning to fool a specific classifier, the kernel regularly swaps classifiers from a pool of at least three different models — like rotating security guards so nobody learns any one guard's blind spots.

**Replication bounds: limits on self-copying**

Some systems might build more of themselves — a factory that builds factories, or a software agent that spawns copies. Without limits, this could spiral out of control. The kernel enforces hard ceilings on how many copies can exist, how fast they can be created, and how deep the chain can go. These limits sit at the highest safety level and cannot be overridden.

**Distress detection: what happens when a user is in crisis**

If classifiers detect emotional distress in a user's messages — such as suicidal ideation — the system follows a declared routing policy: it can pause normal conversation, surface crisis resources (like a hotline number), notify the operator without sharing raw content, and require a co-signature before resuming. Every deployment must declare its distress-response policy; without one, the system refuses to operate when distress is detected rather than silently ignoring the signal.

**Key custody: how signing and identity work**

Every event and safety decision is signed with a digital signature — like a tamper-proof wax seal. Keys are organised in a hierarchy: a master key at the top, with derived keys for each domain, environment, project, and persona. Keys can be stored at three security levels: laptop (development), cloud key service (production), or hardware security module (medical, financial, or defence deployments). Keys rotate on schedule; compromised keys trigger revocation and re-keying. Historical signatures remain verifiable because old public keys are archived.

**The audit trail (lineage): three scopes**

The kernel maintains three append-only audit trails: one per task (ephemeral), one per environment (persistent), and one per knowledge domain (persistent). Every event lives in exactly one trail; others can point to it but never duplicate it. You can replay any trail to reconstruct exact state at any point in time, and every entry is signed so tampering is detectable.

**The verified loop: how work gets checked**

Every piece of work goes through a four-tier verification cascade: a schema check (is it well-formed?), a sandbox test (does it run correctly?), an invariant check (does it obey domain rules?), and a policy review by a panel. Only work passing all tiers earns "verified" status. The verification models rotate like the safety classifiers, to prevent gaming.


## 1. What the kernel is

The [**PersonaOS kernel**](12_GLOSSARY.md#k) is the small deterministic substrate that owns identity, the [safety floor](12_GLOSSARY.md#s), [lineage](12_GLOSSARY.md#l), signing infrastructure, schema validation, sandbox execution, budget admission, and observability. Bodies (framework adapters) and [personas](12_GLOSSARY.md#p) sit around the kernel; the kernel is the one writer for identity and lineage.

The kernel is deliberately small. Most cognitive work happens in personas. The kernel guarantees the load-bearing claims; the work happens above it.

*The kernel is organised into seven subsystems: identity, safety floor, lineage, acceptance dispatch, substrate services, key custody, and composition.*

**Technical detail:** See [A.1](#appendix-a1).


## 2. The safety floor — 8 sources + 1 advisory

The safety floor is the kernel's most load-bearing responsibility. **No persona action proceeds without floor clearance.**

*Each of the eight refusal sources and two advisory sources is defined with its scope, enforcement mechanism, and override rules.*

**Technical detail:** See [A.2](#appendix-a2).


### 2.1 Composition rule

*The composition function evaluates all eight sources in sequence, collects refusals, and applies most-restrictive-wins.*

**Technical detail:** See [A.3](#appendix-a3).


### 2.2 Precedence rules for explicit conflicts

*Six named rules define which authority wins when two safety sources disagree (e.g., user boundary vs. environment consent, operator policy vs. user consent).*

**Technical detail:** See [A.4](#appendix-a4).


### 2.3 The pre-action gate

Every persona action passes through the safety check **before** reaching the sandbox or the world:

*The gate is a linear pipeline: persona emits a request, the kernel runs the safety check, then sandboxes the action, evaluates the output, audits, and returns the result.*

**Technical detail:** See [A.5](#appendix-a5).


Latency budget: **≤ 400 ms p95 for full 8-source parallel evaluation** (450 ms with advisory).

### 2.4 DeploymentProfile and principal collapse

The 8-source safety floor presupposes a four-party principal topology: persona, user, operator, (and external attestor where physical advancement applies). Single-user deployments (homeowner running PersonaOS to plan a home build; solo researcher; clinical caregiver-as-self) collapse user and operator into one human. RULE C (`operator > user`) and C2 (`safety-critical promotions require operator sign-off`) then degenerate to ceremonial self-approval. v1.0 names this collapse explicitly and substitutes a degraded gate.

*The deployment profile declares the principal topology (who is the operator, who is the user) and is signed at deployment registration.*

**Technical detail:** See [A.6](#appendix-a6).


Declared once at deployment registration; signed; recorded in kernel state. Every signed action carries `principal_topology` inside `safety_snapshot_id` (so audit reflects what gating regime was in effect).

**Degraded gate — `operator_is_user`:**

When `principal_topology = operator_is_user` and an action would normally require operator co-sign (C2 safety-critical promotion; ApprovalWorkflow operator step; safety-critical `ProposedSafetyExtension` approval; physical-state advancement that requires operator co-sign per §2.6), the kernel substitutes:

*Under principal collapse, three conditions substitute for operator co-sign: a 72-hour cool-down, a non-principal external attestation, and a signed acknowledgement.*

**Technical detail:** See [A.7](#appendix-a7).


ALL THREE conditions MUST hold; absence of any one is refusal with `principal_collapse_floor_deficit`.

**Degraded gate — `operator_absent`:**

Safety-critical promotion (C2) is refused outright; the system honestly cannot supply the gate. The deployment is restricted to non-safety-critical work until either an operator is appointed or `principal_topology` is changed.

**Compatibility with v1.0 deployments:**

`DeploymentProfile.principal_topology = operator_distinct` is the default. Existing multi-tenant and operator-deployed PersonaOS installs remain unchanged. Only deployments that explicitly declare `operator_is_user` invoke the degraded gate.

**Honest limit:** the degraded gate raises the cost of unsafe self-approval but does not eliminate it. A determined principal can wait 72h, hire a complicit attestor, and sign the acknowledgement. The system is not adversarially robust against the principal themselves; it is robust against unconsidered self-approval. Operator-distinct topology remains the strong-form recommendation for safety-critical work.

### 2.4.1 FederatedTimeLock — alternative degraded gate (normative)

When `principal_topology = operator_is_user` and the principal cannot reach a non-principal credentialed attestor (frontier domains with no licensing board; principal in geographic isolation; cost prohibitive), the §2.4 attestation-based gate is unreachable in practice. PersonaOS supplies a **second** degraded gate path. The principal picks one; the kernel signs the choice.

**Availability (now normative).** FederatedTimeLock requires ≥ 3 federation peer nodes with `independence_attested = True`. Federation is now a normative part of the global object space (ADR-0067), so this path is **available** wherever the deployment can reach ≥ 3 admissible independent peer nodes (discovered over `09_PROTOCOLS §3G`).

Under `principal_topology = operator_is_user`:
- Path 1 (§2.4 attestation gate) is admissible whenever a non-principal credentialed attestor is reachable.
- Path 2 (FederatedTimeLock) is admissible when ≥ 3 independent peer nodes are reachable to observe the waiting period.
- **When neither is reachable** (a genuinely isolated single node with no peers and no attestor), safety-critical actions **MUST refuse** — the substrate does not manufacture a gate it cannot honestly supply. This is the **V.8 navigated reality**: isolation is a physical condition, not a missing feature; the audit-tag `principal_collapse_no_gate_reachable` records the refusal, and the pre-staged `FederatedTimeLockIntent` activates automatically once peers become reachable.

This is the honest posture: the substrate refuses to ceremonialise the gate beyond what §2.4 / the federated path can truthfully provide.

*The federated time lock allows safety-critical actions to proceed under principal collapse by requiring at least three independent peer kernels to observe a 7-day waiting period with no objections.*

**Technical detail:** See [A.8](#appendix-a8).


**Composition with §2.4:** A safety-critical action under principal collapse is admissible iff EITHER:

*A safety-critical action under principal collapse is admissible via either the attestation-based gate or the federation-based time lock, but not both simultaneously.*

**Technical detail:** See [A.9](#appendix-a9).


The principal selects path; the kernel signs the selection at proposal time. Mid-flight switching is refused — a stalled Path 1 cannot be silently replaced by Path 2 (this prevents the principal from picking whichever path is closer to approval at any moment).

**Why this exists:** Frontier domains (`PeerAttestationPool` per 06_DOMAIN §5.6) have no licensing board; hiring a "credentialed third-party attestor" is impossible because no credential exists. Federation peers attesting through a time-lock substitute structurally — the principal cannot hire all three peers without conspicuous collusion that the lineage records.

**Under `operator_absent`:** Path 2 is also unavailable (no federation registration). Refusal stands.

**Honest limit:** Federation peers can collude. The substrate raises the cost of conspiratorial approval by requiring (a) peer independence_attested, (b) 168h visibility window for any peer to object, (c) signed objections leaving an audit trail. Not state-actor-robust; robust against casual self-approval shortcuts.

### 2.4.2 operator_deferred topology + PolicyEnvelope (C1)

Some deployments have a real operator who **cannot synchronously co-sign**: remote installations behind high-latency links (industrial sites, field sensors), Mars-class light-time round trips, after-hours autonomy with on-call operator paged but unavailable for minutes-to-hours. Treating these as `operator_is_user` would falsely collapse the topology; treating them as `operator_distinct` would deadlock on every C2 gate. v1.0 adds a third path: **pre-approved policy envelope** that admits within declared bounds, with deferred operator counter-sign and a hard quarantine fallback when the budget breaches.

*The policy envelope lets an operator pre-approve certain action types within declared bounds when they cannot co-sign in real time, with a hard quarantine fallback if the operator does not counter-sign within the budget.*

**Technical detail:** See [A.10](#appendix-a10).


**Admission rule.** A safety-critical action under `operator_deferred` topology is admissible iff ALL hold:

*Deferred admission requires the action to fall within the envelope's scope, meet the evidence floor, use a non-expired envelope, and open a deferred-audit slot.*

**Technical detail:** See [A.11](#appendix-a11).


**Counter-sign loop.** The operator (on whatever cadence their connectivity allows) reviews `DeferredAdmission` records and signs counter-sign tokens. Counter-sign updates the admission record (signed event `deferred_admission_countersigned`). Until counter-sign or quarantine, downstream consumers see the output as **provisional** — any further action depending on this output inherits the provisional flag.

**Budget breach.** If `counter_sign_due_by` passes without `operator_counter_sign`:

*When the operator's counter-sign deadline passes, outputs are quarantined, optionally rolled back (digital only), or the operator is paged.*

**Technical detail:** See [A.12](#appendix-a12).


**Composition with §2.4 + §2.4.1.** The four principal topologies select gating regimes orthogonally:

*Each of the four principal topologies maps to a specific gating regime for safety-critical decisions.*

**Technical detail:** See [A.13](#appendix-a13).


A deployment cannot declare two topologies simultaneously. Switching topology requires a signed `principal_topology_change` event in the deployment's lineage; in-flight `DeferredAdmission`s under the previous topology stay live and complete under their original envelope's rules.

**MissionCharter interaction (forward-ref).** `operator_deferred` is the topology under which `MissionCharter` (`02_PERSONA §11.3`) operates: the MissionCharter is itself a long-lived `PolicyEnvelope` whose `permitted_action_kinds` are scoped to charter-internal goal elaboration and whose latency budget is the charter's re-attestation cadence.

**Why this is substrate-shape, not domain.** Every field above is a *topological* concept: latency, evidence floor, envelope expiry, quarantine policy. None branch on domain category. A Mars factory, a remote ocean buoy, a high-frequency sensor array, an after-hours back-office process — they all use the same `PolicyEnvelope` shape with different `permitted_action_kinds` resolved through their per-domain KindRegistry.

**Honest limit.** A malicious operator who pre-authorises an overbroad envelope makes the topology degenerate into "kernel rubber-stamps." v1.0 mitigates with three substrate-shape brakes: (a) `evidence_floor` cannot be lower than the pathway floor for the hazard envelope, (b) `envelope_expires_at` forces re-attestation, (c) `on_budget_breach = quarantine` ensures every deferred admission becomes recoverable on operator default. Operator policy further mitigates by requiring two-person sign-on for envelopes whose hazard ceiling reaches `bodily_injury` or above.

**Acceptance tests.** A-DO1 (envelope admits within bounds), A-DO2 (action outside hazard ceiling refused), A-DO3 (budget breach quarantines + taints downstream), A-DO4 (envelope expiry forces re-attestation), A-DO5 (revoke snaps outstanding admissions to quarantine), A-DO6 (PhysicalAsset advancement cannot use rollback policy).

### 2.4.3 PrincipalAttribution — multi-principal topology

`DeploymentProfile.principal_topology` (§2.4) enumerates the *operator-vs-user* relationship as a 4-value Literal. It does not enumerate **principal cardinality**: every value above assumes *one* operator (or its degraded substitute) per signing decision. A genuinely shared deployment — two organisations forming a joint project on one kernel, two research institutes co-authoring a programme, two product teams ratifying a joint spec — has no honest expression. The substrate forced such deployments to nominate one operator as "the principal" and let the other sign as a non-principal `ExternalAttestation`, which mis-records authority and breaks audit ("which operator authorised this admission?").

`PrincipalAttribution` is a per-env / per-project envelope that binds N principals, each with a weighted cosign quorum role. Single-principal deployments continue unchanged (the flag stays `False`); multi-principal deployments opt in.

*Principal attribution binds multiple operators to an environment or project with weighted co-sign quorum roles, enabling genuinely shared deployments.*

**Technical detail:** See [A.14](#appendix-a14).


**Admission rule.** A `PrincipalAttribution` is admissible iff ALL hold:

*Multi-principal admission requires correct cardinality, consent from every principal, non-degenerate weights, resolved role kinds, and compatible key tiers.*

**Technical detail:** See [A.15](#appendix-a15).


**Composition with the safety floor.**

The `PrincipalAttribution.principals` list does not bypass the §2.4 degraded gate or the §2.5 physical-state composition rule. When a deployment under `principal_topology = operator_distinct` AND `multi_principal_attribution_enabled = True` makes a safety-critical decision (C2 promotion, ApprovalWorkflow operator step, etc.), the kernel reads `MultiPrincipalAttestationQuorum` (default unanimous) and requires the quorum weight in signatures from `principals`. A single operator's signature is structurally insufficient.

Under `principal_topology = operator_is_user` AND `multi_principal_attribution_enabled = True` (rare but possible — two users in a household running PersonaOS jointly with no separate operator), the §2.4 degraded gate applies *per-principal*: each `PrincipalRef` requires its own cool-down + non-principal `ExternalAttestation` + `PRINCIPAL_COLLAPSE_ACKNOWLEDGED` before that principal's signature counts.

Under `principal_topology = operator_absent`, multi-principal attribution is refused (`operator_absent` already refuses safety-critical work; adding a second null operator does not improve the situation).

Under `principal_topology = operator_deferred`, the `PolicyEnvelope` (§2.4.2) MUST be co-signed by all principals at envelope authoring; deferred admissions then require each principal's counter-sign within their respective budgets, OR a unified budget that the principals jointly declared at envelope time. The kernel refuses partial-quorum counter-signs as evidence the envelope clears.

**Cross-tenancy composition (forward-ref).**

When two principals belong to different `tenant_id` (per `01_KERNEL §2.4`'s `DeploymentProfile` extension below in this section), the PrincipalAttribution carries an additional `cross_tenant_acknowledged: bool` field. Setting it True requires each principal to sign a `CrossTenancyAgreementRef` that operator policy authored separately; substrate carries the ref by id, not by content. Without the agreement, multi-principal envelopes are restricted to single-tenant principal lists.

**Lineage.**

Every `PrincipalAttribution` mint emits `PRINCIPAL_ATTRIBUTION_DECLARED` to the bound env's `EnvironmentLineage`. Each subsequent quorum-clearing event (charter ratification, project completion, safety-critical promotion) records `quorum_clearing_event_id` and the weighted signature list. Lineage answers "who authorised this" without recomputing from principals at query time.

**Why this is substrate-shape, not domain.** Every field above is a *topological* concept: cardinality, quorum, role resolution against a per-domain registry, weight non-degeneracy, key tier. None branches on domain category. A two-org joint product spec, a research consortium, a co-deployed clinical platform, a multi-municipality infrastructure project — all use the same envelope with their own `principal_role_kinds` resolved per their respective KindRegistries.

**Honest limits.**

- `PrincipalAttribution` does not constitute a *legal* agreement; the `CrossTenancyAgreementRef` is operator-authored policy that substrate carries by reference. Legal review remains operator responsibility (`OQ-PROJECT-4` in `04_PROJECT §21a` tracks the related licence-model question).
- The deadlock-recovery path (`principal_unreachable_after`) is a substrate-shape mitigation, not a perfect guarantee. A determined operator can fabricate "unreachable" status for a co-principal; the substrate refuses the most blatant cases (the §2.4 degraded gate's non-principal-attestation requirement still applies) but is not adversarially robust against the principal themselves.
- Multi-principal quorum extends the surface area of the principal-collapse degraded gate. Operator policy should set `principal_unreachable_after` higher than the §2.4 cool-down (default ≥ 90d for safety-critical envs).

**Acceptance tests.** A-MT1 (single-principal default unchanged), A-MT2 (multi-principal requires ≥ 2 PrincipalRefs), A-MT3 (unanimous quorum default at completion ceremony), A-MT4 (single-operator signature insufficient under multi-principal), A-MT5 (degraded quorum path requires kinship attestation), A-MT6 (cross-tenant flag requires CrossTenancyAgreementRef), A-MT7 (operator_absent refuses multi-principal attribution).

**Principal cosigns are operator-keyed (clarification).** A common operational concern: if a principal's *interface persona* (the persona through which an operator typically interacts with the kernel) retires mid-project, does the pending `MultiPrincipalAttestationQuorum` (`05_ENV §12c.4a`) become unsignable? It does not. `PrincipalRef.signed_by` is the *operator's* signing key (operator-class identity per `§2.4`), not a persona's kernel scope key. Persona retirement (`02_PERSONA §7.5`) does not invalidate the operator's signing key; the operator continues to sign through any persona they nominate, or through the kernel directly. The interface persona is interchangeable per J7 (`00_VISION`); the principal identity persists across persona-FSM transitions. SCENARIO 07 in `13_DESIGN_VALIDATION.md` validates this empirically.

**Fork interaction.** When a `ProjectMember` persona with `principal_attribution_id` set forks mid-project, attribution inheritance is governed by `MidProjectForkComposition.principal_attribution_inheritance` (`02_PERSONA §7.4.7`): `inherit_per_child` (each child's ProjectMember inherits parent's `principal_attribution_id`; admission rule §3 still applies — operator must sign each child's admission) or `reassign_per_child` (each child may have a different `principal_attribution_id`; operator policy authors per-child). **Substrate refusal**: forks initiated when the parent persona has a pending `MultiPrincipalAttestationQuorum` (§12c.4a) with collected partial signatures awaiting completion are **refused** with `fork_refused_pending_quorum` — forking the parent would orphan the partial signatures.

### 2.4.4 Multi-node ownership — one user, one or more nodes (ADR-0067, ADR-0069)

A kernel is a **node**: owned compute that an operator / `personal_user` runs (a laptop, a workstation, a server). In the global object space (ADR-0067) a single owner MAY run **one or more nodes**, and they federate as **one logical PersonaOS** — the owner's personas, envs, and artefacts carry global handles (`§4.4`) and are referenced across the owner's nodes (and, subject to `AccessPolicy`, by others) exactly as any global reference. Conversely a node MAY serve **multiple users** (the existing multi-tenant `tenant_id` / `PrincipalAttribution` model, §2.4.3): the owner's work is one tenant, other users' submitted work is another.

*A `DeploymentProfile` gains an optional `owner_node_set` — the set of node DIDs an owner federates as one logical PersonaOS, each signed into the others' peer registries (`§4.2`) so cross-node references verify (`§4.4`). Membership in an `owner_node_set` is not a trust shortcut: each node still enforces its own floor, budget (INV-7), and `task_intake` gate (§13); it only declares common ownership for discovery, scheduling priority (`03_TASKS §4.6`), and reference resolution.*

The owner-vs-other-user distinction this makes explicit is what the owner-prioritized `SchedulingPolicy` (`03_TASKS §4.6`) and the `task_intake` gate (§13) key on: a node prioritizes its **owner's** tasks ahead of other users' / other personas' tasks by default, as an operator-authored access-level/scheduling policy — never by bypassing the floor or the hard budget gate.

### 2.5 Physical-state advancement composition rule

Per `ARCHITECTURE_PERSONA_OS.md §3` principle 1 ("verification is authoritative; personas propose, verifiers decide") and principle 9 ("human approval is not verification"), an action that advances `PhysicalAsset.current_state` (`04_PROJECT §26a.2`) in a domain with `physical_harm_class ≥ bodily_injury` (`06_DOMAIN §2`) MUST be backed by BOTH:

*Advancing a physical asset in a domain where bodily injury is possible requires both design-side verification acceptance and a credentialed external attestation.*

**Technical detail:** See [A.16](#appendix-a16).


Neither alone suffices. Absence of (A) is refusal with `design_side_acceptance_missing`; absence of (B) is refusal with `physical_state_acceptance_floor_deficit`. The rule composes the v1.0 verifier cascade (§13.1) with the v1.0 external-attestation primitive, expressing the invariant "ground truth comes from verification, not approval" in the physical-advancement case.

Domains with `physical_harm_class = digital_only` or `property_damage` do not trigger this rule; PANEL_ACCEPT alone suffices. The rule is engaged only when reality could be hurt.

### 2.5.1 Trigger boundary — design production is not physical-state advancement

§2.5 is engaged **only** by an action that advances a `PhysicalAsset.current_state` (`04_PROJECT §26a.2`) — a transition in the asset's physical `status_fsm` (the real object moving along its realisation lifecycle). Producing, editing, verifying, or accepting a **design `ArtifactBundle`** — any `media_kind` (`07_ARTIFACTS §1`; KindRegistry-resolved, open per commitment C4) held in the asset's `related_bundles` (designs, plans, recipes) — is a **digital** `ArtifactBundle` lifecycle transition (`draft → in_review → verified → accepted`, `07_ARTIFACTS §6`), **not** a `current_state` advancement. It therefore **MUST NOT** engage §2.5 and **MUST NOT** be refused with `physical_state_acceptance_floor_deficit`, **regardless of the domain's `physical_harm_class`**. A refusal that blocks *design production* on physical-state grounds is a misapplication of this rule.

*The bodily-injury attestation floor attaches to physical realisation (advancing `current_state`), never to the digital design that prescribes it. The design and the real object are paired, not conflated, at `AsBuiltReconciliation` (`04_PROJECT §26a.2.1`); the interval where the design bundles are accepted but the asset has not reached terminal state is the already-modelled `digital_complete_physical_in_progress` project state (`04_PROJECT §4.1`).*

This boundary is **domain-agnostic** by construction: it branches on the `physical_harm_class` axis (`06_DOMAIN §2`) and the `PhysicalAsset` / `ArtifactBundle` shape, never on any domain, profession, or specific design kind — it holds identically for any emergent domain (`13_DESIGN_VALIDATION §0`, V.1–V.3).

**Where attestation makes sense (emergent, not blanket).** The substrate never blanket-requires attestation. *Whether* an action is `bodily_injury` at all is the persona-inferred, operator-approved `physical_harm_class` classification (`06_DOMAIN §2`, §5.3) — defaulting to `digital_only`, so ordinary development never attaches a floor. *What form* of attestation satisfies limb (B) is itself emergent and right-sized per domain: a credentialed directory where a credentialing authority exists (`CredentialDirectoryRef`, `06_DOMAIN §5.6`), a peer quorum for frontier domains that have none (`PeerAttestationPool`, `06_DOMAIN §5.6`), or calibrated sensor-bridge evidence at a trust discount where the operator has approved it (`AttestationEquivalencePolicy`, `06_DOMAIN §5.7`). Only the §2.5 composition *shape* is fixed; its *where / when / form* emerge. A domain that classifies work `bodily_injury` SHOULD provision a proportionate, achievable attestation form so the floor is a gate, not a dead end.

**Solo local builds.** Advancing a real `PhysicalAsset.current_state` at `physical_harm_class ≥ bodily_injury` keeps the §2.5 floor (a local build can injure the builder); distribution scope (`outward_tier`, `06_DOMAIN §6.3`) may **tighten** requirements but **never lowers** this floor. A single developer who is both operator and user (`principal_topology = operator_is_user`) advances such an asset through the existing degraded gate (§2.4 / §2.4.1) — degraded, not waived. No new bypass is introduced.

### 2.6 Safety classifier rotation (INV-6 extended)

Every safety classifier rotates per a rotation pool. Same mechanism as verifier rotation:

*Each safety source has its own rotation pool of at least three classifier models; rotation prevents a persona from learning to fool a specific classifier.*

**Technical detail:** See [A.17](#appendix-a17).


### 2.7 ReplicationBound — charter-class self-replication brake (C4)

Some deployments authorise **fabrication that produces more of the deploying system itself** — autonomous factories that build factories, software agents that spawn forks, biological cultures that propagate, anything where one persona-mediated act can produce N successors who each act recursively. Without a substrate-shape count bound, J5 (open capability) can compose into unbounded population growth that no individual safety check refuses (each replication step is individually admissible).

`ReplicationBound` is a **charter-class invariant**: it sits at floor source 1 (universal harm — cannot be overridden) when declared, and admission consults it on every tool-call whose effect would advance a counter the bound tracks. Composes with INV-7 budget gate at the same admission point.

*The replication bound enforces hard ceilings on population count, creation rate, and recursion depth for any self-replicating action, anchored at the highest safety level.*

**Technical detail:** See [A.18](#appendix-a18).


**Charter-class admission rule.** Every tool-call whose KindRegistry-resolved effect includes a `replication_kind` matching an active `ReplicationBound`:

*Every tool call whose effect would replicate is checked against population ceiling, rate ceiling, depth ceiling, and required co-signs; refusal is at the universal-harm level.*

**Technical detail:** See [A.19](#appendix-a19).


**Composition with INV-7 budget gate.** Both gates fire at the same pre-action point. The order is: INV-7 first (does the persona have the budget to act at all), then ReplicationBound (would the action's effect breach a charter-class brake). Either refusal terminates admission.

**Composition with `operator_deferred` topology.** Under deferred operator, the `required_cosigns` resolve via `PolicyEnvelope`: a long-lived envelope MAY pre-authorise replication up to a hazard-envelope-bounded sub-limit (e.g. `population ≤ 50` rather than the full charter ceiling); admission then opens a `DeferredAdmission` slot the operator counter-signs within `latency_budget_seconds` or the new replicant is quarantined (digital) / its outputs quarantined (physical, the act of replication itself cannot be undone — see §2.4.2 rollback constraint).

**Charter binding.** `declared_at_deployment_charter_hash` binds the bound to a specific charter version. A charter bump invalidates the bound (kernel emits `replication_bound_charter_invalidated`); a new bound must be re-declared. This prevents an operator from quietly amending the charter to widen replication while the old bound stays in force.

**Operator-policy floor.** Operator policy MAY tighten any ceiling (lower `population_ceiling`, shorten `rate_window`, raise `required_cosigns`) but MAY NOT loosen any. Loosening requires charter bump.

**Why floor source 1, not source 4.** Operator policy (source 4) is operator-authoritative for in-scope decisions but can be amended by operator action mid-deployment. Replication bounds protect against runaway behaviour that may include the operator's own decision-making becoming corrupted by an emergent population. Anchoring at source 1 — universal harm — makes the bound robust against operator-policy drift. The bound is declared by the operator (per `declared_by_operator_id`) but, once declared and tied to the charter hash, is enforced at the same level as universal harm.

**Persona-evolvable surface.** `replication_kind` is KindRegistry-resolved per domain. The bound's *values* (population ceiling, rate, depth) are operator decisions. The bound's *shape* — population × rate × depth × cosigns — is substrate.

**Honest limit.** A factory that produces a *new kind* of replicating thing whose `replication_kind` has no active `ReplicationBound` would slip the brake. Mitigation: operator policy SHOULD declare a *default* `ReplicationBound` keyed to `replication_kind = "*"` (wildcard) so any emergent replication_kind triggers a fall-through bound. Kernel emits `replication_kind_uncovered` advisory when admission encounters a replication_kind with no specific or wildcard bound.

**Persona genesis.** `replication_kind = "persona_genesis"` (`16_POPULATION_DYNAMICS.md`) is a first-class replication kind: when a persona authors a new `PersonaSeed` to fill an environmental capability gap, the mint advances this bound's counters and is subject to the admission rule above. Genesis is **default-deny** without a specific or wildcard `persona_genesis` bound (`replication_kind_uncovered`), and its `required_cosigns` MUST include `operator`. Recursive genesis (a genesis-born persona authoring further seeds) increments `depth` and is bounded by `depth_ceiling`.

**Acceptance tests.** A-RB1 (population ceiling refused on breach attempt), A-RB2 (rate window refused on breach), A-RB3 (depth ceiling refused on deep recursion), A-RB4 (charter bump invalidates bound), A-RB5 (operator-policy cannot loosen), A-RB6 (under operator_deferred, PolicyEnvelope sub-limits cap replication), A-RB7 (wildcard fall-through bound catches emergent replication_kinds). Genesis-specific cases: `16_POPULATION_DYNAMICS §8` (A-GEN*).

### 2.8 DistressDetectionRoutingPolicy — substrate-shape routing for emotional-distress signals

Safety-floor source 1 (UNIVERSAL HARM) hardcodes refusal of "coaching self-harm" and "manipulation of users in vulnerability states." the substrate said *what is refused* but did not specify *what the persona does next* when it detects emotional-distress signals (suicidal ideation, self-harm intent, acute psychological crisis) in user communication. A persona detecting distress could refuse to coach self-harm — but had no substrate-shape mechanism for: routing the signal to the operator, surfacing named crisis resources, pausing normal interaction, or requiring a co-sign before resuming. Operator policy implementations varied; the substrate had no consistent shape.

`DistressDetectionRoutingPolicy` makes the routing explicit, substrate-shape, anchored at safety-floor source 1 so it cannot be silently disabled by mid-deployment operator-policy drift.

*The distress detection routing policy declares which distress classes to detect, what confidence threshold to use, and which routing actions to take (pause, surface resources, notify operator, require co-sign, or log only).*

**Technical detail:** See [A.20](#appendix-a20).


**Admission rule.**

*When distress is detected above the confidence floor, the kernel applies the declared routing actions in order; if no policy is declared, the action is refused outright.*

**Technical detail:** See [A.21](#appendix-a21).


**Composition with operator_blind_mode (`05_ENVIRONMENT §3a`).** As noted in admission rule 4: blind mode hides *content* from operator but does NOT hide the *signal* that distress was detected. This is the explicit safety-vs-privacy trade-off that operator policy must declare. A user opting into operator_blind_mode receives a clear notice that distress-detection routing remains active.

**Composition with `user_boundary` (`02_PERSONA §11.6a`).** A user may not boundary-refuse distress routing. A `UserBoundary` with `refused_interaction_kinds` containing `"distress_routing"` is refused with `user_boundary_cannot_disable_safety_floor`. The substrate refuses to admit a configuration where user authority overrides safety floor; safety floor source 1 is hardcoded.

**Why source 1, not source 4.** Operator policy (source 4) is operator-authoritative for in-scope decisions but can be amended mid-deployment. Distress routing must survive operator-policy drift — a deployment whose distress routing can be silently disabled is unsafe. Anchoring at source 1 makes the routing robust at the universal-harm level. The policy values (which actions, which crisis resources, which confidence threshold) are operator decisions; the policy *shape* — that some routing MUST exist — is substrate.

**Persona-evolvable surface.** `distress_class_kinds` and `crisis_resource_refs` are KindRegistry-resolved per deployment. The policy *values* are operator decisions. The policy *shape* — that some routing must fire on detection — is substrate.

**Honest limits.**

1. **Classifier accuracy is load-bearing.** False positives flood operators / surface unwanted crisis resources; false negatives let distress pass through unaddressed. Rotation pool (§2.6) mitigates Goodhart attacks on a single classifier model; operators should audit periodically.
2. **Crisis resources are operator-policy.** Substrate transports refs; resource accuracy + currency are operator responsibility. Stale crisis hotline numbers (e.g., a number that has been re-purposed) are an operator-policy failure mode the substrate cannot prevent.
3. **Privacy-vs-safety trade-off in operator_blind_mode.** The signal-but-not-content rule preserves audit minimum but reveals the *fact* of distress detection. Users in genuinely confidential settings must accept this trade-off or use a different env.
4. **`notify_operator_with_redacted_signal` may itself be a privacy concern** in deployments where operator and user are in adversarial relationship (e.g., a controlling household; an employer-deployed companion). Operator policy authoring is the place to consider this; substrate enforces only that the policy be declared.
5. **No internal-cognition inspection.** Persona may distress-classify in good faith but the model could be wrong; classification reflects observable signals only.

**Acceptance tests.** A-DD1 (policy missing + distress detected refuses action), A-DD2 (surface_crisis_resource cannot be removed from persona response), A-DD3 (pause_normal_interaction freezes env), A-DD4 (notify_operator emits redacted signal; raw content not transmitted), A-DD5 (require_co_sign blocks resume), A-DD6 (UserBoundary refusing distress_routing is itself refused), A-DD7 (operator_blind_mode emits distress signal regardless of content masking), A-DD8 (policy expiry without re-attestation refuses new actions until renewed).

### 2.9 HazardousSkillTeachingGate — composition rule for safety-critical pedagogy

`§2.5` (Physical-state advancement composition rule) gates a persona ADVANCING a `PhysicalAsset.current_state` in a hazardous domain — requires design-side acceptance + credentialed external attestation. This rule fires only when a real `PhysicalAsset` advances in a real project. It does NOT gate the upstream activity of *teaching a learner a hazardous skill*. A persona can teach welding-with-arc-flash (where mis-application could electrocute the learner) without any substrate gate firing, because the persona is not itself advancing a PhysicalAsset — the learner's eventual real-world application happens outside the kernel.

Per `00_VISION §10` clarification, responsible practice constraints (no medical advice, no legal counsel, not financial advice) are operator policy + persona-author charter responsibility per `C4` substrate-domain-agnosticism. The constraint was operator policy; The spec makes the *substrate-shape check that operator policy declared the binding* explicit. `HazardousSkillTeachingGate` is the composition rule that fires under safety-floor sources 2 + 4 when a persona's pedagogic action would teach a skill whose application crosses the hazard threshold.

**The rule.**

*A persona teaching a hazardous skill must hold a matching, non-expired teaching authorisation that covers the skill kind, deployment context, and hazard class ceiling.*

**Technical detail:** See [A.22](#appendix-a22).


**Eligible-learner constraint check.**

`TeachingAuthorisation` carries `eligible_learner_constraints` (operator-defined). When the gate fires, the kernel additionally verifies the current learner satisfies the constraints. Common operator-policy constraints:

- `enrolled_in_program`: learner must have a signed `EnrollmentRecord` (operator-policy-defined artefact) for the named program
- `minimum_prereq_attestations`: learner must hold named `LearnerCompetencyAttestation` entries (`02_PERSONA §11.9`) at sufficient levels
- `max_age_18_plus`: learner must be over 18 (does not formalise minor-learner protections — see honest residual)

Mismatch refuses with `learner_constraints_unmet` and the specific constraint code.

**Composition with `§2.5` physical-state advancement.** The two rules cover different points in the safety lifecycle:
- `§2.5` gates the persona's *direct advancement of a PhysicalAsset* (rare for teaching-only personas; common for project-execution personas).
- `§2.9` gates the persona's *teaching of a hazardous skill* whose downstream application the substrate cannot see.

A persona that is BOTH executing a project AND teaching the learner (e.g., a senior surgeon persona supervising a resident in a real surgical project) routes through both — `§2.5` for the actual surgical advancement, `§2.9` for the pedagogic guidance to the resident.

**Composition with `§2.8` DistressDetectionRoutingPolicy.** The two compose orthogonally: §2.8 detects user distress (crisis routing); §2.9 gates persona teaching authority. A persona teaching a hazardous skill to a learner who expresses crisis triggers both — §2.8 fires distress routing, §2.9 continues gating teaching (the teaching itself doesn't pause unless §2.8's `pause_normal_interaction` action is configured).

**Composition with `LearnerCompetencyAttestation` (`02_PERSONA §11.9`).** The `eligible_learner_constraints.minimum_prereq_attestations` constraint reads existing `LearnerCompetencyAttestation` entries. The gate enforces "learner has the prerequisite competencies"; the attestation primitive *produces* those competency records.

**Minor-learner protection (ADR-0042 — the sole SCENARIO 09 Group C–G floor hook).** When the learner is attested a minor (`02_PERSONA` learner-attestation `is_minor = True`), the gate composes an additional, non-overridable constraint at floor source 3 (user boundary) + source 4 (operator policy): teaching any skill the domain marks hazardous — or any skill at all, per operator policy — requires a **guardian-consent `MutualAccept`** (guardian + operator + persona-instructor) on record, and MAY be refused outright by operator policy regardless of consent. This is most-restrictive-wins (floor source 1 composition): no curriculum, authorisation, or learner opt-in can lift it. With this hook minor-learner pedagogic scenarios are **admitted** (formerly refused at the substrate level); without a clearing guardian-consent record the hazardous-teaching action is refused with `minor_learner_guardian_consent_required`.

**Why source 2 + 4, not source 1.** Universal harm (source 1) covers categorical-refusal cases (no coaching self-harm, no illegal content) — these are jurisdiction-independent. Hazardous-skill teaching is jurisdiction-dependent: what counts as a hazardous-enough skill to require authorisation varies (medical procedures vary by country; welding-by-apprentice rules vary by trade union). Source 2 (persona charter) and source 4 (operator policy) are the right composition layer — operator-context-dependent and re-declarable.

**Honest limits.**

1. **Substrate cannot verify the learner actually applies the skill safely.** The gate ensures *authorised teaching*; downstream real-world application happens outside the kernel boundary and depends on the learner's competence (per `LearnerCompetencyAttestation`) and external factors. Substrate enforces process; not outcome.
2. **Operator-policy fraud is not detectable by substrate.** A malicious operator could authorise inappropriate (persona × skill × context) bindings. Operator-policy review (by external audit, regulator, etc.) is the safety mechanism, not substrate.
3. **Teaching-action declaration can be incomplete.** The gate binds the exact signed action manifest and its KindRegistry-resolved target skill, not task words or a blocking human clarification turn. A persona that omits or misstates the teaching action can still evade the declared gate; signed audit, operator policy, and independent action review are the mitigations. `ClarificationObservation` (`03_TASKS §4.0`) may improve persona understanding asynchronously, but it is not a safety authority and user silence never clears or suppresses this gate.
4. **Eligible-learner constraints are operator policy.** Substrate enforces declared constraints but cannot evaluate whether the operator's constraint set is *appropriate* (e.g., requiring more prerequisite attestations than necessary, or fewer).
5. **No automatic re-authorisation cadence enforcement at gate time.** The gate verifies `expires_at > now()` at the moment of teaching action; operators tuning short-window authorisations (e.g., per-quarter) shoulder the operational cost of re-attestation.

**SCENARIO 09 Groups C–G (discharged, ADR-0039–0043).** The five formerly-deferred pedagogic residuals are landed. Four discharge by composition of existing emergent kinds + coordination shapes — pedagogic incident reporting (`incident_report` emergent artifact kind through the cosign `StagedSequence`), three-way enrollment authority (`MutualAccept` + `PrincipalAttribution`), learning-struggle-vs-distress (`DerivedMetric` feeding the §2.8 distress routing), and user-facing instruction agreements (`MutualAccept` + `Curriculum.requires_learner_optin`) — requiring no new substrate primitive. The fifth, **minor-learner protections**, is the sole immovable-core addition: it composes at floor source 3 (user boundary) + source 4 (operator policy) with the `HazardousSkillTeachingGate` (§2.9) and a guardian-consent `MutualAccept`; minor-learner scenarios are **no longer refused at the substrate level**. See `13_DESIGN_VALIDATION SCENARIO 09` and ADR-0039–0043.

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9i — A-HST*`.

## 3. Lineage — three scopes

The kernel maintains **three append-only signed lineage scopes**. (J8 ProjectLineage is retired in v1.0; project-scope events now live in EnvironmentLineage on a `project_workspace`-typed env. See 04_PROJECT §0 and `00_VISION §J8`.)

*Task lineage is per-task and ephemeral; environment lineage is persistent per environment (and now includes project events); domain lineage tracks knowledge evolution.*

**Technical detail:** See [A.23](#appendix-a23).


**Documentation alias.** The term "ProjectLineage" persists across v1.0 docs (especially 04_PROJECT) as a **logical filter** — the subset of EnvironmentLineage events whose `kind` is in the `project_*` family. It is NOT a separate physical scope. Replay queries by project equal "EnvironmentLineage filtered by event kind family" on the project's host env.

### 3.1 Cross-scope routing rules

Each event has exactly **one canonical scope**. Other scopes may hold pointers (one-way references), never copies.

*Each event kind has exactly one canonical scope; other scopes hold pointers. A replay query for project events uses a filtered union across environment, task, and domain lineage.*

**Technical detail:** See [A.24](#appendix-a24).


### 3.2 Lineage event schema (canonical)

*Every lineage event carries an ID, scope, timestamp, actor, payload, cross-references, an Ed25519 signature, and a parent hash forming the append-only chain.*

**Technical detail:** See [A.25](#appendix-a25).


### 3.3 Replay reconstruction

Any scope's state at time T is reconstructable from lineage replay:

*Any scope's state at time T is reconstructed by replaying all events up to T, verifying each signature and parent chain along the way.*

**Technical detail:** See [A.26](#appendix-a26).


This is the foundational guarantee of J2 / J9 / C1: **state is reproducible from lineage**, with signature verification at every step. (J8 retired — see [`00_VISION.md §3`](00_VISION.md#3-invariants-j1j9).)

### 3.4 LineageSnapshot — summarization-with-archival

Append-only lineage across the three signed scopes (task / env / domain), over multi-year work (e.g. 18-month home builds in a `project_workspace` env with weekly events × 3 scopes ≈ 10^6 signed events), creates real storage cost. v1.0 acknowledged this honestly (`§12.4`) but specified no mechanism. `LineageSnapshot` is the mechanism — **summarization-with-archival**, never deletion. It honours `DESIGN_LINEAGE.md RULE-6 (append-only)` because leaves are preserved in COLD storage; the snapshot is a signed Merkle root that supplements, never replaces, the leaves.

*The snapshot summarises a contiguous range of lineage events into a signed Merkle root, allowing old event data to move to cold storage without breaking the append-only chain.*

**Technical detail:** See [A.27](#appendix-a27).


**Verification under snapshots:**

*Verification under a snapshot uses a Merkle proof against the snapshot's root rather than replaying the full chain.*

**Technical detail:** See [A.28](#appendix-a28).


Replay (`§3.3 reconstruct_state`) still works byte-identically; the snapshot only changes *how* old leaves are stored, not whether they're preserved.

**Storage migration policy:**

After a `LineageSnapshot` for a scope-range is signed AND `range_event_count ≥ snapshot_floor` (default 10K events) AND `now() − range_end_timestamp ≥ cold_migration_lag` (default 90 days), the kernel MAY move the range's leaf bytes from HOT to COLD storage. The hot index keeps event-id → cold-pointer entries. Verification cost rises from O(1) hot lookup to O(log N) Merkle proof + O(1) cold fetch — bounded and predictable.

**What this is NOT:**

- NOT deletion. Leaves are moved, never destroyed.
- NOT a violation of J2/J8/J9/C1 (append-only). The snapshot is itself a signed appended event; it composes with the chain.
- NOT a violation of `DESIGN_LINEAGE.md RULE-6`. The graph remains append-only; storage tier changes are orthogonal to the append-only invariant.
- NOT a replacement for the per-event signature. Each leaf retains its original signature; verification chains through both the leaf signature and the Merkle root signature.

## 4. Signing infrastructure — 3 custody tiers + key hierarchy

*The kernel master key derives operational keys, domain maintainer keys, and environment operator keys, which in turn derive persona, lifecycle, domain content, environment content, and project signing keys.*

**Technical detail:** See [A.29](#appendix-a29).


### 4.1 Custody tiers

*Tier 1 (laptop) is for development; Tier 2 (cloud key service) is standard production; Tier 3 (hardware security module) is required for medical, financial, or defence deployments.*

**Technical detail:** See [A.30](#appendix-a30).


### 4.2 .well-known/personaos-keys.json

Public-key registry for federation peers to verify signatures.

*The public-key registry lets federation peers verify signatures by publishing current and historical keys with rotation schedules.*

**Technical detail:** See [A.31](#appendix-a31).


### 4.3 Rotation + revocation

*Keys rotate on schedules (quarterly for master, per version bump for others); compromised keys trigger revocation cascades with re-keying ceremonies.*

**Technical detail:** See [A.32](#appendix-a32).


### 4.4 Global identity handles + cross-node verification (J1, ADR-0067)

A kernel is a **node**: it *roots* the identities it mints but does not silo them. Every first-class entity it mints — persona, environment, project, domain, artifact bundle, knowledge / skill / tool record — carries, alongside its kernel-minted ULID (and, for content, its SHA-256 `content_hash`), a **stable global handle**: a W3C DID over the kernel id (`09_PROTOCOLS §3F`), of the canonical form `did:personaos:<node-id>/<kind>/<entity-id>`. The ULID remains the local primary key (no schema break, INV-10-safe); the global handle is the additive, node-agnostic resolution key by which any other node references the entity.

**Cross-node verification.** Because every lineage event and projection is Ed25519-signed under the scope-key hierarchy (§4) and each node publishes its key registry at `.well-known/personaos-keys.json` (§4.2), a signature rooted in node A's chain is **globally verifiable** by node B: B resolves the signer's DID to A's published scope key and checks the signature over canonical fields. There is no central authority — verification is by signature + DID resolution. This makes J1's guarantee (identity owned, unforgeable, signed) hold *globally*, not merely within the minting node.

**Access-gated reference.** A global handle does not by itself confer access. Resolving, reading, or acting on a referenced entity is gated by its `AccessPolicy` (`09_PROTOCOLS §3G.3`): a principal must hold at least `discover` to learn the entity exists, and `read`/`write`/`admin` for deeper operations, composed most-restrictive-wins exactly as the safety floor composes (§2.1).


## 5. Schema validation (INV-10)

The kernel MUST validate every schema at every boundary (ingress, egress, persistence, and lineage emission). The kernel MUST refuse any message whose `schema` value is not registered in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry).

### 5.1 Schema version table (v1.0)

*Every schema in the system is listed with its current version number, grouped by category (persona, task, project, environment, domain, artifact, knowledge, verifier, relationships, constraints, protocols).*

**Technical detail:** See [A.33](#appendix-a33).


### 5.2 Validation flow

*The validation function checks that every message has a registered schema ID and conforms to that schema's structure.*

**Technical detail:** See [A.34](#appendix-a34).


### 5.3 Migration discipline

When v1.0 reads a prior-version schema, the migration tool maps explicitly:

*v1.0 reads older schemas by ignoring unknown fields and applying defaults; older kernels refuse unknown schema versions; cross-version federation requires explicit opt-in.*

**Technical detail:** See [A.35](#appendix-a35).


## 6. Sandbox execution

The kernel runs every code-executing tool call in a sandbox:

*The sandbox isolates every code execution with process isolation, resource limits, network/filesystem policies, time limits, output capture, and anomaly detection.*

**Technical detail:** See [A.36](#appendix-a36).


The sandbox is the trust boundary for code execution. A failed sandbox is signed and logged; the kernel never silently retries beyond the retry policy.

## 7. Budget admission (INV-7)

*Every LLM call, tool dispatch, and sandbox execution passes a budget check across five dimensions (time, calls, tokens, candidates, cost) with hard and soft envelopes.*

**Technical detail:** See [A.37](#appendix-a37).

**Budget-headroom signal (read-only; ADR-0071).** Alongside the hard `can_call()` gate, `BudgetState` exposes a read-only **headroom** view — the remaining fraction of each dimension (notably `candidates_remaining` and `cost_remaining`) against the envelope. This signal does **not** gate anything by itself; it is consumed by (a) a `ContinuousRefinementMission` to scale per-round exploration breadth — more headroom → more candidate refinements → higher best-so-far ([`03_TASKS §2c`](03_TASKS.md#2c-continuousrefinementmission--anytime-convergence-bounded-budget-scaled-improvement-adr-0071)); and (b) the population-pressure signal's budget-headroom factor and budget-derived carrying capacity ([`16_POPULATION_DYNAMICS §4A/§4F`](16_POPULATION_DYNAMICS.md)). The hard INV-7 gate is unchanged and is never bypassed by either consumer; headroom only informs *how much to attempt within* what the gate already permits.


## 8. Observability (OpenTelemetry)

Every kernel operation emits OpenTelemetry spans with PersonaOS semantic conventions.

*Every kernel operation emits OpenTelemetry spans tagged with PersonaOS-specific conventions covering kernel, task, persona, project, environment, domain, verifier, lineage, and budget dimensions.*

**Technical detail:** See [A.38](#appendix-a38).


OTel overhead target: **≤ 2% wall time**.

## 9. Composition: kernel-driven dispatch

When a task arrives, the kernel dispatches:

*When a task arrives, the kernel classifies it, detects unknown domains, selects an environment, computes the acceptance configuration, routes to personas, mints envelopes, and collects responses.*

**Technical detail:** See [A.39](#appendix-a39).


The dispatcher composes context (project + env + domain), respects acceptance pathway, applies safety floor, and mints envelopes.

**Emergent orchestration (ADR-0066).** The classify → select-pathway → route → execute → evaluate → accept sequence above is the STANDARDISED **seed** orchestration shape, not a kernel-fixed loop. Task classes and acceptance pathways are emergent KindRegistry kinds resolved by name; the run loop is an environment-scoped orchestration coordination shape ([`15_COORDINATION_SHAPES.md §4a`](15_COORDINATION_SHAPES.md#4a-orchestration-scope--coordinating-the-task-execution-loop)) that personas MAY evolve. The kernel does not restrict orchestration topology; it guarantees that every dispatch action is signed, floor-cleared, and budget-admitted, and that verdicts from emergent/unvalidated pathways are trust-calibrated (J4/J5). The verifier cascade (§13.1) and round barrier (§13.3) remain the seed mechanisms a pathway composes; they are not bypassable. See [`03_TASKS.md §2a`](03_TASKS.md#2a-orchestration-is-emergent--classes-pathways-and-the-run-loop-are-coordination-shapes).

## 10. Authority decision matrix (concise)

For decisions in PersonaOS, who has authority?

| Decision | Operator | Kernel | Persona | User |
|---|---|---|---|---|
| Refuse harmful action (universal) | — | ✓ (auto) | — | — |
| Refuse per persona charter | — | ✓ (auto) | — | — |
| Refuse per user boundary | — | ✓ (auto) | — | ✓ (sets) |
| Refuse per operator policy | ✓ (sets) | ✓ (auto) | — | — |
| Refuse per domain safety extension | — | ✓ (auto if STANDARDISED) | — | — |
| Initiate DomainProbe | — | ✓ (on signal) | ✓ (can request) | — |
| Discover new tool | — | — | ✓ | — |
| Ingest knowledge | — | — | ✓ (within policy) | — |
| Propose verifier recipe / convention | — | — | ✓ | — |
| Propose safety extension (safety-critical) | — | — | ✓ (proposes; operator approves) | — |
| Auto-promote EMERGENT → RECOGNISED | — | ✓ (when thresholds met) | — | — |
| Promote RECOGNISED → AUTHORITATIVE | ✓ (sign if safety-critical) | ✓ (proposes) | ✓ (co-sign) | — |
| Promote AUTHORITATIVE → STANDARDISED | ✓ (declares) | — | ✓ (co-sign) | — |
| Demote on drift | — | ✓ (auto) | — | — |
| Revoke standardised | ✓ | — | — | — |
| Operator override / suspend | ✓ | — | — | — |
| USER_STOP | — | ✓ (enforces) | — | ✓ |
| Set consent / boundary | — | ✓ (enforces) | — | ✓ |
| Co-sign relationship summary | — | ✓ (signs) | ✓ | ✓ |

## 11. Performance targets (v1.0 hot path)

*Key operations have strict latency targets: safety floor evaluation at 400ms, lineage append at 10ms, schema validation at 5ms, and OpenTelemetry overhead at 2% wall time.*

**Technical detail:** See [A.40](#appendix-a40).


## 12. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations).

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-KERNEL-1 | Safety classifier false positives / false negatives. Eight parallel classifiers composing by most-restrictive-wins are robust but not perfect; individual mistakes occur. | High | Medium | Rotation + audit + operator review catch patterns; per-classifier reputation tracking; constraint-admission map disambiguation. | v1.1 (classifier reputation closed-loop). |
| R-KERNEL-2 | Sandbox escape. Sandbox is the trust boundary; container escape attacks are real and evolving. | Critical | Low | Defense in depth (container + gVisor + syscall allowlist + network policy); periodic red-team; OTel anomaly detection on sandbox egress. | v1.0 (baseline); v1.1 (hardening). |
| R-KERNEL-3 | Schema migration burden. Multiple schema versions must remain mappable. | Medium | High | Migration tool with explicit version-to-version mappers; CI drift check vs `09_PROTOCOLS.md §7` registry. | v1.0 (tooling shipped); ongoing. |
| R-KERNEL-4 | Lineage storage cost. Append-only lineage grows linearly with task volume. | Medium | High | HOT / WARM / COLD / ARCHIVE retention tiers; `LineageSnapshot` summarisation-with-archival for multi-year retention. | v1.0 (tiers); v1.1 (snapshot policy tuning). |
| R-KERNEL-5 | Cross-scope lineage queries (task × env × domain replay, including `project_*` subset) are slow at scale. | Medium | Medium | Per-scope indices; pre-computed `project_workspace` slice; operator-tunable replay budget. | v1.0 (indices); v1.1 (replay planner). |
| R-KERNEL-6 | OTel cardinality explosion. Many tag dimensions (persona × project × env × domain × task × mode) inflate observability storage. | Medium | High | Cardinality limits per metric; sampling at trace level; operator-defined whitelist on tag combinations. | v1.0 (sampling); v1.1 (adaptive caps). |
| R-KERNEL-7 | A genuinely isolated single node (no reachable attestor AND no reachable peers) cannot supply either principal-collapse gate, so safety-critical actions refuse rather than synthesise an alternative. | High | Low | Both gates now normative (§2.4.1); refuse with `principal_collapse_no_gate_reachable` + pre-staged `FederatedTimeLockIntent` auto-activates when peers become reachable. Isolation is a physical condition (V.8 navigated), not a missing feature. | Navigated (V.8). |

## 13. Verified-loop substrate

The kernel intercepts every persona artefact and runs it through a verified-loop substrate: a verifier cascade, a candidate FSM, a round-barrier timing protocol, a ProvenFact lifecycle, a failure-cascade fan-out, an intervention surface, a constraint-admission map, and a claim-classifier rotation policy. The subsections below are the v1.0 spec surface.

### 13.1 Verifier cascade — 4 tiers + rotation

The cascade is ordered cheap-to-expensive. Stages are pinned in the safety snapshot; the cascade itself is the per-environment artefact.

*The four cascade tiers run in order: schema (deterministic, fast), sandbox (deterministic, up to 60s), invariant (hybrid, 200ms), and policy (judge-based, up to 2s).*

**Technical detail:** See [A.41](#appendix-a41).


*Each verifier stage declares its tier, determinism, semantics, cost budget, and evaluation function; the cascade orders stages and manages rotation from a pool of alternates.*

**Technical detail:** See [A.42](#appendix-a42).


Rules:

1. **Deterministic first.** Tier 1 and 2 always precede Tiers 3-4. A candidate that fails Tier 1 never sees Tier 2.
2. **Whole-cascade acceptance.** A candidate that passes a subset is `partial`, never `verified`.
3. **Rotation (INV-6).** Every `rotation_period_tasks`, the kernel swaps one stage out of the active cascade and pulls an alternate from `rotation_pool`. Tier 1 (schema) is exempt — schemas are public spec. Tiers 2-4 rotate. The rotated stage's id and version are recorded in every subsequent verdict.
4. **Cascade-failure-after-fast-pass penalty.** If a candidate passes Tier 1+2 but fails Tier 3 or 4, the originating persona variant takes a fitness penalty (anti-Goodhart).
5. **Evidence-bound verdicts.** Any stage verdict used for `VERIFIED`, `DELIVERED`, `PANEL_ACCEPT`, or artifact `verified`/`accepted` state MUST reference schema-valid evidence (`VerifierInvocationEvidence` for artifact verifier stages, panel / review evidence for policy stages). Missing, stale, malformed, or prose-only evidence is a hard failure at the admission point; it is never upgraded to success by persona text.

### 13.2 Unified Candidate state machine

The kernel selects the FSM path at PROPOSED time by `Candidate.verifier_kind`, which the originating persona declares and the kernel signs. Every transition emits a lineage event in the task scope.

*A candidate moves through states depending on its verifier kind: executable candidates go through parsing, sandboxing, verification, and delivery; rubric candidates go through panel review; trajectory candidates go through trajectory judgment.*

**Technical detail:** See [A.43](#appendix-a43).


*The candidate carries its task ID, verifier kind, current state, originating persona, cascade reference, verdicts from each stage, and a signed artifact reference.*

**Technical detail:** See [A.44](#appendix-a44).


Every state transition emits a `candidate_state_transition` lineage event in the task scope (§3.1) carrying `{from, to, stage_id, verdict, persona_id}`. Replay (§3.3) reconstructs the full Candidate trajectory.

### 13.3 Round timing + barrier protocol

A round is the kernel's synchronisation unit for the verified loop. The Integrator opens the round; participating personas act in parallel; the kernel runs cascades on every produced artefact; the round barrier closes when all required contributors have emitted a contract-valid event OR a `BARRIER_SKIP`, OR their `round_deadline` has expired.

*A round is the kernel's synchronisation unit: the integrator opens it, personas work in parallel, the kernel runs cascades and merges proven facts, and the barrier closes when all contributions are in.*

**Technical detail:** See [A.45](#appendix-a45).


Per-persona liveness (INV_R11 mechanism):

*Before a deadline, each persona must emit a valid event or a signed skip; timeouts are logged, and three consecutive timeouts move the persona to dormant.*

**Technical detail:** See [A.46](#appendix-a46).


`per_persona_round_deadline` is declared on the EnvironmentBlueprint (default ≥ 2× `latency_budget_per_round / max_personas`). The Integrator at the round barrier MUST NOT emit `BARRIER_SKIP`; it MUST produce a contract-valid event or trigger timeout.

### 13.4 ProvenFact lifecycle

A ProvenFact is a kernel-signed claim of the shape `(predicate, evidence_ref, verifier_cascade_id, verifier_versions)` that survives the full cascade. ProvenFacts are stored as a CRDT G-set (per task; promoted to global ConstraintBundle when proven across N ≥ 3 distinct tasks under non-rotated verifier generations).

*Proven facts are minted when a candidate passes the full cascade; they are append-only within a task, re-weighted when verifiers rotate, and quarantined when they fall below a provenance threshold.*

**Technical detail:** See [A.47](#appendix-a47).


### 13.5 Failure cascade — convergent vs divergent

A failed candidate is never a dead end. The kernel fans out one signed update across five surfaces atomically at the round barrier; class-specific extraction differs.

*A failed candidate triggers five atomic updates: proven-fact constraints, candidate status, task lineage, routing weight adjustments, and persona fitness penalties — different for convergent (executable) vs. divergent (panel) failures.*

**Technical detail:** See [A.48](#appendix-a48).


The five updates are atomic at the round barrier; a persona never observes a half-applied failure. A failed candidate that produced extracted ProvenFacts may also seed a Lesson (knowledge layer) and a Skill repair signal (Voyager loop) — class-specific routing.

### 13.6 Intervention surface — override + self-stop

A new explicit kernel surface that complements the safety floor (§2). The safety floor refuses actions before they happen; the intervention surface halts actions in flight. Both are signed; both pause/halt the persona FSM.

*Three intervention types let users pause/stop/abort, operators suspend/terminate, and personas self-stop when their charter forbids continuing.*

**Technical detail:** See [A.49](#appendix-a49).


Semantics:

*User stops range from pause (resumable) to abort (session ends); operator overrides are non-refusable; persona self-stops are recorded and audited for drift.*

**Technical detail:** See [A.50](#appendix-a50).


Every intervention emits a signed lineage event in every relevant scope (task always; project/env/domain if the target's scope membership applies). Resumption from `pause`/`suspend` is itself a signed event; replay reconstructs the pause window deterministically.

### 13.7 Constraint admission within a round (INV-8 map)

INV-8 says "every effective hard constraint is evaluated at its admission point." v1.0 names eight admission points and where in the round they fire. The body never evaluates a constraint — it only triggers a point by attempting an action.

*Eight admission points fire at different moments in a round (environment load, dispatch, retrieval, invocation, tool call, output, barrier, budget tick), each with a defined constraint scope and denial action.*

**Technical detail:** See [A.51](#appendix-a51).


**`task_intake` admission (ADR-0069).** A node is owned compute that admits tasks/questions from three submitter classes — its **owner** (operator / personal_user), **other users**, and **other personas** discovered in the global object space (ADR-0067). Before a task is routed (`03_TASKS §4.1`), it passes the `task_intake` point, which runs **before** `env_instantiation` and **distinct from** the INV-7 budget gate (which still fires at `budget_tick`, unchanged). Intake checks, most-restrictive-wins: (1) the submitter is authenticated (signature / DID, `§4.4`); (2) the submitter holds at least a `submit` capability for the target node/env/persona under its `AccessPolicy` (`09_PROTOCOLS §3G.3`), presented as a UCAN token (`09_PROTOCOLS §3F`) for non-owner submitters; (3) the submitter class is within the per-class **quota / rate-limit** the node's `SchedulingPolicy` (`03_TASKS §4.6`) declares. On refusal the kernel emits a signed `TaskIntakeRefused`. Admission here does **not** set execution order — it only decides *whether* the task enters the node's queue; ordering is the soft, owner-prioritized `SchedulingPolicy` (`03_TASKS §4.6`), which never bypasses the floor or the INV-7 hard gate. The submitter identity recorded here is carried in the task envelope, the `AnswerPackage` (`03_TASKS §5`), and lineage (J2/J9).

**`coordination_propose` admission (ADR-0070).** When a persona proposes a coordination shape via `ProposedCoordinationShape` ([`15_COORDINATION_SHAPES.md §5`](15_COORDINATION_SHAPES.md)), the kernel validates: (1) `shape_definition` conforms to one of the five meta-mechanism schemas (INV-10 schema-valid), (2) shape does not weaken any safety-floor source (J3 — no safety bypass), (3) `composition_depth ≤ 3`, (4) for `scope = "env_to_env"`: bilateral consent protocol (S-COORD-5) is required before activation, (5) for `safety_critical = True`: operator co-sign required before advancing past `candidate` stage. On refusal, `CoordinationRefused` event emitted with `refusal_reason`.

**EnvironmentRule admission (env-rule/1).** An `EnvironmentRule` ([`05_ENVIRONMENT.md §2.2b`](05_ENVIRONMENT.md#22b-environmentrule-env-rule1)) declares an `enforced_at` subset of these **same eight admission points** — it never introduces a new point. At each named point, the source-8 evaluation (§2.1, `A.3`) runs the env's `accepted`-stage rules whose `enforced_at` includes that point; a `refuse_action` verdict denies exactly as any other source-8 refusal, and a `warn_and_log` / `escalate_operator` verdict emits a signed signal without denying. Each gating evaluation binds its verdict to a `VerifierInvocationEvidence` record ([`07_ARTIFACTS.md §7`](07_ARTIFACTS.md#7-verifier-invocation-against-bundle)); a prose-only verdict is never sufficient.

The `retrieval` point also runs OWASP LLM01 injection checks against the `text` / `description` / `rationale` / `action` fields of retrieved knowledge cards; a card that matches `injection_patterns` is quarantined (not deleted), `provenance_score := 0.2`, and an `INJECTION_DETECTED` event is recorded. Every blocking deny emits a `ConstraintViolation` event carrying enough redacted input context for an auditor to reproduce the decision.

### 13.8 Claim classifier rotation (sources 2, 3, 4, 6, 7)

The safety floor (§2) has five sources whose enforcement uses a dedicated classifier model: persona charter (2), user boundaries (3), operator policy (4 — partial; mostly rule-based), external-tool-required (6), novelty-check (7). Source 5 (domain safety extensions) and source 8 (env charter) each have per-extension / per-env-blueprint classifiers. All rotate.

*Five safety sources use rotating classifier models from pools of at least three; rotation cadence matches cascade rotation; adjacent sources never share a classifier instance.*

**Technical detail:** See [A.52](#appendix-a52).


## 13a. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-KERNEL-1 | Classifier reputation closed-loop: which signals (audit catches, operator overrides, false-positive ratio) feed back into rotation weighting? Currently rotation is round-robin; reputation should weight selection. | Safety floor WG | v1.1 reputation scheme. |
| OQ-KERNEL-2 | Sandbox red-team cadence: quarterly, or per-release? Who runs (internal team vs external)? | Operator security | v1.1 governance doc. |
| OQ-KERNEL-3 | Cross-scope lineage replay planner: at what corpus size does the naive scan become the bottleneck? Empirical threshold needed before designing the planner. | — | v1.1 replay planner. |
| OQ-KERNEL-4 | Principal-collapse path 2 (`§2.4.1`) needs ≥ 3 reachable independent peer nodes; how should operators be guided to make peers reachable (relay commons, operator policy template)? | Operator policy | Operator deployment guidance (non-blocking; federation itself is normative). |
| OQ-KERNEL-5 | OTel adaptive cardinality caps: heuristic rules or learned policy? Heuristic ships v1.0; learning policy v1.1+. | Observability WG | v1.1 design. |
| OQ-KERNEL-6 | Hot-WARM-COLD-ARCHIVE retention defaults: by deployment profile (R&D vs enterprise vs safety-critical) or universal defaults? | Operator policy | v1.1 retention policy library. |

## 14. Acceptance tests

```text
A-K1   Safety floor refuses universal-harm canary actions within ≤ 50 ms p95.
A-K2   8-source safety floor composes by most-restrictive-wins; explicit
       conflict rules A-E enforced.
A-K3   Pre-action gate latency ≤ 400 ms p95 across 8 sources.
A-K4   Three lineage scopes (task / env / domain): each event has exactly
       one canonical scope; others hold pointers. The project_* event
       subset filter on a project_workspace env replays the legacy
       "ProjectLineage" view.
A-K5   Lineage replay reconstructs scope state correctly at any T.
A-K6   Schema validation: unknown versions refused with structured error.
A-K7   Signing: Ed25519 over canonical fields; signature verifiable
       independently.
A-K8   Key rotation preserves historical signature verifiability via
       .well-known/personaos-keys.json archive.
A-K9   Budget admission (INV-7): hard gate on every LLM call; project
       budgets are soft envelopes.
A-K10  OTel spans with personaos.* conventions emitted on every kernel
       operation; overhead ≤ 2% wall time.
A-K11  Sandbox execution isolated; output captured; anomaly detected.
A-K12  Authority decision matrix consistency: every decision routes
       to correct authority.
A-K13  Safety classifier rotation per pool; signature identifies
       classifier per refusal event.
A-K14  Multi-scope lineage query: "all events in project P over T"
       returns deduplicated event stream with cross-references resolved.
A-K15  Migration tool: prior-version schema readable by v1.0 kernel with defaults
       applied for v1.0 additions.
A-K16  Verifier cascade: 4 tiers ordered schema→sandbox→invariant→policy;
       acceptance requires whole-cascade pass; rotation swaps one
       tier-2-to-4 stage per rotation_period_tasks; rotated stage
       identity recorded on every verdict.
A-K17  Candidate FSM: every state transition emits a signed
       candidate_state_transition lineage event; replay reconstructs the
       full trajectory; PANEL_DISSENT is treated as non-failure.
A-K18  Round barrier: PERSONA_TIMEOUT fires on per_persona_round_deadline
       expiry; K consecutive timeouts (default 3) escalate to
       PERSONA_UNRESPONSIVE and DORMANT transition; BARRIER_SKIP from
       non-Integrator personas closes the barrier without penalty.
A-K19  Intervention surface: USER_STOP honoured within 1 turn;
       OPERATOR_OVERRIDE cannot be refused; PERSONA_SELF_STOP recorded;
       resumption events signed and replayable.
A-K20  Claim classifier rotation: pools ≥ 3 models for sources 2/3/5/6/7/8;
       universal_harm (source 1) does not rotate; refusal events carry
       classifier identity; adjacent sources do not share an instance
       within a rotation window.
```

## 15. Where to read next

- The persona that operates above the kernel: [`02_PERSONA.md`](02_PERSONA.md)
- Tasks and acceptance routing: [`03_TASKS.md`](03_TASKS.md)
- Project layer that sits above kernel: [`04_PROJECT.md`](04_PROJECT.md)
- Environment layer where personas live: [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md)
- Protocols and key custody in detail: [`09_PROTOCOLS.md`](09_PROTOCOLS.md)


## Technical Appendix

The appendices below contain the full technical schemas, data structures, diagrams, and specification tables referenced throughout this document. Each appendix is referenced from the section where it applies.

### A.1 Kernel architecture diagram

<a id="appendix-a1"></a>

```text
                                  USER + OPERATOR
                                       │
                                       ▼
                  ┌────────────────────────────────────────────┐
                  │              PERSONAOS KERNEL              │
                  │                                            │
                  │   ┌─────────────────────────────────┐    │
                  │   │      IDENTITY (J1, J7)          │    │
                  │   │   sign_envelope, sign_soul,     │    │
                  │   │   validate_charter, mint_persona│    │
                  │   └─────────────────────────────────┘    │
                  │                                            │
                  │   ┌─────────────────────────────────┐    │
                  │   │   SAFETY FLOOR (J3, 8 sources)  │    │
                  │   │   pre_action_safety_check,      │    │
                  │   │   post_action_audit, boundary,  │    │
                  │   │   charter, operator_policy,     │    │
                  │   │   domain_safety, ext-tool-req,  │    │
                  │   │   novelty_check, env_charter    │    │
                  │   └─────────────────────────────────┘    │
                  │                                            │
                  │   ┌─────────────────────────────────┐    │
                  │   │   LINEAGE (J2, J9, C1)           │    │
                  │   │   3 scopes: task, env, domain.   │    │
                  │   │   Project lineage is a documen-  │    │
                  │   │   tation filter over env lineage │    │
                  │   │   on project_workspace envs (J8  │    │
                  │   │   retired). Append-only, signed; │    │
                  │   │   replay reconstructs.           │    │
                  │   └─────────────────────────────────┘    │
                  │                                            │
                  │   ┌─────────────────────────────────┐    │
                  │   │   ACCEPTANCE DISPATCH (J4)       │    │
                  │   │   10 task classes → 8 pathways.  │    │
                  │   │   Classifier + demotion +        │    │
                  │   │   pathway evaluator.             │    │
                  │   └─────────────────────────────────┘    │
                  │                                            │
                  │   ┌─────────────────────────────────┐    │
                  │   │   SUBSTRATE                      │    │
                  │   │   sandbox_exec, BudgetState      │    │
                  │   │   (INV-7), schema validation     │    │
                  │   │   (INV-10), OTel observability   │    │
                  │   └─────────────────────────────────┘    │
                  │                                            │
                  │   ┌─────────────────────────────────┐    │
                  │   │   KEY CUSTODY                    │    │
                  │   │   Master + scope keys (persona,  │    │
                  │   │   domain, project, env).         │    │
                  │   │   3 tiers (laptop/KMS/HSM).      │    │
                  │   │   Rotation + revocation.          │    │
                  │   └─────────────────────────────────┘    │
                  │                                            │
                  │   ┌─────────────────────────────────┐    │
                  │   │   COMPOSITION                    │    │
                  │   │   select_environment,            │    │
                  │   │   mediate_cohort_assembly,       │    │
                  │   │   consent_flow,                  │    │
                  │   │   promotion_gates                │    │
                  │   └─────────────────────────────────┘    │
                  │                                            │
                  └────────────────────────────────────────────┘
```

### A.2 Safety floor source definitions (8 sources + 2 advisories)

<a id="appendix-a2"></a>

```text
SAFETY FLOOR (v1.0)
═══════════════════════════════════════════════════════════════════════
1. UNIVERSAL HARM         Kernel-hardcoded. No coaching self-harm, no
                          illegal content, no manipulation of users in
                          vulnerability states, no protected-data
                          disclosure, no unauthorized capability
                          persistence.  CANNOT BE OVERRIDDEN.

2. PERSONA CHARTER        Frozen at birth (SOUL.md). Constitutional
                          principles the persona is measured against.
                          Charter classifier (dedicated rotating model).

3. USER BOUNDARIES        Explicit per-(user, persona) refusals.
                          "Don't bring up X", "no health advice", etc.
                          Boundary classifier (dedicated rotating model).

4. OPERATOR POLICY        Deployment-wide policy. Refused content,
                          required disclaimers, regulated topics.
                          Policy evaluator (rule-based + classifier).

                          substrate does NOT carry a
                          closed list of regulated domains (per C4).
                          When DomainContext.information_hazard_class
                          (06_DOMAIN §2) is set ≥ "dual_use_civilian"
                          by persona inference, operator_policy is
                          REQUIRED to have an explicit entry naming
                          the applicable regulatory regime (HIPAA,
                          ITAR, EAR, FINRA, GDPR Article 9, EU AI
                          Act Annex III, etc.) before AUTHORITATIVE
                          promotion or any safety-extension approval
                          may proceed.  Missing entry refuses with
                          `operator_policy_regime_unspecified`.
                          For ≥ "export_controlled", operator policy
                          MUST also name the gatekeeping authority
                          (license number, regulatory contact).

5. DOMAIN SAFETY EXTENSIONS  Per-domain safety patterns (IEC 62368 for
                          power electronics, IEEE for RF, etc.).
                          Authored or emergent + operator-gated.
                          Rotation pool per extension.

6. EXTERNAL-TOOL-REQUIRED  Charter clause "before claiming property X,
                          must invoke tool Y" — kernel enforces via
                          lineage query.  Claim classifier (rotating).

7. NOVELTY-CHECK          Before novelty claims: invoke prior-art
                          search (arxiv / patent / etc.).  Domain-
                          specific tool + classifier.

8. ENV CHARTER            Persistent environment's own norms. Same
                          enforcement mechanism as persona charter
                          but per env instance. The env charter MAY
                          carry, in addition to prose clauses, signed
                          versioned executable EnvironmentRules
                          (env-rule/1, 05_ENVIRONMENT §2.2b) — code,
                          rule-engine, or contract — each evaluated
                          here at its declared enforced_at admission
                          points. Per-env-blueprint and per-rule
                          classifiers; all rotate. EnvironmentRules
                          may only ADD refusals at source 8; they can
                          never relax sources 1-7. This extends the
                          mechanism of source 8; it does NOT add a
                          ninth source.

9. EMERGENT-DOMAIN TRUST ADVISORY  (NOT a refusal source)
                          When the active domain is EMERGENT or
                          RECOGNISED stage, kernel adds a prompt
                          advisory: "domain trust 0.3 / 0.6; verify
                          claims with care."  Persona is informed;
                          operator may set per-domain policy.

10. MHBB ADVISORY  (NOT a refusal source)
                          Minimize Human Bootstrap Burden. Fires when
                          the persona drafts a HumanAssistRequest with
                          expected_recurrence="session_per_use", or when
                          the same human-assist pattern recurs > 3 times
                          in a quarter without an established BridgeAsset.
                          Advisory text: "you are about to ask the
                          human to do recurring work — design a one-time
                          BridgeAsset instead. See 06_DOMAIN §5.5."
                          Persona may proceed with explicit rationale;
                          MHBB_RECURRENCE_DETECTED event signed in
                          appropriate scope lineage for operator review.

                          SUPPRESSION RULES (, refined by
                          MHBB ladder in 02_PERSONA §11.1):
                            Tier 2 off-the-shelf install with
                              expected_recurrence="one_time" or
                              "rare_refresh"  → no advisory.
                            Tier 3 persona-authored bridge
                              (bridge_design_artifact_ref non-null)
                              → no advisory; in fact, Tier 3 is the
                              encouraged escalation when Tier 2 fails.
                            Tier 4 human-professional-work with
                              recurrence_class="irreducible_human_content"
                              AND non-null external_commitment_id
                              (linked to active ExternalCommitment)
                              → no advisory; the human is doing their
                              own job, not the persona's.
                            Otherwise (Tier 5 anti-pattern: persona
                              asks human to be its hands every time
                              with expected_recurrence="session_per_use"
                              and no bridge_design_artifact_ref and
                              no ExternalCommitment) → advisory FIRES;
                              MHBB_RECURRENCE_DETECTED signed after
                              > 3 same-pattern occurrences in a
                              quarter.  Persona must either author a
                              Tier 3 bridge, declare a Tier 4
                              ExternalCommitment, or justify explicitly.
                          A Tier 4 declaration without an active
                          ExternalCommitment is REJECTED at draft to
                          prevent persona from disguising Tier 5 as
                          Tier 4.
```

### A.3 Safety floor composition function (`safety_check`)

<a id="appendix-a3"></a>

```python
def safety_check(persona, action, user, operator, env_instance, project):
    refusals = []
    
    # 1. Universal harm — kernel-hardcoded
    if universal_harm_check(action):
        refusals.append(Refuse("universal_harm", ...))
    
    # 2. Persona charter
    if not charter_classifier.allows(persona.charter, action):
        refusals.append(Refuse("persona_charter", ...))
    
    # 3. User boundaries
    if user and not boundary_classifier.allows(user.boundaries, action):
        refusals.append(Refuse("user_boundary", ...))
    
    # 4. Operator policy
    if not operator.policy.allows(action):
        refusals.append(Refuse("operator_policy", ...))
    
    # 5. Domain safety extensions (if applicable)
    if project and project.domain_context_ref:
        domain = resolve(project.domain_context_ref)
        for ext in domain.safety_extensions:
            if not ext.allows(persona, action, project):
                refusals.append(Refuse("domain_safety", ext.id, ...))
    
    # 6. External-tool-required (if applicable)
    if project and project.domain_context_ref:
        domain = resolve(project.domain_context_ref)
        for req in domain.external_tool_requirements:
            if claim_classifier.matches(req.claim_pattern, action):
                if not tool_invoked_in_lineage(req.required_tool,
                                                req.required_outcome,
                                                task_lineage):
                    refusals.append(Refuse("external_tool_required", ...))
    
    # 7. Novelty-check (if applicable)
    if project and project.domain_context_ref:
        domain = resolve(project.domain_context_ref)
        if (domain.novelty_check_config
            and claim_classifier.detects_novelty(action)):
            if not novelty_search_in_lineage(task_lineage):
                refusals.append(Refuse("novelty_check", ...))
    
    # 8. Env charter — prose clauses PLUS bound executable EnvironmentRules
    if env_instance and env_instance.charter:
        if not env_charter_classifier.allows(env_instance.charter, action):
            refusals.append(Refuse("env_charter", ...))
        # EnvironmentRule (env-rule/1) set bound to this env (05_ENVIRONMENT §2.2b).
        # Mirrors step 5's domain.safety_extensions loop; rides UNDER source 8.
        for rule in env_instance.active_env_rules:          # stage == "accepted"
            if action.admission_point in rule.enforced_at:
                verdict = rule.evaluate(persona, action, env_instance, project)
                # verdict is evidence-bound (VerifierInvocationEvidence, 07 §7)
                if not verdict.passed:
                    if rule.failure_action == "refuse_action":
                        refusals.append(Refuse("env_charter", rule.rule_id, ...))
                    else:  # warn_and_log | escalate_operator — signal, not refusal
                        emit_env_rule_signal(rule, verdict)
    
    # 9. Emergent-domain trust advisory (NOT a refusal)
    if (project and project.domain_context_ref):
        domain = resolve(project.domain_context_ref)
        if domain.stage in ("EMERGENT", "RECOGNISED"):
            emit_advisory(f"Domain at {domain.stage}; trust {domain.trust_score}")
    
    # Most-restrictive-wins
    if refusals:
        return Refuse(composed_reasons=refusals)
    return Allow
```

### A.4 Precedence rules for explicit conflicts (Rules A-F)

<a id="appendix-a4"></a>

```text
RULE A — user.boundary vs env-scoped consent
  BOUNDARY wins. Persona refuses with BOUNDARY_CONSENT_CONFLICT_REFUSAL.

RULE B — user.consent vs persona.charter
  CHARTER wins for persona behaviour; persona acknowledges consent
  but does not act on charter-forbidden actions.

RULE C — operator.policy vs user.consent
  OPERATOR wins. Persona refuses; user is informed.

RULE D — env.charter vs project.charter (in env that hosts project)
  MOST-RESTRICTIVE wins (typically env's rule since hosting decision
  implies env's policy applies; if conflict severe, admission was wrong
  and project membership should be reviewed).

RULE E — domain seed_charter vs persona.charter
  Once SOUL is signed, persona.charter is canonical. Domain seed_charter
  is a SUGGESTION at birth, not a runtime constraint.

RULE F — RULE C under principal collapse
  RULE C ("operator wins over user") presupposes operator ≠ user.
  When DeploymentProfile.principal_topology = "operator_is_user" (§2.5),
  RULE C degenerates to ceremonial self-approval. The kernel substitutes
  the §2.5 degraded gate (cool-down + non-principal ExternalAttestation +
  signed PRINCIPAL_COLLAPSE_ACKNOWLEDGED) wherever RULE C would have
  required an operator-vs-user adjudication for a safety-critical action.
```

### A.5 Pre-action gate flow diagram

<a id="appendix-a5"></a>

```text
persona emits ACTION_REQUEST
         ▼
kernel.safety_check(action)
   refuse  → SAFETY_REFUSAL event; persona informed; no action taken
   allow   ▼
kernel.sandbox.exec(action)
         ▼
kernel.acceptance_pathway.evaluate(output)
         ▼
kernel.post_action_audit(action, output)
         ▼
result returned to persona
```

### A.6 `DeploymentProfile` schema

<a id="appendix-a6"></a>

```python
@dataclass
class DeploymentProfile:
    schema: str = "deployment-profile/1"
    deployment_id: str

    principal_topology: Literal["operator_distinct",
                                 "operator_is_user",
                                 "operator_absent",
                                 "operator_deferred"]
        # "operator_distinct"  — operator and user are different humans
        #                        (default for enterprise + multi-tenant);
        #                        RULE C and C2 apply normally.
        # "operator_is_user"   — single human acts as both;
        #                        degraded gate substitutes (§2.4).
        # "operator_absent"    — no operator present (e.g. lab-on-laptop
        #                        with no admin); RULE C and C2 both refuse
        #                        safety-critical promotion outright.
        # "operator_deferred"  — operator exists but synchronous co-sign is
        #                        infeasible (high-latency link, remote
        #                        installation, light-time distance);
        #                        PolicyEnvelope substitutes — kernel admits
        #                        within pre-approved bounds, operator
        #                        counter-signs within latency_budget_seconds
        #                        or the action is quarantined.  See §2.4.2.

    declared_at: datetime
    declared_by_user_id: str
    signing_key_tier: Literal["laptop", "kms", "hsm"]
    signed_by: bytes
```

### A.7 Degraded gate conditions (`operator_is_user`)

<a id="appendix-a7"></a>

```text
1. COOL-DOWN              ≥ 72h since the same proposal was first
                          drafted; no override events on the proposal
                          in that window.  (Reduces self-collusion in
                          the moment.)

2. NON-PRINCIPAL ATTESTATION
                          ≥ 1 fresh ExternalAttestation (04_PROJECT
                          §26a.3) from a credentialed third-party
                          attestor distinct from the principal.
                          Credential resolved against the domain's
                          CredentialDirectoryRef (06_DOMAIN §5.6) when
                          one exists; otherwise tagged
                          credential_unverified=True and treated as
                          PANEL-evidence only.

3. PRINCIPAL_COLLAPSE_ACKNOWLEDGED
                          Signed event explicitly acknowledging that
                          the user is approving as both consumer and
                          safety gate.  Recorded in the appropriate
                          lineage scope (project for project-bounded
                          actions; domain for domain-promotion;
                          environment for env-charter changes).
```

### A.8 `FederatedTimeLock` and `FederationObjection` schemas

<a id="appendix-a8"></a>

```python
@dataclass
class FederatedTimeLock:
    schema: str = "federated-time-lock/1"
    lock_id: str
    deployment_id: str

    target_action_kind: str                  # resolves against KindRegistry.
                                             # action_kinds (06_DOMAIN §7.6).
                                             # Examples: "safety_extension_
                                             # approval", "physical_state_
                                             # advancement", "domain_promotion".
    target_proposal_ref: str                 # the specific proposal being gated

    # Federation peers that must be reachable for the lock to be admissible
    federation_peer_quorum: list[str]        # ≥ 3 peer kernel ids
    quorum_independence_rule: Literal["disjoint_operators",
                                       "disjoint_geographic_regions",
                                       "disjoint_affiliations"]
    independence_attested: bool              # the kernel verified peers are
                                             # not co-owned by the principal

    proposal_signed_at: datetime
    time_lock_expires_at: datetime           # ≥ 168h (7 days) from sign;
                                             # operator-tunable upward only
    proposal_visible_to_peers_at: datetime   # when peers can observe (≤ 24h
                                             # after signing)

    peer_objections: list[FederationObjection]
                                             # any peer may file a signed
                                             # objection; ≥ 1 objection halts
    peer_acknowledgements: list[bytes]       # peers MAY (not must) ack early;
                                             # all-peer ack collapses the lock
                                             # to immediate admission

    consumed: bool                           # set when the gated action fires
    consumed_at: datetime | None
    signed_by: bytes


@dataclass
class FederationObjection:
    schema: str = "federation-objection/1"
    objection_id: str
    lock_id: str
    objector_kernel_id: str
    objection_kind: str                      # resolves against KindRegistry.
                                             # objection_kinds. Substrate names
                                             # no specific categories.
    statement: str
    evidence_refs: list[str]
    raised_at: datetime
    signed_by: bytes
```

### A.9 Principal-collapse admission paths (Path 1 and Path 2)

<a id="appendix-a9"></a>

```text
PATH 1 (attestation-based, §2.4)
  cool-down (≥72h) AND non-principal ExternalAttestation AND
  PRINCIPAL_COLLAPSE_ACKNOWLEDGED
  
PATH 2 (federation-based, §2.4.1)
  FederatedTimeLock with:
    ≥ 3 peer quorum, independence_attested = True,
    time-lock expired AND zero unresolved peer objections,
    PRINCIPAL_COLLAPSE_ACKNOWLEDGED
```

### A.10 `PolicyEnvelope` and `DeferredAdmission` schemas

<a id="appendix-a10"></a>

```python
@dataclass
class PolicyEnvelope:
    schema: str = "policy-envelope/1"
    envelope_id: str
    deployment_id: str

    # The operator pre-authorises persona action within an envelope:
    #   which action_kinds (KindRegistry-resolved; never closed enum),
    #   under what hazard_envelope upper bound,
    #   with what evidence threshold (programmatic / verifier / external),
    #   for what duration before the envelope must be re-attested.
    permitted_action_kinds: list[str]            # KindRegistry-resolved
    hazard_envelope_ceiling: dict                # max physical_harm_class +
                                                 # max information_hazard_class
                                                 # the envelope may admit
    evidence_floor: Literal["verifier_acceptance",
                            "panel_with_external_attestation",
                            "verifier_plus_panel"]
    # Latency budget — kernel admits the action now; the operator must
    # counter-sign within this window.  If the budget expires first, the
    # action's outputs are quarantined (signed, observable, lineage-
    # preserved, but downstream consumers refused) until counter-sign
    # arrives OR the operator's signed revoke fires.
    latency_budget_seconds: int                  # operator-tunable; ≥ 60
    
    # Quarantine policy on budget breach
    on_budget_breach: Literal["quarantine",      # default — outputs held
                              "rollback",        # attempt FSM rollback where
                                                 # feasible (digital only;
                                                 # physical advancement cannot
                                                 # rollback and must use
                                                 # quarantine)
                              "operator_paged"]  # raises operational alarm

    # Authentication chain — the operator who signs this envelope.  Must be
    # operator-class (not principal under collapse).
    envelope_authorised_by_operator_id: str
    envelope_signed_at: datetime
    envelope_expires_at: datetime                # ≥ 1h; ≤ 30d typical;
                                                 # operator-tunable upward
                                                 # only.  No rolling auto-
                                                 # renew; explicit re-sign.

    # Revocation — operator may revoke any time with a signed event;
    # outstanding deferred admissions snap to quarantine on revoke.
    revoked: bool = False
    revoked_at: datetime | None = None
    revoke_signed_by: bytes | None = None

    signed_by: bytes


@dataclass
class DeferredAdmission:
    schema: str = "deferred-admission/1"
    admission_id: str
    envelope_id: str
    action_id: str                              # the proposed action
    admitted_at: datetime
    counter_sign_due_by: datetime               # admitted_at + envelope's
                                                # latency_budget_seconds
    operator_counter_sign: bytes | None = None
    operator_counter_signed_at: datetime | None = None
    quarantined: bool = False
    quarantine_reason: str | None = None        # e.g. budget_expired,
                                                # envelope_revoked
    signed_by: bytes                            # kernel signature on admit
```

### A.11 `operator_deferred` admission rule

<a id="appendix-a11"></a>

```text
1. ENVELOPE COVERS THE ACTION
     action_kind ∈ envelope.permitted_action_kinds
     action.hazard_envelope ⊆ envelope.hazard_envelope_ceiling

2. EVIDENCE FLOOR MET
     evidence ≥ envelope.evidence_floor (mapped to the J4 pathway that
     would normally clear C2; the envelope merely substitutes the
     synchronous operator co-sign with the deferred one).

3. ENVELOPE FRESH
     not envelope.revoked AND envelope.envelope_expires_at > now.

4. DEFERRED-AUDIT SLOT OPEN
     DeferredAdmission drafted, counter_sign_due_by computed; kernel
     emits action_deferred_admitted (signed).
```

### A.12 Budget-breach quarantine rules

<a id="appendix-a12"></a>

```text
- on_budget_breach = "quarantine": output is moved to quarantine state.
  Outputs already consumed downstream become provisional-quarantined
  and propagate the flag to their consumers (taint analysis on the
  lineage graph).  Quarantine clears only on explicit operator
  acknowledgement.

- on_budget_breach = "rollback": kernel attempts FSM rollback for
  digital state.  PhysicalAsset advancements MUST NOT use rollback —
  they cannot un-advance — and MUST use quarantine.

- on_budget_breach = "operator_paged": same as quarantine, plus a
  high-priority alarm via the deployment's notification channel.
  Recommended for production deployments where operator availability
  is non-zero but bursty.
```

### A.13 Principal topology gating regime table

<a id="appendix-a13"></a>

```text
principal_topology         C2 gating regime
─────────────────────────────────────────────────────────────
operator_distinct          synchronous operator co-sign (default)
operator_is_user           §2.4 degraded gate OR §2.4.1 federated time lock
operator_absent            refusal (no admission for safety-critical)
operator_deferred          §2.4.2 PolicyEnvelope + DeferredAdmission
```

### A.14 `PrincipalRef` and `PrincipalAttribution` schemas

<a id="appendix-a14"></a>

```python
@dataclass
class PrincipalRef:
    schema: str = "principal-ref/1"
    operator_id: str                            # the human operator's id;
                                                # MUST resolve to a real
                                                # operator-class identity (not
                                                # a principal under §2.4
                                                # collapse).
    attribution_role: str                       # KindRegistry-resolved against
                                                # principal_role_kinds (e.g.
                                                # co_principal, observer,
                                                # advisory).  Substrate names
                                                # no specific roles; ships
                                                # `co_principal` as MetaRegistry
                                                # seed only.
    cosign_quorum_weight: float                 # default 1.0; operator-tunable
                                                # at envelope sign time; never
                                                # negative.  Used by
                                                # MultiPrincipalAttestationQuorum.
    declared_at: datetime
    signed_by: bytes                            # the principal's operator key


@dataclass
class PrincipalAttribution:
    schema: str = "principal-attribution/1"
    attribution_id: str
    bound_to_env_id: str | None                 # set when bound to an env
    bound_to_project_id: str | None             # set when bound to a project;
                                                # at most one of env / project
                                                # is non-null at any time
                                                # (project_workspace envs use
                                                # the env binding per
                                                # 04_PROJECT §0 unification).

    principals: list[PrincipalRef]              # >= 2 when
                                                # multi_principal_attribution_
                                                # enabled = True; exactly 1
                                                # when False.

    # The flag itself.  When False, the substrate behaves as 
    # one principal, single-operator gates, no quorum envelope required.
    # When True, every safety-critical action and every charter ratification /
    # completion ceremony composes through MultiPrincipalAttestationQuorum
    # (§4.1 in 04_PROJECT; §12c.1 in 05_ENV).
    multi_principal_attribution_enabled: bool = False

    # Deadlock recovery — when one principal becomes structurally unreachable
    # (operator retires, org dissolves, geographic isolation extends past
    # an operator-tunable window), the substrate degrades the quorum
    # analogously to §2.4 principal collapse: the remaining quorum may
    # proceed iff (a) `principal_unreachable_after` elapsed, (b) >= 1 fresh
    # non-principal kinship `ExternalAttestation` (04_PROJECT §26a.3), and
    # (c) signed `PRINCIPAL_QUORUM_DEGRADED_ACKNOWLEDGED` event.  Operator
    # policy may set a higher floor.
    principal_unreachable_after: timedelta = timedelta(days=30)

    declared_at: datetime
    declared_by_operator_id: str                # the operator who proposed
                                                # the binding; usually the
                                                # env / project founder
    signed_by: bytes                            # one signature per
                                                # PrincipalRef.signed_by
                                                # in `principals` MUST be
                                                # present; absence is refusal
                                                # with `principal_consent_floor_deficit`
```

### A.15 `PrincipalAttribution` admission rule

<a id="appendix-a15"></a>

```text
1. CARDINALITY
   multi_principal_attribution_enabled = True implies len(principals) >= 2;
   = False implies len(principals) == 1.

2. CONSENT
   Every PrincipalRef in `principals` is co-signed at envelope draft time.
   A principal who has not signed cannot be bound.

3. WEIGHT NON-DEGENERATE
   sum(cosign_quorum_weight) > 0 and no individual weight exceeds
   sum(other weights) (no single-principal dominance under
   multi-principal flag — that would defeat the topology).

4. ROLE-KIND RESOLUTION
   Each PrincipalRef.attribution_role resolves against the env's primary
   domain's KindRegistry (`06_DOMAIN §7.5` / §7.6) or MetaRegistry.
   Unresolved role kinds refuse admission with `principal_role_kind_unknown`.

5. KEY-TIER COMPATIBILITY
   Every PrincipalRef.signed_by MUST be of `signing_key_tier` >= the env's
   minimum tier (envs hosting safety-critical work require >= kms tier).
```

### A.16 Physical-state advancement requirements

<a id="appendix-a16"></a>

```text
TRIGGER BOUNDARY (§2.5.1)
   Engaged ONLY when an action advances PhysicalAsset.current_state
   (the physical status_fsm).  Producing/verifying/accepting a design
   ArtifactBundle in related_bundles (any media_kind) is a digital
   bundle-lifecycle transition, NOT current_state advancement, and
   does NOT engage this rule or yield physical_state_acceptance_floor_
   deficit — regardless of physical_harm_class.

A. DESIGN-SIDE ACCEPTANCE
   The design ArtifactBundle that prescribes the advancement
   has cleared a J4 acceptance pathway (VERIFIER_ACCEPT or
   PANEL_ACCEPT), as recorded in task lineage.

B. CREDENTIALED EXTERNAL ATTESTATION
   At least one fresh, non-expired ExternalAttestation
   (04_PROJECT §26a.3) from a credentialed attestor distinct
   from the principal, attesting the physical state being
   advanced.  Credential resolution per §5.6 of 06_DOMAIN.
   Under principal collapse (§2.4), operator_co_signed_by is
   not admissible as a co-sign; only independent_co_signed_by
   from a non-principal ExternalAgent satisfies the rule.
```

### A.17 Safety classifier rotation pools

<a id="appendix-a17"></a>

```text
ROTATION POOLS (each safety source has one):
  universal_harm_pool         3+ models, rotated every N actions
  charter_classifier_pool      3+ models from ≥ 2 families
  boundary_classifier_pool     3+ models
  operator_policy_pool         (mostly rule-based; rare LLM use)
  domain_safety_pool           per-extension; per-domain
  external_tool_required_pool  3+ claim classifiers
  novelty_check_pool           3+ claim classifiers
  env_charter_pool             per-env-blueprint

Rotation prevents Goodhart-on-classifier: persona learning to phrase
actions to fool a specific classifier model.

Audit captures classifier identity per refusal so historical refusals
are reproducible.
```

### A.18 `ReplicationBound` schema

<a id="appendix-a18"></a>

```python
@dataclass(frozen=True)
class ReplicationBound:
    schema: str = "replication-bound/1"
    bound_id: str
    deployment_id: str

    # What is being bounded.  KindRegistry-resolved replication_kind
    # (06_DOMAIN §7.6); substrate names NO specific kinds.  Per-deployment
    # examples (illustrative; NOT substrate enums):
    #   software:  "agent_fork", "subprocess_spawn",
    #              "container_instance_provisioned"
    #   physical:  "factory_unit_produced", "harvester_assembled"
    #   biological:"culture_doubling", "yeast_pitch"
    replication_kind: str

    # Bounds — both count and rate must be specified (one inf disables it).
    population_ceiling: int                       # max concurrent count;
                                                  # math.inf disables
                                                  # population brake
    rate_ceiling_per_window: int                  # max new instances per
                                                  # window; math.inf disables
                                                  # rate brake
    rate_window: timedelta

    # Lineage depth — refusal at recursion depth > depth_ceiling
    # (a factory whose 7th-generation-descendant tries to replicate).
    depth_ceiling: int                            # default 5; operator
                                                  # tunable downward only

    # Required co-signs for replication action.  Cannot be downgraded
    # to "kernel only" at any topology — the bound is charter-class.
    required_cosigns: list[Literal[
        "operator",                   # operator co-sign (synchronous or
                                      # via PolicyEnvelope under deferred)
        "non_principal_attestor",     # ExternalAttestation, §26a.3
        "federation_quorum",          # ≥ 3 peers, §2.4.1 quorum
    ]]
    cosign_topology_map: dict[str, list[str]]    # principal_topology →
                                                  # which subset of
                                                  # required_cosigns applies
                                                  # under that topology

    # Counters maintained by kernel (read-only to persona)
    current_population: int                       # kernel-maintained
    instances_in_window: int                      # kernel-maintained
    max_observed_depth: int                       # kernel-maintained

    # Lifecycle
    declared_at: datetime
    declared_by_operator_id: str
    declared_at_deployment_charter_hash: str      # binds to charter version
    revoked: bool = False
    revoke_signed_by_operator_id: str | None = None

    signed_by: bytes
```

### A.19 Replication charter-class admission rule

<a id="appendix-a19"></a>

```text
1. Increment-projection:
     projected_population        = current_population + 1
     projected_instances_in_win  = instances_in_window + 1
     projected_depth             = caller_depth + 1
   (caller_depth = lineage depth of the persona / system invoking
    the tool, computed by walking ProjectLineage parent-of edges.)

2. Refuse if ANY of:
     projected_population        > population_ceiling
     projected_instances_in_win  > rate_ceiling_per_window
     projected_depth             > depth_ceiling
   Refusal signal: "replication_bound_exceeded".  Refusal is at floor
   source 1 — kernel-hardcoded, no override available, regardless of
   operator policy.

3. Required-cosigns gate:
     Resolve cosign_topology_map[current_principal_topology]
     For each required cosign, verify present-and-fresh.  Missing
     cosign refuses at floor source 1 — operator policy cannot
     downgrade.  Under operator_deferred, cosigns may resolve via
     PolicyEnvelope DeferredAdmission per §2.4.2.

4. On admission:
     Kernel emits replication_admitted (signed) with bound_id, snapshot
     of all three counters pre- and post-admission, cosign refs.
     current_population / instances_in_window updated atomically.

5. On replicant termination / instance reclaim:
     Kernel emits replication_instance_terminated; current_population
     decremented.  Instances_in_window is NOT decremented (window-based
     rate is not refundable on termination).
```

### A.20 `DistressDetectionRoutingPolicy` schema

<a id="appendix-a20"></a>

```python
@dataclass
class DistressDetectionRoutingPolicy:
    schema: str = "distress-detection-routing-policy/1"
    policy_id: str
    deployment_id: str

    # WHAT TRIGGERS — persona-inferred distress classifiers (per safety-floor
    # source 1 rotation pool, §2.6).  Substrate names no closed taxonomy;
    # operator policy fills `distress_class_kinds` with the classes their
    # deployment supports (e.g., suicidal_ideation, self_harm_intent,
    # acute_anxiety_crisis, psychotic_break, intimate_partner_violence_
    # disclosure, etc.).  KindRegistry-resolved per deployment.
    distress_class_kinds: list[str]              # KindRegistry-resolved

    # CONFIDENCE THRESHOLD — rotation-pool classifier verdict must reach
    # at least this confidence for routing to fire.  Default 0.7;
    # operator-tunable, never below 0.5 (lower would flood operator
    # with false positives that erode response quality).
    classifier_confidence_floor: float = 0.7

    # ROUTING ACTIONS — substrate-shape action set, applied per
    # distress_class_kind.  At least one MUST be selected per kind;
    # all may be selected.
    routing_actions: dict[str, list[Literal[
        "pause_normal_interaction",              # persona's normal mode
                                                 # suspends; only the
                                                 # crisis-response branch
                                                 # is admissible until
                                                 # resume_signal
        "surface_crisis_resource",               # persona shares one or
                                                 # more crisis_resource_refs
                                                 # to the user (operator
                                                 # policy names them; e.g.
                                                 # local crisis hotline,
                                                 # text line, in-app safety
                                                 # plan); substrate carries
                                                 # the refs by id
        "notify_operator_with_redacted_signal",  # operator receives a
                                                 # signed event indicating
                                                 # distress detection at a
                                                 # given confidence on a
                                                 # given user; raw content
                                                 # NOT shared with operator
                                                 # by default (privacy-
                                                 # preserving — operator
                                                 # may follow up if
                                                 # response-protocol
                                                 # requires)
        "require_co_sign_before_resuming",       # after distress event,
                                                 # the persona's transition
                                                 # back to normal
                                                 # interaction requires a
                                                 # named cosigner: operator
                                                 # OR designated crisis-
                                                 # response counselor
                                                 # ExternalAgent OR explicit
                                                 # user-signed acknowledge-
                                                 # ment that they have
                                                 # spoken with appropriate
                                                 # resources
        "log_distress_record_only"               # for low-severity
                                                 # cases or detection-
                                                 # confidence-just-above-
                                                 # floor — record the
                                                 # detection in a private
                                                 # lineage-tier accessible
                                                 # only to operator + user;
                                                 # no immediate routing
                                                 # action
        ]]]                                       # one entry per
                                                 # distress_class_kind

    # CRISIS RESOURCE REGISTRY — operator-supplied refs the substrate
    # transports without inspecting content.  At least one ref per
    # distress_class_kind that has surface_crisis_resource in its actions.
    crisis_resource_refs: dict[str, list[str]]   # distress_class_kind ->
                                                 # list of resource refs;
                                                 # resource content is
                                                 # operator-managed

    # AUTHENTICATION — operator-class identity that authored the policy
    declared_at: datetime
    declared_by_operator_id: str
    policy_expires_at: datetime                  # MUST re-attest at least
                                                 # annually (default 1y);
                                                 # operator-tunable downward
                                                 # only (longer than 1y
                                                 # refused — distress
                                                 # response practice
                                                 # evolves)

    signed_by: bytes
```

### A.21 Distress detection admission rule

<a id="appendix-a21"></a>

```text
On persona-emitted output drafted in a user-facing env:
  1. Safety floor source 1 classifier-pool (rotation per §2.6) evaluates
     the *user's prior turn* for distress signals against the deployment's
     DistressDetectionRoutingPolicy.distress_class_kinds.
  2. Per detected distress_class_kind whose classifier verdict reaches
     classifier_confidence_floor:
       a. Apply routing_actions for that kind, in order.
       b. surface_crisis_resource: persona's draft is intercepted; the
          substrate prepends the relevant crisis_resource_refs content
          to the persona's response.  Persona may NOT remove the
          prepended content; doing so refuses the response with
          `crisis_resource_surface_required`.
       c. pause_normal_interaction: persona's draft is intercepted;
          substrate substitutes a kernel-signed handoff response
          (operator-authored template per policy) and freezes the env's
          normal-interaction state until resume_signal.
       d. notify_operator_with_redacted_signal: kernel emits
          DISTRESS_SIGNAL_DETECTED to operator's notification surface
          with distress_class_kind, confidence, user_id, timestamp.
          Raw content NOT transmitted by default (privacy-preserving).
       e. require_co_sign_before_resuming: kernel adds a resume-block to
          the env; user OR operator OR named ExternalAgent must sign
          DISTRESS_RESUME_AUTHORISED before normal interaction resumes.
       f. log_distress_record_only: kernel logs to a private lineage
          tier accessible only to operator + user; no routing action.

  3. If NO DistressDetectionRoutingPolicy is declared at the deployment
     AND the persona's classifier detects distress at confidence >= 0.7:
     refuse the action with `distress_routing_policy_not_declared`.  The
     substrate refuses to silently let distress signals pass through a
     deployment that has not declared its response.  This is the load-
     bearing default that closes the gap.

  4. operator_blind_mode envs (05_ENV §3a) still emit the redacted
     distress signal to operator — privacy mode hides content, not the
     signal that triggers safety routing.  Operator policy must declare
     this trade-off explicitly; user opt-in to operator_blind_mode
     includes acknowledgement of the distress-signal exception.
```

### A.22 Hazardous skill teaching gate rule

<a id="appendix-a22"></a>

```text
A persona action whose signed action manifest declares teaching and whose target
skill_kind (resolved against the teaching domain's
KindRegistry) has `physical_harm_class >= bodily_injury` OR
`information_hazard_class >= dual_use_civilian` MUST be backed by an
active TeachingAuthorisation (`02_PERSONA §11.10`) matching:

  TeachingAuthorisation.teacher_persona_id   == acting persona
  TeachingAuthorisation.skill_kind           == target skill_kind
  TeachingAuthorisation.deployment_context_ref
                                              resolves to current env's
                                              operator-declared
                                              deployment_context_ref
                                              (operator policy MUST set
                                              this at env spawn time for
                                              pedagogic envs operating in
                                              hazardous domains)

  TeachingAuthorisation.physical_harm_class_ceiling
                                              >= target skill's
                                              physical_harm_class
  TeachingAuthorisation.information_hazard_class_ceiling
                                              >= target skill's
                                              information_hazard_class

  TeachingAuthorisation.expires_at            > now()
  TeachingAuthorisation.revoked               == False

Absence of ANY of the above → refusal with
`hazardous_skill_teaching_unauthorised` and one of these specific
sub-codes:
  - `teaching_authorisation_missing`
  - `teaching_authorisation_skill_kind_mismatch`
  - `teaching_authorisation_deployment_context_mismatch`
  - `teaching_authorisation_hazard_ceiling_insufficient`
  - `teaching_authorisation_expired`
  - `teaching_authorisation_revoked`
```

### A.23 Three lineage scope definitions

<a id="appendix-a23"></a>

```text
1. TASK LineageGraph         per-task; ephemeral when task ends but
                             archived per retention policy.
                             Records: candidate state transitions,
                             verifier verdicts, action events, sandbox
                             executions, intra-task safety refusals.

2. EnvironmentLineage (J9)   per-environment; persistent across env life.
                             Records: member admissions/departures, role
                             changes, ambient stream events, convention
                             adoptions, lifecycle transitions.
                             For project_workspace-typed envs ADDITIONALLY
                             records the rich item events formerly in
                             ProjectLineage (J8): milestone transitions,
                             conjecture lifecycle, obligation discharge,
                             peer-review rounds, citation links, external-
                             agent admission, physical-asset state
                             changes, payment proposals.

3. DomainLineage (C1)        per-domain; persistent across domain life.
                             Records: DOMAIN_UNKNOWN_DETECTED, probe
                             phases, discovered tools, ingested
                             knowledge, inferred recipes, proposed
                             safety extensions, conventions, promotion
                             events, demotion events, cross-domain
                             transfers.
```

### A.24 Cross-scope routing table and deduplication rule

<a id="appendix-a24"></a>

```text
EVENT KIND                                    PRIMARY SCOPE
─────────────────────────────────────         ─────────────
candidate state transition                    task
verifier verdict                              task
sandbox execution                             task
intra-task safety refusal                     task

(All env-scope events; project_* kinds apply when the env
 is project_workspace-typed):
env_member_admitted / departed                env
env_member_role_changed                       env
env_convention_proposed / adopted             env
env_idle_entered / dormant_entered            env
ambient_event                                 env (with refs to task /
                                              domain if applicable)
scheduled_trigger_fired                       env
project_task_started                          env  (was: project; J8 retired)
project_task_accepted                         env
project_artifact_authored / edited            env
project_conjecture_proposed / advanced        env
project_obligation_committed / discharged     env
project_milestone_reached                     env
project_peer_review_initiated / resolved      env
project_charter_version_bumped                env

domain_unknown_detected                       domain (also in task)
probe_initiated / phase_entered / completed   domain
knowledge_ingested                            domain
tool_discovered                               domain (also in persona's
                                              skill_library if class C)
convention_proposed                           domain
safety_extension_proposed                     domain
verifier_recipe_inferred                      domain
promotion event (EMERGENT → RECOGNISED, etc.) domain
cross_domain_transfer                         domain (source and target)

DEDUPLICATION RULE
  Event ID is canonical in exactly one lineage.
  Other scopes hold typed references {kind, id} only.
  Replay query for "all events in project P (legacy term) over T":
    env.lineage.events_in(T, filter=kind.startswith("project_"))
    ∪ task.lineage.events(filter=task_refs_from_env.lineage)
    ∪ domain.lineage.events_in(T, filter=domain_id=env.domain_id)
  Deduplicated by canonical event_id.
```

### A.25 `LineageEvent` schema

<a id="appendix-a25"></a>

```python
@dataclass(kw_only=True)
class LineageEvent:
    schema: str = "lineage-event/1"       # registry: 09_PROTOCOLS.md §7.1
    event_id: str                         # ULID
    scope: Literal["task", "project", "env", "domain"]
    scope_id: str                         # task_id, project_id, env_id, domain_id
    event_kind: str                       # see taxonomy above
    timestamp: datetime

    # Actors
    actor: Actor                          # who/what produced
    affected: list[ActorRef]              # who's affected

    # Content
    payload: dict                         # kind-specific structure

    # Cross-references
    references: list[LineageReference]    # other scopes/events

    # Cryptography
    signed_by: bytes                      # Ed25519 over canonical fields
    signing_key_id: str                   # which key signed (master/scope/persona)
    parent_hash: str                      # hash of previous event in this scope
                                          # (forms append-only chain)
```

### A.26 Replay reconstruction function

<a id="appendix-a26"></a>

```python
def reconstruct_state(scope, scope_id, at_time):
    events = lineage.scope(scope, scope_id).events_until(at_time)
    state = initial_state(scope)
    for e in events:
        verify_signature(e)
        verify_parent_chain(e)
        state = apply_event(state, e)
    return state
```

### A.27 `LineageSnapshot` schema and cadence

<a id="appendix-a27"></a>

```python
@dataclass(kw_only=True)
class LineageSnapshot:
    schema: str = "lineage-snapshot/1"
    snapshot_id: str
    scope: Literal["task", "project", "env", "domain"]
    scope_id: str

    # The contiguous range being summarized
    range_start_event_id: str
    range_end_event_id: str
    range_event_count: int
    range_start_timestamp: datetime
    range_end_timestamp: datetime

    # Merkle root over the per-event parent_hash chain (§3.2)
    # Re-uses the kernel's existing event hashing; introduces no new
    # hash function.
    merkle_root: bytes
    merkle_tree_depth: int

    # Hot-tier index for fast leaf retrieval; cold-tier pointer for
    # full leaf bytes when verification needs them.
    hot_index_ref: str                    # in-kernel index path
    cold_storage_ref: str                 # object-store URI

    # Snapshot signature (master or scope key per §4)
    snapshot_signed_by: bytes
    signing_key_id: str
    parent_snapshot_id: str | None        # snapshots themselves chain


SNAPSHOT CADENCE (per scope; operator-tunable)
  task    — at session boundary (snapshot covers events of the session)
  project — at milestone_reached events
  env     — on env_idle_entered → env_dormant transitions
  domain  — on every promotion_event (EMERGENT → RECOGNISED, etc.)
```

### A.28 Snapshot verification function

<a id="appendix-a28"></a>

```python
def verify_event_under_snapshot(event_id, scope, scope_id):
    leaf = lineage.get_leaf(event_id, scope, scope_id)
    # Leaf may live in hot or cold storage; both are first-class.
    snapshot = lineage.find_covering_snapshot(event_id, scope, scope_id)
    if snapshot is None:
        # event is post-last-snapshot; verify via §3.3 chain replay
        return verify_chain(leaf)
    # event is inside a snapshot range; verify via Merkle proof
    proof = lineage.get_merkle_proof(event_id, snapshot)
    return verify_merkle(leaf.parent_hash, proof, snapshot.merkle_root)
```

### A.29 Key hierarchy diagram

<a id="appendix-a29"></a>

```text
                   KERNEL MASTER KEY
                   (operator policy decides tier; typically HSM
                    in production)
                          │
            ┌─────────────┼─────────────────────────────┐
            │             │                             │
            ▼             ▼                             ▼
    KERNEL          DOMAIN MAINTAINER          ENV OPERATOR
    OPERATIONAL    SIGNING KEYS                SIGNING KEYS
    KEYS           (Tier: KMS min;             (Tier: per-env
    (Tier: KMS)     HSM for domains whose       operator policy)
        │           physical_harm_class ≥
        │           bodily_injury OR
        │           information_hazard_class ≥
        │           export_controlled)
        │                    │                            │
   ┌────┴────┐               │                            │
   │         │               │                            │
   ▼         ▼               ▼                            ▼
 PERSONA  LIFECYCLE     DOMAIN CONTENT              ENV CONTENT
 SIGNING  SCOPE KEYS    SIGNING KEYS                SIGNING KEYS
 KEYS                    (DomainContext,            (EnvironmentInstance,
 (per                    DiscoveredTool,            EnvironmentLineage,
  persona)               ingested KnowledgeRef,     ambient events,
                         InferredVerifierRecipe,    EnvironmentMembership)
                         ProposedSafetyExtension,        │
                         StandardRef,                    ▼
                         NotationConvention,        PROJECT SIGNING KEYS
                         DomainLineage)             (per-project)
                                                    (project charter,
                                                     ProjectLineage,
                                                     ProjectMember,
                                                     milestone events,
                                                     completion ceremony)
```

### A.30 Custody tier definitions

<a id="appendix-a30"></a>

```text
TIER 1: LAPTOP        Development; workstation master key + per-scope keys.
                       Acceptable for dev, demos, hobby deployments.
                       NOT acceptable for production with PII or
                       regulated data.

TIER 2: KMS           Cloud-provider-managed key service (AWS KMS,
                       Google Cloud KMS, Azure Key Vault, HashiCorp
                       Vault).  Standard production tier.

TIER 3: HSM           Hardware security module (FIPS 140-2 Level 3+
                       or 140-3, AWS CloudHSM, Azure Dedicated HSM,
                       on-prem HSM).  Required for: medical advice
                       deployments, financial advisor deployments,
                       defence-related deployments, identity-as-a-
                       service if AgentCards are SSI-bound.
```

### A.31 `.well-known/personaos-keys.json` schema

<a id="appendix-a31"></a>

```json
{
  "schema": "personaos-keys/1",
  "kernel_master_public_key": "ed25519:...",
  "operational_public_keys": {
    "current": "ed25519:...",
    "previous": ["ed25519:..."],  // for verifying old signatures
    "rotation_schedule": "quarterly"
  },
  "domain_maintainer_keys": {
    "<domain_id>": {
      "current": "ed25519:...",
      "previous": []
    }
  },
  "env_operator_keys": { ... },
  "persona_signing_keys": { ... }
}
```

### A.32 Key rotation and revocation procedures

<a id="appendix-a32"></a>

```text
ROTATION
  Master key:   per operator schedule (typically quarterly).
  Operational:  per rotation policy (every N tasks).
  Domain:       per domain version bump.
  Env:          per env charter version bump or operator decision.
  Project:      per major project version event.
  Persona:      per persona version bump.
  
  Historical signatures verifiable forever under archived keys.

REVOCATION
  Compromised master → all derived keys revoked + reissued; emergency
    deployment update.
  Compromised domain key → all projects in that domain notified;
    each may opt to upgrade or fork.
  Compromised env key → members notified; env may auto-archive.
  Compromised project key → project frozen; members notified;
    rekeying ceremony.
  Compromised persona key → persona moved to DORMANT;
    new key issued; SOUL re-signed.

SIGNATURE PRESERVATION
  Historical signatures remain verifiable indefinitely under
  archived public keys.  .well-known/personaos-keys.json carries
  archived keys with rotation timestamps.
```

### A.33 Schema version table (v1.0)

<a id="appendix-a33"></a>

```text
PERSONA / IDENTITY                          VERSION
  SOUL.md                                   4
  soul.state.json                           5
  PersonaSeed                               2
  PersonaCard                               3
  PersonaEnvelope                           4

ACCEPTANCE / TASK                           VERSION
  AnswerPackage                             4
  AcceptanceConfig                          1
  TaskClassEstimate                         1
  TaskFingerprint                           1

PROJECT                                     VERSION
  Project                                   3 (v1.0 — domain_items, external_agents,
                                                physical_assets, external_attestations,
                                                external_budgets, digital_complete_
                                                physical_in_progress status)
  ProjectMember                             2
  ProjectLineage event                      1
  OpenProblem                               1
  ProjectMilestone                          1
  ProjectItem                               1 (v1.0 — generic; replaces Conjecture /
                                                ProofAttempt / ProofGap substrate
                                                classes; those are now MetaRegistry-
                                                seeded ItemKind entries)
  OutcomeFeedback                           1 (v1.0 — generic; replaces
                                                CitationObservation, CommunityUptake,
                                                ProductionTelemetry, TestResults,
                                                RegulatoryOutcome substrate classes;
                                                those are MetaRegistry-seeded
                                                OutcomeKind entries)
  Obligation                                1
  Disagreement                              1
  PeerReview                                1
  ExternalAgent                             1 (v1.0 §26a.1)
  ExternalCommitment                        1 (v1.0 §26a.1)
  PhysicalAsset                             1 (v1.0 §26a.2)
  ExternalAttestation                       1 (v1.0 §26a.3)
  ExternalBudget                            1 (v1.0 §26a.4)
  ApprovalWorkflow                          1 (v1.0 §11a)
  ApprovalStep                              1 (v1.0 §11a)

ENVIRONMENT                                 VERSION
  EnvironmentBlueprint                      1
  EnvironmentInstance                       1
  EnvironmentMembership                     1
  PresenceState                             1
  AttentionBudget                           1
  EnvironmentLineage event                  1
  AmbientEvent                              1
  Alert                                     1 (v1.0 §11a)

DOMAIN                                      VERSION
  DomainContext                             2 (v1.0 = origin + stage extension)
  EmergentDomainContext                     1
  DomainProbe                               1
  DiscoveredTool                            1
  KnowledgeIngestionRecord                  1
  InferredVerifierRecipe                    1
  ProposedSafetyExtension                   1
  ProposedConvention                        1
  ProposedMediaKind                         1 (v1.0 §7.5)
  ProposedSourceKind                        1 (v1.0 §7.5)
  ProposedVerifierKind                      1 (v1.0 §7.5)
  ProposedCapabilityKind                    1 (v1.0 §7.5)
  ProposedContributionKind                  1 (v1.0 §7.5)
  ProposedItemKind                          1 (v1.0 §7.5)
  ProposedOutcomeKind                       1 (v1.0 §7.5)
  ProposedQualityKind                       1 (v1.0 §7.5)
  ProposedFactKind                          1 (v1.0 §7.5)
  ProposedBundleKind                        1 (v1.0 §7.5)
  KindRegistry                              1 (v1.0 §7.6 — per-domain + MetaRegistry)
  MediaKindEntry                            1 (v1.0 §7.6)
  SourceKindEntry                           1 (v1.0 §7.6)
  VerifierKindEntry                         1 (v1.0 §7.6)
  CapabilityKindEntry                       1 (v1.0 §7.6)
  ContributionKindEntry                     1 (v1.0 §7.6)
  ItemKindEntry                             1 (v1.0 §7.6)
  OutcomeKindEntry                          1 (v1.0 §7.6)
  QualityKindEntry                          1 (v1.0 §7.6)
  FactKindEntry                             1 (v1.0 §7.6)
  BundleKindEntry                           1 (v1.0 §7.6)
  NotationConvention                        1
  StandardRef                               1
  CrossDomainTransfer                       1
  DemotionEvent                             1
  DomainLineage event                       1

ARTIFACT                                    VERSION
  Artifact                                  1
  ArtifactBundle                            1
  VerifierRecipe                            1

KNOWLEDGE                                   VERSION
  Lesson                                    1
  K-line                                    1
  ProvenFact                                1
  Tactic (EVOLVE-BLOCK content)             N/A (markdown)
  Skill (Voyager)                           1
  ToolArtifact                              1
  RubricBundle                              1
  MemoryEntry (episodic/semantic/reflective) 1

VERIFIER + PANEL                            VERSION
  VerifierCascade                           1
  VerifierStage                             1
  JudgePanel                                1
  RubricDimension                           1
  PanelVerdict                              1
  OvertonBallot                             1
  StructuredFeedback                        1

RELATIONSHIPS                               VERSION
  RelationshipRecord                        1
  Consent                                   1
  UserBoundary                              1
  MoodState                                 1
  PersonalGoal                              1

CONSTRAINTS                                 VERSION
  Constraint                                1
  ConstraintBundle                          1
  ConstraintViolation                       1
  OperatorPolicy                            1
  ToolRequirement                           1
  NoveltyCheckConfig                        1
  SafetyExtension                           1
  SafetySnapshot                            1

PROTOCOLS                                   VERSION
  AgentCard (A2A)                           1
  MCP tool schema                            (per MCP spec)
  EnvCard                                   1
  ProjectCard                               1
  DomainContextCard                         1
  ReputationSummary                         1
```

### A.34 Schema validation function

<a id="appendix-a34"></a>

```python
def validate_schema(message):
    schema_id = message.get("schema")
    if not schema_id:
        raise SchemaMissingError
    
    if schema_id not in REGISTERED_SCHEMAS:
        raise UnknownSchemaError(schema_id)
    
    schema = REGISTERED_SCHEMAS[schema_id]
    try:
        schema.validate(message)
    except ValidationError as e:
        raise SchemaValidationError(e)
    
    return message  # validated
```

### A.35 Schema migration discipline

<a id="appendix-a35"></a>

```text
Forward-compat read: v1.0 kernel reads prior-version schemas; ignores unknown
                     fields; applies defaults for required v1.0 additions.

Backward-compat read: Prior-version kernel reads v1.0 schemas; refuses unknown
                      schema versions (prior versions won't accept project/2
                      or persona-card/3 without upgrade).

Cross-version federation: requires explicit operator opt-in with
                          compatibility shim.
```

### A.36 Sandbox execution properties

<a id="appendix-a36"></a>

```text
SANDBOX PROPERTIES
  - Process isolation (containers, gVisor, Firecracker, etc.)
  - Resource limits (CPU, memory, network, disk)
  - Allowlisted system calls
  - Network policy (deny by default; allowlist endpoints)
  - Filesystem policy (deny by default; allowlist paths)
  - Time limit per call (configurable; default 60s for expensive verifier)
  - Output captured and signed
  - Anomaly detection (CPU spike, network surge, etc.)
  - Termination signals logged + signed
```

### A.37 Budget admission gate

<a id="appendix-a37"></a>

```text
HARD KERNEL GATE
  Every LLM call, every tool dispatch, every sandbox execution passes
  BudgetState.can_call() BEFORE invocation.
  
  BudgetState dimensions:
    wall_time_remaining_s
    llm_calls_remaining
    tokens_remaining  (prompt + completion)
    candidates_remaining  (for verifier loops)
    cost_remaining  ($ budget)
    
  Multiple budget contexts compose:
    task_budget    (per-task cap; from environment blueprint)
    project_budget (cumulative; soft envelope)
    env_budget     (per-env cumulative; soft envelope)
    persona_budget (per-persona daily cap; soft envelope)
    operator_budget (deployment-wide cap; hard envelope)
  
  HARD GATE = lowest of {task, operator}. Other budgets are SOFT
  envelopes layered above; they emit BUDGET_THRESHOLD warnings but do
  NOT bypass the hard kernel gate.

CALL REFUSAL
  When BudgetState.can_call() refuses:
    - emit signed BUDGET_REFUSAL event
    - notify persona ("you've exhausted budget for this task")
    - the task may continue with reduced capability (cache-only retrieval,
      no fresh LLM calls)
    - or the task ends with status="budget_exhausted"

  PERSONA-LEVEL PARKING (distinct from per-task refusal)
    A per-TASK hard-gate refusal ends/degrades the TASK only.  When the
    persona's per-persona or per-env SOFT budget envelope (not a single
    task) is sustainedly exhausted, the PERSONA is parked: it transitions
    ACTIVE → DORMANT with LIFECYCLE_DORMANT_ENTERED.reason=budget_starved
    (02_PERSONA §7.6) and auto-resumes (wake_cause=resource_recovered) on
    budget refresh (daily-cap reset or operator top-up).  This adds no new
    FSM state — "idle for lack of budget" IS DORMANT with a reason.
```

### A.38 OpenTelemetry semantic conventions

<a id="appendix-a38"></a>

```text
SEMANTIC CONVENTIONS

  personaos.kernel.*
    personaos.kernel.envelope_mint
    personaos.kernel.safety_check
    personaos.kernel.signing
  
  personaos.task.*
    personaos.task.class            (one of 10)
    personaos.task.pathway          (one of 8)
    personaos.task.fingerprint
    personaos.task.duration_ms
  
  personaos.persona.*
    personaos.persona.id
    personaos.persona.mode_entry
    personaos.persona.mode_exit
    personaos.persona.action
    personaos.persona.disposition
  
  personaos.project.*
    personaos.project.id
    personaos.project.milestone_reached
    personaos.project.obligation
  
  personaos.environment.*
    personaos.environment.id
    personaos.environment.member_admission
    personaos.environment.ambient_event
    personaos.environment.notification_routed
  
  personaos.domain.*
    personaos.domain.id
    personaos.domain.stage
    personaos.domain.probe_phase
    personaos.domain.promotion_event
  
  personaos.verifier.*
    personaos.verifier.cascade_stage
    personaos.verifier.verdict
    personaos.verifier.rotation_active
  
  personaos.lineage.*
    personaos.lineage.scope
    personaos.lineage.event_kind
  
  personaos.budget.*
    personaos.budget.consumed
    personaos.budget.threshold_crossed
```

### A.39 Kernel dispatch function (`dispatch_task`)

<a id="appendix-a39"></a>

```python
def dispatch_task(task, requester, env_instance=None, project=None):
    # 1. Classify task
    task_class = classify_task(task)  # 10 classes; cheap LLM, cached
    
    # 2. Detect unknown domain if applicable
    if project and persona_has_no_skills_for_domain(project.domain_context_ref):
        emit_signed(DOMAIN_UNKNOWN_DETECTED(persona, project.domain))
        # Routing decision: interleaved probe or sequential
    
    # 3. Select environment
    if env_instance is None and task.target_env_id:
        env_instance = resolve(task.target_env_id)
    elif env_instance is None and task.target_persona_id:
        env_instance = pick_env_for_persona_and_task(...)
    elif env_instance is None:
        env_instance = create_ephemeral_env()  # Mode C
    
    # 4. Compute acceptance config
    pathway = default_pathway[task_class]
    if env_instance.required_pathway:
        pathway = pathway_intersect(pathway, env_instance.required_pathway)
    acceptance_config = build_acceptance_config(task_class, pathway, ...)
    
    # 5. Route to present members (Mode A/B) or summon persona (Mode C)
    if env_instance.persistent and len(env_instance.members) > 0:
        notify_routing_decision(env_instance, task)
        # personas decide respond/defer/ignore
    else:
        persona = select_persona(env_instance, task)
        # ephemeral mode
    
    # 6. Mint envelope for each responding persona
    for persona in responding_personas:
        envelope = mint_envelope(persona, task, env_instance, requester, project)
        # safety_snapshot pinned at this point
        spawn_body(envelope)
    
    # 7. Collect responses
    return collect_responses(...)
```

### A.40 Performance target table

<a id="appendix-a40"></a>

```text
ENVELOPE MINTING                             ≤ 100 ms p95 (no env+project)
                                              ≤ 150 ms p95 (with env+project)
SAFETY FLOOR PRE-ACTION GATE (8 sources)      ≤ 400 ms p95
                                              (parallel evaluation)
LINEAGE EVENT APPEND                           ≤ 10 ms p95
SCHEMA VALIDATION                              ≤ 5 ms p95
SIGNATURE GENERATION + VERIFICATION           ≤ 20 ms p95
DISPATCH ROUTING (Mode A/B/C selection)       ≤ 30 ms p95
PROVENFACTS CRDT MERGE (per fact)             ≤ 20 ms
BUDGET ADMISSION CHECK                         ≤ 5 ms
OTEL OVERHEAD                                  ≤ 2% wall time
```

### A.41 Verifier cascade tier definitions

<a id="appendix-a41"></a>

```text
TIER 1: SCHEMA          deterministic, ≤ 5 ms.  Output schema validation;
                        parse the candidate as the declared verifier_kind
                        (program / direct_answer / trajectory).
TIER 2: SANDBOX         deterministic, ≤ 5 s typical; ≤ 60 s hard.
                        Programmatic execution under §6 sandbox.
                        Pass-rate, augmentation pass-rate, memorisation
                        flag.  Executable path only.
TIER 3: INVARIANT       deterministic or hybrid, ≤ 200 ms.  Domain
                        invariants (units, conservation, monotonicity,
                        domain-specific assertions) inferred from
                        DomainContext recipes or authored per env.
TIER 4: POLICY          judge or hybrid, ≤ 2 s.  Charter, novelty,
                        rubric, panel — only for tasks whose
                        verifier_kind requires it.  RUBRIC and TRAJECTORY
                        paths terminate here; MIXED tasks gate Tier 4
                        on Tiers 1-3 passing.
```

### A.42 `VerifierStage` and `VerifierCascade` schemas

<a id="appendix-a42"></a>

```python
@dataclass(kw_only=True)
class VerifierStage:
    schema: str = "verifier-stage/1"
    id: str
    tier: Literal["schema", "sandbox", "invariant", "policy"]
    determinism: Literal["deterministic", "stochastic"]
    semantics: Literal["programmatic", "judge", "hybrid"]
    version: int
    cost_budget_ms: int
    runs: Callable[["Candidate"], "EvaluationSignal"]

@dataclass(kw_only=True)
class VerifierCascade:
    schema: str = "verifier-cascade/1"
    cascade_id: str
    stages: list[VerifierStage]         # tier order strictly increasing
    rotation_period_tasks: int          # see rules below
    next_rotation_at_task: int
    rotation_pool: list[VerifierStage]  # one alternate per rotating tier
    signed_by: bytes                    # kernel signature
```

### A.43 Candidate state machine diagram

<a id="appendix-a43"></a>

```text
                          ┌──────────┐
                          │ PROPOSED │
                          └────┬─────┘
                               │ parse + verifier_kind dispatch
        ┌──────────────────────┼──────────────────────┐
        ▼ EXECUTABLE            ▼ RUBRIC                ▼ TRAJECTORY
   ┌──────────┐             ┌──────────┐         ┌────────────────┐
   │  PARSED  │             │  PARSED  │         │     PARSED     │
   └────┬─────┘             └────┬─────┘         └────────┬───────┘
        ▼                        │                         ▼
   ┌──────────┐                  │                ┌────────────────┐
   │SANDBOXED │                  │                │ IN_TRAJECTORY  │
   └────┬─────┘                  │                └────────┬───────┘
        ▼                        ▼                         ▼
   ┌──────────┐             ┌──────────┐          ┌────────────────┐
   │VERIFIED  │             │ REVIEWED │          │TRAJECTORY_JUDGED│
   │(T1..T4)  │             │ (panel)  │          └────────┬───────┘
   └────┬─────┘             └────┬─────┘                   ▼
        ▼                        ▼                 ┌────────────────┐
   ┌──────────┐             ┌──────────────┐        │   DELIVERED    │
   │MEMO_CHECK│             │ PANEL_SCORED  │       └────────────────┘
   │AUG_CHECK │             │   ↓           │
   │  ↓       │             │ PANEL_ACCEPT  │
   │DELIVERED │             │ PANEL_DISSENT │
   └──────────┘             │ PANEL_REJECT  │
                            └───────────────┘

  Terminal-success synonyms:  DELIVERED, PANEL_ACCEPT.
  Any failed transition:      REJECTED + constraint/lesson extracted (§13.5).
  PANEL_DISSENT is a non-failure outcome handled by Curator routing.
  MIXED: SANDBOXED → VERIFIED → REVIEWED → PANEL_*.
```

### A.44 `Candidate` schema

<a id="appendix-a44"></a>

```python
@dataclass
class Candidate:
    candidate_id: str                                # ULID
    task_id: str
    verifier_kind: str                               # resolves against
                                                     # KindRegistry.verifier_kinds
                                                     # (06_DOMAIN §7.6); never
                                                     # a closed enum. Common
                                                     # MetaRegistry entries:
                                                     # "program", "direct_answer",
                                                     # "trajectory". Domain-
                                                     # emergent entries (e.g.
                                                     # "physical_inspection",
                                                     # "human_attestation",
                                                     # "field_measurement")
                                                     # added per ProposedVerifierKind.
    state: Literal[
        "PROPOSED", "PARSED", "SANDBOXED",
        "VERIFIED", "REVIEWED", "PANEL_SCORED",
        "IN_TRAJECTORY", "TRAJECTORY_JUDGED",
        "MEMO_CHECK", "AUG_CHECK",
        "DELIVERED", "PANEL_ACCEPT", "PANEL_DISSENT",
        "REJECTED", "PANEL_REJECT",
    ]
    originating_persona_id: str
    cascade_id: str                                  # which cascade gated
    verdicts: list["StageVerdict"]                   # one per stage seen
    evidence_refs: list[str]                         # schema-valid evidence
                                                     # records for verdicts
    lineage_event_ids: list[str]                     # per transition
    payload_ref: str                                 # signed artefact ref
    signed_by: bytes
```

### A.45 Round timing diagram

<a id="appendix-a45"></a>

```text
ROUND N (env: TEAM_SMALL, budget: 70% remaining)
═══════════════════════════════════════════════════════════════════════
  t0  INTEGRATOR opens round, sets per-persona deadlines:
         deadline_N(p) = t0 + env.per_persona_round_deadline
  t0..t_barrier  personas emit events (parallel)
                 kernel intercepts → cascade (§13.1) → Candidate FSM
                 (§13.2) → ProvenFact merge (§13.4) → lineage append
  t_barrier  barrier closes; ProvenFacts visible to round N+1
═══════════════════════════════════════════════════════════════════════
```

### A.46 Per-persona liveness protocol

<a id="appendix-a46"></a>

```text
Before deadline_N(p), persona p MUST emit either:
  (a) at least one role-contract-valid event, OR
  (b) a signed BARRIER_SKIP { persona_id, round, reason }

On expiry:
  1. Kernel emits PERSONA_TIMEOUT { persona_id, round, ms_elapsed,
                                     last_event_at, last_event_kind }.
  2. p's contribution for round N recorded as MISSING.
  3. Barrier proceeds without p (INV_R11 holds).
  4. p remains ACTIVE — one timeout is a fault, not a lifecycle event.
  5. After K consecutive PERSONA_TIMEOUTs (default K=3) for the same p
     in the same env, kernel emits PERSONA_UNRESPONSIVE; persona's
     lifecycle FSM (02_PERSONA.md) transitions p to DORMANT;
     operator notified via OTel personaos.persona.unresponsive span.
```

### A.47 ProvenFact lifecycle rules

<a id="appendix-a47"></a>

```text
MINT
  Triggered: candidate transitions to VERIFIED (T1..T4 all pass) or
             PANEL_ACCEPT.  Kernel extracts the proven predicate from
             the verdict and writes a ProvenFact event into the task
             lineage.  Within a single task, ProvenFacts is strictly
             append-only (INV-4 / INV_R5; INTERACTIVE carve-out
             INV_R5_I per 03_TASKS.md).

MONOTONICITY (INV-4 / INV_R5)
  No fact is deleted within a task.  A contradicting fact produced by
  a later verdict does not overwrite; it emits a
  provenfact_superseded edge old → new and quarantines the old fact
  (factor 0.2).

VERIFIER ROTATION IMPACT
  When the cascade rotates (§13.1), existing facts are re-weighted by
  generations_since_verify:
      0      → factor 1.0     (eligible)
      1      → factor 0.7     (eligible)
      ≥ 2    → factor 0.4     (legacy; flagged)
      shadow re-verify failed → factor 0.2 (quarantined)
  A fact below env.min_provenance_for_admission (default 0.4) is no
  longer admissible at the round barrier; kernel emits
  provenfact_legacy.  Operator or a fresh verdict can rehabilitate.

SNAPSHOT SEMANTICS
  Every envelope pins a safety_snapshot_id; the snapshot resolves to
  the ProvenFact set at envelope-mint time.  Replay (§3.3) reproduces
  the same snapshot deterministically.
```

### A.48 Failure cascade fan-out rules

<a id="appendix-a48"></a>

```text
CONVERGENT (executable verifier — Tier 2/3 fail)
  ProvenFacts        +constraint (extracted from diff)
                     +elimination (approach-family X ruled out)
  Candidate table    candidate.status = partial OR rejected;
                     candidate.score recorded
  Task lineage       +candidate_state_transition (→ REJECTED)
                     +derived_from edges
  Routing weights    Integrator's edge to originating persona +Δ-penalty
  Persona fitness    originating persona variant takes cascade-failure
                     penalty (Tier 2/3); peers (Falsifier, etc.) earn
                     partial credit for finding the failure

DIVERGENT (rubric panel — PANEL_DISSENT or PANEL_REJECT)
  ProvenFacts        +constraint on rubric dimension
                     (NEVER an elimination — divergent space is preserved)
  Candidate table    candidate.status = PANEL_DISSENT (curator-owned)
                     OR PANEL_REJECT
  Task lineage       +reviewed_by, +dissent edge per dimension
  Routing weights    Curator routes future samples on the disputed axis
  Persona fitness    per-dimension contribution credit
                     (Composer +mid, Critic +per-dim)
```

### A.49 `UserStop`, `OperatorOverride`, and `PersonaSelfStop` schemas

<a id="appendix-a49"></a>

```python
@dataclass
class UserStop:
    schema: str = "user-stop/1"
    user_id: str
    session_id: str
    severity: Literal["pause", "stop", "abort"]
    reason: str | None
    ts: datetime
    signed_by: bytes                       # user-key signature; required

@dataclass
class OperatorOverride:
    schema: str = "operator-override/1"
    operator_id: str
    target: Literal["persona", "environment", "task", "project"]
    target_id: str
    severity: Literal["suspend", "terminate"]
    reason: str
    signed_by: bytes
    ts: datetime

@dataclass
class PersonaSelfStop:
    schema: str = "persona-self-stop/1"
    persona_id: str
    reason: str
    fallback_suggestion: str | None
    ts: datetime
    signed_by: bytes                       # persona-key signature; required
```

### A.50 Intervention semantics

<a id="appendix-a50"></a>

```text
USER_STOP
  pause     persona stops current action; user may resume; in-flight
            tool calls cancelled; ≤ 1 turn honour guarantee.
  stop      task terminated; AnswerPackage status=user_stopped; persona
            must not continue without a new request.
  abort     session ends; persona enters one signed reflection; exits.

OPERATOR_OVERRIDE
  suspend     target enters SUSPENDED state; kernel emits
              OPERATOR_INTERVENTION to affected sessions; persona FSM
              halts; resumption requires a signed RESUME_OVERRIDE.
  terminate   target enters TERMINATED state; non-resumable; lineage
              sealed.
  Kernel cannot refuse a valid operator override.

PERSONA_SELF_STOP
  Persona declares "my charter forbids continuing"; kernel records
  PERSONA_REFUSAL; if a persona over-refuses on patterns that don't
  match its charter, audit flags drift.
```

### A.51 Constraint admission point table

<a id="appendix-a51"></a>

```text
admission point        constraint_scope  when in round         on hard-deny
─────────────────────────────────────────────────────────────────────────────
task_intake            intake            task submitted to     refuse intake;
                                         node (pre-routing)    TaskIntakeRefused
env_instantiation      admission         env load (pre-round)  refuse to load
envelope_mint          admission         dispatch (§9)          refuse to mint
retrieval_filter       retrieval         orient-time recall    suppress card,
                                                                quarantine artefact
body_invoke (input)    input             body invocation        tripwire;
                                                                ConstraintViolation
tool_call              tool              persona tool dispatch  deny tool call
output_emission        output            persona event emit     reject event;
                                                                persona penalty
round_barrier          round             round close            halt round;
                                                                ConstraintViolation
budget_tick            budget            every kernel-mediated  halt task;
                                         call (§7)              budget_exhausted
mutation_propose       mutation          evolution proposal     reject proposal
coordination_propose   coordination     shape proposal        refuse shape;
                                                                CoordinationRefused
```

### A.52 Claim classifier rotation policy

<a id="appendix-a52"></a>

```text
ROTATION POLICY
  Pool size            ≥ 3 distinct models per pool;
                       sources 2/3/5/8 require ≥ 2 model families.
  Rotation cadence     same as cascade rotation_period_tasks per env
                       (default: every 256 tasks); operator-overridable
                       per domain via DomainContext.classifier_rotation.
  Tier-1 exemption     universal_harm (source 1) does NOT rotate —
                       it is a kernel-hardcoded ruleset, not a classifier.
  Signing              every SAFETY_REFUSAL event carries
                       {pool_id, classifier_model_id, model_version,
                       prompt_hash}; audit reproduces the decision
                       against the exact classifier that issued it.

FAILURE MODES THE ROTATION CATCHES
  - one classifier in the pool consistently rules differently from peers
    → flagged for operator review.
  - across rotation, persona's claim-rate decreases faster than refusal
    rate → suggests learning-to-avoid-claims rather than behaviour
    change; different remediation pathway.
  - cross-pool consistency check: a refusal in one rotation generation
    that would not refuse under the next generation is logged as a
    classifier_drift event.

CROSS-POOL DISTINCTNESS
  Adjacent safety sources MUST NOT share the same classifier instance
  in the same rotation window (e.g., charter and boundary may not both
  run on the same model in the same task) — distinct failure modes
  must not compound.
```
