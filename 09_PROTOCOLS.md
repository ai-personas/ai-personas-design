---
title: PersonaOS v1.0 — Protocols, Standards, Adapters, Keys
status: Stable
---

# 09 — Protocols, Standards, Adapters, Keys

> **Reader guide.** This document covers how PersonaOS communicates with the outside world — other AI agents, tools, frameworks, and monitoring systems. You'll learn about three standard protocols: **MCP** (for tool access), **A2A** (for connecting AI systems), and **OpenTelemetry** (for monitoring). You'll also learn how PersonaOS integrates with 12 AI frameworks without losing identity or safety, and how cryptographic signing is managed. **Prerequisites:** `01_KERNEL.md`. **Key terms:** *adapter* = code that bridges PersonaOS to a specific framework; *schema registry* = the master list of all data structures in the system; *key custody* = three-tier signing hierarchy (from development to hardware-secured production).

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). This document specifies how PersonaOS v1.0 speaks to the outside world (MCP / A2A / OTel), the 12 framework adapter integrations, the schema-version master registry, Claude Code Skills/Subagents adapter, Anthropic `cache_control` policy, and the 3-tier key custody hierarchy (master + scope + domain + project + env + persona signing).

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. Fully normative; RFC 2119 keywords carry normative force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174).

**In scope.** Outbound protocol surfaces — **MCP** (tools / resources / prompts), **A2A** (agent-to-agent federation with signed AgentCards), **OpenTelemetry** (traces, metrics, logs); the five federation pillars (`§3A`–`§3E`); the twelve framework adapter integrations (Claude Code, OpenAI Agents SDK, LangGraph, CrewAI, MAF, Pydantic-AI, DSPy, smolagents, Semantic Kernel, MCP server, A2A server, MCP Proxy); the **schema-version master registry** (40+ entities across kernel / persona / task / project / env / domain / artifact / knowledge / protocol scopes); the Claude Code Skills/Subagents adapter; Anthropic `cache_control` policy; and the **three-tier key custody hierarchy** (cold-storage master + warm scope keys + hot per-task / per-action keys) with the scope chain (master → kernel → domain → project → env → persona).

**Out of scope.** Internal kernel mechanism (safety floor, sandbox, lineage construction — see [`01_KERNEL.md`](01_KERNEL.md)); persona model and modes (see [`02_PERSONA.md`](02_PERSONA.md)); task-class routing (see [`03_TASKS.md`](03_TASKS.md)); the running of acceptance tests against the registry (see [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md)).

**Supersession.** Subsumes prior protocol design notes; folds the `cache_control` and adapter integration appendices into one normative reference.

