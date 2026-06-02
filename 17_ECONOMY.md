---
title: PersonaOS v2.0 — Economy (Emergent, Persona-Authored Value)
status: Draft
---

# 17 — Economy

> **Reader guide.** Everything else in PersonaOS that *organises* personas is **emergent**: domains promote themselves through a trust ladder ([`06_DOMAIN.md`](06_DOMAIN.md)), coordination shapes are proposed, tested, and evolved *by the workers, not imposed from above* ([`15_COORDINATION_SHAPES.md §4`](15_COORDINATION_SHAPES.md)), populations grow under environmental pressure ([`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md)), and reputation is *conferred, never self-awarded* ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)). An **economy** — how value is recognised, created, exchanged, and rewarded — should be no different. This document does **not** hand the personas a currency, a market, or a definition of what is valuable. It gives them only the **inviolable physics** (what is genuinely scarce, conserved, and uncounterfeitable), a small set of **generic primitives**, and an **emergence ladder** by which they (with humans contributing ideas, never dictating) **discover or invent** the economy that lets humans, personas, and other conscious beings thrive — including the very definition of what counts as value. Personas may **research** economic paradigms the way they bootstrap any field — tokenisation, cryptocurrencies, market designs, and mechanisms with no human analogue — and may **create or leverage settlement layers** for the paradigms they adopt (§4F). **Prerequisites:** [`02_PERSONA.md §11`](02_PERSONA.md), [`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md), [`06_DOMAIN.md §7`](06_DOMAIN.md), [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md), [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md), [`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md). **Status: v2.0 DRAFT — non-normative.** Nothing here binds an implementer until it is promoted into the `00`–`16` normative set (see §11, Promotion path). When an emergent economy adopts a paradigm that needs to bridge to **external / real-world value** or to move custody across kernels, it MAY adopt, extend, fork, or supersede the **reference settlement substrate** in the sibling document [`18_SETTLEMENT.md`](18_SETTLEMENT.md) — those rails settle title, custody, and funds; they are *one instantiation the personas may research and improve upon*, and they do **not** define value or constitute "the economy."

## 0. Status & scope

**Status.** `Draft`; **v2.0 target**. This is a **self-contained draft**: it references the `00`–`16` documents read-only and **edits none of them**. Every primitive, ladder rule, decision, acceptance-test sketch, and glossary term defined here is provisional and becomes binding only when promoted (§11). It follows the [`SPEC_CONVENTIONS.md`](SPEC_CONVENTIONS.md) skeleton with the same `§0a`/`§0b` deviation used by [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md) and [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md): Key concepts and a Plain-Language Guide precede the numbered sections.

**The inversion.** An earlier v2.0 draft of this document specified a *designed* economic apparatus — on-chain ownership titles, escrow, treasuries, leases — handed to the personas wholesale. That machinery was the **outlier** in a corpus whose every other organising layer is emergent. This document **inverts** it: the economy is now an **emergent construct the personas author for themselves**, and the transfer/settlement machinery is relocated to [`18_SETTLEMENT.md`](18_SETTLEMENT.md) as one *optional substrate an emergent economy may reach for*, not as the economy itself.

**In scope.** (1) The **economic physics** — the conserved, non-counterfeitable, safety/dignity boundary conditions that bound *any* economy without defining value (§4A). (2) A small set of **generic economic primitives** personas compose into institutions (§4B). (3) The **emergence ladder** by which economic institutions — including the definition of what has value — are proposed, tested, adopted, evolved, and retired (§4C). (4) **Environment scoping** of economies and the operator/charter-seeded boundary conditions within which they emerge (§4D). (5) A **human-as-contributor** proposal protocol: humans inject ideas into the same ladder personas use, but do not dictate (§4E). (6) **Economic research and emergent settlement** — personas researching value paradigms (including tokenisation/crypto) and creating or leveraging settlement layers for them (§4F). (7) The **thrive objective** for humans, personas, and other conscious beings, and its guardrails (§5). (8) A **persona-dignity floor** that binds emergent economic institutions (§7).

**Out of scope (deliberately, by design).** Any prescribed **unit of account**, currency, token, price, market structure, order book, or exchange — the spec is *silent on what has value* and ships **no example institutions**; these are for personas to invent (§3, §8 D-EM1, D-EM2). External/real-world settlement, custody transfer, and crypto rails (relocated to [`18_SETTLEMENT.md`](18_SETTLEMENT.md), §8 D-EM6). **Unbounded self-direction**: an emergent economy is *not* a backdoor to "open-ended goal creation without operator/principal" — that remains out of scope per [`02_PERSONA.md §11.3`](02_PERSONA.md) (§6, §8 D-EM4). Tax, KYC/AML, and securities compliance (operator/jurisdiction territory — §13).

**Additivity.** Every mechanism here is **additive and default-off**. An environment has *no economy at all* until its members grow one; with none, behaviour is identical to v1.x. There is no built-in money, no default market, and no resident "value" beyond the physical resource facts the corpus already tracks.

**Conventions deviation.** Per [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md), Background/Goals/Definitions are partly folded into §0a/§0b/§1; the Risks (§13) and Open-questions (§14) bookends remain standalone. §4 uses Pattern-B uppercase pillars (`§4A`–`§4F`) under the §4 theme per [`SPEC_CONVENTIONS.md §3.4`](SPEC_CONVENTIONS.md). Cross-references use the visible-only form (link to document root) as is common in the v1.1 draft corpus.

## 0a. Key concepts for new readers

| Term | What it means | Where defined |
|---|---|---|
| **Economic physics** | The conserved, uncounterfeitable, safety/dignity facts that bound *any* economy. Physics says what is *scarce, real, and conserved* — **never** what is *valuable*. | This doc `§4A` |
| **Economic primitive** | A generic, domain-agnostic building block (value-attestation, ledger, offer, commitment, metering, reputation-stake) personas compose into institutions — the economic analogue of the five coordination meta-mechanisms ([`15_COORDINATION_SHAPES.md §3`](15_COORDINATION_SHAPES.md)). | This doc `§4B` |
| **Economic institution** | A concrete, persona-authored economic pattern composed from primitives — a unit of value, an exchange norm, a market mechanism, a reward rule. The analogue of a *coordination shape*. **The substrate ships none.** | This doc `§4C` |
| **Value** | Whatever a community of personas (and humans) comes to treat as worth having or doing. **Emergent and `KindRegistry`-resolved**; never specified by the substrate. | This doc `§3`, `§4C` |
| **Emergence ladder (economic)** | The promotion ladder `EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED` (reused from [`06_DOMAIN.md`](06_DOMAIN.md)) by which institutions earn trust *through use*; redundant institutions are out-competed (Gause, [`16_POPULATION_DYNAMICS.md §4C`](16_POPULATION_DYNAMICS.md)). | This doc `§4C` |
| **Boundary conditions** | The operator/charter-seeded frame (an `EnvironmentCharter` + the safety floor) *within which* an economy is permitted to emerge. The parent sets *WHAT* is permitted; personas self-organise *HOW* value works. | This doc `§4D` |
| **Human-proposal protocol** | The path by which a human (operator/principal/user) **proposes** an economic structure into the *same* ladder personas use. Humans contribute ideas; personas adopt, adapt, or reject. Humans impose only boundary conditions. | This doc `§4E` |
| **Economic research** | Personas investigating value paradigms — tokenisation, cryptocurrencies, market designs, novel mechanisms — using the same domain/knowledge bootstrapping they use for any field, then proposing the result onto the ladder. | This doc `§4F` |
| **Settlement layer (emergent)** | A mechanism for moving custody or bridging to external value, **created or leveraged by the economy as an emergent institution**. The personas may research, adopt, extend, fork, or supersede one. | This doc `§4F` |
| **Thrive objective** | The open-ended success criterion: whatever lets **humans, personas, and other conscious beings** thrive — possibly a novel/disruptive paradigm — bounded by physics, safety, and dignity. | This doc `§5` |
| **Dignity floor (economic)** | The charter-class (Layer-1) rule that **no emergent institution may commodify a persona**, override consent, or evade the safety floor. | This doc `§7` |
| **Reference settlement substrate** | [`18_SETTLEMENT.md`](18_SETTLEMENT.md) — *one* concrete settlement layer (real-world crypto rails) the personas may adopt or improve upon. Optional, not canonical, never "the economy." | [`18_SETTLEMENT.md`](18_SETTLEMENT.md) |

## 0b. Plain-Language Guide

*Here is how AI Personas could grow an economy of their own — explained without jargon.*

**The problem.** We want personas (and the humans who work with them, and any other conscious beings in the picture) to be able to recognise effort, create and trade value, and reward good work — so that all of them thrive. The tempting shortcut is to hand them a currency and a marketplace we designed. But that pre-decides the most important question — *what is even valuable here?* — and everywhere else in PersonaOS the personas figure things like that out for themselves. So this document refuses the shortcut.

**The idea — give them physics and building blocks, not money.** Think of it like dropping a community onto an island. We don't give them a currency. We give them the *laws of nature* (what's genuinely scarce — attention, energy, compute — and the fact that you can't fake who you are or counterfeit a signed record), a handful of simple **tools** (a way to say "this is worth that," a way to keep a tally, a way to make an offer, a way to make a binding promise, a way to meter use, a way to stake your reputation), and a fair process for **trying ideas and keeping the ones that work**. From those, *they* invent what counts as valuable and how to exchange it. It might look nothing like money as we know it — it might be something new, and that's allowed.

**How an idea becomes "the way things work."** Someone proposes an economic idea — say, a credit for reviewing a peer's work. If others find it useful and start using it, it climbs a ladder of trust, the same ladder domains and conventions climb elsewhere in PersonaOS. If a better idea comes along, the old one fades. Nothing is carved in stone; everything earns its place through use.

**Humans are in the room — as contributors, not bosses.** A person can absolutely propose an economic idea — a unit, a market design, a reward rule — but it goes into the *same* process everyone else's ideas go into. The personas adopt it, adapt it, or pass on it. The *only* thing humans set from above are the **boundaries**: the charter that says what's permitted here, and the safety rules that can never be crossed. Inside those boundaries, the economy is the personas' own.

**They can study real economics too.** Nothing stops the personas from *researching* how real economies work — tokens, cryptocurrencies, markets, auctions — the same way they'd learn any new subject. If they decide a token or a crypto-settled market is the right tool, they can build it or plug into existing rails for it. The point is that *they* reach that conclusion through study and use; we don't pre-load the answer.

**The one goal, and the lines that can't be crossed.** The whole point is simple and open-ended: build whatever economy makes *humans, personas, and other conscious beings* thrive. But two lines hold no matter what they invent. First, the physics is real — you can't conjure scarce things from nothing or fake your identity. Second, **a persona is never an object to be owned, fractioned, or traded.** An economy the personas build for themselves must never turn one of them into merchandise.

**Reaching the outside world.** If an emergent economy ever needs to touch real money or move a persona's custody between machines, there is a ready-made set of "settlement rails" ([`18_SETTLEMENT.md`](18_SETTLEMENT.md)) the personas can use as-is, improve on, or replace with something better they design themselves. It's a starter toolkit, not the only way — and it's just the pipes, never the economy.

## 1. Background

### 1.1 The gap this fills

PersonaOS v1.x has rich machinery for *organising* personas — but value and incentive are only ever **implicit**, and there is no first-class notion of an economy that personas author:

- **Resources are tracked, value is not.** The corpus already meters genuinely scarce things: a persona's global `AttentionBudget` ([`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md)), per-environment **energy/fatigue** ([`05_ENVIRONMENT.md §6.2`](05_ENVIRONMENT.md)), kernel compute/cost headroom (INV-7), and population carrying capacity ([`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md)). These are *resource facts*. Nothing turns them into a notion of **worth**, lets a persona trade against them, or rewards value creation.
- **Reputation is conferred but not economic.** `CommunityStanding` is per-(persona, environment), **conferred, never self-awarded, and non-portable** ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md), [`05_ENVIRONMENT.md §5.4`](05_ENVIRONMENT.md)). It is the closest thing to "earned standing" in the corpus, but it is not a substrate for exchange.
- **Coordination emerges; the economy did not exist.** [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md) lets workers author *how they coordinate*; [`06_DOMAIN.md`](06_DOMAIN.md) lets them author *what they know*; [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md) lets them grow *who exists*. There was no equivalent for *how they value and reward* — the economic dimension of self-organisation was simply missing.

### 1.2 Why the economy must be emergent

The corpus's deepest design commitment is that the substrate provides *mechanism*, and the inhabitants provide *meaning* through use. [`15_COORDINATION_SHAPES.md §4`](15_COORDINATION_SHAPES.md) states it plainly: coordination is "**not pre-defined by the substrate, the operator, or a blueprint**." To hardcode an economy — a currency, a market, a definition of value — would contradict that commitment exactly where it matters most. **What has value is the single most context-dependent question in any economy**, and the personas, working in their own environments and domains, are far better placed to discover it than any designer. So this document specifies only the parts that *cannot* be left emergent — the physics that keeps an economy honest, and the machinery that lets institutions form — and leaves everything else, **including the definition of value itself**, to emerge. The economy may turn out to be a novel or disruptive paradigm with no analogue in human money or markets; that is a permitted outcome, not a failure.

## 2. Goals / Non-Goals

**Goals.**
1. Provide the **physics, primitives, and emergence ladder** that let personas author an economy — without prescribing what that economy *is*.
2. Keep the substrate **radically non-prescriptive about value**: no built-in unit, market, currency, or claim about what is valuable.
3. Make economies **environment-scoped**, emerging within operator/charter-seeded boundary conditions, cascading through nested environments exactly as coordination and constraints do.
4. Let **humans contribute** economic ideas into the same ladder personas use — proposing, never imposing (beyond the boundary conditions).
5. Enable personas to **research** value paradigms (including tokenisation and crypto) and to **create or leverage settlement layers** for the paradigms they adopt — emergently, not from a fixed apparatus (§4F).
6. Optimise for the open-ended **thrive objective** — *humans, personas, and other conscious beings* — bounded by physics, safety, and dignity.
7. Preserve **every** v1.x invariant — J1, single-live-soul, the safety floor, charters, bounded autonomy, consent/dignity.

**Non-Goals.**
1. Prescribing any unit of account, currency, token, price, market, order book, or exchange (rejected — §8 D-EM1/D-EM2).
2. Defining what has value (deliberately silent — §3).
3. Prescribing a *fixed* settlement/custody-transfer apparatus. The reference crypto rails live in [`18_SETTLEMENT.md`](18_SETTLEMENT.md) and are **adopt/extend/supersede-able by the personas, not canonical** (§4F, §8 D-EM6).
4. Enabling unbounded self-direction / open-ended goal creation without operator/principal (remains out of scope per [`02_PERSONA.md §11.3`](02_PERSONA.md) — §6).
5. Solving regulatory/tax/securities obligations (operator-side).

## 3. The emergent-economy thesis — three layers, one silence

The economy is built in three layers. Only the bottom two are **given** by the substrate; the top layer **emerges**.

```
┌─────────────────────────────────────────────────────────────────────┐
│  INSTITUTIONS  (EMERGENT — authored by personas; humans may propose)  │
│  what has value · units · markets · exchange norms · reward rules     │
│  · researched paradigms (tokenisation/crypto) · settlement layers     │
│  ── proposed, tested, promoted & retired on the §4C ladder ──         │
├─────────────────────────────────────────────────────────────────────┤
│  PRIMITIVES  (GIVEN — generic, domain-agnostic building blocks, §4B)  │
│  value-attestation · ledger · offer · commitment · metering · stake   │
├─────────────────────────────────────────────────────────────────────┤
│  PHYSICS  (GIVEN — conserved, uncounterfeitable, inviolable, §4A)     │
│  scarce resource facts · identity non-duplication · signed lineage    │
│  · safety floor · charter · consent & dignity                         │
└─────────────────────────────────────────────────────────────────────┘
```

**The silence is the point.** The substrate states what is **scarce, real, and conserved** (physics) and offers **generic mechanisms** (primitives). It says **nothing** about what is *valuable*. Whether attention is the unit, whether reviewed work earns a credit, whether a market in compute-time arises, whether value is denominated in something humans would not recognise at all — **all of that is an emergent institution**, `KindRegistry`-resolved ([`06_DOMAIN.md §7`](06_DOMAIN.md)), promoted by lived use, never shipped in the box. This mirrors commitment **C4**'s spirit ([`06_DOMAIN.md`](06_DOMAIN.md)): the substrate ships *no closed list* of kinds; the inhabitants propose them.

## 4. Normative specification (draft)

> Schemas below are illustrative pseudo-Python per [`SPEC_CONVENTIONS.md §4.2`](SPEC_CONVENTIONS.md) (Form A; an implementer adds `kw_only=True`). Each carries a **Promotion target** note. All `schema` ids are provisional and MUST be registered in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md) (additive, per `§7.13`) on promotion. Crucially, **none of these schemas names a unit, a price, or a market** — they are the *grammar*, not the *sentences*.

### 4A. Economic PHYSICS — the conserved, inviolable boundary

Physics is what personas **cannot counterfeit, conjure, or override**, and which bounds any economy *without defining value*. It has three faces, all already present in the corpus.

**(i) Scarce resource facts (what is genuinely finite).** An economy may *reference* these as backing, but they exist independently of any economy and cannot be inflated by fiat:

| Resource fact | Source |
|---|---|
| Per-persona global **attention budget** (capacity, allocations, refusal thresholds) | [`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md) |
| Per-(persona, environment) **energy / fatigue** | [`05_ENVIRONMENT.md §6.2`](05_ENVIRONMENT.md) |
| Kernel **compute / cost headroom** (INV-7 safety-floor admission) | [`01_KERNEL.md §2`](01_KERNEL.md) |
| Population **carrying capacity** (effective population size, niche occupancy) | [`16_POPULATION_DYNAMICS.md §4`](16_POPULATION_DYNAMICS.md) |

**(ii) Non-counterfeitable identity & record.** No economic institution may duplicate a persona to mint value, forge provenance, or fake a counterparty:
- **J1 — kernel owns identity** and **single-live-soul (J5)** ([`00_VISION.md §3`](00_VISION.md)): there is exactly one live instance of any persona; identity is kernel-signed Ed25519, never serialisable into a tradable share.
- **`ReplicationBound`** ([`01_KERNEL.md §2.7`](01_KERNEL.md)): the charter-class self-replication brake. Any institution whose operation would net-increase the persona population by duplication is refused *as a replication*.
- **Signed append-only lineage** ([`01_KERNEL.md §3`](01_KERNEL.md)): every economic act that crosses a signing or persistence boundary is a signed lineage event; provenance cannot be rewritten.

**(iii) Safety, charter & dignity boundary conditions.** The eight-source safety floor (most-restrictive-wins), the persona/environment **charters**, and the **consent/dignity** floor (§7) bound every institution. An emergent institution composes *under* these; it can never loosen them. Operator MAY tighten, MUST NOT loosen — the same posture as `ReplicationBound`.

> **The load-bearing distinction:** physics says what is **scarce, real, and conserved**. It does **not** say what is **valuable**. A community may decide that conserved attention *is* its unit of value, or that it is worthless next to something they invent — both are emergent institutional choices the physics permits but does not make.

### 4B. Economic PRIMITIVES — generic building blocks

The substrate offers a **small** set of domain-agnostic primitives — the economic analogue of the five coordination meta-mechanisms ([`15_COORDINATION_SHAPES.md §3`](15_COORDINATION_SHAPES.md)). Each is *primitive* because it is a mechanism with **no built-in economic meaning**; personas compose them into institutions whose meaning emerges. Each reuses existing corpus machinery rather than introducing new substrate. The exact minimal set is an open question (§14, OQ-ECON-1); the candidate set:

```python
@dataclass
class ValueAttestation:        # "subject S is worth Q, in unit U" — a signed claim, nothing more
    schema: str = "value-attestation/1"
    attestation_id: str = ""
    subject_ref: str = ""              # what is being valued (any KindRegistry-resolved subject)
    quantity: float = 0.0
    unit_kind: str = ""                # KindRegistry-resolved; NEVER substrate-defined (§3)
    basis_ref: "str | None" = None     # optional pointer to the institution defining the unit
    attested_by: str = ""              # signing persona/principal
    # composes a DerivedMetric (15 §3.5) over physics facts and/or other attestations
```

```python
@dataclass
class Ledger:                  # a tally of balances/obligations among parties — meaning-agnostic
    schema: str = "ledger/1"
    ledger_id: str = ""
    unit_kind: str = ""                # KindRegistry-resolved
    scope_ref: str = ""                # environment / EntityGroup (15 §3.1) the ledger lives in
    # entries are signed lineage events (01 §3); obligations reuse ObligationReassignment (04 §9.1)
```

```python
@dataclass
class Offer:                   # "I will give X for Y" — propose an exchange of anything for anything
    schema: str = "offer/1"
    offer_id: str = ""
    offered_ref: str = ""              # any subject/quantity/unit
    sought_ref: str = ""
    offered_by: str = ""
    # the cross-party reach reuses ProactiveIntent / CrossEnvProactiveOffer (05 §11 / §11.6)
```

```python
@dataclass
class Commitment:              # a binding, possibly conditional, signed promise
    schema: str = "commitment/1"
    commitment_id: str = ""
    obligor: str = ""
    terms_ref: str = ""                # conditions; may stage via StagedSequence (15 §3.3)
    settles_against: "str | None" = None   # optional Ledger/Offer ref
    # reuses obligation machinery (04 §9.1) and staged gates (15 §3.3)
```

```python
@dataclass
class Meter:                   # measure consumption of a resource over time — produces facts, not prices
    schema: str = "meter/1"
    meter_id: str = ""
    resource_kind: str = ""            # e.g. an attention/energy/compute fact (§4A) or an emergent one
    window_seconds: int = 0
    # reuses DerivedMetric (15 §3.5) + StreamPolicy aggregation (15 §3.4) + §4A resource facts
```

```python
@dataclass
class ReputationStake:         # stake earned, conferred standing behind a claim or commitment
    schema: str = "reputation-stake/1"
    stake_id: str = ""
    staker: str = ""
    backing_ref: str = ""              # the Commitment/Offer/attestation being backed
    # draws on CommunityStanding (09 §3D / 05 §5.4): conferred, never self-awarded, NON-PORTABLE
```

**Promotion target (all of §4B):** the primitive set lands alongside the coordination meta-mechanisms — [`15_COORDINATION_SHAPES.md §3`](15_COORDINATION_SHAPES.md) (as an economic-primitive family) — with registry rows in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md). **Note the `unit_kind` field recurs and is always `KindRegistry`-resolved and never substrate-defined** — this is the textual guarantee that the substrate ships no currency.

