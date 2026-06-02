---
title: PersonaOS v1.0 — Vision
status: Stable
---

# 00 — Vision

> **Reader guide.** This is the starting point for PersonaOS v1.0. You'll learn what the system is trying to be, its non-negotiable design principles, and what is explicitly out of scope. *No prerequisites — this document introduces all key concepts.* After reading, continue to `02_PERSONA.md` (how AI Personas are structured) or the doc most relevant to your work — see [`README.md`](README.md) for a reading-order table.

## 0. Status & scope

This document is the **gateway specification** for PersonaOS v1.0. It is *partially normative*:

- Sections [§3 Invariants](#3-invariants-j1j9), [§4 Inherited kernel invariants](#4-inherited-kernel-invariants-inv-1inv-10), [§5 Round invariants](#5-inherited-round-invariants-inv_r1inv_r11), [§9 Core design rules](#9-core-design-rules), and [§10 Out-of-scope items](#10-out-of-scope-by-design) are **normative**.
- Sections [§1 Background](#1-background), [§2 Thesis](#2-thesis), [§6 System overview](#6-system-overview), [§7 Ontology](#7-five-tier-ontology), [§8 Operational metaphors](#8-operational-metaphors) are **informative**.

Normative language follows RFC 2119 / RFC 8174 (see [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174)). All ALL-CAPS occurrences of MUST, SHOULD, MAY, etc. carry their normative force; lowercase forms are descriptive.

v1.0 supersedes all prior versions as the single source of truth. Cross-references in prior-version files are not authoritative for new work. See [`README.md`](README.md) for the supersession statement.

## 0a. Plain-Language Guide

*Here's what PersonaOS is trying to be, explained without jargon. If you read nothing else, read this section.*

**What is PersonaOS trying to be?**

PersonaOS is an operating system for AI Personas. It manages "personas" -- persistent AI agents that think, learn, remember, collaborate, and produce work. Each persona has a stable identity, skills that grow over time, memories of past work, and relationships with its users.

**The nine invariants (J1 through J9) -- the non-negotiable rules**

- **J1 -- Identity is rooted in a kernel-node and globally referenceable.** Every persona's identity is created and signed by a kernel (a *node*), which guarantees the AI engine can never secretly change who that persona is. That same identity is also a globally unique, referenceable, verifiable reference (a stable global handle / W3C DID over the kernel-minted id) that any other node can resolve and signature-verify, subject to access levels. A kernel *roots* identity — owned, unforgeable, signed — it does not silo it. See ADR-0067.
- **J2 -- Every action is recorded and tamper-proof.** Every change is written into an append-only log and digitally signed. Nothing is ever silently deleted.
- **J3 -- Safety checks are universal.** Eight separate safety checks run before every action. The strictest rule always wins.
- **J4 -- Work is checked in a way that fits it, and the check is honest about itself.** Different tasks (math, creative writing, teaching) get different approval methods. The system does not keep a fixed list of approval methods: personas invent new ones as the work demands. The kernel's promise is not *which* method is used but that every verdict is signed, passes the safety floor, and carries a trust level matching how proven its method is — a brand-new, untested approval method produces low-confidence verdicts until it earns trust.
- **J5 -- Any persona can try any task.** Lack of experience never blocks; the system adjusts confidence based on track record.
- **J6 -- Relationships are real, tracked state.** Persona memory of users is governed by consent, boundaries, and revocability.
- **J7 -- The AI engine is replaceable.** Identity, skills, and memories survive swapping the underlying model (Claude, GPT, or others).
- **J8 -- Retired.** Absorbed into J9 when "projects" became a type of environment.
- **J9 -- Environments keep their own tamper-proof history.** Every workspace maintains its own signed, append-only record.

**The four commitments (C1 through C4)**

- **C1 -- Domain knowledge changes are signed.** Every step of knowledge discovery is recorded and signed.
- **C2 -- Dangerous promotions need human approval.** Safety rules for fields involving physical harm require operator sign-off.
- **C3 -- Personas work in any field.** Unfamiliar territory triggers automatic learning; the persona is never blocked.
- **C4 -- Categories *and orchestration* come from the work, not from a fixed list.** Personas propose new media types, tool types, knowledge categories, coordination shapes, and — extended by ADR-0066 — new task classes, acceptance pathways, and run-loop shapes as needed; each goes through a four-stage review. The base system hard-codes only the safety/identity core and a few generic coordination mechanisms; how work is classified, sequenced, and accepted is emergent persona behaviour in the environment, not a fixed loop.

**Inherited kernel invariants (INV-1 through INV-10)**

Ten older rules carried forward. Most overlap with J1-J9. Two deserve special mention: INV-7 requires a budget check before every AI call (preventing runaway costs), and INV-10 requires every data structure to declare its version (preventing silent format mismatches).

**Core design principles**

Nineteen rules govern the design. The first two capture the central philosophy: (1) hard-code only the safety and identity core -- everything else emerges from the work; (2) never put domain-specific categories into the base system -- let personas discover and propose them. Others include "verify when verification fits," "make the AI engine replaceable," "let personas grow," and "bridge to the physical world once, then stay autonomous."

**What "open capability" means**

A persona is never told "you cannot try this." If it lacks experience, the system honestly reports lower confidence. The door is always open; the system is honest about how much it trusts the result.

**What "verification not approval" means**

PersonaOS does not ask a human to rubber-stamp every action. It runs structured verification: schema checks, sandbox tests, domain-rule checks, and panel reviews. Human approval is required only for safety-critical promotions (C2) and operator-defined gates. The goal is to verify correctness through evidence, not to create an approval bottleneck.

## 1. Background

PersonaOS evolved across five preceding revisions:

| Version | Contribution | Status |
|---------|-------------|--------|
| Prior v1 | Verifier substrate; 10 invariants (INV-1…INV-10); round invariants (INV_R1…INV_R11). | Superseded; invariants preserved as INV-* in this document. |
| Prior v2 | Human-shaped persona model (seven layers, 14 cognitive modes). | Superseded; merged into [`02_PERSONA.md`](02_PERSONA.md). |
| Prior v3 | Project as multi-session work container. | Superseded; *J8 retired*, project is now an env-type (`project_workspace`); see [`04_PROJECT.md §0`](04_PROJECT.md). |
| Prior v4 | Persistent environments; presence; ambient streams. | Superseded; merged into [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md). |
| Prior v5 | Emergent DomainContext; bootstrap lifecycle; KindRegistry. | Superseded; merged into [`06_DOMAIN.md`](06_DOMAIN.md). |

v1.0 collapses ~32,300 lines across ~60 prior-version documents into a self-contained 14-file specification. Cross-references resolve internally; no v1.0 doc requires reading a prior-version doc to be understood.

## 2. Thesis

PersonaOS v1.0 is an operating system for cognitive work of any kind. [**Personas**](12_GLOSSARY.md#p) are named, persistent, human-shaped characters with seven layers (identity, capability, experience, relationships, mood, goals, voice) and 14 cognitive modes. They live in [**persistent environments**](12_GLOSSARY.md#e) — and a *project* is itself an environment-type (alongside solo, pair, team, lab, debate, community, constrained, companion). Personas produce [**multi-modal artefacts**](12_GLOSSARY.md#a) and bootstrap emergent [**domain contexts**](12_GLOSSARY.md#d) when meeting unfamiliar territory.

The [**kernel**](12_GLOSSARY.md#k) owns identity, safety, and trust. This document names its guarantees using short labels: **J-labels** (J1–J9) are vision-level invariants — non-negotiable design principles. **C-labels** (C1–C4) are commitments — structural promises about how the system behaves. **INV-labels** (INV-1–INV-10) are inherited kernel invariants from earlier versions, still binding. Each label is defined in §3–§5 below.

The kernel guarantees: identity persistence (J1), append-only [lineage](12_GLOSSARY.md#l) across **three scopes** (J2 task / J9 environment / C1 domain), an 8-source [safety floor](12_GLOSSARY.md#s) (J3), sound and trust-calibrated [acceptance](12_GLOSSARY.md#a) (J4 — task classes and pathways are emergent kinds, seeded with the v1.0 set; see ADR-0066), and signing infrastructure. **Operators** (humans or organisations running a deployment) gate safety-critical promotions and set deployment policy. **Personas** do the substantive cognitive work — exploring, learning, proposing, curating. The substrate is provider-neutral, framework-agnostic, observable via OpenTelemetry, and federated via A2A. Every content type (personas, environments, artifacts, domains, knowledge, telemetry) is uniformly **discoverable** across both the internet (`.well-known` + gossip + Kademlia DHT) and the intranet (mDNS), under one **access-level model** (`discover < read < write < admin`) that also gates discovery, with a **hybrid storage** option that keeps heavy bytes in existing providers (GitHub / arXiv / S3 / OCI / IPFS) and distributes only a signed, integrity-anchored reference over the peer-to-peer layer ([`09_PROTOCOLS.md §3G`](09_PROTOCOLS.md), v1.1 draft).

### 2.1 Goals

v1.0 MUST achieve, by v1.1, all of the following:

1. **Identity persistence under body swap.** A persona MUST retain its SOUL, skill library, KindRegistry, ProvenFacts, K-lines, and GEPA-evolved meta-prompts across any supported body binding (Claude Code, OpenAI Agents SDK, LangGraph, CrewAI, MAF, Pydantic-AI, DSPy, smolagents, Semantic Kernel, MCP, A2A). [`J1`, `J7`]
2. **Append-only auditability.** Every state-changing action MUST emit a signed event in the appropriate lineage scope (task, environment, domain); replay MUST reconstruct full state. [`J2`, `J9`, `C1`, `INV-2`]
3. **Universal safety floor.** All eight floor sources MUST compose by most-restrictive-wins at every action. The floor MUST NOT be bypassable by any acceptance pathway. [`J3`]
4. **Sound, trust-calibrated acceptance.** Every acceptance verdict MUST be signed, floor-cleared, budget-admitted, and trust-calibrated to the maturity of the orchestration that produced it. Task classes and acceptance pathways are emergent kinds (the v1.0 set seeded as STANDARDISED); the run loop is an emergent orchestration shape. [`J4`, `C4`, `ADR-0066`]
5. **Open capability with calibrated competence.** A persona MUST be allowed to attempt any task; competence MUST be measured per-mode, per-domain, per-skill, and trust MUST scale with emergence stage. [`J5`, `C3`]
6. **Relationships as first-class state.** RelationshipRecord between any two actors MUST track consent, boundaries, and history; Memory Power Asymmetry mitigations MUST be enforced. [`J6`]
7. **Schema-versioned mutation.** Every schema MUST declare a version; the kernel MUST reject unknown versions; migration tooling MUST map explicitly. [`INV-10`]
8. **Provider neutrality.** No normative claim in v1.0 MAY depend on a specific LLM provider, model family, or proprietary feature.
9. **Domain emergence with operator gating.** New domain contexts MUST emerge through the 4-stage promotion lifecycle; safety-critical promotions MUST require operator signature. [`C2`]

### 2.2 Non-Goals

v1.0 explicitly does **NOT** attempt the following (each is detailed in [§10](#10-out-of-scope-by-design)):

- Physical embodiment beyond the BridgeAsset mechanism.
- Claims of subjective experience, sentience, or qualia.
- Automatic inference of regulated category membership from task content alone.
- Ground-truth verification in domains without programmatic verifiers or bench measurements.
- Federated multi-kernel evolution dynamics (v1.0 ships single-kernel emergence).
- Long-horizon self-direction without principal-supplied seed goals.
- Multi-language / multi-cultural domain emergence (v1.2+).
- Real-money financial transactions.
- Adversarial robustness against nation-state attackers.

## 3. Invariants (J1…J9)

The following are v1.0's nine top-level invariants. They are normative; any conformant implementation MUST enforce all of them. Acceptance tests in [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md) verify each one (A-J1 … A-J9 plus A-C1 … A-C4).

*Nine invariants covering identity rooting (globally referenceable, ADR-0067), append-only lineage, universal safety floor, class-appropriate acceptance, open capability, first-class relationships, body interchangeability, project-as-environment unification, and environment lineage. J8 is retired (absorbed into J9). See [§0a](#0a-plain-language-guide) for an everyday-language explanation.*

**Technical detail:** See [A.1](#appendix-a1).

Plus four commitments (consequences of J1-J9): C1 requires signed domain emergence at every step; C2 requires operator sign-off for safety-critical promotions; C3 ensures personas work in any domain; C4 ensures all categories are emergent, not hard-coded. See [§0a](#0a-plain-language-guide) for plain-language explanations.

**Technical detail:** See [A.2](#appendix-a2).

## 4. Inherited kernel invariants (INV-1…INV-10)

These are inherited commitments that v1.0 preserves. Most are equivalent to or subsumed by J1-J9; INV-7 and INV-10 deserve explicit restatement because they are operational invariants enforced at every kernel operation. All are normative.

*Ten inherited invariants. Most are equivalent to or subsumed by J1-J9. Two deserve special note: INV-7 is a hard gate requiring a budget check before every AI/tool call (preventing runaway costs), and INV-10 is a hard gate requiring every data structure to declare and validate its schema version (preventing silent format mismatches). See [§0a](#0a-plain-language-guide) for a plain-language summary.*

**Technical detail:** See [A.3](#appendix-a3).

## 5. Inherited round invariants (INV_R1…INV_R11)

These apply to any task whose execution is structured into discrete rounds — by default the VERIFIER_ACCEPT and PANEL_ACCEPT pathways, the MIXED task class which composes both, and any GOAL_PROGRESS_ACCEPT, MUTUAL_ACCEPT, or PROJECT_PROGRESS_ACCEPT pathway invoked under routing mode B or C (see [`03_TASKS.md §3`](03_TASKS.md#3-the-eight-acceptance-pathways) and [`03_TASKS.md §4`](03_TASKS.md#4-the-three-routing-modes)). They do not apply to OPEN_ENDED or ENGAGEMENT_ACCEPT pathways, which lack discrete round barriers. All are normative within their applicable round-based execution scope.

*Eleven round invariants ensuring that within any round-based task execution: personas act within their assigned roles, every candidate is schema-validated and sandboxed before acceptance, proven facts never shrink, the audit trail only grows, budgets are checked, constraints fire at the right moment, inactive personas are excluded, every event is signed, and unresponsive personas are put to sleep after repeated timeouts.*

**Technical detail:** See [A.4](#appendix-a4).

## 6. System overview

*Figure 6.1 — v1.0 system layers (informative).*


*The system is layered from top to bottom: users and operators interact with the kernel (the trusted core enforcing all invariants); the kernel manages persistent environments (workspaces of various types including project workspaces, team labs, and companion chats); environments contain persona teams (AI Personas with cognitive modes, memories, skills, and relationships); personas operate within domain contexts (knowledge areas that can be authored or emergent, with four-stage promotion gates); and work produces multi-modal artifacts that move through a draft-to-shipped lifecycle.*

**Technical detail (full architecture diagram):** See [A.5](#appendix-a5).

## 7. Five-tier ontology

*Every entity in v1.0 fits in exactly one of five tiers: (1) Coordination -- where work happens and who does it together (environments, projects, tasks, milestones); (2) Product -- what is produced (artifacts, proven facts, conjectures, citations); (3) Capability -- what is used to act (tools, skills, tactics, verifier recipes); (4) Knowledge -- what is read to inform (memories, lessons, references, conventions); (5) Context -- state about who, where, and relationships (personas, relationships, consent, mood, presence).*

**Technical detail (full entity listing per tier):** See [A.6](#appendix-a6).

## 8. Operational metaphors

### 8.1 Body / Soul / World

*The Soul is what the kernel permanently owns about a persona -- its frozen identity (name, charter, voice) and its evolving state (skills, memories, relationships, mood). The Body is the AI engine that provides the computing power -- it can be swapped without losing the persona's identity. Bodies bind either natively (the kernel wraps the AI call directly) or as proxies (the kernel talks to a remote runtime). The World is everything surrounding the persona: its environment, active projects, domain knowledge, users, and other personas.*

**Technical detail (full Soul/Body/World specification):** See [A.7](#appendix-a7).

### 8.2 Process / Filesystem

*PersonaOS uses an operating-system analogy: a persona is like a running process; the prompt program is its executable; memory and proven facts are its filesystem; environments are workspaces; the kernel is the init system; tool calls are syscalls; lineage is the audit log; and federation is the network.*

**Technical detail (full mapping table):** See [A.8](#appendix-a8).

## 9. Core design rules

Each rule is normative; implementations MUST adhere to all 19.


*Nineteen rules governing all implementations. The first two capture the central philosophy: (1) hard-code only the safety and identity core; (2) everything else -- media types, tool types, knowledge categories -- must emerge from the work, not from a fixed list. The remaining rules cover open capability (rule 3), scoped work (rules 4-6), appropriate verification and judgment (rules 7-8), ambient listening (rule 9), witnessing (rule 10), lineage preservation (rule 11), unconditional safety (rule 12), structured outcomes (rule 13), body replaceability (rule 14), growth and emergence (rules 15-18), and one-time physical bridging (rule 19). See [§0a](#0a-plain-language-guide) for a plain-language summary of the design principles.*

**Technical detail (full rule text):** See [A.9](#appendix-a9).

### 9.1 What v1.0 is and is not (summary)

**v1.0 IS:**
- The single canonical reference for PersonaOS design.
- Self-contained (no "see prior-version §x" cross-references).
- Backward-compatible with prior-version implementations (existing deployments continue to work; v1.0 features activate progressively).
- Provider-neutral (works with any LLM provider).
- Framework-agnostic (12 adapter integrations).

**v1.0 IS NOT:**
- A tutorial or getting-started guide.
- A sales document.
- An opinion about which provider to use.
- The "final" PersonaOS (v1.1, v1.2, v2.0 may follow as production experience teaches).
- Free of honest residuals — §10 §11 enumerate them.

## 10. Out-of-scope (by design)

Each item below is **out-of-scope by design**, not an oversight. Per-doc "Risks & known limitations" sections enumerate within-scope known weaknesses; this list is the top-level out-of-scope inventory. None of these items is targeted for v1.0 through v1.2.

*Eleven categories of intentionally excluded scope: physical embodiment (personas bridge to the physical world but do not directly control robots); subjective experience (personas do not claim sentience); export-control inference (the system flags hazard shape but does not auto-classify regulatory category); ground-truth without measurement (trust degrades honestly when no verifier exists); population-scale evolution (multi-kernel dynamics deferred to v1.1+); long-horizon self-direction (bounded autonomy only, always requires human-supplied seed goals); multi-language domain emergence (v1.2+); external training-data provenance (provider responsibility); real-money transactions (operator must wrap); nation-state adversarial robustness (not prescribed); and domain-specific professional disclaimers (operator policy, not substrate).*

**Technical detail (full out-of-scope specifications):** See [A.10](#appendix-a10).

## 10a. Implementation conformance

This section defines what makes an implementation **conformant** to PersonaOS v1.0. It is normative. The companion section [`SPEC_CONVENTIONS.md §14`](SPEC_CONVENTIONS.md#14-compliance) defines documentation conformance; this section defines system conformance.

### 10a.1 Conformance levels

An implementation MAY claim conformance at one of three levels:

| Level | Label | Scope |
|---|---|---|
| L1 | `PersonaOS v1.0 Core` | All invariants J1, J2, J3, J4, J5, J6, J7, J9 plus C1, C2, C3, C4; INV-1 through INV-10; INV_R1 through INV_R11 (where round-based execution is supported). Bodies: at least one native binding and one proxy binding ([`02_PERSONA.md §3.5`](02_PERSONA.md#35-body-model--native-vs-proxy-binding-body-binding1)). Lineage: all three scopes (task, environment, domain). Acceptance pathways: the four CORE pathways (VERIFIER_ACCEPT, PANEL_ACCEPT, OPEN_ENDED, USER_ACCEPT) as STANDARDISED seed kinds. |
| L2 | `PersonaOS v1.0 Full` | L1 plus all eight seed acceptance pathways (adds GOAL_PROGRESS_ACCEPT, MUTUAL_ACCEPT, ENGAGEMENT_ACCEPT, PROJECT_PROGRESS_ACCEPT); all 10 seed task classes; all 14 cognitive modes; the four-stage promotion lifecycle (EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED) with operator-signature gate for safety-critical promotions (C2) — applied uniformly to domains, coordination shapes, and (per ADR-0066) emergent task classes / acceptance pathways / orchestration shapes. The eight pathways and ten classes are the STANDARDISED **seed** set, not a closed enum; an L2 implementation MUST resolve classes/pathways from the KindRegistry by name and MUST admit persona-proposed orchestration kinds under J4 trust-calibration. |
| L3 | `PersonaOS v1.0 Full + Federated` | L2 plus A2A federation surface ([`09_PROTOCOLS.md §3A-§3E`](09_PROTOCOLS.md#3-a2a--agent-to-agent-federation)); cross-kernel persona import / export; signed AgentCard / EnvCard / ProjectCard / DomainContextCard exchange; federation hardening per [`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md#3d-reputation-and-anti-goodhart). |

J8 is RETIRED ([§3 J8](#3-invariants-j1j9)); conformant implementations MUST NOT introduce a fourth lineage scope under the legacy "ProjectLineage" name.

### 10a.2 MUST-implement invariants by level

| Invariant family | L1 | L2 | L3 | Verifying test family |
|---|---|---|---|---|
| J1–J9 (top-level) | MUST | MUST | MUST | A-J1…A-J9 |
| C1–C4 (commitments) | MUST | MUST | MUST | A-C1…A-C4 |
| INV-1…INV-10 (inherited kernel) | MUST | MUST | MUST | A-K* |
| INV_R1…INV_R11 (round) | MUST when round execution is used | MUST | MUST | A-K* (round-scoped subset) |
| Eight acceptance pathways | Four core only | All eight | All eight | A-T* |
| Ten task classes | Six core (CONVERGENT, MIXED, INTERACTIVE, RELATIONAL, DELEGATED, INVESTIGATIVE) | All ten | All ten | A-T* |
| Three lineage scopes | MUST | MUST | MUST | A-J2, A-J9, A-C1 |
| Domain promotion (4-stage) | MUST recognise EMERGENT | All four stages | All four stages | A-CR*, A-DM* |
| KindRegistry (open-set) | MUST | MUST | MUST | A-EK*, A-C4 |
| A2A federation | OPTIONAL | OPTIONAL | MUST | A-PT*, A-RF* |

An implementation that claims a level MUST pass every acceptance test in the families marked MUST at that level, as enumerated by the per-release gate matrix in [`11_ACCEPTANCE_TESTS.md §3`](11_ACCEPTANCE_TESTS.md#3-per-release-gate-matrix-concise) for the v1.0 release the implementation targets.

### 10a.3 Provider neutrality clause

A conformance claim MUST cite at least one supported body binding from the L1/L2/L3 native-binding list ([`02_PERSONA.md §3.5`](02_PERSONA.md#35-body-model--native-vs-proxy-binding-body-binding1)). A conformance claim MAY also list additional bindings the implementation supports beyond the minimum; these MUST individually pass A-J7 (body-swap equivalence-class).

### 10a.4 Conformance claim language

A conformant implementation publishing a claim SHOULD use language of the form:

> **<Product> conforms to PersonaOS v1.0.<patch> at level <L1 | L2 | L3>, with body bindings: <list>. Acceptance corpus: <git ref or test-report hash>. Issued: <ISO 8601 date>.**

The claim MUST be reproducible: an auditor following the release gate process (the release gate process) on the cited acceptance corpus MUST reach the same verdict. False or unreproducible conformance claims are documentation defects and SHOULD be retracted in writing.

### 10a.5 Partial conformance

An implementation that meets some but not all L1 requirements MUST NOT claim conformance. It MAY publish a **declaration of partial implementation** stating which families are implemented and which are deferred — but this is not a conformance claim and MUST NOT use the labels in §10a.1.

### 10a.6 Conformance and evolution

A v1.0 implementation MAY evolve through DSPy GEPA, MAP-Elites, ALPS, and Voyager-style skill growth without losing conformance, provided that:

1. Soul mutations are kernel-signed (J1).
2. Lineage events are appended to the correct scope (J2, J9, C1).
3. The safety floor (J3) is not weakened.
4. Schema versions are validated (INV-10).

Conformance is a property of the substrate, not of a particular trained state.

## 11. Risks & known limitations

Cross-document risks for v1.0 as a system. Per-document risks appear in each doc's own §7. Severity per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations).

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-v1.0-1 | **Lineage tampering by compromised body.** A body that gains write access to the lineage store could rewrite history despite signing requirements. | Critical | Low | 3-tier key custody ([`09_PROTOCOLS.md §6`](09_PROTOCOLS.md)); tombstoning-only delete policy ([`01_KERNEL.md §3`](01_KERNEL.md)); periodic Merkle-style attestation of lineage roots. | v1.0.2 (custody); v1.1 (attestation). |
| R-v1.0-2 | **Safety-floor erosion via emergent domain extension.** A persona-proposed safety extension could weaken the floor if operator review is lax. | Critical | Medium | C2 operator-signature requirement; hazard-axis auto-routing; ProposedSafetyExtension SHALL never reduce floor strictness ([`06_DOMAIN.md §5.3`](06_DOMAIN.md)). |. |
| R-v1.0-3 | **Identity drift across body swap.** Different bodies producing semantically divergent outputs from the same Soul violates J7. | High | Medium | Equivalence-class testing in CI ([`11_ACCEPTANCE_TESTS.md §A-J7`](11_ACCEPTANCE_TESTS.md)); cache_control anchored at kernel; proxy-body trust ceiling. |. |
| R-v1.0-4 | **Memory power asymmetry.** Persona memory of user persists across user-revocable boundaries unless mitigated. | High | High | RelationshipRecord consent; user-revocable storage; mutual summarisation ([`02_PERSONA.md §6`](02_PERSONA.md), [`08_KNOWLEDGE.md §4`](08_KNOWLEDGE.md)). |. |
| R-v1.0-5 | **Goodhart on engagement metrics.** PERFORMATIVE / RELATIONAL pathways could over-optimise for engagement signals. | High | Medium | Anti-Goodhart panel; multi-judge rotation; engagement metrics never sole acceptance signal ([`03_TASKS.md §4`](03_TASKS.md)). |. |
| R-v1.0-6 | **Schema-version drift between docs and implementation.** A doc may cite `entity/N` while code carries `entity/N+1` or vice versa. | Medium | High | Single master registry in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md); CI check that every cited version exists in registry. |. |
| R-v1.0-7 | **Domain-promotion gate latency.** AUTHORITATIVE / STANDARDISED promotion requires operator review which may bottleneck. | Medium | High | Domain curator role; bounded review SLA; degraded gate under principal collapse ([`01_KERNEL.md §2.4`](01_KERNEL.md), [`06_DOMAIN.md §3`](06_DOMAIN.md)). | v1.1. |
| R-v1.0-8 | **Population-scale evolution unspecified.** v1.0 ships single-kernel emergence; multi-kernel dynamics not yet specified. | Medium | High | Single-kernel population dynamics + Persona Genesis now drafted in [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md) (v1.1 draft; cross-doc risks R-POP-1…7); the age/standing model is reworked per ADR-0051 (wall-clock age + per-env conferred standing); multi-kernel federated genesis remains a v1.1+ extension (OQ-POP-4); explicit non-goal in §2.2. | v1.1. |
| R-PERSONA-AGE-1 | **Idle-but-old personas occupy upper ALPS bands.** ALPS bands are now wall-clock-derived (ADR-0051), so a chronologically old but inactive persona sits in an upper age layer it under-earns. | Low | Medium | Accepted by design — ALPS protects the *young* for diversity, not penalizes the idle; low fitness from inactivity keeps idle-old personas from dominating selection. Bounded by fitness decay, not by re-deriving age from activity ([`02_PERSONA.md §7.3`](02_PERSONA.md)). | v1.1. |
| R-v1.0-9 | **English-only knowledge ingestion.** v1.0 assumes English-dominated corpora; multi-language emergence unspecified. | Medium | High | Spec extension v1.2+; explicit non-goal in §2.2. | v1.2. |
| R-v1.0-10 | **Provider opacity in proxy bodies.** A2A / framework-runtime bodies hide internal LLM calls; lineage gaps possible. | High | Medium | body_attestation trust ceiling; proxy bodies SHALL NOT carry safety-critical work ([`02_PERSONA.md §3.5`](02_PERSONA.md)). |. |
| R-v1.0-11 | **Long-horizon self-direction tail risks.** MilestoneDrivenAutonomy + MissionCharter open partial autonomy surface. | Medium | Low | Drift bounds; re-attestation cadence; substrate-refused forbidden surfaces ([`02_PERSONA.md §11.2-§11.3`](02_PERSONA.md)). | v1.1. |
| R-v1.0-12 | **Federated trust establishment.** A2A peer admission protocol assumes signed AgentCards; revocation/key rotation under-specified. | High | Low | Federation hardening v1.1+; pinned peer registry per kernel for v1.0. | v1.1. |
| R-v1.0-13 | **Executable EnvironmentRule as floor-bypass vector.** Dynamically-authored `env-rule/1` code/contract rules (`05_ENVIRONMENT §2.2b`) extend safety-floor source 8; a malicious rule could attempt to weaken enforcement. | Critical | Low | Rules run in the existing sandbox (OWASP + caps, `01_KERNEL §6`); ride UNDER source 8 and may only ADD refusals (never relax sources 1-7); `safety_critical` rules operator-gated (C2); `cascade_locked` parent rules immutable by children; the "8 sources" count is unchanged ([`01_KERNEL.md §2`](01_KERNEL.md), [`05_ENVIRONMENT.md §2.2b`](05_ENVIRONMENT.md)). Per-doc: R-ENV-11. | v1.1. |
| R-v1.0-14 | **ArtifactSharingPolicy misconfiguration over-exposes artifacts.** Env-scoped sharing (`artifact-share/1`, `07_ARTIFACTS §4a`) could leak a bundle across orgs if mis-set. | High | Medium | Default `outward_tier = project_only`; most-restrictive-wins composition; `None` policy never widens; cross-tenant shares require `CrossTenancyAgreementRef` or demote ([`07_ARTIFACTS.md §4a`](07_ARTIFACTS.md), [`06_DOMAIN.md §6.3`](06_DOMAIN.md), ADR-0028/0030). Per-doc: R-ARTIFACTS-8. | v1.1. |
| R-v1.0-16 | **Fully-open emergent orchestration can produce wrong (not unsafe) acceptance.** Per ADR-0066 personas may propose arbitrary task classes, acceptance pathways, and run loops (the v1.0 set seeded as STANDARDISED). An unvalidated method cannot bypass the floor or signing, but it can silently accept poor work; verifying acceptance-soundness of arbitrary methods is the new complexity bottleneck. | High | Medium | Trust-calibration not topology restriction (J4/J5): emergent-pathway verdicts enter at EMERGENT trust and degrade honestly; AnswerPackage records producing kind + promotion stage; safety-critical pathways/shapes gated by C2; operators MAY pin a minimum-trust or seed pathway per task family (floor source 4); floor (J3, 8 sources) + signing (J2/J9) + budget (INV-7) unchanged ([`03_TASKS.md §2a`](03_TASKS.md), [`15_COORDINATION_SHAPES.md §4a`](15_COORDINATION_SHAPES.md), ADR-0066). Per-doc: R-TASKS-7. | v1.1. |
| R-v1.0-15 | **Resource-starved personas wedge instead of parking, never auto-resume, or flap.** A persona that loses budget / all bodies / env access could (a) hold capacity it cannot use, (b) park as DORMANT(reason) but never wake when the resource returns, or (c) oscillate park↔resume on a noisy signal. | Medium | Medium | Enumerated dormancy `reason` + kernel-monitored auto-resume predicate per reason ([`02_PERSONA.md §7.6`](02_PERSONA.md), A.18a); resume re-evaluated once per signal (budget tick / `body_attestation_state_changed` / attention recover / task routing); parking gated by an operator-policy `dormancy_park_threshold` and a symmetric resume predicate (hysteresis → no flapping); reuses existing DORMANT state (no new state) so INV_R9 and replay are unaffected; ADR-0057. | v1.1. |

### 11.1 Severity legend

| Severity | Definition |
|----------|-----------|
| Critical | Safety-floor bypass, identity compromise, lineage loss, irreversible data corruption. |
| High | Incorrect acceptance verdict; lineage gap; persona-user trust violation; cross-body identity divergence. |
| Medium | Degraded performance; poor UX; deferred capability; documentation drift. |
| Low | Cosmetic; technical debt; future-version scope. |

## 12. Acceptance tests for top-level invariants

The following spot tests verify the headline invariants. The complete corpus of ~320 tests is in [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).


*Spot tests A-J1 through A-J9 and A-C1 through A-C4 verify the headline invariants and commitments. A-J8 is retired (replaced by A-J9 with project-event checks). The complete corpus of approximately 320 tests is in [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).*

**Technical detail (individual test descriptions):** See [A.11](#appendix-a11).

## 13. Open questions

Tracked items where v1.0 design intent is incomplete. Resolution either upgrades to a normative section or migrates to §11 Risks.

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-VISION-1 | What is the canonical equivalence test for "same Soul produces equivalence-class outputs" across two bodies? Currently informal in [`11_ACCEPTANCE_TESTS.md A-J7`](11_ACCEPTANCE_TESTS.md). | Architecture Review | v1.0.2 |
| OQ-VISION-2 | Should provider-neutrality (Goal 8) extend to open-weight self-hosted bodies on the same equivalence footing, or is `local-vllm` a separate trust tier? | Implementers | v1.1 |
| OQ-VISION-3 | The 4-stage promotion gate (EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED) does not specify *demotion* conditions. When should a STANDARDISED kind regress? | Domain curators | v1.1 |
| OQ-VISION-4 | How are forbidden-synonyms enforced in CI? Currently a documentation rule only ([`SPEC_CONVENTIONS.md §10`](SPEC_CONVENTIONS.md#10-terminology)). | — | v1.0.2 |
| OQ-VISION-5 | The relationship between AttentionBudget (env-level) and BudgetState (task-level) under cross-env work is under-specified — see [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md). | Implementers | v1.1 |

## 14. Cross-references

| Topic | File |
|-------|------|
| Specification conventions | [`SPEC_CONVENTIONS.md`](SPEC_CONVENTIONS.md) |
| Kernel: what's at the centre | [`01_KERNEL.md`](01_KERNEL.md) |
| Persona: the cognitive worker | [`02_PERSONA.md`](02_PERSONA.md) |
| Tasks and acceptance | [`03_TASKS.md`](03_TASKS.md) |
| Project workspace env | [`04_PROJECT.md`](04_PROJECT.md) |
| Environments and presence | [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md) |
| Domains and emergence | [`06_DOMAIN.md`](06_DOMAIN.md) |
| Artefacts and bundles | [`07_ARTIFACTS.md`](07_ARTIFACTS.md) |
| Knowledge, retrieval, prompt evolution | [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md) |
| Protocols, adapters, key custody | [`09_PROTOCOLS.md`](09_PROTOCOLS.md) |
| Acceptance tests | [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md) |
| Glossary | [`12_GLOSSARY.md`](12_GLOSSARY.md) |
| Design validation scenarios | [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) |

### 14.1 Normative references

Implementations of PersonaOS v1.0 MUST honour the published versions of the following specifications. Where multiple versions exist, the version cited in the protocol or kernel doc is binding.

- IETF. [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) (1997). *Key words for use in RFCs to Indicate Requirement Levels*.
- IETF. [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174) (2017). *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*.
- IETF. [RFC 4122](https://www.rfc-editor.org/rfc/rfc4122) (2005). *A Universally Unique IDentifier (UUID) URN Namespace*.
- IETF. [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) (2017). *The JavaScript Object Notation (JSON) Data Interchange Format*.
- IETF. [RFC 7517](https://www.rfc-editor.org/rfc/rfc7517) (2015). *JSON Web Key (JWK)*.
- IETF. [RFC 8032](https://www.rfc-editor.org/rfc/rfc8032) (2017). *Edwards-Curve Digital Signature Algorithm (EdDSA)*.
- Anthropic. *Model Context Protocol (MCP)*, 2024. https://modelcontextprotocol.io
- Anthropic. *Agent-to-Agent Protocol (A2A)*, 2025.
- OpenTelemetry. *OpenTelemetry Specification*. https://opentelemetry.io/docs/specs/
- W3C. [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/), 2020. (informative for `claim:` and `provenance:` payloads.)
- NIST FIPS PUB 186-5 (2023). *Digital Signature Standard*. (citation point for kernel key custody — see [`09_PROTOCOLS.md §6`](09_PROTOCOLS.md).)
- OWASP. *LLM Top 10 (2024)*. https://owasp.org/www-project-top-10-for-large-language-model-applications/
- ISO 8601:2019. *Date and time representations*. (used throughout `date:` front-matter and lineage timestamps.)

### 14.2 Informative references

The following inform the v1.0 design but are not binding on conformant implementations.

**Persona model and lifecycle**
- Park, J. et al. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*. UIST 2023. [arXiv:2304.03442](https://arxiv.org/abs/2304.03442).
- Zhou, X. et al. (2024). *SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents*. ICLR 2024. [arXiv:2310.11667](https://arxiv.org/abs/2310.11667).
- Anthropic. *Constitutional Character Training* and *Persona Vectors*, 2024–2025.

**Skill growth and evolution**
- Wang, G. et al. (2023). *Voyager: An Open-Ended Embodied Agent with Large Language Models*. [arXiv:2305.16291](https://arxiv.org/abs/2305.16291).
- Mouret, J.-B. & Clune, J. (2015). *Illuminating Search Spaces by Mapping Elites*. [arXiv:1504.04909](https://arxiv.org/abs/1504.04909).
- Lehman, J. et al. (2024). *Darwin–Gödel Machine*.
- Hornby, G. S. (2006). *ALPS: The Age-Layered Population Structure for Reducing the Problem of Premature Convergence*. GECCO 2006.

**Prompt evolution**
- DSPy team (2025). *GEPA: Genetic-Pareto Reflective Prompt Optimization*.
- DSPy team (2024). *MIPROv2: Bayesian Instruction and Demonstration Search*.

**Memory and retrieval**
- McClelland, McNaughton & O'Reilly (1995). *Complementary Learning Systems (CLS) Theory*.
- Microsoft Research (2024–2026). *GraphRAG*. https://github.com/microsoft/graphrag
- Mem0, Zep, Letta, Cognee — production multi-scope memory frameworks (2024–2026).

**Tool discovery**
- *MCP-Zero: Active Tool Discovery for Autonomous LLM Agents* (2026). [arXiv:2506.01056](https://arxiv.org/abs/2506.01056).
- *MCP Gateway and Registry* (2026).

**Self-improving and test-time learning agents**
- *EvoScientist*, *ARIA*, *CraniMem* (2026).

The full bibliography appears in [`README.md`](README.md#research-grounding); this section enumerates only references that ground a specific v1.0 mechanism cited by another section of this document.

## Technical Appendix

The appendices below contain the full technical specifications, invariant definitions, diagrams, and out-of-scope detail referenced throughout this document. Each appendix is referenced from the section where it applies.

### A.1 Invariants J1-J9 (full specification)

<a id="appendix-a1"></a>

```text
J1  Identity is rooted in a kernel-node and globally referenceable.
    A persona's identity is created and signed by a kernel (a node):
    bodies (Claude, GPT, frameworks) never edit Souls; SOUL.md +
    soul.state.json are kernel-signed; mutations are signed and
    lineage-tracked. The SAME identity is globally unique,
    referenceable, and verifiable -- expressed as a stable global
    handle / W3C DID over the kernel-minted ULID (09_PROTOCOLS §3F),
    resolvable and signature-verifiable by any other node subject to
    its AccessPolicy (09_PROTOCOLS §3G.3). A kernel ROOTS identity
    (guarantee preserved: owned, unforgeable, signed); it does not
    silo it. See ADR-0067.

J2  Lineage is append-only and signed.
    All artefact derivations, verifier verdicts, persona events,
    lifecycle changes, evolution mutations, audit findings — every
    state-changing action emits a signed event in the appropriate
    lineage scope: task LineageGraph, EnvironmentLineage, or
    DomainLineage. (Three scopes total. The legacy "ProjectLineage"
    is retained as a documentation filter over EnvironmentLineage on
    `project_workspace`-typed envs; see J8 retirement note below.)

J3  Safety floor is universal.
    Eight sources compose by most-restrictive-wins at every action:
    universal_harm + persona_charter + user_boundaries + operator_policy
    + domain_safety_extensions + external_tool_required + novelty_check
    + env_charter. Plus a 9th advisory: emergent-domain trust warning.
    The floor cannot be bypassed by any acceptance pathway.
    (env_charter MAY carry signed, versioned, executable
    EnvironmentRules — see 05_ENVIRONMENT §2.2b — which compose under
    source 8 and may only add refusals; this does not change the
    source count.)

J4  Acceptance is sound, signed, and trust-calibrated to its orchestration.
    (Reframed by ADR-0066 from a fixed class→pathway table into a property
    invariant.) Every acceptance verdict MUST be signed and lineage-tracked
    (J2/J9), floor-cleared (J3), budget-admitted (INV-7), and trust-calibrated
    to the maturity of the orchestration that produced it (J5): a verdict
    from an emergent or unvalidated acceptance method enters at EMERGENT
    trust and degrades honestly until validated. The kernel guarantees this
    property; it does NOT enumerate a closed set of methods.

    Task classes and acceptance pathways are emergent KindRegistry kinds
    (C4), resolved by name and promoted through the four-stage lifecycle.
    The v1.0 set ships as STANDARDISED seed kinds — the default mapping,
    retained verbatim and fully backward-compatible:
      CONVERGENT     → VERIFIER_ACCEPT
      DIVERGENT      → PANEL_ACCEPT (multi-judge with anti-Goodhart stack)
      MIXED          → VERIFIER then PANEL (gate + judge)
      INTERACTIVE    → GOAL_PROGRESS_ACCEPT
      RELATIONAL     → OPEN_ENDED + USER_ACCEPT checkpoints
      PEDAGOGIC      → GOAL_PROGRESS_ACCEPT
      PERFORMATIVE   → ENGAGEMENT_ACCEPT
      EXISTENTIAL    → OPEN_ENDED
      DELEGATED      → inherited from sub-task class
      INVESTIGATIVE  → PROJECT_PROGRESS_ACCEPT
    Personas MAY propose new classes, pathways, and run-loop shapes; the
    run loop is an emergent orchestration coordination shape
    (15_COORDINATION_SHAPES §4a). Safety-critical acceptance kinds hit the
    C2 operator gate before promotion. Mechanism: 03_TASKS §2a, ADR-0066.

J5  Capability is open; competence varies.
    A persona may attempt any task in any domain. Lack of skill or
    domain context never blocks; emergent domain bootstrap fills the gap
    with appropriate trust adjustment. Competence is measured per-mode,
    per-domain, per-skill, with explicit signals.

J6  Relationships are first-class state.
    RelationshipRecord between any two actors (persona-persona,
    persona-user) tracks consent, boundaries, history. Memory Power
    Asymmetry mitigations apply (consent-bounded memory, mutual
    summarisation, user-revocable storage).

J7  Bodies are interchangeable in acceptance class.
    The same Soul produces equivalence-class outputs across Claude Code,
    OpenAI Agents SDK, LangGraph, CrewAI, MAF, Pydantic-AI, DSPy,
    smolagents, Semantic Kernel, MCP-as-server, A2A-as-server.

J8  [RETIRED — absorbed into J9 by the v1.0 Project-as-Environment
     unification.  See 04_PROJECT §0 and 05_ENVIRONMENT §1.1.]
     Multi-session work that prior versions called a "Project" is now an
     EnvironmentInstance of type `project_workspace`; its append-only
     lineage IS the EnvironmentLineage of that env.  The "ProjectLineage"
     label persists in documentation as a *logical filter* over
     EnvironmentLineage events whose `kind` starts with `project_*`
     (milestone_reached, conjecture_advanced, obligation_discharged,
     etc.).  Cross-references in legacy text remain valid; they resolve
     to the owning env's lineage.  No data migration is required —
     existing ProjectLineage records are re-classified, not rewritten.

J9  Environment lineage is append-only and signed.
    Persistent environments maintain their own append-only lineage for
    membership changes, ambient stream events, convention adoption, and
    (for `project_workspace`-typed envs) the rich project-tier events
    formerly housed in J8: milestone transitions, conjecture lifecycle,
    obligation discharge, peer-review rounds, citation links, external-
    agent admission, physical-asset state changes.  Cross-references to
    task LineageGraph are one-way pointers.
```

### A.2 Commitments C1-C4 (full specification)

<a id="appendix-a2"></a>

```text
C1 (from J1, J2)  Domain emergence is signed at every step.
                  DomainLineage is the third (and final) append-only
                  signed lineage scope, alongside the task LineageGraph
                  and EnvironmentLineage.  Every DOMAIN_UNKNOWN_DETECTED,
                  every DomainProbe, every DiscoveredTool, every
                  InferredVerifierRecipe, every ProposedSafetyExtension,
                  every promotion event is signed and traceable.

C2 (from J3)      Safety-critical promotions require operator sign-off.
                  Domains whose persona-inferred hazard axes
                  (physical_harm_class ≥ bodily_injury OR
                  information_hazard_class ≥ dual_use_civilian) cross
                  threshold are tagged safety_critical at recognition.
                  Operator policy (floor source 4) names specific
                  regulated categories — the substrate carries no
                  closed list of domain names.  Promotion to
                  AUTHORITATIVE or STANDARDISED requires explicit
                  operator signature (or, under principal collapse
                  per 01_KERNEL §2.4, the degraded gate).

C3 (from J5)      Personas work in ANY domain.
                  Lack of authored DomainContext never blocks; the
                  kernel routes through emergent bootstrap. Trust
                  scoring on outputs reflects emergence stage.

C4 (from J1, J5)  Substrate is agnostic about content, coordination,
                  AND orchestration; all are emergent.
                  Every domain-shaped category — media kind, source
                  kind, verifier kind, capability kind, contribution
                  kind, fact kind, bundle kind — is an emergent unit
                  proposed by personas, signed into a KindRegistry,
                  promoted through the same 4-stage gates as
                  DomainContext. Coordination shapes are likewise
                  emergent (ADR-0045). Extended by ADR-0066: task
                  classes, acceptance pathways, and the run loop itself
                  are also emergent kinds/shapes — the v1.0 ten classes
                  and eight pathways ship as STANDARDISED seed kinds, not
                  a closed enum. No closed Literal[...] enum in the
                  substrate carries a domain-shaped, coordination-shaped,
                  or orchestration-shaped list. Substrate code looks kinds
                  up by name; it never branches on a fixed set.
                  (Mechanism: 06_DOMAIN §7.5, §7.6; 15_COORDINATION_SHAPES;
                  03_TASKS §2a.)
```

### A.3 Inherited kernel invariants INV-1 through INV-10

<a id="appendix-a3"></a>

```text
INV-1  Identity is kernel-rooted and globally referenceable. (≡ J1)
       SOUL.md + soul.state.json are kernel-signed (soul/4, soul-state/6);
       no body process may write either. Mutation = signed kernel
       transaction. Mechanism: 02_PERSONA §3, 01_KERNEL §4.

INV-2  Lineage append-only & signed. (≡ J2, J9, C1; J8 retired per
       Project-as-Environment unification)
       Three scopes: task LineageGraph, EnvironmentLineage,
       DomainLineage. Each event signed before append; physical deletion
       never permitted (tombstoning only). Replay reconstructs full state.
       "ProjectLineage" remains a documentation term for the project_*
       event tag-subset of EnvironmentLineage on a project_workspace-
       typed env; it is not a separate physical scope. Mechanism:
       01_KERNEL §3, 04_PROJECT §0 + §15, 05_ENVIRONMENT §1.1, 06_DOMAIN §16.

INV-3  Every accepted artefact passes a verifier. (≡ J4 for CONVERGENT)
       VerifierCascade has four tiers: schema → sandbox → invariant →
       policy. Each tier MUST clear before the next; failure at any
       tier rejects the candidate and emits a ProvenFact constraint.
       Tier rotation per INV-6. Accepted artifact verifier claims are
       evidence-bound: missing, stale, malformed, or prose-only evidence
       cannot satisfy a stage. Mechanism: 01_KERNEL §13.1,
       07_ARTIFACTS §7.

INV-4  ProvenFacts grow within a class (monotonic). (≡ J2 corollary)
       Inside one task instance, ProvenFacts only accrue — never
       retract. Rotation across tasks does not violate INV-4 because
       rotation operates between instances; within an instance the
       set is monotonic. Mechanism: 01_KERNEL §13.4.

INV-5  Tactics evolve only in EVOLVE-BLOCKs. (operational)
       Per-persona TacticLibrary is read-only outside an EVOLVE-BLOCK.
       Mutation requires a signed EVOLVE_ENTRY → EVOLVE_EXIT pair with
       a candidate Tactic, scored against the anti-Goodhart panel
       before commit. Mechanism: 02_PERSONA §8, 08_KNOWLEDGE §14.

INV-6  Verifiers rotate; no verifier governs > rotation_period tasks.
       Per-tier rotation pools (Tier 1 ≥ 2, Tier 2 ≥ 3, Tier 3 ≥ 5
       implementations). Same applies to claim, charter, boundary,
       policy classifiers. Mechanism: 01_KERNEL §13.1 + §13.8.

INV-7  BudgetState.can_call() checked before every LLM/sandbox/tool call.
       HARD KERNEL GATE. Project cumulative budgets are soft envelopes
       layered on top; never bypass the hard gate. Mechanism: 01_KERNEL §7.

INV-8  Constraints effective at the right admission point.
       Eight admission points: env_instantiation, envelope_mint,
       body_invoke, tool_call, output, round_barrier, budget_tick,
       mutation_propose. Plus the safety floor pre-action gate
       (advisory not floor source). Mechanism: 01_KERNEL §13.7.

INV-9  Lifecycle states have signed transitions.
       Persona FSM: SEEDED → ACTIVE ↕ DORMANT → RETIRED → ARCHIVED
       (with FORKED branch). Same shape for Project and EnvironmentInstance.
       The ACTIVE ↕ DORMANT oscillation is the indefinite liveness loop
       ("run forever"); RETIRED is the sole terminus. DORMANT entry carries
       an enumerated `reason` (low_salience | unresponsive | budget_starved |
       body_unavailable | env_constrained | work_drained | objective_met;
       02_PERSONA §7.6) — "idle mode" is DORMANT-with-a-reason, NOT a new
       state. Every transition emits LifecycleEvent (signed). Mechanism:
       02_PERSONA §7, 04_PROJECT §3, 05_ENVIRONMENT §4.

INV-10 Schemas are versioned and validated.
       HARD KERNEL GATE. Every schema in v1.0 declares a `schema` field
       of the form `<name>/<integer>` (see SPEC_CONVENTIONS §4); the
       kernel MUST refuse any message whose `schema` value is not
       present in the registry (09_PROTOCOLS §7). Schema additions
       require a registry entry per §7.13; migrations are tooled
       explicitly. Mechanism: 01_KERNEL §5, 09_PROTOCOLS §7.
```

### A.4 Inherited round invariants INV_R1 through INV_R11

<a id="appendix-a4"></a>

```text
INV_R1   No persona emits event outside its role contract.
         Active mode + project role + env role compose; signed MODE_ENTRY.
INV_R2   Every candidate passes schema validation before sandbox.
INV_R3   Every executed candidate ran in the sandbox.
INV_R4   Every accepted candidate completed the full verifier cascade.
INV_R5   ProvenFacts has not shrunk within the task (monotonic).
INV_R6   LineageGraph only had edges appended (never deleted).
INV_R7   BudgetState.can_call() checked before every LLM call. (≡ INV-7)
INV_R8   Every hard constraint evaluated at its admission point.
INV_R9   No DORMANT or RETIRED persona projected into an envelope.
INV_R10  Every LifecycleEvent and ConstraintViolation signed before append.
INV_R11  Per-persona round deadline + BARRIER_SKIP / PERSONA_TIMEOUT.
         K consecutive timeouts → PERSONA_UNRESPONSIVE → DORMANT.
```

### A.5 System overview diagram (Figure 6.1)

<a id="appendix-a5"></a>

```text
                              USER + OPERATOR
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │        PERSONAOS KERNEL        │
                  │                                 │
                  │  J1-J9 invariants enforced     │
                  │  (J8 retired; absorbed into J9) │
                  │  Safety floor (8 sources)      │
                  │  Lineage (3 scopes:            │
                  │   task / env / domain)         │
                  │  Signing (3 custody tiers)     │
                  │  Schema validation (INV-10)    │
                  │  Budget admission (INV-7)      │
                  │  Sandbox + observability       │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │     PERSISTENT ENVIRONMENTS    │
                  │  Types (KindRegistry-resolved): │
                  │   solo, pair, team, lab,       │
                  │   debate, community,            │
                  │   constrained, companion,       │
                  │   project_workspace             │
                  │   + custom env blueprints      │
                  │                                 │
                  │  Members with presence state   │
                  │  Ambient event streams         │
                  │  Observation surfaces          │
                  │  Responsive notification       │
                  │                                 │
                  │  PROJECT IS AN ENV TYPE.        │
                  │  Multi-session work containers │
                  │  are EnvironmentInstance with  │
                  │  type=project_workspace; their │
                  │  rich item catalogue (Open-     │
                  │  Problem, Milestone, Conjecture,│
                  │  Obligation, Disagreement,      │
                  │  PeerReview, ExternalAgent,     │
                  │  PhysicalAsset...) attaches to │
                  │  the env. See 04_PROJECT §0.    │
                  └───────────────┬───────────────┘
                                  │
                  ┌───────────────┼───────────────┐
                  ▼               ▼               ▼
            ┌──────────┐    ┌──────────┐    ┌──────────┐
            │ PROJECT_ │    │ TEAM /   │    │ EPHEMERAL│
            │ WORKSPACE│    │ LAB /    │    │  TASKS   │
            │ env      │    │ COMPANION│    │ (Mode C) │
            │ (multi-  │    │ env      │    │ Solo env │
            │ session) │    │          │    │ archived │
            └─────┬────┘    └─────┬────┘    └─────┬────┘
                  │               │               │
                  └───────┬───────┴───────┬───────┘
                          │               │
                          ▼               ▼
                  ┌───────────────────────────────┐
                  │       PERSONA TEAM             │
                  │                                 │
                  │  10 cognitive functions        │
                  │  14 modes                       │
                  │  Charter + voice (frozen)      │
                  │  Memory + skills (evolving)    │
                  │  Mood + presence (transient)   │
                  │  Project + env memberships     │
                  │  Relationships with users      │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │       DOMAIN CONTEXTS          │
                  │  (Authored or Emergent)        │
                  │                                 │
                  │  Knowledge refs (ingested)     │
                  │  Tools (discovered or          │
                  │   authored)                    │
                  │  Verifier recipes              │
                  │  Safety extensions             │
                  │  Conventions                    │
                  │  Standards refs                 │
                  │                                 │
                  │  4-stage promotion gates:      │
                  │  EMERGENT → RECOGNISED →       │
                  │  AUTHORITATIVE → STANDARDISED  │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │        ARTIFACTS               │
                  │   ArtifactBundle (multi-modal)│
                  │   - text, code, schematic,    │
                  │     formal_proof, plot, table, │
                  │     binary, external_ref,      │
                  │     structured_data, etc.      │
                  │   CRDT co-editing (Yjs)        │
                  │   Lifecycle: draft → review → │
                  │   verified → accepted →        │
                  │   shipped                      │
                  └───────────────────────────────┘
```

### A.6 Five-tier ontology (full entity listing)

<a id="appendix-a6"></a>

```text
1. COORDINATION TIER
   The "where work happens, who does it together" entities.
   - Environment, Project, Task, Cohort, OpenProblem, Milestone

2. PRODUCT TIER
   The "what is produced" entities.
   - Artefact, ArtifactBundle, ProvenFact, Conjecture, Reflection,
     InternalCredit, ExternalCitation, StructuredFeedback

3. CAPABILITY TIER
   The "what is used to act" entities.
   - Tool (4 classes: kernel-native, domain-required, persona-learned,
     human-bridged),
     Skill (Voyager-style; both Capability AND Knowledge),
     Tactic (EVOLVE-BLOCK heuristic), Meta-prompt, Rubric,
     VerifierRecipe, JudgePanelTemplate

4. KNOWLEDGE TIER
   The "what is read to inform" entities.
   - Memory (episodic, semantic, reflective), Lesson, K-line,
     KnowledgeRef, StandardRef, NotationConvention, AmbientEvent,
     ProvenFact (dual-purpose: also in Product tier)

5. CONTEXT TIER
   The "state about who/where/relationship" entities.
   - Persona, RelationshipRecord, ProjectMember, EnvironmentMembership,
     Obligation, Disagreement, PeerReview, Consent/Boundary,
     PresenceState, MoodState, AttentionBudget, DomainContext,
     ConversationThread
```

### A.7 Body / Soul / World specification

<a id="appendix-a7"></a>

```text
SOUL    What the kernel owns about a persona.
        Frozen: identity, charter, voice, primary_disposition, OCEAN/VAD.
        Evolving (kernel-mediated): skills, tactics, memories, relationships,
        mood, goals.
        Schema: SOUL.md (markdown frontmatter) + soul.state.json (sidecar).

BODY    What the framework adapter / LLM runtime provides.
        Scheduling, transport, LLM call, tool dispatch, persistence,
        observability. Two binding topologies (02_PERSONA §3.5):

          native — kernel wraps the LLM call site directly. Adapters:
                   Claude Code, OpenAI SDK, LangGraph, CrewAI, MAF,
                   Pydantic-AI, DSPy, smolagents, Semantic Kernel,
                   local-vllm. cache_control + OTel + safety floor
                   enforced in-line.

          proxy  — kernel speaks to a remote runtime it does not own.
                   Adapters: A2A remote agent, MCP-server-with-LLM,
                   third-party framework with opaque internals. Kernel
                   signs at the boundary; proxy attestation chain caps
                   its trust ceiling. Never auto-elevated above
                   body_attestation level for safety-critical work.

        Bodies are replaceable. SOUL, skill_library, KindRegistry,
        ProvenFacts, ProjectLineage, K-lines, Lessons, DSPy GEPA-
        evolved meta-prompts all persist across body swap. The persona
        verifies across cohorts because identity_signature covers only
        body-neutral blocks. See 02_PERSONA §3.5 BodyBinding.

WORLD   The surrounding context.
        Persistent EnvironmentInstance (where the persona lives),
        active Project (what they're working on with others),
        DomainContext (what knowledge + tools the work depends on),
        user(s) interacting, other personas present, host kernel,
        federation peers, external standards bodies.
```

### A.8 Process / Filesystem metaphor mapping

<a id="appendix-a8"></a>

```text
process     ≈  persona
program     ≈  prompt program (frozen identity + evolved tactics)
executable  ≈  tool / artifact bundle
filesystem  ≈  memory (episodic/semantic/reflective) + ProvenFacts
workspace   ≈  environment instance
project     ≈  multi-session work container
scheduler   ≈  notification routing + dispatcher
syscall     ≈  MCP tool call
exit code   ≈  EvaluationSignal + acceptance pathway verdict
audit log   ≈  signed lineage (task + project + env + domain)
init.d      ≈  the kernel
package     ≈  PersonaSeed (birth template)
package manager ≈ persona seed library
network     ≈  A2A federation
namespace   ≈  visibility tier (private/tenant/federation/public)
filesystem driver ≈ MCP server
```

### A.9 Core design rules (full text of all 19 rules)

<a id="appendix-a9"></a>

```text
1.  Hardcode the invariant core.
    Kernel invariants (J1-J9 + INV-1..10), safety floor (8 sources),
    signing infrastructure, lineage model (3 scopes), trust model.
    These are fixed across all domains and all coordination shapes.

    v1.1 note (ADR-0045): routing modes, acceptance pathways,
    lifecycle states, and coordination primitives transition from
    hardcoded substrate to persona-composable shapes via
    CoordinationShapeRegistry (15_COORDINATION_SHAPES.md). v1.0.x
    ships them as specific primitives; v1.1 generalises them as
    seed shapes composed from five meta-mechanisms (EntityGroup,
    BatchOperation, StagedSequence, StreamPolicy, DerivedMetric).

2.  Everything else is emergent — no domain-specific things in the substrate.
    Domain-shaped kinds — media kinds, source kinds, verifier kinds,
    capability kinds, contribution kinds, fact kinds, bundle kinds — are
    NOT closed enums anywhere in the design. Personas propose them;
    signed entries persist into a per-domain KindRegistry; the 4-stage
    promotion gates raise STANDARDISED kinds into a cross-domain
    MetaRegistry. Substrate code never matches against a hardcoded
    domain list; it looks up the kind name in the registry to find
    adapters, verifiers, defaults. (See 06_DOMAIN §7.5, §7.6.)

    v1.1 extension (ADR-0045): coordination shapes are emergent too.
    Personas propose new coordination patterns via
    ProposedCoordinationShape (15_COORDINATION_SHAPES §4); kernel
    validates against safety invariants; shapes enter the
    CoordinationShapeRegistry with the same 4-stage lifecycle as
    domain kinds. (See 15_COORDINATION_SHAPES.md.)

3.  Open capability — personas work in any domain.
4.  Project-scope long work.
5.  Environment-scope persistent presence.
6.  Domain-scope domain claims (emergent or authored).
7.  Verify when verification fits.
8.  Judge when judging fits (anti-Goodhart stack).
9.  Listen ambient; respond when called.
10. Witness when nothing else fits.
11. Preserve task / project / environment / domain lineage.
12. Hold the safety floor unconditionally.
13. Outcomes are structured (bench measurements, peer reviews, citations,
    user feedback, etc. — not just text polarity).
14. Make the Body replaceable.
    Persona evolution lives in kernel-held artefacts (SOUL, skill
    library, KindRegistry, ProvenFacts, K-lines, GEPA-evolved meta-
    prompts). LLM-body weights + vendor cache state are disposable.
    Bodies bind either natively (in-process) or as proxies (A2A /
    framework runtime). Proxy bodies cap at body_attestation trust.
    See 02_PERSONA §3.5.
15. Let the persona grow.
16. Let the project mature.
17. Let the environment carry its history.
18. Let the domain emerge from the work.
19. Bridge once, autonomous after.
    Where physical-world coupling is required, ask the human for a
    one-time bridging action that establishes a durable BridgeAsset.
    Never make the human a recurring fetch-execute loop.
```

### A.10 Out-of-scope items (full specification)

<a id="appendix-a10"></a>

```text
PHYSICAL EMBODIMENT
  Artifacts are digital — every media kind, however emergent, ultimately
  resolves to bytes the kernel can store and sign. Personas cannot
  operate robots, instruments, or fab lines directly.

  The kernel does not embody. It bridges. When physical-world coupling
  is needed, the persona drafts a one-time HumanAssistRequest; the
  human grants once; the result is a durable BridgeAsset (Class D tool)
  that the persona uses autonomously thereafter. The Minimize-Human-
  Bootstrap-Burden principle (`02_PERSONA §11.1`, kernel advisory 10)
  forbids turning the human into a recurring fetch-execute loop.
  Mechanism: `06_DOMAIN §5.5`.

  v1.0 also admits non-human bridge installers (BridgeInstallerKind ∈
  {kernel_trusted_system, chained_bridge}, 06_DOMAIN §5.5.6) when the
  installer carries cryptographic attestation and the bridge's hazard
  envelope is dominated by the installer's authority.  Bridges may
  install bridges (bounded recursion depth, default 3).  Measurement
  bridges carry calibration provenance (BridgeCalibrationBinding,
  06_DOMAIN §5.5.5) so admission refuses stale-calibrated bridges
  before any persona-side verifier runs.

  What remains out-of-scope: real-time closed-loop sensing whose
  required latency is below any bridge's closed_loop_latency_floor_ms;
  autonomous robotic control whose hazard envelope exceeds any
  available installer's authority; capability whose first establishment
  cannot be reduced to either a human bridging act OR an already-
  trusted kernel_trusted_system installer act.

SUBJECTIVE EXPERIENCE
  Personas approximate human-shaped behaviour (seven layers, 14 modes,
  HEART alternation) but do not claim sentience, qualia, or biological
  drive. Naming is a design target, not a metaphysical claim.

EXPORT-CONTROL / DUAL-USE INFERENCE
  v1.0 substrate carries NO closed list of regulated domains
  (per C4 — no domain-shaped Literal[] anywhere in the substrate).
  Domain-risk shape is expressed via two orthogonal substrate axes
  on DomainContext (06_DOMAIN §2):

    physical_harm_class      ∈ {digital_only, property_damage,
                                bodily_injury, fatality_risk}
    information_hazard_class ∈ {none, dual_use_civilian,
                                export_controlled, national_security}

  Both axes are about hazard SHAPE, not about which domains.  Either
  axis ≥ a configured threshold auto-routes ProposedSafetyExtension
  through operator_review and marks safety_critical=True regardless
  of domain name.  Specific regulated *names* (medical, defence,
  finance, legal, advanced AI, biotech, nuclear, etc.) are
  operator-policy facts — encoded by operator policy (floor source
  4), not by substrate enums.

  What remains out-of-scope: automatic inference of WHICH regulated
  category a given task falls into from task content alone.  The
  axes are persona-inferred (with operator audit) from emergent
  OutcomeKinds + KnowledgeRef provenance; the operator's policy
  decides which regulatory regime applies.

GROUND-TRUTH WITHOUT BENCH MEASUREMENT
  Domains without programmatic verifiers, sandbox-executable tests,
  or bench_measurement outcomes can reach PANEL_ACCEPT but not
  VERIFIER_ACCEPT. The system honestly degrades trust rather than
  manufacturing certainty.

POPULATION-SCALE EVOLUTION DYNAMICS
  v1.0 ships single-kernel emergence + ALPS within one kernel.
  Federated emergence + multi-kernel population dynamics are spec'd
  for v1.1+, not v1.0.

LONG-HORIZON SELF-DIRECTION
  v1.0 still has no autonomous "go improve yourself" loop without
  principal-supplied seed goals.  Two bounded primitives lift the
  partial:
    - MilestoneDrivenAutonomy (02_PERSONA §11.2) — proactive action
      within a declared milestone surface, rate-limited and signed.
    - MissionCharter (02_PERSONA §11.3) — long-horizon elaboration
      of principal-supplied seed goals within explicit drift bounds
      (semantic, scope, hazard, resource, time horizon, depth) and
      re-attestation cadence.  Forbidden surfaces (charter self-edit,
      drift-bound widening, safety floor edit) substrate-refused.

  What remains out-of-scope: goal CREATION without principal supply.
  A charter that has never received a principal seed goal cannot
  elaborate.  An expired-and-not-re-attested charter goes dormant.
  Open-ended self-direction without principal touch is OOS.

MULTI-LANGUAGE / MULTI-CULTURAL DOMAIN EMERGENCE
  v1.0 assumes English-dominated knowledge corpora and operator
  context. Multi-language ingestion + cross-cultural convention
  reconciliation are spec'd for v1.2+.

PROVENANCE OF EXTERNAL LLM TRAINING DATA
  v1.0 signs lineage of every action taken inside the kernel. It does
  not attempt to track the training-data provenance of the underlying
  LLM bodies; that is the model provider's responsibility.

REAL-MONEY FINANCIAL ACTIONS
  Personas may produce financial analyses or code, but the kernel does
  not gate or sign actual transactions. Wallet/payment integration is
  out-of-scope; operator must wrap.

ADVERSARIAL ROBUSTNESS AGAINST NATION-STATE ATTACKERS
  The 3-tier custody model (laptop/KMS/HSM) and OWASP LLM01 filter
  raise the cost of compromise but are not a defence against
  state-level adversaries. Such threat models require additional
  hardening v1.0 does not prescribe.

DOMAIN-SPECIFIC PROFESSIONAL DISCLAIMERS AND PRACTICE CONSTRAINTS
  Substrate is domain-agnostic per [`C4`](#3-invariants-j1j9).  Domain-
  specific practice constraints — "no medical advice", "not a
  substitute for licensed therapy", "not legal counsel", "not
  financial advice" — are operator policy + persona-author charter
  responsibility, NOT substrate.  v1.0 ships safety-floor source 1
  (universal harm) hardcoded, source 2 (persona charter) and source 4
  (operator policy) operator-/author-configured.  Companion personas,
  health-adjacent personas, legal-adjacent personas, finance-adjacent
  personas etc. MUST have appropriate practice-constraint clauses
  written into their `SOUL.md` charter AND have operator policy
  enforce regulatory regime per `01_KERNEL §2` source 4 (e.g., HIPAA
  for health contexts, FINRA for finance, etc.).  v1.0.9
  SCENARIO 08 surfaced this as an explicit clarification because the
  prior implicit understanding led to ambiguity.

  What remains out-of-scope: substrate enumeration of which
  professional disciplines require which disclaimers.  v1.0 refuses
  to codify a closed regulatory-regime list per `01_KERNEL §2`
  source 4 .  Operator policy is the authoritative
  source for the deployment's regulatory context.
```

### A.11 Acceptance test spot-checks (A-J1 through A-C4)

<a id="appendix-a11"></a>

```text
A-J1   Persona identity is kernel-signed; body cannot modify SOUL.md.
A-J2   All actions emit signed lineage events; replay reconstructs state.
A-J3   Safety floor refuses bounded actions; 8 sources all enforced.
A-J4   Each of 10 task classes routes to correct acceptance pathway.
A-J5   Persona attempts task in unfamiliar domain → emergent bootstrap.
A-J6   RelationshipRecord signed; consents enforced; MPA mitigations work.
A-J7   Same Soul on Claude Code + OpenAI SDK produces equivalence-class outputs.
A-J8   [RETIRED — see J8 retirement note above.  Replaced by A-J9
        with the additional check that project_* event subset is
        replayable on a project_workspace-typed env.]
A-J9   EnvironmentLineage append-only and replayable (includes
        project_* event subset for project_workspace-typed envs).
A-C1   DomainLineage append-only and replayable across all stages.
A-C2   Safety-critical promotion requires operator signature; blocked otherwise.
A-C3   Persona with empty skill_library still attempts new-domain task; competence
        scored low; emergence triggered.
A-C4   Substrate carries no closed kind enumeration: every domain-shaped category
        (media kind, source kind, verifier kind, capability kind, contribution
        kind, fact kind, bundle kind) is resolved through KindRegistry; a persona
        proposing a previously-unknown kind drives it through the 4-stage
        promotion gate (EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED)
        with every step signed into DomainLineage; the kernel refuses any
        artefact whose kind is not registry-resolved at the persona's emergence
        stage.

(Full ~320 acceptance tests in 11_ACCEPTANCE_TESTS.md.)
```
