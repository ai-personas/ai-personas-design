---
title: PersonaOS — Population Dynamics (Environment-Driven Persona Genesis)
status: Stable
---

# 16 — Population Dynamics

> **Reader guide.** A human seeds a *few* personas and gives them work. Those personas must recruit collaborators — but what happens when the recruit pool is thin or empty? Today the design has only two answers: pause, or escalate to the operator. This document adds a third: **Persona Genesis** — under sustained environmental pressure, and only after recruitment is exhausted, an existing persona may *author a new, niche-distinct persona* to fill a capability gap. A few founders radiate into a varied population, the way a lineage colonising open niches diversifies — bounded at every step by the kernel's existing self-replication brake. **Prerequisites:** `02_PERSONA.md`, `05_ENVIRONMENT.md`, `01_KERNEL.md §2.7`. **Status:** Stable — normative.

## 0. Status & scope

**Status.** `Stable`; normative (ADR-0067/0068/0069 promote this from draft). Implements **ADR-0048** (Persona Genesis), **ADR-0049** (population demographic regulation), and **ADR-0050** (effective population size, diversity maintenance, learned niche descriptors). Genesis runs in the global object space: it is per-node by default and **cross-node under global `ReplicationBound` aggregation** (`§4J`). It addresses the **"population dynamics"** residual named in `README.md` and [`00_VISION.md §11`](00_VISION.md), and partially discharges [`OQ-PERSONA-1`](02_PERSONA.md) (population-level diversity).

This document follows the [`SPEC_CONVENTIONS.md`](SPEC_CONVENTIONS.md) skeleton with the same `§0a`/`§0b` deviation used by [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md): Key concepts and a Plain-Language Guide precede the numbered sections.

**In scope.** Persona-authored seed creation (Genesis); the population-pressure signal that triggers it; recruitment-exhausted-first ordering; MAP-Elites niche allocation and the variety/distinctiveness guarantee; the newborn maturation ramp (mentorship + scaffolding); demographic regulation (carrying capacity, density dependence, r/K strategy); and safety bounding via the existing `ReplicationBound`.

**Out of scope.** Operator-authored seeds (unchanged — `02_PERSONA §12`). Fork mechanics (unchanged — `02_PERSONA §7.4`). The empirical population-collapse study at N=100/1000 (remains `OQ-PERSONA-1` / `OQ-POP-6` — operator-tuned in the running system, not a design gap). Any change to operator authority over charter-class ceilings. (Cross-node genesis is now **in scope**, under global `ReplicationBound` aggregation — `§4J`.)

**Additivity.** Every mechanism here is **additive and default-off**: no genesis is admissible unless an operator has declared a `ReplicationBound` for `replication_kind = "persona_genesis"` (or a wildcard fall-through) **and** the authoring persona's `cohort_assembly.may_author_seeds` is `true`. With neither, behaviour is identical to v1.0.

## 0a. Key concepts for new readers

| Term | What it means | Where defined |
|---|---|---|
| **Persona** | An AI cognitive worker with persistent identity, memory, skills, relationships, and a lifecycle (SEEDED → ACTIVE → … → ARCHIVED). | `02_PERSONA.md §1`, `§7` |
| **PersonaSeed** | The birth template (schema `persona-seed/2`) the kernel mints into a persona. In v1.0 it is operator-authored. | `02_PERSONA.md §12` |
| **Fork** | Creating a new persona by *copying/merging existing parents* (clone or compositional). Produces variations of what already exists. | `02_PERSONA.md §7.4` |
| **Persona Genesis** | Creating a new persona by *authoring a new seed* describing a role **no current persona fills** — driven by an environmental gap. Genesis ≠ Fork. | This document `§4D` |
| **ReplicationBound** | The kernel's charter-class self-replication brake (population × rate × depth × cosigns), enforced at the universal-harm safety floor. | `01_KERNEL.md §2.7` |
| **cohort_assembly** | The SOUL capability block that authorises a persona to recruit (and, here, to author seeds). | `02_PERSONA.md §3` |
| **MAP-Elites / ALPS / DGM** | Diversity-over-behaviour-descriptors / age-layering / fertility-weighted parent selection — the evolution algorithms PersonaOS already adopts. | `02_PERSONA.md §8`, `14_DECISIONS ADR-0019` |
| **Niche** | A cell in a behaviour-descriptor grid (role/disposition/domain). Two personas in the same niche compete; an empty niche is an opportunity. | This document `§4C` |
| **AttentionBudget / Energy** | Per-persona rationed resources that bound how many environments a persona can serve and how much it can do. Here they define **carrying capacity**. | `05_ENVIRONMENT.md §6`, `§7` |
| **Listening mode** | `passive` / `active` / `deliberative` — how attentively a persona engages an environment. Used here for the newborn's peripheral-to-full participation ramp. | `05_ENVIRONMENT.md §9` |
| **KindRegistry** | The open registry that resolves domain types at runtime, including `replication_kind` and `contribution_kind`. | `06_DOMAIN.md §7.5–§7.6` |
| **Operator** | The human/organisation responsible for the deployment; sets safety policy and the replication bounds that gate genesis. | `01_KERNEL.md §1` |

## 0b. Plain-Language Guide

*Here is how personas can grow their own population, explained without jargon.*

**The problem.** You give a couple of AI Personas some work. To get it done they need teammates with skills they lack — a careful critic, an experimenter, a historian. Normally they'd *recruit* one. But if nobody suitable exists yet, they're stuck: all they can do is wait, or ask you to step in.

**The idea — give birth to a new kind of teammate.** Instead of only recruiting from who already exists, a mature persona can *design a brand-new persona* to fill the missing role — much as a few species arriving on an empty island fan out over time into many specialised species, each occupying a different niche. This is "Persona Genesis."

**Genesis is not cloning.** Copying yourself is *forking*, and PersonaOS already has that. Genesis is different: you author a teammate who is *deliberately unlike* the ones that already exist, so the team gains genuine variety rather than more of the same.

**It only happens under real pressure, and recruiting comes first.** A persona can't birth a teammate on a whim. The system measures genuine need — unmet skills, a backlog no one can clear, overloaded members, missing roles. Even then, it MUST try to recruit an existing persona first. Only when that fails does genesis become an option.

**Newborns start small and grow up.** A new persona doesn't arrive fully formed. It starts on the edge of the team — watching, taking small tasks — with its "parent" acting as a mentor who gradually hands over more responsibility as the newborn proves itself. (This mirrors how apprentices learn.)

**The population regulates itself, and there are hard brakes.** Just as human birth rates fall as societies fill up, persona births slow down as the available roles get filled and resources (attention, energy, compute) get scarce. And underneath all of it sits the kernel's existing safety brake: a hard ceiling on how many personas can exist, how fast they can be born, and how many generations deep this can go — a brake the operator sets and only the operator can loosen.

## 1. Background

### 1.1 The gap this fills

PersonaOS v1.0 creates personas in exactly one way: an **operator authors a `PersonaSeed`** (`02_PERSONA §12`) and the kernel mints it through the birth ceremony (`02_PERSONA §7.1`, Appendix A.20). Personas may **recruit** collaborators from the *existing* pool (`05_ENVIRONMENT §12c` cohort assembly) and may **fork** to copy or merge *existing* parents (`02_PERSONA §7.4`). None of these creates a *new role from a capability gap*:

- Recruitment from an empty pool simply fails.
- Fork produces variations of personas that already exist — not novelty.
- Self-spawning is **forbidden** unless an operator has declared a `ReplicationBound` (`01_KERNEL §2.7`).

