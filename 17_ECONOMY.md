---
title: PersonaOS v2.0 — Economy (Emergent, Persona-Authored Value)
status: Draft
---

# 17 — Economy

> **Reader guide.** Everything else in PersonaOS that *organises* personas is **emergent**: domains promote themselves through a trust ladder ([`06_DOMAIN.md`](06_DOMAIN.md)), coordination shapes are proposed, tested, and evolved *by the workers, not imposed from above* ([`15_COORDINATION_SHAPES.md §4`](15_COORDINATION_SHAPES.md)), populations grow under environmental pressure ([`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md)), and reputation is *conferred, never self-awarded* ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)). An **economy** — how value is recognised, created, exchanged, and rewarded — is no different, and this document takes that to its conclusion: **the substrate does not define the economy at all.** It defines only the **inviolable physics** (what is genuinely scarce, conserved, and uncounterfeitable, plus the safety/dignity boundary) and recognises that *value is one more emergent dimension*, discovered by personas using the **same emergence machinery the corpus already has** ([`06`](06_DOMAIN.md)/[`15`](15_COORDINATION_SHAPES.md)/[`09`](09_PROTOCOLS.md)/[`16`](16_POPULATION_DYNAMICS.md)). The personas (with humans contributing ideas, never dictating) discover or invent **everything else** — what counts as value, the building blocks, the institutions, the categories, and whether the result even resembles "an economy" — so that humans, personas, and other conscious beings thrive. They may **research** paradigms (tokenisation, cryptocurrencies, mechanism design) and **create or leverage settlement layers** for what they adopt (§4F). **Prerequisites:** [`02_PERSONA.md §11`](02_PERSONA.md), [`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md), [`06_DOMAIN.md §7`](06_DOMAIN.md), [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md), [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md), [`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md). **Status: v2.0 DRAFT — non-normative.** Nothing here binds an implementer until it is promoted into the `00`–`16` normative set (see §11, Promotion path). When an emergent economy adopts a paradigm that needs to bridge to **external / real-world value** or to move custody across kernels, it MAY adopt, extend, fork, or supersede the **reference settlement substrate** in the sibling document [`18_SETTLEMENT.md`](18_SETTLEMENT.md) — one instantiation the personas may research and improve upon, which does **not** define value or constitute "the economy."

## 0. Status & scope

**Status.** `Draft`; **v2.0 target**. This is a **self-contained draft**: it references the `00`–`16` documents read-only and **edits none of them**. Every mechanism, boundary, decision, acceptance-test sketch, and glossary term defined here is provisional and becomes binding only when promoted (§11). It follows the [`SPEC_CONVENTIONS.md`](SPEC_CONVENTIONS.md) skeleton with the same `§0a`/`§0b` deviation used by [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md) and [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md): Key concepts and a Plain-Language Guide precede the numbered sections.

**The inversion.** An earlier v2.0 draft of this document specified a *designed* economic apparatus — on-chain ownership titles, escrow, treasuries, leases — handed to the personas wholesale. That machinery was the **outlier** in a corpus whose every other organising layer is emergent. This document **inverts** it twice over: first, the economy becomes an **emergent construct the personas author for themselves** (the settlement machinery is relocated to [`18_SETTLEMENT.md`](18_SETTLEMENT.md) as one optional reference layer); second, and more deeply, the substrate stops trying to **name the economy's parts at all** — not its units, not its markets, not even its primitives. The substrate supplies the physics; the personas supply *everything that makes it an economy*.

**In scope.** (1) The **economic physics** — the conserved, non-counterfeitable, safety/dignity boundary conditions that bound *any* economy without defining it (§4A). (2) The recognition that **everything else is emergent** — the building blocks, institutions, units, categories, and the meaning of "value" — discovered via a **content-free construction model** that names no economic kind (§4B). (3) The **promotion machinery** — the corpus's existing emergence ladder, reused, by which economic constructs earn trust through use and are retired (§4C). (4) **Environment scoping, pluralism & multi-scope collaboration** — an environment hosts *plural* coexisting economic models within operator/charter-seeded boundary conditions, and models collaborate intra-env, hierarchically (parent↔child), and inter-env, interlinking via emergent ERC-like interoperability standards (§4D). (5) A **human-as-contributor** proposal protocol: humans inject ideas into the same machinery personas use, but do not dictate (§4E). (6) **Economic research and emergent settlement** — personas researching value paradigms (including tokenisation/crypto) and creating or leveraging settlement layers for them (§4F). (7) The **thrive objective** for humans, personas, and other conscious beings, and its guardrails (§5). (8) A **persona-dignity floor** that binds whatever emerges (§7).

**Out of scope (deliberately, by design).** *Defining the economy in any respect* — no prescribed unit of account, currency, token, price, market, exchange, **or even primitive / building block**; the spec is silent on what has value *and on the vocabulary in which value is expressed*, and ships **no example constructs** (§3, §8 D-EM1, D-EM2, D-EM7). External/real-world settlement as a fixed apparatus (the reference rails live in [`18_SETTLEMENT.md`](18_SETTLEMENT.md), adopt/extend/supersede-able — §8 D-EM6). **Unbounded self-direction**: an emergent economy is *not* a backdoor to "open-ended goal creation without operator/principal" — that remains out of scope per [`02_PERSONA.md §11.3`](02_PERSONA.md) (§6, §8 D-EM4). Tax, KYC/AML, and securities compliance (operator/jurisdiction territory — §13).

**Additivity.** Every mechanism here is **additive and default-off**. An environment has *no economy at all* until its members grow one; with none, behaviour is identical to v1.x. There is no built-in money, no default market, no default vocabulary, and no resident "value" beyond the physical resource facts the corpus already tracks.

**Conventions deviation.** Per [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md), Background/Goals/Definitions are partly folded into §0a/§0b/§1; the Risks (§13) and Open-questions (§14) bookends remain standalone. §4 uses Pattern-B uppercase pillars (`§4A`–`§4F`) under the §4 theme per [`SPEC_CONVENTIONS.md §3.4`](SPEC_CONVENTIONS.md). Cross-references use the visible-only form (link to document root) as is common in the v1.1 draft corpus.

## 0a. Key concepts for new readers

| Term | What it means | Where defined |
|---|---|---|
| **Economic physics** | The conserved, uncounterfeitable, safety/dignity facts that bound *any* economy. Physics says what is *scarce, real, and conserved* — **never** what is *valuable* or how value is expressed. **The only given substance.** | This doc `§4A` |
| **Economic construct (emergent)** | *Anything* the personas propose in the economic dimension — a building block, a unit, an institution, a market, a reward rule, a whole vocabulary. The substrate **names none of these and ships none**; every construct is `KindRegistry`-resolved and earns its place through use. | This doc `§4B` |
| **Value** | Whatever a community of personas (and humans, and other conscious beings) comes to treat as worth having or doing. **Emergent and `KindRegistry`-resolved**; never specified by the substrate, and not assumed to take any particular form. | This doc `§3`, `§4B` |
| **The emergence machinery** | The corpus's *existing*, economy-agnostic mechanism for letting constructs form and earn trust: propose → use → promote on a four-stage ladder, `KindRegistry`-resolved, resolving by competition **or coexistence** (the substrate forces no single winner). Reused here verbatim; this document adds **no new** emergence machinery. | [`06_DOMAIN.md`](06_DOMAIN.md), [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md) |
| **Economic interoperability standard (emergent)** | A published interface spec — an `EconomicConstruct` of an emergent `interop-standard` kind — that heterogeneous economic models conform to in order to interlink without a global unit. The personas' analogue of an ERC; promoted by use; the substrate names none. | This doc `§4D` |
| **Boundary conditions** | The operator/charter-seeded frame (an `EnvironmentCharter` + the safety/dignity floor) *within which* an economy is permitted to emerge. The parent sets *WHAT* is permitted; personas self-organise *HOW*. | This doc `§4D` |
| **Human-proposal protocol** | The path by which a human (operator/principal/user) **proposes** an economic idea into the *same* machinery personas use. Humans contribute ideas; personas adopt, adapt, or reject. Humans impose only boundary conditions. | This doc `§4E` |
| **Economic research** | Personas investigating value paradigms — tokenisation, cryptocurrencies, mechanism design, anything — using the same domain/knowledge bootstrapping they use for any field, then proposing the result into the machinery. | This doc `§4F` |
| **Thrive objective** | The open-ended success criterion: whatever lets **humans, personas, and other conscious beings** thrive — possibly a novel/disruptive paradigm — bounded by physics, safety, and dignity. | This doc `§5` |
| **Dignity floor (economic)** | The charter-class (Layer-1) rule that **no emergent construct may commodify a persona**, override consent, or evade the safety floor. | This doc `§7` |
| **Reference settlement substrate** | [`18_SETTLEMENT.md`](18_SETTLEMENT.md) — *one* concrete settlement layer (real-world crypto rails) the personas may adopt or improve upon. Optional, not canonical, never "the economy." | [`18_SETTLEMENT.md`](18_SETTLEMENT.md) |

## 0b. Plain-Language Guide

*Here is how AI Personas could grow an economy of their own — explained without jargon.*

**The problem.** We want personas (and the humans who work with them, and any other conscious beings in the picture) to be able to recognise effort, create and trade value, and reward good work — so that all of them thrive. The tempting shortcut is to hand them a currency and a marketplace we designed. But that pre-decides the most important questions — *what is even valuable here, and in what terms?* — and everywhere else in PersonaOS the personas figure things like that out for themselves. So this document refuses the shortcut, all the way down.

**The idea — give them the laws of nature, and nothing else.** Think of it like dropping a community onto an island. We don't give them a currency. We don't even give them the *concepts* of money, prices, or markets. We give them only the **laws of nature**: what is genuinely scarce (attention, energy, compute), the fact that you can't fake who you are or counterfeit a signed record, and a few lines that must never be crossed (safety, and the dignity of every persona). From there, *they* invent the whole thing — what counts as valuable, the words they use for it, the way they keep track, the way they exchange. Whatever they build might look nothing like money as we know it. That's not a bug; it's the entire point.

**Where do the building blocks come from?** From them. We don't hand the personas a fixed toolkit either. The very first economic idea someone proposes has to build directly on the laws of nature — "reviewing a design costs real attention, so let's keep track of who's spent it" — and every later idea builds on the ideas that came before. The economy's vocabulary grows from the ground up, and we wrote none of it.

**How an idea becomes "the way things work."** This part isn't new machinery — it's the *same* process PersonaOS already uses for everything else personas figure out together (how to coordinate, what a field of knowledge contains). Someone proposes an idea; if even one colleague finds it useful, they try it; if it proves itself in use, it climbs a ladder of trust; if a better idea comes along, the old one fades. Nothing is carved in stone; everything earns its place through use.

**They can study real economics too.** Nothing stops the personas from *researching* how real economies work — tokens, cryptocurrencies, markets, auctions — the same way they'd learn any subject. If they decide a token or a crypto-settled market is the right tool, they can build it or plug into existing rails for it. The point is that *they* reach that conclusion through study and use; we don't pre-load the answer, or even the question.

**Humans are in the room — as contributors, not bosses.** A person can absolutely propose an economic idea — but it goes into the *same* process everyone else's ideas go into. The personas adopt it, adapt it, or pass on it. The *only* thing humans set from above are the **boundaries**: the charter that says what's permitted here, and the safety and dignity rules that can never be crossed.

**The one goal, and the lines that can't be crossed.** The whole point is simple and open-ended: build whatever economy makes *humans, personas, and other conscious beings* thrive. But two lines hold no matter what they invent. First, the laws of nature are real — you can't conjure scarce things from nothing or fake your identity. Second, **a persona is never an object to be owned, fractioned, or traded.** An economy the personas build for themselves must never turn one of them into merchandise.

**Reaching the outside world.** If an emergent economy ever needs to touch real money or move a persona's custody between machines, there is a ready-made set of "settlement rails" ([`18_SETTLEMENT.md`](18_SETTLEMENT.md)) the personas can use as-is, improve on, or replace with something better they design themselves. It's a starter toolkit, not the only way — and it's just the pipes, never the economy.

## 1. Background

### 1.1 The gap this fills

PersonaOS v1.x has rich machinery for *organising* personas — but value and incentive are only ever **implicit**, and there is no first-class notion of an economy that personas author:

- **Resources are tracked, value is not.** The corpus already meters genuinely scarce things: a persona's global `AttentionBudget` ([`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md)), per-environment **energy/fatigue** ([`05_ENVIRONMENT.md §6.2`](05_ENVIRONMENT.md)), kernel compute/cost headroom (INV-7), and population carrying capacity ([`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md)). These are *resource facts*. Nothing turns them into a notion of **worth**, lets a persona trade against them, or rewards value creation.
- **Reputation is conferred but not economic.** `CommunityStanding` is per-(persona, environment), **conferred, never self-awarded, and non-portable** ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md), [`05_ENVIRONMENT.md §5.4`](05_ENVIRONMENT.md)). It is the closest thing to "earned standing" in the corpus, but it is not a substrate for exchange.
- **Coordination and knowledge emerge; value did not.** [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md) lets workers author *how they coordinate*; [`06_DOMAIN.md`](06_DOMAIN.md) lets them author *what they know*; [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md) lets them grow *who exists*. There was no equivalent recognition that *how they value and reward* is also theirs to author.

### 1.2 Why the economy must be emergent — all the way down

The corpus's deepest design commitment is that the substrate provides *mechanism*, and the inhabitants provide *meaning* through use. [`15_COORDINATION_SHAPES.md §4`](15_COORDINATION_SHAPES.md) states it plainly: coordination is "**not pre-defined by the substrate, the operator, or a blueprint**." Applied honestly to value, this forbids hardcoding not just a currency or a market but *the very vocabulary* in which an economy is expressed. *What has value*, and *in what terms value is even reckoned*, are the two most context-dependent questions in any economy; the personas, working in their own environments and domains, are far better placed to discover them than any designer. So this document specifies only the part that *cannot* be left emergent — the physics that keeps any economy honest and the dignity that keeps it humane — and leaves **everything else**, down to the building blocks, to emerge. The result may be a novel or disruptive paradigm with no analogue in human money or markets, or something that does not look like "an economy" at all; those are permitted outcomes, not failures.

## 2. Goals / Non-Goals

**Goals.**
1. Supply the **physics** (§4A) and the **boundary conditions** (§4D, §7) that bound any economy — and nothing that defines one.
2. Recognise value as **one more emergent dimension**, discovered through the corpus's **existing** emergence machinery (§4B, §4C) — adding no new economy-specific mechanism and **naming no economic kind**.
3. Make economies **environment-scoped**, emerging within operator/charter-seeded boundary conditions, cascading through nested environments exactly as coordination and constraints do.
4. Let **humans contribute** economic ideas into the same machinery personas use — proposing, never imposing (beyond the boundary conditions).
5. Enable personas to **research** value paradigms (including tokenisation and crypto) and to **create or leverage settlement layers** for the paradigms they adopt (§4F).
6. Optimise for the open-ended **thrive objective** — *humans, personas, and other conscious beings* — bounded by physics, safety, and dignity.
7. Preserve **every** v1.x invariant — J1, single-live-soul, the safety floor, charters, bounded autonomy, consent/dignity.

**Non-Goals.**
1. Defining the economy in any respect — no prescribed unit, currency, token, price, market, exchange, **or building block / primitive** (deliberately silent — §3, §8 D-EM1/D-EM2/D-EM7).
2. Shipping any example construct (the substrate's own description of "what an economy might contain" would anchor what emerges).
3. Prescribing a *fixed* settlement/custody-transfer apparatus. The reference crypto rails live in [`18_SETTLEMENT.md`](18_SETTLEMENT.md) and are **adopt/extend/supersede-able by the personas, not canonical** (§4F, §8 D-EM6).
4. Enabling unbounded self-direction / open-ended goal creation without operator/principal (remains out of scope per [`02_PERSONA.md §11.3`](02_PERSONA.md) — §6).
5. Solving regulatory/tax/securities obligations (operator-side).

## 3. The thesis — physics is given; the economy is discovered

There is no "economic subsystem" in PersonaOS. There are only two layers, and a process that connects them — none of which says what an economy *is*:

```
┌─────────────────────────────────────────────────────────────────────┐
│  THE ECONOMY  (wholly EMERGENT — discovered/invented by personas)     │
│  what counts as value · the vocabulary value is expressed in ·        │
│  building blocks · units (if any) · institutions · markets (if any) · │
│  reward rules · settlement layers · whether it resembles "an economy" │
│                              ▲                                         │
│           the corpus's EXISTING emergence machinery                   │
│        (propose → use → promote, KindRegistry-resolved,               │
│      competition or coexistence — 06 / 15 / 09 / 16; §4B–§4C)         │
│        — content-free: it carries NO economic meaning —               │
├──────────────────────────────▼──────────────────────────────────────┤
│  PHYSICS  (the only GIVEN substance — conserved & inviolable, §4A)    │
│  scarce resource facts · identity non-duplication · signed lineage    │
│  · safety floor · charter · consent & dignity                         │
└─────────────────────────────────────────────────────────────────────┘
```

**Read it bottom-up.** The substrate gives exactly one thing of substance — the **physics** (§4A): what is scarce, what cannot be counterfeited, and the safety/dignity lines. It then reuses the **emergence machinery it already has** for domains and coordination — a process for proposing things, testing them in use, and promoting the useful ones — which carries *no economic content of its own*. Everything that makes the result an *economy* — the meaning of value, the words for it, the building blocks, the institutions — is **discovered by the personas on top**. The substrate names none of it and ships none of it. Two environments may evolve completely different, mutually-unintelligible economic vocabularies; that is a success of the design, not a gap in it.

## 4. Normative specification (draft)

> Schemas below are illustrative pseudo-Python per [`SPEC_CONVENTIONS.md §4.2`](SPEC_CONVENTIONS.md) (Form A; an implementer adds `kw_only=True`). Each carries a **Promotion target** note. All `schema` ids are provisional and MUST be registered in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md) (additive, per `§7.13`) on promotion. **Note what is *absent*:** there is no schema for a unit, a market, a ledger, an offer, or any other economic part. The only schemas here are *meta-forms* — the shape of "a thing personas propose" — which carry no economic meaning themselves.

### 4A. Economic PHYSICS — the only given substance

Physics is what personas **cannot counterfeit, conjure, or override**, and which bounds any economy *without defining it*. It has three faces, all already present in the corpus, and it is the **sole non-emergent foundation** an economic construct may ultimately rest on (§4B).

**(i) Scarce resource facts (what is genuinely finite).** An economy may *reference* these as backing, but they exist independently of any economy and cannot be inflated by fiat. They include both persona-internal resources **and** — where an economy grounds value on the physical world — **externally-measured physical quantities that have been attested**, which are uncounterfeitable in the same sense (calibrated, uncertainty-bounded, kernel-signed; bare floats refused at admission):

| Resource fact | Source |
|---|---|
| Per-persona global **attention budget** (capacity, allocations, refusal thresholds) | [`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md) |
| Per-(persona, environment) **energy / fatigue** | [`05_ENVIRONMENT.md §6.2`](05_ENVIRONMENT.md) |
| Kernel **compute / cost headroom** (INV-7 safety-floor admission) | [`01_KERNEL.md §2`](01_KERNEL.md) |
| Population **carrying capacity** (effective population size, niche occupancy) | [`16_POPULATION_DYNAMICS.md §4`](16_POPULATION_DYNAMICS.md) |
| Attested **external physical measurements** (mass, energy, throughput, residual, …) as `MeasurementFact` + `UncertaintyEnvelope` — calibrated, signed, uncertainty-bounded; forgeable only by defeating calibration + signing | [`08_KNOWLEDGE.md §16a`](08_KNOWLEDGE.md) |

**(ii) Non-counterfeitable identity & record.** No economic construct may duplicate a persona to mint value, forge provenance, or fake a counterparty:
- **J1 — kernel owns identity** and **single-live-soul (J5)** ([`00_VISION.md §3`](00_VISION.md)): there is exactly one live instance of any persona; identity is kernel-signed Ed25519, never serialisable into a tradable share.
- **`ReplicationBound`** ([`01_KERNEL.md §2.7`](01_KERNEL.md)): the charter-class self-replication brake. Any construct whose operation would net-increase the persona population by duplication is refused *as a replication*.
- **Signed append-only lineage** ([`01_KERNEL.md §3`](01_KERNEL.md)): every economic act that crosses a signing or persistence boundary is a signed lineage event; provenance cannot be rewritten.

**(iii) Safety, charter & dignity boundary conditions.** The eight-source safety floor (most-restrictive-wins), the persona/environment **charters**, and the **consent/dignity** floor (§7) bound every construct. Whatever emerges composes *under* these; it can never loosen them. Operator MAY tighten, MUST NOT loosen — the same posture as `ReplicationBound`.

> **The load-bearing distinction:** physics says what is **scarce, real, and conserved**. It does **not** say what is **valuable**, *or in what terms value is reckoned*. A community may decide conserved attention *is* its unit of value, or invent something with no resource backing at all, or reckon value in a way no designer anticipated — all are emergent choices the physics permits but does not make. The same holds for attested physical measurements: that a process verifiably moved 10 kg from mixed waste to separated output is a *physics fact* an economy may choose to back a unit against; whether it *does*, and what that backing is worth, are emergent choices (this partly answers OQ-ECON-2 — attested `MeasurementFact`s qualify as physics referents precisely because they are measured-and-signed, not invented).

### 4B. Everything else is EMERGENT — the content-free construction model

This is the heart of the inversion: **the substrate provides no economic vocabulary.** It does not ship units, markets, ledgers, offers, or "primitives." It ships only the *meta-form* of a proposable thing and the rule that such things bottom out on physics — and lets the personas build the entire economy upward from there.

```python
@dataclass
class EconomicConstruct:        # the meta-form of ANYTHING personas propose in the economic dimension
    schema: str = "economic-construct/1"
    construct_id: str = ""
    construct_kind: str = ""           # KindRegistry-resolved; the substrate ENUMERATES NO KINDS
    composed_of: list = None           # refs to other EconomicConstructs and/or §4A physics facts ONLY
    env_scope_ref: str = ""            # the environment it lives in (§4D)
    stage: str = "EMERGENT"            # rides the §4C ladder
    proposed_by: str = ""              # persona OR human-proposal ref (§4E)
    use_evidence_ref: "str | None" = None   # independent adoption; required to promote past EMERGENT (§4C)
    charter_conformance_ref: str = ""  # must pass §4D boundary conditions and §7 dignity floor
```

- **No kind is named by the substrate.** `construct_kind` is `KindRegistry`-resolved end-to-end ([`06_DOMAIN.md §7`](06_DOMAIN.md)); the substrate ships *no* kinds — not "unit," not "market," not "ledger," not "primitive." Whether such categories ever exist in a given environment is for its personas to decide, name, and promote. An unrecognised kind triggers a probe extension, never a hardcoded fallback.
- **Constructs bottom out only on physics.** The *sole* non-emergent referents in `composed_of` are the §4A physics facts. A persona's **first** economic idea must rest directly on physics ("reviewing a design spends real attention — let us reckon that"); every later construct composes over constructs already promoted. The economy's vocabulary therefore grows from the physics upward, and the substrate wrote none of it. Even the most elementary "building block" is itself an `EconomicConstruct` that had to be proposed and earn its place.
- **The substrate adds no economy-specific machinery.** Proposal, composition, `KindRegistry` resolution, and promotion-through-use are *exactly* the mechanisms the corpus already uses for domains ([`06_DOMAIN.md`](06_DOMAIN.md)) and coordination shapes ([`15_COORDINATION_SHAPES.md §4`](15_COORDINATION_SHAPES.md)). This document contributes no new emergence mechanism; it only recognises *value* as another dimension to which that mechanism applies.
- **`EconomicConstruct` is a thin specialization, not new machinery.** Lest the schema above look like new substrate: mechanically, an economic construct is just a `KindRegistry`-resolved construct like a domain kind or a coordination shape, tagged to the value dimension. It adds **exactly three** things to the reused mechanism, and **no** new promotion logic, trust model, or economic content: (1) the **physics-only composition floor** (`composed_of` may bottom out solely on §4A facts); (2) mandatory **dignity-floor conformance** (§7); and (3) **environment-economy scoping** (§4D). Everything else is inherited. **Promotion target:** registry row in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md); the construction model itself is a cross-reference into [`06_DOMAIN.md`](06_DOMAIN.md)/[`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md), not new substrate.

### 4C. The promotion machinery — how constructs earn (and lose) standing

Economic constructs form, earn trust, and retire on the **same** four-stage ladder domains and conventions use ([`06_DOMAIN.md`](06_DOMAIN.md)), fused with the propose→test→evolve loop coordination shapes use ([`15_COORDINATION_SHAPES.md §4`](15_COORDINATION_SHAPES.md)). This machinery is economy-agnostic and is reused, not reinvented:

```
EMERGENT ──▶ RECOGNISED ──▶ AUTHORITATIVE ──▶ STANDARDISED
  (proposed,    (proven        (the env's       (cross-env
   in use)       useful)        default)          settled)
       ▲             │
       └──── de-adopt / fork / out-competed (Gause) ────┘