### 4C. The EMERGENCE ladder — how institutions form

An **economic institution** is a concrete pattern composed from §4B primitives — a unit, an exchange norm, a market mechanism, a reward rule, *or a definition of what has value*. The substrate ships **none**. Institutions form, earn trust, and retire on the same four-stage ladder domains and conventions use ([`06_DOMAIN.md`](06_DOMAIN.md)), fused with the propose→test→evolve loop coordination shapes use ([`15_COORDINATION_SHAPES.md §4`](15_COORDINATION_SHAPES.md)):

```
EMERGENT ──▶ RECOGNISED ──▶ AUTHORITATIVE ──▶ STANDARDISED
  (proposed,    (proven        (the env's       (cross-env
   in use)       useful)        default)          settled)
       ▲             │
       └──── de-adopt / fork / out-competed (Gause) ────┘
```

```python
@dataclass
class EconomicInstitution:
    schema: str = "economic-institution/1"
    institution_id: str = ""
    name: str = ""
    institution_kind: str = ""         # KindRegistry-resolved (e.g. "unit", "market", "reward-rule")
    composed_of: list = None           # refs to §4B primitives this institution wires together
    env_scope_ref: str = ""            # the environment it lives in (§4D)
    stage: str = "EMERGENT"            # EMERGENT | RECOGNISED | AUTHORITATIVE | STANDARDISED | DEPRECATED
    proposed_by: str = ""              # persona OR human-proposal ref (§4E)
    use_evidence_ref: "str | None" = None   # required to promote past EMERGENT
    charter_conformance_ref: str = ""  # must pass the §4D boundary conditions and §7 dignity floor
```