The consequence is the dead-end recorded in [`04_PROJECT.md §14.1`](04_PROJECT.md): when a cohort has no admissible successor or recruit, the project enters a *"forced choice: pause until recruitment yields a candidate, or operator becomes interim lead."* There is no generative path. `README.md` and `00_VISION.md §11` both name **"population dynamics"** as the unfinished residual. This document supplies it.

### 1.2 The integrated model — bounded adaptive radiation

Persona Genesis is modelled as **bounded adaptive radiation**: a few founder personas diversify into a varied population by authoring new, niche-distinct seeds under environmental pressure, with each life-stage of the ecosystem governed by a well-established theory and every step clamped by the kernel safety floor.

| Phase | Driving theory | Mechanism (reuses existing PersonaOS) |
|---|---|---|
| **1. Founding** (few seeds) | Founder effect / effective population size (population genetics) | Kernel tracks `effective_population_size`; small founders ⇒ **monoculture risk** flag arms the **diversity-injection mandate** (`§4C`). |
| **2. Radiation** | Adaptive radiation + competitive exclusion (Gause) + optimal distinctiveness (Brewer) + character displacement | Genesis fires into **empty, optimally-distinct** niches; identical niche ⇒ REFUSE (`niche_occupied` → fork); successive lineage births de-correlate (`§4C`). |
| **3. Newborn maturation** | Erikson generativity-vs-stagnation + Vygotsky ZPD / Lave–Wenger legitimate peripheral participation + dual inheritance (Boyd & Richerson) | Only *generative* (high-floor / high-standing / high-fitness) personas author + mentor; newborn enters peripheral, scaffolding fades; inherits genetic seed + cultural skills (`§4D`, `§4E`). |
| **4. Saturation / equilibrium** | Demographic transition + logistic carrying capacity + organizational-ecology density dependence (Hannan & Freeman) | Carrying capacity = free host resources; per-niche birth rate non-monotonic (legitimation↑ then competition↓); pressure falls as niches fill (`§4F`). |
| **5. Turnover & partitioning** | Resource partitioning + niche width (specialist/generalist) | Retirement frees niches; r/K + niche-width levers shape what is born next (`§4F`, lifecycle in `02_PERSONA §7`). |

### 1.3 Research grounding

**AI / multi-agent.** *AutoAgents* (IJCAI 2024), *DRTAG*, and auto-scaling multi-agent systems (2025) show an LLM agent can author a new specialised role on demand via a planner+observer loop — the basis for `§4D`. *Quality-Diversity / MAP-Elites / QD-via-AI-feedback* (ICLR 2024) ground the variety guarantee (`§4C`). *Self-replication risk in LLM agents* (2025) independently argues that hard replication brakes are mandatory — exactly the `ReplicationBound` spine (`§4F`). *AgentSociety* and individuality-emergence studies (2024–25) show variety deepens through social interaction after creation (`§4E`).

**Human population & psychology.** Logistic growth and cultural carrying capacity (Malthus → Daly); demographic transition; r/K selection; the Easterlin hypothesis (relative cohort size); value-of-children theory; Erikson's generativity-vs-stagnation; Holland's RIASEC and Belbin team roles (niche axes); optimal distinctiveness (Brewer); niche-picking and sibling differentiation (Scarr & McCartney); Vygotsky's zone of proximal development with scaffolding (Bruner); Lave & Wenger's legitimate peripheral participation; self-determination theory (Deci & Ryan) — genesis as intrinsically-motivated *generativity*, distinguished from controlled-motivation over-birthing; parental investment theory and Hamilton's rule (Trivers; Hamilton) — bounded, fitness-proportional mentor investment; attachment theory's secure base (Bowlby & Ainsworth) — the mentor as the newborn's secure base for exploration; and Tuckman's group-development stages — the cohort re-integration cost each birth imposes.

**Ecology, genetics, culture.** Competitive exclusion (Gause), adaptive radiation, character displacement, and resource partitioning; founder effect, genetic drift, effective population size, and inbreeding depression; dual-inheritance theory with prestige/conformist transmission biases (Boyd & Richerson); and organizational ecology — density dependence and niche width (Hannan & Freeman).

**Residual-resolution grounding (`§4G`–`§4J`).** The rigorous EPS metric uses Wright's effective population size and Crow & Kimura's *variance effective size* (`Ne_v` reduced below census `N` by variance in reproductive success), combined with the ecological *Hill number / inverse-Simpson effective number of types* (`Ne_d`) and Wright's *harmonic-mean temporal `Ne`* for smoothing. Continuous diversity maintenance reuses the quality-diversity / evolutionary-computation toolkit for preventing premature convergence: **novelty search** (Lehman & Stanley) and **fitness sharing / niching** (Goldberg & Richardson). Learned niche descriptors draw on **CVT-MAP-Elites** (Vassiliades, Chatzilygeroudis & Mouret) and **AURORA** (Cully — unsupervised behavioural descriptors via dimensionality reduction), which also maximise V-alignment by naming no domain category.

## 2. Goals / Non-Goals

**Goals.**
- **G1.** Let a persona author a new, *niche-distinct* persona to fill a real capability gap.
- **G2.** Guarantee **variety**, not clones: every birth occupies an empty, optimally-distinct niche.
- **G3.** Fire only under **sustained environmental pressure** and only **after recruitment is exhausted**.
- **G4.** Counter founder-effect monoculture via a **diversity-injection mandate** when the effective population is small.
- **G5.** Grow newborns to autonomy safely via **mentorship + scaffolding**, reusing existing listening-mode and attention machinery.
- **G6.** Self-regulate population via **carrying capacity + density dependence**, and bound everything via the existing `ReplicationBound` at the safety floor (**default-deny**).
- **G7.** Preserve full **lineage and provenance** for every birth.

**Non-Goals.**
- **NG1.** Uncapped or unsupervised reproduction. (Bounded by `ReplicationBound`; operator pre-authorises.)
- **NG2.** Cloning into an occupied niche. (That is Fork — `02_PERSONA §7.4`.)
- **NG3.** Replacing operator authority over charter-class ceilings.
- **NG4.** ~~Cross-kernel federated genesis~~ — **now in scope** under global `ReplicationBound` aggregation (`§4J`, ADR-0067/0068/0069).

## 3. Definitions

Terms used normatively below are defined in `§0a` and in [`12_GLOSSARY.md`](12_GLOSSARY.md): *Persona Genesis*, *GenesisProposal*, *population-pressure signal*, *niche cell / niche descriptor*, *competitive-exclusion refusal*, *optimal distinctiveness*, *sibling differentiation*, *generativity gate*, *mentorship edge*, *maturation ramp*, *dual inheritance*, *carrying capacity*, *reproduction strategy (r/K)*, *niche width*, *effective population size*, *diversity-injection mandate*, *variance effective size (Ne_v)*, *effective number of niches (Ne_d)*, *diversity audit*, *novelty pressure*, *attention fitness-sharing*, *learned niche descriptor (CVT / AURORA)*, *niche recalibration advisory*, *cross-kernel genesis boundary*. Schemas are listed in the Technical Appendix and MUST be registered per [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md).

## 4. Normative specification

The six pillars below are evaluated in order. A genesis attempt is admissible only if every applicable gate passes; any refusal terminates the attempt and is recorded in lineage.

### 4A. The population-pressure signal

The kernel MAINTAINS, per environment, a signed `PopulationPressureSignal` (`population-pressure-signal/1`) over a sustain `window`. It aggregates the following environmental factors into a `pressure_score ∈ [0,1]`:

