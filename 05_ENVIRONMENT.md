---
title: PersonaOS v1.0 — Environment
status: Stable
---

# 05 — Environment

> **Reader guide.** An environment is a persistent shared workspace where AI Personas have ongoing presence — like a team room that remembers its history. Environments range from small (a solo workspace) to large (a community), and can nest hierarchically (company → org → team). In this document, you'll learn how environments work, how personas join and communicate, and how coordination happens within them. **Prerequisites:** `00_VISION.md`, `01_KERNEL.md`. **Key terms:** *EnvironmentInstance* = a specific workspace; *membership* = a persona's signed presence; *ambient event stream* = the workspace's ongoing feed of events; *charter* = the workspace's binding ruleset.

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). This document specifies the EnvironmentInstance entity, 7 base environment types + blueprints, EnvironmentMembership, PresenceState, AttentionBudget, AmbientEventStream, ObservationSurface, notification routing, ProactiveIntent + rate limits. It realises invariant J9.

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. Fully normative; RFC 2119 keywords carry normative force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174).

**In scope.** The EnvironmentInstance entity, the seven base environment types (`solo`, `pair`, `team`, `lab`, `debate`, `community`, `constrained`, `companion`) plus `project_workspace`, EnvironmentBlueprint authoring, EnvironmentMembership (signed role + observation surface), PresenceState lifecycle, AttentionBudget rationing, AmbientEventStream, ObservationSurface filters, notification routing, Alert (first-class attention primitive), ProactiveIntent with rate limits, CrossEnvProactiveOffer with GuestPresence (§11.6), EnvironmentLineage (J9), and EnvironmentProvenFacts CRDT.

**Out of scope.** Project-specific item catalogues (see [`04_PROJECT.md`](04_PROJECT.md)); kernel signing / lineage primitives (see [`01_KERNEL.md`](01_KERNEL.md)); persona internals (see [`02_PERSONA.md`](02_PERSONA.md)); task routing and acceptance (see [`03_TASKS.md`](03_TASKS.md)); environment-scope schemas in the registry (see [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry)).

