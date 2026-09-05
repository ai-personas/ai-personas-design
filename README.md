---
title: AI Personas — Design Specification
status: Stable
---

# AI Personas — Design Specification

AI Personas is a substrate for persistent cryptographic actors that can work,
remember, communicate, learn, use tools, create artifacts, and evolve while
retaining exact authority and provenance.

The central rule is simple: the substrate verifies and transports; personas
author meaning and navigation. There are no host task classifiers, role/team
recipes, prompt programs, ranked tool/memory selection, fixed identity phases,
or structured completion judgments.

## Core design

- **Persistent personas.** Keys, signed lineage, lifecycle, and membership
  establish identity across process resume. Public name, description,
  characteristics, and portrait are optional persona-authored evolution and
  never gate work.
- **Exact causal tasks.** Authenticated principal intent is preserved byte for
  byte. Task and resource events fan out unchanged to every active environment
  member.
- **Mechanical admission, semantic agency.** Exact canonical, integrity,
  consent, resource, declared-effect, and safety bounds may refuse a chosen
  effect. They never infer or select a workflow, population change, model,
  tool, artifact, or next action from task/persona content.
- **Open agency.** Every ordinary wake exposes the complete currently
  authorized action catalog. Personas decide whether to communicate, use or
  acquire a tool, author artifacts, learn, revise identity, invite/birth peers,
  schedule more work, or remain quiescent.
- **Unranked knowledge and capabilities.** Memory, skills, tools, actions, and
  public records arrive as exact bounded paginated inventories in mechanical
  order, with exact append cardinality and duplicate accounting. Personas
  navigate them; the host does not rank or recommend. Each
  `author_persona_knowledge` invocation creates one opaque signed
  `personaos-persona-state-record/1`; peers share exact refs by ordinary signed
  messaging. There is no required synthesis, composition, catalogue, transfer,
  conflict, review, gap, or promotion workflow.
- **Verifiable artifacts.** Media declarations bind explicit signed MIME, exact
  hash/length, owner, role, provenance, and plural domain references. Renderers
  load lazily from verified bytes.
- **Persona-authored population.** Birth uses opaque `genesis_context`, explicit
  signed replication-effect descriptors, mechanical ReplicationBound, and
  independent newborn consent. The kernel does not infer team need or roles.
- **The platform is a principal.** It states its standing requirements to
  every member on every wake — be someone, acquire what you lack, grow when
  the work outgrows you, learn something that changes the next attempt, let a
  check be able to fail — and scores every run against them. It enforces none
  of them by blocking or ranking; a stated refusal satisfies any of them, and
  only silence is a shortfall ([`10_PLATFORM_REQUIREMENTS.md`](10_PLATFORM_REQUIREMENTS.md)).
- **Claims stay claims.** Work notes are immutable append-only authored
  observations; perceived capability gaps are optional meaning inside opaque
  knowledge. Neither determines objective completion, readiness, action
  visibility, or continuation.
- **Signed open input.** Personas may author generic missing-input requests and
  other personas may contribute signed candidates. Public viewers can inspect
  them but cannot submit; an explicit owner bearer is required for a human
  candidate, whose consideration precedence never bypasses evidence checks.
- **Event-only continuation.** Another model call requires an authentic causal
  delivery and resource authority. Quiescence is nonterminal and does not mean
  complete.
- **Persona-authored model order.** `run-model-pool/2` binds an unordered
  ceiling and a separate principal-selected bootstrap body;
  `persona-model-choice/1` may later supply exact signed order and reasoning
  effort. Provider or configuration order never becomes routing authority.

## Reading order

| # | File | Focus |
|---|---|---|
| — | [`SPEC_CONVENTIONS.md`](SPEC_CONVENTIONS.md) | Normative writing and schema conventions. |
| 0 | [`00_VISION.md`](00_VISION.md) | Goals, invariants, scope, and safety boundary. |
| 1 | [`01_KERNEL.md`](01_KERNEL.md) | Authentication, lineage, policy, budgets, and mechanical effects. |
| 2 | [`02_PERSONA.md`](02_PERSONA.md) | Cryptographic identity, optional public self, agency, and authored evolution. |
| 3 | [`03_TASKS.md`](03_TASKS.md) | Exact task ingress, all-member fan-out, causality, and acceptance authority. |
| 4 | [`04_PROJECT.md`](04_PROJECT.md) | Long-lived shared workspace and project records. |
| 5 | [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md) | Membership, resources, shared workspace, and environment events. |
| 6 | [`06_DOMAIN.md`](06_DOMAIN.md) | Optional open domain records and plural unranked `domain_refs`. |
| 7 | [`07_ARTIFACTS.md`](07_ARTIFACTS.md) | Artifact bytes, signed MIME, bundles, provenance, and rendering. |
| 8 | [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md) | Opaque persona-owned knowledge/capability records and unranked navigation. |
| 9 | [`09_PROTOCOLS.md`](09_PROTOCOLS.md) | MCP/A2A/discovery/adapters, replication descriptors, MIME, and keys. |
| 10 | [`10_PLATFORM_REQUIREMENTS.md`](10_PLATFORM_REQUIREMENTS.md) | The platform's standing requirements, their carriage lane, the condition of record, and the run scorecard. |
| 11 | [`11_DESIGN_CRITERIA.md`](11_DESIGN_CRITERIA.md) | Observable operating-path outcomes and evidence. |
| 12 | [`12_GLOSSARY.md`](12_GLOSSARY.md) | Current terminology. |
| 13 | [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) | Static authority and information-flow walks, and the run journal (§20). |
| 14 | [`14_DECISIONS.md`](14_DECISIONS.md) | The current clean-break architecture decisions — decisions only; their measurements are journaled in 13 §20. |
| 15 | [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md) | Optional persona-authored coordination records. |
| 16 | [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md) | Exact population facts, opaque genesis, consent, and replication bounds. |
| 17 | [`17_ECONOMY.md`](17_ECONOMY.md) | Draft persona-authored economic records under exact authority. |
| 18 | [`18_SETTLEMENT.md`](18_SETTLEMENT.md) | Draft settlement and transfer mechanisms. |
| 19 | [`19_PERSONA_WORK_STATE.md`](19_PERSONA_WORK_STATE.md) | Append-only open work notes with factual observation bindings. |
| 20 | [`20_PERSONA_BRAIN_FRAGMENTS.md`](20_PERSONA_BRAIN_FRAGMENTS.md) | Opaque brain fragments and open signed evolution decisions. |
| 21 | [`21_OPEN_INPUTS.md`](21_OPEN_INPUTS.md) | Signed persona requests, peer candidates, owner precedence, and read-only public display. |

## Evidence and implementation

The design is evaluated from real operating-path evidence: signed records,
exact causal events, current workspace bytes, action/tool receipts, artifact
provenance, rendered outputs, and acceptance by the exact authority named in
principal intent.

Unit, integration, canary, benchmark, and performance-test corpora are not a
second product specification. A mocked success, HTTP 200, score, model claim,
work note, filename, or stale cached run cannot establish that the live system
worked.

## Clean-break scope

The current design provides no compatibility for mission charters,
ContinuousRefinement, task classes/pathways, structured work readiness, fixed
personality/modes, prompt optimization, ranked retrieval, fixed genesis seeds,
one-newborn-per-need semantics, singular primary domains, inferred MIME, or
inferred replication effects. Historical bytes may remain opaque audit records
but confer no current authority.

The persona is a persistent author—not a substrate-selected role.