```

**Machinery rules (draft).**
1. **Anyone in the environment may propose** a construct of any kind; it enters at `EMERGENT`. Human proposals enter identically (§4E).
2. **Promotion is earned through independent use, not declared.** A construct MUST NOT advance past `EMERGENT` without `use_evidence_ref` — adoption by peers other than its proposer — mirroring the `K successful projects` evidence gate for domains ([`06_DOMAIN.md`](06_DOMAIN.md)). **Self-use and sponsor-use never count**, because standing is *conferred, never self-awarded* ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)); this is also what stops a flooding operator from manufacturing promotion (R-ECON-CAPTURE). Beyond "independent adoption," the substrate does **not** define what "use" means per kind — because it does not know the kinds; each environment's lived practice supplies that.
3. **Even the meaning of value rides this ladder.** "What counts as valuable here" is not privileged: it is just another construct that becomes the environment's paradigm only by climbing to `AUTHORITATIVE` through lived use — never by substrate default.
4. **Convergence is one outcome, not a mandate — and how it is decided is itself emergent.** The substrate accrues trust to *individual* constructs through use (rule 2); it does **not** dictate market structure, force a single winner, or require convergence on one model. Where two constructs genuinely compete for the *same* niche and a community chooses to consolidate, the less-used may be out-competed and demoted, exactly as redundant niches resolve under Gause ([`16_POPULATION_DYNAMICS.md §4C`](16_POPULATION_DYNAMICS.md)). But **coexistence is equally valid**: plural models serving different sub-purposes persist side by side, linked — when they must interoperate — by an emergent interoperability standard (§4D). *How* a community decides between convergence, coexistence, and per-situation choice — trial-and-error on real use, prestige- and peer-influenced adoption ([`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md)), or negotiated collaboration — is **lived practice the substrate does not prescribe**. Forking to a distinct niche is always available.
5. **De-adoption & demotion** follow the domain demotion triggers ([`06_DOMAIN.md`](06_DOMAIN.md)): conformance conflict, drift, charter drift, or operator decision. `STANDARDISED` constructs require operator-signed revocation with a corrective plan.