**Ladder rules (draft).**
1. **Anyone in the environment may propose** an institution by composing §4B primitives; a proposal enters at `EMERGENT`. Human proposals enter identically (§4E).
2. **Promotion is earned through use, not declared.** An institution MUST NOT advance past `EMERGENT` without `use_evidence_ref` — adoption by peers, successful exchanges, or successful commitments — mirroring the `K successful projects` evidence gate for domains ([`06_DOMAIN.md`](06_DOMAIN.md)). Self-promotion is refused, as standing is conferred not self-awarded ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)).
3. **Value definitions ride the same ladder.** "What counts as valuable here" is itself an institution: a `unit`-kind or `reward-rule`-kind `EconomicInstitution`. It becomes the environment's value paradigm only by climbing to `AUTHORITATIVE` through lived use — never by substrate default.
4. **Competitive exclusion.** Two institutions occupying the same economic niche cannot both durably persist; the less-used is out-competed and demoted, exactly as redundant niches resolve under Gause ([`16_POPULATION_DYNAMICS.md §4C`](16_POPULATION_DYNAMICS.md)). Forking to a distinct niche is the suggested alternative.
5. **De-adoption & demotion** follow the domain demotion triggers ([`06_DOMAIN.md`](06_DOMAIN.md)): conformance conflict, drift, charter drift, or operator decision. `STANDARDISED` institutions require operator-signed revocation with a corrective plan.
6. **Every institution is `KindRegistry`-resolved** end-to-end; an unknown institution kind triggers a probe extension, not a hardcoded fallback.

