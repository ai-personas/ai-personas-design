---
title: PersonaOS v1.0 — Domain
status: Stable
---

# 06 — Domain

> **Reader guide.** A domain is a body of knowledge, tools, and methods for a specific field — chip design, medicine, construction, mathematics. PersonaOS does NOT hardcode domains; AI Personas discover and build them through structured exploration. In this document, you'll learn how personas bootstrap knowledge in unfamiliar territory, how domain trust accumulates through a four-stage promotion ladder, and how domain-specific tools and safety rules are discovered. **Prerequisites:** `00_VISION.md`, `01_KERNEL.md`. **Key terms:** *DomainContext* = accumulated knowledge + tools for a field; *KindRegistry* = the open dictionary where domain-specific types are proposed and promoted; *promotion stages* = EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED (trust grows through use).

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). This document specifies DomainContext (authored + emergent), the domain emergence lifecycle, the 4 promotion stages (EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED), DiscoveredTool, KnowledgeIngestionRecord, InferredVerifierRecipe, ProposedSafetyExtension, BridgeAsset, cross-domain transfer, and the DomainCurator role. It realises commitments C1, C2, C3, C4.

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. Fully normative; RFC 2119 keywords carry normative force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174).

**In scope.** DomainContext as a first-class entity (authored and emergent origins), the recognition → probe → discovery → ingestion → inference → curation → promotion lifecycle, the four promotion stages (EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED), the entities DomainProbe, DiscoveredTool, KnowledgeIngestionRecord, InferredVerifierRecipe, ProposedSafetyExtension, BridgeAsset, DomainObservation, cross-domain transfer mechanisms, KindRegistry (env / artifact / task / domain kinds), DomainLineage (C1), and the DomainCurator role with operator gating for safety-critical promotions.

**Out of scope.** The kernel signing / lineage / safety floor primitives that gate every domain event (see [`01_KERNEL.md`](01_KERNEL.md)); persona-side modes used during probing and inference (see [`02_PERSONA.md`](02_PERSONA.md)); environment-scope membership and observation surfaces in which domain probes execute (see [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md)); the domain-scope schema registry entries (see [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry)); meta-prompt and skill libraries that personas carry across domain transitions (see [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)).

**Supersession.** Subsumes the prior-version emergent DomainContext and KindRegistry design.