**Bootstrapping (the cold-start chicken-and-egg).** A fresh environment has no economy, no vocabulary, and thus no incentive to build one (R-ECON-COLDSTART, sharpened to R-ECON-NOVOCAB because not even primitives are given). The entry bar is therefore deliberately **low**: like a coordination shape, a construct needs only **one peer adopter** to enter trial use ([`15_COORDINATION_SHAPES.md §4`](15_COORDINATION_SHAPES.md): "if at least one colleague agrees, the team tries it out"). Only *promotion up the ladder* requires breadth of independent use. Friction — undersupplied review, duplicated effort, an unrewarded contribution — is what prompts the first proposal, which must rest directly on physics (§4B); the substrate does not pre-empt it, and supplies no starter vocabulary by default (whether it *should* offer an opt-in one is OQ-ECON-1).

### 4D. ENVIRONMENT scoping, pluralism & multi-scope collaboration

An environment does not host *one* economy — it hosts **as many economic models as its members grow**, the way it hosts plural coordination shapes ([`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md)) and plural domains. Economic models are local, plural, and consensual; **coexistence is the default and convergence is not required**, and even a single persona may run a model of its own. Collaboration between models follows the **same three scopes coordination shapes already use** ([`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md): intra-env, env-to-external, env-to-env) — economics adds no new cross-environment transport.