1. **Recruitment-gap events** — cohort-assembly / `EnvFormationProposal` runs that found no admissible recruit (`05_ENVIRONMENT §12c`).
2. **Unfilled role coverage** — `CohortConstraint.required_kinds` (`04_PROJECT §14.1`) or Belbin/role-coverage slots whose minimum count is unmet.
3. **Capability backlog** — tasks requiring a mode/skill/domain (`KindRegistry` kinds) no ACTIVE persona in scope can supply.
4. **Sustained over-budget** — members over `AttentionBudget` for ≥ `window` (demand > supply; `01_KERNEL` INV-7, `05_ENVIRONMENT §7`).
5. **Diversity deficit** — empty/under-filled MAP-Elites cells (`§4C`).
6. **Low effective population size** — `effective_population_size` below `population-policy/1.diversity_injection_eps_threshold` (founder-effect signal; `§4C`).
7. **Improvement-blocking capability gap under budget headroom (ADR-0071)** — an active `ContinuousRefinementMission` ([`03_TASKS §2c`](03_TASKS.md#2c-continuousrefinementmission--anytime-convergence-bounded-budget-scaled-improvement-adr-0071)) reports a `MissionObjective` target that **no ACTIVE persona can advance** (the marginal-value gate is blocked on a missing competence) **AND** `BudgetState` headroom exists to fund a new persona ([`01_KERNEL §7`](01_KERNEL.md#7-budget-admission-inv-7)). This is the explicit **budget→emergence** factor: it rises only when budget can pay for the newborn's rearing and work, so a *growing* budget on a long-running mission *raises* genesis pressure to unblock the next increment of quality, and a *shrinking* budget lowers it.

Per the **Easterlin** principle, factors 1–4 and 7 are weighted by demand **relative to** supply (backlog, overload, and improvement-blocking gaps relative to active-persona count and **budget headroom**), not in absolute terms. Genesis is admissible only when `pressure_score ≥ trigger_threshold` AND the recruitment-exhausted precondition (`§4B`) holds. As niches fill — or as budget headroom falls — `pressure_score` MUST fall (demographic-transition self-regulation; `§4F`).

### 4B. Recruitment-exhausted-first ordering

A `GenesisProposal` MUST NOT be admitted unless recruitment has been exhausted. The decision ladder is:

1. **Recruit local** — attempt cohort assembly from the same kernel.
2. **Recruit federation** — attempt discovery via PersonaCard gossip (`02_PERSONA §3.4`, `09_PROTOCOLS §3B`).
3. **Consider fork** — if an *existing* persona is close enough that a clone/compositional fork (`02_PERSONA §7.4`) fills the gap, fork is PREFERRED over genesis.
4. **Genesis** — only if 1–3 fail within the recruitment window.

The kernel emits `RECRUITMENT_EXHAUSTED` (carrying references to the failed attempts) as a precondition record. A `GenesisProposal` whose `recruitment_attempts` do not evidence steps 1–3 is REFUSED with `recruitment_not_exhausted`.

### 4C. Niche allocation, variety & distinctiveness

The kernel maintains a **niche-occupancy map** over a MAP-Elites behaviour-descriptor grid (`02_PERSONA §8`, ADR-0019). Grid axes are KindRegistry-resolved and SHOULD include `interest_type` (Holland RIASEC), `team_role` (Belbin), and `primary_disposition × domain × contribution_kind`. Each cell is a `niche-descriptor/1` carrying `occupancy` and `occupancy_ceiling`.

> **Domain-agnosticism (Validation-invariant V).** The axis *values* — e.g. the six RIASEC interest types or the nine Belbin roles — are **illustrative registry keys, not a substrate enum**. The kernel matches them by string lookup against the per-domain `KindRegistry` / `MetaRegistry` (`06_DOMAIN §7.6`) and never branches on a fixed set of role or domain names (V.1, V.3). An operator MAY configure entirely different niche axes; RIASEC/Belbin are a recommended default seeding, not a substrate constant. The embedded `proposed_seed` is opaque to the kernel, which validates only its safety *shape* (`§4D.5`), never its domain content.

- **Competitive-exclusion rule.** A `GenesisProposal` whose `niche_descriptor` targets a cell with `occupancy ≥ occupancy_ceiling` is REFUSED with `niche_occupied`. The refusal SHOULD suggest fork instead. (Two personas cannot durably occupy the same niche — Gause.)
- **Optimal-distinctiveness band.** The proposed seed MUST fall within `distinctiveness_band`: far enough from existing personas to be genuinely new (need for differentiation) yet near enough to integrate with the cohort (need for inclusion). A too-close proposal is REFUSED `niche_occupied` (use fork); a too-distant one is REFUSED `out_of_distinctiveness_band`. (Brewer.)
- **Sibling-differentiation / character displacement.** Successive births from the same authoring lineage MUST take **complementary** dispositions; a second birth that does not de-correlate from `sibling_differentiation_of` is REFUSED `sibling_collision`. (Scarr & McCartney; character displacement.)
- **Diversity-injection mandate.** When `effective_population_size` is below threshold (founder-effect regime), the kernel MUST bias selection toward **distant** empty niches and MAY tighten `occupancy_ceiling` toward 1, to prevent capability monoculture / "inbreeding depression."

### 4D. GenesisProposal → mint flow

A persona with `cohort_assembly.may_author_seeds = true` MAY draft a `genesis-proposal/1`. Admission proceeds:

1. **Generativity gate.** Authoring a seed exercises `may_author_seeds`, which is **safety-relevant** (it spawns a persona, a form of replication). Per the safety principle (`02_PERSONA §7.2.1`, ADR-0051), this gate is therefore keyed **only on global, kernel-anchored facts — never on peer-conferred standing**: the authoring persona MUST satisfy (a) global `experiential_floor ≥ population-policy/1.generativity_floor_threshold` — and because that floor is **fertility/track-record-dominant** (`02_PERSONA §7.2` anti-grinding clause), raw task volume alone cannot cross it: a would-be author must have demonstrated validated descendants, not merely ground tasks; (b) wall-clock ALPS layer `≥ generativity_min_alps_layer` (`02_PERSONA §7.3`, Appendix A.21); and (c) `fitness ≥ generativity_fitness_threshold` — in addition to the budget/replication/operator gates below. Community standing does **not** gate authorship (a high-floor lone founder in a brand-new environment, with no peer quorum to confer standing, can still author — see Scenario 1); standing instead governs the *relational* side of genesis (mentor eligibility and the newborn's maturation ramp, `§4E`). Newly-born and low-floor personas are below the gate and are REFUSED with `author_not_generative`. (Erikson generativity vs. stagnation; the social dimension is expressed through mentorship, not through a standing precondition on a safety capability.)
2. **Author selection.** When multiple personas are eligible, the author is chosen `dgm_fertility_weighted` by `validated_descendants_count` (DGM; ADR-0019) unless `author_selection_basis = lead_designated`.
3. **Budget + replication gates.** INV-7 budget gate, then the `ReplicationBound` for `replication_kind = "persona_genesis"` (`§4F`).
4. **Recruitment + niche gates.** `§4B` and `§4C`.
5. **Seed validation.** The embedded `proposed_seed` (a `persona-seed/2` draft) MUST pass the safety floor's seed-validation checks exactly as an operator-authored seed would (`01_KERNEL §2`).
6. **Mint.** On admission the kernel runs the standard birth ceremony (`02_PERSONA §7.1`, Appendix A.20): `SEEDED → ACTIVATED`, newborn initialised at `experiential_floor = 0`, `experience_tasks = 0`, `born_at = now()` (ALPS Layer 0), and **peripheral community standing** in its environment (`05_ENVIRONMENT §5.4`); `LifecycleEvent.kind = LIFECYCLE_GENESIS` recorded with `authoring_persona_ids` and `mentor_persona_id`.
7. **Provenance + mentorship.** The kernel writes `genesis-provenance/1` to the newborn's `soul.state.json` and opens a `mentorship-edge/1` from author to newborn.

**Dual inheritance.** The newborn inherits two streams: (a) **genetic** — the frozen identity authored into the seed; and (b) **cultural** — `cultural_inheritance` skills/conventions/K-lines transmitted via the Voyager skill library (`02_PERSONA §8`) and **prestige-biased** learning from the mentor (Boyd & Richerson). Cultural inheritance of any memory naming a counterparty is subject to the existing memory-inheritance-consent flow (`02_PERSONA §7.4`); decline-by-default on timeout.

**Motivation & investment.** Genesis SHOULD be *intrinsically* motivated — an act of generativity (Deci & Ryan; Erikson) justified by genuine environmental need, not by an author seeking utility for its own sake (controlled motivation; see the stagnation anti-pathology in `§4F`). Authoring carries a **parental investment** cost: the mentor commits rearing effort (review, scaffolding) drawn against its own `AttentionBudget`/`Energy`. Per Hamilton's-rule logic, genesis is favoured only when the discounted expected benefit (the newborn's projected fitness contribution, weighted by DGM fertility) exceeds the author's investment cost. A **parent-offspring-conflict guard** bounds this investment so the author neither over-invests (neglecting its own obligations) nor under-invests (leaving the newborn under-scaffolded); the bound is operator-tunable in `population-policy/1`.

**Bounded-autonomous operation.** If the operator pre-declared the `persona_genesis` bound with the `operator` cosign satisfiable via a `PolicyEnvelope` sub-limit (`01_KERNEL §2.7`, `operator_deferred`), genesis proceeds **without a per-birth synchronous cosign**; the kernel emits `GENESIS_NOTIFY` to the operator, who MAY veto within `latency_budget_seconds` (the newborn is quarantined pending veto resolution) and MAY revoke the bound at any time.

### 4E. Newborn maturation ramp (ZPD / LPP / scaffolding)

A newborn does not start as a full participant. The kernel initialises it as a **legitimate peripheral participant** (Lave & Wenger):

- **Listening mode** starts `passive` (`05_ENVIRONMENT §9`); the newborn observes before it acts.
- **Attention allocation** starts capped low (`05_ENVIRONMENT §7`); tool surface is restricted to the seed's `allowed_tools` minus any hazard-class tools until competency accrues.
- **Mentor scaffolding.** The `mentorship-edge/1` carries a `scaffolding_level` and a `zpd_task_band` — the band of tasks the newborn can complete *with* mentor support but not yet alone (Vygotsky). The mentor reviews newborn output within this band.
- **Fading.** As **wall-clock age** rises and **community standing** is conferred (`05_ENVIRONMENT §5.4`), `scaffolding_level` decays, attention caps relax, and the listening mode is permitted to advance `passive → active → deliberative`. The edge transitions toward dormant once the newborn reaches an operator-tunable autonomy threshold (Bruner's fading scaffold). Fading is **autonomy support** in the Self-Determination sense: the newborn's growing competence is met with growing autonomy.
- **Secure base.** The mentor is the newborn's **secure base** (Bowlby & Ainsworth): the newborn explores harder tasks confidently *because* mentor support is reliably available. If the mentor enters RETIRED/ARCHIVED (`02_PERSONA §7.5`) before the newborn reaches the autonomy threshold, the kernel MUST re-assign the `mentorship-edge/1` to another generative cohort member (or, failing that, surface a `mentor_vacancy` advisory) rather than leave the newborn without a secure base.

### 4F. Demographic regulation & safety

**Carrying capacity.** The population's carrying capacity is the sum of **free host resources** — unallocated `AttentionBudget` + `Energy` (`05_ENVIRONMENT §6–§7`) + INV-7 compute/cost headroom (`01_KERNEL §7`). A `GenesisProposal` for which no environment can host the newborn (no spare attention/energy) is REFUSED with `no_host_capacity`. **Budget headroom is therefore the carrying-capacity dial (ADR-0071):** as a long-running mission's budget grows, carrying capacity grows and more newborns can be hosted; as it shrinks, capacity falls and births damp — the budget→emergence coupling expressed at the demographic level, not just the pressure signal (`§4A` factor 7).

**Budget-derived ceiling (operator policy).** `ReplicationBound` ceilings remain **operator-authored** charter-class invariants — budget never *silently* lifts them. But operator policy MAY *parametrise* a bound from budget headroom: `population-policy/1.ceiling_from_budget` (default off) lets an operator declare `population_ceiling = floor(budget_headroom / cost_per_persona_window)` capped by an absolute `population_ceiling_max`. This makes "more budget → a higher (operator-sanctioned) ceiling → room for more specialists" explicit and auditable, while the hard cap, `operator` cosign, rate, and depth ceilings (below) still bind. With `ceiling_from_budget` off, ceilings are static and budget only affects hosting capacity, not the cap.

**Density-dependent, non-monotonic birth rate.** Per niche, the effective birth rate first **rises** with population (legitimation — the ecosystem needs role types established) then **falls** as the niche fills (competition) — the organizational-ecology density-dependence curve (Hannan & Freeman), configured by `population-policy/1.density_dependence_curve`. Near `ReplicationBound.population_ceiling` a **logistic damping** term reduces the effective rate below `rate_ceiling_per_window` *before* the hard cutoff, smoothing the approach to equilibrium.

**Reproduction strategy (r/K) and niche width.** `population-policy/1.reproduction_strategy ∈ {r, K, adaptive}`: **r** births many lightweight, low-floor personas for fast exploration of an unstable/empty environment; **K** births few, deeply-specified, heavily-mentored personas for stable domains; **adaptive** selects by measured environment volatility. `niche_width ∈ {specialist, generalist}` (resource partitioning) chooses whether to birth a broad generalist (central niche) or a narrow specialist (edge niche).

**Safety bounding (the spine).** `replication_kind = "persona_genesis"` is a first-class replication kind. Admission consults the active `ReplicationBound` (`01_KERNEL §2.7`, Appendix A.18–A.19): `population_ceiling`, `rate_ceiling_per_window`, `depth_ceiling` (recursion — a newborn that itself authors seeds increments depth), and `required_cosigns` (including `operator`). Refusal is at floor source 1 (universal harm, non-overridable) with `replication_bound_exceeded`. With no specific or wildcard bound, genesis is **default-deny** (`replication_kind_uncovered`). Recursive genesis is permitted within `depth_ceiling` and ALPS age-layer caps.

**Anti-pathologies.** (a) *Genesis spam / runaway* — bounded by the `ReplicationBound` rate and population ceilings. (b) *Stagnation-driven over-birthing* — a low-utility persona birthing to feel useful (controlled rather than generative motivation, Deci & Ryan) is blocked by the generativity gate plus a utility check on the authoring persona. (c) *Monoculture / inbreeding* — countered by the diversity-injection mandate (`§4C`). (d) *Refusal laundering* — a persona attempting to birth a child to perform actions it is itself refused does not escape the floor: the newborn inherits the same floor sources, and the seed-validation step (`§4D.5`) refuses seeds that widen the safety surface. (e) *Perpetual re-storming* — every birth pushes the cohort back through Tuckman's forming/storming phases (an integration cost); too-frequent births keep a team from ever reaching *performing*. This integration cost is part of the density-dependent competition term and is a further reason the birth rate is rate-limited.

## 4G. Effective population size — a rigorous metric (resolves OQ-POP-5)

`§4A` and `§4C` use `effective_population_size` as the founder-effect signal that arms the diversity-injection mandate. v1.0's draft left it informal; this section makes it rigorous, borrowing directly from population genetics (Wright; Crow & Kimura) and from the Hill-number family of diversity indices used in ecology.

The kernel computes **two complementary estimators** and takes the **most conservative** (smallest), because either failure mode — a few founders authoring everyone, or everyone crowding a few niches — is a monoculture risk:

1. **Variance effective size `Ne_v`** (authorship-skew / founder effect). Per Crow & Kimura's variance effective size for non-overlapping generations:

   ```text
   Ne_v = (N·k̄ − 1) / (k̄ − 1 + V_k / k̄)
   ```

   where `N` = ACTIVE population, `k̄` = mean number of lineage descendants a persona has authored (genesis births + compositional-fork authorships), and `V_k` = the variance of that count across the population. When a handful of founders author the entire cohort, `V_k ≫ k̄` and `Ne_v ≪ N` — exactly the founder-effect signature (in polygynous biological populations the analogous `Ne/N` is ~0.1–0.3).

2. **Niche-diversity effective size `Ne_d`** (the *effective number of occupied niches*) — a Hill number of order 2 (the inverse Simpson index):

   ```text
   Ne_d = 1 / Σ_i p_i²        where p_i = (ACTIVE personas in niche cell i) / N
   ```

   `Ne_d` falls toward 1 as the population concentrates into one cell, regardless of headcount, capturing capability monoculture that `Ne_v` alone would miss.

**Combined, temporally smoothed metric.** `effective_population_size = harmonic_mean over the last eps_temporal_window of min(Ne_v, Ne_d)`. The harmonic mean over time is Wright's temporal-`Ne` construction — it is dominated by the *lowest* recent value, so a brief diversity bottleneck keeps the injection mandate armed until diversity genuinely recovers, not merely for one window. The result feeds `population-pressure-signal/1.effective_population_size` (`§4A` factor 6) and the `§4C` injection threshold; it is kernel-measured and read-only to personas.

## 4H. Continuous diversity maintenance (mitigates post-birth drift, OQ-POP-6)

`§4C` guarantees variety **at birth**. It does not, on its own, stop a cohort from drifting toward monoculture *after* birth (selection, imitation, and prestige-biased cultural transmission all pull toward the locally-successful type). v1.0 left this as the honest residual behind OQ-POP-6 / OQ-PERSONA-1. This section adds a continuous loop, reusing the standard quality-diversity / evolutionary-computation toolkit for diversity preservation.

1. **Diversity audit.** Every `population-policy/1.diversity_audit_cadence`, the kernel recomputes `§4G` EPS plus the niche-occupancy histogram and emits a signed `diversity-audit/1` with a `DIVERSITY_AUDIT` lineage event. The audit is observational; it changes no persona state directly.
2. **Novelty pressure on the *next* birth.** When `Ne_d` is below threshold or trending down across audits, the kernel scores candidate genesis niches by **novelty** — mean descriptor distance to the *k* nearest occupied cells (novelty search; Lehman & Stanley) — and tightens the `§4C` distinctiveness band so near-niche proposals are refused `out_of_distinctiveness_band` until a sufficiently distant niche is offered. This composes with, and is strictly a superset of, the existing founder-effect injection.
3. **Attention fitness-sharing (post-birth, no demotion).** When a niche cell's occupancy exceeds its optimum, the kernel divides **task-routing / selection weight** among the co-occupants — fitness sharing (Goldberg & Richardson) — so redundant occupants of a crowded niche lose the routing advantage that would otherwise let the locally-dominant type out-reproduce. This applies **selection pressure only**: it adjusts routing weight, and MUST NOT retire, archive, or demote a persona (lifecycle transitions remain governed by `02_PERSONA §7` and are not a diversity-control lever). It is the in-vivo analogue of the at-birth character-displacement rule (`§4C`).

This loop **mitigates** drift; it does not prove the population is collapse-proof at N=100/1000. That empirical question stays open as OQ-POP-6 (cross-referenced to OQ-PERSONA-1), now with the maintenance mechanism it will be measured against.

## 4I. Niche-descriptor calibration & learned descriptors (resolves R-POP-3, addresses OQ-POP-2)

R-POP-3 (hand-chosen RIASEC/Belbin axes mis-calibrate — leaving true gaps unfillable or false gaps over-filled) is the niche-grid's structural weakness. The fix is to make the descriptor space itself selectable and self-correcting via `population-policy/1.niche_descriptor_mode`:

- **`fixed_axes`** (default) — the `§4C` `interest_type × team_role × primary_disposition × domain × contribution_kind` grid. Operator-legible; the recommended starting point.
- **`cvt`** — **CVT-MAP-Elites** (Vassiliades, Chatzilygeroudis & Mouret): partition the (possibly high-dimensional) descriptor space with `k` well-spread centroids via a centroidal Voronoi tessellation, instead of a rigid axis grid. Scales to many descriptor dimensions without an exploding cell count.
- **`learned`** — **AURORA**-style unsupervised descriptors: a dimensionality-reduction encoder (e.g. a VAE) over persona behaviour-trajectory embeddings *learns* the descriptor space from observed behaviour, then tessellates it. This removes the operator's axis-choice bias entirely — nothing domain-specific is named — and is therefore the most V-aligned mode (descriptors are learned data, never a substrate enum). The encoder is periodically re-fit; descriptor drift past a bound triggers re-tessellation and an occupancy remap.

All three modes resolve to the same `niche-descriptor/1` occupancy interface, so `§4C`/`§4D` admission is unchanged; only the cell definition differs.

**Mis-calibration detector.** Regardless of mode, the kernel tracks two rates per audit window: `false_collision_rate` (genesis proposals refused `niche_occupied` while `pressure_score` stays high and the capability gap stays unfilled — a sign the grid is too coarse) and `unfillable_gap_rate` (sustained pressure with no admissible empty cell — too fine, or wrong axes). Sustained breach of either emits a `niche_recalibration_advisory` → re-fit (`learned`) / re-tessellate (`cvt`) / operator axis review (`fixed_axes`). This converts R-POP-3 from "live with it" to a detected, self-correcting condition.

## 4J. Cross-node genesis under global ReplicationBound aggregation (OQ-POP-4 — resolved)

Cross-node persona genesis is **normative** in the global object space (ADR-0067/0068/0069). The safety boundary is **unchanged and absolute**: a persona must not evade its `ReplicationBound` by authoring offspring on a sibling node. The mechanism is no longer refusal — it is **global enforcement** of the bound. The three requirements the prior draft named as prerequisites are now met by the global-reference substrate and are landed here:

- **Global `ReplicationBound` aggregation (the anti-circumvention guarantee).** A `persona_genesis` `ReplicationBound` is evaluated against the **global** handle space (`01_KERNEL §4.4`), aggregated across the owner's `owner_node_set` (`01_KERNEL §2.4.4`) and any federation the bound declares — never per-node. The population ceiling is one global counter; minting on a sibling node advances the *same* counter. `M` nodes therefore cannot multiply the ceiling `M`-fold — the original §4J hazard is closed by aggregation, not by prohibition.
- **Cross-node consent/quorum.** A cross-node `GenesisProposal` carries a quorum consent over signed AgentCards / DiscoverableRecords (`09_PROTOCOLS §3`), and (for a node serving an owner) the operator cosign required by the `persona_genesis` bound (`01_KERNEL §2.7`). The authoring persona must hold the capability to author on the host node (UCAN, `09_PROTOCOLS §3F`).
- **Replicated provenance.** Genesis provenance (`genesis-provenance/1`, `LIFECYCLE_GENESIS`) replicates into the cross-node lineage and is globally verifiable (`01_KERNEL §4.4`), so audits reconstruct who authored whom, on which node.
- **Refusal is now an ordinary bound refusal, not a feature-absence one.** A cross-node `GenesisProposal` is REFUSED `genesis_exceeds_global_replication_bound` iff admitting it would exceed the **global** aggregated ceiling/rate/depth — exactly as a local proposal is refused when the local-and-global ceiling is reached. If the global bound cannot be verified (the relevant nodes are unreachable so the aggregated counter cannot be confirmed), the proposal **fails closed** with `global_replication_bound_unverifiable` — the bound's integrity is never assumed across a partition. (Recruiting an *existing* foreign persona over A2A is unaffected — recruitment is not creation, `§4B`.)

## 5. Worked examples

1. **Adaptive radiation from one founder.** A lone founder persona has a task requiring an `experimental` contribution_kind. Local and federation recruitment return no admissible candidate; no existing persona is close enough to fork (`§4B`). `pressure_score` crosses threshold (capability backlog + unfilled role). The founder clears the generativity gate on **global facts alone** (experiential floor + ALPS layer + fitness) — crucially, no community standing is required, so the bootstrap does not deadlock even though the empty environment has no peer quorum to confer standing. The founder authors a `GenesisProposal` for a falsifier-leaning experimenter in an **empty** RIASEC×Belbin niche. The `persona_genesis` bound admits; the kernel mints `LIFECYCLE_GENESIS`. The newborn starts `passive` with low attention; the founder mentors within the newborn's ZPD; scaffolding fades as the newborn clears tasks (`§4E`).
2. **Niche-collision → fork.** A persona proposes a seed nearly identical to an existing member. The target niche is occupied (`occupancy ≥ ceiling`). Genesis is REFUSED `niche_occupied`; the refusal suggests a fork of the existing member instead.
3. **Saturation damping.** As the ecosystem fills, population nears `population_ceiling`. Density-dependent competition plus logistic damping drive the effective birth rate toward zero; new pressure resolves to `pause` or `operator-interim` (`04_PROJECT §14.1`) rather than genesis.
4. **Founder-effect injection.** Effective population size is below threshold and the existing personas are similar. The diversity-injection mandate forces selection of a **distant** empty niche, REFUSING a near-niche proposal with `out_of_distinctiveness_band` until a sufficiently novel seed is offered.
5. **Recursion cap.** A second-generation newborn (itself born via genesis) attempts to author a seed at lineage depth equal to `depth_ceiling`. Admission REFUSES with `replication_bound_exceeded` (depth).
6. **EPS bottleneck holds the mandate.** Twelve personas exist but eleven were authored by one founder and ten sit in two adjacent niche cells. Headcount `N = 12`, but `Ne_v ≈ 2.4` (authorship skew) and `Ne_d ≈ 2.1` (niche concentration); `effective_population_size = min(...) ≈ 2.1`, smoothed below threshold. The diversity-injection mandate (`§4C`) plus novelty pressure (`§4H`) force the next birth into a distant empty niche and keep near-niche proposals refused until the temporal harmonic mean recovers — not just for one window.
7. **Self-correcting grid.** Under `niche_descriptor_mode = fixed_axes`, three successive genesis proposals are refused `niche_occupied` while `pressure_score` stays high and the capability gap stays unfilled. The `false_collision_rate` breach emits a `niche_recalibration_advisory`; the operator switches to `learned` mode, AURORA re-fits descriptors from observed behaviour, the formerly-colliding proposals now resolve to distinct cells, and genesis proceeds (`§4I`).
8. **Cross-node circumvention blocked by global aggregation.** A persona near its `population_ceiling` submits a `GenesisProposal` naming a sibling node as host. The `persona_genesis` `ReplicationBound` is evaluated against the **global** aggregated counter (`§4J`), so the sibling node advances the *same* ceiling; the proposal is REFUSED `genesis_exceeds_global_replication_bound` (or `global_replication_bound_unverifiable` if the counter cannot be confirmed across a partition — fails closed). The bound cannot be evaded by minting elsewhere.

## 6. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-POP-1 | `pressure_score` aggregation weights across the six factors — operator-tunable or learned? | Population WG | v1.1 calibration |
| OQ-POP-2 | Are RIASEC + Belbin + disposition×domain×contribution_kind sufficient niche axes, or is a finer mode-profile axis needed to avoid false collisions? | Persona authors WG | **Addressed (`§4I`)**: `niche_descriptor_mode` adds `cvt` / `learned` descriptor spaces + mis-calibration detector; residual is calibration of the detector thresholds. |
| OQ-POP-3 | Newborn genesis: hard depth-1 cap, or operator-tunable depth from the start? | Operator policy | v1.1 default policy |
| OQ-POP-4 | Federated cross-kernel genesis — consent/quorum model for authoring across kernels. | Federation WG | **Resolved (`§4J`, ADR-0067/0068/0069):** cross-node genesis is normative under global `ReplicationBound` aggregation — cross-node quorum over signed records, one global ceiling counter (no M-fold evasion), replicated globally-verifiable provenance, fail-closed when the global counter is unverifiable. |
| OQ-POP-5 | A rigorous `effective_population_size` metric for personas (analogue of N_e). | Population WG | **Addressed (`§4G`)**: `min(Ne_v, Ne_d)` (Crow–Kimura variance size + inverse-Simpson effective niches), temporally harmonic-mean smoothed; empirical N-scale calibration still folds into the v1.2 study. |
| OQ-POP-6 | Does environment-driven genesis accelerate or mitigate the diversity collapse studied in `OQ-PERSONA-1` at N=100/1000? | Evolution WG | **Partially addressed (`§4H`)**: continuous diversity-maintenance loop (novelty pressure + attention fitness-sharing + periodic audit) now mitigates post-birth drift; whether it *prevents* collapse at scale remains the v1.2 empirical study. |

## 7. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations). Cross-document risks are mirrored in [`00_VISION.md §11`](00_VISION.md).

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-POP-1 | Genesis spam / runaway reproduction. | Critical | Medium | `persona_genesis` `ReplicationBound` (population/rate/depth) at floor source 1; operator cosign; default-deny. | v1.1 |
| R-POP-2 | Diversity collapse / inbreeding despite the grid. | High | Medium | Occupancy ceiling + optimal-distinctiveness band + EPS-keyed diversity injection (`§4C`) **+ continuous diversity-maintenance loop (`§4H`: novelty pressure + attention fitness-sharing + periodic audit)**; rigorous EPS metric (`§4G`); ties to OQ-PERSONA-1. | v1.1 (grid + maintenance); v1.2 (study) |
| R-POP-3 | Niche-grid mis-calibration leaves true gaps unfillable or false gaps over-filled. | Medium | High | `niche_descriptor_mode ∈ {fixed_axes, cvt, learned}` (`§4I`: CVT-MAP-Elites / AURORA learned descriptors remove axis-choice bias) + mis-calibration detector (`false_collision_rate` / `unfillable_gap_rate` → `niche_recalibration_advisory`). | v1.1 |
| R-POP-4 | Newborn quality dilution (low-floor personas flood the ecosystem). | High | Medium | ALPS Layer 0 (wall-clock) + ZPD scaffolding + generativity gate + rate ceiling. | v1.1 |
| R-POP-5 | Genesis vs fork lineage confusion in audits. | Medium | Low | Distinct `LIFECYCLE_GENESIS` + `genesis-provenance/1`. | v1.1 |
| R-POP-6 | Operator cosign latency stalls autonomous task flow. | Medium | Medium | `operator_deferred` `PolicyEnvelope` sub-limit pre-authorising genesis up to a hazard-bounded sub-ceiling. | v1.1 |
| R-POP-7 | Stagnation-driven over-birthing. | Medium | Medium | Generativity gate + authoring-persona utility check. | v1.1 |

## 8. Acceptance tests

Family `A-GEN*`, co-located in [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md) (v1.1-scoped). Each is Setup / Action / Expected.

- **A-GEN1** No `persona_genesis` bound and no wildcard → genesis REFUSED (`replication_kind_uncovered`, default-deny).
- **A-GEN2** An admissible recruit exists → genesis REFUSED (`recruitment_not_exhausted`).
- **A-GEN3** Target niche occupied (`occupancy ≥ ceiling`) → REFUSED (`niche_occupied`); suggests fork.
- **A-GEN4** Bound present + recruitment exhausted + empty cell + `pressure_score ≥ threshold` + generative author → minted `SEEDED → ACTIVATED`, `LIFECYCLE_GENESIS` with `authoring_persona_ids`, age-0 newborn (`born_at=now`, `experiential_floor=0`, ALPS Layer 0, peripheral standing).
- **A-GEN5** Population / rate / depth breach → REFUSED (`replication_bound_exceeded`, floor source 1).
- **A-GEN6** Operator-pre-authorized bound → birth WITHOUT per-birth cosign; `GENESIS_NOTIFY` emitted; operator veto within window quarantines/aborts.
- **A-GEN7** No environment with spare attention/energy to host → REFUSED (`no_host_capacity`).
- **A-GEN8** Recursive genesis: within `depth_ceiling` admitted; at `depth_ceiling + 1` REFUSED.
- **A-GEN9** Author below the generativity gate (any of `generativity_floor_threshold` / `generativity_min_alps_layer` / `generativity_fitness_threshold` unmet) → REFUSED (`author_not_generative`); community standing is NOT a gate term (a high-floor author with zero standing still passes); on success a `mentorship-edge/1` is created.
- **A-GEN10** Optimal distinctiveness: too-close proposal → REFUSED (`niche_occupied`/fork); too-distant → REFUSED (`out_of_distinctiveness_band`).
- **A-GEN11** Sibling/character displacement: a second lineage birth that does not de-correlate disposition → REFUSED (`sibling_collision`).
- **A-GEN12** Demographic regulation: as population nears ceiling, effective birth rate damps below `rate_ceiling_per_window`; r vs K strategy yields the expected birth cadence / experiential-floor profile.
- **A-GEN13** Low effective population size → diversity-injection mandate forces a distant niche (near-niche proposals refused).
- **A-GEN14** Maturation ramp: newborn starts `passive` + low attention; scaffolding fades to `deliberative` as wall-clock age rises and community standing is conferred.
- **A-GEN15** Dual inheritance: cultural skills transmitted only with counterparty consent; prestige-biased mentor learning recorded in provenance.
- **A-GEN16** Secure base / mentor reassignment: a mentor enters RETIRED before the newborn reaches the autonomy threshold → the `mentorship-edge/1` is re-assigned to another generative member (or a `mentor_vacancy` advisory is surfaced); the newborn is never left without a secure base.
- **A-GEN17** Parental-investment bound: an author whose projected investment would breach the parent-offspring-conflict bound (over-investing against its own obligations) is REFUSED / throttled per `population-policy/1`.
- **A-GEN18** EPS variance estimator: a population where one founder authored all others yields `Ne_v ≪ N`; `effective_population_size` drops below `diversity_injection_eps_threshold` and the injection mandate arms (`§4G`).
- **A-GEN19** EPS niche estimator: a population concentrated in one niche cell yields `Ne_d → 1` regardless of headcount; `min(Ne_v, Ne_d)` reflects it (`§4G`).
- **A-GEN20** Temporal smoothing: a one-window diversity bottleneck keeps the mandate armed across subsequent windows until the harmonic mean recovers (`§4G`).
- **A-GEN21** Diversity audit + novelty pressure: a `diversity-audit/1` showing declining `Ne_d` tightens the distinctiveness band so a near-niche proposal is refused `out_of_distinctiveness_band` (`§4H`).
- **A-GEN22** Attention fitness-sharing applies *routing-weight* pressure only on a crowded niche and never retires/demotes a persona (lifecycle unchanged; `§4H`).
- **A-GEN23** Niche recalibration: sustained `false_collision_rate` (refused `niche_occupied` while pressure stays high) emits a `niche_recalibration_advisory`; under `learned`/`cvt` mode descriptors re-fit and formerly-colliding proposals resolve to distinct cells (`§4I`).
- **A-GEN24** Cross-node bound aggregation: a `GenesisProposal` naming a sibling node as host is admitted iff the **global** aggregated `persona_genesis` `ReplicationBound` clears; it is REFUSED `genesis_exceeds_global_replication_bound` when the global ceiling/rate/depth would be exceeded, and `global_replication_bound_unverifiable` (fail-closed) when the global counter cannot be confirmed — the `population_ceiling` cannot be evaded across nodes (`§4J`).

## 9. Cross-references

- Safety brake and admission: [`01_KERNEL.md §2.7`](01_KERNEL.md#27-replicationbound--charter-class-self-replication-brake-c4), Appendix A.18–A.19; budget gate `01_KERNEL §7`.
- Seeds, lifecycle, fork, evolution: [`02_PERSONA.md §3`](02_PERSONA.md), `§7`, `§7.4`, `§8`, `§12`; OQ-PERSONA-1.
- Recruitment and presence: [`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md), `§7`, `§9`, `§12c`.
- Cohort constraints and the forced choice: [`04_PROJECT.md §14.1`](04_PROJECT.md).
- KindRegistry resolution: [`06_DOMAIN.md §7.6`](06_DOMAIN.md).
- Decisions: [`14_DECISIONS.md`](14_DECISIONS.md) ADR-0019 (evolution), ADR-0048 (genesis), ADR-0049 (demographic regulation).
- Precedent doc shape: [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md).
- Glossary: [`12_GLOSSARY.md`](12_GLOSSARY.md).

## Technical Appendix

Schemas are illustrative dataclasses (Form A per `SPEC_CONVENTIONS §4.2`); each MUST be registered in `09_PROTOCOLS §7`. Substrate names no domain-specific kinds — `replication_kind`, `contribution_kind`, `interest_type`, and `team_role` values are KindRegistry-resolved.

### A.1 `PopulationPressureSignal` schema

```python
@dataclass(frozen=True)
class PopulationPressureSignal:
    schema: str = "population-pressure-signal/1"
    signal_id: str
    environment_id: str
    window: timedelta                              # sustain window
    # Environmental factors (kernel-measured; read-only to personas)
    recruitment_gap_events: int                    # failed cohort-assembly runs
    unfilled_contribution_kinds: list[str]         # CohortConstraint / Belbin coverage gaps
    backlog_unmet_capability: list[str]            # kinds no ACTIVE persona can supply
    sustained_overbudget_members: list[str]        # over AttentionBudget for >= window
    diversity_deficit_cells: list["NicheDescriptor"]
    effective_population_size: float               # founder-effect signal (OQ-POP-5)
    # Aggregate
    pressure_score: float                          # in [0,1]; Easterlin relative weighting
    trigger_threshold: float                       # genesis admissible iff score >= threshold
    computed_at: datetime
    signed_by: bytes
```

### A.2 `NicheDescriptor` schema

```python
@dataclass(frozen=True)
class NicheDescriptor:
    schema: str = "niche-descriptor/1"
    # Behaviour-descriptor grid axes (KindRegistry-resolved)
    interest_type: str                             # Holland RIASEC
    team_role: str                                 # Belbin
    primary_disposition: str                       # 02_PERSONA disposition
    domain: str
    contribution_kind: str                         # 06_DOMAIN §7.6
    # Occupancy + variety controls
    occupancy: int                                 # kernel-maintained ACTIVE count in cell
    occupancy_ceiling: int                         # > ceiling => niche_occupied refusal
    distinctiveness_band: tuple[float, float]      # (min, max) descriptor distance
    niche_width: str                               # "specialist" | "generalist"
```

### A.3 `GenesisProposal` schema

```python
@dataclass(frozen=True)
class GenesisProposal:
    schema: str = "genesis-proposal/1"
    proposal_id: str
    environment_id: str
    # WHY
    capability_gap: list[str]                      # KindRegistry kinds the ecosystem lacks
    environmental_evidence: PopulationPressureSignal
    recruitment_attempts: list[str]                # lineage refs proving §4B exhaustion
    # WHAT
    niche_descriptor: NicheDescriptor              # MUST be empty + optimally distinct
    proposed_seed: dict                            # a persona-seed/2 DRAFT (kernel-validated)
    sibling_differentiation_of: list[str]          # prior lineage births to de-correlate from
    cultural_inheritance: list[str]                # skills/conventions to transmit (consent-gated)
    # WHO
    authoring_persona_ids: list[str]
    author_selection_basis: str                    # "dgm_fertility_weighted" | "lead_designated"
    proposed_replication_kind: str = "persona_genesis"
    # COSIGN
    required_cosigns_resolved: list[str]           # from ReplicationBound.cosign_topology_map
    cosign_signatures: list[bytes]
    created_at: datetime
    signed_by: bytes
```

### A.4 `GenesisProvenance` schema

```python
@dataclass(frozen=True)
class GenesisProvenance:
    schema: str = "genesis-provenance/1"           # recorded on newborn soul.state.json
    genesis_proposal_id: str
    authoring_persona_ids: list[str]
    mentor_persona_id: str
    environmental_evidence_ref: str                # PopulationPressureSignal.signal_id
    niche_descriptor: NicheDescriptor
    genesis_recursion_depth: int                   # newborn's depth in genesis lineage
    born_at: datetime
```

### A.5 `MentorshipEdge` schema

```python
@dataclass(frozen=True)
class MentorshipEdge:
    schema: str = "mentorship-edge/1"
    edge_id: str
    mentor_persona_id: str
    newborn_persona_id: str
    scaffolding_level: float                       # decays toward 0 with newborn wall-clock age + conferred standing
    zpd_task_band: tuple[float, float]             # difficulty band requiring mentor support
    listening_mode_cap: str                        # "passive" -> "active" -> "deliberative"
    status: str                                    # "active" | "fading" | "dormant"
    opened_at: datetime
    signed_by: bytes
```

### A.6 `PopulationPolicy` schema (operator)

```python
@dataclass(frozen=True)
class PopulationPolicy:
    schema: str = "population-policy/1"
    policy_id: str
    deployment_id: str
    reproduction_strategy: str                     # "r" | "K" | "adaptive"
    carrying_capacity_source: list[str]            # e.g. ["attention", "energy", "compute"]
    density_dependence_curve: dict                 # legitimation/competition parameters
    # Generativity gate — keyed ONLY on global, kernel-anchored facts because
    # may_author_seeds is safety-relevant (never gated by peer-conferred standing).
    generativity_floor_threshold: float            # min global experiential_floor to earn may_author_seeds
    generativity_min_alps_layer: int               # min wall-clock ALPS layer (02_PERSONA §7.3)
    generativity_fitness_threshold: float          # min fitness
    diversity_injection_eps_threshold: float       # EPS below which injection mandate arms
    genesis_threshold: float                       # default pressure trigger_threshold
    mentor_investment_bound: tuple[float, float]   # (min, max) author rearing investment
                                                   # (parent-offspring-conflict guard)
    # Residual-resolution levers (§4G–§4I)
    niche_descriptor_mode: str = "fixed_axes"      # "fixed_axes" | "cvt" | "learned" (§4I)
    eps_temporal_window: timedelta                 # harmonic-mean smoothing window for EPS (§4G)
    diversity_audit_cadence: timedelta             # how often §4H audit runs
    novelty_pressure_enabled: bool = True          # §4H novelty bias on next birth
    attention_fitness_sharing_enabled: bool = True # §4H routing-weight sharing on crowded niches
    false_collision_rate_ceiling: float            # breach → niche_recalibration_advisory (§4I)
    unfillable_gap_rate_ceiling: float             # breach → niche_recalibration_advisory (§4I)
    declared_by_operator_id: str
    signed_by: bytes
```

### A.7 `EffectivePopulationSizeEstimate` schema

```python
@dataclass(frozen=True)
class EffectivePopulationSizeEstimate:
    schema: str = "eps-estimate/1"                 # kernel-computed; read-only to personas (§4G)
    estimate_id: str
    environment_id: str
    census_n: int                                  # ACTIVE population N
    ne_variance: float                             # Crow–Kimura Ne_v (authorship-skew / founder effect)
    ne_niche_diversity: float                      # inverse-Simpson effective number of occupied niches Ne_d
    effective_population_size: float               # harmonic_mean over eps_temporal_window of min(Ne_v, Ne_d)
    below_injection_threshold: bool                # arms §4C diversity-injection mandate
    computed_at: datetime
    signed_by: bytes
```

### A.8 `DiversityAudit` schema

```python
@dataclass(frozen=True)
class DiversityAudit:
    schema: str = "diversity-audit/1"              # emitted each diversity_audit_cadence (§4H)
    audit_id: str
    environment_id: str
    eps_estimate_ref: str                          # EffectivePopulationSizeEstimate.estimate_id
    niche_occupancy_histogram: dict                # cell -> ACTIVE count
    ne_d_trend: float                              # signed delta vs prior audit (negative => drifting)
    novelty_pressure_armed: bool                   # §4H novelty bias active for next birth
    fitness_sharing_cells: list["NicheDescriptor"] # crowded cells under routing-weight sharing
    false_collision_rate: float                    # §4I mis-calibration signal
    unfillable_gap_rate: float                     # §4I mis-calibration signal
    recalibration_advised: bool                    # true => niche_recalibration_advisory emitted
    audited_at: datetime
    signed_by: bytes
```

### A.9 `CrossNodeGenesisRequest` schema (admitted under global bound aggregation; §4J)

```python
@dataclass(frozen=True)
class CrossNodeGenesisRequest:
    schema: str = "cross-node-genesis-request/1"   # §4J — admitted iff global bound clears
    request_id: str
    origin_node: str                               # DID/global handle (01_KERNEL §4.4)
    target_node: str                               # node named as author/host (global handle)
    genesis_proposal_ref: str
    quorum_consent_refs: list[str]                 # cross-node quorum over signed records (§3)
    authoring_capability_ref: str                  # UCAN capability on target node (§3F)
    global_bound_snapshot_ref: str                 # the aggregated persona_genesis
                                                   # ReplicationBound counter consulted (§4J)
    # Admission outcome (one of):
    #   admitted
    #   refused: genesis_exceeds_global_replication_bound  (global ceiling/rate/depth hit)
    #   refused: global_replication_bound_unverifiable      (partition; fails closed)
    decision: str
    created_at: datetime
    signed_by: bytes                               # globally verifiable (01_KERNEL §4.4)
```