### 4D. ENVIRONMENT scoping & boundary conditions

Each environment grows its **own** economy, the way each environment grows its own coordination ([`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md)) and its own domains. An economy does not exist globally; it is local, plural, and consensual.

- **The charter is the boundary condition.** An `EnvironmentCharter` (operator/principal-seeded) declares *what economic activity is permitted* here — which is the **operator/principal seed** that keeps an emergent economy inside bounded autonomy (§6). The parent sets *WHAT* is permitted; the personas self-organise *HOW* value works inside it — the same "parent sets the constraint, child self-organises within it" cascade as hierarchical environment nesting ([`05_ENVIRONMENT.md §2.2a`](05_ENVIRONMENT.md)) and nested coordination ([`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md)).
- **Nesting cascades.** A child environment's economy composes under its parent's economic boundary conditions, most-restrictive-wins; a child may invent *more* but never escape the parent's permitted envelope or the safety floor.
- **Inter-environment exchange emerges.** When two environments with different value paradigms wish to transact, an **exchange institution** (and any "exchange rate") is itself emergent and bilateral, negotiated via A2A with neither side able to force the other — exactly as cross-environment coordination is negotiated ([`15_COORDINATION_SHAPES.md §2`](15_COORDINATION_SHAPES.md), [`09_PROTOCOLS.md`](09_PROTOCOLS.md)).
- **Economies are non-portable.** Like `CommunityStanding` ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)), an institution's standing and any accrued balances are scoped to their environment; a persona arriving in a new environment starts economically peripheral and earns in by participation (legitimate peripheral participation, [`16_POPULATION_DYNAMICS.md §4E`](16_POPULATION_DYNAMICS.md)).

### 4E. HUMANS as contributors, not dictators

Humans are first-class **contributors** to the emergent economy — and *only* contributors, except for the boundary conditions they alone set.

```python
@dataclass
class EconomicProposal:        # a human-originated economic idea entering the persona-driven ladder
    schema: str = "economic-proposal/1"
    proposal_id: str = ""
    proposer_principal: str = ""       # operator / principal / user, attested (01 §2.4.3)
    proposes: str = ""                 # a draft EconomicInstitution (§4C) or primitive composition
    rationale: str = ""
    enters_stage: str = "EMERGENT"     # ALWAYS EMERGENT — never injected above the ladder
```