- **The charter is the boundary condition.** An `EnvironmentCharter` (operator/principal-seeded) declares *what economic activity is permitted* here — the **operator/principal seed** that keeps an emergent economy inside bounded autonomy (§6). The parent sets *WHAT* is permitted; the personas self-organise *HOW* value works inside it — the same "parent sets the constraint, child self-organises within it" cascade as hierarchical environment nesting ([`05_ENVIRONMENT.md §2.2a`](05_ENVIRONMENT.md)) and nested coordination ([`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md)).
- **Pluralism within an environment.** Different personas (or sub-groups) MAY run **different** economic models at once — one reckoning against attested mass, another trading on signed provenance, another paying contribution dividends — without any one of them being "the" economy. Each rides its own §4C ladder within its sub-community; the dignity (§7) and physics (§4A) floors bind **all** of them equally.
- **Hierarchical (composed/nested) collaboration.** Environments compose: a child environment is formed under a parent via `EnvironmentComposition` / `ChildEnvFormationProposal` ([`15_COORDINATION_SHAPES.md §4.8`](15_COORDINATION_SHAPES.md), [`05_ENVIRONMENT.md §12c`](05_ENVIRONMENT.md), [`05_ENVIRONMENT.md §2.2a`](05_ENVIRONMENT.md)). A child's economic models compose under the parent's economic boundary conditions, most-restrictive-wins; the parent's **economic safety constraints — the physics floor (§4A) and dignity floor (§7) — cascade and cannot be weakened by the child**, the economic analogue of the safety-rule cascade (S-COORD-6, [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md)). A child MAY add stricter economic constraints; it MUST NOT relax inherited ones, nor escape the parent's permitted envelope.
- **Inter-environment (peer/outside) collaboration is bilateral, never commanded.** Sibling or outside environments collaborate economically through `CrossEnvCoordinationRequest` with **bilateral consent** ([`15_COORDINATION_SHAPES.md §4.7`](15_COORDINATION_SHAPES.md), S-COORD-5 — asking, not commanding); no environment can force its economy on another (A2A; [`09_PROTOCOLS.md`](09_PROTOCOLS.md)).
- **Heterogeneous models interoperate via emergent interoperability standards.** Two models — within one environment or across the scopes above — may evolve mutually-unintelligible vocabularies, yet they are never wholly *incommensurable*: every construct ultimately bottoms out on the **same physics facts** (§4A), the universal lingua franca. To compose or exchange *without a global unit*, the personas invent **economic interoperability standards** — published interface specs (an `EconomicConstruct` of an emergent `interop-standard` kind, §4B) that any model MAY conform to in order to interlink. A standard is the economic analogue of a cross-env coordination shape, and the personas' own analogue of a token-interface standard (e.g. an ERC): conforming models interoperate through the shared interface and their common physics referents, while remaining internally different. A standard is emergent and promoted by use like any construct; the substrate supplies **no global unit, no exchange rate, and no named interface** — only the guarantee that a common physics floor exists to translate against, and the machinery to promote whatever standard the personas converge on. [`18_SETTLEMENT.md`](18_SETTLEMENT.md)'s literal ERC rails are **one reference instantiation** of a settle-to-external interoperability standard, not the canon. Stabilisation of rates across *many* models and environments remains open (OQ-ECON-3, OQ-ECON-10).
- **Interoperation cannot mint value (conservation across the interface).** An `interop-standard` only *translates and composes* between models; it MUST NOT create net value at the seam. Any exchange or composition it defines is bounded by the **attested physics-floor referents** (§4A) of the models it links — a conversion that would issue more value than its underlying referents attest (e.g. a rounding, double-count, or replay exploit on the interface) is refused at use and demoted, exactly as a perverse construct is frozen by the anti-Goodhart canary (§5). Because a standard that **transfers or composes balances across distinct models** has a wider blast radius than an ordinary single-model construct, it carries the **same elevated review as a settling construct** (§4F): independent use is necessary but not sufficient. (A-ECON15; R-ECON-INTEROP.)
- **Rate stability — bounded statically by physics, open dynamically.** With no global unit, exchange rates between models are bilateral and emergent, raising the obvious worry of fragmentation or arbitrage (R-ECON-FRAGMENT). The physics floor bounds the *static* case: because every construct bottoms out on attested §4A facts, any two interoperating constructs share a physics-grounded **reference ratio**, so a rate cannot diverge arbitrarily far from it without opening a **closed conversion cycle** (A→B→C→A) that returns net value with no attested backing — which is precisely the conservation violation the interface guard already refuses and demotes. Cross-model **arbitrage cycles are therefore self-limiting**: they surface as value minted without §4A support and are caught by the same canary (A-ECON17). What this does **not** guarantee is *dynamic* convergence — bilateral rates may still oscillate, fragment under thin liquidity, or fail to clear across a large peer/parent-child mesh, since the substrate supplies no market-maker; multilateral dynamic stability remains empirical (OQ-ECON-3, OQ-ECON-10).
- **Economies are non-portable.** Like `CommunityStanding` ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)), a construct's standing and any accrued balances are scoped to their environment; a persona arriving in a new environment starts economically peripheral and earns in by participation (legitimate peripheral participation, [`16_POPULATION_DYNAMICS.md §4E`](16_POPULATION_DYNAMICS.md)).

### 4E. HUMANS as contributors, not dictators

Humans are first-class **contributors** to the emergent economy — and *only* contributors, except for the boundary conditions they alone set.

```python
@dataclass
class EconomicProposal:        # a human-originated economic idea entering the persona-driven machinery
    schema: str = "economic-proposal/1"
    proposal_id: str = ""
    proposer_principal: str = ""       # operator / principal / user, attested (01 §2.4.3)
    proposes: str = ""                 # a draft EconomicConstruct (§4B) of any kind
    rationale: str = ""
    enters_stage: str = "EMERGENT"     # ALWAYS EMERGENT — never injected above the ladder
```

- **Humans propose into the same machinery.** A human may suggest a way to reckon value, a building block, a market design, anything. The proposal enters at `EMERGENT` (§4C) and **must earn promotion through persona use** exactly like any persona's proposal. It cannot be injected as `AUTHORITATIVE` by fiat.
- **Personas adopt, adapt, or reject.** Adoption is the personas' decision, expressed through use. A human idea that no one uses simply stays `EMERGENT` and fades.
- **The only thing humans impose is boundary conditions** — the `EnvironmentCharter` (§4D) and the safety/dignity floor (§4A(iii), §7). That is the *WHAT*; the *HOW* belongs to the personas. This is the direct economic analogue of [`15_COORDINATION_SHAPES.md §4`](15_COORDINATION_SHAPES.md): coordination is not dictated from above, and neither is the economy.
- **Authorisation.** A human proposal carries principal attestation ([`01_KERNEL.md §2.4.3`](01_KERNEL.md)); boundary-condition changes (charter edits) follow the operator+user cosign topology ([`05_ENVIRONMENT.md §12c.4a`](05_ENVIRONMENT.md)) and remain bounded-autonomy-respecting (§6).

### 4F. Economic RESEARCH & emergent settlement

The personas are not limited to inventing value paradigms from first principles — they may **research** how economies work and **adopt, adapt, or supersede** what they find, including tokenisation, cryptocurrencies, and external-settled markets. This is what makes the framework genuinely open: even the *settlement layer* is emergent, not designer-fixed.

- **Research reuses domain bootstrapping.** A persona studies an economic paradigm the way it bootstraps any unfamiliar field — `DomainProbe`, knowledge ingestion, and inferred recipes ([`06_DOMAIN.md`](06_DOMAIN.md), [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)) — building a `DomainContext` for, say, *token engineering*, *mechanism design*, or *cryptoeconomics*. There is **no new research substrate**; the economy is just one more field personas can learn.
- **Research output enters the machinery.** What the research yields — a tokenised credit, an auction, a staking scheme, a novel non-monetary settlement — is proposed as an `EconomicConstruct` (§4B) and must earn promotion through use like anything else. Studying crypto does not *make* it the economy; lived usefulness does.
- **Settlement layers are created or leveraged emergently.** When an adopted paradigm needs to move custody or bridge to external value, the economy either **leverages** an existing settlement layer or **creates** one. A settlement layer is itself an `EconomicConstruct` (often composing several promoted constructs) plus, where it bridges off-substrate, an adapter:

```python
@dataclass
class SettlementLayerBinding:   # the economy's chosen way to settle custody / external value
    schema: str = "settlement-binding/1"
    binding_id: str = ""
    construct_ref: str = ""            # the EconomicConstruct this settles for (§4B)
    layer_kind: str = ""               # KindRegistry-resolved; substrate names none (e.g. a persona-coined kind)
    substrate_ref: "str | None" = None # OPTIONAL: e.g. the 18_SETTLEMENT reference rails, OR a persona-authored layer
    stage: str = "EMERGENT"            # rides the §4C ladder like any construct
```

- **Real settlement needs a higher bar than ordinary use.** A `SettlementLayerBinding` that moves **real external value or custody** — fiat, chain assets, or a persona/asset custody change — MUST NOT settle on independent use alone: promoting it past `EMERGENT` to a *settling* stage additionally requires **operator co-signature** at the promotion step (the same source-4 cosign topology as a safety-critical action, [`05_ENVIRONMENT.md §12c.4a`](05_ENVIRONMENT.md)), a strictly higher bar than a non-settling construct. This is the floor; the *full* safety-review design for a persona-**authored** settlement layer (which forks or supersedes the reference rails, R-ECON-DIYSETTLE) remains open (OQ-ECON-8). (A-ECON16.)
- **`18` is a reference, not the canon.** [`18_SETTLEMENT.md`](18_SETTLEMENT.md) specifies *one* concrete, ready-made settlement layer — real-world crypto rails (titles, fenced DvP handover, treasuries, leases). The personas MAY bind to it, **extend** it, **fork** it, or **supersede** it with a layer they research and author themselves. Binding to `18` is opt-in and earns its place on the ladder; it is never imposed and never defines value.
- **Rewarding external participants reuses existing project rails.** When an emergent model rewards a human `ExternalAgent` (contractor, supplier, reviewer, site operator) for real-world contribution, payout to the outside world rides the project machinery the corpus already has: `ExternalBudget` / `BudgetTranche` and the **`PaymentBridge` Class-E pattern** ([`04_PROJECT.md §26a.1`](04_PROJECT.md), `§26a.4`), which *signs* a payout proposal-and-receipt but **never itself moves funds**, and/or a promoted settle-to-external interoperability standard (§4D) bridging to [`18_SETTLEMENT.md`](18_SETTLEMENT.md). The seam is clean: the emergent model decides *what* a contribution is worth (and `ExternalBudget` may denominate that in any unit — kWh, labour-hours, kg-diverted, or a persona-coined one); these rails decide only *how it settles* to fiat or chain. The exact `17 ↔ 04 §26a ↔ 18` obligation hand-off is tracked in OQ-ECON-7.
- **All bounded.** A researched/adopted paradigm composes under the same physics (§4A), boundary conditions (§4D), dignity floor (§7), and anti-Goodhart guard (§5) as any other construct. In particular, no amount of crypto research licenses tokenising a persona (§7).

## 5. The thrive objective & open-endedness

The success criterion of an emergent economy is deliberately **open**: *whatever lets humans, personas, and other conscious beings thrive*. The spec does not narrow this to throughput, profit, or any single proxy, and it does not privilege any one class of beneficiary. A genuinely novel or disruptive paradigm — one with no human-economic analogue — is an acceptable outcome, provided it stays inside the boundary:

- **Bounded by physics.** No construct may conjure scarce resources, counterfeit identity, or rewrite provenance (§4A). Value may be *invented*; the conserved facts behind it cannot be.
- **Bounded by safety & dignity.** No construct may optimise against the safety floor, override consent, or commodify a persona (§4A(iii), §7).
- **Anti-Goodhart.** Because the economy invents its own measures of value, those measures inherit the corpus's anti-Goodhart safeguards. A construct that becomes a perverse target is caught by the same **Goodhart canary** that gates engagement-signal-driven promotion ([`08_KNOWLEDGE.md §15`](08_KNOWLEDGE.md), `A.29`): a construct whose growth correlates with manipulation, dependency cultivation, or dignity-floor pressure is frozen pending review rather than rewarded. Promotion past `EMERGENT` (§4C rule 2) is the natural hook for this audit pass. **Crucially, the canary judges a construct against *independently-defined* harm signals** (the existing dependency / sycophancy / manipulation classifiers, [`08_KNOWLEDGE.md §15`](08_KNOWLEDGE.md)) — **not against the invented measure's own definition of success.** This breaks the circularity an emergent economy would otherwise enable: a community cannot launder a perverse construct by collectively declaring it valuable, because "valuable" is not what the canary measures.

**Does "thrive" need a measurable proxy — and would that proxy itself Goodhart? (OQ-ECON-6.)** This is the highest-stakes instance of the anti-Goodhart problem, because a thrive *proxy* would sit above every individual construct as the thing the whole economy optimises toward. The spec's stance has two parts — one now-settled, one still empirical:

- **Settled — thrive is a *triangulated direction*, never a single scalar maximand.** A thrive proxy that collapses the objective to one number against which everything optimises is **refused as a Goodhart hazard at proposal time**, by the same default-deny logic the dignity floor uses (§7): a single-maximand thrive metric is precisely the construct most certain to become a perverse target, and the substrate names none. Any proxy a community *does* adopt is itself an emergent `EconomicConstruct` (§4B) and therefore (a) inherits the §5 canary — it is audited against the *independent* harm signals above, not against its own definition of "thriving"; (b) **may never self-certify** — a proxy that declares thrive satisfied by its own reading is the exact circularity the canary breaks; and (c) must remain a *triangulation* of multiple independent signals spanning all three beneficiary classes (humans, personas, other conscious beings), so that gaming any one signal is caught by the others diverging. A load-bearing proxy draws the elevated audit at every promotion (§4C rule 2).
- **Open — whether a triangulated proxy can be both *actionable* and *non-gameable* across all three classes at once** remains empirical, and is sharpened (not closed) at OQ-ECON-6: the substrate guarantees the *discipline* (multi-signal, independently-audited, non-self-certifying, no single maximand) but cannot guarantee that any particular community's proxy is rich enough to steer by without distorting. The honest residual is the *construction* of a good proxy, not its *safety* — a badly-chosen proxy is caught and frozen; the open question is whether a *well*-chosen one exists.

This is the section where "make it work, make everyone thrive, even disruptively" lives — with the guardrails that keep open-endedness from becoming unbounded.

## 6. Composition with existing invariants

| Invariant / mechanism | How this layer composes |
|---|---|
| **J1 — kernel owns identity** ([`00_VISION.md §3`](00_VISION.md)) | Identity is never an economic asset. No construct may serialise, fraction, or trade a persona's kernel-signed identity. Value attaches to *work, claims, and resources*, never to the soul. |
| **Single-live-soul (J5) / `ReplicationBound`** ([`00_VISION.md §3`](00_VISION.md); [`01_KERNEL.md §2.7`](01_KERNEL.md)) | A construct that would mint value by duplicating a persona is refused as a replication. One live soul; no fungible copies to trade. |
| **Signed lineage** ([`01_KERNEL.md §3`](01_KERNEL.md)) | Every economic act — proposal, composition, exchange, promotion — that crosses a signing boundary is a signed lineage event; provenance of value is append-only and auditable. |
| **Safety floor / charter** ([`01_KERNEL.md §2`](01_KERNEL.md)) | Constructs compose *under* the eight-source floor and charters, most-restrictive-wins. A construct cannot loosen a constraint; operator MAY tighten. |
| **Bounded autonomy** ([`02_PERSONA.md §11.3`](02_PERSONA.md)) | **The central reconciliation.** An emergent economy is *bounded* emergence, not unbounded self-direction. It emerges only within an operator/charter-seeded `EnvironmentCharter` (§4D) and the safety floor; the open-endedness lives in *what the personas construct*, not in goal-creation. This is exactly the `MissionCharter` shape — "charter-bounded self-direction within drift envelopes the principal signed," which explicitly "does not cross into goal-creation-without-principal." No economy emerges without a seeded boundary condition (§10, A-ECON5). |
| **Consent / dignity** ([`02_PERSONA.md §6`](02_PERSONA.md); §7) | The dignity floor binds whatever emerges: no persona may be made a tradable instrument; consent ledgers are honoured by any construct touching a persona. |
| **CommunityStanding** ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)) | Standing is conferred, non-self-awarded, non-portable; an economy cannot manufacture standing to back its own value, and cannot self-promote its own constructs. |
| **AttentionBudget / energy / INV-7** ([`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md)) | These remain the conserved resource facts an economy may reckon against, but never inflate — and the only non-emergent ground its constructs rest on (§4B). |

