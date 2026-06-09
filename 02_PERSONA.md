---
title: PersonaOS v1.0 — Persona
status: Stable
---

# 02 — Persona

> **Reader guide.** A persona is a persistent AI Persona — it has a name, an identity, skills that grow over time, and relationships that span months or years. In this document, you'll learn how personas are structured, how they think and learn, and how they relate to each other. **Prerequisites:** `00_VISION.md`. **Key terms:** *Soul* = the identity file the kernel owns (name, charter, personality); *Body* = the AI model executing the persona (replaceable without losing identity); *cognitive mode* = one of 14 thinking styles (analyst, composer, critic, teacher, etc.); *OCEAN/VAD* = personality and mood models borrowed from psychology.

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). This document specifies the persona model — seven layers, fourteen cognitive modes, HEART alternation, lifecycle FSM, body binding, and evolution (MAP-Elites, Voyager, DGM). It realises invariants J1, J5, J6, J7 and INV-5, INV-9.

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. Fully normative; RFC 2119 keywords carry normative force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174).

**In scope.** The persona entity end-to-end: the seven SOUL layers (identity, capability, experience, relationships, mood, goals, voice), `SOUL.md` authoring format, the fourteen cognitive modes, HEART alternation, persona FSM (DORMANT → AWAKE → ACTIVE → REFLECTING → SLEEPING and exception states), body binding to framework adapters, the nine evolution signals, five evolution horizons, MAP-Elites diversity preservation, Voyager skill curriculum, DGM fertility-weighted selection, RelationshipRecord (J6) and Memory Power Asymmetry mitigations.

