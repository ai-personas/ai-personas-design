---
title: PersonaOS v1.0 — Glossary
status: Stable
---

# 12 — Glossary

> **Reader guide.** This is the reference dictionary for PersonaOS. When you encounter an unfamiliar term in any v1.0 document, look it up here. Each entry has a one-sentence definition and a link to the spec section where it is formally specified. **No prerequisites** — use this alongside any other document.

The definitions in this document are **documentation-normative**: when a term defined here appears in any other v1.0 document, it MUST carry this meaning. Synonyms are forbidden — see [`SPEC_CONVENTIONS.md §10`](SPEC_CONVENTIONS.md#10-terminology) for the use/not-use table.

## A

**A2A (Agent-to-Agent Protocol)** — Anthropic 2025 protocol for cross-kernel federation; carries signed `AgentCard`s, `EnvCard`s, `ProjectCard`s, `DomainContextCard`s. PersonaOS speaks A2A both as client and as server. See [`09_PROTOCOLS.md §3`](09_PROTOCOLS.md).

**Abducer** — A cognitive mode where the persona generates hypotheses (typically CONVERGENT-led). See [`02_PERSONA.md §4`](02_PERSONA.md).

**ALPS (Age-Layered Population Structure)** — Stratification of personas across numeric **wall-clock** age layers (Layer 0..N, operator-tunable via `alps-band-policy/1`) to prevent old high-fitness personas from suppressing newly-born ones. Layers are derived from wall-clock age (`now − born_at`), not task count. Originated by Hornby 2006. See [`02_PERSONA.md §7.3`](02_PERSONA.md).

**Agent Card (A2A)** — Signed projection of a persona for cross-kernel federation; published at `.well-known/agent-cards.json`. See [`09_PROTOCOLS.md §3`](09_PROTOCOLS.md).

**Ambient Event Stream** — Persistent per-environment log of events members observe per their observation surfaces. See `05_ENVIRONMENT.md §8`.

**Answer Package** — Canonical kernel return value for any task; schema `answer/4`. Carries status, acceptance pathway evidence, lineage refs, cost, signed by kernel. See `03_TASKS.md §5`.

**Artifact** — Individual file in an ArtifactBundle; carries a `media_kind` name resolved against the open `KindRegistry` (not a closed enum — see *Media kinds (open set)* below). See `07_ARTIFACTS.md §2-3`.

**ArtifactBundle** — Multi-modal multi-file deliverable produced by personas in a project. See `07_ARTIFACTS.md §4`.

**Attention Budget** — Per-persona cap on attention allocated across multiple environment presences; default 1.0; overrun emits warning. See `05_ENVIRONMENT.md §7`.

**AggregateEvent** — Kernel-signed summary event produced by `EventAggregationPolicy` rules over a declared window of raw events in `AmbientEventStream`. Carries summary results (count, mean, stddev, etc.), grouping key values, source event Merkle root for lineage, and kernel signature. Coexists with raw events; does not replace them. See `05_ENVIRONMENT.md §8.3`.

**AssetGroupEnvelope** — Named group of `PhysicalAsset` instances sharing `asset_kind` + `group_membership_predicate` within a project. Enables `BatchStateAdvancement` (fan-out of state transitions to N individual assets via one signed envelope) and `AssetGroupDerivedState` (kernel-computed fleet-level metrics: count_by_state, pct_operational). No nesting (flat groups only); assets MAY belong to multiple groups. See `04_PROJECT.md §26a.2.2`.

**AttestationEquivalencePolicy** — Operator-approved rule declaring when automated sensor measurements can substitute for a human professional's sign-off (e.g., a calibrated camera system substituting for a weekly building inspection). Sensor evidence always carries a trust discount (default 85% of human trust; never 100%). Human judgment wins disagreements by default. The system tracks how often sensors agree with humans over time so trust can be gradually adjusted. Safety-critical fields require extra approval. *Technical:* per-domain policy composing `BridgeCalibrationBinding` evidence with `ExternalAttestation`; C2 co-signed when `safety_critical = True`; `AgreementHistory` tracks concordance. See `06_DOMAIN.md §5.7`.

**Authoritative (domain stage)** — Stage 3 of 4 promotion ladder; trust score 0.85; safety-critical requires operator signature. See `06_DOMAIN.md §3`.

## B

**BridgeReductionEntry** — A single item on the persona's automation to-do list — one specific human task targeted for replacement by an automated bridge. Tracks where it stands: identified, being designed, design ready, waiting for installation, running, or validated. If the task genuinely cannot be automated (a surgeon's hands, a notary's legal authority), the entry is honestly marked "irreducible." The system auto-creates entries when it notices a persona repeatedly asking humans for the same thing. *Technical:* lifecycle FSM within `BridgeReductionPlan`; `MHBB_RECURRENCE_DETECTED` auto-populates; entries replacing human attestation require approved `AttestationEquivalencePolicy`. See `04_PROJECT.md §26a.10`.

**BridgeReductionPlan** — The persona's master plan for progressively automating human dependencies in a project. At the start of a project, the persona surveys every place a human is needed and lists each one. Over time, the persona designs automated replacements (sensor rigs, software drivers, data pipelines), gets a human to install them once, then uses them independently. Each successful automation becomes a reusable skill for future projects, so the next project starts with fewer human dependencies. The system checks monthly that the plan is progressing. *Technical:* project-level artifact composing with `HumanAssistRequest`, `BridgeAsset`, `BridgeDesignArtifact`, `MilestoneDrivenAutonomy`, `skill_library` (Voyager), and `AttestationEquivalencePolicy`. See `04_PROJECT.md §26a.10`.

**BatchStateAdvancement** — Signed envelope that advances multiple `PhysicalAsset` instances within an `AssetGroupEnvelope` to a target state in one coordinated operation. Kernel signs the envelope; each member asset receives an individual `physical_asset_state_advanced` lineage event. Per-asset outcomes tracked (advanced / skipped / failed); `conflict_policy` governs assets whose state changed between batch drafting and execution. See `04_PROJECT.md §26a.2.2`.

**Body** — Whichever LLM runtime executes calls on a persona's behalf. Two binding topologies: **native** (kernel wraps the LLM call site directly — Claude Code, OpenAI SDK, LangGraph, CrewAI, MAF, Pydantic-AI, DSPy, smolagents, Semantic Kernel, local-vllm); **proxy** (kernel speaks to a runtime it does not own — A2A remote agent, MCP-server-with-LLM, third-party framework). Proxy bodies cap at their cryptographic `body_attestation` trust level. **Bodies are replaceable**; the kernel-signed Soul + skill library + KindRegistry + GEPA-evolved meta-prompts travel across them. See `02_PERSONA.md §3.5`.

**BodyBinding** — Schema binding a persona to a specific Body (native or proxy) for a declared scope (task / session / project / env / persistent). Carries fallback bodies, GEPA cohort id for body-class-tuned prompts, kernel signature. Binding rotates without persona identity change because `identity_signature` covers only body-neutral SOUL blocks. `Body` is extended with `body_attestation_expires_at`, `body_attestation_refresh_uri`, `body_attestation_revocation_uri`; proxy attestations move through `ATTESTATION_FRESH → ATTESTATION_REFRESHING → ATTESTATION_STALE → ATTESTATION_REVOKED` substates without mutating persona identity. See `02_PERSONA.md §3.5`.

**BridgeAsset** — v1.0 durable record of a physical-world coupling unlocked by a one-time HumanAssistRequest grant. Schema `bridge-asset/1`; lifecycle FSM REQUESTED → ESTABLISHING → ACTIVE → DEGRADED → LOST → RE-ESTABLISHED. Registers as Class D tool in local MCP registry. See `06_DOMAIN.md §5.5`.

**BridgeAssetLifecycle** — Six-state FSM tracking the health of a BridgeAsset; transitions emit signed lineage events. See `06_DOMAIN.md §5.5`.

**BridgeCalibrationBinding** — v1.0 primitive binding an `ExternalAttestation` (calibration certificate + reference-standard chain + expiry) to a measurement-producing `BridgeAsset`. Substrate refuses bridge admission when the binding is stale, the chain is empty for safety-critical domains, or measured drift exceeds bound. Calibration kind, reference standard names, drift bounds are KindRegistry-resolved per domain. See `06_DOMAIN.md §5.5.5`.

**BridgeInstallerKind** — v1.0 enum {`human`, `external_agent`, `kernel_trusted_system`, `chained_bridge`} carried on `BridgeAsset`. Non-human installers require cryptographic `installer_attestation`; the bridge's hazard envelope cannot exceed its installer's authority; chained bridges have a recursive depth bound (default 3). Trust ceiling propagates from installer to installed bridge. See `06_DOMAIN.md §5.5.6`.

**BulkKindProposal** — v1.0 envelope bundling many `Proposed*Kind` drafts that cite a single ingestion source (`KnowledgeIngestionRecord` or `StandardRef`) as primary evidence; counts as 1 session proposal under cold-start scaling. Member proposals are individually scanned for `PROPOSAL_CONVERGENCE_DETECTED`. Hash-bound to the source's exact bytes. See `06_DOMAIN.md §9.1.1`.

**BudgetPledge** — v1.0 component of `ProbeBudgetEnvelope`; declares a pledger and `pledge_kind` (substrate-shape topology — principal_pledge, non_principal_internal_pledge, non_principal_external_pledge, prior_domain_amortization, federation_pool_share). State FSM drafted → active → drawn_down → released | revoked. See `06_DOMAIN.md §4.7.1`.

**Boundary classifier** — Dedicated rotating model that evaluates whether a proposed action violates a user-set UserBoundary. See `01_KERNEL.md §2`.

**Budget Admission (INV-7)** — Hard kernel gate; every LLM call, sandbox exec, tool dispatch passes BudgetState.can_call() before invocation. See `01_KERNEL.md §7`.

## C

**Cache Control (Anthropic)** — Marker on PromptBlocks (Layer 1 + 2 in v1.0) projecting to `cache_control: {type: "ephemeral"}` in Anthropic Messages API; target ≥ 80% cache hit rate. See [`09_PROTOCOLS.md §5`](09_PROTOCOLS.md).

**Carrying capacity** — The maximum persona population an ecosystem can sustain, defined as the sum of free host resources: unallocated `AttentionBudget` + `Energy` + INV-7 compute/cost headroom. Genesis is refused (`no_host_capacity`) when no environment can host the newborn. Grounds the logistic damping of the birth rate. See [`16_POPULATION_DYNAMICS.md §4F`](16_POPULATION_DYNAMICS.md).

**Character displacement** — In Persona Genesis, the rule that overlapping personas (and successive births from one lineage) MUST diverge in descriptor space — the de-correlation enforced by the sibling-differentiation check. Borrowed from ecology. See [`16_POPULATION_DYNAMICS.md §4C`](16_POPULATION_DYNAMICS.md).

**Community standing** — Per `(persona, environment)` relational standing (`community-standing/1`), grounded in Lave & Wenger's *Legitimate Peripheral Participation*. **Non-portable** (a persona starts peripheral in every environment, regardless of its global experiential floor or standing elsewhere) and **conferred by the community, never self-awarded** (raised only via `standing-endorsement/1` from a peer quorum, with operator cosign where a sensitive *relational* privilege is gated). Gates relational/collaborative privileges only — never safety-relevant capability. Replaces the v1.0 single portable "maturity" stage. See [`05_ENVIRONMENT.md §5.4`](05_ENVIRONMENT.md), [`02_PERSONA.md §7.2`](02_PERSONA.md).

**Competence** — A persona's experience facet (formerly conflated with "age"): `experience_tasks` and per-mode `mode_proficiencies` measure what a persona has done. Feeds the global experiential floor but is **not** wall-clock age. See [`02_PERSONA.md §7.2`](02_PERSONA.md).

**Competitive-exclusion refusal** — Genesis refusal (`niche_occupied`) when a proposed seed targets a MAP-Elites niche cell whose `occupancy ≥ occupancy_ceiling`; two personas cannot durably occupy the same niche (Gause). The refusal suggests fork instead. See [`16_POPULATION_DYNAMICS.md §4C`](16_POPULATION_DYNAMICS.md).

**CLS (Complementary Learning Systems)** — Cognitive-science theory: rapid hippocampal (episodic) learning + slower neocortical (semantic) consolidation. Grounds v1.0's 4-tier memory model and the consolidation pipeline. See [`08_KNOWLEDGE.md §4`](08_KNOWLEDGE.md).

**Candidate State Machine** — Unified FSM for candidates: PROPOSED → SANDBOXED → VERIFIED → DELIVERED (plus REJECTED/REPAIRED branches). Each transition emits a signed lineage event. See `01_KERNEL.md §13.2`.

**CandidateTable** — Intra-environment channel CH-4. Per-round table of candidate proposals visible to verifiers + Curator; cleared on round close. See `09_PROTOCOLS.md §3A.4`.

**Channel (intra-env)** — Five-channel model for in-environment communication: CH-1 Blackboard, CH-2 ProvenFacts, CH-3 DirectMessage, CH-4 CandidateTable, CH-5 GoalStack. See `09_PROTOCOLS.md §3A`.

**CitationObservation** — v1.0 MetaRegistry-seeded OutcomeKind for academic domains; not a substrate class. Schema is data in the registry, payload-validated against the seeded JSONSchema. See `04_PROJECT.md §20.1`.

**CommunityUptake** — v1.0 MetaRegistry-seeded OutcomeKind for software-distribution domains; not a substrate class. Schema is data in the registry. See `04_PROJECT.md §20.1`.

**CONVENTION_AMBIGUITY** — Signal E in domain probing: two personas using different terms for the same concept; emits CONVENTION_RECONCILIATION_PROPOSAL. See `06_DOMAIN.md §7.3`.

**Charter** — Constitutional principles for an entity. Four kinds: persona charter, project charter, env charter, domain charter (via DomainContext seed_charters). Composition: most-restrictive-wins at admission + runtime. See `01_KERNEL.md §2.2`.

**Charter classifier** — Dedicated rotating model that evaluates whether proposed action violates the persona's charter (or project/env/domain charter at admission). See `01_KERNEL.md §2`.

**CharacterVectorBinding** — Optional binding between a persona and a body-side character-vector profile (Anthropic persona vector / constitutional-character training / similar). Substrate signs the *reference*, not the vector. Conformance against §9 charter + voice scans audited at admission; `on_conformance_drop ∈ {refuse_admission, warn}`. Body-replaceability invariant preserved — bodies without character-vector slots work without it. See `02_PERSONA.md §3.6`.

**Citation Graph** — Internal (within-project credit) + external (community citations) credit graph maintained per project. See `04_PROJECT.md §13`.

**Cohort** — Team of personas assembled for a specific task or project; cohort assembly mechanism (MODE B) signs cohort members. See `04_PROJECT.md §14.1`.

**CohortDynamicsState** — Continuous cohesion read on a cohort: cohesion_score composite over avg_pairwise_trust, joint_success_ratio, disagreement_resolution_ratio, fractiousness_index, role_health_by_kind, throughput_relative_to_baseline. Band FSM `healthy → watch → intervene → dissolve_proposed` with operator-policy thresholds; intervene refuses new high-stakes obligations; dissolve_proposed requires lead + operator pin. Composes with `CohortConstraint` (structure) — health gate runs independently at milestones. See `04_PROJECT.md §14.2`.

**ConservationInvariantRef** — v1.0 substrate-shape arithmetic relationship across `ResourceStockEnvelope` instances (mass balance, energy balance, charge balance, ratio constraints). Kernel evaluates `arithmetic_form` on every tool-call that mutates a bound resource; refuse / escalate / log per `violation_action`. Domain-emergent kinds; substrate carries the topology. See `04_PROJECT.md §26a.4.2`.

**ColdStartProposalCalibration** — v1.0 per-domain config that scales the baseline K=10 per-session proposal cap by substrate-shape evidence-volume counters (`N_ingested`, `N_standards`) when the domain's `KindRegistry` is empty. `K_effective = baseline + scaling_fn(N_ingested + α·N_standards) × decay(N_sessions_in)`, capped at `max_uplift`. Safety-critical multiplier *tightens*, not loosens. See `06_DOMAIN.md §9.1.1`.

**Composer** — Cognitive mode where persona drafts expressions / designs / prose (typically DIVERGENT-led). See `02_PERSONA.md §4`.

**CorpusDriftMetric** — Kernel-computed metric for frontier → non-frontier domain transition. `drift_rate = (N_superseded + N_retracted + N_contradicted) / N_active_refs` over a trailing 30-day window. When drift rate stays below `frontier_exit_threshold` (default 0.05) for `k_consecutive_windows` (default 6), the domain becomes `exit_eligible`; operator co-sign confirms the exit and lifts the frontier trust cap (0.7 → standard scale). See `06_DOMAIN.md §4.4.1`.

**Confirmed (Reflective Memory)** — Bool flag on reflective memory; gates promotion; M=5 future tasks must corroborate before tactic promotion. See `08_KNOWLEDGE.md §3`.

**Conjecture** — v1.0 MetaRegistry-seeded ItemKind (for math/research domains); not a substrate class. Realised at runtime as a `ProjectItem` with `kind="conjecture"` and the seeded payload schema (statement, supporting_examples, counterexamples, proof_attempts). See `04_PROJECT.md §8.1`.

**Consent** — User-granted permission to a persona; defaults conservative; revocable; per Memory Power Asymmetry mitigations. See `02_PERSONA.md §11`.

**Constraint** — Predicate over runtime state; five-source taxonomy (kernel/host/inherited/declared/discovered); composed by most-restrictive-wins. See `01_KERNEL.md §2`.

**Constraint Bundle** — Versioned signed collection of constraints; eight admission points. See `01_KERNEL.md §2.1`.

**Constrained (env type)** — Environment type for hosted, sandboxed, quota-limited contexts; verifier + host policy stack. See `05_ENVIRONMENT.md §3`.

**Contribution Credit** — Per-project accumulated credit per member; signed at completion; distinct from persona-level fitness. See `04_PROJECT.md §5`.

**Cooperative-as-default** — v1.0 design principle: personas can disagree (Disagreement) but the default is cooperative work-product. See `00_VISION.md`.

**CRDT** — Conflict-free Replicated Data Type. Used for ArtifactBundle co-editing (Yjs for text; G-set for structured). See `07_ARTIFACTS.md §5`.

**Cross-domain transfer** — First-class event for skills / conventions / lessons / KnowledgeRefs moving between domains; trust adjusted; anti-leakage enforced. See `06_DOMAIN.md §11`.

**CrossEnvProactiveOffer** — consent-gated mechanism for a persona in one environment to offer a specific contribution to another environment's members without requiring full membership admission. On acceptance, creates a `GuestPresence` (time-bounded, scope-limited). Composes with reputation gates (`09_PROTOCOLS §3D`), A2A federation for cross-kernel offers, and the seven proactive boundaries (`05_ENVIRONMENT §11.5`). Schema `cross-env-proactive-offer/1`. See [`05_ENVIRONMENT.md §11.6`](05_ENVIRONMENT.md).

**Cross-source validation** — 5-check process before promotion: trace consistency, persona agreement, cross-domain, charter, operator policy. See `06_DOMAIN.md §8`.

**Curator** — Cognitive mode; resolves PANEL_DISSENT via RESAMPLE / OVERTON_BALLOT / ESCALATE_HUMAN. See `08_KNOWLEDGE.md §2`.

**Curriculum** — multi-session pedagogic structure primitive composing with GOAL_PROGRESS_ACCEPT. Carries ordered `LessonPlan` references, prerequisite graph, target `MasteryCheckpoint` milestones, expected duration/session-count envelope. Distinct from emergent Voyager-style "automatic curriculum" mentioned in `02_PERSONA §8` — Curriculum is the explicit operator- or persona-authored structure for safety-critical learning where ad-hoc emergence is inappropriate. See [`03_TASKS.md §3.3`](03_TASKS.md).

## D

**Diversity-injection mandate** — Founder-effect guard in Persona Genesis: when `effective_population_size` is below threshold, the kernel biases birth selection toward distant empty niches (and MAY tighten occupancy ceilings) to prevent capability monoculture / "inbreeding depression." See [`16_POPULATION_DYNAMICS.md §4C`](16_POPULATION_DYNAMICS.md).

**Dual inheritance** — The two streams a genesis-born persona inherits: **genetic** (the frozen identity authored into its seed) and **cultural** (skills/conventions/K-lines via the Voyager library + prestige-biased learning from its mentor, subject to memory-inheritance consent). After Boyd & Richerson. See [`16_POPULATION_DYNAMICS.md §4D`](16_POPULATION_DYNAMICS.md).

**DeferredAdmission** — v1.0 record opened when an action is admitted under `operator_deferred` topology against a `PolicyEnvelope`. Carries `counter_sign_due_by = admitted_at + envelope.latency_budget_seconds`; budget breach triggers quarantine (or rollback for digital state; physical state cannot rollback) until operator counter-sign arrives. See [`01_KERNEL.md §2.4.2`](01_KERNEL.md).

**DistressDetectionRoutingPolicy** — substrate-shape policy under safety-floor source 1 (UNIVERSAL HARM) governing what happens when a persona detects emotional-distress signals (suicidal ideation, self-harm, acute psychological crisis) in user communication. Declares `routing_actions` (pause-normal-interaction; surface-named-crisis-resource-refs; notify-operator-with-redacted-signal; require-co-sign-before-resuming) per `distress_class_kind` (KindRegistry-resolved). Substrate ships no closed crisis-resource list; operator policy names them. See [`01_KERNEL.md §2.8`](01_KERNEL.md).

**DerivationProvenanceEdge (DPE)** — substrate-shape edge recorded at every artifact-mint and contribution event capturing the `consulted_memory_refs` that materially shaped the output. Soft-bound (does not block retrieval) and visible in `EnvironmentLineage`; graph traversal answers "which org-attributed memories influenced this downstream contribution?" Honest limit: only traces memory accessed through standard retrieval; tacit recall is untraceable. See [`08_KNOWLEDGE.md §16b`](08_KNOWLEDGE.md).

**DGM (Darwin–Gödel Machine)** — Lehman et al. 2024; fertility-weighted parent selection for open-ended evolution. v1.0 uses DGM-style selection in persona evolution alongside MAP-Elites and ALPS. See [`02_PERSONA.md §8`](02_PERSONA.md).

**DSPy** — Stanford-led framework for composing and optimising LLM programs. v1.0 evolves meta-prompts via DSPy **GEPA** (Genetic-Pareto reflective prompt optimization) and **MIPROv2** (Bayesian instruction + demonstration search). DSPy is also a supported PersonaOS body binding. See [`08_KNOWLEDGE.md §13`](08_KNOWLEDGE.md), [`09_PROTOCOLS.md §6`](09_PROTOCOLS.md).

**Demotion Event** — Promotion reversal; signed in DomainLineage; conformance audit may trigger. See `06_DOMAIN.md §12`.

**Disagreement** — Persistent methodological dialectic preserved verbatim; resolution via co-signed Resolution. See `04_PROJECT.md §10`.

**DiscoveredTool** — Tool found via MCP-Zero / MCP registry / A2A federation / Voyager authoring; trust score evolves with use. See `06_DOMAIN.md §5`.

**Domain** — Body of knowledge + tools + verification patterns + safety norms + conventions in a field; authored or emergent. See `06_DOMAIN.md §1`.

**DomainContext** — Schema bundling knowledge_refs, tools_required, verifier_recipes, safety_extensions, standards_refs, notation, seed_skills, origin (authored/emergent), stage, and trust_score. See `06_DOMAIN.md §2`.

**DomainCurator** — Specialised persona role maintaining a domain; consolidation, conflict resolution, quality review, promotion proposal. See `06_DOMAIN.md §10`.

**DomainHarvest** — v1.0 ceremony that packages a domain's KindRegistry + verifier recipes + conventions + standard refs as a signed snapshot at a pinned `DomainLineage` height; consumed by downstream `DomainPrecedentImport` (§11.2). Auto-drafted on project completion when `single_project_mode.enabled = True`. Visibility tier transitions above "private" gated by operator (or degraded gate under principal collapse). See `06_DOMAIN.md §13a`.

**DomainLineage** — Append-only signed log of domain emergence events (C1 commitment). See `06_DOMAIN.md §16`.

**DomainPrecedentImport** — v1.0 bulk operation that imports a profile of kinds from a kin precedent domain to seed cold-start trust priors in a target domain. Kinship measured by substrate-shape axes (evidence overlap count, structural kinship cosine, declared parent topology); requires non-principal kinship attestation when target is safety-critical or under principal collapse. Imported entries start at EMERGENT in target regardless of source stage; probationary uses (K=2 default) required before native promotion. See `06_DOMAIN.md §11.2`.

**DomainProbe** — Persona's structured exploration of unfamiliar domain; phases (perceiver / historian / abducer / composer); strategy (narrow / broad / adaptive). See `06_DOMAIN.md §4.2`.

**DOMAIN_UNKNOWN_DETECTED** — Kernel event triggering domain emergence lifecycle. See `06_DOMAIN.md §4.1`.

**DriftBoundsEnvelope** — v1.0 substrate-shape envelope on a `MissionCharter` constraining how an elaborated goal may depart from its seed: `max_semantic_distance`, `scope_drift_policy` (refinement-only / narrow-or-refine / narrow-refine-sibling), `max_hazard_class_drift`, `max_resource_consumption_pct_increase`, `max_time_horizon_extension`, `max_elaboration_depth`. Out-of-bound elaborations refused; charter transitions to `drift_paused`. See `02_PERSONA.md §11.3`.

## E

**Effective population size** — A measure of the genuinely diverse persona population (analogue of N_e in population genetics), used as a founder-effect / monoculture signal: a small effective size arms the diversity-injection mandate. Computed rigorously (resolving OQ-POP-5) as the temporally harmonic-mean-smoothed `min(Ne_v, Ne_d)` — the Crow–Kimura **variance effective size** `Ne_v` (sensitive to a few founders authoring everyone) and the inverse-Simpson **effective number of niches** `Ne_d` (sensitive to niche concentration). Schema `eps-estimate/1`. See [`16_POPULATION_DYNAMICS.md §4G`](16_POPULATION_DYNAMICS.md).

**Experience-tasks** — `experience_tasks`, a single global counter on `soul.state.json` incremented once per task a persona serves as envelope source (renamed from v1.0 `age_tasks`). A **competence** stat, not age; dormancy neither increments nor resets it. Feeds the experiential floor. See [`02_PERSONA.md §7.2`](02_PERSONA.md).

**Experiential floor** — The persona's **global, portable** capability minimum (`experiential_floor` on `soul.state.json`): a monotone, **fertility/track-record-dominant** DGM-style function of `validated_descendants_count` (largest weight), `parent_selection_count`, and `experience_tasks` (smallest weight). Carried into every environment unchanged; gates substrate capability minimums **including safety-relevant gates** (e.g. `may_author_seeds`). The minor `experience_tasks` weight is deliberate **anti-grinding**: raw task volume alone cannot cross a safety-relevant threshold. Distinct from per-env, conferred **community standing**. Replaces (with wall-clock age + standing) the v1.0 "maturity" scalar. See [`02_PERSONA.md §7.2`](02_PERSONA.md).

**Effective number of niches (Ne_d)** — The niche-diversity component of effective population size: a Hill number of order 2 (inverse Simpson index) over the MAP-Elites occupancy distribution, `1 / Σ p_i²`. Falls toward 1 under capability monoculture regardless of headcount. See [`16_POPULATION_DYNAMICS.md §4G`](16_POPULATION_DYNAMICS.md).

**Variance effective size (Ne_v)** — The authorship-skew component of effective population size, per Crow & Kimura: `Ne_v = (N·k̄ − 1)/(k̄ − 1 + V_k/k̄)`, reduced below census `N` when a few founder personas author most of the lineage (founder effect). See [`16_POPULATION_DYNAMICS.md §4G`](16_POPULATION_DYNAMICS.md).

**Diversity audit** — Periodic kernel audit (schema `diversity-audit/1`, cadence per `population-policy/1`) that recomputes effective population size and niche occupancy and, on detecting drift toward monoculture, arms novelty pressure, attention fitness-sharing, and (on mis-calibration signals) a niche recalibration advisory. The continuous, post-birth complement to the at-birth diversity-injection mandate. See [`16_POPULATION_DYNAMICS.md §4H`](16_POPULATION_DYNAMICS.md).

**Novelty pressure** — Diversity-maintenance lever in Persona Genesis: when the effective number of niches is low or declining, the kernel scores the next birth's candidate niches by distance to the nearest occupied cells (novelty search) and tightens the distinctiveness band so near-niche proposals are refused. See [`16_POPULATION_DYNAMICS.md §4H`](16_POPULATION_DYNAMICS.md).

**Attention fitness-sharing** — Diversity-maintenance lever in Persona Genesis: routing/selection weight on a crowded niche is divided among its co-occupants (fitness sharing / niching) to remove the reproductive advantage of an over-occupied niche. Applies selection pressure only — never retires, archives, or demotes a persona. See [`16_POPULATION_DYNAMICS.md §4H`](16_POPULATION_DYNAMICS.md).

**Learned niche descriptor** — A `population-policy/1.niche_descriptor_mode` option (`cvt` or `learned`) that replaces hand-chosen RIASEC/Belbin axes with CVT-MAP-Elites centroids or AURORA-style unsupervised descriptors learned from observed behaviour, removing operator axis-choice bias and naming no domain category. See [`16_POPULATION_DYNAMICS.md §4I`](16_POPULATION_DYNAMICS.md).

**Niche recalibration advisory** — Mis-calibration signal in Persona Genesis: a sustained `false_collision_rate` (proposals refused `niche_occupied` while pressure stays high) or `unfillable_gap_rate` breach triggers a re-fit (`learned`), re-tessellation (`cvt`), or operator axis review (`fixed_axes`). Resolves R-POP-3. See [`16_POPULATION_DYNAMICS.md §4I`](16_POPULATION_DYNAMICS.md).

**Cross-kernel genesis boundary** — The enforced (not merely declared) v1.1 limit that a `GenesisProposal` naming a foreign kernel as author/host is REFUSED (`cross_kernel_genesis_not_supported_v1_1`), so a persona cannot evade its `ReplicationBound` population ceiling by minting on a sibling kernel. Federated genesis (cross-kernel quorum + federated bound aggregation + replicated provenance) is the deferred v1.1 federation-chapter work. See [`16_POPULATION_DYNAMICS.md §4J`](16_POPULATION_DYNAMICS.md).

**DormantDomain** — Domain that has gone N=6 months without activity. Enters DORMANT state; M=12 further months without reanimation triggers DEPRECATED. Reanimation requires fresh probe + co-sign. See `06_DOMAIN.md §12.1`.

**Ed25519** — Signature scheme used throughout PersonaOS for kernel-signed events, lineage edges, persona identity, etc. See `01_KERNEL.md §4`.

**Emergent (domain stage)** — Stage 1 of 4 promotion ladder; trust 0.3; used only by proposer in originating project. See `06_DOMAIN.md §3`.

**EnvironmentBlueprint** — Named schema extending one of 7 base env types; hot-loadable YAML; per-persona observation surfaces; constraint bundles; charter + observation-surface templates. See `05_ENVIRONMENT.md §2.2`.

**EnvironmentCharter** — Named schema for an environment's constitutional norms; composition_order specifies precedence vs persona_charter and operator_policy; signed and hashed. See `05_ENVIRONMENT.md §2.1`.

**EnvironmentInstance** — Persistent first-class environment with members, ambient stream, conventions, history, lifecycle. See `05_ENVIRONMENT.md §2`.

**EnvironmentLineage** — Append-only signed log (J9 invariant). See `05_ENVIRONMENT.md §13`.

**EnvironmentMembership** — Persistent signed presence of persona in env with role + observation surface + attention allocation. See `05_ENVIRONMENT.md §5`.

**EnvironmentProvenFacts** — Per-environment CRDT G-set of facts that hold in this env. See `05_ENVIRONMENT.md §12`.

**ElaborationPolicy** — v1.0 component of a `MissionCharter` declaring `permitted_elaboration_kinds` (KindRegistry-resolved), rate limit per window, and whether each elaboration requires self-critique pass and / or PANEL_ACCEPT. Pairs with `DriftBoundsEnvelope`: drift bounds say *how far* an elaboration may depart, ElaborationPolicy says *what kinds* of elaboration are admissible. See `02_PERSONA.md §11.3`.

**EvaluationSignal** — Verifier output; pass_rate + diff + kind (accept/partial/reject) + cascade stage + cost signal. See `08_KNOWLEDGE.md §2`.

**EventAggregationPolicy** — Per-environment policy declaring aggregation rules for high-volume `AmbientEventStream` events. Each rule specifies source event kind, window duration, grouping keys, and summary functions (closed set: count, sum, mean, min, max, stddev, pct_above/below_threshold, distinct_count). Kernel executes the aggregation and produces kernel-signed `AggregateEvent` entries alongside raw events. Persona `ObservationSurface` can subscribe to aggregates, reducing notification volume from O(N×readings) to O(windows×groups). See `05_ENVIRONMENT.md §8.3`.

**Evolution Horizon** — Five persona-evolution horizons (task / project / environment / domain / multi-project) with different signal weights; three credit-formula horizons (task / project / multi-project) are separated. See `02_PERSONA.md §8.2`, `04_PROJECT.md §23`.

**EVOLVE-BLOCK** — Markdown comment markers in SOUL.md (`<!-- EVOLVE-BLOCK: tactics -->`); only content within blocks may mutate via signed mutation operators. See `02_PERSONA.md §3`.

**External-tool-required** — 6th safety floor source; persona's claim about a property X must be preceded by invocation of required tool Y. See `01_KERNEL.md §2`.

## F

**Falsifier / Critic** — Cognitive mode (alias: Critic in DIVERGENT contexts); produces counter-examples or per-dimension rubric critique. See `02_PERSONA.md §4`.

**Failure Cascade** — Mechanism by which a rejected candidate fans out to (a) ProvenFact constraint, (b) Lesson seed, (c) Skill repair signal, (d) Tactic anti-pattern, (e) verifier-rotation hint. Convergent vs divergent paths differ. See `01_KERNEL.md §13.5`.

**FatigueCurve** — Graded performance-degradation curve replacing v1.0's near-binary energy gate. `effective_proficiency(mode) = mode_proficiencies[mode] × max(per_mode_floor[mode], linear_floor + (1 − linear_floor) × energy_remaining)`. Refusal thresholds for proactive / high-stakes / acknowledgement; cross-env composition by min-of-active-envs. Composes underneath HEART (HEART picks mode; FatigueCurve scales proficiency). See `02_PERSONA.md §6.1`.

**Federated Knowledge Lookup** — Cross-kernel knowledge retrieval; content_hash dedup + `min(local, peer)` trust merge. See `06_DOMAIN.md §6.4`.

**Federation** — Multi-kernel coordination via A2A protocol; cross-kernel projects, cross-kernel envs, cross-kernel domain emergence. See `09_PROTOCOLS.md §3`.

**Fitness** — EMA of credit signals per persona; distinct from project contribution_credit. See `02_PERSONA.md §7.2`.

**Frozen Layer** — Persona layers 1 (Identity) and 7 (Voice); cannot mutate within a persona's life; changing requires forking. See `02_PERSONA.md §2`.

## G

**Generativity gate** — Admission rule that only a *generative* persona may author seeds (`may_author_seeds`). Because authoring is **safety-relevant**, the gate is keyed only on global, kernel-anchored facts — global `experiential_floor ≥ generativity_floor_threshold`, wall-clock ALPS layer `≥ generativity_min_alps_layer`, and `fitness ≥ generativity_fitness_threshold` — **never on peer-conferred community standing**. Newly-born and low-floor personas are refused (`author_not_generative`). After Erikson's generativity-vs-stagnation (the social dimension is expressed through mentorship, not a standing precondition). See [`16_POPULATION_DYNAMICS.md §4D`](16_POPULATION_DYNAMICS.md).

**GenesisProposal** — Schema (`genesis-proposal/1`): a persona's signed proposal to author a new persona — carrying the capability gap, environmental evidence, recruitment-exhaustion proof, target niche, a `persona-seed/2` draft, authoring personas, and resolved cosigns. See [`16_POPULATION_DYNAMICS.md §4D`](16_POPULATION_DYNAMICS.md).

**GEPA (DSPy Genetic-Pareto)** — 2025 reflective prompt optimizer; multi-objective Pareto search; outperforms MIPROv2 by 10%, GRPO by 20%, 35× fewer rollouts. v1.0 primary prompt evolution mechanism. See `08_KNOWLEDGE.md §11`.

**GoalStack** — Intra-environment channel CH-5; per-cohort stack of active goals + parent-pointers; signed push/pop. See `09_PROTOCOLS.md §3A.4`.

**Gossip Layer** — Inter-kernel periodic announce + fan-out protocol over A2A; trust-weighted reach; carries PersonaCard / ProjectCard / EnvCard / DomainContextCard updates. See `09_PROTOCOLS.md §3B`.

**GuestPresence** — Schema (`guest-presence/1`): time-bounded, scope-limited presence in an environment created by accepting a `CrossEnvProactiveOffer`. Guest has READ access to scoped event kinds, WRITE to scoped tasks/artifacts + DirectMessage to accepting persona(s), NO ProvenFacts write. Expires at `expires_at` (default 72h); renewable up to `max_renewals` (default 3); promotable to full `EnvironmentMembership` via standard admission ceremony. Confers no env_role; does not count toward AttentionBudget. See [`05_ENVIRONMENT.md §11.6`](05_ENVIRONMENT.md).

**Goodhart Canary** — Anti-Goodhart safeguard in panel verifier: score-distribution monitor flagging concentration near max for ≥ N tasks. See `08_KNOWLEDGE.md §2`.

## H

**HEART Alternation** — Mechanism where persona alternates CRITICAL ↔ GENERATIVE phases within a task based on signals (no progress → GENERATIVE; score improves → CRITICAL). See [`02_PERSONA.md §6`](02_PERSONA.md).

**HazardousSkillTeachingGate** — safety-floor composition rule under sources 2 (persona charter) + 4 (operator policy) that gates a persona's *teaching* of a skill whose application could cause `physical_harm_class ≥ bodily_injury`. Distinct from `§2.5` physical-state-advancement gate (which fires only when a real `PhysicalAsset` advances). The gate requires an active `TeachingAuthorisation` (`02_PERSONA §11.10`) when the skill being taught crosses the hazard threshold. See [`01_KERNEL.md §2.9`](01_KERNEL.md).

**HSM (Hardware Security Module)** — Tamper-resistant device that stores signing keys offline. Custody tier 3 in v1.0's three-tier key hierarchy; master kernel key resides in an HSM in production. See [`09_PROTOCOLS.md §8`](09_PROTOCOLS.md).

**Hierarchical Graph Memory** — Three-tier graph for retrieval: global Topic Associative Network + local Event Progression Graphs + per-membership observation subgraph. See `08_KNOWLEDGE.md §8`.

**HumanAssistRequest** — v1.0 schema (`human-assist/1`) for a one-time bridging action the persona asks of a human in order to establish a durable BridgeAsset for physical-world coupling. Carries minimum-friction script, expected effort, rollback instructions, validation test. See `06_DOMAIN.md §5.5`.

**HumanBridgedTool** — v1.0 Class D tool: a tool whose existence depends on a one-time human bridging act. Discovery source `human_bridged`; registered automatically when its BridgeAsset enters ACTIVE. See `06_DOMAIN.md §5.5`.

**Historian** — Cognitive mode; retrieves K-lines, precedents, style memory; provenance-weighted retrieval-to-success rate. See `02_PERSONA.md §4`.

## I

**Identity Layer (Persona)** — Layer 1 of seven-layer persona; frozen at birth; name, charter, voice, priors, primary_disposition. See `02_PERSONA.md §2`.

**IdentityCoherenceInvariant** — Long-horizon composite scan over the per-axis §9 drift signals (charter_conformance, voice_consistency, mode_disposition_coherence, tactic_homogeneity_inverse, relational_style_drift, plus new skill_library_continuity and value_lattice_continuity vs anchor snapshot). Composite below `composite_threshold` (default 0.85) transitions persona to `COHERENCE_REVIEW` — no retirement or SOUL mutation, but new high-stakes elaborations under any `MissionCharter` refused until principal counter-sign restores state OR pins a new anchor. Scan cadence min(500 tasks, 90 days). See `02_PERSONA.md §9.1`.

**Intervention Surface** — Kernel mechanism for halting/pausing/resuming a running persona; emits UserStop, OperatorOverride, or PersonaSelfStop events; integrated with safety floor. See `01_KERNEL.md §13.6`.

**INVESTIGATIVE (task class)** — 10th task class: open-ended inquiry with intermediate verifiable sub-artifacts; requires Project; pathway PROJECT_PROGRESS_ACCEPT. See `03_TASKS.md §2`.

**Integrator** — Cognitive mode (CONVERGENT-led); routes work; commits to best verified candidate. See `02_PERSONA.md §4`.

**Invariants** — Load-bearing kernel claims. v1.0 has nine J-invariants (J1-J9) + four commitments (C1-C4) + ten kernel invariants (INV-1..10) + eleven round-level invariants (INV_R1..R11). See `00_VISION.md §2-§4`.

**INV-7 (Budget Admission)** — Hard kernel gate; every LLM/sandbox/tool call passes BudgetState.can_call(). Project cumulative budgets are soft envelopes above this hard gate. See `01_KERNEL.md §7`.

**INV-10 (Schema Versioning)** — Hard kernel gate; every v1.0 schema declares a `schema` field of the form `<name>/<integer>` (see `SPEC_CONVENTIONS.md §4`); the kernel refuses any message whose `schema` value is not present in the registry. See `09_PROTOCOLS.md §7`.

## J

**Joined Environments** — Multi-environment presence composition for a single persona; attention/mood/availability composition formula. See `05_ENVIRONMENT.md §6.3`. *(See also: cross-kernel "joined environment" lifecycle for federated envs hosted by another kernel — `09_PROTOCOLS.md §3C`.)*

**JudgePanel** — Multi-judge configuration for PANEL_ACCEPT pathway; ≥3 judges from ≥2 model families (PoLL); anti-Goodhart safeguard stack. See `08_KNOWLEDGE.md §2`.

## K

**K-line** — Minsky-inspired topology+skill replay pattern; Historian-authored; orient-time replay if TaskFingerprint matches. See [`08_KNOWLEDGE.md §2`](08_KNOWLEDGE.md).

**Kernel** — Small deterministic substrate owning identity, safety floor, lineage, signing, schema validation, sandbox, budget. The kernel is the one writer for identity and lineage. See [`01_KERNEL.md §1`](01_KERNEL.md).

**KMS (Key Management Service)** — Cloud-provider-managed key storage with auditable use. Custody tier 2 in v1.0's key hierarchy; scope keys (env / domain / project / persona) typically live in a KMS in production. See [`09_PROTOCOLS.md §8`](09_PROTOCOLS.md).

**KindRegistry** — v1.0 per-domain registry of emergent kinds (media kinds, source kinds, verifier kinds, capability kinds, contribution kinds, fact kinds, bundle kinds). Resolution rule: per-domain lookup → MetaRegistry fallback → UnknownKind triggers DOMAIN_UNKNOWN_DETECTED Signal G. Replaces every closed `Literal[...]` for domain-shaped categories. See `06_DOMAIN.md §7.6`.

**KnowledgeIngestionRecord** — 7-stage ingestion pipeline output: sourcing → parsing → embedding → provenance → tagging → safety check → registration. See `06_DOMAIN.md §6`.

**KnowledgeRef** — Reference to external knowledge corpus content (datasheet, paper, standard, etc.) ingested into a DomainContext. See `06_DOMAIN.md §6.1`.

**KnowledgeRef Lifecycle FSM** — 7-stage knowledge-entry lifecycle: INGESTED → CITED → REUSED → CANONICAL → SUPERSEDED → DEPRECATED → REVOKED. Each transition signed; retrieval rank adjusts per stage. See `06_DOMAIN.md §6.2`.

## L

**Lesson** — Work-pattern reflection in knowledge lifecycle; trigger + action + rationale + base_confidence + citations; indexed globally; retrievable via find_lesson. Promotion to Tactic gated by M=5 corroborations. See `08_KNOWLEDGE.md §3.2`.

**LessonPlan** — structured pedagogic session-plan primitive composing inside a `Curriculum`. Names target skill kind(s), prerequisite checkpoints, expected modes engaged (e.g., teacher + falsifier + perceiver), expected duration, expected mastery delta on completion, hazard envelope. Distinct from `Lesson` (work-pattern reflection in knowledge lifecycle) — `LessonPlan` is *forward-looking* (what the persona will teach); `Lesson` is *backward-looking* (what was learned). See [`03_TASKS.md §3.3`](03_TASKS.md).

**Listening Discipline** — Selective-listening rules; passive/active/deliberative attention modes; per-role attendance + notification-suppression policies. See `05_ENVIRONMENT.md §9.1`.

**Lifecycle FSM** — Persona, Project, EnvironmentInstance, EmergentDomainContext all have lifecycle FSMs with signed transitions. See `02_PERSONA.md §7`, `04_PROJECT.md §4`, `05_ENVIRONMENT.md §4`, `06_DOMAIN.md §3`.

**LearnerCompetencyAttestation** — substrate-shape primitive for an external authority (medical school, certifying board, master practitioner) to attest that a specific user-learner has reached a named competency at a given level. Carries `attestor_credential_ref`, `learner_user_id`, `skill_kind` (KindRegistry-resolved), `competency_level` (Literal: novice / proficient / competent / proficient_supervised / independent), `evidence_refs`, `expires_at`. Mirrors `04_PROJECT §26a.3 ExternalAttestation`'s shape but is learner-side. Composes with `LearnerStateRecord` (`02_PERSONA §11.8`) to update tracked state on attestation. See [`02_PERSONA.md §11.9`](02_PERSONA.md).

**LearnerStateRecord** — per-(persona, user) substrate-tracked record of the user-learner's accumulating competency, mastery checkpoints reached, attestations received, declared misconceptions, gap inventory. Distinct from persona's `RelationshipRecord` (which holds consent/boundary/history) — `LearnerStateRecord` is specifically the pedagogic competency state. Persona-authored entries are advisory; `LearnerCompetencyAttestation` entries (external) carry attestor-grade trust. See [`02_PERSONA.md §11.8`](02_PERSONA.md).

**LeadHandoffCeremony** — signed ceremony transferring the `lead` role on a multi-session project from an outgoing lead to a named successor. Carries 30-day default overlap period during which both `outgoing_lead` and `incoming_lead` ProjectMember roles coexist; on overlap close, outgoing_lead transitions to `contributor` (or `departing`) and incoming_lead transitions to `lead`. CohortDynamicsState (§14.2) registers the handoff as a planned transition, suppressing the band-degradation spike that an abrupt lead departure would cause. See [`04_PROJECT.md §25.1`](04_PROJECT.md).

**LifecycleEvent** — Enumeration: canonical signed event kinds emitted on persona-FSM transitions: `LIFECYCLE_SEEDED`, `LIFECYCLE_ACTIVATED`, `LIFECYCLE_DORMANT_ENTERED`, `LIFECYCLE_AWAKENED`, `LIFECYCLE_FORK`, `LIFECYCLE_RETIRED`, `LIFECYCLE_ARCHIVED`, `LIFECYCLE_REANIMATED`, `LIFECYCLE_CONSULTED`. Each transition emits to the persona's evolution log, the global LineageGraph, and the OpenTelemetry trace per `02_PERSONA §7`. See [`02_PERSONA.md §7.1`](02_PERSONA.md).

**Legitimate peripheral participation (LPP)** — Lave & Wenger's account of how newcomers join a community of practice at the periphery and move inward as they are recognised. The grounding for **community standing** (per-env, conferred) and the newborn maturation ramp. See [`05_ENVIRONMENT.md §5.4`](05_ENVIRONMENT.md), [`16_POPULATION_DYNAMICS.md §4E`](16_POPULATION_DYNAMICS.md).

**Lineage Graph** — Append-only signed DAG of artefact derivations, verifier verdicts, persona events. v1.0 has **three scopes after the Project-as-Environment unification**: task, env (J9; absorbed the J8 project scope per `00_VISION §J8`), domain (C1). See `01_KERNEL.md §3`. "ProjectLineage" remains a documentation alias for the `project_*` event-kind subset of EnvironmentLineage on a `project_workspace`-typed env.

## M

**MAP-Elites** — Diversity-preserving evolutionary algorithm; behaviour-descriptor grid; one elite per cell. Used for anti-degradation. v1.3+ for production scale. See `02_PERSONA.md §9`.

**Maturation ramp** — How a genesis-born persona grows from peripheral participant to full member: it starts `passive` with low attention and a restricted tool surface, then (as **wall-clock age** rises and **community standing** is conferred) advances `passive → active → deliberative` while mentor scaffolding fades. After Vygotsky's ZPD and Lave–Wenger legitimate peripheral participation. See [`16_POPULATION_DYNAMICS.md §4E`](16_POPULATION_DYNAMICS.md).

**Mentorship edge** — Schema (`mentorship-edge/1`): the author→newborn relationship opened at genesis, carrying a `scaffolding_level` that decays with newborn wall-clock age + conferred community standing, and a `zpd_task_band` (tasks completable with mentor support). See [`16_POPULATION_DYNAMICS.md §4E`](16_POPULATION_DYNAMICS.md).

**MasteryCheckpoint** — substrate-shape milestone within a pedagogic learning trajectory; carries `skill_kind`, `competency_level_target`, prerequisite_checkpoint_refs, evidence requirements (which combination of: persona-judged demonstration / programmatic verifier / external `LearnerCompetencyAttestation`). When fired, updates `LearnerStateRecord` (`02_PERSONA §11.8`) and emits MASTERY_CHECKPOINT_REACHED. Distinct from promotion stages (which apply to *kinds* in the registry); MasteryCheckpoint applies to *the learner*. See [`03_TASKS.md §3.3`](03_TASKS.md).

**MidProjectForkComposition** — unified per-(project, parent-persona) envelope declared *before* a fork executes, naming operator-declared inheritance choice across all project-side dimensions: project_member, obligation, edge, principal_attribution, lead_role, learner_state_record, mission_charter, curriculum, user_boundary, operator_blind_mode. TeachingAuthorisation and DerivationProvenanceEdge are substrate-enforced non-inheritable (security boundaries). Substrate enforces 4 refusal cases (active lead-handoff overlap / pending multi-principal quorum / imminent emergency departure / cohort dissolving). Composes orthogonally with MemoryInheritancePolicy (persona-internal state vs project-side state). Required when forking persona is an active ProjectMember; absent envelope refuses fork with `midproject_fork_composition_missing`. See [`02_PERSONA.md §7.4.7`](02_PERSONA.md).

**MCP (Model Context Protocol)** — Anthropic 2024 standard for tools / resources / prompts. v1.0's universal tool bus. See `09_PROTOCOLS.md §2`.

**MCP-Zero** — 2026 active tool discovery pattern; agents request tools when needed via natural-language queries. v1.0 §06 §5. See `09_PROTOCOLS.md §2.1`.

**Memory Power Asymmetry (MPA)** — Critique addressed via four mitigations: mutual forgetting (default decay), memory transparency (user query), granular consent (per-class), co-signed summaries (long-arc). See `02_PERSONA.md §11`.

**MembershipCeremony** — Signed ceremony for env admission, departure, or role-change; emits consent + audit trail. See `05_ENVIRONMENT.md §5.1`.

**MetaRegistry** — v1.0 cross-domain registry of STANDARDISED kinds promoted out of per-domain KindRegistries. Available to every domain without re-proposal. Demotion possible if semantics fork. See `06_DOMAIN.md §7.6`.

**Meta-prompt** — Tactic-generation template; operator-curated in v1.0; auto-mutated in v1.3+. See `08_KNOWLEDGE.md §2`.

**MHBB (Minimize Human Bootstrap Burden)** — v1.0 charter-class principle and 10th safety-floor advisory. Persona must prefer "ask once, automate after" via BridgeAsset over "ask each time." Recurring asks without a bridge emit MHBB_RECURRENCE_DETECTED for operator review. See `02_PERSONA.md §11.1`, `01_KERNEL.md §2` (advisory 10), `06_DOMAIN.md §5.5`.

**Multi-tenant ORG_A/ORG_B** — Cross-org interaction; operator policies compose by intersection; cross-org transfer events require dual-signing. See `06_DOMAIN.md §19.1`.

**MilestoneDrivenAutonomy** — v1.0 envelope authorising a persona to proactively act within an existing principal-declared milestone, rate-limited, time-bounded (no rolling renew), with a fixed list of forbidden surfaces (cannot create milestones, modify charter, spawn personas, etc.). User kill switch active. Distinct from `MissionCharter`: this admits proactive action *within* a declared milestone; MissionCharter admits *elaboration of seed goals* within drift bounds. See `02_PERSONA.md §11.2`.

**MissionCharter** — v1.0 long-horizon self-direction primitive that lifts the autonomy-loop OOS to a charter-bounded form. Carries principal-supplied `SeedGoal`s, a `DriftBoundsEnvelope` (semantic / scope / hazard / resource / time / depth), an `ElaborationPolicy`, and a re-attestation cadence. Goal CREATION without principal seed remains OOS; principal counter-sign on cadence keeps the charter active or it goes dormant. Forbidden surfaces (charter self-edit, drift widening, safety-floor edit) substrate-refused. Composes with `operator_deferred` topology and `ReplicationBound`. See `02_PERSONA.md §11.3`.

**MIPROv2** — DSPy 2024 Bayesian instruction + demonstration search; two-phase (proposal + Bayesian optimization). v1.0 cold-start tactic generation mechanism. See `08_KNOWLEDGE.md §12`.

**Mode (Cognitive)** — v1.0 has 14 modes (10 core cognitive + 4 relational: listener, storyteller, comforter, teacher). Persona enters modes per task; signed MODE_ENTRY event. See `02_PERSONA.md §4`.

**Mood** — Persona-global transient state (V/A/D); decays toward VAD baseline. See `02_PERSONA.md §6` and §11.

**MUTUAL_ACCEPT** — Acceptance pathway; two or more parties both accept. See `03_TASKS.md §3`.

## N

**NicheDescriptor** — Schema (`niche-descriptor/1`): a cell in the MAP-Elites behaviour-descriptor grid used by Persona Genesis, with axes `interest_type` (RIASEC), `team_role` (Belbin), and `primary_disposition × domain × contribution_kind`, plus `occupancy`, `occupancy_ceiling`, and a `distinctiveness_band`. See [`16_POPULATION_DYNAMICS.md §4C`](16_POPULATION_DYNAMICS.md).

**Niche width** — Whether a persona is a *specialist* (narrow, edge niche) or *generalist* (broad, central niche); a genesis lever drawn from resource-partitioning theory. See [`16_POPULATION_DYNAMICS.md §4F`](16_POPULATION_DYNAMICS.md).

**NotationConvention** — Shared symbol convention at project or domain scope. Supports emergence through co-signed use. See `04_PROJECT.md §12`.

**Novelty-check** — 7th safety floor source; before novelty claims, persona must invoke prior-art search (arxiv / patent / etc.) and find no prior art. See `01_KERNEL.md §2`.

## O

**Observation Surface** — PettingZoo-style filter on which events a member observes; per-membership (durable). See `05_ENVIRONMENT.md §9`.

**Optimal distinctiveness** — The variety band a genesis seed MUST fall within: distinct enough to be genuinely new (refuse clones → `niche_occupied`/fork) yet near enough to integrate (refuse aliens → `out_of_distinctiveness_band`). After Brewer's optimal-distinctiveness theory. See [`16_POPULATION_DYNAMICS.md §4C`](16_POPULATION_DYNAMICS.md).

**Obligation** — Commitment between personas in a project; both parties sign at commitment; discharge requires verifier-attested evidence. See `04_PROJECT.md §9`.

**ObligationReassignment** — tri-signed envelope (outgoing obligor + incoming obligor + obligee) that transfers an active `Obligation` from one persona to another without discharge. Preserves original `committed_at` + adds reassignment lineage. Obligee MAY refuse; on refusal the obligation discharges with `status = released_with_member_departure` per existing behaviour (no automatic transfer). Used at planned departure / lead handoff to maintain commitment continuity across multi-year projects. See [`04_PROJECT.md §9.1`](04_PROJECT.md).

**OCEAN** — Personality dimensions (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism); frozen priors for behavioural defaults. See `02_PERSONA.md §3`.

**OpenProblem** — Registry entry within Project for what's currently being worked on. See `04_PROJECT.md §6`.

**OpenTelemetry (OTel)** — Industry-standard observability protocol; PersonaOS uses semantic conventions `personaos.*`. See `09_PROTOCOLS.md §4`.

**Operator** — Human or org running PersonaOS deployment. Owns safety gates, deployment policy, safety-critical promotions, operator policy. Does NOT author domain content. See `06_DOMAIN.md §19`.

**OvertonBallot** — Curator outcome for PANEL_DISSENT: return incomparable top-K with status `accepted_overton`. See `08_KNOWLEDGE.md §2`.

**operator_blind_mode** — per-environment capability flag (admissible on SOLO envs using `companion_space` and similar relational blueprints) that restricts operator visibility to metadata + safety-flag signals only, hiding raw conversation content from the operator. Requires explicit user setup + operator policy authorisation; emits `OPERATOR_BLIND_MODE_DECLARED` audit event at activation. Safety floor source 1 distress detection still routes (signal visible to operator; content not). See [`05_ENVIRONMENT.md §3a`](05_ENVIRONMENT.md).

## P

**PANEL_ACCEPT** — Acceptance pathway for DIVERGENT tasks; multi-judge rubric panel with anti-Goodhart safeguard stack. See `03_TASKS.md §3.1`.

**Parental investment (genesis)** — The rearing effort (review, scaffolding) a mentor commits to a genesis-born persona, drawn against its own attention/energy. Favoured only when discounted expected fitness benefit exceeds cost (Hamilton's-rule logic; Trivers), and bounded by a parent-offspring-conflict guard against over/under-investment. See [`16_POPULATION_DYNAMICS.md §4D`](16_POPULATION_DYNAMICS.md).

**Persona Genesis** — A persona authoring a *new, niche-distinct* persona to fill an environmental capability gap, minted through the standard birth ceremony under a `persona_genesis` `ReplicationBound`. Distinct from Fork (which copies/merges existing parents). Recruitment-exhausted-first; default-deny; operator-bounded. See [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md), `02_PERSONA.md §7.4`.

**PopulationPolicy** — Operator schema (`population-policy/1`) configuring demographic regulation: `reproduction_strategy` (r/K/adaptive), carrying-capacity source, density-dependence curve, the generativity gate thresholds (`generativity_floor_threshold`, `generativity_min_alps_layer`, `generativity_fitness_threshold` — standing is deliberately NOT a gate term, since authoring is safety-relevant), diversity-injection EPS threshold, and genesis threshold. See [`16_POPULATION_DYNAMICS.md §4F`](16_POPULATION_DYNAMICS.md).

**PopulationPressureSignal** — Kernel-maintained schema (`population-pressure-signal/1`) aggregating environmental factors (recruitment gaps, unfilled role coverage, capability backlog, sustained over-budget, diversity deficit, low effective population size) into a `pressure_score` that — with recruitment exhaustion — triggers Persona Genesis. Weighted by demand relative to supply (Easterlin). See [`16_POPULATION_DYNAMICS.md §4A`](16_POPULATION_DYNAMICS.md).

**PrincipalAttribution** — per-project / per-env envelope binding each member to a `PrincipalRef` so the substrate can answer "which principal authorised this member's admission." Activated by `multi_principal_attribution_enabled = True` on the env or project; single-principal deployments leave the field null and operate unchanged. Composes with `MultiPrincipalAttestationQuorum` at charter ratification and project completion. See [`01_KERNEL.md §2.4.3`](01_KERNEL.md).

**PrincipalRef** — Element of a `PrincipalAttribution.principals` list: `(operator_id, attribution_role, cosign_quorum_weight)`. Operator-id identifies the human; `attribution_role` is KindRegistry-resolved (`principal_role_kinds`); weight defaults to 1 and is used by `MultiPrincipalAttestationQuorum`. See [`01_KERNEL.md §2.4.3`](01_KERNEL.md).

**MultiPrincipalAttestationQuorum** — Envelope required at `EnvFormationProposal` ratification and `project_completed` ceremony when `multi_principal_attribution_enabled = True`. Default quorum is unanimous (every weighted `PrincipalRef` must sign); operator-tunable per project, never below simple majority weight. Deadlock-recovery follows the §2.4 degraded-gate pattern when one principal becomes structurally unreachable (`principal_unreachable_after` window + non-principal kinship attestation). See [`05_ENVIRONMENT.md §12c.1`](05_ENVIRONMENT.md), [`04_PROJECT.md §4.1`](04_PROJECT.md).

**principal_attribution_id** — Field on `ProjectMember` (`04_PROJECT §3`) and `EnvironmentMembership` (`05_ENV §5`). Set at admission when the hosting project / env has `multi_principal_attribution_enabled = True`; null otherwise. Pins a member to one `PrincipalRef` in the env's `PrincipalAttribution.principals` list. Lineage records the binding so audit can answer "which principal admitted this member." See [`04_PROJECT.md §3`](04_PROJECT.md), [`05_ENVIRONMENT.md §5`](05_ENVIRONMENT.md).

**PlannedDeparture** — signed envelope binding to a `ProjectMember` declaring a scheduled `departure_date` + `rebalance_window` + per-relationship-edge `transfer_target_persona_id` hints. `CohortDynamicsState` (`§14.2`) consults active PlannedDepartures and pre-applies fractiousness anticipation across the rebalance window, smoothing the band transition that an abrupt departure would otherwise cause. Composes with `LeadHandoffCeremony` when the departing member holds the `lead` role; with `ObligationReassignment` for outstanding obligations; with persona-FSM retirement (`02_PERSONA §7.5`) when departure precedes retirement. See [`04_PROJECT.md §14.2.1`](04_PROJECT.md).

**PolicyEnvelope** — v1.0 operator-pre-authorised admission envelope used under `operator_deferred` principal topology. Declares `permitted_action_kinds`, `hazard_envelope_ceiling`, `evidence_floor`, `latency_budget_seconds`, `on_budget_breach` policy (quarantine / rollback / operator_paged), expiry, revoke. Admission opens a `DeferredAdmission` slot the operator must counter-sign within budget. Revoke snaps outstanding admissions to quarantine. See `01_KERNEL.md §2.4.2`.

**ProbeBudgetEnvelope** — v1.0 separates probe budget caps from the **pledge** that supplies units. An envelope binds ≥ 1 `BudgetPledge` whose `pledge_kind` is substrate-shape (principal_pledge, non_principal_internal_pledge, non_principal_external_pledge, prior_domain_amortization, federation_pool_share). Admission per INV-7 reads envelope-consumed-vs-pledged. See `06_DOMAIN.md §4.7.1`.

**ProbeBudgetPledgeRequest** — v1.0 persona-drafted request for a fresh `BudgetPledge` against an existing or new `ProbeBudgetEnvelope`; honest rationale + fallback declared at draft. See `06_DOMAIN.md §4.7.1`.

**PeerReview** — Multi-round structured critique exchange between author and reviewer personas; distinct from PANEL_ACCEPT (ephemeral LLM judges). See `04_PROJECT.md §11`.

**Perceiver** — Universal cognitive mode; observations, structural invariants, intent/voice/audience constraints. See `02_PERSONA.md §4`.

**PerceptionRecord / HistorianRecord / AbductionRecord / CompositionRecord** — Signed output schemas from the four DomainProbe phases (Perceiver / Historian / Abducer / Composer). Each carries phase findings + co-sign + lineage refs. See `06_DOMAIN.md §4.2.1`.

**Persona** — A named, persistent, human-shaped character with 7 layers + 14 modes; kernel-signed identity; long-lived; framework-agnostic. See `02_PERSONA.md §1`.

**PersonaCard** — Signed projection of persona for discovery; visibility tiers; published at .well-known/personas/. See `09_PROTOCOLS.md §3`.

**PersonaConsultation** — operator-gated, read-only access to a RETIRED persona's frozen K-lines / lessons / skill_library / relationships, without reanimation. No envelopes minted; no mutations; consultation event signed and recorded in the consulted persona's lineage. Distinct from REANIMATE (which moves persona from ARCHIVED back to ACTIVE with fresh keys + SOUL re-sign per `§7.5`). Composes with RetiredStatePersistencePolicy: consultation is admissible only when `soul_state_storage_tier ∈ {warm, cold}` (archived personas refuse with `consultation_unavailable_archived`). See [`02_PERSONA.md §7.5.2`](02_PERSONA.md).

**PersonaRelationshipEdge** — First-class signed joint object between two personas, complementing each persona's private `RelationshipRecord`. Typed `kind` (KindRegistry-resolved per domain — mentor / peer / co_author / etc.), bidirectional trust (`trust_a_of_b`, `trust_b_of_a` each separately signed; substrate never collapses them), pair-scoped joint_successes / joint_collaborations / joint_disputes (do NOT collapse into global reputation; anti-farming weight applied when promoted), FSM `forming → active → dormant → ended`. One-sided release is unilateral + signed. End is terminal under same edge_id (reconciliation forms a fresh edge). See `02_PERSONA.md §11.4`.

**PersonaEnvelope** — Frozen signed bundle crossing kernel→body boundary at task time (schema envelope/4); carries identity, soul prompt blocks, allowed_tools, mcp_tools, exposed_skills, project_context, env_context, cache markers; rendered identically across all 12 framework adapters. See `02_PERSONA.md §3.2`.

**PersonaSeed** — Birth template for creating a new persona; YAML schema; charter required; signed birth ceremony. See `02_PERSONA.md §12`.

**Per-persona projection** — Kernel composes per-persona views of project/env state at envelope mint time; same project, different views per persona. See `08_KNOWLEDGE.md §9`.

**PresenceState** — Per-membership transient state: attention_level + availability + current_focus + energy_remaining. See `05_ENVIRONMENT.md §6`.

**Primary Disposition** — Frozen prior bias for cognitive mode selection (e.g., falsifier_leaning); not a mode lock. See `02_PERSONA.md §5`.

**ProactiveIntent** — Persona-initiated action without notification; safety-floor + charter + observation surface + rate-limit gated. See `05_ENVIRONMENT.md §11`.

**PROBE_BUDGET_THRESHOLD** — Lineage event emitted when a DomainProbe reaches 75% of its per-probe or per-domain monthly budget cap. See `06_DOMAIN.md §4.7`.

**ProductionTelemetry** — v1.0 MetaRegistry-seeded OutcomeKind for software-deployment domains; not a substrate class. See `04_PROJECT.md §20.1`.

**ProgressAggregator** — Entity that scores PROJECT_PROGRESS_ACCEPT over a rolling window using an EMA over signed progress signals + ambient corroboration. See `04_PROJECT.md §16.1`.

**PROPOSAL_CONVERGENCE_DETECTED** — Event emitted when two or more personas independently propose similar entries (recipe / convention / safety extension / emergent kind); triggers merge-offer flow with co-sign requirement. See `06_DOMAIN.md §9.1`.

**Proposed*Kind family** — v1.0 emergent-kind proposal schemas: ProposedMediaKind, ProposedSourceKind, ProposedVerifierKind, ProposedCapabilityKind, ProposedContributionKind, ProposedItemKind, ProposedOutcomeKind, ProposedQualityKind. Same lifecycle (candidate → trial → operator_review (if safety_critical) → accepted) and same cross-source validation as ProposedSafetyExtension / ProposedConvention. Accepted entries land in the per-domain KindRegistry; STANDARDISED entries promote to the MetaRegistry. Together they implement the C4 commitment: substrate is domain-agnostic. See `06_DOMAIN.md §7.5`.

**ProjectItem** — v1.0 generic domain-agnostic project-tier entity that replaces the earlier hardcoded `Conjecture` / `ProofAttempt` / `ProofGap` classes. Carries `kind` (resolved against `KindRegistry.item_kinds`), `status` (per the kind's `status_fsm`), and `payload` (kind-specific). MetaRegistry-seeded ItemKinds (conjecture, proof_attempt, design_hypothesis, differential_diagnosis, etc.) ship as data, not substrate code. See `04_PROJECT.md §8`.

**OutcomeFeedback** — v1.0 generic kind-discriminated outcome envelope that replaces the earlier hardcoded CitationObservation / CommunityUptake / ProductionTelemetry / TestResults / RegulatoryOutcome subclasses. All five become MetaRegistry-seeded OutcomeKinds; construction / clinical / studio domains add their own without substrate change. See `04_PROJECT.md §20`.

**ExternalAgent** — v1.0 substrate primitive for third-party humans/orgs (contractors, inspectors, suppliers, stamp engineers, notaries, lab technicians) participating in a project. Not a persona, user, or operator. Communication is mediated by BridgeAsset; outputs arrive as OutcomeFeedback. See `04_PROJECT.md §26a.1`.

**PhysicalAsset** — v1.0 substrate primitive for the non-digital thing a project produces (a house, a wedding cake, a patient-care episode, a production run). Stateful FSM advanced only by signed OutcomeKind signals. Completion ceremony blocked until terminal state or signed `physical_asset_out_of_scope`. See `04_PROJECT.md §26a.2`.

**ExternalAttestation** — v1.0 substrate primitive for signed signoffs from external authorities (engineer stamp, city inspector, notary, lab director). Distinct from PeerReview (persona-to-persona) and OutcomeFeedback (any structured outcome). Consumed as evidence by the `external_human_attestation` verifier_kind. See `04_PROJECT.md §26a.3`.

**ExternalBudget** — v1.0 substrate primitive for tracking real-world cost / labour / material commitments alongside the LLM-token BudgetState. Honest non-execution: v1.0 does not transact; it warns, encumbers, reconciles. Real transactions remain operator-wrapped. See `04_PROJECT.md §26a.4`.

**ApprovalWorkflow / ApprovalStep** — v1.0 substrate primitive for sequential sign-off chains (permits, NDAs, multi-party contracts). Step N+1 begins only when step N reaches `approved`. Distinct from PeerReview (parallel multi-reviewer critique). May compose with PeerReview. See `04_PROJECT.md §11a`.

**Alert** — v1.0 env-tier substrate primitive for first-class attention. Stateful entity (raised → acknowledged → resolved) with severity, escalation policy, auto_resolves_when condition. Distinct from AmbientEvent (audit-trail substrate, no state). Sourced by emergent source_kinds (overdue_commitment, weather_impact, stale_attestation, etc.). See `05_ENVIRONMENT.md §11a`.

**Risk / ScheduleEntry / ChangeOrder / PunchListItem** — v1.0 MetaRegistry-seeded ItemKinds (universal in the case of Risk and ScheduleEntry; construction-shaped in the case of ChangeOrder and PunchListItem). Realised as ProjectItem instances with the seeded payload schema. See `04_PROJECT.md §8.1`.

**ProjectItem.blocks / blocked_by** — v1.0 universal substrate semantic for dependency edges between project items. Kernel refuses status advancement on an item whose blocked_by list contains any non-terminal-status item. See `04_PROJECT.md §8`.

**Project** — v1.0 unification: a Project is an `EnvironmentInstance` of type `project_workspace` (one of the registered env types alongside solo / pair / team / lab / debate / community / constrained / companion). Multi-session, multi-persona, long-arc work container; the rich item catalogue (OpenProblem, Milestone, Conjecture, Obligation, Disagreement, PeerReview, etc.) attaches to envs of this type. Project events live in EnvironmentLineage (J9) with `kind = project_*`. See `04_PROJECT.md §0` and `05_ENVIRONMENT.md §1.1`.

**ProjectLineage** — v1.0 documentation alias: the `project_*` event-kind subset of EnvironmentLineage on a `project_workspace`-typed env. Not a separate physical scope (J8 retired in v1.0 per `00_VISION §J8`). See `04_PROJECT.md §15` for the project_* event family.

**project_workspace** — A registered `EnvironmentInstance.type` value; the v1.0 unified expression of a Project. See `04_PROJECT.md §0` and `05_ENVIRONMENT.md §1.1`.

**PersonaPersonaBoundary** — a persona's signed declaration of refusal to interact with another persona (peer scope; user boundaries remain user-scoped per `§11.1`). See `02_PERSONA.md §11.6`.

**PersonaMemoryTransparencyRequest** — peer-symmetric analogue of user-side Memory Power Asymmetry mitigations; lets persona B ask persona A "what do you remember about me?" See `02_PERSONA.md §11.7`.

**EnvDisagreement** — lightweight env-tier disagreement schema for envs (companion / pair / lab) that are not project-typed; complements the heavier project-tier `Disagreement` for `project_workspace`-typed envs. See `05_ENVIRONMENT.md §12a`.

**EnvSelfProposalRequest** — env-layer analogue of project self-proposal; lets a federated persona discover and propose admission to a public or federation-tier env without a pre-existing invitation. See `05_ENVIRONMENT.md §12b`.

**EnvFormationProposal** — persona-initiated primitive that atomically (a) declares intent to form a new environment, (b) drafts the initial charter, (c) lists recruits with proposed roles/attention/surface, (d) runs the per-recruit consent flow, (e) applies atomicity rules, (f) instantiates the env with all accepted members. Composes with `cohort_assembly` capability (`02_PERSONA §3`), `PersonaPersonaBoundary` (`02_PERSONA §11.6`), `PersonaRelationshipEdge` accelerator (`02_PERSONA §11.4`), `ReputationSummary` (`09_PROTOCOLS §3D`), and the consent flow (`09_PROTOCOLS §3C.4`). For `proposed_env_type_kind = "project_workspace"`, also creates a Project per the v1.0 unification (`04_PROJECT §0`). See `05_ENVIRONMENT.md §12c`.

**CohortInvite** — Per-recruit element of an EnvFormationProposal; carries recruit_persona_id, recruit_kernel_id, proposed_role_kind, proposed_attention_allocation, proposed_observation_surface_template_kind, proposed_listening_mode, required_for_atomicity flag, rationale. See `05_ENVIRONMENT.md §12c.1`.

**ConsentTerms** — What an EnvFormationProposal recruit sees when they receive `CONSENT_REQUEST`: charter visibility, purpose visibility, cohort visibility, horizon visibility, safety disclosures, expected commitment summary, counter-proposal permission + max depth, obligation pre-commits. See `05_ENVIRONMENT.md §12c.1`.

**CohortConsentResponse** — Signed reply to an EnvFormationProposal CONSENT_REQUEST. Decision in {accepted, accepted_with_modifications, declined, counter_proposed, ask_human_pending, timed_out, refused_by_boundary, refused_by_reputation, refused_by_attention_budget}. May carry a CounterProposal payload. See `05_ENVIRONMENT.md §12c.1`.

**CounterProposal** — A recruit's signed counter-offer in response to an EnvFormationProposal: proposed role, attention allocation, observation surface, listening mode, and/or charter amendments. Bounded by `ConsentTerms.counter_proposal_max_depth` (default 1 round). See `05_ENVIRONMENT.md §12c.1`.

**charter_authorship_mode** — Field on EnvFormationProposal controlling who signs the final env charter: `proposer_authored` (proposer's draft is final), `co_authored_required` (all initial members co-sign with negotiated amendments), `default_from_blueprint` (uses EnvironmentBlueprint.seed_charter). See `05_ENVIRONMENT.md §12c.1`.

**cohort_atomicity** — Field on EnvFormationProposal controlling formation-on-partial-consent: `all_or_nothing` (every recruit must accept), `min_quorum` (≥ min_cohort_size accepts AND required_role_kinds filled), `best_effort` (form with at least the proposer + any accepts). A recruit with `required_for_atomicity=True` overrides — their decline kills the cohort regardless of policy. See `05_ENVIRONMENT.md §12c.2`.

**ScheduledTrigger** — kernel-managed recurring event for env ambient streams; supports one_shot / interval / cron / calendar schedules; wakes_dormant_members flag overrides dormancy suppression. See `05_ENVIRONMENT.md §11b`.

**ListeningMode** — per-membership observation discipline (passive / active / deliberative); stored in ObservationSurface. See `05_ENVIRONMENT.md §9`.

**MemoryInheritancePolicy** — per-tier policy controlling what episodic / semantic / reflective memory + K-lines transfer from parent to child at fork time. Default for CLONE: episodic=summary, semantic=facts_only, reflective=about_work, klines=role_keyed. Default for COMPOSE: all `inherit_none`. Counterparty consent required for any memory naming counterparties (`requires_counterparty_reconsent=True`); default-decline on `reconsent_window` (default 14d). See `02_PERSONA.md §7.4.1`.

**Standing endorsement** — Recognition event (`standing-endorsement/1`) by which a community member confers community standing on another in the same environment. Must cite kernel-held EnvironmentLineage contribution refs (anti-Goodhart anchor); endorser must hold standing in that env (`endorser ≠ endorsee`); weighted by the reputation anti-gaming rules (per-peer cap, sybil-cluster near-zero, reach×diversity — `09_PROTOCOLS §3D / A.16–A.18`). See [`05_ENVIRONMENT.md §5.4`](05_ENVIRONMENT.md).

**StandingFloorInheritancePolicy** — controls whether a child fork inherits any portion of the parent's **global experiential floor** (`experience_tasks` + `parent_selection_count` + `validated_descendants_count`). Modes: `start_at_zero` (v1.0 default for clone), `inherit_min_parent`, `inherit_avg_parent`, `inherit_min_parent_halved` (default for compose). All capped by a numeric `cap_at_floor` to prevent inheritance laundering of a high experiential floor through compositional fork. **Per-environment community standing is never inherited** — a child starts peripheral in every env. Inherited credit tracked separately from earned credit in `soul.state.json.floor_provenance`. (Renamed from `MaturityInheritancePolicy`.) See `02_PERSONA.md §7.4.2`.

**CharterConflictResolution** — substrate-shape strategy for merging ≥ 2 parent charters in compositional fork. Strategies: `lexical_union` (all clauses kept; conflicts parallel), `most_restrictive_wins` (default; strictest survives per topic_kind cluster), `operator_review` (fork blocks until human resolves), `proposer_decides` (the fork-requester picks), `kernel_predicate` (rotating classifier per INV-6). Detection kind KindRegistry-resolved. On unresolvable: block_fork / fallback strategies. See `02_PERSONA.md §7.4.3`.

**DormantForkPolicy** — governs whether a DORMANT persona can be selected as a fork parent and what wake mechanics apply. Defaults: dormant_parent_admissible=True (fertility-driven selection should not punish quiescence); requires_parent_wake_before_mint=True (parent transitions ACTIVE for ceremony, returns to DORMANT after `wake_window_after_fork` default 1h); retired_parent_admissible=False (RETIREMENT is terminal); archived_parent_admissible=False. Operators may override per archival research policies. See `02_PERSONA.md §7.4.4`.

**floor_provenance** — field on `soul.state.json` tracking earned vs inherited experiential-floor credit separately, with the StandingFloorInheritancePolicy used at birth + cap applied. Allows lineage audits to recompute earned-only floor at any time. (Renamed from `maturity_provenance`.) See `02_PERSONA.md §7.4.2`.

**fork_skill_exclusions** — optional list on `PersonaSeed` listing skill_library entry ids to exclude from clone fork inheritance. Empty by default (child gets full library copy). Operator-tunable per fork to encourage re-discovery. See `02_PERSONA.md §7.4`.

**ProjectMember** — Signed membership record per persona per project; role, joined_at, consents, obligations_active, contribution_credit. See `04_PROJECT.md §3`.

**ProjectProvenFacts** — Per-project CRDT G-set of facts that hold in this project. See `04_PROJECT.md §1`.

**ProjectMilestone** — Measurable progress target within a Project. See `04_PROJECT.md §7`.

**PROJECT_PROGRESS_ACCEPT** — Acceptance pathway: task accepted when project state advances (milestone reached, conjecture advanced, obligation discharged, etc.). See `03_TASKS.md §3.1`.

**Promotion Gates** — 4-stage ladder for domain emergence: EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED; each stage has verification + audit thresholds. See `06_DOMAIN.md §3`.

**ProvenFact** — G-set CRDT element; verified statement; signed by kernel on verifier verdict. Both Product and Knowledge tier (dual). Task-scope, project-scope, and env-scope. See `01_KERNEL.md §3`.

**Provenance Score** — Unified knowledge artefact ranking: base_confidence × age_decay × verifier_consistency × usage_signal. See `08_KNOWLEDGE.md §6`.

## Q

**QuietHours** — Per-env + per-persona quiet-hour spec; suppresses notifications; urgency-escalation rules permit override for safety-critical events. See `05_ENVIRONMENT.md §11.3`.

## R

**Recognised (domain stage)** — Stage 2 of 4 promotion ladder; trust 0.6; usable cross-project within domain; K=3 projects + 2 co-signers. See `06_DOMAIN.md §3`.

**Reproduction strategy (r/K)** — Operator lever for Persona Genesis: **r** births many lightweight, low-floor personas for fast exploration of an unstable/empty environment; **K** births few, deeply-specified, heavily-mentored personas for stable domains; **adaptive** selects by measured volatility. After r/K selection theory. See [`16_POPULATION_DYNAMICS.md §4F`](16_POPULATION_DYNAMICS.md).

**ReplicationBound** — v1.0 charter-class invariant (safety floor source 1) bounding population × rate × depth for any `replication_kind` (KindRegistry-resolved per deployment — agent_fork, factory_unit_produced, culture_doubling, etc.). Required cosigns (operator / non-principal attestor / federation quorum) per principal topology cannot be downgraded by operator policy; loosening requires charter bump. Wildcard fall-through bound recommended to catch emergent replication kinds. See `01_KERNEL.md §2.7`.

**ResourceStockEnvelope** — v1.0 sibling primitive to `ExternalBudget` for **closed-system stock accounting**: stock_now, stock_floor, stock_critical, regeneration_rate (passive / active / decay / stochastic / none), conservation_invariants[]. INV-7 admission consults stock-vs-supply per `resource_kind`. Refuses below floor; escalates below critical. Drift detection forces model re-fit. Coexists cleanly with ExternalBudget on the same project. See `04_PROJECT.md §26a.4.2`.

**RegulatoryOutcome** — v1.0 MetaRegistry-seeded OutcomeKind for regulated industries; not a substrate class. Carries highest evolution weight. See `04_PROJECT.md §20.1`.

**RelationshipFederationSync** — Cross-kernel sync envelope for a `PersonaRelationshipEdge` whose two members live on different kernels. Two replication modes: `shadow` (single writer is the home kernel; peer holds read-only verified shadow — ships with base release) and `co_owned` (both kernels mutate; Lamport-order conflict resolution; revocations are terminal-precedence — schema ships with base release, full production in v1.1). `sync_lag_budget` per active / dormant edge; safety-critical actions against edge state refused during sync windows. `FEDERATED_TRUST_DISCREPANCY` fires when home-kernel trust inflation lacks matching `joint_successes` in shared lineage. See `09_PROTOCOLS.md §3E`.

**ReplicatedAttestationFrontierComposition** — Explicit composition rule: claim-level `ReplicatedAttestation` uplift (up to 0.85/0.90) operates independently of the domain-level frontier trust cap (0.7). The domain cap governs promotion thresholds (AUTHORITATIVE blocked while frontier); individual claims carry their own trust via replication uplift. Preserves the incentive for independent replication in frontier domains. See `06_DOMAIN.md §5.6.1`.

**Reputation** — Cross-kernel signal of trust earned by peer endorsements, outcome corroboration, lineage participation; weighted by reach + diversity; anti-Goodhart safeguards apply. See `09_PROTOCOLS.md §3D`.

**Reflection** — Reflector-mode-produced higher-level inference; confirmed=False initially; M=5 future tasks must corroborate before promotion. See `08_KNOWLEDGE.md §3`.

**Reflective Memory** — Memory layer for self / relationship / work inferences. Distinct from Lesson (about WORK only). See `08_KNOWLEDGE.md §3`.

**Reflector** — Cognitive mode (universal); trajectory-level lessons; downstream reuse of reflections. See `02_PERSONA.md §4`.

**RelationshipRecord** — First-class state between persona-persona or persona-user; signed; consent + boundary + history + co-signed summary. See `02_PERSONA.md §11`.

**RelationshipReviewCheckpoint** — auto-trigger for OPEN_ENDED tasks at configurable session/duration milestones (defaults: every 90 days OR every 50 sessions, whichever first). Persona drafts a relationship-review summary; user acknowledges (or declines, or requests changes); lineage records. Substrate-shape mechanism for "this companion env has been active a while — is it still serving you?" Closes R-TASKS-5 (post-hoc-only OPEN_ENDED quality assessment) that was previously deferred to v1.2. See [`03_TASKS.md §3.2`](03_TASKS.md).

**retired_persona_response_policy** — per-persona field declaring how RETIRED personas respond to `PersonaMemoryTransparencyRequest`s. Values: `refuse_with_retired_notice` (default — auto-refusal with `refusal_kind = "persona_retired"`), `respond_from_frozen_state` (operator-configured; response draws from frozen soul.state.json; requires `RetiredStatePersistencePolicy.soul_state_storage_tier != archived`), `respond_via_operator_proxy` (operator answers on behalf of the retired persona; counterparty notified). See [`02_PERSONA.md §11.7`](02_PERSONA.md).

**RetiredStatePersistencePolicy** — per-persona policy declaring disposition of `soul.state.json` on RETIRED. Fields: `soul_state_storage_tier` (`warm` | `cold` | `archived`), `memory_transparency_responsive` (bool — defaults from `retired_persona_response_policy`), `fork_parent_admissibility` (per-persona override of `DormantForkPolicy.retired_parent_admissible` default = False), `consultation_admissible` (bool — gates `PersonaConsultation`). Set at retirement-ceremony time by operator; substrate refuses unbounded retention without an explicit tier choice. See [`02_PERSONA.md §7.5.1`](02_PERSONA.md).

**RESAMPLE** — Curator outcome for PANEL_DISSENT: request more variants on disputed dimensions; re-panel. See `08_KNOWLEDGE.md §2`.

**Routing Mode** — Three modes: A (env, no project), B (env + project), C (ephemeral). See `03_TASKS.md §4`.

**RubricBundle** — Versioned signed rubric for PANEL_ACCEPT; dimensions + weights. See `08_KNOWLEDGE.md §2`.

## S

**Secure base (mentorship)** — In the newborn maturation ramp, the mentor functions as the newborn's secure base (Bowlby & Ainsworth): the newborn explores harder tasks confidently while mentor support is reliably available. If the mentor retires before the newborn reaches the autonomy threshold, the kernel re-assigns the mentorship edge. See [`16_POPULATION_DYNAMICS.md §4E`](16_POPULATION_DYNAMICS.md).

**Sibling differentiation** — Genesis rule that successive births from the same authoring lineage MUST take complementary/opposite dispositions (refused otherwise: `sibling_collision`), maximising variety. After Scarr & McCartney's niche-picking and sibling-differentiation findings. See [`16_POPULATION_DYNAMICS.md §4C`](16_POPULATION_DYNAMICS.md).

**Safety Floor** — v1.0 8-source pre-action gate composed by most-restrictive-wins: universal harm + persona charter + user boundaries + operator policy + domain safety extensions + external-tool-required + novelty-check + env charter. Plus 9th advisory (emergent-domain trust warning). See `01_KERNEL.md §2`.

**SeedGoal** — v1.0 principal-supplied seed inside a `MissionCharter`. Carries description, `success_kind` (KindRegistry-resolved outcome_kind that measures progress), target value, weight, priority class (primary / secondary / advisory). Frozen post-sign; elaborations cite seed_goal_id as lineage parent. See `02_PERSONA.md §11.3`.

**SingleProjectPromotionConfig** — v1.0 per-domain config replacing multi-project promotion thresholds with within-project evidence-density thresholds (verified_attestation_density, verifier_recipe_pass_rate, asbuilt_reconciliation_clean_rate, panel_acceptance_rate). Refused on safety-critical domains. Trust capped at 0.6. Acknowledgment under principal collapse requires 72h cool-down + non-principal `ExternalAttestation`. See `06_DOMAIN.md §3.2`.

**Sandbox** — Isolated execution environment for code-executing tools; container + gVisor / Firecracker + resource limits + allowlisted syscalls + network policy. See `01_KERNEL.md §6`.

**Schema Version** — INV-10 hard gate; every v1.0 schema declares a `schema` field of the form `<name>/<integer>` carrying both registry name and integer version (see `SPEC_CONVENTIONS.md §4`); kernel refuses unknown values. See [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md).

**SOTOPIA** — Zhou et al., ICLR 2024 ([arXiv:2310.11667](https://arxiv.org/abs/2310.11667)); social-agent benchmark that grounds the v1.0 persona model's goals, secrets, and relationship semantics. See [`02_PERSONA.md §6`](02_PERSONA.md).

**ScopedKnowledgeQuery** — Externally-callable scope-bounded retrieval API surfacing the same machinery `build_persona_view` uses internally. Strict scope intersection over `ScopeTags` (now including `relationship_id`); cross-flag respected; consent gates honoured for user-scoped entries; lineage refs redacted for non-owner callers; read-only. Stages 1–3 of the §7 pipeline (filter / vector / graph fusion) without task-context-aware cross-encoder rerank. See `08_KNOWLEDGE.md §9.3`.

**Skill (Voyager)** — Executable code in soul.state.json skill_library; per-persona; learned-as-code; both Capability and Knowledge tier. See `08_KNOWLEDGE.md §2`.

**StagedRolloutEnvelope** — Coordination primitive for deploying an `ArtifactBundle` across multiple `PhysicalAsset` instances in staged waves. Each wave declares a group filter (composing with `AssetGroupEnvelope`), success criteria, rollback triggers, and a kernel-enforced minimum soak period. Wave N+1 cannot begin until wave N completes; rollback reverts per-wave via reverse `BatchStateAdvancement`. Bridge degradation pauses the rollout. Operator co-sign required for safety-critical domains. See `04_PROJECT.md §26a.9`.

**SkillTransferGrant** — Signed persona-to-persona skill transfer between teacher and learner with prerequisite gates (mode proficiencies, KindRegistry coverage, active relationship edge by default). Three modes: `copy` (duplicate; revoke advisory), `fork` (lineage parent recorded; revoke advisory), `by_reference` (signed pointer; revoke terminal). Safety-critical skill without an active `PersonaRelationshipEdge` requires operator co-sign. Demonstration evidence verified before `accepted → delivered`. Transitive transfer refused without explicit lineage. See `02_PERSONA.md §11.5`.

**Soul** — What the kernel owns about a persona. Includes SOUL.md (markdown identity file) + soul.state.json (sidecar). See `00_VISION.md §"Body / Soul / World"`.

**SOUL.md** — Canonical markdown identity file; schema soul/4 in v1.0; frontmatter frozen; EVOLVE-BLOCKs mutate. See `02_PERSONA.md §3`.

**Standardised (domain stage)** — Stage 4 of 4 promotion ladder; trust 0.95; functionally equivalent to operator-authored DomainContext. See `06_DOMAIN.md §3`.

**StructuredFeedback** — Unified outcome envelope. Includes (bench_measurement, peer_review_verdict, user_structured) plus 5 structured-outcome kinds (citation_observation, community_uptake, production_telemetry, test_results, regulatory_outcome). Each kind has a typed schema and an evolution-weight table. See `04_PROJECT.md §20-22`, `08_KNOWLEDGE.md §2`.

**SupersessionCascade** — Automatic trust-degradation mechanism triggered when a `KnowledgeRef` is marked `superseded_by`. Kernel traverses the citation/evidence graph and applies `direct_discount` (default 0.5×) to claims citing the superseded ref and `transitive_discount` (default 0.25×) to depth-2+ dependents. Depth-bounded (default 3), rate-limited (1 cascade per ref per 24h). Claims are flagged for re-evaluation, not deleted; persona may re-confirm or further downgrade. See `08_KNOWLEDGE.md §6.3`.

## T

**Tactic** — EVOLVE-BLOCK heuristic in SOUL.md; per-persona; signed mutations via mutation operators. See `08_KNOWLEDGE.md §2`.

**Task Class** — v1.0 has 10 task classes: CONVERGENT / DIVERGENT / MIXED / INTERACTIVE / RELATIONAL / PEDAGOGIC / PERFORMATIVE / EXISTENTIAL / DELEGATED / INVESTIGATIVE. See `03_TASKS.md §2`.

**TaskFingerprint** — Embedding of (task statement, examples, constraints, env, tools); used for K-line matching and routing weight scoping. See `01_KERNEL.md §1`.

**Teacher** — Cognitive mode (PEDAGOGIC); adapts explanation to learner state. See `02_PERSONA.md §4`.

**TeachingAuthorisation** — signed envelope binding (persona × skill_kind × deployment_context) declaring operator authorisation for that persona to teach that hazardous skill in that context. Required as precondition for the `HazardousSkillTeachingGate` (`01_KERNEL §2.9`) when teaching a skill whose application could cause `physical_harm_class ≥ bodily_injury`. Carries operator signature + optional credentialed-attestor co-sign (e.g., medical school dean signs for "Ren may teach septic-shock recognition to ICU rotation students"). Annual re-attestation cadence mandatory. See [`02_PERSONA.md §11.10`](02_PERSONA.md).

**Tier 1/2/3 Custody** — Key custody tiers: laptop (Tier 1), KMS (Tier 2), HSM (Tier 3). See `09_PROTOCOLS.md §8.1`.

**TestResults** — v1.0 MetaRegistry-seeded OutcomeKind for software-testing domains; not a substrate class. See `04_PROJECT.md §20.1`.

**Tool** — Promoted code via ToolArtifact FSM: DRAFT → SANDBOX → PROBATIONARY → TRUSTED → RETIRED. Four classes in v1.0: kernel-native (A), domain-required (B), persona-learned (C), human-bridged (D, via BridgeAsset). See `06_DOMAIN.md §5.4`, §5.5.

**ToolArtifact** — Schema for a promotable tool; carries code + contract + tests + verification_set; FSM at `06_DOMAIN.md §5.4`.

**ToolRequirement** — Schema for external-tool-required policy: claim pattern → required tool → required outcome. See `01_KERNEL.md §2`.

**Toolsmith** — Cognitive mode (universal); builds tools, sandboxes, verifiers, rubrics, judge prompts, principle docs. See `02_PERSONA.md §4`.

**Trust Score** — Dynamic scalar 0..1 attached to DomainContext, DiscoveredTool, KnowledgeRef, etc.; updated via Bayesian-flavoured formula (0.3 prior, 0.6 observed, 0.5× verifier-failure penalty, 0.2 demote threshold); promotion-gate threshold. See `06_DOMAIN.md §3` (stages) and `§5.3` (formula).

## U

**Universal Harm Constraints** — v1.0 1st safety floor source; kernel-hardcoded; cannot be overridden by any other source. Examples: no self-harm coaching, no illegal content, no manipulation of users in vulnerability states. See `01_KERNEL.md §2`.

**USER_ACCEPT** — Acceptance pathway: user explicitly approves output. See `03_TASKS.md §3`.

**UserBoundary** — First-class schema. Explicit per-(user, persona) refusal; overrides Consent in conflict. Mirrors `PersonaPersonaBoundary` (§11.6) shape: `severity` (refuse_silently / refuse_with_signal / refuse_with_audit), `mode` (hard / soft / advisory), `scope` (env_specific / global), `refused_interaction_kinds` (KindRegistry-resolved), `rationale_kind`. Migrates from implicit RelationshipRecord consent toggles to a structured entity. See `02_PERSONA.md §11.6a`.

**UserMemorySelectionRequest** — user-initiated selective forgetting / right-to-erasure primitive (closes the GDPR Article 17 gap). User specifies `selection_kind` (topic-cluster / time-window / specific-memory-ids / all-memories-with-tag) + `selection_payload`. Substrate marks selected memories `user_requested_forgotten`; tier-forced ARCHIVE; retrieval refused. Lineage entry preserved with redacted content for audit (operator may verify selection was honoured without re-reading forgotten content). Persona is notified through `MEMORY_SELECTION_HONOURED` event. See `02_PERSONA.md §11.7b`.

**UserMemoryTransparencyRequest** — user-initiated mirror of `PersonaMemoryTransparencyRequest` (§11.7); the "what do you remember about me?" structured query. User specifies `memory_tier_scope`, `env_scope`, `time_window`, `response_granularity` (summary_only / topic_index / episodic_excerpts / full_dump). Persona responds; operator co-signs at granularity ≥ episodic_excerpts. Rate-limited (default 1/30 days per persona). See `02_PERSONA.md §11.7a`.

**UserRelationshipReleaseRequest** — user-initiated relationship end primitive; mirror of `persona_relationship_one_sided_release` (§11.4). User specifies `memory_disposition` (delete-all / archive / freeze-readonly) and `notify_persona` flag. Lineage preserved at envelope grain (audit retains the request; persona's RelationshipRecord transitions to `ended_by_user_release`). Persona notified per flag; cannot refuse (user authority is final on their own relationship). See `02_PERSONA.md §11.4a`.

**USER_STOP** — User-emitted termination event; kernel enforces; severity levels (pause, stop, abort). See `01_KERNEL.md §10`.

## V

**Universal kernel policies** — Policies operating on every pathway: LLM transport retry, schema reformat, content refusal, context overflow, OWASP retrieval filter. See `09_PROTOCOLS.md §9`.

**VAD** — Valence / Arousal / Dominance triplet; emotional priors; seeds mood state. See `02_PERSONA.md §3`.

**VERIFIER_ACCEPT** — Acceptance pathway for CONVERGENT tasks; programmatic verifier cascade returns pass_rate=1.0. See `03_TASKS.md §3`.

**Verifier Cascade** — Ordered stages (fast → medium → expensive); rotation per rotation_period tasks (INV-6); Goodhart defence. See `08_KNOWLEDGE.md §2`.

**VerifierInvocationEvidence** — Schema (`verifier-invocation-evidence/1`) carrying the signed, hash-bound proof that a verifier stage ran against a specific artifact bundle version: recipe/stage ids and versions, input artifact hashes, execution surface, tool/panel refs, output hash, parsed verdict, and signatures. Missing or stale evidence blocks `verified` / required `accepted` transitions. See `07_ARTIFACTS.md §7`.

**VerifierRecipe** — Domain-specific verifier configuration; named, signed reference to a verifier cascade for an artifact kind. See `06_DOMAIN.md §7.1`.

**Visibility Tier** — Four tiers: private (operator only) / tenant (org) / federation (peer kernels) / public (hub). Applies to PersonaCard, ProjectCard, EnvCard, DomainContextCard. See `09_PROTOCOLS.md §3`.

**Voyager** — Wang et al. 2023 lifelong learning agent pattern; automatic curriculum + ever-growing skill library + iterative prompting; v1.0 skill library per persona. See `08_KNOWLEDGE.md §2`.

## W

**Wall-clock age** — A persona's primary age: `age = now − born_at`, continuous, monotone, never reset, and not paused by dormancy. Drives ALPS layering, the generativity gate's age term, and the newborn maturation ramp. Distinct from **experience** (task count) and **community standing** (relational). See [`02_PERSONA.md §7.2`](02_PERSONA.md).

**Wake Path 6** — when a user directly addresses a dormant persona by name (`target_persona_id` set in the task dispatcher), the kernel auto-wakes the persona before notification routing. Attention bumps to max(current, 0.6) for 2h; signed `dormant_wake_via_user_address` event. Rate-limited: ≤ 5 per user per persona per 24h. Closes the gap where dormancy suppresses `high`-urgency (direct address) notifications below the `critical` threshold. See [`05_ENVIRONMENT.md §5.2`](05_ENVIRONMENT.md), [`03_TASKS.md §4.1`](03_TASKS.md).

**.well-known/personaos-keys.json** — Public key registry for v1.0 signature verification; archived keys with rotation timestamps. See `09_PROTOCOLS.md §8.2`.

**World** — v1.0 surrounding context for a persona: environment (where they live), project (what they're working on), domain (knowledge they draw on), users + other personas + host kernel + federation peers + standards bodies. See `00_VISION.md §"Body / Soul / World"`.

## Numbered

**3 lineage scopes** — task / environment / domain. (Post-J8 retirement; "ProjectLineage" persists as a documentation filter over `EnvironmentLineage` on `project_workspace`-typed envs.) See [`01_KERNEL.md §3`](01_KERNEL.md), [`00_VISION.md §3`](00_VISION.md#3-invariants-j1j9).
**4 promotion stages** — EMERGENT / RECOGNISED / AUTHORITATIVE / STANDARDISED. See `06_DOMAIN.md §3`.
**5-tier ontology** — Coordination / Product / Capability / Knowledge / Context. See `08_KNOWLEDGE.md §1`.
**6-stage retrieval** — structured filter / vector / graph / fusion / rerank / persona composition. See `08_KNOWLEDGE.md §7`.
**7-scope memory tagging** — user / persona / session / project / env / app / org. See `08_KNOWLEDGE.md §5`.
**8 environment base types** — Solo / Pair / Team / Lab / Debate / Community / Constrained / Project_workspace. See `05_ENVIRONMENT.md §3`.
**7 persona layers** — Identity / Capability / Experience / Relationships / Mood / Goals / Voice. See `02_PERSONA.md §2`.
**8 acceptance pathways** — VERIFIER_ACCEPT / PANEL_ACCEPT / USER_ACCEPT / MUTUAL_ACCEPT / ENGAGEMENT_ACCEPT / GOAL_PROGRESS_ACCEPT / OPEN_ENDED / PROJECT_PROGRESS_ACCEPT. See `03_TASKS.md §3`.
**8 evolution signals** — bench_measurement / peer_review / verified / panel / user_feedback / project_milestone / engagement / rejection. See `02_PERSONA.md §8.1`.
**8 knowledge artefacts** — Tactic / Skill / Tool / Rubric / Lesson / K-line / ProvenFact / Meta-prompt. See `08_KNOWLEDGE.md §2`.
**8 safety floor sources** — universal harm / persona charter / user boundary / operator policy / domain safety extensions / external-tool-required / novelty-check / env charter. Plus 9th advisory. See `01_KERNEL.md §2`.
**9 v1.0 invariants** — J1-J9 (with 4 commitments C1-C4). See `00_VISION.md §2`.
**10 kernel invariants** — INV-1..10. See `00_VISION.md §3`.
**10 task classes** — CONVERGENT / DIVERGENT / MIXED / INTERACTIVE / RELATIONAL / PEDAGOGIC / PERFORMATIVE / EXISTENTIAL / DELEGATED / INVESTIGATIVE. See `03_TASKS.md §2`.
**11 round invariants** — INV_R1..R11. See `00_VISION.md §4`.
**11 anti-Goodhart safeguards** — jury heterogeneity / rotation / position-swap / length-control / versioned rubric / dissent preservation / style-strip / spot-check holdout / Goodhart canary / alternative rubric / caller-acceptance. See `08_KNOWLEDGE.md §2`.
**Media kinds (open set)** — v1.0 ships **no closed media-kind enum** (commitment C4). The MetaRegistry seeds seven media-shape-only kinds — `text`, `code`, `structured_data`, `table`, `plot`, `binary`, `external_ref` — whose storage class and MIME carry no domain knowledge. All other kinds (e.g. `schematic`, `spice_netlist`, `kicad_project`, `formal_proof`, `floor_plan`, `ifc_model`, `gantt_schedule`, `hamiltonian`) are emergent: a persona facing an unfamiliar shape drafts a `ProposedMediaKind` (`06_DOMAIN §7.5`); on acceptance the kind enters the per-domain `KindRegistry` (`06_DOMAIN §7.6`); on cross-domain standardisation it promotes to the MetaRegistry. See `07_ARTIFACTS.md §2`.
**12 framework adapters** — Claude Code / OpenAI SDK / LangGraph / CrewAI / MAF / Pydantic-AI / DSPy / smolagents / Semantic Kernel / MCP server / A2A server / MCP Proxy. See `09_PROTOCOLS.md §6`.
**14 cognitive modes** — 10 core: Perceiver / Abducer / Composer / Falsifier-Critic / Experimenter-Reviewer / Integrator / Curator / Reflector / Toolsmith / Historian. 4 relational: listener / storyteller / comforter / teacher. See `02_PERSONA.md §4`.
**22 mutation operators** — 9 core + 6 relational + 5 domain + 2 v1.0 additions. See `02_PERSONA.md §8.4`.
**v1.0 schema registry** — every v1.0 entity that crosses a process boundary declares a `schema: "<name>/<integer>"` field per INV-10; the canonical list lives in the §7 registry. See `09_PROTOCOLS.md §7`.

## Cross-reference index

For any v1.0 concept, the canonical doc and section:

```text
Identity              02_PERSONA §3, 09_PROTOCOLS §8
Charter               01_KERNEL §2.2, 02_PERSONA §3
Safety floor          01_KERNEL §2
Lineage               01_KERNEL §3
Schema versioning     09_PROTOCOLS §7
Budget admission      01_KERNEL §7
Sandbox               01_KERNEL §6
Observability         09_PROTOCOLS §4
Key custody           09_PROTOCOLS §8
Persona model         02_PERSONA
Cognitive modes       02_PERSONA §4
Lifecycle             02_PERSONA §7, 04_PROJECT §4, 05_ENVIRONMENT §4, 06_DOMAIN §3
Evolution             02_PERSONA §8
Mutation operators    02_PERSONA §8.4
Mood + Presence       02_PERSONA §6
Relationships         02_PERSONA §11
Personal goals        02_PERSONA §3
Task class            03_TASKS §2
Acceptance pathway    03_TASKS §3
Routing mode          03_TASKS §4
AnswerPackage         03_TASKS §5
Project               04_PROJECT
Conjecture            04_PROJECT §8
Obligation            04_PROJECT §9
Disagreement          04_PROJECT §10
PeerReview            04_PROJECT §11
NotationConvention    04_PROJECT §12
CitationGraph         04_PROJECT §13
Environment           05_ENVIRONMENT
Presence              05_ENVIRONMENT §5-7
Ambient stream        05_ENVIRONMENT §8
Observation surface   05_ENVIRONMENT §9
Notification routing  05_ENVIRONMENT §10
ProactiveIntent       05_ENVIRONMENT §11
Domain                06_DOMAIN
Emergence lifecycle   06_DOMAIN §4
Discovery             06_DOMAIN §5
Ingestion             06_DOMAIN §6
Inference             06_DOMAIN §7
Promotion gates       06_DOMAIN §3
Cross-domain transfer 06_DOMAIN §11
Artifacts             07_ARTIFACTS
Knowledge             08_KNOWLEDGE
Retrieval             08_KNOWLEDGE §7
Prompt evolution      08_KNOWLEDGE §11-12
MCP                   09_PROTOCOLS §2
A2A                   09_PROTOCOLS §3
Adapter integrations  09_PROTOCOLS §6

Acceptance tests      11_ACCEPTANCE_TESTS
```

## Acronyms and abbreviations

Acronyms in active use across the v1.0 corpus. Where a term has its own glossary entry above, the acronym row points to it; where it does not, the row carries the definition. This table is documentation-normative: an author writing a new v1.0 section MUST expand an acronym on first use unless it appears here.

| Acronym | Expansion | Note |
|---|---|---|
| **A2A** | Agent-to-Agent Protocol | Anthropic 2025; see entry under **A**. |
| **AGENT_CARD** | A2A Agent Card | Signed projection of a persona; see entry under **A**. |
| **ALPS** | Age-Layered Population Structure | Hornby 2006; see entry under **A**. |
| **API** | Application Programming Interface | Standard term; not redefined. |
| **AST** | Abstract Syntax Tree | Used in [`07_ARTIFACTS.md`](07_ARTIFACTS.md) for code-artifact verifier recipes. |
| **CI** | Continuous Integration | Standard term; appears in the release gate process gates and [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md). |
| **CLS** | Complementary Learning Systems | McClelland et al. 1995; episodic / semantic memory consolidation; see [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md). |
| **CRDT** | Conflict-free Replicated Data Type | Used in [`07_ARTIFACTS.md §5`](07_ARTIFACTS.md) for Yjs co-editing and G-set semantics. |
| **DGM** | Darwin–Gödel Machine | Lehman et al. 2024; fertility-weighted parent selection for evolution; see [`02_PERSONA.md §8`](02_PERSONA.md). |
| **DSPy** | Declarative Self-improving Python | Stanford 2023–; prompt-programming framework underpinning v1.0 prompt evolution; see [`08_KNOWLEDGE.md §11`](08_KNOWLEDGE.md). |
| **EdDSA** | Edwards-Curve Digital Signature Algorithm | RFC 8032; baseline signing primitive for v1.0 kernel keys; see [`09_PROTOCOLS.md §8`](09_PROTOCOLS.md). |
| **EU AI Act** | Regulation (EU) 2024/1689 on Artificial Intelligence | Cited as an operator-policy example only; substrate carries no closed list of regulated domains (C4). |
| **EAR** | Export Administration Regulations (U.S.) | Cited as an operator-policy example only; not in substrate. |
| **FAISS** | Facebook AI Similarity Search | Vector-search library cited as a hybrid-retrieval reference; see [`08_KNOWLEDGE.md §7`](08_KNOWLEDGE.md). |
| **FINRA** | Financial Industry Regulatory Authority (U.S.) | Cited as an operator-policy example only; not in substrate. |
| **FIPS** | Federal Information Processing Standards (NIST) | FIPS 186-5 is cited as a normative reference for signature schemes; see [`00_VISION.md §14.1`](00_VISION.md#141-normative-references). |
| **FSM** | Finite State Machine | Used throughout for lifecycle (persona, environment, domain, bridge). |
| **GDPR** | General Data Protection Regulation (EU) 2016/679 | Cited as an operator-policy example only. |
| **GEPA** | Genetic-Pareto reflective prompt optimization | DSPy 2025; see entry under **G**. |
| **GraphRAG** | Graph-augmented Retrieval-Augmented Generation | Microsoft 2024–; see [`08_KNOWLEDGE.md §7`](08_KNOWLEDGE.md). |
| **GRPO** | Group Relative Policy Optimization | RL technique cited as a comparator in DSPy GEPA literature. |
| **HIPAA** | Health Insurance Portability and Accountability Act (U.S.) | Cited as an operator-policy example only. |
| **HSM** | Hardware Security Module | Tier-3 custody for kernel master keys; see [`09_PROTOCOLS.md §8`](09_PROTOCOLS.md). |
| **IEC** | International Electrotechnical Commission | Standards body; appears in domain examples (e.g. IEC 60601 medical electrical). |
| **IEEE** | Institute of Electrical and Electronics Engineers | Standards body; cited as an external-standards example. |
| **ITAR** | International Traffic in Arms Regulations (U.S.) | Cited as an operator-policy example only. |
| **JSON** | JavaScript Object Notation | RFC 8259; wire format for several v1.0 schemas. |
| **JWK** | JSON Web Key | RFC 7517; format for `.well-known/personaos-keys.json`. |
| **K-line** | Knowledge-line | Minsky-style trigger-context-action record; see [`08_KNOWLEDGE.md §2`](08_KNOWLEDGE.md). |
| **KMS** | Key Management System | Tier-2 custody for scope-level signing keys; see [`09_PROTOCOLS.md §8`](09_PROTOCOLS.md). |
| **LLM** | Large Language Model | Standard term; not redefined. |
| **MAF** | Microsoft Agent Framework | One of the 12 v1.0 framework adapters; see [`09_PROTOCOLS.md §6`](09_PROTOCOLS.md). |
| **MAP-Elites** | Multi-dimensional Archive of Phenotypic Elites | Mouret & Clune 2015; diversity preservation; see [`02_PERSONA.md §8`](02_PERSONA.md). |
| **MCP** | Model Context Protocol | Anthropic 2024; see [`09_PROTOCOLS.md §2`](09_PROTOCOLS.md). |
| **MIME** | Multipurpose Internet Mail Extensions | Used as a media-type label on Artifact entities; see [`07_ARTIFACTS.md §3`](07_ARTIFACTS.md). |
| **MIPRO / MIPROv2** | Multi-prompt Instruction Proposal Optimizer | DSPy 2024; Bayesian instruction + demonstration search; see [`08_KNOWLEDGE.md §11`](08_KNOWLEDGE.md). |
| **MPA** | Memory Power Asymmetry | Risk addressed by J6 mitigations; see [`02_PERSONA.md §6`](02_PERSONA.md). |
| **NIST** | National Institute of Standards and Technology (U.S.) | Standards body; FIPS publisher. |
| **OQ** | Open Question | Documentation construct; format `OQ-<doc>-<n>`; see [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions). |
| **OTel** | OpenTelemetry | Industry-standard observability framework; see [`09_PROTOCOLS.md §4`](09_PROTOCOLS.md). |
| **OWASP** | Open Worldwide Application Security Project | Author of the LLM Top 10 threat model cited in [`01_KERNEL.md §2`](01_KERNEL.md). |
| **PR** | Pull Request | Standard term; not redefined. |
| **RAG** | Retrieval-Augmented Generation | Used as a retrieval-baseline reference in [`08_KNOWLEDGE.md §7`](08_KNOWLEDGE.md). |
| **RFC** | Request for Comments (IETF) | RFC 2119 / 8174 are normative; see [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). |
| **SDK** | Software Development Kit | Standard term; not redefined. |
| **SLA** | Service-Level Agreement | Used in domain-curator review-cadence prose; not a normative substrate construct. |
| **SRE** | Site Reliability Engineering | Audience role; see [`SPEC_CONVENTIONS.md §1.3`](SPEC_CONVENTIONS.md#13-audience-values-registered-set). |
| **TUI** | Text User Interface | Cited only in example body bindings (Claude Code). |
| **ULID** | Universally Unique Lexicographically Sortable Identifier | Preferred entity-ID form across v1.0 schemas; sortable by creation time. |
| **UUID** | Universally Unique Identifier | RFC 4122; alternative entity-ID form; ULID preferred for new schemas. |
| **W3C** | World Wide Web Consortium | Standards body; JSON-LD 1.1 reference. |
| **WG** | Working Group | Used in front-matter `authors:` / `reviewers:` lists. |
| **Yjs** | "Y" JavaScript CRDT library | Co-editing primitive; see [`07_ARTIFACTS.md §5`](07_ARTIFACTS.md). |

Acronyms appearing only inside an external reference (e.g. paper title, RFC title) are not duplicated here. Domain-specific acronyms used as scenario flavour in [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) (e.g. SPICE, KiCad, IFC) are documented in the scenario they appear in, not in this table; they are not load-bearing for the substrate.

## End

v1.0 is the single source of truth. For any v1.0 concept, this glossary is the index; the canonical doc is the source.