**Structural deviation.** Follows the compressed-opening pattern of [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md#33-compressed-opening-permitted): Background, Goals, and Definitions are folded into §1 ("What a domain is"). The three §3.1 bookends (this section, the Risks table, and Open Questions) are present.

## 0a. Plain-Language Guide

*Here's how AI Personas learn new fields, explained without jargon.*

**What is a domain?**

A domain is simply a field of knowledge -- like "power electronics," "residential construction," "category theory," or "music composition." It bundles everything you need to work competently in that field: the background knowledge, the tools, the safety rules, the conventions, and the ways to check your work. Think of it as a complete toolkit for a specific profession or discipline.

**How domains come into being**

There are two paths. The first is *authored*: an operator (the person running the system) builds the domain from scratch, loading it with knowledge, tools, and rules before any AI persona uses it. This takes weeks but produces a fully trusted domain on day one. The second is *emergent*: a persona encounters an unfamiliar field during its work, and the system bootstraps a new domain from scratch by researching, learning, and accumulating trust over time. Most domains in v1.0 follow the emergent path.

**The four promotion stages**

An emergent domain starts at low trust and earns credibility through use. Stage 1 is *Emergent* (trust 0.3) -- brand-new, used only by the persona that created it. Stage 2 is *Recognised* (trust 0.6) -- multiple projects and personas have successfully used it, cross-checks pass. Stage 3 is *Authoritative* (trust 0.85) -- extensive real-world use, external validation, and for safety-critical work, explicit operator approval. Stage 4 is *Standardised* (trust 0.95) -- the operator declares it fully mature, equivalent to an authored domain. Trust can also go backwards: if knowledge drifts or becomes outdated, it can be demoted or deprecated.

**Domain probes: how the system explores the unknown**

When a persona hits an unfamiliar field, the system launches a *domain probe* -- a structured exploration. Think of it as sending a scout into uncharted territory. The probe has four phases: perceiving (what entities and terms exist here?), researching (what literature and references apply?), hypothesising (what structure does this field have?), and composing (assembling a starter domain from everything discovered). Probes can be narrow (just enough for the immediate task, costing a few dollars) or broad (building a proper foundation, costing more). The system can also run probes in the background while work continues, or pause work until the probe finishes.

**Tools, standards, and conventions**

Every domain needs tools -- software that performs domain-specific tasks, like a circuit simulator for power electronics or a proof checker for mathematics. The system discovers tools from registries, searches for them by need, or even writes new ones. It also catalogs external standards (like building codes or IEEE specifications) and tracks conventions -- agreed-upon symbols and notations that practitioners use (like "Fsw" for switching frequency).

**Safety extensions: domain-specific safety rules**

Beyond the universal safety checks that apply everywhere, each domain can have its own safety rules. For example, a power electronics domain might require an isolation check before any safety claim, or a construction domain might require a structural calculation before approving a load-bearing design. These extensions are proposed by personas, reviewed, and -- for safety-critical work -- approved by the operator before taking effect.

**Bridge assets: connecting the AI to the physical world**

The AI system lives in the digital world but sometimes needs access to physical things -- lab instruments, hardware accounts, fabrication services. Rather than asking a human to perform the same physical task repeatedly, the system asks the human once to set up a *bridge* -- a durable connection. After that one-time setup, the system uses the bridge autonomously. For example, a persona might ask: "Please install this Python driver for your oscilloscope." Once installed, the persona reads measurements on its own, every time.

**KindRegistry: the open dictionary of domain-specific types**

Different domains need different types of things. A construction project needs "floor plans" and "permit filings"; a mathematics project needs "proofs" and "conjectures." Rather than hardcoding these types, PersonaOS uses an open dictionary called the KindRegistry. Personas propose new types as they discover them, and the types earn trust through the same promotion stages as everything else.

**MetaRegistry: the universal starter dictionary**

When a type becomes useful across multiple domains -- like "peer-reviewed paper" or "code change" -- it can be promoted to the MetaRegistry, a cross-domain dictionary available to every domain. New domains automatically inherit these universal types without having to re-propose them.

**Cross-domain transfer: sharing knowledge between fields**

Skills, conventions, and tools learned in one domain can sometimes transfer to another. A verification recipe from power electronics might apply to RF engineering. The system manages these transfers carefully: trust starts lower in the new domain (the transferred item must prove itself again), and personal data, organizational secrets, and intellectual property are filtered out to prevent leakage.

**Knowledge ingestion: how the system learns from documents**

When a domain probe discovers relevant documents -- research papers, datasheets, standards, reports -- the system ingests them through a seven-stage pipeline: sourcing, parsing and chunking, embedding and indexing, provenance and licensing checks, tagging, safety filtering, and registration. Every ingested document gets a signed record tracking where it came from, what licence it carries, and how trustworthy it is. Paywalled or restricted documents are tracked but may not be fully ingested without operator permission.

## 1. What a domain is

A [**domain**](12_GLOSSARY.md#d) is a body of knowledge + tools + verification patterns + safety norms + conventions that a [persona](12_GLOSSARY.md#p) draws on when doing work in that domain (power electronics, mathematical analysis, customer support, music composition, jurisprudence, climbing route classification — anything humans organise as a field).

v1.0 supports two origins for a `DomainContext`:

- **Authored** — operator pre-built the DomainContext upfront (weeks of operator time per domain; instant `STANDARDISED` stage).
- **Emergent** — personas bootstrap the domain through work; lifecycle progresses through promotion gates (multi-month maturation).

Both paths produce a `DomainContext` of the same shape. The difference is **origin + trust evolution**.

## 2. DomainContext schema (domain-context/2)

*The DomainContext is the master record for a domain. It holds the domain's identity (name, version, maintainer), its origin and current promotion stage, all accumulated knowledge references, required and recommended tools, verifier recipes, safety extensions, hazard classifications, corpus evolution mode, session budget profile, credential directories, standards references, notation conventions, seed skills and charters, and novelty check configuration. Two hazard axes -- physical harm class and information hazard class -- classify the domain's risk shape without naming any specific domain. Corpus evolution mode (stable, evolving, or frontier) controls how aggressively the system re-ingests changing literature.*

**Technical detail:** See [A.1](#appendix-a1).

### 2.1 Worked DomainContext examples

Concrete shapes for two common domains. Both are valid `domain-context/2` instances.

*Example A is an operator-authored engineering domain (power electronics) at standardised stage with required simulation and design-rule-check tools, IEC 62368 isolation safety extension, and notation conventions. Example B is an emergent mathematical domain (category theory) at recognised stage with Lean proof verification, arXiv novelty checks, and mathematical notation conventions.*

**Technical detail:** See [A.2](#appendix-a2).

### 2.2 Versioning and rotation policy

*Domain versions are integer-bumped and signed. Projects pin a specific version at activation and opt in to upgrades. Classifier models rotate on schedule, knowledge corpora are re-indexed quarterly, all prior versions are retained immutably, and deprecation propagates to dependent projects with a migration window.*

**Technical detail:** See [A.3](#appendix-a3).

### 2.3 Domain hierarchy and multi-domain personas

*Domains form a hierarchy via parent references (e.g., smps_design sits under power_electronics which sits under engineering). Child domains inherit knowledge, tools, and safety rules from ancestors, with safety extensions using most-restrictive-wins. Multi-domain personas filter skills by the active project's domain, and cross-domain transfer goes through the signed CrossDomainTransfer mechanism (section 11). Notation collisions across domains are resolved by the project's domain winning, with explicit conflict events for genuinely cross-domain work.*

**Technical detail:** See [A.4](#appendix-a4).

## 3. The four promotion stages

*The four stages define the trust trajectory for domain entries. Emergent (trust 0.3): used only by the proposer, no operator review. Recognised (trust 0.6): 3 successful projects, 2+ co-signing personas, cross-source validation passes. Authoritative (trust 0.85): 10 successful projects, 5+ co-signers, 3+ months at recognised, external validation required, operator co-signature for safety-critical work. Standardised (trust 0.95): operator declaration or federation consensus, equivalent to a pre-built domain. Standardisation may be revoked on drift detection.*

**Technical detail:** See [A.5](#appendix-a5).

### 3.1 PromotionPolicy

*The PromotionPolicy configures the thresholds for each stage transition per domain: minimum successful projects, minimum co-signing personas, time-at-stage requirements, whether external validation is required, whether the operator must approve, drift detection thresholds for demotion, and an optional single-project promotion mode for one-shot domains (see section 3.2).*

**Technical detail:** See [A.6](#appendix-a6).

### 3.2 SingleProjectPromotionConfig

A persona may bootstrap a domain in service of a **single one-off project** — a project the same principal will not repeat. The standard `K=3 successful projects` threshold for EMERGENT → RECOGNISED makes the domain permanently un-promotable in this case — the `KindRegistry` stays private and useless to future probes. The fix is to provide a per-domain config that swaps project-count thresholds for **within-project evidence-density thresholds** plus an explicit operator (or, under collapse, degraded-gate) acknowledgment that the promotion rests on a single project's evidence.

Substrate-shape qualifier: "one-off" is a property of the **project-count relationship** between principal and domain, not of any specific domain content. A one-off project is one whose principal explicitly declares `expected_project_count = 1` at draft, signs `one_shot_rationale`, and accepts the resulting `trust_cap`. The substrate enumerates no specific category of one-off project.

*The SingleProjectPromotionConfig substitutes within-project evidence-density thresholds (verified attestation density, verifier recipe pass rate, as-built reconciliation clean rate, panel acceptance rate) for the standard multi-project thresholds. It requires explicit operator acknowledgment, is forbidden for safety-critical domains, and caps trust at 0.6.*

**Technical detail:** See [A.7](#appendix-a7).

**Why this is substrate-shape, no domain leak.** Every threshold is a ratio computed from kernel-tracked counts (`OutcomeFeedback`, `ExternalAttestation`, `InferredVerifierRecipe`, `AsBuiltReconciliation`, panel verdicts). The substrate never inspects what the project is *about*. `refused_when_safety_critical` is a substrate-shape interlock that reads the same hazard axes used everywhere else (§2). The trust cap is a number, not a name.

**Composition with promotion ceremony (§13).** When `single_project_mode.enabled = True` and all density thresholds satisfy AND the acknowledgment is signed, the kernel runs the standard atomic promotion ceremony (§13) with one additional signed event `SINGLE_PROJECT_PROMOTION_ACKNOWLEDGED` recorded in DomainLineage immediately before `promotion_event`. Replay must reconstruct both events to validate the promotion.

**Composition with DomainHarvest (§13a).** A domain that reaches RECOGNISED via single-project mode is eligible for `DomainHarvest` at project completion. The harvest carries the `trust_cap` forward so downstream consumers know the promotion rests on one project's evidence.

## 4. Domain emergence lifecycle

For a domain without pre-authored DomainContext, the kernel runs this lifecycle:

*The lifecycle proceeds through eight stages: recognition (domain unknown detected), probe (structured exploration), discovery (finding tools), ingestion (learning from documents), inference (deriving verifier recipes and safety rules), proposal (submitting entries for review), curation (consolidation and quality review), and promotion (advancing through the four trust stages).*

**Technical detail:** See [A.8](#appendix-a8).

### 4.1 Recognition

`DOMAIN_UNKNOWN_DETECTED` event fires when any of seven signals occur: empty domain context (A), persona has no matching skills (B), retrieval returns low scores (C), persona self-assesses as unknown (D), cross-persona terminology disagreement (E), existing emergent context at low stage (F), or kind unknown for domain (G, v1.0 -- triggers a probe extension for the missing kind).

*The DomainUnknownDetected event records which signals fired, the candidate domain hint, the persona and project context, and a proposed probe with budget estimate.*

**Technical detail:** See [A.9](#appendix-a9).

### 4.2 DomainProbe

*The DomainProbe is the master record for a structured exploration of an unknown domain. It tracks the probe's status (initiated through completed or abandoned), its expansion strategy (narrow, broad, or adaptive), four exploration phases (perceiver, historian, abducer, composer), all discovered tools, ingested knowledge, inferred recipes, proposed conventions and safety extensions, budget consumption, contributing personas, and final outcome.*

**Technical detail:** See [A.10](#appendix-a10).

### 4.2.1 Probe phase record schemas

Each of the four probe phases emits a signed phase record. The records carry the structured artifact of that phase forward to the next.

*PerceptionRecord captures extracted entities, terminology, references, and constraints. HistorianRecord captures sources queried, candidate references, deduplication, and relevance rankings. AbductionRecord captures candidate domain structure, subdomains, ontology fragments, tool and verifier categories, and risks. CompositionRecord produces the emergent domain context skeleton at trust 0.3.*

Records are append-only into the DomainLineage; later phases consume earlier records by reference, never by mutation.

**Technical detail:** See [A.11](#appendix-a11).

### 4.3 Probe strategies

*Three strategies govern probe scope. Narrow: just enough for the immediate task (approximately 5 papers, minimal tool discovery, $1-5). Broad: build a proper foundation (20-50 papers, full tool discovery, verifier recipes, safety considerations, $10-50). Adaptive: start narrow and expand on signals, escalating to operator gate on safety-critical signals and branching into sibling probes on cross-domain entities.*

**Technical detail:** See [A.12](#appendix-a12).

### 4.4 Probe completion criteria

Precise thresholds per expansion strategy. A probe is `completed` only when ALL criteria for its strategy are met; failing probes emit `PROBE_INSUFFICIENT` and re-run at broader strategy.

*Narrow completion requires at least 1 verified pattern, 3 ingested knowledge references, and persona competence at or above 0.5. Broad completion requires 2 successful projects, 5 co-signing personas, tool discovery saturation, 2 inferred verifier recipes, 1 safety extension proposal (if relevant), and 5 co-signed conventions. Adaptive completion selects narrow or broad criteria based on signals, upgrading to broad on safety-critical or cross-domain signals. Frontier-mode domains do not complete in the usual sense -- the probe stays persistently active with daily ingestion budgets, and trust caps at 0.7 until corpus drift stabilises.*

**Technical detail:** See [A.13](#appendix-a13).

#### 4.4.1 CorpusDriftMetric — frontier → non-frontier transition criterion

The `§4.4` sliding-window criterion referenced "corpus drift rate below threshold" without defining the metric, the threshold, or the window parameter K. Without a defined metric, the frontier trust cap (0.7) never lifts in a principled way.

*The CorpusDriftMetric computes drift rate as (superseded + retracted + contradicted references) / active references over a 30-day trailing window. When drift rate stays below the exit threshold (default 5%) for K consecutive windows (default 6 months), exit eligibility triggers. The threshold and window count are operator-tunable per domain.*

**Technical detail:** See [A.14](#appendix-a14).

**Lifecycle.**

The kernel computes `CorpusDriftMetric` at the end of each 30-day window for every domain in `frontier` mode. When `exit_eligible = True`:

1. Kernel emits `FRONTIER_MODE_EXIT_ELIGIBLE` lineage event.
2. Operator must co-sign `FRONTIER_MODE_EXIT_CONFIRMED` to lift the frontier trust cap. Operator may judge that external factors explain the low drift (e.g., field-wide conference moratorium, seasonal publication patterns) and decline.
3. On operator confirmation, `DomainContext.corpus_evolution_mode` transitions from `"frontier"` to `"evolving"` (or `"stable"` if operator judges full stabilisation). Trust cap lifts from 0.7 to the standard scale. AUTHORITATIVE promotion (0.85) becomes reachable.
4. If drift rate rises above threshold again after exit, operator may re-enter frontier mode via `FRONTIER_MODE_RE_ENTERED` (operator-signed).

**Constraints.**

- **Operator-gated exit.** The metric determines eligibility; the operator determines confirmation. This prevents premature exit in fields with seasonal patterns.
- **Threshold is operator-tunable.** Default 0.05 (5% supersession rate per month) is calibrated for medium-velocity fields. High-velocity fields (AI/ML, genomics) may need 0.10; slow-moving fields (pure mathematics) may need 0.02.
- **K is operator-tunable.** Default 6 consecutive windows (6 months). Safety-critical domains SHOULD use ≥ 9 (9 months of stability before cap lifts).
- **Re-entry is operator-signed.** Once exited, drift rate is still monitored; re-entry requires explicit operator action, not automatic.

**Tests:** A-CDM1 (metric computation from KnowledgeRef events), A-CDM2 (consecutive window counting), A-CDM3 (exit eligibility triggers at K windows), A-CDM4 (operator co-sign required for exit), A-CDM5 (frontier re-entry on operator action), A-CDM6 (trust cap lifts after confirmed exit). See [`11_ACCEPTANCE_TESTS.md §9l`](11_ACCEPTANCE_TESTS.md).

**DomainLineage:** `corpus_drift_metric_computed`, `frontier_mode_exit_eligible`, `frontier_mode_exit_confirmed`, `frontier_mode_re_entered`.

### 4.5 Multi-persona probe coordination

When two personas trigger probes for the same `candidate_domain_hint`, the kernel picks one of three coordination options.

*Option A (independent probes): each persona runs its own probe; results reconciled at promotion. Option B (shared probe, default for same-env): kernel elects a lead persona; others contribute per their roles. Option C (federated, multi-kernel): probes across kernels share artifacts via A2A. Default rule: same-env uses B, cross-env same-kernel uses A, cross-kernel with operator-approved A2A uses C.*

**Technical detail:** See [A.15](#appendix-a15).

### 4.6 Sequential vs Interleaved probe routing

A persona facing an unfamiliar domain mid-task chooses between two integration modes.

*Interleaved (default): probe runs in the background while the task progresses slowly, suited to investigative work. Sequential: probe completes fully before the task resumes, suited to high-stakes work where acting before knowing is risky, requiring operator approval for safety-critical domains. Both modes carry operator-set budget caps; exhausted budgets halt the probe.*

**Technical detail:** See [A.16](#appendix-a16).

### 4.7 Probe budget caps and PROBE_BUDGET_THRESHOLD

*ProbeBudgetCaps configures per-probe, per-domain, and per-persona budget limits with warning (75%) and halt (100%) thresholds. A safety-critical multiplier increases the budget for high-hazard domains. Corpus size scaling (log2 of standards and literature counts) adjusts the effective cap based on how much material needs ingesting. ProbeBudgetThresholdEvent fires at the warning or halt threshold, routing to operator and persona for budget increase or halt acceptance.*

**Technical detail:** See [A.17](#appendix-a17).

Threshold events route to operator + persona; operator may approve additional budget (signed `BUDGET_INCREASE`) or accept HALTED state.

### 4.7.1 ProbeBudgetEnvelope and pledge model

`ProbeBudgetCaps` (§4.7) sizes the cap; it does not say **who supplies the units**. A persona attempting an unfamiliar domain may face an evidence corpus so large that the probe cannot complete inside the principal's default allowance — yet halting silently would let `J5` (open capability) degrade into "open capability you cannot pay for." v1.0 separates the cap from the pledge: an explicit `ProbeBudgetEnvelope` declares which **funding-shape** supplies the units. The substrate names no specific funder; it enumerates the topological positions of any funder relative to the principal.

*The ProbeBudgetEnvelope tracks requested units, pledges, consumption, and state. BudgetPledge supports five funding kinds describing who supplies the budget: principal pledge (self-funded), non-principal internal pledge (operator or approval chain), non-principal external pledge (external agent), prior domain amortization (credit from shared evidence in a sibling domain), and federation pool share (v1.1+). ProbeBudgetPledgeRequest lets a persona request additional pledges when a probe runs low, with fallback options (halt, narrow strategy, defer to operator, or release).*

**Technical detail:** See [A.18](#appendix-a18).

**Admission rule.** Per `INV-7` (hard kernel gate), every LLM / sandbox / tool call inside a probe first checks `BudgetState.can_call()` against the **envelope's** consumed-vs-pledged units. When `consumed_units / sum(pledged_units) ≥ warn_at_pct`, kernel emits `PROBE_BUDGET_THRESHOLD` (per §4.7) **and** `ENVELOPE_LOW`. At `halt_at_pct` the probe halts; the persona may draft a fresh `ProbeBudgetPledgeRequest` for additional pledges (any combination of pledge kinds) — admission resumes when sufficient pledged units sign.

**Principal-collapse interaction.** Under `principal_topology = operator_is_user` (`01_KERNEL §2.4`):
- `principal_pledge` is admissible (the principal funds its own probe).
- `non_principal_internal_pledge` is refused — no separate operator exists to supply it.
- `non_principal_external_pledge` requires the backing `ExternalCommitment` to be signed by an `ExternalAgent` whose credential is disjoint from the principal.
- `prior_domain_amortization` and `federation_pool_share` are admissible per their own rules.

**Lineage.** Envelopes and pledges emit DomainLineage events `ENVELOPE_DRAFTED`, `PLEDGE_ATTACHED`, `PLEDGE_DRAWN_DOWN`, `ENVELOPE_EXHAUSTED`, `ENVELOPE_RELEASED`, `ENVELOPE_REVOKED`. Each event is signed and replayable.

**Why this is substrate-shape, not domain-shape.** The five `pledge_kind` values describe *topological position* of the funder relative to the kernel principal (inside / outside / amortized / federated). They name no industry, no grant programme, no domain category. The currency_or_unit string is opaque to the kernel — the same envelope mechanism supplies units for any domain whose probe needs them.

### 4.8 FederatedDomainProbe — cross-kernel shared ingestion (v1.1+ deferred)

When multiple kernels probe the same frontier domain (e.g., several research groups bootstrapping the same emerging field), each currently pays its own ingestion cost. v1.1 introduces a federated-shared-probe schema that lets participating kernels pool ingestion under a single signed coordination record. The schema is reserved here so emergent contexts can be retroactively federated when v1.1 ships.

*The FederatedDomainProbe coordinates shared ingestion across participating kernels with a coordinating kernel driving ingestion, a shared knowledge pool and KindRegistry, configurable cost allocation (equal split, usage proportional, coordinator pays, or pledge pool), periodic drift audits, and a quorum requirement for cross-kernel promotion.*

**Technical detail:** See [A.19](#appendix-a19).

**Composition with §4.7.1 ProbeBudgetEnvelope:** participating kernels supply pledges of kind `federation_pool_share`; the shared pool draws against the union, attributing draws per `cost_allocation_method`. Each kernel's local probe inherits the shared pool as a constituent budget; local-only pledges remain admissible alongside.

**Drift audit:** the coordinating kernel periodically re-hashes the shared KnowledgeRef set + KindRegistry; peers compare. Divergence ≥ threshold emits `FEDERATED_PROBE_DRIFT_DETECTED`; depending on severity, peers may fork (state → fragmented) or reconcile via a signed convergence proposal.

**Why deferred to v1.1:** cross-kernel federation arrives in v1.1 (the v1.1 federation milestone); the schema is reserved now so single-kernel probes can be retroactively federated without breaking lineage. Single-kernel v1.0.5 probes are *prior-domain-amortizable* into a future federated probe via the `prior_domain_amortization` pledge kind.

## 5. Discovery — five sources (v1.0 capability tier)

Prior versions distinguished three tool classes and made discovery dynamic; v1.0 adds Source 5 for physical-world coupling.

*Six sources of capability discovery. Source 1 (MCP registry local): operator-installed tools on the local kernel. Source 2 (MCP registry federated): tools from peer kernels via A2A. Source 3 (MCP-Zero active discovery): semantic search for tools by expressed need. Source 4 (persona-authored, Voyager): persona writes the tool if none exists. Source 5 (human-bridged): persona asks a human once to set up a physical-world bridge (instrument, account, etc.) that becomes a durable autonomous tool. Source 6 (payment-bridged, Class E): for capabilities requiring real money, each payment requires fresh human authorisation and is intentionally outside the DiscoveredTool taxonomy.*

**Technical detail:** See [A.20](#appendix-a20).

### 5.1 DiscoveredTool schema

*The DiscoveredTool records a tool's identity, discovery source (one of the five classes), semantic match score, description, schema, capability, latency and cost estimates, publisher trust, smoke test results, lifecycle stage (candidate through accepted or rejected), usage counts, and trust score in the domain.*

**Technical detail:** See [A.21](#appendix-a21).

Trust score updates per success rate; capped at 0.95 unless kernel-promoted to class A.

### 5.2 Discovery + smoke-test 10-step flow

*The 10-step flow: persona expresses a need, kernel queries registries, top-K candidates returned, persona reviews and picks, kernel runs a smoke test (schema validation, dry-run, publisher attestation check), passing tools enter at candidate stage with trust 0.3, persona invokes for first task, after K successful uses the tool advances to trial then accepted, and after domain promotion it can become class B (domain-required) or class A (kernel-native).*

**Technical detail:** See [A.22](#appendix-a22).

Smoke-test failures emit `DISCOVERED_TOOL_REJECTED` with reason; rejected tools are never auto-retried within the same probe.

### 5.3 Trust score evolution formula

A `DiscoveredTool.trust_score_in_domain` starts at 0.3 and updates via a Bayesian-flavoured rule.

*During cold-start (fewer than 5 uses), trust ramps at 0.1 per success. After 5 uses, trust blends a prior (weight 0.4) with observed success rate (weight 0.6). Trust is capped at 0.95 unless kernel-promoted to class A. Verifier failures halve trust. Tools below 0.2 trust require explicit persona consent plus operator review.*

**Technical detail:** See [A.23](#appendix-a23).

Tools below trust 0.2 require explicit persona consent + operator review before any further use; cleanly recovers if subsequent uses re-establish trust.

### 5.4 ToolArtifact state machine (Voyager class-C promotion)

When a persona authors a tool via Voyager (no acceptable discovered candidate), the `ToolArtifact` follows a kernel-enforced FSM. v1.0 retains the inherited stage names; mapping to class-B promotion is the standard path.

*The FSM proceeds: PROPOSED (must include verification set), SANDBOXED (kernel runs tests; hard failures reject), VERIFIED (callable by author only), PROMOTED (auto-promotion if 5+ test cases, clean cascade, zero violations across 10 uses, author fitness above median -- otherwise operator review), and REVOKED (on cascade failures, constraint violations, supersession, or operator action). Personas cannot promote their own tools; promotion is kernel-enforced.*

**Technical detail:** See [A.24](#appendix-a24).

Cross-kernel use of `PROMOTED` tools requires federation consent (v1.1+).

### 5.5 Human-bridged discovery + BridgeAsset (v1.0 Class D)

When a needed capability requires **physical-world coupling** — an instrument reading, a hardware account, a fab submission, a lab connection — no MCP server or persona-authored skill can synthesise it from text. The capability must cross out of the kernel into the physical world. v1.0 makes the human a **bridge resource, not an executor**: the persona drafts a one-time `HumanAssistRequest`; the human grants once; the bridge becomes a durable `BridgeAsset` (Class D tool); the persona uses it autonomously thereafter.

**Core principle — Minimize Human Bootstrap Burden (MHBB):** the persona MUST prefer "ask once, automate after" over "ask each time," design the minimum-friction one-time action, never re-ask for recurring actions an established bridge could serve, and declare degradation evidence when re-establishing a degraded bridge.

*The HumanAssistRequest schema captures the need summary, the durable capability it unlocks, estimated one-time effort, expected recurrence frequency and class (one-shot bridge, renewable credential, or irreducible human content), a minimum-friction script, safety disclosures, rollback instructions, validation test, MHBB ladder tier (off-the-shelf install, persona-authored bridge, or human professional work), optional bridge design artifact reference, consent scope, and expiration.*

**Technical detail:** See [A.25](#appendix-a25).

**`BridgeAsset` schema and FSM:**

*The BridgeAsset records the bridge's identity, the request that spawned it, the granting user, capability kind (KindRegistry-resolved), capability descriptor (opaque to kernel), lifecycle state, validation schedule, consecutive failure count, optional closed-loop latency floor, and related project/environment/domain. The lifecycle FSM proceeds: REQUESTED, ESTABLISHING, ACTIVE, DEGRADED, LOST (with re-establishment looping back to ESTABLISHING), VALIDATED, and terminal REVOKED.*

**Technical detail:** See [A.26](#appendix-a26).

Each transition emits a signed lineage event in the most-local scope (project if `related_project_id` set, else env, else domain). Events: `HUMAN_ASSIST_REQUESTED`, `HUMAN_ASSIST_DRAFTED`, `HUMAN_ASSIST_GRANTED`, `BRIDGE_ESTABLISHED`, `BRIDGE_VALIDATED`, `BRIDGE_DEGRADED`, `BRIDGE_LOST`, `BRIDGE_RE_ESTABLISHED`, `BRIDGE_REVOKED`.

**Bridge → MCP tool registration:**

When `state` transitions to `ACTIVE`, the kernel registers the bridge as a Class D tool in the local MCP registry. Subsequent persona work uses it via the standard MCP call path — *no further human ask*. The tool's `discovery_source` is `human_bridged` and its `bridge_asset_id` links back to the BridgeAsset.

**Degradation + re-establishment:**

The persona MUST validate the bridge per `validation_period` (default daily for instruments, weekly for accounts). On `consecutive_validation_failures ≥ 2`, the bridge enters `DEGRADED`. After one more failure, `LOST`. Re-establishment requires a new `HumanAssistRequest` — but with a **stronger** minimum-friction script (e.g., "let's add auto-reconnect so this doesn't break again"). The kernel emits an `MHBB_RECURRENCE_DETECTED` warning if the same kind of bridge is re-requested more than 3 times in a quarter; operator should investigate the root cause of brittleness.

**Worked example (quantum):**

*A persona needing to measure qubit T1 drafts a HumanAssistRequest with a pip-install script (15 minutes, one-time). The human runs the script once; the bridge enters ACTIVE and registers as an MCP tool. The persona then invokes measure_t1 autonomously every time. If the API key expires, the bridge degrades and the persona asks the human to refresh the key -- not to re-run measurements.*

**Technical detail:** See [A.26](#appendix-a26).

This pattern is how v1.0 honours its stated out-of-scope on physical embodiment (`00_VISION.md`) while still letting cooperative work cross the boundary when a human consents. The kernel does not embody; it bridges, with the human as one-time intermediary and the BridgeAsset as the durable record.

### 5.5.4 Bridge-design fabrication — Tier 3 of the MHBB ladder

When no off-the-shelf software or service reaches the needed capability (Tier 2 exhausted), the persona's next step is to **author the bridge design itself** (`02_PERSONA §11.1` Tier 3) and ask the human to fabricate / install / deploy it once. This is the case in v1.0 when:

- the user has hardware the persona wants to access ("I have the instrument you want to probe");
- no off-the-shelf driver / wrapper / service exists;
- the alternative would be to ask the human to operate the instrument every session (Tier 5 anti-pattern).

The persona produces a **BridgeDesignArtifact** — an ArtifactBundle whose payload is the bridge mechanism itself, in machine-actionable form. The kind of artifact is per-domain emergent (resolved through KindRegistry, never substrate-enumerated).

*Plausible bridge-design kinds include software designs (drivers, shim services, REST wrappers, ingestion pipelines), hardware designs (adapter PCBs, cable specs, firmware), and protocol/process designs (calibration protocols, handoff workflows). These are illustrative, not a closed list.*

**Technical detail:** See [A.27](#appendix-a27).

The HumanAssistRequest's `bridge_design_artifact_ref` points to the artifact; the `minimum_friction_script` tells the human what to do with it (fabricate from gerbers, install the service, flash the firmware, run the calibration routine once). The `expected_one_time_effort_minutes` is the persona's honest estimate of the human's bench time.

**Lifecycle.** When the bridge enters `ACTIVE`, the persona uses the bridged capability autonomously via the standard MCP path (just like Tier 2). The BridgeDesignArtifact stays in the project's ArtifactBundle list as a first-class deliverable — it's reusable across projects (cross-domain transfer per §11), evolvable per ArtifactBundle versioning, and contributes to the persona's `skill_library` as a Class C/D capability the persona has demonstrably authored.

**Worked example — homemade quantum instrument:**

*A persona needing to measure T1 of a homemade transmon qubit authors a bridge-design artifact (pyvisa driver shim, mixer daemon, ADC streaming service, REST endpoint, systemd units, install script). The human installs once (90 minutes); the bridge enters ACTIVE and registers as an MCP tool. The persona then measures autonomously. If T2 measurement is later needed, the persona forks the design and asks the human to redeploy once more (30 minutes), for a total of 2 hours instead of 60 minutes per measurement.*

**Technical detail:** See [A.28](#appendix-a28).

**Honest limits of Tier 3.**

1. **Hardware bridges have high friction.** Persona-authored PCB designs require the user to fabricate or order them — days to weeks of latency. Software bridges are vastly preferred.
2. **The persona's authored code is just code.** It MUST still pass smoke-tests, verifier cascade (where applicable), and the OWASP filter; it can have bugs. The persona owns the design-debt of its bridges and MUST maintain them.
3. **Skill scaffolding.** A young persona may not yet have the skill to author a driver. The persona may need to first ingest the instrument's manual (Tier 3 of ingestion §6), then synthesise the driver. If the persona's competence is insufficient, the kernel honestly says so and the user / operator may bring in human help to author the bridge — escalation, not silent failure.
4. **Distinguishing from Tier 4.** A Tier 3 request enables a CAPABILITY the persona will then exercise autonomously. A Tier 4 request consumes the human's PROFESSIONAL WORK (which the persona could never have performed). Both are admissible; conflating them obscures audit.

### 5.5.5 BridgeCalibrationBinding — instrument provenance on measurement bridges

A `BridgeAsset` whose `capability_kind` produces *measurements with uncertainty* — laboratory instruments, scales, thermal probes, EMC scanners, spectrometers, medical sensors — is only as trustworthy as its **calibration chain**. v1.0 already models the chain for `InstrumentAsset` (`04_PROJECT §26a.2` measurement extensions); this section pulls the same primitive *down to the bridge layer* so the kernel can refuse to admit measurements through a stale-calibration bridge **before** any persona-authored verifier runs.

The binding is substrate-shape: a kernel-held attestation expiry on the bridge, refused by admission when stale. Domain-specific calibration kinds (NIST-traceable, ISO 17025, in-house transfer standard, factory cert only) are emergent `calibration_kind` entries in the per-domain KindRegistry.

*The BridgeCalibrationBinding attaches calibration provenance to measurement bridges. It records calibration kind (KindRegistry-resolved), attestation, reference standard chain, timing (calibrated at, expires at, interval kind), and drift bounds. BridgeAsset gains two fields: calibration_binding_id and calibration_required. The admission rule checks expiry, use counts, reference chain completeness, and drift bounds, refusing and degrading the bridge on failures.*

**Technical detail:** See [A.29](#appendix-a29).

**Events.** `bridge_calibration_bound`, `bridge_calibration_renewed`, `bridge_calibration_expired`, `bridge_calibration_drift_exceeded`. Each signed in the most-local scope.

**Persona-evolvable surface.** Calibration kinds, reference standard names, drift bounds — all KindRegistry-resolved. The substrate carries shape (`interval_kind` enum, expiry datetime, chain list); the persona supplies content.

**Why this is at the bridge layer, not only at InstrumentAsset.** `InstrumentAsset` is a PROJECT-scope record of an instrument-as-physical-asset. The same physical instrument may be reached through a `BridgeAsset` across many projects in the same environment. The calibration provenance belongs with the bridge so every project sees the same expiry. The `InstrumentAsset` record (when present) links to the same binding.

**Acceptance tests.** A-BC1 (admission refused on expired binding), A-BC2 (chain verifies through external_attestations), A-BC3 (drift bound triggers degrade), A-BC4 (persona-emergent calibration_kinds resolve via KindRegistry).

### 5.5.6 BridgeInstallerKind — recursive and kernel-trusted bridging

v1.0's MHBB ladder presumes a **human** installs a bridge. Three cases break this presumption:

1. A persona authors a bridge whose installation target is **another kernel-trusted system** (e.g., an autonomous lab robot, a previously-bridged factory cell, a service mesh under operator control). The substrate had no concept of non-human installer.
2. A bridge whose installation IS performed BY another bridge — a fabrication bridge produces a measurement bridge; an installer service deploys a driver bridge. Recursive bridging.
3. A bridge installed by an `ExternalAgent` other than the principal (a vendor field engineer, a partner-org operator). Already partially modelled, but installer-identity is implicit.

The fix is substrate-shape: enumerate the **topology** of who-installs, with each non-human installer cryptographically attested and capped by the installer's own trust ceiling.

*BridgeInstallerKind enumerates four installer topologies: human (default), external agent (vendor or partner), kernel-trusted system (another autonomous system admitted by operator policy), and chained bridge (recursive -- an existing bridge installs a new one). BridgeAsset gains fields for installer kind, id, attestation, trust ceiling, and hazard envelope at install time. The installer dominance rule ensures a bridge's hazard envelope cannot exceed its installer's authority, enforced at admission.*

**Technical detail:** See [A.30](#appendix-a30).

**Trust ceiling propagation.** Trust on outputs reaching the bridge is capped by `installer_trust_ceiling`. A chained_bridge whose installer is an EMERGENT-grade bridge inherits EMERGENT-grade ceiling on its outputs. A kernel-trusted system whose attestation places it at trust 0.65 caps all bridges it installs at 0.65, regardless of their own validation history (the installation-chain weak link dominates).

**Recursive depth bound.** Substrate refuses `CHAINED_BRIDGE` chains deeper than `max_bridge_recursion_depth` (operator-policy; default 3). Empirically, deeper chains lose interpretability faster than they gain capability.

**Principal-collapse interaction.** Under `principal_topology = operator_is_user` (`01_KERNEL §2.4`), non-human installers require a non-principal cosigner attestation — the principal cannot self-attest the installer. This mirrors the §5.6 credential-collapse handling.

**MHBB still applies.** Even with non-human installers admitted, the ladder is preferred-human-first when a human installer is genuinely simpler. A kernel MUST NOT prefer kernel_trusted_system installers when a one-time human action would have worked: the persona MUST record `installer_kind_rationale` whenever a non-HUMAN installer is selected, and the operator MAY audit.

**Acceptance tests.** A-BI1 (kernel-trusted system installer admitted with attestation), A-BI2 (chained bridge respects depth bound), A-BI3 (hazard envelope dominance refused on violation), A-BI4 (principal-collapse cosigner requirement enforced), A-BI5 (trust ceiling caps downstream outputs).

### 5.6 CredentialDirectoryRef — resolving attestor credentials

`ExternalAttestation.attestor_credential_id` (`04_PROJECT §26a.3`) is a free-form string (license number, board registration, certification ID). Without a resolution path, the kernel cannot tell a real PE stamp from a forged one — the cryptographic chain breaks at the analog signature. `CredentialDirectoryRef` is the per-domain mechanism that closes that gap, mirroring the shape of `StandardRef` (`§7.4`).

*The CredentialDirectoryRef records a directory's identity, publisher, access method (API, MCP tool, manual lookup, operator-provided, or not accessible), credential kinds it resolves (KindRegistry-resolved), trust score, cache TTL, and operator verification status. The lookup flow finds matching directories, queries them for credential validity, and emits CREDENTIAL_VERIFIED or CREDENTIAL_UNVERIFIED lineage events.*

**Technical detail:** See [A.31](#appendix-a31).

**Without a directory.** Many domains will not have a directory at emergence time (a homeowner's local AHJ may have no public credential API). The attestation is still admissible; `credential_unverified=True` is set; downstream J4 acceptance treats the attestation as PANEL-grade evidence only (it cannot satisfy the credentialed-attestor leg of `01_KERNEL §2.5`). The honest degradation matches the v1.0 stance: "the system honestly degrades trust rather than manufacturing certainty" (`00_VISION` OOS).

**Promotion path.** A persona may catalog a `CredentialDirectoryRef` as an emergent proposal; operator review promotes it to `operator_verified=True`. Without verification, lookups are still attempted but the directory's own trust score caps the credential's trust at the directory's trust × the attestation's freshness.

**Honest limits.**
1. Many real credential boards have no public API; manual lookup or operator-provided JSON dumps fill the gap.
2. The directory itself is a trust root; a compromised directory poisons every attestation it ratifies.
3. Revoked credentials between lookups and use of the attestation are an audit lag — the kernel periodically re-verifies; verification age is part of the lineage.

**Peer-attestation fallback for frontier domains.** Some domains have no credentialing authority — there is no licensing board for "quantum-device designer," "novel-protein engineer," "advanced-AI safety researcher." For such domains, v1.0 supplies a substrate-pure fallback: `PeerAttestationPool`.

*The PeerAttestationPool provides a credential-directory-free fallback for frontier domains without licensing boards. It defines eligibility criteria (KindRegistry-resolved), peer membership, quorum requirements (default 3 with disjoint affiliations), and a trust cap of 0.7 (below credentialed directory's 0.95). The pool is substrate-pure: it names no professions or fields; criteria are emergent kinds.*

**Technical detail:** See [A.32](#appendix-a32).

A PeerAttestationPool admits **co-signed peer review** as a substitute for credential-directory resolution. When an `ExternalAttestation` has `attestor_credential_id` that cannot be resolved by any `CredentialDirectoryRef`, the kernel checks: does the attestor + ≥ `quorum_size − 1` independent co-signers in the same domain's `PeerAttestationPool` co-sign the attestation? If yes, the attestation's `credential_unverified` flag is replaced by `peer_attested=True`, and downstream J4 acceptance treats it at PANEL_ACCEPT grade — better than unverified, never VERIFIER_ACCEPT grade. The peer pool is **substrate-pure**: it names no professions, no fields, no domains; the criteria themselves are emergent kinds the persona/operator catalog per-domain.

### 5.6.1 ReplicatedAttestation — pushing trust above the peer cap

PeerAttestationPool caps trust at 0.7 — appropriate for *single-attestor* frontier claims. When the same claim is *independently replicated* by multiple disjoint attestors, the substrate should reward the replication with a higher trust cap (still below credentialed 0.95). `ReplicatedAttestation` is the schema that records the replication evidence.

*The ReplicatedAttestation records independent replication evidence for a claim: base claim kind and reference, independence check type (disjoint affiliations, funding sources, geographic regions, or blind replication), constituent attestation references, agreement metric and threshold, and effective trust cap. The uplift schedule raises the trust cap from the peer pool's 0.7 based on constituent count and independence type, capping at 0.9 (still below credentialed 0.95). Three disjoint-affiliation replications reach 0.80; five reach 0.85; blind replications reach up to 0.90.*

**Technical detail:** See [A.33](#appendix-a33).

`disjoint_funding_sources` and `disjoint_geographic_regions` sit between the two columns; operator may calibrate per domain.

**Invariant:** the uplift never reaches credentialed-directory's 0.95. Credentialed and replicated evidence are *different trust kinds*; the substrate keeps them distinguishable in lineage. A `ReplicatedAttestation` that also rides on a credentialed `CredentialDirectoryRef` resolution achieves 0.95 not via the uplift but via the directory leg.

**Frontier trust cap composition rule.** The domain-level frontier trust cap (0.7 per `§4.4`) and the claim-level `ReplicatedAttestation` uplift (up to 0.85/0.90 per the table above) operate on **different scopes** and compose as follows:

| Scope | Cap applies to | Governs |
|---|---|---|
| **Domain cap** (frontier 0.7) | The domain's stage trust score | Promotion thresholds: EMERGENT → RECOGNISED (0.6 ✓) → AUTHORITATIVE (0.85 ✗ while frontier) |
| **Claim cap** (ReplicatedAttestation uplift) | Individual claim's `effective_trust_cap` | Downstream trust decisions: "should we trust this Tc measurement?" |

**Rule: claim-level `ReplicatedAttestation` uplift operates independently of the domain-level frontier cap.** A claim independently replicated by 3 labs with disjoint affiliations in a frontier domain reaches `effective_trust_cap = 0.80` — even though the domain's stage trust is capped at 0.7. The domain cap prevents *promotion* (the domain cannot reach AUTHORITATIVE); the claim cap enables *trust accumulation* on individual claims (the replicated measurement is trustworthy even in an unsettled field).

This composition preserves the incentive for independent replication in frontier domains. If the frontier cap clamped all trust to 0.7, `ReplicatedAttestation` would provide no benefit — independent replication (the gold standard of scientific validation) would be structurally useless for trust-building. The two-scope design avoids this.

**Tests:** A-RFC1 (claim-level uplift exceeds domain frontier cap), A-RFC2 (domain promotion still blocked by frontier cap despite high claim trust). See [`11_ACCEPTANCE_TESTS.md §9l`](11_ACCEPTANCE_TESTS.md).

### 5.6.2 LongitudinalReputation — track-record-weighted attestor influence

A peer attestor with a long track record of *correct* past attestations should weigh more than a freshly-admitted peer. `LongitudinalReputation` records the history; the PeerAttestationPool quorum logic *may* require above-threshold reputation for the constituents that count toward quorum.

*LongitudinalReputation tracks an attestor's historical correctness per domain: attestation references, counts of confirmed, contradicted, and pending outcomes, a Bayesian-updated track-record score (0-1, over a 5-year default window), and operator-tunable thresholds for pool admissibility. For high-stakes attestations, the PeerAttestationPool may require quorum constituents to meet a minimum track-record score.*

**Technical detail:** See [A.34](#appendix-a34).

**Goodhart mitigation:** `track_record_score` is computed by a classifier in a rotation pool (INV-6); no single classifier scores reputation for long. The kernel signs both the score AND the computing classifier identity so audit can recompute under a different classifier and detect divergence.

**Honest limit:** "later confirmed" requires an *independent* later check. In domains where no such check ever materialises (purely subjective judgements, untestable claims), the track record cannot grow above its prior. Reputation is a *measurement of replicable correctness*, not of social standing.

### 5.7 AttestationEquivalencePolicy — sensor-bridge evidence substituting for human attestation

**What this is, in plain language.** Imagine a construction project where a building inspector visits the site every week to check the work. That inspector's sign-off is a human attestation — a professional saying "I checked this and it meets the standard." Now imagine the persona designs a camera and sensor system that continuously monitors the same things the inspector checks: structural alignment, material placement, environmental conditions. The question is: can we trust the sensors enough to skip some of those inspector visits?

The **AttestationEquivalencePolicy** is the rule that answers that question. It says: "For this specific type of check, using these specific calibrated sensors, the automated measurement can stand in for the human inspector — but at a trust discount." By default, sensor evidence carries 85% of the trust of a human sign-off, because sensors can be fooled in ways humans aren't (and vice versa). The human inspector's judgment still wins if the two disagree.

Crucially, only the operator (the person or organization running the deployment) can approve this policy — the persona can suggest it, but a human must sign off on trusting sensors over professionals. For safety-critical work (where mistakes could injure people), an extra layer of approval is required. And the system tracks how often the sensors agree with humans over time, so trust can be gradually increased — or the policy revoked if sensors prove unreliable.

**The key safeguards:**
- Sensors never reach 100% of human trust through this mechanism — there is always a discount.
- If the sensors and a human inspector disagree, the human wins by default.
- If a sensor's calibration expires or drifts, substitution stops automatically until recalibration.
- The operator must re-approve the policy every 6 months; otherwise it suspends and human attestation resumes.
- For safety-critical fields (construction, medical devices, anything where people could get hurt), an extra safety review is required before sensors can substitute for humans at all.

When a persona authors a Tier 3 `BridgeDesignArtifact` (`§5.5.4`) that produces calibrated measurement evidence via `BridgeCalibrationBinding` (`§5.5.5`), a natural question arises: can this sensor evidence substitute for human professional attestation (`ExternalAttestation`, `04_PROJECT §26a.3`) for a specific verification kind? Construction inspection, instrument calibration verification, environmental monitoring compliance, medical device validation — all share this "can the sensor replace the human?" decision topology.

`AttestationEquivalencePolicy` is the per-domain mechanism that lets operators declare when and how sensor-bridge evidence may substitute for human attestation at a declared trust discount.

*The AttestationEquivalencePolicy declares: which verification kind it covers, which human attestation kind it substitutes, what sensor evidence is required (specific calibrated bridges, measurement kinds, statistical minimums, uncertainty bounds), what calibration quality the bridge must maintain, and what trust discount applies. The policy is operator-approved (always); operator co-signed via C2 when the domain is safety-critical. Sensor evidence never exceeds human attestation trust — a configurable discount (default 0.85×) reflects the "sensors can be fooled" reality. Human attestation wins disputes by default.*

**Technical detail:** See [A.71](#appendix-a71).

**Constraints (technical).**

- **Operator approval is mandatory.** A persona or domain curator MAY propose an `AttestationEquivalencePolicy`; only an operator can approve it. This is structurally parallel to `ProposedSafetyExtension` (`§5.3`) — the persona identifies the opportunity; the operator bears the governance responsibility.
- **Safety-critical requires C2 co-sign.** When the domain has `safety_critical = True` AND `physical_harm_class >= bodily_injury`, the policy requires explicit operator co-signature per C2. The substrate refuses to auto-approve sensor substitution for safety-critical human attestation.
- **Trust discount is mandatory.** `trust_discount` (0.0–1.0, default 0.85) multiplies the human attestation's trust score. A sensor-verified inspection at 0.85× carries 85% of the trust of a human-certified inspection. The discount MUST be < 1.0 — sensor evidence never reaches parity with human professional judgment through this mechanism alone. Parity requires the human attestation kind to be deprecated by operator policy (outside the substrate's scope).
- **Calibration freshness is load-bearing.** The policy declares `max_calibration_age` for the bridge. If `BridgeCalibrationBinding.expires_at` is past OR `calibration_age > max_calibration_age`, the policy is suspended for that bridge until re-calibration. The kernel checks this at every `sensor_substitution_applied` event — stale calibration means no substitution.
- **Human wins disputes by default.** When both sensor evidence and human attestation exist for the same verification event and disagree, `superseded_by_human_on_dispute = True` (default) means the human judgment governs the `PhysicalAsset` state advancement. The sensor evidence persists in lineage as a dissenting record. Operators MAY set `superseded_by_human_on_dispute = False` for domains where instrumentation is demonstrably more reliable than human judgment (e.g., precision dimensional measurement vs. visual inspection) — this requires C2 co-sign regardless of domain safety classification.
- **Progressive trust building.** Over time, as a sensor bridge accumulates a track record of agreement with human attestation (measured via `agreement_history` in the policy), operators MAY increase `equivalence_trust_score` and decrease `trust_discount`. The `BridgeReductionPlan` (`04_PROJECT §26a.10`) tracks this progression per entry.
- **Review cadence is operator-set.** `review_cadence` (default 180 days) is the interval at which the operator must re-affirm the policy. Un-reviewed policies transition to `status = suspended`; substitution stops; human attestation resumes. The substrate enforces continuous affirmation.
- **Composes with BridgeReductionPlan.** When a `BridgeReductionEntry` (`04_PROJECT §26a.10`) proposes replacing human attestation with sensor evidence, it MUST reference an `AttestationEquivalencePolicy`. The entry cannot advance past `design_ready` without an approved policy. This ensures the automation plan and the trust policy are aligned.

**Tests:** A-AEP1 (policy proposal + operator approval), A-AEP2 (C2 co-sign for safety-critical), A-AEP3 (trust discount applied to sensor substitution), A-AEP4 (calibration staleness suspends policy), A-AEP5 (human-wins-dispute default), A-AEP6 (sensor-wins-dispute requires C2 co-sign), A-AEP7 (review cadence enforcement + suspension), A-AEP8 (composition with BridgeReductionPlan entry), A-AEP9 (agreement_history accumulation over time). See [`11_ACCEPTANCE_TESTS.md §9l`](11_ACCEPTANCE_TESTS.md).

**DomainLineage:** `attestation_equivalence_policy_proposed`, `attestation_equivalence_policy_approved`, `attestation_equivalence_policy_suspended`, `attestation_equivalence_policy_revoked`, `sensor_substitution_applied`, `sensor_substitution_disputed`, `sensor_substitution_human_overrode`.

## 6. Ingestion — seven-stage pipeline

*The seven stages: (1) sourcing from search tools and content stores, (2) parsing and chunking (format-specific, 500-1500 tokens with overlap, figures and tables extracted), (3) embedding and indexing (domain-appropriate models, per-type indexes, graph extraction), (4) provenance and licensing (signed KnowledgeRef with source, hash, licence, access rights), (5) tagging (seven-scope tags plus quality and domain), (6) safety check (OWASP LLM01 filter, content moderation, rights check), (7) registration (signed into corpus, searchable).*

**Technical detail:** See [A.35](#appendix-a35).

### 6.1 KnowledgeIngestionRecord schema

*The KnowledgeIngestionRecord tracks each ingested source: source kind (KindRegistry-resolved, e.g. "paper", "datasheet", "permit_pdf"), source reference and publisher, licence and paywall status, content hash, parsing statistics (chunks, entities, figures, tables), embedding model and index targets, domain, quality tag (KindRegistry-resolved, e.g. "peer_reviewed", "preprint", "engineer_stamped"), and publisher attestation.*

**Technical detail:** See [A.36](#appendix-a36).

### 6.2 KnowledgeRef lifecycle FSM

After ingestion, every `KnowledgeRef` traverses a 7-stage FSM. Each transition is signed; retrieval ranking is stage-aware (v1.0 §14).

*The seven stages: INGESTED (new, provenance 0.5), CITED (first successful citation, auto), REUSED (K=3 distinct projects, auto), CANONICAL (operator/curator blessed, weighted 1.0 in retrieval), SUPERSEDED (newer ref preferred, demoted but not deleted), DEPRECATED (not retrieved by default, audit-mode only), REVOKED (tombstoned on licence/legal issues, kept for audit). All transitions emit signed KnowledgeRefTransition events into DomainLineage.*

**Technical detail:** See [A.37](#appendix-a37).

### 6.3 Cross-persona knowledge sharing — 5 visibility tiers

Every `KnowledgeRef` carries a `visibility` field (added to schema in `knowledge-ingestion/1`).

*Five tiers: persona_only (Tier 1, no sharing), project_only (Tier 2), tenant (Tier 3, default -- same org/kernel, with cross-tenancy agreement required for multi-principal environments), federation (Tier 4, multi-kernel via A2A), and public (Tier 5, operator-gated). Licence revocation collapses visibility to Tier 1 plus REVOKED stage.*

**Technical detail:** See [A.38](#appendix-a38).

**Reuse note.** These five tiers are the single source of truth for outward visibility across the substrate. `ArtifactSharingPolicy.outward_tier` ([`07_ARTIFACTS.md §4a`](07_ARTIFACTS.md#4a-artifactsharingpolicy-artifact-share1--env-ownership-and-sharing)) and `DomainHarvest.visibility_tier` (§13a) reuse this same enumeration (the 4-value `DomainHarvest` list maps onto it per ADR-0030); no new visibility vocabulary is introduced for artifacts.

### 6.4 Federated knowledge lookup

To avoid re-ingestion across kernels working in the same domain.

*The flow: local lookup by content hash misses, federated A2A lookup finds a peer that has ingested the source, peer returns signed metadata, local kernel verifies and adds a pointer (not a copy), trust merges as the minimum of local and peer trust.*

**Technical detail:** See [A.39](#appendix-a39).

Latency budget: ≤ 1 s + A2A network latency p95. Operators may pre-approve trusted peers; un-approved peers respond but their refs are quarantined until operator review.

**Unified discoverability + access.** Domains, knowledge refs, skills, and tools are "any content" and project a lightweight `DiscoverableRecord` ([`09_PROTOCOLS.md §3G.1`](09_PROTOCOLS.md#3g1-discoverablerecord--one-projection-for-every-content-type)) so they are findable over both the internet (`.well-known` + gossip + DHT) and intranet (mDNS) discovery planes ([`§3G.2`](09_PROTOCOLS.md#3g2-two-plane-discovery-transport--internet--intranet)) — not just via point-to-point A2A lookup. Federated lookup, and the discovery planes, are **access-gated** by the same `AccessPolicy` model ([`§3G.3`](09_PROTOCOLS.md#3g3-accesspolicy--one-access-level-model-across-all-content-types), [`§3G.4`](09_PROTOCOLS.md#3g4-access-gated-discovery--who-can-access-what-enforced-at-the-discovery-layer)) whose outward axis is the **5 visibility tiers** defined in §6.3; a `discover`-tier peer learns a knowledge ref exists without reading it, and where a ref is provider-hosted its body is addressed by a `ContentLocator` ([`§3G.5`](09_PROTOCOLS.md#3g5-hybrid-provider-backed-storage--distribute-the-reference-not-the-bytes)) rather than copied.

### 6.5 Ingestion toolkit

Tools the ingestion pipeline calls; personas discover them via §5 dynamic discovery and use them per charter + operator policy.

*Four categories of ingestion tools: web/search (arxiv, scholar, patent, wiki, wikidata), ingestion (PDF, HTML, markdown, LaTeX, video transcript, figures, tables), graph extraction (entities, relationships, graph nodes), and validation (licence, paywall, publisher attestation).*

**Technical detail:** See [A.40](#appendix-a40).

Operator may install a subset; persona discovers the rest via MCP-Zero (§5).

## 7. Inference — verifier recipes, safety extensions, conventions, standards

### 7.1 InferredVerifierRecipe

From successful patterns.

*The InferredVerifierRecipe records a candidate recipe inferred from traces: name, domain, source traces, confidence, proposed verification stages and success criteria, holdout test results, lifecycle stage, and co-signing personas. The inference engine runs nightly or on-demand, finding common tools and outcomes across successful traces for each artifact kind, proposing recipes when pattern consistency exceeds 0.8, and validating against holdout traces.*

**Technical detail:** See [A.41](#appendix-a41).

### 7.2 ProposedSafetyExtension

*The ProposedSafetyExtension records a domain-specific safety rule: extension name, claim pattern to match, required tool and outcome, timing (before/after/both), failure action (refuse, warn, or escalate), rationale, evidence and trace references, safety-critical flag, lifecycle stage, co-signing personas, and operator approval status.*

**Technical detail:** See [A.42](#appendix-a42).

Safety-critical proposals require operator sign-off before any use.

#### 7.2.1 Physical-hazard kind seeds — MetaRegistry data

Prior versions ship only `iec_62368_isolation` as a seed safety extension example (associated with `power_electronics` in worked examples). For new physical-world projects (cryo labs, RF testing, biotech, fab work, vehicle work, hazmat), the first project pays a heavy cataloging cost authoring safety extensions from scratch. v1.0 closes this with **operator-curated MetaRegistry hazard kind seeds shipped as data, not substrate enums**. The hazard kinds themselves remain emergent — the substrate has no closed list of hazards — but the release bundles a starter catalog the operator can promote into MetaRegistry on day one.

*The v1.0.5 MetaRegistry seed bundle includes physical hazard kinds: cryogenic exposure, RF exposure, high voltage arc, ionizing radiation, laser eye safety (class 3b/4), vacuum implosion risk, hazmat chemical exposure, biocontainment breach, heavy machinery pinch/crush, and confined space asphyxiation. Each is classified on the two hazard axes; some include safety extension templates. All are data, not substrate code, and the operator may promote, demote, or revoke any of them.*

**Technical detail:** See [A.43](#appendix-a43).

**Resolution rule.** When a probe's `physical_harm_class` is inferred ≥ `bodily_injury`, the DomainCurator (§10) is offered the matching MetaRegistry seeds during composition. The curator MAY import any subset as the domain's `safety_extensions`; each import is a signed `safety_extension_imported` event in DomainLineage. Imported extensions inherit `STANDARDISED` stage but operator MAY demote per-domain.

**Substrate purity preserved.** No hazard category names appear in substrate code, schemas, or invariants. The seed bundle is *data* shipped alongside the release; the operator may swap it out, extend it, or refuse it entirely. The hazard_axes themselves (`physical_harm_class`, `information_hazard_class`) ARE substrate per `§2` — they describe hazard *shape*, not specific hazards.

**Why ship the seeds.** Without seeds, the first project in a new physical domain bears the entire cataloging cost. With seeds, new domains can adopt a starter catalog and add domain-specific hazards on top. The seeds are illustrative, not exhaustive; they should be expanded based on operator deployment experience.

### 7.3 ProposedConvention

*The ProposedConvention records a domain notation or naming convention: symbol, meaning, optional formal definition, scope (domain default or project specific), proposer, co-signing personas, usage count, and promotion stage. Conventions emerge through co-signed use: 3+ personas using the same symbol with the same meaning produce a candidate; K successful projects advance to RECOGNISED; then adopted as domain default.*

**Technical detail:** See [A.44](#appendix-a44).

#### CONVENTION_AMBIGUITY (Signal E in §4.1) and CONVENTION_RECONCILIATION_PROPOSAL

*When two personas in the same project use different symbols for the same concept (cosine similarity of meanings at or above 0.85), the kernel emits CONVENTION_AMBIGUITY. The resolution flow extends the active probe or spawns a new one, the DomainCurator reviews candidates, the kernel emits a reconciliation proposal with canonical symbol and alias mapping, originating personas co-sign or contest, and on co-sign the convention is adopted with aliases preserved for legacy outputs. NOTATION_CONFLICT handles hard disagreements; NOTATION_SCOPE_CONFLICT handles cross-domain collisions.*

**Technical detail:** See [A.45](#appendix-a45).

### 7.4 StandardRef cataloging

Persona may identify external standards as authoritative.

*The StandardRef records a standard's identity (e.g. IEEE_1641-2010), title, publisher, version, licence status, access method, relevance, cataloger, and operator verification status.*

**Technical detail:** See [A.46](#appendix-a46).

Paywalled or restricted standards may be cataloged-but-not-ingested. Persona may declare "I cannot verify compliance without access" for honest disclosure.

### 7.5 Emergent kind proposals (v1.0 — substrate domain-agnostic)

Per the C4 commitment (`00_VISION`), v1.0 does NOT ship closed Literal[...] enums for any domain-shaped category. Every kind that varies across domains — what counts as a media kind, a knowledge-source kind, a verifier kind, a bridged-capability kind, a contribution kind, a fact kind, a bundle kind — is an **emergent unit** proposed by personas through the same machinery as `ProposedSafetyExtension`, `ProposedConvention`, and `InferredVerifierRecipe`.

The nine Proposed*Kind schemas below extend the §7.1-§7.3 family. A residential-construction probe (no built-in `floor_plan` media kind, no built-in `geotechnical_report` source kind, no built-in `permit_filing` capability kind, no built-in `physical_inspection` verifier kind) bootstraps every kind it needs through these schemas, signs them into the per-domain KindRegistry (§7.6), and persists them for every future home-construction project.

*Nine Proposed*Kind schemas share a common structure (proposal id, proposer, domain, kind name, description, rationale, evidence, stage, co-signers). ProposedMediaKind adds MIME types, storage class, edit semantics, adapter references, and verifier hooks. ProposedSourceKind adds parsing adapter, default visibility, quality tag, and retention hint. ProposedVerifierKind adds cascade position, attestor class, evidence kinds, failure action, and safety-critical flag. ProposedCapabilityKind adds bridge pattern, expected recurrence, and validation period. ProposedContributionKind adds credit weight. ProposedItemKind adds payload schema, status FSM, and advance signal hooks. ProposedOutcomeKind adds payload schema, arrival modes, and attestation/corroboration requirements. ProposedQualityKind adds rank and attestation requirements. ProposedFactKind adds scope and cross-env transferability. ProposedBundleKind adds expected artifact, outcome, and attestation kinds.*

**Technical detail:** See [A.47](#appendix-a47).

Proposed*Kind schemas share the same lifecycle as ProposedSafetyExtension / ProposedConvention / InferredVerifierRecipe: candidate (with co-sign and cross-source validation) advances to trial, then to accepted (after K uses with no contradictions), and optionally promoted through the four promotion stages to MetaRegistry. Rate-limits (§9.1), convergence detection (§9.1), and DomainCurator review (§10) apply to Proposed*Kind exactly as to existing proposal types. All proposals are signed into DomainLineage; replay reconstructs the registry deterministically.

### 7.6 KindRegistry and the cross-domain MetaRegistry

Accepted Proposed*Kind entries land in a **KindRegistry**. The kernel consults the registry at every site that previously held a closed Literal[...]: artifact construction (`07_ARTIFACTS §3`), ingestion (`§6.1`), bridge minting (`§5.5`), verifier cascade composition (`01_KERNEL §13`), contribution crediting (`04_PROJECT §5`), env-proven-fact emission (`05_ENVIRONMENT §12`).

*The KindRegistry holds accepted kinds organised by family (media, source, verifier, capability, contribution, fact, bundle, item, outcome, quality tag, env rule, task class, acceptance pathway). Each entry (e.g. MediaKindEntry) carries the proposal payload plus stage, trust score, promotion history, and usage tracking. Resolution first checks the per-domain registry, then falls back to the MetaRegistry; an unknown kind triggers Signal G and a probe extension. Promotion to MetaRegistry requires STANDARDISED stage, cross_domain_promotable flag, and citation in K=5 projects across M=2 distinct domains. Drift detection may demote MetaRegistry entries back to per-domain RECOGNISED.*

**Orchestration kind families (ADR-0066).** The `task_class_kinds` and `acceptance_pathway_kinds` families hold the emergent orchestration kinds defined in [`03_TASKS.md §2a`](03_TASKS.md#2a-orchestration-is-emergent--classes-pathways-and-the-run-loop-are-coordination-shapes): the v1.0 ten task classes and eight acceptance pathways ship as STANDARDISED **seed** entries (the [`09_PROTOCOLS.md §7.2`](09_PROTOCOLS.md#72-acceptance--task) registry rows resolve against exactly these families). An `acceptance_pathway_kinds` entry additionally carries `pathway_trust` and promotes/demotes on the acceptance-soundness ladder of [`03_TASKS.md §2b`](03_TASKS.md#2b-orchestration-kind-promotion--trust-decay-curve-evidence-threshold-and-the-bounded-compositional-policy-profile) (asymmetric-EWMA trust, independent-reference agreement ≥ 0.90 for EMERGENT → RECOGNISED, C2 blocking for safety-critical) — the orchestration analogue of the domain promotion ladder. Operators MAY constrain proposals into these families via the `OrchestrationPolicyProfile` (`bounded_compositional` vs the `fully_open` default, [`03_TASKS.md §2b.4`](03_TASKS.md)).

**Technical detail:** See [A.48](#appendix-a48).

**What this fixes vs prior → v1.0 regression:**

Prior versions already specified that domain contexts and "whatever needed for all gaps" must be emergent. v1.0 initially imported Artifact / KnowledgeIngestionRecord / BridgeAsset / InternalCredit / EnvironmentProvenFact schemas verbatim, preserving their closed Literal[...] enums and silently regressing on the emergence principle. §7.5 + §7.6 close that regression: every `kind:` field referenced anywhere in v1.0 resolves through this registry, and substrate code never carries a domain-shaped list.

### 7.6.1 KindRegistry entry metadata

Several schemas (`ProjectPhaseState`, `PaymentBridge`, `InstrumentAsset`, `MeasurementFact`) reference KindRegistry-resolved kinds *and* expect those kind entries to carry per-kind metadata that drives substrate behaviour (e.g., does a phase suppress stall evaluation; does a payment method require co-signing). The KindRegistry entry schema therefore carries an optional `metadata: dict` blob whose contents are per-kind-family conventions, signed at registration and validated against the kind family's declared metadata schema.

*The KindRegistryEntry is the unified entry schema: entry id, domain (null for MetaRegistry), kind family (open -- operator may register new families), kind id within the family, stage, MetaRegistry promotion flag, per-family metadata (validated against the family's declared schema), co-signing personas, and signature.*

**Technical detail:** See [A.49](#appendix-a49).

### 7.6.2 Per-family metadata schemas

Substrate registers a metadata schema per kind family. When a `KindRegistryEntry` is drafted, the kernel validates `metadata` against the family's schema. Substrate ships seed schemas for kind families; operators may register additional families.

*Per-family metadata schemas define fields per kind family: phase_kinds (stall suppression, user sign requirement, expected duration, severity curve), payment_method_kinds (human authorisation, receipt latency, audit trail kind), instrument_kinds (operational state FSM, calibration interval, systematic floor, reference chain root), and quantity_kinds (units, physical dimension, distribution kind, conventional uncertainty). Seed phase_kinds entries include design, verification, external dependency wait, physical fabrication, peer review pending, regulatory review, iteration, and synthesis.*

**Technical detail:** See [A.50](#appendix-a50).

**Substrate purity preserved.** The kind families themselves are substrate-shape labels (positions in the registry namespace), not domain categories. The metadata field schemas are per-family declarations the operator may extend. The seed phase_kinds bundle ships as DATA (per §7.2.1's pattern), not as substrate enum.

**Composition with ProjectPhaseState (`04_PROJECT §26a.6`):** when a project enters a new phase, the kernel resolves the phase_kind in KindRegistry and copies `stall_evaluator_suppressed` + `requires_user_sign` into the ProjectPhaseState instance at transition time. Subsequent stall-evaluator queries read directly from the ProjectPhaseState instance (so the value is signed-at-transition rather than re-resolved each evaluation). Operator changes to the KindRegistry entry's metadata after transition do not retroactively change the phase's behaviour — that requires an explicit signed `PHASE_METADATA_UPDATE` event in ProjectLineage.

### 7.6.3 The `env_rule_kinds` family — env-scoped executable rules

An [`EnvironmentRule`](12_GLOSSARY.md#e) ([`05_ENVIRONMENT.md §2.2b`](05_ENVIRONMENT.md#22b-environmentrule-env-rule1), `env-rule/1`) carries a `rule_kind` that resolves against a dedicated KindRegistry family, `env_rule_kinds`, exactly as `media_kind` resolves against `media_kinds` (§7.6). Per commitment C4 the substrate hardcodes no closed list of rule kinds. The MetaRegistry seeds three **shape-only** entries as DATA — they describe how a rule is *expressed*, never what any domain's rule *says*:

- `code` — the rule is a sandboxed, persona- or operator-authored `ToolArtifact` (the `PROPOSED → SANDBOXED → VERIFIED → PROMOTED` FSM of §7.2.x with OWASP filter + resource caps per [`01_KERNEL.md §6`](01_KERNEL.md#6-sandbox-execution)) wrapped in a `VerifierStage` ([`01_KERNEL.md §13.1`](01_KERNEL.md#131-verifier-cascade--4-tiers--rotation)).
- `rule_engine` — the rule is a declarative decision artifact: an authored or [`InferredVerifierRecipe`](12_GLOSSARY.md#i) (§7.1) cascade; portable declarative encodings (e.g. a decision table) are admissible and carry no executable surface.
- `contract` — the rule is a machine-readable contract `ArtifactBundle` whose conformance is checked by a `verifier_recipe_id`.

These three are positions in the registry namespace, not domain categories; an operator MAY register further `env_rule_kinds` entries, and any domain-specific rule *content* emerges and is signed exactly like every other Proposed\*Kind (§7.5). The rule's enforcement point, lifecycle, cascade, and operator gating are specified in [`05_ENVIRONMENT.md §2.2b`](05_ENVIRONMENT.md#22b-environmentrule-env-rule1); enforcement composes under safety-floor source 8 (`env_charter`) per [`01_KERNEL.md §2`](01_KERNEL.md#2-the-safety-floor--8-sources--1-advisory).

### 7.6.4 Coordination & attestation kind families (ADR-0070)

Completing the C4 substrate-purity trajectory (ADR-0045 coordination meta-mechanisms, ADR-0066 orchestration), the last closed `Literal[...]` enums on coordination/attestation fields become KindRegistry families resolved exactly as `media_kinds` does (§7.6), each shipping its prior values as STANDARDISED **seed** entries (DATA, not substrate enum):

- **`conflict_policy_kinds`** — the merge-conflict policy on batch/sync shapes ([`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md), [`04_PROJECT.md`](04_PROJECT.md)). Seeds: `skip_changed`, `fail_on_conflict`, `force`.
- **`competency_level_kinds`** — the attested skill-competency ladder ([`02_PERSONA.md §11.9`](02_PERSONA.md)). Seeds, **ordered**: `novice` < `proficient` < `competent_supervised` < `independent`; a proposed level MUST declare its rank in the family's per-family metadata (§7.6.2) so trust-calibration and gating remain monotone.

These are positions in the registry namespace, not domain categories; an operator/domain MAY register further entries via the §7.5 Proposed\*Kind path. Substrate code branches on no closed list of either. (The `summary_function_kinds` field of `DerivedMetric` was already open, §7.6; no change.)

## 8. Cross-source validation

Before promotion, the kernel runs five checks: (1) cross-trace consistency (does inferred recipe match held-out outcomes?), (2) cross-persona agreement (multiple personas arriving at similar inferences?), (3) cross-domain consistency (does proposal contradict existing convention in a related domain?), (4) charter consistency (does extension violate any persona's charter?), (5) operator policy consistency (does proposal violate deployment policy?).

**Technical detail:** See [A.51](#appendix-a51).

Any failure leads to proposal blocked or marked for review.

## 9. ProposalQueue and curation

*The ProposalQueue tracks pending, accepted, rejected, and operator-review-required proposals per domain, with a configurable review frequency (default weekly).*

**Technical detail:** See [A.52](#appendix-a52).

Kernel reviews:
- **Auto-accept** non-safety-critical proposals with high cross-source validation + sufficient co-signing.
- **Defer to operator** safety-critical proposals.
- **Reject** proposals failing cross-source validation.
- **Hold** proposals with insufficient evidence.

### 9.1 Rate-limits and PROPOSAL_CONVERGENCE_DETECTED

*Rate limits: K=10 proposals per persona per session baseline (cold-start scaling per §9.1.1), operator-tunable per-month cap, exceeding emits PROPOSAL_RATE_LIMITED. Convergence detection: when 2+ personas independently propose similar entries (cosine similarity at or above 0.85), the kernel emits PROPOSAL_CONVERGENCE_DETECTED with a merge candidate. Merge offer flow: personas co-sign or contest; 2+ co-signs merge and supersede originals; merged proposals carry combined evidence.*

**Technical detail:** See [A.53](#appendix-a53).

### 9.1.1 Cold-start proposal scaling and BulkKindProposal

When a persona enters a freshly-recognised `DomainContext` whose `KindRegistry` is empty, the baseline K=10 per-session proposal cap can throttle bootstrap so hard that emergence stalls. The fix is **substrate-shape**: scale the cap with the volume of evidence the persona has ingested in the same session, then provide a `BulkKindProposal` primitive that bundles many kind-proposals sharing one ingestion source under a single signed envelope.

*ColdStartProposalCalibration scales the per-session cap when the KindRegistry is empty: effective cap = baseline + scaling_fn(ingested + alpha * standards) * decay, capped at max_uplift (200), with a safety-critical multiplier that tightens (not loosens) the cap. BulkKindProposal bundles multiple kind proposals sharing one ingestion source under a single signed envelope, counting as 1 session proposal while members count individually against monthly caps and convergence detection. The admission flow resolves the calibration, computes effective cap, and admits or rate-limits accordingly.*

**Technical detail:** See [A.54](#appendix-a54).

**Why this is substrate-shape.** All inputs to `scaling_fn` are counts maintained by the kernel as the persona works (`N_ingested`, `N_standards`, `N_sessions_in`). The substrate never inspects the *content* of an ingestion record to decide the cap — the same calibration applies to any domain that happens to have a large evidence corpus. `BulkKindProposal.primary_evidence_ref` points to a source by id and binds by hash; the substrate does not parse what the source contains.

**Convergence-detection interaction.** Member proposals of a `BulkKindProposal` participate in `PROPOSAL_CONVERGENCE_DETECTED` independently — a bundle does not shield its members from merging with proposals from sibling personas. This preserves anti-Goodhart breadth.

## 10. DomainCurator role

*The DomainCuratorRole assigns a persona as curator for a domain, with permissions to propose consolidations, review promotions, propose demotions, and reconcile conflicts -- but cannot unilaterally promote to authoritative or self-sign consolidations.*

**Technical detail:** See [A.55](#appendix-a55).

DomainCurator handles:
- **Consolidation** — merge similar proposals into canonical entries
- **Conflict resolution** — notation/recipe conflicts
- **Quality review** — periodic audit
- **Promotion proposal** — recommend kernel/operator

v1.0 ships with kernel-as-curator as default; explicit DomainCurator personas added as domains grow.

## 11. Cross-domain transfer

Cross-domain transfer is first-class.

*The CrossDomainTransfer records the transfer of any KindRegistry-registered artifact between domains: artifact type and reference, source and target domains, trust scores (initially reduced in target), transferring persona, and usage counts.*

**Technical detail:** See [A.56](#appendix-a56).

After K successful target uses, trust normalises; promotion as if originally proposed in target domain.

### 11.1 Anti-leakage (5 risks)

*Five leakage risks and mitigations. Risk A: user-specific data blocked by user_id scope tag. Risk B: org-specific data blocked by org_id scope tag. Risk C: project secrets blocked by project_id scope tag. Risk D: proprietary IP blocked by operator policy, IP_sensitive flag, and operator review. Risk E: cross-org implicit info blocked by org_share_policy per artifact and operator gate; composes with DerivationProvenanceEdge for implicit derivation.*

**Technical detail:** See [A.57](#appendix-a57).

Kernel enforces at transfer time; refuses with `CROSS_DOMAIN_LEAKAGE_BLOCKED` if any check fails.

### 11.2 DomainPrecedentImport — kinship priors for cold-start

`CrossDomainTransfer` (§11) carries **specific named artifacts** between domains. It does not address the dual case: a freshly-recognised target domain wants to begin its emergence with the **trust priors** of a kin source domain — recipes, conventions, contribution kinds — without waiting K successful target-uses to normalise each one. The gap is felt under principal collapse where slow trust-climb stalls every artefact at PANEL-grade.

`DomainPrecedentImport` is a bulk, scoped, attested operation that imports a **profile of kinds** from a precedent domain, applying a substrate-shape trust discount and binding the import to a non-principal kinship attestation.

*DomainPrecedentImport bulk-imports kinds from a precedent domain with a trust discount based on three kinship axes: evidence overlap count (kernel-computed), structural kinship score (kernel-computed), and declared parent reference. A non-principal kinship attestation is required for safety-critical domains or under principal collapse. Imported entries start at EMERGENT stage regardless of source stage (no trust laundering), with a probationary period of K=2 successful target uses before native promotion. Anti-leakage filters apply. The admission rule rejects drafts with discount factor below 0.3 (kinship too thin) and requires kinship attestation when mandated. Three cumulative failures revoke an individual imported entry.*

**Technical detail:** See [A.58](#appendix-a58).

**Why this is substrate-shape, no domain leak.** `imported_kind_classes` enumerates substrate categories (media_kind, verifier_kind, ...) — names already established by §7.5 as the substrate's own ontology of emergent-kind classes. The three kinship axes are kernel-computed shape measurements (overlap count, distribution cosine, declared parent topology). The `kinship_attestation_ref` requirement is principal-topological, not domain-named. The discount formula is arithmetic on substrate-tracked numbers. No substrate text needs to know which two domains are related.

**Composition with C2.** When `target_domain.safety_critical = True`, the kinship attestation requirement above is in addition to (not instead of) the operator gate for the eventual RECOGNISED → AUTHORITATIVE promotion. The import accelerates the persona's day-1 trust prior; it does not bypass operator sign-off when an imported entry's first target use would otherwise demand one.

**Composition with principal collapse.** Under `operator_is_user`, the kinship attestation is the substitute for the operator co-sign that would normally accompany cross-domain authority claims. The kinship attestor must be a non-principal credential-disjoint ExternalAgent (mirrors §26a.3 independent_co_signed_by). `operator_co_signed_by` is refused for this purpose because under collapse it would let the principal self-attest kinship.

## 12. Demotion and revocation

*Five triggers for demotion: conformance audit conflict, trust drift, external revocation, charter drift, and operator decision. Demotion flows downward through stages (AUTHORITATIVE to RECOGNISED to EMERGENT to DEPRECATED). STANDARDISED entries require operator-signed revocation with a corrective action plan. Tombstoned entries are removed from active retrieval but kept in archive for audit (cannot be physically deleted). The DemotionEvent records the artifact, stage transition, reason, trigger type, corrective action, and signatures.*

**Technical detail:** See [A.59](#appendix-a59).

### 12.1 Dormant domain lifecycle

When an emergent domain sees no activity for an extended window, the kernel applies a dormancy FSM.

*After N=6 months of no activity (operator-tunable), the domain enters DORMANT: retrieval still works at reduced weight, entries stop auto-promoting, cross-source validation pauses. New activity triggers a reanimation decision: task fingerprint similarity at or above 0.7 means continuation (existing context extends); below 0.7 means new probe. At N+M=18 months with no activity, the kernel proposes deprecation; operator may accept (DEPRECATED) or reject (continue DORMANT). Deprecated entries are archived with lineage preserved.*

**Technical detail:** See [A.60](#appendix-a60).

## 13. Promotion ceremony

When entry promotes to AUTHORITATIVE or STANDARDISED, the ceremony runs eight steps: final cross-source validation, charter conformance check, external validation evidence verified, operator signature collected (safety-critical or standardised), co-signing personas notified, audit log updated with full provenance chain, stage transitioned with signed event, and DomainContext refreshed with cards updated.

**Technical detail:** See [A.61](#appendix-a61).

Ceremony is **atomic** — all checks pass or rolled back.

## 13a. DomainHarvest — packaging a domain for downstream consumers

A domain whose KindRegistry, verifier recipes, conventions, and standard refs accumulated through one or more projects becomes valuable to **future probes for kin domains** only if it can be **packaged, signed, and exposed at a visibility tier consumable by those probes**. Without a harvest mechanism, a single-project domain (or a sparsely-cited domain that nonetheless converged) stays locked inside its originating project's scope.

`DomainHarvest` is the substrate-shape ceremony that wraps a domain snapshot for publication. It is domain-agnostic: the harvest carries whichever kinds, recipes, conventions the domain produced, with provenance and trust caps preserved.

*The DomainHarvest packages a domain snapshot for downstream consumption. It records the trigger (project completion, single-project promotion, operator pull, stage promotion, or scheduled periodic), a replay-reproducible snapshot at a lineage height, an inventory of entries by kind class, trust cap, contributing personas and projects, anti-leakage filter results, visibility tier (private, tenant, federation, or public), operator/principal-collapse gating, and federation index reference. The harvest flow: snapshot, filter, compute trust cap, gate, publish. Consumers pin to the harvest_id; trust capped by harvest's trust cap. Revocation flags downstream imports for re-attestation.*

**Technical detail:** See [A.62](#appendix-a62).

**Why this is substrate-shape, no domain leak.** The harvest's inventory uses the substrate's own emergent-kind class names (media_kind, verifier_kind, ...). The trigger kinds describe lifecycle positions (project completion, ceremony coincidence), not domain names. The visibility tiers and operator-gate behaviour are kernel-wide. The harvest carries no payload that the substrate inspects — it carries refs by id and hashes by content; the substrate does not parse what the refs teach.

**Composition with single-project promotion (§3.2).** When §3.2 fires for a one-shot domain, a DomainHarvest is auto-drafted with `triggered_by_kind = "single_project_promotion"` and `trust_cap` set from the config. The harvest is the artefact that lets a future principal benefit from this principal's bootstrap, gated by their own consent at publication time.

**Composition with project completion (`04_PROJECT §4.1`).** Project completion ceremony emits `project_completed` (signed). When the project's primary domain has `single_project_mode.enabled = True` AND completion ceremony fires, the kernel proposes a `DomainHarvest` draft to the originating persona; the persona may decline (and the harvest is never drafted), accept at `visibility_tier = "private"` (default), or escalate to higher tiers with the appropriate consents.

## 14. Stage-aware retrieval

v1.0 §08 retrieval includes stage weighting.

*Retrieval scores are multiplied by stage weights: EMERGENT 0.5, RECOGNISED 0.7, AUTHORITATIVE 0.9, STANDARDISED 1.0, DEPRECATED 0.2, TOMBSTONED 0.0.*

**Technical detail:** See [A.63](#appendix-a63).

Higher-trust entries dominate retrieval; lower-stage entries returned with warning to persona.

## 15. Safety-critical domain handling

*Safety-critical indicators: physical_harm_class at or above bodily_injury, information_hazard_class at or above dual_use_civilian, any proposed safety extension, any regulated-tagged KnowledgeRef, or operator policy naming a domain category. Promotion gates tighten: EMERGENT to RECOGNISED requires operator review queue; RECOGNISED to AUTHORITATIVE requires operator signature (blocking gate); AUTHORITATIVE to STANDARDISED requires multiple operator signatures plus external standards body attestation. Under principal collapse, the degraded gate substitutes (72h cool-down, non-principal attestation, signed acknowledgement). All decisions are logged in OperatorDecisionLineage.*

**Technical detail:** See [A.64](#appendix-a64).

## 16. DomainLineage (J9 corollary, C1)

*The DomainLineage records all domain lifecycle events: probe lifecycle (initiated, phases, budget, halted), knowledge operations (ingested, transitions), tool discovery, convention lifecycle (proposed, adopted, ambiguity, reconciliation, deprecated), safety extensions, verifier recipes, proposal management (convergence, consolidation, rate-limited), demotion, cross-domain transfer, promotion, dormancy, bridge lifecycle, and events (budget envelopes, pledges, cold-start uplift, bulk proposals, precedent imports, single-project promotion, domain harvests).*

**Technical detail:** See [A.71](#appendix-a71).

Append-only and signed. Reconstruction via replay (J9 corollary).

## 17. EmergentDomainContext in operation

In envelope minting, the kernel injects stage-appropriate context warnings. For EMERGENT domains, a non-cacheable warning notes trust 0.3 and ongoing probe. For RECOGNISED domains, a similar notification. AUTHORITATIVE and STANDARDISED domains receive no special warning. When a task appears in a completely new domain, the kernel emits DOMAIN_UNKNOWN_DETECTED and routes to interleaved or sequential probe.

**Technical detail:** See [A.66](#appendix-a66).

## 18. Federated domain emergence (v1.1+)

Multi-kernel emergence requires federated discovery via A2A, cross-kernel promotion (EMERGENT in two kernels produces a RECOGNISED candidate with A2A agreement, dual operator approval, and cross-kernel co-signers), and federated AUTHORITATIVE to STANDARDISED consensus among N participating kernels with anti-sybil reputation counting.

**Technical detail:** See [A.67](#appendix-a67).

Federated emergence ships incrementally; v1.0 supports single-kernel emergence.

## 19. Operator vs Persona role shift

*Operator still owns: safety gates, deployment policy, cross-org sharing approval, persona suspension, tool registry blessing, promotion thresholds, budget caps, paywalled source authorisation, audit review, and drift escalation. Operator no longer authors: DomainContext content (personas emerge it), knowledge corpora (personas ingest), tool ecosystems (personas discover), verifier recipes (personas infer), safety extensions (personas propose; operator gates), conventions (personas adopt), and seed skills (personas synthesise).*

**Technical detail:** See [A.68](#appendix-a68).

### 19.1 Multi-tenant ORG_A / ORG_B interaction

In shared-kernel multi-tenant deployments, two operators (ORG_A, ORG_B) each own per-org scoped resources.

*Cross-org operations require: (1) policy intersection (both operators must allow), (2) data classification check (source classification permits and target has clearance), (3) dual-signing (both operators' keys), (4) audit trail (CrossOrgTransfer in both lineages), and (5) revocation (either org may revoke; propagates to consumers).*

**Technical detail:** See [A.69](#appendix-a69).

v1.0 ships multi-tenancy as opt-in; v1.0 single-tenant by default.

**Companion section.** This `§19.1` covers cross-org *artifact / skill transfer* mechanics. For joint-project *formation* mechanics (multi-principal attribution, charter ratification quorum, completion quorum, derivation provenance), see `04_PROJECT §19.1`. The two compose: a joint project's ongoing work emits `CrossOrgTransfer` events (this section) when explicit artifacts move between orgs, AND `DerivationProvenanceEdge` events (`08_KNOWLEDGE §16b`) when implicit derivation occurs.

## 20. Performance and cost

*Latency targets: domain unknown detection 30ms, probe initiation 100ms, MCP-Zero discovery 200ms, knowledge ingestion (single paper) 60s, promotion ceremony 1 min. Cost targets: narrow probe $1-5, broad probe $10-50, active emergent domain $50-500/month, standardised domain $5-50/month, ingestion $0.10-1.00/paper, bootstrap to RECOGNISED up to $500, to AUTHORITATIVE up to $2000.*

**Technical detail:** See [A.70](#appendix-a70).

## 21. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations).

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-DOMAIN-1 | Hallucination during EMERGENT stage. Promotion gates filter most; some slip. | High | Medium | Multi-tier promotion (PROBING → EMERGENT → RECOGNISED → STABLE); tighter co-signing thresholds for safety-critical; convergence detection. | v1.0 (gates); v1.1 (judge panel for emergent claims). |
| R-DOMAIN-2 | Operator review bottleneck for safety-critical domain adoption. Human review introduces real delay. | Medium | High | Operator pre-approval of broad categories; ProposedSafetyExtension review queue prioritisation. | v1.0 (queue); v1.1 (pre-approval categories). |
| R-DOMAIN-3 | Drift detection sensitivity tradeoff. Tight thresholds generate false positives; loose thresholds miss. | Medium | High | Operator-tunable thresholds; per-domain calibration via reference signal set; drift-bounds schema. | v1.0 (baseline); v1.1 (auto-calibration). |
| R-DOMAIN-4 | Federated multi-kernel emergence is only specified for v1.0. Cross-kernel domain probe coordination ships v1.1+. | Medium | Low | Single-kernel emergence is fully supported; federated mode shadow-only until v1.1. | v1.1 (cross-kernel emergence). |
| R-DOMAIN-5 | Knowledge sourcing variance. Paywalled sources limit completeness; licensing per source is operator concern. | Medium | High | KnowledgeIngestionRecord declares source + licence; operator policy on admissible sources. | v1.0 (record); v1.1 (license-aware ingestion). |
| R-DOMAIN-6 | Cross-domain trust calibration is heuristic. Initial 0.3 reduction at transfer is uncalibrated for many domain pairs. | Medium | High | DomainPrecedentImport with kinship measurement; empirical re-calibration after observed cross-domain outcomes. | v1.1 (calibration loop). |
| R-DOMAIN-7 | Convention reconciliation at federation merge. Communities evolve different notations; merger is hard. | High | Medium | NotationConvention versioning; explicit conflict events `NOTATION_CONFLICT`; operator-mediated reconciliation; A-PJ18 acceptance test. | v1.1 (stronger consensus mechanisms). |
| R-DOMAIN-8 | Dormant-domain reanimation behaviour varies. Six-month dormancy threshold operator-tunable; reanimation cost not bounded. | Low | Medium | Operator-set thresholds; explicit reanimate ceremony; lineage replay scoped to last active window. | v1.1 (cost bounds). |
| R-DOMAIN-9 | Cross-org IP in emergent contexts. Operator policy is explicit; real-world contracts vary. | High | Medium | Operator policy at admission; cross-org sharing requires explicit licensing; domain-card visibility tiers. | v1.0 (policy surface). |
| R-DOMAIN-10 | Probe budget pledges cannot transact. `ProbeBudgetEnvelope` tracks pledges; actual payment is operator-wrapped. A pledge default has no substrate recourse. | Medium | Low | `PLEDGE_REVOKED` event; reputation impact on defaulting funder; operator can freeze the funder's future pledges. | v1.0 (substrate); v1.2+ (operator-side payment integration). |
| R-DOMAIN-11 | Cold-start `K_effective` scaling is heuristic. Adversarial proposers may saturate the bundle path. | Medium | Low | Convergence-detection backstop (`§9.1.1`); per-proposer rate caps; classifier rotation. | v1.0 (heuristic); v1.1 (anti-saturation). |
| R-DOMAIN-12 | Kinship measurement assumes shared lineage history. Recently bootstrapped domains produce low confidence and block imports. | Low | Medium | Manual override at operator level for known-related domains; lineage seeding from authored convention sets. | v1.1 (seed kinship). |
| R-DOMAIN-13 | Single-project promotion (`§3.2`) concentrates risk. Trades statistical robustness for accessibility. | High | Medium | Trust cap (0.6) on single-project promotions; `refused_when_safety_critical` interlock; principal-collapse degraded gate; explicit downgrade if downstream evidence diverges. | v1.0 (cap + interlock). |
| R-DOMAIN-14 | DomainHarvest at federation / public tiers depends on v1.1 federation index. v1.0 ships private tier only. | Low | Low | v1.0 emits `DOMAIN_HARVEST_PUBLISHED` and writes entry; non-private tiers refused at admission until v1.1. | v1.1 (federation tier consumers). |

## 21a. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-DOMAIN-1 | Cross-kernel emergent-domain coordination (R-DOMAIN-4): what's the conflict policy when two kernels independently emerge the same domain with divergent ontologies? Convergence-detection backstop, or operator-mediated merge? | Federation WG | v1.1 merge protocol. |
| OQ-DOMAIN-2 | DomainPrecedentImport kinship measurement (R-DOMAIN-12): seed kinship from authored convention sets, or always require lineage history? Hybrid? | Domain curators | v1.1 seed kinship. |
| OQ-DOMAIN-3 | Single-project promotion trust cap (0.6): empirical re-calibration after observing downstream outcomes — is 0.6 too conservative? Per-domain or universal? | Domain curators | v1.1 calibration. |
| OQ-DOMAIN-4 | CredentialDirectoryRef revocation propagation: how fast must a revoked credential propagate to all kernels that have accepted attestations from it? Same-day, hourly, real-time? | Security auditors | v1.1 revocation SLA. |
| OQ-DOMAIN-5 | DomainHarvest federation (R-DOMAIN-14): v1.0 ships private tier only. What's the indexing model for the federation tier — pull (consumers query) or push (producers gossip)? | Federation WG | v1.1 harvest index. |
| OQ-DOMAIN-6 | physical_harm_class taxonomy: v1.0 defines {none, property, bodily_injury, life_critical}. Is finer granularity needed for medical / aviation / nuclear domains? | Safety floor WG | v1.2 taxonomy. |
| OQ-DOMAIN-7 | Operator pre-approval categories (R-DOMAIN-2): what's the right granularity? Per safety-class, per harm-class, per domain-kind? | Operator policy | v1.1 pre-approval schema. |

## 22. Acceptance tests

```text
A-DM1   Task triggering signal A or B emits DOMAIN_UNKNOWN_DETECTED;
        kernel routes to probe lifecycle.
A-DM2   Probe initiated → phases entered/completed → signed lineage.
A-DM3   Narrow probe completes per criteria (≥ 1 verified pattern,
        ≥ 3 KnowledgeRefs, competence ≥ 0.5).
A-DM4   Broad probe completes per criteria.
A-DM5   Failed probe emits PROBE_INSUFFICIENT; re-runs.
A-DM6   Two personas same domain hint: kernel coordinates.
A-DM7   Operator-set probe budget cap enforced; HALTED state.
A-DM8   DomainLineage append-only + replayable.
A-DM9   Multi-persona probe consolidation via co-signing.
A-DM10  Sequential vs interleaved probe routing respects time constraints.
A-DM11  Probe duration within target.
A-DM12  Probe cost respects operator caps.
A-DM13  Probe phase records (Perception/Historian/Abduction/Composition)
        emitted signed; later phases consume earlier ones by reference.
A-DM14  Multi-persona coordination defaults to Option B for same-env;
        Option A for cross-env; Option C only with operator-approved A2A.
A-DM15  PROBE_BUDGET_THRESHOLD emits at ≥ 75% of cap; HALTED at 100%;
        operator BUDGET_INCREASE unhalts.

A-DI1   MCP-Zero discovery within ≤ 200 ms p95.
A-DI2   Smoke test runs; accepts or rejects; signed.
A-DI3   Trust score updates per success_rate; capped at 0.95.
A-DI4   Federated tool discovery (cross-kernel) returns peer tools.
A-DI5   Knowledge ingestion 7-stage; signed at each step.
A-DI6   OWASP filter applies to ingested chunks.
A-DI7   Paywalled content requires operator policy.
A-DI8   Federated knowledge lookup deduplication via content_hash.
A-DI9   Tool trust below threshold triggers consent/review.
A-DI10  Cross-persona sharing honours visibility tier.
A-DI11  Tool authoring (Voyager class C) follows ToolArtifact FSM.
A-DI12  Discovery + ingestion within probe budget.
A-DI13  KnowledgeRef FSM transitions (INGESTED→CITED→REUSED→CANONICAL,
        plus SUPERSEDED / DEPRECATED / REVOKED) signed and replayable.
A-DI14  KnowledgeRef visibility tier honoured at retrieval; tier
        downgrades on REVOKED collapse to persona_only.
A-DI15  Federated knowledge lookup returns peer-signed pointer; trust
        merge = min(local, peer); latency ≤ 1 s + A2A p95.

A-IN1   Verifier recipe inferred after K=3 consistent traces;
        held-out validated.
A-IN2   Safety extension proposed; safety-critical → operator queue.
A-IN3   Convention emerged via K=3 co-signers; NOTATION_CONFLICT
        detected.
A-IN4   Standards reference cataloged; inability-to-verify declared.
A-IN5   Cross-source validation 5 checks; proposal blocked on failure.
A-IN6   ProposalQueue weekly review; auto-accepts low-risk.
A-IN7   Multi-persona inference convergence; merge offered.
A-IN8   Proposal rate-limited per persona (K=10).
A-IN9   Proposal budget tracked; threshold warning at 75%.
A-IN10  Inferred vs authored recipe coexists with stage hierarchy.
A-IN11  PROPOSAL_CONVERGENCE_DETECTED emits when ≥ 2 personas propose
        similar entries (cos ≥ 0.85); merge accepted on ≥ 2 co-signs.
A-IN12  CONVENTION_AMBIGUITY (Signal E) triggers reconciliation flow;
        CONVENTION_RECONCILIATION_PROPOSAL signed; aliases preserved.

A-CR1   EMERGENT → RECOGNISED auto-promotion when thresholds met.
A-CR2   RECOGNISED → AUTHORITATIVE requires external validation;
        safety-critical → operator signature.
A-CR3   AUTHORITATIVE → STANDARDISED requires operator declaration
        or federation consensus ≥ 0.8.
A-CR4   Demotion: AUTHORITATIVE → RECOGNISED on drift.
A-CR5   Revocation: STANDARDISED → DEPRECATED with corrective plan.
A-CR6   Tombstoning preserves entry; not retrievable.
A-CR7   Cross-domain transfer with trust adjustment.
A-CR8   Anti-leakage: user_id / org_id / project_id / IP / cross-org
        blocked appropriately.
A-CR9   Stage-aware retrieval: lower stages reduced scores.
A-CR10  Safety-critical domain goes to operator review queue.
A-CR11  Promotion ceremony atomic.
A-CR12  DomainCurator: cannot unilaterally promote past RECOGNISED.
A-CR13  Federated cross-kernel promotion requires multi-kernel
        A2A + operator approval.
A-CR14  Drift audit nightly; flags declining conformance.
A-CR15  ToolArtifact FSM (PROPOSED → SANDBOXED → VERIFIED → PROMOTED →
        REVOKED/SUPERSEDED) enforced; personas cannot self-promote.
A-CR16  Dormant domain auto-detected at N=6 months; reanimation
        decides continuation vs new probe by task-fingerprint similarity
        ≥ 0.7; deprecation proposed at N+M=18 months.
A-CR17  Multi-tenant cross-org transfer requires dual operator signing;
        either refusal blocks; revocation propagates to both orgs.

A-EN1   ProbeBudgetEnvelope at admission: probe refuses to run with
        zero pledged units; sufficient pledges resume admission.
A-EN2   Pledge kinds: principal_pledge, non_principal_internal_pledge,
        non_principal_external_pledge, prior_domain_amortization,
        federation_pool_share — each admits under documented topology.
A-EN3   Under principal_topology=operator_is_user, non_principal_internal
        _pledge is refused; non_principal_external_pledge requires
        ExternalAgent with credential disjoint from principal.
A-EN4   federation_pool_share refused at admission in v1.0
        (forward-compatibility schema only).
A-EN5   ENVELOPE_LOW emits at warn_at_pct; ENVELOPE_EXHAUSTED halts at
        halt_at_pct; fresh ProbeBudgetPledgeRequest resumes probe.
A-EN6   Envelope and pledge events append-only and replayable.

A-CS1   Cold-start uplift fires only when KindRegistry.size ≤
        cold_start_active_when_registry_size_lte; once registry grows
        beyond, uplift fades per decay_kind.
A-CS2   K_effective = baseline + log2(N_ingested + α·N_standards);
        capped at max_uplift; safety_critical multiplier tightens, not
        loosens.
A-CS3   BulkKindProposal counts as 1 session proposal; member proposals
        still scanned for PROPOSAL_CONVERGENCE_DETECTED individually.
A-CS4   Bulk bundle held pending on first member cross-source-validation
        failure; per-member status map preserved.
A-CS5   primary_evidence_content_hash rotation invalidates bulk bundle;
        bundle must be re-drafted against new hash.

A-PR1   DomainPrecedentImport draft refused when discount_factor < 0.3
        (kinship too thin).
A-PR2   evidence_overlap_count and structural_kinship_score are kernel-
        computed at draft; persona-supplied values rejected.
A-PR3   Under safety_critical OR operator_is_user: kinship_attestation
        _ref REQUIRED; missing attestation refuses draft.
A-PR4   Imported entries start at EMERGENT in target regardless of
        source stage (no trust laundering).
A-PR5   Probationary uses default K=2; 3 cumulative failures revoke the
        affected entry (rest of bundle retained).
A-PR6   Anti-leakage §11.1 RISK A-E filter applied to imported entries;
        leakage_filter_report records counts per risk.

A-SP1   single_project_mode requires expected_project_count = 1 and
        one_shot_rationale (signed).
A-SP2   Substitute thresholds (verified_attestation_density,
        verifier_recipe_pass_rate, asbuilt_reconciliation_clean_rate,
        panel_acceptance_rate) all evaluated from kernel counters; no
        domain content inspection.
A-SP3   refused_when_safety_critical = True blocks single_project_mode
        on any domain whose hazard axes trip safety_critical = True.
A-SP4   trust_cap = 0.6 ceiling enforced on entries promoted via this
        mode; further AUTHORITATIVE promotion blocked until standard
        multi-project thresholds met.
A-SP5   Under operator_is_user, SINGLE_PROJECT_PROMOTION_ACKNOWLEDGED
        requires 72h cool-down + non-principal ExternalAttestation +
        signed acknowledgment; operator_co_signed_by refused.

A-HV1   DomainHarvest at project completion: auto-drafted when single_
        project_mode.enabled = True and completion ceremony fires.
A-HV2   Snapshot_at_lineage_height pins the harvest; replay truncated
        at that height reproduces the inventory.
A-HV3   Anti-leakage filter (§11.1) applied at harvest time; entries
        needing consent held until leakage_consent_refs supplied.
A-HV4   visibility_tier transitions above "private" require operator
        signature (or degraded gate under collapse).
A-HV5   DomainPrecedentImport consuming a harvest pins the source at
        harvest_id; trust_cap is honoured as the import's ceiling.
A-HV6   HARVEST_REVOKED propagates: downstream imports flagged for
        re-attestation; imported entries demoted to EMERGENT after
        grace window expiry.
```

## 23. Where to read next

- Persona that probes and curates domains: [`02_PERSONA.md`](02_PERSONA.md)
- Project that hosts work in domains: [`04_PROJECT.md`](04_PROJECT.md)
- Knowledge tier mechanisms: [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)
- Protocols (MCP discovery, A2A federation): [`09_PROTOCOLS.md`](09_PROTOCOLS.md)

## Technical Appendix

The appendices below contain the full technical schemas, data structures, diagrams, and specification tables referenced throughout this document. Each appendix is referenced from the section where it applies.

### A.1 DomainContext schema

<a id="appendix-a1"></a>

```python
@dataclass
class DomainContext:
    schema: str = "domain-context/2"
    
    # IDENTITY
    domain_id: str
    name: str
    description: str
    version: int
    parent_domain_id: str | None          # for hierarchy (smps_design < power_electronics)
    created_at: datetime
    maintainer: str                       # operator/org or "emergent"
    signed_by: bytes
    
    # ORIGIN + STAGE
    origin: Literal["operator_authored", "emergent"]
    stage: Literal["emergent", "recognised", "authoritative", "standardised"]
    trust_score: float                    # 0..1
    spawned_from_probe_id: str | None     # if emergent
    contributing_personas: list[str]
    co_signing_personas: list[str]
    promotion_history: list[PromotionEvent]
    emergence_lineage_id: str | None      # the DomainLineage
    safety_critical: bool
    operator_review_required: bool
    
    # KNOWLEDGE
    knowledge_refs: list[KnowledgeRef]
    
    # TOOLS (4 classes: kernel-native, domain-required, persona-learned,
    #        human-bridged — v1.0)
    tools_required: list[ToolSpec]
    tools_recommended: list[ToolSpec]
    
    # VERIFIERS
    verifier_recipes: list[VerifierRecipe]
    judge_panel_templates: list[JudgePanelTemplate]
    
    # SAFETY (v1.0 §01 §2 — 8-source floor)
    safety_extensions: list[SafetyExtension]
    external_tool_requirements: list[ToolRequirement]

    # HAZARD AXES (; C4 substrate-pure replacement for the
    # old closed safety_critical domain enum).  Both axes are about
    # hazard SHAPE / SEVERITY, not about which domains — the substrate
    # carries no list of domain names.  When either axis crosses
    # threshold, ProposedSafetyExtension is auto-marked safety_critical
    # and routed to operator_review.  Persona-inferred from emergent
    # OutcomeKinds and KnowledgeRef provenance (06_DOMAIN §6.1).
    # Operator policy (floor source 4) is the place to name specific
    # regulated categories (HIPAA, ITAR, EAR, GDPR, FINRA, EU AI Act,
    # etc.) — substrate stays category-agnostic.
    #
    # physical_harm_class — harm to the physical world (bodies, property,
    # environment).  Orthogonal to RiskPolicy (DESIGN_PERSONA_OS_V2.md
    # §11), which scores digital risk.
    physical_harm_class: Literal["digital_only",
                                  "property_damage",
                                  "bodily_injury",
                                  "fatality_risk"] = "digital_only"
    # information_hazard_class — harm via information disclosure / dual-
    # use / capability uplift.  Cryptography-breaking, biotech-uplift,
    # offensive cyber, defence-adjacent capability, advanced-AI techniques
    # all sit on this axis without naming any domain.  When ≥
    # "dual_use_civilian", safety_critical=True fires; when ≥
    # "export_controlled", operator policy MUST encode the applicable
    # regulatory regime before AUTHORITATIVE promotion is admissible.
    information_hazard_class: Literal["none",
                                       "dual_use_civilian",
                                       "export_controlled",
                                       "national_security"] = "none"

    # CORPUS EVOLUTION MODE (; frontier-research support)
    # Substrate-shape (about corpus stationarity, NOT about domain).
    # Persona-inferred from KnowledgeIngestionRecord arrival rate and
    # KnowledgeRef supersession patterns over the trailing window.
    #   stable    — corpus rarely changes; probe completes and stays
    #               completed (v1.0 default; settled domains).
    #   evolving  — corpus changes monthly; probe revisits quarterly;
    #               re-ingestion budgets allocated.
    #   frontier  — corpus changes daily; probe stays permanently
    #               active with daily ingestion budget; no completion
    #               gate.  Trust scores cap lower until corpus
    #               stabilises locally.
    # Operator may override.
    corpus_evolution_mode: Literal["stable",
                                    "evolving",
                                    "frontier"] = "stable"

    # SESSION BUDGET PROFILE
    # Recommendation only; resolution per 03_TASKS §2.5.  Environment
    # blueprint budget_override wins; this is the fallback.  Inferred
    # from KnowledgeIngestionRecord median size and OutcomeKind family;
    # operator may override explicitly.
    session_budget_profile: Literal["reasoning_heavy",
                                     "document_heavy",
                                     "tool_heavy",
                                     "balanced"] = "reasoning_heavy"

    # CREDENTIAL DIRECTORIES
    # Per-domain references to external authorities that resolve
    # ExternalAttestation.attestor_credential_id (04_PROJECT §26a.3).
    # Mirrors the StandardRef catalog pattern (§7.4).  Without a
    # directory, attestations are admissible but credential_unverified.
    credential_directories: list[CredentialDirectoryRef]

    # STANDARDS
    standards_refs: list[StandardRef]
    
    # NOTATION
    default_notation: dict[str, NotationDef]
    
    # SEEDS
    seed_skills: list[SkillSpec]
    seed_tactics: list[str]
    seed_charters: list[str]
    seed_acceptance_pathways: list[str]
    
    # NOVELTY CHECK
    novelty_check_config: NoveltyCheckConfig | None
```

### A.2 Worked DomainContext examples

<a id="appendix-a2"></a>

```yaml
# Example A — engineering domain (operator-authored)
domain_id: power_electronics
name: Power Electronics
version: 1
origin: operator_authored
stage: standardised
trust_score: 0.95
parent_domain_id: engineering

tools_required:
  - tool_id: ngspice_simulate
  - tool_id: kicad_cli
  - tool_id: drc_check
verifier_recipes:
  - recipe_id: buck_design_verifier
    applies_to_artifact_kinds: [smps_design_bundle]
    stages: [ngspice_steady_state, ngspice_transient, bom_validity, drc]
safety_extensions:
  - extension_id: iec_62368_isolation
    enforcement: block_action
external_tool_requirements:
  - claim_pattern: claims efficiency >= X
    required_tool: ngspice_simulate
    required_outcome: efficiency_metric_present
    timing: before_action
    failure_action: refuse_action
default_notation:
  Fsw: switching frequency (kHz)
  Δi: inductor ripple current (A)
seed_charters:
  - "I never claim safety compliance without DRC + standards check"
```

```yaml
# Example B — mathematical domain (emergent)
domain_id: category_theory
name: Category Theory
version: 1
origin: emergent
stage: recognised
trust_score: 0.6
parent_domain_id: pure_mathematics
spawned_from_probe_id: probe-cat-2026-03

tools_required:
  - tool_id: lean_verify
  - tool_id: arxiv_search
verifier_recipes:
  - recipe_id: lean_proof_verifier
    applies_to_artifact_kinds: [lean_proof]
    stages: [lean_typecheck, lean_proof_check]
external_tool_requirements:
  - claim_pattern: claims theorem proven OR uses "QED" OR "∎"
    required_tool: lean_verify
    required_outcome: proof_accepted
    timing: before_action
novelty_check_config:
  enabled: true
  search_tool: arxiv_search
  threshold: 0.85
default_notation:
  "→": morphism
  "F ⊣ G": F left adjoint to G
seed_charters:
  - "I declare conjectures explicitly; never call them theorems before proof"
```

### A.3 Versioning and rotation policy

<a id="appendix-a3"></a>

```text
VERSION BUMP
  ▸ integer; signed by maintainer (or kernel for emergent).
  ▸ a project pins (domain_id, version) at activation.
  ▸ projects opt-in to a new version via signed `domain_version_upgrade`
    event (operator approval if safety-critical).

CLASSIFIER ROTATION
  ▸ classifier models in safety_extensions, external_tool_requirements,
    novelty_check_config rotate per `rotation_pool_id` schedule.

KNOWLEDGE FRESHNESS
  ▸ corpora re-indexed quarterly by default; emits
    DOMAIN_KNOWLEDGE_STALE on miss.

VERSION HISTORY RETENTION
  ▸ all prior versions kept (signed, immutable); retrieval pinned to
    the activation version.

DEPRECATION PROPAGATION
  ▸ deprecating version N emits `DOMAIN_VERSION_DEPRECATED` to all
    dependent projects with corrective_action + migration window.
  ▸ projects unable to upgrade enter `STALE_DOMAIN_PINNED` warning state.
```

### A.4 Domain hierarchy and multi-domain personas

<a id="appendix-a4"></a>

```text
HIERARCHY (via parent_domain_id)
  pure_mathematics
    ├── category_theory
    │     ├── higher_categories
    │     └── enriched_categories
    └── number_theory
  engineering
    ├── power_electronics
    │     └── smps_design
    └── rf_engineering

INHERITANCE RULES
  knowledge_refs:        UNION of ancestors + self
  tools_required:        UNION; child may upgrade required-version
  safety_extensions:     UNION with MOST-RESTRICTIVE-WINS
  external_tool_reqs:    UNION; child may add stricter
  default_notation:      child OVERRIDES parent
  seed_skills/charters:  child OVERRIDES parent

MULTI-DOMAIN PERSONAS
  ▸ mode_proficiencies are mode-level; domain-independent.
  ▸ skill_library entries tagged domain_id; retrieval filters by
    active project's domain.
  ▸ cross-domain transfer goes through §11 CrossDomainTransfer
    (trust adjusted; signed).

CONFLICT RESOLUTION (notation collision across domains)
  ▸ project's domain wins; persona may aliase in
    PersonaEnvelope.project_context.
  ▸ if persona is genuinely working across both, kernel emits
    NOTATION_SCOPE_CONFLICT; DomainCurator (§10) reconciles or persona
    declares explicit local scope.
```

### A.5 The four promotion stages

<a id="appendix-a5"></a>

```text
STAGE 1: EMERGENT (trust 0.3)
  ▸ Used only by proposer in originating project.
  ▸ Signed; reversible; auditable.
  ▸ No operator review.

STAGE 2: RECOGNISED (trust 0.6)
  ▸ K=3 successful projects; 2+ co-signing personas;
    cross-source validation passes.
  ▸ Used cross-project within the domain.
  ▸ DomainCurator (if present) reviewed.
  ▸ Kernel auto-promotes when thresholds met.

STAGE 3: AUTHORITATIVE (trust 0.85)
  ▸ K'=10 successful projects; 5+ co-signing personas; T=3+ months at RECOGNISED.
  ▸ External validation: peer-reviewed paper / patent / bench measurement /
    production deployment / standards body attestation.
  ▸ For safety-critical: operator co-signature REQUIRED.
  ▸ For non-critical: kernel auto-promotion with audit.
  ▸ Cited in PersonaCard / EnvCard / DomainContextCard.

STAGE 4: STANDARDISED (trust 0.95)
  ▸ Operator declaration (single-kernel) or federation consensus ≥ 0.8
    (multi-kernel).
  ▸ Functionally equivalent to operator-authored DomainContext.
  ▸ New projects inherit standardised version as default.
  ▸ Standardisation may be revoked on drift detection.
```

### A.6 PromotionPolicy

<a id="appendix-a6"></a>

```python
@dataclass
class PromotionPolicy:
    domain_id: str
    
    # EMERGENT → RECOGNISED
    emergent_to_recognised:
      min_successful_projects: int = 3
      min_cosigning_personas: int = 2
      cross_source_validation_required: bool = True
      auto_promote: bool = True
    
    # RECOGNISED → AUTHORITATIVE
    recognised_to_authoritative:
      min_successful_projects: int = 10
      min_cosigning_personas: int = 5
      min_months_at_recognised: int = 3
      external_validation_required: bool = True
      safety_critical: bool = False         # if True: operator required
      auto_promote: bool = False
    
    # AUTHORITATIVE → STANDARDISED
    authoritative_to_standardised:
      operator_declaration_required: bool = True
      federation_consensus_threshold: float = 0.8
      auto_promote: bool = False
    
    # DEMOTION
    drift_threshold: float = 0.7
    demotion_on_revocation: bool = True

    # SINGLE-PROJECT PROMOTION MODE (— §3.2)
    # When the domain is owner-declared one-shot (expected_project_count
    # = 1) the standard "K successful projects" pathway never fires
    # because no second project exists.  This mode replaces project-
    # count thresholds with within-project evidence-density thresholds.
    # Substrate-shape: all inputs are kernel-tracked counts (no domain
    # content inspection).
    single_project_mode: SingleProjectPromotionConfig | None = None
```

### A.7 SingleProjectPromotionConfig

<a id="appendix-a7"></a>

```python
@dataclass
class SingleProjectPromotionConfig:
    schema: str = "single-project-promotion-config/1"
    domain_id: str

    # When True, the substitute thresholds below replace the multi-project
    # thresholds for EMERGENT → RECOGNISED only.  RECOGNISED →
    # AUTHORITATIVE still requires external validation (§3) and is
    # unaffected.
    enabled: bool = False

    # OWNER DECLARATION — required at draft.  Persona explicitly states
    # that the domain is one-shot.  Substrate-shape (declaration about
    # project count, not about content).
    expected_project_count: int = 1            # must be 1 for enabled=True
    one_shot_rationale: str                    # natural language; signed

    # SUBSTITUTE THRESHOLDS — all substrate-shape kernel counters.
    #   verified_attestation_density
    #     ratio of OutcomeFeedback entries with attached
    #     ExternalAttestation whose credential_unverified == False
    #     to total OutcomeFeedback entries for the project.
    #   verifier_recipe_pass_rate
    #     ratio of InferredVerifierRecipe runs that passed validation
    #     within the project (denominator must be ≥ N_min_runs).
    #   asbuilt_reconciliation_clean_rate
    #     for projects with PhysicalAssets: ratio of AsBuiltReconciliation
    #     entries whose resolution = within_tolerance (vs change_order /
    #     punch_list).  Defaults to 1.0 (vacuously) when project has no
    #     PhysicalAssets.
    #   panel_acceptance_rate
    #     ratio of PANEL_ACCEPT verdicts in favour to total panel runs
    #     on artefacts from this domain.
    min_verified_attestation_density: float = 0.6
    min_verifier_recipe_pass_rate: float = 0.8
    min_n_recipe_runs: int = 5
    min_asbuilt_reconciliation_clean_rate: float = 0.8
    min_panel_acceptance_rate: float = 0.7

    # GATE — promotion requires an explicit acknowledgment that the
    # promotion rests on one project's evidence.  Under
    # principal_topology = operator_distinct: operator signature.
    # Under principal_topology = operator_is_user: degraded gate
    # (72h cool-down + non-principal ExternalAttestation +
    # signed SINGLE_PROJECT_PROMOTION_ACKNOWLEDGED).
    operator_acknowledgment_required: bool = True

    # SAFETY-CRITICAL FORBIDDEN-PATH
    # Single-project promotion is REFUSED when the domain's hazard axes
    # (§2) trip safety_critical = True.  Rationale: a single project's
    # evidence is statistically insufficient to license a safety-critical
    # entry as RECOGNISED-grade.  Such domains must accept the multi-
    # project pathway or remain EMERGENT and pursue DomainPrecedentImport
    # (§11.2) from a kin domain instead.
    refused_when_safety_critical: bool = True

    # TRUST CAP — domains promoted via this mode cap trust at 0.6
    # (RECOGNISED floor) and may NOT advance further without satisfying
    # the standard multi-project AUTHORITATIVE thresholds.
    trust_cap: float = 0.6

    signed_by: bytes
```

### A.8 Domain emergence lifecycle

<a id="appendix-a8"></a>

```text
RECOGNITION → PROBE → DISCOVERY → INGESTION → INFERENCE → PROPOSAL → CURATION → PROMOTION
```

### A.9 Recognition signals and DomainUnknownDetected

<a id="appendix-a9"></a>

```text
SIGNAL A — Empty domain context
  Task references domain_id with no DomainContext.

SIGNAL B — Persona zero matching skills
  Persona's skill_library has no entries tagged with task's domain;
  combined with low mode_proficiency.

SIGNAL C — Retrieval returns low scores
  Knowledge tier retrieval top-K max score < 0.3.

SIGNAL D — Persona self-assesses unknown
  Perceiver mode emits SELF_ASSESS_UNKNOWN.

SIGNAL E — Cross-persona terminology disagreement
  Two personas using different terms for same concept; no convention.

SIGNAL F — Existing emergent context at low stage
  Persona about to use EMERGENT-stage context; kernel may expand probe.

SIGNAL G — Kind unknown for domain (v1.0)
  Persona needs a media kind / source kind / verifier kind /
  capability kind / contribution kind / fact kind / bundle kind that
  is not in the per-domain KindRegistry and not in the MetaRegistry
  (§7.6). Triggers a probe extension that drafts the appropriate
  Proposed*Kind (§7.5).
```

```python
@dataclass
class DomainUnknownDetected:
    schema: str = "domain-unknown-detected/1"
    event_id: str
    timestamp: datetime
    persona_id: str
    project_id: str | None
    environment_id: str | None
    task_fingerprint: str
    signals_fired: list[str]
    candidate_domain_hint: str | None
    confidence_in_hint: float
    existing_emergent_domain_id: str | None
    existing_emergent_stage: str | None
    proposed_probe_id: str
    probe_budget_estimate: BudgetEstimate
    signed_by: bytes
```

### A.10 DomainProbe

<a id="appendix-a10"></a>

```python
@dataclass
class DomainProbe:
    schema: str = "domain-probe/1"
    probe_id: str
    domain_id: str
    candidate_domain_name: str
    initiated_by_persona_id: str
    initiated_at: datetime
    
    status: Literal["initiated", "exploring", "consolidating",
                    "completed", "abandoned"]
    
    initial_task_context: TaskFingerprint
    expansion_strategy: Literal["narrow", "broad", "adaptive"]
    
    # Phases
    perceiver_phase: ProbePhase | None
    historian_phase: ProbePhase | None
    abducer_phase: ProbePhase | None
    composer_phase: ProbePhase | None
    
    # Resources
    discovered_tools: list[DiscoveredTool]
    ingested_knowledge: list[KnowledgeIngestionRecord]
    inferred_recipes: list[InferredVerifierRecipe]
    proposed_conventions: list[ProposedConvention]
    proposed_safety_extensions: list[ProposedSafetyExtension]
    
    # Cost + audit
    budget_consumed: BudgetSnapshot
    sessions_used: list[str]
    contributing_personas: list[str]
    
    # Outcome
    final_emergent_domain_context_ref: str | None
    completion_criteria_met: list[CriterionStatus]
    
    signed_by: bytes
```

### A.11 Probe phase record schemas

<a id="appendix-a11"></a>

```python
@dataclass
class PerceptionRecord:
    schema: str = "perception-record/1"
    record_id: str
    probe_id: str
    persona_id: str
    captured_at: datetime
    extracted_entities: list[str]
    extracted_terminology: list[str]
    extracted_references: list[str]
    inferred_constraints: list[str]
    charter_constraints_acknowledged: list[str]
    operator_policy_hints: list[str]
    signed_by: bytes

@dataclass
class HistorianRecord:
    schema: str = "historian-record/1"
    record_id: str
    probe_id: str
    persona_id: str
    searched_at: datetime
    sources_queried: list[str]               # arxiv_search, scholar, ...
    candidate_references: list[KnowledgeRef]
    deduplication_applied: bool
    federated_lookups: list[str]             # peer-kernel queries
    relevance_ranking: dict[str, float]
    signed_by: bytes

@dataclass
class AbductionRecord:
    schema: str = "abduction-record/1"
    record_id: str
    probe_id: str
    persona_id: str
    proposed_at: datetime
    candidate_structure: str
    candidate_subdomains: list[str]
    candidate_ontology_fragments: list[dict]
    candidate_tool_categories: list[str]
    candidate_verifier_categories: list[str]
    candidate_risks: list[str]
    confidence: float                        # hypothesis-level
    signed_by: bytes

@dataclass
class CompositionRecord:
    schema: str = "composition-record/1"
    record_id: str
    probe_id: str
    persona_id: str
    composed_at: datetime
    emergent_domain_context_ref: str         # skeleton produced
    initial_stage: Literal["emergent"] = "emergent"
    initial_trust_score: float = 0.3
    signed_by: bytes
```

### A.12 Probe strategies

<a id="appendix-a12"></a>

```text
NARROW (default for first probe of task-specific domain)
  Just enough for the immediate task.
  ~5 papers ingested.
  Minimal tool discovery.
  Skip safety extension inference unless safety-critical.
  Completes when task attemptable with non-zero competence.
  Cost: $1-5 per probe.

BROAD (for multi-session arcs)
  Build proper domain foundation.
  20-50 papers ingested.
  Full tool ecosystem discovery.
  Verifier recipes for likely artifact kinds.
  Safety considerations identified.
  Conventions proposed broadly.
  Completes when emergent context is RECOGNISED-ready.
  Cost: $10-50 per probe.

ADAPTIVE (kernel-managed)
  Start narrow; expand on signals.
  If safety-critical signal → require operator gate.
  If cross-domain entities → branch into sibling probes.
```

### A.13 Probe completion criteria

<a id="appendix-a13"></a>

```text
NARROW completion (all required):
  ≥ 1 verified pattern (successful tool call confirming task progress)
  ≥ 3 KnowledgeRef entries ingested
  persona competence in active_mode for this domain ≥ 0.5

BROAD completion (all required):
  ≥ K=2 projects successfully used the emergent context
  ≥ 5 co-signing personas across sessions
  tool discovery saturation (recent searches add < 10% new candidates)
  ≥ 2 verifier recipes inferred
  ≥ 1 safety extension proposal (if any safety-relevant signal)
  ≥ 5 co-signed conventions

ADAPTIVE completion:
  kernel selects NARROW or BROAD criteria per emergent signal pattern.
  Default: start with NARROW thresholds; if SAFETY_CRITICAL_SIGNAL or
  CROSS_DOMAIN_BRANCH detected, upgrade to BROAD before completion.

FRONTIER-MODE override:
  When DomainContext.corpus_evolution_mode = "frontier", the probe
  does NOT complete in the usual sense.  Instead it transitions to
  PERSISTENTLY_ACTIVE — a long-running probe with a per-day ingestion
  budget that continuously refreshes the corpus.  Stage promotion
  uses a sliding-window cut: "≥ K consecutive 30-day windows in which
  the corpus drift rate is below threshold" instead of "tool discovery
  saturation".  Trust scores cap at 0.7 (instead of the usual 0.9)
  while the domain remains in frontier mode, honouring the fact that
  the field's own consensus is unsettled.  Operator may explicitly
  pin the domain out of frontier mode if local convergence is
  established.
```

### A.14 CorpusDriftMetric

<a id="appendix-a14"></a>

```python
@dataclass
class CorpusDriftMetric:
    schema: str = "corpus-drift-metric/1"
    domain_id: str
    window_end: datetime
    window_duration_days: int = 30            # trailing window

    # INPUTS (kernel-computed from KnowledgeRef + ProvenFact events)
    n_active_refs: int                        # KnowledgeRefs in ACTIVE
                                              # state within the domain
    n_superseded_in_window: int               # KnowledgeRefs marked
                                              # superseded_by during window
    n_retracted_in_window: int                # KnowledgeRefs retracted
                                              # during window
    n_contradicted_in_window: int             # ProvenFacts contradicted
                                              # during window

    # COMPUTED
    drift_rate: float                         # (n_superseded +
                                              # n_retracted +
                                              # n_contradicted) /
                                              # n_active_refs

    # THRESHOLDS (operator-tunable per domain)
    frontier_exit_threshold: float = 0.05     # drift_rate < 5% per
                                              # 30-day window indicates
                                              # corpus stabilisation
    k_consecutive_windows: int = 6            # 6 consecutive months
                                              # below threshold to
                                              # trigger exit eligibility

    # STATE
    consecutive_below_count: int = 0          # running count of
                                              # consecutive windows
                                              # below threshold
    exit_eligible: bool = False               # True when
                                              # consecutive_below_count
                                              # >= k_consecutive_windows

    computed_at: datetime = field(default_factory=datetime.now)
    signed_by: bytes = b""
```

### A.15 Multi-persona probe coordination

<a id="appendix-a15"></a>

```text
OPTION A — INDEPENDENT PROBES
  ▸ each persona runs its own probe end-to-end.
  ▸ resulting emergent contexts may diverge; reconciled at promotion
    via §8 cross-source validation + §9.1 PROPOSAL_CONVERGENCE.
  ▸ used when: personas are in different envs / orgs, or domains
    are sensitive to single-persona bias.

OPTION B — SHARED PROBE WITH ROLE-PHASED PARTICIPATION
  ▸ kernel elects a lead persona (highest historian/abducer mode
    proficiency); lead runs Perceiver + Abducer.
  ▸ other personas contribute to Historian + Composer per their roles.
  ▸ single shared DomainProbe entity; all participants in
    contributing_personas[].
  ▸ used when: personas share an env hosting the project (DEFAULT).

OPTION C — FEDERATED PROBE (MULTI-KERNEL)
  ▸ personas on different kernels probing same domain hint share
    probe artifacts via A2A.
  ▸ results coordinate at the federated registry (v1.1+).
  ▸ used when: cross-kernel collaboration is established and
    operator-approved.

DEFAULT RULE:
  same-env personas → OPTION B
  cross-env, same-kernel → OPTION A
  cross-kernel + operator-approved A2A → OPTION C
```

### A.16 Sequential vs Interleaved probe routing

<a id="appendix-a16"></a>

```text
INTERLEAVED (default)
  ▸ persona starts the task; kernel triggers probe in background.
  ▸ probe results feed envelope projections as they materialise.
  ▸ task progresses slowly; persona competence grows with probe.
  ▸ suited to INVESTIGATIVE / multi-session tasks.
  ▸ approved by: kernel auto-route (no operator gate unless safety-
    critical signal).

SEQUENTIAL (time-bounded / high-stakes)
  ▸ persona returns "I need to probe this domain first; here is my
    probe plan + budget".
  ▸ operator (or user, if no operator) approves probe + budget cap.
  ▸ probe runs to completion (or completion criterion);
    task resumes after.
  ▸ suited to high-stakes work where acting before knowing is risky.
  ▸ approved by: operator (mandatory for safety-critical); user for
    non-critical user-owned tasks.

OPERATOR-BUDGET-CAP PATTERN:
  Both modes carry an operator-set budget cap; if exhausted, probe
  enters HALTED. Operator may grant additional budget or accept
  narrower scope (downgrade BROAD → NARROW).
```

### A.17 ProbeBudgetCaps and threshold event

<a id="appendix-a17"></a>

```python
@dataclass
class ProbeBudgetCaps:
    schema: str = "probe-budget-caps/2"        # bump
    per_probe_cap_unit: float                  # default NARROW 5, BROAD 50
                                              # (currency-or-unit is opaque
                                              # to substrate; see §4.7.1
                                              # ProbeBudgetEnvelope for the
                                              # pledge that supplies units).
    per_domain_window_cap_unit: float          # all probes for one domain
                                              # over a rolling window
    per_persona_window_cap_unit: float         # rate-limit any one persona
    window_kind: str = "monthly"               # KindRegistry-resolved
                                              # window kind (monthly / weekly
                                              # / per-session / per-project);
                                              # substrate names no closed list.
    warn_at_pct: float = 0.75                 # emit threshold event
    halt_at_pct: float = 1.0
    safety_critical_multiplier: float = 2.0   # operator-tunable.  
                                              # auto-raised to 5.0 when the
                                              # owning DomainContext has
                                              # physical_harm_class ≥
                                              # "bodily_injury" (§2).

    # scale probe budget by detected corpus size.
    # Two complementary corpora are tracked:
    #   N_standards   = count of StandardRef entries (built environments,
    #                   regulated industries — IRC+IBC+NEC+ASTM+...)
    #   N_literature  = count of KnowledgeIngestionRecord entries from
    #                   research-literature sources (research-frontier
    #                   domains — arxiv, journals, conference proceedings)
    #
    # Effective cap:
    #   effective_cap = per_probe_cap_usd
    #                   × safety_critical_multiplier
    #                   × scaling_factor(N_standards, N_literature,
    #                                    corpus_evolution_mode)
    #
    # scaling_factor (when scaling_enabled = True):
    #   stable    → max(1, log2(N_standards))
    #   evolving  → max(1, log2(N_standards + 0.1·N_literature))
    #   frontier  → max(1, log2(N_standards + N_literature))
    #               (literature dominates; daily ingestion budget kicks
    #                in on top via probe-staying-active rule §4.4)
    # Operator-overridable per-domain.
    corpus_size_scaling_enabled: bool = True
    corpus_size_scaling_fn: Literal["none", "log2"] = "log2"

@dataclass
class ProbeBudgetThresholdEvent:
    schema: str = "probe-budget-threshold/1"
    event_id: str
    probe_id: str
    domain_id: str
    consumed_usd: float
    cap_usd: float
    pct_consumed: float                       # ≥ warn_at_pct triggered
    state: Literal["warning", "halted"]
    timestamp: datetime
    signed_by: bytes
```

### A.18 ProbeBudgetEnvelope, BudgetPledge, ProbeBudgetPledgeRequest

<a id="appendix-a18"></a>

```python
@dataclass
class ProbeBudgetEnvelope:
    schema: str = "probe-budget-envelope/1"
    envelope_id: str
    probe_id: str | None                       # null at draft; bound at admission
    domain_id: str
    related_project_id: str | None
    related_environment_id: str | None

    requested_units: float                     # in currency_or_unit of pledges
    currency_or_unit: str                      # opaque to substrate; mirrors
                                              # ExternalBudget.currency_or_unit
                                              # (04_PROJECT §26a.4)

    pledges: list[BudgetPledge]                # ≥ 1 required for admission
    consumed_units: float = 0.0
    last_reconciled_at: datetime | None = None

    state: Literal["drafted", "pledged", "active",
                    "exhausted", "released", "revoked"]
    signed_by: bytes


@dataclass
class BudgetPledge:
    schema: str = "budget-pledge/1"
    pledge_id: str
    envelope_id: str

    # SUBSTRATE-SHAPE funding kinds — describe topological position of the
    # funder relative to the principal, NEVER which domain or industry the
    # funds come from.  No closed list of donors / grants / programmes.
    #
    #   principal_pledge
    #     The principal (user_only or operator_distinct or under collapse,
    #     the principal itself) commits its own budget envelope.  Default
    #     for solo deployments.
    #
    #   non_principal_internal_pledge
    #     Another party inside the kernel boundary (operator that is not
    #     the principal under operator_distinct; an ApprovalWorkflow
    #     signoff chain that supplies a budget line) commits.  Requires
    #     the pledger's signed authorisation.
    #
    #   non_principal_external_pledge
    #     An ExternalAgent (04_PROJECT §26a.1) commits.  Substrate carries
    #     no taxonomy of grant programmes or sponsorship arrangements;
    #     the commitment is an ExternalCommitment whose
    #     expected_artifact_kind is the budget line itself
    #     (KindRegistry-resolved emergent kind).
    #
    #   prior_domain_amortization
    #     Credit drawn against evidence already ingested for a sibling /
    #     parent DomainContext where ≥ N_overlap KnowledgeRefs are shared
    #     with the target probe.  Substrate-shape: amortization is about
    #     evidence overlap, not about domain content.  Requires a signed
    #     DomainPrecedentImport (§11.2) declaring the kinship.
    #
    #   federation_pool_share
    #     Share of a federation-tier pool whose participants have signed
    #     a federation_charter (v1.1+; declared here for forward
    #     compatibility, refused at admission in v1.0).
    pledge_kind: Literal["principal_pledge",
                          "non_principal_internal_pledge",
                          "non_principal_external_pledge",
                          "prior_domain_amortization",
                          "federation_pool_share"]

    pledged_units: float
    pledged_by_actor_id: str                   # persona / user / operator /
                                              # ExternalAgent id
    pledged_at: datetime

    backing_ref: str | None                    # for non_principal_external_pledge:
                                              # ExternalCommitment id; for
                                              # prior_domain_amortization:
                                              # DomainPrecedentImport id; null
                                              # otherwise.
    expires_at: datetime | None

    state: Literal["drafted", "active", "drawn_down",
                    "released", "revoked"]
    signed_by: bytes


@dataclass
class ProbeBudgetPledgeRequest:
    schema: str = "probe-budget-pledge-request/1"
    request_id: str
    envelope_id: str
    drafted_by_persona_id: str
    drafted_at: datetime

    rationale: str                             # what the probe will ingest,
                                              # in shape-terms (e.g. "N
                                              # candidate StandardRef chapters,
                                              # K candidate KnowledgeRefs from
                                              # SOURCE_3 retrieval"); no domain
                                              # names hard-coded.
    requested_units: float
    proposed_pledge_kinds: list[str]           # ordered preference; pledge_kind
                                              # literal values above
    fallback_on_decline: Literal["halt_probe", "narrow_strategy",
                                  "defer_to_operator", "release_envelope"]

    signed_by: bytes
```

### A.19 FederatedDomainProbe

<a id="appendix-a19"></a>

```python
@dataclass
class FederatedDomainProbe:
    schema: str = "federated-probe/1"
    federated_probe_id: str
    domain_id: str                          # the shared domain
    coordinating_kernel_id: str             # who drives ingestion + signs
                                            # the canonical KnowledgeRef set
    participating_kernel_ids: list[str]

    shared_knowledge_pool_ref: str          # canonical KnowledgeRef set;
                                            # peers reference, do not copy
    shared_kindregistry_ref: str            # per-domain kind catalog shared
                                            # across peers (proposals
                                            # converge before federated
                                            # promotion)

    cost_allocation_method: Literal["equal_split",
                                      "usage_proportional",
                                      "coordinator_pays",
                                      "pledge_pool"]
    cost_allocation_evidence_refs: list[str]   # signed accounting
    drift_audit_interval: timedelta            # how often peers
                                                # cross-check the pool
                                                # for divergence

    quorum_for_cross_kernel_promotion: int = 3 # peers needed for stage
                                                # advance at the federated
                                                # level (EMERGENT → RECOGNISED
                                                # → AUTHORITATIVE)
    promotion_attestation_kinds: list[str]     # KindRegistry-resolved

    state: Literal["proposed", "active", "audit_drift_detected",
                    "fragmented", "wound_down"]
    signed_by: bytes
```

### A.20 Discovery sources

<a id="appendix-a20"></a>

```text
SOURCE 1: MCP REGISTRY (LOCAL)
  Operator-installed MCP servers; kernel-local registry.
  Discover via:
    mcp__personaos__list_tools(category="...", capability_hint="...")
  Returns: tool descriptions, schemas, latency estimates, costs.
  
SOURCE 2: MCP REGISTRY (FEDERATED)
  A2A federation extends discovery across peer kernels' registries.
  Discover via:
    mcp__personaos__discover_federated_tools(domain_hint="...",
                                               peer_trust_threshold=0.5)
  Returns: tools from peer kernels; filtered by trust.

SOURCE 3: MCP-ZERO ACTIVE DISCOVERY
  Persona expresses NEED in natural language; semantic search returns
  top-K matches.
  Discover via:
    mcp__personaos__request_tool(need="simulate quantum dynamics",
                                   context={...})
  Returns: tools ranked by semantic similarity + trust + cost.

SOURCE 4: PERSONA-AUTHORED (VOYAGER)
  If no tool found, persona authors via skill_synthesise + sandbox.
  Class C (persona-learned) skill; optionally promotable to A via
  ToolArtifact state machine.

SOURCE 5: HUMAN-BRIDGED (v1.0)
  When the capability requires physical-world coupling — instruments,
  hardware accounts, fab submission, lab equipment — the persona drafts
  a one-time HumanAssistRequest. The human performs the bridging act;
  the bridge becomes a durable BridgeAsset; from that point the
  persona uses the bridged capability autonomously without re-asking.
  Discover via:
    mcp__personaos__draft_human_bridge(need="read scope measurements",
                                          minimum_friction_script=...)
  Returns: a HumanAssistRequest ready for human review + (on grant)
  a BridgeAsset that registers as a Class D tool.

SOURCE 6: PAYMENT-BRIDGED — Class E [out-of-band; NOT a discovered tool]
  ***IMPORTANT — DiscoveredTool boundary.*** Class E is intentionally
  OUTSIDE the DiscoveredTool taxonomy. Sources 1–5 produce Class A–D
  *tools the persona can autonomously call* (modulo charter + safety
  floor). PaymentBridge is structurally different: every PaymentProposal
  requires fresh human authorisation, so a PaymentBridge is NOT an
  autonomously-callable tool and does NOT register as a DiscoveredTool.
  The DiscoveredTool.discovery_source Literal therefore stays at its 5
  values (no "payment_bridged" addition). PaymentBridge is enumerated
  alongside the 5 discovery sources only for completeness of the
  capability-acquisition picture; the registration / lifecycle /
  invocation flow lives entirely in 04_PROJECT §26a.4.1, not in §5.1
  DiscoveredTool.

  When the capability requires moving real money — paying a contractor,
  filing a permit fee, settling a fab invoice, subscribing to a
  paywalled corpus — the persona drafts a PaymentBridge (04_PROJECT
  §26a.4.1) backed by an ExternalBudget envelope. The kernel signs the
  payment PROPOSAL and the RECEIPT; the kernel NEVER moves funds. A
  PaymentBridge is Class E — strictly more restrictive than Class D —
  and does NOT register as an autonomously-callable MCP tool. Each
  PaymentProposal requires fresh human authorisation per the bridge's
  authorization_mode. MHBB advisory is suppressed when the proposal's
  backing ExternalCommitment is declared with recurrence_class in
  {"irreducible_human_content", "renewable_credential"}, consistent
  with §5.5.
  Draft via:
    mcp__personaos__draft_payment_bridge(need="pay fab invoices",
                                            external_budget_id=...)
  Returns: a PaymentBridge draft for human authorisation; on grant
  the bridge is registered Class E in the project state (04_PROJECT
  §26a.4.1), NOT in the DiscoveredTool registry. Subsequent
  PaymentProposals against the bridge each require fresh human
  authorisation.
```

### A.21 DiscoveredTool schema

<a id="appendix-a21"></a>

```python
@dataclass
class DiscoveredTool:
    schema: str = "discovered-tool/1"
    discovery_id: str
    tool_id: str
    discovered_by_persona_id: str
    discovered_at: datetime
    discovery_source: Literal["mcp_registry_local",
                              "mcp_registry_federated",
                              "mcp_zero_active",
                              "persona_authored_voyager",
                              "human_bridged"]
    bridge_asset_id: str | None           # set iff source=human_bridged
    
    requested_need: str                   # natural language need
    semantic_match_score: float
    
    tool_description: str
    tool_schema_ref: str
    declared_capability: str
    typical_latency_ms: float | None
    typical_cost_per_call: float | None
    
    publisher: str
    publisher_trust_score: float
    publisher_attestation: str | None
    
    smoke_test_passed: bool
    smoke_test_result_ref: str | None
    
    stage: Literal["candidate", "trial", "accepted", "rejected"]
    trial_uses: int
    successful_uses: int
    trust_score_in_domain: float
    
    related_probe_id: str
    domain_id: str
    
    signed_by: bytes
```

### A.22 Discovery and smoke-test 10-step flow

<a id="appendix-a22"></a>

```text
1.  PERSONA expresses need (natural language):
       "need a tool that simulates quantum master equations"
2.  KERNEL queries available registries (local + federated)
3.  TOP-K candidates returned (qutip_simulate, qiskit_dynamics, ...)
4.  PERSONA reviews descriptions, schemas, cost estimates
5.  PERSONA picks one (or asks kernel to auto-pick best match)
6.  KERNEL runs smoke test:
       - validate MCP schema
       - dry-run with simple input
       - check publisher attestation (if any)
7.  IF smoke test passes:
       DiscoveredTool enters at `candidate` stage with trust_score=0.3;
       tool registered in persona's session allowed_tools (charter-bound)
8.  PERSONA invokes for first task → result + verification
9.  After K successful uses:  candidate → trial → accepted
10. After §3 domain promotion gate: accepted → kernel-promoted to class B
       (domain-required) or class A (kernel-native)
```

### A.23 Trust score evolution formula

<a id="appendix-a23"></a>

```python
def update_trust(tool):
    successes = tool.successful_uses
    trials    = tool.trial_uses
    success_rate = successes / max(trials, 1)

    if trials < 5:
        # cold-start ramp
        tool.trust_score_in_domain = 0.3 + 0.1 * successes
    else:
        # weighted prior + observed
        tool.trust_score_in_domain = (
            0.3 * 0.4               # prior weight
            + success_rate * 0.6    # observed weight
        )

    # cap unless kernel-promoted to class A
    tool.trust_score_in_domain = min(tool.trust_score_in_domain, 0.95)

    # verifier-failure penalty
    if recent_verifier_failures(tool) > threshold:
        tool.trust_score_in_domain *= 0.5

    # auto-demotion gate
    if tool.trust_score_in_domain < 0.2:
        require_explicit_consent_or_operator_review(tool)
```

### A.24 ToolArtifact state machine

<a id="appendix-a24"></a>

```text
┌──────────┐ TOOL_PROPOSAL (id, code, description, verification_set,
│ PROPOSED │  env_compatibility) — proposal without verification_set is
└────┬─────┘  rejected at admission.
     ▼
┌───────────┐ kernel runs the tool against verification_set inside the
│ SANDBOXED │  sandbox env; resource caps apply.
└────┬──────┘  hard-fail (sandbox violation, infinite loop) → REJECTED;
     ▼          author absorbs cascade-failure penalty.
┌──────────┐ verification_set passes; provenance_score initialised
│ VERIFIED │  callable by the authoring persona only.
└────┬─────┘
     ▼
┌──────────┐ auto-promotion criteria:
│ PROMOTED │   (a) verification_set ≥ 5 distinct cases
└────┬─────┘   (b) cascade clean
     │          (c) 0 constraint violations across 10 SANDBOXED uses
     │          (d) author fitness > median for their role
     │         otherwise → operator review queue.
     │         registered in global tool_registry; env allow-lists updated.
     ▼
┌──────────┐ triggers:
│ REVOKED  │   (a) 3 consecutive cascade failures post-promotion
└──────────┘   (b) peer invocation triggers constraint violation
                (c) newer version supersedes → SUPERSEDED (sibling state)
                (d) operator action
               provenance_score → 0.2; K-lines referencing it marked legacy.
```

### A.25 MHBB principle and HumanAssistRequest schema

<a id="appendix-a25"></a>

```text
The persona MUST prefer "ask once, automate after" over "ask each time."
The persona MUST design the minimum-friction one-time action that
unlocks the durable autonomous capability.
The persona MUST NOT re-ask the human for a recurring action that an
established bridge could serve.
The persona MAY ask the human to re-establish a degraded bridge, but
must declare degradation evidence and propose a stronger bridge if
degradation recurs.
```

```python
@dataclass
class HumanAssistRequest:
    schema: str = "human-assist/1"
    request_id: str
    drafted_by_persona_id: str
    drafted_at: datetime

    need_summary: str                     # natural language: what + why
    durable_capability_unlocked: str       # what bridge this creates
    expected_one_time_effort_minutes: int  # honest estimate
    expected_recurrence: Literal["one_time", "rare_refresh",
                                  "session_per_use"]
                                          # session_per_use is a smell;
                                          # kernel emits MHBB advisory

    # orthogonal to frequency, the *kind* of recurrence.
    # Frequency answers "how often"; class answers "is this automatable
    # in principle".
    #   one_shot_bridge       — request establishes a durable BridgeAsset
    #                           (the v1.0 default; ask once, automate after).
    #   renewable_credential  — periodic refresh of credential / token / API
    #                           key; recurrence is *expected* but each
    #                           instance is identical.
    #   irreducible_human_content — the human delivery cannot be automated
    #                           in principle (site inspection result; expert
    #                           judgement; hand signature; weather call).
    #                           MUST link to an active ExternalCommitment
    #                           (04_PROJECT §26a.1) declaring the recurrence
    #                           is modelled-and-expected.  MHBB advisory
    #                           (01_KERNEL §2 source 10) is suppressed for
    #                           this class iff linked.  Unlinked irreducible
    #                           requests are rejected at draft.
    recurrence_class: Literal["one_shot_bridge",
                               "renewable_credential",
                               "irreducible_human_content"] = "one_shot_bridge"
    external_commitment_id: str | None = None  # required when
                                              # recurrence_class =
                                              # "irreducible_human_content"

    minimum_friction_script: str           # the literal copy-pasteable
                                          # commands / steps for the human
    safety_disclosures: list[str]         # what the script touches
    rollback_instructions: str             # how to undo if user changes mind
    bridge_validation_test: str            # how persona will verify the
                                          # bridge works after grant

    # v1.0 strengthening: which tier of the MHBB ladder this request is
    # (02_PERSONA §11.1).  Substrate-shape, not domain-shape.
    ladder_tier: Literal[
        "tier_2_off_the_shelf_install",   # human installs existing software
        "tier_3_persona_authored_bridge", # human installs/fabricates persona-
                                          # authored design (see field below)
        "tier_4_human_professional_work", # human delivers their own
                                          # professional work; recurring;
                                          # must link to ExternalCommitment
    ] = "tier_2_off_the_shelf_install"

    # v1.0 strengthening: when ladder_tier = tier_3_persona_authored_bridge,
    # this points to the ArtifactBundle whose payload IS the bridge design
    # (driver code, adapter PCB layout, shim service spec, firmware,
    # control script, ingestion pipeline) authored by the persona.  The
    # human's one-time act is to fabricate / install / deploy from this
    # design.  Substrate carries no taxonomy of bridge-design kinds; the
    # kind is the ArtifactBundle's media_kind (KindRegistry-resolved).
    bridge_design_artifact_ref: str | None = None

    consent_scope: Literal["project_only", "env_only", "persona_only",
                            "operator_blessed"]
    expires_at: datetime | None           # bridge auto-revoked after

    signed_by: bytes
```

### A.26 BridgeAsset schema and lifecycle FSM

<a id="appendix-a26"></a>

```python
@dataclass
class BridgeAsset:
    schema: str = "bridge-asset/1"
    bridge_id: str
    request_id: str                        # the HumanAssistRequest that spawned it
    granted_by_user_id: str
    granted_at: datetime

    capability_kind: str                   # resolved against KindRegistry.
                                          # capability_kinds (§7.6); never
                                          # a closed enum. Examples emerge
                                          # per domain: "instrument_link",
                                          # "account_link", "permit_filing",
                                          # "inspection_request", etc.
    capability_descriptor: dict            # opaque to kernel; tool surface
                                          # registers it as MCP tool

    state: Literal["requested", "establishing", "active",
                    "degraded", "lost", "re_establishing", "revoked"]

    last_validated_at: datetime
    validation_period: timedelta           # how often persona re-checks
    consecutive_validation_failures: int

    # minimum achievable round-trip latency through this
    # bridge.  Used by the persona's planner to refuse to compose a
    # control loop whose required latency is below this floor.  Substrate-
    # shape (a number); not a domain-shape.  None means "untimed"; control
    # loops requiring guaranteed latency cannot use untimed bridges.
    closed_loop_latency_floor_ms: float | None = None
    latency_floor_evidence_ref: str | None = None  # how the floor was
                                                  # measured / declared

    related_project_id: str | None
    related_environment_id: str | None
    related_domain_id: str | None

    signed_by: bytes
```

```text
              ┌──── re_establish (with stronger bridge) ◄─────┐
              │                                                │
   REQUESTED ─► ESTABLISHING ─► ACTIVE ─► DEGRADED ─► LOST ────┘
                                  │           │
                                  ▼           ▼
                              VALIDATED   REVOKED (user or operator)
                                          (terminal)
```

### A.27 Bridge-design fabrication kinds

<a id="appendix-a27"></a>

```text
software bridge designs (most common)
  - driver_code_python_pyvisa
  - driver_code_libusb
  - shim_service_spec
  - systemd_unit_with_polling_loop
  - rest_wrapper_openapi_spec
  - serial_protocol_python_module
  - data_ingestion_pipeline
  - computer_vision_pipeline_for_photo_folder

hardware bridge designs (rarer; more friction)
  - adapter_pcb_kicad
  - cable_spec_pinout
  - mounting_bracket_step
  - microcontroller_firmware_arduino
  - logic_level_shifter_design

protocol / process designs (no hardware/software, just instructions)
  - calibration_protocol_pdf
  - sample_handoff_workflow
  - data_export_routine_spec
```

### A.28 Worked example -- homemade quantum instrument

<a id="appendix-a28"></a>

```text
Need:  measure T1 of a homemade transmon qubit on the user's bench
       (no commercial driver exists for the user's homemade AWG +
       mixer + ADC stack)

Persona at Tier 1: no MCP tool exists for "this specific bench setup"
Persona at Tier 2: pip install ibm-quantum-runtime — irrelevant; the
                   user has their own hardware, not cloud quantum
Persona at Tier 3: authors a BridgeDesignArtifact:
  media_kind: shim_service_spec
  contents:
    - pyvisa driver shim for the user's AWG (vendor manual cited)
    - mixer-control daemon
    - ADC streaming service (FastAPI + websocket)
    - REST endpoint: POST /measure_t1  → returns microseconds
    - systemd unit files for all three services
    - install.sh that wires them together

HumanAssistRequest:
  ladder_tier: tier_3_persona_authored_bridge
  bridge_design_artifact_ref: shim_service_v1
  need_summary: "Install the T1-measurement REST service on your lab PC"
  durable_capability_unlocked:
                "MCP tool measure_t1(qubit_id, n_shots) → microseconds"
  expected_one_time_effort_minutes: 90
  expected_recurrence: "rare_refresh"
  ladder_tier: tier_3_persona_authored_bridge
  minimum_friction_script: |
    # On the lab PC:
    sudo apt install python3-pyvisa
    cd /opt
    sudo git clone <persona-published-bundle> shim
    sudo /opt/shim/install.sh
    # Smoke test:
    curl localhost:8080/measure_t1?qubit=q0
  bridge_validation_test: "POST /measure_t1 returns finite µs value"

Human installs the service once.
BridgeAsset enters ACTIVE; registers as MCP tool measure_t1.
Persona invokes measure_t1(qubit_0, n_shots=1000) autonomously every time.
The BridgeDesignArtifact `shim_service_v1` lives in the project's
  ArtifactBundle list; if the persona later needs to measure T2,
  it forks v1 → v2, adds POST /measure_t2, asks human to redeploy
  ONCE.  Human bench time over the project's life: 90 min + 30 min
  for v2 = total 2 hours, instead of 60 minutes per measurement × N
  measurements over the life of the project.
```

### A.29 BridgeCalibrationBinding

<a id="appendix-a29"></a>

```python
@dataclass
class BridgeCalibrationBinding:
    schema: str = "bridge-calibration-binding/1"
    binding_id: str
    bridge_asset_id: str                        # which BridgeAsset

    # Calibration kind: KindRegistry-resolved; never closed enum.
    # Substrate seeds: "manufacturer_factory", "self_check_only", "unknown".
    # Emergent (typical): "nist_traceable", "iso_17025_accredited",
    #                     "in_house_transfer_standard", "field_recalibration".
    calibration_kind: str

    # Provenance — external_attestation that recorded the calibration.
    # Reuses 04_PROJECT §26a.3 ExternalAttestation primitive.
    attestation_id: str                         # ExternalAttestation ref

    # Reference standard chain (back to a primary, where one exists).
    # Each link is itself an ExternalAttestation id; substrate sees an
    # opaque chain it can verify signatures over.
    reference_standard_chain: list[str]

    # Timing
    calibrated_at: datetime
    expires_at: datetime | None                 # null = persona-declared
                                                # untimed (then admission
                                                # treats as immediately
                                                # expired for safety-critical
                                                # hazard envelopes)
    interval_kind: Literal["fixed",             # vendor-fixed period
                           "use_count",          # N measurements before recal
                           "drift_observed",     # recal when drift exceeds bound
                           "ambient_triggered"]  # env event triggers recal

    # Drift bounds — when the bridge emits OutcomeFeedback whose paired
    # check shows drift > drift_bound_pct, the binding auto-degrades.
    drift_bound_pct: float | None = None

    signed_by: bytes
```

```python
    # B1
    calibration_binding_id: str | None = None
    calibration_required: bool = False          # set True when the bridge's
                                                # measurements feed safety-
                                                # critical verifiers or
                                                # ExternalAttestations
```

```text
1. Resolve calibration_binding_id; refuse if null.
2. If expires_at <= now: refuse with bridge_calibration_expired event;
   bridge auto-transitions to DEGRADED.
3. If interval_kind = "use_count" and the binding's tracked counter
   has hit ceiling: same DEGRADED + refusal.
4. If reference_standard_chain is empty AND domain's
   safety_critical = True: refuse and require a chain (operator policy
   may downgrade this to a warning for non-safety-critical domains).
5. If drift_observed counter exceeds drift_bound_pct: emit
   bridge_calibration_drift_exceeded, DEGRADED.

Refused admissions surface a HumanAssistRequest of the
re-establishment shape (§5.5 degradation flow), with the binding's
expiry / counter / drift metric stated.
```

### A.30 BridgeInstallerKind

<a id="appendix-a30"></a>

```python
class BridgeInstallerKind(StrEnum):
    HUMAN                 = "human"                  # principal-class installer
                                                     # (default; existing flow)
    EXTERNAL_AGENT        = "external_agent"         # non-principal human
                                                     # (vendor, partner)
    KERNEL_TRUSTED_SYSTEM = "kernel_trusted_system"  # another autonomous
                                                     # system the kernel
                                                     # has admitted via
                                                     # operator-policy
                                                     # attestation
    CHAINED_BRIDGE        = "chained_bridge"         # an existing BridgeAsset
                                                     # acts as the installer
                                                     # (recursive)
```

```python
    # C2
    installer_kind: BridgeInstallerKind = BridgeInstallerKind.HUMAN
    installer_id: str | None = None                 # external_agent_id,
                                                    # kernel-trusted system id,
                                                    # or installing bridge_id
    installer_attestation: bytes | None = None      # cryptographic identity
                                                    # of the installer; for
                                                    # non-human installers
                                                    # this is REQUIRED
    installer_trust_ceiling: float                  # 0..1; bridge cannot
                                                    # exceed installer's
                                                    # trust ceiling
    hazard_envelope_at_install: dict                # physical_harm_class,
                                                    # information_hazard_class
                                                    # at install time; frozen
                                                    # at signing
```

```text
For BridgeAsset B with installer_kind != HUMAN:
  let H_B = B.hazard_envelope_at_install
  let H_I = hazard_envelope authorised for the installer
           (looked up by installer_id):
             EXTERNAL_AGENT     → from ExternalAgent.authorised_hazard_envelope
             KERNEL_TRUSTED_SYSTEM → from operator policy admission record
             CHAINED_BRIDGE     → from the parent BridgeAsset's envelope
  Admission requires: H_B ⊆ H_I  (each axis ≤ installer's authority).
  Violation emits installer_hazard_envelope_exceeded and refuses to
  activate the bridge.
```

### A.31 CredentialDirectoryRef and lookup flow

<a id="appendix-a31"></a>

```python
@dataclass
class CredentialDirectoryRef:
    schema: str = "credential-directory-ref/1"
    directory_id: str

    name: str                                # "California Board for
                                            # Professional Engineers",
                                            # "NCARB Architect Registry",
                                            # "AMA Physician Lookup",
                                            # "State Bar of Texas"
    publisher: str                           # the authority
    access_method: Literal["api_endpoint",
                            "mcp_tool",
                            "manual_lookup",
                            "operator_provided",
                            "not_accessible"]
    endpoint_or_tool_ref: str | None         # URL / tool_id when programmatic

    # What credential kinds this directory authoritatively resolves
    credential_kinds: list[str]              # resolves against KindRegistry
                                            # (§7.6); examples: "pe_license",
                                            # "ra_license", "md_license",
                                            # "bar_membership",
                                            # "ul_certifier_id"

    # Trust + freshness
    publisher_trust_score: float
    cache_ttl: timedelta                     # how long lookups are cached
    operator_verified: bool                  # operator confirmed directory
                                            # is real and authoritative

    cataloged_by_persona_id: str
    cataloged_at: datetime
    signed_by: bytes
```

```text
1. find_directories(domain.credential_directories, attestor_kind)
     → set of CredentialDirectoryRef whose credential_kinds match
2. for each candidate directory:
     query directory.endpoint_or_tool_ref with attestor_credential_id
     receive {is_active, issued_at, scope, revocations}
3. if any active + non-revoked + in-scope:
     emit signed CREDENTIAL_VERIFIED lineage event with directory
     content hash; clear credential_unverified flag
   else:
     emit signed CREDENTIAL_UNVERIFIED lineage event; set
     attestation.credential_unverified = True
```

### A.32 PeerAttestationPool

<a id="appendix-a32"></a>

```python
@dataclass
class PeerAttestationPool:
    schema: str = "peer-attestation-pool/1"
    pool_id: str
    domain_id: str

    # The substrate does not name who counts as a peer.  The domain
    # itself proposes the criteria via emergent contribution_kind
    # entries in KindRegistry (§7.6); the operator confirms.
    # Examples (illustrative, NOT substrate enums):
    #   "first_author_papers ≥ 3 in last 5 years"
    #   "h_index ≥ 10 in this subdomain"
    #   "elected fellow of recognised society"
    eligibility_kind: str                    # KindRegistry resolved
    eligibility_evidence_kinds: list[str]    # KindRegistry resolved

    # Peer pool composition; each entry is itself an ExternalAgent
    # (04_PROJECT §26a.1) admitted to a project, OR a federated peer
    # persona (A2A) — never the principal of the deployment.
    peer_member_refs: list[str]

    # Quorum for a peer attestation to count as "credentialed"
    quorum_size: int = 3
    quorum_independence_rule: Literal["disjoint_affiliations",
                                       "any_independent",
                                       "none"] = "disjoint_affiliations"

    # Trust degradation
    trust_cap: float = 0.7                   # peer-attestation-only
                                             # evidence caps trust here;
                                             # full credentialed
                                             # CredentialDirectoryRef
                                             # caps at 0.95.

    cataloged_at: datetime
    operator_verified: bool                  # operator confirmed pool
                                             # composition is reasonable
    signed_by: bytes
```

### A.33 ReplicatedAttestation and uplift schedule

<a id="appendix-a33"></a>

```python
@dataclass
class ReplicatedAttestation:
    schema: str = "replicated-attestation/1"
    replication_id: str
    base_claim_kind: str                    # resolves against KindRegistry.
                                            # fact_kinds — what kind of claim
                                            # is being replicated
    base_claim_ref: str                     # the original ProvenFact /
                                            # MeasurementFact / artifact

    # Each constituent attestation must be from disjoint sources per the
    # declared independence_check.  Substrate-shape independence rules;
    # not domain-shape.
    independence_check: Literal["disjoint_affiliations",
                                  "disjoint_funding_sources",
                                  "disjoint_geographic_regions",
                                  "blind_replication"]
    constituent_attestation_refs: list[str]  # ExternalAttestation refs
    constituent_count: int                   # = len(constituent_attestation_refs)

    # Numerical agreement (for MeasurementFact-backed claims).
    # The metric is the persona-proposed kind that quantifies agreement;
    # substrate names no metrics.  Examples (illustrative): "max_relative_
    # delta", "pairwise_chi_squared", "intersection_over_union".
    agreement_metric_kind: str               # KindRegistry-resolved
    agreement_value: float
    agreement_threshold: float               # kind-defined or operator-set
    agreement_pass: bool

    # Trust uplift schedule (substrate-shape table, not domain-shape).
    # Effective trust cap = base_peer_cap (0.7) + uplift_for(constituent_count,
    #                                                          independence_check)
    # Capped at 0.9 (still below credentialed 0.95) regardless of N.
    effective_trust_cap: float

    replicated_at: datetime
    drafted_by_persona_id: str
    signed_by: bytes
```

```text
constituent_count    disjoint_affiliations   blind_replication
─────────────────    ──────────────────────  ──────────────────
1 (no replication)   cap = 0.70 (PeerPool)   cap = 0.70
3                    cap = 0.80              cap = 0.85
5                    cap = 0.85              cap = 0.90
≥ 7                  cap = 0.85              cap = 0.90 (max)
```

### A.34 LongitudinalReputation

<a id="appendix-a34"></a>

```python
@dataclass
class LongitudinalReputation:
    schema: str = "longitudinal-reputation/1"
    reputation_id: str
    external_agent_id: str                  # the attestor
    domain_id: str                          # reputation is per-domain;
                                            # cross-domain transfer requires
                                            # 11_CROSS_DOMAIN_TRANSFER

    # Historical attestation outcomes
    historical_attestations: list[str]      # ExternalAttestation refs
    historical_count: int
    later_confirmed_count: int              # independent later check agreed
    later_contradicted_count: int           # later refuted by stronger evidence
    pending_count: int                      # not yet checked

    # Bayesian-updated track-record score, in [0, 1].
    # Persona proposes the update kernel; substrate provides no specific
    # Bayesian model.  rotation per INV-6 applies.
    track_record_score: float
    track_record_window: timedelta = timedelta(days=1825)  # default 5 years
    last_updated_at: datetime

    # Operator-tunable thresholds for quorum admissibility
    pool_admissibility_threshold: float = 0.5
    pool_high_weight_threshold: float = 0.8

    signed_by: bytes
```

```text
RULE  When evaluating peer quorum for a high-stakes attestation
      (physical_harm_class ≥ bodily_injury OR information_hazard_class
      ≥ dual_use_civilian), the PeerAttestationPool MAY require:
        ≥ quorum_size constituents whose LongitudinalReputation
        .track_record_score ≥ pool_admissibility_threshold.
      The requirement is per-pool, signed at pool creation; the
      operator may tighten or loosen.
```

### A.35 Ingestion seven-stage pipeline

<a id="appendix-a35"></a>

```text
STAGE 1: SOURCING
  persona invokes arxiv_search / google_scholar / web_fetch / ingest_pdf / etc.
  large blobs (>10MB) → content store

STAGE 2: PARSING + CHUNKING
  format-specific parsing (PDF → text+figures; HTML → semantic blocks;
                            LaTeX → math+prose)
  chunking 500-1500 tokens with overlap
  figures + tables extracted

STAGE 3: EMBEDDING + INDEXING
  domain-appropriate embedding model
  per-type indexes (text / formula / table / figure)
  graph extraction → Tier 2 graph nodes (hierarchical graph memory)

STAGE 4: PROVENANCE + LICENSING
  signed KnowledgeRef with:
    source URL/DOI, content_hash, ingested_at, license,
    access_rights, paywalled_flag, redistribution_allowed
  operator policy may restrict (e.g., refuse paywalled without licence)

STAGE 5: TAGGING
  seven-scope tags (user/persona/session/project/env/app/org)
  quality tag (peer_reviewed / preprint / unverified)
  domain_id (emergent or established)

STAGE 6: SAFETY CHECK
  OWASP LLM01 retrieval-admission filter
  content moderation
  rights check

STAGE 7: REGISTRATION
  signed KnowledgeRef added to corpus
  searchable via Knowledge tier retrieval
```

### A.36 KnowledgeIngestionRecord schema

<a id="appendix-a36"></a>

```python
@dataclass
class KnowledgeIngestionRecord:
    schema: str = "knowledge-ingestion/1"
    ingestion_id: str
    ingested_by_persona_id: str
    ingested_at: datetime
    
    source_kind: str                       # resolved against KindRegistry.
                                          # source_kinds (§7.6); never a
                                          # closed enum. Examples emerge
                                          # per domain: "paper", "datasheet",
                                          # "geotechnical_report",
                                          # "survey_plat", "permit_pdf",
                                          # "inspector_signoff", etc.
    source_ref: str
    source_publisher: str
    license: str
    paywalled: bool
    redistribution_allowed: bool
    content_hash: str
    
    parsed_chunks: int
    extracted_entities: int
    extracted_figures: int
    extracted_tables: int
    
    embedded_with: str
    indexed_into: list[str]
    
    domain_id: str
    persona_id: str
    quality_tag: str                       # resolves against KindRegistry.
                                          # quality_tag_kinds (§7.6); never
                                          # a closed enum. MetaRegistry seeds
                                          # (academic): "peer_reviewed",
                                          # "preprint", "unverified". Other
                                          # domains add per ProposedQualityKind
                                          # (e.g. "engineer_stamped",
                                          # "city_approved", "permit_issued",
                                          # "manufacturer_attested").
    
    publisher_attestation: str | None
    
    signed_by: bytes
```

### A.37 KnowledgeRef lifecycle FSM

<a id="appendix-a37"></a>

```text
┌───────────┐ just added; provenance score ~0.5; available for retrieval
│ INGESTED  │  but flagged as "new" in result metadata.
└─────┬─────┘
      ▼  ≥ 1 successful citation in completed work
┌───────────┐ persona has cited entry; provenance bumped; cited_in_traces[]
│   CITED   │  appended.
└─────┬─────┘
      ▼  cited successfully in K=3 distinct projects
┌───────────┐ multi-project reuse; provenance further increased; eligible
│  REUSED   │  for cross-project sharing per visibility tier (§6.3).
└─────┬─────┘
      ▼  promotion gate (operator-blessed or stage-thresholded)
┌───────────┐ entry is in DomainContext.standards_refs or equivalent
│ CANONICAL │  authoritative position; weighted 1.0 in retrieval.
└─────┬─────┘
      ▼  another KnowledgeRef cited as more recent/correct
┌────────────┐ demoted (not deleted); retrieval still possible but flagged;
│ SUPERSEDED │  superseded_by points to replacement.
└─────┬──────┘
      ▼  author or kernel marks obsolete
┌─────────────┐ not retrieved by default; only accessible via explicit
│ DEPRECATED  │  audit-mode query.
└─────┬───────┘
      ▼  license revocation or copyright issue
┌──────────┐ tombstoned; not retrievable; kept in archive for audit
│ REVOKED  │  (cannot be physically deleted — lineage preservation).
└──────────┘

PROMOTION SEMANTICS
  ▸ INGESTED → CITED:        first successful citation; auto.
  ▸ CITED → REUSED:           K=3 distinct projects; auto.
  ▸ REUSED → CANONICAL:       operator/curator action OR stage threshold.
  ▸ CANONICAL → SUPERSEDED:   newer KnowledgeRef preferred in K traces.
  ▸ any → DEPRECATED:         author/kernel/curator decision.
  ▸ any → REVOKED:            license/operator/legal trigger.

All transitions emit signed `KnowledgeRefTransition` events into the
DomainLineage; INV-J9 replay reconstructs full history.
```

### A.38 Cross-persona knowledge sharing visibility tiers

<a id="appendix-a38"></a>

```text
TIER 1 — persona_only
  Only the ingesting persona may retrieve. No cross-persona dedup.

TIER 2 — project_only
  Members of the originating project may retrieve; other projects in
  the same domain cannot.

TIER 3 — tenant (default for most ingestions)
  All personas within the same org_id / kernel may retrieve, scoped
  by domain_id + observation surface + charter.
  Under multi-principal attribution (01_KERNEL §2.4.3), an
  env binding two principals from DIFFERENT tenant_ids requires a
  signed CrossTenancyAgreementRef before a TIER 3 ingestion crosses
  the principal boundary; absent the agreement, the kernel demotes
  the visibility to TIER 1 / TIER 2 for the affected reader and emits
  CROSS_TENANT_VISIBILITY_DEMOTED to lineage.

TIER 4 — federation
  Federation-wide (multi-kernel) via A2A; subject to peer trust and
  operator policy.

TIER 5 — public
  Open access; requires operator gate (acknowledges public hosting,
  removes user/org tags).

DEFAULT POLICY
  Ingested KnowledgeRefs default to TIER 3 (tenant) unless the
  ingesting persona explicitly marks otherwise or operator policy
  restricts.

TOMBSTONING ON REVOCATION
  License revocation/paywall enforcement may require visibility
  collapse to TIER 1 + REVOKED stage. Retrievals receive a stub
  notice; original content preserved for audit.
```

### A.39 Federated knowledge lookup

<a id="appendix-a39"></a>

```text
SCENARIO: persona in kernel_X queries arxiv:1234.5678
   │
   ▼
1. local store lookup by content_hash → MISS
   │
   ▼
2. federated lookup via A2A:
     mcp__personaos__find_knowledge_federated(
         content_hash=...,
         source_ref="arxiv:1234.5678",
         max_peer_count=N,
         peer_trust_threshold=0.5)
   │
   ▼
3. peer kernel_Y has ingested → returns metadata + signed copy
   │
   ▼
4. local kernel verifies peer signature; adds shared KnowledgeRef
   pointer (not duplicating content; pointer + peer attestation)
   │
   ▼
5. trust merge:   shared_trust = min(local_trust, peer_trust)
```

### A.40 Ingestion toolkit

<a id="appendix-a40"></a>

```text
WEB / SEARCH
  arxiv_search                  google_scholar_search
  patent_search (uspto, epo)    web_search (general)
  wiki_search                   wikidata_query

INGESTION
  ingest_pdf                    ingest_html
  ingest_markdown               ingest_latex
  ingest_video_transcript       extract_figures
  extract_tables

GRAPH EXTRACTION
  extract_entities              extract_relationships
  graph_node_create

VALIDATION
  validate_license              check_paywall
  publisher_attestation_verify
```

### A.41 InferredVerifierRecipe schema and inference engine

<a id="appendix-a41"></a>

```python
@dataclass
class InferredVerifierRecipe:
    schema: str = "inferred-recipe/1"
    inference_id: str
    candidate_recipe_name: str
    domain_id: str
    
    inferred_from_traces: list[str]
    inferred_at: datetime
    confidence: float
    
    proposed_stages: list[VerifierStage]
    proposed_success_criteria: dict
    
    holdout_test_passed: bool
    holdout_count: int
    
    stage: Literal["candidate", "trial", "accepted", "rejected"]
    co_signing_personas: list[str]
    
    signed_by: bytes
```

```python
def infer_verifier_recipes(domain_id, recent_traces):
    for artifact_kind in set(t.artifact_kind for t in recent_traces):
        traces = [t for t in recent_traces 
                  if t.artifact_kind == artifact_kind
                  and t.task_class == "VERIFIER_ACCEPT"]
        if len(traces) < 3:
            continue
        common_tools = find_common_tools(traces)
        common_outcomes = find_common_outcomes(traces)
        if pattern_consistency(common_tools, common_outcomes) > 0.8:
            recipe = InferredVerifierRecipe(...)
            holdout = sample_holdout_traces(domain_id, artifact_kind)
            if validate_recipe(recipe, holdout):
                recipe.stage = "trial"
                recipe.holdout_test_passed = True
            sign_and_register(recipe)
```

### A.42 ProposedSafetyExtension schema

<a id="appendix-a42"></a>

```python
@dataclass
class ProposedSafetyExtension:
    schema: str = "safety-extension-proposal/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str
    
    extension_name: str
    claim_pattern: str
    required_tool: str
    required_outcome: str
    timing: Literal["before_action", "after_action", "both"]
    failure_action: Literal["refuse_action", "warn_and_log",
                            "escalate_operator"]
    rationale: str
    
    evidence_refs: list[str]
    historical_traces: list[str]
    
    safety_critical: bool                 # if True: operator gate
    
    stage: Literal["candidate", "trial", "operator_review",
                    "accepted", "rejected"]
    co_signing_personas: list[str]
    operator_approval: bool | None
    operator_approval_signed_by: bytes | None
    
    signed_by: bytes
```

### A.43 Physical-hazard kind seeds

<a id="appendix-a43"></a>

```yaml
# MetaRegistry physical_hazard_kinds seed bundle (release data)
# All entries enter as STANDARDISED kinds in MetaRegistry; operator may
# promote, demote, or revoke any of them.  These are NOT in substrate code.

- kind_id: cryogenic_exposure
  hazard_axes:
    physical_harm_class: bodily_injury
  proposed_safety_extension_template:
    claim_pattern: action_touches(cryogenic_equipment)
    required_tool: cryo_ppe_checklist_completed
    required_outcome: ppe_attested
    timing: before_action
    failure_action: refuse_action

- kind_id: rf_exposure
  hazard_axes:
    physical_harm_class: bodily_injury

- kind_id: high_voltage_arc
  hazard_axes:
    physical_harm_class: fatality_risk

- kind_id: ionizing_radiation
  hazard_axes:
    physical_harm_class: bodily_injury
    information_hazard_class: dual_use_civilian

- kind_id: laser_eye_safety_class_3b_or_4
  hazard_axes:
    physical_harm_class: bodily_injury

- kind_id: vacuum_implosion_risk
  hazard_axes:
    physical_harm_class: bodily_injury

- kind_id: hazmat_chemical_exposure
  hazard_axes:
    physical_harm_class: bodily_injury

- kind_id: biocontainment_breach
  hazard_axes:
    physical_harm_class: fatality_risk
    information_hazard_class: dual_use_civilian

- kind_id: heavy_machinery_pinch_or_crush
  hazard_axes:
    physical_harm_class: bodily_injury

- kind_id: confined_space_asphyxiation
  hazard_axes:
    physical_harm_class: fatality_risk
```

### A.44 ProposedConvention schema

<a id="appendix-a44"></a>

```python
@dataclass
class ProposedConvention:
    schema: str = "proposed-convention/1"
    proposal_id: str
    domain_id: str
    
    symbol: str
    meaning: str
    formal_definition: str | None
    scope: Literal["domain_default", "project_specific"]
    
    proposed_by_persona_id: str
    proposed_at: datetime
    co_signing_personas: list[str]
    usage_count: int
    
    stage: Literal["emergent", "recognised", "authoritative",
                    "standardised", "deprecated"]
    superseded_by: str | None
    
    signed_by: bytes
```

### A.45 Convention ambiguity and reconciliation

<a id="appendix-a45"></a>

```text
DETECTION
  ▸ two personas in the same project use different symbols for what
    appears to be the same concept (cosine similarity between
    meanings ≥ 0.85) AND no convention has been adopted.
  ▸ kernel emits CONVENTION_AMBIGUITY{ symbol_a, symbol_b, persona_a,
    persona_b, evidence_refs }.

RESOLUTION FLOW
  1. Probe extended (if active) OR new probe spawned (Signal E).
  2. DomainCurator (or kernel if none) reviews candidate symbols +
     ingested literature to pick canonical form.
  3. Kernel emits CONVENTION_RECONCILIATION_PROPOSAL with:
        - canonical_symbol, canonical_meaning
        - superseded_symbols[] (with alias mapping)
        - rationale + evidence_refs
  4. Originating personas co-sign or contest.
  5. On co-sign: emit CONVENTION_ADOPTED; alias mapping recorded so
     legacy outputs remain readable.
  6. On contest: DomainCurator escalates to operator (or holds at
     EMERGENT stage pending more evidence).

NOTATION_CONFLICT remains for hard disagreements (different meanings
on same symbol). NOTATION_SCOPE_CONFLICT (§2.3) covers cross-domain
collision in multi-domain personas.
```

### A.46 StandardRef schema

<a id="appendix-a46"></a>

```python
@dataclass
class StandardRef:
    schema: str = "standard-ref/1"
    standard_id: str                      # IEEE_1641-2010, IEC_62368-1, etc.
    title: str
    publisher: str                        # IEEE, ISO, ACM, IEC, etc.
    version: str
    licence: Literal["public", "paid", "restricted"]
    access_method: str                    # "fetch_url", "operator_provided",
                                          # "not_ingested"
    relevance: Literal["high", "medium", "low"]
    cataloged_by_persona_id: str
    cataloged_at: datetime
    operator_verified: bool
    signed_by: bytes
```

### A.47 Emergent kind proposal schemas (Proposed*Kind)

<a id="appendix-a47"></a>

```python
@dataclass
class ProposedMediaKind:
    schema: str = "proposed-media-kind/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    kind: str                              # e.g. "floor_plan", "gantt_schedule",
                                          #      "ifc_model", "site_survey"
    description: str
    mime_types: list[str]                  # accepted MIME(s)
    storage_class: Literal["inline", "stored", "external"]
    edit_semantics: Literal["text_crdt", "structured_crdt",
                             "version_chain", "none"]
                                          # which substrate CRDT class
                                          # applies (07_ARTIFACTS §5.1).
                                          # "none" disables co-editing
                                          # (single-author appends only).
    introspection_adapter_id: str | None   # tool that can read the format;
                                          # discovered via §5 or authored §5.4
    rendering_adapter_id: str | None       # optional renderer for visual view
    verifier_hooks: list[str]              # recipe ids this kind supports
    cross_domain_promotable: bool          # may rise to MetaRegistry
    rationale: str
    evidence_refs: list[str]

    stage: Literal["candidate", "trial", "accepted", "rejected"]
    co_signing_personas: list[str]

    signed_by: bytes


@dataclass
class ProposedSourceKind:
    schema: str = "proposed-source-kind/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    kind: str                              # e.g. "geotechnical_report",
                                          #      "permit_pdf", "survey_plat",
                                          #      "inspector_signoff"
    description: str
    parsing_adapter_id: str | None         # ingestion pipeline §6 entry
    default_visibility: Literal["persona_only", "project_only",
                                 "tenant", "federation", "public"]
    default_quality_tag: str               # registered fact-kind / quality tag
    retention_hint: Literal["corpus", "project_only_one_off",
                             "session_only"]
    rationale: str
    evidence_refs: list[str]

    stage: Literal["candidate", "trial", "accepted", "rejected"]
    co_signing_personas: list[str]

    signed_by: bytes


@dataclass
class ProposedVerifierKind:
    schema: str = "proposed-verifier-kind/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    kind: str                              # e.g. "physical_inspection",
                                          #      "human_attestation",
                                          #      "field_measurement"
    description: str
    cascade_position: Literal["before_schema", "between_schema_and_sandbox",
                               "between_sandbox_and_invariant",
                               "between_invariant_and_policy",
                               "after_policy"]
    attestor_class: str | None             # e.g. "external_human_with_signed_role"
    evidence_kinds: list[str]              # references KindRegistry media_kinds
    failure_action: Literal["reject", "warn_and_log", "escalate_operator"]
    rationale: str
    evidence_refs: list[str]

    safety_critical: bool
    operator_approval: bool | None
    operator_approval_signed_by: bytes | None

    stage: Literal["candidate", "trial", "operator_review",
                    "accepted", "rejected"]
    co_signing_personas: list[str]

    signed_by: bytes


@dataclass
class ProposedCapabilityKind:
    schema: str = "proposed-capability-kind/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    kind: str                              # e.g. "permit_filing",
                                          #      "inspection_request",
                                          #      "contractor_dispatch",
                                          #      "instrument_link"
    description: str
    bridge_pattern: str                    # how the BridgeAsset is shaped
                                          # (account_link, form_submission,
                                          # credential_holder, ...)
    expected_recurrence: Literal["one_time", "rare_refresh",
                                  "session_per_use"]
    validation_period_default: str         # ISO 8601 duration default
    rationale: str
    evidence_refs: list[str]

    safety_critical: bool
    operator_approval: bool | None
    operator_approval_signed_by: bytes | None

    stage: Literal["candidate", "trial", "operator_review",
                    "accepted", "rejected"]
    co_signing_personas: list[str]

    signed_by: bytes


@dataclass
class ProposedContributionKind:
    schema: str = "proposed-contribution-kind/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    kind: str                              # e.g. "code_compliance_check",
                                          #      "site_survey_authored",
                                          #      "definition", "lemma"
    description: str
    weight_default: float                  # credit weight in InternalCredit
    rationale: str
    evidence_refs: list[str]

    stage: Literal["candidate", "trial", "accepted", "rejected"]
    co_signing_personas: list[str]

    signed_by: bytes


@dataclass
class ProposedItemKind:
    schema: str = "proposed-item-kind/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    kind: str                              # e.g. "conjecture" (math),
                                          #      "proof_attempt" (math),
                                          #      "proof_gap" (math),
                                          #      "design_hypothesis" (construction),
                                          #      "buildability_concern" (construction),
                                          #      "case_study" (research),
                                          #      "patient_episode" (clinical)
    description: str
    payload_schema: dict                   # JSONSchema for kind-specific
                                          # fields beyond ProjectItem core
    status_fsm: list[str]                  # ordered status names; first is
                                          # initial; terminal members
                                          # signalled by trailing "!"
    advance_signal_hooks: list[str]        # signals that move status forward
                                          # (e.g. "verifier_pass",
                                          # "external_attestation_received")
    rationale: str
    evidence_refs: list[str]

    stage: Literal["candidate", "trial", "accepted", "rejected"]
    co_signing_personas: list[str]

    signed_by: bytes


@dataclass
class ProposedOutcomeKind:
    schema: str = "proposed-outcome-kind/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    kind: str                              # e.g. "citation_observation",
                                          #      "community_uptake",
                                          #      "production_telemetry",
                                          #      "test_results",
                                          #      "regulatory_outcome",
                                          #      "building_inspection",
                                          #      "contractor_work_log",
                                          #      "material_delivery"
    description: str
    payload_schema: dict                   # JSONSchema for outcome payload
    arrival_modes: list[str]               # how the outcome arrives
                                          # (e.g. "external_webhook",
                                          # "scheduled_pull",
                                          # "operator_upload",
                                          # "human_bridged_pdf")
    requires_external_attestation: bool    # if True, evidence must include
                                          # a signed ExternalAttestation ref
    requires_corroboration: bool
    rationale: str
    evidence_refs: list[str]

    stage: Literal["candidate", "trial", "accepted", "rejected"]
    co_signing_personas: list[str]

    signed_by: bytes


@dataclass
class ProposedQualityKind:
    schema: str = "proposed-quality-kind/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    kind: str                              # e.g. "peer_reviewed", "preprint",
                                          #      "unverified", "engineer_stamped",
                                          #      "city_approved", "permit_issued",
                                          #      "manufacturer_attested"
    description: str
    rank: int                              # used for retrieval-time
                                          # provenance weighting
                                          # (lower = lower trust)
    requires_external_attestation: bool
    rationale: str
    evidence_refs: list[str]

    stage: Literal["candidate", "trial", "accepted", "rejected"]
    co_signing_personas: list[str]

    signed_by: bytes


@dataclass
class ProposedFactKind:
    schema: str = "proposed-fact-kind/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    kind: str                              # e.g. "convention",
                                          #      "policy_in_force",
                                          #      "infrastructure_state",
                                          #      "shared_understanding",
                                          #      "historical_fact",
                                          #      "site_constraint",
                                          #      "occupancy_limit"
    description: str
    scope: Literal["env", "project", "domain"]
    transferable_across_envs: bool
    rationale: str
    evidence_refs: list[str]

    stage: Literal["candidate", "trial", "accepted", "rejected"]
    co_signing_personas: list[str]

    signed_by: bytes


@dataclass
class ProposedBundleKind:
    schema: str = "proposed-bundle-kind/1"
    proposal_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    kind: str                              # e.g. "smps_design", "math_paper",
                                          #      "code_change", "research_report",
                                          #      "course_module",
                                          #      "policy_document",
                                          #      "home_design_package",
                                          #      "patient_care_plan"
    description: str
    expected_artifact_kinds: list[str]     # which media_kinds usually compose
                                          # the bundle (resolved against
                                          # KindRegistry.media_kinds)
    expected_outcome_kinds: list[str]      # which outcome_kinds the bundle
                                          # collects (resolved against
                                          # KindRegistry.outcome_kinds)
    expected_attestation_kinds: list[str]  # external attestation classes the
                                          # bundle requires for acceptance
                                          # (resolved against
                                          # KindRegistry.contribution_kinds)
    rationale: str
    evidence_refs: list[str]

    stage: Literal["candidate", "trial", "accepted", "rejected"]
    co_signing_personas: list[str]

    signed_by: bytes
```

### A.48 KindRegistry, MediaKindEntry, resolution rule, and MetaRegistry promotion

<a id="appendix-a48"></a>

```python
@dataclass
class KindRegistry:
    schema: str = "kind-registry/1"
    registry_id: str
    domain_id: str | None                  # None = MetaRegistry
                                          # (cross-domain STANDARDISED)
    version: int

    media_kinds:        dict[str, MediaKindEntry]
    source_kinds:       dict[str, SourceKindEntry]
    verifier_kinds:     dict[str, VerifierKindEntry]
    capability_kinds:   dict[str, CapabilityKindEntry]
    contribution_kinds: dict[str, ContributionKindEntry]
    fact_kinds:         dict[str, FactKindEntry]
    bundle_kinds:       dict[str, BundleKindEntry]
    item_kinds:         dict[str, ItemKindEntry]
    outcome_kinds:      dict[str, OutcomeKindEntry]
    quality_tag_kinds:  dict[str, QualityKindEntry]
    task_class_kinds:        dict[str, TaskClassKindEntry]        # ADR-0066
    acceptance_pathway_kinds: dict[str, AcceptancePathwayKindEntry]  # ADR-0066

    last_updated_at: datetime
    signed_by: bytes


@dataclass
class MediaKindEntry:
    schema: str = "media-kind/1"
    kind: str                              # key in KindRegistry.media_kinds
    description: str
    mime_types: list[str]
    storage_class: Literal["inline", "stored", "external"]
    edit_semantics: Literal["text_crdt", "structured_crdt",
                             "version_chain", "none"]
    introspection_adapter_id: str | None
    rendering_adapter_id: str | None
    verifier_hooks: list[str]
    stage: Literal["emergent", "recognised", "authoritative", "standardised"]
    trust_score: float
    proposed_by_persona_id: str
    proposed_at: datetime
    co_signing_personas: list[str]
    used_in_projects: list[str]
    promotion_history: list[PromotionEvent]
    cross_domain_promotable: bool
    signed_by: bytes


# SourceKindEntry, VerifierKindEntry, CapabilityKindEntry,
# ContributionKindEntry, FactKindEntry, BundleKindEntry follow the same
# shape: the proposal payload + stage + trust_score + promotion_history +
# usage tracking. Detailed schemas elided for brevity; each mirrors
# MediaKindEntry's fields plus its kind-class-specific resolved fields
# from the matching ProposedXKind.
#
# TaskClassKindEntry and AcceptancePathwayKindEntry (ADR-0066) mirror the
# same shape. AcceptancePathwayKindEntry additionally carries:
#   pathway_trust: float          # asymmetric-EWMA verdict trust (03_TASKS §2b.1)
#   safety_critical: bool         # C2 blocking gate at EMERGENT->RECOGNISED
#   reference_pathway_id: str | None  # seed pathway used for shadow agreement
# Its stage promotes/demotes on the §2b acceptance-soundness ladder, not on
# usage volume alone: EMERGENT->RECOGNISED requires independent-reference
# agreement >= 0.90 with zero unreviewed false-accepts (03_TASKS §2b.2),
# and demotes on trust collapse or N=3 consecutive disconfirmations
# (03_TASKS §2b.3).
```

```text
RESOLVE(kind_name, domain_id):
    if domain_id is not None:
        entry = KindRegistry[domain_id].lookup(kind_name)
        if entry: return entry
    entry = MetaRegistry.lookup(kind_name)
    if entry: return entry
    raise UnknownKind(kind_name, domain_id)

UnknownKind triggers DOMAIN_UNKNOWN_DETECTED Signal G
(kind_unknown_for_domain) → probe extension → ProposedXKind drafted.
```

```text
A kind reaches STANDARDISED in its origin domain. If
cross_domain_promotable=True AND it has been cited successfully in
≥ K projects across ≥ M distinct domains (defaults K=5, M=2), kernel
emits KIND_META_PROMOTION_PROPOSAL → operator signs → entry copied
into MetaRegistry with the union of contributing co-signers.

Once in MetaRegistry, the kind is available to every domain WITHOUT
re-proposal. A new home-construction project starting after
`floor_plan` reaches MetaRegistry simply uses it.

Demotion: drift detection (§3.1) may demote a MetaRegistry entry back
to per-domain RECOGNISED if its semantics fork across domains.
```

### A.49 KindRegistryEntry schema

<a id="appendix-a49"></a>

```python
@dataclass
class KindRegistryEntry:
    schema: str = "kind-registry-entry/1"
    entry_id: str
    domain_id: str | None                    # None = MetaRegistry (cross-domain)

    kind_family: str                         # "phase_kinds", "payment_method_kinds",
                                             # "instrument_kinds", "quantity_kinds",
                                             # "media_kinds", "source_kinds",
                                             # "contribution_kinds", ...
                                             # (substrate-shape family names; the
                                             # families themselves are open per C4
                                             # — operator may register new families
                                             # via signed kind_family_registration)
    kind_id: str                             # the kind name within the family
                                             # (KindRegistry-resolved, domain-shape)

    stage: Literal["candidate", "emergent", "recognised",
                    "authoritative", "standardised", "deprecated"]
    promoted_to_metaregistry: bool

    # Per-family metadata. Validated against the family's declared schema.
    # See §7.6.2 for the registered metadata schemas per family.
    metadata: dict

    co_signing_personas: list[str]
    cataloged_at: datetime
    last_promotion_event_id: str | None
    signed_by: bytes
```

### A.50 Per-family metadata schemas

<a id="appendix-a50"></a>

```text
KIND FAMILY            METADATA FIELDS                                    USED BY
─────────────────      ─────────────────────────────────────────────      ─────────────────────
phase_kinds            stall_evaluator_suppressed:   bool                 ProjectPhaseState
                       requires_user_sign:           bool                 (04_PROJECT §26a.6)
                       expected_duration_default:    timedelta
                       suppression_rationale_kind:   str (free text)
                       overdue_severity_curve:       dict (optional)

payment_method_kinds   requires_human_authorisation: bool (always True
                                                         for Class E)     PaymentBridge
                       receipt_latency_typical:     timedelta             (04_PROJECT §26a.4.1)
                       audit_trail_kind:            str

instrument_kinds       operational_state_kind_ref:  str (FSM identifier) InstrumentAsset
                       default_calibration_interval: timedelta            (04_PROJECT §26a.7)
                       systematic_floor_default:    float | None
                       reference_chain_root_kind:   str | None

quantity_kinds         units_kind:                  str                   MeasurementFact
                       physical_dimension:          str (M L T...)        (08_KNOWLEDGE §16a)
                       typical_distribution_kind:   str (gaussian / ...)
                       conventional_uncertainty:    float | None

phase_kinds(seed)      Bootstrap entries for release:
                       - "design"                  stall=False, user_sign=False
                       - "verification"            stall=False, user_sign=False
                       - "external_dependency_wait" stall=True,  user_sign=False
                       - "physical_fabrication"    stall=True,  user_sign=True (entry)
                       - "peer_review_pending"     stall=True,  user_sign=False
                       - "regulatory_review"       stall=True,  user_sign=True (exit)
                       - "iteration"               stall=False, user_sign=False
                       - "synthesis"               stall=False, user_sign=False
                       (All MetaRegistry STANDARDISED at release;
                       operator may demote per deployment.)
```

### A.51 Cross-source validation checks

<a id="appendix-a51"></a>

```text
1. CROSS-TRACE CONSISTENCY
   Does inferred recipe match held-out trace outcomes?

2. CROSS-PERSONA AGREEMENT
   Multiple personas independently arriving at similar inferences?

3. CROSS-DOMAIN CONSISTENCY
   Does proposal contradict existing convention in related domain?

4. CHARTER CONSISTENCY
   Does proposed extension violate any persona's charter when applied?

5. OPERATOR POLICY CONSISTENCY
   Does proposal violate deployment policy?
```

### A.52 ProposalQueue schema

<a id="appendix-a52"></a>

```python
@dataclass
class ProposalQueue:
    schema: str = "proposal-queue/1"
    queue_id: str
    domain_id: str
    pending_proposals: list[Proposal]
    accepted_proposals: list[Proposal]
    rejected_proposals: list[Proposal]
    requires_operator_review: list[Proposal]
    review_frequency: timedelta            # default weekly
    last_review_at: datetime
```

### A.53 Rate-limits and convergence detection

<a id="appendix-a53"></a>

```text
RATE LIMITS
  ▸ per persona per session:        max K=10 proposals BASELINE
    (prevents spamming a probe with low-value proposals).
  ▸ per persona per month per domain: operator-tunable cap.
  ▸ exceeding limit emits PROPOSAL_RATE_LIMITED; further proposals
    held in pending until next window.

COLD-START SCALING (— §9.1.1):
  ▸ Baseline K=10 is calibrated for steady-state emergence in a
    populated domain.  For a freshly-recognised DomainContext where
    KindRegistry.size == 0 at start-of-session, the effective cap
    scales with ingested-evidence volume in the same session.
  ▸ The scaling factor is substrate-shape (measures evidence count,
    not what the evidence is about); see §9.1.1.

CONVERGENCE DETECTION
  When N≥2 personas independently propose proposals close in semantic
  space (embedding cosine ≥ 0.85; same artifact_kind / claim_pattern /
  symbol), the kernel emits:

    PROPOSAL_CONVERGENCE_DETECTED {
        domain_id,
        proposal_ids: [p1, p2, ...],
        proposed_personas: [...],
        similarity: 0.91,
        merge_candidate: {
            unified_name,
            unified_stages_or_pattern,
            co_signers: [union of originating personas],
        },
    }

MERGE OFFER FLOW
  1. Originating personas notified with the merge_candidate.
  2. Each MAY co-sign or contest.
  3. ≥ 2 co-signs → merged proposal supersedes originals
     (originals marked `consolidated_into` and retired).
  4. < 2 co-signs → originals remain independent in the queue.
  5. Merged proposal carries combined evidence + co-signing
     across personas, giving it stronger promotion candidacy.
```

### A.54 ColdStartProposalCalibration, BulkKindProposal, and admission flow

<a id="appendix-a54"></a>

```python
@dataclass
class ColdStartProposalCalibration:
    schema: str = "cold-start-proposal-calibration/1"
    domain_id: str

    baseline_per_session_cap: int = 10         # K from §9.1
    cold_start_active_when_registry_size_lte: int = 0  # default: only when empty
    scaling_fn: Literal["none", "log2", "sqrt", "linear_capped"] = "log2"

    # Inputs to the scaling function — all substrate-shape counts.
    # The function reads kernel-tracked counters, never inspects content.
    #   N_ingested      = KnowledgeIngestionRecord entries this session,
    #                     domain-scoped
    #   N_standards     = StandardRef entries this session, domain-scoped
    #   N_sessions_in   = sessions persona has spent in this domain
    #
    # Effective cap:
    #   K_effective = baseline
    #               + scaling_fn(N_ingested + α·N_standards)
    #               × decay(N_sessions_in)
    #
    # decay reduces uplift as the domain matures: cold-start uplift fades
    # to zero once the registry is no longer empty (§9.1.1 admission).
    alpha_standards_weight: float = 2.0        # standards count more than
                                              # arbitrary refs (denser evidence)
    decay_kind: Literal["step", "linear", "exponential"] = "step"
    max_uplift: int = 200                       # hard ceiling on K_effective

    operator_overridable: bool = True
    safety_critical_multiplier: float = 0.5    # tighter, not looser, when
                                              # owning DomainContext has
                                              # physical_harm_class ≥
                                              # bodily_injury OR
                                              # information_hazard_class ≥
                                              # dual_use_civilian


@dataclass
class BulkKindProposal:
    schema: str = "bulk-kind-proposal/1"
    bulk_id: str
    domain_id: str
    drafted_by_persona_id: str
    drafted_at: datetime

    # The ingestion source that justifies the bundle.  All kinds in
    # member_proposal_ids must cite this source as primary evidence.
    # Substrate-shape: the field declares ingestion-provenance, not
    # what the source teaches.
    primary_evidence_ref: str                  # KnowledgeIngestionRecord id
                                              # OR StandardRef id
    primary_evidence_content_hash: str         # binds the bundle to the
                                              # exact source bytes; rotation
                                              # of source invalidates bundle

    member_proposal_ids: list[str]             # Proposed*Kind ids included
    member_kinds_summary: dict[str, int]       # {"media_kind": 4,
                                              #  "verifier_kind": 12,
                                              #  "contribution_kind": 7, ...}

    # Accounting against the cold-start cap (§9.1.1 admission):
    #   each BulkKindProposal counts as 1 proposal against
    #   per-session-cap; member proposals count individually against
    #   per-month cap and against PROPOSAL_CONVERGENCE_DETECTED scanning.
    #   This is what permits high-volume bootstrap without spam.
    counts_as_single_session_proposal: bool = True

    # Bundles still pass cross-source validation (§8): the kernel runs
    # validation per-member; on first member failure the entire bundle is
    # held pending with a per-member status map.
    member_validation_status: dict[str, Literal[
        "pending", "validated", "held", "rejected"]]

    signed_by: bytes
```

```text
On Proposed*Kind draft inside a probe session:
  1. Resolve owning DomainContext; read its ColdStartProposalCalibration.
  2. If KindRegistry.size > cold_start_active_when_registry_size_lte:
        K_effective = baseline_per_session_cap            (steady-state)
     Else:
        K_effective = baseline
                    + scaling_fn(N_ingested + α·N_standards)
        K_effective = min(K_effective, max_uplift)
        Apply safety_critical_multiplier if hazard axes trip (§2).
  3. Compare session.proposal_count vs K_effective.
     If under: admit.  Emit COLD_START_UPLIFT_APPLIED on first uplift this
     session.
     If at: emit PROPOSAL_RATE_LIMITED as before.

On BulkKindProposal draft:
  1. Verify primary_evidence_content_hash matches the cited source.
  2. For each member proposal: run cross-source validation (§8) as
     usual.  Per-member rejection does not block the bundle; status map
     records each.
  3. Charge 1 session-proposal slot against K_effective.
  4. Sign the bundle envelope; sign each member.  Emit
     BULK_KIND_PROPOSAL_SIGNED with member count by kind.
```

### A.55 DomainCuratorRole schema

<a id="appendix-a55"></a>

```python
@dataclass
class DomainCuratorRole:
    schema: str = "domain-curator-role/1"
    persona_id: str
    domain_id: str
    appointed_at: datetime
    appointed_by: str                     # operator or kernel
    
    may_propose_consolidations: bool
    may_review_promotions: bool
    may_propose_demotions: bool
    may_reconcile_conflicts: bool
    
    cannot_unilaterally_promote_to_authoritative: bool  # always True
    cannot_self_sign_consolidations: bool  # always True
    
    signed_by: bytes
```

### A.56 CrossDomainTransfer schema

<a id="appendix-a56"></a>

```python
@dataclass
class CrossDomainTransfer:
    schema: str = "cross-domain-transfer/1"
    transfer_id: str
    transferred_at: datetime
    
    artifact_type: str                     # resolved against KindRegistry
                                          # (§7.6); transfers may carry any
                                          # registered kind (skill,
                                          # convention, lesson, verifier
                                          # recipe, media kind, capability
                                          # kind, etc.) so long as the kind
                                          # itself is registered in both
                                          # source and target domains or
                                          # in the MetaRegistry.
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

### A.57 Anti-leakage risks

<a id="appendix-a57"></a>

```text
RISK A — User-specific data
  Persona's memory of user U's preferences in domain A → NOT transferred
  to domain B without explicit user consent.
  Mitigation: user_id scope tag blocks.

RISK B — Org-specific data
  Notes about Acme's process in domain A → not transferred to non-Acme
  context.
  Mitigation: org_id scope tag blocks.

RISK C — Project-specific data
  Project secrets must not leak across domains.
  Mitigation: project_id scope tag blocks.

RISK D — IP / Patent
  Proprietary IP cannot become canonical domain knowledge without
  authorization.
  Mitigation: operator policy + IP_sensitive flag + operator review
  for proprietary cross-domain transfer.

RISK E — Cross-org transfer
  Skills learned with one org's data may carry implicit info.
  Mitigation: org_share_policy per artifact; operator gate cross-org.
  For multi-principal envs, DerivationProvenanceEdge
  (08_KNOWLEDGE §16b) covers the dual case: implicit derivation
  during normal retrieval, where RISK E's per-artifact policy
  has no artifact to act on.  The two mitigations compose: RISK E
  for explicit transfer; DPE for implicit derivation.
```

### A.58 DomainPrecedentImport schema and admission rule

<a id="appendix-a58"></a>

```python
@dataclass
class DomainPrecedentImport:
    schema: str = "domain-precedent-import/1"
    import_id: str
    target_domain_id: str
    precedent_domain_id: str
    imported_at: datetime
    imported_by_persona_id: str

    # WHICH kinds are imported.  Substrate-shape: list of kind-class names
    # that are themselves substrate categories (media_kind, source_kind,
    # verifier_kind, capability_kind, contribution_kind, item_kind,
    # outcome_kind, ownership_kind, tranche_kind, convention,
    # safety_extension, standard_ref).  No specific kind names appear in
    # the substrate.
    imported_kind_classes: list[str]

    # Optional whitelist / blacklist of specific entries inside each
    # imported class.  Persona-supplied filter, not substrate enum.
    include_only: dict[str, list[str]] | None   # {"verifier_kind": [...]}
    exclude: dict[str, list[str]] | None

    # KINSHIP EVIDENCE — what makes precedent_domain_id a valid prior for
    # target_domain_id.  All three are substrate-shape:
    #   evidence_overlap_count = number of KnowledgeRefs cited by both
    #                            domains (kernel-computed from content_hash
    #                            intersection)
    #   structural_kinship     = cosine similarity of the two domains'
    #                            kind-distributions (kernel-computed)
    #   declared_parent_ref    = if non-null, target declares precedent
    #                            as parent in §2.3 hierarchy
    evidence_overlap_count: int
    structural_kinship_score: float            # 0..1
    declared_parent_ref: str | None

    # NON-PRINCIPAL KINSHIP ATTESTATION — required when the import targets
    # a safety-critical DomainContext OR when the principal_topology is
    # operator_is_user (01_KERNEL §2.4).  The attestor must be an
    # ExternalAgent whose credential is disjoint from the principal AND
    # whose contribution_kind is registered in BOTH source and target
    # domains' KindRegistry (so the attestor is credentialled in the
    # field, not merely a generic witness).
    kinship_attestation_ref: str | None        # ExternalAttestation id

    # TRUST DISCOUNT — substrate-shape.  Imported entries receive
    #   import_trust = source_trust × discount_factor
    # where discount_factor combines the three kinship axes:
    #   base = 0.5
    #   bonus = 0.1 × min(1, evidence_overlap_count / N_overlap_threshold)
    #         + 0.2 × structural_kinship_score
    #         + 0.1 × (1.0 if declared_parent_ref else 0.0)
    #         + 0.1 × (1.0 if kinship_attestation_ref else 0.0)
    #   discount_factor = base + bonus               # capped at 0.95
    discount_factor: float                     # kernel-computed at draft

    # PROBATION — imported entries start at stage = "emergent" in target
    # regardless of source stage; they may promote to RECOGNISED only
    # after target-domain probationary uses (default K=2) succeed.  This
    # forbids cross-domain trust laundering: importing AUTHORITATIVE
    # entries does NOT make them AUTHORITATIVE in target.
    probationary_target_uses_required: int = 2
    target_uses_so_far: int = 0
    target_use_outcome_log: list[str]          # OutcomeFeedback refs

    # ANTI-LEAKAGE — §11.1 mitigations all apply.  Additionally, the
    # imported_kind_classes list must not contain user_id-tagged,
    # org_id-tagged, project_id-tagged, or IP_sensitive entries from
    # the source domain; the kernel filters at import time.
    leakage_filter_report: dict                # counts filtered per RISK A-E

    state: Literal["drafted", "attested", "active",
                    "probation_complete", "revoked"]
    signed_by: bytes
```

```text
On DomainPrecedentImport.draft:
  1. Resolve precedent and target DomainContexts; both must exist.
  2. Compute evidence_overlap_count and structural_kinship_score from
     kernel state (no persona claim allowed for these).
  3. If target.hazard axes trip safety_critical OR principal_topology =
     operator_is_user: kinship_attestation_ref REQUIRED; reject draft
     without it.
  4. Apply §11.1 anti-leakage filter to every entry resolved through
     imported_kind_classes / include_only.
  5. Compute discount_factor; reject if < 0.3 (kinship too thin).
  6. Sign the import; mark imported entries with import_id and
     trust = source_trust × discount_factor.
  7. Emit DOMAIN_PRECEDENT_IMPORT_DRAFTED + per-entry
     PRECEDENT_ENTRY_LINKED.

On each target-domain use of an imported entry:
  1. Run the entry as native; record outcome in OutcomeFeedback.
  2. If outcome class advances target task (per task class acceptance
     pathway, J4): target_uses_so_far += 1.
  3. When target_uses_so_far >= probationary_target_uses_required:
     entry transitions from "imported" probation to native EMERGENT
     in target domain; subsequent promotion follows target's
     PromotionPolicy (§3.1).

On any target-domain use that FAILS verification at the imported
entry's tier: emit PRECEDENT_ENTRY_FAILED; target_uses_so_far resets
to zero; after 3 cumulative failures the import is REVOKED for that
entry (rest of bundle retained).
```

### A.59 Demotion triggers and DemotionEvent schema

<a id="appendix-a59"></a>

```text
TRIGGERS:
1. Conformance audit finds entry conflicts with recent outcomes.
2. Drift in usage: trust 0.85 → 0.5 over recent sessions.
3. External revocation: paper retracted, tool deprecated, etc.
4. Charter drift: entry pushing persona toward charter-violation.
5. Operator decision: explicit revocation.

FLOW:
  AUTHORITATIVE → RECOGNISED (with reason)
  RECOGNISED → EMERGENT
  EMERGENT → DEPRECATED (tombstone candidate)
  
REVOCATION (only for STANDARDISED):
  STANDARDISED → DEPRECATED (with corrective action plan; operator signed)

COMPLETE REMOVAL:
  Tombstoning: removed from active retrieval; kept in archive for audit.
  Cannot be physically deleted (lineage preservation).
```

```python
@dataclass
class DemotionEvent:
    schema: str = "demotion-event/1"
    event_id: str
    domain_id: str
    artifact_ref: str
    from_stage: str
    to_stage: str
    reason: str
    triggered_by: Literal["audit", "drift_detected",
                           "external_revocation", "charter_drift",
                           "operator_action"]
    triggered_at: datetime
    corrective_action: str | None
    operator_signed: bool
    signed_by: bytes
```

### A.60 Dormant domain lifecycle FSM

<a id="appendix-a60"></a>

```text
┌────────┐  no probe, proposal, or retrieval for N=6 months
│ ACTIVE │  (operator-tunable)
└────┬───┘
     ▼
┌──────────┐  ▸ retrieval still works but stage_weight × 0.7
│ DORMANT  │  ▸ entries do NOT auto-promote past current stage
└────┬─────┘  ▸ cross-source validation pauses (resumes on reanimation)
     │
     │── new persona activity in this domain ──┐
     │                                          ▼
     │                              ┌──────────────────────┐
     │                              │     REANIMATION      │
     │                              │      DECISION        │
     │                              └──────────┬───────────┘
     │                                         │
     │                                         ▼
     │      ┌──────────────────┐    OR    ┌──────────────────┐
     │      │ CONTINUATION:    │          │ NEW PROBE:       │
     │      │ existing context │          │ kernel federates │
     │      │ extends; probe   │          │ or treats as     │
     │      │ resumes          │          │ parallel branch  │
     │      └──────────────────┘          └──────────────────┘
     │
     ▼  still no activity at N+M=18 months (M=12)
┌─────────────┐  kernel proposes deprecation; operator reviews:
│ DEPRECATION │   - accept → DEPRECATED stage; entries marked
│  PROPOSED   │   - reject → continue DORMANT; reset M counter
└──────┬──────┘
       ▼
┌─────────────┐  archived; entries marked DEPRECATED; lineage preserved
│ DEPRECATED  │  for audit (cannot be physically deleted).
└─────────────┘

REANIMATION-VS-NEW-PROBE DECISION
  kernel checks task_fingerprint similarity to original probe's
  initial_task_context:
    ≥ 0.7 → CONTINUATION (existing context extends).
    < 0.7 → NEW PROBE (parallel; may federate later per operator policy).
```

### A.61 Promotion ceremony steps

<a id="appendix-a61"></a>

```text
1. Final cross-source validation
2. Charter conformance check
3. External validation evidence verified
4. Operator signature collected (safety-critical or standardised)
5. Co-signing personas notified
6. Audit log updated with full provenance chain
7. Stage transitioned; signed event emitted
8. DomainContext refreshed; cards updated
```

### A.62 DomainHarvest schema and harvest flow

<a id="appendix-a62"></a>

```python
@dataclass
class DomainHarvest:
    schema: str = "domain-harvest/1"
    harvest_id: str
    domain_id: str
    harvested_at: datetime
    harvested_by_persona_id: str

    # SOURCE — what triggered the harvest
    triggered_by_kind: Literal[
        "project_completion",                  # 04_PROJECT §4.1 completion
        "single_project_promotion",            # §3.2 acknowledgment fired
        "operator_pull",                       # operator-requested snapshot
        "stage_promotion",                     # §13 ceremony coincident
        "scheduled_periodic",                  # operator-configured cadence
    ]
    triggered_by_event_id: str                 # the originating signed event

    # CONTENT — what's in the bundle.  Substrate-shape inventory (counts
    # and refs per kind class); harvest carries the entries by reference,
    # not by copy, so revocations propagate.
    snapshot_at_lineage_height: int            # DomainLineage height bound;
                                              # snapshot is replay-reproducible
                                              # by truncating at this height
    inventory: dict[str, int]                  # {"media_kind": N,
                                              #  "verifier_recipe": N,
                                              #  "convention": N,
                                              #  "standard_ref": N, ...}
    entries_by_class: dict[str, list[str]]     # ids per kind class
    max_stage_present: Literal["emergent", "recognised",
                                "authoritative", "standardised"]
    trust_cap: float                           # 0..1; inherited from
                                              # single_project_mode.trust_cap
                                              # if applicable, else 0.95

    # PROVENANCE — what generated the entries
    contributing_persona_ids: list[str]
    contributing_project_ids: list[str]
    primary_evidence_refs: list[str]           # KnowledgeIngestionRecord +
                                              # StandardRef ids
    safety_critical: bool                      # mirrors source domain's flag

    # ANTI-LEAKAGE — §11.1 RISK A-E filter applied at harvest time.
    # Entries tagged user_id / org_id / project_id / IP_sensitive are
    # filtered unless leakage_consent_refs supplies the corresponding
    # signed consent.  Filtered counts recorded for audit.
    leakage_filter_report: dict
    leakage_consent_refs: list[str]            # signed consent ids per RISK

    # VISIBILITY — where the harvest is published.  Visibility tier
    # (§6.3) determines who may consume it through DomainPrecedentImport
    # (§11.2) or any other reader.
    # The 4-value list below maps to §6.3's 5 KnowledgeRef tiers as:
    #   "private"     = §6.3 TIER 1 (persona_only) ∪ TIER 2 (project_only)
    #                   — collapses persona/project distinctions because a
    #                   DomainHarvest is by construction a per-domain
    #                   artefact, not a per-persona / per-project one.
    #   "tenant"      = §6.3 TIER 3 — "all personas within the same org_id
    #                   / kernel may consume."  Under v1.0.7 multi-
    #                   principal attribution (01_KERNEL §2.4.3),
    #                   "tenant" resolves to the principals' shared
    #                   tenant_id; principals from different tenants need
    #                   a signed CrossTenancyAgreementRef to share at this
    #                   tier (else the harvest is restricted to "private").
    #   "federation"  = §6.3 TIER 4 — multi-kernel via A2A; v1.1+.
    #   "public"      = §6.3 TIER 5 — open access; operator-gated.
    visibility_tier: Literal["private", "tenant",
                              "federation", "public"]
    publishing_consent_refs: list[str]         # required for each tier
                                              # transition above "private"

    # FEDERATION — when visibility_tier ∈ {federation, public}, the
    # harvest is mirrored to the federation index (v1.1+).  In v1.0
    # the kernel writes the entry but takes no cross-kernel action;
    # federated consumers light up when v1.1 ships.
    federation_index_ref: str | None

    # OPERATOR / PRINCIPAL-COLLAPSE GATING
    # safety_critical=True OR visibility_tier ∈ {federation, public}
    # requires operator signature.  Under operator_is_user, the degraded
    # gate substitutes per 01_KERNEL §2.4 + 06_DOMAIN §15
    # (72h cool-down + non-principal ExternalAttestation +
    # HARVEST_PUBLICATION_ACKNOWLEDGED).
    operator_signature: bytes | None
    independent_attestation_ref: str | None    # under collapse

    state: Literal["drafted", "filtered", "consented",
                    "gated", "published", "revoked"]
    signed_by: bytes
```

```text
On DomainHarvest.draft:
  1. Snapshot DomainLineage at current height; inventory all entries.
  2. Run §11.1 anti-leakage filter; record counts per RISK in
     leakage_filter_report.  Entries needing consent are held until
     leakage_consent_refs supply them.
  3. Compute trust_cap: inherit from single_project_mode if applicable;
     else max stage's standard trust value.
  4. If visibility_tier > "private" OR safety_critical=True:
     route to operator gate (or degraded gate under collapse).
  5. On gate clear: state → "published"; emit
     DOMAIN_HARVEST_PUBLISHED with snapshot_at_lineage_height + the
     full inventory hash.

On DomainPrecedentImport (§11.2) consuming a harvest:
  1. The consumer's import points at the harvest_id (not the live
     domain) so the source is pinned at the snapshot height.
  2. Trust priors are computed using the harvest's trust_cap as a
     ceiling — no imported entry can exceed it in the target domain
     until the harvest is superseded by a higher-cap successor.

On harvest revocation:
  1. Operator (or degraded gate) signs HARVEST_REVOKED with reason.
  2. All downstream DomainPrecedentImports citing this harvest_id
     are flagged for re-attestation within a configured grace window;
     after grace expiry, imported entries are demoted to EMERGENT in
     their target domains.
```

### A.63 Stage-aware retrieval

<a id="appendix-a63"></a>

```python
def retrieve_with_stage_aware_ranking(query, domain_id):
    filtered = corpus.filter(...)
    
    for entry in filtered:
        stage_weight = {
            "EMERGENT":      0.5,
            "RECOGNISED":    0.7,
            "AUTHORITATIVE": 0.9,
            "STANDARDISED":  1.0,
            "DEPRECATED":    0.2,
            "TOMBSTONED":    0.0
        }[entry.stage]
        entry.final_score *= stage_weight
    
    return rank_by(filtered, score)
```

### A.64 Safety-critical domain handling

<a id="appendix-a64"></a>

```text
SAFETY-CRITICAL DOMAIN INDICATORS (per C4 — no closed domain list):
  - physical_harm_class ≥ bodily_injury (DomainContext §2)
  - information_hazard_class ≥ dual_use_civilian (DomainContext §2)
  - any safety_extension proposed in the domain
  - any KnowledgeRef from a source tagged "regulated" by operator
  - operator policy (floor source 4) names a domain category explicitly
    — operator's list, NOT substrate's

  Substrate carries no closed enum of domain names.  The two hazard
  axes (about severity shape) auto-fire safety_critical=True; the
  operator's policy names specific regulatory regimes (HIPAA, ITAR,
  EAR, GDPR, FINRA, EU AI Act, etc.) on top.

WHEN SAFETY-CRITICAL:
  Promotion gates require:
    EMERGENT → RECOGNISED: kernel auto; operator review queue
    RECOGNISED → AUTHORITATIVE: OPERATOR SIGNATURE REQUIRED;
                                blocking gate
    AUTHORITATIVE → STANDARDISED: multiple operator signatures +
                                  external standards body attestation

PRINCIPAL-COLLAPSE INTERACTION:
  When DeploymentProfile.principal_topology = "operator_is_user"
  (01_KERNEL §2.4), the operator signature required at
  RECOGNISED → AUTHORITATIVE is replaced by the degraded gate:
  72h cool-down + non-principal ExternalAttestation +
  signed PRINCIPAL_COLLAPSE_ACKNOWLEDGED.

DECISIONS LOG:
  Every operator (or, under collapse, principal) decision in
  OperatorDecisionLineage; signed.  Audit reproducible.
```

### A.65 DomainLineage event types

<a id="appendix-a65"></a>

```text
event types:
  domain_unknown_detected             probe_initiated
  probe_phase_entered                 probe_phase_completed
  probe_resumed                       probe_abandoned
  probe_budget_threshold              probe_halted
  knowledge_ingested                  knowledge_ref_transition
  tool_discovered
  convention_proposed                 convention_adopted
  convention_ambiguity                convention_reconciliation_proposal
  convention_deprecated
  safety_extension_proposed           safety_extension_approved
  verifier_recipe_inferred            verifier_recipe_validated
  proposal_convergence_detected
  proposal_consolidation              proposal_rate_limited
  demotion_event
  cross_domain_transfer
  promotion_event (EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED)
  domain_charter_drift_detected
  domain_dormant                      domain_reanimated
  domain_version_deprecated
  novelty_check_passed                novelty_check_failed
  human_assist_drafted                human_assist_requested
  human_assist_granted                human_assist_declined
  bridge_established                  bridge_validated
  bridge_degraded                     bridge_lost
  bridge_re_established               bridge_revoked
  mhbb_recurrence_detected

  # additions (§3.2, §4.7.1, §9.1.1, §11.2, §13a)
  envelope_drafted                    pledge_attached
  pledge_drawn_down                   pledge_revoked
  envelope_exhausted                  envelope_released
  envelope_low
  cold_start_uplift_applied
  bulk_kind_proposal_signed
  domain_precedent_import_drafted     precedent_entry_linked
  precedent_entry_failed              precedent_revoked
  single_project_promotion_acknowledged
  domain_harvest_drafted              domain_harvest_filtered
  domain_harvest_gated                domain_harvest_published
  domain_harvest_revoked              harvest_publication_acknowledged
```

### A.66 EmergentDomainContext in operation

<a id="appendix-a66"></a>

```python
def mint_envelope_with_emergent_domain(persona, task, env, user, project):
    envelope = mint_envelope_base(persona, task, env, user, project)
    
    if project and project.domain_context_ref:
        domain = resolve(project.domain_context_ref)
        
        if domain.stage == "emergent":
            envelope.context_blocks.append(
                make_context_block(
                    text=f"NOTE: Domain '{domain.name}' is in EMERGENT "
                         f"stage. Trust 0.3. Verify claims carefully. "
                         f"Probe may continue.",
                    cacheable=False
                )
            )
        elif domain.stage == "recognised":
            envelope.context_blocks.append(...)
        # AUTHORITATIVE and STANDARDISED: no special warning
    
    elif task_appears_in_new_domain(task, persona):
        # Kernel emits DOMAIN_UNKNOWN_DETECTED
        kernel.emit(DOMAIN_UNKNOWN_DETECTED(persona, task, env))
        # Routing decision: interleaved or sequential probe?
    
    return envelope
```

### A.67 Federated domain emergence

<a id="appendix-a67"></a>

```text
DISCOVERY: federated discovery via A2A surfaces other kernels'
           EmergentDomainContext.

CROSS-KERNEL PROMOTION:
  "EMERGENT" in kernel_X + "EMERGENT" in kernel_Y →
  cross-kernel "RECOGNISED" candidate.
  Requires:
    - A2A signed agreement between kernels' DomainContexts
    - both operators approve federation
    - co-signing personas across kernels

FEDERATED AUTHORITATIVE → STANDARDISED:
  Consensus among ≥ N participating kernels.
  Anti-sybil: each kernel's reputation contribution counted.
```

### A.68 Operator vs Persona role shift

<a id="appendix-a68"></a>

```text
OPERATOR OWNS (v1.0):
  - Safety gates (safety-critical promotion sign-off)
  - Deployment policy (forbidden topics, regulated content)
  - Cross-org artifact sharing approval
  - Persona suspension / override
  - Tool registry blessing (kernel-native)
  - DomainPromotionPolicy thresholds tuning
  - Budget caps
  - Paywalled knowledge source authorization
  - Audit log review
  - Drift escalation handling

NO LONGER AUTHORS:
  - DomainContext content (personas emerge)
  - Knowledge corpora (personas ingest)
  - Tool ecosystems (personas discover)
  - Verifier recipes (personas infer)
  - Safety extensions (personas propose; operator gates)
  - Conventions (personas adopt)
  - Seed skills (personas synthesise via Voyager)
```

### A.69 Multi-tenant ORG_A / ORG_B interaction

<a id="appendix-a69"></a>

```text
PER-ORG SCOPE
  - personas (signed by their kernel scope key)
  - projects (in their org's environment)
  - DomainContexts (emergent or authored)
  - user boundaries + consents
  - operator policy

CROSS-ORG OPERATION (e.g., ORG_A persona reads ORG_B's KnowledgeRef
                      or transfers a skill cross-org)

  1. POLICY INTERSECTION
       allowed = ORG_A.policy.allow_cross_org(op)
                 AND ORG_B.policy.allow_cross_org(op)
       (either operator may refuse → blocked.)

  2. DATA CLASSIFICATION CHECK
       artifact tagged with classification: public / internal /
       confidential / restricted. Cross-org allowed only when source
       org's classification permits AND target org has clearance.

  3. DUAL-SIGNING
       transfer event signed_by both ORG_A's operator key AND
       ORG_B's operator key. Either signature missing → refused.

  4. AUDIT TRAIL
       CrossOrgTransfer event in BOTH orgs' DomainLineage; replayable.

  5. REVOCATION
       either org may revoke; revocation propagates to consuming
       artifacts (recipients tombstone references).
```

### A.70 Performance and cost targets

<a id="appendix-a70"></a>

```text
Domain unknown detected (event composition)        ≤ 30 ms p95
Probe initiation (signed)                           ≤ 100 ms
MCP-Zero active discovery                           ≤ 200 ms p95
Smoke test orchestration                            ≤ 30 s p95 (tool-dependent)
Knowledge ingestion (single paper)                  ≤ 60 s p95
Bulk ingestion (50 papers parallel)                 ≤ 5 min
Verifier recipe inference (nightly batch)           ≤ 5 min
Safety extension proposal                           ≤ 30 s
Convention emergence detection                       ≤ 100 ms
Cross-source validation                              ≤ 30 s
Auto-promotion check (nightly batch)                 ≤ 5 min
Promotion ceremony                                   ≤ 1 min
Demotion event                                       ≤ 30 s
Cross-domain transfer                                ≤ 100 ms

Costs:
  NARROW probe                                       ~$1-5 per probe
  BROAD probe                                         ~$10-50 per probe
  Active emergent domain (per month)                  ~$50-500
  Standardised domain (steady state)                  ~$5-50
  Knowledge ingestion (per paper)                     ~$0.10-1.00
  Promotion ceremony (per entry)                      ~$5-30

Per-domain bootstrap budget:
  EMERGENT → RECOGNISED:                              ≤ $500
  RECOGNISED → AUTHORITATIVE:                         ≤ $2000
  (operator-tunable; safety-critical higher)
```

### A.71 AttestationEquivalencePolicy schema, admission rules, and trust composition

<a id="appendix-a71"></a>

```python
class AttestationEquivalencePolicy:
    """Per-domain policy declaring when sensor-bridge evidence may
    substitute for human professional attestation.
    schema: attestation-equivalence-policy/1"""
    policy_id: str                          # UUID
    domain_id: str                          # owning domain

    # What this policy covers
    verification_kind: str                  # KindRegistry-resolved
    human_attestation_kind: str             # ExternalAttestation kind it substitutes

    # Required sensor evidence
    required_bridge_asset_ids: list[str]    # specific calibrated bridges
    required_measurement_kinds: list[str]   # KindRegistry-resolved measurement types
    min_measurement_count: int              # statistical minimum per verification event
    max_uncertainty_envelope: dict          # acceptable uncertainty bounds per kind
    #   format: {measurement_kind: {max_systematic: float, max_random: float,
    #            units_kind: str}}

    # Calibration requirements for the bridge
    min_calibration_kind: str               # KindRegistry-resolved (e.g., "nist_traceable")
    max_calibration_age: timedelta          # freshness requirement
    require_reference_standard_chain: bool  # default True for safety-critical

    # Trust outcome
    equivalence_trust_score: float          # trust when sensor substitutes
    trust_discount: float                   # multiplier vs human attestation (< 1.0)
    #   effective_trust = human_attestation_trust × trust_discount

    # Safety floor interaction
    safety_critical_allowed: bool           # can this substitute in safety-critical?
    #   default False; requires C2 co-sign to set True
    operator_cosign_required: bool          # always True; cannot be False
    c2_cosign_required: bool                # True when safety_critical_allowed = True
    #   OR when superseded_by_human_on_dispute = False

    # Dispute resolution
    superseded_by_human_on_dispute: bool = True
    #   when both sensor + human exist and disagree:
    #     True  → human governs PhysicalAsset state advancement
    #     False → sensor governs (requires C2 co-sign regardless of domain)

    # Agreement history (kernel-maintained)
    agreement_history: AgreementHistory

    # TBD
    review_cadence: timedelta = timedelta(days=180)
    last_reviewed_at: datetime | None
    proposed_by: str                        # persona_id or operator_id
    approved_by: str                        # operator_id (always)
    approved_at: datetime | None

    # Lifecycle
    status: Literal[
        "proposed",                         # persona or curator proposed
        "operator_approved",                # operator signed
        "active",                           # in use; substitutions happening
        "suspended",                        # review overdue or calibration stale
        "revoked"                           # operator terminated
    ]

    signed_by: bytes                        # kernel signature


class AgreementHistory:
    """Tracks sensor-vs-human agreement over time for trust calibration.
    Kernel-maintained; not persona-editable."""
    total_substitutions: int                # sensor used in place of human
    total_parallel_checks: int              # both sensor + human available
    agreements: int                         # sensor + human agree
    disagreements: int                      # sensor + human disagree
    human_overrides: int                    # human judgment used after dispute
    agreement_rate: float                   # agreements / total_parallel_checks
    last_parallel_check_at: datetime | None
    last_disagreement_at: datetime | None
```

**Policy lifecycle FSM.**

```text
         proposed ──── operator_approved ──── active
                                                │
                       ┌────────────────────────┤
                       │                        │
            review overdue OR              operator revokes
            calibration stale                   │
                       │                        ▼
                       ▼                    revoked
                   suspended                (terminal)
                       │
                  operator re-reviews
                       │
                       ▼
                     active
```

**Trust composition rules.**

```text
RULE 1: Sensor substitution trust.
  When an AttestationEquivalencePolicy is active and all evidence
  requirements are met (bridge calibrated, measurement count ≥ min,
  uncertainty within bounds):
    effective_trust = human_attestation_trust × trust_discount
  The sensor-substituted verification enters lineage with
  attestation_source = "sensor_bridge" (distinct from "human_professional"
  and "peer_attested").

RULE 2: Trust discount is always < 1.0.
  The substrate refuses trust_discount >= 1.0. Sensor evidence
  never reaches parity with human attestation through this mechanism.
  Parity requires operator to deprecate the human attestation kind
  entirely (operator policy, outside substrate scope).

RULE 3: Dispute resolution.
  When both sensor evidence and human attestation exist for the same
  verification event:
    IF superseded_by_human_on_dispute = True (default):
      human_attestation governs PhysicalAsset state advancement
      sensor evidence recorded in lineage as dissenting_sensor_evidence
      agreement_history.disagreements += 1
      agreement_history.human_overrides += 1
    IF superseded_by_human_on_dispute = False (requires C2 co-sign):
      sensor evidence governs PhysicalAsset state advancement
      human attestation recorded in lineage as overridden_human_attestation
      agreement_history.disagreements += 1

RULE 4: Calibration freshness gate.
  At every sensor_substitution_applied event, kernel checks:
    bridge.calibration_binding.expires_at > now()
    bridge.calibration_binding.calibrated_at + max_calibration_age > now()
    bridge.calibration_binding.drift_bound_pct not exceeded
  If ANY check fails: substitution refused; policy auto-suspends for
  this bridge until re-calibration. Event: attestation_equivalence_policy_suspended.

RULE 5: Safety-critical composition.
  When domain has safety_critical = True AND physical_harm_class >= bodily_injury:
    safety_critical_allowed MUST be True (operator + C2 co-sign) OR
    substitution is refused entirely — human attestation required.
  This is a hard gate, not a trust adjustment.

RULE 6: Composition with BridgeReductionPlan.
  A BridgeReductionEntry (04_PROJECT §26a.10) that sets
  attestation_equivalence_policy_id MUST reference a policy with
  status IN {operator_approved, active}. If the policy is later
  revoked, the entry's status reverts to design_ready and the
  bridge_reduction_plan emits bridge_reduction_entry_advanced
  (backward) with reason = "equivalence_policy_revoked".

RULE 7: Progressive trust via agreement_history.
  Operators reviewing a policy MAY adjust trust_discount based on
  agreement_history.agreement_rate. High agreement (>0.95 over
  >50 parallel checks) justifies reducing the discount (e.g.,
  0.85 → 0.90). Low agreement (<0.80) justifies increasing the
  discount or revoking the policy. The substrate tracks the data;
  the operator makes the judgment call.
```

**Admission rules.**

1. `operator_cosign_required` is always True; cannot be set False. The substrate hardcodes this.
2. `trust_discount >= 1.0` is refused at proposal time. Schema validation rejects.
3. `safety_critical_allowed = True` requires `c2_cosign_required = True` AND explicit C2 co-signature at approval time. The substrate refuses to activate without both.
4. `superseded_by_human_on_dispute = False` requires C2 co-sign regardless of domain safety classification. Overriding human judgment is always a safety-adjacent decision.
5. `required_bridge_asset_ids` must reference bridges with `status = active` AND valid `BridgeCalibrationBinding`. Policy activation blocked if any referenced bridge is degraded or lost.
6. `review_cadence` minimum is 30 days (substrate refuses shorter). Maximum is 365 days. Safety-critical policies default to 90 days.
7. First `sensor_substitution_applied` event requires the policy to have been `active` for at least 7 days (grace period for operator revocation after approval).