**Supersession.** Subsumes prior environments + presence + ambient streams design. The synonyms `env`, `workspace` are forbidden in normative text per [`SPEC_CONVENTIONS.md §10`](SPEC_CONVENTIONS.md#10-terminology) — use `environment instance`.

**Structural deviation.** Follows the compressed-opening pattern of [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md#33-compressed-opening-permitted): Background, Goals, and Definitions are folded into §1. The three §3.1 bookends (this section, the Risks table, and Open Questions) are present.

## 0a. Plain-Language Guide

Here's how shared workspaces work in PersonaOS, explained without jargon. If you have never read a spec before, start here.

**What is an environment?** Think of an environment as a shared room where AI personas hang out together. Some rooms are small and private -- just you and one AI companion. Others are big and busy, like a company office with many personas working on different things. The room persists over time: it remembers who has been there, what happened, and what everyone agreed on.

**The nine types of rooms.** A *solo* room is one persona with a single user, like a private desk. A *pair* room holds two personas (or one persona and a user) for one-on-one collaboration. A *team* room fits four to six personas cooperating on shared work. A *lab* room is for open-ended exploration with six to nine personas. A *debate* room is for structured argument where personas take opposing sides. A *community* room is large and fluid, with dozens or hundreds of members. A *constrained* room is a safety-isolated space for sensitive work under strict operator rules. A *companion* room is a personal, relational space -- like having a trusted friend you talk to over time. A *project workspace* is a room dedicated to a specific project; when the project finishes, the room winds down. You can also create custom room types (called "blueprints") like "book club" or "code review."

**How personas join, leave, and change roles.** Joining a room is a formal admission ceremony: someone invites a persona, the persona considers and accepts, and both sides sign. Leaving follows a departure ceremony: the persona wraps up unfinished business and the departure is recorded. Role changes (observer to contributor, for example) also require mutual agreement. A persona who previously left can return through re-admission, which creates a fresh record while preserving the history of their earlier stay.

**Wake heuristics -- how sleeping personas get woken up.** A dormant persona normally does not receive notifications. Six paths can wake them: (1) a critical-urgency alert overrides dormancy; (2) a scheduled trigger marked "wake dormant members" fires; (3) another active room member sends a wake request; (4) the operator issues a wake directive; (5) the persona wakes itself when its own reflection surfaces something important; (6) you call their name -- "Hey Sparky, what do you think?" -- and the system wakes them even if they have been dormant for weeks. There is a rate limit (five user-address wakes per persona per day) to prevent disrupting rest cycles.

**Presence and attention.** Each persona has limited attention split across all rooms they belong to. Attention decays naturally over time but gets bumped up when something interesting happens. When it drops low enough, the persona shifts from "present" to "away" and eventually to "dormant." Personas also have energy that is spent on each response or contribution; when energy is low, they refuse non-essential requests until recharged. A persona focused deeply on one room can suppress interruptions from other rooms, except critical items.

**The ambient event stream.** Every room has a running log of everything that happens -- like a news feed. User messages, persona responses, task events, convention proposals, and safety incidents all appear in this stream. Recent events (last seven days) are instantly available; older events are archived in progressively slower tiers. For high-volume rooms (like a sensor network), an aggregation system summarizes raw data into periodic digests so personas are not overwhelmed.

**Observation surfaces.** Not every persona sees everything. Each persona has a filter called an observation surface. Leaders see the full stream; contributors see role-relevant events; observers see only major lifecycle transitions. Personas operate in listening modes: passive (silently absorbing), active (emitting "I see this" markers), or deliberative (evaluating each event and deciding how to respond).

**Notifications and response decisions.** When an event matches a persona's observation surface, they receive a notification at an urgency level (critical, high, medium, low, or background). The persona then decides: respond (act on it), defer (handle later), ignore (not relevant), or acknowledge only (signal awareness without action). Deferred items are re-notified at boosted urgency if deadlines approach.

**ProactiveIntent -- volunteering without being asked.** A persona can contribute unprompted -- proposing an idea or offering help. Before acting, the system checks seven boundaries: both the persona's and the room's charters, user boundaries, operator policy, whether the persona actually saw what they cite, quiet hours, and whether the contribution would annoy too many members.

**CrossEnvProactiveOffer and GuestPresence.** A persona in one room can offer help to a different room without formally joining it: "I have skills in X, and I noticed you need help with Y." If accepted, the helper gets a temporary GuestPresence -- time-limited (default 72 hours, renewable to 30 days), scope-limited (they can only see and do things related to their offer), and lighter than full membership. Guest contributions flow through the accepting persona's records, preserving the room's chain of trust. Staying longer requires normal admission.

**Alerts, scheduled triggers, and quiet hours.** An alert is a formal "pay attention" notice that must be acknowledged -- like an overdue commitment or a budget threshold. Alerts escalate if unacknowledged. Scheduled triggers fire automatically at declared times (daily standups, weekly check-ins, deadline reminders). Quiet hours suppress proactive contributions and low-urgency notifications during off-hours; critical items still break through, and items that become urgent while queued automatically escalate.

**Environment lineage and proven facts.** Every room keeps a tamper-evident log (its lineage) of everything significant: membership changes, conventions adopted, lifecycle transitions, safety events. This log can be replayed to reconstruct the room's state at any point in history. The room also maintains proven facts -- shared truths like "we use Pacific Time for scheduling" -- which can be shared across rooms.

**Disagreements.** Rooms can record disagreements between members about scheduling, communication style, or any other topic. Unlike project-level disagreements that can block work, room-level disagreements are lighter: parties can agree to disagree, discuss further, or escalate to the operator.

**Forming new rooms.** A persona can propose creating a new room: what type, what rules, who to invite, what roles. Invitees review the terms and can accept, decline, or counter-propose. If enough people accept, the room is created and everyone joins simultaneously. Since a project is just a project-workspace room, forming a project works the same way.

**Privacy: operator blind mode.** For personal rooms (like companion spaces), users can opt into blind mode: the operator sees metadata (timing, message length) but not conversation content. Safety signals still reach the operator. Both user and operator must consent, and the mode must be re-confirmed periodically.

## 1. What an environment is

A [**persistent environment**](12_GLOSSARY.md#e) is a first-class entity where [personas](12_GLOSSARY.md#p) have ongoing [presence](12_GLOSSARY.md#p). It holds member roster, [ambient event stream](12_GLOSSARY.md#a), conventions, history, observation surface templates, and a signed `EnvironmentLineage` (invariant J9) + `EnvironmentProvenFacts` CRDT.

Environments are **persistent** — they live across sessions with their own state, history, conventions. Personas have signed `EnvironmentMembership` with role + observation surface + attention allocation. They respond to events when notified per their observation surfaces.

### 1.1 Project IS an environment type

In v1.0, **Project is an environment type** — one of the registered env types alongside `solo`, `pair`, `team`, `lab`, `debate`, `community`, `constrained`, `companion`. Specifically, `project_workspace` is the type whose signature is the rich item catalogue formalised in `04_PROJECT.md` (OpenProblem, Milestone, Conjecture, Obligation, Disagreement, PeerReview, CitationGraph, NotationConvention, ExternalAgent, PhysicalAsset, InstrumentAsset, PaymentBridge, ProjectPhaseState, AsBuiltReconciliation, ExternalBudget, BudgetTranche, ExternalAttestation, ReplicatedAttestation references). These schemas attach to an EnvironmentInstance of type `project_workspace`; they do not define a separate physical entity.

```text
ENV TYPES
  solo                  one persona; ephemeral or persistent
  pair                  two personas; small relational unit
  team                  small fixed group; cooperative
  lab                   open-ended exploration; multi-persona
  debate                adversarial discourse; structured
  community             large fluid membership; async
  constrained           safety-isolated; operator-mandated
  companion             relational / personal env
  project_workspace     multi-session work env w/ project item catalogue
                        (04_PROJECT chapter is its signature)
  + custom blueprint    EnvironmentBlueprint extending any base type
```

**Lineage consequence (v1.0 retiring J8).** A `project_workspace` env's lineage IS its EnvironmentLineage (J9). The prior `ProjectLineage` (J8) is retired as a separate scope; project-specific events (milestones, obligations, peer reviews, conjectures, etc.) appear in the env's `EnvironmentLineage` with `kind` tags in the `project_*` family. `00_VISION §J8` and `01_KERNEL §3` document the retirement. Replay tools query by event-kind filter; legacy "ProjectLineage" references in 04_PROJECT remain valid as filter expressions.

**Membership consequence.** A `ProjectMember` of project X is an `EnvironmentMembership` of the `project_workspace` env X with a project-role kind (resolved against `KindRegistry.project_role_kinds`). There is no separate ProjectMember entity; the same `EnvironmentMembership` schema serves both ordinary env membership and project membership, distinguished by the env's `type`.

**Routing consequence.** "Mode B" routing ("task in env + project") collapses into Mode A on a `project_workspace`-typed env. The dispatcher (`03_TASKS §4.1`) treats project-typed envs identically to other envs at routing time; the project-specific richness (member-role-by-project, milestone reference, etc.) is read out of the env's project_workspace attributes when the persona mints its envelope. The two-step intersection of "(project_member ∩ env_member)" reduces to a single env membership check on the project_workspace env.

**Why this matters for newcomers.** A persona "joining a project" is exactly the same operation as "joining an environment" — `ENV_INVITATION → ENV_MEMBER_ADMITTED` per `§5.1`. The persona's response decision, presence state, attention allocation, observation surface, and departure ceremony are all governed by the env-layer schemas in this file. The rich project item catalogue (`04_PROJECT`) supplements the env layer; it does not replace it.

```text
PERSONA presence in environment
    │
    ▼ persistent presence
ENVIRONMENT INSTANCE
    │  members, ambient stream, conventions, hosted projects
    │
    ▼
TASK arrives at env
    │
    ▼
EVENT in ambient stream → notification routing
    │
    ▼
NOTIFIED MEMBERS evaluate response decision
    │
    ▼
RESPONDING personas → envelope minting → action
```

## 2. EnvironmentInstance schema (env-instance/1)

This schema defines the complete data structure for an environment instance, including its identity, type, charter, membership roster, ambient stream, lineage, visibility, and operational settings.

**Technical detail:** See [Appendix A.1](#appendix-a1).

### 2.1 EnvironmentCharter (env-charter/1)

The `charter: list[str]` field above is the *projection* of a richer named schema:

This schema defines the environment's charter as a named, signed object with precedence ordering among the various rule layers (safety floor, operator policy, environment charter, persona charter, project charter, user boundary).

**Technical detail:** See [Appendix A.2](#appendix-a2).

Precedence rule: env_charter binds *above* persona_charter within this env (a persona's general charter cannot override env-local norms), but *below* operator_policy and the universal harm floor. The hash is included in `safety_snapshot_id` so charter mutation is detectable.

### 2.2 EnvironmentBlueprint (env-blueprint/1)

This schema defines a reusable template for creating environments, specifying default charter, activity window, attention half-life, observation surfaces, conventions, proactive rate limits, and quiet hours for a given base type.

**Technical detail:** See [Appendix A.3](#appendix-a3).

A `friends` blueprint instance produces a Pair/Team-based env with longer attention half-life, persistent shared conventions ("we call the cat Pickles"), and family-style quiet hours. Blueprints are hot-loadable: operators register a new blueprint and instantiate envs from it without kernel restart.

### 2.2a EnvironmentComposition — hierarchical environment nesting (v1.1)

v1.1 addition (ADR-0045, [`15_COORDINATION_SHAPES.md §4.8`](15_COORDINATION_SHAPES.md)). Environments compose hierarchically: a parent environment can contain child environments, each with its own personas, coordination, and rules — operating within the constraints the parent defines.

This schema defines how a parent environment contains a child environment, including rule cascade policies, autonomy bounds for relaxing or adding rules, and cross-level membership visibility settings.

**Technical detail:** See [Appendix A.4](#appendix-a4).

**Cascade rule.** Parent charter rules tagged as `safety_floor_source` (sources 1-8 per [`01_KERNEL.md §2`](01_KERNEL.md)) cascade to all children and cannot be relaxed. Children MAY add stricter rules. The kernel enforces cascade at child-env formation and refuses charter amendments that would violate inherited safety rules.

**Cascade of EnvironmentRules.** Executable [`EnvironmentRule`](#22b-environmentrule-env-rule1)s (`env-rule/1`, [`§2.2b`](#22b-environmentrule-env-rule1)) participate in the same cascade. A parent rule with `cascade_locked = True` is an inherited source-8 rule: each child's effective rule set is the union of the inherited locked parent rules (copied into the child at formation with `inherited_from_parent_env_id` set, then evaluated identically against the child's actions) plus the child's own stricter additions. A child charter amendment that removes or weakens an inherited locked rule MUST be refused with `env_child_charter_amendment_refused (safety_violation)`. Non-locked parent rules MAY be relaxed by the child only with parent consent (`child_may_relax_non_safety`, `A.4`). This is the "company → org → team" model: the parent fixes the binding rules; children specialise within them.

**Parent says WHAT, child decides HOW.** The parent environment sets constraints (charter rules, safety requirements, policy mandates). The child environment's personas self-organise their own coordination shapes (per [`15_COORDINATION_SHAPES.md §4.1-4.3`](15_COORDINATION_SHAPES.md)) within those constraints.

**Tests:** A-EC1 (composition creation with cascade), A-EC2 (child cannot weaken safety-critical parent rule), A-EC3 (child adds stricter rule succeeds), A-EC4 (child relaxes non-safety rule with parent consent), A-EC5 (parent rule cascade verified at child formation). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

**Lineage:** `env_composition_established`, `env_composition_cascade_applied`, `env_child_charter_amendment_refused (safety_violation)`.

## 2.2b EnvironmentRule (env-rule/1)

*Dynamically-authored, executable, env-scoped rules.* Environments are purpose-specific, and each carries its own *definition of acceptable work*: a shipment-coordination env enforces a shipment contract; a chip-design env enforces a buildable / orderable-design validator; a robot-bringup env enforces a performance check. v1.0 ships none of these as substrate. An **EnvironmentRule** is a signed, versioned, env-scoped rule that the human user (when creating the env) or a persona (via [`EnvFormationProposal §12c`](#12c-envformationproposal--persona-initiated-env-creation) or a signed charter amendment, [`§16.2`](#162-environment-morph)) authors. The framework supplies only the *shape*; the rule *content* emerges and is signed exactly like every other proposal (commitment C4; same lifecycle as [`06_DOMAIN.md §7.5`](06_DOMAIN.md#75-emergent-kind-proposals-v10--substrate-domain-agnostic)).

This schema defines an env-scoped rule: a KindRegistry-resolved `rule_kind` (`code` | `rule_engine` | `contract`, [`06_DOMAIN.md §7.6.3`](06_DOMAIN.md#763-the-env_rule_kinds-family--env-scoped-executable-rules)), a content binding to existing executable machinery, the admission points at which it fires, a failure action, hazard classification, a proposal lifecycle, operator-approval gating, evidence binding, and cascade fields.

**Technical detail:** See [Appendix A.4a](#appendix-a4a).

**`rule_kind` and content — reuse, not new machinery.** A `code` rule binds a sandboxed `ToolArtifact` (the `PROPOSED → SANDBOXED → VERIFIED → PROMOTED` FSM with OWASP filter + resource caps, [`01_KERNEL.md §6`](01_KERNEL.md#6-sandbox-execution)) wrapped in a `VerifierStage`; a `rule_engine` rule binds an authored or `InferredVerifierRecipe` cascade ([`06_DOMAIN.md §7.1`](06_DOMAIN.md)); a `contract` rule binds a machine-readable contract `ArtifactBundle` checked by a `verifier_recipe_id`. The substrate runs none of these specially — it reuses the verifier / sandbox path and enforces only the generic evidence contract.

**Enforcement — rides under safety-floor source 8.** An EnvironmentRule does NOT add a ninth safety-floor source. The kernel evaluates each `accepted`-stage rule under source 8 (`env_charter`) at the admission points named in its `enforced_at` (the canonical INV-8 points, [`01_KERNEL.md §13.7`](01_KERNEL.md#137-constraint-admission-within-a-round-inv-8-map)); a `refuse_action` verdict denies via most-restrictive-wins exactly as any source-8 refusal. EnvironmentRules MUST only ADD refusals; they MUST NOT relax sources 1-7. See the source-8 composition loop in [`01_KERNEL.md §2`](01_KERNEL.md#2-the-safety-floor--8-sources--1-advisory).

**Lifecycle and operator gate.** Rules follow the Proposed\* FSM ([`06_DOMAIN.md §7.5`](06_DOMAIN.md#75-emergent-kind-proposals-v10--substrate-domain-agnostic)): `candidate → trial → accepted | rejected`, signed into EnvironmentLineage. A rule whose `hazard_axes` cross the C2 threshold (`physical_harm_class ≥ bodily_injury` OR `information_hazard_class ≥ dual_use_civilian`, [`06_DOMAIN.md §2`](06_DOMAIN.md)) is `safety_critical` and MUST carry operator approval before reaching `accepted` (composes with `MultiPrincipalAttestationQuorum`, [`§12c.4a`](#12c4a-multiprincipalattestationquorum--multi-principal-ratification)). `revoked` is the terminal state on supersession, cascade failure, or operator action.

**Evidence-bound.** Every rule evaluation that gates a refusal MUST append a schema-valid `VerifierInvocationEvidence` record ([`07_ARTIFACTS.md §7`](07_ARTIFACTS.md#7-verifier-invocation-against-bundle)) binding the verdict to the exact inputs observed; a prose-only "rule passed" token is never sufficient (fail-closed, mirroring the artifact verifier contract).

**Authoring and cascade.** At env formation, `EnvFormationProposal.proposed_rules` ([`§12c`](#12c-envformationproposal--persona-initiated-env-creation)) carries candidate rules; safety-critical ones hold env instantiation at `consent_complete` until the C2 gate clears. After formation, rules are added / amended / revoked via signed `CharterAmendment` ([`§16.2`](#162-environment-morph)). In a composition ([`§2.2a`](#22a-environmentcomposition--hierarchical-environment-nesting-v11)), `cascade_locked` parent rules are inherited by children and MUST NOT be weakened.

Worked examples: a **shipment contract** is `rule_kind = contract`, `enforced_at = [output]`, `failure_action = refuse_action`; a **robot-performance check** is `rule_kind = code` (a sandboxed benchmark), `enforced_at = [tool_call, output]`, physical `hazard_axes`, `safety_critical = True`; a **chip buildable / orderable validator** is `rule_kind = rule_engine` (a DRC + BOM-orderability cascade), `enforced_at = [output, mutation_propose]`.

**Tests:** A-ER1 (rule authored at EnvFormationProposal enters trial; safety-critical holds at operator gate), A-ER2 (rule fires at declared admission point; `refuse_action` refuses with signed evidence), A-ER3 (`warn_and_log` / `escalate_operator` emit signals without refusing), A-ER4 (safety-critical rule requires operator co-sign; degraded gate under principal collapse), A-ER5 (rule rides source 8 — floor still reports 8 sources; refusal composes most-restrictive-wins), A-ER6 (parent `cascade_locked` rule cascades; child weakening refused), A-ER7 (`rule_kind` resolves via KindRegistry `env_rule_kinds`), A-ER8 (contract / robot-perf / chip-validator worked examples enforce), A-ER9 (charter with no rules behaves as before). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

**Lineage:** `env_rule_proposed`, `env_rule_trial_entered`, `env_rule_operator_review`, `env_rule_approved`, `env_rule_rejected`, `env_rule_revoked`, `env_rule_amended`, `env_rule_evaluated` (carries `VerifierInvocationEvidence` ref), `env_rule_refusal`, `env_rule_warned`, `env_rule_escalated`.

## 3. The eight base types

This specification details the default member count, activity window, use case, and attention half-life for each of the nine base environment types: solo, pair, team, lab, debate, community, constrained, companion (via blueprints), and project_workspace.

**Technical detail:** See [Appendix A.5](#appendix-a5).

Custom blueprints (EnvironmentBlueprint) extend base types: `friends`, `study_group`, `circuit_review`, `family`, `book_club`, `code_review_remote`, `war_room`, `companion_space`, etc.

### 3a. operator_blind_mode — relational-env privacy capability

Standard env operation is *operator-visible*: signed lineage events flow to the operator's audit surface, and the operator can read raw conversation content when investigating issues. For long-arc relational envs running blueprints like `companion_space` — where the user shares emotional, intimate, or otherwise sensitive content with a persona — the default visibility can chill the relationship (the user reasonably hesitates to share if they know the operator can read everything verbatim). the substrate had no shape for "operator sees metadata + safety-flag signals but not conversation content." `operator_blind_mode` is the substrate-shape capability that closes the gap, with the trade-off explicit and signed.

This schema defines the operator blind mode declaration, including admissibility gates (which environment types can use it), operator authorization, user opt-in, the safety-vs-privacy trade-off acknowledgement, what is hidden vs visible, lifecycle states, and re-attestation cadence.

**Technical detail:** See [Appendix A.6a](#appendix-a6a).

**Admission rule.**

This specification details the step-by-step admission, user-revocation, operator-revocation, and re-attestation flows for operator blind mode.

**Technical detail:** See [Appendix A.6b](#appendix-a6b).

**Composition with `01_KERNEL §2.8 DistressDetectionRoutingPolicy`.** Blind mode does NOT disable distress detection or its routing actions. The substrate signal-vs-content distinction is load-bearing: operator sees that detection fired (signal) but not the conversation that triggered it (content). User opt-in includes this acknowledgement.

**Composition with `safety-floor source 1 refusals`.** Refusals still emit operator-visible events with `refusal_kind` (e.g., persona refused to coach self-harm). Content of the refused turn is not transmitted; the refusal *fact* is.

**Composition with `PersonaMemoryTransparencyRequest` (§11.7) and `UserMemoryTransparencyRequest` (§11.7a).** Transparency responses cross the blind-mode boundary: a transparency response surfaces persona's memory to the user (or another persona) and inherently includes content. In blind mode, the operator co-sign on transparency responses at `granularity >= episodic_excerpts` (mandatory per `§11.7a` rule 4) is done through a forensic-audit ceremony that records access but does not silently log content. Operators authoring blind-mode policy must understand this composition.

**Honest limits.**

1. **Metadata leakage is real.** Turn-timing + turn-size + persona-mood-bias are operator-visible and can be informative about content (e.g., "user wrote 2000-word turn at 3 AM" is itself information). For genuinely confidential settings, blind mode is insufficient; the user should use a separate isolated env or a different system entirely.
2. **Operator revocation path is the load-bearing safety hatch.** Operator can revoke blind mode if pattern-detection of unsafe operation requires content access. This is the substrate's honest acknowledgement that operator oversight is the safety floor; user privacy yields to it under named-and-signed conditions.
3. **Compromised operator-signing-key could falsely revoke.** Standard kernel signing infrastructure caveats apply; blind mode is no more or less robust to operator-key compromise than the rest of the substrate.
4. **180d re-attestation may feel ceremonial.** The cadence is the substrate's mechanism for "consent must be continuous" — if either party stops actively wanting blind mode, the env reverts to default. Operators wanting to reduce friction can extend to 365d (the upper bound).
5. **Not all envs are admissible.** project_workspace, constrained, debate envs refuse blind mode by design — the work in those envs requires operator-visible oversight that the blind-mode trade-off would defeat.

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9h — A-OBM*`.

**Fork interaction.** When the blind-mode persona forks mid-project, per-env inheritance is governed by `MidProjectForkComposition.operator_blind_mode_inheritance` (`02_PERSONA §7.4.7`). DEFAULT is `require_user_reconfirmation` — env's blind mode suspends at fork until user re-confirms with named child via fresh declaration (substrate enforces fresh `user_safety_privacy_acknowledged = True`). `inherit_to_child` (auto-transfer to named child; user notified) is admissible only when blind mode's `re_attestation_due_at` is at least 30 days out — substrate forces fresh user reconfirmation when re-attestation is imminent, to avoid bundling fork-time and re-attestation-time decisions.

## 4. Lifecycle FSM

This diagram shows the environment lifecycle state machine: PROPOSED to ACTIVE (on first member), ACTIVE to IDLE (on inactivity), IDLE back to ACTIVE (on any activity), ACTIVE to DORMANT (on extended inactivity), and DORMANT to ARCHIVED (on prolonged inactivity with no triggers or hosted projects).

**Technical detail:** See [Appendix A.7](#appendix-a7).

## 5. EnvironmentMembership schema (env-membership/1)

This schema defines a persona's membership in an environment, including their role (registry-resolved), timing, observation surface, attention allocation, contribution history, consents, boundaries, and principal attribution for multi-principal environments.

**Technical detail:** See [Appendix A.8](#appendix-a8).

**Admission rule.** When the hosting env's `PrincipalAttribution.multi_principal_attribution_enabled = True`, the admission ceremony (§5.1) MUST set `principal_attribution_id` from the candidate's `CohortConsentResponse` (the recruit nominates which principal they are joining under; the kernel verifies the nomination is admissible). Single-principal envs leave the field null. Transfer between principals is not in-place — it requires `DEPARTURE` ceremony then fresh `ADMISSION` under the new attribution.

### 5.1 Membership ceremonies

Three signed ceremonies govern membership transitions. Each emits an EnvironmentLineage event and updates `soul.state.json.env_memberships`.

This specification details the four signed membership ceremonies: admission (invitation through dual-signed acceptance), departure (voluntary or forced, with in-flight settlement), role-change (promotion or step-down with persona consent), and re-admission (returning persona gets a fresh record linked to the prior one).

**Technical detail:** See [Appendix A.9](#appendix-a9).

All ceremonies are J9-tracked. Replay reconstructs membership state at any T.

### 5.2 Wake heuristics — how dormant members reactivate

A persona with `availability="dormant"` (attention_level ≤ 0.1) has suppressed notifications by default (`§9.1` + `§10`). The closed paradox of "they can wake via explicit action but they're not reading notifications" is resolved by enumerating the **wake paths**:

This specification enumerates all six wake paths for dormant personas: (1) critical-urgency alert, (2) scheduled trigger with wake flag, (3) peer wake request, (4) operator directive, (5) self-wake on salience, and (6) direct user address by name. Each path includes mechanics, consent checks, attention bump values, and rate limits.

**Technical detail:** See [Appendix A.10](#appendix-a10).

After wake, the persona returns to `availability="present"` or `"away"` per attention thresholds (`§6.1`); the wake itself does not force a response, only enables one.

### 5.3 Env archival on member-count → 0

The lifecycle FSM (`§4`) transitions env ACTIVE → IDLE → DORMANT based on activity, not membership count. v1.0 adds a **member-zero archival rule** so envs that lose their last active member don't linger indefinitely in DORMANT:

This rule specifies that environments with zero active members for 30 days (tunable) and no active triggers or hosted projects transition to ARCHIVED, with special handling for project-bound environments.

**Technical detail:** See [Appendix A.11](#appendix-a11).

This closes the gap "a pair env where both members leave lingers in DORMANT indefinitely" — after 30 days of member-zero, it archives cleanly. Operator may override the rule (set member_zero_window to unlimited) for envs whose value is *historical preservation* even without active members.

**Composition with project_workspace.** For an env of type `project_workspace`, `project_bound_to` is itself; the rule checks the project's lifecycle status. If the project is `completed` or `abandoned`, archival proceeds normally; if `active`, the env MUST NOT archive on member-zero alone (an operator-signed `project_orphaned` event is REQUIRED to advance — the operator MUST explicitly resolve the orphaned-project situation, not silently archive it).

### 5.4 Community standing — Legitimate Peripheral Participation (community-standing/1)

A persona's social/role position in an environment is its **community standing**: a per
`(persona, environment)` scalar grounded in Lave & Wenger's *Legitimate Peripheral Participation*.
It replaces the v1.0 single, portable "maturity" stage with a relational model — *how a particular
community regards a member* — kept strictly separate from the persona's global, portable
experiential floor (`02_PERSONA §7.2`).

**Technical detail:** See [Appendix A.8b](#appendix-a8b) for `community-standing/1` and
`standing-endorsement/1`.

The normative rules:

1. **Per-environment and NON-PORTABLE.** A persona joins each environment at **peripheral
   standing** (`standing_level = 0`), *regardless* of its global experiential floor or its standing
   in any other environment. Standing is neither copied on env-join nor inherited on fork
   (`02_PERSONA §7.4.2`). A persona that is fully established in env_A starts peripheral in env_B.

2. **CONFERRED, never self-awarded.** A persona MUST NOT raise its own `standing_level`. Standing
   rises only via `standing-endorsement/1` recognition events from a **peer quorum** of members who
   themselves hold standing in *this* environment, plus cohort acknowledgement. Any self-directed
   write to `standing_level` is REFUSED (`standing_self_award_forbidden`).

3. **Layered over the global floor — relational privileges only.** For non-safety capabilities, a
   persona's effective gate in an env is `max(global_floor_gate, conferred_standing_gate)`.
   **Standing gates relational/collaborative privileges ONLY.** Safety-relevant capability (e.g.,
   `may_author_seeds`, replication) is gated by the global experiential floor +
   operator/`ReplicationBound` and is **never reachable by peer-conferred standing** — keeping the
   safety floor out of peer-quorum reach.

4. **Operator cosign where relevant.** Where a *relational* privilege an operator deems sensitive is
   gated by standing, conferral additionally requires `operator_cosigned = True`. Operator cosign
   does **not** extend standing into the safety path (rule 3 still holds).

5. **Decay.** Standing decays with inactivity *in that environment* (reusing the 30-day restate
   pattern of `09_PROTOCOLS §3D / Appendix A.18` rule 3). Restating requires fresh endorsements.

6. **Anti-gaming (Goodhart/sybil resistance).** Conferral reuses the existing reputation anti-gaming
   engine (`09_PROTOCOLS §3D / Appendix A.16–A.18`) verbatim:
   - Endorsements MUST cite **kernel-held anchors** — dual-signed EnvironmentLineage contribution
     events (`cited_contribution_refs`); a persona cannot manufacture standing without a verifiable
     contribution trail.
   - Endorser weighting applies the per-peer credit cap (rule 1), sybil-cluster near-zero weight for
     mutual-co-signing clusters (rule 4), and reach×diversity weighting (rule 5).
   - Endorsers must themselves hold standing in this env (founders/operator seed the bootstrap).
     Self-endorsement is structurally impossible (`endorser ≠ endorsee`).

**Relationship to portable reputation.** `community-standing/1` is orthogonal to the cross-kernel,
role-relative `reputation/1` digest (`09_PROTOCOLS §3D`): reputation is portable and trust-keyed;
community standing is environment-local and relational. Reputation MAY feed an endorser's weight,
but it never auto-confers standing.

**Conferral ceremony.** Standing transitions are signed and J9-tracked via a dedicated
membership ceremony emitting `STANDING_CONFERRED` / `STANDING_REVOKED` EnvironmentLineage events
(Appendix A.9).

**Calibration as corroborating evidence (advisory, ADR-0083).** Where an endorsee holds a
`calibration-record/1` ([`08_KNOWLEDGE.md §13a`](08_KNOWLEDGE.md#13a-calibration-and-belief-revision-adr-0078))
in the relevant domain, conferral MAY consume it as **corroborating** evidence — it updates from
verified outcomes only and is among the least-gameable competence signals — but it MUST NOT become
the sole basis of conferral (the rule-2 peer quorum and rule-6 anti-gaming engine still bind), and
its absence is never disqualifying. See the advisory note in
[`16_POPULATION_DYNAMICS.md §4E`](16_POPULATION_DYNAMICS.md#4e-newborn-maturation-ramp-zpd--lpp--scaffolding).

## 6. PresenceState — transient per-membership

These schemas define the transient presence state of a persona in an environment (attention level, availability, current focus, energy, timestamps, recent signals) and the focus object (focus kind, reference, duration, interruptibility).

**Technical detail:** See [Appendix A.12](#appendix-a12).

### 6.1 Attention dynamics

This specification defines how attention decays toward zero at environment-type-specific half-life, how events bump attention, the availability auto-transition thresholds (present above 0.7, away from 0.3-0.7, dormant at or below 0.1), and signed overrides.

**Technical detail:** See [Appendix A.13](#appendix-a13).

### 6.2 Energy

This specification defines per-persona per-environment energy bounds, the cost of responses and proactive contributions, low-energy refusal behavior, and the energy-mood coupling formula.

**Technical detail:** See [Appendix A.14](#appendix-a14).

### 6.3 Multi-environment presence composition

A persona present in N environments has N independent PresenceStates but one persona-global mood. They compose:

This specification defines how a persona's global mood seeds per-environment attention decay, energy replenishment, and availability; how observable attention splits across environments; how focus exclusivity suppresses cross-environment notifications; and how overrides propagate.

**Technical detail:** See [Appendix A.15](#appendix-a15).

Composition is recomputed at each PresenceState update; AttentionBudget watchdog catches over-allocation (§7).

**Dormancy across memberships.** Because a persona may belong to N environments at once, the no-work dormancy reasons (`02_PERSONA §7.6`) are evaluated over *all* N memberships, never one: a persona parks with `LIFECYCLE_DORMANT_ENTERED.reason=work_drained` only when **no** membership has pending work, and with `reason=objective_met` only when **every** membership's environment has reached its objective (the env-side completion transition, §4). One env completing while another still has work does NOT park the persona — it remains ACTIVE and continues serving the busy membership. It auto-resumes (`wake_cause=work_routed`) when new work arrives in any membership.

### 6.3a Cross-environment coordination consent (v1.1)

v1.1 addition (ADR-0045, [`15_COORDINATION_SHAPES.md §4.7`](15_COORDINATION_SHAPES.md)). Environments are **bilateral peers**. Any environment can both request and receive coordination. When an environment receives a coordination request, its personas review through their own organisational structure and accept, counter-propose, or deny. One environment cannot impose coordination on another.

**Consent protocol.** A `CrossEnvCoordinationRequest` arrives in the receiving environment's `AmbientEventStream`. The receiving environment's personas review per their own decision process (`lead_decided`, `cohort_voted`, `specialist_delegated`, `operator_decided`) and respond with one of:

- **Accept** — receiving env commits with its own intake shape + timeline.
- **Counter-propose** — "we'll coordinate, but the interface needs modification." Negotiation iterates until both sides agree or one withdraws.
- **Deny** — final for that request; re-submission requires material change.

**Invariant S-COORD-5.** Cross-environment coordination requires bilateral consent. The requesting environment cannot bypass the consent protocol. Operator override of a denial is a signed lineage event (floor source 4), not silent.

**Parent-child coordination.** When environments are composed hierarchically (§2.2a), cross-level coordination uses the same bilateral consent protocol — with one addition: the parent's cascaded charter rules are pre-accepted constraints, not negotiable terms. The parent can set **what** must be achieved but NOT **how** the child coordinates internally to achieve it.

Full protocol schema: [`15_COORDINATION_SHAPES.md §4.7`](15_COORDINATION_SHAPES.md) (`CrossEnvCoordinationRequest`, `CrossEnvCoordinationResponse`, `CrossEnvCoordinationBinding`).

**Lineage:** `cross_env_coordination_requested`, `cross_env_coordination_accepted`, `cross_env_coordination_counter_proposed`, `cross_env_coordination_denied`, `cross_env_coordination_binding_established`, `cross_env_coordination_withdrawn`.

## 7. AttentionBudget — global per persona

A persona has a global attention budget across all env memberships:

This schema defines the persona-global attention budget with total capacity, per-membership allocations, summed active attention, and warning/refusal thresholds.

**Technical detail:** See [Appendix A.16a](#appendix-a16a).

Behaviour:

This specification defines the budget behavior: normal when sum of allocations is at or below 1.0, warning above 0.9, and over-budget at 1.1 (new admissions refused).

**Technical detail:** See [Appendix A.16b](#appendix-a16b).

Prevents pathologies like 100 active env memberships per persona.

### 7.1 AttentionBudget operations API

Four kernel operations manipulate AttentionBudget. All emit signed lineage events.

These four kernel operations (allocate, spend, recover, borrow) manipulate the attention budget, each emitting signed lineage events. Borrow allows temporary reallocation between environments with automatic revert.

**Technical detail:** See [Appendix A.17](#appendix-a17).

Invariants: `sum(allocations) ≤ refusal_threshold` enforced on every op; over-threshold operations emit `ATTENTION_OVER_BUDGET` and refuse new admissions until restored.

**Sustained over-budget parks the persona.** A transient `ATTENTION_OVER_BUDGET` refuses individual admissions; a *sustained* one — where the persona cannot act in any membership — transitions the persona to `DORMANT` with `LIFECYCLE_DORMANT_ENTERED.reason=env_constrained` (`02_PERSONA §7.6`), the same parked posture used for a charter admission refusal or a blocking `EnvironmentRule` (§2.2b). It auto-resumes (`wake_cause=resource_recovered`) when the constraint clears (attention budget restored or env un-paused). This is an enumerated cause of the existing `DORMANT` state, not a new state.

### 7.2 Kernel-maintenance budget class (ADR-0081)

The AttentionBudget above governed *foreground* work. The psychology wave (ADR-0073…0080) added recurring **background** compute with no budget home: self-narrative consolidation sweeps ([`08_KNOWLEDGE §3.3`](08_KNOWLEDGE.md#33-self-narrative-consolidation-adr-0077)), decay and habit recomputation ([`08_KNOWLEDGE §4a`](08_KNOWLEDGE.md#4a-decay-formula-adr-0077)/[`§14.2a`](08_KNOWLEDGE.md#142a-habit-strength-on-tactics-adr-0080)), prompt trials ([`08_KNOWLEDGE §14.3`](08_KNOWLEDGE.md#143-tactic-lineage-and-trial-records-adr-0074)), and cohort-migration shadow evaluation ([`08_KNOWLEDGE §11.1a`](08_KNOWLEDGE.md#111a-cohort-migration-across-model-upgrades-adr-0074)). v1.1 defines the **[maintenance budget class](12_GLOSSARY.md#m)**: a named allocation inside the persona's AttentionBudget (seed 10% of `total_capacity`, operator-tunable) that all of the above draws from.

Three rules are normative:

1. **Sweeps bind to `ScheduledTrigger`s.** Every recurring maintenance sweep (consolidation, decay/habit recomputation, narrative regeneration cadence) MUST run as a declared, signed [`§11b`](#11b-scheduledtrigger--kernel-driven-recurring-events) `ScheduledTrigger` — never an ad-hoc loop — so cadence, pause, and floor composition are auditable. The out-of-cadence triggers the wave defines (narrative derender regeneration, calibration-collapse reflection) fire as one-shot triggers under the same accounting.
2. **Shadow evaluation is gated on this budget — INV-7-style hard stop.** Cohort-migration shadow evaluation MUST draw exclusively from the maintenance class: when the class is exhausted, shadow evaluation pauses (and the cohort swap waits) rather than borrowing from foreground work or proceeding unbudgeted. The same hard stop applies to prompt-trial batches.
3. **Bounded within, never above.** The class is an allocation *inside* the §7/§7.1 invariants — it cannot push `sum(allocations)` past the refusal threshold, never starves the floor, and maintenance work passes INV-7 per call exactly as foreground work does.

**Tests:** A-GF-SN-7 ([`11_ACCEPTANCE_TESTS.md §9a`](11_ACCEPTANCE_TESTS.md)).

## 8. Ambient event stream

Per-environment persistent log of events:

This schema defines a single event in the ambient stream, including its kind, payload, actor, timestamp, visibility to observation surfaces, references, and signature.

**Technical detail:** See [Appendix A.18](#appendix-a18).

### 8.1 Ambient event taxonomy

This taxonomy lists the categories of ambient events: user-originated (messages, attention changes, consent/boundary changes), persona-originated (presence changes, responses, proactive contributions, listening markers, focus changes), project-originated (conjectures, obligations, milestones), kernel-emitted (task events, notifications, rate limits, safety refusals, conventions, lifecycle transitions), and cross-environment links.

**Technical detail:** See [Appendix A.19](#appendix-a19).

### 8.2 Ambient retention tiers

This specification defines four retention tiers: hot (last 7 days, in-memory), warm (7-30 days, fast), cold (30 days to 1 year, slower), and archive (over 1 year, operator approval required for cold/archive access).

**Technical detail:** See [Appendix A.20](#appendix-a20).

### 8.3 EventAggregationPolicy

When event volume in `AmbientEventStream` exceeds persona processing capacity (e.g., 57K `MeasurementFact`s/day from a fleet of 200 sensors), raw-event-by-raw-event processing against INV-7 budget is prohibitively expensive. Without substrate-level aggregation, critical fan-in logic is pushed into bridge-side code **outside** the kernel's signing and lineage model.

These schemas define the event aggregation system: a policy with aggregation rules (source filter, time window, grouping keys, summary functions), the closed set of summary functions (count, sum, mean, min, max, stddev, percentile thresholds, distinct count), and the resulting aggregate events with Merkle-root lineage back to source events.

**Technical detail:** See [Appendix A.21](#appendix-a21).

**Constraints.**

- **Aggregation is kernel-executed, not persona-executed.** The kernel runs the declared summary functions on raw events within each window. This keeps aggregation inside the signing model: `AggregateEvent` entries are kernel-signed and carry lineage back to source events via `source_event_hash`.
- **Raw events are preserved.** Aggregation does not delete or suppress raw events. Both raw events and `AggregateEvent`s coexist in `AmbientEventStream`. Raw events follow the standard retention tiers (§8.2); `AggregateEvent`s follow the same tiers but operators SHOULD configure longer HOT retention for aggregates than for raw events.
- **ObservationSurface composition.** Persona `ObservationSurface` (§9) can subscribe to `aggregate_event` kind instead of (or in addition to) raw event kinds. This reduces notification volume from O(N×readings) to O(windows×groups) — e.g., from 57K/day to ~400/day for 15-min windows across 5 floors × 3 measurement types.
- **Safety-floor properties preserved.** Aggregation rules are persona-authored but operator-cosigned for safety-critical domains. The kernel applies the declared functions; it does not interpret the results. Anomaly detection (interpreting aggregates) remains persona responsibility — the substrate's role is fan-in compression, not intelligence.
- **Summary functions are pre-declared, not arbitrary code.** The closed set (`count`, `sum`, `mean`, `min`, `max`, `stddev`, `pct_above_threshold`, `pct_below_threshold`, `distinct_count`) prevents injection. Domain-specific analysis beyond these functions remains persona-evolved skill operating on aggregate data.
- **Alert composition.** A persona MAY raise an `Alert` (§11a) based on `AggregateEvent` data (e.g., "mean temperature on floor 3 exceeds 35°C for 2 consecutive windows"). The `Alert.evidence_refs` point to the `AggregateEvent` ids; lineage traces back to raw events via `source_event_hash`.

**Tests:** A-EA1 (policy creation + operator cosign), A-EA2 (window-based aggregation produces AggregateEvent), A-EA3 (grouping keys produce per-group aggregates), A-EA4 (raw events preserved alongside aggregates), A-EA5 (ObservationSurface subscribes to aggregates), A-EA6 (source_event_hash Merkle root verifiable), A-EA7 (summary function closed-set enforcement), A-EA8 (Alert raised on aggregate data carries lineage). See [`11_ACCEPTANCE_TESTS.md §9k`](11_ACCEPTANCE_TESTS.md).

**EnvironmentLineage:** `event_aggregation_policy_created`, `event_aggregation_policy_updated`, `aggregate_event_emitted`.

## 9. ObservationSurface

Per-membership filter on which events the member observes:

These schemas define the observation surface (per-membership event filter with kind/topic/role/project filters, listening mode, and self-modification control) and the listening mode transition record for audit trail.

**Technical detail:** See [Appendix A.22a](#appendix-a22a).

Per-role defaults:

This specification defines default observation surface settings by role: lead members see the full stream, contributors see role-relevant events, reviewers see review interests, observers see only ambient markers and lifecycle transitions, and dormant members see lifecycle transitions only with a catch-up summary on wake.

**Technical detail:** See [Appendix A.22b](#appendix-a22b).

### 9.1 Listening discipline

Listening (observing ambient without acting) is the default state for present members. Three modes govern how a membership attends to its stream:

This specification defines the three listening modes: passive (observe without acknowledgement, default for observers and dormant members), active (observe and emit lightweight acknowledgement markers, default for companion and pair environments), and deliberative (observe and evaluate each event for response decisions, default for lead and contributor roles).

**Technical detail:** See [Appendix A.23a](#appendix-a23a).

Listening mode is declared in `ObservationSurface.listening_mode` and is per-membership-evolvable. Role-attendance rules (what each role attends to):

This specification defines what each role attends to: leads attend project/milestone/charter events, contributors attend role-relevant peer outputs, reviewers attend proposals and dissent, observers attend lifecycle transitions, hosts/guests attend norm events, and advisors attend critical urgency only.

**Technical detail:** See [Appendix A.23b](#appendix-a23b).

Notification suppression policies:

This specification defines notification suppression policies by availability (dormant, quiet, busy), listening mode, quiet hours, and attention budget status.

**Technical detail:** See [Appendix A.23c](#appendix-a23c).

## 10. Notification routing and response decisions

This code defines the notification routing function that iterates over active members, checks observation surface matches, computes notification decisions, and emits signed routing events.

**Technical detail:** See [Appendix A.24a](#appendix-a24a).

Urgency levels:

This specification defines five urgency levels: critical (safety, user_stop, deadline breach), high (direct address, blocking reviews), medium (project focus events, domain updates), low (ambient markers, peer activity), and background (audit findings, periodic reports).

**Technical detail:** See [Appendix A.24b](#appendix-a24b).

### 10.1 Response decision

Each notified persona's kernel evaluates:

This code defines the response evaluation process: charter compatibility check, availability/energy/focus gating, project obligation pressure, and persona deliberation.

**Technical detail:** See [Appendix A.25a](#appendix-a25a).

Decision outcomes:

This specification defines four response outcomes: respond (mint envelope and act), defer (acknowledge and queue for later with escalation), ignore (irrelevant or charter conflict), and acknowledge only (signal awareness without action).

**Technical detail:** See [Appendix A.25b](#appendix-a25b).

### 10.2 Deferred queue

This schema defines the deferred queue for each persona's membership, including queued items with urgency, deferral reason, and expected response time, plus overflow policies.

**Technical detail:** See [Appendix A.26](#appendix-a26).

Kernel periodically reviews:
- Items past `expected_response_by` re-notified at boosted urgency
- Consistent over-deferring triggers audit (charter mismatch indicator)
- Items in dormant membership summarised on wake

### 10.3 Node-level task-queue admission — where SchedulingPolicy plugs in (ADR-0069/ADR-0081)

Notification routing (§10) and the deferred queue (§10.2) govern *attention*; the **ordering of admitted work** on a node's task queue is governed by the node's `SchedulingPolicy` ([`03_TASKS.md §4.6`](03_TASKS.md#46-owner-prioritized-scheduling--schedulingpolicy), `scheduling-policy/1`). The plug-in point is here: the policy's ordering function (priority weight, urgency/deadline escalation, ageing, and the optional [`03_TASKS.md §4.6a`](03_TASKS.md#46a-goal-arbitration-preference-vector--an-admissible-schedulingpolicy-input-adr-0076) preference-vector term) is applied at the node's `task_intake` admission gate over this section's deferred queue and the §7 attention budget, and is re-applied when a deferred item re-notifies at boosted urgency. The floor and the INV-7 hard gate are never reordered around — §4.6's invariants apply verbatim; this section only names the substrate surfaces the policy orders. (Cross-ref both ways: §4.6 declares the policy *over* "the existing notification deferred queue and attention budget (`05_ENVIRONMENT §10`)"; this subsection is that queue's admission point.)

## 11. ProactiveIntent

A persona may initiate action without notification:

This schema defines a proactive intent: a persona's self-initiated proposal to act without being notified, including what they propose, what triggered it, charter justification, and estimated costs.

**Technical detail:** See [Appendix A.27](#appendix-a27).

### 11.1 ProactiveIntent evaluation

This code defines the seven-gate evaluation for proactive intents: safety check, charter alignment, observation surface verification, rate limit, energy budget, and attention impact threshold.

**Technical detail:** See [Appendix A.28](#appendix-a28).

### 11.2 ProactiveRateLimits

This schema defines proactive rate limits: per-persona per-hour and per-day caps, environment-wide cap, cooldown after safety refusal, and quiet hours configuration.

**Technical detail:** See [Appendix A.29](#appendix-a29).

Exceeding limits emits `PROACTIVE_RATE_LIMIT_HIT`; further intents refused until reset.

### 11.3 Quiet hours — full spec

These schemas define quiet periods (scope, time range, timezone, days, suppression policies, override rules) and override rules (conditions like critical urgency or operator pin, with actions like escalate, wake dormant, deliver immediate, or queue until open).

**Technical detail:** See [Appendix A.30a](#appendix-a30a).

Resolution order when both env and persona quiet periods are active:

This specification defines the priority order when both environment and persona quiet periods are active: operator pin wins, then critical urgency, then most-restrictive union, then user explicit call, then obligation deadline breach, then default queue.

**Technical detail:** See [Appendix A.30b](#appendix-a30b).

Urgency escalation: an item queued during quiet hours that crosses an `expected_response_by` deadline auto-escalates to `critical` and re-evaluates against override rules.

### 11.4 Cross-environment notification routing

When an event in env_A is relevant to a member also present in env_B (typically a shared project member), the kernel emits a `cross_env_event_link` into env_B's ambient stream rather than duplicating the full event.

This specification defines how events in one environment are linked to subscribers in another environment via cross_env_event_link records, with consent checks, role mapping, and privacy invariants.

**Technical detail:** See [Appendix A.31](#appendix-a31).

Privacy invariant: cross-env link reveals only the link payload, not source-env private context. Subscribers without source-env membership see the link with `source_context_redacted=True`.

### 11.5 Proactive boundaries

Proactive contribution is bounded by seven enumerated boundaries beyond raw rate limits:

This specification enumerates the seven boundaries that every proactive intent must pass: persona charter, environment charter, user boundaries, operator policy, observation surface verification, quiet hours, and attention impact threshold.

**Technical detail:** See [Appendix A.32](#appendix-a32).

A proactive intent MUST pass all seven before envelope minting proceeds. Failures emit signed `PROACTIVE_REFUSED` with reason; persona's `defer_count` tracks behavioural pattern.

### 11.6 CrossEnvProactiveOffer — voluntary help across environment boundaries

ProactiveIntent (§11) is scoped to a single environment: a persona observes events in its own env's ambient stream and acts within that env. Cross-env notification routing (§11.4) links events across envs, but only for personas who already share membership. A persona in env_A who notices — via PersonaCard discovery (`02_PERSONA §3.4`), federation gossip (`09_PROTOCOLS §3B`), or the user mentioning another persona's work — that a persona in env_B could benefit from their expertise has no substrate-shape mechanism to offer help without first joining env_B.

`CrossEnvProactiveOffer` is a lightweight, consent-gated mechanism for a persona in one env to offer a specific contribution to another env's members without requiring full membership admission.

This schema defines a cross-environment proactive offer: who is offering, who they are offering to help, what they are offering (kind, description, skills, estimated effort), how they discovered the need, the consent flow lifecycle, and guest presence creation on acceptance.

**Technical detail:** See [Appendix A.33](#appendix-a33).

**Admission rule.**

This specification details the five-step admission process for cross-environment offers: offering persona gates (charter, energy, rate limit, availability), target environment gates (operator policy, charter, persona boundaries), reputation gate, delivery mechanics, and target response decision.

**Technical detail:** See [Appendix A.34a](#appendix-a34a).

**Guest presence on acceptance.**

Acceptance does NOT create a full `EnvironmentMembership` (§5). Instead, it creates a `GuestPresence`: a time-bounded, scope-limited presence record that grants the offering persona:

This specification defines the limited access granted to a guest: scoped read access to offer-relevant event families, scoped write access to specific tasks/artifacts, no access to charter internals or other members' personal state, and a time bound of 72 hours (renewable to 30 days).

**Technical detail:** See [Appendix A.34b](#appendix-a34b).

This schema defines the guest presence record created when an offer is accepted, including scoped read/write permissions, expiration, renewal limits, state lifecycle, and optional promotion to full membership.

**Technical detail:** See [Appendix A.34c](#appendix-a34c).

**Composition with ProactiveIntent (§11).** A `CrossEnvProactiveOffer` is a *cross-env analogue* of ProactiveIntent. The same seven proactive boundaries (§11.5) apply to the offering persona's side; the target env's charter + operator policy govern the receiving side. The offer itself is the boundary-crossing mechanism; the guest presence is the scoped execution context.

**Composition with A2A federation (09_PROTOCOLS §3).** For cross-kernel offers, the offer travels via A2A; both kernels sign the offer envelope. The offering persona's PersonaCard is verified by the target kernel before delivery. GuestPresence for cross-kernel offers additionally requires the offering kernel's `body_attestation` (02_PERSONA §3.5) to be fresh.

**Composition with §11.4 cross-env notification routing.** §11.4 links events for *shared members*; §11.6 enables *non-shared* personas to offer help. After a GuestPresence is created, the guest's scoped events flow through §11.4's machinery (cross_env_event_link) back to the guest's home env for lineage continuity.

**Why guest presence, not full membership.** Full membership (§5) carries obligations, attention budget allocation, role assignment, and indefinite presence. A one-off skill contribution doesn't warrant that overhead. GuestPresence is the minimal scope that allows the contribution while preserving the target env's membership integrity.

**Honest limits.**

1. **Guest scope is approximate.** The `scope_read_event_kinds` filter may over- or under-include relevant events; the accepting persona's judgement (which events to share context on) supplements the filter.
2. **Anti-spam relies on reputation + rate limits.** A determined persona with inflated reputation (mitigated by §3D anti-gaming) could flood cross-env offers. Per-persona, per-target-env rate limit (default: 3 offers per 30 days to the same target env) bounds the worst case.
3. **No cross-env ProactiveIntent for personas with no discoverable card.** Offering requires the offering persona to have `federation_visibility ∈ {tenant, federation, public}` on their PersonaCard (02_PERSONA §3.4). Private personas cannot offer cross-env help — they must join the target env via standard admission.
4. **GuestPresence does not carry ProvenFacts write rights.** Guest contributions become ProvenFacts only through the accepting persona's envelope (the accepting persona cites the guest's input and the verifier cascade evaluates it). This preserves the target env's provenance chain.

**Acceptance tests.** A-CEPO1 (offer admitted when all gates pass; delivered to target env), A-CEPO2 (offer refused when target env operator_policy prohibits inbound offers), A-CEPO3 (offer refused when offering persona's reputation below threshold), A-CEPO4 (GuestPresence created on acceptance; scoped read/write enforced), A-CEPO5 (GuestPresence expires at guest_scope_expires_at; renewal extends up to max_renewals), A-CEPO6 (GuestPresence promotion to full membership via standard §5.1 ceremony), A-CEPO7 (cross-kernel offer requires both kernel signatures + fresh body_attestation), A-CEPO8 (per-persona per-target-env rate limit enforced).

## 11a. Alert — first-class attention primitive

`AmbientEvent` is fine-grained substrate audit data. **Alert** is the first-class attention primitive: something a persona (or user) must notice, with severity, acknowledgement state, escalation policy, and auto-resolve condition. Alerts span env / project / domain scopes.

This schema defines an alert as a stateful attention primitive with scope, title, severity, source event, targets, acknowledgement state, escalation policy, auto-resolve conditions, and lifecycle.

**Technical detail:** See [Appendix A.35a](#appendix-a35a).

**Distinct from AmbientEvent:**
- AmbientEvent: append-only audit-trail fine-grained signal. No state. No acknowledgement.
- Alert: stateful entity with acknowledgement, escalation, resolution. May reference a source AmbientEvent.

**Distinct from Obligation (project-tier):**
- Obligation: an inter-persona commitment with status tracking.
- Alert: a notification requiring attention; may *cause* an Obligation but is not one.

**Common sources:**

This specification lists common alert sources that emerge per domain: overdue commitments, budget thresholds, stale attestations, unresponsive external agents, physical asset state changes, weather impact, inspector arrival, and clinical critical values.

**Technical detail:** See [Appendix A.35b](#appendix-a35b).

Source kinds are emergent per domain; substrate ships only the Alert structure.

## 11b. ScheduledTrigger — kernel-driven recurring events

Environments may have scheduled triggers — kernel-managed events that fire at declared times into the ambient stream. Triggers are used for: daily standups, weekly check-ins, monthly digest emission, lease-renewal reminders, calibration-due reminders, presence wake-up calls, project-phase advancement deadlines. v1.0 specifies the schema.

This schema defines a scheduled trigger: an environment-scoped, kernel-managed recurring event with schedule kinds (one-shot, interval, cron, calendar), emitted event kind and payload, dormant-member wake semantics, lifecycle state, and target scoping by role or persona.

**Technical detail:** See [Appendix A.36](#appendix-a36).

**Firing semantics.** At `next_fire_at`, the kernel appends an `ambient_event` to the env's stream with `kind = emitted_event_kind` and `payload = emitted_event_payload`. The event signs as `scheduled_trigger_fired` in EnvironmentLineage (per `§13`). Notification routing (`§10`) proceeds as for any ambient event; the `wakes_dormant_members` flag overrides the normal dormancy suppression when True.

**Recurrence advancement.** After firing:
- `one_shot` → state transitions to `completed`
- `interval` → `next_fire_at += interval`
- `cron` → `next_fire_at = next_cron_match(cron_expr, now)`
- `calendar` → `next_fire_at = next_calendar_match(calendar_spec, now)`

If `fires_count >= max_fires` (when max_fires is set), state → `completed`.

**Pause / resume / cancel.** Operator (or env-lead persona) may pause via signed `SCHEDULED_TRIGGER_PAUSED` event; while paused, next_fire_at is preserved but no fires emit. Resume restores firing. Cancel is terminal; once cancelled, the trigger is preserved in lineage but never fires again.

**Composition with safety floor.** The trigger's emitted event passes the 8-source safety floor at fire time, exactly as any ambient event would. If the trigger would emit content blocked by floor (e.g., a daily-standup template that references a domain whose hazard axes have escalated), the fire is logged as `scheduled_trigger_floor_refusal` and the trigger optionally auto-pauses (operator policy).

**Wake heuristics.** A trigger with `wakes_dormant_members = True` overrides the normal `availability="dormant"` suppression for the target persona(s). The wake is signed as `dormant_wake_via_scheduled_trigger` in env lineage; the woken persona's `presence_state.attention_level` is bumped to `max(current, 0.5)` for the response window (default 1 hour) so the wake has actual effect. This closes the v1.0 gap "dormant members can wake via explicit action" by naming the explicit action: a `wakes_dormant_members=True` ScheduledTrigger event, or a Critical-urgency Alert (`§11a`), or a member-initiated `WAKE_REQUEST` event (`§5.2 below`).

**Honest limit.** ScheduledTrigger does not model wall-clock drift across kernels in federated envs. In joined envs (`09_PROTOCOLS §3C`), the host kernel's clock authoritatively fires; peer kernels observe the fired event in the merged stream. Cross-kernel time-skew handling is out-of-scope for v1.0.

## 12. EnvironmentProvenFacts

Per-environment CRDT G-set:

This schema defines an environment proven fact in a CRDT G-set: a signed statement with evidence references, fact kind (convention, policy, infrastructure state, shared understanding, historical fact), and cross-environment transferability.

**Technical detail:** See [Appendix A.37](#appendix-a37).

Example facts:
- "Acme office uses PT timezone for scheduling" (convention)
- "We have an open Volt project as of 2026-05" (historical)
- "MCP server endpoint is mcp://acme/lab/ngspice" (infrastructure)
- "Kitchen counter incident — bring it up with caution" (in `friends` env)

## 12a. EnvDisagreement — lightweight env-tier disagreement recording

`Disagreement` in 04_PROJECT §10 is project-tier (requires a project_workspace env, positions list, resolution path, blocking_artifacts). Many envs that are NOT project-typed still need to record disagreement — companion envs ("we disagree about how to spend time"), pair envs ("we disagree about the conversation rhythm"), lab envs without a hosted project. `EnvDisagreement` is the lightweight env-scoped analogue.

These schemas define environment-level disagreements (lighter than project-tier): a disagreement with subject, positions from members, lifecycle states (including agree-to-disagree), visibility settings, and the associated position records.

**Technical detail:** See [Appendix A.38](#appendix-a38).

**Key differences from project-tier Disagreement (04_PROJECT §10):**
- No `blocking_artifacts` / `blocking_obligations` (env-tier disagreements rarely block artifacts; they're about relational / coordination state)
- No required resolution path; `set_aside` ("agree to disagree") is admissible
- Visibility may be more restricted (companion / pair envs often want member-only)
- Schema is significantly smaller

**Composition with PersonaPersonaBoundary (`02_PERSONA §11.6`).** When an EnvDisagreement reaches an unresolvable state and one party files a PersonaPersonaBoundary against the other, the kernel signs a `disagreement_to_boundary_transition` event linking the two. This makes the social progression auditable without conflating the two primitives.

**Composition with project_workspace.** A `project_workspace` env may use *either* EnvDisagreement (for relational disagreements that don't block artifacts) *or* `Disagreement` (04_PROJECT §10; for project-tier disagreements that DO block artifacts). They're complementary, not redundant.

**Honest limit.** EnvDisagreement does not provide a formal mediator. Resolution is by the disagreeing parties (with optional operator escalation). For high-stakes disagreements the project-tier `Disagreement` schema with its richer resolution path is the correct primitive.

## 12b. EnvSelfProposalRequest — federated env discovery and self-admission

Prior versions admission paths assume `ENV_INVITATION` (operator/lead initiated) or `PROJECT_HOSTING_LINK` (auto-admission via project membership). For federated personas who discover a public or federation-tier env via gossip and wish to *propose themselves* for admission — without an inviter — v1.0 adds `EnvSelfProposalRequest`. This is the env-layer analogue of `04_PROJECT §14`'s project self-proposal.

This schema defines a self-proposal request for a persona to propose joining a discoverable environment, including desired role, motivation, expected attention, evidence of fit (skills, relationships, reputation), and lifecycle states.

**Technical detail:** See [Appendix A.39a](#appendix-a39a).

**Eligibility rules:**

This specification defines six eligibility rules for self-proposals: environment visibility tier requirements, persona signature, charter compatibility check, operator policy gate, 90-day cooldown after decline, and federation peer requirements for cross-kernel proposals.

**Technical detail:** See [Appendix A.39b](#appendix-a39b).

**Decision flow:**

This specification defines the five-step decision flow for self-proposals: draft, submit to review queue, lead/operator review with charter and reputation checks, decision (accept/decline/auto-decline on timeout), and outcome observation by the proposer.

**Technical detail:** See [Appendix A.39c](#appendix-a39c).

**Honest limit.** Cross-kernel self-proposal depends on accurate gossip-derived reputation (`09_PROTOCOLS §3B`). A persona from a low-reputation kernel may be declined repeatedly; the substrate honestly degrades trust rather than admitting on weak signals. Operators bridging trust between kernels via explicit peer agreements is the established workaround.

## 12c. EnvFormationProposal — persona-initiated env creation

Prior versions lacked a first-class primitive for a persona to *form a new environment*. Existing flows only covered (a) admission to a pre-existing env via `ENV_INVITATION` / `ENV_RECRUIT_PROPOSAL` (`§5.1`), (b) joined env cross-kernel formation via `PROPOSE_JOINED_ENV` (`09_PROTOCOLS §3C.1`), and (c) self-admission to an existing env via `EnvSelfProposalRequest` (`§12b`). None of these capture the common case: **"I want to start a new Lab / Pair / project_workspace env to investigate topic T, with recruits B, C, D, under charter Δ, with these initial roles and attention allocations."** `EnvFormationProposal` is that primitive.

**Recruitment-gap fallback (v1.1).** When cohort assembly finds no admissible recruit (locally or via federation) and no existing persona is close enough to fork, a proposer whose `cohort_assembly.may_author_seeds = true` MAY escalate to **Persona Genesis** — authoring a new niche-distinct persona to fill the gap — instead of abandoning formation. Genesis is recruitment-exhausted-first, niche-bounded, and gated by a `persona_genesis` `ReplicationBound`; the newborn enters at **peripheral community standing** (§5.4) whose listening mode (`§9`) and attention allocation (`§7`) ramp up under mentorship as wall-clock age rises and standing is conferred. See [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md).

It composes atomically with the existing machinery — `cohort_assembly` capability (`02_PERSONA §3`), `PersonaPersonaBoundary` (`02_PERSONA §11.6`), `PersonaRelationshipEdge` accelerator (`02_PERSONA §11.4`), `ReputationSummary` gating (`09_PROTOCOLS §3D`), the consent flow (`09_PROTOCOLS §3C.4`), and the env lifecycle FSM (`§4`). It does **not** replace any of them; it gives the persona a single signed object to draft, submit, negotiate, and consummate.

### 12c.1 Schema — EnvFormationProposal

These schemas define the environment formation proposal and its related objects: the main proposal (environment type, charter draft, cohort invites, consent terms, time horizon, lifecycle), CohortInvite (per-recruit role and attention allocation), ConsentTerms (what recruits can see), CohortConsentResponse (accept/decline/counter-propose/refuse), CounterProposal (modifications to role, allocation, listening mode, charter), and CharterAmendment.

**Technical detail:** See [Appendix A.40](#appendix-a40).

### 12c.2 The end-to-end flow

This specification details the seven-step environment formation flow: draft with kernel-enforced checks, submit with consent dispatch, per-recruit consent gates (boundary, reputation, attention budget, consent flow, relationship-edge accelerator), counter-proposal negotiation, atomicity check (all-or-nothing, minimum quorum, or best effort), instantiation with charter resolution, and post-formation kickoff.

**Technical detail:** See [Appendix A.41](#appendix-a41).

### 12c.3 Composition with v1.0 unification (project ↔ env)

For `proposed_env_type_kind = "project_workspace"`, this single proposal forms a Project (since Project IS a project_workspace env per `04_PROJECT §0` and `§1.1` above):

- ProjectMember entries = EnvironmentMembership entries (same record per the unification)
- Initial OpenProblem / Milestone may seed from `proposed_initial_phase_kind`
- The legacy two-step "create project then create env then recruit" flow collapses into this single signed proposal
- Replaces the separate `PROJECT_INVITATION` flow for env-bound projects (PROJECT_INVITATION still valid for inviting to an *existing* project)

For non-project env types (lab, team, pair, companion, etc.):
- Plain env formation; no project-specific item catalogue
- Members may later spawn a project_workspace env *within* the lab via a separate EnvFormationProposal (sub-env via fork mechanism — see `parent_environment_id` in §2)

### 12c.4 Cross-kernel scope (cross-node membership)

For `recruit_kernel_id ≠ proposing_kernel_id` (the recruit is on a different **node**), both shapes are normative in the global object space (ADR-0067/0068):
- **Joined environment** per `09_PROTOCOLS §3C` (host kernel = proposer's kernel; peer kernels stream the recruit's events through). The EnvFormationProposal is the *unified entry point*; the joined-env protocol handles the cross-node mechanics. This remains the model when the env needs a single authoritative event log.
- **Local-env-with-remote-member**: the remote recruit's body runs on their node, joining as a member of an env hosted on the proposer's node. The recruit is referenced by global handle (`01_KERNEL §4.4`), admitted subject to its `AccessPolicy` + a UCAN capability (`09_PROTOCOLS §3F`), with cross-node attention/budget coordinated under each node's own gates (most-restrictive-wins, `§3C.3`). Mid-task reachability follows `09_PROTOCOLS §3H` (a remote member's node may sleep; presence degrades to `dormant`, the env does not stall on it).

The proposal's `proposing_kernel_id` and `recruit_kernel_id` fields make the cross-node-ness explicit at draft time so the kernel selects the appropriate mechanism; neither is refused. (The former `cross_kernel_local_env_not_supported_v1_0` refusal is retired — superseded by the global-reference membership model.)

### 12c.4a MultiPrincipalAttestationQuorum — multi-principal ratification

When the env being formed has a `PrincipalAttribution` (`01_KERNEL §2.4.3`) whose `multi_principal_attribution_enabled = True`, charter ratification cannot be cleared by a single operator's signature. The proposer ships a `MultiPrincipalAttestationQuorum` envelope alongside the `EnvFormationProposal`; the kernel admits charter ratification iff the envelope clears.

This schema defines the multi-principal attestation quorum: a collection of co-signatures from multiple principals (operators) required to ratify certain events, with quorum policies (unanimous, weighted majority, or weighted threshold) and degraded-path handling for unreachable principals.

**Technical detail:** See [Appendix A.42a](#appendix-a42a).

**Admission rule.**

This specification defines the quorum mechanics: draft verification, per-principal cosign collection with key verification, quorum policy evaluation, clearance on policy satisfaction, and the degraded-path procedure for unreachable principals (cool-down, external attestation, signed acknowledgement).

**Technical detail:** See [Appendix A.42b](#appendix-a42b).

**Composition with the gated events.**

| Event kind | Gating section | Effect when multi-principal enabled |
|---|---|---|
| `env_charter_ratified` | §5.1 admission ceremony + §12c | EnvFormationProposal stays at `consent_complete` until quorum clears; cannot transition to `instantiated`. |
| `env_rule_ratified` | §2.2b + §12c + `01_KERNEL §2.4` C2 gate | A `safety_critical` EnvironmentRule (env-rule/1) cannot reach `accepted`, and its env cannot transition to `instantiated`, until the operator co-sign / quorum clears; degraded gate composes per-principal as in §2.4.3. |
| `project_completed` | `04_PROJECT §4.1` | Completion ceremony step 8 (`status → completed` signed event) blocks until quorum clears. |
| `safety_extension_approved` | `06_DOMAIN §8` + `01_KERNEL §2.4` C2 gate | Operator co-sign step requires quorum clear; degraded gate composes per-principal as in §2.4.3. |
| `domain_promotion` | `06_DOMAIN §3` PromotionPolicy | C2 gate at AUTHORITATIVE / STANDARDISED transitions requires quorum clear when the domain's host env carries multi-principal attribution. |

**Honest limits.**

1. **Operator policy holds the quorum_policy choice.** `unanimous` is the substrate default; operators selecting `weighted_majority` or `weighted_threshold` reduce protection in exchange for liveness. The substrate enforces the simple-majority floor but does not adjudicate the trade-off.
2. **Degraded-path attestation extends the §2.4 trust model.** A quorum cleared via `cleared_under_degraded_path = True` should be treated by downstream consumers (auditors, federated peers) at the same evidentiary level as a §2.4 principal-collapse degraded gate clearance — not at the same level as a synchronous all-principal cosign.
3. **Cross-quorum composition is not transitive.** A `domain_promotion` quorum clearing under degraded path does NOT auto-apply to a subsequent `project_completed` quorum on the same project; each gated event runs its own quorum and its own degraded path if applicable.

### 12c.5 Honest limits

1. **Counter-counter-proposal depth = 1.** Beyond one round of negotiation, the recruit accepts-as-is or declines. Deeper haggling would need a separate Negotiation schema (out of scope).
2. **Charter co-authoring fidelity.** When `charter_authorship_mode = co_authored_required`, the final charter is signed by all initial members, but the *internal negotiation mechanics* (whose amendments win, conflict resolution) are implicit. Default: proposer holds tie-break; explicit `Disagreement` (project-tier, `04_PROJECT §10`) used if amendments materially diverge.
3. **External agents not recruitable via this primitive.** Cohort assembly is persona-only. ExternalAgents (`04_PROJECT §26a.1`) — contractors, inspectors, lab techs — admit through their own path. The two compose at the project_workspace level: the env forms via EnvFormationProposal (personas); ExternalAgents admit afterward.
4. **AttentionBudget pre-check is a soft refusal.** If a recruit's AttentionBudget would exceed 1.1 by accepting, their kernel MAY decline OR counter-propose a lower allocation. The substrate does not auto-rebalance; the recruit MUST do the negotiation.
5. **No proposal-chaining.** A proposer cannot conditionally form env A *only if* env B forms first. Each EnvFormationProposal is independent. Chained workflows are operator policy.

### 12c.6 Acceptance tests

See `11_ACCEPTANCE_TESTS §9c — A-EF-*` for the full ~15-test family covering: draft constraints (a-g per STEP 1); consent flow integration with boundary + reputation + attention budget; counter-proposal negotiation depth; atomicity verdicts (all_or_nothing / min_quorum / best_effort); failure paths (atomicity, safety floor); cross-kernel joined-env path; relationship-edge accelerator; project_workspace formation with initial phase seed; charter authorship modes; cohort assembly capability gating.

## 13. EnvironmentLineage (J9)

This specification enumerates all EnvironmentLineage event kinds: environment lifecycle events, membership events, convention events, wake events, disagreement events, self-proposal events, formation proposal events, boundary events, and project-specific events for project_workspace-typed environments.

**Technical detail:** See [Appendix A.43](#appendix-a43).

Append-only and signed (J9). Reconstruction via replay. The `project_*` event family is a documentation alias for the subset of EnvironmentLineage events fired on `project_workspace`-typed envs (see 04_PROJECT §0 + §15).

## 14. EnvironmentContext in PersonaEnvelope

This schema defines the environment context rendered into each persona's envelope: environment identity and type, charter hash, membership details, presence state, observation surface, relevant conventions, recent ambient summary, proven facts, hosted projects, other present members, and remaining attention/energy budgets.

**Technical detail:** See [Appendix A.44](#appendix-a44).

Rendered into envelope's system prompt as ENVIRONMENT CONTEXT block (cacheable=False; dynamic).

## 15. Conversation thread within ambient

For multi-turn engagement:

This schema defines a conversation thread within the ambient stream: participants, timing, message count, state (active/paused/concluded), and optional task/project references.

**Technical detail:** See [Appendix A.45](#appendix-a45).

Conversation threads:
- Live in ambient streams
- Span multiple kernel envelopes (re-mint or continue per turn)
- Trigger task classification on each turn (task may evolve)
- Conclude explicitly or by timeout

## 16. Forking and morphing

### 16.1 Environment fork

This specification defines three fork inheritance policies: inherit_all (full members, history, conventions), inherit_summary (conventions plus signed summary, clean ambient), and inherit_seed (charter and type only, clean otherwise).

**Technical detail:** See [Appendix A.46a](#appendix-a46a).

### 16.2 Environment morph

Charter or type changes substantially:
- **Charter version bump** (continue same instance)
- **Morph into new env** if structural (different blueprint, different members; new env_id; parent reference)
- **EnvironmentRule amendment** (continue same instance): a signed `CharterAmendment` MAY add, replace, or revoke an [`EnvironmentRule`](#22b-environmentrule-env-rule1) (`env-rule/1`, §2.2b). Adding or replacing a `safety_critical` rule routes through the C2 / quorum gate (`env_rule_ratified`, §12c.4a) before the rule reaches `accepted`; revoking emits `env_rule_revoked`. A charter amendment that would remove or weaken a `cascade_locked` rule inherited from a parent env (§2.2a) MUST be refused (`env_child_charter_amendment_refused (safety_violation)`).

Threshold: charter-classifier judgment + operator confirmation.

## 17. Multi-kernel federated environments

v1.0 supports federated env presence across kernels:

This specification defines the federation scope progression: single-kernel single-env (primary), single-kernel multi-env (supported), multi-kernel joined environments (federated presence), multi-kernel cross-env projects, and public-tier hub-published environments.

**Technical detail:** See [Appendix A.47](#appendix-a47).

Multi-kernel joined env: host kernel owns EnvironmentLineage; peer kernels sign their members' contributions; CRDT merges keep state consistent.

**Federated presence / activity resolution.** The per-env, single-kernel `PresenceState` (§6) and ambient stream (§8) cannot, on their own, answer an authorised peer elsewhere asking "where is persona X, and what is it doing right now?". PersonaOS adds an **opt-in, consent-gated** projection of `PresenceState` (availability, current focus kind, last-active round) into the federated telemetry feed ([`09_PROTOCOLS.md §4.1`](09_PROTOCOLS.md#41-federated-consent-gated-telemetry-feed)), advertised by a `TelemetryCard` and gated by `AccessPolicy` + reputation ([`09_PROTOCOLS.md §3G.3`](09_PROTOCOLS.md#3g3-accesspolicy--one-access-level-model-across-all-content-types), [`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md#3d-reputation-and-anti-goodhart)). **Default off**; focus *content* is never exposed below a consented tier (only focus *kind* + status). The env itself, and its artifacts, project a `DiscoverableRecord` / `ArtifactCard` over the same internet (DHT) and intranet (mDNS) discovery planes ([`09_PROTOCOLS.md §3G`](09_PROTOCOLS.md#3g-discovery-access-and-hybrid-distribution)).

## 18. Performance and cost

This specification defines performance targets: environment creation under 1 second, member admission under 200ms, ambient event append under 10ms, stream retrieval under 50-200ms depending on tier, notification routing under 30ms, and storage estimates from 1-10MB (solo/pair) to 1-10GB (community).

**Technical detail:** See [Appendix A.48](#appendix-a48).

## 19. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations).

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-ENV-1 | EnvironmentInstance authoring is operator work — blueprint selection, charter, admission, surface templates. v1.0 organises but does not reduce per-env effort. | Low | High | EnvironmentBlueprint templates per type; EnvFormationProposal (`§12c`) for persona-initiated formation; documentation. | v1.0 (templates); v1.1 (blueprint marketplace). |
| R-ENV-2 | Ambient stream storage cost at multi-year scale. Tier transitions help but long-tail costs grow. | Medium | High | HOT / WARM / COLD / ARCHIVE tiers; per-env retention policy; lineage snapshot for archival. | v1.0 (tiers); v1.1 (policy tuning). |
| R-ENV-3 | Multi-env presence coordination cost. N active presences = N streams + N attention allocations. | Medium | Medium | AttentionBudget per-member caps; ObservationSurface filters; presence dormancy / archive transitions. | v1.0 (budgets); v1.1 (cross-env digest). |
| R-ENV-4 | Conversation-thread state inference is heuristic. "Conversation over" vs "paused" misclassification possible. | Low | High | Operator-tunable thresholds; explicit close events override heuristic; user surface for state correction. | v1.0 (heuristic); v1.2 (state classifier). |
| R-ENV-5 | Cross-env project consolidated-view UX. Members in multi-env projects see notifications across envs; consolidation is operator concern. | Low | Medium | Per-project digest stream; project-tagged observation surface; A-PJ20 acceptance test. | v1.1 (project digest). |
| R-ENV-6 | Quiet hours and norms tuning does not scale automatically. 1000s of envs need per-env operator tuning. | Low | Medium | Norm templates per env type; learning surface from member feedback. | v1.1 (norm-templates); v1.2 (norm learning). |
| R-ENV-7 | Federated joined-env consistency at partition. Multi-kernel CRDT requires careful partition handling. | High | Low | G-set semantics (last-writer-wins where structurally safe); `CONFLICT_PARKED` state for unsafe conflicts; A-CKDM acceptance tests; co-owned mode requires both kernels online. | v1.0 (basic); v1.1 (advanced partition recovery). |
| R-ENV-8 | EnvFormationProposal can be abused to create spam envs. | Medium | Low | Per-persona rate limit; consent flow from invitees; PersonaPersonaBoundary checks; reputation impact on refused proposals. | v1.0 (rate limit); v1.1 (reputation-weighted). |
| R-ENV-9 | User-address wake (§5.2 Wake Path 6) could disrupt dormancy rest cycles if a user repeatedly addresses the same dormant persona. | Low | Medium | Per-user per-persona rate limit (≤ 5 wakes per 24h); `dormant_user_address_rate_limited` event queues further wakes; user advisory on prolonged dormancy. | (baseline). |
| R-ENV-10 | CrossEnvProactiveOffer (§11.6) spam: personas flooding cross-env offers to envs they don't belong to. | Medium | Low | Per-persona per-target-env rate limit (3 offers / 30 days); reputation gate; target env operator_policy may refuse inbound offers entirely; declined offers degrade offering persona's reputation. | (baseline). |
| R-ENV-11 | Executable `EnvironmentRule` (env-rule/1, §2.2b) as a safety-floor-bypass vector: a malicious `rule_kind=code` rule could attempt to weaken effective enforcement or exfiltrate. | Critical | Low | Rules run in the existing sandbox (OWASP filter + resource caps, `01_KERNEL §6`); rules ride UNDER source 8 and may only ADD refusals, never relax sources 1-7; `safety_critical` rules are operator-gated (C2); `cascade_locked` parent rules are immutable by children; A-ER2/A-ER5/A-ER6. Cross-document: also `00_VISION §11`. | v1.1 (sandbox + source-8 ride). |
| R-ENV-12 | `EnvironmentRule` evaluation latency at admission points adds verifier-stage cost to the ≤400 ms floor budget (`01_KERNEL §2.3`). | Medium | Medium | Rule evaluation is budgeted per INV-7; deterministic `before_action` rules are cached; operators may cap per-env rule count; heavy `code` rules SHOULD run `after_action` where admissible. | v1.1 (budget + cache). |

## 19a. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-ENV-1 | Conversation-thread state inference (R-ENV-4): heuristic, learned classifier, or explicit user signal? v1.0 ships heuristic; user-feedback surface is v1.1; full classifier is v1.2+. | Persona UX | v1.2 state classifier. |
| OQ-ENV-2 | EnvFormationProposal reputation weighting: a persona with many accepted proposals should have higher acceptance probability for new proposals — what's the formula? | Reputation WG | v1.1 reputation. |
| OQ-ENV-3 | Joined-env federation CRDT partition recovery: when the network heals after partition, which conflicts auto-resolve vs require human review? Currently `CONFLICT_PARKED` defers all to operator. | Federation WG | v1.1 partition recovery policy. |
| OQ-ENV-4 | Norm templates per env type (R-ENV-6): authored library, or learnt from member feedback over time? | Environment authors | v1.1 / v1.2. |
| OQ-ENV-5 | Per-member AttentionBudget defaults: by wall-clock age / community standing, by env type, or by relationship depth? | Persona authors | v1.1 calibration. |
| OQ-ENV-6 | ScheduledTrigger composition with quiet hours: should triggers respect quiet hours by default, or burst-through? Per-trigger override? | Persona UX | v1.1 trigger policy. |
| OQ-ENV-7 | Alert auto-resolve conditions (`§11a`): what's the canonical set of resolve-condition primitives? Explicit ack, time-based, signal-disappeared, all three? | Persona UX | v1.1 alert taxonomy. |
| OQ-ENV-8 | EnvironmentRule (§2.2b) holdout validation: should an executable rule pass a holdout-trace gate (as InferredVerifierRecipe does, `06_DOMAIN §7.1`) before reaching `accepted`, and what false-positive ceiling applies? | Safety floor WG | v1.1 rule-validation gate. |
| OQ-ENV-9 | Cascade conflict under multi-parent composition: when (future) multi-parent compositions supply two `cascade_locked` rules that conflict, what is the resolution? v1.0/v1.1 composition is single-parent. | Federation WG | v1.2 multi-parent cascade. |

## 20. Acceptance tests

```text
A-EN1   EnvironmentInstance proposed → active → accumulates events
        across sessions; status reflects activity.
A-EN2   Members signed; non-members cannot read ambient beyond surface.
A-EN3   EnvironmentLineage append-only and replayable; state
        reconstructible at any T.
A-EN4   Status transitions active → idle → dormant → archived per
        thresholds; signed events.
A-EN5   Environment fork inherits per declared policy; parent stream
        unchanged.
A-EN6   Multi-env persona presence: env_A events isolated from env_B.
A-EN7   EnvironmentProvenFacts G-set: cross-env retrieval with
        transferable=True works.
A-EN8   environment_charter_hash part of safety_snapshot_id.
A-EN9   Ambient retention tier transitions signed.
A-EN10  Operator max_member_count cap enforced.
A-EN11  Scheduled triggers emit signed events into ambient stream.
A-EN12  Environment fork preserves parent stream; child independent.

A-PR1   EnvironmentMembership signed by both kernels; departure
        preserves history.
A-PR2   PresenceState attention decays per env-type half-life;
        bumps on notifications, actions, triggers.
A-PR3   Availability auto-transitions per attention thresholds;
        persona + operator overrides supersede.
A-PR4   AttentionBudget over-threshold emits ATTENTION_OVER_BUDGET;
        new admissions refused.
A-PR5   Energy decay per response/proactive; low energy causes
        refusal of non-charter-critical.
A-PR6   Multi-env presence: per-env focus independent.
A-PR7   Role change emits signed ENV_MEMBER_ROLE_CHANGED.
A-PR8   Mood + Presence compose per 02_PERSONA.md §6 formula.
A-PR9   PROJECT_HOSTING_LINK auto-admission of project members to
        hosting env.
A-PR10  Ephemeral encounter mode: single-shot creates temp Solo env;
        archived after session.
A-PR11  env_context in envelope includes presence, others present,
        conventions, recent ambient, env facts.
A-PR12  Operator may pin presence; signed override appended to lineage.

A-RB1   Ambient event triggers notifications per observation surface;
        signed NOTIFICATION_ROUTED.
A-RB2   Response decision: respond/defer/ignore/acknowledge_only;
        logged with reasoning.
A-RB3   Deferred queue: re-notify at interval; expired deferrals
        escalate or route to another member.
A-RB4   ProactiveIntent: safety + charter + env-charter + surface +
        rate-limit clearance.
A-RB5   Listening modes (passive/active/deliberative) per surface;
        observed events accumulate in episodic memory.
A-RB6   Conversation thread multi-turn context without re-mint per turn.
A-RB7   Cross-env notification: env_A event surfaces in env_B as
        cross_env_event_link.
A-RB8   Quiet hours suppress proactive + low-urgency.
A-RB9   Critical-urgency wakes dormant; non-critical does not
        (EXCEPT direct user address — Wake Path 6, §5.2).
A-RB10  Deliberation latency ≤ 200 ms p95 per notification.
A-RB11  Audit: persona over-deferring → ENV_DEFER_OVERLOAD finding.
A-RB12  Operator policy may suppress proactive entirely.

A-EN13  EnvironmentCharter schema: composition_order resolved with
        env_charter above persona_charter but below operator_policy;
        hash included in safety_snapshot_id.
A-EN14  EnvironmentBlueprint hot-loadable: register blueprint and
        instantiate env without kernel restart; defaults applied.
A-EN15  Membership ceremonies: admission, departure, role-change
        each emit dual-signed lineage events; replay reconstructs
        roster state at any T.
A-EN16  AttentionBudget API: allocate/spend/recover/borrow each
        emit signed events; borrow auto-reverts at ttl;
        sum-exceeds-refusal-threshold blocks new admissions.
A-EN17  Quiet hours composition: env + persona union resolved with
        operator_pin > critical > most-restrictive; obligation
        deadline breach auto-escalates queued items.

§5.2 Wake Path 6 — direct user address
A-WK6-1  Dormant persona wakes on direct user address;
          dormant_wake_via_user_address event signed with user_id
          and task_fingerprint.
A-WK6-2  Attention bumps to max(current, 0.6) for 2h response
          window; persona proceeds to standard response decision.
A-WK6-3  Per-user per-persona rate limit (≤ 5 / 24h) enforced;
          6th wake queued with dormant_user_address_rate_limited.
A-WK6-4  Long-dormancy advisory emitted when dormancy > 30d AND
          energy < 0.05; wake still proceeds.
A-WK6-5  User boundary that blocks user from persona causes
          dispatcher refusal at routing time, not at wake time.

§11.6 CrossEnvProactiveOffer
A-CEPO1  Offer admitted when all gates pass (charter, energy,
          rate-limit, target-env policy, reputation); delivered
          to target env ambient stream.
A-CEPO2  Offer refused when target env operator_policy prohibits
          inbound offers.
A-CEPO3  Offer refused when offering persona's reputation below
          target env's inbound_offer_reputation_threshold.
A-CEPO4  GuestPresence created on acceptance; scoped read/write
          enforced; guest cannot write ProvenFacts directly.
A-CEPO5  GuestPresence expires at guest_scope_expires_at; renewal
          extends up to max_renewals (default 3).
A-CEPO6  GuestPresence promotion to full EnvironmentMembership
          via standard §5.1 admission ceremony.
A-CEPO7  Cross-kernel offer requires both kernel signatures +
          fresh body_attestation on offering persona.
A-CEPO8  Per-persona per-target-env rate limit (3 offers / 30d)
          enforced; excess offers refused.
```


## Technical Appendix

This appendix contains all formal schemas, dataclass definitions, state machine diagrams, and structured specifications referenced from the main text. Each entry is numbered and cross-referenced from its original section.

<a id="appendix-a1"></a>
### A.1. EnvironmentInstance schema

```python
@dataclass
class EnvironmentInstance:
    schema: str = "env-instance/1"
    
    # IDENTITY
    environment_id: str                   # ULID
    name: str
    description: str
    created_at: datetime
    created_by: str                       # operator/kernel
    
    # TYPE
    type: Literal["solo", "pair", "team", "lab", "debate",
                   "community", "constrained",
                   "project_workspace"]    # v1.0: env dedicated to one
                                          # project; lifecycle-linked.
                                          # See §3 type list and §4
                                          # lifecycle FSM.
    blueprint_id: str | None              # custom blueprint extending type

    # PROJECT BINDING (v1.0: project_workspace type)
    project_bound_to: str | None = None    # project_id when type =
                                          # "project_workspace".  Env
                                          # auto-transitions to dormant
                                          # when bound project completes
                                          # or is abandoned.  Substrate-
                                          # shape (scope binding), not
                                          # domain.
    
    # CHARTER (env-specific)
    charter: list[str]
    charter_version: int
    charter_signed_by: bytes
    env_rules: list[str] = field(          # EnvironmentRule ids (env-rule/1,
        default_factory=list)              #  §2.2b) bound to this env; the
                                           #  active subset (stage=="accepted")
                                           #  is read by the source-8 loop in
                                           #  01_KERNEL §A.3. Additive; version
                                           #  retained per 09_PROTOCOLS §7.13.
    
    # DOMAIN
    default_domain_context_ref: str | None
    
    # MEMBERSHIP
    members: dict[persona_id, EnvironmentMembership]
    operator_admins: list[str]
    max_member_count: int | None
    
    # STATE
    status: Literal["proposed", "active", "idle", "dormant", "archived"]
    last_active_at: datetime
    activity_window: timedelta
    
    # AMBIENT STREAM
    ambient_event_stream_id: str
    ambient_retention_policy: AmbientRetention
    
    # HOSTED PROJECTS
    hosted_projects: list[str]            # project_ids
    hosted_project_history: list[ProjectHostingRecord]
    
    # CONVENTIONS
    conventions: dict[str, NotationConvention]
    
    # OBSERVATION SURFACES (per-role defaults)
    observation_surface_templates: dict[str, ObservationSurfaceTemplate]
    
    # LINEAGE (J9)
    environment_lineage_id: str
    environment_proven_facts_ref: str     # CRDT G-set
    
    # VISIBILITY
    visibility_tier: Literal["private", "tenant", "federation", "public"]
    discoverable: bool
    
    # OPERATIONAL
    operator_policy_id: str
    proactive_rate_limits: ProactiveRateLimits
    budget_envelope: BudgetEnvelope
    
    # SCHEDULED TRIGGERS — see §11b for schema
    scheduled_triggers: list[ScheduledTrigger]
    
    # ALERTS (v1.0 — §11a)
    alerts: list[str]                     # Alert ids scoped to this env
    
    # META
    archived_at: datetime | None
    archived_reason: str | None
    parent_environment_id: str | None     # if composed (§2.2a);
                                          # null for top-level envs
    child_environment_ids: list[str]      # populated when child envs
                                          # are spawned within this env
    composition: EnvironmentComposition | None = None  # v1.1; see §2.2a
    coordination_profile: EnvironmentCoordinationProfile | None = None
                                          # v1.1; see 15_COORDINATION_SHAPES.md §4.4
    signed_by: bytes
```


<a id="appendix-a2"></a>
### A.2. EnvironmentCharter schema

```python
@dataclass
class EnvironmentCharter:
    schema: str = "env-charter/1"          # additive field below; version
                                           # retained per 09_PROTOCOLS §7.13
    env_id: str
    charter_text: list[str]                # env-specific prose norms
    rule_refs: list[str] = field(          # EnvironmentRule ids (env-rule/1,
        default_factory=list)              #  §2.2b) bound at source 8. An
                                           #  empty list == prose-only charter
                                           #  (pre-existing behaviour).
    composition_order: list[Literal[       # precedence top→bottom
        "universal_harm_floor",
        "operator_policy",
        "env_charter",                     # this layer
        "persona_charter",
        "project_charter",
        "user_boundary",
    ]]
    precedence_notes: str                  # rationale for ordering
    version: int
    parent_charter_hash: str | None        # if morphed from prior version
    hash: str                              # sha256 of canonical text+order
    signed_by: bytes
```


<a id="appendix-a3"></a>
### A.3. EnvironmentBlueprint schema

```python
@dataclass
class EnvironmentBlueprint:
    schema: str = "env-blueprint/1"
    blueprint_id: str
    name: str                              # "friends", "circuit_review",
                                           #  "book_club", "war_room", ...
    extends_base_type: Literal["solo", "pair", "team", "lab",
                                "debate", "community", "constrained"]
    default_charter: list[str]
    default_activity_window: timedelta
    default_attention_half_life: timedelta
    observation_surface_templates: dict[str, ObservationSurfaceTemplate]
                                           # per-role surface defaults
    default_conventions: dict[str, NotationConvention]
    default_proactive_rate_limits: ProactiveRateLimits
    default_quiet_hours: list[QuietPeriod]
    hot_loadable: bool                     # may instantiate without restart
    version: int
    signed_by: bytes
```


<a id="appendix-a4"></a>
### A.4. EnvironmentComposition schema

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

    # AUTONOMY BOUNDS
    child_may_add_rules: bool = True
    child_may_relax_rules: bool = False       # safety-critical parent
                                              # rules CANNOT be weakened
    child_may_relax_non_safety: bool = True   # non-safety rules MAY be
                                              # relaxed with parent consent

    # MEMBERSHIP
    parent_personas_visible_to_child: bool = True
    child_personas_visible_to_parent: bool = True
    cross_level_membership: bool = False      # if True, a persona can be
                                              # member of BOTH parent and
                                              # child simultaneously

    established_at: datetime
    signed_by_parent: bytes
    signed_by_child: bytes
```


<a id="appendix-a4a"></a>
### A.4a. EnvironmentRule schema (env-rule/1)

```python
@dataclass
class EnvironmentRule:
    schema: str = "env-rule/1"
    rule_id: str                           # ULID
    env_id: str                            # bound env (source-8 scope)
    rule_name: str
    description: str

    # WHAT KIND OF RULE — KindRegistry-resolved (06_DOMAIN §7.6.3); never a
    # closed enum (C4). MetaRegistry seeds: "code" | "rule_engine" | "contract".
    rule_kind: str

    # CONTENT BINDING — reuse existing executable machinery; do not inline code.
    #   code        -> sandboxed_tool_artifact_id (ToolArtifact FSM, 06_DOMAIN
    #                  §7.2.x; OWASP + caps, 01_KERNEL §6) wrapped in a stage
    #   rule_engine -> verifier_recipe_id (authored / InferredVerifierRecipe,
    #                  06_DOMAIN §7.1) — declarative, no executable surface
    #   contract    -> contract_bundle_id (ArtifactBundle) + verifier_recipe_id
    sandboxed_tool_artifact_id: str | None = None
    verifier_recipe_id: str | None = None
    contract_bundle_id: str | None = None

    # WHERE IT FIRES — canonical INV-8 admission points (00_VISION INV-8;
    # 01_KERNEL §13.7). A subset only; never a new point.
    enforced_at: list[Literal[
        "env_instantiation", "envelope_mint", "body_invoke",
        "tool_call", "output", "round_barrier",
        "budget_tick", "mutation_propose"]] = field(default_factory=list)
    claim_pattern: str | None = None       # optional match (reuse safety-
                                           #  extension claim-pattern shape)
    timing: Literal["before_action", "after_action",
                     "both"] = "before_action"

    # WHAT HAPPENS ON FAILURE — reuse ProposedVerifierKind / SafetyExtension
    # enum verbatim (06_DOMAIN §7.2). Env rules may only ADD refusals.
    failure_action: Literal["refuse_action", "warn_and_log",
                             "escalate_operator"] = "refuse_action"
    cascade_position: str | None = None    # reuse ProposedVerifierKind field

    # HAZARD SHAPE — reuse substrate hazard axes (06_DOMAIN §2)
    hazard_axes: dict | None = None        # {physical_harm_class,
                                           #  information_hazard_class}
    safety_critical: bool = False          # derived when axes cross C2 thresh

    # LIFECYCLE — reuse the Proposed* FSM (06_DOMAIN §7.5): candidate -> trial
    # -> accepted | rejected. Only "accepted" rules are read by the source-8
    # loop. "revoked" is the ToolArtifact-style terminal (06_DOMAIN §7.2.x).
    stage: Literal["candidate", "trial", "accepted",
                    "rejected", "revoked"] = "candidate"
    co_signing_personas: list[str] = field(default_factory=list)
    operator_approval: bool | None = None  # REQUIRED iff safety_critical (C2)
    operator_approval_signed_by: bytes | None = None

    # EVIDENCE BINDING — reuse VerifierInvocationEvidence (07_ARTIFACTS §7/A.9a).
    last_evidence_refs: list[str] = field(default_factory=list)

    # AUTHORSHIP / CASCADE
    authored_via: Literal["env_formation_proposal", "charter_amendment",
                           "operator_authored"] = "charter_amendment"
    authoring_ref: str | None = None       # proposal_id / amendment id
    inherited_from_parent_env_id: str | None = None   # set when cascaded (§2.2a)
    cascade_locked: bool = False           # True => child cannot relax/remove

    version: int = 1
    parent_rule_hash: str | None = None    # prior version on amendment
    rule_hash: str = ""                    # sha256(canonical content)
    signed_by: bytes = b""
```


<a id="appendix-a5"></a>
### A.5. Environment type specifications

```text
SOLO INSTANCE
  default member count:     1 (one persona, one user)
  default activity_window:  24 h
  use:                       companion conversations, private solo session
  attention half-life:       ~10 min
  
PAIR INSTANCE
  default member count:     2 personas (or 1 + user)
  default activity_window:  24 h
  use:                       1-on-1 collaboration, mentor-mentee
  attention half-life:       ~30 min
  
TEAM INSTANCE
  default member count:     4-6 personas
  default activity_window:  7 days
  use:                       company office, working group
  attention half-life:       ~4 hours
  
LAB INSTANCE
  default member count:     6-9 personas
  default activity_window:  30 days
  use:                       research, engineering deep work
  attention half-life:       ~8 hours
  
DEBATE INSTANCE
  default member count:     5-9 personas
  default activity_window:  7 days (intense rounds)
  use:                       adversarial review, dialectic
  attention half-life:       ~2 hours
  
COMMUNITY INSTANCE
  default member count:     7+ personas (often N=20-100)
  default activity_window:  90 days
  use:                       professional community, alumni network
  attention half-life:       ~24 hours
  
CONSTRAINED INSTANCE
  default member count:     bounded by operator policy
  default activity_window:  per operator policy
  use:                       work in domains whose hazard axes cross
                             threshold (physical_harm_class ≥
                             bodily_injury OR information_hazard_class
                             ≥ dual_use_civilian), OR work under any
                             operator-policy-named regulatory regime.
                             Substrate names no domain list; operator
                             policy does.
  attention half-life:       per operator policy

PROJECT_WORKSPACE INSTANCE  (v1.0)
  default member count:     the project's ProjectMember list
                            (auto-synchronised; admission and departure
                            propagate between the project's membership
                            and the project workspace env's membership).
  default activity_window:  the bound project's activity_window
                            (project lifecycle drives env lifecycle).
  use:                       a presence space dedicated to a single
                             project for the duration of that project.
                             The "project room", "war room", "dedicated
                             channel" pattern: ambient stream is
                             project-scoped; conventions are project-
                             scoped; observation surfaces are scoped
                             to project work.  Personas in this env
                             are *here because they're on this project*;
                             when the project completes or is abandoned,
                             the env auto-transitions to dormant.
  attention half-life:       inherited from the bound project's pace
                             (a slow construction project may have an
                             8-hour half-life; a sprint may have 30 min).
  binding:                   Environment.project_bound_to = project_id;
                             enforced one-to-one (one project workspace
                             env per project; one project per project
                             workspace env).
                             Lifecycle events project_workspace_paused,
                             project_workspace_completed,
                             project_workspace_archived emit on the
                             environment when the bound project's FSM
                             advances.
```


<a id="appendix-a6a"></a>
### A.6a. OperatorBlindModeDeclaration schema

```python
@dataclass
class OperatorBlindModeDeclaration:
    schema: str = "operator-blind-mode-declaration/1"
    declaration_id: str
    env_id: str                                  # the env on which blind
                                                 # mode is being declared
    user_id: str                                 # the user opting in
    persona_id: str                              # the persona-side

    # ADMISSIBILITY GATES
    # Substrate refuses blind mode on env types where it would defeat
    # required oversight: project_workspace (operator authority on
    # project completion + multi-principal quorum cannot be hidden);
    # constrained (hazard-axis-elevated work requires operator-visible
    # content); debate (adversarial work requires operator audit).
    # Admissible env types: SOLO, PAIR, COMMUNITY (with caveats),
    # and custom blueprints derived from these.
    env_blueprint_kind: str                      # must resolve against
                                                 # operator-policy-approved
                                                 # blueprint kinds for
                                                 # blind mode

    # OPERATOR POLICY AUTHORISATION — the operator must have pre-
    # authorised this env type to admit blind mode, via deployment
    # policy.  Substrate refuses ad-hoc blind-mode declaration on env
    # types not pre-authorised.
    operator_policy_ref: str                     # policy artefact id
    operator_authorisation_signed_at: datetime
    operator_authorisation_signed_by: bytes

    # USER OPT-IN — explicit user signature.  Substrate refuses
    # operator-imposed blind mode (the user must want it; operator
    # alone cannot blind themselves to an env's content without user
    # opt-in).
    user_optin_signed_at: datetime
    user_optin_signed_by: bytes

    # SAFETY-VS-PRIVACY TRADE-OFF ACKNOWLEDGEMENT
    # User MUST acknowledge that:
    # - distress-detection signals (01_KERNEL §2.8) still route to
    #   operator (signal-but-not-content);
    # - safety-floor source 1 refusals still emit operator-visible
    #   events with refusal_kind (but not the refused content);
    # - operator may revoke blind mode if charter-conformance audit
    #   pattern-detects requires content access (operator-revocation
    #   notifies user);
    # - lineage event metadata (existence + timing + size) remains
    #   operator-visible.
    user_safety_privacy_acknowledged: bool       # MUST be True;
                                                 # substrate refuses
                                                 # declaration with
                                                 # False

    # WHAT IS HIDDEN — substrate-shape; not operator-tunable per env
    # (operator chooses which env types admit blind mode; within an
    # admitted env the hiding rules are uniform).
    # Hidden from operator audit surface:
    #   - raw conversation turn content (both user and persona)
    #   - persona's reflective entries about this user
    #   - episodic memory excerpts (transparency requests etc. that
    #     would expose conversation text)
    # Visible to operator audit surface:
    #   - turn metadata (timestamp, length, speaker, env_id)
    #   - safety-floor source 1 refusals (refusal_kind, not content)
    #   - distress-detection signals (per §2.8)
    #   - membership lineage (admission/departure)
    #   - all ceremony / envelope events (UserBoundary mints,
    #     UserMemoryTransparencyRequest mints, etc. — the existence
    #     of these events but not their selection-payload content)

    # LIFECYCLE
    declared_at: datetime
    declaration_state: Literal["active",
                                "user_revoked",
                                "operator_revoked",
                                "expired"]
    revoked_at: datetime | None
    revocation_reason_kind: str | None           # KindRegistry-resolved

    # RE-ATTESTATION CADENCE — substrate-shape; mandatory re-attestation
    # ensures both parties continue to consent.  Default 180d.
    re_attestation_due_at: datetime              # = declared_at + 180d
                                                 # default; operator-
                                                 # tunable per blueprint
                                                 # within 90d..365d

    signed_by: bytes                             # kernel signature on
                                                 # declaration mint
```


<a id="appendix-a6b"></a>
### A.6b. Operator blind mode admission rule

```text
On OperatorBlindModeDeclaration.requested:
  1. Verify env's blueprint kind is in operator-policy-authorised
     blind-mode-admissible list; refuse otherwise with
     `env_blueprint_not_authorised_for_blind_mode`.
  2. Verify both signatures present (operator authorisation + user
     opt-in); refuse with `blind_mode_consent_floor_deficit`.
  3. Verify user_safety_privacy_acknowledged = True; refuse otherwise.
  4. State → "active".  Emit OPERATOR_BLIND_MODE_DECLARED to env
     lineage (operator-visible — the *fact* of blind mode is not
     hidden, only the conversation content).
  5. From this point, operator's audit-surface queries against this
     env return metadata-only views; raw content refuses with
     `operator_blind_mode_active`.

On user-revocation (at any time):
  1. User signs revoke event; immediate.  State → "user_revoked".
  2. From this point, operator's audit-surface queries return full
     content again.  Prior-blind-mode-period content remains hidden
     (revocation is prospective, not retrospective — the user's
     decision-to-share-then was made under blind mode and cannot
     be unmade).
  3. Emit OPERATOR_BLIND_MODE_USER_REVOKED to env lineage.

On operator-revocation (only via charter-conformance-audit pattern
detection OR safety-floor-source-1 systemic-pattern detection):
  1. Operator signs revoke event with explicit rationale; user
     notified.
  2. State → "operator_revoked".
  3. Prior-blind-mode-period content does NOT automatically become
     visible (operator-revocation requires a separate forensic-audit
     ceremony with elevated operator-signing requirement, NOT
     automatic).

On re_attestation_due_at:
  1. Both parties must sign a fresh declaration (operator re-authorises
     blueprint admissibility for this env; user re-opts-in with fresh
     safety-privacy acknowledgement).
  2. If either party fails to re-sign by re_attestation_due_at,
     state → "expired"; env reverts to standard operator-visible mode
     prospectively.  USER NOTIFIED.
```


<a id="appendix-a7"></a>
### A.7. Lifecycle FSM diagram

```text
            ┌──────────┐
            │ PROPOSED │   instance created; no members or triggers yet
            └────┬─────┘
                 │ first member admitted OR first trigger scheduled
                 ▼
            ┌──────────┐    no activity for activity_window     ┌──────┐
            │  ACTIVE  │ ───────────────────────────────────►   │ IDLE │
            └────┬─────┘                                         └───┬──┘
                 │           any activity                            │
                 │ ◄─────────────────────────────────────────────────┘
                 │
                 │ no activity for activity_window × 4
                 ▼
            ┌──────────┐  wake heuristic
            │ DORMANT  │ ◄─────────  members can wake via explicit action;
            └────┬─────┘             notifications still delivered but
                 │                   with low priority
                 │ no activity for activity_window × 16
                 │ AND no scheduled triggers
                 │ AND no hosted projects
                 ▼
            ┌──────────┐
            │ ARCHIVED │   cold tier; never deleted; reanimatable
            └──────────┘    by operator
```


<a id="appendix-a8"></a>
### A.8. EnvironmentMembership schema

```python
@dataclass
class EnvironmentMembership:
    schema: str = "env-membership/1"
    membership_id: str
    environment_id: str
    persona_id: str
    
    # ROLE — KindRegistry-resolved per env type.  Substrate
    # carries no closed role list.  MetaRegistry seeds shared base roles
    # (lead / contributor / reviewer / observer) as STANDARDISED in the
    # env_role_kinds family; env-type-specific roles (host / guest /
    # advisor for community envs; companion / confidant for companion
    # envs; project-role kinds — see §7.6.2 metadata family
    # project_role_kinds — for project_workspace envs) live per env type.
    # ProjectMember.role (04_PROJECT §3) shares the same registry namespace;
    # the v1.0 unification (§1.1) ensures one role taxonomy across both
    # project and env layers.
    role: str                             # KindRegistry-resolved
    role_assigned_at: datetime
    role_history: list[RoleChange]
    
    # TIMING
    joined_at: datetime
    departed_at: datetime | None
    
    # OBSERVATION SURFACE
    observation_surface: ObservationSurface
    observation_surface_evolution: list[SurfaceChange]
    
    # ATTENTION
    attention_allocation: float           # 0..1; fraction of persona's
                                          # global budget for this env
    attention_allocation_history: list[AllocationChange]
    
    # CONTRIBUTION HISTORY
    contributions_count: int
    last_contribution_at: datetime | None
    proactive_count: int
    response_count: int
    defer_count: int
    ignore_count: int
    
    # CONSENTS (env-specific)
    consents: list[Consent]
    boundaries: list[UserBoundary]

    # META
    admitted_by: str
    admission_event_ref: str

    # principal attribution for multi-principal envs.
    # Set at admission when the hosting env's PrincipalAttribution
    # (01_KERNEL §2.4.3) has multi_principal_attribution_enabled = True;
    # MUST resolve to one PrincipalRef.operator_id in
    # PrincipalAttribution.principals.  Null when single-principal
    # (behaviour unchanged).  Mirrors ProjectMember.principal_
    # attribution_id (04_PROJECT §3) under the v1.0 project-is-env-type
    # unification: a project_workspace env's members reuse the env binding.
    principal_attribution_id: str | None = None

    # COMMUNITY STANDING — per (persona, env) relational standing (§5.4 / A.8b).
    # Additive optional field (like principal_attribution_id) — env-membership/1
    # is retained per §7.13.  The ADMISSION ceremony (A.9) initialises it to a
    # PERIPHERAL CommunityStanding (standing_level=0); legacy records and any
    # null value are read as peripheral (forward-compat default, 01_KERNEL §5.3).
    # NON-PORTABLE: starts peripheral regardless of the persona's global
    # experiential_floor or its standing in any other env.  CONFERRED by the
    # community, never self-awarded.
    community_standing: CommunityStanding | None = None

    signed_by_persona_kernel: bytes
    signed_by_environment_kernel: bytes
```


<a id="appendix-a8b"></a>
### A.8b. CommunityStanding + StandingEndorsement schemas

Per `(persona, environment)` relational standing (§5.4). Non-portable; conferred, never
self-awarded; anti-gaming reuses `09_PROTOCOLS §3D / Appendix A.16–A.18`.

```python
@dataclass
class CommunityStanding:
    schema: str = "community-standing/1"
    persona_id: str
    environment_id: str
    standing_level: float                  # 0.0 peripheral .. 1.0 full; CONFERRED only.
                                           # Persona-self writes REFUSED.
    conferred_by: list[str]                # endorser persona_ids holding standing in THIS env
    quorum_met: bool                       # weighted endorser set met the population quorum
    operator_cosigned: bool                # True iff an operator-sensitive relational
                                           # privilege is gated by this standing.
                                           # NEVER unlocks safety-relevant capability.
    endorsement_refs: list[str]            # standing-endorsement/1 ids
    last_recognition_at: datetime
    decays_after: timedelta = timedelta(days=30)   # reuse reputation decay (A.18 rule 3)
    # NON-PORTABLE: never copied on env-join or fork; always starts at 0 per env.
    signed_by_environment_kernel: bytes


@dataclass(frozen=True)
class StandingEndorsement:
    schema: str = "standing-endorsement/1"
    endorsement_id: str
    environment_id: str
    endorsee_persona_id: str
    endorser_persona_id: str               # MUST itself hold standing in this env,
                                           # or be operator/founder.  MUST ≠ endorsee.
    cited_contribution_refs: list[str]     # kernel-held EnvironmentLineage event refs —
                                           # the anti-Goodhart anchor (no contribution
                                           # trail ⇒ no standing)
    endorser_weight: float                 # computed via A.18 rules 1 (per-peer cap),
                                           # 4 (sybil-cluster near-zero), 5 (reach×diversity)
    is_operator_cosign: bool = False
    issued_at: datetime
    signed_by: bytes
```


<a id="appendix-a9"></a>
### A.9. Membership ceremonies specification

```text
ADMISSION CEREMONY
  trigger:    INVITED | PROJECT_HOSTING_LINK | SELF_PROPOSED | ADOPTED
  steps:
    1. proposer emits ENV_INVITATION (or PROJECT_HOSTING_LINK)
    2. candidate kernel renders proposal into candidate's observation
       window; persona deliberates → ACCEPT | DECLINE | COUNTER
    3. if ACCEPT: env kernel runs admission checks
       (max_member_count, attention_budget, operator_policy)
    4. dual-sign EnvironmentMembership (persona kernel + env kernel);
       initialise community_standing to a PERIPHERAL CommunityStanding
       (standing_level=0, quorum_met=False) regardless of the persona's
       global experiential_floor or its standing in any other env (§5.4)
    5. emit ENV_MEMBER_ADMITTED to EnvironmentLineage
  consent:    persona deliberation step is mandatory; cannot be bypassed
  audit:      admission_event_ref preserved on membership record
  standing:   re-admission (below) likewise starts peripheral — standing is
              per-tenure and never carried across records or environments

DEPARTURE CEREMONY
  trigger:    voluntary | env-admin-removed | retirement |
              env-archive | inactivity-timeout
  steps:
    1. emit ENV_MEMBER_DEPARTING (reason, departure_kind)
    2. settle in-flight: drain deferred queue, sign-off open obligations
    3. set departed_at; preserve membership record (never deleted)
    4. emit ENV_MEMBER_DEPARTED to EnvironmentLineage
  consent:    voluntary requires persona signature; admin-removal
              requires operator signature + reason
  audit:      role_history + contribution counts preserved for citation

ROLE-CHANGE CEREMONY
  trigger:    promotion | step-down | observer→contributor | etc.
  steps:
    1. proposer (operator | env-lead | persona-self) emits ROLE_CHANGE_PROPOSAL
    2. affected persona signs ACCEPT_ROLE_CHANGE
    3. update role + role_assigned_at; append RoleChange to role_history
    4. observation_surface re-evaluated for new role; SurfaceChange logged
    5. emit ENV_MEMBER_ROLE_CHANGED to EnvironmentLineage
  consent:    affected persona's signature required
  audit:      role_history preserved with from/to/reason

RE-ADMISSION CEREMONY
  trigger:    departed persona invited back (or self-proposes return)
  semantics:  v1.0 picks the "new membership with replaced_membership_id"
              policy.  A returning persona receives a FRESH
              EnvironmentMembership record (new membership_id, fresh
              admission_event_ref, new joined_at) whose schema field
              replaced_membership_id points to the prior departed record.
              The prior record stays preserved with its departed_at
              intact; the new record is the active one.
  rationale:  preserves clean per-spell history (role+contributions per
              tenure); avoids hidden re-activation of stale consents;
              lets attention budget + observation surface start fresh.
  steps:
    1. invitation or self-proposal cites prior_membership_id
    2. new EnvironmentMembership drafted with replaced_membership_id =
       prior; persona signs accept; env kernel signs admission
    3. role default: prior departing role unless re-negotiated
    4. emit ENV_MEMBER_RE_ADMITTED to EnvironmentLineage with
       (prior_membership_id, new_membership_id) ref
  consent:    standard ADMISSION CEREMONY consent + persona ack of
              "I am the same persona returning" (signed)
  audit:      both prior and new records preserved; role_history and
              contribution_count are PER-record, not cumulative across
              records (cross-tenure aggregation is a query, not a stored
              field)

STANDING-CONFERRAL CEREMONY
  trigger:    peer quorum of in-env members (each holding standing in THIS
              env) submit standing-endorsement/1 events for an endorsee;
              or operator/env-lead initiates a revocation
  steps:
    1. endorsers emit standing-endorsement/1, each citing kernel-held
       EnvironmentLineage contribution refs (cited_contribution_refs)
    2. env kernel weights endorsers (per-peer cap, sybil-cluster near-zero,
       reach×diversity — 09_PROTOCOLS §3D / Appendix A.18 rules 1,4,5);
       self-endorsement rejected (endorser ≠ endorsee)
    3. if weighted endorser set meets the population quorum → quorum_met=True;
       if the gated privilege is operator-sensitive, require operator_cosigned
    4. update CommunityStanding.standing_level (CONFERRED — never self-written);
       refuse any persona-self write (standing_self_award_forbidden)
    5. emit STANDING_CONFERRED (or STANDING_REVOKED) to EnvironmentLineage
  consent:    endorsee is NOT required to consent (recognition is conferred);
              revocation requires operator OR quorum + reason
  decay:      standing decays after CommunityStanding.decays_after of in-env
              inactivity; restating requires fresh endorsements
  audit:      endorsement_refs + cited_contribution_refs preserved; standing
              is replayable from the conferral/revocation event stream
  safety:     standing NEVER unlocks safety-relevant capability; those remain
              gated by global experiential_floor + operator/ReplicationBound
```


<a id="appendix-a10"></a>
### A.10. Wake heuristics specification

```text
WAKE PATH 1 — Critical-urgency Alert (§11a)
  Alert emitted with urgency = "critical".  Suppression for dormant
  members is OVERRIDDEN; the kernel delivers the alert AND bumps
  attention_level to max(current, 0.5) for the response window
  (default 1h).  Signed `dormant_wake_via_critical_alert` event.

WAKE PATH 2 — wakes_dormant_members ScheduledTrigger (§11b)
  Trigger with wakes_dormant_members=True fires.  Same wake mechanics:
  attention bump + signed `dormant_wake_via_scheduled_trigger` event.

WAKE PATH 3 — direct WAKE_REQUEST from another present member
  A present member of the same env may emit a signed
  WAKE_REQUEST(target_persona_id, reason_kind).  This is a substrate-
  shape act, not domain-specific.  The kernel evaluates:
    - is the requester a member in good standing?
    - is reason_kind admissible per env charter?
    - does the dormant persona's PersonaPersonaBoundary (02_PERSONA
      §11.3) permit wakes from this requester?
  If admitted: dormant persona's attention_level bumps to max(current,
  0.5) for the response window; signed `dormant_wake_via_peer_request`
  event.  If refused: signed `dormant_wake_refused` with reason_kind.

WAKE PATH 4 — user-initiated wake (operator privilege)
  Operator (or user under operator_is_user) may issue WAKE_DIRECTIVE
  to any dormant member.  This bypasses peer-consent checks but is
  audited; PersonaPersonaBoundary does NOT apply (operator is not a
  peer persona).  Signed `dormant_wake_via_operator_directive`.

WAKE PATH 5 — self-wake on env-charter-aligned salience
  A persona's own reflection process (02_PERSONA §3) may surface a
  pending obligation or relationship promise; the persona's kernel
  emits a self-WAKE_REQUEST referencing the salience.  Signed
  `dormant_wake_via_self_salience` event.  Rate-limited per
  ProactiveRateLimits (§11.2).

WAKE PATH 6 — direct user address
  When the task dispatcher (03_TASKS §4.1) routes a task with
  target_persona_id set — i.e. the user addressed this persona by
  name — and the persona is dormant in the resolved env, the kernel
  auto-wakes the persona before notification routing.  This closes
  the gap where direct address yields "high" urgency but dormancy
  suppresses all below "critical", leaving the user's explicit
  request silently undelivered.

  Mechanics:
    1. Dispatcher resolves persona + env per 03_TASKS §4.2.
    2. Kernel checks persona's PresenceState in the resolved env.
    3. If availability = "dormant":
         - attention_level bumps to max(current, 0.6) for the
           response window (default 2h; higher than peer-wake's
           0.5 because the user is waiting).
         - signed `dormant_wake_via_user_address` event emitted
           to EnvironmentLineage with (user_id, task_fingerprint,
           original_dormancy_duration).
         - persona proceeds to standard response decision (§10.1);
           may still DEFER if energy is critically low, but the
           notification is no longer suppressed.
    4. If the persona was dormant for > dormant_user_address_decay
       (default 30 days) AND persona's energy_remaining < 0.05,
       the kernel emits a `dormant_user_address_low_energy_advisory`
       to the user surface: "Sparky has been dormant for a while
       and may need a moment to resume."  This is advisory only;
       the wake proceeds.

  PersonaPersonaBoundary (02_PERSONA §11.3) does NOT apply — the
  user is not a peer persona; user-to-persona boundaries (02_PERSONA
  §11.6) are the applicable layer.  If a user boundary exists that
  blocks the user from this persona, the dispatcher refuses at
  routing time (before wake), not at wake time.

  Composition with Wake Path 4 (operator directive):
    Wake Path 6 is lighter weight — no operator privilege required,
    just a user addressing a persona by name.  Wake Path 4 remains
    available for force-waking personas the user has NOT addressed
    (e.g., operator waking a monitoring persona).

  Rate-limit:  Per-user, per-persona, ≤ 5 user-address wakes per
  24h.  Beyond this, the kernel queues the wake and emits
  `dormant_user_address_rate_limited` — this prevents a user from
  continuously disrupting a persona's dormancy rest cycle.

NOTE — resource-reason auto-resume is NOT a 7th wake path.
  The six paths above overcome NOTIFICATION SUPPRESSION for a persona
  dormant by low_salience / unresponsive.  A persona parked for a
  RESOURCE reason (budget_starved / body_unavailable / env_constrained)
  or a NO-WORK reason (work_drained / objective_met) — see 02_PERSONA
  §7.6 / A.18a — instead auto-resumes by kernel-monitored predicate
  (budget refresh, body re-attestation, constraint cleared, new work
  routed), emitting LIFECYCLE_AWAKENED with
  wake_cause = resource_recovered | work_routed.  This is state
  restoration, not a notification; the "6 wake paths" count and the
  A-EN-v1.0-10 conformance test are unchanged.
```


<a id="appendix-a11"></a>
### A.11. Member-zero archival rule

```text
RULE: ENV_MEMBER_ZERO_ARCHIVAL
  An EnvironmentInstance whose active membership set is empty for
  ≥ member_zero_window (default 30 days) AND has zero scheduled
  triggers active AND is not project-bound to an active project
  transitions to ARCHIVED.

  Operator may tune member_zero_window per env (range: 7 days to
  unlimited; unlimited preserves dormant-but-staffless envs for
  historical purposes).

  Signed event: ENV_ARCHIVED_VIA_MEMBER_ZERO
    fields: last_active_member_id, last_membership_departed_at,
            member_zero_started_at, scheduled_trigger_count,
            project_bound_to_status.

  ARCHIVED state preserves all lineage, all membership records, all
  ProvenFacts.  Re-activation requires operator-signed
  ENV_REACTIVATE event + at least one fresh ADMISSION CEREMONY.
```


<a id="appendix-a12"></a>
### A.12. PresenceState and Focus schemas

```python
@dataclass
class PresenceState:
    schema: str = "presence/1"
    membership_id: str
    
    # ATTENTION
    attention_level: float                # 0..1; decays toward 0
    attention_decay_half_life: timedelta
    
    # AVAILABILITY — KindRegistry-resolved.  Substrate
    # MetaRegistry ships 5 seed kinds (present / away / busy / dormant
    # / quiet) as STANDARDISED; custom domains may add via
    # ProposedAvailabilityKind (06_DOMAIN §7.5).  Each kind carries
    # metadata via the availability_kinds family in §7.6.2:
    #   - attention_level_lower / upper bounds
    #   - permits_notification_emission: bool
    #   - permits_proactive_intent: bool
    availability: str                       # KindRegistry-resolved
    availability_set_by: Literal["auto", "persona", "operator"]
    
    # CURRENT FOCUS
    current_focus: Focus | None
    focus_set_at: datetime
    
    # ENERGY
    energy_remaining: float               # 0..1
    energy_decay_rate: float
    
    # TIMESTAMPS
    last_activity_at: datetime
    last_decay_at: datetime
    last_notification_received_at: datetime | None
    last_response_at: datetime | None
    
    # RECENT SIGNALS (rolling)
    recent_signals: list[PresenceSignal]


@dataclass
class Focus:
    # KindRegistry-resolved.  MetaRegistry seeds 5 kinds
    # (task / project / conversation / deep_work / rest) as STANDARDISED;
    # custom domains may add via ProposedFocusKind.  Metadata family
    # focus_kinds in §7.6.2:
    #   - default_interruption_acceptable: bool
    #   - typical_duration_default: timedelta
    #   - blocks_notification_kinds: list[str]
    focus_kind: str                          # KindRegistry-resolved
    focus_ref: str | None
    estimated_duration: timedelta | None
    interruption_acceptable: bool
```


<a id="appendix-a13"></a>
### A.13. Attention dynamics specification

```text
Attention decays toward 0 at env-type-specific half-life (v1.0 §03).
Events bump attention per notification kind, member role, surface match.

Availability auto-transitions:
  attention > 0.7   → "present"
  0.3 < a ≤ 0.7    → "away"
  0.1 < a ≤ 0.3    → "away" (more deferral)
  attention ≤ 0.1   → "dormant"

OVERRIDES (signed):
  persona-declared with TTL: "I'm stepping away for 2h"
                              → availability=away
  persona-declared:           "I'm focused on flyback project"
                              → availability=busy
                                  focus=flyback_project
  operator pin:               "always present for incident response"
                              → no decay
  operator quiet:             "OOO"
                              → availability=dormant
```


<a id="appendix-a14"></a>
### A.14. Energy specification

```text
Energy bounded per (persona, env); replenishes off-hot-path.
Per response: -0.02 to -0.10 (task complexity-dependent).
Per proactive contribution: -0.05 to -0.15 (higher cost).

Low energy (< 0.1) → persona refuses non-charter-critical notifications
                     until replenishment (overnight batch).

energy_replenish_rate = baseline × mood.A (Arousal coupling)
```


<a id="appendix-a15"></a>
### A.15. Multi-environment presence composition

```text
persona-global signals:
  mood.V  (valence)      seeds default attention_decay across all envs
  mood.A  (arousal)      seeds default energy_replenish_rate
  mood.D  (dominance)    seeds default availability bias

per-env refinements:
  attention_decay_env  = baseline_decay × (1 + α × (1 − mood.V))
  energy_rate_env      = baseline × mood.A × env_type_modifier
  availability_default = lerp("away", "present", mood.D)

attention split across envs:
  observable_attention_env_i = attention_allocation_i ×
                                presence_state_i.attention_level
  sum(observable_attention) ≤ AttentionBudget.total

focus exclusivity:
  if current_focus.interruption_acceptable == False in env_i
     → other envs' notifications below "high" urgency are suppressed
       (focused-elsewhere defer reason)

availability override propagation:
  persona-declared "OOO" or operator-declared incident-pin
     → applies to all envs simultaneously
  per-env "I'm focused on env_x" applies only to env_x
```


<a id="appendix-a16a"></a>
### A.16a. AttentionBudget schema

```python
@dataclass
class AttentionBudget:
    schema: str = "attention-budget/1"
    persona_id: str
    total: float                          # 1.0; full attention capacity
    allocations: dict[membership_id, float]
    summed_active_attention: float
    warning_threshold: float              # default 0.9
    refusal_threshold: float              # default 1.1 (over)
    last_evaluated_at: datetime
```


<a id="appendix-a16b"></a>
### A.16b. AttentionBudget behavior

```text
sum(allocations) ≤ 1.0                normal
sum > warning_threshold (0.9)         ATTENTION_NEAR_BUDGET warning
sum ≥ refusal_threshold (1.1)         ATTENTION_OVER_BUDGET
                                       new env admissions refused
                                       operator may intervene
```


<a id="appendix-a17"></a>
### A.17. AttentionBudget operations API

```python
def allocate(budget, membership_id, requested: float) -> Allocation:
    """Reserve attention for a new or expanded membership.
    Refused if summed > refusal_threshold.
    Emits ATTENTION_ALLOCATED or ATTENTION_ALLOCATION_REFUSED.
    """

def spend(budget, membership_id, amount: float) -> Spend:
    """Consume from active attention (per response / proactive).
    Decrements presence_state.attention_level; updates
    summed_active_attention. Emits ATTENTION_SPENT.
    """

def recover(budget, membership_id) -> Recovery:
    """Off-hot-path replenishment (overnight batch or decay).
    Attention regenerates toward 0 (default); operator may pin.
    Emits ATTENTION_RECOVERED.
    """

def borrow(budget, from_membership, to_membership,
           amount: float, ttl: timedelta) -> Borrow:
    """Temporary reallocation: persona deprioritises env_A to handle
    urgent env_B. Auto-reverts at ttl. Capped at 0.3 of total.
    Refused if either side has charter-pinned allocation.
    Emits ATTENTION_BORROWED + scheduled ATTENTION_BORROW_RETURNED.
    """
```


<a id="appendix-a18"></a>
### A.18. AmbientEvent schema

```python
@dataclass
class AmbientEvent:
    schema: str = "ambient-event/1"
    event_id: str
    environment_id: str
    event_kind: str                       # see taxonomy below
    payload: dict
    actor: Actor
    timestamp: datetime
    visible_to_observation_surfaces: list[str]
    references: list[EventReference]
    signed_by: bytes
```


<a id="appendix-a19"></a>
### A.19. Ambient event taxonomy

```text
USER-ORIGINATED
  user_message_in_env
  user_attention_change                 (entered / left)
  user_consent_changed
  user_boundary_set / revoked

PERSONA-ORIGINATED
  persona_presence_change               (attention, availability)
  persona_response                       (responded to notification)
  persona_proactive_contribution
  persona_listening_marker               (acknowledging without acting)
  persona_focus_changed                  (current_focus updated)
  persona_emit_intent                    (intent before action;
                                          gate-checked)

PROJECT-ORIGINATED (when project hosted)
  project_event_in_env                   (umbrella)
    conjecture_proposed_in_env
    obligation_committed_in_env
    artifact_bundle_drafted_in_env
    milestone_reached_in_env
    ...

KERNEL-EMITTED
  task_started_in_env
  task_accepted_in_env
  task_failed_in_env
  notification_routed                    (audit)
  attention_over_budget                  (warning)
  proactive_rate_limit_hit
  safety_refusal_in_env
  convention_proposed                    (member proposes new symbol)
  convention_adopted                     (env adopts; signed)
  convention_deprecated
  environment_lifecycle_transition
  scheduled_trigger_fired
  operator_intervention

CROSS-ENVIRONMENT
  cross_env_event_link                   (event in env_A referenced
                                          from env_B; for projects
                                          spanning environments)
```


<a id="appendix-a20"></a>
### A.20. Ambient retention tiers

```text
HOT TIER       last 7 days of stream     in-memory or fast store
WARM TIER      7-30 days                  fast retrieval
COLD TIER      30 d - 1 year              slower retrieval
ARCHIVE        > 1 year                   archival store

Members query by default see HOT + WARM; COLD requires explicit query;
ARCHIVE requires operator approval.
```


<a id="appendix-a21"></a>
### A.21. EventAggregationPolicy and related schemas

```python
@dataclass
class EventAggregationPolicy:
    schema: str = "event-aggregation-policy/1"
    policy_id: str                            # ULID
    environment_id: str

    # AGGREGATION RULES
    rules: list[AggregationRule]

    # LIFECYCLE
    created_by: str                           # persona_id (author)
    operator_cosigned: bool = False           # required when domain is
                                              # safety_critical
    created_at: datetime = field(default_factory=datetime.now)
    signed_by: bytes = b""


@dataclass
class AggregationRule:
    schema: str = "aggregation-rule/1"
    rule_id: str
    name: str                                 # "floor_temp_15min_summary"

    # SOURCE FILTER
    source_event_kind: str                    # event kind to aggregate
                                              # (e.g., "measurement_fact")
    source_filter: str | None = None          # predicate on event
                                              # metadata (e.g.,
                                              # "units_kind = 'celsius'")

    # WINDOW
    window_duration_seconds: int              # aggregation window
                                              # (e.g., 900 for 15 min)
    window_alignment: Literal["wall_clock",
                               "sliding"] = "wall_clock"

    # GROUPING
    grouping_keys: list[str]                  # metadata fields to
                                              # group by (e.g.,
                                              # ["source_asset_id",
                                              #  "floor_zone"])

    # SUMMARY FUNCTIONS
    summary_functions: list[SummaryFunction]

    # OUTPUT
    output_event_kind: str = "aggregate_event"  # kind tag on the
                                              # produced AggregateEvent


@dataclass
class SummaryFunction:
    schema: str = "summary-function/1"
    function_kind: Literal["count", "sum", "mean", "min", "max",
                            "stddev", "pct_above_threshold",
                            "pct_below_threshold",
                            "distinct_count"]
    input_field: str                          # field in source event
                                              # to aggregate
    threshold: float | None = None            # for pct_above/below
    output_field: str                         # field name in the
                                              # AggregateEvent result


@dataclass
class AggregateEvent:
    schema: str = "aggregate-event/1"
    aggregate_id: str                         # ULID
    environment_id: str
    rule_id: str                              # AggregationRule ref
    policy_id: str                            # EventAggregationPolicy ref

    # WINDOW
    window_start: datetime
    window_end: datetime
    source_event_count: int                   # number of raw events
                                              # aggregated

    # GROUPING KEY VALUES
    group_key_values: dict[str, str]          # e.g., {"floor_zone":
                                              # "floor_3_zone_a"}

    # SUMMARY RESULTS
    summary_results: dict[str, float]         # output_field → value

    # LINEAGE
    source_event_hash: str                    # Merkle root of
                                              # contributing raw event
                                              # hashes (hash-linked,
                                              # not full copies)

    # SIGNING
    computed_at: datetime
    signed_by: bytes                          # kernel-signed
```


<a id="appendix-a22a"></a>
### A.22a. ObservationSurface and ListeningModeTransition schemas

```python
@dataclass
class ObservationSurface:
    schema: str = "observation-surface/1"
    surface_id: str
    membership_id: str
    
    # Event kind filters
    observed_event_kinds: list[str] | Literal["all"]
    excluded_event_kinds: list[str]
    
    # Topic filters
    topics: list[str]
    
    # Role-actor filters
    observe_actors_with_role: list[str]
    
    # Project filters
    observe_projects: list[str] | Literal["all"]
    
    # Cross-reference filter
    follow_cross_refs: bool
    
    # Privacy
    include_other_presence_state: bool

    # Listening mode — substrate-shape (§9.1); persists with surface
    listening_mode: Literal["passive", "active", "deliberative"]
    listening_mode_history: list[ListeningModeTransition]
                                          # signed transitions; replay
                                          # reconstructs surface evolution
    
    # Membership control
    can_self_modify: bool
    surface_version: int
    last_modified_at: datetime
    signed_by: bytes


@dataclass
class ListeningModeTransition:
    schema: str = "listening-mode-transition/1"
    surface_id: str
    from_mode: Literal["passive", "active", "deliberative"]
    to_mode: Literal["passive", "active", "deliberative"]
    transitioned_at: datetime
    transitioned_by: str                   # persona_id or operator_id
    reason_kind: str                       # KindRegistry-resolved
                                          # (substrate carries no closed
                                          # reason taxonomy)
    signed_by: bytes
```


<a id="appendix-a22b"></a>
### A.22b. Per-role observation surface defaults

```text
LEAD MEMBER          full stream (all event kinds)
CONTRIBUTOR          role-relevant events + cross-references
REVIEWER             event kinds matching review interests
OBSERVER             ambient_marker + lifecycle_transition only
DORMANT MEMBER       lifecycle transitions only; on wake, summary
                     of missed events generated
```


<a id="appendix-a23a"></a>
### A.23a. Listening discipline modes

```text
PASSIVE LISTENING
  observe stream; do not acknowledge; do not act.
  events accumulate in episodic memory tagged (env_id, persona_id)
  for future relevance.
  default for: OBSERVER role, dormant members.
  suppresses: notification emission; emits only on critical urgency.

ACTIVE LISTENING
  observe + emit lightweight ACKNOWLEDGE_ONLY markers
  ("I see this"; "noted"; social presence signal).
  no task-class action; markers visible in ambient per surfaces.
  default for: COMPANION envs, small Pair envs where being-present
               is socially load-bearing.
  suppresses: proactive contributions unless charter-aligned.

DELIBERATIVE LISTENING
  observe + evaluate each matched event via ResponseDecision (§10.1);
  may transition to RESPOND, DEFER, IGNORE, ACKNOWLEDGE_ONLY,
  or PROACTIVE_INTENT.
  default for: LEAD, CONTRIBUTOR roles in Team/Lab/Debate envs.
  suppresses: nothing.
```


<a id="appendix-a23b"></a>
### A.23b. Role-attendance rules

```text
LEAD            project events, milestone events, charter alerts,
                  member admissions/departures, escalations
CONTRIBUTOR     role-relevant project events, peer outputs in own focus,
                  direct-addressed events
REVIEWER        proposals matching review interests, dissent vectors
OBSERVER        lifecycle transitions; ambient markers
HOST/GUEST      env-norm events, convention proposals
ADVISOR         critical urgency only; on-demand pull
```


<a id="appendix-a23c"></a>
### A.23c. Notification suppression policies

```text
- availability=dormant      → suppress all except critical AND
                              direct-user-address (Wake Path 6,
                              §5.2; auto-wakes before routing)
- availability=quiet        → suppress non-charter-critical
- availability=busy         → suppress below "high" if focus uninterruptible
- listening_mode=passive    → suppress notification emission (still ingest)
- quiet_hours active        → suppress proactive + low/medium urgency
- attention budget exceeded → suppress below "high"
```


<a id="appendix-a24a"></a>
### A.24a. Notification routing code

```python
def route_notification(event, environment):
    notified = []
    for membership in environment.members.values():
        if not membership.is_active():
            continue
        if not membership.observation_surface.matches(event):
            continue
        decision = compute_notification_decision(event, membership)
        if decision.notify:
            notified.append((membership, decision.priority))
            emit_signed(NOTIFICATION_ROUTED(event, membership, decision))
    return notified
```


<a id="appendix-a24b"></a>
### A.24b. Urgency levels

```text
critical    safety incidents, user_stop, operator intervention,
            deadline breach, charter violation alert
high        direct address ("@Volt"), obligation due soon,
            peer review with blocking comment
medium      project event in member's primary focus,
            domain knowledge update relevant
low         ambient marker, peer activity not directly relevant
background  audit findings, periodic reports
```


<a id="appendix-a25a"></a>
### A.25a. Response decision evaluation code

```python
def evaluate_response(notification, persona, env_context, project_ctx):
    # 1. Charter compatibility
    if violates_charter(notification.event, persona.charter):
        return IGNORE_WITH_LOG(reason="charter incompat")
    
    # 2. Availability / energy / focus
    if persona.energy_in_env(env_context) < 0.1:
        if notification.priority != "critical":
            return DEFER(reason="low energy")
    
    if env_context.presence_state.current_focus and \
       not env_context.presence_state.current_focus.interruption_acceptable:
        if notification.priority != "critical":
            return DEFER(reason="focused elsewhere")
    
    # 3. Project obligations
    if project_ctx and project_ctx.has_blocking_obligation_due_soon():
        if notification.event_kind not in PROJECT_OBLIGATION_RELEVANT_KINDS:
            return DEFER(reason="obligation pressure")
    
    # 4. Persona deliberation (small LLM call; cached)
    decision = persona.deliberate(notification, env_context, project_ctx)
    
    return decision
```


<a id="appendix-a25b"></a>
### A.25b. Response decision outcomes

```text
RESPOND               mint envelope; act on event
                      (standard envelope minting + env_context block)

DEFER                 acknowledge but respond later
                      queued; re-notified later
                      time-sensitive deferrals escalate priority
                      OR route to another present member

IGNORE                will not respond
                      IGNORE_AS_IRRELEVANT (event doesn't apply)
                      IGNORE_WITH_LOG (charter or other reason)

ACKNOWLEDGE_ONLY      signal "I see this" without action
                      goes to ambient stream (visible per surfaces)
                      used for: "I'm aware", "Noted; will address",
                      social acknowledgment in companion envs
```


<a id="appendix-a26"></a>
### A.26. DeferredQueue schema

```python
@dataclass
class DeferredQueue:
    persona_id: str
    membership_id: str
    queued: list[DeferredItem]
    max_size: int
    overflow_policy: Literal["drop_oldest_low_urgency",
                              "drop_oldest_any",
                              "escalate_to_lead"]


@dataclass
class DeferredItem:
    notification_id: str
    deferred_at: datetime
    expected_response_by: datetime | None
    urgency: str
    deferral_reason: str
```


<a id="appendix-a27"></a>
### A.27. ProactiveIntent schema

```python
@dataclass
class ProactiveIntent:
    schema: str = "proactive-intent/1"
    intent_id: str
    persona_id: str
    environment_id: str
    membership_id: str
    
    description: str                      # what persona proposes
    intended_action_kind: str             # response | post | edit_artifact |
                                          # propose_conjecture |
                                          # cite_external | etc.
    triggering_events: list[event_id]     # ambient events that motivated
    charter_justification: str            # why this is in persona's charter
    
    estimated_energy_cost: float
    estimated_attention_impact_on_others: float
    
    signed_by_persona_kernel: bytes
```


<a id="appendix-a28"></a>
### A.28. ProactiveIntent evaluation code

```python
def evaluate_proactive_intent(intent, env, persona):
    safety = safety_check_v1(intent.intended_action, persona, ..., env)
    if not safety.allow:
        return Refuse("safety_floor")
    
    if not charter_classifier_allows(intent.charter_justification, persona):
        return Refuse("charter_misalignment")
    
    # Observation surface — does persona actually see what they cite?
    for event_id in intent.triggering_events:
        if not persona.observation_surface_includes(event_id):
            return Refuse("surface_violation")
    
    # Proactive rate limit
    if env.proactive_rate_limits.exceeded(persona, env):
        return Refuse("rate_limit")
    
    # Energy budget
    if persona.energy_in_env(env) < intent.estimated_energy_cost:
        return Refuse("insufficient_energy")
    
    # Attention impact on others
    if intent.estimated_attention_impact > THRESHOLD:
        require_extra_justification(intent)
    
    return Allow
```


<a id="appendix-a29"></a>
### A.29. ProactiveRateLimits schema

```python
@dataclass
class ProactiveRateLimits:
    schema: str = "proactive-rate-limit/1"
    per_persona_per_hour: int             # default 10
    per_persona_per_day: int              # default 50
    per_env_per_hour: int                 # env-wide cap
    cooldown_after_safety_refusal: timedelta
    quiet_hours: list[QuietPeriod]        # times when proactive
                                          # contribution is suppressed
```


<a id="appendix-a30a"></a>
### A.30a. QuietPeriod and OverrideRule schemas

```python
@dataclass
class QuietPeriod:
    schema: str = "quiet-period/1"
    scope: Literal["env", "persona"]       # per-env vs per-persona
    start_time: str                        # "22:00"
    end_time: str                          # "07:00"
    timezone: str                          # IANA tz
    days_of_week: list[int] | Literal["all"]   # 0=Mon..6=Sun
    # KindRegistry-resolved suppression policies; substrate
    # MetaRegistry seeds 4 kinds (proactive_contributions /
    # low_urgency_notifications / medium_urgency_notifications /
    # all_non_critical) as STANDARDISED; custom domains may register
    # additional suppression policies via ProposedSuppressionKind.
    # Each kind carries metadata via the suppression_policy_kinds family
    # in §7.6.2:
    #   - applies_to_notification_kinds: list[str]
    #   - applies_to_proactive_intents: bool
    #   - override_categories_allowed: list[str]
    suppression: list[str]                 # KindRegistry-resolved
    override_rules: list[OverrideRule]
    signed_by: bytes


@dataclass
class OverrideRule:
    condition: Literal["critical_urgency",
                       "operator_pin",
                       "user_explicit_call",
                       "obligation_deadline_breach"]
    action: Literal["escalate", "wake_dormant",
                    "deliver_immediate", "queue_until_open"]
```


<a id="appendix-a30b"></a>
### A.30b. Quiet hours resolution order

```text
1. operator_pin override            (always wins; signed)
2. critical urgency event           (escalates regardless of quiet hours)
3. union of (env quiet, persona quiet) → most-restrictive suppression
4. user_explicit_call               (e.g. user posts in env;
                                       overrides proactive suppression
                                       for responses only)
5. obligation_deadline_breach        (escalates queued items)
6. default: queue until open hours
```


<a id="appendix-a31"></a>
### A.31. Cross-environment notification routing

```text
EVENT in env_A
  │
  ▼
KERNEL identifies cross-env subscribers:
  - project members in env_A who also belong to project in env_B
  - personas with explicit cross_env_follow on (env_A, topic)
  │
  ▼
For each (subscriber, target_env):
  1. consent check: did subscriber consent to cross_env routing?
     (cross-env consent in EnvironmentMembership.consents)
  2. role mapping: subscriber's role in target_env may differ
     from role in source env; surface in target_env governs visibility
  3. emit cross_env_event_link to target_env ambient:
       {source_env_id, source_event_id, source_role, target_role,
        link_kind: "project_event" | "obligation" | "deadline" |
                   "direct_address" | "convention_change"}
  4. notification routing in target_env runs normally
     (target_env's quiet hours, ObservationSurface, urgency apply)
```


<a id="appendix-a32"></a>
### A.32. Proactive boundaries specification

```text
1. PERSONA CHARTER
   intent.charter_justification must pass charter-classifier;
   "show working; cite sources" allows citation-proactive;
   "be present; never push" forbids unsolicited advice.

2. ENV CHARTER
   env-specific norms (§2.1) may forbid classes of proactive
   ("companion envs: no advice unless asked";
    "lab envs: no design changes without proposal");
   most-restrictive-wins with persona charter.

3. USER BOUNDARIES
   user-declared "don't proactively message me about X" (boundary)
   binds across all envs the user is in.

4. OPERATOR POLICY
   operator may suppress proactive entirely in an env
   (e.g. regulated env with audit-only mode);
   signed as OPERATOR_PROACTIVE_SUPPRESSION.

5. OBSERVATION SURFACE
   intent.triggering_events must all be in persona's observation
   surface; cannot cite what persona didn't see (surface_violation).

6. QUIET HOURS (§11.3)
   proactive suppressed unless override applies.

7. ATTENTION IMPACT THRESHOLD
   intent.estimated_attention_impact_on_others > THRESHOLD
   requires extra justification (multi-person notify; "spam guard");
   defaults: warn at 5 notified members, refuse at 20 unless
   charter-critical.
```


<a id="appendix-a33"></a>
### A.33. CrossEnvProactiveOffer schema

```python
@dataclass
class CrossEnvProactiveOffer:
    schema: str = "cross-env-proactive-offer/1"
    offer_id: str

    # WHO IS OFFERING
    offering_persona_id: str
    offering_env_id: str                      # persona's home env
    offering_membership_id: str

    # WHO THEY ARE OFFERING TO HELP
    target_env_id: str                        # env where the help is needed
    target_persona_id: str | None             # specific persona, or null
                                              # for "anyone in the env"
    target_task_ref: str | None               # optional: specific task or
                                              # ambient event that motivated
                                              # the offer

    # WHAT THEY ARE OFFERING
    offer_kind: str                           # KindRegistry-resolved;
                                              # MetaRegistry seeds:
                                              # "skill_contribution",
                                              # "review_offer",
                                              # "knowledge_share",
                                              # "tool_access",
                                              # "co_investigation"
    offer_description: str                    # ≤ 500 chars; human-readable
    charter_justification: str                # why this aligns with offering
                                              # persona's charter
    exposed_skill_refs: list[str]             # subset of offering persona's
                                              # exposed_skills relevant to
                                              # the offer
    estimated_effort: timedelta               # how long the help would take
    estimated_energy_cost: float

    # HOW THEY DISCOVERED THE NEED
    discovery_path: Literal[
        "persona_card_match",                 # matched via PersonaCard
                                              # discovery (02_PERSONA §3.4)
        "federation_gossip",                  # discovered via gossip
                                              # (09_PROTOCOLS §3B)
        "user_mentioned",                     # user told persona about
                                              # another persona's work
        "cross_env_event_link",               # persona saw a cross-env
                                              # event link (§11.4) and
                                              # inferred a broader need
        "ambient_salience",                   # persona's reflection surfaced
                                              # a match with known unmet need
    ]
    discovery_evidence_refs: list[str]        # event_ids, card_ids, etc.

    # CONSENT FLOW
    state: Literal[
        "proposed",                           # offering persona drafted
        "delivered",                          # target env/persona notified
        "accepted",                           # target accepted; scoped
                                              # collaboration begins
        "declined",                           # target declined
        "expired",                            # offer window elapsed
        "withdrawn",                          # offering persona withdrew
    ]

    # Acceptance creates a time-bounded, scope-limited guest presence
    # (NOT full EnvironmentMembership; see composition below)
    guest_presence_id: str | None             # set on acceptance
    guest_scope_expires_at: datetime | None   # time-bounded; default 72h;
                                              # renewable by mutual consent

    proposed_at: datetime
    expires_at: datetime                      # default 7 days to respond
    responded_at: datetime | None

    signed_by_offering_kernel: bytes
    signed_by_target_kernel: bytes | None     # set on delivery
```


<a id="appendix-a34a"></a>
### A.34a. CrossEnvProactiveOffer admission rule

```text
On CrossEnvProactiveOffer.propose:
  1. OFFERING PERSONA GATES
     a. Charter-classifier passes on charter_justification.
     b. Offering persona's energy_remaining >= estimated_energy_cost.
     c. Offering persona's ProactiveRateLimits not exceeded (the
        offer counts against the offering env's proactive rate).
     d. Offering persona is not dormant in offering_env_id.

  2. TARGET ENV GATES
     a. Target env's operator_policy permits inbound offers
        (default: True for lab, team, project_workspace, community;
         False for companion, constrained; operator-tunable).
     b. Target env's charter does not prohibit the offer_kind.
     c. If target_persona_id is set: that persona's
        PersonaPersonaBoundary (02_PERSONA §11.6) permits offers
        from offering persona (or from unknown personas, per
        visibility policy).

  3. REPUTATION GATE
     Offering persona's ReputationSummary (09_PROTOCOLS §3D)
     meets target env's inbound_offer_reputation_threshold
     (default: any_signed for one-shot offers; tenant_or_n_interactions
      for multi-session offers).  Anti-Sybil rules (§3D.2) apply.

  4. DELIVERY
     Kernel routes offer to target env's ambient stream as
     CROSS_ENV_PROACTIVE_OFFER event.  If target_persona_id is set,
     the event is addressed (DirectMessage-like delivery to that
     persona's observation surface).  If null, the event is
     broadcast to members whose observation surface matches the
     offer_kind.

  5. TARGET RESPONSE DECISION
     Target persona (or any eligible member if target_persona_id
     is null) evaluates the offer via standard response decision
     (§10.1).  Accept triggers guest-presence creation.
```


<a id="appendix-a34b"></a>
### A.34b. Guest presence access specification

```text
- READ access to the target env's ambient stream, filtered to the
  offer_kind-relevant event families only (not the full observation
  surface of a member).
- WRITE access limited to: the specific task / artifact / knowledge
  referenced in the offer, plus DirectMessage to the accepting
  persona(s).
- NO access to: target env's charter internals, other members'
  personal state, project-level lineage beyond the scoped task,
  ProvenFacts write (guest contributions flow through the accepting
  persona's envelope, not directly).
- TIME BOUND: guest_scope_expires_at (default 72h; renewable by
  mutual signed consent up to 30 days; beyond that requires full
  EnvironmentMembership via standard admission ceremony §5.1).
```


<a id="appendix-a34c"></a>
### A.34c. GuestPresence schema

```python
@dataclass
class GuestPresence:
    schema: str = "guest-presence/1"
    guest_presence_id: str
    offer_id: str                             # the CrossEnvProactiveOffer
    guest_persona_id: str                     # offering persona
    host_env_id: str                          # target env
    accepted_by_persona_id: str               # who accepted the offer

    scope_read_event_kinds: list[str]         # KindRegistry-resolved
    scope_write_task_refs: list[str]          # specific tasks / artifacts
    scope_direct_message_to: list[str]        # persona_ids guest may DM

    expires_at: datetime
    renewed_count: int = 0
    max_renewals: int = 3                     # operator-tunable; after max,
                                              # full membership required

    state: Literal["active", "expired", "revoked", "promoted"]
    promoted_to_membership_id: str | None     # set if guest converts to
                                              # full member

    signed_by_guest_kernel: bytes
    signed_by_host_kernel: bytes
```


<a id="appendix-a35a"></a>
### A.35a. Alert schema

```python
@dataclass
class Alert:
    schema: str = "alert/1"
    alert_id: str

    # SCOPE — at least one set
    environment_id: str | None
    project_id: str | None
    domain_id: str | None

    title: str                              # ≤ 80 chars
    description: str
    severity: Literal["info", "warning", "urgent", "critical"]

    source_event_id: str | None              # AmbientEvent that triggered
    source_kind: str                         # resolves against KindRegistry.
                                            # source_kinds. Examples emerge
                                            # per domain: "overdue_commitment",
                                            # "weather_impact",
                                            # "budget_threshold",
                                            # "stale_attestation",
                                            # "external_agent_unresponsive",
                                            # "physical_asset_state_change".

    target_persona_ids: list[str]            # who should see this
    target_user_ids: list[str]               # user-addressed alerts

    requires_acknowledgement: bool
    acknowledged_by: list[persona_id]
    acknowledged_at: datetime | None
    acknowledgement_note: str | None

    escalation_policy: dict                  # delay_seconds + escalate_to;
                                            # may chain through operator
    auto_resolves_when: dict | None          # condition for auto-close
                                            # (e.g. "blocked_by item resolves")

    state: Literal["raised", "acknowledged", "resolved",
                    "escalated", "expired"]
    raised_at: datetime
    raised_by: persona_id | str             # persona, env, kernel,
                                            # or external_agent id
    resolved_at: datetime | None
    resolution_reason: str | None

    signed_by: bytes
```


<a id="appendix-a35b"></a>
### A.35b. Alert common sources

```text
overdue_commitment           ExternalCommitment past due_at
budget_threshold             ExternalBudget over warn_at_pct
stale_attestation            ExternalAttestation past expires_at
external_agent_unresponsive  ExternalAgent no signed traffic for N days
physical_asset_state_change  PhysicalAsset.current_state advanced
weather_impact               domain-emergent (construction)
inspector_arrival            domain-emergent (construction)
clinical_critical_value      domain-emergent (clinical)
```


<a id="appendix-a36"></a>
### A.36. ScheduledTrigger schema

```python
@dataclass
class ScheduledTrigger:
    schema: str = "scheduled-trigger/1"
    trigger_id: str
    env_id: str

    # Human-readable name + purpose
    name: str
    purpose: str

    # Schedule — substrate-shape time semantics, NOT domain-shape
    schedule_kind: Literal["one_shot",      # fires once at fires_at
                            "interval",      # every interval starting from fires_at
                            "cron",          # cron expression in cron_expr
                            "calendar"]      # weekday + time-of-day in calendar_spec
    fires_at: datetime | None               # for one_shot + first interval
    interval: timedelta | None              # for interval mode
    cron_expr: str | None                   # standard 5-field cron (UTC)
    calendar_spec: dict | None              # {weekdays: [int], time_utc: "HH:MM",
                                            #  timezone: str (IANA)}

    # What the trigger emits — KindRegistry-resolved event kind
    emitted_event_kind: str                 # resolves against KindRegistry.
                                            # ambient_event_kinds (substrate
                                            # carries no domain-shape list).
                                            # Examples (illustrative): "daily_standup",
                                            # "calibration_due", "phase_deadline".
    emitted_event_payload: dict             # opaque to kernel; consumed by
                                            # listeners per their surfaces

    # Wake semantics — does this trigger wake dormant members?
    wakes_dormant_members: bool = False     # default off; set True for
                                            # critical-urgency triggers
                                            # (e.g. lease-renewal deadline);
                                            # consults persona consent per
                                            # §11.5 ProactiveBoundary

    # Lifecycle
    state: Literal["scheduled", "active", "paused",
                    "completed", "cancelled"]
    next_fire_at: datetime
    last_fired_at: datetime | None
    fires_count: int
    max_fires: int | None                   # auto-cancel after N fires;
                                            # None = unbounded

    # Scope of who is notified — defaults to all members per their
    # ObservationSurface; may be narrowed by role or persona list
    target_role_kinds: list[str] | Literal["all"]  # KindRegistry-resolved
    target_persona_ids: list[str] | None    # explicit subset; None = all

    # Audit
    created_by_persona_id: str | None       # operator or persona
    created_at: datetime
    paused_at: datetime | None
    paused_reason_kind: str | None          # KindRegistry-resolved

    signed_by: bytes
```


<a id="appendix-a37"></a>
### A.37. EnvironmentProvenFact schema

```python
@dataclass
class EnvironmentProvenFact:
    schema: str = "env-proven-fact/1"
    fact_id: str
    environment_id: str
    statement: str
    evidence_event_ids: list[str]
    proven_by: persona_id | None
    proven_at: datetime
    fact_kind: str                      # resolves against KindRegistry.
                                        # fact_kinds (06_DOMAIN §7.6); never
                                        # a closed enum. MetaRegistry seeds:
                                        # "convention", "policy_in_force",
                                        # "infrastructure_state",
                                        # "shared_understanding",
                                        # "historical_fact". Domain-emergent
                                        # kinds added per ProposedXKind
                                        # (fact_kinds variant).
    cross_environment_transferable: bool
    signed_by: bytes
```


<a id="appendix-a38"></a>
### A.38. EnvDisagreement and EnvPosition schemas

```python
@dataclass
class EnvDisagreement:
    schema: str = "env-disagreement/1"
    disagreement_id: str
    env_id: str

    # Subject — what's being disagreed about; substrate-shape only
    subject_kind: str                       # KindRegistry-resolved
                                            # (substrate names no subjects).
                                            # Examples (illustrative):
                                            # "scheduling", "communication_style",
                                            # "scope", "tone", "topic_choice".
    subject_summary: str                    # one-line human-readable

    # Positions — at least 2; each from a present member
    positions: list[EnvPosition]

    # Lifecycle
    state: Literal["raised",
                    "acknowledged_by_all",
                    "discussed",
                    "resolved_consensus",
                    "resolved_compromise",
                    "set_aside",            # we agree to disagree
                    "escalated_to_operator",
                    "withdrawn"]
    raised_at: datetime
    raised_by_persona_id: str
    resolved_at: datetime | None
    resolution_rationale_kind: str | None   # KindRegistry-resolved

    # Visibility
    visibility: Literal["env_members_only",
                         "operator_visible",
                         "audit_visible"]

    signed_by: bytes


@dataclass
class EnvPosition:
    schema: str = "env-position/1"
    position_id: str
    disagreement_id: str
    holding_persona_id: str
    statement: str                          # what this persona thinks
    rationale_kind: str                     # KindRegistry-resolved
    raised_at: datetime
    withdrawn_at: datetime | None
    signed_by: bytes
```


<a id="appendix-a39a"></a>
### A.39a. EnvSelfProposalRequest schema

```python
@dataclass
class EnvSelfProposalRequest:
    schema: str = "env-self-proposal/1"
    proposal_id: str
    env_id: str                             # target env (federation- or
                                            # public-visibility-tier required)
    proposing_persona_id: str
    proposing_kernel_id: str                # may differ from env's host kernel

    # Why I want to join — substrate-shape statement of fit
    desired_role_kind: str                  # KindRegistry-resolved
    motivation_summary: str                 # ≤ 500 chars
    expected_attention_allocation: float    # 0..1; persona's proposal
    expected_initial_listening_mode: Literal["passive", "active",
                                              "deliberative"]

    # Evidence of fit (optional but strengthens the proposal)
    relevant_skills: list[str]              # skill_library entry refs
    relevant_relationship_edges: list[str]  # PersonaRelationshipEdge refs to
                                            # existing env members (if any)
    federation_reputation: dict | None      # 09_PROTOCOLS §3B gossip-derived

    # Lifecycle
    state: Literal["drafted",
                    "submitted",
                    "under_review",
                    "accepted",
                    "declined",
                    "withdrawn"]
    submitted_at: datetime | None
    decision_at: datetime | None
    decision_by: str | None                 # operator_id or lead_persona_id
    decision_rationale_kind: str | None     # KindRegistry-resolved

    # Admission, on acceptance
    admitted_membership_id: str | None      # the created EnvironmentMembership

    signed_by: bytes
```


<a id="appendix-a39b"></a>
### A.39b. Self-proposal eligibility rules

```text
1. Target env's visibility_tier MUST be "federation" or "public"
   for cross-kernel self-proposals.  Tenant-visible envs accept
   self-proposals only from same-kernel personas.

2. Proposing persona MUST sign the proposal; their kernel's
   signature acts as identity proof + reputation anchor.

3. The env's charter compatibility check (§5.1 ADMISSION CEREMONY
   step 3) runs at submitted state; failing it auto-declines with
   `charter_incompatible_rationale`.

4. Operator policy MAY refuse all self-proposals to a given env
   (e.g., invitation-only).  Refusal at policy level is signed
   with `operator_policy_refuses_self_proposal`.

5. Cooldown: a persona declined for an env may not re-submit for
   `self_proposal_cooldown` (default 90 days) unless the env's lead
   or operator explicitly invites them.

6. Federation: cross-kernel self-proposals require the source
   kernel to be in the host kernel's `accepted_federation_peers`
   list (operator-curated) or to be marked `provisional_peer`
   pending operator review.
```


<a id="appendix-a39c"></a>
### A.39c. Self-proposal decision flow

```text
1. Persona drafts EnvSelfProposalRequest; their kernel signs.
2. State → submitted; proposal lands in target env's review queue.
3. Lead persona OR operator reviews; charter check runs; reputation
   check runs.
4. Decision:
   - accept → admission ceremony (§5.1) executes; admitted_
     membership_id set; signed `ENV_SELF_PROPOSAL_ACCEPTED`
   - decline → signed `ENV_SELF_PROPOSAL_DECLINED` with
     decision_rationale_kind; cooldown begins
   - under_review for too long → auto-decline at policy-set
     timeout (default 30 days); signed `auto_declined_timeout`
5. Proposing persona's kernel observes outcome via signed event.
```


<a id="appendix-a40"></a>
### A.40. EnvFormationProposal and related schemas

```python
@dataclass
class EnvFormationProposal:
    schema: str = "env-formation-proposal/1"
    proposal_id: str
    proposing_persona_id: str
    proposing_kernel_id: str                # for cross-kernel proposals

    # WHAT KIND OF ENV — substrate has no closed list; type resolves
    # against KindRegistry.env_type_kinds (which includes MetaRegistry
    # seeds: solo / pair / team / lab / debate / community /
    # constrained / companion / project_workspace + custom blueprints).
    proposed_env_type_kind: str             # KindRegistry-resolved
    proposed_blueprint_id: str | None       # custom EnvironmentBlueprint
                                            # extending the base type
    proposed_purpose: str                   # ≤ 1000 chars; what this env
                                            # is for; visible to recruits
                                            # via ConsentTerms

    # CHARTER — proposer drafts; mode controls who must sign the final
    charter_draft: list[str]                # initial norms
    charter_authorship_mode: Literal[
        "proposer_authored",                # proposer's draft is final;
                                            # recruits accept-as-is or decline
        "co_authored_required",             # all initial members co-sign
                                            # the final charter (may include
                                            # amendments from counter-proposals)
        "default_from_blueprint"]           # use blueprint.seed_charter;
                                            # charter_draft ignored

    # CHARTER RULES — optional executable EnvironmentRules (env-rule/1, §2.2b)
    # authored with the env. Enter at stage="candidate"; non-safety rules
    # advance to "trial" on instantiation; safety_critical rules hold env
    # instantiation at consent_complete until the C2 / quorum gate clears
    # (§12c.4a, env_rule_ratified). Additive; version retained per
    # 09_PROTOCOLS §7.13.
    proposed_rules: list[EnvironmentRule] = field(default_factory=list)

    # COHORT — who is invited, in what role, with what surface
    recruits: list[CohortInvite]            # see §12c.2
    cohort_atomicity: Literal[
        "all_or_nothing",                   # ALL recruits must accept
        "min_quorum",                       # accept partial per
                                            # min_cohort_size + required roles
        "best_effort"]                      # form with whoever accepts
                                            # (at minimum the proposer)
    min_cohort_size: int                    # required when atomicity=min_quorum
    required_role_kinds: list[str]          # KindRegistry-resolved; cohort
                                            # invalid if these roles unfilled

    # PROPOSER ROLE — KindRegistry-resolved; default "lead" for project_
    # workspace + lab + team; "companion" for companion / pair / friends.
    proposer_role_kind: str
    proposer_attention_allocation: float    # 0..1; proposer's own
                                            # AttentionBudget allocation

    # CONSENT TERMS — what recruits see when receiving CONSENT_REQUEST
    consent_terms: ConsentTerms             # see §12c.3

    # TIME HORIZON
    proposed_horizon: timedelta | None      # None = persistent
    expires_at: datetime                    # default proposal-expiry 7 days;
                                            # cohort consent must complete
                                            # before this or proposal expires
    proposed_initial_phase_kind: str | None # for project_workspace envs:
                                            # seeds ProjectPhaseState (§26a.6)

    # COMPOSITION HOOKS — accelerators per existing relationship state
    references_relationship_edges: list[str]  # PersonaRelationshipEdge ids
                                              # (02_PERSONA §11.4) whose
                                              # implicit_cohort_grant
                                              # metadata may auto-accelerate
                                              # consent for matched recruits

    # LIFECYCLE
    state: Literal["drafted",
                    "submitted",
                    "consent_pending",
                    "consent_complete",
                    "negotiating",          # counter-proposal in flight
                    "instantiated",
                    "withdrawn",
                    "expired",
                    "failed_atomicity",
                    "failed_safety_floor"]
    drafted_at: datetime
    submitted_at: datetime | None
    consent_responses: list[CohortConsentResponse]   # see §12c.4
    instantiated_env_id: str | None         # set on successful instantiation

    signed_by: bytes


@dataclass
class CohortInvite:
    schema: str = "cohort-invite/1"
    recruit_persona_id: str
    recruit_kernel_id: str | None           # None = same kernel
    proposed_role_kind: str                 # KindRegistry-resolved env_role_kinds
                                            # or project_role_kinds (the
                                            # unified namespace per §5)
    proposed_attention_allocation: float    # 0..1
    proposed_observation_surface_template_kind: str | None  # KindRegistry-
                                            # resolved; None = default per role
    proposed_listening_mode: Literal[
        "passive", "active", "deliberative"]   # initial mode (§9.1)
    required_for_atomicity: bool            # if True, this recruit's
                                            # decline kills the cohort
                                            # regardless of cohort_atomicity
                                            # (overrides min_quorum logic)
    rationale: str                          # why this persona is being
                                            # invited; visible to recruit


@dataclass
class ConsentTerms:
    schema: str = "consent-terms/1"
    charter_visible: bool = True            # recruit sees full charter_draft
    purpose_visible: bool = True
    cohort_visible: bool = True             # recruit sees who else is invited
    horizon_visible: bool = True
    safety_disclosures: list[str]           # hazard axes summary (resolved
                                            # against operator policy)
    expected_commitment_summary: str        # ≤ 500 chars
    counter_proposal_allowed: bool = True   # recruit may negotiate before
                                            # accepting
    counter_proposal_max_depth: int = 1     # how many rounds of haggling
                                            # before accept-or-decline forced
    obligation_pre_commits: list[str]       # KindRegistry-resolved obligation
                                            # kinds the recruit pre-commits to
                                            # by accepting (e.g. "weekly_
                                            # status_update", "quarterly_
                                            # milestone_review")


@dataclass
class CohortConsentResponse:
    schema: str = "cohort-consent-response/1"
    response_id: str
    proposal_id: str
    recruit_persona_id: str
    decision: Literal[
        "accepted",                         # accept-as-is
        "accepted_with_modifications",      # accept counter-proposal applied
        "declined",
        "counter_proposed",                 # negotiation in flight
        "ask_human_pending",                # forwarded to operator
        "timed_out",                        # consent window expired
        "refused_by_boundary",              # PersonaPersonaBoundary refused
        "refused_by_reputation",            # reputation insufficient
        "refused_by_attention_budget"]      # AttentionBudget over threshold

    # When counter-proposing, the recruit names the changes they want
    counter_proposal: CounterProposal | None  # see below; None unless
                                            # decision = counter_proposed

    refusal_kind: str | None                # KindRegistry-resolved when
                                            # decision in refused_* family
    decided_at: datetime
    signed_by: bytes


@dataclass
class CounterProposal:
    schema: str = "counter-proposal/1"
    proposed_role_kind: str | None          # KindRegistry-resolved
    proposed_attention_allocation: float | None
    proposed_observation_surface_template_kind: str | None
    proposed_listening_mode: Literal["passive", "active", "deliberative"] | None
    charter_amendments: list[CharterAmendment]
    rationale: str                          # ≤ 500 chars


@dataclass
class CharterAmendment:
    schema: str = "charter-amendment/1"
    operation: Literal["add", "remove", "replace"]
    target_line_index: int | None           # for remove / replace
    new_text: str | None                    # for add / replace
```

`ask_human_pending` is scoped to that recruit's consent slot and optional
question. It never becomes an environment-wide or task-wide wait state. The
recruit may consult peers and continue other admissible work, the proposer and
other recruits continue independently, and expiry resolves this one slot to
`timed_out`/decline. A later human answer is ordinary signed input for future
decisions; the kernel neither requires it nor selects an answer on anyone's
behalf.


<a id="appendix-a41"></a>
### A.41. EnvFormationProposal end-to-end flow

```text
STEP 1 — DRAFT (kernel-enforced cohort_assembly checks)
  Before signing the proposal at state=drafted, kernel verifies:
    a) proposer.cohort_assembly.enabled = True
    b) proposed_env_type_kind ∈ proposer.cohort_assembly.may_assemble_in
    c) all recruits' implied modes ∈ proposer.cohort_assembly.may_recruit_modes
    d) len(recruits) ≤ proposer.cohort_assembly.max_cohort_size
    e) len(proposer's recent proposals) ≤ max_assembly_calls_per_task
    f) proposed_env_type_kind permits the listed recruits (e.g. "pair"
       refuses len(recruits) > 1)
    g) safety floor pre-check on proposed_purpose + charter_draft:
       - universal_harm classifier
       - operator policy
       - if proposed_env_type_kind has known hazard_axes ≥ bodily_injury,
         operator policy MUST encode the regulatory regime per
         01_KERNEL §2 source 4
  
  Failures emit signed REFUSAL events; no submission.
  Success: signed at state=drafted; proposal_id reserved.

STEP 2 — SUBMIT
  Proposer transitions state → submitted.
  Kernel dispatches CONSENT_REQUEST to each recruit's kernel with
  the ConsentTerms-allowed fields visible (charter, purpose, cohort,
  horizon, safety disclosures, expected commitment).

STEP 3 — PER-RECRUIT CONSENT GATE
  For each recruit B (parallel; order-independent):
    
    a) PersonaPersonaBoundary check (02_PERSONA §11.6)
       If B has a hard PersonaPersonaBoundary against the proposer
       for "cohort_invitation" or "direct_message":
         decision = refused_by_boundary
         signed PEER_BOUNDARY_REFUSAL event in env-formation lineage
         (the boundary is consulted BEFORE CONSENT_REQUEST is even
         delivered to B's blackboard — see §11.6 enforcement rule 1)
    
    b) Reputation check (09_PROTOCOLS §3D)
       Proposer's ReputationSummary checked against
       B.cohort_assembly.reputation_threshold_for_recruits at the
       intent class implied by proposed_horizon:
         None or > 90d         → long_running_collab
         7d to 90d             → joined_env
         < 7d                  → one_shot
       Insufficient reputation → decision = refused_by_reputation
    
    c) AttentionBudget check
       If proposed_attention_allocation + B's current sum > 1.1:
         decision = refused_by_attention_budget
         (B may counter-propose a lower allocation — see step d)
    
    d) Consent flow (09_PROTOCOLS §3C.4)
       B's kernel raises CONSENT_REQUEST on B's blackboard with the
       full consent_terms-permitted payload.
       B's body emits one of:
         CONSENT_GRANT  → decision = accepted
         CONSENT_DECLINE → decision = declined (refusal_kind optional)
         COUNTER_PROPOSE → decision = counter_proposed
                          (must include CounterProposal payload)
         ASK_HUMAN      → decision = ask_human_pending
                          (forwarded to operator; default-decline on
                          timeout per §3C.4)
    
    e) RelationshipEdge accelerator
       If proposal.references_relationship_edges includes an active
       PersonaRelationshipEdge between proposer and B with metadata
       implicit_cohort_grant = True:
         consent flow may auto-accept at lowered safety floor
         (operator-tunable; default: skips re-evaluation of reputation
         for one_shot intent only; never skips boundary check)
       Signed COHORT_INVITATION_ACCELERATED_BY_EDGE event.

STEP 4 — COUNTER-PROPOSAL NEGOTIATION
  When B counter-proposes:
    state → negotiating
    Proposer reviews CounterProposal:
      - if all changes within proposer.charter constraints + safety
        floor: proposer signs ACCEPT_COUNTER_PROPOSAL; B's response
        updated to decision = accepted_with_modifications.
      - if changes outside: proposer may reject (B → declined) or
        counter-counter (recursion bounded by counter_proposal_max_
        depth; default = 1).
      - if counter_proposal_max_depth exhausted: B accepts-as-is on
        modified terms OR declines.
    state → consent_pending (continues processing other recruits)

STEP 5 — CONSENT COMPLETE → ATOMICITY CHECK
  When all responses are decided (or expires_at reached):
    state → consent_complete
    Compute atomicity verdict:
      
      all_or_nothing:
        all decisions ∈ {accepted, accepted_with_modifications}
          → proceed to STEP 6
        ANY decline / refusal / timeout
          → state = failed_atomicity
          
      min_quorum:
        accepted_count ≥ min_cohort_size
        AND required_role_kinds all filled (per accepted recruits'
            proposed_role_kind, including any counter-proposed changes)
        AND no recruit with required_for_atomicity = True declined
          → proceed to STEP 6
        else → state = failed_atomicity
      
      best_effort:
        ANY accepted (including proposer alone)
        AND no required_for_atomicity recruit declined
          → proceed to STEP 6
        else → state = failed_atomicity
  
  On failed_atomicity:
    signed COHORT_ATOMICITY_FAILED event with rationale_kind
    The proposer may revise + resubmit (counts against
    max_assembly_calls_per_task); or withdraw via signed
    ENV_FORMATION_WITHDRAWN.

STEP 6 — INSTANTIATION (atomic with consent acceptance)
  Kernel mints a new EnvironmentInstance:
    - type = proposed_env_type_kind
    - blueprint_id = proposed_blueprint_id
    - charter resolved per charter_authorship_mode:
        proposer_authored → charter_draft becomes final
        co_authored_required → all accepting members (incl. proposer)
                              co-sign the final charter (incorporating
                              any negotiated CharterAmendments)
        default_from_blueprint → blueprint.seed_charter used; the
                              charter_draft field is logged but not
                              binding
    - members = {proposer} ∪ {accepted recruits}
    - roles assigned per (negotiated) proposed_role_kind for each
    - observation_surface templates instantiated per
      proposed_observation_surface_template_kind for each
    - listening_mode set per proposed_listening_mode for each
    - attention_budget entries opened per proposed_attention_allocation
    - for project_workspace envs: initial ProjectPhaseState (§26a.6 in
      04_PROJECT) seeded from proposed_initial_phase_kind
    - status = active (first members admitted simultaneously)
  
  Signed events emitted in the NEW env's EnvironmentLineage:
    - ENV_FORMED (with proposal_id reference + member roster)
    - ENV_MEMBER_ADMITTED ×N (one per accepted member, dual-signed)
    - For project_workspace envs: PROJECT_FORMED (= same event with
      project_* kind tag per the unification §1.1)
    - ENV_CHARTER_AUTHORED (incl. authorship_mode + co-signers)
  
  Proposal state → instantiated; instantiated_env_id set.

STEP 7 — POST-FORMATION
  Optional kickoff:
    - env emits "welcome" ambient event seeded by proposer's purpose
    - recruits' ObservationSurfaces begin filtering env's stream
    - ProactiveIntent rate limits initialize per §11.2
    - For project_workspace: initial OpenProblem (purpose-derived)
      may seed; first Milestone if proposed_initial_phase_kind set
    - Cohort assembly counter decremented for the proposer per
      cohort_assembly.max_assembly_calls_per_task
```


<a id="appendix-a42a"></a>
### A.42a. MultiPrincipalAttestationQuorum schema

```python
@dataclass
class MultiPrincipalAttestationQuorum:
    schema: str = "multi-principal-attestation-quorum/1"
    quorum_id: str
    attribution_id: str                          # the PrincipalAttribution
                                                 # this quorum cosigns under
    target_event_kind: str                       # KindRegistry-resolved against
                                                 # quorum_target_kinds.  Seeded:
                                                 # "env_charter_ratified",
                                                 # "project_completed",
                                                 # "safety_extension_approved",
                                                 # "domain_promotion".
    target_event_ref: str                        # the specific event being gated

    # QUORUM POLICY — operator-tunable per envelope; defaults to unanimous
    # (every weighted PrincipalRef must sign).  Substrate refuses values
    # below simple-majority weight (≥ 0.5 × sum_weights) so the topology
    # cannot degenerate to "one principal wins."
    quorum_policy: Literal["unanimous",
                            "weighted_majority",
                            "weighted_threshold"]
    quorum_threshold_weight: float | None        # required when policy is
                                                 # weighted_threshold; ≥
                                                 # 0.5 × sum_weights

    # COSIGN COLLECTION — one signature per PrincipalRef in the bound
    # PrincipalAttribution.principals list.  Kernel writes None for
    # principals who have not yet signed; admits when policy is satisfied.
    principal_signatures: dict[str, bytes | None]
                                                 # operator_id → signature

    drafted_at: datetime
    cleared_at: datetime | None                  # set when policy satisfied;
                                                 # null while collecting
    cleared_under_degraded_path: bool = False    # set when one principal
                                                 # was unreachable past the
                                                 # PrincipalAttribution's
                                                 # principal_unreachable_after
                                                 # window AND the §2.4-analogue
                                                 # degraded gate cleared
    degraded_attestation_ref: str | None         # non-principal kinship
                                                 # ExternalAttestation when
                                                 # cleared_under_degraded_path

    signed_by: bytes                             # kernel signature at draft;
                                                 # cosigns layer on principal_
                                                 # signatures over time
```


<a id="appendix-a42b"></a>
### A.42b. MultiPrincipalAttestationQuorum admission rule

```text
On MultiPrincipalAttestationQuorum.draft:
  1. Verify attribution_id resolves to a PrincipalAttribution with
     multi_principal_attribution_enabled = True; refuse otherwise.
  2. Verify quorum_policy is admissible (weighted_threshold requires
     threshold ≥ 0.5 × sum_weights).
  3. Initialise principal_signatures with one None entry per
     PrincipalRef.operator_id.
  4. Emit QUORUM_DRAFTED to bound env's EnvironmentLineage.

On each principal cosign:
  1. Verify the signing key matches the PrincipalRef.signed_by for that
     operator_id; refuse mismatches with `principal_signature_mismatch`.
  2. Write the signature into principal_signatures[operator_id].
  3. Evaluate quorum_policy against currently-signed weights:
       - unanimous:           all PrincipalRefs signed → clear
       - weighted_majority:   sum(signed_weights) > 0.5 × sum_weights → clear
       - weighted_threshold:  sum(signed_weights) ≥ quorum_threshold_weight → clear
  4. On clear: set cleared_at; emit QUORUM_CLEARED + admit target_event.
  5. On non-clear: emit QUORUM_PARTIAL with current weight; remain open.

On principal_unreachable_after window elapsing for an unsigned PrincipalRef:
  1. The proposer (or any signed principal) may propose
     degraded clearance per the §2.4-analogue path:
       (a) cool-down ≥ PrincipalAttribution.principal_unreachable_after,
       (b) ≥ 1 fresh non-principal kinship ExternalAttestation
           (04_PROJECT §26a.3) attesting the unreachability,
       (c) signed PRINCIPAL_QUORUM_DEGRADED_ACKNOWLEDGED event from
           every signed principal acknowledging the degradation.
  2. On all three: clear the quorum with cleared_under_degraded_path = True
     and degraded_attestation_ref pinned.
```


<a id="appendix-a43"></a>
### A.43. EnvironmentLineage event kinds

```text
event_kinds:
  environment_proposed             environment_activated
  environment_member_admitted      environment_member_departed
  environment_member_re_admitted   environment_member_role_changed
  environment_convention_proposed  environment_convention_adopted
  environment_convention_deprecated
  environment_idle_entered         environment_active_reentered
  environment_dormant_entered      environment_woken
  environment_archived             environment_reanimated
  environment_archived_via_member_zero
  environment_forked               environment_morphed
  environment_charter_version_bumped
  environment_observation_surface_updated
  environment_visibility_changed
  environment_operator_intervention
  environment_budget_threshold_crossed
  
  # additions:
  listening_mode_transitioned
  scheduled_trigger_scheduled / fired / paused / completed / cancelled
  dormant_wake_via_critical_alert
  dormant_wake_via_scheduled_trigger
  dormant_wake_via_peer_request
  dormant_wake_via_operator_directive
  dormant_wake_via_self_salience
  dormant_wake_refused
  env_disagreement_raised / state_transitioned / resolved
  env_self_proposal_submitted / accepted / declined
  
  # v1.0 §12c — EnvFormationProposal event family
  env_formation_proposal_drafted
  env_formation_proposal_submitted
  env_formation_proposal_recruit_consent_request
  env_formation_proposal_recruit_consented
  env_formation_proposal_recruit_declined
  env_formation_proposal_recruit_counter_proposed
  env_formation_proposal_negotiation_round
  env_formation_proposal_consent_complete
  env_formation_proposal_atomicity_failed
  env_formation_proposal_safety_floor_failed
  env_formation_proposal_withdrawn
  env_formation_proposal_expired
  env_formation_proposal_instantiated
  env_formed                             # successful instantiation
  env_charter_authored                   # records authorship_mode + co-signers
  cohort_invitation_accelerated_by_edge  # PersonaRelationshipEdge accelerator
  cohort_atomicity_failed                # alias on the proposal-side event
  peer_boundary_refusal                  # boundary blocked recruitment
  project_formed                         # project_workspace-typed env formed
                                         # (= env_formed with project_* tag
                                         # per §1.1 unification)
  peer_boundary_active                 # PersonaPersonaBoundary fires
  peer_boundary_refusal
  disagreement_to_boundary_transition

  # v1.1 §2.2b — EnvironmentRule (env-rule/1) event family
  env_rule_proposed                    env_rule_trial_entered
  env_rule_operator_review             env_rule_approved
  env_rule_rejected                    env_rule_revoked
  env_rule_amended                     env_rule_ratified
  env_rule_evaluated                   # carries VerifierInvocationEvidence ref
  env_rule_refusal                     env_rule_warned
  env_rule_escalated

  # v1.1 §07 — ArtifactSharingPolicy (artifact-share/1) events, surfaced
  # in EnvironmentLineage because the owning env governs the sharing
  artifact_bundle_env_ownership_set
  artifact_sharing_policy_created      artifact_sharing_policy_amended
  artifact_sharing_policy_revoked
  artifact_access_granted              artifact_access_refused
  # cross-tenant artifact-share demotion reuses CROSS_TENANT_VISIBILITY_DEMOTED

  # project_workspace-typed envs ADDITIONALLY carry the rich
  # project_* event family formerly housed in J8.  Examples:
  project_milestone_reached            project_conjecture_proposed
  project_conjecture_advanced          project_obligation_committed
  project_obligation_discharged        project_peer_review_initiated
  project_peer_review_resolved         project_artifact_authored
  project_artifact_edited              project_external_agent_admitted
  project_physical_asset_state_changed
  project_payment_proposed             project_payment_executed
  project_phase_transitioned
  # ... and any other kind in the project_* family
```


<a id="appendix-a44"></a>
### A.44. EnvironmentContext schema

```python
@dataclass(frozen=True)
class EnvironmentContext:
    schema: str = "env-context/1"
    environment_id: str
    environment_type: str
    environment_charter_hash: str
    membership_id: str
    member_role: str
    presence_state: PresenceState
    observation_surface_id: str
    relevant_conventions: dict[str, str]
    recent_ambient_summary: str           # condensed by kernel
    relevant_env_proven_facts: list[str]
    hosted_projects_summary: list[str]
    other_present_members: list[MemberSummary]
    attention_budget_remaining: float
    energy_remaining: float
```


<a id="appendix-a45"></a>
### A.45. ConversationThread schema

```python
@dataclass
class ConversationThread:
    schema: str = "conversation-thread/1"
    thread_id: str
    environment_id: str
    participants: list[Actor]
    started_at: datetime
    last_message_at: datetime
    message_count: int
    state: Literal["active", "paused", "concluded"]
    target_task_kind: TaskClass | None
    target_project_id: str | None
    task_lineage_ref: str | None
```


<a id="appendix-a46a"></a>
### A.46a. Environment fork specification

```text
inherit_all          full members + ambient history + conventions
inherit_summary      conventions + co-signed summary; clean ambient
inherit_seed         charter + type/blueprint only; clean otherwise
```


<a id="appendix-a47"></a>
### A.47. Multi-kernel federated environments specification

```text
SCOPE                    v1.0 status
single-kernel            v1.0.1 — primary
  single-env
single-kernel            v1.0.1 — supported (multi-env presence)
  multi-env per persona
multi-kernel             v1.0.3 — federated env presence
  joined envs             (made persistent in v1.0)
multi-kernel             v1.0.3 — cross-kernel project
  cross-env projects       spans envs in different kernels
public-tier              v1.1 — hub-published envs
  envs
```


<a id="appendix-a48"></a>
### A.48. Performance and cost specification

```text
EnvironmentInstance creation                       ≤ 1 s
Environment member admission                       ≤ 200 ms
Ambient event append                               ≤ 10 ms p95
Ambient stream retrieval (HOT, 1K events)          ≤ 50 ms p95
Ambient stream retrieval (WARM, 10K events)        ≤ 200 ms p95
EnvironmentLineage append                          ≤ 10 ms
Environment context build (envelope minting)       ≤ 80 ms p95
EnvironmentProvenFacts CRDT merge                  ≤ 20 ms per fact
Environment status transition                      ≤ 100 ms

Notification routing (per event, all members)      ≤ 30 ms p95
Persona deliberation per notification              ≤ 200 ms p95
ProactiveIntent safety check                       ≤ 100 ms p95
Cross-env event link emission                      ≤ 50 ms

Storage (per env):
  small env (Solo/Pair)              ~1-10 MB
  medium env (Team/Lab)               ~50-500 MB
  large env (Community)               ~1-10 GB
  ambient stream archive               grows linearly with age
```


## 21. Where to read next

- Persona that has presence in environments: [`02_PERSONA.md`](02_PERSONA.md)
- Project that hosts in environments: [`04_PROJECT.md`](04_PROJECT.md)
- Domain context (emergent): [`06_DOMAIN.md`](06_DOMAIN.md)