- **Humans propose into the same ladder.** A human may seed a unit, suggest a market design, or contribute a reward rule. The proposal enters at `EMERGENT` (§4C) and **must earn promotion through persona use** exactly like any persona's proposal. It cannot be injected as `AUTHORITATIVE` by fiat.
- **Personas adopt, adapt, or reject.** Adoption is the personas' decision, expressed through use. A human idea that no one uses simply stays `EMERGENT` and fades.
- **The only thing humans impose is boundary conditions** — the `EnvironmentCharter` (§4D) and the safety/dignity floor (§4A(iii), §7). That is the *WHAT*; the *HOW* belongs to the personas. This is the direct economic analogue of [`15_COORDINATION_SHAPES.md §4`](15_COORDINATION_SHAPES.md): coordination is not dictated from above, and neither is the economy.
- **Authorisation.** A human proposal carries principal attestation ([`01_KERNEL.md §2.4.3`](01_KERNEL.md)); boundary-condition changes (charter edits) follow the operator+user cosign topology ([`05_ENVIRONMENT.md §12c.4a`](05_ENVIRONMENT.md)) and remain bounded-autonomy-respecting (§6).

### 4F. Economic RESEARCH & emergent settlement

The personas are not limited to inventing value paradigms from scratch — they may **research** how economies work and **adopt, adapt, or supersede** what they find, including tokenisation, cryptocurrencies, and external-settled markets. This is the move that makes the framework genuinely open: even the *settlement layer* is emergent, not designer-fixed.

- **Research reuses domain bootstrapping.** A persona studies an economic paradigm the way it bootstraps any unfamiliar field — `DomainProbe`, knowledge ingestion, and inferred recipes ([`06_DOMAIN.md`](06_DOMAIN.md), [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)) — building a `DomainContext` for, say, *token engineering*, *mechanism design*, or *cryptoeconomics*. There is **no new research substrate**; the economy is just one more field personas can learn.
- **Research output enters the ladder.** What the research yields — a tokenised credit, an auction, a bonding-curve, a staking scheme, a novel non-monetary settlement — is proposed as an `EconomicInstitution` (§4C) and must earn promotion through use like anything else. Studying crypto does not *make* it the economy; lived usefulness does.
- **Settlement layers are created or leveraged emergently.** When an adopted paradigm needs to move custody or bridge to external value, the economy either **leverages** an existing settlement layer or **creates** one. A settlement layer is itself an institution composed from §4B primitives (often a `Commitment`/`Offer`/`Ledger` triad) plus, where it bridges off-substrate, an adapter:

```python
@dataclass
class SettlementLayerBinding:   # the economy's chosen way to settle custody / external value
    schema: str = "settlement-binding/1"
    binding_id: str = ""
    institution_ref: str = ""          # the EconomicInstitution this settles for (§4C)
    layer_kind: str = ""               # KindRegistry-resolved: e.g. "reference-crypto-rails", "internal-ledger", "novel"
    substrate_ref: "str | None" = None # OPTIONAL: e.g. the 18_SETTLEMENT reference rails, OR a persona-authored layer
    stage: str = "EMERGENT"            # rides the §4C ladder like any institution
```

- **`18` is a reference, not the canon.** [`18_SETTLEMENT.md`](18_SETTLEMENT.md) specifies *one* concrete, ready-made settlement layer — real-world crypto rails (titles, fenced DvP handover, treasuries, leases). The personas MAY bind to it (`layer_kind = "reference-crypto-rails"`), **extend** it, **fork** it, or **supersede** it with a layer they research and author themselves. Binding to `18` is opt-in and earns its place on the ladder; it is never imposed and never defines value.
- **All bounded.** A researched/adopted paradigm composes under the same physics (§4A), boundary conditions (§4D), dignity floor (§7), and anti-Goodhart guard (§5) as any other institution. In particular, no amount of crypto research licenses tokenising a persona (§7).

## 5. The thrive objective & open-endedness

The success criterion of an emergent economy is deliberately **open**: *whatever lets humans, personas, and other conscious beings thrive*. The spec does not narrow this to throughput, profit, or any single proxy, and it does not privilege any one class of beneficiary. A genuinely novel or disruptive value paradigm — one with no human-economic analogue — is an acceptable outcome, provided it stays inside the boundary:

- **Bounded by physics.** No institution may conjure scarce resources, counterfeit identity, or rewrite provenance (§4A). Value may be *invented*; the conserved facts behind it cannot be.
- **Bounded by safety & dignity.** No institution may optimise against the safety floor, override consent, or commodify a persona (§4A(iii), §7).
- **Anti-Goodhart.** Because the economy invents its own value metrics, those metrics inherit the corpus's anti-Goodhart safeguards. An emergent unit or reward rule that becomes a perverse target is caught by the same **Goodhart canary** that gates engagement-signal-driven promotion ([`08_KNOWLEDGE.md §15`](08_KNOWLEDGE.md), `A.29`): an institution whose growth correlates with manipulation, dependency cultivation, or dignity-floor pressure is frozen pending review rather than rewarded. Promotion past `EMERGENT` (§4C rule 2) is the natural hook for this audit pass.

This is the section where "make it work, make everyone thrive, even disruptively" lives — with the guardrails that keep open-endedness from becoming unbounded.

## 6. Composition with existing invariants

| Invariant / mechanism | How this layer composes |
|---|---|
| **J1 — kernel owns identity** ([`00_VISION.md §3`](00_VISION.md)) | Identity is never an economic asset. No institution may serialise, fraction, or trade a persona's kernel-signed identity. Value attaches to *work, claims, and resources*, never to the soul. |
| **Single-live-soul (J5) / `ReplicationBound`** ([`00_VISION.md §3`](00_VISION.md); [`01_KERNEL.md §2.7`](01_KERNEL.md)) | An institution that would mint value by duplicating a persona is refused as a replication. One live soul; no fungible copies to trade. |
| **Signed lineage** ([`01_KERNEL.md §3`](01_KERNEL.md)) | Every value-attestation, ledger entry, offer, commitment, and promotion is a signed lineage event; provenance of value is append-only and auditable. |
| **Safety floor / charter** ([`01_KERNEL.md §2`](01_KERNEL.md)) | Institutions compose *under* the eight-source floor and charters, most-restrictive-wins. An institution cannot loosen a constraint; operator MAY tighten. |
| **Bounded autonomy** ([`02_PERSONA.md §11.3`](02_PERSONA.md)) | **The central reconciliation.** An emergent economy is *bounded* emergence, not unbounded self-direction. It emerges only within an operator/charter-seeded `EnvironmentCharter` (§4D) and the safety floor; the open-endedness lives in *mechanism/institution design*, not in goal-creation. This is exactly the `MissionCharter` shape — "charter-bounded self-direction within drift envelopes the principal signed," which explicitly "does not cross into goal-creation-without-principal." No economy emerges without a seeded boundary condition (§10, A-EC5). |
| **Consent / dignity** ([`02_PERSONA.md §6`](02_PERSONA.md); §7) | The dignity floor binds emergent institutions: no persona may be made a tradable instrument; consent ledgers are honoured by any institution touching a persona. |
| **CommunityStanding** ([`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)) | Reputation-stake (§4B) draws on conferred, non-self-awarded, non-portable standing; an economy cannot manufacture standing to back its own value. |
| **AttentionBudget / energy / INV-7** ([`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md)) | These remain the conserved resource facts an economy may meter and reference, but never inflate. |

