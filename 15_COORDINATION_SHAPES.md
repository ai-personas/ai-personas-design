---
title: PersonaOS v1.1 — Coordination Shapes (Environment-Scoped Self-Organizing Coordination)
status: Draft
---

# 15 — Coordination Shapes

> **Reader guide.** How do AI Personas in a shared workspace figure out how to coordinate with each other? Instead of hardcoding patterns like "design review" or "staged rollout," PersonaOS lets the workers themselves propose, test, and evolve their coordination through experience — using five generic building blocks. This document also covers cross-environment coordination and hierarchical nesting (company → org → team). **Prerequisites:** `05_ENVIRONMENT.md`, `00_VISION.md`. **Status:** v1.1 Draft — not yet normative.

## 0. Status & scope

**Status.** `Draft`; v1.1 target. This document will become normative when it reaches `Stable` status. Implements **ADR-0045** (self-organizing coordination). Coordination is **environment-scoped**: each environment defines how its members coordinate — internally, with external agents, and with peer environments. The five meta-mechanisms are the kernel-level building blocks; environments compose them into specific coordination patterns.

**In scope.** The five meta-mechanism building blocks, environment-scoped coordination shape declarations, the four coordination scopes (intra-env, env-to-external, env-to-env, and orchestration of the task-execution loop — §4a, ADR-0066), shape proposal within environments, cross-environment shape inheritance, seed-shape catalog, and safety-floor composition.

**Out of scope.** Cross-kernel coordination shape negotiation (v1.1 federation chapter). Implementation of the shape-validation engine (operator tooling).

## 0a. Key concepts for new readers

This document uses terms from the broader PersonaOS v1.0 specification. If you are reading this document first, these definitions will help.

| Term | What it means | Where defined |
|---|---|---|
| **Environment** | A persistent container where personas have ongoing presence, do work, and coordinate. Environments can nest hierarchically (company → org → team) or exist as peers (chip lab ↔ firmware lab). Each has a charter, members, history, and conventions. | `05_ENVIRONMENT.md §1` |
| **Persona** | An AI cognitive worker with a persistent identity, memory, skills, and relationships. Personas join environments, propose coordination shapes, and evolve their working patterns through experience. Each persona has cognitive modes (Reflector, Composer, Verifier, etc.) that influence how it works. | `02_PERSONA.md §1` |
| **Operator** | The human or organisation responsible for a PersonaOS deployment. Operators set safety policies, approve safety-critical coordination shapes, and manage the deployment. Not a persona — external to the environment. | `01_KERNEL.md §1` |
| **ExternalAgent** | Any entity outside the environment — a vendor, a regulatory body, a partner lab, an external API. Environments coordinate with ExternalAgents through the env-to-external scope. | `04_PROJECT.md §26a.1` |
| **Charter** | An environment's binding ruleset — what must happen, what must not happen, safety constraints. Parent charters cascade to child environments. | `05_ENVIRONMENT.md §2.1` |
| **KindRegistry** | An open, extensible registry of domain-specific types. Instead of hardcoding categories (like "firmware" or "schematic"), PersonaOS lets personas propose new types into the registry. When this document says a field is "KindRegistry-resolved," it means the field's value is looked up from this registry at runtime, not hardcoded. | `06_DOMAIN.md §7.5-§7.6` |
| **Safety floor** | Eight sources of safety constraints that the kernel enforces at all times: (1) universal harm prevention, (2) persona charter, (3) user boundaries, (4) operator policy, (5) domain safety extensions, (6) external-tool-required, (7) novelty-check, (8) environment charter. No coordination shape can bypass these. | `01_KERNEL.md §2` |
| **Lineage** | An immutable, append-only audit trail of every state change — who did what, when, why, signed cryptographically. All coordination shape events are recorded in lineage for auditability. | `01_KERNEL.md §3` |
| **Meta-mechanism** | One of five abstract coordination patterns provided by the kernel (EntityGroup, BatchOperation, StagedSequence, StreamPolicy, DerivedMetric). These are the building blocks; personas compose specific coordination shapes from them. | This document §3 |
| **Coordination shape** | A concrete, environment-specific coordination pattern composed from one or more meta-mechanisms. Example: "design-review-ceremony" is a StagedSequence shape with stages [draft → review → revision → approved]. Shapes are proposed by personas, validated by the cohort, and evolved through experience. | This document §4 |
| **Seed shape** | One of ~35 pre-existing coordination shapes migrated from v1.0.x specific primitives. These are available to all environments as proven, reusable building blocks — but not imposed. Personas may import, modify, or ignore them. | This document §7 |
| **Ambient event stream** | Each environment's ongoing feed of state changes, measurements, and notifications. Coordination shapes (especially StreamPolicy) read from and write to this stream. | `05_ENVIRONMENT.md §8` |
| **Admission gate** | A kernel checkpoint that validates an action against safety invariants before allowing it to proceed. The `coordination_propose` gate validates proposed shapes against the safety floor. | `01_KERNEL.md §13.7` |
| **Cohort** | The set of personas currently active in an environment. The cohort validates coordination shapes through adoption — cosigning proposals and testing shapes in practice. | `04_PROJECT.md §14.1` |

## 0b. Plain-Language Guide

*Here's how AI Personas organise themselves, explained without jargon.*

**What are coordination shapes?**

Imagine a team of AI Personas sharing a workspace. They need to figure out how to work together -- who handles what, how work gets handed off, how to avoid stepping on each other's toes. Instead of someone dictating those rules from above, the workers themselves propose, test, and evolve their own ways of coordinating. A "coordination shape" is one of those agreed-upon patterns -- for example, "every design goes through a three-stage review before it is approved."

**The five building blocks**

All coordination shapes are built from five generic building blocks:

1. **Groups** (EntityGroup) -- Organise things into sets. "All design blocks assigned to Alice" or "all sensors on the third floor." The group updates automatically when things change.
2. **Batch operations** (BatchOperation) -- Do the same thing to every item in a group at once. "Update firmware on all 40 devices."
3. **Staged sequences** (StagedSequence) -- Step-by-step processes with checkpoints. "Draft, then review, then revise, then approve -- and you need two reviewers to pass the review gate."
4. **Stream policies** (StreamPolicy) -- Manage high-volume information flows. "Summarise 57,000 sensor readings per day into 96 floor-level reports."
5. **Derived metrics** (DerivedMetric) -- Compute scores from raw data and trigger actions at thresholds. "Team health = trust + velocity; alert the lead when it drops below 0.4."

**The four coordination scopes**

Coordination happens at four levels: (1) *Within a room* -- how workers inside one environment coordinate with each other (reviews, handoffs, task assignment). (2) *With outsiders* -- how the environment coordinates with external parties like vendors or regulators. (3) *Between rooms* -- how two environments coordinate as peers (a chip lab and a firmware lab exchanging register maps), including parent-child relationships when environments nest (company sets rules, team operates within them). (4) *The work loop itself* -- how the room decides what kind of work a task is, how to run it, and when it counts as done (added by ADR-0066, so the run loop is something the workers shape, not a fixed machine).

**How coordination patterns emerge and evolve**

On day one, a new environment has no coordination shapes -- workers just communicate through tasks and events. Over time, someone notices friction ("we keep duplicating work") and proposes a shape. If at least one colleague agrees, the team tries it out. If it works, more people adopt it. If a shape stops being useful, someone proposes retiring it. Coordination grows from experience, not from a template imposed from above.

**Seed shapes: a starter library**

PersonaOS ships with about 35 pre-built coordination shapes drawn from real use. These are available to every environment but never forced on anyone. Workers can import one off the shelf, customise it, or build something new from the five building blocks.

**Cross-environment coordination: asking, not commanding**

When one environment needs to coordinate with another, it sends a request. The receiving environment's workers review it through their own decision-making process and can accept, counter-propose, or decline. Neither side can force the other. If both agree, a bilateral binding is created that both sides reference.

**Safety composition: the guardrails**

No coordination shape can bypass the system's safety checks. Every shape must declare its scope, every state change must be signed and recorded in the audit trail, and safety-critical shapes require the operator's co-signature. Parent environment safety rules cascade to all children and cannot be weakened. The kernel enforces these guardrails at both proposal time and execution time.

## 1. The architectural insight

v1.0.x treated coordination as global substrate primitives: `StagedRolloutEnvelope` lived in `04_PROJECT`, `EventAggregationPolicy` in `05_ENVIRONMENT`, `SupersessionCascade` in `08_KNOWLEDGE`. Each was defined once, applied everywhere identically.

But coordination is not global — it is **contextual**. A chip design lab coordinates differently from a construction project. A research programme coordinates differently from a companionship environment. The coordination patterns are shaped by:

- **Who is inside** (the personas, their roles, their cognitive modes)
- **What is being made** (digital artifacts, physical assets, knowledge, relationships)
- **Who is outside** (external agents, peer environments, operators)
- **What constraints apply** (safety hazards, regulatory requirements, principal topology)

The environment already holds all of these: membership, charter, conventions, observation surfaces, ambient events. Coordination shapes belong here — as part of the environment's self-description, not as global substrate types.

## 2. The coordination scopes

Every environment manages coordination across four scopes:

*Scope 1 (intra-environment) covers how personas inside coordinate with each other -- design reviews, handoff ceremonies, staged operations, obligation management, milestone gates. Scope 2 (env-to-external) covers how the environment coordinates with outside agents -- foundry submissions, calibration requests, inspection scheduling, vendor communication. Scope 3 (env-to-env) covers how this environment coordinates with peer environments -- chip lab and firmware lab, research and publishing, design and manufacturing -- including parent-child coordination when environments nest hierarchically (company to org to team, country to state to city), where parent rules cascade as constraints while child coordination remains autonomous. Scope 4 (orchestration), added by [ADR-0066](14_DECISIONS.md#adr-0066--self-organizing-orchestration-the-run-loop-is-an-emergent-coordination-shape-not-a-fixed-dispatcher), covers how the environment coordinates the **task-execution loop itself** — how work is classified, sequenced, evaluated, and accepted — so the run loop is emergent rather than a fixed kernel dispatcher. See [§4a](#4a-orchestration-scope--coordinating-the-task-execution-loop).*

**Technical detail:** See [A.1](#appendix-a1).

Each scope has different trust boundaries, different coordination patterns, and different safety constraints. The environment's charter declares which shapes apply at each scope.

## 3. The five meta-mechanisms

These are the kernel-level building blocks — abstract patterns that the kernel knows how to validate and enforce. Personas compose them into specific **coordination shapes** for their environment.

**The relationship:** A meta-mechanism is the abstract pattern (like "StagedSequence"). A coordination shape is a concrete instance applied to a specific environment (like "design-review-ceremony: a StagedSequence with stages [draft → review → revision → approved] and a ≥2 reviewer gate"). Think of meta-mechanisms as the grammar and coordination shapes as the sentences.

*For example: EntityGroup becomes "block-ownership" (assign design blocks to personas); BatchOperation becomes "firmware-flash-batch" (update 40 devices at once); StagedSequence becomes "tape-out-checklist" (DRC, LVS, ERC, timing, power, submit); StreamPolicy becomes "telemetry-aggregation" (summarise 57K sensor readings/day); DerivedMetric becomes "team-health-score" (compute cohesion from trust + velocity).*

**Technical detail:** See [A.2](#appendix-a2).

Why exactly five? These five are sufficient to compose every coordination pattern found across 12 validation scenarios (~35 primitives). Risk R-CS-5 (§10) acknowledges the theoretical possibility that a future scenario might require expanding this set — but expansion adds one architectural mechanism, not one primitive per scenario.

### 3.1 EntityGroup — group entities by predicate

Selects a set of entities within the environment by a declarative predicate. The grouped set has identity, membership that recomputes on state change, and optional derived state.

*The EntityGroupShape declares a shape ID, name, scope, entity kind (resolved from the KindRegistry), a predicate schema for filtering, optional derived-state metrics, events that trigger membership recomputation, and flags for nesting and multi-membership.*

**Technical detail:** See [A.3](#appendix-a3).

### 3.2 BatchOperation — apply operation to a group

Applies a signed operation to every member of an `EntityGroup` with per-member outcome tracking.

*The BatchOperationShape declares a target group, an operation kind (KindRegistry-resolved), an operation schema, a per-member outcome model, a conflict policy (skip changed, fail on conflict, or force), and flags for rollback support and co-sign requirements.*

**Technical detail:** See [A.4](#appendix-a4).

### 3.3 StagedSequence — sequence operations with gates

Declares an ordered sequence of stages with gate predicates, dwell periods, rollback triggers, and per-stage lineage events.

*The StagedSequenceShape declares an ordered list of stages, terminal stages, an initial stage, and flags for parallel stages, rollback, operator co-sign, and safety-critical gating. Each StageDefinition names a stage, its gate predicate (KindRegistry-resolved), minimum dwell time, optional rollback trigger, lineage events on entry and exit, and an optional batch operation to execute at that stage.*

**Technical detail:** See [A.5](#appendix-a5).

### 3.4 StreamPolicy — aggregate or propagate events

Declares rules for aggregating high-volume events (fan-in) or propagating state changes through dependency graphs (cascade).

*The StreamPolicyShape supports three modes. Aggregation compresses many events into summaries (e.g., 57K sensor readings/day into 96 floor-level summaries) using time windows, grouping keys, and summary functions. Cascade propagates a change through a dependency graph (e.g., a retracted paper degrades all claims that cited it) with configurable depth limits and rate limiting. Propagation fans out an event to peer environments (e.g., broadcasting a capability update to partner labs) with topology and TTL settings. All modes share source event kinds and produce an output event kind with lineage linking.*

**Technical detail:** See [A.6](#appendix-a6).

### 3.5 DerivedMetric — compute metrics from constituent state

Declares a metric computed from entity state or event streams, with threshold-gated operations.

*The DerivedMetricShape draws from multiple input sources (entity fields, event counts, aggregate fields, group-derived state), applies a formula (ratio, linear combination, logarithmic, Bayesian update, count, exponential moving average, or custom), and produces an output value within a declared range. Gate thresholds trigger KindRegistry-resolved actions when the metric crosses a boundary (e.g., "alert the lead when team health drops below 0.4"). Operator-tunable parameters allow runtime adjustment without modifying the shape definition. Each MetricInputSource declares its source kind, reference, and weight; each MetricGate declares a comparison, threshold, and pass/fail actions.*

**Technical detail:** See [A.7](#appendix-a7).

## 4. Persona-driven coordination within environments

Coordination is **not pre-defined by the substrate, the operator, or a blueprint**. Personas placed into an environment establish their own coordination strategy, and that strategy evolves through experience. The substrate provides the five meta-mechanisms as building blocks; the personas compose, test, refine, and retire coordination shapes as they discover what their work requires.

### 4.1 Who establishes coordination

Coordination emerges from the personas in the environment — the same way domain knowledge emerges from persona ingestion, not from substrate constants.

**The coordination lifecycle:**

*On day one, personas join with minimal coordination -- just membership, the ambient event stream, observation surfaces, and basic lineage. By week two, someone notices friction (e.g., duplicated work on the same design block) and proposes an EntityGroup shape to assign ownership; one cosigner puts it into trial. By month one, a second shape emerges -- a StagedSequence for design review with draft, review, revision, and approved stages and a two-reviewer gate -- adopted from experience, not a template. By month three, a persona notices the two-reviewer gate is too slow for non-critical blocks and proposes a modification (v2) with evidence; the cohort adopts it and v1 retires. By month six, a shape that was useful early on (daily-sync-standup) is retired because async coordination now suffices. The environment's coordination profile grows and shrinks organically.*

**Technical detail:** See [A.8](#appendix-a8).

### 4.2 Any persona proposes; the cohort validates

**Proposal authority.** ANY persona in the environment may propose a coordination shape. The lead has no special proposal privilege — coordination ideas come from whoever notices the need. A junior contributor who sees a handoff gap has the same proposal authority as the lead.

**Validation authority.** The cohort validates through adoption:

| Stage | Criteria | What it means |
|---|---|---|
| `candidate` | 1 persona proposes; schema-valid; safety-floor check passes | "This shape exists; try it if you want." |
| `trial` | ≥1 cosigning persona; used in ≥1 task successfully | "This shape is being tested by part of the team." |
| `accepted` | ≥2 cosigning personas (or majority of env members, whichever is smaller); used in ≥3 tasks | "This shape is how we coordinate here." |
| `retired` | Proposer or lead proposes retirement; no active dependencies; cohort majority agrees | "We no longer need this shape." |

**Operator gate.** Safety-critical shapes (in environments with `safety_critical = True`) require operator co-sign before advancing past `candidate`. The operator does not design the shape — the personas do — but the operator validates that it respects safety invariants.

**Evolution.** A shape can be versioned. A persona proposes `design-review-ceremony-v2` with modified gates. If the cohort adopts v2, v1 transitions to `retired`. The lineage records both versions. Old tasks that used v1 retain their lineage; new tasks use v2.

### 4.3 Coordination signals — how personas know what to propose

Personas don't propose coordination shapes randomly. They respond to **coordination signals** — observable friction in the environment:

*Duplicate work leads to EntityGroup (assign ownership). Handoff failures lead to StagedSequence (ceremony with gates). Stalled external tasks lead to StagedSequence (env-to-external with tracking and escalation). Information overload leads to StreamPolicy (aggregate events). Inconsistent quality leads to StagedSequence (review ceremony). Declining team health leads to DerivedMetric (cohesion scoring with threshold alerts). Cross-env friction leads to StagedSequence (env-to-env with interface alignment). Budget uncertainty leads to DerivedMetric (utilisation tracking).*

**Technical detail:** See [A.9](#appendix-a9).

The Reflector cognitive mode (`02_PERSONA §4`) is the natural source of these observations — a Reflector persona periodically assesses "is our coordination working?" and proposes adjustments. But any mode can notice friction and propose.

### 4.4 The EnvironmentCoordinationProfile

The profile is the **living record** of an environment's current coordination shapes. It starts empty (or near-empty) and grows as personas propose and adopt shapes.

*The EnvironmentCoordinationProfile holds four lists of active shapes (one per scope: intra-env, env-to-external, env-to-env, and — per §4a / ADR-0066 — orchestration of the task-execution loop), a complete history of all shapes ever proposed, adopted, or retired, a version counter, and a signature. Each CoordinationShapeBinding records a shape's ID, version, meta-mechanism type, definition, lifecycle stage (candidate, trial, accepted, retired), proposer, cosigning personas, adoption/retirement timestamps, and operator co-sign status. Each CoordinationShapeEvent records what happened (proposed, cosigned, trial started, accepted, modified, retired, operator cosigned, or refused), which shape, which persona, when, why, and the signature.*

**Technical detail:** See [A.10](#appendix-a10).

### 4.5 Seed shapes: available, not imposed

MetaShapes (the ~35 v1.0.x primitives) are **available** to every environment but **not automatically active**. They sit in a library that personas can draw from when they recognise a coordination need.

*The shape availability hierarchy has three tiers: MetaShapes (~35 seed shapes) are available to all environments but not active by default; domain-promoted shapes are available to environments in that domain but not active by default; and the environment's active profile contains only shapes that personas have explicitly adopted.*

**Technical detail:** See [A.11](#appendix-a11).

When a persona notices "we need staged rollout for our firmware deployment," the persona can:
1. **Import** `staged-rollout-v1` from the MetaShape library (adapting parameters to this env).
2. **Compose** a custom shape from the meta-mechanisms.
3. **Modify** an imported shape for local needs.

The persona chooses; the substrate doesn't impose.

### 4.6 Example: chip design lab — coordination emerges over time

*This extended example traces a chip design lab through 12 months: month 0, five personas join with an empty profile and communicate via tasks. Month 1, Logic and Analog discover duplicated RTL work and propose an EntityGroup ("block-ownership"); Verify proposes a StagedSequence ("simulation-review-gate"). Month 3, Arch composes a custom StagedSequence for foundry submission with external attestation gates. Month 4, cross-env coordination with firmware_lab begins via a register-map-handoff shape. Month 6, the simulation review gate evolves to v2 (differentiated reviewer counts based on evidence). Month 9, the block-ownership shape is retired because work partitioned naturally by discipline. Month 12, the foundry-submission shape is promoted to the domain library for other chip labs to import -- but never forced. The example also shows env-to-env shapes: a firmware-handoff StagedSequence and a test-vector-exchange StreamPolicy.*

**Technical detail:** See [A.12](#appendix-a12).

This chip lab environment **defines its own coordination** — the substrate doesn't hardcode "tape-out-checklist" or "foundry-submission-sequence." Another environment (say, a pharmaceutical lab) would define completely different shapes using the same five meta-mechanisms.

### 4.7 Cross-environment coordination: bilateral peers

Environments are **peers**. Any environment can both **request** coordination with another environment AND **receive** coordination requests from other environments. There is no client-server hierarchy — the chip lab can request the firmware lab's help AND the firmware lab can request the chip lab's help, independently, through the same consent protocol.

When an environment receives a coordination request, its personas review the request through their own organisational structure — however that environment is organised — and accept, counter-propose, or deny. One environment cannot impose coordination on another, regardless of which side initiated.

**The cross-env coordination consent protocol:**

*The requesting environment drafts a CrossEnvCoordinationRequest specifying the proposed shape, interface (what artifacts are handed off, what stages are expected from the receiver, and what completion signal is expected). The request arrives in the receiving environment's ambient event stream. The receiving environment's personas review it per their own organisational structure (lead-decides, cohort-votes, or specialist-delegates). The receiver responds with one of three outcomes: Accept (with their own intake shape and commitment), Counter-propose (with modified interface, stages, or scope), or Deny (with a reason such as capacity unavailable, scope mismatch, charter conflict, or operator refusal).*

**Technical detail:** See [A.13](#appendix-a13).

**Schema:**

*The CrossEnvCoordinationRequest identifies the requesting and target environments, the requesting persona, the proposed shape name and definition, a CrossEnvInterface (handoff artifact kinds, expected stages from the receiver, expected completion signal, and data scope), a rationale, an urgency level, and a signature. The CrossEnvCoordinationResponse references the request, identifies the responder, and carries the decision (accept, counter-propose, or deny) along with the relevant payload for each outcome: intake shape and commitment timeline on accept, counter-proposed interface and rationale on counter-propose, denial reason and rationale on deny. It also records the decision process used (lead decided, cohort voted, specialist delegated, or operator decided) and the list of cosigning personas.*

**Technical detail:** See [A.14](#appendix-a14).

**Principles:**

1. **No forced coordination.** The requesting env cannot skip the consent protocol. Even if both envs share the same operator, the receiving env's personas must review and respond. The operator MAY override a denial only via operator policy (floor source 4) — and this override is a signed lineage event, not silent.

2. **The receiving env decides HOW to decide.** Whether the response comes from the lead, a cohort vote, a specialist, or the operator depends on the receiving env's own coordination structure. The substrate does not prescribe the decision process — it only requires that the response is signed by a member with authority.

3. **Counter-proposals iterate.** If the receiving env counter-proposes, the requesting env can accept the counter-proposal, counter again, or withdraw. The negotiation is a conversation between the two envs' personas, not a substrate protocol with fixed rounds. Convergence happens when both sides accept; divergence is honest (both sides know they disagree).

4. **Accepted coordination binds both sides.** On accept, a `CrossEnvCoordinationBinding` is created — a bilateral shape that both envs' profiles reference. Either env can propose modification or retirement of the binding, but unilateral withdrawal emits `CROSS_ENV_COORDINATION_WITHDRAWN` and requires a reason.

5. **Denial is final for that request.** A denied request cannot be re-submitted without material change. The requesting env must modify the proposed interface, rationale, or scope before re-proposing. Repeated identical submissions are rate-limited (max 1 per 30-day window).

6. **The interface MAY carry a task, not just artifacts.** A `CrossEnvInterface` extends beyond artifact handoff to optionally delegate a **task** to the receiving env's personas: it MAY specify `permitted_task_classes`, `permitted_acceptance_pathways`, and the resolved sub-task being delegated. This is how a task handled in one env hands a sub-task to a different set of personas in another env (or on another node) — the `CrossEnvTaskDelegation` composition specified in [`03_TASKS.md §4.5`](03_TASKS.md#45-cross-env--cross-node-task-delegation--placement). It is still bilateral and access-gated: the receiver reviews and consents exactly as for any other interface, and the delegator must hold the requisite capability (`09_PROTOCOLS §3F` UCAN token) — these envs MAY be on different nodes, identified by global handle (`01_KERNEL §4.4`).

*The CrossEnvCoordinationBinding records the binding ID, the two environment IDs, each side's agreed shape (as a CoordinationShapeBinding), the agreed CrossEnvInterface, and the binding state (active, paused, completed, or withdrawn), with establishment timestamp and dual signatures.*

**Technical detail:** See [A.15](#appendix-a15).

**Example continued from §4.6:**

*This extended example traces the negotiation in detail. In month 4, Arch requests firmware_lab's help with a register-map handoff; firmware_lab's specialist (HAL_Dev) counter-proposes a broader scope (adding interrupt map and DMA channels, delivering a full BSP instead of just a HAL). Arch accepts the counter-proposal, and a CrossEnvCoordinationBinding is created with both sides' agreed shapes. In month 5, the flow reverses: firmware_lab requests pin-mux data from chip_design_lab, which accepts with a 10-day commitment. Now the two environments have two active bilateral bindings, each initiated by a different side. By month 7, test_lab joins the network with three more bindings, forming a graph of bilateral coordination -- not a hierarchy with a root. No environment owns the coordination; each pair self-organises through the consent protocol.*

**Technical detail:** See [A.16](#appendix-a16).

### 4.8 Environment composition: environments within environments

Environments compose hierarchically. A parent environment can contain child environments, each with its own personas, coordination, and rules — but operating **within the constraints the parent defines**. This mirrors how jurisdictions, organisations, and teams nest in the real world.

*For example, AcmeCorp (company-level) has a charter requiring security review on all deployments. Its Engineering Org inherits that charter and adds "80% test coverage required." Within Engineering, the Backend Team inherits both levels and adds "2 reviewers per PR"; the Frontend Team adds "design review before implementation"; the Infra Team adds "change window Tue-Thu only." Each team's coordination is self-organised by its own personas. Similarly, jurisdictions nest: a country environment sets federal rules (tax law, export controls), state environments inherit and add state-specific rules, and county/city environments inherit all parent rules and add local requirements. Each child can add stricter rules but cannot weaken inherited safety constraints.*

**Technical detail:** See [A.17](#appendix-a17).

#### 4.8.1 Composition schema

*The EnvironmentComposition links a parent and child environment with three configurable dimensions. Rule cascade controls which parent charter rules the child inherits (all, specified, or none). Autonomy bounds determine whether the child can add stricter rules (default: yes), relax parent rules (default: no), or relax non-safety parent rules with parent consent (default: yes). Membership visibility controls whether parent personas are visible to the child, child personas to the parent, and whether cross-level membership is allowed. The composition is established with dual signatures.*

**Technical detail:** See [A.18](#appendix-a18).

#### 4.8.2 Rule cascade — parent constrains, child specialises

The parent environment's charter rules **cascade** to all children. Children can **add** rules (stricter) but cannot **remove or weaken** safety-critical parent rules.

*For example, if the parent requires "security review for all deployments," a child can add "2 reviewers per PR" (stricter -- allowed) or "deploy window Tue-Thu only" (additional -- allowed), but cannot remove the security review (refused -- safety rule) or make it optional for hotfixes (refused -- weakening parent constraint). For non-safety rules like "standups every morning at 9am," the child may remove or modify them with parent consent.*

**Technical detail:** See [A.19](#appendix-a19).

**Safety-critical cascade is non-negotiable.** If the parent env has `safety_critical = True` or a charter rule tagged as `safety_floor_source` (sources 1-8), children inherit that rule and cannot relax it. This ensures that a company's security policy, a country's export controls, or a lab's biosafety requirements apply at every level — the backend team can't opt out of security reviews.

#### 4.8.3 Coordination at each level

Each environment in the hierarchy has its own coordination profile — its own shapes, proposed and adopted by its own personas. Parent coordination does NOT dictate child coordination.

*At the company level, CTO/CISO/VP_Eng coordinate company-wide policies, cross-org resource allocation, and audit cadence. At the engineering org level, VP_Eng and directors coordinate cross-team architecture decisions, shared infrastructure, and release trains. At the backend team level, the lead and developers coordinate sprint planning, code review ceremonies, deploy sequences, and on-call rotation.*

**Technical detail:** See [A.20](#appendix-a20).

Each level's personas self-organise their coordination using the 5 meta-mechanisms. The backend team doesn't need company-level personas to tell them how to do code reviews — they propose and adopt their own `StagedSequence: code-review-ceremony` shape.

#### 4.8.4 Cross-level coordination

When a parent env needs to coordinate with a child env (or vice versa), the same **bilateral peer consent protocol** (§4.7) applies — with one addition: the parent's cascaded rules are pre-accepted constraints, not negotiable terms.

*For example, VP_Eng (eng org) requests the Backend Team to implement a new auth service by Q3. The Backend Team reviews per their own structure and counter-proposes: they can deliver by Q3 but need the Infra Team to provision a new database cluster first. The eng org now has two coordination bindings (one to each team), and the backend-to-infra dependency is a peer binding (per section 4.7), not a parent-child mandate.*

**Technical detail:** See [A.21](#appendix-a21).

**Parent authority vs child autonomy.** The parent can set **what** must be achieved (company policy, org-level goals) but NOT **how** the child coordinates internally to achieve it. The parent's charter cascades as constraints; the child's coordination shapes are self-organised.

*For example, the parent says "security review required before deployment" (charter rule -- cascades, non-negotiable). The parent does not say "use a 3-stage review ceremony with reviewer rotation and 48-hour soak period" (that is a coordination shape -- the child decides). The backend team proposes their own security-review StagedSequence with stages self-review, peer-review, and deploy, gated by a CISO-approved checklist. The parent's rule is satisfied; the child's coordination is self-organised.*

**Technical detail:** See [A.22](#appendix-a22).

#### 4.8.5 Environment spawning within a parent

When personas in a parent environment decide they need a child environment, they use the existing `EnvFormationProposal` (05_ENV §12c) with an additional `parent_env_id` field. The parent's personas must consent to the child's formation (standard consent protocol). The child inherits the parent's charter rules per cascade mode.

*The ChildEnvFormationProposal declares the parent environment, the proposed child's type and name, the cascade mode (inherit all, inherit specified, or inherit none), the initial member proposals, which parent personas consented and through what process (lead decided, cohort voted, or operator decided), and the proposer's identity and signature.*

**Technical detail:** See [A.23](#appendix-a23).

The child environment starts with an EMPTY coordination profile (per §4.1) — its personas self-organise from there, within the parent's cascaded constraints.

## 4a. Orchestration scope — coordinating the task-execution loop

*This section is normative. It establishes the fourth coordination scope (§2): coordination of the run loop itself, per [ADR-0066](14_DECISIONS.md#adr-0066--self-organizing-orchestration-the-run-loop-is-an-emergent-coordination-shape-not-a-fixed-dispatcher). The full reframe of task classes and acceptance pathways lives in [`03_TASKS.md §2a`](03_TASKS.md#2a-orchestration-is-emergent--classes-pathways-and-the-run-loop-are-coordination-shapes); this section states how it composes from the five meta-mechanisms.*

**The insight.** "Orchestration" — classify → route → execute → evaluate → accept — is just coordination of the task-execution loop. It therefore needs no separate model: it is a coordination shape like any other, declared in the [`EnvironmentCoordinationProfile`](#44-the-environmentcoordinationprofile) (§4.4) and proposed via [`ProposedCoordinationShape`](#5-proposedcoordinationshape) (§5). v1.0.x froze this scope in the kernel; ADR-0066 unfreezes it.

**Composition.** An orchestration shape composes from the same five meta-mechanisms (§3):
- a **`StagedSequence`** (§3.3) expresses the run loop's phases and gates — e.g. the INVESTIGATIVE `exploration → verification → synthesis → expert_review` arc ([`03_TASKS §2.3`](03_TASKS.md#23-investigative-sub-modes)) is a STANDARDISED seed `StagedSequence`, not a kernel constant;
- a **`DerivedMetric`** (§3.5) expresses an acceptance gate (a verdict computed from constituent evidence — the generalisation of progress scores, panel quorum, engagement signals);
- **`StreamPolicy`** / **`EntityGroup`** / **`BatchOperation`** express round aggregation, judge-panel grouping, and batch evaluation.

A `TaskClass` and an `AcceptancePathway` are emergent KindRegistry kinds (per `03_TASKS §2a`); an orchestration shape binds a class to a pathway-composition over these mechanisms.

**Fully open, with the meta-mechanism set itself extensible.** Personas MAY propose orchestration shapes that compose the five mechanisms, AND MAY propose a **new acceptance primitive** (a new meta-mechanism) when none of the five fits — promoted through the same lifecycle, with safety-critical primitives gated by C2. This extends ADR-0045 (which fixed the five) per the fully-open-orchestration decision in ADR-0066.

**Safety composition (unchanged floor).** Orchestration shapes are validated exactly as other shapes (§8): the kernel verifies INV-7 budget admission, signed lineage on every transition (J2/J9), and most-restrictive-wins floor clearance (J3) on every action. What is NOT pre-restricted is the *acceptance method*; instead, a verdict from an emergent/unvalidated orchestration shape is **trust-calibrated** (J4/J5) — it enters at EMERGENT trust and degrades honestly until validated, and the AnswerPackage records the producing shape and its promotion stage. Operator policy (floor source 4) MAY pin a minimum-trust or seed pathway for safety-critical task families.

**Promotion ladder and policy profile.** An emergent acceptance shape accrues and loses trust on an asymmetric-EWMA curve and auto-promotes EMERGENT → RECOGNISED only against an independent acceptance-soundness reference; operators MAY select the `bounded_compositional` policy profile (compose only from STANDARDISED seed primitives) where they want a hard a-priori floor on acceptance methods, with `fully_open` the substrate default. The full ladder, thresholds, and profile definition are normative in [`03_TASKS.md §2b`](03_TASKS.md#2b-orchestration-kind-promotion--trust-decay-curve-evidence-threshold-and-the-bounded-compositional-policy-profile).

**Tests:** A-EO1–A-EO13 ([`11_ACCEPTANCE_TESTS.md §9o`](11_ACCEPTANCE_TESTS.md)).

## 5. ProposedCoordinationShape

Personas propose new coordination shapes **within their environment**. Any member may propose; the cohort validates through adoption.

*The ProposedCoordinationShape identifies the environment, proposer, and timestamp; names the shape, declares its scope and meta-mechanism type, and carries the full shape definition. It may reference composed shapes (up to depth 3), evidence, and a rationale. Two parallel tracks govern its progress: the lifecycle stage (candidate, trial, accepted, promoted) tracks cohort adoption with cosigning personas and optional operator co-sign; the validation status (pending, schema valid, safety checked, admitted, refused) tracks kernel admission checks. A shape must reach "admitted" before advancing to trial.*

**Technical detail:** See [A.24](#appendix-a24).

**Promotion path.** A shape that proves useful outgrows its environment:
1. **Env-local accepted** — used successfully within this env; available to all current members.
2. **Domain-promoted** — used in ≥3 environments within the same domain; ≥5 cosigning personas across envs. Available for import by any env in this domain. Personas in other envs can discover and adopt it — they are NOT forced to.
3. **MetaShape-promoted** — used across ≥2 domains; ≥10 projects; federation consensus ≥0.8. Available for import by any env, any domain. The ~35 v1.0.x seed shapes start here.

## 6. Shape library — available, not imposed

Shapes accumulate in a three-tier library. Each tier makes shapes **discoverable** — personas browse the library when they recognise a coordination need. No tier imposes shapes on any environment.

*The library has three tiers: MetaShapes (~35 seed shapes from v1.0.x) are browsable and importable by any persona in any environment -- the "common vocabulary" proven across domains. Domain-promoted shapes are browsable and importable by personas in environments within that domain -- "what teams in this field found useful." Env-local shapes from other environments in the same deployment are discoverable if visibility permits, importable with proposer consent. An environment instance starts with an empty active coordination profile and grows as personas propose and adopt shapes; they may import from the library or compose their own. No tier forces activation.*

**Technical detail:** See [A.25](#appendix-a25).

**Blueprints as suggestions, not mandates.** An `EnvironmentBlueprint` (05_ENV §2.2) MAY include a list of **suggested** coordination shapes. These are recommendations from the blueprint author (often the operator), not activation mandates. When personas form an environment from a blueprint, they see the suggestions and decide which to adopt. The only exception: **safety-critical shapes mandated by operator policy** (floor source 4) — these activate automatically and cannot be retired without operator co-sign.

## 7. Seed shapes catalog

v1.1 launches with ~35 `MetaShape`-promoted shapes — the specific primitives from v1.0.x. These are available to all environments as universally reusable building blocks.

| Seed shape | v1.0.x primitive | Meta-mechanisms | Typical scope |
|---|---|---|---|
| `asset-group-v1` | AssetGroupEnvelope | EntityGroup | intra_env |
| `batch-advancement-v1` | BatchStateAdvancement | BatchOperation | intra_env |
| `staged-rollout-v1` | StagedRolloutEnvelope | StagedSequence + BatchOperation | intra_env / env_to_external |
| `event-aggregation-v1` | EventAggregationPolicy | StreamPolicy | intra_env |
| `supersession-cascade-v1` | SupersessionCascade | StreamPolicy | intra_env |
| `corpus-drift-v1` | CorpusDriftMetric | StreamPolicy + DerivedMetric | intra_env |
| `lead-handoff-v1` | LeadHandoffCeremony | StagedSequence | intra_env |
| `obligation-reassignment-v1` | ObligationReassignment | BatchOperation | intra_env |
| `planned-departure-v1` | PlannedDeparture | StagedSequence + DerivedMetric | intra_env |
| `cohort-dynamics-v1` | CohortDynamicsState | DerivedMetric | intra_env |
| `env-formation-v1` | EnvFormationProposal | StagedSequence | env_to_env |
| `multi-principal-quorum-v1` | MultiPrincipalAttestationQuorum | EntityGroup + DerivedMetric | intra_env |
| `peer-attestation-pool-v1` | PeerAttestationPool | EntityGroup | env_to_external |
| `replicated-attestation-v1` | ReplicatedAttestation | EntityGroup + DerivedMetric | env_to_external |
| `distress-routing-v1` | DistressDetectionRoutingPolicy | StreamPolicy | intra_env |
| `review-checkpoint-v1` | RelationshipReviewCheckpoint | StagedSequence + DerivedMetric | intra_env |
| `approval-workflow-v1` | ApprovalWorkflow | StagedSequence | intra_env / env_to_external |
| `gossip-propagation-v1` | GossipEvent | StreamPolicy | env_to_env |
| `relationship-federation-v1` | RelationshipFederationSync | StagedSequence + BatchOperation | env_to_env |

(Full catalog: ~35 shapes; abbreviated here for the draft.)

## 8. Safety composition model

All coordination shapes — regardless of how they are proposed or adopted — operate within a safety envelope. The kernel enforces these invariants at shape-proposal time (`coordination_propose` admission gate, `01_KERNEL §13.7`) and at shape-execution time. Self-organised coordination cannot violate trust boundaries, bypass audit, or exhaust resources.

**S-COORD-1.** Every coordination shape must declare its `scope` (intra_env / env_to_external / env_to_env). The kernel validates that the shape's operations respect the trust boundary of its scope:
- **intra_env**: all operations are within the environment's trust boundary; persona charter (floor source 2) + env charter (floor source 8) apply.
- **env_to_external**: operations cross the environment boundary to ExternalAgents; operator policy (floor source 4) applies; ExternalAttestation may be required per gate.
- **env_to_env**: operations cross between environments; both environments' charters must be respected; kernel validates shape compatibility at the interface.

**S-COORD-2.** Every state transition in a coordination shape must emit a signed lineage event into the environment's `EnvironmentLineage`. Silent state changes are refused at admission.

**S-COORD-3.** INV-7 budget admission applies to every operation within a shape. A shape that would exhaust the budget is refused at execution time.

**S-COORD-4.** Safety-critical shapes (those in environments with `safety_critical = True` or touching `physical_harm_class ≥ bodily_injury`) require operator co-sign before advancing past `candidate` stage.

**S-COORD-5.** Cross-environment coordination requires bilateral consent. A `CrossEnvCoordinationRequest` must be reviewed and accepted by the receiving environment's personas through their own decision process. The requesting environment cannot bypass this consent. Operator override of a denial is a signed lineage event (floor source 4), not a silent action.

**S-COORD-6.** Parent environment charter rules tagged as safety-critical cascade to all child environments and cannot be relaxed by the child. A child environment MAY add stricter rules but MUST NOT weaken inherited safety constraints. The kernel enforces cascade at child-env formation time and refuses charter amendments that would violate inherited safety rules.

## 9. Migration path

**v1.0.x → v1.1.** No breaking changes.

1. v1.0.x specific primitives remain valid; they become seed shapes in the MetaShape tier.
2. Each EnvironmentBlueprint gains a default `EnvironmentCoordinationProfile` populated from the seed shapes. The `project_workspace` blueprint includes `staged-rollout-v1`, `batch-advancement-v1`, `lead-handoff-v1`, `planned-departure-v1`, etc.
3. Personas that want new coordination patterns propose them within their environment via `ProposedCoordinationShape`.
4. Shapes that prove useful across environments promote through domain → MetaShape tiers.

## 10. Risks & known limitations

| ID | Risk | Severity | Mitigation |
|---|---|---|---|
| R-CS-1 | Shape validation is harder than kind validation | High | 4-pass validation; operator gate for safety-critical |
| R-CS-2 | Env-to-env shape compatibility checking is complex | High | Kernel validates stage-interface alignment at boundary; incompatibility emits clear signal |
| R-CS-3 | Environment coordination profiles may grow large | Medium | Blueprint defaults handle common cases; per-env customisation is incremental |
| R-CS-4 | Promotion path (env → domain → MetaShape) is long | Low | Seed shapes start at MetaShape; only novel shapes climb the ladder |
| R-CS-5 | The 5 meta-mechanisms may be incomplete | Medium | If a future scenario surfaces a coordination pattern that cannot be composed from the five, the mechanism set expands — but this is one architectural addition, not one primitive per scenario |

## 11. Open questions

| ID | Question | Status |
|---|---|---|
| OQ-CS-1 | Should blueprint coordination profiles be versioned independently from the blueprint itself? | Open |
| OQ-CS-2 | Can an environment override a safety-critical shape from its blueprint with a less-restrictive alternative? (Likely no — floor source 8.) | Open |
| OQ-CS-3 | How does env-to-env shape negotiation interact with A2A federation (09_PROTOCOLS)? | Open — v1.1 federation chapter |
| OQ-CS-4 | Should the `DerivedMetric` formula language support persona-authored sandboxed functions? | Open — security trade-off |

## Technical Appendix

The appendices below contain the full technical schemas, data structures, diagrams, and specification tables referenced throughout this document. Each appendix is referenced from the section where it applies.

### A.1 Four coordination scopes diagram

<a id="appendix-a1"></a>

```text
┌─────────────────────────────────────────────────────────┐
│                    ENVIRONMENT                          │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │  SCOPE 1: INTRA-ENVIRONMENT                      │   │
│  │  How personas inside coordinate with each other   │   │
│  │  (design reviews, handoff ceremonies, staged ops, │   │
│  │   obligation management, milestone gates)         │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │  SCOPE 2: ENV-TO-EXTERNAL                         │   │
│  │  How the env coordinates with ExternalAgents      │   │
│  │  (foundry submissions, calibration requests,      │   │
│  │   inspection scheduling, vendor communication)    │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │  SCOPE 3: ENV-TO-ENV                              │   │
│  │  How this env coordinates with peer envs          │   │
│  │  (chip lab ↔ firmware lab, research ↔ publishing,  │   │
│  │   design ↔ manufacturing, training ↔ deployment)  │   │
│  │  Includes PARENT ↔ CHILD coordination when envs   │   │
│  │  compose hierarchically (company → org → team,    │   │
│  │  country → state → city). Parent rules cascade    │   │
│  │  as constraints; child coordination is autonomous. │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │  SCOPE 4: ORCHESTRATION  (§4a, ADR-0066)          │   │
│  │  How the env coordinates the task-execution loop  │   │
│  │  itself — classify → route → execute → evaluate → │   │
│  │  accept. Task classes & acceptance pathways are    │   │
│  │  emergent kinds (v1.0 set seeded STANDARDISED);    │   │
│  │  the run loop is a StagedSequence personas evolve. │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### A.2 Meta-mechanism to coordination shape mapping

<a id="appendix-a2"></a>

```text
META-MECHANISM (abstract)        COORDINATION SHAPE (concrete, per-env)
─────────────────────────────    ──────────────────────────────────────
EntityGroup                   →  "block-ownership" (assign design blocks to personas)
BatchOperation                →  "firmware-flash-batch" (update 40 devices at once)
StagedSequence                →  "tape-out-checklist" (DRC → LVS → ERC → timing → power → submit)
StreamPolicy                  →  "telemetry-aggregation" (summarise 57K sensor readings/day)
DerivedMetric                 →  "team-health-score" (compute cohesion from trust + velocity)
```

### A.3 `EntityGroupShape` schema

<a id="appendix-a3"></a>

```python
@dataclass
class EntityGroupShape:
    schema: str = "entity-group-shape/1"
    shape_id: str
    name: str
    scope: Literal["intra_env", "env_to_external", "env_to_env"]

    entity_kind: str                          # KindRegistry-resolved
    predicate_schema: dict                    # JSON Schema for the
                                              # predicate expression
    derived_state_metrics: list[str] | None = None
    membership_recompute_on: list[str]        # event kinds that trigger
                                              # recomputation
    no_nesting: bool = True
    multi_membership: bool = True
```

### A.4 `BatchOperationShape` schema

<a id="appendix-a4"></a>

```python
@dataclass
class BatchOperationShape:
    schema: str = "batch-operation-shape/1"
    shape_id: str
    name: str
    scope: Literal["intra_env", "env_to_external", "env_to_env"]

    target_group_shape_id: str | None = None
    operation_kind: str                       # KindRegistry-resolved
    operation_schema: dict
    per_member_outcome_model: dict
    conflict_policy: Literal["skip_changed",
                              "fail_on_conflict",
                              "force"] = "skip_changed"
    rollback_supported: bool = True
    requires_cosign: bool = False
```

### A.5 `StagedSequenceShape` and `StageDefinition` schemas

<a id="appendix-a5"></a>

```python
@dataclass
class StagedSequenceShape:
    schema: str = "staged-sequence-shape/1"
    shape_id: str
    name: str
    scope: Literal["intra_env", "env_to_external", "env_to_env"]

    stages: list[StageDefinition]
    terminal_stages: list[str]
    initial_stage: str
    parallel_stages_allowed: bool = False
    rollback_to_prior: bool = True
    requires_operator_cosign_per_stage: bool = False
    safety_critical_gate: bool = False


@dataclass
class StageDefinition:
    schema: str = "stage-definition/1"
    stage_name: str
    gate_predicate_kind: str                  # KindRegistry-resolved
    min_dwell_seconds: int = 0
    rollback_trigger_kind: str | None = None
    lineage_event_on_enter: str
    lineage_event_on_exit: str
    batch_operation_shape_id: str | None = None
```

### A.6 `StreamPolicyShape` schema

<a id="appendix-a6"></a>

```python
@dataclass
class StreamPolicyShape:
    schema: str = "stream-policy-shape/1"
    shape_id: str
    name: str
    scope: Literal["intra_env", "env_to_external", "env_to_env"]

    # Three modes. Use ONLY the fields for your chosen mode.
    #
    # AGGREGATION: compress many events into summaries
    #   (e.g., 57K sensor readings/day → 96 floor-level summaries)
    #   Fields: source_event_kinds, window_duration_seconds,
    #           grouping_keys, summary_function_kinds
    #
    # CASCADE: propagate a change through a dependency graph
    #   (e.g., a retracted paper → degrade all claims that cited it)
    #   Fields: source_event_kinds, graph_edge_kind,
    #           cascade_operation_kind, max_depth,
    #           rate_limit_window_hours
    #
    # PROPAGATION: fan-out an event to peer environments
    #   (e.g., broadcast a capability update to partner labs)
    #   Fields: source_event_kinds, propagation_topology,
    #           ttl_seconds
    #
    policy_kind: Literal["aggregation",
                          "cascade",
                          "propagation"] = "aggregation"

    # SHARED (all modes)
    source_event_kinds: list[str]             # which events to process

    # AGGREGATION mode fields
    window_duration_seconds: int | None = None  # time window for grouping
    grouping_keys: list[str] | None = None    # group events by these
                                              # metadata fields
    summary_function_kinds: list[str] | None = None  # count, mean, max, etc.

    # CASCADE mode fields
    graph_edge_kind: str | None = None        # what edge type to traverse
    cascade_operation_kind: str | None = None  # what to do at each node
    max_depth: int = 3                        # prevent unbounded traversal
    rate_limit_window_hours: int = 24         # max 1 cascade per source
                                              # per window

    # PROPAGATION mode fields
    propagation_topology: Literal["flat",
                                   "graph",
                                   "peer_env"] | None = None
    ttl_seconds: int | None = None            # event expires after TTL

    # OUTPUT (all modes)
    output_event_kind: str                    # what event is produced
    lineage_linking: Literal["hash_linked",
                              "ref_linked"] = "hash_linked"
```

### A.7 `DerivedMetricShape`, `MetricInputSource`, and `MetricGate` schemas

<a id="appendix-a7"></a>

```python
@dataclass
class DerivedMetricShape:
    schema: str = "derived-metric-shape/1"
    shape_id: str
    name: str
    scope: Literal["intra_env", "env_to_external", "env_to_env"]

    input_sources: list[MetricInputSource]
    formula_kind: Literal["linear_combination", "ratio",
                           "logarithmic", "bayesian_update",
                           "count", "exponential_moving_average",
                           "custom_kind"] = "ratio"
    custom_formula_kind: str | None = None

    output_field: str
    output_range: tuple[float, float] = (0.0, 1.0)
    gate_thresholds: list[MetricGate] | None = None
    operator_tunable_params: list[str] | None = None
    recompute_on: list[str]
    recompute_cadence_seconds: int | None = None


@dataclass
class MetricInputSource:
    schema: str = "metric-input-source/1"
    source_kind: Literal["entity_field", "event_count",
                          "aggregate_event_field",
                          "group_derived_state"]
    source_ref: str
    weight: float = 1.0


@dataclass
class MetricGate:
    schema: str = "metric-gate/1"
    gate_name: str
    comparison: Literal["gte", "lte", "gt", "lt", "eq"]
    threshold: float
    action_on_pass: str                       # KindRegistry-resolved
    action_on_fail: str                       # KindRegistry-resolved
```

### A.8 Coordination lifecycle timeline

<a id="appendix-a8"></a>

```text
DAY 1: MINIMAL COORDINATION
  Personas join the environment. The substrate provides only:
    - Membership ceremonies (05_ENV §5.1)
    - Ambient event stream (05_ENV §8)
    - Observation surfaces (05_ENV §9)
    - Basic lineage (J2, J9)
  No coordination shapes are active. Personas communicate
  through tasks and ambient events.

WEEK 2: FIRST COORDINATION NEED
  A persona notices friction: "we keep duplicating work on
  the same design block." The persona (any member, not just
  the lead) proposes a coordination shape:
    EntityGroup: block-assignment-groups
    predicate: {assigned_to: <persona_id>}
  The cohort reviews. If ≥1 cosigning persona agrees, the
  shape enters TRIAL. The env tries it.

MONTH 1: COORDINATION MATURES
  The block-assignment shape works. The lead proposes a
  second shape:
    StagedSequence: design-review-ceremony
    stages: [draft → review → revision → approved]
    gate: ≥2 reviewer approvals
  The cohort adopts it. Coordination is accumulating from
  experience, not from a template.

MONTH 3: COORDINATION EVOLVES
  A persona notices the 2-reviewer gate is too slow for
  non-critical blocks. The persona proposes a MODIFICATION:
    design-review-ceremony (v2)
    gate: ≥1 reviewer for non-critical blocks;
          ≥2 reviewers for critical-path blocks
  The cohort reviews the evidence (completion times, error
  rates). If convinced, shape v2 replaces v1.

MONTH 6: COORDINATION RETIRES
  A shape that was useful early on (daily-sync-standup) is
  no longer needed — the team is mature, async coordination
  via ambient events suffices. A persona proposes RETIREMENT.
  The cohort agrees. Shape deactivated. The environment's
  coordination profile is leaner.
```

### A.9 Coordination signals table

<a id="appendix-a9"></a>

```text
SIGNAL                              COORDINATION RESPONSE
──────────────────────────────────  ─────────────────────────────────────
Duplicate work detected             → EntityGroup (assign ownership)
Handoff failures between personas   → StagedSequence (ceremony with gates)
Stalled tasks waiting on external   → StagedSequence (env-to-external with
                                      tracking + escalation)
Information overload (too many      → StreamPolicy (aggregate events before
  events in ambient stream)           notification)
Inconsistent quality across         → StagedSequence (review ceremony)
  deliverables
Team health declining               → DerivedMetric (cohesion scoring +
                                      threshold alerts)
Cross-env handoff friction          → StagedSequence (env-to-env with
                                      interface alignment)
Budget/resource uncertainty         → DerivedMetric (utilisation tracking)
```

### A.10 `EnvironmentCoordinationProfile`, `CoordinationShapeBinding`, and `CoordinationShapeEvent` schemas

<a id="appendix-a10"></a>

```python
@dataclass
class EnvironmentCoordinationProfile:
    schema: str = "env-coordination-profile/1"
    environment_id: str

    # Active shapes across the four scopes.
    # Starts EMPTY at env formation. Grows as personas propose.
    intra_env_shapes: list[CoordinationShapeBinding]
    env_to_external_shapes: list[CoordinationShapeBinding]
    env_to_env_shapes: list[CoordinationShapeBinding]
    # Scope 4 (orchestration of the task-execution loop; §4a, ADR-0066).
    # Additive field; the env-coordination-profile/1 version is retained.
    # Empty here means the env uses the STANDARDISED seed orchestration shape.
    orchestration_shapes: list[CoordinationShapeBinding]

    # HISTORY (lineage of all shapes ever proposed, adopted, retired)
    shape_history: list[CoordinationShapeEvent]

    version: int                              # increments on every
                                              # shape adoption/retirement
    last_updated_at: datetime
    signed_by: bytes


@dataclass
class CoordinationShapeBinding:
    schema: str = "coordination-shape-binding/1"
    shape_id: str
    shape_version: int = 1
    meta_mechanism: Literal["entity_group", "batch_operation",
                             "staged_sequence", "stream_policy",
                             "derived_metric"]
    shape_definition: dict
    stage: Literal["candidate", "trial",
                    "accepted", "retired"] = "candidate"
    proposed_by: str                          # persona_id who proposed
    cosigning_personas: list[str] = field(default_factory=list)
    adopted_at: datetime | None = None
    retired_at: datetime | None = None
    active: bool = True
    operator_cosigned: bool = False


@dataclass
class CoordinationShapeEvent:
    schema: str = "coordination-shape-event/1"
    event_kind: Literal["proposed", "cosigned", "trial_started",
                         "accepted", "modified", "retired",
                         "operator_cosigned", "refused"]
    shape_id: str
    persona_id: str
    timestamp: datetime
    rationale: str | None = None
    signed_by: bytes
```

### A.11 Shape availability hierarchy diagram

<a id="appendix-a11"></a>

```text
SHAPE AVAILABILITY vs ACTIVATION:

  MetaShapes (~35 seed shapes)     AVAILABLE to all envs
      ↓                            but NOT active by default
  Domain shapes                    AVAILABLE to envs in this domain
      ↓                            but NOT active by default
  ──────────────────────────────
  Environment's active profile     ACTIVE — only shapes personas
                                   have explicitly adopted
```

### A.12 Chip design lab example -- coordination emerges over time

<a id="appendix-a12"></a>

```text
MONTH 0: ENV FORMED
  5 personas join: Arch (lead), Logic (digital), Analog (analog),
  Verify (verification), Rev (review/falsifier).
  Coordination profile: EMPTY.
  Personas communicate via tasks + ambient events.

MONTH 1: FIRST SHAPES EMERGE
  Logic and Analog discover they're editing the same RTL file.
  Logic proposes:
    EntityGroup: "block-ownership"
      entity_kind: design_block
      predicate: {owner_persona_id: <assigned>}
  Analog cosigns. Shape → trial → accepted (after 3 successful
  uses with no conflicts).

  Verify proposes:
    StagedSequence: "simulation-review-gate"
      stages: [sim_drafted → sim_reviewed → sim_approved]
      gate: ≥1 reviewer (Rev) must sign per stage
  Arch + Rev cosign. Shape → accepted.

MONTH 3: EXTERNAL COORDINATION NEEDED
  The project needs foundry tape-out. Arch proposes:
    StagedSequence (env-to-external): "foundry-submission"
      stages: [gds_prepared → submitted → drc_at_foundry →
               mask_ordered → wafer_fab → test_chip_received]
      gate: ExternalAttestation from foundry per stage
      min_dwell: 14 days (wafer_fab)
  This is a new shape, not imported from MetaShapes — Arch
  composes it from the StagedSequence mechanism because no
  seed shape matches the specific foundry workflow. The cohort
  adopts it.

MONTH 4: CROSS-ENV COORDINATION
  The chip needs firmware. Arch discovers a firmware_lab env
  exists. Arch proposes:
    StagedSequence (env-to-env): "register-map-handoff"
      stages: [reg_map_drafted → reviewed_by_fw → hal_authored
               → integration_test_passed]
  The firmware_lab's lead proposes a compatible intake shape.
  Kernel validates interface compatibility. Both envs adopt.

MONTH 6: COORDINATION EVOLVES
  Rev notices simulation reviews are bottlenecking. Rev
  proposes modifying "simulation-review-gate" v2:
    gate: ≥1 reviewer for unit-level sims;
          ≥2 reviewers for top-level sims
  Evidence: unit-level sims had 0 post-review failures; top-level
  sims had 3. Cohort adopts v2; v1 retires.

MONTH 9: SHAPE RETIREMENT
  The "block-ownership" EntityGroup is no longer needed — the
  team naturally partitioned work by discipline (Logic handles
  all digital; Analog handles all analog). Logic proposes
  retirement. Cohort agrees. Shape → retired. Profile is leaner.

MONTH 12: COORDINATION HARVEST
  The "foundry-submission" shape has proven valuable across 2
  tape-out cycles. Arch proposes domain-promotion: other chip
  design envs in the same domain can import it. The domain
  curator reviews; shape promotes. Future chip labs can import
  "foundry-submission" from the domain library — but they're
  NOT forced to use it.
```

```text
  ENV-TO-ENV SHAPES:
    firmware-handoff                StagedSequence
      scope: chip_design_lab ↔ firmware_lab
      stages: [register_map_drafted → register_map_reviewed_by_fw
               → hal_authored_by_fw → integration_test_passed]
      gate: cross-env attestation per stage

    test-vector-exchange            StreamPolicy
      scope: chip_design_lab → test_lab
      policy: propagation
      source: simulation_pass_vectors
      target_env: test_lab
      format: aggregate simulation results per block
```

### A.13 Cross-environment coordination consent protocol flow

<a id="appendix-a13"></a>

```text
REQUESTING ENV (chip_design_lab)          RECEIVING ENV (firmware_lab)
                                          
1. Arch drafts CrossEnvCoordinationRequest    
   shape: "register-map-handoff"              
   proposed_interface: {                      
     handoff_artifact: "register_map",        
     expected_stages_from_receiver: [         
       "receive", "validate", "hal_author"    
     ],                                       
     expected_completion_signal: "hal_ready"   
   }                                          
   ──────────────────────────────────────→     
                                          2. Request arrives in firmware_lab's
                                             AmbientEventStream as a
                                             cross_env_coordination_request event.
                                              
                                          3. firmware_lab's personas review
                                             PER THEIR OWN STRUCTURE:
                                              
                                             If lead-decides env:
                                               FW_Lead reviews and decides.
                                             If cohort-votes env:
                                               All members vote; majority rules.
                                             If specialist-delegates env:
                                               FW_Lead assigns to the persona
                                               with relevant expertise (HAL_Dev).
                                              
                                          4. The receiving env responds with ONE OF:
                                              
   ←── ACCEPT ─────────────────────────────   "We accept. Our intake shape:
                                               stages: [receive, validate,
                                                        hal_author, integration]
                                               gate: our reviewer signs per stage.
                                               We commit to 'hal_ready' signal."
                                              
   ←── COUNTER-PROPOSE ───────────────────   "We accept the concept but need
                                               different interface:
                                               - We need 'memory_map' not just
                                                 'register_map' (broader scope).
                                               - Our stages are [receive, review,
                                                 hal_author, driver_author, test].
                                               - Completion signal: 'bsp_ready'
                                                 not 'hal_ready'."
                                              
   ←── DENY ──────────────────────────────   "We cannot coordinate on this now.
                                               reason: 'capacity_unavailable' /
                                                       'scope_mismatch' /
                                                       'charter_conflict' /
                                                       'operator_refused'"
```

### A.14 `CrossEnvCoordinationRequest`, `CrossEnvInterface`, and `CrossEnvCoordinationResponse` schemas

<a id="appendix-a14"></a>

```python
@dataclass
class CrossEnvCoordinationRequest:
    schema: str = "cross-env-coordination-request/1"
    request_id: str
    requesting_env_id: str
    requesting_persona_id: str                # who in the requesting
                                              # env initiated this
    target_env_id: str

    # PROPOSED SHAPE
    proposed_shape_name: str
    proposed_shape_definition: dict           # meta-mechanism composition
    proposed_interface: CrossEnvInterface

    rationale: str
    urgency: Literal["routine", "time_sensitive",
                      "blocking"] = "routine"

    requested_at: datetime
    signed_by: bytes                          # requesting persona signs


@dataclass
class CrossEnvInterface:
    schema: str = "cross-env-interface/1"
    handoff_artifact_kinds: list[str]         # KindRegistry-resolved;
                                              # what is being exchanged
    expected_stages_from_receiver: list[str]  # what the requester
                                              # expects the receiver
                                              # to do with the handoff
    expected_completion_signal: str           # event kind the requester
                                              # expects on completion
    data_scope: Literal["artifact_only",
                         "artifact_plus_metadata",
                         "full_project_context"] = "artifact_only"


@dataclass
class CrossEnvCoordinationResponse:
    schema: str = "cross-env-coordination-response/1"
    request_id: str                           # references the request
    responding_env_id: str
    responding_persona_id: str                # who in the receiving
                                              # env authored the response

    # DECISION
    decision: Literal["accept", "counter_propose", "deny"]

    # ON ACCEPT: the receiving env's intake shape
    intake_shape_definition: dict | None = None
    intake_interface: CrossEnvInterface | None = None
    commitment_timeline: str | None = None    # "we'll complete within
                                              # 30 days" — persona
                                              # commitment, not substrate
                                              # enforcement

    # ON COUNTER-PROPOSE: modified interface
    counter_proposed_interface: CrossEnvInterface | None = None
    counter_rationale: str | None = None

    # ON DENY
    denial_reason_kind: str | None = None     # KindRegistry-resolved
    denial_rationale: str | None = None

    # WHO DECIDED (transparency into the receiving env's process)
    decision_process: Literal["lead_decided",
                               "cohort_voted",
                               "specialist_delegated",
                               "operator_decided"] = "lead_decided"
    cosigning_personas: list[str] = field(default_factory=list)

    responded_at: datetime
    signed_by: bytes                          # responding persona signs
```

### A.15 `CrossEnvCoordinationBinding` schema

<a id="appendix-a15"></a>

```python
@dataclass
class CrossEnvCoordinationBinding:
    schema: str = "cross-env-coordination-binding/1"
    binding_id: str
    requesting_env_id: str
    receiving_env_id: str

    # THE AGREED SHAPES (one per side)
    requesting_side_shape: CoordinationShapeBinding
    receiving_side_shape: CoordinationShapeBinding

    # THE AGREED INTERFACE
    interface: CrossEnvInterface

    # STATE
    state: Literal["active", "paused",
                    "completed", "withdrawn"] = "active"
    established_at: datetime
    signed_by_requesting: bytes
    signed_by_receiving: bytes
```

### A.16 Cross-environment coordination -- detailed example and multi-env network

<a id="appendix-a16"></a>

```text
MONTH 4: CROSS-ENV COORDINATION (detailed)

  Arch (chip_design_lab) drafts CrossEnvCoordinationRequest:
    target: firmware_lab
    shape: "register-map-handoff"
    interface: {
      handoff_artifact: register_map,
      expected_stages: [receive, validate, hal_author],
      completion_signal: hal_ready
    }

  firmware_lab receives the request. Their structure:
    lead: FW_Lead
    specialist: HAL_Dev, Driver_Dev, BSP_Dev
    decision_process: specialist_delegated

  FW_Lead delegates review to HAL_Dev (the relevant specialist).

  HAL_Dev reviews and COUNTER-PROPOSES:
    "Register map alone isn't enough — we also need the
    interrupt map and DMA channel allocation to write the HAL.
    Our stages are [receive, review, hal_author, driver_stub,
    integration_test]. Completion signal: bsp_ready (not just
    hal_ready — we deliver the whole BSP)."

  Arch reviews the counter-proposal. Agrees — broader scope
  is actually better. ACCEPTS the counter-proposal.

  CrossEnvCoordinationBinding created:
    chip_design_lab side: register-map-handoff (v2, broadened)
    firmware_lab side: hardware-interface-intake
    interface: {
      handoff_artifacts: [register_map, interrupt_map, dma_channels],
      stages: [receive, review, hal_author, driver_stub, integration],
      completion_signal: bsp_ready
    }

  Both envs' coordination profiles now reference the binding.
  Lineage in both envs records the negotiation.

MONTH 5: REVERSE DIRECTION — firmware_lab REQUESTS from chip_design_lab

  HAL_Dev (firmware_lab) drafts CrossEnvCoordinationRequest:
    target: chip_design_lab
    shape: "pin-mux-table-request"
    interface: {
      handoff_artifact: pin_mux_configuration,
      expected_stages: [request_filed, pin_mux_drafted,
                        pin_mux_reviewed, delivered],
      completion_signal: pin_mux_delivered
    }
    rationale: "BSP needs final pin assignments before we can
                author the board-level device tree."

  chip_design_lab receives the request. Their structure:
    decision_process: lead_decided (Arch reviews)

  Arch reviews. ACCEPTS — pin mux is already in progress:
    intake_shape: "pin-mux-delivery"
    stages: [request_acknowledged, pin_mux_finalized,
             peer_reviewed, delivered]
    commitment: "10 business days"

  Second CrossEnvCoordinationBinding created — this time
  firmware_lab is the requester, chip_design_lab is the receiver.

  The two envs now have TWO active bindings:
    Binding 1: chip_lab → firmware_lab (register-map-handoff)
    Binding 2: firmware_lab → chip_lab (pin-mux-delivery)

  Each binding was initiated by a different side. Each went
  through the receiving env's own consent process. Neither
  env is subordinate — they are peers coordinating bilaterally.

MONTH 7: MULTI-ENV COORDINATION NETWORK

  The test_lab env also enters the picture:
    chip_design_lab → test_lab (test-vector-handoff)
    test_lab → chip_design_lab (silicon-measurement-feedback)
    firmware_lab → test_lab (bsp-validation-request)

  Each pair negotiates independently. The coordination network
  is a graph of bilateral bindings, not a tree with a root.
  No environment "owns" the coordination — each pair self-
  organises through the consent protocol.

  ┌────────────┐     binding 1,2     ┌──────────────┐
  │ chip_design │ ←──────────────→  │ firmware_lab  │
  │    _lab     │                    │               │
  └──────┬──┬──┘                    └───────┬───────┘
         │  │                               │
  bind 3 │  │ bind 4                 bind 5 │
         │  │                               │
         ▼  ▼                               ▼
      ┌──────────┐                          │
      │ test_lab │ ←────────────────────────┘
      └──────────┘
```

### A.17 Environment composition hierarchies -- company and jurisdiction examples

<a id="appendix-a17"></a>

```text
COMPANY ENVIRONMENT (AcmeCorp)
  charter: "all deployments require security review"
  personas: CTO, CISO, VP_Eng
  │
  ├── ENGINEERING ORG ENVIRONMENT
  │     charter: inherits AcmeCorp + "80% test coverage required"
  │     personas: VP_Eng, Dir_Backend, Dir_Frontend, Dir_Infra
  │     │
  │     ├── BACKEND TEAM ENVIRONMENT
  │     │     charter: inherits Eng_Org + "2 reviewers per PR"
  │     │     personas: Lead_BE, Dev_A, Dev_B, Dev_C, QA_1
  │     │     coordination: self-organised by this team's personas
  │     │
  │     ├── FRONTEND TEAM ENVIRONMENT
  │     │     charter: inherits Eng_Org + "design review before implementation"
  │     │     personas: Lead_FE, Dev_D, Dev_E, Designer_1
  │     │     coordination: self-organised by this team's personas
  │     │
  │     └── INFRA TEAM ENVIRONMENT
  │           charter: inherits Eng_Org + "change window Tue-Thu only"
  │           personas: Lead_Infra, SRE_1, SRE_2
  │           coordination: self-organised by this team's personas
  │
  └── PRODUCT ORG ENVIRONMENT
        charter: inherits AcmeCorp + "customer data access requires PII review"
        personas: VP_Product, PM_1, PM_2, Analyst_1
        coordination: self-organised by this org's personas
```

```text
COUNTRY ENVIRONMENT (federal rules)
  charter: "federal tax law applies; export controls enforced"
  │
  ├── STATE ENVIRONMENT (state rules)
  │     charter: inherits federal + "state income tax 5%"
  │     │
  │     ├── COUNTY ENVIRONMENT
  │     │     charter: inherits federal + state + "county permits required"
  │     │
  │     └── CITY ENVIRONMENT
  │           charter: inherits federal + state + "business license required"
  │
  └── STATE ENVIRONMENT (different state, different rules)
        charter: inherits federal + "no state income tax; sales tax 8%"
```

### A.18 `EnvironmentComposition` schema

<a id="appendix-a18"></a>

```python
@dataclass
class EnvironmentComposition:
    schema: str = "env-composition/1"
    parent_env_id: str
    child_env_id: str

    # RULE CASCADE
    cascade_mode: Literal["inherit_all",
                           "inherit_specified",
                           "inherit_none"] = "inherit_all"
    inherited_charter_rules: list[str] | None = None
                                              # if cascade_mode =
                                              # "inherit_specified";
                                              # None = all parent rules
                                              # when mode = "inherit_all"

    # AUTONOMY BOUNDS
    child_may_add_rules: bool = True          # child can add stricter
                                              # rules beyond parent's
    child_may_relax_rules: bool = False       # child CANNOT weaken
                                              # parent rules (default)
    child_may_relax_non_safety: bool = True   # child MAY relax non-
                                              # safety parent rules
                                              # with parent consent

    # MEMBERSHIP
    parent_personas_visible_to_child: bool = True
    child_personas_visible_to_parent: bool = True
    cross_level_membership: bool = False      # persona can be member
                                              # of BOTH parent and child

    established_at: datetime
    signed_by_parent: bytes
    signed_by_child: bytes
```

### A.19 Rule cascade examples

<a id="appendix-a19"></a>

```text
RULE CASCADE:

  Parent rule: "all deployments require security review"
    │
    ▼ CASCADES TO ALL CHILDREN
    │
    ├── Child adds: "2 reviewers per PR"           ✓ STRICTER — allowed
    ├── Child adds: "deploy window Tue-Thu only"   ✓ ADDITIONAL — allowed
    ├── Child removes: "security review"           ✗ REFUSED — safety rule
    └── Child relaxes: "security review optional   ✗ REFUSED — weakening
                        for hotfixes"                  parent constraint

NON-SAFETY RULES:

  Parent rule: "standups every morning at 9am"
    │
    ├── Child removes: "no standups for us"        ✓ ALLOWED (non-safety;
    │                                                  with parent consent)
    └── Child modifies: "standups at 10am"         ✓ ALLOWED (non-safety)
```

### A.20 Coordination at each hierarchy level

<a id="appendix-a20"></a>

```text
LEVEL           WHO COORDINATES                     WHAT THEY COORDINATE
─────────────   ──────────────────────────────────  ──────────────────────────
Company         CTO, CISO, VP_Eng                   company-wide policies,
                                                     cross-org resource
                                                     allocation, audit cadence

Eng Org         VP_Eng, Dir_Backend, Dir_Frontend    cross-team architecture
                                                     decisions, shared infra,
                                                     release trains

Backend Team    Lead_BE, Dev_A, Dev_B, Dev_C, QA    sprint planning, code
                                                     review ceremonies, deploy
                                                     sequences, on-call rotation
```

### A.21 Cross-level coordination example

<a id="appendix-a21"></a>

```text
CROSS-LEVEL COORDINATION:

  VP_Eng (eng_org) requests from Backend Team:
    "Implement the new auth service by Q3."

  Backend Team personas review PER THEIR OWN STRUCTURE:
    Lead_BE assigns to Dev_A + Dev_B.
    Team ACCEPTS with counter-proposal:
      "We can deliver auth service by Q3, but we need
       Infra Team to provision the new database cluster
       first — that's a dependency we can't resolve alone."

  eng_org now has TWO coordination bindings:
    eng_org → backend_team (auth service delivery)
    eng_org → infra_team (database cluster provisioning)

  The backend_team → infra_team dependency is a PEER binding
  (§4.7), not a parent-child mandate. Infra team reviews
  through their own process.
```

### A.22 Parent authority vs child autonomy example

<a id="appendix-a22"></a>

```text
PARENT SAYS:      "Security review required before deployment."
                   (charter rule — cascades, non-negotiable)

PARENT DOES NOT SAY: "Use a 3-stage review ceremony with
                      reviewer rotation and 48h soak period."
                      (coordination shape — child decides)

CHILD DECIDES:     The backend team proposes their own
                   security-review shape:
                     StagedSequence: "security-review"
                     stages: [self_review → peer_review → deploy]
                     gate: CISO-approved checklist per stage
                   The parent's rule is satisfied; the child's
                   coordination is self-organised.
```

### A.23 `ChildEnvFormationProposal` schema

<a id="appendix-a23"></a>

```python
@dataclass
class ChildEnvFormationProposal:
    schema: str = "child-env-formation-proposal/1"
    proposal_id: str
    parent_env_id: str                        # the parent environment
    proposed_child_type: str                  # env type for the child
    proposed_child_name: str

    # WHICH PARENT RULES CASCADE
    cascade_mode: Literal["inherit_all",
                           "inherit_specified",
                           "inherit_none"] = "inherit_all"
    specified_rules: list[str] | None = None  # if cascade_mode =
                                              # "inherit_specified"

    # INITIAL MEMBERS
    initial_member_proposals: list[str]       # persona_ids to invite
                                              # to the child env

    # WHO IN THE PARENT CONSENTED
    parent_consent_persona_ids: list[str]
    parent_consent_process: Literal["lead_decided",
                                     "cohort_voted",
                                     "operator_decided"]

    proposed_at: datetime
    proposed_by: str                          # persona_id in parent env
    signed_by: bytes
```

### A.24 `ProposedCoordinationShape` schema

<a id="appendix-a24"></a>

```python
@dataclass
class ProposedCoordinationShape:
    schema: str = "proposed-coordination-shape/1"
    proposal_id: str
    environment_id: str                       # scoped to this env
    proposed_by: str                          # persona_id (must be
                                              # a member of the env)
    proposed_at: datetime

    shape_name: str
    scope: Literal["intra_env", "env_to_external", "env_to_env"]
    meta_mechanism: Literal["entity_group", "batch_operation",
                             "staged_sequence", "stream_policy",
                             "derived_metric"]
    shape_definition: dict

    composed_shape_refs: list[str] | None = None
    composition_depth: int = 0                # max 3

    evidence_refs: list[str]
    rationale: str

    safety_critical: bool = False

    # LIFECYCLE STAGE (persona adoption trajectory):
    #   candidate — proposed, not yet tested
    #   trial     — being tested by part of the cohort
    #   accepted  — adopted as "how we coordinate here"
    #   promoted  — promoted beyond this env (domain or MetaShape tier)
    # A shape advances through stages as the cohort adopts it.
    stage: Literal["candidate", "trial",
                    "accepted", "promoted"] = "candidate"
    cosigning_personas: list[str] = field(default_factory=list)
    operator_cosigned: bool = False

    # VALIDATION STATUS (kernel admission checks):
    #   pending       — not yet validated by kernel
    #   schema_valid  — schema conforms to meta-mechanism
    #   safety_checked — safety-floor composition verified
    #   admitted      — ready for trial stage (all checks passed)
    #   refused       — kernel rejected the shape (see refusal_reason)
    # A shape must reach "admitted" before it can advance to trial.
    validation_status: Literal["pending", "schema_valid",
                                "safety_checked", "admitted",
                                "refused"] = "pending"
    refusal_reason: str | None = None

    signed_by: bytes = b""
```

### A.25 Shape library tiers diagram

<a id="appendix-a25"></a>

```text
SHAPE LIBRARY (discoverable, not imposed):

  MetaShapes (~35 seed shapes from v1.0.x)
      Any persona in any env can browse and import.
      These are the "common vocabulary" — proven across domains.

  Domain-promoted shapes
      Any persona in an env within this domain can browse and import.
      These are "what teams in this field found useful."

  Env-local shapes (other envs in the same deployment)
      Discoverable if visibility permits; importable with proposer
      consent.

ENVIRONMENT INSTANCE (active coordination):
  Starts EMPTY. Grows as personas propose and adopt.
  Personas MAY import from the library — or compose their own.
  No tier forces activation. The personas decide.
```