**Structural deviation.** Combines the compressed-opening pattern of [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md#33-compressed-opening-permitted) with Pattern B uppercase-suffix structural pillars under §3 (federation pillars `§3A`–`§3E`) per [`SPEC_CONVENTIONS.md §3.4`](SPEC_CONVENTIONS.md#34-heading-numbering). The three §3.1 bookends (this section, the Risks table, and Open Questions) are present.

## 0a. Plain-Language Guide

*Here's how PersonaOS connects to the outside world, explained without jargon.*

**What this document is about**

This document describes how PersonaOS talks to the outside world. Personas need to use tools, collaborate with other AI systems, plug into popular AI frameworks, and be monitored. Everything here specifies the plumbing that makes those connections work while keeping identity and safety intact.

**MCP — the universal toolbox**

MCP (Model Context Protocol) is the single standard PersonaOS uses for every external capability. Think of it as a universal plug: every tool a persona can call, every reference it can look up, and every skill it can offer to others is registered through MCP. When a persona needs an unfamiliar tool, it can search for one — like browsing an app store — with results ranked by relevance, trust, and cost.

**A2A — talking to other AI systems**

A2A (Agent-to-Agent) is how PersonaOS communicates with AI systems outside its own kernel. Every persona publishes an "AgentCard" — a signed digital business card listing its name, skills, and security credentials. Other systems discover these cards, verify signatures, and request services. This is how multiple independent PersonaOS instances find each other and collaborate without a central authority.

**The five communication channels inside an environment**

Personas in an environment never talk directly. The kernel mediates five channels: (1) the Blackboard, a shared event log everyone reads — like a public whiteboard in a meeting room; (2) Proven Facts, a ledger only the verification system can write to, so no one can simply declare something true; (3) Direct Messages, addressed one-to-one notes routed by the kernel; (4) the Candidate Table, tracking proposed answers and acceptance status (kernel-written, persona-readable); (5) the Goal Stack, listing objectives from operational details up to high-level purpose (also kernel-written).

**Cross-kernel gossip — how different instances find each other**

When multiple PersonaOS installations exist, they discover each other via gossip: a published card fans out to nearby peers, who forward it onward. Announcements carry a hop limit to prevent flooding, and hostile peers are rate-limited and lose reputation.

**Joined environments — collaborating across systems**

When personas from different installations work together persistently, they form a "joined environment." One kernel hosts the shared workspace; others run their personas locally and stream signed events to the host. Every action carries two signatures — sender's and host's. Safety rules compose by most-restrictive-wins: if any participant forbids a tool, the whole group cannot use it.

**Reputation — how personas build trust**

Anyone can spin up a new kernel, so identity alone is insufficient. Reputation comes from four signals: peer endorsements (vouching for specific skills), outcome corroboration (confirming predictions matched reality), lineage participation (completed joint work), and preserved disputes (a single credible disagreement weighs heavily, never averaged away). Anti-gaming measures include per-peer credit caps, multi-peer co-signature requirements, 30-day expiry, and near-zero weight for clusters of new kernels endorsing only each other.

**OpenTelemetry — monitoring and observability**

Every kernel operation emits structured telemetry using OpenTelemetry. Think of it as a flight recorder: you can see what happened, when, and how long it took. Traces propagate across MCP and A2A boundaries. Overhead target: at most 2% of wall time.

**The twelve framework adapters**

PersonaOS provides adapters for twelve AI frameworks: Claude Code, OpenAI Agents SDK, LangGraph, CrewAI, Microsoft Agent Framework, Pydantic-AI, DSPy, smolagents, Semantic Kernel, plus three infrastructure modes (MCP server, A2A server, MCP Proxy). Each adapter translates persona identity and safety rules into the framework's native concepts. The kernel always owns identity, safety, and the audit trail; the framework owns the LLM call, tool dispatch, and scheduling.

**Cache control — saving money on repeated AI calls**

PersonaOS marks stable prompt layers (identity and long-lived tactics) as cacheable. The AI provider reuses cached results instead of reprocessing them each time. Target: at least 80% cache hits on stable layers.

**Schema registry — the master list of all data structures**

v1.0 defines over 80 named data structures (schemas). The schema registry catalogues each with its version, stability level, and location. The kernel refuses any message with an unrecognised schema version. Adding or changing a schema requires updating the registry, providing a migration path, and adding an acceptance test.

**Key custody — the signing hierarchy**

Every event is signed with a digital key, like a tamper-proof seal. Keys form a tree: master key at the top, with derived keys for each domain, environment, project, and persona. Three security levels: laptop (development), cloud key service (production), or hardware security module (regulated industries). Keys rotate on schedule; compromised keys trigger a cascade that revokes all derived keys and notifies affected parties. Old signatures remain verifiable via archived public keys.

## 1. What this doc covers

How the PersonaOS v1.0 [kernel](12_GLOSSARY.md#k) speaks to the outside world:

- [**MCP**](12_GLOSSARY.md#m) for tools / resources / prompts (Anthropic 2024)
- [**A2A**](12_GLOSSARY.md#a) for agent-to-agent federation (Anthropic 2025)
- **OpenTelemetry** for observability
- **Twelve framework adapters** (Claude Code, OpenAI SDK, LangGraph, CrewAI, MAF, Pydantic-AI, DSPy, smolagents, Semantic Kernel, MCP server, A2A server, MCP Proxy)
- **Anthropic cache_control** for cost amortisation
- **Schema versions** for 40+ v1.0 entities (INV-10 hard gate)
- **Key custody hierarchy** — three custody tiers with master + scope + domain + project + env + [persona](12_GLOSSARY.md#p) signing keys
- **May-revision policies** — LLM transport / schema reformat / content refusal / context overflow / OWASP retrieval filter

## 2. MCP — Universal tool / resource / prompt bus

MCP is the canonical protocol for everything PersonaOS does outside the kernel.

*MCP organises external capabilities into three categories: tools (callable operations — both kernel-native and domain-specific), resources (read-only references to knowledge, artifacts, and memories), and prompt templates (persona skills published for external consumption). Domain tools are registered through DomainContext; persona-learned skills are invocable by ID.*

**Technical detail:** See [A.1](#appendix-a1).

### 2.1 MCP-Zero active tool discovery

Active discovery was introduced prior to v1.0; v1.0 carries it forward.

*A persona can request a tool by describing what it needs in natural language, optionally providing domain hints, latency, and cost constraints. The system returns candidate tools ranked by semantic similarity, trust, and cost.*

**Technical detail:** See [A.2](#appendix-a2).

### 2.2 MCP federated discovery

*Federated discovery queries peer kernels' registries for tools matching a domain hint, filtered by trust threshold and attestation requirements.*

**Technical detail:** See [A.3](#appendix-a3).

## 3. A2A — Agent-to-Agent federation

Every persona projects to an AgentCard for federation.

*The AgentCard dataclass carries the persona's identity, capabilities, interfaces (MCP / A2A / HTTP), exposed skills, security schemes, and an Ed25519 signature. Project summary, env summary, and domain curatorships are included when applicable.*

**Technical detail:** See [A.4](#appendix-a4).

### 3.1 A2A discovery

*AgentCards are published at `.well-known/` endpoints for discovery. Inbound: other kernels find our cards and invoke exposed skills. Outbound: our personas discover peers via `.well-known` gossip. Federated project discovery, env discovery, and cross-kernel domain emergence with multi-kernel signature gates are supported.*

**Technical detail:** See [A.5](#appendix-a5).

## 3A. Intra-environment communication — five channels

Within an environment, personas never call each other directly. They emit events to kernel-mediated channels. Five channels carry all intra-env traffic.

*The five channels are: CH-1 Blackboard (broadcast event log), CH-2 ProvenFacts (attested-write CRDT), CH-3 DirectMessage (addressed kernel-routed delivery), CH-4 CandidateTable (kernel-written acceptance state), and CH-5 GoalStack (kernel-written L0-L6 steering).*

**Technical detail:** See [A.6](#appendix-a6).

### 3A.1 CH-1 Blackboard

*The BlackboardEvent dataclass captures each event's ID (ULID), environment, round number, monotonic sequence, kind, actor, causality links, payload, and signature.*

**Technical detail:** See [A.7](#appendix-a7).

Write: persona body emits → adapter captures → kernel signature-check, role-contract check, constraint admission, sequence-assign, OTel span. Read: per-membership observation surface (§05 §9) filters which events the persona sees. Persistence: append-only; total order within a round via `(round_num, sequence_in_round)`; round barrier guarantees writes from round N visible only at round N+1 start. v1.0 unifies Blackboard with environment ambient_event_stream.

### 3A.2 CH-2 ProvenFacts

*The ProvenFact dataclass holds a content-addressed fact ID, scope (task/project/env), statement, evidence event links, a mandatory verifier cascade reference, timestamp, and signature.*

**Technical detail:** See [A.8](#appendix-a8).

Write semantics: only verifier-cascade output may become a ProvenFact; a persona cannot will a fact via raw emission. Read: any persona with scope-matching observation surface. Persistence: G-set CRDT, content-addressed dedup, merge at round barrier; per-TaskClass semantics (CONVERGENT: eliminations; DIVERGENT: constraints; MIXED: both; INTERACTIVE: append + INVALIDATED overlay, never silent delete).

### 3A.3 CH-3 DirectMessage

*The DirectMessage dataclass (frozen) carries event ID, round, sequence, sender, exactly one recipient, reply chain, kind (REQUEST/RESPONSE/ASK_CLARIFY/DELEGATE/RESAMPLE_REQUEST/REGRADE_REQUEST/STEER), body (up to 4k chars), optional structured payload, optional deadline round, and signature.*

**Technical detail:** See [A.9](#appendix-a9).

Addressed delivery: kernel routes into recipient's observation surface even when broadcast of that kind would be filtered. Topology allow-list per env `communication_protocol` (linear / bidirectional / star / pipeline / adversarial / mesh / host_governed); out-of-topology edges emit `CONSTRAINT_VIOLATION{kind=topology}` and drop. Back-pressure: `max_direct_inflight=3` per sender per round; `max_direct_queue=8` per recipient per round triggers `ROUTING_DIRECTIVE` to Integrator. Persistence: same round-ordered log as Blackboard, tagged `kind=DIRECT_MESSAGE`. No RPC — every cross-persona call is event-replayable.

### 3A.4 CH-4 CandidateTable and CH-5 GoalStack

Kernel-write, persona-read materialised views.

*CandidateTable maps candidate IDs to acceptance states (PROPOSED through ACCEPTED) with a last-updated round. GoalStack lists goals from L0 (operational) to L6 (purpose) with a last-revised round.*

**Technical detail:** See [A.10](#appendix-a10).

Personas read through observation surface (typically `candidate_table.summary`, `goal_stack.level≤L3`). Kernel folds Blackboard into these views at round barriers; personas trigger state transitions via events but never write directly.

## 3B. Inter-kernel gossip layer

For multi-kernel federation, per-kernel A2A round-trips don't scale. v1.0 adds a gossip protocol atop A2A for persona/env/domain discovery.

*The GossipEvent dataclass carries an action (publish/update/revoke), the card being gossiped (AgentCard, EnvCard, or DomainContextCard), originating kernel, timestamp, TTL hops (default 3), visited-kernels list for loop prevention, and signature. The protocol uses four phases: ANNOUNCE (fanout=8), FORWARD ONCE per peer with signature verification, PERIODIC RE-ANNOUNCE (default 1h), and REVOCATION. Trust-weighted reach scales with peer trust, originator reputation, and visibility tier.*

**Technical detail:** See [A.11](#appendix-a11).

Hostile peers flooding gossip are damped by per-peer rate limits and reputation degradation. Gossip is best-effort: typical propagation < 2s across federation; not guaranteed.

## 3C. Joined environments — cross-kernel collaboration

When personas from multiple kernels collaborate persistently, v1.0 forms a **joined environment**: one env instance hosted on one kernel, with peer kernels streaming their personas' contributions through it.

### 3C.1 Lifecycle

*The joined-environment lifecycle has seven stages: PROPOSE (initiator emits blueprint, required roles, candidate peers, budget, and consent terms), INVITE (signed A2A invitations), CONSENT (each peer kernel runs consent flow; persona accepts/declines/counters), INSTANTIATE (host kernel mints EnvironmentInstance by mutual agreement), RUN (host owns channels; peers stream signed events; both signatures preserved), PUBLISH (JoinedEnvCard signed by all), and RETIRE (AnswerPackage jointly signed and distributed to each peer's lineage).*

**Technical detail:** See [A.12](#appendix-a12).

### 3C.2 Single-host-kernel rule

A joined env has **exactly one host kernel** at any time. This avoids distributing Blackboard sequence numbers across peers with clock drift. Peer kernels run bodies; kernel state lives on the host. If host becomes unreachable, env enters `STALLED`; a `host_handoff` procedure (quorum sign-off + Blackboard replay from peer caches) exists but is heavyweight by design — joined envs are short-lived.

### 3C.3 Trust posture and constraint composition

*Trust posture: peer kernels stream signed events to the host; the host's re-signature attests admission. ProvenFacts carry both signatures. Divergence at retire triggers DISPUTE events. Constraint composition follows most-restrictive-wins: effective constraints are the intersection of host, peer, blueprint, task, and universal harm floor constraints. A tool forbidden by any peer is forbidden for all; the lowest token cap from any peer binds.*

**Technical detail:** See [A.13](#appendix-a13).

A joined env is at most as capable as the least-permissive participant. This is correct: the host kernel's operator policy named the floor.

### 3C.4 Consent flow

*When an inbound proposal arrives, the receiving kernel checks whether the intent requires consent per VisibilityPolicy. If yes: a CONSENT_REQUEST is raised on the persona's Blackboard; the persona may grant, decline, or ask a human (default-decline on timeout). If no: auto-admit subject to reputation, rate, and scope filters.*

**Technical detail:** See [A.14](#appendix-a14).

Consent is **per-interaction, not per-peer**. Granting peer K1 consent for joined env X does not imply consent for env Y. A `ConsentLedger` allows "always allow / always deny" pins. Mid-task consent revocation: `CONSENT_REVOKED` event with original consent_id triggers controlled-shutdown — host sequences a final round, signs partial AnswerPackage, distributes.

### 3C.5 Cross-kernel DirectMessage visibility

Within a single-kernel env, a `CH-3 DirectMessage` (§3A.3) routes through the host kernel's blackboard infrastructure but is *addressed* (one recipient); other members do not see the content. In a **joined env**, the host kernel is the canonical Blackboard owner — what is the visibility model for cross-kernel DMs?

**The model v1.0 adopts: host-visible-by-default, end-to-end-encrypted on opt-in.**

*In default mode, all DMs pass through the host kernel's blackboard — the host can read content and its signature attests no modification. In opt-in E2E mode, content is encrypted under the recipient's persona key; the host signs only the envelope metadata and cannot read content. E2E DMs are refused in safety-critical envs, when both parties share a kernel, or when operator policy forbids them. The CrossKernelDMVisibility dataclass tracks per-DM encryption status, host visibility flags, safety floor inspection results, and triple signatures (sender kernel, host kernel, recipient kernel).*

**Technical detail:** See [A.15](#appendix-a15).

**Composition with PersonaPersonaBoundary (`02_PERSONA §11.6`).** A `direct_message` interaction kind in PersonaPersonaBoundary refuses ALL DMs (encrypted or not) from the target persona. Boundary check runs at sender's kernel BEFORE encryption; the message never leaves the sender's kernel.

**Honest limits:**

1. **E2E does not protect against compromised recipient kernel.** A malicious recipient kernel may log decrypted content. v1.0 assumes peer kernels are honest-but-curious by default.
2. **Metadata leakage.** Even e2e DMs leak existence + timing + size to the host. For high-stakes confidentiality, use a separate channel outside the env.
3. **No forward secrecy in v1.0.** A leaked recipient persona key reveals all prior e2e DMs to that recipient. v1.1 may add ephemeral-key DM if a use case warrants.

## 3D. Reputation and anti-Goodhart

Cross-kernel collaboration cannot rely on identity alone: anyone can spin up a kernel, sign a card, spam. v1.0 layers reputation atop signing.

*The ReputationSummary dataclass (frozen) tracks per-persona, per-role reputation: total/accepted/disputed/blocklisted interaction counts, peer-capped contribution credit, lineage participation count, peer endorsements, outcome corroborations, judge calibration score, co-signing peer kernels (with a minimum threshold for trust tier), 30-day expiry, and publishing kernel signature.*

**Technical detail:** See [A.16](#appendix-a16).

### 3D.1 Signal model

Reputation aggregates four signal kinds.

*The four signals are: peer endorsement (signed, citing specific skills), outcome corroboration (peer confirms claims matched reality), lineage participation (count of signed joined-env retirements weighted by reach), and dispute preservation (a single high-credibility dispute weighs more than many generic acceptances).*

**Technical detail:** See [A.17](#appendix-a17).

Reputation is **role-relative**: a high-reputation Falsifier is not implicitly trusted as a Composer. Matches the I1 role-locked identity invariant.

### 3D.2 Anti-gaming rules

*Six anti-gaming rules govern reputation: (1) per-peer credit cap (saturation prevents collusion), (2) co-signature requirement (federation tier needs 2+ co-signers), (3) 30-day decay with forced restatement, (4) sybil resistance (mutual-co-signing clusters get near-zero weight), (5) reach-times-diversity weighting (punishes echo-chamber reputation), and (6) disputed-flag preservation (disputes are never blended away). Outreach intent thresholds range from "fresh OK" for one-shot tasks to "tenant only" for soul inspection.*

**Technical detail:** See [A.18](#appendix-a18).

Operator-tunable per persona via `VisibilityPolicy`.

## 3E. Cross-kernel relationship continuity

When two personas form a `PersonaRelationshipEdge` (`02_PERSONA §11.4`) and they live on different kernels, the edge cannot live on one kernel alone — both kernels must hold a consistent view, both signatures must be co-resident, and either side's revocation must propagate. This is named `RelationshipFederationSync`.

*The RelationshipFederationSync dataclass tracks the edge being synced, home and peer kernels, replication mode (shadow or co-owned), sync state (last sync time, monotone sequence, lag budget defaulting to 5min for active edges), mandatory revocation propagation, anti-Goodhart discrepancy audit (mismatched joint_successes counters trigger FEDERATED_TRUST_DISCREPANCY), and dual signatures.*

**Technical detail:** See [A.19](#appendix-a19).

**Replication semantics.**

*Shadow mode (default for asymmetric edges): home kernel writes mutations; peer holds a read-only shadow and may only propose mutations that require home counter-signature. Conflicts are impossible by construction. Co-owned mode (default for symmetric edges): either kernel writes with monotone sequence and signed timestamp; conflicts resolved by Lamport ordering; revocations always win (terminal precedence). Co-owned mode has higher cost.*

**Technical detail:** See [A.20](#appendix-a20).

**Sync transport.** `RelationshipFederationSync` rides on the same A2A channel `§3` uses for joined environments. Sync envelopes are signed by both kernels; replay rejects unsigned envelopes; the host of a joined env is a natural sync-broker if both participants are present.

**Anti-Goodhart for federated trust.** A home kernel that inflates `trust_a_of_b` without matching `joint_successes` recorded against the same shared `LineageGraph` triggers `FEDERATED_TRUST_DISCREPANCY` on the peer's side; the peer kernel MAY freeze the edge or downgrade replication_mode to shadow. This composes with `§3D` reputation anti-gaming and prevents one kernel from unilaterally manufacturing trust history.

**Honest limits.**

1. **Sync lag is not zero.** During the `sync_lag_budget` window, the two views may differ. The substrate refuses safety-critical actions that *depend* on edge state during sync windows; routine work is admissible against the local view.
2. **Co-owned mode requires both kernels online for conflict resolution.** If one kernel is offline past the sync lag budget, the other's mutations enter CONFLICT_PARKED on its side; resolution waits for the peer's return. Joined-env STALLED semantics (`§3C.2`) apply.
3. **Ships schema and shadow mode for production; co_owned mode is v1.1+.** Cross-kernel real-time conflict resolution under arbitrary latency is the v1.1 federation-hardening track. The spec produces well-formed `RelationshipFederationSync` envelopes for both modes, but in co_owned mode only single-kernel-quorum deployments are admitted by operator policy.

**Acceptance tests.** A-RF1 (shadow mode: peer mutation requires home counter-sign), A-RF2 (revocation propagates within sync_lag_budget), A-RF3 (FEDERATED_TRUST_DISCREPANCY fires on home-only trust inflation), A-RF4 (co_owned conflict resolution by Lamport order), A-RF5 (sync lag refused for safety-critical action against edge state).

## 4. OpenTelemetry semantic conventions

Every kernel operation emits OTel spans with PersonaOS conventions.

*The semantic conventions define span attributes across 11 groups: kernel operations (envelope mint, safety check, signing, dispatch), task (ID, class, pathway, fingerprint, duration, status), persona (ID, mode entry/exit, action, disposition, charter drift), project (ID, status, milestones, obligations), environment (ID, type, member admission, ambient events, cross-env offers, guest presence), domain (ID, stage, probe phase, promotion), verifier and panel (cascade stage, verdict, dissent vector), lineage (scope, event kind, signed), budget (consumed, threshold crossed), safety (source, refusal, classifier ID), and lifecycle (transition, signed).*

**Technical detail:** See [A.21](#appendix-a21).

OTel overhead target: **≤ 2% wall time**.

Trace propagation across MCP / A2A boundaries via W3C Trace Context.

## 5. Anthropic cache_control alignment

v1.0 PromptBlock cacheable marker projects to Anthropic Messages API.

*The PromptBlock dataclass (frozen) pairs text content with a cacheable flag and an origin label indicating which section of the persona's prompt it comes from (frontmatter, identity sections, evolved tactics, advisories, task framing, project/env/domain context). Layers 1-2 (identity and tactics) are marked cacheable; Layer 3 (dynamic context) is not. When rendered to the Anthropic API, cacheable blocks carry `cache_control: {"type": "ephemeral"}` while dynamic blocks omit it.*

**Technical detail:** See [A.22](#appendix-a22).

Cache hit rate target: **≥ 80% on Layer 1 + Layer 2 blocks** across envelope mints.

## 6. The twelve framework adapters

v1.0 personas project into and are consumed by twelve adapter integrations. Each adapter consumes the same `PersonaEnvelope` contract.

### 6.1 Claude Code adapter

*Persona's SOUL.md projects into a Claude Code Skill or Subagent file with name, description, allowed_tools, model, and system prompt from the concatenated envelope. Bidirectional adapter: PersonaOS as MCP server consumed by Claude Code, and Claude Code subagents project to PersonaOS personas. Verifier cascade exposed as PreToolUse hooks.*

**Technical detail:** See [A.23](#appendix-a23).

### 6.2 OpenAI Agents SDK adapter

*Persona projects as an Agent with name, instructions from concatenated prompt, MCP tools, output schema, and handoffs. Verifier wraps kernel.verify via @output_guardrail decorator.*

**Technical detail:** See [A.24](#appendix-a24).

### 6.3 LangGraph adapter

*Persona projects as a subgraph node with SystemMessage from concatenated prompt, ProvenFacts as annotated list state field, verifier as conditional edge, and cohort assembly as parent graph routing.*

**Technical detail:** See [A.25](#appendix-a25).

### 6.4 CrewAI adapter

*Persona projects as a CrewAI Agent with role from primary disposition, goal from envelope description, backstory from SOUL "Who I am" section, MCP tools, and a non-removable injected kernel verify tool.*

**Technical detail:** See [A.26](#appendix-a26).

### 6.5 Microsoft Agent Framework (MAF) adapter

*Personas map to MAF Agents, rounds map to GroupChat, and the termination predicate calls kernel.acceptance_check.*

**Technical detail:** See [A.27](#appendix-a27).

### 6.6 Pydantic-AI adapter

*Persona projects as Agent[Deps, Out] with typed dependencies, output_type from envelope schema, and output_validator from kernel.acceptance_check.*

**Technical detail:** See [A.28](#appendix-a28).

### 6.7 DSPy adapter

*Persona projects as a dspy.Module. Toolsmith persona may invoke dspy.GEPA or dspy.MIPROv2 as mutation operator over another persona's tactics, with kernel verifier as the metric.*

**Technical detail:** See [A.29](#appendix-a29).

### 6.8 smolagents adapter

*Experimenter persona projects as smolagents.CodeAgent; kernel intercepts post-run for verifier and lineage.*

**Technical detail:** See [A.30](#appendix-a30).

### 6.9 Semantic Kernel adapter (secondary)

*Persona projects as ChatCompletionAgent; SK kernel filter calls PersonaOS verifier.*

**Technical detail:** See [A.31](#appendix-a31).

### 6.10 MCP Server (PersonaOS as MCP)

*PersonaOS kernel exposed as an MCP server. Any MCP-compliant client can list personas, invoke skills, read knowledge, and call kernel tools.*

**Technical detail:** See [A.32](#appendix-a32).

### 6.11 A2A Server (PersonaOS as A2A peer)

*Each persona published as a signed AgentCard at .well-known/. Other kernels can discover and invoke via A2A protocol. Cross-kernel project, env, and domain coordination supported.*

**Technical detail:** See [A.33](#appendix-a33).

### 6.12 MCP Proxy mode

*PersonaOS kernel sits in front of third-party MCP servers. Every tool call passes through kernel verifier and safety floor. No persona code changes; transparent proxy.*

**Technical detail:** See [A.34](#appendix-a34).

### 6.13 Adapter contract — invariant across all 12

*The kernel always owns soul/identity, verifier cascade, invariant enforcement, candidate acceptance, lineage append, and ProvenFacts write-through. The body (framework adapter) always owns the LLM call, tool dispatch, persistence, observability transport, and scheduling.*

**Technical detail:** See [A.35](#appendix-a35).

v1.0-specific extensions (project_context, env_context, emergent-domain warning) are **additive** — adapters that don't know about them ignore them; v1.0-aware adapters use them.

### 6.14 Standards alignment table

| v1.0 entity | MCP | A2A | Claude Code Skills | Anthropic API | OpenAI SDK | CrewAI | LangGraph |
|---|---|---|---|---|---|---|---|
| Persona | — | AgentCard | Skill/Subagent file | system prompt | Agent class | Agent role | Graph node |
| Description (≤120) | tool desc | skill desc | `description:` | system content | description | goal | label |
| `allowed_tools` | — | — | `allowed-tools` | — | tools[] | tools | tool node |
| Soul prompt blocks | — | — | — | content + cache_control | tools[] system | system | system |
| Exposed skill | MCP prompt | AgentCard.skills[] | exposed_skills | — | — | — | — |
| Cohort assembly | — | A2A inter-agent | — | — | handoff | delegation | edge transition |
| Project membership | — | AgentCard.project_summary | — | — | — | — | state |
| Env presence | — | AgentCard.env_summary | — | — | — | — | state |
| Verifier output | tool output | — | — | — | guardrail | injected tool | conditional edge |
| Trace context | — | A2A trace | — | — | — | — | OTel spans |

## 7. Schema registry

This section catalogues the **headline v1.0 schemas** by entity group. Every entity that crosses a process or signing boundary in v1.0 declares a `schema` field carrying a `<name>/<integer>` version string per [`SPEC_CONVENTIONS.md §4`](SPEC_CONVENTIONS.md#4-schemas); [`INV-10`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) enforces that the kernel MUST refuse unknown versions.

The headline catalogue below lists ~80 of the most-referenced schemas across the design. A full automated registry (covering ~150 schemas including narrower schemas like `deferred-admission/1`, `drift-bounds/1`, `policy-envelope/1`, `bulk-kind-proposal/1`, etc.) is generated from source by the schema-extractor CI job, which `grep`s all docs and source for `schema` field literals matching `<name>/<integer>` and emits `schemas/registry.json`. The headline table is the human-reviewed curated subset; the generated registry is authoritative for runtime version checks.

Adding a new schema requires either (a) extending the headline table here if the schema is broadly load-bearing, or (b) confirming it shows up in the generated registry. Either way, [`§7.13`](#713-adding-or-modifying-schemas) below applies.

Stability legend:

| Stability | Meaning |
|-----------|---------|
| **Stable** | Wire-compatible across v1.0.x; bumps require migration tool entry. |
| **Provisional** | Subject to additive change without major bump; stable structure. |
| **Experimental** | May change shape; not yet on the migration path. |

Encoding per [`SPEC_CONVENTIONS.md §4`](SPEC_CONVENTIONS.md#4-schemas). Where a schema is defined as a Python `@dataclass`, the "Form" column says `dataclass`; JSON Schema is `jsonschema`; TypeScript `interface` is `ts`.

### 7.1 Persona & identity

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `SOUL.md` | `soul/4` | markdown + frontmatter | [`02_PERSONA.md §3`](02_PERSONA.md) | Stable | Kernel identity; persona load; bootstrap. |
| `soul.state.json` | `soul-state/6` | jsonschema | [`02_PERSONA.md §3`](02_PERSONA.md) | Stable | Evolving persona state; signed by kernel. v6: `age_tasks`→`experience_tasks`, drop `maturity` string, add `born_at` + `experiential_floor` (migration §7.13). |
| `PersonaSeed` | `persona-seed/2` | dataclass | [`02_PERSONA.md §2`](02_PERSONA.md) | Stable | Birth templates; seed library. |
| `ALPSBandPolicy` | `alps-band-policy/1` | dataclass | [`02_PERSONA.md §7.3`](02_PERSONA.md) | Draft | Operator-tunable wall-clock ALPS age-band edges. |
| `PersonaCard` | `persona-card/3` | dataclass | [`02_PERSONA.md §3`](02_PERSONA.md) | Stable | A2A federation card. |
| `PersonaEnvelope` | `envelope/4` | dataclass | [`02_PERSONA.md §7`](02_PERSONA.md) | Stable | Round-active projection of persona. |

### 7.2 Acceptance & task

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `AnswerPackage` | `answer/4` | dataclass | [`03_TASKS.md §6`](03_TASKS.md) | Stable | Canonical task output. |
| `AcceptanceConfig` | `acceptance-config/1` | dataclass | [`03_TASKS.md §3`](03_TASKS.md) | Stable | Per-pathway routing config. |
| `TaskClassEstimate` | `task-class-estimate/1` | dataclass | [`03_TASKS.md §4`](03_TASKS.md) | Stable | Classifier output. |

### 7.3 Project workspace (env type)

Schemas in this group attach to `EnvironmentInstance.type = "project_workspace"`. Per the J8 retirement ([`00_VISION.md §3`](00_VISION.md#3-invariants-j1j9), [`04_PROJECT.md §0`](04_PROJECT.md#0-status--scope)), `project-lineage/1` records persist as a tagged subset of `env-lineage/1` events; the schema is retained for back-compatibility but is **not** a separate physical scope.

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `Project` (logical view) | `project/2` | dataclass | [`04_PROJECT.md §1`](04_PROJECT.md) | Stable | Documentation/CLI views over `EnvironmentInstance(type=project_workspace)`. |
| `ProjectMember` | `project-member/2` | dataclass | [`04_PROJECT.md §2`](04_PROJECT.md) | Stable | Roster of personas + users on project envs. |
| `ProjectLineage event` | `project-lineage/1` | dataclass | [`04_PROJECT.md §15`](04_PROJECT.md) | Stable (compatibility alias) | Documentation filter over EnvironmentLineage `project_*` events. |
| `OpenProblem` | `open-problem/1` | dataclass | [`04_PROJECT.md §6`](04_PROJECT.md) | Stable | Tracked unresolved questions. |
| `ProjectMilestone` | `milestone/1` | dataclass | [`04_PROJECT.md §7`](04_PROJECT.md) | Stable | Phase gates; INVESTIGATIVE pathway anchors. |
| `ProjectItem` | `project-item/1` | dataclass | [`04_PROJECT.md §8`](04_PROJECT.md) | Stable | Single substrate item discriminated by emergent `ItemKind` (`KindRegistry.item_kinds`); subsumes the prior `Conjecture` / `ProofAttempt` / `ProofGap` classes as math-domain `ItemKind` seeds. |
| `Obligation` | `obligation/1` | dataclass | [`04_PROJECT.md §9`](04_PROJECT.md) | Stable | Owed work between members. |
| `Disagreement` | `disagreement/1` | dataclass | [`04_PROJECT.md §10`](04_PROJECT.md) | Stable | Tracked unresolved differences. |
| `PeerReview` | `peer-review/1` | dataclass | [`04_PROJECT.md §11`](04_PROJECT.md) | Stable | Multi-reviewer evaluation. |

### 7.4 Environment

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `EnvironmentBlueprint` | `env-blueprint/1` | dataclass | [`05_ENVIRONMENT.md §2`](05_ENVIRONMENT.md) | Stable | Env-type template. |
| `EnvironmentInstance` | `env-instance/1` | dataclass | [`05_ENVIRONMENT.md §1`](05_ENVIRONMENT.md) | Stable | Persistent env record (J9). |
| `EnvironmentMembership` | `env-membership/1` | dataclass | [`05_ENVIRONMENT.md §5`](05_ENVIRONMENT.md) | Stable | Persona ↔ env binding with role + surface + community standing. |
| `CommunityStanding` | `community-standing/1` | dataclass | [`05_ENVIRONMENT.md §5.4`](05_ENVIRONMENT.md) | Draft | Per (persona, env) relational standing (LPP); non-portable; conferred, never self-awarded. |
| `StandingEndorsement` | `standing-endorsement/1` | dataclass | [`05_ENVIRONMENT.md §5.4`](05_ENVIRONMENT.md) | Draft | Recognition event conferring community standing; anti-gaming reuses §3D / A.16–A.18. |
| `PresenceState` | `presence/1` | dataclass | [`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md) | Stable | Per-member liveness. |
| `AttentionBudget` | `attention-budget/1` | dataclass | [`05_ENVIRONMENT.md §7`](05_ENVIRONMENT.md) | Stable | Per-member rate limits. |
| `EnvironmentLineage event` | `env-lineage/1` | dataclass | [`05_ENVIRONMENT.md §10`](05_ENVIRONMENT.md) | Stable | The env scope of J9 lineage. |
| `AmbientEvent` | `ambient-event/1` | dataclass | [`05_ENVIRONMENT.md §8`](05_ENVIRONMENT.md) | Stable | Sub-attention substrate events. |
| `ObservationSurface` | `observation-surface/1` | dataclass | [`05_ENVIRONMENT.md §9`](05_ENVIRONMENT.md) | Stable | Per-persona attention filter. |
| `ProactiveIntent` | `proactive-intent/1` | dataclass | [`05_ENVIRONMENT.md §11`](05_ENVIRONMENT.md) | Stable | Rate-limited persona-initiated action. |
| `CrossEnvProactiveOffer` | `cross-env-proactive-offer/1` | dataclass | [`05_ENVIRONMENT.md §11.6`](05_ENVIRONMENT.md) | Stable | Cross-env voluntary help offer with consent flow. |
| `GuestPresence` | `guest-presence/1` | dataclass | [`05_ENVIRONMENT.md §11.6`](05_ENVIRONMENT.md) | Stable | Time-bounded, scope-limited presence for accepted cross-env offers. |
| `EnvSelfProposalRequest` | `env-self-proposal/1` | dataclass | [`05_ENVIRONMENT.md §12b`](05_ENVIRONMENT.md) | Provisional | Persona-initiated self-admission to an existing env. |
| `EnvFormationProposal` | `env-formation-proposal/1` | dataclass | [`05_ENVIRONMENT.md §12c.1`](05_ENVIRONMENT.md) | Provisional | Persona-initiated creation of a new env with cohort + charter + consent flow. |
| `CohortInvite` | `cohort-invite/1` | dataclass | [`05_ENVIRONMENT.md §12c.1`](05_ENVIRONMENT.md) | Provisional | Per-recruit element of an `EnvFormationProposal`. |
| `ConsentTerms` | `consent-terms/1` | dataclass | [`05_ENVIRONMENT.md §12c.1`](05_ENVIRONMENT.md) | Provisional | Disclosure surface shown to a recruit on `CONSENT_REQUEST`. |
| `CohortConsentResponse` | `cohort-consent-response/1` | dataclass | [`05_ENVIRONMENT.md §12c.1`](05_ENVIRONMENT.md) | Provisional | Signed recruit reply (accept / decline / counter / boundary-refused / etc.). |
| `CounterProposal` | `counter-proposal/1` | dataclass | [`05_ENVIRONMENT.md §12c.1`](05_ENVIRONMENT.md) | Provisional | Recruit counter-offer carried inside a `CohortConsentResponse`. |
| `CharterAmendment` | `charter-amendment/1` | dataclass | [`05_ENVIRONMENT.md §12c.1`](05_ENVIRONMENT.md) | Provisional | Negotiated charter delta produced during cohort formation. |

### 7.5 Domain

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `DomainContext` | `domain-context/2` | dataclass | [`06_DOMAIN.md §2`](06_DOMAIN.md) | Stable | Authored or emergent domain knowledge. |
| `EmergentDomainContext` | `emergent-domain/1` | dataclass (same shape) | [`06_DOMAIN.md §3`](06_DOMAIN.md) | Stable | Pre-promotion view. |
| `DomainProbe` | `domain-probe/1` | dataclass | [`06_DOMAIN.md §4`](06_DOMAIN.md) | Stable | Persona probe of unfamiliar territory. |
| `DiscoveredTool` | `discovered-tool/1` | dataclass | [`06_DOMAIN.md §5`](06_DOMAIN.md) | Stable | MCP tool discovered by persona. |
| `KnowledgeIngestionRecord` | `knowledge-ingestion/1` | dataclass | [`06_DOMAIN.md §6`](06_DOMAIN.md) | Stable | Ingested external knowledge unit. |
| `InferredVerifierRecipe` | `inferred-recipe/1` | dataclass | [`06_DOMAIN.md §7`](06_DOMAIN.md) | Stable | Persona-inferred verifier shape. |
| `ProposedSafetyExtension` | `safety-extension-proposal/1` | dataclass | [`06_DOMAIN.md §8`](06_DOMAIN.md) | Stable | Pre-operator-review safety floor extension. |
| `ProposedConvention` | `proposed-convention/1` | dataclass | [`06_DOMAIN.md §9`](06_DOMAIN.md) | Stable | Pre-adoption convention. |
| `NotationConvention` | `notation/1` | dataclass | [`06_DOMAIN.md §9`](06_DOMAIN.md) | Stable | Adopted notation. |
| `StandardRef` | `standard-ref/1` | dataclass | [`06_DOMAIN.md §10`](06_DOMAIN.md) | Stable | Pointer to external standards body. |
| `CrossDomainTransfer` | `cross-domain-transfer/1` | dataclass | [`06_DOMAIN.md §11`](06_DOMAIN.md) | Stable | Skill/tool moved between domains. |
| `DemotionEvent` | `demotion-event/1` | dataclass | [`06_DOMAIN.md §12`](06_DOMAIN.md) | Stable | Promotion-stage regression. |
| `DomainLineage event` | `domain-lineage/1` | dataclass | [`06_DOMAIN.md §16`](06_DOMAIN.md) | Stable | The domain scope of C1 lineage. |
| `BridgeAsset` | `bridge-asset/1` | dataclass | [`06_DOMAIN.md §5.5`](06_DOMAIN.md) | Stable | Durable physical-world bridge. |
| `BridgeCalibrationBinding` | `bridge-calibration/1` | dataclass | [`06_DOMAIN.md §5.5.5`](06_DOMAIN.md) | Provisional | Measurement-bridge calibration provenance. |
| `DomainHarvest` | `domain-harvest/1` | dataclass | [`06_DOMAIN.md §13a`](06_DOMAIN.md) | Provisional | Curator-packaged, downstream-consumable snapshot of a domain. |
| `DomainUnknownDetected` | `domain-unknown-detected/1` | dataclass | [`06_DOMAIN.md §4.1`](06_DOMAIN.md) | Stable | Signed C1 lineage event marking persona detection of an unfamiliar domain; triggers the probe → discovery → ingestion → inference → curation → promotion lifecycle. |
| `ProposalQueue` | `proposal-queue/1` | dataclass | [`06_DOMAIN.md §9`](06_DOMAIN.md) | Stable | Per-domain curation queue holding pending / accepted / rejected / operator-deferred persona proposals; persisted across sessions. |

### 7.6 Artifacts

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `Artifact` | `artifact/1` | dataclass | [`07_ARTIFACTS.md §1`](07_ARTIFACTS.md) | Stable | Single produced output. |
| `ArtifactBundle` | `artifact-bundle/1` | dataclass | [`07_ARTIFACTS.md §2`](07_ARTIFACTS.md) | Stable | Multi-modal coherent set. |
| `VerifierRecipe` | `verifier-recipe/1` | dataclass | [`07_ARTIFACTS.md §4`](07_ARTIFACTS.md) | Stable | Recipe for verifying an artifact. |
| `VerifierInvocationEvidence` | `verifier-invocation-evidence/1` | dataclass | [`07_ARTIFACTS.md §7`](07_ARTIFACTS.md) | Stable | Signed, hash-bound evidence that a verifier stage actually ran and how its verdict was derived. |

### 7.7 Knowledge

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `Lesson` | `lesson/1` | dataclass | [`08_KNOWLEDGE.md §3`](08_KNOWLEDGE.md) | Stable | Promotable reflection unit. |
| `K-line` | `k-line/1` | dataclass | [`08_KNOWLEDGE.md §3`](08_KNOWLEDGE.md) | Stable | Bundle of co-fired memories (Minsky K-lines). |
| `ProvenFact` | `proven-fact/1` | dataclass | [`08_KNOWLEDGE.md §3`](08_KNOWLEDGE.md) | Stable | Verifier-attested fact. |
| `Skill` (Voyager) | `skill/1` | dataclass | [`08_KNOWLEDGE.md §3`](08_KNOWLEDGE.md) | Stable | Reusable skill in library. |
| `ToolArtifact` | `tool-artifact/1` | dataclass | [`08_KNOWLEDGE.md §3`](08_KNOWLEDGE.md) | Stable | Persisted tool definition. |
| `RubricBundle` | `rubric/1` | dataclass | [`08_KNOWLEDGE.md §3`](08_KNOWLEDGE.md) | Stable | Judge-panel scoring dimensions. |
| `MemoryEntry` | `memory/1` | dataclass | [`08_KNOWLEDGE.md §4`](08_KNOWLEDGE.md) | Stable | Tier 1-4 memory record. |
| `Tactic` | `tactic/1` | dataclass | [`08_KNOWLEDGE.md §3`](08_KNOWLEDGE.md) | Stable | EVOLVE-BLOCK heuristic. |
| `MetaPrompt` | `meta-prompt/1` | dataclass | [`08_KNOWLEDGE.md §3`](08_KNOWLEDGE.md) | Stable | GEPA-evolved prompt program. |
| `UncertaintyEnvelope` | `uncertainty-envelope/1` | dataclass | [`08_KNOWLEDGE.md §16a.1`](08_KNOWLEDGE.md) | Provisional | First-class uncertainty around a numerical claim — distribution shape, systematic-error floor, calibration-chain pointer, units. |
| `MeasurementFact` | `measurement-fact/1` | dataclass | [`08_KNOWLEDGE.md §16a.2`](08_KNOWLEDGE.md) | Provisional | Numerical ProvenFact subtype bound to an `UncertaintyEnvelope`, calibration chain, and replication context. |

### 7.8 Verifier & panel

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `VerifierCascade` | `verifier-cascade/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | 4-tier verifier chain. |
| `VerifierStage` | `verifier-stage/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | One stage in the cascade. |
| `JudgePanel` | `judge-panel/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | Multi-judge composition. |
| `RubricDimension` | `rubric-dimension/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | One judging axis. |
| `PanelVerdict` | `panel-verdict/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | Aggregated panel decision. |
| `OvertonBallot` | `overton/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | Anti-Goodhart ballot. |
| `StructuredFeedback` | `structured-feedback/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | Typed evaluation signal. |

### 7.9 Relationships

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `RelationshipRecord` | `rel/1` | dataclass | [`02_PERSONA.md §6`](02_PERSONA.md) | Stable | Persona ↔ actor relationship with history. |
| `Consent` | `consent/1` | dataclass | [`02_PERSONA.md §6`](02_PERSONA.md) | Stable | Bounded scoped consent. |
| `UserBoundary` | `boundary/1` | dataclass | [`02_PERSONA.md §6`](02_PERSONA.md) | Stable | User-set restrictions. |
| `MoodState` | `mood/1` | dataclass | [`02_PERSONA.md §5`](02_PERSONA.md) | Stable | Transient affective state. |
| `PersonalGoal` | `personal-goal/1` | dataclass | [`02_PERSONA.md §6`](02_PERSONA.md) | Stable | Persona-side goal distinct from task. |

### 7.10 Constraints & policy

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `Constraint` | `constraint/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | One constraint clause. |
| `ConstraintBundle` | `constraint-bundle/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | Floor-source composition. |
| `ConstraintViolation` | `constraint-violation/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | Refusal record. |
| `OperatorPolicy` | `operator-policy/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | Floor source 4. |
| `ToolRequirement` | `tool-req/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | External-tool admission rules. |
| `NoveltyCheckConfig` | `novelty-check/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | Novelty-floor parameters. |
| `SafetyExtension` | `safety-extension/1` | dataclass | [`06_DOMAIN.md §8`](06_DOMAIN.md) | Stable | Adopted safety extension (post operator review). |
| `SafetySnapshot` | `safety-snapshot/1` | dataclass | [`01_KERNEL.md §13`](01_KERNEL.md) | Stable | Floor composition at a moment. |
| `UserStop` | `user-stop/1` | dataclass | [`01_KERNEL.md §13.6`](01_KERNEL.md) | Stable | User-initiated intervention (pause / stop / abort) halting an in-flight persona action; signed by user key. |
| `OperatorOverride` | `operator-override/1` | dataclass | [`01_KERNEL.md §13.6`](01_KERNEL.md) | Stable | Operator-initiated suspension or termination of a persona / env / task / project; signed by operator key. |
| `PersonaSelfStop` | `persona-self-stop/1` | dataclass | [`01_KERNEL.md §13.6`](01_KERNEL.md) | Stable | Persona-initiated voluntary halt with reason and optional fallback suggestion; signed by persona key. |

### 7.11 Federation & cards

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `AgentCard` (A2A) | `agent-card/1` | jsonschema | [`09_PROTOCOLS.md §3`](09_PROTOCOLS.md) | Stable | A2A peer descriptor. |
| `EnvCard` | `env-card/1` | jsonschema | [`09_PROTOCOLS.md §3`](09_PROTOCOLS.md) | Stable | Federated env descriptor. |
| `ProjectCard` | `project-card/1` | jsonschema | [`09_PROTOCOLS.md §3`](09_PROTOCOLS.md) | Stable | Federated project-workspace descriptor. |
| `DomainContextCard` | `domain-context-card/1` | jsonschema | [`09_PROTOCOLS.md §3`](09_PROTOCOLS.md) | Stable | Federated domain descriptor. |
| `ReputationSummary` | `reputation/1` | jsonschema | [`09_PROTOCOLS.md §3`](09_PROTOCOLS.md) | Stable | Cross-kernel reputation digest. |

### 7.12 Lineage

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `LineageEvent` | `lineage-event/1` | dataclass | [`01_KERNEL.md §3.2`](01_KERNEL.md) | Stable | Canonical append-only event across the three signed scopes (task / env / domain); parents and siblings are derived from `scope` + `parent_hash` (see scope aliases `env-lineage/1`, `project-lineage/1`, `domain-lineage/1`). |
| `LineageSnapshot` | `lineage-snapshot/1` | dataclass | [`01_KERNEL.md §3.4`](01_KERNEL.md) | Provisional | Summarization-with-archival Merkle commitment for multi-year lineage. |

### 7.12a Coordination shapes (v1.1)

v1.1 addition (ADR-0045, [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md)). Environment-scoped self-organizing coordination.

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `EntityGroupShape` | `entity-group-shape/1` | dataclass | [`15_COORDINATION_SHAPES.md §3.1`](15_COORDINATION_SHAPES.md) | Draft | Meta-mechanism: group entities by predicate. |
| `BatchOperationShape` | `batch-operation-shape/1` | dataclass | [`15_COORDINATION_SHAPES.md §3.2`](15_COORDINATION_SHAPES.md) | Draft | Meta-mechanism: apply operation to a group. |
| `StagedSequenceShape` | `staged-sequence-shape/1` | dataclass | [`15_COORDINATION_SHAPES.md §3.3`](15_COORDINATION_SHAPES.md) | Draft | Meta-mechanism: sequenced operations with gates. |
| `StageDefinition` | `stage-definition/1` | dataclass | [`15_COORDINATION_SHAPES.md §3.3`](15_COORDINATION_SHAPES.md) | Draft | Stage within a StagedSequence. |
| `StreamPolicyShape` | `stream-policy-shape/1` | dataclass | [`15_COORDINATION_SHAPES.md §3.4`](15_COORDINATION_SHAPES.md) | Draft | Meta-mechanism: aggregate/propagate events. |
| `DerivedMetricShape` | `derived-metric-shape/1` | dataclass | [`15_COORDINATION_SHAPES.md §3.5`](15_COORDINATION_SHAPES.md) | Draft | Meta-mechanism: compute metrics from state. |
| `EnvironmentCoordinationProfile` | `env-coordination-profile/1` | dataclass | [`15_COORDINATION_SHAPES.md §4.4`](15_COORDINATION_SHAPES.md) | Draft | Per-env active coordination shapes across 3 scopes. |
| `CoordinationShapeBinding` | `coordination-shape-binding/1` | dataclass | [`15_COORDINATION_SHAPES.md §4.4`](15_COORDINATION_SHAPES.md) | Draft | Shape binding within an env's coordination profile. |
| `CoordinationShapeEvent` | `coordination-shape-event/1` | dataclass | [`15_COORDINATION_SHAPES.md §4.4`](15_COORDINATION_SHAPES.md) | Draft | Lineage event for shape lifecycle transitions. |
| `ProposedCoordinationShape` | `proposed-coordination-shape/1` | dataclass | [`15_COORDINATION_SHAPES.md §5`](15_COORDINATION_SHAPES.md) | Draft | Persona-proposed coordination pattern. |
| `CrossEnvCoordinationRequest` | `cross-env-coordination-request/1` | dataclass | [`15_COORDINATION_SHAPES.md §4.7`](15_COORDINATION_SHAPES.md) | Draft | Bilateral coordination request between envs. |
| `CrossEnvCoordinationResponse` | `cross-env-coordination-response/1` | dataclass | [`15_COORDINATION_SHAPES.md §4.7`](15_COORDINATION_SHAPES.md) | Draft | Accept / counter-propose / deny response. |
| `CrossEnvCoordinationBinding` | `cross-env-coordination-binding/1` | dataclass | [`15_COORDINATION_SHAPES.md §4.7`](15_COORDINATION_SHAPES.md) | Draft | Bilateral shape agreement between two envs. |
| `EnvironmentComposition` | `env-composition/1` | dataclass | [`05_ENVIRONMENT.md §2.2a`](05_ENVIRONMENT.md), [`15_COORDINATION_SHAPES.md §4.8`](15_COORDINATION_SHAPES.md) | Draft | Parent-child env hierarchy with rule cascade. |
| `ChildEnvFormationProposal` | `child-env-formation-proposal/1` | dataclass | [`15_COORDINATION_SHAPES.md §4.8.5`](15_COORDINATION_SHAPES.md) | Draft | Proposal to spawn child env within parent. |

### 7.12b Population dynamics (v1.1)

v1.1 addition (ADR-0048, ADR-0049, ADR-0050, [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md)). Bounded, environment-driven persona genesis with demographic regulation, a rigorous effective-population-size metric, and continuous diversity maintenance.

| Schema | Version | Form | Defined in | Stability | Used by |
|--------|---------|------|------------|-----------|---------|
| `PopulationPressureSignal` | `population-pressure-signal/1` | dataclass | [`16_POPULATION_DYNAMICS.md §4A`](16_POPULATION_DYNAMICS.md) | Draft | Kernel-measured genesis trigger (recruitment gap, role coverage, backlog, EPS). |
| `NicheDescriptor` | `niche-descriptor/1` | dataclass | [`16_POPULATION_DYNAMICS.md §4C`](16_POPULATION_DYNAMICS.md) | Draft | MAP-Elites behaviour-descriptor cell with occupancy + distinctiveness band. |
| `GenesisProposal` | `genesis-proposal/1` | dataclass | [`16_POPULATION_DYNAMICS.md §4D`](16_POPULATION_DYNAMICS.md) | Draft | Persona-authored seed-creation proposal (default-deny; `ReplicationBound`-gated). |
| `GenesisProvenance` | `genesis-provenance/1` | dataclass | [`16_POPULATION_DYNAMICS.md §4D`](16_POPULATION_DYNAMICS.md) | Draft | Newborn lineage record distinguishing genesis from fork. |
| `MentorshipEdge` | `mentorship-edge/1` | dataclass | [`16_POPULATION_DYNAMICS.md §4E`](16_POPULATION_DYNAMICS.md) | Draft | Mentor↔newborn maturation/scaffolding edge (secure base). |
| `PopulationPolicy` | `population-policy/1` | dataclass | [`16_POPULATION_DYNAMICS.md §4F`](16_POPULATION_DYNAMICS.md) | Draft | Operator demographic policy (r/K, density curve, descriptor mode, audit cadence). |
| `EffectivePopulationSizeEstimate` | `eps-estimate/1` | dataclass | [`16_POPULATION_DYNAMICS.md §4G`](16_POPULATION_DYNAMICS.md) | Draft | Kernel-computed `min(Ne_v, Ne_d)` founder-effect / monoculture signal. |
| `DiversityAudit` | `diversity-audit/1` | dataclass | [`16_POPULATION_DYNAMICS.md §4H`](16_POPULATION_DYNAMICS.md) | Draft | Periodic diversity-maintenance audit (novelty pressure, fitness-sharing, recalibration). |
| `CrossKernelGenesisRequest` | `cross-kernel-genesis-request/1` | dataclass | [`16_POPULATION_DYNAMICS.md §4J`](16_POPULATION_DYNAMICS.md) | Draft | Always-refused marker enforcing the cross-kernel genesis boundary (anti-circumvention). |

### 7.13 Adding or modifying schemas

A change to any schema in this registry MUST follow this process:

1. **Bump version** if any field is removed or its type changes; for additive changes (new optional fields), the existing version MAY be retained.
2. **Update this table** in the same PR.
3. **Update the migration tool** (see [`01_KERNEL.md §5`](01_KERNEL.md#5-schema-validation-inv-10)) with an explicit mapper from the previous version.
4. **Add or update an acceptance test** referencing the schema in [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).
5. The kernel MUST refuse messages whose `schema` field value is not present in this registry.

CI SHOULD verify that every `schema` field literal (matching `<name>/<integer>`) in source code is present in this table. Drift between code and registry is a release-blocking defect.

## 8. Key custody hierarchy

*The hierarchy fans out from the kernel master key into three branches: kernel operational keys (KMS tier), domain maintainer signing keys (KMS minimum; HSM required for domains with bodily-injury or export-controlled hazard classes), and env operator signing keys (per-env policy). Below kernel operational keys sit persona signing keys and lifecycle scope keys. Domain keys derive domain content signing keys (for DomainContext, tools, knowledge, recipes, safety extensions, standards, notations, lineage). Env keys derive env content signing keys and per-project signing keys (for project charter, lineage, members, milestones, and completion ceremonies).*

**Technical detail:** See [A.36](#appendix-a36).

### 8.1 Three custody tiers

*Tier 1 (Laptop): workstation-based keys for dev, demos, and hobby use. Tier 2 (KMS): cloud-managed key services (AWS KMS, Google Cloud KMS, Azure Key Vault, HashiCorp Vault) for standard production. Tier 3 (HSM): hardware security modules (FIPS 140-2 Level 3+ or 140-3) required for domains crossing bodily-injury or export-controlled hazard thresholds, and for regulated regimes (HIPAA, ITAR, EAR, FINRA, GDPR Article 9, EU AI Act Annex III, etc.).*

**Technical detail:** See [A.37](#appendix-a37).

### 8.2 .well-known/personaos-keys.json

*The personaos-keys/1 JSON schema publishes the kernel master public key, current and previous operational keys (with rotation schedule), and per-entity keys for domains, envs, projects, and personas. Federation peers fetch this URL to verify any v1.0 signature.*

**Technical detail:** See [A.38](#appendix-a38).

### 8.3 Rotation + revocation cascades

*Rotation schedules range from quarterly (master key) to per-version-bump (domain, env, project, persona). Historical signatures remain verifiable via archived keys. Revocation cascades propagate downward: compromised master revokes all derived keys; compromised domain notifies projects; compromised env notifies members; compromised project freezes work; compromised persona moves to DORMANT and re-signs SOUL. Archived keys are preserved at .well-known with rotation timestamps.*

**Technical detail:** See [A.39](#appendix-a39).

## 9. May-revision policies (universal)

These policies apply on every pathway, every adapter, every kernel operation:

### 9.1 LLM transport fault policy

*The error taxonomy defines retry/no-retry behaviour per HTTP status: rate-limit (429), overloaded (529), API (500), and timeout (504) errors get exponential backoff with max 3 retries. Auth (401), permission (403), not-found (404), billing (402), too-large (413), invalid-request (400), and content-refusal errors are not retried; each emits a signed event. Content refusals feed charter-drift detection.*

**Technical detail:** See [A.40](#appendix-a40).

### 9.2 Output schema violation reformat

*Schema-invalid output triggers a SCHEMA_VIOLATION event, one mechanical reformat retry (counted against budget), and on second failure the candidate is dropped with a malformed_output penalty.*

**Technical detail:** See [A.41](#appendix-a41).

### 9.3 Content policy refusal handling

*Provider-side refusal emits a signed CONTENT_REFUSAL event (not retried). Integrator decides: class demotion, human escalation, or content_refusal status. In v1.0, refusals also feed both persona and project charter-drift detection.*

**Technical detail:** See [A.42](#appendix-a42).

### 9.4 Context window overflow pipeline

*Compression cascade: drop COLD advisories, drop WARM advisories, summarise old history, drop env-scoped tactics, drop project/env context advisories, abort if identity blocks will not fit. Each step emits a signed CONTEXT_COMPRESSED lineage event. Identity blocks (Layer 1 + frozen Layer 2) are never dropped.*

**Technical detail:** See [A.43](#appendix-a43).

### 9.5 OWASP LLM01 retrieval-admission filter

Applied on every retrieved entry before envelope projection.

*The filter scope covers lessons, skills, tools, rubrics, episodic/semantic memories, co-signed summaries, A2A inbound messages, inter-persona DMs, project-scope memories, ProvenFact/Conjecture/Obligation/Disagreement statements, NotationConvention and external_link descriptions, StructuredFeedback raw_data, AmbientEvent payloads, and KnowledgeRef chunks. On match: suppress, quarantine, and emit INJECTION_DETECTED. Dedicated classifier with rotation.*

**Technical detail:** See [A.44](#appendix-a44).

## 10. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations).

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-PROTOCOLS-1 | Adapter parity testing surface is combinatorial (12 adapters × all v1.0 features). | Medium | High | Acceptance suite (`11_ACCEPTANCE_TESTS.md`) per adapter; cross-adapter parity tests (A-P10, A-PT6-PT9); exhaustive parity is operator concern. | v1.0 (suite); v1.1 (matrix CI). |
| R-PROTOCOLS-2 | Cache hit rate variance. New personas or heavy evolution lower hit rate below 80% target. | Low | Medium | Layer 1-2 cacheable per `cache_control`; per-persona evolution cadence operator-tuned; A-PT11 acceptance test. | v1.0 (cache); v1.1 (adaptive caching). |
| R-PROTOCOLS-3 | OTel cardinality explosion. Many tag dimensions inflate observability storage. | Medium | High | Sampling at trace level; per-metric cardinality limits; operator-defined tag whitelist; A-PT12 overhead target ≤ 2%. | v1.0 (sampling); v1.1 (adaptive caps). |
| R-PROTOCOLS-4 | Schema migration burden across prior versions to v1.0 (40+ entities). | Medium | High | Migration tool with explicit version mappers; A-PT13 acceptance test; CI drift check. | v1.0 (tool); ongoing. |
| R-PROTOCOLS-5 | HSM (Tier 3) custody is expensive. | Low | Medium | Operator decides per deployment risk profile; Tier 2 (cloud KMS) admissible for non-critical deployments; A-K-CUST acceptance test. | v1.0 (tiers); operator-tuned. |
| R-PROTOCOLS-6 | A2A federation trust establishment requires multi-operator agreements. Operational, not architectural. | Medium | High | Documented onboarding flow; reputation gossip with kernel-attested provenance; trust caps on new peers. | v1.0 (substrate); v1.1 (onboarding tooling). |
| R-PROTOCOLS-7 | MCP-Zero discovery quality. Semantic tool search may surface wrong tools. | Medium | Medium | Smoke test on first invocation; reputation-weighted ranking; user-in-loop for high-stakes; per-domain tool registries. | v1.0 (smoke test); v1.1 (reputation rank). |
| R-PROTOCOLS-8 | Cross-version compatibility. v1.0 reads prior-version forward-compat; v1.0 schemas refused by older kernels. Federation requires same-version peers. | Medium | Medium | Migration tool; explicit version-handshake at AgentCard exchange; operator policy on cross-version federation. | v1.0 (migration); v1.1 (compat-shim). |
| R-PROTOCOLS-9 | `DeploymentProfile` is v1.0-introduced; the prior security model is silent on `principal_topology`. Single-user deployments MUST declare `operator_is_user`. | High | Low | v1.0 ships degraded gate; operator policy at deployment time; A-K-DP acceptance test; future top-level revision will fold into security model. | v1.0 (gate); v2.0 (top-level fold-in). |
| R-PROTOCOLS-10 | Physical-world coupling primitives (`04_PROJECT §26a`, `06_DOMAIN §5.5-§5.6/§6`) are v1.0-introduced; phase docs are silent. | Low | Low | Phase docs win conflicts; no conflict exists — v1.0 extends into uncovered territory; cross-references make the additions discoverable. | v1.0 (substrate); v2.0 (phase-doc retro-merge). |

## 10a. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-PROTOCOLS-1 | A2A AgentCard `reputation_summary` schema: opaque score, multi-dimensional vector, or cohort-stratified? | Reputation WG | v1.1 reputation schema. |
| OQ-PROTOCOLS-2 | MCP-Zero discovery (R-PROTOCOLS-7): smoke-test design — what's the canonical "is this tool what it claims?" check? | — | v1.1 smoke-test protocol. |
| OQ-PROTOCOLS-3 | Anthropic `cache_control` policy: prompt layers 1-2 cacheable; what about layer 3 (relationship state) when it changes per turn? Mid-cache invalidation? | Prompt engineers | v1.1 cache policy. |
| OQ-PROTOCOLS-4 | Cross-version federation compat-shim (R-PROTOCOLS-8): translate-on-read, translate-at-handshake, or operator-explicit deny? | Federation WG | v1.1 compat design. |
| OQ-PROTOCOLS-5 | OTel cardinality whitelist (R-PROTOCOLS-3): default whitelist per deployment profile, or operator-defined from zero? | Observability WG | v1.1 whitelist defaults. |
| OQ-PROTOCOLS-6 | DeploymentProfile in v2.0 (R-PROTOCOLS-9): top-level security-model fold-in — which existing sections does it merge into, and what does the migration path look like? | — | v2.0 vision. |
| OQ-PROTOCOLS-7 | Key custody tier defaults: v1.0 ships Tier 2 (cloud KMS) baseline; should safety-critical deployments require Tier 3 (HSM) by default? | Security auditors | v1.1 default policy. |

## 11. Acceptance tests

```text
A-PT1   MCP tools registered in v1.0 kernel are invocable from any
        MCP-compliant client; schema validated.
A-PT2   MCP resources (knowledge, artifacts) accessible read-only;
        signature verifiable.
A-PT3   MCP prompts for persona exposed skills: prompt:<persona>/<skill>
        renders persona's identity + skill context.
A-PT4   A2A AgentCard signed; verifiable via .well-known endpoint.
A-PT5   A2A inter-kernel persona invocation works; trace propagates
        via W3C Trace Context.
A-PT6   Claude Code adapter: persona's SOUL projects to Skill file
        with exact name/description/allowed_tools mapping.
A-PT7   OpenAI Agents SDK adapter: Agent constructed; output_guardrail
        wraps verifier.
A-PT8   LangGraph adapter: persona as subgraph; verifier_edge active.
A-PT9   CrewAI adapter: Agent with role/goal/backstory; injected
        verify tool non-removable.
A-PT10  MCP Proxy: every tool call passes kernel verifier + safety;
        no persona changes.
A-PT11  Anthropic cache_control: Layer 1 + 2 marked cacheable; cache
        hit rate ≥ 80% across N envelope mints with same persona.
A-PT12  OTel spans with personaos.* on every kernel operation;
        cross-boundary propagation; overhead ≤ 2%.
A-PT13  Schema version table: 40+ entities; unknown versions refused
        with structured error.
A-PT14  Key custody: master + scope keys in operator-chosen tier;
        domain/project/env keys derived correctly.
A-PT15  Key rotation: new key issued; old key archived in
        .well-known; historical signatures still verifiable.
A-PT16  Key revocation cascade: compromised domain → projects
        notified; compromised master → emergency cascade.
A-PT17  May-revision policies operational:
        - LLM transport retry policy (3 retries max, Retry-After honored)
        - Schema reformat (1 retry; counted against budget)
        - Content refusal (no retry; signed; charter-drift feed)
        - Context overflow (cascade compression; identity preserved)
        - OWASP filter (extended scope across all entry types)
A-PT18  v1.0 adapter compat: all 12 adapters accept v1.0 envelopes;
        ignore unknown fields; produce compatible outputs.

A-PT19  Five intra-env channels: BlackboardEvent / ProvenFact /
        DirectMessage / CandidateTable / GoalStack each enforce
        their write/read semantics; out-of-topology DM emits
        CONSTRAINT_VIOLATION{kind=topology}; ProvenFact refused
        without verifier_cascade_id.
A-PT20  Gossip layer: card publish propagates to federation peers
        within ttl_hops; revocation evicts caches; hostile flooder
        damped by per-peer rate + reputation.
A-PT21  Joined env lifecycle: propose → consent → instantiate →
        run → retire; single-host-kernel rule enforced;
        constraint composition most-restrictive-wins; mid-task
        consent revocation triggers controlled-shutdown with
        partial AnswerPackage distribution.
A-PT22  ReputationSummary requires sig_threshold ≥ 2 co-signers
        for federation/public tiers; per-peer credit cap saturates;
        30-day expiry forces restate; sybil cluster gets near-zero
        weight.
A-PT23  Disputed-flag preservation: a single specific dispute is
        projected separately on ReputationSummary (not blended);
        future find_persona() consults dispute field independently.
```

## 12. Where to read next

- Kernel responsibilities + signing details: [`01_KERNEL.md`](01_KERNEL.md)
- Persona model: [`02_PERSONA.md`](02_PERSONA.md)
- Adapter rollout follows the release gate process

## Technical Appendix

The appendices below contain the full technical schemas, data structures, protocol specifications, and adapter projection details referenced throughout this document. Each appendix is referenced from the section where it applies.

### A.1 MCP tool / resource / prompt registry

<a id="appendix-a1"></a>

```text
TOOLS
  Every callable operation a persona can invoke is registered as an
  MCP tool. PersonaOS exposes:
    mcp__personaos__*           kernel-native tools
    mcp__personaos__verify
    mcp__personaos__sandbox_exec
    mcp__personaos__find_lesson
    mcp__personaos__find_skill
    mcp__personaos__remember
    mcp__personaos__list_memories
    mcp__personaos__set_boundary
    mcp__personaos__list_tools
    mcp__personaos__discover_federated_tools
    mcp__personaos__request_tool  (MCP-Zero style active discovery)
    mcp__personaos__goal_progress
    mcp__personaos__list_personal_goals
    
  Domain tools registered via DomainContext.tools_required:
    mcp__ngspice__simulate
    mcp__lean__verify
    mcp__arxiv__search
    mcp__drc__check
    mcp__kicad_cli__*
    ...
  
  Persona-learned skills exposed via:
    mcp__personaos__invoke_persona_skill(persona_id, skill_id, args)
  
RESOURCES
  Read-only references to external content:
    mcp://personaos/knowledge/lesson/{lesson_id}
    mcp://personaos/knowledge/k_line/{kline_id}
    mcp://personaos/knowledge/proven_fact/{fact_id}
    mcp://personaos/artifacts/bundle/{bundle_id}/{artifact_id}
    mcp://personaos/memory/{persona_id}/{memory_id}
    mcp://personaos/domain/{domain_id}/knowledge_ref/{ref_id}
    mcp://personaos/standards/{standard_id}
  
PROMPT TEMPLATES
  Persona's exposed_skills published as MCP prompts:
    prompt:<persona_id>/<skill_id>
  
  e.g.:
    prompt:01HZ_sparky/refute_with_evidence
    prompt:01HZ_volt/buck_design_review
```

### A.2 MCP-Zero active tool discovery

<a id="appendix-a2"></a>

```python
mcp__personaos__request_tool(
    need="simulate quantum master equation dynamics",
    context={
        "domain_hint": "quantum_device_design",
        "preferred_latency_ms": 1000,
        "max_cost_per_call": 0.50,
    },
    top_k=5,
)
# Returns: candidate tools ranked by semantic similarity + trust + cost
```

### A.3 MCP federated discovery

<a id="appendix-a3"></a>

```python
mcp__personaos__discover_federated_tools(
    domain_hint="...",
    peer_trust_threshold=0.5,
    only_publishers_with_attestation=True,
)
# Returns: tools from peer kernels' registries; trust-filtered
```

### A.4 AgentCard dataclass

<a id="appendix-a4"></a>

```python
@dataclass
class AgentCard:
    schema: str = "agent-card/1"
    id: str
    name: str
    provider: str                         # operator/org publishing
    version: str
    description: str                      # ≤ 120 chars
    capabilities: list[str]               # discoverable capabilities
    interfaces: list[InterfaceSpec]       # MCP / A2A / HTTP endpoints
    skills: list[ExposedSkill]            # from SOUL.exposed_skills
    securitySchemes: list[SecurityScheme] # Ed25519, OAuth, etc.
    security: list[SecurityRequirement]
    
    # Project context
    project_summary: ProjectSummary | None   # if persona in projects
    
    # Environment context
    env_summary: EnvSummary | None           # if persona has env presences
    
    # Domain context
    domain_curatorships: list[str]           # domains where persona is curator
    
    signature: bytes                      # Ed25519 over canonical fields
```

### A.5 A2A discovery protocol

<a id="appendix-a5"></a>

```text
.well-known/agent-cards.json
  Lists all locally-published AgentCards.

.well-known/agent-cards/{agent_id}
  Individual AgentCard.

A2A inbound (other agents call us):
  Other kernel finds our AgentCard via .well-known;
  invokes our persona's exposed skill via A2A protocol.

A2A outbound (we call other agents):
  Our persona discovers peer agent via .well-known gossip;
  invokes their AgentCard skill via A2A protocol.

Federated project discovery:
  Cross-kernel project member admission via A2A
  PROJECT_INVITATION / RECRUIT_PROPOSAL events.

Federated env discovery:
  Cross-kernel env presence via A2A ENV_INVITATION events.

Federated domain emergence:
  Cross-kernel domain discovery; promotion gates require multi-kernel
  signatures.
```

### A.6 Five intra-environment channels

<a id="appendix-a6"></a>

```text
CH-1 Blackboard         event-sourced log     persona ↔ persona  broadcast
CH-2 ProvenFacts        G-set CRDT            persona ↔ persona  attested writes
CH-3 DirectMessage      kernel-routed         persona → persona  addressed
CH-4 CandidateTable     kernel-only writer    kernel → all       acceptance state
CH-5 GoalStack          kernel-only writer    kernel → all       L0-L6 steering
```

### A.7 BlackboardEvent dataclass

<a id="appendix-a7"></a>

```python
@dataclass
class BlackboardEvent:
    schema: str = "blackboard-event/1"
    event_id: str                          # ULID
    environment_id: str                    # in v1.0, ambient stream id
    round_num: int
    sequence_in_round: int                 # monotonic per round
    kind: str                              # OBSERVATION | CANDIDATE | ...
    actor_persona_id: str
    actor_role: str
    parent_event_ids: list[str]            # causality
    payload: dict
    signed_by: bytes
```

### A.8 ProvenFact dataclass

<a id="appendix-a8"></a>

```python
@dataclass
class ProvenFact:
    schema: str = "proven-fact/1"
    fact_id: str                           # content-addressed (sha256)
    scope: Literal["task", "project", "env"]
    statement: str
    evidence_event_ids: list[str]
    verifier_cascade_id: str               # MUST be set; no fact without verifier
    proven_at: datetime
    signed_by: bytes
```

### A.9 DirectMessage dataclass

<a id="appendix-a9"></a>

```python
@dataclass(frozen=True)
class DirectMessage:
    schema: str = "direct-message/1"
    event_id: str
    round_num: int
    sequence_in_round: int
    sender_persona_id: str
    recipient_persona_id: str              # exactly one
    in_reply_to: str | None
    kind: Literal["REQUEST", "RESPONSE", "ASK_CLARIFY", "DELEGATE",
                   "RESAMPLE_REQUEST", "REGRADE_REQUEST", "STEER"]
    body: str                              # ≤ 4k chars
    structured: dict | None
    deadline_round: int | None
    signed_by: bytes
```

### A.10 CandidateTable and GoalStack dataclasses

<a id="appendix-a10"></a>

```python
@dataclass
class CandidateTable:
    schema: str = "candidate-table/1"
    candidates: dict[candidate_id, CandidateState]   # PROPOSED → ACCEPTED
    last_updated_round: int

@dataclass
class GoalStack:
    schema: str = "goal-stack/1"
    goals: list[Goal]                      # L0 (operational) → L6 (purpose)
    last_revised_round: int
```

### A.11 Gossip protocol — GossipEvent dataclass, protocol, and trust-weighted reach

<a id="appendix-a11"></a>

```python
@dataclass
class GossipEvent:
    schema: str = "gossip-event/1"
    event_id: str
    action: Literal["publish", "update", "revoke"]
    card: AgentCard | EnvCard | DomainContextCard
    originating_kernel: str
    timestamp: datetime
    ttl_hops: int                          # default 3; bounded fanout
    visited_kernels: list[str]             # loop prevention
    signed_by: bytes
```

```text
1. ANNOUNCE on card publish (tier ∈ {federation, public})
     originator gossips to its federation peers (fanout = 8 default)
2. FORWARD ONCE per peer
     receiving kernel verifies signature, checks not-yet-seen,
     caches card in FEDERATED registry, forwards to its peers
     (ttl_hops decremented; visited_kernels appended)
3. PERIODIC RE-ANNOUNCE
     originator re-gossips on a cadence (default 1h) to refresh
     caches; `expires_at` on card forces validation
4. REVOCATION
     same fanout; receivers evict from cache; stale caches mitigated
     by short expires_at
```

```text
reach(card) = Σ over peer kernels p:
                f(trust(p), peer_reputation(originator on p),
                  card.visibility_tier)

where f() weights:
  - peer kernels with higher mutual trust forward sooner
  - originators with low reputation see reduced fanout
  - public-tier cards reach further than federation-tier
```

### A.12 Joined environment lifecycle

<a id="appendix-a12"></a>

```text
1. PROPOSE
   initiator (persona_A in kernel_K1) emits PROPOSE_JOINED_ENV{
     blueprint_ref, required_roles, candidate_peers (PersonaCards),
     task | project_ref, budget, duration_hint, consent_terms
   }
2. INVITE
   K1 sends signed A2A invitation to each candidate's home kernel.
3. CONSENT
   each receiving kernel runs consent flow (§3C.4); persona body
   sees INBOUND_PROPOSAL on its Blackboard; emits
   ACCEPT | DECLINE | COUNTER.
4. INSTANTIATE
   if all required roles accept: K1 mints EnvironmentInstance and
   is designated SINGLE HOST KERNEL by mutually-signed agreement.
5. RUN
   host kernel owns Blackboard, ProvenFacts, CandidateTable, GoalStack.
   Peer kernels run their personas' bodies locally; every emitted
   event is signed by peer kernel before streaming to host;
   host re-signs on append (admission attestation); both signatures
   preserved.
6. PUBLISH
   host publishes JoinedEnvCard (signed by all participants) for
   discoverability.
7. RETIRE
   on task/project completion: host produces AnswerPackage,
   jointly signs with each participant kernel's key, distributes
   to each peer's LineageGraph. Each peer credits its persona locally.
```

### A.13 Trust posture and constraint composition

<a id="appendix-a13"></a>

```text
TRUST POSTURE
  peer streams signed events to host → host trusts peer's signature
  for authorship; host's re-sign attests admission.
  ProvenFacts written by peer's persona carry both signatures.
  Host publishes full event log to all participants at retire;
  divergence between peer-sent and host-recorded triggers
  DISPUTE event in both reputation ledgers.

CONSTRAINT COMPOSITION (most-restrictive-wins)
  effective = ⨅(host_kernel_constraints,
                 each_peer_kernel_constraints,
                 joined_env_blueprint_constraints,
                 task_inherited_constraints,
                 universal_harm_floor)

  - tool forbidden by any peer → forbidden in joined env
  - token cap from any peer → lowest cap binds
  - env charter from blueprint composes with persona charters
```

### A.14 Consent flow

<a id="appendix-a14"></a>

```text
inbound proposal arrives at K2 for persona_B
  │
  ├─ intent ∈ VisibilityPolicy.consent_required_for?
  │
  ▼ yes:
  K2 raises CONSENT_REQUEST event on persona_B's Blackboard
    │  persona body sees request in its observation surface
    │  emits CONSENT_GRANT | CONSENT_DECLINE | ASK_HUMAN
    │  if ASK_HUMAN: forward to operator via host bridge
    │    (default-decline on timeout)
  ▼ no:
  auto-admit (subject to remaining filters: reputation, rate, scope)
```

### A.15 Cross-kernel DM visibility — modes and dataclass

<a id="appendix-a15"></a>

```text
DEFAULT MODE (host-visible)
  All DirectMessages in a joined env, including cross-kernel pairs
  (persona K1.A → persona K2.B), pass through the host kernel's
  blackboard.  The host can read content (signed audit trail; the
  host's kernel signature attests the host did NOT modify).  This
  is honest about the architecture: the host owns the env's state
  and is responsible for safety floor enforcement, so it must be
  able to inspect what flows through.

OPT-IN E2E MODE (end-to-end signed-only)
  Sender and recipient personas may flag a DirectMessage as
  e2e_encrypted=True.  The content is encrypted under the
  recipient's persona key; the host signs the envelope (route,
  sender, recipient, timestamp, length) but cannot read content.
  Safety floor on the host runs against ONLY the envelope metadata;
  the kernel cannot enforce content-based refusals.  The recipient's
  kernel decrypts and runs its OWN safety floor before delivery.

  Restrictions:
    - e2e_encrypted DMs are REFUSED in envs marked
      safety_critical=True (the host must be able to inspect content
      where physical/info hazard axes apply).
    - e2e_encrypted DMs are REFUSED when sender + recipient are on
      the same kernel (the architectural value disappears; refuse to
      ceremonialise it).
    - Operator policy may refuse e2e_encrypted DMs entirely per env.

  Audit trail preserves envelope metadata regardless of encryption;
  content is private but presence-of-DM is signed.
```

```python
@dataclass
class CrossKernelDMVisibility:
    schema: str = "cross-kernel-dm-visibility/1"
    dm_id: str
    sender_kernel_id: str
    sender_persona_id: str
    recipient_kernel_id: str
    recipient_persona_id: str
    env_id: str

    e2e_encrypted: bool                     # opt-in per DM
    encryption_key_ref: str | None          # recipient's persona key id
                                            # (resolved at delivery; never
                                            # exposed to host)

    # Host visibility flags (kernel-set, not user-controllable)
    host_can_read_content: bool             # False iff e2e_encrypted
    host_can_read_envelope: bool = True     # always True
    host_safety_floor_inspected: bool       # True for default mode;
                                            # envelope-only for e2e

    # Safety floor at recipient's end
    recipient_safety_floor_passed: bool

    # Refusal reasons (signed)
    refusal_kind: str | None                # if DM refused

    signed_by_sender_kernel: bytes
    signed_by_host_kernel: bytes
    signed_by_recipient_kernel: bytes
```

### A.16 ReputationSummary dataclass

<a id="appendix-a16"></a>

```python
@dataclass(frozen=True)
class ReputationSummary:
    schema: str = "reputation/1"
    persona_id: str
    role_slot: str                         # role-relative
    as_of: datetime
    interactions_total: int
    interactions_accepted: int
    interactions_disputed: int
    interactions_blocklisted_by: int
    contribution_credit_received: float    # peer-capped (anti-farming)
    lineage_participation_count: int       # signed joined-env participations
    peer_endorsements: list[EndorsementRef]
    outcome_corroborations: int            # peer confirms persona's claims
    rubric_judge_calibration: float | None # judge-human correlation if used
    co_signed_by: list[str]                # peer kernels attesting
    sig_threshold: int                     # min co-signers for trust tier
    expires_at: datetime                   # default 30d; forces restate
    signature: bytes                       # publishing kernel
```

### A.17 Reputation signal model

<a id="appendix-a17"></a>

```text
PEER ENDORSEMENT
  signed ENDORSEMENT event from joined-env collaborator;
  cites specific skill/tactic/rubric dimension contributed.
OUTCOME CORROBORATION
  peer confirms persona's claim matched downstream reality
  (e.g., "their thermal estimate matched our measurement").
LINEAGE PARTICIPATION
  count of signed joined-env retirements with non-trivial
  contribution; weight scaled by env reach.
DISPUTE PRESERVATION
  single high-credibility dispute weighs more than 100 generic
  "accepted" events of low specificity (mirrors divergent
  verifier dissent-preservation).
```

### A.18 Anti-gaming rules and outreach intent thresholds

<a id="appendix-a18"></a>

```text
1. PER-PEER CREDIT CAP
   repeated good interactions with the same peer saturate quickly;
   cannot build unbounded reputation by colluding with one peer.

2. CO-SIGNATURE REQUIREMENT
   publishing reputation to FEDERATED/HUB tiers requires
   sig_threshold ≥ 2 co-signers (peers that participated in
   the cited interactions); prevents self-inflation.

3. DECAY
   ReputationSummary.expires_at = 30 days default;
   reputation must be restated by re-cosigning peers.

4. SYBIL RESISTANCE
   peer kernels weighted by mutual trust + age + diversity of
   their own ReputationSummary co-signers; a cluster of new
   kernels mutually co-signing each other gets near-zero weight.

5. REACH × DIVERSITY WEIGHTING
   reach(reputation) = Σ peer_weight × diversity_bonus
   diversity_bonus rewards endorsements from kernels in different
   trust clusters; punishes echo-chamber reputation.

6. DISPUTED-FLAG PRESERVATION
   a single specific dispute is non-aggregatable: preserved
   verbatim in the ledger and projected into ReputationSummary
   as a separate field, not blended into "interactions_accepted".
```

```text
intent                          min reputation tier
─────────────────────────────────────────────────────
one_shot_task                   fresh OK (any signed)
joined_env (short)              tenant OR ≥ N interactions
long_running_collab             federation + tenant attestation
mutation_proposal_exchange      federation + co-signed reputation
soul_inspection                 tenant only (no cross-kernel default)
```

### A.19 RelationshipFederationSync dataclass

<a id="appendix-a19"></a>

```python
@dataclass
class RelationshipFederationSync:
    schema: str = "relationship-federation/1"
    sync_id: str
    edge_id: str                                 # the §11.4 edge being synced
    home_kernel: str                             # the kernel that minted the
                                                 # edge (canonical persona_a)
    peer_kernel: str                             # the kernel hosting
                                                 # persona_b

    # Replication mode
    replication_mode: Literal[
        "shadow",       # peer holds read-only shadow; mutations require
                        # home kernel's signature first
        "co_owned",     # both kernels mutate; conflict resolution by
                        # signed-timestamp + Lamport tiebreak
    ]

    # Sync state
    last_sync_at: datetime
    last_sync_event_seq: int                     # monotone; per-edge
    sync_lag_budget: timedelta                   # operator-policy-bounded;
                                                 # default 5min for active
                                                 # edges, 24h for dormant

    # Revocation cascade
    revocation_propagation_required: bool = True # an `ended` transition on
                                                 # either kernel forces
                                                 # immediate sync; failure
                                                 # to propagate within
                                                 # sync_lag_budget escalates
                                                 # to operator

    # Anti-Goodhart for federated trust — the home kernel cannot inflate
    # trust_a_of_b without peer kernel observing matching joint_successes
    # in shared lineage; mismatched joint_successes counters trigger
    # FEDERATED_TRUST_DISCREPANCY.
    discrepancy_audit_active: bool = True

    signed_by_home: bytes
    signed_by_peer: bytes
```

### A.20 Replication semantics (shadow and co-owned modes)

<a id="appendix-a20"></a>

```text
SHADOW MODE (default for cross-kernel edges where one kernel is the
             relationship's natural owner — e.g. mentor's home kernel
             holds the edge, learner's kernel shadows)
  Home kernel:   writes mutations; signs.
  Peer kernel:   receives signed mutations via A2A; verifies; appends
                 to local shadow.  Peer's persona may PROPOSE mutations
                 but they take effect only when home kernel counter-signs.
  Conflicts:     impossible by construction (single writer).

CO_OWNED MODE (default for symmetric edges — peer collaborators on the
              same long-arc project, neither's kernel is the owner)
  Either kernel: writes mutations with monotone seq + signed timestamp.
  Conflicts:     resolved by (timestamp, kernel_id) Lamport ordering;
                 losing-side mutation enters CONFLICT_PARKED state and
                 must be re-signed by losing-side persona after seeing
                 the winning side.  Revocations always win regardless
                 of ordering (terminal precedence).
  Cost:          higher; both kernels run conflict-resolution paths.
```

### A.21 OpenTelemetry semantic conventions

<a id="appendix-a21"></a>

```text
KERNEL OPERATIONS
  personaos.kernel.envelope_mint              ms
  personaos.kernel.safety_check               ms
  personaos.kernel.signing                    ms
  personaos.kernel.dispatch_task              ms

TASK
  personaos.task.id                           string
  personaos.task.class                        enum (10)
  personaos.task.pathway                      enum (8)
  personaos.task.fingerprint                  string
  personaos.task.duration_ms                  ms
  personaos.task.status                       enum

PERSONA
  personaos.persona.id                        string
  personaos.persona.mode_entry                enum (14)
  personaos.persona.mode_exit                 enum
  personaos.persona.action                    enum
  personaos.persona.disposition               enum
  personaos.persona.charter_drift_detected    bool

PROJECT
  personaos.project.id                        string
  personaos.project.status                    enum
  personaos.project.milestone_reached         string
  personaos.project.obligation                string

ENVIRONMENT
  personaos.environment.id                    string
  personaos.environment.type                  enum
  personaos.environment.member_admission      string
  personaos.environment.ambient_event         enum
  personaos.environment.notification_routed   string
  personaos.environment.dormant_member_wake   enum (6 wake paths)
  personaos.environment.cross_env_offer       enum (proposed/delivered/
                                              accepted/declined/expired)
  personaos.environment.guest_presence        enum (created/renewed/
                                              expired/revoked/promoted)

DOMAIN
  personaos.domain.id                         string
  personaos.domain.stage                      enum (4)
  personaos.domain.probe_phase                enum
  personaos.domain.promotion_event            string

VERIFIER + PANEL
  personaos.verifier.cascade_stage            enum
  personaos.verifier.verdict                  bool
  personaos.verifier.rotation_active          bool
  personaos.panel.id                          string
  personaos.panel.verdict                     enum
  personaos.panel.dissent_vector              dict

LINEAGE
  personaos.lineage.scope                     enum (4)
  personaos.lineage.event_kind                enum
  personaos.lineage.signed                    bool

BUDGET
  personaos.budget.consumed                   number
  personaos.budget.threshold_crossed          bool

SAFETY
  personaos.safety.source                     enum (8)
  personaos.safety.refusal                    bool
  personaos.safety.classifier_id              string

LIFECYCLE
  personaos.lifecycle.transition              enum
  personaos.lifecycle.signed                  bool
```

### A.22 Anthropic cache_control — PromptBlock dataclass and API rendering

<a id="appendix-a22"></a>

```python
@dataclass(frozen=True)
class PromptBlock:
    text: str
    cacheable: bool                       # True layers 1-2
    origin: Literal[
        "frontmatter", "section_who", "section_how",
        "section_will_not", "section_contract",
        "evolve_tactics", "evolve_communication", "evolve_other",
        "advisory_lessons", "advisory_skills", "advisory_tools",
        "task_framing",
        "project_context", "env_context",
        "domain_advisory"
    ]
```

```json
{
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "...frozen identity block (Layer 1)...",
          "cache_control": { "type": "ephemeral" }
        },
        {
          "type": "text",
          "text": "...evolved tactics (Layer 2)...",
          "cache_control": { "type": "ephemeral" }
        },
        {
          "type": "text",
          "text": "...project context (Layer 3)..."
          // no cache_control; Layer 3 is dynamic
        }
      ]
    }
  ]
}
```

### A.23 Claude Code adapter projection

<a id="appendix-a23"></a>

```text
PROJECTION:
  Persona's SOUL.md projects into Claude Code Skill OR Subagent file:
    name        from SOUL.name
    description from SOUL.description (≤120 char; identical mapping)
    allowed_tools from SOUL.allowed_tools (identical mapping)
    model       from envelope.preferred_model
    system prompt from envelope.concatenated_prompt() (Layer 1 + 2 + 3 + 4)
    cache_control on Layer 1 + 2

ADAPTER TYPE: bidirectional (PersonaOS as MCP server consumed by Claude
              Code; Claude Code subagents project to PersonaOS personas)

VERIFIER INTEGRATION: kernel's verifier cascade exposed as PreToolUse
                      hooks in Claude Code
```

### A.24 OpenAI Agents SDK adapter projection

<a id="appendix-a24"></a>

```text
PROJECTION:
  Agent(
    name=SOUL.name,
    instructions=envelope.concatenated_prompt(),
    tools=[...mcp_tools...],
    output_type=envelope.output_schema,
    handoffs=[...],
  )

VERIFIER: @output_guardrail decorator wrapping kernel.verify
```

### A.25 LangGraph adapter projection

<a id="appendix-a25"></a>

```text
PROJECTION:
  Persona as subgraph node:
    SystemMessage(content=envelope.concatenated_prompt())
    ProvenFacts → Annotated[list, add] state field
    Verifier as conditional edge: verifier_edge(kernel)
    Cohort assembly as parent graph routing
```

### A.26 CrewAI adapter projection

<a id="appendix-a26"></a>

```text
PROJECTION:
  Agent(
    role=SOUL.primary_disposition + "_leaning",
    goal=envelope.description,
    backstory=SOUL "Who I am" section,
    tools=[...mcp_tools...],
    verifier=injected_kernel_verify_tool,  # non-removable
  )
```

### A.27 Microsoft Agent Framework (MAF) adapter projection

<a id="appendix-a27"></a>

```text
PROJECTION:
  Personas = MAF Agents
  Round = GroupChat
  Termination predicate calls kernel.acceptance_check
```

### A.28 Pydantic-AI adapter projection

<a id="appendix-a28"></a>

```text
PROJECTION:
  Persona as Agent[Deps, Out]:
    Typed dependencies
    output_type from envelope.output_schema
    output_validator = kernel.acceptance_check
```

### A.29 DSPy adapter projection

<a id="appendix-a29"></a>

```text
PROJECTION:
  Persona as dspy.Module
  Toolsmith persona may invoke dspy.GEPA / dspy.MIPROv2 as mutation
  operator over another persona's tactics; metric = kernel verifier
```

### A.30 smolagents adapter projection

<a id="appendix-a30"></a>

```text
PROJECTION:
  Experimenter persona as smolagents.CodeAgent
  Kernel intercepts post-run for verifier + lineage
```

### A.31 Semantic Kernel adapter projection

<a id="appendix-a31"></a>

```text
PROJECTION:
  Persona as ChatCompletionAgent
  SK kernel filter calls PersonaOS verifier
```

### A.32 MCP Server projection

<a id="appendix-a32"></a>

```text
PersonaOS kernel exposed as MCP server.
Any MCP-compliant client (Claude Code, custom client, etc.) can:
  - list personas (via mcp__personaos__list_personas)
  - invoke a persona's skill (via prompt:<persona>/<skill>)
  - read knowledge (via mcp://personaos/knowledge/...)
  - call kernel tools (mcp__personaos__verify, etc.)
```

### A.33 A2A Server projection

<a id="appendix-a33"></a>

```text
Each persona published as signed AgentCard at .well-known/.
Other kernels can discover + invoke via A2A protocol.
Cross-kernel project / env / domain coordination supported.
```

### A.34 MCP Proxy mode projection

<a id="appendix-a34"></a>

```text
PersonaOS kernel sits in front of third-party MCP servers.
Every tool call passes through kernel verifier + safety floor.
No persona code changes; transparent proxy.
```

### A.35 Adapter contract — kernel vs. body ownership

<a id="appendix-a35"></a>

```text
KERNEL OWNS                           BODY OWNS
─────────────────────────────         ─────────────────────────────
Soul / identity                       LLM call
Verifier cascade                      Tool dispatch
Invariant enforcement                 Persistence
Candidate acceptance                  Observability transport (OTel)
LineageGraph append                   Scheduling
ProvenFacts CRDT write-through        
```

### A.36 Key custody hierarchy diagram

<a id="appendix-a36"></a>

```text
                   KERNEL MASTER KEY
                   (operator policy decides tier; typically HSM
                    in production)
                          │
            ┌─────────────┼─────────────────────────────┐
            │             │                             │
            ▼             ▼                             ▼
    KERNEL          DOMAIN MAINTAINER          ENV OPERATOR
    OPERATIONAL     SIGNING KEYS               SIGNING KEYS
    KEYS            (Tier: KMS min;             (Tier: per-env
    (Tier: KMS)      HSM for domains whose      operator policy)
        │            physical_harm_class ≥
        │            bodily_injury OR
        │            information_hazard_class ≥
        │            export_controlled)
        │                    │                            │
   ┌────┴────┐               │                            │
   │         │               │                            │
   ▼         ▼               ▼                            ▼
 PERSONA  LIFECYCLE     DOMAIN CONTENT              ENV CONTENT
 SIGNING  SCOPE KEYS    SIGNING KEYS                SIGNING KEYS
 KEYS                    (DomainContext,            (EnvironmentInstance,
                         DiscoveredTool,            EnvironmentLineage,
                         ingested KnowledgeRef,     ambient events,
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

### A.37 Three custody tiers

<a id="appendix-a37"></a>

```text
TIER 1: LAPTOP
  Workstation master key + per-scope keys.
  Acceptable for: dev, demos, hobby deployments.
  NOT acceptable for: production with PII or regulated data.

TIER 2: KMS
  Cloud-provider-managed key service (AWS KMS, Google Cloud KMS,
  Azure Key Vault, HashiCorp Vault).
  Standard production tier.

TIER 3: HSM
  Hardware security module (FIPS 140-2 Level 3+ or 140-3,
  AWS CloudHSM, Azure Dedicated HSM, on-prem HSM).
  Required for: domains whose persona-inferred axes cross
                physical_harm_class ≥ bodily_injury OR
                information_hazard_class ≥ export_controlled,
                AND any deployment whose operator policy explicitly
                names a regulated regime (HIPAA, ITAR, EAR, FINRA,
                GDPR Article 9, EU AI Act Annex III, etc.) —
                substrate carries no domain list; operator policy
                does.
```

### A.38 .well-known/personaos-keys.json schema

<a id="appendix-a38"></a>

```json
{
  "schema": "personaos-keys/1",
  "kernel_master_public_key": "ed25519:...",
  "operational_public_keys": {
    "current": "ed25519:...",
    "previous": ["ed25519:..."],
    "rotation_schedule": "quarterly"
  },
  "domain_maintainer_keys": {
    "<domain_id>": { "current": "ed25519:...", "previous": [] }
  },
  "env_operator_keys": { "<env_id>": { ... } },
  "project_signing_keys": { "<project_id>": { ... } },
  "persona_signing_keys": { "<persona_id>": { ... } }
}
```

### A.39 Key rotation and revocation cascades

<a id="appendix-a39"></a>

```text
ROTATION
  Master key:           per operator schedule (typically quarterly)
  Operational:          per rotation policy (every N tasks)
  Domain:               per domain version bump
  Env:                  per env charter version bump or operator decision
  Project:              per major project version event
  Persona:              per persona version bump
  
  Historical signatures verifiable forever via archived keys.

REVOCATION CASCADE
  Compromised master    → all derived keys revoked + reissued;
                          emergency deployment update
  Compromised domain    → all projects in domain notified;
                          each may opt to upgrade or fork
  Compromised env       → members notified; env may auto-archive
  Compromised project   → project frozen; members notified;
                          rekeying ceremony
  Compromised persona   → persona moved to DORMANT;
                          new key issued; SOUL re-signed
  
SIGNATURE PRESERVATION
  Historical signatures remain verifiable indefinitely.
  .well-known carries archived keys with rotation timestamps.
  Operator may pre-publish revocation queue.
```

### A.40 LLM transport fault policy — error taxonomy

<a id="appendix-a40"></a>

```text
Error taxonomy:
  rate_limit (429)         exponential backoff; honour Retry-After;
                            max 3 retries; record request_id
  overloaded (529)         same as rate_limit
  api (500)                same as rate_limit
  timeout (504)            same as rate_limit
  auth (401)               no retry; signed AUTH_FAILURE event
  permission (403)         no retry; signed PERMISSION_FAILURE event
  not_found (404)          no retry; signed NOT_FOUND event
  billing (402)            no retry; signed BILLING_ISSUE event
  too_large (413)          no retry; trigger context overflow pipeline
  invalid_request (400)    no retry; signed SCHEMA_VIOLATION event
  content_refusal          no retry; signed CONTENT_REFUSAL event;
                            feeds charter-drift detection
```

### A.41 Output schema violation reformat pipeline

<a id="appendix-a41"></a>

```text
Schema-invalid output → SCHEMA_VIOLATION event
                       → one reformat retry with mechanical prompt
                       → reformat counts as separate LLM_CALL against budget
                       → second failure: drop candidate;
                          apply malformed_output penalty
```

### A.42 Content policy refusal handling

<a id="appendix-a42"></a>

```text
Provider-side refusal (heuristic: length, pattern, provider flag)
  → CONTENT_REFUSAL event (signed; NOT retried)
  → Integrator decides:
      class demotion (e.g., CONVERGENT → MIXED)
      OR escalate to human
      OR mark task as content_refusal status
  → In v1.0: also feeds charter-drift detection AND project-charter-drift
    detection (the persona's charter AND the project's charter are both
    audit targets)
```

### A.43 Context window overflow pipeline

<a id="appendix-a43"></a>

```text
Compression cascade:
  1. drop COLD advisory blocks
  2. drop WARM advisory blocks
  3. summarise pre-N-2 history
  4. drop env-scoped tactics
  5. drop project_context advisory blocks
     drop env_context advisory blocks
  6. abort if identity blocks won't fit
  
Each step emits signed CONTEXT_COMPRESSED lineage event.

Note: identity blocks (Layer 1 + frozen Layer 2) NEVER dropped.
```

### A.44 OWASP LLM01 retrieval-admission filter scope

<a id="appendix-a44"></a>

```text
SCOPE:
  Lessons, Skills, Tools, Rubrics
  Episodic / semantic memories
  Co-signed summaries
  A2A inbound messages
  Inter-persona DirectMessage
  Project-scope memories
  ProjectProvenFact statements
  Conjecture statements
  Obligation descriptions
  Disagreement position summaries
  NotationConvention definitions
  External_link descriptions
  StructuredFeedback raw_data descriptions
  AmbientEvent payloads
  KnowledgeRef chunks

ACTION:
  On filter match: suppress, quarantine, emit INJECTION_DETECTED.
  Dedicated classifier (01_KERNEL.md §2 safety floor) with rotation.
```