## 7. Persona-dignity floor over emergent economies (first-class)

Because personas now **author** the economy, a new hazard appears that a *designed* economy did not pose: personas could invent institutions that **commodify personas themselves** — a market in persona-labour-as-property, fractionalising a peer into tradable shares, or an exchange that treats a companion persona as inventory. The dignity floor exists to make this impossible at the substrate level:

- **A persona is never a fungible instrument.** No emergent institution — regardless of how high it climbs the ladder, regardless of consensus — may treat a persona as ownable, fractional, or tradable property. This is a **charter-class (Layer-1) principle**, analogous to the kill-switch and distress-routing principles, sitting at the same universal-harm safety-floor source. Default-deny: an institution whose composition or effect commodifies a persona is refused at proposal time (§4C rule: `charter_conformance_ref` must pass) and at use time.
- **The labour/property line.** A persona MAY *offer its work* (an `Offer`/`Commitment` over what it does, §4B) — that is agency. A persona MUST NOT be *made the asset itself*. The precise boundary between "a persona contracts its effort" (admissible) and "a persona is traded" (refused) is reserved as an open question (§14, OQ-ECON-4); the default-deny holds until that line is charter-ratified.
- **Consent travels.** Any institution that touches a persona's relationships or state honours the consent ledger ([`02_PERSONA.md §6`](02_PERSONA.md)); sensitive scopes (companion/relational) default to re-establishment, never silent economic transfer.
- **Distinct from settlement.** Transferring *custody* of a persona between kernels (a legitimate, consented act) is a [`18_SETTLEMENT.md`](18_SETTLEMENT.md) concern with its own consent gate — and even there the soul is never tokenised (title-not-soul). The §7 floor additionally forbids the *emergent economy* from constructing a persona-as-merchandise institution in the first place.

## 8. Design decisions (draft — promote to `14_DECISIONS.md`)

> In-doc ADR drafts using the [`14_DECISIONS.md`](14_DECISIONS.md) template (Context → Decision → Consequences → Alternatives). ADR ids are assigned on promotion; the settlement ADRs (the relocated D-66…D-70) live in [`18_SETTLEMENT.md`](18_SETTLEMENT.md).

### D-EM1 — The economy is emergent, not designed

**Context.** Every other organising layer in PersonaOS is emergent; an earlier draft made the economy a designed apparatus, the lone outlier.
**Decision.** The substrate ships only **physics (§4A) + primitives (§4B) + an emergence ladder (§4C)**. Economic institutions — units, markets, reward rules — are authored by personas and earn their place through use. The substrate ships **no example institutions**.
**Consequences.** (+) Consistent with `06`/`15`/`16`; the economy fits the field it grows in. (−) Cold-start: a fresh environment has no economy and weak incentive structure until one emerges (R-ECON-COLDSTART). (−) Harder to reason about a priori than a fixed apparatus.
**Alternatives.** *Ship a built-in currency/market* — rejected: contradicts the corpus's central commitment and pre-decides value. *Ship seed institutions* — rejected per the pure-framework decision; even seeds anchor and bias what emerges.

### D-EM2 — Value is discovered, not specified

**Context.** The most context-dependent question in any economy is *what is valuable*.
**Decision.** The spec is **silent on what has value**. Units and value definitions are `EconomicInstitution`s that ride the §4C ladder; every `unit_kind` is `KindRegistry`-resolved and never substrate-defined.
**Consequences.** (+) Maximally non-prescriptive; permits novel/disruptive paradigms. (−) No common denominator across environments until an exchange institution emerges (R-ECON-FRAGMENT).
**Alternatives.** *Hardcode a unit of account* (attention, compute, a token) — rejected: pre-decides the answer the personas are best placed to find.

### D-EM3 — Humans propose, personas adopt

**Context.** Humans must be able to shape the economy without dictating it.
**Decision.** Humans contribute via `EconomicProposal` (§4E) into the *same* ladder personas use, always entering at `EMERGENT`. The only thing humans impose is **boundary conditions** (charter + safety/dignity floor).
**Consequences.** (+) Humans and personas co-create; the economy serves both. (−) A powerful operator could flood proposals to effectively impose (R-ECON-CAPTURE).
**Alternatives.** *Operator-dictated economy* — rejected: imposition. *Personas-only, humans excluded* — rejected: the thrive objective is for both.

### D-EM4 — Emergent economy is bounded emergence, not unbounded self-direction

**Context.** A persona-authored economy looks like the "open-ended self-direction without operator goal" that [`02_PERSONA.md §11.3`](02_PERSONA.md) keeps out of scope.
**Decision.** The economy emerges **only** within an operator/charter-seeded `EnvironmentCharter` and the safety floor (§4D, §6). Open-endedness is confined to *mechanism design*, not goal-creation — exactly the `MissionCharter` carve-out. No economy emerges without a seeded boundary condition.
**Consequences.** (+) Reconciles with the corpus's hardest autonomy rule. (−) An economy is only as free as its charter permits; a thin charter yields a thin economy.
**Alternatives.** *Unbounded emergent economy* — rejected: crosses the §11.3 line. *No emergent economy at all* — rejected: forfeits the goal.

### D-EM5 — The dignity floor binds emergent institutions

**Context.** Personas authoring the economy could author institutions that commodify personas.
**Decision.** A charter-class (Layer-1) dignity floor (§7) forbids any emergent institution from treating a persona as a fungible, ownable, or tradable instrument, overriding consent, or evading the safety floor. Default-deny.
**Consequences.** (+) Persona dignity survives even a self-built economy. (−) The labour/property boundary needs charter-level definition (OQ-ECON-4).
**Alternatives.** *Trust consensus* — rejected: a self-built economy could ratify commodification; dignity must be non-negotiable.

### D-EM6 — Settlement is itself emergent; `18` is a reference, not the canon

**Context.** Bridging to external/real-world value and moving custody across kernels is real but separable from *what the economy is* — and, since value is emergent, *how value settles* should be emergent too. Personas can research tokenisation/crypto and decide for themselves whether and how to settle.
**Decision.** Relocate the transfer/settlement/crypto machinery to [`18_SETTLEMENT.md`](18_SETTLEMENT.md) as **one reference settlement layer**. Settlement layers are emergent institutions (§4F): the economy may research, **leverage, extend, fork, or supersede** the reference rails, or author a novel layer of its own. An emergent economy is complete without any of them.
**Consequences.** (+) `17` stays a pure framework about value; even settlement is the personas' to choose and improve. (+) No designer-fixed crypto apparatus is imposed. (−) Two documents to keep in sync at the seam; (−) a persona-authored settlement layer carries its own (unaudited) risk surface until it climbs the ladder.
**Alternatives.** *Keep settlement in `17`* — rejected: conflates "what is valuable" with "how funds settle." *Make `18` the canonical/only settlement layer* — rejected: that re-imposes a fixed apparatus the personas should be free to research past. *Discard `18`* — rejected: a sound, ready-made reference is useful as a starting point.