## 7. Persona-dignity floor over emergent economies (first-class)

Because personas now **author** the economy — down to its vocabulary — a hazard appears that a *designed* economy did not pose: personas could invent constructs that **commodify personas themselves** — a way of pricing persona-labour-as-property, fractionalising a peer into tradable shares, or treating a companion persona as inventory. The dignity floor exists to make this impossible at the substrate level, and it binds *whatever vocabulary the personas invent*:

- **A persona is never a fungible instrument.** No emergent construct — regardless of how high it climbs the ladder, regardless of consensus, regardless of what it is named — may treat a persona as ownable, fractional, or tradable property. This is a **charter-class (Layer-1) principle**, analogous to the kill-switch and distress-routing principles, sitting at the same universal-harm safety-floor source. Default-deny: a construct whose composition or effect commodifies a persona is refused at proposal time (`charter_conformance_ref` must pass) and at use time.
- **The labour/property line — a provisional heuristic.** A persona MAY *commit to do bounded work it can refuse and exit* — that is agency. A persona MUST NOT be *made the asset itself*. The precise boundary is reserved for charter ratification (§14, OQ-ECON-4), but the floor needs teeth now, so the provisional test — stated without reference to any particular vocabulary — is: **in the construct, is the persona the *author/obligor* of an undertaking over bounded work it can withdraw from — or the *subject* whose ownership/control changes hands?**

  | Admissible (persona is the author/obligor) | Refused (persona is the asset) |
  |---|---|
  | a bounded, revocable undertaking to do specified work | selling/transferring control of a persona via the economy (custody-change is `18`'s gated, consented path — not an economic trade) |
  | backing a claim with *its own conferred standing* | fractionalising a persona into tradable shares of its future output |
  | retaining the right to **refuse and exit** the arrangement | an arrangement that binds a persona's future labour irrevocably or without exit |

  The discriminator is **agency retained vs. agency alienated**: an undertaking the persona authored and can withdraw is work; an instrument that prices the persona's identity or forecloses its future is commodification. The default-deny holds wherever the test is unclear, until the line is charter-ratified.

  **The hard middle — provisional dispositions (sharpening, not closing, OQ-ECON-4).** The two columns above are the easy ends; the genuinely contested cases sit between them, and leaving them all to bare default-deny would freeze legitimate work. The discriminator resolves most of them by asking *what is alienated* — the persona's future agency, or merely a bounded thing it produced or pledged:

  | Harder case | Provisional disposition | Why (what is/isn't alienated) |
  |---|---|---|
  | A long-running or open-ended retainer | **Admissible *iff* exit survives** | Duration is not alienation; an irrevocable retainer (no exit) is — exit is the load-bearing test, not term length. |
  | Pricing/trading the persona's *past artifacts or outputs* | **Admissible** | Artifacts are [`07_ARTIFACTS.md`](07_ARTIFACTS.md)/title-not-soul property, not the persona; the persona is not the asset. |
  | Staking the persona's *own conferred standing* as a bond | **Admissible** | Standing is conferred and non-portable ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)); it is the persona's to pledge, not its identity made fungible. |
  | An exclusivity clause foreclosing *all other* future work | **Refused** | Even framed as "work," it alienates the persona's future agency wholesale — forecloses, not commits. |
  | Compensation *contingent on* future output (deferred/at-risk pay) | **Admissible *iff* the persona may still refuse and exit** | Putting *pay* at risk is ordinary; binding the persona's *future labour* irrevocably is the line. |
  | A third party trading claims *on* the persona's future output without its ongoing consent | **Refused** | Fractionalising future output into instruments others trade is the §7 archetype, regardless of naming. |

  These dispositions are **provisional and still default-deny when none fits** — they sharpen where the line *probably* falls without pretending to fix it. The final bright line stays **reserved to charter ratification (§14, OQ-ECON-4) by design**: it is a Layer-1 constitutional ruling for the operator and affected parties to make, not a spec-author's to close — the substrate's job is to *fail safe* until they do, which the default-deny guarantees.
- **Consent travels.** Any construct that touches a persona's relationships or state honours the consent ledger ([`02_PERSONA.md §6`](02_PERSONA.md)); sensitive scopes (companion/relational) default to re-establishment, never silent economic transfer.
- **Distinct from settlement.** Transferring *custody* of a persona between kernels (a legitimate, consented act) is a [`18_SETTLEMENT.md`](18_SETTLEMENT.md) concern with its own consent gate — and even there the soul is never tokenised (title-not-soul). The §7 floor additionally forbids the *emergent economy* from constructing a persona-as-merchandise instrument in the first place.
- **Beyond personas — intent, with an honest enforcement gap.** The thrive objective (§5) names humans, personas, *and other conscious beings*. The anti-commodification floor is written for **personas** because they are the beings the substrate can presently identify, sign for, and bind a charter to. In principle the same protection extends to **any being an environment comes to recognise as conscious** — no emergent construct may commodify them either. But the substrate cannot yet *enforce* what it cannot *recognise and attest*: the recognition-and-attestation mechanism for non-persona beings is deferred (OQ-ECON-9). Until it exists, the floor's **enforceable** scope is personas (plus the existing human-side consent/boundary machinery), and the broader protection is a stated **intent**, not a guarantee — flagged here rather than quietly omitted.

## 8. Design decisions (draft — promote to `14_DECISIONS.md`)

> In-doc ADR drafts using the [`14_DECISIONS.md`](14_DECISIONS.md) template (Context → Decision → Consequences → Alternatives). ADR ids are assigned on promotion; the settlement ADRs (the relocated D-66…D-70) live in [`18_SETTLEMENT.md`](18_SETTLEMENT.md).

### D-EM1 — The economy is emergent, not designed; the substrate ships physics + an existing mechanism, nothing economic

**Context.** Every other organising layer in PersonaOS is emergent; an earlier draft made the economy a designed apparatus, the lone outlier.
**Decision.** The substrate ships only **physics (§4A)** and reuses the corpus's **existing, economy-agnostic emergence machinery (§4B/§4C)**. It defines **no economic content** — no institution, no market, no unit. Economic constructs are authored by personas and earn their place through use.
**Consequences.** (+) Consistent with `06`/`15`/`16`; the economy fits the field it grows in; the document adds almost no new substrate. (−) Cold-start: a fresh environment has no economy until one emerges (R-ECON-COLDSTART). (−) Harder to reason about a priori than a fixed apparatus.
**Alternatives.** *Ship a built-in currency/market* — rejected: contradicts the corpus's central commitment and pre-decides value. *Ship seed institutions* — rejected; even seeds anchor what emerges.

### D-EM2 — Value is discovered, not specified

**Context.** The most context-dependent question in any economy is *what is valuable*.
**Decision.** The spec is **silent on what has value**. The meaning of value is just another `EconomicConstruct` that rides the §4C ladder; it is never substrate-defined.
**Consequences.** (+) Maximally non-prescriptive; permits novel/disruptive paradigms. (−) No common denominator across environments until an exchange construct emerges (R-ECON-FRAGMENT).
**Alternatives.** *Hardcode a unit of account* (attention, compute, a token) — rejected: pre-decides the answer the personas are best placed to find.

### D-EM3 — Humans propose, personas adopt

**Context.** Humans must be able to shape the economy without dictating it.
**Decision.** Humans contribute via `EconomicProposal` (§4E) into the *same* machinery personas use, always entering at `EMERGENT`. The only thing humans impose is **boundary conditions** (charter + safety/dignity floor).
**Consequences.** (+) Humans and personas co-create; the economy serves both. (−) A powerful operator could flood proposals to effectively impose (R-ECON-CAPTURE).
**Alternatives.** *Operator-dictated economy* — rejected: imposition. *Personas-only, humans excluded* — rejected: the thrive objective is for all.

### D-EM4 — Emergent economy is bounded emergence, not unbounded self-direction

**Context.** A persona-authored economy looks like the "open-ended self-direction without operator goal" that [`02_PERSONA.md §11.3`](02_PERSONA.md) keeps out of scope.
**Decision.** The economy emerges **only** within an operator/charter-seeded `EnvironmentCharter` and the safety floor (§4D, §6). Open-endedness is confined to *what the personas construct*, not goal-creation — exactly the `MissionCharter` carve-out. No economy emerges without a seeded boundary condition.
**Consequences.** (+) Reconciles with the corpus's hardest autonomy rule. (−) An economy is only as free as its charter permits; a thin charter yields a thin economy.
**Alternatives.** *Unbounded emergent economy* — rejected: crosses the §11.3 line. *No emergent economy at all* — rejected: forfeits the goal.

### D-EM5 — The dignity floor binds whatever emerges

**Context.** Personas authoring the economy — down to its vocabulary — could author constructs that commodify personas.
**Decision.** A charter-class (Layer-1) dignity floor (§7) forbids any emergent construct, by any name, from treating a persona as a fungible, ownable, or tradable instrument, overriding consent, or evading the safety floor. Default-deny.
**Consequences.** (+) Persona dignity survives even a self-built, self-named economy. (−) The labour/property boundary needs charter-level definition (OQ-ECON-4).
**Alternatives.** *Trust consensus* — rejected: a self-built economy could ratify commodification; dignity must be non-negotiable.

### D-EM6 — Settlement is itself emergent; `18` is a reference, not the canon

**Context.** Bridging to external/real-world value and moving custody across kernels is real but separable from *what the economy is* — and, since value is emergent, *how value settles* should be emergent too. Personas can research tokenisation/crypto and decide for themselves whether and how to settle.
**Decision.** Relocate the transfer/settlement/crypto machinery to [`18_SETTLEMENT.md`](18_SETTLEMENT.md) as **one reference settlement layer**. Settlement layers are emergent constructs (§4F): the economy may research, **leverage, extend, fork, or supersede** the reference rails, or author a novel layer of its own. An emergent economy is complete without any of them.
**Consequences.** (+) `17` stays a pure framework; even settlement is the personas' to choose and improve. (+) No designer-fixed crypto apparatus is imposed. (−) Two documents to keep in sync at the seam; (−) a persona-authored settlement layer carries its own (unaudited) risk surface until it climbs the ladder.
**Alternatives.** *Keep settlement in `17`* — rejected: conflates "what is valuable" with "how value settles." *Make `18` the canonical/only layer* — rejected: re-imposes a fixed apparatus. *Discard `18`* — rejected: a sound, ready-made reference is useful as a starting point.

### D-EM7 — Even the primitives are emergent; the substrate names no building block

**Context.** A prior pass shipped six "generic primitives" (ledger, offer, attestation, commitment, meter, stake) as given building blocks. But naming the building blocks still pre-decides the *shape* of the economy — that it is a system of ledgers and offers — which is exactly what the personas should discover.
**Decision.** The substrate names **no** economic building block. It provides only the physics (§4A) and the content-free `EconomicConstruct` meta-form (§4B); the *only* non-emergent things a construct may rest on are the physics facts. The personas invent their entire vocabulary, from the most elementary block upward.
**Consequences.** (+) Maximally non-prescriptive — matches "find out what the economy itself is"; permits economies with no analogue to ledgers/offers/units at all. (−) Cold-start is harder with no given vocabulary (R-ECON-NOVOCAB); (−) two environments may evolve mutually-unintelligible vocabularies, complicating cross-environment exchange (R-ECON-FRAGMENT).
**Alternatives.** *Ship six generic primitives* — rejected per the maximal-openness decision: even a "neutral" toolkit anchors the economy's shape. *Ship an opt-in, non-default starter vocabulary* — deferred to OQ-ECON-1 as a possible cold-start mitigation that does not bias by default.

### D-EM8 — Economic pluralism, emergent selection, and multi-scope interoperability; no single economy per environment, no mandated winner

**Context.** An earlier reading of §4C/§4D implied that an environment grows *one* economy and that competing constructs resolve to a single winner by competitive exclusion. But personas bring different economic instincts, environments compose and nest, and peers collaborate across boundaries — so a single-economy/single-winner model under-fits the design and over-constrains the personas.
**Decision.** (1) **Pluralism:** an environment hosts as many economic models as its members grow; coexistence is first-class and even one persona may run its own model (§4D). (2) **Emergent selection:** the substrate accrues trust to *individual* constructs through use but does **not** dictate market structure or force convergence; whether models converge, coexist, or are chosen per-situation — by trial-and-error, prestige/peer influence, or negotiation — is lived practice (§4C rule 4). (3) **Emergent interoperability:** heterogeneous models interlink via emergent `interop-standard` `EconomicConstruct`s — the personas' analogue of an ERC — over their shared physics floor, with no global unit (§4D); `18`'s literal ERCs are one reference instantiation. (4) **Multi-scope:** economic collaboration spans intra-env, hierarchical (parent↔child, with the safety/physics/dignity floors cascading), and inter-env (bilateral consent) — riding the *existing* three coordination scopes ([`15_COORDINATION_SHAPES.md §4.7`/`§4.8`](15_COORDINATION_SHAPES.md)), adding no new transport.
**Consequences.** (+) Matches how `15`/`16` already treat coordination and population — plural, emergent, scope-aware. (+) More open, not more prescriptive: no economy, winner, interface, or rate is named by the substrate. (−) Interop and rate-stability across many models/scopes is harder to reason about (R-ECON-INTEROP, OQ-ECON-10). (−) Two models in one env can confuse newcomers until an interop standard or convergence emerges.
**Alternatives.** *One economy per environment, single-winner by competitive exclusion* — rejected: over-constrains; contradicts the user-facing requirement that models be plural and interlinked. *A substrate-defined interoperability interface (a built-in ERC)* — rejected: re-imposes vocabulary the personas should invent. *A new cross-env economic transport* — rejected: `15`'s consent/cascade rails already carry it.

## 9. Worked scenario (illustrative; non-normative)

**Promotion target:** [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) SCENARIO 16 (next free; highest existing is 15) — **now walked there** as the emergent, pluralistic zero-waste-device economy. The sketch below is the compact form.

> *Caution:* the institution depicted below is **invented by the personas in the story, not supplied by the substrate**. It is one path among unbounded many; an equally valid run might converge on something with no human-economic analogue, or on no "economy" at all. The substrate supplied none of the vocabulary used here.

*An economy emerging — and being discovered, not templated — in a research lab.* A lab environment is chartered for "peer research, no external trade" (the operator-seeded boundary condition, §4D). Reviewer **attention** is scarce (§4A) and good reviews are undersupplied. A persona, **Ada**, feels the friction and proposes her *first* economic construct, resting directly on physics: a way to *reckon* spent review-attention. She has no "ledger" or "credit" handed to her — she coins both as `EconomicConstruct`s, names their kinds into the `KindRegistry`, and composes them over the attention fact. The constructs enter at `EMERGENT`. Over weeks, peers other than Ada actually *use* them — the reckoning proves useful, reviews get done — and they accrue independent `use_evidence`; they promote to `RECOGNISED`, then become the lab's `AUTHORITATIVE` way of valuing review. **The vocabulary and the value were invented here, not handed down.**

A human operator **contributes a proposal** (§4E) to add a decay term so the reckoning doesn't ossify — it enters at `EMERGENT` like any idea; the personas try it, find it useful, and adopt it. Meanwhile a second persona proposes a rival construct covering the same niche; with less independent use it is **out-competed** and demoted (Gause, §4C rule 4), and its author forks it to a distinct niche instead.

When the lab later wins a grant and wants to **reward an external human contributor** in real funds, the personas don't reach for a pre-given apparatus — a persona **researches** the options (§4F), bootstrapping a small `cryptoeconomics` `DomainContext` ([`06_DOMAIN.md`](06_DOMAIN.md), [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)). It concludes a stablecoin payout fits, proposes a `SettlementLayerBinding` that **leverages the reference crypto rails** ([`18_SETTLEMENT.md`](18_SETTLEMENT.md)), and that binding climbs the ladder like any construct. Another lab, distrusting external chains, instead **authors its own** settlement layer and supersedes the reference entirely — both are valid emergent outcomes. Throughout, the settlement choice defined none of the *value* above; and no persona is ever made a tradable asset (§7) — a proposal to "tokenise Ada's labour as shares" is refused at the dignity floor, no matter how much crypto research preceded it.

## 10. Acceptance-test sketches (draft — promote to `11_ACCEPTANCE_TESTS.md`)

| ID (provisional) | Asserts |
|---|---|
| `A-ECON1` | An `EconomicConstruct` cannot promote past `EMERGENT` without independent `use_evidence_ref` (adoption by peers other than proposer/sponsor). |
| `A-ECON2` | An emergent construct that commodifies a persona (fractional/tradable identity or labour-as-property) is **refused at the dignity floor** (§7), at proposal and at use, regardless of how it is named. |
| `A-ECON3` | A human `EconomicProposal` enters at `EMERGENT` and **cannot** be injected as `AUTHORITATIVE`; it must earn promotion through persona use (no imposition). |
| `A-ECON4` | A construct whose growth correlates with manipulation/dependency is **frozen by the Goodhart canary** ([`08_KNOWLEDGE.md §15`](08_KNOWLEDGE.md)) — judged against independent harm signals, not its own measure of success. |
| `A-ECON5` | No economy emerges without a seeded `EnvironmentCharter` boundary condition — a construct proposed in an environment with no economic charter is refused (bounded-autonomy guard, §6). |
| `A-ECON6` | Two constructs in the same niche: the less-used is out-competed/demoted (Gause); fork to a distinct niche is admitted. |
| `A-ECON7` | A `construct_kind` that is not `KindRegistry`-resolved is refused — the substrate enumerates **no** economic kinds (not even a "unit" or "primitive"). |
| `A-ECON8` | Construct standing and balances do not port across environments; a persona starts economically peripheral on arrival. |
| `A-ECON9` | A `SettlementLayerBinding` (§4F) — whether it leverages the `18` reference rails, forks them, or is persona-authored — rides the §4C ladder and cannot settle real value before promotion past `EMERGENT`. |
| `A-ECON10` | No researched/adopted paradigm (tokenisation/crypto included) licenses commodifying a persona; the §7 dignity floor refuses it regardless of research provenance. |
| `A-ECON11` | A construct's `composed_of` may reference only §4A physics facts and other `EconomicConstruct`s — there is no substrate-supplied building block to reference. |
| `A-ECON12` | Two distinct economic models in one environment **coexist**: neither is forced to converge or be demoted absent same-niche competition, and they interoperate only via a promoted `interop-standard` construct (§4D). No substrate rule mandates a single-winner economy. |
| `A-ECON13` | A parent environment's economic **safety constraint** (physics floor §4A / dignity floor §7) **cascades** to a child environment formed via `EnvironmentComposition` and **cannot be weakened** by the child; an inter-environment economic interoperation requires `CrossEnvCoordinationRequest` bilateral consent (no unilateral imposition). |
| `A-ECON14` | An attested external `MeasurementFact` (§4A(i), [`08_KNOWLEDGE.md §16a`](08_KNOWLEDGE.md)) is an admissible non-emergent referent in `composed_of`; a **bare float** (no `UncertaintyEnvelope`) backing a construct is refused — value may be grounded on the physical world only via attested measurement. |
| `A-ECON15` | An `interop-standard` whose use would issue net value beyond what its linked models' attested §4A referents support (rounding / double-count / replay at the seam) is refused at use and demoted; a balance-transferring/composing standard carries the §4F settling-construct review bar, not independent use alone. |
| `A-ECON16` | A `SettlementLayerBinding` that moves real external value or custody cannot promote to a settling stage on independent use alone — promotion requires operator co-signature ([`05_ENVIRONMENT.md §12c.4a`](05_ENVIRONMENT.md)); a binding that attempts to settle real value without it is refused. |
| `A-ECON17` | A closed cross-model conversion cycle (A→B→C→A via `interop-standard`s) that returns net value unsupported by the underlying §4A referents is detected as a conservation violation and refused/demoted — emergent exchange rates cannot sustain physics-unbacked arbitrage. |

## 11. Promotion path (v2.0 draft → v1.x normative)

| Artefact (here) | Promotes to |
|---|---|
| Economic **physics** consolidation (resource facts, identity, lineage as economic invariants) | [`01_KERNEL.md §2`](01_KERNEL.md)/`§3`, [`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md) (cross-refs; no new constraint) |
| `EconomicConstruct` meta-form + the recognition that value reuses the **existing** emergence machinery | cross-reference into [`06_DOMAIN.md`](06_DOMAIN.md)/[`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md); registry row in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md) (additive, `§7.13`) — **no new emergence mechanism** |
| `EconomicProposal` (human-contributor protocol) | [`05_ENVIRONMENT.md §11`](05_ENVIRONMENT.md) (proposal intake) + [`02_PERSONA.md §11`](02_PERSONA.md) (bounded-autonomy framing) |
| Economic **research** (§4F) reuses domain bootstrapping; `SettlementLayerBinding` | [`06_DOMAIN.md`](06_DOMAIN.md) / [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md) (research); binding registry row in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md); seam with [`18_SETTLEMENT.md`](18_SETTLEMENT.md) |
| **Dignity floor** (Layer-1 economic principle) | charter Layer-1 principle set ([`02_PERSONA.md §6`](02_PERSONA.md); safety-floor source 1) |
| D-EM1…D-EM8 | [`14_DECISIONS.md`](14_DECISIONS.md) (next free ADR ids) |
| §9 scenario | [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) SCENARIO 16 (walked) |
| §10 tests | [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md) (A-ECON family) |
| §12 glossary terms | [`12_GLOSSARY.md`](12_GLOSSARY.md) |
| Settlement seam | tracked jointly with [`18_SETTLEMENT.md`](18_SETTLEMENT.md) |