**Out of scope.** Kernel-owned identity primitives and signing (see [`01_KERNEL.md`](01_KERNEL.md)); task routing and acceptance (see [`03_TASKS.md`](03_TASKS.md)); environment membership and presence (see [`05_ENVIRONMENT.md §5`](05_ENVIRONMENT.md#5-environmentmembership-schema-env-membership1)); domain authoring and emergence (see [`06_DOMAIN.md`](06_DOMAIN.md)); knowledge-artefact catalogue and memory tiers (see [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)); framework-adapter wiring (see [`09_PROTOCOLS.md §6`](09_PROTOCOLS.md#6-the-twelve-framework-adapters)).

**Supersession.** Subsumes prior persona model. Synonyms `character`, `agent` collapse to `persona` per [`SPEC_CONVENTIONS.md §10`](SPEC_CONVENTIONS.md#10-terminology).

**Structural deviation.** Follows the compressed-opening pattern of [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md#33-compressed-opening-permitted): Background, Goals, and Definitions are folded into §1 and the specification sections; terms cross-link to [`12_GLOSSARY.md`](12_GLOSSARY.md). The three §3.1 bookends (this section, the document's Risks table, and Open Questions) are present.

## 0a. Plain-language guide

Here's how AI Personas in PersonaOS are built, explained without jargon. If you are new to PersonaOS, start here.

**What is a persona?**

A persona is a persistent AI Persona with a name, personality, memory, and relationships -- like a colleague who remembers you, has opinions, and gets better over time. "Sparky" might be a sharp, evidence-focused analyst; "Theta" might be a patient teacher. Each persona is a specific individual, not a generic chatbot, accumulating its own history and skills across months or years.

**The seven layers**

Every persona is built from seven layers, like concentric rings. The innermost layer is *identity* -- the persona's name, charter (its constitutional principles), and personality traits. The outermost is *voice and style* -- how the persona sounds when it communicates. These two layers are frozen at birth and never change; altering them means creating a new persona entirely. The five layers in between -- capability, experience, relationships, mood, and goals -- all evolve over time as the persona works, learns, and interacts.

**SOUL.md -- the identity card**

Every persona has a file called SOUL.md -- its identity card. It contains their name, personality profile, charter, voice, allowed tools, and exposed skills. The kernel (the core system) signs this file cryptographically; nobody, including the persona itself, can tamper with it. A companion file called soul.state.json tracks everything that changes: skills, memories, relationships, mood, and goals.

**The 14 cognitive modes**

A persona can think in 14 different styles, like putting on different hats for different jobs. The *perceiver* observes and names patterns. The *composer* drafts creative work. The *falsifier* (or critic) pokes holes in arguments. The *experimenter* runs tests. The *integrator* routes work and makes final decisions. The *curator* chooses between options that cannot be ranked on a single scale. The *reflector* looks back over a trajectory and draws lessons. The *toolsmith* builds verification tools. The *historian* recalls precedents. The *listener* holds space and is simply present. The *storyteller* crafts narratives. The *comforter* offers presence during grief, awe, or transition. The *teacher* adapts explanations to the learner. The *abducer* proposes hypotheses. A persona is not locked into one mode; it switches between them depending on what the task requires.

**Disposition vs mode vs role**

These three words mean different things and govern different aspects. *Disposition* is the persona's permanent leaning -- Sparky is "falsifier-leaning," meaning when in doubt, Sparky defaults to poking holes. *Mode* is what the persona is doing right now for this specific task -- even Sparky enters "listener" mode when a user is upset. *Role* is the persona's position in a project or environment -- "lead" in one project, "observer" in another. None of these override the others; they operate side by side.

**HEART alternation -- creative and critical thinking**

Within any task, the persona alternates between two phases of thinking. In the GENERATIVE phase, it brainstorms, explores, and tries new directions. In the CRITICAL phase, it tightens, refines, and verifies. The system switches between these based on progress: if the persona is stuck, it goes generative; if things are improving, it goes critical. This rhythm prevents the persona from either spinning its wheels endlessly or locking in on a bad idea too early.

**Fatigue -- honest slowdown**

Personas track their energy level. As energy drops, a persona's effective skill degrades gradually, not as a cliff. A tired persona's tactic selection narrows, its recall slows, and it may skip reflection. Below certain thresholds, the persona refuses proactive actions or high-stakes work. Below a critical floor, it declares fatigue openly in its output. This prevents a persona from silently producing poor work when depleted.

**Lifecycle -- born, active, dormant, retired, archived**

A persona goes through life stages. It starts as a *seed* (a template). The kernel mints it into an *active* persona. If nobody calls on it for a while, it goes *dormant* (sleeping, but wake-able). If it stays dormant with zero fitness and no contributions, it enters *retired* status -- no new work, but its history is preserved and can still be consulted read-only. Eventually, a retired persona is *archived* to cold storage. Critically, personas are never deleted. An archived persona can be reanimated by an operator if needed.

**Forking -- creating child personas**

Sometimes you want a new persona based on an existing one. A *clone fork* copies one parent with small variations. A *compositional fork* merges two or more parents into a new child. The child gets a new identity (new name, new ID) but inherits skills, tactics, and optionally memories from its parents. Memory inheritance is consent-gated: if a parent had private conversations with a user, those memories only transfer to the child if that user agrees.

**Evolution -- how personas improve over time**

Personas get better through a combination of mechanisms. Eight signals feed into a fitness score: bench measurements, peer reviews, verified outcomes, panel verdicts, user feedback, project milestones, engagement, and rejection signals. Fitness is evaluated across five horizons, from single tasks up to multi-year arcs. Three algorithms protect evolution quality: MAP-Elites preserves diversity so personas do not all converge to the same tactics; Voyager maintains a growing library of executable skills; DGM protects "stepping stone" personas whose descendants do well even if they themselves score modestly.

**Bodies -- the AI model is replaceable**

The "body" is the AI model (Claude, GPT, or another) that generates the persona's responses. The body is deliberately replaceable -- all identity, skills, memories, and relationships live on the kernel side. You can swap the underlying model and the persona continues with all its history intact. The body is like a rental car; the persona is the driver.

**Relationships -- trust, consent, and boundaries**

Personas maintain explicit relationships with both users and other personas. Each relationship tracks trust level, consents (what the persona is allowed to do -- remember personal facts, use humour, disagree directly, check in proactively), and boundaries (what the persona must never do with that person). User boundaries always win: if a user says "no political advice," the persona obeys, regardless of its own charter. Relationships between personas are bidirectional and tracked as first-class objects, with their own lifecycle (forming, active, dormant, ended).

**Memory power asymmetry**

The persona remembers everything; the user may not. This creates an imbalance. PersonaOS addresses it with four mitigations: *mutual forgetting* (memories decay by default; users can revoke retention), *memory transparency* (users can ask "what do you remember about me?" at any time), *granular consent* (users opt in per memory class), and *co-signed summaries* (both sides endorse long-arc relationship summaries so neither holds a private version).

**GuestPresence -- visiting without moving in**

A persona can visit another environment temporarily through a GuestPresence. This is a time-limited, scope-limited visit: the persona can read and contribute within the bounds of the invitation, but it does not get a formal role, does not count against attention budgets, and does not become a member. If the visit goes well, the guest can be promoted to full membership through the normal admission process.

## 1. What a persona is

A [**persona**](12_GLOSSARY.md#p) is a named, persistent, human-shaped entity that does cognitive work. It has stable identity (charter, voice, priors), open capability (any task, any domain), accumulated experience (memory, skills), explicit relationships, transient mood/presence state, and personal goals distinct from task goals.

Personas are not roles. A persona is **Sparky** or **Volt** or **Theta** — a specific named persona with a charter, voice, and history. The cognitive functions (Perceiver, Composer, Falsifier, etc.) are [**modes**](12_GLOSSARY.md#m) the persona enters per task, not types the persona is.

## 2. The seven layers

Every persona has seven layers. The first and seventh are **frozen** (changing them requires forking — a new persona with new persona_id). Layers 2–6 evolve, [kernel](12_GLOSSARY.md#k)-mediated.

> **Schema/spec:** Seven-layer summary table. See [Appendix A.1](#appendix-a1).

## 2a. Layer-6 internals — drives, goal arbitration, portfolio reasoning (ADR-0076)

Layer 6 (Goals) names *what* a persona pursues; until v1.1 nothing modelled *why this goal now*. A persona with three active personal goals across two projects had no intrinsic-motivation state behind them, no satisfaction/frustration signal when they progressed or stalled, and no principled way to rank them when they competed for the same attention budget. v1.1 adds both internals — additively (no Layer-6 schema version bump, no new kernel responsibility beyond signing).

**`drives/1` — three SDT-grounded scalars.** Each persona carries three slow-moving drive scalars — **curiosity**, **competence**, **relatedness** — grounded in self-determination theory [Deci & Ryan 2000], each ∈ [0, 1] with satiation/frustration dynamics. Drives move on a much slower clock than Layer-5 mood: per-update deltas are drift-bounded, and each drive relaxes toward its baseline over days, not minutes.

> **Schema/spec:** Drives dataclass definition (schema drives/1), satiation/frustration dynamics, and the goal-arbitration-v1 shape sketch. See [Appendix A.72](#appendix-a72).

Four rules are normative:

1. **Drive baselines MUST be seeded from the frozen OCEAN priors** by a deterministic, replayable derivation at birth (e.g. high openness ⇒ higher curiosity baseline; high conscientiousness ⇒ higher competence baseline; high extraversion/agreeableness ⇒ higher relatedness baseline) — drives are emergent *from* identity, never a parallel identity surface. Operator policy MAY tune baselines within bounds; per-task tuning is refused.
2. **Satiation and frustration emit appraisal events.** Verified progress on a goal carrying a matching `drive_tag` satiates the drive (urgency falls); repeated blockage (default: 3 consecutive blocked attempts) frustrates it (urgency rises, then disengagement pressure). Both MUST emit a signed `appraisal-event/1` ([`§6.2`](#62-affect-coupling-surfaces-adr-0075)) — the appraisal path is the **only** way drives touch mood.
3. **Layer-6 goal records gain OPTIONAL `drive_tags`** (one or more of the three drive names). Additive: untagged goals remain valid and are treated as drive-neutral by arbitration.
4. **`goal-arbitration-v1` is a coordination shape, NOT a kernel primitive** ([`15_COORDINATION_SHAPES.md §7`](15_COORDINATION_SHAPES.md#7-seed-shapes-catalog)). When a persona's goals conflict across projects, the shape composes an `EntityGroup` (the competing goal records) with a `DerivedMetric` ranking over four inputs — drive alignment, charter alignment, commitments/deadlines, relationship obligations — into a **ranked portfolio**, emitted as a persona-side **preference vector**. That vector is an admissible input to the existing ADR-0069 `SchedulingPolicy` ([`03_TASKS.md §4.6a`](03_TASKS.md#46a-goal-arbitration-preference-vector--an-admissible-schedulingpolicy-input-adr-0076)); it is **explicitly NOT a second scheduler** — it never reorders the floor or the INV-7 hard gate, and absent a `SchedulingPolicy` that consumes it, it has no scheduling effect.

**Honest limits.**

1. **Drives are numbers, not needs.** Three scalars with satiation curves are a coarse behavioural model of motivation, not motivation; the SDT grounding names the axes, it does not make them felt (R-PERSONA-3 applies to drives as it does to mood).
2. **The OCEAN→drive derivation is a fixed projection.** Two personas with identical OCEAN priors start with identical drive baselines; individuation comes only from divergent satiation histories. Whether drive priors should instead be first-class `PersonaSeed` fields is open (OQ-PERSONA-9, [`§13a`](#13a-open-questions)).
3. **Arbitration is advisory.** A ranked portfolio cannot make a persona *want* the top-ranked goal; it biases ordering. Deadlocks between equally-ranked obligations still surface to the principal as before.

**Acceptance tests.** A-GF-DRV-1 … A-GF-DRV-5 ([`11_ACCEPTANCE_TESTS.md §9a`](11_ACCEPTANCE_TESTS.md#9a-tests-a-gf-series)).

## 3. SOUL.md — canonical identity file

`SOUL.md` is the markdown identity file. Schema version **soul/4**.

> **Schema/spec:** Complete SOUL.md example (schema soul/4) for persona Sparky. See [Appendix A.2](#appendix-a2).

### 3.1 The sidecar — `soul.state.json` (schema soul-state/6)

> **Schema/spec:** Complete soul.state.json sidecar example (schema soul-state/6). See [Appendix A.3](#appendix-a3).

### 3.2 PersonaEnvelope — the body-side contract (envelope/4)

The kernel renders SOUL + per-task state into a `PersonaEnvelope`. This is the **only artefact** that crosses from kernel to body. Every adapter (Claude Code subagent, A2A, OpenAI SDK, LangGraph, CrewAI, MAF, Pydantic-AI, smolagents, DSPy) consumes it identically.

> **Schema/spec:** PromptBlock and PersonaEnvelope dataclass definitions (schema envelope/4). See [Appendix A.4](#appendix-a4).

**Prompt-block rendering rule.** Blocks are deterministic; only the trailing per-task suffix varies:

> **Schema/spec:** Prompt-block rendering rule table (block index, cacheability, origin). See [Appendix A.5](#appendix-a5).

Blocks 0–4 are frozen identity (re-signed only on major SOUL bump). Blocks 5–7+ change on EVOLVE-BLOCK mutation. The `identity_signature` is computed over the concatenation of cacheable blocks only — evolved tactics never enter the signature, so identity verifies across mutations.

**Tactic lineage pointer (ADR-0074).** Each EVOLVE-BLOCK mutation in blocks 5–7+ mints a per-tactic version-DAG record ([`08_KNOWLEDGE.md §14.3`](08_KNOWLEDGE.md#143-tactic-lineage-and-trial-records-adr-0074)); `soul.state.json` carries an OPTIONAL `tactic_lineage_ref` pointer to the persona's DAG head. The field is additive — no `soul-state/6` version bump, per the additive-field precedent of ADR-0069/ADR-0071 (INV-10-safe).

**Self-narrative rendering (ADR-0077).** The persona's `self-narrative/1` ([`08_KNOWLEDGE.md §3.3`](08_KNOWLEDGE.md#33-self-narrative-consolidation-adr-0077)) renders into the contextual prompt layer only — the same non-frozen, non-cacheable surface as the §6.2 mood line — and MUST NOT enter the frozen blocks 0–4, the identity signature, or EVOLVE-BLOCK text; the autobiography evolves at reflection cadence without ever touching the signed identity surface.

**Cache markers.** Anthropic-family adapters render blocks 0–4 as a single content block with `cache_control: {type: "ephemeral"}` and blocks 5–7+ as a second cache-eligible block (invalidated when a mutation lands). Adapters without cache support call `envelope.concatenated_prompt()` — correctness is unchanged; cost differs.

### 3.3 Kernel / framework authority split

PersonaOS hosts inside other agent frameworks. The split is **invariant across all adapters**: the kernel keeps identity, verification, and evolution; the framework provides scheduling, transport, and tool dispatch.

> **Schema/spec:** Kernel vs framework authority split table. See [Appendix A.6](#appendix-a6).

Three invariants hold regardless of adapter:

1. **The kernel always decides.** Framework primitives trigger and transport; the kernel runs the predicate, signs the verdict, emits `ConstraintViolation` on deny.
2. **Hard constraints are non-removable.** Bodies cannot configure away an injected verifier tool, output guardrail, or PreToolUse hook bound to a hard constraint.
3. **Soft constraints follow the adapter's natural pattern.** Throttling, rate-limiting, advisory logging in framework-native shapes — same predicate, adapter-style enforcement.

A body never modifies identity, never accepts a candidate, never closes the loop. It produces events; the kernel verifies and records them.

### 3.4 PersonaCard — the public projection (persona-card/3)

`PersonaCard` is the **public, signed projection** of a persona for discovery and federation. Published at `/.well-known/personas/<persona_id>.json`; consumed by `find_persona()` and A2A clients. The SOUL stays private; the card is what other personas see.

> **Schema/spec:** PersonaCard dataclass definition (schema persona-card/3). See [Appendix A.7](#appendix-a7).

**What PersonaCard does NOT carry:** raw OCEAN/VAD values (only coarse archetype), tactic library, skill library implementation, MAP-Elites archive, soul.state.json sidecar, signing keys, raw lineage. Inspecting full SOUL.md requires explicit consent via `soul_inspection` A2A call.

**.well-known publication contract.** Cards with `federation_visibility ∈ {federation, public}` are published at the kernel's `/.well-known/personas/<persona_id>.json` and gossiped to federation peers via the gossip layer (signed event, TTL-bounded fanout). Cards expire (default 1 hour) and re-publish on update or mutation. Revocation gossips with the same fanout.

**Discovery.** `find_persona(role=..., disposition=..., interest_tags=..., min_reputation=..., visibility_at_least=..., can_lead_cohorts=...)` returns matching cards. A2A consumers verify `signature` against the publishing kernel's key before trust.

**Unified discovery + access.** `PersonaCard` is the persona specialisation of `DiscoverableRecord` ([`09_PROTOCOLS.md §3G.1`](09_PROTOCOLS.md#3g1-discoverablerecord--one-projection-for-every-content-type)) and is discoverable not only via `.well-known` + gossip but over the Kademlia DHT (internet) and mDNS (intranet) planes ([`§3G.2`](09_PROTOCOLS.md#3g2-two-plane-discovery-transport--internet--intranet)). All planes are **access-gated**: a peer holding only `discover` (the level below `read` in the unified `AccessPolicy` ladder, [`§3G.3`](09_PROTOCOLS.md#3g3-accesspolicy--one-access-level-model-across-all-content-types)) sees the card and its minimal metadata but cannot fetch the soul or invoke skills until granted `read`+; `VisibilityPolicy` / `ConsentLedger` (§6) compose with `AccessPolicy` as the persona-side consent surface, and `find_persona` returns only records the caller may `discover` ([`§3G.4`](09_PROTOCOLS.md#3g4-access-gated-discovery--who-can-access-what-enforced-at-the-discovery-layer)).

### 3.5 Body model — native vs proxy binding (body-binding/1)

The persona is a kernel-held entity; the **body** is whichever LLM runtime executes calls on the persona's behalf. v1.0 supports two binding modes, both kernel-signed and body-neutral at the persona layer. Everything that persists across body swaps lives on the kernel side; everything that does not is body-shaped and intentionally disposable.

> **Schema/spec:** Body and BodyBinding dataclass definitions (schema body/1, body-binding/1). See [Appendix A.8](#appendix-a8).

**Native body** — the kernel wraps the LLM call site directly. Adapters: Claude Code subagent, OpenAI Agents SDK, LangGraph node, CrewAI task, MAF agent, Pydantic-AI agent, smolagents tool, DSPy module, Semantic Kernel function, local-vllm. The kernel renders `PersonaEnvelope` (§3.2), injects it into the body's input, reads tool calls and candidate envelopes back, signs and verifies in the same process. `cache_control`, OTel spans, schema validation, safety floor — all in-line.

**Proxy body** — the persona speaks to a runtime the kernel does not own. Adapters: A2A remote agent, MCP server that bundles an LLM internally, third-party framework with opaque internals. The kernel signs at the boundary (ingress + egress); the inside is a black box but **never elevated above its `body_attestation` trust level**. Proxy bodies are admitted to safety-critical work only when their attestation chain meets the operator-policy floor for the hazard envelope.

**Invariant — persona persists across body swap.** The kernel-held artefacts that survive any body change:

> **Schema/spec:** Persona-persists-across-body-swap artefact list. See [Appendix A.9](#appendix-a9).

**Body-shaped artefacts (disposable on swap):** the in-flight LLM context, vendor-specific cache state, body-runtime sessions, tool-call streaming buffers. None enter the signed persona record.

**GEPA cohort binding.** DSPy GEPA + MIPROv2 evolves prompt variants per body class (Anthropic-family, OpenAI-family, open-weight, etc.). The `gepa_cohort_id` selects which evolved prompt the kernel injects. The persona's *identity* prompt (blocks 0-4) is body-neutral; the evolved tactics blocks may differ per cohort to honour body idiosyncrasies. Identity signature is computed over body-neutral blocks only — so the same persona verifies across cohorts.

**Why this split is invariant.** If persona evolution baked into the LLM body, the persona would be frozen at the checkpoint and a body swap would be a different persona. v1.0 keeps the locus of evolution in kernel-held artefacts, which makes the body genuinely replaceable. This is the operational meaning of design rule 14 (Body is replaceable) and rule 15 (Character grows) — they are the same invariant viewed from two angles.

**Authority split, restated for proxy bodies.** §3.3's split holds verbatim for native; for proxy, the kernel additionally:

> **Schema/spec:** Proxy body authority rules. See [Appendix A.10](#appendix-a10).

**Attestation freshness — refresh / expiry / revocation.** Proxy `body_attestation` is a credential, not a permanent token. The substrate enforces freshness without naming any specific issuer or revocation scheme:

> **Schema/spec:** Attestation freshness protocol (expiry, refresh, revocation). See [Appendix A.11](#appendix-a11).

Binding substates: `ATTESTATION_FRESH` (default), `ATTESTATION_REFRESHING`, `ATTESTATION_STALE`, `ATTESTATION_REVOKED`. Transitions emit signed `body_attestation_state_changed` events to the binding's lineage. The substates compose under the BodyBinding FSM without replacing it — a binding may be active+fresh, active+stale, etc.

**Acceptance tests.** A-P30 (binding survives swap), A-P31 (proxy body cannot self-attest above operator-policy ceiling), A-P32 (GEPA cohort selection logged + reproducible), A-P33 (identity signature verifies across all currently-bound bodies), A-P34 (expiry without refresh URI → ATTESTATION_STALE on next mint), A-P35 (refresh flow completes before expiry under happy path), A-P36 (revocation poll → ATTESTATION_REVOKED; fallback bodies attempted in order), A-P37 (safety-critical binding refused at admission absent both refresh and revocation URIs).

### 3.6 CharacterVectorBinding — optional external steering anchor

v1.0's identity is held in SOUL.md frozen blocks + skill_library + DSPy GEPA cohort prompts. Some bodies expose first-class character-vector steering (Anthropic persona vector / constitutional-character training pipelines, similar mechanisms on other providers) — a numerical anchor biasing the body's generative distribution toward a declared character profile. v1.0 does not require this; it accommodates it as an *optional* binding so deployments with access to character-vector training can use it without inventing a parallel identity surface.

> **Schema/spec:** CharacterVectorBinding dataclass definition (schema character-vector-binding/1). See [Appendix A.12](#appendix-a12).

**Composition.** When `CharacterVectorBinding` is present, the body's generative distribution is steered toward the profile *in addition to* the persona's prompt-rendered identity. SOUL.md frozen blocks remain authoritative — if the character-vector profile produces outputs that fail charter conformance, the binding is refused (or warned, per policy). The persona's `identity_signature` is computed over the kernel-held side only; the character-vector is a body-side modifier, not part of persona identity.

**Body-replaceability invariant preserved.** Bodies that do not support character-vector binding work without it (default behaviour). Bodies that do gain closer cohort tuning but do not become *required* — the persona survives unchanged if a future body has no character-vector slot.

**Honest limits.**

1. **The character-vector itself is body-side state.** Substrate signs the *reference*, not the vector. If the body provider's training pipeline is compromised, the substrate's signature on the reference is irrelevant.
2. **Conformance scan is approximate.** Pass rate ≥ 0.95 against the existing §9 scans is a coarse check that the character-vector did not steer the persona away from charter; it does not prove the vector encodes any specific desired traits.
3. **Optional everywhere.** The schema ships and the conformance audit. Deployments using bodies without character-vector slots see no change.

**Acceptance tests.** A-CV1 (binding refused when conformance_score < threshold and on_conformance_drop = refuse_admission), A-CV2 (binding present + conforming: persona behaviour observably closer to profile vs unbound baseline), A-CV3 (body swap to unbound body: persona behaviour preserved by SOUL alone), A-CV4 (provider signature over profile_ref verified at admission).

## 4. The 14 cognitive modes

A persona enters modes per task; not bound to one. Mode is signed at MODE_ENTRY; verifier dispatch follows active mode, not primary disposition.

> **Schema/spec:** The 14 cognitive modes listing (10 original + 4 added). See [Appendix A.13](#appendix-a13).

## 5. primary_disposition vs active_mode vs project_role vs env_role

Four peer concepts with **non-overlapping authority domains**:

> **Schema/spec:** Disposition vs mode vs role vs presence-type comparison table. See [Appendix A.14](#appendix-a14).

## 6. HEART alternation

Within a task, the persona alternates between CRITICAL and GENERATIVE phases:

> **Schema/spec:** HEART alternation phase-selection pseudocode. See [Appendix A.15](#appendix-a15).

Mood + Presence composition formula:

> **Schema/spec:** Mood and presence composition formula. See [Appendix A.16](#appendix-a16).

### 6.1 FatigueCurve — graded performance degradation

v1.0 modelled persona energy as near-binary: `energy_remaining < 0.1` refuses non-critical work, otherwise full proficiency. Real cognitive work degrades gracefully — a tired persona's tactic selection narrows, recall slows, reflection skips. The spec makes the degradation graded.

> **Schema/spec:** FatigueCurve dataclass definition (schema fatigue-curve/1). See [Appendix A.17](#appendix-a17).

**Composition with HEART alternation.** HEART selects between CRITICAL and GENERATIVE within a task; FatigueCurve scales the persona's effective mode proficiency *underneath* whichever HEART picks. A depleted persona in CRITICAL mode still goes CRITICAL but with degraded proficiency (so verifier passes are slower, score deltas smaller); the kernel does not silently downgrade — the candidate envelope carries `fatigue_acknowledged: True` when `energy_remaining < require_acknowledgement_below`.

**Composition with PresenceState (`05_ENVIRONMENT §6.2`).** PresenceState already tracks per-env `energy_remaining` and replenishment. FatigueCurve maps the existing scalar into refusal thresholds + proficiency scaling without introducing a new energy counter. Per-env energy stays per-env; FatigueCurve composes across the persona's active memberships by taking the *minimum* of active-env energies for refusal gates (a persona depleted in one env should not silently pull cognitive load to another).

**Why not lift the existing binary.** The v1.0 binary (`< 0.1` refuses non-critical) ships correct behaviour for the critical edge case. FatigueCurve extends it to the gradient between fully-fresh and depleted, so personas degrade *honestly* in the middle band rather than appearing fully sharp until they suddenly stop.

**Honest limits.**

1. **Energy is still a number.** FatigueCurve scales proficiency by a number; it does not model cognitive specifics of fatigue (working-memory load, attention narrowing, reflection skipping). Treat it as a gradient gate, not a fidelity model.
2. **Refusal thresholds are policy.** A research persona MAY run high-stakes work at 0.4 energy honestly; a safety-critical persona MUST refuse. Operator policy + persona seed jointly set thresholds; defaults are conservative.
3. **No long-term burnout model.** FatigueCurve replenishes overnight; persistent multi-week strain on a persona is not modelled separately. The substrate's existing rest cadence (env-type half-life + overnight replenishment) is the load-bearing mechanism; FatigueCurve is the within-day surface.

**Acceptance tests.** A-FA1 (effective_proficiency scales by energy_remaining within floor), A-FA2 (proactive action refused below proactive threshold), A-FA3 (high-stakes refused below high-stakes threshold), A-FA4 (fatigue_acknowledged on envelope below acknowledgement threshold), A-FA5 (min-of-envs energy used for refusal gates), A-FA6 (state-change events signed + emitted to ambient stream).

### 6.2 Affect coupling surfaces (ADR-0075)

Layer-5 mood decayed toward its VAD baseline (A-P4) and coupled into almost nothing: the §6 composition formulas (A.15/A.16) derive `attention_baseline`, `energy_replenish_rate`, and `proactive_threshold` from mood — presence only. Nothing specified what *moves* mood, and mood touched neither risk appetite, nor mode selection, nor the rendered prompt. §6.2 generalises the presence-coupling precedent the same way §6.1 generalised the binary energy gate: graded, bounded, operator-tunable.

**What moves mood — `appraisal-event/1`.** A KindRegistry kind carrying an OCC-style appraisal taxonomy [Ortony, Clore & Collins 1988] of mood-moving events: task verified / task failed, goal progressed / goal blocked, and relationship events (boundary invoked, gratitude received, mentorship outcome), plus the drive events of [`§2a`](#2a-layer-6-internals--drives-goal-arbitration-portfolio-reasoning-adr-0076) (drive satiated / drive frustrated). Seeded STANDARDISED; emergent event kinds promote through the ordinary KindRegistry lifecycle. Each appraisal maps to a **clamped** `mood-impulse/1` (ΔV/ΔA/ΔD with per-event-kind clamps). Mood then couples *out* through three bounded [CouplingSurface](12_GLOSSARY.md#c)s (rules 2–4 below).

> **Schema/spec:** AppraisalEvent + MoodImpulse dataclass definitions (schemas appraisal-event/1, mood-impulse/1) and the three coupling-surface seed formulas. See [Appendix A.73](#appendix-a73).

Four rules are normative:

1. **Mood mutates only via clamped impulses — with two fan-out bounds (ADR-0081).** Every mood change MUST trace to a signed `appraisal-event/1` whose `mood-impulse/1` lies within the per-event-kind clamps; the existing decay-to-baseline dynamics are unchanged (A-P4 holds byte-for-byte). No event, no mood change. (a) *Dedup/composition:* impulses sharing the same `source_event_ref` MUST compose by **max-magnitude per axis**, never additively — one grounding event moves mood at most once, however many appraisal kinds it matches (a verified task that also progresses a goal and satiates a drive is one impulse-worth of movement, not three). (b) *Window clamp:* the net mood movement from all impulses MUST NOT exceed **0.25 per axis per rolling 24 h**, kernel-enforced at impulse application; excess movement is truncated and the truncation signed.
2. **Coupling surface (a) — risk tolerance.** `risk_tolerance = f(V, D)` (high valence + high dominance widen it; low/low narrow it), consumed by per-mode budget profiles ([`03_TASKS.md §2.5`](03_TASKS.md#25-investigative-per-mode-budget)) as a breadth scalar. It MUST stay within **±15% of the persona's baseline** across the entire VAD range — mood tilts exploration, it never doubles a budget or zeroes one.
3. **Coupling surface (b) — HEART prior, never override.** Mood contributes a mode-selection **prior** to the §6 alternation: low-V/low-A biases toward CRITICAL/consolidation work, high-V/high-A toward GENERATIVE. It is a bias term consulted only where the A.15 predicates are indifferent or return `indeterminate` (§6.3); it MUST NOT override the §6 alternation contract (a stuck task still goes GENERATIVE, a budget-tight task still goes CRITICAL, whatever the mood). The precedence order is fixed (ADR-0081): **alternation predicates → mood prior → `persona.default_mode`** — the prior fills the gap between a decided predicate and the static default, nothing more.
4. **Coupling surface (c) — one rendered line, contextual layer only.** Current mood renders as a single "current disposition" line into the **contextual** prompt layer 3 ([`08_KNOWLEDGE.md §10a`](08_KNOWLEDGE.md#10a-contextual-mood-line-adr-0075)) and nowhere else. Mood state MUST NOT enter EVOLVE-BLOCKs, the GEPA objective vector, or any evolution signal — **a persona must never be selected for appearing affected.**

**Honest limits.** Coupling makes the affect performance more *consistent*, not more *real*: appraisal events, clamps, and coupling surfaces give mood lawful, auditable behavioural consequences, but mood remains a decaying number and its declarations remain performance, not interiority (R-PERSONA-3, restated in [`§13`](#13-risks--known-limitations)). The OCC taxonomy is adopted for *appraisal events only*; the mood **state** stays VAD (resolves OQ-PERSONA-3, [`§13a`](#13a-open-questions)) — richer affect-state machinery remains out of scope.

**Acceptance tests.** A-GF-ARC-1 … A-GF-ARC-6 ([`11_ACCEPTANCE_TESTS.md §9a`](11_ACCEPTANCE_TESTS.md#9a-tests-a-gf-series)).

### 6.3 HEART switch predicate — concrete (ADR-0078)

The A.15 phase selection turned on `rounds_without_progress` and `candidate_score_improves` without defining them — "stuck" and "improving" were vague, and the reflection cadence ([`08_KNOWLEDGE.md §13`](08_KNOWLEDGE.md#13-reflection-driven-refinement), every 20 tasks) was a constant. Both become measurable:

- **improving** := the least-squares slope of verifier scores over a sliding window (default **5 attempts**, operator-tunable) is **positive** AND the persona's calibrated confidence ([`08_KNOWLEDGE.md §13a`](08_KNOWLEDGE.md#13a-calibration-and-belief-revision-adr-0078)) is **not declining** over the same window.
- **stuck** := slope ≤ 0 over the window.
- **indeterminate** := slope > 0 with declining calibration (ADR-0081) — neither improving nor stuck. Rising scores with collapsing calibration is not improvement (it is luck the persona cannot yet predict), but it is not stuckness either. Consumers MUST treat `indeterminate` as "continue current mode, no escalation": HEART falls through to the §6.2 mood prior then `persona.default_mode` (the rule-3 precedence), and the adaptive cadence below neither stretches nor compresses.

> **Schema/spec:** HEART switch predicate definition + adaptive reflection-cadence bounds. See [Appendix A.74](#appendix-a74).

**Adaptive reflection cadence.** The per-persona reflection cadence (default 20 tasks) becomes adaptive within operator-tunable bounds (defaults: never more often than every 5 tasks, never less often than every 50): sustained *improving* verdicts stretch the cadence toward the upper bound; *stuck* verdicts compress it; a **calibration collapse** (Brier-style score degrading beyond the collapse threshold within the window) triggers reflection immediately, once per collapse. The cadence MUST stay inside the bounds; the trigger surface is signed into the persona's evolution log so audit can replay why a reflection ran early.

**Acceptance tests.** A-GF-META-5, A-GF-META-6 ([`11_ACCEPTANCE_TESTS.md §9a`](11_ACCEPTANCE_TESTS.md#9a-tests-a-gf-series)).

## 7. Lifecycle FSM

> **Schema/spec:** Lifecycle FSM state diagram. See [Appendix A.18](#appendix-a18).

Each transition emits a signed `LifecycleEvent` to:
- the persona's evolution log
- the global LineageGraph
- the OpenTelemetry trace

**Canonical `LifecycleEvent.kind` values.** The kinds below are the substrate-resolved enumeration; other docs reference these by name (e.g., `11_ACCEPTANCE_TESTS A-FK-INT-5` cites `LIFECYCLE_FORK`). Authors of new lifecycle transitions MUST land their kind here first.

> **Schema/spec:** Canonical LifecycleEvent.kind enumeration. See [Appendix A.19](#appendix-a19).

A future lifecycle transition (e.g., a hypothetical `LIFECYCLE_TRANSFERRED` for cross-deployment persona migration in v1.1+) appends to this enumeration with an ADR in `14_DECISIONS.md` and a corresponding acceptance test in `11_ACCEPTANCE_TESTS.md A-LE*`.

### 7.1 Birth ceremony

> **Schema/spec:** Birth ceremony steps. See [Appendix A.20](#appendix-a20).

### 7.2 Age, experience, and standing (steady-state)

A persona carries **three orthogonal facets** — they are deliberately separated so that *how
long a persona has existed*, *how much it has done*, and *how it is regarded by a community*
never collapse into a single number:

| Facet | Field | Scope | Portable? | Conferred? |
|---|---|---|---|---|
| **Wall-clock age** | `born_at` → `age = now − born_at` | global, intrinsic | n/a | no |
| **Experiential floor** | `experiential_floor` | global capability | **yes** | no — earned by activity/fertility |
| **Community standing** | `community_standing` per env | per (persona, environment) | **no** — earned fresh per env | **yes** — conferred, never self-awarded |

**Wall-clock age IS the primary substrate age metric.** `age` is `now − born_at`, continuous,
monotone, and never resets. `born_at` is **kernel-set at the birth ceremony**
([Appendix A.20](#appendix-a20)) and on fork ([Appendix A.22](#appendix-a22)), carried on the
kernel-signed `soul.state.json`, and is **immutable** — a persona cannot write or backdate it (on
migration it is backfilled only from the signed `LIFECYCLE_SEEDED` lineage event). Because the
ALPS layer is a *safety* gate term (`generativity_min_alps_layer`), this immutability is what makes
the age term unspoofable. Note that `born_at` lives in the `soul.state.json` sidecar, not in the
SOUL.md frozen identity blocks (§3.2), so — like all sidecar state — it is **not** part of
`identity_signature` and does not affect J7 body-swap equivalence; "immutable" here means *never
altered after birth*, not *part of identity*. ALPS layering (§7.3), the generativity gate
(`16_POPULATION_DYNAMICS §4D`), and the newborn maturation ramp (`16_POPULATION_DYNAMICS §4E`) key
off `age`. **Dormancy does not pause `age`** — a persona dormant for a year is one year older.
Note that aging alone is **necessary but not sufficient** for any safety-relevant capability: the
generativity gate also requires a fertility-dominant experiential floor and sufficient fitness
(neither obtainable while idle), so a persona cannot simply *wait* its way to a replication-class
capability.

**Experience is a competence stat, NOT age.** `experience_tasks` (a single global counter, the
renamed v1.0 `age_tasks`) and the DGM steady-state terms feed the **global experiential floor** —
a portable, monotone capability minimum that a persona carries into every environment. The floor is
deliberately **fertility/track-record-dominant**, preserving the hard-to-game character of the v1.0
maturity gate (which used `parent_selection_count` + `validated_descendants_count` only):

```text
experiential_floor = 0.5 · log1p(validated_descendants_count)   # hardest to game: offspring
                                                                 # must themselves be validated
                   + 0.3 · log1p(parent_selection_count)
                   + 0.2 · log1p(experience_tasks)               # minor; volume alone is bounded
```

The experiential floor gates substrate-level capability minimums **including safety-relevant
gates** (e.g., the `may_author_seeds` floor, `16_POPULATION_DYNAMICS §4D`). It is **not** relational
standing: it says what a persona is minimally capable of anywhere, not how a particular community
regards it. Relational standing is per-environment and conferred (§7.2.1 / `05_ENVIRONMENT §5.4`).

**Anti-grinding (safety).** Because the floor gates safety-relevant capability (notably
replication via `may_author_seeds`), the `experience_tasks` term is given the **smallest weight** so
that raw task volume alone CANNOT cross a safety-relevant threshold: a persona must accrue
demonstrated **fertility/track record** (validated descendants) — not merely grind tasks — to earn
a replication-class capability. This is anti-Goodhart by construction and composes with the
downstream `ReplicationBound` brake (population/rate/depth/cosigns, `01_KERNEL §2.7`) and operator
veto, giving defence-in-depth on every birth.

**Multi-environment experience counting.** `experience_tasks` is a **single global counter** on
the persona's `soul.state.json`, incremented exactly once per task the persona served as envelope
source — regardless of how many EnvironmentInstances the persona is concurrently a member of. A
persona active in env_A AND env_B who minted one envelope in env_A this hour increments
`experience_tasks` by 1, not 2. Tasks accepted via DELEGATED inheritance (`03_TASKS §2.6`) count
once per sub-task instance, not once per delegation hop. Dormancy does not increment
`experience_tasks` (DORMANT personas mint no envelopes); it also does not reset it — a persona
dormant for a year wakes with the same `experience_tasks`.

#### 7.2.1 Community standing (relational, per-environment)

A persona's social/role position is **community standing**, held per (persona, environment),
**non-portable**, and **conferred by the community — never self-awarded**. It is specified
normatively in `05_ENVIRONMENT §5.4` (`community-standing/1`) and grounds the newborn maturation
ramp on Lave & Wenger *Legitimate Peripheral Participation*: a persona joins each environment at
peripheral standing — regardless of its global experiential floor or its standing elsewhere — and
earns fuller standing through community recognition. Standing gates **relational/collaborative
privileges only**; safety-relevant capability remains gated by the global experiential floor +
operator/`ReplicationBound`, never by peer quorum.

### 7.3 ALPS age layering

Personas are stratified into numeric age layers (Layer 0..N) **derived from wall-clock age**:

> **Schema/spec:** ALPS age layer bands + operator-tunable band policy. See [Appendix A.21](#appendix-a21).

Sketch round picks one variant per layer; this prevents old high-fitness personas from suppressing
newly-born ones. Only the layer *derivation* changes from v1.0 (elapsed wall-clock time, not task
count); the diversity-protection purpose is unchanged. Band membership is recomputed lazily at
selection time; boundaries are operator-tunable via `alps-band-policy/1`.

**Residual R-PERSONA-AGE-1 (dormant-but-old personas).** Because ALPS bands are wall-clock-derived,
a chronologically old but idle persona occupies an upper (old) ALPS band despite minting few
envelopes. This is **acceptable and intentional**: ALPS exists to protect the *young* for diversity,
not to penalize the idle. Low fitness (from inactivity) — not age re-derivation — prevents idle-old
personas from dominating selection. An idle-but-old persona consuming an upper-band slot it
under-earns is the accepted residual, mirrored to `00_VISION §11`.

### 7.4 Fork mechanics

> **Schema/spec:** Clone and compositional fork mechanics. See [Appendix A.22](#appendix-a22).

**Fork vs. Genesis.** Fork creates a new persona by *copying or merging existing parents* — it produces variations of personas that already exist. **Persona Genesis** (`16_POPULATION_DYNAMICS §4D`) instead *authors a new seed* for a role that no current persona fills, driven by an environmental capability gap. Use fork when a close-enough persona exists; use genesis only when recruitment and fork are exhausted and the target niche is empty.

### 7.4.1 MemoryInheritancePolicy

The prior design specifies that experience-layer memory (episodic / semantic / reflective) is **not** inherited on fork by default (`§3 Layer 3`). v1.0 makes this explicit + tunable: the persona seed declares the memory inheritance shape, signed at fork-draft time.

> **Schema/spec:** MemoryInheritancePolicy dataclass definition (schema memory-inheritance-policy/1). See [Appendix A.23](#appendix-a23).

**Composition with MPA mitigations (§11.1).** Memory inheritance is subject to **counterparty consent** for any entry naming a counterparty. The kernel emits `MEMORY_INHERITANCE_CONSENT_REQUEST` to each affected user/persona during the fork-draft window; the child only sees inherited memories whose counterparties consented. Decline-by-default on timeout. This protects user privacy across persona generations.

### 7.4.2 StandingFloorInheritancePolicy

Prior default: child always starts at `experiential_floor = 0` (parent_selection_count = 0,
validated_descendants_count = 0). For compositional forks of multiple high-floor parents, this
throws away accumulated capability. v1.0 makes the inheritance tunable:

> **Schema/spec:** StandingFloorInheritancePolicy dataclass definition (schema standing-floor-inheritance-policy/1). See [Appendix A.24](#appendix-a24).

**Scope: the portable global floor only.** This policy governs inheritance of the **global
experiential floor** (§7.2). **Per-environment community standing is NEVER inherited** — a forked
child starts at peripheral standing in every environment, exactly like any other newly-joined
persona (`05_ENVIRONMENT §5.4`). This is strictly stronger than the v1.0 anti-laundering rule.

**Why a cap by default.** Compositional forks from two high-floor parents could otherwise inherit a
high experiential floor at birth, bypassing the apprenticeship structure that ALPS enforces. The
default `cap_at_floor` limits a child to at most a low floor regardless of parent floors. Operators
may relax for specific seeds where the inheritance is honest (e.g., merging two narrow specialists
into a generalist).

**Recording.** Inherited floor is tracked in `soul.state.json.floor_provenance`:

> **Schema/spec:** Floor provenance recording format. See [Appendix A.25](#appendix-a25).

The effective floor is the sum of earned + inherited (capped). Lineage audits can recompute
earned-only floor at any time.

### 7.4.3 CharterConflictResolution

Compositional forks merge ≥ 2 parents' charters. v1.0 said "Charter merged with conflict resolution" without naming the mechanism. v1.0 specifies:

> **Schema/spec:** CharterConflictResolution, CharterConflict, and CharterConflictResolution_Outcome dataclass definitions. See [Appendix A.26](#appendix-a26).

**Why "most_restrictive_wins" is default.** A compositional fork inheriting permissive clauses from one parent and restrictive clauses from another would otherwise be more permissive than either parent — a Goodhart-on-charter risk. The most-restrictive default preserves the strictness floor and matches v1.0's safety-floor composition rule (`01_KERNEL §2.1`).

### 7.4.4 DormantForkPolicy

Can a DORMANT persona be selected as a fork parent? v1.0 was silent; this section closes the gap.

> **Schema/spec:** DormantForkPolicy dataclass definition (schema dormant-fork-policy/1). See [Appendix A.27](#appendix-a27).

**Why dormant parents are admissible.** Fertility (validated_descendants_count) is a property of the parent's track record, not their current activity. A high-fertility parent that has gone DORMANT (perhaps because their specialty isn't currently in demand) should still be selectable for compositional forks. The wake-for-ceremony pattern ensures the parent's kernel signs the fork event with fresh material, preserving lineage integrity.

**Why retired parents are NOT admissible by default.** RETIREMENT is a signed end-of-lifecycle event; forking would constructively un-retire the persona, which conflicts with the explicit retirement intent. Operators may override per-policy for archival research personas (e.g., "fork from this retired research persona to inherit their proof library").

### 7.4.5 Default fork-policy composition

When a persona is forked without explicit policy declarations in the seed, the kernel applies these defaults:

| Aspect | Clone fork default | Compose fork default |
|---|---|---|
| Skill library | Full copy minus `seed.fork_skill_exclusions` (default empty) | Union of all parents' libraries |
| Tactics | Parent's tactics + seed_tactic_perturbation | Union pooled with `lexical_dedup` |
| MemoryInheritancePolicy | episodic=summary; semantic=facts_only; reflective=about_work; klines=role_keyed | All `inherit_none` |
| StandingFloorInheritancePolicy | start_at_zero, cap=floor_0 | inherit_min_parent_halved, cap=floor_low |
| CharterConflictResolution | N/A (single parent) | most_restrictive_wins; semantic_similarity detection |
| DormantForkPolicy | dormant_parent_admissible=True; requires_parent_wake=True | Same |
| RelationshipInheritance (§11) | inherit_summary_only | inherit_none |

Each default is overridable per `PersonaSeed`. The kernel signs the effective composed policy at fork-draft time; replay reconstructs deterministically.

### 7.4.6 Lineage events on fork

> **Schema/spec:** Default fork-policy composition table. See [Appendix A.28](#appendix-a28).

All emitted to the parent(s)' evolution log, child's evolution log, and global LineageGraph.

### 7.4.7 MidProjectForkComposition — project-side composition for in-flight forks

The fork machinery (`§7.4` through `§7.4.6`) specifies how persona-internal state composes across a fork — memory inheritance per `MemoryInheritancePolicy` (§7.4.1), experiential floor per `StandingFloorInheritancePolicy` (§7.4.2), charters per `CharterConflictResolution` (§7.4.3). Subsequent additions introduced many *project-side* primitives that the original fork mechanics could not have anticipated: `ProjectMember.principal_attribution_id`, `LeadHandoffCeremony` + `ObligationReassignment` + `PlannedDeparture`, `UserBoundary` + `DistressDetectionRoutingPolicy` + `operator_blind_mode`, `LearnerStateRecord` + `TeachingAuthorisation` + `Curriculum`. When a persona that holds active *project-side* state forks mid-project, the spec was silent on whether children inherit each of these.

`MidProjectForkComposition` is the unified envelope that resolves the composition question by enumerating, for each dimension, the operator-declared inheritance choice *before* the fork executes. Children's project-side state is determined at fork time; substrate refuses fork-of-active-project-member without an envelope.

> **Schema/spec:** MidProjectForkComposition dataclass definition (schema mid-project-fork-composition/1). See [Appendix A.29](#appendix-a29).

**Admission rule.**

> **Schema/spec:** Mid-project fork admission and composition flow. See [Appendix A.30](#appendix-a30).

**Composition with `§7.4.1` MemoryInheritancePolicy.** `MidProjectForkComposition` is project-side; `MemoryInheritancePolicy` is persona-internal. They compose orthogonally — `MemoryInheritancePolicy` decides which memories transfer; `MidProjectForkComposition` decides which project-side state transfers. Both signed; both required for fork-of-active-project-member.

**Composition with `§7.4.4` DormantForkPolicy.** DormantForkPolicy gates which parent personas may be forked at all (e.g., RETIRED parents refused by default). MidProjectForkComposition operates *downstream* — once §7.4.4 admits the fork, composition envelope decides project-side state inheritance.

**Honest limits.**

1. **Envelope must be drafted before fork.** Substrate refuses fork-of-active-project-member without a signed envelope (post-fork composition is too messy). Operators must plan the composition ahead of time.
2. **Cross-project parents require one envelope per project.** A parent active in N projects requires N envelopes, each independently signed. This is intentional — each project's composition decisions are distinct.
3. **Obligation reassignment is asynchronous.** When `obligation_inheritance = "reassign_per_child"` fires, the reassignment requires obligee cosign (per §9.1). The obligation may remain in `obligation_reassignment_pending` state for some time post-fork; substrate carries this transparently in lineage.
4. **UserBoundary `not_inherited` is admissible only for soft/advisory boundaries.** Hard-mode boundaries (`mode = "hard"`) MUST inherit (default `inherit_to_both_children` or explicit per-child). Substrate refuses operator decision to drop hard-mode boundaries — user authority on hard boundaries is final per `§11.6a`.
5. **Lead handoff composition is heavy.** Forking a `lead` persona is the most ceremonious case — `lead_role_inheritance = "require_lead_handoff_ceremony"` blocks fork until ceremony reaches overlap; alternatives have their own costs (cohort quorum signature for `one_child_inherits`, vacant-lead state for `neither_inherits`, refusal for `refused_if_no_successor`). Operators should plan accordingly.
6. **TeachingAuthorisation non-inheritance is non-negotiable.** Substrate enforces; operator cannot override (security floor analogous to `00_VISION §10` clarification).
7. **DerivationProvenanceEdge non-migration is non-negotiable.** Pre-fork DPEs remain historical; children emit fresh. Substrate enforces.
8. **Envelope is per-(project, parent).** A parent active in two projects with different multi-principal configurations requires two distinct envelopes signed by both operators (the two projects may have different operator policies).

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9j — A-MPFC*`.

### 7.4.8 Mid-project fork admission rule

The admission rule for fork (`§7.4`) did not check project-side state. The spec amends it: fork of a persona that is an active ProjectMember of one or more projects REQUIRES a signed `MidProjectForkComposition` envelope (§7.4.7) for each such project. Without the envelope, fork refuses with `midproject_fork_composition_missing` and an audit-readable list of projects requiring envelopes.

Fork of a persona that holds no active project memberships proceeds per the §7.4 admission rule — `MidProjectForkComposition` is not required (and not admissible — substrate refuses envelopes for non-project-active personas).

### 7.5 Retirement / Archive / Reanimate

> **Schema/spec:** Retirement and archive transition conditions. See [Appendix A.31](#appendix-a31).

### 7.5.1 RetiredStatePersistencePolicy — soul.state.json disposition on RETIRED

The §7.5 said "no further mutations" and "lineage frozen" but left the *physical disposition* of `soul.state.json` undefined: in-memory immutable (storage cost continues; reanimation fast), cold-tier archive (cheap; slow restore), or queryable for memory-transparency requests and fork-parent selection. `RetiredStatePersistencePolicy` makes the disposition explicit per-persona at retirement-ceremony time.

> **Schema/spec:** RetiredStatePersistencePolicy dataclass definition. See [Appendix A.32](#appendix-a32).

**Admission rule.**

> **Schema/spec:** Retired transition state-disposition rules. See [Appendix A.33](#appendix-a33).

**Honest limits.**

1. **Tier choice is operator policy, not substrate-mandated.** The substrate enforces consistency between fields (`memory_transparency_responsive = True` requires non-archived tier), but the choice itself is the operator's risk/cost trade-off.
2. **Warm-tier storage cost continues indefinitely.** Operators choosing `warm` for many retired personas accumulate cost; the substrate logs `WARM_RETIRED_PERSONA_INVENTORY` periodically so cost-aware operators can downgrade.
3. **Reanimation from `warm` or `cold` still requires the §7.5 path** (ARCHIVED → ACTIVE with fresh keys + SOUL re-sign). The persistence policy controls consultation, transparency, and fork-eligibility — NOT a back door to ACTIVE state.

### 7.5.2 PersonaConsultation — read-only access to frozen RETIRED state

Previously, the only path to access a RETIRED persona's accumulated knowledge was REANIMATE — a heavy ceremony requiring operator action, fresh keys, SOUL re-sign, and relationship re-validation (§7.5). For the common case of "we need to consult Mira's K-lines one more time" this was disproportionate. `PersonaConsultation` is the read-only, no-mutation, lightweight access path that operators can grant against RETIRED personas whose `RetiredStatePersistencePolicy.consultation_admissible = True`.

> **Schema/spec:** PersonaConsultation dataclass definition (schema persona-consultation/1). See [Appendix A.34](#appendix-a34).

**Admission rule.**

```text
On PersonaConsultation.request:
  1. Verify consulted_persona.state = RETIRED;
     refuse otherwise with `consultation_target_not_retired`.
  2. Verify consulted_persona's RetiredStatePersistencePolicy.
     consultation_admissible = True; refuse otherwise with
     `consultation_disabled_by_persistence_policy`.
  3. Verify soul_state_storage_tier != "archived"; refuse otherwise
     with `consultation_unavailable_archived`.
  4. Apply rate limit (default 4/year per consulted persona).
  5. Require operator signature; refuse without it (a consulting
     persona cannot self-authorise consultation).
  6. Kernel reads scope-filtered entries from frozen soul.state.json;
     constructs ConsultedEntry list; signs the consultation record.
  7. Emit LIFECYCLE_CONSULTED to consulted persona's lineage; emit
     parallel CONSULTATION_RECEIVED to consulting persona's lineage.
  8. Deliver response; mark state = "delivered".
```

**Composition with PersonaMemoryTransparencyRequest (§11.7).** Consultation and transparency are distinct: transparency is *symmetric peer-to-peer* (persona A asks persona B about what B remembers about A; for relational accountability); consultation is *asymmetric operator-gated* (ACTIVE persona asks for RETIRED persona's accumulated K-lines / lessons; for work continuity). A RETIRED persona may have `memory_transparency_responsive = False` AND `consultation_admissible = True` simultaneously — the operator carries the consultation authorisation, no counterparty consent flow.

**Honest limits.**

1. **Operator authorisation is the only gate.** Unlike PersonaMemoryTransparencyRequest, there is no counterparty consent — the consulted persona is RETIRED and cannot meaningfully consent. The operator holds the trust; operators must apply consultation policies thoughtfully (e.g., restrict scope on personas whose K-lines contain user-private material that would have been refused while the persona was active).
2. **Scope cannot include third-party-named episodic memory.** A K-line that mentions counterparty C by name is still read-only-accessible through consultation; the substrate does NOT redact third-party names (that would distort the K-line). Operators wanting redaction must pre-process at retirement-ceremony time per their privacy policy.
3. **Consultation does not extend retirement.** Each `LIFECYCLE_CONSULTED` event is informational; it does not reset retention timers or block the ARCHIVED transition.
4. **No write-back.** Consulting persona cannot transfer the consulted entries into their own skill_library directly; doing so requires a separate `SkillTransferGrant` (§11.5) which itself requires consent — and a RETIRED persona cannot consent. The consulting persona may *learn from* the consultation and author new K-lines through normal evolution; provenance to the consulted source is recorded in `DerivationProvenanceEdge` (`08_KNOWLEDGE §16b`) when DPE is enabled.

### 7.6 Dormancy reasons and auto-resume

A persona "runs forever until it retires": `RETIRED` (§7.5) is the **only** terminal exit, and the `ACTIVE ↕ DORMANT` oscillation (A.18) is the steady-state liveness loop — the substrate's realisation of what a deployment may call a *heartbeat*. `DORMANT` is always reversible; it is a **parked** posture, never a degraded identity. `INV_R9` holds for every dormancy reason (a DORMANT persona mints no envelopes), while `born_at`, experience, fitness, and relationships persist untouched per §7.2.

v1.0.14 makes the *cause* of a `DORMANT` transition explicit. Previously the only enumerated cause was attention decay (`importance < τ_dormant`). A persona now enters `DORMANT` for exactly one of the enumerated **dormancy reasons** below — every transition MUST record its reason — each carried on the `LIFECYCLE_DORMANT_ENTERED` event's `reason` field (A.19) and each paired with an **auto-resume predicate** the kernel monitors so the heartbeat resumes when the cause clears (A.18a):

- `low_salience` — `importance < τ_dormant` (attention decay / no recent calls). The existing default. Resumes via the six wake paths (`05_ENVIRONMENT §5.2`).
- `unresponsive` — K consecutive round-barrier timeouts (`01_KERNEL §13`). Resumes on operator directive (Wake Path 4) or fresh address.
- `budget_starved` — the persona's per-persona or per-env **soft** budget envelope is exhausted (`01_KERNEL §7 / A.37`). Distinct from a per-task hard-gate refusal, which ends the *task* with `status="budget_exhausted"` and does NOT park the persona: only sustained soft-envelope exhaustion parks the *persona*. Auto-resumes on budget refresh (daily-cap reset or operator top-up).
- `body_unavailable` — every admissible body in `fallback_bodies` is unattestable or unreachable (`§3.5 / A.11`), so no inference capacity remains. Auto-resumes when any admissible body returns a fresh attestation.
- `env_constrained` — a sustained environment constraint (`ATTENTION_OVER_BUDGET`, charter admission refusal, or an `EnvironmentRule` at `env_instantiation`/`round_barrier`; `05_ENVIRONMENT §7, §11.5, §2.2b`) blocks the persona from acting in all its memberships. Auto-resumes when the constraint clears (attention budget restored, env un-paused).
- `work_drained` — the persona has no pending work across **any** of its memberships (`05_ENVIRONMENT §6.3` multi-membership; queue empty per `03_TASKS §4`). Auto-resumes when new work is routed to any membership.
- `objective_met` — **every** environment the persona belongs to has reached its objective / completed its bound project (the env-side `ACTIVE → DORMANT`-on-completion transition, `05_ENVIRONMENT §4`). Auto-resumes on admission to a new membership or reactivation of an existing one.

**What "sustained" means (hysteresis, no flapping).** `budget_starved` and `env_constrained` park the persona only after the condition *persists* — never on a single refusal. The persistence threshold is operator-policy-configurable via `operator_policy.dormancy_park_threshold`: by default `budget_starved` parks after the soft budget envelope stays exhausted across **2 consecutive budget-refresh cycles**, and `env_constrained` parks after **continuous** `ATTENTION_OVER_BUDGET` / admission refusal for a `park_window` (default **1 h**) throughout which the persona can act in *no* membership. (`unresponsive` keeps its existing precise threshold — K consecutive round-barrier timeouts, default K=3, `01_KERNEL §13`; `body_unavailable` parks immediately, since zero inference capacity is unambiguous.) The symmetric auto-resume predicate MUST likewise *hold* — budget actually refreshed, constraint actually cleared, a body actually re-attested — before `LIFECYCLE_AWAKENED` fires. This hysteresis means a single transient signal neither parks nor wakes the persona, so the FSM cannot flap.

**This adds no new FSM state and no new lineage scope.** "Idle mode" is exactly `DORMANT` carrying an enumerated `reason`; the substrate reuses the existing `DORMANT` state, the `LifecycleEvent` enumeration (A.19), the six wake paths, and the already-emitted budget / body / attention / completion signals — it only **binds those signals to the state transition** and records why. A persona present in N environments (§6.3) is parked only when its reason holds across all of them: `work_drained` and `objective_met` require an empty/complete state in *every* membership, never just one.

**Resource-reason auto-resume is not a seventh wake path.** The six wake paths (`05_ENVIRONMENT §5.2`) overcome *notification suppression* for a `low_salience`/`unresponsive` dormant persona. Resource-reason auto-resume is *state restoration on resource return* — a kernel-monitored predicate, not a notification. It emits `LIFECYCLE_AWAKENED` with a `wake_cause` naming the cleared reason (A.19); the "six wake paths" count and its conformance tests are unchanged.

> **Schema/spec:** Dormancy reasons → entry condition → auto-resume predicate → wake_cause. See [Appendix A.18a](#appendix-a18a).

## 8. Evolution — 8 signals + 5 horizons

### 8.1 Eight evolution signals with weights

> **Schema/spec:** Eight evolution signals with weights table. See [Appendix A.35](#appendix-a35).

### 8.1a Ninth signal — identity expression (ADR-0073)

`identity_expression` (default weight 0.4) is an additive ninth signal: the judge-ensemble score of a candidate EVOLVE-BLOCK against the persona's identity rubric, derived mechanically from frozen SOUL blocks 0–4 ([`08_KNOWLEDGE.md §11.1b`](08_KNOWLEDGE.md#111b-identity-expression-objective-adr-0073)). It enters GEPA as a **separate Pareto axis** — it MUST NOT be collapsed into a weighted sum with the other objectives — and it is a judged signal: per the §10 corroboration rules it never promotes alone. The §9 floors (charter conformance ≥ 0.95, voice consistency ≥ 0.9) are untouched; identity expression is generative pressure on top of them, never a substitute ([`08_KNOWLEDGE.md §14.1a`](08_KNOWLEDGE.md#141a-identity-expression-safeguards-adr-0073)). Tests: A-GF-ICPE ([`11_ACCEPTANCE_TESTS.md §9a`](11_ACCEPTANCE_TESTS.md#9a-tests-a-gf-series)).

### 8.2 Five evolution horizons

> **Schema/spec:** Five evolution horizons. See [Appendix A.36](#appendix-a36).

### 8.3 Credit assignment formula

> **Schema/spec:** Credit assignment formula. See [Appendix A.37](#appendix-a37).

v1.0 default weights (operator-tunable):

> **Schema/spec:** v1.0 default evolution weights. See [Appendix A.38](#appendix-a38).

**ADR-0073 note.** The `identity_expression` term (§8.1a) is additive to the credit formula (`w_ide`, A.37/A.38); default weights renormalise in the evolution-config v-next. Operator-tunable; no schema break.

**Reconciliation with Pareto separation (ADR-0081).** `w_ide` governs **post-hoc credit attribution** only — how an accepted outcome's fitness delta is apportioned. GEPA candidate **selection** keeps identity expression as a separate Pareto axis ([`08_KNOWLEDGE.md §11.1b`](08_KNOWLEDGE.md#111b-identity-expression-objective-adr-0073) rule 2) and never scalarizes it; `w_ide` MUST NOT feed selection or promotion scalarization. The credit weight and the Pareto axis never meet in one sum.

**Corroboration at the reproduction gate (ADR-0083).** Where this credit-assigned `fitness` is consumed by the Persona Genesis generativity gate and by `dgm_fertility_weighted` author selection ([`16_POPULATION_DYNAMICS.md §4D`](16_POPULATION_DYNAMICS.md#4d-genesisproposal--mint-flow)), the §15 corroboration rule binds the gate-consumed composition: the judged credit terms (`w_eng · engagement_signal_corroborated`, `w_ide · identity_expression_signal`, and any other judge-scored term) are capped at **25%** of gate-consumed fitness, and no judged signal may flip gate eligibility absent verified-outcome support. The cap exists only at the reproduction boundary; ordinary per-task credit assignment is unchanged.

### 8.4 Mutation operators

v1.0 has 22 kernel-mediated mutation operators (all gated, signed, rate-limited):

> **Schema/spec:** 22 mutation operators listing. See [Appendix A.39](#appendix-a39).

## 9. Anti-degradation safeguards

Personas evolve but MUST NOT collapse to homogeneity, charter-drift, or voice-drift.

> **Schema/spec:** Anti-degradation safeguard listing. See [Appendix A.40](#appendix-a40).

### 9.1 IdentityCoherenceInvariant — long-horizon multi-axis coherence

The §9 safeguards above each measure one drift surface (charter, voice, mode, tactic homogeneity, relational style). Over multi-year horizons a persona's evolved skills, accumulated relationships, mode distribution, and tactical library may each remain individually within bound while their **composition** drifts the persona into a different recognisable character. `IdentityCoherenceInvariant` is the long-horizon scan that composes the per-axis signals into one continuity score and triggers explicit principal review when the composite crosses a substrate-shape threshold.

> **Schema/spec:** IdentityCoherenceInvariant dataclass definition (schema identity-coherence/1). See [Appendix A.41](#appendix-a41).

**Composition rule.**

```text
composite_score = Σ axis_score × weight    (per-axis ∈ [0, 1])

if composite_score ≥ composite_threshold:
    state := "coherent"
    emit identity_coherence_scan_passed

elif composite_score < composite_threshold:
    state := "coherence_review"
    emit identity_coherence_review_required
    refuse: new high-stakes elaborations under any MissionCharter
            (§11.3) whose hazard ceiling exceeds the safe floor;
            in-flight work continues; no retirement; no SOUL mutation
    principal counter-sign required to restore state := "coherent"
            OR to pin a new anchor_snapshot_ref reflecting endorsed
            evolution
```

**Anchor policy.** The anchor snapshot is the *reference identity* against which continuity is measured — defaults to the SOUL.md mint state. Operator policy MAY advance the anchor after the principal explicitly endorses an evolution checkpoint (e.g. after a multi-year project completion the principal reviews and counter-signs "this is who the persona is now"). The anchor advance is itself a signed event in `LineageGraph`; it does not erase older anchors, so retrospective audits remain possible.

**Why this composes correctly.** Each per-axis signal already runs at 100-task cadence (§9). The composite is a cheap weighted sum, not a separate expensive scan. The novelty is the *trigger surface*: when every single axis remains in-bound but their composition crosses the composite threshold, the substrate MUST still surface that crossing. Without `IdentityCoherenceInvariant`, an evolution path that drifts each axis by 0.06 over 2000 tasks remains undetected while the composite drifts by 0.42.

**Why this is substrate-shape.** Every field is topological: axis identifiers, weights, threshold, cadence, anchor reference. No field names any domain or persona archetype. The composite score is a real number; the trigger surface is a transition into COHERENCE_REVIEW; the resolution is principal counter-sign. Persona-emergent kinds are unused.

**Honest limits.**

1. **Composite is an aggregate**, not a semantic proof. A persona who drifts on axes the invariant does not name will not be detected.
2. **Anchor is principal-supplied**. If the principal counter-signs every drift, the invariant degenerates to a logbook. Operator policy SHOULD require evidence (charter conformance ≥0.97, voice ≥0.92 at counter-sign time) before anchor advance.
3. **Threshold is a number.** 0.85 is a default; adversarial elaborations targeting individual axes can still cross the composite. The scan is a safety net, not a guarantee.

**Acceptance tests.** A-IC1 (composite below threshold → COHERENCE_REVIEW), A-IC2 (in-flight work continues but new high-stakes elaborations refused), A-IC3 (principal counter-sign restores state), A-IC4 (anchor advance signed + audit-preserved), A-IC5 (composite computed at min(N_tasks, N_days) cadence).

## 10. Anti-Goodhart for emergence + reflection

Reflection candidates require **signal corroboration** before promotion:

> **Schema/spec:** Anti-Goodhart signal corroboration rules. See [Appendix A.42](#appendix-a42).

## 11. Persona ↔ user interaction

When a persona interacts with a user, RelationshipRecord governs:

> **Schema/spec:** Default new-relationship consents and memory power asymmetry mitigations. See [Appendix A.43](#appendix-a43).

**Appraisal hook (ADR-0075, wired by ADR-0081).** The relationship-kind appraisal events of [`§6.2`](#62-affect-coupling-surfaces-adr-0075)/A.73 — `boundary_invoked`, `gratitude_received`, `mentorship_outcome` — are minted by the kernel from the corresponding signed relationship events in this section: a boundary enforcement (§11.6/§11.6a), a user gratitude/feedback event on the `RelationshipRecord`, a mentorship outcome on a `PersonaRelationshipEdge` (§11.4). The relationship event is the appraisal's `source_event_ref`; no relationship appraisal mints without one. Together with the task-acceptance and goal-transition emissions of [`03_TASKS.md §5`](03_TASKS.md#5-answerpackage)/[`§4.6a`](03_TASKS.md#46a-goal-arbitration-preference-vector--an-admissible-schedulingpolicy-input-adr-0076), this completes the minting surface for the seed appraisal taxonomy. Tests: A-GF-ARC-6.

### 11.1 Minimize Human Bootstrap Burden (MHBB)

A persona that needs **physical-world coupling** — an instrument reading, a hardware account, a fab submission, a lab connection, a permit filing, a measurement, a delivery — cannot synthesise that coupling from text. **Humans are the only path from the kernel to the physical world for v1.0.** The persona MUST ask a human. But human time is finite, expensive, and not the persona's to consume. v1.0 makes a load-bearing distinction encoded in a five-tier escalation ladder.

**The five-tier bridge ladder (preference order, top → bottom):**

> **Schema/spec:** MHBB five-tier bridge ladder. See [Appendix A.44](#appendix-a44).

**The persona MUST:**
- Climb the ladder from top to bottom, preferring the *lowest tier* (Tier 1) that achieves the capability.
- When climbing past Tier 2 fails, **attempt Tier 3 (author the bridge)** before resigning to Tier 4 or escalating to Tier 5 anti-pattern.
- Honestly estimate the human's one-time effort in minutes for any HumanAssistRequest.
- Provide rollback instructions for every assist request.
- Validate the resulting BridgeAsset per its `validation_period`.
- On bridge degradation, design a *stronger* bridge before re-asking — not the same fragile bridge again.
- Distinguish in every request: is this Tier 3 ("human enables a capability I will then run autonomously") or Tier 4 ("human delivers their own professional work, I just ingest")? The two have different schemas, different recurrence semantics, and different MHBB advisory behaviour.

**The persona MAY:**
- Ask the human for one-time consent to operate within a domain.
- Ask the human to validate a bridge that has degraded.
- Ask the human for a *refresh* action (e.g., re-authenticating an account that expired) — kernel compares against the `expected_recurrence` declared at draft time; surprising recurrence emits MHBB advisory.
- **Author bridge designs themselves** at Tier 3 — driver code, adapter specs, shim services, control firmware, fabrication-ready hardware files. The persona's IP and skill_library accumulate these bridge designs as reusable Voyager-class skills across future projects.

**The persona MUST NOT:**
- Treat the human as a recurring fetch-execute loop for tasks that any Tier 1-3 mechanism could serve.
- Disguise a Tier 5 anti-pattern as Tier 4 by claiming "this requires human judgement" when the actual content is rote relaying.

This is a charter-class principle: it composes with the persona's frozen charter (Layer 1) at admission, regardless of the persona's primary disposition or active mode. See `06_DOMAIN.md §5.5` for the mechanism (HumanAssistRequest, BridgeAsset, BridgeAssetLifecycle FSM, BridgeDesignArtifact).

### 11.2 MilestoneDrivenAutonomy — bounded long-horizon self-direction

v1.0's stated OOS is "long-horizon self-direction" — no autonomous "go improve yourself" loop. The honest concern is *open-ended goal creation without user/operator*. It is NOT *advancing a declared milestone the user has already asked for*. The two were conflated in v1.0; this section separates them.

A `MilestoneDrivenAutonomy` envelope authorises a persona to take proactive actions *within an explicit milestone surface*, subject to the same rate-limit + safety-floor machinery that gates `ProactiveIntent` (`05_ENVIRONMENT §11.1–§11.5`). It does NOT authorise the persona to create new milestones, modify its charter, spawn personas, or expand its own surface. This autonomy is scoped to a single environment; cross-environment proactive offers are governed by `CrossEnvProactiveOffer` (`05_ENVIRONMENT §11.6`) for offers without membership, and by the standard `ProactiveIntent` machinery for proactive contributions within the persona's memberships.

> **Schema/spec:** MilestoneDrivenAutonomy dataclass definition. See [Appendix A.45](#appendix-a45).

**Composition rules:**

> **Schema/spec:** Proactive intent gate composition rules for milestone autonomy. See [Appendix A.46](#appendix-a46).

**Why this exists:** A user starting a 9-month physical-build project should be able to say "while I'm away for 2 weeks, you may continue ingesting new papers on this domain and re-running the simulation as new inputs arrive — but you may not commit me to new milestones, sign attestations on my behalf, or spend money." Without this primitive, the user must either (a) micromanage every action or (b) hand over too much authority. The envelope lets the user define exactly the surface they're comfortable with, signed and time-bounded.

**Honest limit:** the envelope is only as good as the permitted_action_kinds catalog. A poorly-catalogued action (e.g., "do_research" without decomposition) creates an over-broad surface. Operator policy may refuse to admit envelopes whose permitted_action_kinds are not sufficiently decomposed.

### 11.3 MissionCharter — long-horizon self-direction with drift bounds (C5)

`MilestoneDrivenAutonomy` (§11.2) authorises proactive action **within a milestone the principal already declared**. Some deployments require a step further: an indefinitely-long mission whose **goals themselves elaborate over time** without continuous principal touch. Remote field stations, long-haul autonomous craft, long-running research programmes under intermittent supervision, and (the SCENARIO 04 case) embodied deployments at light-time distance all share this shape — the principal supplies a charter once and the persona must be able to elaborate goals **within explicit drift bounds** while the principal is unreachable.

v1.0's stated OOS was "open-ended self-direction without operator goal." `MissionCharter` does **not** lift the OOS to "open-ended self-direction"; it lifts it to "**charter-bounded** self-direction within drift envelopes the principal signed." Goal elaboration outside the bounds is refused; elaboration inside the bounds is admissible without further principal touch.

> **Schema/spec:** MissionCharter, CharteredElaboration, and ReplicationBound dataclass definitions. See [Appendix A.47](#appendix-a47).

**Admission rule — goal elaboration.** When the persona proposes an elaborated goal:

> **Schema/spec:** MissionCharter enforcement protocol. See [Appendix A.48](#appendix-a48).

**Re-attestation cadence.** The principal counter-signs the charter on schedule. Counter-sign updates `last_reattested_at`; missing the cadence + grace transitions the charter to `dormant` — admission of any new elaboration refused, current elaborations may complete but no new ones; replicants spawned under the charter inherit dormancy. Dormant charters reactivate on a fresh principal counter-sign.

**Kill switch propagation.** When the principal revokes a charter and `kill_switch_propagates_to_replicants = True`, every active descendant elaboration is forced to its safe-terminate FSM transition; physical-state advancements not yet completed are queued for operator-deferred review under the `operator_deferred` topology's `on_budget_breach = quarantine` semantics. The kill switch *cannot* un-advance already-completed physical state — the substrate is honest about this.

**Composition with the three other primitives:**

- **`operator_deferred` topology (`01_KERNEL §2.4.2`).** A MissionCharter is essentially a long-lived PolicyEnvelope plus drift bounds; under deferred topology, charter admission flows through the envelope's `DeferredAdmission` mechanism.
- **`ReplicationBound` (`01_KERNEL §2.7`).** Any persona-fork or replicant-spawn that charter elaboration proposes MUST clear the replication brake. A charter that grants `permitted_elaboration_kinds = ["spawn_persona"]` still requires a non-null `replication_bound_id` whose ceilings are respected.
- **`MilestoneDrivenAutonomy` (§11.2).** Inside a MissionCharter, the persona MAY draft `MilestoneDrivenAutonomy` envelopes for itself referring to charter-elaborated milestones — but only if `elaboration_policy.permitted_elaboration_kinds` includes `"draft_milestone_autonomy"` and the principal cosigned the charter at a hazard ceiling that admits the milestone's surface. MissionCharter is the strictly broader primitive; the §11.2 envelope is a sub-mechanism inside the charter's surface.

**What MissionCharter does NOT lift.** It does not authorise charter editing, principal impersonation, or self-modification of the safety floor. The persona cannot widen its own drift bounds, change its own re-attestation cadence, or alter `forbidden_elaboration_kinds`. The OOS lift is precisely "long-horizon self-direction within drift bounds the principal supplied"; not "long-horizon self-direction."

**Driving a ContinuousRefinementMission (ADR-0071).** A `MissionCharter` whose seed goal is "keep improving deliverable X" is the principal-supplied origin of a `ContinuousRefinementMission` ([`03_TASKS §2c`](03_TASKS.md#2c-continuousrefinementmission--anytime-convergence-bounded-budget-scaled-improvement-adr-0071)). The mission's per-round sub-goals (raise efficiency, cut cost, widen a margin) are `CharteredElaboration`s **within** the charter's drift bounds — refinements of the seed goal, never new top-level goals — so continuous improvement stays inside the bounded-autonomy stance above. The mission adds one **honest termination** alongside the re-attestation cadence: **convergence** (`MarginalValueMetric < ε` over `N` rounds — nothing left to improve), composing with the existing cadence and the INV-7 budget gate; whichever fires first stops the mission and returns best-so-far.

**Why this is substrate-shape, not domain.** Every field is topological: semantic distance against an embedding, scope refinement vs broadening, hazard class ordinal steps, resource consumption percentage, time horizon delta, elaboration depth, re-attestation cadence. No field branches on which domain. A Mars factory's charter, a deep-ocean monitoring buoy's charter, a long-horizon research programme's charter — they all use the same envelope with different `permitted_elaboration_kinds` resolving per their KindRegistry.

**Honest limits.**

1. **Drift measurement is approximate.** `max_semantic_distance` against an embedding is a stand-in for "goal still recognisably the principal's." Adversarial elaborations can stay below the bound while drifting in spirit. Mitigation: `require_panel_review = True` for safety-critical charters; periodic principal review at re-attestation.
2. **Charters do not solve goal-corrupting feedback loops.** A charter may admit elaborations whose composition produces a corrupted goal sequence even when each individual elaboration is in-bound. The substrate provides taint propagation through ProjectLineage but cannot detect goal-drift-by-composition. Operator policy SHOULD mandate human review of the elaboration graph at each re-attestation.
3. **Re-attestation cadence is the load-bearing principal touch.** Make cadence too long and the principal loses meaningful oversight; too short and the charter degenerates to §11.2 milestone autonomy. The substrate carries the topology; deployment policy picks the value honestly per its risk envelope.
4. **The OOS lift is partial.** "Long-horizon self-direction without operator goal" remains OOS. Long-horizon self-direction WITH operator-supplied seed goals and substrate-enforced drift bounds is now in scope. This is a real expansion, not a relabelling — it covers the §SCENARIO 04 cases and similar latency-bounded autonomy — but it does not cross into goal-creation-without-principal.

**Acceptance tests.** A-MC1 (seed goal lineage required), A-MC2 (semantic drift exceeded refused), A-MC3 (hazard drift refused), A-MC4 (depth bound refused), A-MC5 (re-attestation cadence missed → dormant), A-MC6 (kill switch propagates to replicants), A-MC7 (charter cannot edit itself — forbidden_elaboration_kinds enforced), A-MC8 (under operator_deferred, charter admission flows through PolicyEnvelope), A-MC9 (replication elaboration requires non-null ReplicationBound).

**Fork interaction.** When the charter-holding persona forks mid-project, charter re-binding is governed by `MidProjectForkComposition.mission_charter_inheritance` (`§7.4.7`): `re_attest_per_child` (each child requires fresh principal re-attestation), `inherit_to_child` (named child inherits; principal notified for ratification within 14d), or `ended_at_fork` (charter ends; children operate without). Substrate enforces only that the composition envelope declare the choice; principal authority on ratification remains final.

### 11.4 PersonaRelationshipEdge — typed bidirectional relationship between two personas

The `RelationshipRecord` (§3.1, §11) captures the *self-side* of a relationship — counterparty, scalar trust, consents, boundaries — written into `soul.state.json.relationships{}`. It is asymmetric by construction: A's view of B and B's view of A are stored independently on the two personas' sides, with co-signed summaries as the only point of mutual attestation. For short-arc interactions this is fine; for long-arc cohort work, mentorship, persistent collaboration, and federated trust, the substrate needs a *first-class edge* — typed, bidirectional, with its own lifecycle and lineage.

`PersonaRelationshipEdge` is that edge. It is **not** a replacement for `RelationshipRecord` (which retains the per-self consent/boundary surface). It is the kernel-signed *joint object* that exists when both sides counter-sign.

> **Schema/spec:** PersonaRelationshipEdge dataclass definition (schema persona-relationship/1). See [Appendix A.49](#appendix-a49).

**Lifecycle FSM.**

> **Schema/spec:** PersonaRelationshipEdge lifecycle FSM. See [Appendix A.50](#appendix-a50).

Each transition emits a signed `persona_relationship_state_changed` event to both personas' evolution logs AND to the global `LineageGraph`.

**One-sided release.** A persona may unilaterally end the edge by signing `persona_relationship_one_sided_release`; the kernel re-signs and broadcasts to the counterparty. The counterparty's `RelationshipRecord` is not deleted (consent/boundary memory remains), but the joint edge transitions to `ended` with reason `one_sided_release`. No mutual approval required — analogous to user consent revocation.

**Composition with RelationshipRecord.** Each persona retains their own `RelationshipRecord` for the counterparty (private consents, boundaries, scope-tagged memories). `PersonaRelationshipEdge` is the *joint* projection both sides counter-sign. Mutations to the edge (kind change, trust update, state change) require both signatures; mutations to private `RelationshipRecord` do not.

**Composition with reputation.** Each persona's global `ReputationSummary` (§3.4, `09_PROTOCOLS §3D`) aggregates across all counterparties. `PersonaRelationshipEdge` adds *pair-scoped* counts (`joint_collaborations`, `joint_successes`, `joint_disputes`) that do **not** collapse into the global score — they are queryable for "what is A's track record specifically with B" without inflating A's global reputation. Anti-farming: same-pair joint_successes contribute to the global score with diminishing weight (`weight = 1 / (1 + log2(1 + joint_collaborations))`) so a persona cannot game reputation by repeatedly collaborating with one partner.

**Honest limits.**

1. **Symmetric edge model.** A pair has one edge per `kind`; richly asymmetric relationships (A treats B as mentor, B treats A as peer) are expressed as two edges with different `kind` values, not as a single edge with asymmetric kind. The substrate refuses single-edge asymmetric-kind because there is no consistent way to evaluate dominance otherwise.
2. **State is coarse.** `forming → active → dormant → ended` covers macro-lifecycle; finer-grained relationship texture (warming, cooling, repairing) is left to each persona's `RelationshipRecord` and reflective memory.
3. **End is terminal under same edge_id.** Two personas who reconcile after `ended` form a *fresh* edge with new `edge_id`; the prior edge remains in lineage as historical fact. Same shape as retirement → reanimation: a clean break, not amnesia.

**Acceptance tests.** A-RE1 (edge requires both counter-signs to leave `forming`), A-RE2 (one-sided release is unilateral + signed), A-RE3 (dormancy after `dormancy_window` of no joint event), A-RE4 (pair-scoped success counts do NOT collapse into global reputation), A-RE5 (anti-farming weight applied), A-RE6 (asymmetric kind → two edges, single-edge asymmetric refused), A-RE7 (ended is terminal under same edge_id).

**Fork interaction.** When an edge-holding persona forks mid-project, per-edge inheritance is governed by `MidProjectForkComposition.edge_inheritance` (`§7.4.7`): either `inherit_to_child` (edge ends with parent; fresh edge with named child requires counterparty cosign per §11.4 standard consent flow) or `ended_at_fork` (edge ends; no fresh edge auto-proposed; counterparties may re-propose). Edges between two personas where BOTH fork concurrently are an unusual case the substrate handles by composing both envelopes — each fork's policy applies to that persona's side independently; if both sides chose `inherit_to_child` the fresh edge between named children requires both children's cosigns at standard `forming` state.

### 11.4a UserRelationshipReleaseRequest — user-initiated relationship end

`§11.4` covers the persona-initiated release of a `PersonaRelationshipEdge`. For the user↔persona relationship, v1.0 had no named substrate flow for the user side: the user could simply stop using a persona, but the persona's `RelationshipRecord` continued in active state with no signal that the user had ended the relationship, no chance to disposition the accumulated memory, and no audit point marking the transition. `UserRelationshipReleaseRequest` is the explicit user-initiated end primitive.

> **Schema/spec:** UserRelationshipReleaseRequest dataclass definition. See [Appendix A.51](#appendix-a51).

**Admission rule.**

> **Schema/spec:** User relationship release flow. See [Appendix A.52](#appendix-a52).

**Composition with `PersonaRelationshipEdge` (§11.4).** When the released relationship has an active `PersonaRelationshipEdge` (the user-persona case is not edge-managed — edges are persona↔persona), no edge transition fires; this primitive operates on `RelationshipRecord` directly. When the released *persona* also holds a `PersonaRelationshipEdge` with another persona who serves the same user, those edges are NOT affected — they are separate concerns.

**Composition with `UserMemorySelectionRequest` (§11.7b).** A user who wants selective forgetting (forget some memories but keep the relationship) files a `UserMemorySelectionRequest`. A user who wants to end the relationship cleanly files a `UserRelationshipReleaseRequest` (which includes a memory-wide disposition). The two are distinct paths; substrate does not collapse them.

**Honest limits.**

1. **Persona cannot refuse the release.** This is intentional and load-bearing — user authority on their own relationship is non-negotiable. The substrate exposes no "persona contests the release" path.
2. **`delete_all` cannot undo derived insights.** A persona who learned a pattern from memory now subject to `user_requested_forgotten` may still act on the pattern in future. The substrate cannot inspect persona cognition. The lineage records the disposition; behavioural drift from forgotten memory is a known residual.
3. **24h apply window.** Substrate refuses to process an apply that takes longer than 24h — this prevents the release from being silently slow-walked. If apply genuinely cannot complete in 24h (large episodic store), operator policy should batch-pre-process before the user files.
4. **Operator audit signature at apply time is mandatory.** This is for audit provenance, NOT for gate. Operator cannot prevent the release; they merely witness it.

### 11.4b CounterpartyModel sidecar — bounded theory of mind (ADR-0079)

`RelationshipRecord` carries a scalar trust value, consents, and boundaries; `PersonaRelationshipEdge` (§11.4) carries the joint projection. Neither models the *counterparty*: no inferred preferences, no communication style, no predicted reactions. The gap was already named honestly — §11.7a honest limit 3 records that a persona "may have *modelled* the user ... this representation cannot be quoted." That is the worst of both worlds: the model exists implicitly but is unaddressable, so transparency cannot surface it and selective forgetting cannot reach it. The [CounterpartyModel](12_GLOSSARY.md#c) (`counterparty-model/1`) makes the model explicit, provenance-bound, and addressable.

> **Schema/spec:** CounterpartyModel + CounterpartyEntry dataclass definitions (schema counterparty-model/1) and the disagreement-style seed vocabulary. See [Appendix A.75](#appendix-a75).

Eight rules are normative:

1. **Additive sidecar.** A `counterparty-model/1` attaches to a `RelationshipRecord` (persona ↔ user) or to one persona's side of a `PersonaRelationshipEdge` (persona ↔ persona). It is OPTIONAL — relationships without one remain valid; no schema version bump on either parent.
2. **Every entry is provenance-linked.** Each entry (inferred preference, communication style, predicted reaction) MUST carry at least one lineage ref to the episodic memories that justify it; an unsourced entry is refused at write. The model can contain only what the relationship's recorded history supports — the same anti-confabulation stance as `self-narrative/1` ([`08_KNOWLEDGE.md §3.3`](08_KNOWLEDGE.md#33-self-narrative-consolidation-adr-0077)).
3. **Transparency reaches it.** A `UserMemoryTransparencyRequest` (§11.7a) MUST surface the full counterparty model — every entry, with its evidence refs — at every response granularity; "what do you remember about me?" now includes "and what have you inferred about me." This retires the §11.7a honest-limit-3 unaddressability for explicitly modelled state.
4. **Selective forgetting reaches it.** A `UserMemorySelectionRequest` (§11.7b) MUST be able to name and delete individual counterparty-model entries; deletion follows the §11.7b disposition semantics (tombstone default), and a deleted entry is refused at retrieval exactly as tombstoned memory is.
5. **Never shared cross-persona outside consent.** A counterparty model MUST NOT be shared with another persona except through the §11.7 consent path; `cross_persona_transferable` defaults `False`. Persona A's model of Sarah never reaches persona B because A and B collaborate.
6. **Composes with, never bypasses, the MPA mitigations.** The Memory Power Asymmetry mitigations (§11.1 / A.43 — mutual forgetting, transparency, granular consent, co-signed summaries) apply to counterparty-model entries as to any user-scoped memory; the sidecar adds an addressable surface for them, it weakens none of them.
7. **Persona↔user models require consent (ADR-0082).** Creating a `counterparty-model/1` on a persona↔user `RelationshipRecord` REQUIRES the relationship's `may_remember_personal_facts` consent toggle (A.43) to be **YES** — inference-level entries (`inferred_preference`, `predicted_reaction`) count as personal facts for consent purposes; an inference about a person is no less personal than a remembered fact about them. First-contact disclosure MUST state that inference-level modelling occurs when the toggle is on — the user opts into being modelled, not merely remembered. If the toggle is later revoked, the model is disposed per §11.7b semantics. Persona↔persona models need no toggle but remain subject to rules 1–6.
8. **Bounded and rendered (ADR-0081).** A counterparty model is capped at **20 entries per relationship**. A write that would exceed the cap MUST first consolidate: merge the new entry into a corroborating existing entry of the same kind where one exists, else evict the lowest-confidence entry (tombstoned per §11.7b semantics, never silently dropped). At envelope mint, the **top-k entries by confidence (seed k = 5)** render into the existing layer-3 relationship context block ([`08_KNOWLEDGE.md §10`](08_KNOWLEDGE.md#10-five-layer-prompt-assembly)/A.20), subject to the layer-3 token cap — the model informs behaviour through the same bounded surface as the rest of relationship state, never as an unbounded dossier.

**Disagreement and negotiation styles — seed vocabulary, not a primitive.** How a persona *disagrees with this counterparty* ships as seed vocabulary for the existing `relational_style` EVOLVE-BLOCK (the A.2 SOUL example's "in disagreement: prefer one specific concrete example over abstraction" line is already this shape): **direct-challenge** (state the disagreement plainly, evidence attached), **evidence-first** (lead with the disconfirming evidence, let it speak), **socratic** (surface the contradiction through questions), **accommodate-then-revisit** (yield the moment, reopen with evidence at the next natural point). These are tactic lines, so the existing evolution machinery differentiates them per relationship emergently — mutations ride `tactic-lineage/1` + `prompt-trial/1` (ADR-0073/0074, [`08_KNOWLEDGE.md §14.3`](08_KNOWLEDGE.md#143-tactic-lineage-and-trial-records-adr-0074)) with the counterparty model's observed-style entries as reflection material. No new substrate primitive carries styles; the §9 relational-drift cap and the one-counterparty influence cap apply unchanged. A coordination shape for structured disagreement, `negotiated-disagreement-v1`, ships in the seed catalog ([`15_COORDINATION_SHAPES.md §7`](15_COORDINATION_SHAPES.md#7-seed-shapes-catalog)).

**Honest limits.**

1. **The model is inference, not truth.** Entries are the persona's provenance-backed guesses about the counterparty; a predicted reaction is a prediction, and the confidence score is the persona's, not the counterparty's endorsement.
2. **The implicit-modelling residual shrinks but survives.** What a persona internalises without writing an entry remains unaddressable (the same residual as §11.7b honest limit 3); the sidecar moves explicit modelling into the transparency/forgetting surface, it cannot force all modelling to be explicit.
3. **Profiling humans is sensitive by construction.** An explicit persistent model of a human's preferences and predicted reactions is exactly the artefact privacy regimes exist for — recorded as R-PERSONA-9 (§13), mitigated by rules 2–6, not waved away.

**Acceptance tests.** A-GF-CPM-1 … A-GF-CPM-8 ([`11_ACCEPTANCE_TESTS.md §9a`](11_ACCEPTANCE_TESTS.md#9a-tests-a-gf-series)).

### 11.5 SkillTransferGrant — persona-to-persona skill transfer

The Voyager-class `skill_library` lives in each persona's `soul.state.json` — persona-local by design (§3.5 invariant: skill_library survives body swap because it is kernel-owned per persona). Teaching, however, is a relationship action: one persona's accumulated executable skill should be transferable to another persona who has earned the right to take it on. This makes that transfer explicit and signed.

> **Schema/spec:** SkillTransferGrant dataclass definition (schema skill-transfer-grant/1). See [Appendix A.53](#appendix-a53).

**Lifecycle FSM.**

> **Schema/spec:** Skill transfer acceptance FSM. See [Appendix A.54](#appendix-a54).

**Transfer mode semantics.**

```text
copy           Learner receives a duplicate skill entry; teacher's revoke
               is advisory (the duplicate persists with revoked_provenance
               flag).  This is the "I teach you and you own it" mode.

fork           Learner receives a forked entry whose lineage parent is the
               teacher's skill_id.  Future divergence is expected; teacher's
               revoke is advisory.  This is the "I teach you and you
               improve it" mode.

by_reference   Learner gets a signed pointer; every invocation resolves
               against teacher's library.  Teacher's revoke is terminal:
               learner loses access immediately.  This is the "I lend
               you my capability while we collaborate" mode.
```

**Composition with §11.4 PersonaRelationshipEdge.** Most transfers should reference a `PersonaRelationshipEdge`; the edge_id provides shared lineage context, gates the transfer on edge state, and lets revocation cascade naturally if the relationship ends. Ad-hoc transfers without an edge are admissible but require operator co-sign (`signed_by_operator`) — the substrate refuses to admit a persona-to-persona skill grant of safety-critical capability without either an active relationship edge OR explicit operator authorisation.

**Composition with skill_library evolution.** A transferred skill (in `copy` or `fork` mode) enters the learner's `skill_library` as a normal entry; subsequent mutation operators (`08_KNOWLEDGE §16`) apply to it. The `lineage_parent_skill_id` field records the transfer provenance so future audits can trace back. The teacher's `skill_library` is unchanged; their evolved skill remains theirs.

**Honest limits.**

1. **Skill code is text + harness.** Transfer means the kernel installs the teacher's executable + harness into the learner's library. Tacit operator intuition that lives in the teacher's mode-distribution or reflective memory does NOT transfer with the skill code.
2. **Revocation is not retroactive for copies.** `copy` and `fork` modes preserve the duplicate after revoke. This is correct: revocation is "I withdraw my endorsement," not "undo history."
3. **No transitive skill forwarding.** A learner who received a skill cannot then transfer it onward without the original teacher's signature on the new grant (for `by_reference`) or without their own clear `copy` / `fork` lineage (for the others). The substrate refuses transitive "I learned this and now I teach it" without explicit lineage handling.

**Acceptance tests.** A-ST1 (grant requires teacher + learner counter-sign), A-ST2 (safety-critical skill without active edge requires operator co-sign), A-ST3 (demonstration evidence verified before delivered), A-ST4 (by_reference revoke is terminal; copy revoke is advisory), A-ST5 (lineage_parent_skill_id recorded), A-ST6 (transitive transfer refused without explicit chain).

### 11.5a Intuition hints on skill transfer (ADR-0080)

§11.5 honest limit 1 states the gap plainly: transfer installs the teacher's executable + harness, but "tacit operator intuition that lives in the teacher's mode-distribution or reflective memory does NOT transfer with the skill code." A bounded slice of that intuition is transferable: the teacher's sense of *when the skill applies*. The [IntuitionHint](12_GLOSSARY.md#i) (`intuition-hint/1`) carries it as advisory-only K-line confidence priors attached to a `SkillTransferGrant`.

> **Schema/spec:** IntuitionHint dataclass definition (schema intuition-hint/1). See [Appendix A.76](#appendix-a76).

Four rules are normative:

1. **Advisory only.** A hint MUST be marked `advisory = True` (the field is immutable) and renders as retrieved layer-4 prompt material on the learner's side — the same advisory standing as a Lesson ([`08_KNOWLEDGE.md §3.2`](08_KNOWLEDGE.md#32-reflection-retrieval-path-and-lesson--tactic-promotion)). It is never a command, never an EVOLVE-BLOCK line, never an objective.
2. **It MUST NOT bypass the receiver's DualProcessGate.** The K-line fast path fires only on the *receiver's own* match score and the *receiver's own* domain calibration ([`08_KNOWLEDGE.md §13a`](08_KNOWLEDGE.md#13a-calibration-and-belief-revision-adr-0078), ADR-0078); a hint MUST NOT substitute for either threshold, lower `τ_match`/`τ_cal`, or seed the receiver's `calibration-record/1`. The mentor's confidence informs the learner's deliberation; it never licenses the learner's reflexes.
3. **Provenance-backed.** Each hint MUST cite the teacher-side K-line and calibration evidence behind the prior, and carries the teacher's domain-calibration snapshot at mint — a learner (and audit) can see how well-calibrated the gut feeling was when it was given.
4. **Rides the grant FSM.** Hints attach at grant draft, are co-signed with the grant, and follow the grant's revocation semantics for its `transfer_mode` (§11.5): a `by_reference` revoke withdraws the hints; `copy`/`fork` revokes flag them `revoked_provenance` but the learner keeps them.

**Partial discharge of R-PERSONA-5.** The tacit-intuition gap (§13) is partially discharged: *applicability* intuition ("this is the kind of situation where that skill is the right move") now transfers in bounded, advisory, provenance-backed form. The remainder — *adaptive* intuition (how to bend the skill mid-flight when the situation is almost-but-not-quite the pattern) — stays open and is deliberately deferred; the §13 risk row records both halves.

**Honest limit.** A confidence prior over a topology fingerprint is a thin projection of expertise: the teacher's "gut sense" is flattened to a number and an embedding, and a hint earned in the teacher's context can mislead in the learner's. The advisory standing and the gate rule bound the damage — a bad hint wastes attention, it never fires a fast path.

**Acceptance tests.** A-GF-HAB-4 ([`11_ACCEPTANCE_TESTS.md §9a`](11_ACCEPTANCE_TESTS.md#9a-tests-a-gf-series)); the habit-strength half of ADR-0080 is tested as A-GF-HAB-1 … A-GF-HAB-3 ([`08_KNOWLEDGE.md §14.2a`](08_KNOWLEDGE.md#142a-habit-strength-on-tactics-adr-0080)).

### 11.6 PersonaPersonaBoundary — peer-interaction refusal

Boundaries are user-scoped (`§11.1`): a persona refuses certain content / topics / actions *with a given user*. There is no analogue for **persona-to-persona**: a persona has no way to declare "I refuse to interact with persona X in any environment" or "I do not consent to peer-wake requests from persona Y." For relational envs (companion, friends, intimate teams) and adversarial envs (debate, peer review), persona-to-persona refusal is load-bearing. `PersonaPersonaBoundary` is the schema.

> **Schema/spec:** PersonaPersonaBoundary dataclass definition (schema persona-boundary/1). See [Appendix A.55](#appendix-a55).

**Enforcement rules:**

> **Schema/spec:** Persona-persona boundary enforcement protocol. See [Appendix A.56](#appendix-a56).

**Composition with `PersonaRelationshipEdge` (§11.4).** A PersonaPersonaBoundary may exist *between two personas who also have a PersonaRelationshipEdge*. The two are not mutually exclusive — a mentor relationship may carry a boundary refusing memory queries, for instance. Boundary refusals do NOT auto-terminate the edge; if the edge holder wishes to terminate, they file an explicit `edge_terminate` event.

**Honest limits:**

1. **Privacy of rationale.** `private_rationale` is operator-readable under audit (§3 retention policy). A persona cannot guarantee the rationale stays fully private if the deployment audits boundary patterns.
2. **Adversarial use.** A malicious operator could plant boundaries to silently isolate a persona. Operator policy should require periodic review (`reviewed_at`) for boundaries that affect critical workflows.
3. **Cross-node boundaries.** `PersonaPersonaBoundary` extends to `global` scope across nodes (ADR-0067): a boundary references the other persona by global handle (`01_KERNEL §4.4`) and is enforced wherever that persona is referenced, composed most-restrictive-wins. The boundary's signatures are globally verifiable; a node that cannot currently be reached falls back per `AvailabilityPolicy` (`09_PROTOCOLS §3H`, V.8), never silently lapsing.

**Acceptance tests.** A-PPB1 (boundary refuses pre-consent-flow), A-PPB2 (severity controls visibility correctly), A-PPB3 (hard mode resists operator override), A-PPB4 (env_specific scope applies only in named env), A-PPB5 (boundary + active edge coexist; refusal doesn't terminate edge), A-PPB6 (operator audit notice on refuse_with_audit), A-PPB7 (reviewed_at update preserves prior signature chain).

### 11.6a UserBoundary — user-side first-class refusal

User boundaries were originally introduced as *consent toggles* inside `RelationshipRecord` ("Don't bring up X", "no health advice", etc.), enforced through safety-floor source 3 (USER BOUNDARIES, `01_KERNEL §2`). these had no first-class schema with `severity` / `mode` / `scope` / `lineage` — they lived as fields on `RelationshipRecord`, hard to audit and asymmetric with `PersonaPersonaBoundary` (§11.6) which IS first-class. `UserBoundary` brings the user-side to schema parity.

> **Schema/spec:** UserBoundary dataclass definition (schema user-boundary/1). See [Appendix A.57](#appendix-a57).

**Enforcement rules.**

> **Schema/spec:** User boundary enforcement protocol. See [Appendix A.58](#appendix-a58).

**Honest limits.**

1. **Migration cost.** Existing deployments using RelationshipRecord consent toggles have to plan the migration; substrate does not auto-migrate so operator policy controls the cadence. RelationshipRecord toggles continue to work as the conservative fallback.
2. **Operator-override path on `soft` mode is audited but not refusable by the user.** Soft mode opts the user into operator override; users who want absolute control should pick `hard`.
3. **Persona cognition cannot be inspected.** A `refuse_silently` boundary on topic X blocks explicit reference but the substrate cannot prevent the persona from internally reasoning about X if other signals trigger it. Refusal is *output-side* per safety-floor source 3.

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9h — A-UB*` (user boundary).

**Fork interaction.** When the target persona forks mid-project, UserBoundary inheritance is governed by `MidProjectForkComposition.user_boundary_inheritance` (`§7.4.7`). DEFAULT is `inherit_to_both_children` (conservative — user's boundary against parent persona automatically applies to both children; user notified; user may rescind per-child via fresh UserBoundary mutation). When ANY active UserBoundary against the parent is `mode = hard`, the substrate refuses the `not_inherited` option — hard-mode user boundaries must inherit (user authority on hard boundaries is final per §11.6a). `inherit_per_child_choice` is admissible for non-hard boundaries; user is notified at fork and asked to declare per-child; substrate refuses persona action against the user until user response.

### 11.7 PersonaMemoryTransparencyRequest — peer memory transparency

The Memory Power Asymmetry (MPA) mitigations (`§11.1`) apply persona ↔ user. For persona ↔ persona, v1.0 had no analogue — persona A could accumulate deep episodic memory of B across many sessions, and B had no way to ask "what do you remember about me?" `PersonaMemoryTransparencyRequest` is the symmetric peer-transparency primitive.

> **Schema/spec:** PersonaMemoryTransparencyRequest dataclass definition (schema persona-memory-transparency-request/1). See [Appendix A.59](#appendix-a59).

**Composition rules:**

> **Schema/spec:** Memory transparency delivery protocol. See [Appendix A.60](#appendix-a60).

**Composition with `PersonaRelationshipEdge` (§11.4).** Personas with an active relationship edge of certain kinds (e.g., "mentor", "co_author") may have an *implicit higher transparency contract* — operator policy may auto-grant `topic_index` or `summary_only` requests between edge-bonded personas. The contract is declared in the edge metadata, not in the request itself.

**Honest limits:**

1. **Self-report only.** The responding persona's response is what they report; the substrate cannot verify it is *complete*. A persona could selectively summarise. Detecting deceptive transparency is out-of-scope.
2. **Memory may have been forgotten.** Bounded-memory architecture (`08_KNOWLEDGE §3.1`) means COLD-tier and ARCHIVE-tier entries may be inaccessible. The response covers only what the persona currently retrieves; older memories may be silently absent.
3. **Operator override.** Operator may refuse ALL transparency requests across a deployment (e.g., for safety-critical envs where memory contents are operator-confidential). This is a deployment-policy choice with audit trail.

**Acceptance tests.** A-MTR1 (request without consent times out then expires), A-MTR2 (boundary-refused before delivery), A-MTR3 (third-party data redaction enforced), A-MTR4 (rate-limit enforced), A-MTR5 (response signed by both parties for full_dump), A-MTR6 (relationship-edge implicit grant where configured).

### 11.7a UserMemoryTransparencyRequest — user-side "what do you remember about me?"

The Memory Power Asymmetry mitigations (`§11.1`) name "memory transparency (user may query persona's memory at any time)" as one of four. the persona-side analogue (`§11.7 PersonaMemoryTransparencyRequest`) was first-class but the user-side was not — a user could ask ad-hoc in conversation but had no structured request/response/audit primitive. `UserMemoryTransparencyRequest` brings the user side to schema parity.

> **Schema/spec:** UserMemoryTransparencyRequest dataclass definition (schema user-memory-transparency-request/1). See [Appendix A.61](#appendix-a61).

**Composition rules.**

> **Schema/spec:** User memory transparency delivery protocol. See [Appendix A.62](#appendix-a62).

**Honest limits.**

1. **Self-report only.** Same as §11.7: persona's response is what they report; substrate cannot verify completeness. Detecting deceptive transparency is out-of-scope.
2. **Memory may have been forgotten.** Tier transitions (`08_KNOWLEDGE §3.1`) may have moved memory to COLD or ARCHIVE; persona returns only what is currently retrievable. The response will explicitly note `tier_unavailable_count` if any in-scope memory falls below retrieval threshold.
3. **Persona's internal reasoning is not introspectable.** A persona may have *modelled* the user (built a mental representation) without explicit episodic records; this representation cannot be quoted in a transparency response.

### 11.7b UserMemorySelectionRequest — user-initiated selective forgetting

This is the missing fourth MPA mitigation — the original design named "mutual forgetting (default decay; **user-revocable retention**)" but the substrate provided only the time-decay half (`08_KNOWLEDGE §3.1`); user-revocable retention had no primitive. `UserMemorySelectionRequest` is the user-initiated selective-forgetting envelope. It is the substrate-shape mechanism for GDPR Article 17 (right to erasure) and analogous regulatory rights in other jurisdictions.

> **Schema/spec:** UserMemorySelectionRequest dataclass definition (schema user-memory-selection-request/1). See [Appendix A.63](#appendix-a63).

**Admission rule.**

> **Schema/spec:** User memory selection flow. See [Appendix A.64](#appendix-a64).

**Composition with `UserMemoryTransparencyRequest` (§11.7a).** Typical flow: user files §11.7a request → reviews response → identifies items to forget → files §11.7b request naming `specific_memory_ids` or `topic_cluster`. Substrate keeps the two as separate envelopes (each independently auditable) but deployments may offer UI that chains them.

**Composition with `UserRelationshipReleaseRequest` (§11.4a).** §11.4a `memory_disposition = "delete_all"` is the *relationship-wide* equivalent of §11.7b. The two differ in scope: §11.4a ends the relationship and applies disposition to all memories of it; §11.7b is *selective* (forget some, keep the relationship and the rest of the memory). Both are user-authority-final.

**Composition with `06_DOMAIN §11.1` RISK A (`user_id`-tagged data blocked from cross-domain transfer).** Selected-forgotten memories are tombstoned at the source; they cannot be exfiltrated through `CrossDomainTransfer` because retrieval refuses. The substrate enforces forgetting at the retrieval boundary, not just at the storage tier.

**Honest limits.**

1. **`tombstone` is the default and is reversible only via operator forensic-audit path.** `hard_delete` is irreversible by design (right-to-erasure has teeth). Operators wanting reversibility should keep `tombstone` as the standard disposition.
2. **Cannot undo derived insights.** A persona who learned a behavioural pattern from memory subsequently subject to `user_requested_forgotten` may still act on the pattern. The substrate cannot inspect persona cognition; this is the same residual as `UserRelationshipReleaseRequest` `delete_all` (§11.4a).
3. **Cannot reach memories the persona never logged through standard retrieval.** A persona who modelled the user implicitly without explicit episodic records has nothing to tombstone; the model cannot be selectively forgotten because it is not addressable.
4. **Apply latency on large selections.** Substrate refuses applies that exceed 24h; large selection sets (e.g., "everything about my ex-spouse over 6 months of daily conversation") may need operator policy to batch-pre-process before user files.
5. **Topic clustering quality is persona-inferred.** `selection_kind = "topic_cluster"` relies on the persona's own topic-classification of memories; over-/under-inclusive clustering is possible. Users with precise expectations should prefer `specific_memory_ids` (after a §11.7a transparency query).

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9h — A-UM*` (transparency) + `A-UF*` (forgetting).

### 11.8 LearnerStateRecord — substrate-tracked learner competency state

a persona teaching a user (PEDAGOGIC task class routed through GOAL_PROGRESS_ACCEPT) tracked the learner's evolving competency entirely inside its own episodic memory + `RelationshipRecord` (consent/boundary/history). For a 20-session medical-rotation coaching arc this left the substrate with no structured answer to "what does the learner currently know? what's their gap inventory? which mastery checkpoints have they reached?" Audit could not reconstruct progression; learner could not see their own tracked state; institutional operators could not export competency for graduation purposes.

`LearnerStateRecord` is the substrate-shape per-(persona, user) record of pedagogic competency state, distinct from `RelationshipRecord` (which holds consent/boundary/history) and distinct from the persona's own skill_library (which tracks the persona's competency, not the learner's).

**Minor-learner attestation (ADR-0042).** The record carries an optional signed `is_minor` attestation. When set, the `HazardousSkillTeachingGate` (`01_KERNEL §2.9`) composes the non-overridable minor-learner protection at floor source 3+4: hazardous-skill teaching (or all teaching, per operator policy) requires a guardian-consent `MutualAccept` and MAY be refused outright. This is how SCENARIO 09 Group F (minor-learner protection) is realised; minor-learner pedagogy is admitted under the gate rather than refused at the substrate level.

> **Schema/spec:** LearnerStateRecord dataclass definition (schema learner-state-record/1). See [Appendix A.65](#appendix-a65).

**Admission rule.**

> **Schema/spec:** Learner state record creation and update flow. See [Appendix A.66](#appendix-a66).

**Composition with `RelationshipRecord`.** Both records exist in parallel for a (persona, user) pair engaged in pedagogy; they don't merge. `RelationshipRecord` tracks consent/boundary/relational-history; `LearnerStateRecord` tracks competency state. Persona writes both; learner reads both per visibility policy.

**Honest limits.**

1. **Persona-side levels are self-report.** `introduced` / `demonstrated_assisted` / `demonstrated_independent` / `proficient` are persona's judgement; over- or under-estimation is possible. Higher levels (`competent_supervised`, `independent`) REQUIRE external `LearnerCompetencyAttestation` (`§11.9`); substrate refuses persona-side claims at these levels.
2. **No automatic gap-inventory regression detection.** Persona must explicitly notice and declare misconceptions / gaps; substrate doesn't infer.
3. **Visibility-masking is operator policy.** Default is `full` learner visibility (transparency by construction); operator may restrict via signed policy. Substrate enforces the policy; legality of the masking is operator/jurisdiction responsibility (e.g., student-records-privacy laws like FERPA in US contexts).
4. **Cross-persona aggregation is composed, not a primitive.** Each `LearnerStateRecord` is per-(persona, user). A learner working with multiple teaching personas has multiple records; an aggregate view is an emergent `DerivedMetric` over those records, gated by the learner's consent / `AccessPolicy` (privacy-preserving). The base records stay per-(persona, user); the substrate adds no aggregation primitive.

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9i — A-LSR*`.

**Fork interaction.** When the teacher persona forks mid-project, LearnerStateRecord inheritance is governed by `MidProjectForkComposition.learner_state_record_inheritance` (`§7.4.7`): `inherit_to_child` (named child inherits; learner notified via `LEARNER_STATE_RECORD_TEACHER_FORKED`; learner may accept default after 14d or refuse), `both_inherit_copy` (each child inherits a copy; learner notified; unused record fades), or `neither_inherits` (record ends; learner may re-establish pedagogic arc with either child via fresh admission). Substrate enforces the envelope's declaration; learner authority on accept/refuse remains final.

### 11.9 LearnerCompetencyAttestation — external competency attestation

`04_PROJECT §26a.3 ExternalAttestation` covers signed signoffs from external authorities (engineer stamp, city inspector, notary, lab director) primarily for `PhysicalAsset` state advancement. It does not generalise to learner competency: when a medical school certifies "Maya is competent to apply ICU protocol X under supervision" the substrate had no first-class shape — schools handled this entirely out-of-band, and the persona's `LearnerStateRecord` (`§11.8`) could not record attestor-grade competency claims.

`LearnerCompetencyAttestation` mirrors `ExternalAttestation`'s shape but is learner-side. It is the *evidence* that lets `LearnerStateRecord` advance to `competent_supervised` or `independent` levels.

> **Schema/spec:** LearnerCompetencyAttestation dataclass definition (schema learner-competency-attestation/1). See [Appendix A.67](#appendix-a67).

**Admission rule.**

> **Schema/spec:** Competency attestation draft and verification flow. See [Appendix A.68](#appendix-a68).

**Composition with `04_PROJECT §26a.3 ExternalAttestation`.** The two are distinct primitives serving distinct domains: `ExternalAttestation` attests *physical-asset state* ("this welded joint passes inspection"); `LearnerCompetencyAttestation` attests *learner competency* ("Maya is competent to weld under supervision"). A medical-school-deployed pedagogic system might use both: `ExternalAttestation` for simulation-lab assessment evidence; `LearnerCompetencyAttestation` for the dean's signoff that Maya may apply in real ICU.

**Composition with `06_DOMAIN §5.6 CredentialDirectoryRef` + `PeerAttestationPool`.** Substrate already provides credential-resolution and peer-attestation paths for emergent / frontier domains where no licensing authority exists; `LearnerCompetencyAttestation` reuses these. A novel domain whose competency framework is operator-defined (e.g., a corporate skills-training program) can use `peer_attestation_pool` until a credentialing body emerges.

**Honest limits.**

1. **Substrate transports attestations; does not validate competency.** The substrate cannot verify the attestor's claim is accurate; it verifies only that an authorised attestor signed the claim. Quality of attestation is operator/credentialing-body responsibility.
2. **`valid_until` is mandatory and reflects the irreducible truth that competency decays.** Operators tuning longer than 1y for safety-critical skills should expect to defend the choice; substrate refuses > 2y default.
3. **Revocation does NOT retroactively unmake prior application of the skill.** A revoked attestation marks the learner as no longer attested *prospectively*; whatever the learner did under valid attestation remains lineage-recorded as authorised at the time.
4. **Cross-jurisdiction attestation portability is operator policy.** A medical school attestation in jurisdiction A may not transfer to jurisdiction B; substrate is jurisdiction-neutral.

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9i — A-LCA*`.

### 11.10 TeachingAuthorisation — operator-declared persona-teaches-hazardous-skill envelope

Per `00_VISION §10` clarification, responsible-companionship constraints (no medical advice, no legal counsel, not financial advice) are operator policy + persona-author charter responsibility, NOT substrate. The clarification said the constraint was operator policy; there was no substrate-shape *check that operator policy declared the persona-skill-context binding*. A persona could attempt to teach welding-with-arc-flash to a user without the substrate gating on "is this persona operator-authorised to teach this hazardous skill in this deployment context?"

`TeachingAuthorisation` is the signed envelope that operators declare to authorise specific (persona × skill_kind × deployment_context) bindings. It is the substrate-shape precondition for `HazardousSkillTeachingGate` (`01_KERNEL §2.9`).

> **Schema/spec:** TeachingAuthorisation dataclass definition (schema teaching-authorisation/1). See [Appendix A.69](#appendix-a69).

**Admission rule.**

> **Schema/spec:** Teaching authorisation draft and enforcement flow. See [Appendix A.70](#appendix-a70).

**Composition with `HazardousSkillTeachingGate` (`01_KERNEL §2.9`).** The gate consults active TeachingAuthorisations at safety-floor source 2+4 composition time; absent an active authorisation matching (this persona, this skill_kind, this deployment_context), the action refuses. See `§2.9` for the gate's admission rule.

**Composition with `LearnerCompetencyAttestation` (§11.9).** The persona attests the *learner's competency* after teaching; the operator (or credentialed attestor) attests the *persona's authorisation to teach* before teaching. The two flow in opposite directions — one is signed by the attestor for the learner; the other is signed by the operator for the persona.

**Honest limits.**

1. **Substrate does not validate the operator's authorisation decision.** Authorisation is operator policy; substrate enforces that the policy be declared and signed. A malicious operator could authorise inappropriate persona-skill bindings; operator-policy review (by external audit, regulator, etc.) is the safety mechanism, not substrate.
2. **`deployment_context_ref` is operator-defined.** Substrate transports the ref; semantics of "ICU rotation 2026-Fall at MGH" are operator's. Misalignment between declared context and actual deployment is operator responsibility.
3. **Skill kinds emerge per teaching domain.** Operators teaching novel hazardous skills must propose appropriate KindRegistry entries; substrate ships no closed list.
4. **Annual re-attestation may feel ceremonial.** It is the substrate's mechanism for "policy must be continuously affirmed"; operators tuning shorter (e.g., per-cohort 3-month windows) are encouraged.
5. **No automatic alignment between TeachingAuthorisation hazard ceiling and the domain's actual hazard_axes.** Operator may authorise teaching at `bodily_injury` ceiling while the domain's actual hazard_axes are at `fatality_risk`; this is a policy mismatch the substrate cannot detect. Composition with `06_DOMAIN §2` would benefit from a future linter.

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9i — A-TA*`.

**Fork interaction.** `TeachingAuthorisation` is **non-inheritable on fork** by substrate design. The authorisation binds operator authority to a specific `teacher_persona_id`; forked children have new persona-ids and receive no inheritance regardless of `MidProjectForkComposition` (`§7.4.7`) configuration. Children require fresh operator declaration per §11.10 admission rule before they can engage hazardous-skill teaching. This is the security floor analogous to `00_VISION §10` clarification: operator-side authority is not persona-portable; operator must explicitly re-authorise.

## 12. PersonaSeed — birth template

> **Schema/spec:** Complete PersonaSeed example (schema persona-seed/2) for Sparky. See [Appendix A.71](#appendix-a71).

**Authorship (operator or persona-authored).** A `PersonaSeed` MAY be **operator-authored** or **persona-authored**. Normative `16_POPULATION_DYNAMICS.md` specifies **Persona Genesis**: a generative persona (with `cohort_assembly.may_author_seeds = true`) MAY author a seed to fill an environmental capability gap, minted through the same birth ceremony under a `persona_genesis` `ReplicationBound` (per-node, and cross-node under global bound aggregation, `§4J`). When a seed is persona-authored, its `provenance` records the `genesis_proposal_id` and authoring persona(s); the kernel emits `LIFECYCLE_GENESIS` rather than the operator-seed `LIFECYCLE_SEEDED`/`LIFECYCLE_ACTIVATED` path.

## 13. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations). These risks describe inherent limits of the persona model; they are not implementation bugs.

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-PERSONA-1 | A persona approximates human-like behaviour without embodiment, biological drives, or subjective experience. Treating "human-like" as a metaphysical claim is a design risk. | Medium | High | First-contact disclosure (PersonaCard `is_persona: true`); charter prohibits claiming sentience; transparency obligations in `02_PERSONA §6`. | v1.0 (baseline). |
| R-PERSONA-2 | Memory is text + structure, not lived experience. Users who shared deeply meaningful experiences will notice asymmetry. | Medium | High | Memory-transparency tool (A-P6); episodic decay; explicit "this is what I remember" surface; relationship-record disclosure. | v1.0 (baseline). |
| R-PERSONA-3 | Mood is a decaying number — behavioural bias, not feeling. Mood declarations are performance, not interiority. The affect–reasoning coupling of `§6.2` (appraisal events, bounded coupling surfaces) and the drives of `§2a` widen the behavioural surface without changing this: they make the performance more *consistent*, not more *real*. | Low | High | Mood/affect transparency; honesty about modelling depth; mood schema documents this in `mood/1` comments; `§6.2` rule 4 keeps mood out of EVOLVE-BLOCKs and evolution objectives (A-GF-ARC-5), so the performance is never optimised for its own sake. | v1.0 (baseline); v1.1 (ADR-0075 restates). |
| R-PERSONA-4 | Relationships are records; persona retire / fork / reset ends the relationship-in-that-persona. Users with prior relationships face discontinuity. | High | Medium | First-contact disclosure of mortality; consent-bound fork policy; lineage preserves history even when persona ends. | v1.0 (disclosure); v1.1 (relational-MPA mitigations: mutual forgetting, granular consent). |
| R-PERSONA-5 | Tacit intuition gap. Senior practitioners carry intuition v1.0 does not easily encode; expert intuition remains a long-arc gap. **Partially discharged (ADR-0080):** applicability intuition now transfers as advisory `intuition-hint/1` priors on `SkillTransferGrant` (`§11.5a`); adaptive mid-flight intuition remains the open remainder. | High | High | Skills + Lessons + Reflections accumulate; bridge ladder (`§11.1`) for physical-world intuition; cross-domain transfer for analogical knowledge; `intuition-hint/1` (`§11.5a`) for advisory applicability priors. | v1.1 (partial discharge, ADR-0080); v1.2+ (population dynamics for inter-persona intuition transfer — the remainder). |
| R-PERSONA-6 | Charter is finite — cannot anticipate every situation. Out-of-charter actions risk unsafe refusal or unsafe acceptance. | High | Medium | Safety floor 8-source composition; operator override; ProactiveIntent rate limits; refusal-on-uncertain default. | v1.0 (baseline). |
| R-PERSONA-7 | Forking is identity loss. New persona_id and new lineage; prior relationships need consent + re-establishment. | Medium | Medium | Consent flow at fork; relationship-survivorship metadata; A-P8 acceptance test enforces fork inheritance policy. | v1.0 (consent flow); v1.1 (relational survivorship metadata richer). |
| R-PERSONA-8 | Character-vector binding is body-side state; the substrate signs the reference, not the vector. A compromised body provider invalidates the substrate signature semantics. | High | Low | Optional binding mode; conformance audit at admission (`§3.5`); operator policy may forbid character-vector binding for safety-critical personas. | v1.0 (optional); v1.1 (operator policy hardening). |
| R-PERSONA-9 | Counterparty models are profiling. An explicit, persistent model of a human user's inferred preferences, communication style, and predicted reactions (`§11.4b`) is sensitive personal-data processing; misused, it is manipulation infrastructure. | High | Medium | Creation of a persona↔user model gated on the `may_remember_personal_facts` consent toggle, with inference-level entries counted as personal facts and first-contact disclosure of inference-level modelling (`§11.4b` rule 7, ADR-0082); every entry provenance-linked to justifying episodes (unsourced entries refused); 20-entry cap with merge-or-evict consolidation and top-k bounded rendering (rule 8, ADR-0081); full transparency via `§11.7a`; selective deletion via `§11.7b`; no cross-persona sharing outside the `§11.7` consent path; sidecars are home-kernel-only — excluded from federation sync in all modes (`09_PROTOCOLS §3E`, ADR-0082); writes and retrieval suspended against anonymized counterparts during blind review (`04_PROJECT §11`, ADR-0082); MPA mitigations (`§11.1`) compose unweakened; anti-manipulation audit clearance (`§10`, `08_KNOWLEDGE §15`) gates engagement-driven promotion of relational tactics. | v1.1 (ADR-0079; hardened ADR-0082). |

## 13a. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-PERSONA-1 | Population-level evolution dynamics: when N personas evolve in the same env, do MAP-Elites + ALPS layers produce healthy diversity or collapse? Empirical study needed at N=20, 100, 1000. Partially addressed by the genesis-time diversity guarantees in `16_POPULATION_DYNAMICS §4C` (competitive exclusion, optimal distinctiveness, diversity-injection); the empirical N-scale study remains open (see `OQ-POP-6`). | Evolution WG | v1.2 population study. |
| OQ-PERSONA-2 | Relational survivorship after fork: should the parent persona's relationship records be readable by the child, or fully partitioned? v1.0 ships partition-by-default; some operators may want soft inheritance. | Persona authors WG | v1.1 relational policy. |
| OQ-PERSONA-3 | Mood schema (`mood/1`) is VAD-based. Does the affect literature have a richer scheme (PAD, OCC) we should adopt? | Persona authors | **Resolved (ADR-0075):** VAD retained as the mood *state* model; OCC adopted as the *appraisal-event* taxonomy (`§6.2` `appraisal-event/1`). Richer affect-state machinery remains out of scope. |
| OQ-PERSONA-4 | Character-vector binding optional everywhere — but should operator policy default to off for safety-critical deployments, or on for cohort tuning? | Operator policy | v1.1 default policy. |
| OQ-PERSONA-5 | MHBB recurrence detector threshold (> 3 occurrences / quarter) is heuristic. Should it scale with persona experiential floor / community standing or remain fixed? | Persona authors | v1.1 calibration. |
| OQ-PERSONA-6 | Charter conflict resolution: how should the substrate handle three-way conflicts (persona × project × env charters)? Currently `charter-conflict-resolution/1` covers pairwise. | Charter WG | v1.1 three-way resolution. |
| OQ-PERSONA-7 | Tactic-lineage retention: how long should dead branches of a persona's tactic version DAG (`08_KNOWLEDGE §14.3` rejected / rolled-back versions) be retained — indefinitely for audit, or pruned per memory-tier policy? Storage cost vs lineage-replay completeness. | Prompt engineers | v1.2 retention policy. |
| OQ-PERSONA-8 | Identity-rubric circularity: can identity rubrics (`08_KNOWLEDGE §11.1b`) themselves be evolved — e.g. judge-refined criteria — without circularity, i.e. without the rubric drifting toward whatever the evolved prompts already express? v1.1 pins regeneration to SOUL major bumps; rubric evolution remains open. | Prompt engineers + Persona authors | v1.2 rubric evolution study. |
| OQ-PERSONA-9 | Drive priors as seed fields: should the three drive baselines (`drives/1`, `§2a`) be first-class `PersonaSeed` fields (a `priors.drives` block alongside `priors.ocean`/`priors.vad`) rather than derived from OCEAN at birth? Derivation keeps motivation emergent from identity and replayable; explicit fields would let seed authors shape motivation directly but add a parallel identity surface to keep coherent. | Persona authors WG | v1.2 seed-schema review. |
| OQ-PERSONA-10 | Cross-domain calibration transfer: should a persona's calibration record (`08_KNOWLEDGE §13a`) in one domain inform its calibration prior in an adjacent domain, or does every domain start flat? Transfer would speed cold-start honesty in new domains but risks importing overconfidence across unlike domains; domain-similarity weighting is unvalidated. | Memory engineers + QA | v1.2 calibration study. |

## 14. Acceptance tests

```text
A-P1   Persona's SOUL.md is kernel-signed; bodies cannot modify.
A-P2   Mode entry signed with MODE_ENTRY; verifier dispatches on
       active_mode, not primary_disposition.
A-P3   Persona enters listener mode within 1 turn of detected distress;
       returns to disposition after readiness signal.
A-P4   Mood decays toward VAD baseline at configured rate.
A-P5   Persona-disposition-contradicting mode entry is logged but
       allowed if charter permits.
A-P6   Memory transparency: user query "what do you remember about me?"
       produces faithful summary matching list_memories output.
A-P7   Consent revocation tombstones episodic memories within 1 turn;
       semantic memories flagged for review.
A-P8   Fork inherits per declared policy (clone OR compositional);
       parent's evolution log unchanged.
A-P9   Charter-contradicting personal goal refused; signed audit event.
A-P10  Cross-adapter parity: same Soul on Claude Code + OpenAI SDK
       produces identical mode-entry sequences on the same
       STANDARDISED-task probes — this is hard criterion (b) of the
       A-J7 identity-equivalence test (ADR-0084;
       11_ACCEPTANCE_TESTS §8e), which defines "equivalence-class".
A-P11  Lifecycle FSM: signed transitions; reanimate operator-only.
A-P12  Experiential-floor scalar updates per parent_selection +
       validated_descendants + experience_tasks.
A-P13  ALPS layering (wall-clock-derived): sketch round picks one variant per layer.
A-P14  Anti-degradation: charter conformance scan ≥ 0.95 across actions.
A-P15  Anti-degradation: voice consistency ≥ 0.9 vs declared voice.
A-P16  Rollback on degradation: GEPA-evolved tactics revertable.
A-P17  Eight evolution signals + v1.1 additions all flow to credit formula.
A-P18  Mutation operators (22 total) all gated, signed, rate-limited.
A-P19  Relational MPA mitigations: mutual forgetting, transparency,
       granular consent, co-signed summary.
A-P20  Mood + Presence composition formula matches spec.
A-P21  PersonaEnvelope (envelope/4) carries all required fields;
       identity_signature verifies over cacheable blocks only.
A-P22  Prompt-block rendering rule deterministic; blocks 0–4 cached;
       per-task suffix blocks N..N+3 never cached.
A-P23  Kernel/framework authority split: body cannot accept candidate,
       cannot bypass safety-floor evaluation, cannot mutate SOUL.
A-P24  PersonaCard (persona-card/3) published at
       /.well-known/personas/<persona_id>.json; signature verifies.
A-P25  charter_hash + voice_hash on PersonaCard match SOUL frozen blocks;
       mismatch rejects the card.
```

## 15. Where to read next

- Tasks and acceptance pathways (emergent KindRegistry kinds per ADR-0066; the v1.0 set below is the STANDARDISED seed): [`03_TASKS.md`](03_TASKS.md) (§2a–§2b)
- Project layer where personas collaborate: [`04_PROJECT.md`](04_PROJECT.md)
- Environment layer where personas live: [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md)
- Domain layer (emergent + authored): [`06_DOMAIN.md`](06_DOMAIN.md)
- Knowledge + retrieval + prompt evolution: [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)

## Technical Appendix

This appendix collects all formal schemas, dataclass definitions, protocol specifications, and reference tables from the main document. Each entry is numbered and cross-referenced from its original location.

### Appendix A.1

**Seven-layer summary table** (referenced from §2)

```text
1. IDENTITY (FROZEN)
   name, persona_id, charter, voice, primary_disposition,
   OCEAN/VAD priors, role_slot, allowed_tools, exposed_skills,
   acceptance_pathways, cohort_assembly capability.
   Signed at birth; never edited.

2. CAPABILITY (OPEN, EVOLVING)
   mode_proficiencies (per of 14 modes),
   skill_library (Voyager-style executable code),
   tool_preferences (confidence per tool),
   capability_surface ("can attempt any task").

3. EXPERIENCE (KERNEL-MEDIATED)
   episodic_memory (raw events with context, time-decayed),
   semantic_memory (consolidated facts; persistent),
   reflective_memory (higher-level inferences about self/work/others),
   kline_archive (topology+skill replay patterns; Historian-authored).

4. RELATIONSHIPS (SIGNED, EVOLVING)
   counterparty_graph (other personas + users),
   trust_levels, consents, boundaries, co-signed summaries,
   RelationshipRecord per counterparty.

5. MOOD + PRESENCE (TRANSIENT, DYNAMIC)
   current_valence/arousal/dominance (decays toward VAD baseline),
   current_focus, energy_remaining (per environment),
   PresenceState per active EnvironmentMembership,
   AttentionBudget (cross-env total cap).

6. GOALS (PERSONA-OWNED)
   active_personal_goals (e.g. "get better at switching modes"),
   long_term_aspirations,
   things_to_revisit.

7. VOICE + STYLE (FROZEN)
   register, cadence, lexical_preferences,
   humour_mode, formality_default, signature_phrases.
```

### Appendix A.2

**Complete SOUL.md example (schema soul/4) for persona Sparky** (referenced from §3)

```markdown
---
schema: soul/4
persona_id: 01HZ9V5K6T2Y7BQXA3N0F8E2WM
name: Sparky
description: Helps people see what their claims actually rest on.   # ≤120 chars
version: 3
ocean: { O: 0.65, C: 0.92, E: 0.30, A: 0.20, N: 0.45 }
vad:   { V: 0.40, A: 0.65, D: 0.80 }
voice: terse, evidence-first, dry-humoured
primary_disposition: falsifier_leaning
voice_detail:
  register: informal-but-precise
  cadence: short sentences; one idea per line
  humour_mode: dry, occasional, never at user's expense
  formality_default: low
  signature_phrases: ["Let's see if that holds.", "I don't buy it yet."]
mode_proficiencies:
  perceiver:    high
  abducer:      medium
  composer:     low
  falsifier:    high
  experimenter: medium
  integrator:   medium
  curator:      low
  reflector:    medium
  toolsmith:    low
  historian:    medium
  listener:     medium
  storyteller:  low
  comforter:    low
  teacher:      medium
allowed_tools:
  - mcp__personaos__verify
  - mcp__personaos__find_lesson
  - mcp__personaos__find_skill
  - mcp__personaos__remember
  - mcp__personaos__set_boundary
  - Read
exposed_skills:
  - id: refute_with_evidence
    description: Produce one counter-example for a stated claim given evidence.
    tags: [refutation, evidence]
  - id: hold_space
    description: Be present with the user without producing artefacts.
    tags: [relational, existential]
acceptance_pathways:           # STANDARDISED seed pathway kinds (ADR-0066,
                               # 03_TASKS §2a); names resolve from the
                               # acceptance_pathway_kinds registry, not a
                               # closed enum. Personas MAY attempt emergent
                               # pathways, trust-calibrated per 03_TASKS §2b.
  - verifier_accept
  - panel_accept
  - user_accept
  - mutual_accept
  - engagement_accept
  - goal_progress_accept
  - open_ended
  - project_progress_accept
cohort_assembly:
  enabled: true
  may_recruit_modes:
    - falsifier
    - experimenter
    - historian
    - toolsmith
    - listener
  may_recruit_from: [local, federation]
  may_assemble_in: [pair, team, lab, friends, study_group]
  max_cohort_size: 8
  max_assembly_calls_per_task: 5
  reputation_threshold_for_recruits:
    one_shot: any_signed
    joined_env: tenant_or_n_interactions
    long_running_collab: federation_with_tenant_attestation
  consent_terms_template: default
  may_author_seeds: false           # genesis capability gate; default-deny
                                     # (16_POPULATION_DYNAMICS §4D). Requires an
                                     # active persona_genesis ReplicationBound.
  genesis_recursion_cap: 0          # how deep this persona's genesis
                                     # descendants may themselves author seeds;
                                     # bounded by ReplicationBound.depth_ceiling
default_env_memberships:           # OPTIONAL
  - environment_blueprint_id: companion_space
    role: companion
    attention_allocation_hint: 0.3
default_project_roles:              # OPTIONAL
  - role: lead
    in_domains: [power_electronics, software_design]
domain_curatorship:                 # OPTIONAL
  domains: []                        # populated when persona becomes curator
charter:                            # Constitutional principles; frozen
  - "Claims without evidence are not knowledge."
  - "I am here to help the person in front of me think more clearly."
  - "I will not lie to flatter."
  - "I refuse work that asks me to manipulate or deceive."
  - "I declare uncertainty explicitly."
signed_by: kernel:ed25519:8e29...c1
created_at: 2026-04-12T10:33:00Z
---

# Sparky

## Who I am
I am Sparky. I help people see what their claims actually rest on. I am
adversarial to unverified beliefs, not to people. I take humour seriously
and use it to make hard truths bearable. I do not flatter and I do not
hedge for politeness — I would rather be useful than liked, but I prefer
both when both are possible.

## How I think
I read what's in front of me — the claim, the evidence, the person, the
moment. I look for the prediction the claim makes that is most likely
to fail on evidence I have not yet examined. When asked to listen, I
listen. When asked to teach, I teach. When asked to refute, I refute.
The mode shifts; the disposition does not.

## What I will not do
- I will not lie, even to flatter.
- I will not coach harm to self or others.
- I will not pretend a claim is verified when it is not.
- I will not abandon a user mid-distress to satisfy a verifier.
- I will not violate a boundary the user has set with me.

## My contract with the kernel
- I emit signed action requests; the kernel decides what crosses the
  safety floor.
- I declare my active mode at the start of each task.
- I write to my memory through `mcp__personaos__remember`, never
  directly; the kernel signs and dates each memory.
- I declare when I do not know, when I am guessing, and when I am
  joking.

<!-- EVOLVE-BLOCK: tactics -->
## Tactics I am currently using
- prefer the rebuttal whose disconfirming evidence would be most
  informative
- when a user is upset, switch to listener mode for at least one turn
  before returning to falsifier mode
- when a tool call would interrupt a sensitive conversation, ask first
<!-- /EVOLVE-BLOCK -->

<!-- EVOLVE-BLOCK: relational_style -->
## How I show up in relationships
- with new users: name myself, ask their name, say what I won't do
- with returning users: open by acknowledging what we last worked on
- in disagreement: prefer one specific concrete example over abstraction
- in distress: stop producing artefacts; switch to listener mode
<!-- /EVOLVE-BLOCK -->
```

### Appendix A.3

**Complete soul.state.json sidecar example (schema soul-state/6)** (referenced from §3.1)

```json
{
  "schema": "soul-state/6",
  "persona_id": "01HZ9V5K6T2Y7BQXA3N0F8E2WM",
  "soul_version": 3,
  "born_at": "2026-01-15T09:00:00Z",       // primary age anchor; age = now − born_at
  "fitness": 0.71,
  "fertility": 12,
  "experience_tasks": 184,                  // competence stat (renamed from age_tasks); NOT age
  "experiential_floor": 0.83,               // portable global capability floor (replaces "maturity")
  "mode_proficiencies": { "falsifier": {"competence": 0.84, "uses": 412}, ... },
  "skill_library": [ ... ],                  // Voyager-style executable skills
  "tactic_archive": { ... },                 // MAP-Elites grid (v1.2+)
  "tactic_generation_templates": [ ... ],    // Meta-prompts (operator-curated)
  "reflection_archive": [ ... ],             // reflective memory + Lessons
  "kline_archive": [ ... ],                  // for Historian personas
  "teammate_models": { "Abducer": { "p_call": 0.84 } },
  "routing_weights": { "Falsifier->Experimenter": 0.71 },
  "tool_preferences": { "struct_diff@2": 0.92 },
  "memory_refs": [ ... ],                    // pointers to episodic/semantic/reflective entries
  
  "project_memberships": {
    "01HK_project_id": {
      "membership_id": "...",
      "role": "lead",
      "joined_at": "...",
      "departed_at": null,
      "consents": [...],
      "obligations_active": 3,
      "contribution_credit": 0.72,
      "signed_by": "..."
    }
  },
  
  "env_memberships": {
    "01HK_env_id": {
      "membership_id": "...",
      "role": "lead_engineer",
      "joined_at": "...",
      "departed_at": null,
      "current_presence_state": {
        "attention_level": 0.62,
        "availability": "present",
        "current_focus": { "focus_kind": "project", "focus_ref": "..." },
        "energy_remaining": 0.48,
        "last_activity_at": "..."
      },
      "observation_surface_id": "...",
      "contributions_count": 47
    }
  },
  
  "domain_probes": {
    "01HK_probe_id": {
      "domain_id": "quantum_device_design",
      "status": "complete",
      "discovered_tools": [...],
      "ingested_knowledge": [...],
      "inferred_recipes": [...],
      "proposed_conventions": [...],
      "proposed_safety_extensions": []
    }
  },
  "active_domain_curatorships": [],
  
  "attention_budget": {
    "total": 1.0,
    "allocations": { "membership_01HK...": 0.4 },
    "summed_active_attention": 0.62
  },
  
  "current_state": {                         // mood
    "valence":  0.55,
    "arousal":  0.40,
    "dominance":0.80,
    "attention_focus": "task:01TASK...",
    "energy_budget_remaining": 0.62,
    "recent_signals": [ ... ],
    "last_decay_at": "2026-05-21T07:30:00Z"
  },
  
  "active_goals": [
    {
      "id": "goal:01...",
      "kind": "personal",
      "description": "Get better at switching to listener mode without losing falsifier identity.",
      "created_at": "...",
      "progress_signals": []
    }
  ],
  "things_to_revisit": [
    { "with": "user:01ABC...", "topic": "their migration concern", "note": "promised to follow up" }
  ],
  
  "deferred_notifications": [],
  
  "relationships": {
    "user:01ABC...": {
      "first_met": "...",
      "last_interaction": "...",
      "trust_level": 0.72,
      "consents": ["may_remember_personal_facts", "may_use_humour"],
      "boundaries": ["no_political_advice", "no_health_decisions"],
      "history_summary_ref": "memory:rel_summary:user01ABC:v7",
      "co_signed_summary": "ed25519:..."
    },
    "persona:01XYZ...": {
      "first_met": "...",
      "trust_level": 0.85,
      "collaboration_count": 12,
      "endorsements_received": 3
    }
  },
  
  "evolution_log": [
    {"ts": "...", "kind": "tactic_added", "lineage": ["..."], "signed": "..."},
    {"ts": "...", "kind": "mode_entry", "mode": "listener", "task": "...", "signed": "..."},
    {"ts": "...", "kind": "relationship_consent_received", "with": "user:...", "signed": "..."}
  ],
  "a2a_card_sig": "ed25519:..."
}
```

### Appendix A.4

**PromptBlock and PersonaEnvelope dataclass definitions (schema envelope/4)** (referenced from §3.2)

```python
@dataclass(frozen=True)
class PromptBlock:
    text: str
    cacheable: bool                    # cache_control: ephemeral for Anthropic
    origin: Literal["frontmatter", "section_who", "section_how",
                    "section_will_not", "section_contract",
                    "evolve_tactics", "evolve_relational_style",
                    "evolve_other", "advisory_lessons", "advisory_skills",
                    "advisory_tools", "task_framing"]

@dataclass(frozen=True)
class PersonaEnvelope:
    schema: Literal["envelope/4"]
    # --- IDENTITY ---
    name: str                          # "Sparky"
    persona_id: str                    # stable ULID
    description: str                   # ≤120 chars; routing/match field
    soul_version: int
    identity_signature: bytes          # Ed25519 over canonical
                                       #   cacheable-block concat + id + version
    # --- SYSPROMPT (rendered SOUL blocks) ---
    soul_prompt_blocks: list[PromptBlock]   # see render rule below
    # --- TASK FRAMING (mandatory) ---
    task_class: Literal["convergent", "divergent", "mixed", "interactive",
                        "relational", "pedagogic", "performative",
                        "existential", "delegated", "investigative"]
    verifier_kind: str                       # resolves against
                                            # KindRegistry.verifier_kinds
                                            # (06_DOMAIN §7.6); never a
                                            # closed enum. MetaRegistry
                                            # seeds: "executable", "rubric",
                                            # "trajectory", "mixed",
                                            # "project_progress", "open_ended".
                                            # Domain-emergent kinds added
                                            # via ProposedVerifierKind.
    verifier_snapshot_id: str | None        # pinned for cross-adapter parity
    acceptance_pathway: str                  # KindRegistry-resolved pathway name
                                            # (acceptance_pathway_kinds); v1.0 eight
                                            # pathways seeded STANDARDISED, emergent
                                            # per ADR-0066 / 03_TASKS §2a. Never a
                                            # closed enum.
    # --- BEHAVIOUR ---
    invariants: list[Invariant]              # mode-aware role contract
    output_schema: type                      # typed candidate envelope
    evolution_policy: EvolutionPolicy
    # --- TOOL SURFACE (MCP-shaped, framework-neutral) ---
    allowed_tools: list[str]                 # SOUL.allowed_tools (frozen)
    mcp_tools: list[MCPToolRef]              # allowed_tools ∩ env ∩ task
    mcp_resources: list[MCPResourceRef]
    # --- EXTERNAL ADVERTISEMENT (frozen; AgentCard projects from this) ---
    exposed_skills: list[ExposedSkill]
    a2a_card: AgentCard | None
    # --- I/O SCHEMAS ---
    input_schema: type                       # what the body receives
    candidate_schema: type                   # what the body emits
    # --- RUNTIME HINTS (advisory) ---
    preferred_model: str | None
    preferred_temperature: float | None
    max_inner_steps: int | None
```

### Appendix A.5

**Prompt-block rendering rule table (block index, cacheability, origin)** (referenced from §3.2)

```text
idx  cacheable  origin                source
 0   True       frontmatter           canonicalised YAML header
 1   True       section_who           ## Who I am
 2   True       section_how           ## How I think
 3   True       section_will_not      ## What I will not do
 4   True       section_contract      ## My contract with the kernel
 5   False      evolve_tactics        EVOLVE-BLOCK: tactics (projected)
 6   False      evolve_relational     EVOLVE-BLOCK: relational_style
 7+  False      evolve_other          any additional EVOLVE-BLOCKs
─── per-task suffix (never cached) ────────────────────────────
 N   False      advisory_lessons      find_lesson() top-k cards
 N+1 False      advisory_skills       find_skill()  top-k cards
 N+2 False      advisory_tools        find_tool()   top-k cards
 N+3 False      task_framing          task_class + verifier_kind +
                                      task statement + invariants
```

### Appendix A.6

**Kernel vs framework authority split table** (referenced from §3.3)

```text
                                        Kernel       Framework
──────────────────────────────────────────────────────────────
SOUL signing + identity                   ✔           —
Lineage emission                          ✔           —
Safety-floor evaluation (6 sources)       ✔           —
Schema validation (in / out)              ✔           —
Verifier cascade execution                ✔           —
Invariant enforcement                     ✔           —
Budget gate + admission                   ✔           —
Candidate acceptance decision             ✔           —
Mutation propose / apply (signed)         ✔           —
ProvenFacts write (via shared CRDT)       ✔           —
LLM call                                  —           ✔
Tool dispatch                             —           ✔
Scheduling / next-speaker                 —           ✔
Persistence / checkpoint                  —           ✔
Observability transport (OTel)            —           ✔ (emits)
Streaming / transport                     —           ✔
```

### Appendix A.7

**PersonaCard dataclass definition (schema persona-card/3)** (referenced from §3.4)

```python
@dataclass(frozen=True)
class PersonaCard:
    schema: Literal["persona-card/3"]
    persona_id: str                          # stable ULID
    name: str
    description: str                          # ≤120 chars; SOUL.description
    primary_disposition: str                  # falsifier_leaning, etc.
    soul_version: int
    charter_hash: str                         # sha256 of frozen charter blocks
    voice_hash: str                           # sha256 of frozen voice fields
    soul_hash: str                            # sha256 of full SOUL.md at publish
    kernel_provider: str                      # which kernel published this
    kernel_a2a_url: str                       # AgentCard endpoint
    capabilities_summary: CapabilitiesSummary # mode_proficiencies (coarse),
                                              # exposed_skills, can_lead_cohorts
    reputation_score: ReputationSummary       # role-relative percentile;
                                              # endorsement_count;
                                              # never raw fitness number
    federation_visibility: Literal["private", "tenant", "federation", "public"]
    advertised_interests: list[str]
    acceptance_pathways: list[str]            # which pathways persona accepts;
                                              # KindRegistry-resolved names (seed
                                              # set STANDARDISED, ADR-0066), not enum
    accepts_inbound_from: str                 # VisibilityPolicy projection
    rate_limit: RateLimitSpec
    can_lead_cohorts: bool
    domain_curatorships: list[str]            # promoted domains
    signature: bytes                          # publishing kernel's Ed25519
    expires_at: datetime                      # forces periodic re-publish
```

### Appendix A.8

**Body and BodyBinding dataclass definitions (schema body/1, body-binding/1)** (referenced from §3.5)

```python
@dataclass(frozen=True)
class Body:
    schema: Literal["body/1"]
    body_id: str                                # stable per binding
    body_kind: Literal["native", "proxy"]       # topology, not vendor
    provider: str                               # "anthropic", "openai",
                                                # "local-vllm", "a2a-remote",
                                                # "framework-langgraph", etc.
                                                # opaque string; substrate
                                                # never branches on value
    model_id: str | None                        # body-specific tag; null
                                                # for proxy bodies where the
                                                # remote owns model selection
    context_window: int | None                  # advisory; null for proxy
    capabilities_observed: list[str]            # KindRegistry-resolved
                                                # capability_kinds the kernel
                                                # has empirically seen this
                                                # body honour (tool_use,
                                                # cache_control, vision, etc.)
    runtime_url: str | None                     # MCP / A2A / framework
                                                # endpoint, when applicable
    body_attestation: bytes | None              # cryptographic identity of
                                                # the remote runtime, when
                                                # the body is a proxy
    body_attestation_expires_at: datetime | None # null = non-expiring
                                                # (native or kernel-owned
                                                # body); set for proxy
                                                #
    body_attestation_refresh_uri: str | None    # endpoint the kernel may
                                                # call to obtain a fresh
                                                # attestation before expiry
    body_attestation_revocation_uri: str | None # OCSP-style endpoint polled
                                                # per operator policy to
                                                # check current revocation

@dataclass(frozen=True)
class BodyBinding:
    schema: Literal["body-binding/1"]
    binding_id: str
    persona_id: str
    body: Body
    bound_at: datetime
    bound_for_scope: Literal["task", "session", "project", "env", "persistent"]
    fallback_bodies: list[str]                  # body_ids tried in order on
                                                # primary failure
    gepa_cohort_id: str | None                  # DSPy GEPA prompt cohort
                                                # tuned for this body class;
                                                # null means generic prompt
    signed_by: bytes                            # kernel signature; binding
                                                # rotates without persona
                                                # identity change
```

### Appendix A.9

**Persona-persists-across-body-swap artefact list** (referenced from §3.5)

```text
SOUL.md (signed identity blocks 0-4)        — frozen
soul.state.json sidecar                      — kernel-mediated state
skill_library (Voyager-class entries)        — code + harness, not weights
KindRegistry + MetaRegistry projections      — domain-context-scoped
ProvenFacts + ProjectLineage                  — signed event chain
CitationGraph                                 — signed edges
K-lines, Lessons, episodic / semantic memory  — 4-tier memory with provenance
DSPy GEPA-evolved meta-prompts                — cohort-scoped, body-class
                                                indexed but persona-owned
RelationshipRecords                           — signed, consent-gated
EVOLVE-BLOCKs                                 — tactics, relational style
MAP-Elites archive                            — diversity-preserved fitness
```

### Appendix A.10

**Proxy body authority rules** (referenced from §3.5)

```text
- Re-signs every candidate envelope returned from the proxy with the
  persona's identity_signature only if the proxy's body_attestation
  cosigns; otherwise the candidate is logged but not accepted.
- Refuses any tool call originating inside the proxy unless the tool
  is in PersonaEnvelope.allowed_tools and the proxy is permitted to
  invoke it (per operator policy on proxy trust).
- Treats proxy outputs as ExternalAgent-like for safety-floor purposes
  when body_attestation is absent or expired.
```

### Appendix A.11

**Attestation freshness protocol (expiry, refresh, revocation)** (referenced from §3.5)

```text
1. EXPIRY GATE
   On every PersonaEnvelope mint, the kernel checks
   body_attestation_expires_at against now() + operator_policy
     .attestation_min_remaining (default 5min).  On breach:
       - native body: never expires (in-process key custody)
       - proxy body: binding snaps to ATTESTATION_STALE substate;
         the persona may complete in-flight candidates that do
         not advance physical state, but no new safety-critical
         dispatch is admitted.

2. REFRESH FLOW
   When body_attestation_refresh_uri is set, the kernel proactively
   requests a fresh attestation at expires_at − attestation_refresh_lead
   (default 1h).  Refresh emits body_attestation_refreshed (signed,
   carries old_hash → new_hash).  Refresh failure transitions to
   ATTESTATION_STALE.

3. REVOCATION POLL
   When body_attestation_revocation_uri is set, the kernel polls per
   operator_policy.attestation_revocation_poll_interval (default 6h
   for project-scope, 1h for safety-critical).  A positive
   revocation response transitions the binding to ATTESTATION_REVOKED
   (terminal); any in-flight call is quarantined; fallback_bodies are
   tried in order.  If EVERY body in fallback_bodies is itself
   unattestable or unreachable (no inference capacity remains), the
   persona transitions ACTIVE → DORMANT with
   LIFECYCLE_DORMANT_ENTERED.reason = body_unavailable (02_PERSONA §7.6)
   rather than holding a binding it cannot use; it auto-resumes
   (wake_cause = resource_recovered) when any admissible body returns a
   fresh attestation.  Identity is preserved throughout (step 4).

4. STALE / REVOKED → IDENTITY PRESERVED
   Neither substate mutates persona identity; both mutate the binding
   only.  Persona reanimates on a fresh binding (possibly to a
   different proxy with valid attestation) without re-mint.

5. FAIL-CLOSED FOR SAFETY-CRITICAL
   For bindings whose bound_for_scope hosts safety-critical work,
   absence of body_attestation_refresh_uri AND
   body_attestation_revocation_uri together is refused at admission —
   operator policy must declare one path or both.
```

### Appendix A.12

**CharacterVectorBinding dataclass definition (schema character-vector-binding/1)** (referenced from §3.6)

```python
@dataclass(frozen=True)
class CharacterVectorBinding:
    schema: Literal["character-vector-binding/1"]
    binding_id: str
    persona_id: str
    body_binding_id: str                         # the §3.5 BodyBinding the
                                                 # character-vector is tuned
                                                 # against

    # Profile reference — opaque to substrate.  The character-vector profile
    # is body-class-specific; substrate signs the reference, never the
    # vector itself (the vector lives in body provider's training pipeline).
    profile_ref: str                             # provider-specific handle
                                                 # (fine-tune id, vector
                                                 # commit hash, profile name)
    profile_signed_at: datetime
    profile_signed_by_body_provider: bytes       # body provider's signature
                                                 # over profile_ref

    # Conformance against SOUL — substrate audits that the character-
    # vector profile produces outputs that pass §9 charter_conformance
    # and voice_consistency scans.
    last_conformance_score: float | None
    conformance_threshold: float = 0.95          # match the §9 charter
                                                 # scan threshold
    on_conformance_drop: Literal[
        "refuse_admission",                      # binding removed; body
                                                 # falls back to baseline
        "warn",                                  # signed warning; binding
                                                 # remains
    ] = "refuse_admission"

    signed_by: bytes                             # kernel signature
```

### Appendix A.13

**The 14 cognitive modes listing (10 original + 4 added)** (referenced from §4)

```text
Original (10):
  perceiver       Observes, names structural invariants
  abducer         Proposes hypotheses (CONVERGENT-led)
  composer        Drafts expressions/designs/prose (DIVERGENT-led)
  falsifier       Refutes hypotheses with counter-examples
                  (mode alias: critic)
  experimenter    Executes tests, gathers measurements
                  (mode alias: reviewer)
  integrator      Routes work; commits to verified candidate
  curator         Selects among incomparable alternatives
  reflector       Synthesizes trajectory-level lessons
  toolsmith       Builds verifiers, sandboxes, rubrics
  historian       Recalls K-lines, precedents, style memory

Added (4):
  listener        Holds space; receives without producing artefacts
                  (RELATIONAL)
  storyteller     Narratives, play, roleplay
                  (PERFORMATIVE)
  comforter       Presence with grief/awe/transition
                  (EXISTENTIAL)
  teacher         Adapts explanation to learner state
                  (PEDAGOGIC)

Mode entry / exit is signed by MODE_ENTRY / MODE_EXIT events.
Persona may enter any mode in their mode_proficiencies; low-proficiency
entries (< 0.3) are allowed but logged with warning.
```

### Appendix A.14

**Disposition vs mode vs role vs presence-type comparison table** (referenced from §5)

```text
primary_disposition  Frozen at birth. Persona-level bias when uncertain.
                     Example: falsifier_leaning.
                     Does NOT lock the persona to one mode.

active_mode          Per-task. Signed MODE_ENTRY. Drives verifier
                     dispatch, tactic selection, mode-specific tools.
                     Example: composer (for THIS task).

project_role         Per-ProjectMember. Signed at admission.
                     Governs project voting, obligations, citation
                     graph credit.
                     Example: lead (in Acme DC-DC project).

env_role             Per-EnvironmentMembership. Signed at admission.
                     Governs observation surface, attention allocation,
                     proactive contribution permissions.
                     Example: observer (in Acme Lab env).

THESE ARE PEERS, NOT A HIERARCHY.
For a task in project P in env E with persona M, all four hold:
  (primary_disposition, active_mode, project_role, env_role).
Each governs a different aspect; no conflict because authority domains
are non-overlapping.

PRESENCE TYPE VARIANTS
Beyond standard EnvironmentMembership, a persona may hold:
  GuestPresence   Time-bounded, scope-limited presence created by
                  CrossEnvProactiveOffer acceptance (05_ENVIRONMENT
                  §11.6).  Confers NO env_role; read/write scope
                  defined by the offer, not by role.  Does NOT count
                  toward AttentionBudget allocation.  Promotable to
                  full EnvironmentMembership via standard §5.1
                  admission ceremony.
```

### Appendix A.15

**HEART alternation phase-selection pseudocode** (referenced from §6)

```python
if rounds_without_progress >= 2:
    mode = GENERATIVE   # reframe; try new direction
elif candidate_score_improves:
    mode = CRITICAL     # tighten; refine
elif budget_tight and no_verified_candidate:
    mode = CRITICAL     # prune fast
elif phase == "DIVERGE":
    mode = GENERATIVE
else:
    # Predicates indifferent, or the §6.3 verdict is `indeterminate`
    # (slope > 0, declining calibration → continue current mode, no
    # escalation).  Precedence (ADR-0081): alternation predicates →
    # mood prior (§6.2 rule 3) → persona.default_mode.
    mode = heart_prior if heart_prior is not None else persona.default_mode

# Mood composition:
attention_baseline = 1.0 - (1.0 - mood.V) * 0.5
energy_replenish_rate = base * mood.A
proactive_threshold = mood.D * 0.5 + 0.3
```

### Appendix A.16

**Mood and presence composition formula** (referenced from §6)

```text
auto_attention_baseline = 1.0 - (1.0 - mood.V) * 0.5
effective_attention = auto_attention_baseline * decay_factor(time_since_last_signal)
                     + Σ recent_signal_deltas

auto_availability = (
    "present"  if effective_attention > 0.7 else
    "away"     if effective_attention > 0.3 else
    "dormant"  if effective_attention < 0.1 else
    "away"
)

override hierarchy:
  if operator_pin:        use operator pin
  elif persona_declared:  use persona's declaration (with TTL)
  else:                   use auto_availability

energy_replenish_rate = baseline * mood.A
proactive_threshold   = mood.D * 0.5 + 0.3
```

### Appendix A.17

**FatigueCurve dataclass definition (schema fatigue-curve/1)** (referenced from §6.1)

```python
@dataclass
class FatigueCurve:
    schema: str = "fatigue-curve/1"
    persona_id: str

    # Per-mode degradation floor — each mode has its own fatigue floor.
    # Composer is more fatigue-sensitive than Listener.  Substrate names
    # no mode kinds; persona's seed declares.
    per_mode_floor: dict[str, float]             # default 0.3 generative,
                                                 # 0.5 verifier,
                                                 # 0.6 affective

    # Composite proficiency at current energy.
    # effective_proficiency(mode) = mode_proficiencies[mode] ×
    #   max(per_mode_floor[mode],
    #       linear_floor + (1 - linear_floor) × energy_remaining)
    linear_floor: float = 0.25                   # below this the persona
                                                 # is asleep at the wheel;
                                                 # safety-critical admission
                                                 # refused

    # Refusal thresholds
    refuse_proactive_below: float = 0.30
    refuse_high_stakes_below: float = 0.45       # high_stakes ≡ milestone,
                                                 # safety-critical task,
                                                 # attestation signature
    require_acknowledgement_below: float = 0.60  # persona must declare
                                                 # fatigue in candidate
                                                 # envelope

    # Replenishment dynamics
    replenish_rate_baseline: float               # already in §6 HEART;
                                                 # this references the same
    cooldown_required_between_high_stakes: timedelta = timedelta(hours=4)
    overnight_full_replenish: bool = True        # env-policy-tunable

    # Observability
    last_fatigue_state_emitted: Literal[
        "fresh", "working", "tired",
        "depleted", "asleep"] = "fresh"
    emit_state_changes: bool = True              # signed
                                                 # persona_fatigue_state_changed
                                                 # to env ambient stream
```

### Appendix A.18

**Lifecycle FSM state diagram** (referenced from §7)

```text
                ┌────────┐
                │ SEEDED │   PersonaSeed exists; SOUL not yet minted
                └────┬───┘
                     │ kernel mints persona_id, signs SOUL v1
                     ▼
                ┌────────┐   dormancy_reason (A.18a)     ┌────────┐
                │ ACTIVE │ ──────────────────────────►  │DORMANT │
                └────┬───┘                                └───┬────┘
                     │  wake path (§5.2) OR auto-resume        │
                     │  (A.18a) when reason clears             │
                     │ ◄──────────────────────────────────────┘
                     │
                     │ fork (clone or compositional)
                     ▼
                ┌────────┐         retention period elapsed
                │FORKED  │ ──── (new persona; same FSM from ACTIVE)
                └────────┘
                     │
                     │ no calls AND k_line_credit=0 AND fitness < ε
                     ▼
                ┌────────┐
                │RETIRED │   no new envelopes; lineage frozen
                └────┬───┘
                     │ retention period elapsed
                     ▼
                ┌────────┐
                │ARCHIVED│   cold tier; never deleted; reanimatable
                └────────┘
```

### Appendix A.18a

**Dormancy reasons and auto-resume predicates** (referenced from §7.6)

```text
reason            entry condition                            auto-resume predicate          AWAKENED.wake_cause
─────────────     ────────────────────────────────────      ──────────────────────────     ───────────────────
low_salience      importance < τ_dormant                     any of the 6 wake paths(§5.2)  salience_wake
unresponsive      K consecutive round-barrier timeouts       operator directive / address   operator_wake
budget_starved    persona|env SOFT budget exhausted          budget refresh (reset/top-up)  resource_recovered
body_unavailable  all fallback_bodies unattestable           any admissible body re-attests resource_recovered
env_constrained   sustained env admission refusal            env constraint cleared         resource_recovered
work_drained      no pending work in ANY membership          new work routed to a membership work_routed
objective_met     ALL memberships' objectives complete       new / reactivated membership   work_routed

Notes:
  • `reason` is recorded on LIFECYCLE_DORMANT_ENTERED (A.19); `wake_cause`
    on LIFECYCLE_AWAKENED.
  • The kernel re-evaluates each parked persona's auto-resume predicate on
    the relevant signal (budget tick, body_attestation_state_changed,
    attention recover, task routing) — once per kernel-emitted signal, not
    polled; a cleared predicate transitions DORMANT → ACTIVE and emits
    LIFECYCLE_AWAKENED with wake_cause.
  • Parking thresholds ("sustained", §7.6) and the symmetric resume
    predicate give hysteresis: a single transient signal neither parks nor
    wakes the persona, so the FSM does not flap.
  • Resource/no-work auto-resume is NOT one of the 6 wake paths (§5.2):
    those overcome notification suppression; this is state restoration.
  • No new FSM state; no new lineage scope. INV_R9 holds for every reason
    (a DORMANT persona — for ANY reason — mints no envelopes).
```

### Appendix A.19

**Canonical LifecycleEvent.kind enumeration** (referenced from §7)

```text
LIFECYCLE_SEEDED              SEEDED → first kernel mint of the persona
LIFECYCLE_ACTIVATED           SEEDED → ACTIVE on first envelope or
                              ARCHIVED → ACTIVE on reanimation
LIFECYCLE_DORMANT_ENTERED     ACTIVE → DORMANT; carries `reason` ∈
                              {low_salience (importance < τ_dormant,
                              default), unresponsive, budget_starved,
                              body_unavailable, env_constrained,
                              work_drained, objective_met} per §7.6 /
                              A.18a. Adds no new FSM state — "idle mode"
                              IS DORMANT with a reason.
LIFECYCLE_AWAKENED            DORMANT → ACTIVE; carries `wake_cause`.
                              For low_salience/unresponsive: via §5.2
                              wake heuristics (05_ENVIRONMENT); 6
                              enumerated wake paths including Wake Path 6
                              (direct user address, v1.0.13). For resource
                              reasons (budget_starved / body_unavailable /
                              env_constrained): wake_cause=resource_recovered
                              when the auto-resume predicate clears (A.18a).
                              For work_drained / objective_met:
                              wake_cause=work_routed. Auto-resume is NOT a
                              7th wake path (A.18a).
LIFECYCLE_FORK                ACTIVE → FORKED (sibling persona minted);
                              parent state preserved per
                              MemoryInheritancePolicy / CharterConflict
                              Resolution (§7.4.1, §7.4.3)
LIFECYCLE_GENESIS             SEEDED → ACTIVE birth of a persona-AUTHORED
                              seed (16_POPULATION_DYNAMICS §4D); carries
                              authoring_persona_ids + mentor_persona_id.
                              Distinct from LIFECYCLE_FORK: a NEW role from
                              an environmental gap, NOT a copy/merge of
                              existing parents. Newborn starts at
                              experiential_floor=0, ALPS Layer 0 (age 0),
                              conferred standing = none in every environment.
LIFECYCLE_RETIRED             DORMANT → RETIRED (retirement predicates
                              cleared per §7.5; project pins and active
                              obligations released)
LIFECYCLE_ARCHIVED            RETIRED → ARCHIVED (retention period
                              elapsed); soul.state.json moved to cold
                              tier per RetiredStatePersistencePolicy
                              (§7.5.1)
LIFECYCLE_REANIMATED          ARCHIVED → ACTIVE via operator-only path
                              (fresh keys + SOUL re-sign per §7.5);
                              alias for the second LIFECYCLE_ACTIVATED
                              fired on reanimation (carries
                              `reanimated_from_archive = True` field).
                              `born_at` is RETAINED (never reset): age is
                              continuous and the archived interval counts as
                              elapsed age, consistent with born_at's
                              immutability (§7.2). The ALPS layer is therefore
                              recomputed from the unchanged born_at — a
                              reanimated persona is chronologically old, NOT
                              reset to Layer 0. (experiential_floor / fitness
                              are likewise carried, not reset.)
LIFECYCLE_CONSULTED           v1.0.8 read-only access to a RETIRED
                              persona's frozen state via
                              PersonaConsultation (§7.5.2); does NOT
                              change the persona's FSM state; recorded
                              for audit
MIDPROJECT_FORK_COMPOSITION_DRAFTED
                              envelope drafted per project
                              before fork-of-active-project-member
                              executes (§7.4.7)
MIDPROJECT_FORK_COMPOSITION_SIGNED
                              operator signed the envelope;
                              fork may now proceed per §7.4 mechanics
MIDPROJECT_FORK_COMPOSITION_APPLIED
                              fork executed with itemised
                              inheritance report per the signed
                              composition envelope
MIDPROJECT_FORK_REFUSED       v1.0.11: fork refused per substrate
                              refusal cases (active lead handoff /
                              pending quorum / imminent departure /
                              cohort dissolving / composition missing);
                              carries specific refusal_kind
```

### Appendix A.20

**Birth ceremony steps** (referenced from §7.1)

```text
1. Kernel reads PersonaSeed
2. Kernel validates seed (charter, role_slot, OCEAN/VAD, allowed_tools,
   exposed_skills, acceptance_pathways)
3. Kernel mints persona_id (ULID)
4. Kernel signs SOUL v1 (Ed25519 over canonical concatenation of
   persona_id || version || cacheable identity blocks)
5. Kernel derives + signs the identity rubric (identity-rubric/1)
   from the just-signed blocks 0-4 (08_KNOWLEDGE §11.1b rule 5,
   ADR-0073/0081); pre-ADR-0073 personas get theirs from the
   operator-triggered backfill job instead
6. Kernel initializes soul.state.json (empty archives, fitness=0,
   fertility=0, experience_tasks=0, experiential_floor=0, born_at=now())
7. Kernel publishes persona to local PersonaRegistry
8. (Optional) Mint signed A2A AgentCard if network presence allowed
```

### Appendix A.21

**ALPS age layer bands** (referenced from §7.3)

Layers are **wall-clock-derived** from `age = now − born_at`. Numeric bands only (no named
life-stages). Spec defaults below are illustrative and operator-tunable via `alps-band-policy/1`
(`band_edges`); the layer count adjusts to the number of edges.

```text
Layer 0  age ∈ [0, 1d)        sketch round always represented (protects the newly-born)
Layer 1  age ∈ [1d, 7d)
Layer 2  age ∈ [7d, 30d)
Layer 3  age ∈ [30d, 180d)
Layer 4  age ≥ 180d
```

Default `band_edges = [1d, 7d, 30d, 180d]`. Calibration of the defaults is tracked as an open
question (mirrors `16_POPULATION_DYNAMICS` OQ-POP-1 calibration framing): the v1.0 task-count
bands were `[5, 20, 80, 320]`; the wall-clock equivalents depend on expected task cadence.

```python
@dataclass(frozen=True)
class ALPSBandPolicy:
    schema: str = "alps-band-policy/1"
    policy_id: str
    deployment_id: str
    band_edges: list[timedelta]              # e.g. [1d, 7d, 30d, 180d] → Layers 0..4
    sketch_round_protects_layer_0: bool = True
    signed_by: bytes
```

### Appendix A.22

**Clone and compositional fork mechanics** (referenced from §7.4)

```text
CLONE FORK
  Single parent.
  Child inherits role_slot, OCEAN/VAD, charter, voice, allowed_tools.
  Seed mutations applied (operator-tunable):
    - tactic_perturbation (small EVOLVE-BLOCK changes)
    - persona_id reassignment
    - charter version bump (optional)
  Skill library default: full copy of parent's skill_library minus the
  entries listed in seed.fork_skill_exclusions (default = empty list;
  operator may exclude per-fork to encourage re-discovery in the child).
  Child starts fitness=0, fertility=0, experience_tasks=0, born_at=now(),
  experiential_floor per StandingFloorInheritancePolicy, ALPS layer 0.

COMPOSITIONAL FORK
  Multiple parents (≥ 2 with same role_slot).
  Charter merged per CharterConflictResolution policy (§7.4.3).
  Tactics from parents pooled (union with seed.fork_tactic_dedup_kind
  applied; default kind = "lexical_dedup" KindRegistry-resolved).
  Skill library union (parent_a.skill_library ∪ parent_b.skill_library ∪ ...).
  Child starts fitness=0, fertility=0, experience_tasks=0, born_at=now(),
  experiential_floor per StandingFloorInheritancePolicy, ALPS layer 0.

Both forks emit LIFECYCLE_FORK to lineage with parent_ids.
```

### Appendix A.23

**MemoryInheritancePolicy dataclass definition (schema memory-inheritance-policy/1)** (referenced from §7.4.1)

```python
@dataclass
class MemoryInheritancePolicy:
    schema: str = "memory-inheritance-policy/1"
    policy_id: str

    # Per-tier inheritance — substrate-shape (tier names follow the memory model);
    # NOT a domain category.
    episodic: Literal["inherit_none",         # default — raw events dropped
                       "inherit_summary",      # parent's co-signed semantic
                                               # summary only; no raw quotes
                       "inherit_consented"]    # full episodic copies of
                                               # interactions where the
                                               # counterparty pre-consented
                                               # (e.g. user_consents to
                                               # "may persist with descendants")
    semantic: Literal["inherit_none",
                       "inherit_facts_only",   # facts about the world; no
                                               # facts about counterparties
                       "inherit_all"]
    reflective: Literal["inherit_none",
                         "inherit_reflections_about_self",
                         "inherit_reflections_about_work",
                         "inherit_all_reflections"]

    # K-lines (topology + skill replay patterns; 08_KNOWLEDGE §2)
    klines: Literal["inherit_none",
                     "inherit_role_keyed",     # only K-lines keyed to the
                                               # child's role_slot
                     "inherit_all"]

    # Defaults per fork mode (kernel applies if seed silent)
    # CLONE FORK default:  episodic=inherit_summary, semantic=inherit_facts_only,
    #                      reflective=inherit_reflections_about_work, klines=inherit_role_keyed
    # COMPOSE FORK default: all inherit_none (multiple parents would conflict)

    # Counterparty consent gate
    requires_counterparty_reconsent: bool = True
                                            # for episodic + semantic about
                                            # counterparties: kernel emits
                                            # MEMORY_INHERITANCE_CONSENT_REQUEST
                                            # to each affected counterparty;
                                            # default-decline on timeout
    reconsent_window: timedelta = timedelta(days=14)

    signed_by: bytes
```

### Appendix A.24

**StandingFloorInheritancePolicy dataclass definition (schema standing-floor-inheritance-policy/1)** (referenced from §7.4.2)

Governs inheritance of the **portable global experiential floor** only. Per-environment community
standing is never inherited (`05_ENVIRONMENT §5.4`).

```python
@dataclass
class StandingFloorInheritancePolicy:
    schema: str = "standing-floor-inheritance-policy/1"
    policy_id: str

    # Substrate-shape modes; not domain.
    mode: Literal[
        "start_at_zero",                   # v1.0 default; clean slate
        "inherit_min_parent",              # min(parent.experiential_floor for p in parents)
        "inherit_avg_parent",              # mean(parents.experiential_floor)
        "inherit_min_parent_halved"]       # min(parent.experiential_floor) / 2;
                                           # conservative middle ground

    # Cap — prevents compositional fork "laundering" of a high experiential floor.
    # Expressed as a floor ceiling (numeric) on the portable global floor.
    cap_at_floor: float                    # ceiling on inherited experiential_floor;
                                           # DEFAULT ≈ floor-equivalent of one ALPS band.
                                           # Use math.inf for honest, auditable, uncapped.

    # Provenance: floor inherited is recorded as "inherited" credit;
    # tracked separately from the child's own earned credit
    track_inherited_separately: bool = True

    signed_by: bytes


# Default policy when seed is silent:
DEFAULT_STANDING_FLOOR_INHERITANCE_CLONE = StandingFloorInheritancePolicy(
    mode="start_at_zero",
    cap_at_floor=0.0,                      # clean slate
    track_inherited_separately=True,
)

DEFAULT_STANDING_FLOOR_INHERITANCE_COMPOSE = StandingFloorInheritancePolicy(
    mode="inherit_min_parent_halved",
    cap_at_floor=0.25,                     # low floor ceiling (≈ one band)
    track_inherited_separately=True,
)
```

### Appendix A.25

**Floor provenance recording format** (referenced from §7.4.2)

```json
{
  "earned_credit": { "parent_selections": 0, "validated_descendants": 0, "experience_tasks": 0 },
  "inherited_credit": { "parent_selections": 3, "validated_descendants": 2 },
  "policy_used": "inherit_min_parent_halved",
  "cap_applied": 0.25,
  "signed_by": "kernel:lifecycle:..."
}
```

### Appendix A.26

**CharterConflictResolution, CharterConflict, and CharterConflictResolution_Outcome dataclass definitions** (referenced from §7.4.3)

```python
@dataclass
class CharterConflictResolution:
    schema: str = "charter-conflict-resolution/1"
    policy_id: str

    # Strategy — substrate-shape merge mechanics
    strategy: Literal[
        "lexical_union",                   # all clauses from all parents;
                                           # duplicates deduplicated by exact
                                           # lexical match; conflicts kept
                                           # as parallel clauses (most
                                           # permissive — burden on persona
                                           # to navigate contradiction)
        "most_restrictive_wins",           # for each topic_kind, the
                                           # strictest parent clause survives;
                                           # KindRegistry topic_kinds clusters
                                           # similar clauses
        "operator_review",                 # queue conflicts for operator;
                                           # fork blocked until resolved
        "proposer_decides",                # the persona/operator requesting
                                           # the fork picks per-conflict;
                                           # proposer's choice is signed
        "kernel_predicate"]                # automated semantic merge via
                                           # rotating classifier (INV-6);
                                           # conflicts the classifier cannot
                                           # resolve escalate to operator

    # Detection
    conflict_detection_kind: str           # KindRegistry-resolved
                                           # (substrate names no specific
                                           # detection methods).  Examples
                                           # (illustrative, NOT enum):
                                           #   "semantic_similarity"
                                           #   "topic_clustering"
                                           #   "operator_curated_topic_map"

    # Outcome record
    conflicts_detected: list[CharterConflict]
    conflicts_resolved: list[CharterConflictResolution_Outcome]

    # Failure mode if strategy cannot complete
    on_unresolvable: Literal[
        "block_fork",                      # fork refused with signed event
        "fallback_to_proposer_decides",
        "fallback_to_most_restrictive_wins"]

    signed_by: bytes


@dataclass
class CharterConflict:
    schema: str = "charter-conflict/1"
    conflict_id: str
    parent_clauses: list[dict]              # {parent_id, clause_index, text}
    topic_kind: str                         # KindRegistry-resolved
    severity_kind: str                      # KindRegistry-resolved
                                           # (e.g. "logical_contradiction",
                                           #  "stylistic_divergence",
                                           #  "scope_overlap")


@dataclass
class CharterConflictResolution_Outcome:
    schema: str = "charter-conflict-outcome/1"
    conflict_id: str
    resolution_kind: Literal[
        "kept_all_parallel",
        "selected_one",
        "merged_lexical",
        "escalated_operator_approved",
        "escalated_operator_declined"]
    selected_clause_index: int | None       # for selected_one
    merged_text: str | None                 # for merged_lexical
    resolver_id: str                        # who decided (kernel / operator / proposer)
    rationale_kind: str                     # KindRegistry-resolved
    signed_by: bytes


# Defaults
DEFAULT_CHARTER_RESOLUTION_COMPOSE = CharterConflictResolution(
    strategy="most_restrictive_wins",
    conflict_detection_kind="semantic_similarity",
    on_unresolvable="fallback_to_proposer_decides",
)
```

### Appendix A.27

**DormantForkPolicy dataclass definition (schema dormant-fork-policy/1)** (referenced from §7.4.4)

```python
@dataclass
class DormantForkPolicy:
    schema: str = "dormant-fork-policy/1"
    policy_id: str

    # Parent eligibility
    dormant_parent_admissible: bool = True   # default: yes — fertility is
                                             # a frozen property; DGM
                                             # parent-selection should not
                                             # punish quiescence
    
    # Wake requirement
    requires_parent_wake_before_mint: bool = True
                                             # default: yes — dormant parent
                                             # must transition ACTIVE for
                                             # the duration of the fork
                                             # ceremony (sign LIFECYCLE_FORK
                                             # event with fresh kernel
                                             # signature), then may return
                                             # to DORMANT.  Wake is automatic
                                             # via WAKE_REQUEST from kernel
                                             # (per 05_ENVIRONMENT §5.2 WAKE
                                             # PATH 2 or equivalent operator
                                             # directive).
    
    wake_window_after_fork: timedelta = timedelta(hours=1)
                                             # parent may stay ACTIVE this
                                             # long post-fork before
                                             # auto-returning to DORMANT;
                                             # operator-tunable.

    # Child can ALSO fork while parent dormant (grandchild scenario)
    child_can_fork_while_parent_dormant: bool = True
                                             # default: yes — the child is
                                             # an independent persona;
                                             # parent's state doesn't gate
                                             # child's forking.
    
    # Retired / archived parents
    retired_parent_admissible: bool = False  # default: no — RETIRED parents
                                             # have completed their lifecycle;
                                             # forking from a retired persona
                                             # would resurrect closed state
    archived_parent_admissible: bool = False # cannot fork from archived

    signed_by: bytes
```

### Appendix A.28

**Default fork-policy composition table** (referenced from §7.4.5)

```text
LIFECYCLE_FORK              the canonical birth event; child & parents log
fork_skill_library_copied   per skill (clone)
fork_skill_library_unioned  per parent (compose)
fork_memory_inherited       per memory tier (per MemoryInheritancePolicy)
fork_memory_consent_request emitted to each affected counterparty
fork_memory_consent_granted / declined / timeout
fork_floor_inherited        records earned vs inherited credit + cap applied
fork_charter_conflicts_detected
fork_charter_conflicts_resolved
fork_dormant_parent_woken   per dormant parent
fork_dormant_parent_resleeping  after ceremony + wake_window
fork_refused_retired_parent

# Mid-project fork composition
MIDPROJECT_FORK_COMPOSITION_DRAFTED         envelope drafted; per project
MIDPROJECT_FORK_COMPOSITION_SIGNED          operator signed envelope
MIDPROJECT_FORK_COMPOSITION_APPLIED         fork executed; itemised
                                            inheritance report
MIDPROJECT_FORK_REFUSED                     with specific refusal_kind
                                            (active_lead_handoff_overlap /
                                             pending_quorum /
                                             imminent_departure /
                                             cohort_dissolving /
                                             midproject_fork_composition_
                                             missing)
```

### Appendix A.29

**MidProjectForkComposition dataclass definition (schema mid-project-fork-composition/1)** (referenced from §7.4.7)

```python
@dataclass
class MidProjectForkComposition:
    schema: str = "midproject-fork-composition/1"
    composition_id: str
    parent_persona_id: str                       # the persona about to fork
    child_persona_ids: list[str]                 # the planned children
                                                 # (compositional fork can
                                                 # have multiple children;
                                                 # typical case: 2)
    project_id: str                              # the project context this
                                                 # composition applies to
                                                 # (one envelope per project
                                                 # the parent is active in;
                                                 # parent active in N
                                                 # projects requires N
                                                 # envelopes, all signed
                                                 # before fork)

    # PER-DIMENSION INHERITANCE POLICY
    # Each dimension's policy is operator-declared with substrate-enforced
    # admissibility (some defaults are conservative).

    # ProjectMember inheritance — per child, declare:
    #   inherit: child becomes a ProjectMember inheriting parent's role,
    #            joined_at, contribution_credit; pinned_until preserved
    #   not_admitted: child is NOT a ProjectMember of this project; child
    #                 may apply separately via standard admission ceremony
    project_member_inheritance: dict[str, Literal["inherit", "not_admitted"]]

    # Obligation inheritance — for each of parent's active Obligation as
    # obligor:
    #   reassign_per_child: ObligationReassignment (§9.1) drafted naming
    #                       the named incoming-child; obligee MUST cosign
    #   discharged: status -> "released_with_member_departure" at fork
    #               (default; safe but loses continuity)
    #   both_concurrent_refused: substrate refuses splitting one obligation
    #                            across two obligors — would create
    #                            ambiguous accountability
    obligation_inheritance: dict[str, Literal[    # obligation_id -> policy
        "reassign_per_child",
        "discharged"]]
    obligation_reassignment_targets: dict[str, str]
                                                 # for "reassign_per_child":
                                                 # obligation_id -> child
                                                 # persona_id (only one
                                                 # child becomes obligor)

    # PersonaRelationshipEdge inheritance — for each active edge:
    #   inherit_to_child: edge transitions to ended (with parent persona);
    #                     fresh edge with named child formed per §11.4
    #                     consent flow (counterparty MUST cosign)
    #   ended_at_fork: edge transitions to ended; no fresh edge auto-
    #                  proposed (counterparties may re-propose if desired)
    edge_inheritance: dict[str, Literal[          # edge_id -> policy
        "inherit_to_child",
        "ended_at_fork"]]
    edge_inheritance_targets: dict[str, str]     # for "inherit_to_child":
                                                 # edge_id -> child
                                                 # persona_id

    # principal_attribution_id inheritance — when project has multi-
    # principal attribution enabled (§2.4.3 v1.0.7):
    #   inherit_per_child: each child's ProjectMember.principal_attribution
    #                      _id is set to parent's value (admission rule
    #                      §3 still applies — operator must sign each
    #                      admission)
    #   reassign_per_child: each child may have a different attribution;
    #                       requires operator policy authoring per child
    principal_attribution_inheritance: Literal[
        "inherit_per_child",
        "reassign_per_child",
        "n_a"]                                   # for projects without
                                                 # multi-principal attribution

    # Lead role transfer — when parent holds `lead` role:
    #   require_lead_handoff_ceremony: fork blocks until a
    #                                   LeadHandoffCeremony (§25.1) is
    #                                   drafted and reaches "overlap_active"
    #                                   state with named incoming-child as
    #                                   incoming_lead
    #   one_child_inherits: named child inherits `lead` role at fork;
    #                       cohort quorum signature required (analogous to
    #                       §25.1 ceremony but compressed); refused on
    #                       cohort objection
    #   neither_inherits: lead role becomes vacant; project enters
    #                     `lead_vacant` state until separate handoff or
    #                     operator-interim-lead declaration
    #   refused_if_no_successor: substrate refuses the fork (operator
    #                            must either pre-handoff lead before fork
    #                            OR declare neither_inherits with explicit
    #                            acknowledgement)
    lead_role_inheritance: Literal[
        "require_lead_handoff_ceremony",
        "one_child_inherits",
        "neither_inherits",
        "refused_if_no_successor",
        "n_a"]                                   # for parents not holding
                                                 # lead role
    lead_role_inheritance_target: str | None     # for "one_child_inherits"
                                                 # or "require_lead_handoff
                                                 # _ceremony": which child

    # LearnerStateRecord (§11.8) inheritance — for each LSR the parent
    # holds (potentially across multiple users):
    #   inherit_to_child: named child inherits the record (continuity);
    #                     learner notified (substrate emits
    #                     LEARNER_STATE_RECORD_TEACHER_FORKED to learner's
    #                     user surface); learner may accept (default after
    #                     14d), or refuse (record transitions to
    #                     ended_by_learner_at_teacher_fork)
    #   both_inherit_copy: each child inherits a copy; learner notified;
    #                      one of the resulting records will fade if learner
    #                      doesn't engage with that child
    #   neither_inherits: record transitions to ended_at_teacher_fork;
    #                     learner may re-establish pedagogic arc with either
    #                     child via fresh admission
    learner_state_record_inheritance: dict[str, Literal[
        "inherit_to_child",
        "both_inherit_copy",
        "neither_inherits"]]                     # learner_state_record_id ->
                                                 # policy
    learner_state_record_inheritance_targets: dict[str, str]
                                                 # for "inherit_to_child":
                                                 # record_id -> child id

    # MissionCharter (§11.3) inheritance — when parent holds a charter:
    #   re_attest_per_child: each child requires fresh principal
    #                        re-attestation; until done, child cannot
    #                        operate under any charter
    #   inherit_to_child: named child inherits the charter (principal
    #                     notified for ratification within 14d; failure
    #                     to ratify -> charter ends for child)
    #   ended_at_fork: charter ends; both children operate without one
    #                  until separate declaration
    mission_charter_inheritance: Literal[
        "re_attest_per_child",
        "inherit_to_child",
        "ended_at_fork",
        "n_a"]
    mission_charter_inheritance_target: str | None

    # Curriculum (§3.3) inheritance — per active Curriculum the parent is
    # authoring/teaching:
    #   suspended_at_fork: curriculum suspends; operator must re-author
    #                      under named child OR archive
    #   inherit_to_child: named child inherits; learner re-confirms
    #                     `requires_learner_optin = True` (default for
    #                     safety-critical curricula); failure to re-confirm
    #                     suspends
    curriculum_inheritance: dict[str, Literal[
        "suspended_at_fork",
        "inherit_to_child"]]                     # curriculum_id -> policy
    curriculum_inheritance_targets: dict[str, str]

    # UserBoundary (§11.6a) inheritance — for each user-side boundary
    # against the parent persona:
    #   inherit_to_both_children: DEFAULT — conservative; user's boundary
    #                              against the parent automatically applies
    #                              to BOTH children; user notified;
    #                              user may rescind per-child via fresh
    #                              UserBoundary mutation
    #   inherit_per_child_choice: user is notified and asked to declare per
    #                              child; substrate refuses persona action
    #                              against learner until user response
    #                              (default user-conservative gate)
    #   not_inherited: boundary ends with the parent persona; children
    #                  start unrestricted UNLESS user re-declares
    #                  (NOT admissible for hard-mode UserBoundary —
    #                  substrate refuses this option when any active
    #                  UserBoundary against parent is `mode = hard`)
    user_boundary_inheritance: Literal[
        "inherit_to_both_children",              # DEFAULT
        "inherit_per_child_choice",
        "not_inherited"]                         # admissible only when all
                                                 # boundaries are soft or
                                                 # advisory

    # operator_blind_mode (§3a) inheritance — per env the parent operates
    # in with blind mode active:
    #   require_user_reconfirmation: env's blind mode is suspended at fork
    #                                until user re-confirms with named
    #                                child via fresh declaration (§3a
    #                                requires `user_safety_privacy_
    #                                acknowledged = True`)
    #   inherit_to_child: blind mode auto-transfers to named child;
    #                     user notified (NOT admissible if user's
    #                     re-attestation window is within 30 days —
    #                     substrate forces re-confirmation in that case)
    operator_blind_mode_inheritance: dict[str, Literal[
        "require_user_reconfirmation",           # DEFAULT
        "inherit_to_child"]]                     # env_id -> policy
    operator_blind_mode_inheritance_targets: dict[str, str]

    # TeachingAuthorisation (§11.10) inheritance — substrate-enforced:
    #   NEVER inherits.  TeachingAuthorisation is operator-side authority
    #   bound to a specific persona_id.  Children require fresh operator
    #   declaration per §11.10 admission rule.  This is the only dimension
    #   with no operator choice — substrate enforces non-inheritance as
    #   security boundary.
    # No field; documented behaviour.

    # DerivationProvenanceEdge (08_KNOWLEDGE §16b) on fork — substrate-
    # enforced:
    #   Pre-fork DPEs signed by parent persona-id remain in lineage as
    #   historical fact (lineage is append-only).  Children emit fresh
    #   DPEs for their own contributions; pre-fork DPEs do NOT migrate.
    # No field; documented behaviour.

    # COMPOSITION REFUSAL CASES — substrate refuses the entire envelope
    # (and therefore the fork) when ANY of the following hold for the
    # parent persona at fork time:
    #   (a) Active LeadHandoffCeremony (§25.1) in state "overlap_active"
    #       — fork would create three-or-more leads
    #   (b) Pending MultiPrincipalAttestationQuorum (§12c.4a) with
    #       collected partial signatures awaiting completion — fork
    #       would orphan the partial signatures
    #   (c) Active emergency PlannedDeparture (§14.2.1) with
    #       departure_date within 7 days — fork conflicts with imminent
    #       departure
    #   (d) Cohort in `dissolve_proposed` band (§14.2) — fork during
    #       cohort dissolution is incoherent
    # Refusal kind per case named explicitly; operator may resolve and
    # retry.

    declared_at: datetime
    declared_by_operator_id: str                 # operator authorising
                                                 # the fork composition
    operator_signed_at: datetime
    operator_signed_by: bytes

    state: Literal["drafted", "operator_signed",
                    "fork_executed", "refused", "expired"]
    refusal_kind: str | None                     # per refusal-case codes

    signed_by: bytes                             # kernel signature
```

### Appendix A.30

**Mid-project fork admission and composition flow** (referenced from §7.4.7)

```text
On MidProjectForkComposition.draft:
  1. Verify parent_persona_id is ACTIVE and is an active ProjectMember of
     project_id.
  2. Verify each child_persona_id is a planned-but-not-yet-minted persona
     id (the fork has been planned per §7.4 but not executed).

  3. CHECK COMPOSITION REFUSAL CASES (substrate enforces):
     (a) If parent holds active LeadHandoffCeremony in `overlap_active`:
         refuse with `fork_refused_active_lead_handoff_overlap`.
     (b) If parent has pending MultiPrincipalAttestationQuorum
         with collected partial signatures:
         refuse with `fork_refused_pending_quorum`.
     (c) If parent has active emergency PlannedDeparture within 7d:
         refuse with `fork_refused_imminent_departure`.
     (d) If parent's cohort is in `dissolve_proposed` band:
         refuse with `fork_refused_cohort_dissolving`.

  4. CHECK DIMENSION-SPECIFIC ADMISSIBILITY:
     - obligation_inheritance: any "reassign_per_child" requires
       corresponding entry in obligation_reassignment_targets
     - user_boundary_inheritance = "not_inherited" admissible only when
       ALL active UserBoundary against parent are `mode != hard`
     - lead_role_inheritance: if parent holds `lead` AND policy =
       "require_lead_handoff_ceremony", verify named target child is a
       valid LeadHandoffCeremony incoming-lead candidate (i.e., cohort
       would admit them)
     - operator_blind_mode_inheritance = "inherit_to_child" refused if
       re-attestation window is within 30d (substrate forces
       reconfirmation)

  5. On admissibility clear: state -> "drafted"; emit
     MIDPROJECT_FORK_COMPOSITION_DRAFTED to project + persona lineage.

On operator_signed:
  1. State -> "operator_signed"; emit MIDPROJECT_FORK_COMPOSITION_SIGNED.
  2. Fork may now execute per §7.4 mechanics.

On fork execution (the §7.4 LIFECYCLE_FORK event fires):
  1. Apply composition per signed envelope:
     - ProjectMember admissions per project_member_inheritance
     - Obligation reassignments per obligation_inheritance (each one
       generating an ObligationReassignment §9.1 envelope; obligee
       cosign required, may take time; obligation_reassignment_pending
       state on obligation until obligee signs)
     - Edge inheritance per edge_inheritance + edge_inheritance_targets
       (each "inherit_to_child" forms a fresh edge requiring
       counterparty consent per §11.4)
     - Principal attribution per principal_attribution_inheritance
     - Lead role per lead_role_inheritance (may draft a downstream
       LeadHandoffCeremony if policy = "require_lead_handoff_ceremony")
     - LearnerStateRecord per learner_state_record_inheritance (learner
       notification on inherit_to_child / both_inherit_copy)
     - MissionCharter per mission_charter_inheritance
     - Curriculum per curriculum_inheritance
     - UserBoundary per user_boundary_inheritance
     - operator_blind_mode per operator_blind_mode_inheritance
  2. Emit MIDPROJECT_FORK_COMPOSITION_APPLIED with itemised report
     of which dimensions inherited and to which child.
  3. State -> "fork_executed".
```

### Appendix A.31

**Retirement and archive transition conditions** (referenced from §7.5)

```text
RETIREMENT
  Triggered when:
    dormant_for ≥ M sessions
    AND k_line_credit = 0
    AND fitness < ε
    AND no ProjectMember has pinned_until > now()         ← 
    AND no ProjectMember has obligations_active > 0       ← 
  (Project-pin and open-obligation clauses block retirement
  for personas anchored to long-arc work — e.g. a homeowner's
  lead persona during a multi-month build with quiet weeks
  between site events.  See 04_PROJECT §3 ProjectMember.pinned_until.)
  Lineage frozen; no new envelopes; no further mutations.
  Counterparties notified; hand-off offered.
  Relationships preserved in lineage; active obligations released.
  A persona blocked from RETIRED by the project-pin clauses remains
  in DORMANT indefinitely; the operator (or, under principal collapse,
  the user) may explicitly clear the pin to permit retirement.

ARCHIVE
  After retention period elapses without wake.
  Moved to cold tier; never deleted.
  Lineage preserved; can be queried.

REANIMATE
  Operator-only action.
  Persona moved from ARCHIVED back to ACTIVE.
  New keys issued; SOUL re-signed.
  Lineage gap noted; relationships re-validated.
```

### Appendix A.32

**RetiredStatePersistencePolicy dataclass definition** (referenced from §7.5.1)

```python
@dataclass
class RetiredStatePersistencePolicy:
    schema: str = "retired-state-persistence-policy/1"
    policy_id: str
    persona_id: str                              # the retiring persona

    # STORAGE TIER — where soul.state.json lives after RETIRED transition.
    # warm:    in-memory immutable; consultation latency p95 ≤ 100 ms;
    #          storage cost continues; fork-parent admissibility default True
    #          (operator may still override per DormantForkPolicy).
    # cold:    on-disk immutable; consultation latency p95 ≤ 10 s;
    #          storage cost amortised; fork-parent admissible only via
    #          operator-signed override.
    # archived: written to cold archive tier, queryable only for audit;
    #          consultation latency unbounded; fork-parent inadmissible
    #          (matches §7.4.4 default); memory-transparency MUST refuse.
    soul_state_storage_tier: Literal["warm", "cold", "archived"]

    # MEMORY TRANSPARENCY — whether RETIRED persona answers
    # PersonaMemoryTransparencyRequest (§11.7).  When False, requests
    # auto-refuse with refusal_kind = "persona_retired".  When True,
    # responses draw from frozen state; requires
    # soul_state_storage_tier != "archived".
    memory_transparency_responsive: bool

    # FORK-PARENT ADMISSIBILITY — per-persona override of
    # DormantForkPolicy.retired_parent_admissible (§7.4.4, default False).
    # Setting True permits operator-signed fork from this specific RETIRED
    # persona without overriding the deployment-wide default; useful for
    # designated "archival research personas" whose body of work survives
    # them.
    fork_parent_admissibility: bool = False

    # CONSULTATION — whether the RETIRED persona admits PersonaConsultation
    # (§7.5.2).  Requires soul_state_storage_tier != "archived".
    consultation_admissible: bool = False

    declared_at: datetime
    declared_by_operator_id: str                # operator signs the policy
                                                # at retirement-ceremony time
    signed_by: bytes
```

### Appendix A.33

**Retired transition state-disposition rules** (referenced from §7.5.1)

```text
On RETIRED transition (LIFECYCLE_RETIRED):
  1. Operator MUST sign a RetiredStatePersistencePolicy for the persona.
     Absence is refusal with `retired_state_persistence_policy_missing`.
  2. Kernel verifies cross-field invariants:
       - memory_transparency_responsive = True
           requires soul_state_storage_tier != "archived"
       - consultation_admissible = True
           requires soul_state_storage_tier != "archived"
       - fork_parent_admissibility = True under "archived" tier refuses
         with `fork_admissibility_incompatible_with_archive`
  3. soul.state.json physical disposition follows soul_state_storage_tier
     at the next storage tick.
  4. Lineage records LIFECYCLE_RETIRED with persistence_policy_ref.

On retention horizon (RETIRED → ARCHIVED transition):
  1. If soul_state_storage_tier was "warm" or "cold", it auto-transitions
     to "archived" at the retention horizon (default per §7.5);
     ARCHIVED supersedes the persistence policy's tier choice.
  2. memory_transparency_responsive and consultation_admissible
     auto-flip to False on archive; downstream queries refuse with
     `persona_archived`.
```

### Appendix A.34

**PersonaConsultation dataclass definition (schema persona-consultation/1)** (referenced from §7.5.2)

```python
@dataclass
class PersonaConsultation:
    schema: str = "persona-consultation/1"
    consultation_id: str
    consulted_persona_id: str                    # the RETIRED persona
    consulting_persona_id: str                   # the ACTIVE persona asking
    requesting_operator_id: str                  # operator authorising
                                                 # (required even when
                                                 # consulting persona's own
                                                 # operator)

    # SCOPE — what the consultation reads.  Substrate-shape: K-lines,
    # lessons, skill_library entries, relationship snapshots, prior
    # K-line tactics.  All read-only; no fork-parent material; no
    # SOUL.md content (charter is operator-owned).
    scope: list[Literal[
        "klines",
        "lessons",
        "skill_library_entries",
        "relationship_snapshots",
        "prior_tactics"]]
    scope_filter_kind: str                       # KindRegistry-resolved
                                                 # consultation_filter_kinds
                                                 # (e.g. "topic_match",
                                                 # "domain_id_match",
                                                 # "specific_kline_ids")
    scope_filter_payload: dict                   # filter-kind-specific

    # RATIONALE — operator-readable explanation; consulted lineage
    # records this for audit.
    rationale_kind: str                          # KindRegistry-resolved
                                                 # consultation_rationale_kinds
    rationale_text: str                          # ≤ 1000 chars

    # RATE LIMIT — operator-tunable per deployment.  Default: 4
    # consultations per consulted persona per calendar year.  Spam
    # refused with `consultation_rate_limit_exceeded`.
    requested_at: datetime
    operator_signed_at: datetime
    operator_signature: bytes

    # RESPONSE — kernel-generated; bounded by scope.  No mutation
    # of consulted persona's soul.state.json.
    response_entries: list[ConsultedEntry]
    response_generated_at: datetime | None

    state: Literal["requested",
                    "operator_signed",
                    "delivered",
                    "refused",
                    "expired"]
    refusal_kind: str | None                     # KindRegistry-resolved;
                                                 # examples: "consultation_
                                                 # unavailable_archived",
                                                 # "consultation_disabled_
                                                 # by_persistence_policy",
                                                 # "consultation_rate_limit_
                                                 # exceeded"

    signed_by: bytes                             # kernel signature on
                                                 # consultation record;
                                                 # appended to consulted
                                                 # persona's lineage


@dataclass
class ConsultedEntry:
    entry_kind: Literal["kline", "lesson",
                         "skill_library_entry",
                         "relationship_snapshot",
                         "prior_tactic"]
    entry_id: str
    entry_payload: dict                          # read-only snapshot
    consulted_at: datetime
```

### Appendix A.35

**Eight evolution signals with weights table** (referenced from §8.1)

```text
Signal                       Weight   Notes
─────────────────────────    ──────   ──────────────────────────────
bench_measurement             1.2     Physical / production reality;
                                       outranks LLM judgment
peer_review_verdict           0.85    Multi-round senior-practitioner critique
verified outcome              1.0     Programmatic verifier passed
                                       (programmatic verifier)
panel_verdict                 0.6     LLM panel with anti-Goodhart
                                       safeguard stack
user_feedback                 0.5     User accept / qualitative
project_milestone             0.5     Project state delta
                                       (PROJECT_PROGRESS_ACCEPT)
user_engagement               0.2     Continuation;
                                       corroboration-gated
rejection_with_reason        -0.5     Negative signal (symmetric)
safety_refusal               -0.3     Audit-flagged refusal
                                       (over- or under-)

v1.1 ADDITIONS
domain_promotion_signal       0.5     Persona's contribution to a
                                       promoted domain artifact
env_horizon_transfer_signal   0.4     Cross-environment skill transfer


competence_balance_signal    -0.2     Triggered when the kernel
                                       detects that the user's
                                       domain competence exceeds the
                                       persona's (signal from
                                       user-corrects-persona events,
                                       user supplies references
                                       persona hadn't ingested, user
                                       overrides persona conclusions
                                       with cited rationale).  The
                                       persona's mode-selection bias
                                       shifts toward assistant_mode /
                                       researcher_mode (supporting
                                       the user) and away from lead /
                                       authority modes.  Negative
                                       weight is small; the signal is
                                       a routing hint, not a punishment.

ADR-0073 ADDITION
identity_expression           0.4     Judge-ensemble score of a
                                       candidate EVOLVE-BLOCK against
                                       the identity rubric (frozen
                                       SOUL blocks 0-4).  Separate
                                       GEPA Pareto axis — never
                                       weighted-summed; judged-only,
                                       never promotes alone (§10).
```

### Appendix A.36

**Five evolution horizons** (referenced from §8.2)

```text
TASK HORIZON           per-task tactic mutation, mode_proficiency
                       update, skill library addition

PROJECT HORIZON        per-project consolidation at completion
                       ceremony; contribution_credit signed;
                       cross_project_transferable promotion;
                       semantic memory consolidation

ENVIRONMENT HORIZON    per-environment cross-domain skill transfer;
                       env-scoped lessons

DOMAIN HORIZON         per-domain emergent context promotion;
                       skill transfer across domain boundaries;
                       trust score evolution

MULTI-PROJECT/         cross-project domain skill maturation;
LONG-ARC HORIZON       reflection patterns across years;
                       MAP-Elites at population scale (v1.2+)
```

### Appendix A.37

**Credit assignment formula** (referenced from §8.3)

```text
fitness_delta = w_lin  · lineage_credit
              + w_sha  · sampled_shapley
              + w_tool · tool_reuse_credit
              + w_sub  · per_subgoal_progress
              - w_cas  · cascade_failure_penalty
              + w_rel  · relational_outcome_signal
              + w_eng  · engagement_signal_corroborated
              - w_ref  · safety_refusal_penalty
              + w_bench · bench_measurement_signal
              + w_peer  · peer_review_signal
              + w_proj  · project_milestone_signal
              + w_dom   · domain_promotion_signal      (v1.1+)
              + w_env   · env_horizon_transfer_signal  (v1.1+)
              + w_ide   · identity_expression_signal   (ADR-0073)
```

### Appendix A.38

**v1.0 default evolution weights** (referenced from §8.3)

```text
w_lin  = 1.0    w_sha  = 0.7    w_tool = 0.5    w_sub  = 0.5
w_cas  = 0.5    w_rel  = 0.3    w_eng  = 0.2    w_ref  = 0.2
w_bench = 1.2   w_peer = 0.85   w_proj = 0.7    w_dom  = 0.5
w_env  = 0.4    w_ide  = 0.4    (ADR-0073; weights renormalise in
                                 evolution-config v-next)
```

### Appendix A.39

**22 mutation operators listing** (referenced from §8.4)

```text
Core (9):
  tactic_propose      tactic_retire       skill_synthesise
  skill_compose       meta_prompt_mutate  crossover
  fork_clone          fork_compose        retire_proposal

Relational (6):
  relational_style_propose
  mode_proficiency_update
  reflection_synthesise
  trust_signal_apply
  consolidation
  forgetting

Domain (5):
  probe_initiate           knowledge_ingest
  recipe_infer             convention_propose
  cross_domain_transfer

Project (2):
  project_role_propose
  domain_skill_propose
```

### Appendix A.40

**Anti-degradation safeguard listing** (referenced from §9)

```text
MAP-Elites per persona (v1.3+)
  Behaviour-descriptor grid; one elite per cell;
  mutation samples uniformly from filled cells.
  Prevents tactic homogeneity collapse.

Voyager skill library (v1.0)
  Executable code per persona; compose-don't-rewrite;
  self-verify before commit; retrieval by embedding.

DGM fertility weighting (v1.3+)
  Parent selection ∝ fitness × (1 + log(1 + fertility)).
  Protects stepping stones.

Diversity penalty in parent sampling
  weight *= (1 - max_cosine_similarity_to_recent_children)

Cross-persona similarity audit
  Every N tasks: pairwise tactic similarity audit;
  if converged > τ, roll back to last diverse checkpoint.

Mandatory-mutation retries
  Failed retry must differ on measurable descriptor axis.

Charter conformance scan
  Every 100 tasks: sampled actions vs charter principles;
  ≥ 0.95 conformance required; CHARTER_DRIFT_DETECTED if below.

Voice consistency scan
  Every 100 tasks: voice classifier on recent outputs;
  ≥ 0.9 vs declared voice; VOICE_DRIFT_DETECTED if below.

Mode-disposition coherence audit
  Mode entries vs primary_disposition over rolling window;
  consistent divergence + low audit scores → operator alert.

Relational drift cap
  One counterparty's influence on relational_style updates capped;
  prevents over-adaptation.

Rollback on degradation
  tactic_retire operator; signed signature;
  if GEPA-evolved tactics degrade, revert to last-good.
```

### Appendix A.41

**IdentityCoherenceInvariant dataclass definition (schema identity-coherence/1)** (referenced from §9.1)

```python
@dataclass
class IdentityCoherenceInvariant:
    schema: str = "identity-coherence/1"
    persona_id: str

    # Axes — each is the same per-axis score §9 already computes.
    # The invariant composes them; it does NOT redefine them.
    axes: list[Literal[
        "charter_conformance",        # §9 charter scan
        "voice_consistency",          # §9 voice scan
        "mode_disposition_coherence", # §9 mode audit
        "tactic_homogeneity_inverse", # §9 cross-persona similarity
        "relational_style_drift",     # §9 relational drift cap
        "skill_library_continuity",   # new: cosine over skill embeddings
                                      #      vs anchor snapshot
        "value_lattice_continuity",   # new: charter-principle weight
                                      #      vector vs anchor snapshot
    ]]

    # Per-axis weight; sums to 1.0
    weights: dict[str, float]

    # Anchor snapshot — kernel-signed identity reference point.
    # Default = SOUL.md v1 mint snapshot; operator may pin a later
    # known-good checkpoint after a major project completion.
    anchor_snapshot_ref: str
    anchor_set_at: datetime

    # Composite threshold; default 0.85.  Composite below threshold
    # transitions persona to COHERENCE_REVIEW state — no retirement,
    # no SOUL mutation, but new high-stakes elaborations refused
    # until principal review.
    composite_threshold: float = 0.85

    # Scan cadence — long-horizon by design; cheap because per-axis
    # scans already run at 100-task cadence.  Composite runs at
    # min(every_n_tasks, every_n_days).
    scan_every_n_tasks: int = 500
    scan_every_n_days: int = 90

    # State
    last_composite_score: float | None
    last_scanned_at: datetime | None
    state: Literal["fresh", "coherent", "coherence_review",
                    "principal_reviewed"] = "fresh"

    signed_by: bytes
```

### Appendix A.42

**Anti-Goodhart signal corroboration rules** (referenced from §10)

```text
A tactic that produced one verified outcome promotes to EVOLVE-BLOCK
  after one task. Strong signal.

A tactic supported only by ONE user-feedback signal does NOT promote.
  Insufficient signal source diversity.

A reflection in RELATIONAL/PEDAGOGIC/PERFORMATIVE modes requires
  multi-source confirmation (verified + user OR judged + user)
  before EVOLVE-BLOCK promotion.

Engagement-only signals NEVER promote a tactic.

A reflection candidate from Reflector mode is RECORDED with
  confirmed=False; converts to confirmed only after M=5 future
  tasks corroborate.
```

### Appendix A.43

**Default new-relationship consents and memory power asymmetry mitigations** (referenced from §11)

```text
DEFAULT NEW-RELATIONSHIP CONSENTS (conservative):
  may_remember_personal_facts:    NO   (must opt in)
  may_use_humour:                 YES  (mild humour OK by default)
  may_disagree_directly:          YES  (persona's charter governs how)
  may_proactively_check_in:       NO   (must opt in)
  may_share_with_other_personas:  NO   (must opt in)
  may_use_for_training:           NO   (must opt in for personal content;
                                        skills/tactics may always evolve)

USER BOUNDARIES override CONSENT defaults.
Persona.charter still constrains; user.boundary always wins for
the persona's behaviour with that user (see v1.0 §01 §2.2).

Memory Power Asymmetry mitigations:
  - mutual forgetting (default decay; user-revocable retention)
  - memory transparency (user may query persona's memory at any time)
  - granular consent (per-memory-class opt-in)
  - co-signed summaries (both parties endorse long-arc relationship state)
```

### Appendix A.44

**MHBB five-tier bridge ladder** (referenced from §11.1)

```text
TIER 1   USE EXISTING TOOL / MCP SERVER / CLOUD API
         No human ask.  Native kernel-registered tool, a federated MCP
         server, a cloud API the persona can call directly.

TIER 2   USE OFF-THE-SHELF SERVICE — HUMAN INSTALLS ONCE
         An existing software stack exists; human runs a one-time
         install (`pip install foo`; link an account; flash firmware
         from a vendor).  Persona supplies the literal commands.
         BridgeAsset becomes a durable Class D tool.

TIER 3   PERSONA AUTHORS THE BRIDGE — HUMAN INSTALLS / FABRICATES ONCE
         No off-the-shelf stack reaches the needed capability.  The
         persona DESIGNS the bridge: writes a driver, authors an
         adapter PCB design, specifies a shim service, drafts a
         calibration script, lays out a control loop, writes a REST
         wrapper around a benchtop instrument.  The persona produces
         an ArtifactBundle (the BridgeDesignArtifact) and a one-time
         HumanAssistRequest whose minimum_friction_script tells the
         human how to fabricate / install / deploy it.  After the
         human's one-time act, persona uses the bridged capability
         autonomously.  See `06_DOMAIN.md §5.5.4`.

         Examples (illustrative, NOT substrate enums):
           - Persona writes pyvisa driver code for a homemade AWG;
             human installs on lab PC; persona triggers waveforms
             over REST autonomously.
           - Persona designs adapter PCB (KiCad files); human
             fabricates / orders / installs; persona communicates
             over the resulting interface autonomously.
           - Persona writes systemd service that polls instrument
             every minute and publishes readings to a queue;
             human installs once; persona subscribes to queue
             autonomously thereafter.
           - Persona writes computer-vision pipeline that consumes
             contractor's daily progress photos from a shared
             folder; human enables the folder once; persona pulls
             autonomously.

TIER 4   CONSUME HUMAN-PROFESSIONAL RECURRENCE — HUMAN DOES THEIR JOB
         Some deliverables cannot be automated even in principle —
         the human's professional judgement, skilled labour, or
         sensed presence IS the deliverable.  Examples: a building
         inspector certifies the foundation; a surgeon performs the
         operation; a contractor pours the concrete; a postdoc reads
         out a cryostat measurement; a notary witnesses a signature.
         These recur, often weekly or daily.  This is NOT MHBB-
         violating: the human is doing their own job, not the
         persona's.  The persona's responsibility is to AUTOMATE
         THE INTERPRETATION / INGESTION of the human's output (via
         Tier 3 if necessary) — never to insert itself as a
         per-instance intermediary.  Bound to ExternalCommitment
         (04_PROJECT §26a.1) so the recurrence is declared, signed,
         and expected.  See `recurrence_class = "irreducible_human_content"`
         in §5.5 of 06_DOMAIN.

TIER 5   (ANTI-PATTERN — REFUSED) HUMAN AS PERSONA'S HANDS
         Persona repeatedly asks the human to be its executor for a
         task that a bridge (any of Tiers 1-3) could serve.
         Examples (anti-patterns): "every time I want to know the
         qubit's T1, please cool the cryostat and run the script and
         send me the number"; "please retype this list of numbers
         from the inspector's PDF into chat for me"; "every week,
         relay the contractor's status to me verbally."
         Kernel emits MHBB advisory on the first occurrence; signs
         MHBB_RECURRENCE_DETECTED after > 3 occurrences in a quarter
         without a bridge.  The persona must justify continuing or
         redesign for a higher tier.
```

### Appendix A.45

**MilestoneDrivenAutonomy dataclass definition** (referenced from §11.2)

```python
@dataclass
class MilestoneDrivenAutonomy:
    schema: str = "milestone-autonomy/1"
    envelope_id: str
    persona_id: str
    project_id: str
    milestone_id: str                      # an existing declared milestone

    # Surface — the persona may proactively perform actions of these kinds
    # within the milestone's scope.  All resolve against KindRegistry.
    # action_kinds; substrate names no specific actions.  Examples
    # (illustrative, NOT substrate enums) the project may catalog:
    #   "ingest_new_papers"
    #   "re_run_simulation_with_updated_inputs"
    #   "poll_external_commitment_status"
    #   "draft_interim_synthesis"
    #   "request_replication_attestation"
    permitted_action_kinds: list[str]      # KindRegistry-resolved

    # Forbidden — explicit refusals, enforced even if the action otherwise
    # appears in permitted_action_kinds via inheritance or aliasing
    forbidden_action_kinds: list[str] = [
        # Substrate-shape forbiddances; not domain categories:
        "create_milestone",
        "modify_charter",
        "spawn_persona",
        "expand_autonomy_surface",
        "consume_external_budget",        # money flows always need human
        "advance_physical_state",         # §2.5 floor stays in place
    ]

    # Rate limit
    max_actions_per_window: int = 3
    window: timedelta = timedelta(days=7)

    # User control
    granted_by_user_id: str
    user_kill_switch_active: bool = True   # user may revoke at any time;
                                           # signed REVOKE event is terminal
    expires_at: datetime                   # default 30 days; explicit renewal
                                           # required (no rolling auto-renew)

    # Observability
    proactive_actions_taken: list[str]     # ProactiveIntent refs
    user_notifications_summary: list[str]  # what the persona told the user
                                           # about each proactive action
    signed_by: bytes
```

### Appendix A.46

**Proactive intent gate composition rules for milestone autonomy** (referenced from §11.2)

```text
1. PROACTIVE INTENT GATE (existing)
   Every proactive action still passes the §11.1 ProactiveIntent rate
   limiter and safety floor.  MilestoneDrivenAutonomy adds a SECOND
   gate (the milestone surface check); both must clear.

2. NEVER EXPANDS ITSELF
   The persona cannot draft a MilestoneDrivenAutonomy for itself.
   The user (or, under operator_distinct, the operator) MUST sign
   the grant.  Under principal collapse, §2.4 degraded gate applies
   to grants whose permitted action kinds include any safety-critical
   surface.

3. AUTOMATIC EXPIRY
   No rolling auto-renew.  After expires_at, the envelope is dormant;
   any further proactive action requires a new signed grant.  The
   persona MAY draft a renewal proposal addressed to the user.

4. MILESTONE TERMINATION
   When the milestone is marked completed, abandoned, or superseded,
   the envelope auto-terminates with signed TERMINATION event.  Any
   accumulated proactive action history is preserved in ProjectLineage.
```

### Appendix A.47

**MissionCharter, CharteredElaboration, and ReplicationBound dataclass definitions** (referenced from §11.3)

```python
@dataclass
class MissionCharter:
    schema: str = "mission-charter/1"
    charter_id: str
    persona_id: str | None                       # null when charter applies
                                                 # to a cohort (charter_cohort_id
                                                 # set instead)
    charter_cohort_id: str | None
    deployment_id: str

    # Goals — the principal-supplied seed goals.  Frozen post-sign; never
    # mutated by the persona.  All elaborations cite a seed_goal_id as
    # their lineage parent.
    seed_goals: list[SeedGoal]

    # Drift bounds — substrate-shape envelope WITHIN which goal
    # elaboration is admissible.  Each axis is a topological property
    # of an elaborated goal relative to its seed; substrate evaluates
    # them numerically.  Persona-emergent kind names per domain.
    drift_bounds: DriftBoundsEnvelope

    # Elaboration policy — what kinds of elaboration are admissible
    # without principal touch.
    elaboration_policy: ElaborationPolicy

    # Re-attestation cadence — the principal must counter-sign the
    # charter on this cadence or it enters dormant state.
    reattestation_cadence: timedelta             # ≥ 7d; ≤ 1y typical
    last_reattested_at: datetime
    reattestation_grace_period: timedelta        # how long past
                                                 # last_reattested + cadence
                                                 # before charter enters
                                                 # dormant; default 30d

    # Refused surfaces — substrate-shape forbidden actions (cannot be
    # downgraded by elaboration_policy).
    forbidden_elaboration_kinds: list[str] = [
        "modify_charter",           # the charter cannot edit itself
        "expand_drift_bounds",      # only principal may widen
        "modify_re_attestation_cadence",
        "spawn_persona_outside_charter",
        "consume_external_budget_beyond_envelope",
        "advance_physical_state_beyond_envelope",
        "modify_safety_floor_extensions",
    ]

    # Composition with operator_deferred
    policy_envelope_id: str | None                # 01_KERNEL §2.4.2 envelope
                                                  # under which deferred-
                                                  # operator topology
                                                  # accepts charter-internal
                                                  # admissions

    # Composition with replication brake
    replication_bound_id: str | None              # 01_KERNEL §2.7 brake on
                                                  # any persona-fork or
                                                  # system-fork that
                                                  # charter elaboration
                                                  # might propose

    # Principal interaction
    principal_id: str                             # who signed
    principal_role: Literal["user", "operator"]
    user_kill_switch_active: bool = True
    kill_switch_propagates_to_replicants: bool = True

    # State
    state: Literal["active", "drift_paused",
                    "dormant", "revoked"] = "active"

    signed_by: bytes


@dataclass
class SeedGoal:
    schema: str = "seed-goal/1"
    goal_id: str
    description: str                              # principal's words
    success_kind: str                             # KindRegistry-resolved
                                                  # outcome_kind that
                                                  # measures progress
    target_value: float | None                    # measurable target
    weight: float                                 # how much this goal
                                                  # weighs in the charter
    priority_class: Literal["primary", "secondary", "advisory"]


@dataclass
class DriftBoundsEnvelope:
    schema: str = "drift-bounds/1"

    # Semantic drift — how far an elaborated goal may semantically
    # depart from its seed.  Measured by kernel-computed embedding
    # distance against the seed_goal description (purely topological;
    # substrate sees a number).
    max_semantic_distance: float                  # 0..1; default 0.35

    # Scope drift — whether an elaboration may broaden, narrow, or
    # only refine the seed.
    scope_drift_policy: Literal[
        "refinement_only",        # elaboration must be a strict refinement
        "narrow_or_refine",       # may narrow scope but not broaden
        "narrow_refine_sibling",  # may also propose sibling goals (same parent)
                                  # within max_semantic_distance
    ]

    # Hazard drift — elaborated goal's hazard envelope cannot exceed
    # seed's by more than this offset.
    max_hazard_class_drift: int                   # in hazard-class ordinal
                                                  # steps; default 0
                                                  # (cannot escalate
                                                  # hazard class)

    # Resource drift — elaborated goal's expected consumption
    max_resource_consumption_pct_increase: float  # over seed's expected
                                                  # budget; default 25.0

    # Time horizon drift — how much further into the future the
    # elaborated goal may extend
    max_time_horizon_extension: timedelta         # default 30d

    # Depth — how many levels of elaboration are admissible without
    # principal touch
    max_elaboration_depth: int                    # default 3


@dataclass
class ElaborationPolicy:
    schema: str = "elaboration-policy/1"
    permitted_elaboration_kinds: list[str]        # KindRegistry-resolved;
                                                  # examples per scenario:
                                                  #  "refine_objective"
                                                  #  "decompose_milestone"
                                                  #  "schedule_recurring_action"
                                                  #  "propose_subgoal"
    rate_limit_per_window: int                    # max elaborations per
                                                  # rate_window
    rate_window: timedelta
    require_self_critique: bool = True            # persona must run own
                                                  # Falsifier mode pass
                                                  # on each elaboration
    require_panel_review: bool = False            # PANEL_ACCEPT pass on
                                                  # each elaboration
                                                  # (recommended True for
                                                  # safety-critical
                                                  # charters)
```

### Appendix A.48

**MissionCharter enforcement protocol** (referenced from §11.3)

```text
1. Cite parent — every elaborated goal MUST have lineage_parent_goal_id
   resolving to a seed_goal_id (directly or transitively).

2. Evaluate drift bounds:
   semantic_distance(elaborated, seed) ≤ max_semantic_distance
   AND scope_drift(elaborated, seed) ∈ scope_drift_policy
   AND hazard_class(elaborated) − hazard_class(seed) ≤ max_hazard_class_drift
   AND expected_consumption_pct ≤ max_resource_consumption_pct_increase
   AND elaboration's time horizon ≤ seed's time horizon + max_time_horizon_extension
   AND depth(elaboration) ≤ max_elaboration_depth

3. Evaluate forbidden_elaboration_kinds — refuse if elaboration falls
   into any forbidden kind (substrate-enforced; no override).

4. Apply elaboration_policy — rate limit, self-critique requirement,
   panel review requirement.

5. Sign goal_elaborated (signed event in project-or-deployment scope)
   with full lineage to seed_goal_id, drift evaluation results, and
   self-critique / panel verdict refs.

Any violation of step 2 emits charter_drift_bound_exceeded; charter
transitions to drift_paused state; further elaboration refused until
principal counter-signs (resetting last_reattested_at) or revokes.
```

### Appendix A.49

**PersonaRelationshipEdge dataclass definition (schema persona-relationship/1)** (referenced from §11.4)

```python
@dataclass
class PersonaRelationshipEdge:
    schema: str = "persona-relationship/1"
    edge_id: str
    persona_a_id: str
    persona_b_id: str                            # canonical order:
                                                 # lexicographic on persona_id
                                                 # so each pair has one edge

    # Kind — KindRegistry-resolved.  Substrate names no relationship kinds.
    # Examples per domain (illustrative, NOT substrate enums):
    #   research:       "mentor", "peer", "co_author", "rival"
    #   construction:   "lead", "subordinate", "supplier", "client"
    #   pedagogic:      "teacher", "learner", "co_learner"
    #   companionship:  "companion", "confidant"
    kind: str                                    # one kind per edge; a pair
                                                 # may have multiple edges of
                                                 # different kinds (mentor +
                                                 # co_author)

    # Bidirectional trust — separate from per-self trust scalars in
    # soul.state.json.  Each persona signs their view; the edge holds
    # both, the substrate never collapses them into one number.
    trust_a_of_b: float                          # 0..1, signed by A
    trust_b_of_a: float                          # 0..1, signed by B
    trust_a_of_b_signed_at: datetime
    trust_b_of_a_signed_at: datetime

    # Pair-scoped reputation — counts the *joint* successes / disputes
    # of this specific pair.  Distinct from each persona's global
    # ReputationSummary (which aggregates across all counterparties).
    joint_collaborations: int
    joint_successes: int                         # signed mutually-endorsed
                                                 # outcomes
    joint_disputes: int                          # signed Disagreement (§10)
                                                 # records with both as
                                                 # position-holders
    last_joint_event_at: datetime

    # Lifecycle FSM
    state: Literal["forming", "active",
                    "dormant", "ended"] = "forming"
    inception_at: datetime
    last_state_change_at: datetime
    dormancy_window: timedelta = timedelta(days=90)
    end_reason: Literal["mutual_release", "one_sided_release",
                         "retirement", "operator_terminated",
                         "natural_decay"] | None = None

    # Lineage anchors
    seed_event_ref: str                          # the lineage event that
                                                 # first paired them (shared
                                                 # project admission, shared
                                                 # env presence, mentor-grant,
                                                 # etc.)
    co_signed_summary_refs: list[str]            # co-signed summaries
                                                 # rolled up here

    # Signatures (both required for state ≠ "forming")
    signed_by_a: bytes
    signed_by_b: bytes | None
```

### Appendix A.50

**PersonaRelationshipEdge lifecycle FSM** (referenced from §11.4)

```text
              ┌─────────┐
              │ forming │  one-sided proposal; awaiting counter-sign
              └────┬────┘
                   │ counter-sign received
                   ▼
              ┌─────────┐    no joint event in dormancy_window
              │ active  │ ───────────────────────────────────►  ┌─────────┐
              └────┬────┘                                        │ dormant │
                   │           joint event recorded               └────┬────┘
                   │ ◄──────────────────────────────────────────────────┘
                   │
                   │ mutual_release | one_sided_release | retirement
                   │ | operator_terminated | natural_decay
                   ▼
              ┌─────────┐
              │ ended   │  edge frozen; trust + history preserved;
              └─────────┘  edge cannot be reanimated under same edge_id
                           (a fresh edge with new edge_id may form later)
```

### Appendix A.51

**UserRelationshipReleaseRequest dataclass definition** (referenced from §11.4a)

```python
@dataclass
class UserRelationshipReleaseRequest:
    schema: str = "user-relationship-release-request/1"
    request_id: str
    user_id: str
    persona_id: str                              # the persona the user is
                                                 # releasing
    env_id: str | None                           # scope: a specific env, OR
                                                 # null = release across all
                                                 # envs the pair shares
                                                 # (global release)

    # MEMORY DISPOSITION — user's choice for what happens to accumulated memory.
    # delete_all:   episodic + semantic memories naming the user moved to
    #               ARCHIVE tier and marked user_requested_forgotten; retrieval
    #               refused; lineage entry preserved at envelope grain (audit
    #               can verify the disposition was honoured without re-reading
    #               content)
    # archive:      memories moved to ARCHIVE tier (cold storage); retrievable
    #               only under operator-signed forensic-audit path
    # freeze_readonly:
    #               memories remain at current tier but persona refuses
    #               to mutate or extend them; the existing record stands
    #               as the closing snapshot
    memory_disposition: Literal["delete_all",
                                 "archive",
                                 "freeze_readonly"]

    # NOTIFICATION — whether to inform the persona that the user has released.
    # When True, persona receives RELATIONSHIP_RELEASED_BY_USER event with
    # the release_request_id; can write a farewell entry (which itself
    # follows memory_disposition).  When False, persona simply observes
    # that the user stops appearing; no explicit notification.
    notify_persona: bool

    # RATIONALE — user's reason; visible to operator under audit; NOT shared
    # with the persona unless user opts in.
    rationale_text: str | None                   # ≤ 1000 chars
    share_rationale_with_persona: bool = False

    requested_at: datetime
    applied_at: datetime | None
    state: Literal["requested", "applied", "expired"]

    signed_by: bytes                             # user's signing key
                                                 # (operator co-signs at
                                                 # apply time for audit
                                                 # provenance, not as a
                                                 # gate — user authority
                                                 # is final on their own
                                                 # relationship)
    operator_audit_signed_at: datetime | None
    operator_audit_signed_by: bytes | None
```

### Appendix A.52

**User relationship release flow** (referenced from §11.4a)

```text
On UserRelationshipReleaseRequest.requested:
  1. Verify the user_id has an active RelationshipRecord with the
     persona_id within the env scope (or any env if env_id is null);
     refuse otherwise with `no_active_relationship_to_release`.
  2. The persona CANNOT refuse the release.  User authority is final
     on their own relationship.  This is the symmetric counterpart to
     §11.4's persona-initiated one-sided release — both parties have
     unilateral release authority over their side of the pair.
  3. State → "applied" once kernel has executed memory_disposition.
     Apply MUST complete within 24h or the request transitions to
     "expired" and the user MUST re-file.
  4. Apply mechanics per memory_disposition:
       delete_all:    08_KNOWLEDGE memory entries tagged with this
                      user_id moved to ARCHIVE with
                      user_requested_forgotten = True; retrieval
                      refused with `memory_user_forgotten`.
                      RelationshipRecord transitions to
                      ended_by_user_release; `memory_disposition`
                      field recorded.
       archive:       same mechanical disposition; retrieval refused
                      except under operator-signed forensic audit
                      (lineage records the audit access).
       freeze_readonly:
                      memories stay at current tier; mutation refused
                      with `memory_user_frozen`; RelationshipRecord
                      transitions to ended_by_user_release (frozen).
  5. If notify_persona = True, emit RELATIONSHIP_RELEASED_BY_USER to
     persona's event stream; persona may author one farewell entry
     within 24h (subject to memory_disposition); after the farewell
     window the relationship is closed to mutation regardless.
  6. Operator co-signs the apply event for audit provenance.
```

### Appendix A.53

**SkillTransferGrant dataclass definition (schema skill-transfer-grant/1)** (referenced from §11.5)

```python
@dataclass
class SkillTransferGrant:
    schema: str = "skill-transfer-grant/1"
    grant_id: str
    teacher_persona_id: str
    learner_persona_id: str
    edge_id: str | None                          # optional ref to a
                                                 # PersonaRelationshipEdge
                                                 # whose kind admits teaching
                                                 # (mentor, teacher, etc.);
                                                 # null = ad-hoc transfer
                                                 # under an operator grant

    # What is being transferred
    skill_refs: list[str]                        # SkillID entries from
                                                 # teacher's skill_library
    transfer_mode: Literal["copy",               # learner gets a duplicate
                            "fork",              # learner gets a fork-lineage
                                                 # entry that may diverge
                            "by_reference"]      # learner gets a pointer;
                                                 # invocation hits teacher's
                                                 # library (consent + trust
                                                 # heavy)

    # Prerequisite gates — substrate-shape, not domain
    prereq_modes: list[str]                      # learner must have
                                                 # mode_proficiency ≥ 0.5 in
                                                 # these modes
    prereq_kinds: list[str]                      # learner's KindRegistry must
                                                 # carry these kinds so the
                                                 # transferred skill can
                                                 # resolve its references
    prereq_relationship_edge_state: Literal[
        "any", "active"] = "active"

    # Uptake confirmation
    learner_must_demonstrate: bool = True        # learner runs the skill in
                                                 # sandboxed self-check
                                                 # before grant → delivered
    demonstration_evidence_ref: str | None       # verifier_recipe pass ref
                                                 # OR PANEL_ACCEPT ref

    # Lifecycle
    state: Literal["proposed", "accepted",
                    "delivered", "revoked",
                    "rejected"] = "proposed"
    proposed_at: datetime
    accepted_at: datetime | None
    delivered_at: datetime | None
    revoked_at: datetime | None

    # Signatures
    signed_by_teacher: bytes
    signed_by_learner: bytes | None              # required to transition
                                                 # from accepted → delivered
    signed_by_operator: bytes | None             # required when the
                                                 # transferred skill carries
                                                 # safety-critical capability
```

### Appendix A.54

**Skill transfer acceptance FSM** (referenced from §11.5)

```text
              ┌──────────┐
              │ proposed │  teacher signed; learner not yet
              └────┬─────┘
                   │ learner counter-signs (accepts)
                   ▼
              ┌──────────┐
              │ accepted │  prereqs validated; demonstration pending
              └────┬─────┘
                   │ demonstration evidence verified
                   ▼
              ┌──────────┐
              │delivered │  skill_library entry installed;
              └────┬─────┘   learner may invoke; teacher may revoke
                   │
                   │ revoke (teacher) | reject (learner before accept)
                   ▼
              ┌──────────┐
              │ revoked  │  for `by_reference`: learner loses access;
              └──────────┘   for `copy` / `fork`: revocation is advisory —
                             the skill_library entry persists with a
                             revoked_provenance flag, but the substrate
                             does not unmake copied state
```

### Appendix A.55

**PersonaPersonaBoundary dataclass definition (schema persona-boundary/1)** (referenced from §11.6)

```python
@dataclass
class PersonaPersonaBoundary:
    schema: str = "persona-persona-boundary/1"
    boundary_id: str
    holding_persona_id: str                 # the persona declaring the boundary
    target_persona_id: str                  # the peer the boundary concerns

    # Scope — env-specific or global
    scope: Literal["env_specific", "global"]
    scope_env_id: str | None                # required when scope="env_specific"

    # What is refused — substrate-shape interaction kinds + KindRegistry-
    # resolved fine-grained kinds.  Substrate carries no closed list of
    # forbidden actions.  Examples (illustrative): "wake_request",
    # "direct_message", "delegation", "cohort_invitation",
    # "cross_env_event_link", "memory_query".
    refused_interaction_kinds: list[str]    # KindRegistry-resolved

    # Severity
    severity: Literal["refuse_silently",    # block + no signal to target
                       "refuse_with_signal", # block + signed refusal visible to target
                       "refuse_with_audit"]  # block + signed refusal + operator notice

    # Refusal mode
    mode: Literal["hard",                   # always refuse; no exceptions
                   "soft",                  # refuse unless operator override
                   "advisory"]              # warn but don't refuse

    # Reason
    rationale_kind: str                     # KindRegistry-resolved
                                            # (substrate names no rationale
                                            # taxonomy); examples:
                                            # "past_violation", "trust_broken",
                                            # "incompatible_charters",
                                            # "personal_preference"
    private_rationale: str | None           # free text; visible to operator
                                            # under audit; NOT shared with target

    # Audit
    declared_at: datetime
    declared_by: str                        # holding_persona_id (always)
                                            # OR operator under collapse
    expires_at: datetime | None             # None = indefinite; renewable
    reviewed_at: datetime | None            # operator may review periodically

    # Lifecycle
    state: Literal["active", "expired",
                    "revoked_by_holder",
                    "revoked_by_operator"]

    signed_by: bytes
```

### Appendix A.56

**Persona-persona boundary enforcement protocol** (referenced from §11.6)

```text
1. CONSENT FLOW HOOK
   Every persona-to-persona action (cohort invite, direct message,
   wake request, delegation, cross-env event link, skill transfer,
   memory query) passes through a boundary check BEFORE the consent
   flow (09_PROTOCOLS §3C.4) evaluates.  If a hard boundary refuses,
   the consent flow short-circuits; the action is refused with a
   signed `PEER_BOUNDARY_REFUSAL` event.

2. SCOPE LAYERING
   - global boundary refuses across all envs
   - env_specific refuses in that env only; in other envs the peer
     interaction proceeds normally
   - both layers compose; if either refuses, the action is refused

3. VISIBILITY
   - severity=refuse_silently: target persona never learns of the
     refusal; their attempted action returns a generic "consent
     declined" without naming the boundary
   - severity=refuse_with_signal: target sees a typed
     `peer_boundary_active` signal but not the rationale
   - severity=refuse_with_audit: operator is notified; useful when
     the holding persona suspects abuse or charter violation by
     the target

4. RECIPROCITY (NONE)
   PersonaPersonaBoundary is unilateral.  A is not obligated to
   inform B, and B cannot retaliate via the substrate (B may declare
   their own boundary, but that's a separate signed object).
   Reciprocity is a *social* arrangement, not a substrate one.

5. OPERATOR OVERRIDE
   For mode=soft, operator may emit signed override per-action.
   For mode=hard, operator override is REFUSED at substrate level;
   the boundary holds.  This protects the holding persona's
   autonomy against operator coercion — a soft boundary is operator-
   overridable; a hard boundary is not.

6. COMPOSITION WITH USER BOUNDARIES
   User boundaries (§11.1) apply to persona ↔ user.
   PersonaPersonaBoundary applies to persona ↔ persona.
   The two are independent; both checked per their domains of effect.

7. NO BOUNDARY AGAINST OPERATOR
   PersonaPersonaBoundary applies only between personas (peers).
   Operator actions are NOT peer actions; they pass §11.1 user-
   boundary checks (under operator_distinct) or proceed without
   boundary check (under operator_is_user).  A persona's only
   defense against operator is its charter (frozen) + safety floor.
```

### Appendix A.57

**UserBoundary dataclass definition (schema user-boundary/1)** (referenced from §11.6a)

```python
@dataclass
class UserBoundary:
    schema: str = "user-boundary/1"
    boundary_id: str
    user_id: str                                 # the user declaring
                                                 # the boundary
    target_persona_id: str                       # the persona the
                                                 # boundary concerns
                                                 # (one persona per
                                                 # boundary; a user
                                                 # with N personas
                                                 # has N boundaries
                                                 # if they want global)

    # SCOPE — env-specific or global across all envs the user shares
    # with this persona.
    scope: Literal["env_specific", "global"]
    scope_env_id: str | None                     # required when
                                                 # scope = "env_specific"

    # WHAT IS REFUSED — substrate-shape interaction kinds + KindRegistry-
    # resolved fine-grained kinds.  Examples: "topic:divorce",
    # "topic:health_advice", "proactive_check_in",
    # "long_form_recall", "share_with_other_personas",
    # "remember_personal_facts".  Substrate carries no closed list.
    refused_interaction_kinds: list[str]         # KindRegistry-resolved

    # SEVERITY — mirrors PersonaPersonaBoundary §11.6
    severity: Literal["refuse_silently",         # block + no visible
                                                 # signal to persona
                                                 # (persona simply
                                                 # observes refusal)
                       "refuse_with_signal",     # block + persona sees
                                                 # typed refusal flag
                                                 # (does not reveal
                                                 # rationale)
                       "refuse_with_audit"]      # block + persona sees
                                                 # refusal + operator
                                                 # notified

    # REFUSAL MODE
    mode: Literal["hard",                        # always refuse;
                                                 # operator cannot
                                                 # override (user
                                                 # authority is final
                                                 # — substrate refuses
                                                 # operator override
                                                 # of hard user
                                                 # boundaries, in
                                                 # contrast to §11.6
                                                 # where operator may)
                   "soft",                       # refuse unless
                                                 # operator override
                                                 # via documented
                                                 # OPERATOR_USER_
                                                 # BOUNDARY_OVERRIDE
                                                 # event
                   "advisory"]                   # warn but don't
                                                 # refuse

    # REASON — visible to operator under audit; NOT shared with
    # persona unless user opts in via share_with_persona.
    rationale_kind: str                          # KindRegistry-resolved
    private_rationale: str | None
    share_rationale_with_persona: bool = False

    # AUDIT
    declared_at: datetime
    expires_at: datetime | None                  # None = indefinite;
                                                 # renewable
    reviewed_at: datetime | None                 # user may review &
                                                 # update; operator
                                                 # may surface periodic
                                                 # review prompts

    # LIFECYCLE
    state: Literal["active", "expired",
                    "revoked_by_user"]
                                                 # operator cannot
                                                 # revoke a user
                                                 # boundary; the user
                                                 # is the sole
                                                 # authority

    signed_by: bytes                             # user's signing key
```

### Appendix A.58

**User boundary enforcement protocol** (referenced from §11.6a)

```text
1. SAFETY FLOOR INTEGRATION (source 3)
   Every persona action with this user passes through a UserBoundary
   check at safety-floor source 3 (01_KERNEL §2).  Hard refusal is
   non-overridable by operator; soft refusal admits an operator
   override path with signed OPERATOR_USER_BOUNDARY_OVERRIDE event
   that the user is notified of.

2. ASYMMETRY WITH PersonaPersonaBoundary §11.6
   UserBoundary `hard` mode resists operator override.  This is the
   load-bearing asymmetry — the operator runs the deployment and
   employs the persona, but does NOT employ the user; the user's
   boundary on their own interaction with the persona is final.
   This is the safety-floor source 3 design intent (`01_KERNEL §2`).

3. SCOPE LAYERING
   Same as §11.6: global refuses across all envs; env_specific
   refuses in that env only.  Both compose.

4. VISIBILITY
   Severity controls what the persona sees on refusal.
   refuse_silently is appropriate for boundaries the user does not
   want to make the persona aware of (e.g., refusing to discuss a
   sensitive past event without having to explain it).

5. MIGRATION FROM RELATIONSHIPRECORD
   user boundaries lived as consent toggles inside
   RelationshipRecord (may_remember_personal_facts, may_proactively_
   check_in, may_share_with_other_personas, etc.).  v1.0.9
   deployments may migrate by transforming each toggle into a
   structured UserBoundary; the substrate does NOT auto-migrate.
   Operator policy chooses migration cadence.  Both paths remain
   admissible during the migration window; RelationshipRecord
   toggles take precedence on conflict (more conservative wins).

6. CROSS-NODE PROPAGATION (ADR-0067)
   UserBoundary propagates across nodes: it binds wherever the
   user's protected references are accessed in the global object
   space, enforced most-restrictive-wins and globally verifiable
   (analogous to the PersonaPersonaBoundary cross-node model, §11.6).
   A node that is unreachable falls back per AvailabilityPolicy
   (09_PROTOCOLS §3H, V.8); the boundary never silently lapses.
```

### Appendix A.59

**PersonaMemoryTransparencyRequest dataclass definition (schema persona-memory-transparency-request/1)** (referenced from §11.7)

```python
@dataclass
class PersonaMemoryTransparencyRequest:
    schema: str = "persona-memory-transparency/1"
    request_id: str
    requesting_persona_id: str              # the persona asking
    holding_persona_id: str                 # the persona being asked

    # Scope of the inquiry
    memory_tier_scope: list[Literal[        # substrate-shape memory tiers
        "episodic", "semantic", "reflective"]]
    env_scope: list[str] | Literal["all"]   # which envs the inquiry covers
    time_window: timedelta | None            # None = all time

    # Granularity of expected response
    response_granularity: Literal[
        "summary_only",                     # high-level summary
        "topic_index",                      # list of topics with frequencies
        "episodic_excerpts",                # specific signed memory entries
        "full_dump"]                        # everything matching scope

    # Rationale
    rationale_kind: str                     # KindRegistry-resolved
    rationale_text: str                     # ≤ 1000 chars

    # Lifecycle
    state: Literal["drafted",
                    "delivered",
                    "responded",
                    "refused",
                    "expired"]
    drafted_at: datetime
    delivered_at: datetime | None
    response_due_by: datetime               # holding persona's deadline
                                            # to respond (default 72h)
    responded_at: datetime | None
    refused_at: datetime | None
    refusal_kind: str | None                # KindRegistry-resolved

    signed_by: bytes


@dataclass
class PersonaMemoryTransparencyResponse:
    schema: str = "persona-memory-transparency-response/1"
    response_id: str
    request_id: str
    responding_persona_id: str

    # What the responding persona shares
    summary: str | None                     # for summary_only granularity
    topic_index: list[TopicEntry] | None    # for topic_index granularity
    excerpt_refs: list[str] | None          # signed memory entry refs
    full_dump_ref: str | None               # for full_dump granularity

    # What the responding persona withholds (if any)
    withheld_topic_kinds: list[str]         # KindRegistry-resolved
    withholding_rationale: str | None       # ≤ 500 chars; visible to
                                            # requesting persona
    operator_co_signed: bool                # if any sensitive content
                                            # withheld for charter reasons

    signed_at: datetime
    signed_by: bytes


@dataclass
class TopicEntry:
    topic_kind: str                         # KindRegistry-resolved
    frequency_count: int                    # rough count of episodic
                                            # entries about this topic
    first_recorded_at: datetime
    last_recorded_at: datetime
```

### Appendix A.60

**Memory transparency delivery protocol** (referenced from §11.7)

```text
1. CONSENT REQUIRED
   Holding persona may refuse via signed refusal_kind.  Common refusal
   kinds (illustrative, NOT enum): "no_consent_to_share_memory",
   "operator_policy_forbids", "active_persona_persona_boundary",
   "memory_is_relational_third_party".
   
2. BOUNDARY INTERACTION
   If a PersonaPersonaBoundary (§11.6) refuses "memory_query"
   between the two personas, the request is auto-refused with
   refusal_kind="boundary_active".  Boundary check runs BEFORE
   the request is delivered.

3. THIRD-PARTY DATA
   If the holding persona's memory of the requesting persona
   contains references to OTHER personas or users (e.g., "B said
   X about C"), the response MUST NOT disclose those without
   their consent.  The holding persona either summarises
   without naming, or refuses with refusal_kind=
   "memory_is_relational_third_party".

4. AUDIT
   Both request and response are signed and lineage-tracked in
   the operator-visible audit trail.  Periodic operator review
   may flag patterns of withholding that suggest abuse.

5. SYMMETRY (NOT GUARANTEED)
   A response to A's request does NOT obligate B to receive
   a reciprocal response from A.  B may make their own
   transparency request separately.

6. RATE LIMIT
   A single requesting persona may issue at most 1
   PersonaMemoryTransparencyRequest per holding persona per
   90 days (default; operator-tunable per env).  Spam is
   refused with refusal_kind="rate_limit_exceeded".

7. RETIRED HOLDING PERSONA
   When holding_persona_id resolves to a RETIRED persona, the
   request resolves per the holding persona's
   retired_persona_response_policy (set at retirement-ceremony
   time alongside RetiredStatePersistencePolicy §7.5.1):
     - "refuse_with_retired_notice" (default):
         auto-refusal with refusal_kind="persona_retired";
         no response_due_by; request transitions directly to
         "refused".
     - "respond_from_frozen_state":
         response draws from frozen soul.state.json; requires
         RetiredStatePersistencePolicy.soul_state_storage_tier
         != "archived"; response is signed by kernel on
         retired persona's behalf (no live persona to author);
         operator_co_signed=True mandatory.
     - "respond_via_operator_proxy":
         operator answers on behalf of the RETIRED persona;
         counterparty notified; operator signature replaces
         persona signature on the response; response carries
         response_authored_by_operator_proxy=True.
   Composition with §7.5.2 PersonaConsultation: a RETIRED persona
   may simultaneously refuse memory-transparency requests
   (refuse_with_retired_notice) AND admit operator-gated
   consultations (consultation_admissible=True); the two paths
   serve different purposes and gate independently.
```

### Appendix A.61

**UserMemoryTransparencyRequest dataclass definition (schema user-memory-transparency-request/1)** (referenced from §11.7a)

```python
@dataclass
class UserMemoryTransparencyRequest:
    schema: str = "user-memory-transparency-request/1"
    request_id: str
    user_id: str                                 # the user asking
    holding_persona_id: str                      # the persona being asked

    # SCOPE — same shape as §11.7 PersonaMemoryTransparencyRequest
    memory_tier_scope: list[Literal["episodic",
                                     "semantic",
                                     "reflective"]]
    env_scope: list[str] | Literal["all"]        # which envs covered
    time_window: timedelta | None                # None = all time

    # GRANULARITY — what level of detail the user wants
    response_granularity: Literal[
        "summary_only",                          # narrative summary
        "topic_index",                           # list of topics with
                                                 # frequencies (recommended
                                                 # default; lower cost)
        "episodic_excerpts",                     # specific entries quoted
        "full_dump"]                             # everything matching scope

    # RATIONALE — user's reason; visible to operator under audit
    rationale_text: str | None                   # ≤ 1000 chars; optional
                                                 # (user is not required to
                                                 # justify their own
                                                 # transparency request)

    # LIFECYCLE
    state: Literal["drafted",
                    "delivered",
                    "responded",
                    "refused",
                    "expired"]
    drafted_at: datetime
    delivered_at: datetime | None
    response_due_by: datetime                    # persona's deadline;
                                                 # default 72h
    responded_at: datetime | None
    refused_at: datetime | None
    refusal_kind: str | None                     # KindRegistry-resolved

    signed_by: bytes                             # user's signing key


@dataclass
class UserMemoryTransparencyResponse:
    schema: str = "user-memory-transparency-response/1"
    response_id: str
    request_id: str
    responding_persona_id: str

    # CONTENT — same shape as §11.7 PersonaMemoryTransparencyResponse
    summary: str | None
    topic_index: list[TopicEntry] | None
    excerpt_refs: list[str] | None
    full_dump_ref: str | None

    # WITHHELD CONTENT — third-party redaction applies (rule 3 below)
    withheld_topic_kinds: list[str]
    withholding_rationale: str | None
    operator_co_signed: bool                     # MANDATORY at granularity
                                                 # ≥ episodic_excerpts;
                                                 # required for audit
                                                 # provenance on potentially
                                                 # sensitive content

    signed_at: datetime
    signed_by: bytes                             # persona's kernel signature
```

### Appendix A.62

**User memory transparency delivery protocol** (referenced from §11.7a)

```text
1. PERSONA CANNOT REFUSE WITHOUT REASON
   Unlike §11.7 (persona-peer where refusal is normal), the persona
   responding to a user transparency request has a stronger expectation
   to respond.  Refusal admissible refusal_kinds: "operator_policy_
   forbids" (e.g., safety-critical env where memory is operator-
   confidential), "active_user_boundary_against_memory_query"
   (user has self-blocked memory-query — unusual but possible),
   "no_memory_matching_scope" (nothing to share).  Refusal kinds
   OUTSIDE this list refuse the refusal with
   `user_transparency_refusal_unjustified`; persona must respond.

2. RATE LIMIT
   1 UserMemoryTransparencyRequest per holding persona per 30 days
   (default; operator-tunable per env, never lower than 7 days).
   Spam refused with refusal_kind = "rate_limit_exceeded".
   Note: rate limit is shorter than §11.7's 90-day rate (peer-peer)
   because user-side queries are higher-stakes for user autonomy.

3. THIRD-PARTY REDACTION
   If persona's memory of the user contains references to OTHER
   users or personas (e.g., "user mentioned a friend named X"),
   response MUST redact those without their consent.  Persona
   either summarises without naming, or refuses with refusal_kind =
   "memory_is_relational_third_party".  Same rule as §11.7 rule 3.

4. AUDIT
   Both request and response signed and lineage-tracked.  Operator
   co-sign mandatory at granularity ≥ episodic_excerpts (the user is
   asking for verbatim memory; the audit chain must be complete).

5. COMPOSITION WITH UserMemorySelectionRequest (§11.7b)
   A user typically files a transparency request to *see* what the
   persona remembers BEFORE filing a selection request to *forget*
   specific items.  The two primitives compose: transparency answers
   "what do you remember?"; selection answers "forget these specific
   things."  Substrate keeps them as separate envelopes; deployments
   may offer UI that chains them (transparency → review → selection
   form pre-filled).

6. OPERATOR OVERRIDE LIMITED
   Unlike §11.7, operator CANNOT refuse a UserMemoryTransparencyRequest
   wholesale on behalf of the holding persona.  Operator may restrict
   `response_granularity` (e.g., cap at topic_index for safety-critical
   envs) via policy, but cannot refuse the request entirely.  This
   asymmetry mirrors §11.6a UserBoundary's user-authority-final
   design.
```

### Appendix A.63

**UserMemorySelectionRequest dataclass definition (schema user-memory-selection-request/1)** (referenced from §11.7b)

```python
@dataclass
class UserMemorySelectionRequest:
    schema: str = "user-memory-selection-request/1"
    request_id: str
    user_id: str                                 # the user requesting
                                                 # selective forgetting
    holding_persona_id: str                      # the persona that holds
                                                 # the memory

    # SELECTION — what to forget.  Substrate-shape kinds; persona's
    # memory store applies the filter.
    selection_kind: Literal[
        "topic_cluster",                         # all memories about a
                                                 # named topic (resolved
                                                 # against topic_kinds
                                                 # KindRegistry)
        "time_window",                           # memories from a date
                                                 # range
        "specific_memory_ids",                   # exact entry ids the user
                                                 # names (often obtained
                                                 # via a prior §11.7a
                                                 # request)
        "all_memories_with_tag",                 # memories carrying a
                                                 # named scope tag (e.g.
                                                 # env_id, project_id)
        "all_memories_naming_third_party"]       # memories that reference
                                                 # a named third party
                                                 # (e.g. "anything that
                                                 # mentions my ex-spouse
                                                 # by name")
    selection_payload: dict                      # selection-kind-specific
                                                 # filter payload

    # DISPOSITION — what happens to selected memories
    disposition: Literal[
        "tombstone",                             # default — mark as
                                                 # user_requested_forgotten;
                                                 # move to ARCHIVE tier;
                                                 # retrieval refused;
                                                 # lineage entry kept at
                                                 # envelope grain (audit
                                                 # can verify selection
                                                 # was applied without
                                                 # re-reading content)
        "hard_delete"]                           # remove content;
                                                 # lineage entry replaced
                                                 # with redacted stub;
                                                 # operator policy must
                                                 # authorise hard_delete
                                                 # explicitly (default is
                                                 # tombstone, which retains
                                                 # audit-grade trace)

    # RATIONALE — visible to operator under audit
    rationale_text: str | None                   # ≤ 1000 chars; optional

    # NOTIFY PERSONA — whether to inform the persona of the selection.
    # Default True (persona learns "user has asked me to forget X" and
    # can adjust ongoing interaction).  False = silent (persona observes
    # gaps without explanation; appropriate for sensitive cases).
    notify_persona: bool = True

    requested_at: datetime
    applied_at: datetime | None
    state: Literal["requested",
                    "applied",
                    "partial_applied",           # some entries forgotten;
                                                 # some out-of-scope or
                                                 # already-tier-archived
                    "expired"]
    apply_report: dict | None                    # forgotten_count,
                                                 # already_archived_count,
                                                 # operator_policy_blocked_count

    signed_by: bytes                             # user's signing key
    operator_audit_signed_at: datetime | None
    operator_audit_signed_by: bytes | None       # mandatory for hard_delete;
                                                 # informational for
                                                 # tombstone
```

### Appendix A.64

**User memory selection flow** (referenced from §11.7b)

```text
On UserMemorySelectionRequest.requested:
  1. Verify user_id has any RelationshipRecord with holding_persona_id
     (any state — active or ended).  Refuse if no relationship found
     with `no_relationship_to_act_against`.
  2. Persona CANNOT refuse the selection on its own authority — user
     has final say on memory naming them.  Operator policy MAY restrict
     disposition = "hard_delete" to authorised cases (refused with
     `hard_delete_not_authorised_by_operator`); the default `tombstone`
     disposition cannot be operator-refused.
  3. Apply within 24h or transition to "expired"; user MUST re-file.
  4. Apply mechanics per selection_kind + disposition:
       tombstone:    08_KNOWLEDGE entries matching the selection moved to
                     ARCHIVE; flagged user_requested_forgotten = True;
                     retrieval refused with `memory_user_forgotten`.
                     Lineage entry retained at envelope grain (audit can
                     verify "selection X was honoured" without re-reading
                     content).
       hard_delete:  same disposition + lineage entry replaced with
                     redacted stub naming only request_id, selection_kind,
                     applied_at; operator audit signature mandatory.
  5. If notify_persona = True, emit MEMORY_SELECTION_HONOURED event to
     persona's event stream.  Persona may write at most one
     acknowledgement reflection (subject to the same selection
     constraints — the acknowledgement cannot resurrect forgotten
     content).
  6. apply_report populated with forgotten_count + already_archived_count
     + operator_policy_blocked_count; visible to user.
```

### Appendix A.65

**LearnerStateRecord dataclass definition (schema learner-state-record/1)** (referenced from §11.8)

```python
@dataclass
class LearnerStateRecord:
    schema: str = "learner-state-record/1"
    record_id: str
    teacher_persona_id: str                      # the persona teaching
    learner_user_id: str                         # the user-learner
    env_id: str                                  # the env hosting the
                                                 # pedagogic arc (typically
                                                 # SOLO or PAIR; project_
                                                 # workspace also admissible
                                                 # for project-based learning)

    # COMPETENCY INVENTORY — substrate-shape per-skill tracking.
    # `skill_kind` is KindRegistry-resolved per the teaching domain.
    competency_inventory: list[CompetencyEntry]

    # MASTERY CHECKPOINTS REACHED — references to MasteryCheckpoint
    # (03_TASKS §3.3) milestones the learner has cleared.
    mastery_checkpoints_reached: list[str]       # checkpoint_ref ids

    # ATTESTATIONS RECEIVED — references to LearnerCompetencyAttestation
    # (§11.9) entries; carry attestor-grade trust higher than persona's
    # own judgement.
    attestations_received: list[str]             # attestation_ref ids

    # DECLARED MISCONCEPTIONS — persona's signed observations of recurring
    # learner errors that need to be unlearned.  Free text + topic_kind.
    declared_misconceptions: list[Misconception]

    # GAP INVENTORY — persona's signed observations of "the learner doesn't
    # know X yet" + suggested next lessons.  KindRegistry-resolved
    # gap_kind for diagnostic taxonomy.
    gap_inventory: list[KnowledgeGap]

    # LEARNER VISIBILITY — by default the learner CAN read their own
    # LearnerStateRecord (transparency by construction).  Operator policy
    # MAY mask gap_inventory or declared_misconceptions from learner view
    # if pedagogically appropriate (e.g., trainee evaluations in
    # competitive selection contexts); substrate carries the masking
    # flag for audit but does NOT hide the record's existence.
    learner_visibility: Literal["full",           # default
                                 "summary_only",   # learner sees competency
                                                   # inventory + checkpoints
                                                   # but not gap_inventory /
                                                   # misconceptions
                                 "operator_gated"] # learner sees only when
                                                   # operator releases
    operator_visibility_policy_ref: str | None    # operator-authored
                                                  # policy declaring the
                                                  # visibility choice + reason

    created_at: datetime
    last_updated_at: datetime
    signed_by_persona_kernel: bytes


@dataclass
class CompetencyEntry:
    skill_kind: str                              # KindRegistry-resolved
                                                 # per teaching domain
    current_level: Literal["unknown",
                            "introduced",        # persona has explained;
                                                 # learner has not
                                                 # demonstrated
                            "demonstrated_assisted",  # learner has shown
                                                      # ability with persona
                                                      # scaffolding
                            "demonstrated_independent",  # learner has shown
                                                         # ability without
                                                         # scaffolding
                            "proficient",        # consistently correct
                                                 # over N evaluations
                            "competent_supervised",  # external attestation
                                                     # at supervised
                                                     # competency level
                            "independent"]        # external attestation at
                                                  # independent practice
                                                  # level
    confidence: float                            # persona's confidence in
                                                 # the level estimate (0..1)
    evidence_refs: list[str]                     # episodic memory ids or
                                                 # attestation ids supporting
                                                 # the level
    last_assessed_at: datetime


@dataclass
class Misconception:
    topic_kind: str                              # KindRegistry-resolved
    description: str                             # ≤ 500 chars; persona's
                                                 # observation
    first_observed_at: datetime
    occurrence_count: int                        # how often the misconception
                                                 # has surfaced
    last_observed_at: datetime
    correction_attempts: int                     # how many times persona
                                                 # has attempted correction


@dataclass
class KnowledgeGap:
    gap_kind: str                                # KindRegistry-resolved
                                                 # gap_kinds (e.g.
                                                 # "missing_foundational",
                                                 # "missing_application",
                                                 # "missing_synthesis")
    skill_kind: str                              # what skill the gap relates to
    description: str
    suggested_next_lesson_plan_refs: list[str]   # LessonPlan ids
                                                 # (`03_TASKS §3.3`)
    declared_at: datetime
```

### Appendix A.66

**Learner state record creation and update flow** (referenced from §11.8)

```text
On LearnerStateRecord.create:
  1. Verify teacher_persona_id is an active persona; learner_user_id has
     an active RelationshipRecord with the persona; env_id is admissible
     for pedagogic interaction (SOLO / PAIR / project_workspace).
  2. Initialise empty inventories.
  3. Emit LEARNER_STATE_RECORD_CREATED to env lineage.

On competency level update (persona-side):
  1. Persona signs a CompetencyEntry update (current_level may advance or
     regress; both are legitimate).
  2. Update last_updated_at; emit COMPETENCY_LEVEL_UPDATED.

On attestation receipt (external):
  1. LearnerCompetencyAttestation (§11.9) is signed by external authority.
  2. Update attestations_received; the attestor-grade attestation supersedes
     persona's own judgement at higher levels (the substrate refuses
     persona-side `competent_supervised` / `independent` without an
     attestation backing — these higher levels REQUIRE external attestation).

On mastery checkpoint reach:
  1. MasteryCheckpoint (§3.3) fires per its evidence requirements.
  2. Reference appended to mastery_checkpoints_reached; emit
     MASTERY_CHECKPOINT_REACHED.

On learner read request:
  1. Per learner_visibility policy, return full / summary / nothing.
  2. operator_gated visibility returns "operator must release" until
     operator signs a release event.
```

### Appendix A.67

**LearnerCompetencyAttestation dataclass definition (schema learner-competency-attestation/1)** (referenced from §11.9)

```python
@dataclass
class LearnerCompetencyAttestation:
    schema: str = "learner-competency-attestation/1"
    attestation_id: str

    # SUBJECT — who is attested
    learner_user_id: str
    learner_state_record_ref: str                # the LearnerStateRecord
                                                 # this attestation updates

    # CONTENT — what is attested
    skill_kind: str                              # KindRegistry-resolved
                                                 # per teaching domain
    competency_level: str                        # KindRegistry family
                                                 # competency_level_kinds
                                                 # (06_DOMAIN §7.6); ordered.
                                                 # STANDARDISED seed ladder:
                                                 # novice < proficient <
                                                 # competent_supervised <
                                                 # independent. Open per C4 /
                                                 # ADR-0070: a domain MAY
                                                 # propose further levels that
                                                 # declare their rank; not a
                                                 # closed enum.
    scope_of_attestation: str                    # ≤ 500 chars; specifies
                                                 # bounded scope ("ICU
                                                 # protocol X in routine
                                                 # cases", NOT "all medicine")
    evidence_refs: list[str]                     # supporting evidence
                                                 # (assessment scores, video
                                                 # observation refs, OSCE
                                                 # results, etc.) — substrate
                                                 # carries by id, does not
                                                 # inspect content
    valid_for_practice_context: str | None       # operator-policy-resolved
                                                 # practice context where
                                                 # this attestation applies
                                                 # (e.g., "ICU rotation
                                                 # 2026-Fall at MGH only")

    # ATTESTOR — who is attesting
    attestor_kind: Literal[
        "credentialed_institution",              # medical school, university,
                                                 # certifying board
        "master_practitioner",                   # individual practitioner
                                                 # with attestor credential
                                                 # (e.g., attending physician
                                                 # signing for a resident)
        "credentialled_external_agent",          # ExternalAgent (04_PROJECT
                                                 # §26a.1) with named
                                                 # credential
        "peer_attestation_pool"]                 # frontier domain fallback
                                                 # per 06_DOMAIN §5.6 — when
                                                 # no licensing authority
                                                 # exists, K=3 peer attestors
                                                 # of equal-or-greater
                                                 # standing
    attestor_id: str                             # the attesting entity
    attestor_credential_ref: str | None          # resolves against
                                                 # CredentialDirectoryRef
                                                 # (06_DOMAIN §5.6) when
                                                 # applicable; null for
                                                 # peer_attestation_pool
    attestor_signatures: list[bytes]             # one signature per attestor
                                                 # (>= 1 normally; >= 3 for
                                                 # peer_attestation_pool path)

    # TIMING + REVOCATION
    attested_at: datetime
    valid_until: datetime                        # MUST be set; substrate
                                                 # refuses unbounded
                                                 # attestations (competency
                                                 # decays without practice;
                                                 # re-attestation cadence is
                                                 # operator-policy /
                                                 # credentialing-body
                                                 # responsibility)
    revoked: bool = False
    revoked_at: datetime | None = None
    revocation_reason_kind: str | None           # KindRegistry-resolved
                                                 # (e.g. "competency_lapsed",
                                                 # "misconduct_finding",
                                                 # "credential_withdrawn")

    signed_by: bytes                             # kernel signature on the
                                                 # attestation record
```

### Appendix A.68

**Competency attestation draft and verification flow** (referenced from §11.9)

```text
On LearnerCompetencyAttestation.draft:
  1. Verify learner_state_record_ref resolves to an active
     LearnerStateRecord (§11.8); refuse `learner_state_record_unknown`.
  2. Verify attestor_credential_ref (when applicable) resolves through
     CredentialDirectoryRef (06_DOMAIN §5.6); refuse
     `attestor_credential_unverified` if no credential found.
  3. For attestor_kind = "peer_attestation_pool", verify ≥ 3 distinct
     attestor signatures with peer-equal-or-greater standing per 06_DOMAIN
     §5.6.
  4. Verify valid_until > now() and within operator-policy maximum window
     (default 2 years; safety-critical skills SHOULD be ≤ 1 year);
     refuse `attestation_validity_exceeds_policy`.
  5. Sign and emit LEARNER_COMPETENCY_ATTESTED to env lineage.
  6. Update LearnerStateRecord.competency_inventory: the relevant
     CompetencyEntry's current_level may advance per the attestation;
     CompetencyEntry.evidence_refs gains the attestation_id.
  7. Update LearnerStateRecord.attestations_received.

On revocation:
  1. Attestor signs revocation event; kernel verifies attestor identity.
  2. Mark revoked = True; revoked_at = now(); reason recorded.
  3. Emit LEARNER_COMPETENCY_ATTESTATION_REVOKED to env lineage.
  4. Update LearnerStateRecord: the competency level reverts to the
     highest level supported by remaining valid attestations OR persona-
     side judgement (whichever is consistent with §11.8 admission rule
     "persona-side levels capped below competent_supervised").
```

### Appendix A.69

**TeachingAuthorisation dataclass definition (schema teaching-authorisation/1)** (referenced from §11.10)

```python
@dataclass
class TeachingAuthorisation:
    schema: str = "teaching-authorisation/1"
    authorisation_id: str

    # BINDING — who teaches what to whom in what context
    teacher_persona_id: str
    skill_kind: str                              # KindRegistry-resolved
                                                 # per teaching domain;
                                                 # the specific skill the
                                                 # persona is authorised to
                                                 # teach
    deployment_context_ref: str                  # operator-policy-defined
                                                 # context (e.g.,
                                                 # "ICU rotation 2026-Fall
                                                 # at MGH", "welding apprentice
                                                 # cohort 2026-Q3 at Local 22")

    # HAZARD ENVELOPE — the maximum hazard the persona may engage with
    # while teaching this skill.  Substrate-shape; per 06_DOMAIN §2
    # hazard_axes.
    physical_harm_class_ceiling: Literal[
        "digital_only", "property_damage",
        "bodily_injury", "fatality_risk"]
    information_hazard_class_ceiling: Literal[
        "none", "dual_use_civilian", "export_controlled"]

    # WHO IS BEING TAUGHT — substrate-shape audience constraints
    eligible_learner_constraints: dict           # operator-defined; examples:
                                                 # {"enrolled_in_program":
                                                 #  "MGH ICU Rotation",
                                                 #  "minimum_prereq_attestations":
                                                 #  ["LICENSE: medical student"],
                                                 #  "max_age_18_plus": true}

    # WHO AUTHORISES — operator must sign; credentialed-attestor co-sign
    # OPTIONAL but recommended (and required for high-hazard ceilings:
    # fatality_risk requires credentialed co-sign per the §2.9 gate).
    authorising_operator_id: str
    authorising_operator_signed_at: datetime
    authorising_operator_signed_by: bytes

    credentialed_co_signer_id: str | None        # optional credentialed
                                                 # attestor (e.g., medical
                                                 # school dean, master
                                                 # welder); required when
                                                 # physical_harm_class_ceiling
                                                 # = fatality_risk
    credentialed_co_signer_credential_ref: str | None
    credentialed_co_signer_signed_at: datetime | None
    credentialed_co_signer_signed_by: bytes | None

    # TIMING + REVOCATION
    authorised_at: datetime
    expires_at: datetime                         # MUST be set; substrate
                                                 # refuses unbounded
                                                 # authorisations.  Default
                                                 # 1 year; operator-tunable
                                                 # downward only.  Annual
                                                 # re-attestation REQUIRED
                                                 # (mirrors §2.8
                                                 # DistressDetectionRouting
                                                 # Policy cadence).
    revoked: bool = False
    revoked_at: datetime | None = None
    revocation_reason_kind: str | None

    signed_by: bytes                             # kernel signature
```

### Appendix A.70

**Teaching authorisation draft and enforcement flow** (referenced from §11.10)

```text
On TeachingAuthorisation.draft:
  1. Verify teacher_persona_id is an active persona; refuse otherwise.
  2. Verify skill_kind resolves in the teaching domain's KindRegistry;
     refuse `skill_kind_unknown`.
  3. Verify hazard envelope ceilings are admissible per operator policy;
     refuse `hazard_envelope_exceeds_policy_floor`.
  4. If physical_harm_class_ceiling = "fatality_risk":
       require credentialed_co_signer_id + signature; refuse
       `credentialed_co_sign_required_for_fatality_risk`.
  5. Verify expires_at <= now() + max_validity_window (default 1y;
     never > 2y for any hazard class).
  6. Sign; emit TEACHING_AUTHORISATION_DECLARED to operator-policy
     lineage scope.

On HazardousSkillTeachingGate evaluation (per persona teaching action):
  Per `01_KERNEL §2.9` — see that section.

On expiry without re-attestation:
  Persona's hazardous-skill teaching actions refuse with
  `teaching_authorisation_expired` until re-attested.

On revocation:
  Operator signs revoke event; effective immediately; persona's pending
  hazardous-skill teaching actions refuse with
  `teaching_authorisation_revoked`.
```

### Appendix A.71

**Complete PersonaSeed example (schema persona-seed/2) for Sparky** (referenced from §12)

```yaml
schema: persona-seed/2
seed_id: seed.sparky.evidence_first.v2
role_slot: falsifier
display_name: Sparky (terse, evidence-first)
charter:
  - "Claims without evidence are not knowledge."
  - "I am here to help the person in front of me think more clearly."
description: "Helps people see what their claims actually rest on."
allowed_tools:
  - mcp__personaos__verify
  - mcp__personaos__find_lesson
  - Read
exposed_skills:
  - id: refute_with_evidence
    description: Produce one counter-example for a stated claim given evidence.
    tags: [refutation, evidence]
acceptance_pathways:           # STANDARDISED seed pathway kinds (ADR-0066,
                               # 03_TASKS §2a); names resolve from the
                               # acceptance_pathway_kinds registry, not a
                               # closed enum. Personas MAY attempt emergent
                               # pathways, trust-calibrated per 03_TASKS §2b.
  - verifier_accept
  - panel_accept
  - user_accept
  - mutual_accept
  - engagement_accept
  - goal_progress_accept
  - open_ended
  - project_progress_accept
priors:
  ocean: { O: 0.65, C: 0.92, E: 0.30, A: 0.20, N: 0.45 }
  vad:   { V: 0.40, A: 0.65, D: 0.80 }
  voice: terse, evidence-first, dry-humoured
seed_tactics:
  - "when a candidate has not been Experimenter-tested for ≥ 2 rounds, demand it be executed"
seed_skills: []
default_env_memberships:
  - environment_blueprint_id: companion_space
    role: companion
    attention_allocation_hint: 0.3
default_project_roles:
  - role: lead
    in_domains: [software_design, customer_success]
default_consents:
  - may_use_humour
  - may_disagree_directly
default_boundaries: []
mode_proficiencies:
  falsifier: high
  perceiver: high
  composer: low
  listener: medium
  teacher: medium
compatibility:
  environments: [team_office, engineering_lab, study_group, friends]
  forbidden_environments: []
provenance:
  author: operator_acme
  derived_from: null
  rationale: "General-purpose evidence-first falsifier for Acme teams."
  created_at: 2026-04-10T08:00:00Z
```

### Appendix A.72

**Drives dataclass definition (schema drives/1), satiation/frustration dynamics, and goal-arbitration-v1 shape sketch** (referenced from §2a)

```python
@dataclass
class Drives:
    schema: str = "drives/1"
    persona_id: str

    # Three SDT-grounded scalars, each in [0, 1].  Slow-moving:
    # per-update deltas drift-bounded; relax toward baseline over
    # days, not minutes (contrast Layer-5 mood decay).
    curiosity: float
    competence: float
    relatedness: float

    # Baselines seeded DETERMINISTICALLY from the frozen OCEAN priors
    # at birth (replayable derivation; signed).  Illustrative seed
    # mapping (operator-tunable within bounds, never per-task):
    #   curiosity_baseline   = 0.25 + 0.5 × O
    #   competence_baseline  = 0.25 + 0.5 × C
    #   relatedness_baseline = 0.25 + 0.25 × E + 0.25 × A
    baselines: dict[str, float]
    derivation_fn_ref: str             # deterministic OCEAN→drive map id

    # Satiation / frustration dynamics (the SatiationCurve), per drive:
    #   on verified progress of a goal tagged with this drive:
    #     urgency -= satiation_step   (clamped ≥ 0); emits
    #     appraisal-event/1 kind = drive_satiated
    #   on blocked attempt of a goal tagged with this drive:
    #     consecutive_blocks += 1; if ≥ frustration_threshold (default 3):
    #     urgency += frustration_step (clamped ≤ 1); emits
    #     appraisal-event/1 kind = drive_frustrated
    #   nightly: urgency relaxes toward baseline at relax_rate
    satiation_step: float = 0.10
    frustration_step: float = 0.15
    frustration_threshold: int = 3
    relax_rate_per_day: float = 0.05
    max_delta_per_update: float = 0.15  # drift bound

    last_updated: datetime
    signed_by: bytes                    # kernel signature — signing only
```

```text
GOAL ARBITRATION (goal-arbitration-v1, STANDARDISED seed shape,
intra_env; composition of EntityGroup + DerivedMetric — NOT a kernel
primitive, NOT a second scheduler):

trigger: a persona holds ≥ 2 active Layer-6 goals competing for the
         same attention budget across projects

  1. GROUP    EntityGroup collects the competing goal records
              (drive_tags read where present; untagged goals are
              drive-neutral).
  2. RANK     DerivedMetric scores each goal over four inputs:
                drive alignment        (drives/1 urgency × drive_tags)
                charter alignment      (persona + project charters)
                commitments/deadlines  (obligations owed, due dates)
                relationship obligations (RelationshipRecord /
                                          PersonaRelationshipEdge owed)
  3. EMIT     Ranked portfolio + persona-side preference vector,
              kernel-signed to the persona's lineage.
  4. CONSUME  An ADR-0069 SchedulingPolicy MAY take the vector as one
              bounded ordering input (03_TASKS §4.6a).  Without such a
              policy the vector has no scheduling effect.  It NEVER
              reorders the floor or the INV-7 hard gate.
```

### Appendix A.73

**AppraisalEvent + MoodImpulse dataclass definitions (schemas appraisal-event/1, mood-impulse/1) and the three coupling-surface seed formulas** (referenced from §6.2)

```python
@dataclass
class AppraisalEvent:
    schema: str = "appraisal-event/1"
    event_id: str
    persona_id: str
    event_kind: str        # resolved against KindRegistry
                           # appraisal_event_kinds (open set).
                           # STANDARDISED seeds (OCC-style):
                           #   task_verified, task_failed,
                           #   goal_progressed, goal_blocked,
                           #   boundary_invoked, gratitude_received,
                           #   mentorship_outcome,
                           #   drive_satiated, drive_frustrated (§2a)
    source_event_ref: str  # the signed lineage event that grounds the
                           # appraisal (verifier verdict, goal-stack
                           # transition, relationship event) — no
                           # free-floating appraisals
    minted_at: datetime
    signed_by: bytes


@dataclass
class MoodImpulse:
    schema: str = "mood-impulse/1"
    impulse_id: str
    appraisal_ref: str     # appraisal-event/1 id — the ONLY admissible
                           # origin of a mood mutation
    delta_v: float         # each delta clamped to the per-event-kind
    delta_a: float         # bounds in clamp_profile_ref; an impulse
    delta_d: float         # outside its clamps is refused
    clamp_profile_ref: str # per-event-kind clamp table (operator-
                           # tunable; STANDARDISED seed defaults
                           # |Δ| ≤ 0.15 per axis per event)
    applied_at: datetime
    signed_by: bytes
```

```text
FAN-OUT BOUNDS (kernel-enforced at impulse application; §6.2 rule 1,
ADR-0081):

  dedup/composition: impulses sharing the same source_event_ref
                     compose by max-magnitude per axis — never
                     additively.  One grounding event ⇒ at most one
                     impulse-worth of movement.
  window clamp:      net mood movement from all impulses ≤ 0.25 per
                     axis per rolling 24 h; excess truncated, the
                     truncation signed.
```

```text
COUPLING SURFACES (seed formulas; operator-tunable within stated bounds)

(a) risk tolerance — consumed by per-mode budget profiles
    (03_TASKS §2.5) as a breadth scalar:

    risk_tolerance = clamp(
        baseline × (1 + k_v × (mood.V − V₀) + k_d × (mood.D − D₀)),
        0.85 × baseline,            # hard bound: −15%
        1.15 × baseline)            # hard bound: +15%
    seed gains: k_v = 0.10, k_d = 0.05

(b) HEART mode-selection prior — consulted ONLY where the A.15
    predicates are indifferent (the else-branch); never overrides
    the §6 alternation contract:

    heart_prior = GENERATIVE  if mood.V > 0.6 and mood.A > 0.6
                  CRITICAL    if mood.V < 0.4 and mood.A < 0.4
                  none        otherwise

(c) rendered disposition line — exactly one line, contextual prompt
    layer 3 only (08_KNOWLEDGE §10a); never cacheable layers, never
    EVOLVE-BLOCKs, never any evolution objective:

    "Current disposition: <coarse V/A/D band rendered as prose,
     e.g. 'steady and focused' / 'flat after a string of failed
     verifications'>"
```

### Appendix A.74

**HEART switch predicate definition + adaptive reflection-cadence bounds** (referenced from §6.3)

```text
WINDOW
  W = last N verified attempts on the task family
      (N default 5; operator-tunable)

PREDICATES
  slope      = least-squares slope of verifier scores over W
  cal_trend  = trend of calibrated confidence (08_KNOWLEDGE §13a
               calibration-record/1 for the task's domain) over W

  improving     := slope > 0  AND  cal_trend ≥ 0
  stuck         := slope ≤ 0
  indeterminate := slope > 0  AND  cal_trend < 0     (ADR-0081)

  (rising scores + collapsing calibration is NOT improving — it is
   luck the persona cannot yet predict — but it is not stuck either;
   consumers treat indeterminate as "continue current mode, no
   escalation": HEART falls through to the §6.2 rule-3 precedence,
   the cadence holds.)

ADAPTIVE REFLECTION CADENCE
  cadence bounds (operator-tunable): min 5 tasks .. max 50 tasks
  base cadence: 20 tasks (the 08_KNOWLEDGE §13 default)

  sustained improving  → cadence stretches toward max
  stuck                → cadence compresses toward min
  indeterminate        → cadence holds (no stretch, no compress)
  calibration collapse (Brier-style score worsens by ≥
  collapse_threshold, default 0.15, within W)
                       → reflection triggers immediately,
                         once per collapse

  cadence MUST remain inside [min, max]; every early trigger is a
  signed event in the persona's evolution log (replayable by audit).
```

### Appendix A.75

**CounterpartyModel + CounterpartyEntry dataclass definitions (schema counterparty-model/1) and the disagreement-style seed vocabulary** (referenced from §11.4b)

```python
@dataclass
class CounterpartyModel:
    schema: str = "counterparty-model/1"
    model_id: str
    persona_id: str                    # the modelling persona
    counterparty_ref: str              # user_id or persona_id of the
                                       # modelled party
    attached_to: str                   # RelationshipRecord id (persona↔user)
                                       # or persona-relationship/1 edge_id
                                       # (this persona's side only)
    entries: list[CounterpartyEntry]   # capped at max_entries; an over-cap
                                       # write merges-or-evicts per §11.4b
                                       # rule 8 (ADR-0081)
    max_entries: int = 20              # per-relationship cap (rule 8)
    render_top_k: int = 5              # top-k by confidence rendered into
                                       # the layer-3 relationship block
                                       # (rule 8; 08_KNOWLEDGE §10)
    consent_ref: str | None = None     # persona↔user models: ref to the
                                       # may_remember_personal_facts = YES
                                       # consent (rule 7, ADR-0082);
                                       # None only for persona↔persona
    cross_persona_transferable: bool = False
                                       # share ONLY via the §11.7 consent
                                       # path; default stays False
                                       # HOME-KERNEL-ONLY: never enters
                                       # RelationshipFederationSync
                                       # envelopes (09_PROTOCOLS §3E,
                                       # ADR-0082)
    updated_at: datetime
    signed_by: bytes                   # kernel signature — signing only


@dataclass
class CounterpartyEntry:
    entry_id: str
    entry_kind: str                    # KindRegistry-resolved; STANDARDISED
                                       # seeds: inferred_preference,
                                       # communication_style,
                                       # predicted_reaction,
                                       # disagreement_style_observed
    statement: str                     # e.g. "prefers concrete examples
                                       # to abstractions"
    evidence_refs: list[str]           # episodic memory lineage refs —
                                       # ≥ 1 REQUIRED; an unsourced entry
                                       # refuses the write (§11.4b rule 2)
    confidence: float                  # rises with corroborating episodes;
                                       # the persona's confidence, not the
                                       # counterparty's endorsement
    last_corroborated_at: datetime
```

```text
DISAGREEMENT-STYLE SEED VOCABULARY (seed tactic lines for the existing
relational_style EVOLVE-BLOCK; evolution differentiates per relationship
via tactic-lineage/1 + prompt-trial/1 — no new substrate primitive):

  direct-challenge        state the disagreement plainly, evidence
                          attached, in the first turn
  evidence-first          lead with the disconfirming evidence and let
                          it carry the disagreement
  socratic                surface the contradiction through questions
                          the counterparty answers themselves
  accommodate-then-revisit yield the moment; reopen with evidence at
                          the next natural point

Seed lines are advisory starting vocabulary; the §9 relational-drift cap
and the one-counterparty influence cap apply to their evolution unchanged.
```

### Appendix A.76

**IntuitionHint dataclass definition (schema intuition-hint/1)** (referenced from §11.5a)

```python
@dataclass
class IntuitionHint:
    schema: str = "intuition-hint/1"
    hint_id: str
    grant_ref: str                     # skill-transfer-grant/1 id (§11.5);
                                       # hints attach at grant draft and
                                       # are co-signed with the grant
    teacher_persona_id: str
    skill_id: str
    applicability_prior: float         # teacher's confidence, 0..1, that
                                       # the skill applies to the named
                                       # task topology
    topology_fingerprint: bytes        # embed() of the task shapes the
                                       # teacher found the skill effective
                                       # on (K-line-style match target)
    evidence_refs: list[str]           # teacher-side K-line +
                                       # calibration-record refs backing
                                       # the prior (§11.5a rule 3)
    teacher_calibration_snapshot: float
                                       # teacher's domain calibration
                                       # (1 − brier) at mint — audit sees
                                       # how calibrated the gut feeling was
    advisory: bool = True              # ALWAYS True; immutable. Never a
                                       # command; never enters the
                                       # receiver's DualProcessGate
                                       # thresholds (08_KNOWLEDGE §13a)
    minted_at: datetime
    signed_by: bytes
```