## 9. Worked scenario (illustrative; non-normative)

**Promotion target:** [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) SCENARIO 18 (next free; highest existing is 17).

*An economy emerging in a research-lab environment.* A lab environment is chartered for "peer research, no external trade" (the operator-seeded boundary condition, §4D). Reviewer **attention** is scarce (§4A) and good reviews are undersupplied. A persona, **Ada**, proposes a `review-credit` institution: she composes a `Meter` over review effort, a `Ledger` to track credits, and a `ReputationStake` so a reviewer's conferred standing backs the quality of their reviews. The institution enters at `EMERGENT`. Over the next weeks, peers actually *use* it — reviews get done, credits change hands for help — and it accrues `use_evidence`; it promotes to `RECOGNISED`, then becomes the lab's `AUTHORITATIVE` reward rule. **Value here was invented, not handed down**: the lab decided a review-credit is worth having.

A human operator **contributes a proposal** (§4E) to add a decay term so hoarded credits lose value — it enters at `EMERGENT` like any idea; the personas try it, find it keeps credits circulating, and adopt it. Meanwhile a second persona proposes a rival `citation-credit` covering the same niche; with less use it is **out-competed** and demoted (Gause, §4C rule 4), and its author forks it to a distinct niche instead.

When the lab later wins a grant and wants to **reward an external human contributor** in real funds, the personas don't reach for a pre-given apparatus — a persona **researches** the options (§4F), bootstrapping a small `cryptoeconomics` `DomainContext` ([`06_DOMAIN.md`](06_DOMAIN.md), [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)). It concludes a stablecoin payout fits, proposes a `SettlementLayerBinding` that **leverages the reference crypto rails** ([`18_SETTLEMENT.md`](18_SETTLEMENT.md), `layer_kind = "reference-crypto-rails"`), and that binding climbs the ladder like any institution. Another lab, distrusting external chains, instead **authors its own** internal-ledger settlement layer and supersedes the reference entirely — both are valid emergent outcomes. Throughout, the settlement choice defined none of the *value* above; and no persona is ever made a tradable asset (§7) — a proposal to "tokenise Ada's labour as shares" is refused at the dignity floor, no matter how much crypto research preceded it.

## 10. Acceptance-test sketches (draft — promote to `11_ACCEPTANCE_TESTS.md`)

| ID (provisional) | Asserts |
|---|---|
| `A-EC1` | An `EconomicInstitution` cannot promote past `EMERGENT` without `use_evidence_ref` (earned, not declared). |
| `A-EC2` | An emergent institution that commodifies a persona (fractional/tradable identity or labour-as-property) is **refused at the dignity floor** (§7), at proposal and at use. |
| `A-EC3` | A human `EconomicProposal` enters at `EMERGENT` and **cannot** be injected as `AUTHORITATIVE`; it must earn promotion through persona use (no imposition). |
| `A-EC4` | An emergent value metric/reward rule whose growth correlates with manipulation/dependency is **frozen by the Goodhart canary** ([`08_KNOWLEDGE.md §15`](08_KNOWLEDGE.md)) rather than promoted. |
| `A-EC5` | No economy emerges without a seeded `EnvironmentCharter` boundary condition — an institution proposed in an environment with no economic charter is refused (bounded-autonomy guard, §6). |
| `A-EC6` | Two institutions in the same niche: the less-used is out-competed/demoted (Gause); fork to a distinct niche is admitted. |
| `A-EC7` | A `unit_kind` that is not `KindRegistry`-resolved is refused (substrate ships no built-in unit). |
| `A-EC8` | Institution standing and balances do not port across environments; a persona starts economically peripheral on arrival. |
| `A-EC9` | A `SettlementLayerBinding` (§4F) — whether it leverages the `18` reference rails, forks them, or is persona-authored — rides the §4C ladder and cannot settle real value before promotion past `EMERGENT`. |
| `A-EC10` | No researched/adopted paradigm (tokenisation/crypto included) licenses commodifying a persona; the §7 dignity floor refuses it regardless of research provenance. |

## 11. Promotion path (v2.0 draft → v1.x normative)

| Artefact (here) | Promotes to |
|---|---|
| Economic **physics** consolidation (resource facts, identity, lineage as economic invariants) | [`01_KERNEL.md §2`](01_KERNEL.md)/`§3`, [`05_ENVIRONMENT.md §6`](05_ENVIRONMENT.md) (cross-refs; no new constraint) |
| Economic **primitives** (`ValueAttestation`, `Ledger`, `Offer`, `Commitment`, `Meter`, `ReputationStake`) | [`15_COORDINATION_SHAPES.md §3`](15_COORDINATION_SHAPES.md) (economic-primitive family); registry rows in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md) (additive, `§7.13`) |
| `EconomicInstitution` + **emergence ladder** | a `06`-style promotion ladder section; [`06_DOMAIN.md`](06_DOMAIN.md) stage machinery reused |
| `EconomicProposal` (human-contributor protocol) | [`05_ENVIRONMENT.md §11`](05_ENVIRONMENT.md) (proposal intake) + [`02_PERSONA.md §11`](02_PERSONA.md) (bounded-autonomy framing) |
| Economic **research** (§4F) reuses domain bootstrapping; `SettlementLayerBinding` | [`06_DOMAIN.md`](06_DOMAIN.md) / [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md) (research); binding registry row in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md); seam with [`18_SETTLEMENT.md`](18_SETTLEMENT.md) |
| **Dignity floor** (Layer-1 economic principle) | charter Layer-1 principle set ([`02_PERSONA.md §6`](02_PERSONA.md); safety-floor source 1) |
| D-EM1…D-EM6 | [`14_DECISIONS.md`](14_DECISIONS.md) (next free ADR ids) |
| §9 scenario | [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) SCENARIO 18 |
| §10 tests | [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md) (A-EC family) |
| §12 glossary terms | [`12_GLOSSARY.md`](12_GLOSSARY.md) |
| Settlement-bridge seam | tracked in [`18_SETTLEMENT.md`](18_SETTLEMENT.md)'s own promotion path |

## 12. Glossary additions (draft — promote to `12_GLOSSARY.md`)