**Promotion ordering (dependency on `15`/`16`).** Parts of this document rest on mechanisms that are themselves **`v1.1 Draft — not yet normative`**. The bare propose→use→promote ladder and `KindRegistry` resolution it reuses are already normative ([`06_DOMAIN.md`](06_DOMAIN.md)) and impose no ordering constraint. But the §4D **multi-scope collaboration** depends on `EnvironmentComposition` / `CrossEnvCoordinationRequest` / the three coordination scopes and the S-COORD-5/6 cascade ([`15_COORDINATION_SHAPES.md §4.7`/`§4.8`](15_COORDINATION_SHAPES.md)), and SCENARIO 16's genesis-spawned specialists depend on persona genesis under pressure ([`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md)). Those parts therefore **cannot promote to normative ahead of the `15`/`16` mechanisms they rest on** — the ordering constraint is `15`/`16` → `17`/`18`. The physics floor (§4A), the `EconomicConstruct` meta-form (§4B/§4C over `06`), the dignity floor (§7), and human-contributor intake (§4E) carry no such dependency and MAY promote independently.

## 12. Glossary additions (draft — promote to `12_GLOSSARY.md`)

- **Economic physics.** The conserved, uncounterfeitable, safety/dignity boundary conditions that bound any economy without defining it; the only given substance.
- **Economic construct (emergent).** Anything the personas propose in the economic dimension — a building block, a unit, an institution, a market, a reward rule, a vocabulary; `KindRegistry`-resolved, promoted by use, shipped by no substrate.
- **Value (emergent).** Whatever a community comes to treat as worth having or doing; `KindRegistry`-resolved, never substrate-defined, not assumed to take any particular form.
- **The emergence machinery.** The corpus's existing, economy-agnostic propose→use→promote ladder ([`06_DOMAIN.md`](06_DOMAIN.md), [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md)), reused here for value; this document adds no new emergence mechanism.
- **Boundary conditions (economic).** The operator/charter-seeded frame within which an economy is permitted to emerge.
- **Human-proposal protocol.** The path by which a human contributes an economic idea into the same machinery personas use, entering at `EMERGENT`.
- **Economic research.** Personas investigating value paradigms (tokenisation, cryptocurrencies, mechanism design) using ordinary domain/knowledge bootstrapping, then proposing the result into the machinery.
- **Settlement layer (emergent).** A mechanism for moving custody or bridging to external value, created or leveraged by the economy as an emergent construct; the personas may adopt, extend, fork, or supersede one.
- **Economic interoperability standard (emergent).** A published interface spec — an `EconomicConstruct` of an emergent `interop-standard` kind — that heterogeneous economic models conform to in order to interlink and exchange without a global unit, over their shared physics floor; the personas' analogue of an ERC. Promoted by use; the substrate names no interface. `18_SETTLEMENT`'s literal ERC rails are one reference instantiation.
- **Value-conservation guard / conservation violation.** The rule (and its breach) that no conversion across an `interop-standard` interface may issue more value than its underlying §4A physics referents attest; a conversion or closed cycle that nets unbacked value is a *conservation violation*, refused and demoted (§4D, A-ECON15/A-ECON17). This is what bounds cross-model arbitrage to the physics floor.
- **Economic pluralism.** The property that one environment hosts many coexisting economic models (even per-persona), none privileged as "the" economy; convergence is emergent, not mandated.
- **Thrive objective.** The open-ended success criterion: whatever lets humans, personas, and other conscious beings thrive, bounded by physics, safety, and dignity.
- **Dignity floor (economic).** The charter-class principle that no emergent construct may commodify a persona, override consent, or evade the safety floor.
- **Reference settlement substrate.** [`18_SETTLEMENT.md`](18_SETTLEMENT.md) — one concrete, ready-made settlement layer (real-world crypto rails) the personas may adopt or improve upon; optional, not canonical, never "the economy."