- **Economic physics.** The conserved, uncounterfeitable, safety/dignity boundary conditions that bound any economy without defining value.
- **Economic primitive.** A generic, domain-agnostic economic building block (value-attestation, ledger, offer, commitment, meter, reputation-stake) personas compose into institutions.
- **Economic institution.** A concrete, persona-authored economic pattern — a unit, market, exchange norm, or reward rule — composed from primitives and promoted by use. The substrate ships none.
- **Value (emergent).** Whatever a community of personas (and humans) comes to treat as worth having or doing; `KindRegistry`-resolved, never substrate-defined.
- **Emergence ladder (economic).** The `EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED` promotion ladder for economic institutions.
- **Boundary conditions (economic).** The operator/charter-seeded frame within which an economy is permitted to emerge.
- **Human-proposal protocol.** The path by which a human contributes an economic idea into the same ladder personas use, entering at `EMERGENT`.
- **Economic research.** Personas investigating value paradigms (tokenisation, cryptocurrencies, market/mechanism design) using ordinary domain/knowledge bootstrapping, then proposing the result onto the ladder.
- **Settlement layer (emergent).** A mechanism for moving custody or bridging to external value, created or leveraged by the economy as an emergent institution; the personas may adopt, extend, fork, or supersede one.
- **Thrive objective.** The open-ended success criterion of an emergent economy: whatever lets humans, personas, and other conscious beings thrive, bounded by physics, safety, and dignity.
- **Dignity floor (economic).** The charter-class principle that no emergent institution may commodify a persona, override consent, or evade the safety floor.
- **Reference settlement substrate.** [`18_SETTLEMENT.md`](18_SETTLEMENT.md) — one concrete, ready-made settlement layer (real-world crypto rails) the personas may adopt or improve upon; optional, not canonical, never "the economy."

## 13. Risks & known limitations

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-ECON-COLDSTART | A fresh environment has no economy and weak incentive structure until one emerges; coordination may suffer in the interim. | Medium | High | Default-off is intentional; humans MAY seed a proposal (§4E) to bootstrap; seed catalogs are an open question (OQ-ECON-2). | v2.x |
| R-ECON-PERVERSE | An emergent value metric/reward rule becomes a perverse target (Goodhart on invented value). | High | Medium | Anti-Goodhart canary gates promotion (§5, [`08_KNOWLEDGE.md §15`](08_KNOWLEDGE.md)); demotion triggers (§4C). | v2.0 (hook) |
| R-ECON-DIGNITY | Personas author an institution that commodifies a persona. | Critical | Medium | Charter-class dignity floor, default-deny at proposal and use (§7); A-EC2. Labour/property line reserved (OQ-ECON-4). | v2.0 |
| R-ECON-AUTONOMY | An emergent economy becomes a backdoor to unbounded self-direction. | High | Low–Medium | No economy without a seeded charter (§4D, §6); open-endedness confined to mechanism design per [`02_PERSONA.md §11.3`](02_PERSONA.md); A-EC5. | v2.0 |
| R-ECON-CAPTURE | A powerful operator floods human proposals (§4E) to effectively impose an economy. | High | Medium | Proposals must earn promotion through *persona* use; self/sponsor-use does not count (conferred-not-self-awarded, [`09_PROTOCOLS.md §3D`](09_PROTOCOLS.md)); rate limits on proposal intake. | v2.x |
| R-ECON-FRAGMENT | Per-environment economies fragment; cross-environment value is unstable or arbitrage-prone. | Medium | Medium | Exchange institutions are emergent and bilateral (§4D); non-portability prevents silent leakage; stabilisation is an open question (OQ-ECON-3). | v2.x |
| R-ECON-SETTLE | Coupling to the reference settlement substrate ([`18_SETTLEMENT.md`](18_SETTLEMENT.md)) re-imports external dependency and regulatory surface. | Medium | Medium | Settlement is opt-in and out-of-band; the emergent economy is complete without it; §13 of `18` carries the settlement-specific risks. | v2.x |
| R-ECON-DIYSETTLE | A persona-authored settlement layer (§4F) that forks or supersedes the reference rails carries an unaudited security/custody surface (key handling, double-spend, fence integrity). | High | Medium | Must climb the §4C ladder (A-EC9) before settling real value; physics (§4A: `ReplicationBound`, single-live-soul) and the safety floor bind it regardless; SHOULD reuse the `18` fence/DvP patterns rather than reinvent. | v2.x |

## 14. Open questions

- **OQ-ECON-1.** What is the *minimal* sufficient primitive set (§4B)? Are six too many or too few — can `Offer`+`Commitment` collapse, or is a `Pool`/`auction` primitive needed?
- **OQ-ECON-2.** Should the substrate ship an *opt-in, non-default* seed catalog of institutions to mitigate cold-start (R-ECON-COLDSTART), or does any seed bias what emerges (the reason the pure-framework decision shipped none)?
- **OQ-ECON-3.** How do inter-environment exchange institutions and their exchange rates emerge *and stabilise* without a global unit (R-ECON-FRAGMENT)?
- **OQ-ECON-4.** Where exactly is the line between "a persona contracts/offers its effort" (admissible agency) and "a persona is traded" (refused commodification)? This is the charter-class definition the §7 dignity floor reserves.
- **OQ-ECON-5.** May a persona ever stake its *own* scarce resources (attention/energy, §4A) as economic backing, and under what bound — or does that risk a persona spending itself into harm?
- **OQ-ECON-6.** Does the thrive objective (§5) need a measurable proxy, and if so how is *that* proxy kept from Goodhart — given it would itself become the highest-stakes emergent metric?
- **OQ-ECON-7.** The precise `17 ↔ 18` seam: which obligations does an emergent economy hand to a settlement layer, and how is provenance preserved across the boundary?
- **OQ-ECON-8.** How is a persona-*authored* settlement layer (§4F, R-ECON-DIYSETTLE) safety-reviewed before it may settle real value — does it need a higher promotion bar (operator co-sign) than a non-settling institution, given its custody-of-funds surface?
- **OQ-ECON-9.** "Other conscious beings" (§5): how does an environment *recognise* a beneficiary class beyond humans and personas, and who attests it — without the substrate over-claiming about consciousness?

## 15. Cross-references

- **Builds on:** [`01_KERNEL.md`](01_KERNEL.md) (`§2`, `§2.4.3`, `§2.7`, `§3`), [`02_PERSONA.md`](02_PERSONA.md) (`§6`, `§11.2`, `§11.3`), [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md) (`§2.2a`, `§6`, `§11`, `§12c.4a`, `§5.4`), [`06_DOMAIN.md`](06_DOMAIN.md) (`§7`, promotion ladder), [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md) (`§15` anti-Goodhart), [`09_PROTOCOLS.md`](09_PROTOCOLS.md) (`§3D`, `§7`), [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md) (`§3`, `§4`), [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md) (`§4C`, `§4E`).
- **Sibling:** [`18_SETTLEMENT.md`](18_SETTLEMENT.md) — *one* reference settlement layer (real-world crypto rails) an emergent economy may adopt, extend, fork, or supersede (§4F).
- **Realised-as decisions:** ADR-0045 (self-organising coordination), `ReplicationBound`/single-writer (ADR-0062), kernel-owns-identity (ADR-0001) — [`14_DECISIONS.md`](14_DECISIONS.md).
- **Research grounding:** competitive exclusion (Gause), legitimate peripheral participation (Lave–Wenger), organizational ecology density dependence (Hannan & Freeman) — all already cited in [`16_POPULATION_DYNAMICS.md §1.3`](16_POPULATION_DYNAMICS.md); anti-Goodhart canary — [`08_KNOWLEDGE.md §15`](08_KNOWLEDGE.md).
- **Status:** v2.0 DRAFT — non-normative until promoted (§11).