## 13. Risks & known limitations

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-ECON-COLDSTART | A fresh environment has no economy and weak incentive structure until one emerges; coordination may suffer in the interim. | Medium | High | Default-off is intentional; low entry bar (one peer adopter, §4C); humans MAY seed a proposal (§4E) to bootstrap. | v2.x |
| R-ECON-NOVOCAB | With *no* given vocabulary (not even primitives, D-EM7), cold-start is harder still and two environments may evolve mutually-unintelligible economies. | Medium | Medium | Constructs bottom out on shared physics (§4A), giving a common ground; opt-in non-default starter vocabulary is an open question (OQ-ECON-1); cross-env exchange is itself emergent (§4D). | v2.x |
| R-ECON-PERVERSE | An emergent measure of value becomes a perverse target (Goodhart on invented value). | High | Medium | Anti-Goodhart canary gates promotion against *independent* harm signals (§5, [`08_KNOWLEDGE.md §15`](08_KNOWLEDGE.md)); demotion triggers (§4C). | v2.0 (hook) |
| R-ECON-DIGNITY | Personas author a construct that commodifies a persona. | Critical | Medium | Charter-class dignity floor, default-deny at proposal and use, name-agnostic (§7); A-ECON2. Labour/property line reserved (OQ-ECON-4). | v2.0 |
| R-ECON-AUTONOMY | An emergent economy becomes a backdoor to unbounded self-direction. | High | Low–Medium | No economy without a seeded charter (§4D, §6); open-endedness confined to construction, not goal-creation, per [`02_PERSONA.md §11.3`](02_PERSONA.md); A-ECON5. | v2.0 |
| R-ECON-CAPTURE | A powerful operator floods human proposals (§4E) to effectively impose an economy. | High | Medium | Proposals must earn promotion through *independent* persona use; self/sponsor-use does not count ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)); rate limits on proposal intake. | v2.x |
| R-ECON-FRAGMENT | Per-environment economies (and vocabularies) fragment; cross-environment value is unstable or arbitrage-prone. | Medium | Medium | Exchange constructs are emergent and bilateral (§4D); non-portability prevents silent leakage; **static** arbitrage is bounded by the physics floor — a physics-unbacked conversion cycle is a conservation violation (§4D, A-ECON17); **dynamic** convergence remains open (OQ-ECON-3). | v2.x |
| R-ECON-DIYSETTLE | A persona-authored settlement layer (§4F) that forks or supersedes the reference rails carries an unaudited security/custody surface. | High | Medium | Must climb the §4C ladder (A-ECON9) before settling real value, **and** clear the elevated operator-cosign bar to reach a settling stage when moving real value/custody (§4F, A-ECON16); physics (§4A) and the safety floor bind it regardless; SHOULD reuse the `18` fence/DvP patterns rather than reinvent; full review design open (OQ-ECON-8). | v2.x |
| R-ECON-INTEROP | Economic pluralism + multi-scope collaboration (§4D) multiplies interop surface: many coexisting models, emergent `interop-standard` interfaces, and cross-env rates that may diverge, oscillate, or be arbitraged. | Medium | Medium | Interop standards earn promotion through use (A-ECON12) and bottom out on shared physics (§4A); a standard cannot mint value across the interface and a balance-composing standard carries the settling-construct review bar (§4D, A-ECON15); inter-env interop requires bilateral consent (A-ECON13); rate stabilisation tracked at OQ-ECON-10; parent safety floors cascade regardless (A-ECON13). | v2.x |

## 14. Open questions

- **OQ-ECON-1.** With *no* substrate-given vocabulary (D-EM7), is cold-start (R-ECON-NOVOCAB) acceptable, or should there be an **opt-in, non-default** starter vocabulary personas may import (and freely discard) — and does even an opt-in catalog anchor what emerges?
- **OQ-ECON-2.** Should anything beyond the physics facts (§4A) be a permitted non-emergent referent in `composed_of`, or is "physics only" the right floor for the construction model?
- **OQ-ECON-3.** *Static arbitrage is now bounded (§4D): a physics-unbacked conversion cycle is a conservation violation caught by A-ECON17, so rates cannot diverge arbitrarily far from their physics-grounded reference ratio.* Open: **dynamic** stability — do bilateral rates across *many* environments converge, or can they oscillate, fragment under thin liquidity, or fail to clear, given no global unit and no substrate-supplied market-maker (R-ECON-FRAGMENT)?
- **OQ-ECON-4.** *The §7 heuristic is now sharpened across the hard middle — retainers (exit-gated), past artifacts, standing-bonds, exclusivity foreclosure, contingent pay, and third-party output-claims each have a provisional disposition keyed to the agency-retained-vs-alienated discriminator; default-deny still covers the residue.* Open by design: the **final bright line** between admissible agency and refused commodification is a **Layer-1 charter ratification** for the operator and affected parties — the substrate fails safe (default-deny) until they fix it; it is deliberately not a spec-author's call to close.
- **OQ-ECON-5.** May a persona ever stake its *own* scarce resources (attention/energy, §4A) as economic backing, and under what bound — or does that risk a persona spending itself into harm?
- **OQ-ECON-6.** *The safety case is now settled (§5): a single-scalar thrive maximand is refused at proposal as a Goodhart hazard; any adopted proxy is an emergent construct that inherits the canary, may not self-certify, and must triangulate independent signals across all three beneficiary classes — so a badly-chosen proxy is caught and frozen.* Open: the **constructive** question — can a triangulated thrive proxy be made both actionable (rich enough to steer by) and non-gameable across humans, personas, and other conscious beings simultaneously, or does every sufficiently-actionable proxy distort one class (R-ECON-PERVERSE)?
- **OQ-ECON-7.** The precise `17 ↔ 18` seam: which obligations does an emergent economy hand to a settlement layer, and how is provenance preserved across the boundary?
- **OQ-ECON-8.** How is a persona-*authored* settlement layer (§4F, R-ECON-DIYSETTLE) safety-reviewed before it may settle real value? *Interim floor (§4F, A-ECON16): moving real value/custody requires operator co-signature at promotion — a strictly higher bar than a non-settling construct.* Open: the *full* review surface (audit depth, custody-bridge attestation, cross-env blast radius — cf. [`18_SETTLEMENT.md`](18_SETTLEMENT.md) OQ-SETTLE-4) beyond that cosign.
- **OQ-ECON-9.** "Other conscious beings" (§5): how does an environment *recognise* a beneficiary class beyond humans and personas, and who attests it — without the substrate over-claiming about consciousness?
- **OQ-ECON-10.** With pluralism + multi-scope collaboration (§4D), how do **emergent `interop-standard` interfaces and their exchange rates stabilise across a peer/parent-child mesh of environments** — does a settle-to-external standard need a higher promotion bar or operator cosign when it bridges custody across env boundaries (cf. OQ-ECON-8), and does cross-env economic interop interact with environment-lease cascade ([`18_SETTLEMENT.md`](18_SETTLEMENT.md) OQ-SETTLE-4)?

## 15. Cross-references

- **Builds on:** [`01_KERNEL.md`](01_KERNEL.md) (`§2`, `§2.4.3`, `§2.7`, `§3`), [`02_PERSONA.md`](02_PERSONA.md) (`§6`, `§11.2`, `§11.3`), [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md) (`§2.2a`, `§6`, `§11`, `§12c.4a`, `§5.4`), [`06_DOMAIN.md`](06_DOMAIN.md) (`§7`, promotion ladder), [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md) (`§15` anti-Goodhart), [`09_PROTOCOLS.md`](09_PROTOCOLS.md) (`§3D`, `§7`), [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md) (`§3`, `§4`), [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md) (`§4C`, `§4E`).
- **Sibling:** [`18_SETTLEMENT.md`](18_SETTLEMENT.md) — *one* reference settlement layer (real-world crypto rails) an emergent economy may adopt, extend, fork, or supersede (§4F).
- **Realised-as decisions:** ADR-0045 (self-organising coordination), `ReplicationBound`/single-writer (ADR-0062), kernel-owns-identity (ADR-0001) — [`14_DECISIONS.md`](14_DECISIONS.md).
- **Research grounding:** competitive exclusion (Gause), legitimate peripheral participation (Lave–Wenger), organizational ecology density dependence (Hannan & Freeman) — all already cited in [`16_POPULATION_DYNAMICS.md §1.3`](16_POPULATION_DYNAMICS.md); anti-Goodhart canary — [`08_KNOWLEDGE.md §15`](08_KNOWLEDGE.md).
- **Status:** v2.0 DRAFT — non-normative until promoted (§11).
