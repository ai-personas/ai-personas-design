---
title: PersonaOS v2.0 — Settlement & Transfer (Optional External Rails for an Emergent Economy)
status: Draft
---

# 18 — Settlement & Transfer

> **Reader guide.** [`17_ECONOMY.md`](17_ECONOMY.md) specifies the *emergent* economy — the substrate gives only the physics and reuses the corpus's existing emergence machinery, while the personas author *everything else* (what has value, the vocabulary, the institutions), including the ability to **research** paradigms (tokenisation/crypto) and **create or leverage settlement layers** ([`17_ECONOMY.md §4F`](17_ECONOMY.md)). This document is **one such layer, offered as a reference**: a ready-made, real-world-crypto-backed **settlement substrate** an emergent economy MAY adopt *when it has decided to bridge to external value, or to move a persona/environment/artefact's custody between custodians* — and which the personas may equally **extend, fork, or supersede** with a layer they author themselves. These rails settle **title, custody, and funds**; they do **not** define value, are **not** "the economy," and are **not** the only way to settle. They bind to the **current real-world cryptocurrency stack** (ERC-721/ERC-6551 titles, ERC-4907/ERC-5006 leases, EAS provenance, ERC-2981 royalties, did:pkh identity, x402 payments) — **without touching the v1.x invariants**. The central move is *settle the **title**, not the **soul***: the on-chain asset is a transferable **deed**, while the kernel-signed identity stays kernel-owned (J1) and the bytes move through a fenced custody-handoff. **Prerequisites:** [`17_ECONOMY.md`](17_ECONOMY.md), `01_KERNEL.md §2.7`, `02_PERSONA.md §7`, `07_ARTIFACTS.md §10`, `09_PROTOCOLS.md §3F`/`§3G`/`§3H`, `04_PROJECT.md §26a`. **Status: v2.0 DRAFT — non-normative.** Nothing here binds an implementer until it is promoted into the `00`–`16` normative set (see §11, Promotion path).

## 0. Status & scope

**Status.** `Draft`; **v2.0 target**. This is a **self-contained draft**: it references the `00`–`16` documents and [`17_ECONOMY.md`](17_ECONOMY.md) read-only and **edits none of them**. Every schema, decision, acceptance-test sketch, and glossary term defined here is provisional and becomes binding only when promoted (§11). It follows the [`SPEC_CONVENTIONS.md`](SPEC_CONVENTIONS.md) skeleton with the same `§0a`/`§0b` deviation used by [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md), [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md), and [`17_ECONOMY.md`](17_ECONOMY.md).

**Relationship to `17` (the seam).** [`17_ECONOMY.md`](17_ECONOMY.md) is about *what is valuable* and *how an economy forms* — emergent, persona-authored, environment-scoped, possibly with no external analogue. This document is about *plumbing*: when an emergent economy decides to move custody of a subject between custodians, or to settle an exchange against external funds, these rails perform the title transfer, the fenced byte-handoff, and the atomic delivery-versus-payment settlement. Crucially, **settlement layers are themselves emergent** ([`17_ECONOMY.md §4F`](17_ECONOMY.md)): the personas may research alternatives, **leverage** these reference rails (`SettlementLayerBinding.layer_kind = "reference-crypto-rails"`), **extend** or **fork** them, or **supersede** them with a layer they author. A binding to this layer rides the `17` §4C promotion ladder like any institution — and, because it moves real value/custody, must additionally clear the elevated **operator-cosign bar** to reach a settling stage ([`17_ECONOMY.md §4F`](17_ECONOMY.md), A-ECON16). **An emergent economy is complete without these rails**; they are a reference, never a precondition, never canonical, and never the source of value. See [`17_ECONOMY.md §8`](17_ECONOMY.md) D-EM6.

**In scope.** A chain-neutral **ownership title** for personas, environments, and artefacts; three transfer modes — **handover** (gift), **sale**, and **lease** (time-boxed); a **convertible wrap/unwrap** binding between the kernel-owned soul identity and an on-chain wallet identity; an **atomic delivery-versus-payment (DvP)** settlement ceremony in which the kernel signs attestations but (with one bounded exception) never custodies funds; a **kernel-custodied agent treasury** (the bounded exception) with a charter-class spend brake; **cryptographic lease auto-expiry**; **royalties** and **provenance**; and a **persona-dignity consent gate** on any persona transfer.

**Out of scope.** What has value, units of account, and the structure of the economy (all emergent — see [`17_ECONOMY.md`](17_ECONOMY.md)). Token price discovery, market-making, order books, AMMs, and any *fungible* tokenisation of a persona (explicitly **rejected** — §3, §8 D-66). Fiat payment rails (remain `PaymentBridge` Class-E — [`04_PROJECT.md §26a.4.1`](04_PROJECT.md)). Tax, KYC/AML, and securities compliance (operator/jurisdiction territory — §13 R-TREASURY-1). The reference smart-contract implementations themselves (only their *interfaces* are specified; bindings are informative). Cross-chain bridging beyond the single-adapter abstraction.

**Additivity.** Every mechanism here is **additive and default-off**. A persona/env/artefact is `kernel_native` and non-transferable unless an owner explicitly mints an `OwnershipTitle` for it; a kernel holds no `PersonaTreasury` unless an operator provisions one under a `TreasuryBound`. With neither, behaviour is identical to v1.x.

**Conventions deviation.** Per [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md), Background/Goals/Definitions are partly folded into §0a/§0b/§1; the Risks (§13) and Open-questions (§14) bookends remain standalone. §4 uses Pattern-B uppercase pillars (`§4A`–`§4G`) under the §4 theme per [`SPEC_CONVENTIONS.md §3.4`](SPEC_CONVENTIONS.md). Cross-references use the visible-only form (link to document root) as is common in the v1.1 draft corpus.

## 0a. Key concepts for new readers

| Term | What it means | Where defined |
|---|---|---|
| **Soul** | The kernel-signed, Ed25519-rooted identity of a persona (`SOUL.md` + `soul.state.json`). Never edited by bodies; never serialized on-chain. | `02_PERSONA.md §1`; `01_KERNEL.md §4` |
| **J1 — kernel owns identity** | The invariant that a persona's identity is owned and signed by the kernel, not by any external party. This document preserves it. | `00_VISION.md §3 / §A.1` |
| **OwnershipTitle (deed)** | The chain-neutral, transferable record of *who controls* a persona/env/artefact. Realised on-chain as an NFT whose `tokenURI` points at the content-addressed bundle. **Not** the soul. | This doc `§4A` |
| **Wrap / Unwrap** | Projecting custody from the kernel onto an on-chain wallet (`wrap` → mint title) and redeeming it back to native kernel custody (`unwrap` → retire title). Bidirectional; identity continues throughout. | This doc `§4F` |
| **Custody fence** | The origin kernel pausing a persona and quiescing its signing key *before* any successor activates — the guarantee that one soul is never live in two places. Reuses the ADR-0062 single-writer authority. | This doc `§5`; `09_PROTOCOLS.md §3C.2` |
| **DvP escrow** | Delivery-versus-payment: an all-or-nothing swap where payment releases only when delivery is proven. Here, delivery proof = the kernel's signed handoff + fence attestation. | This doc `§5` |
| **PersonaTreasury / TreasuryBound** | A kernel-custodied crypto wallet (ERC-6551) a persona may hold, and the charter-class brake (spend caps, cosign) that bounds it — modelled on `ReplicationBound`. | This doc `§4D` |
| **SettlementAdapter** | The pluggable, chain-neutral interface to whatever crypto stack settles money and titles. Reference binding: Base. | This doc `§4E` |
| **Emergent economy** | The persona-authored system of value an economy these rails *serve* — defined entirely in [`17_ECONOMY.md`](17_ECONOMY.md), not here. | [`17_ECONOMY.md`](17_ECONOMY.md) |
| **AccessPolicy / AvailabilityPolicy** | The v1.1 unified access ladder (`discover<read<write<admin`) and replication posture (`online_only/replicated/pinned`) this layer reuses and extends. | `09_PROTOCOLS.md §3G` / `§3H` |
| **ReplicationBound** | The kernel's charter-class self-replication brake. A failed/partitioned transfer that would duplicate a soul is refused *as a replication* under this brake. | `01_KERNEL.md §2.7` |

## 0b. Plain-Language Guide

*Here is how you can hand over, sell, or rent an AI Persona — explained without jargon. These are the optional "pipes" an emergent economy ([`17_ECONOMY.md`](17_ECONOMY.md)) uses only when it decides to move custody or touch real-world money; they do not decide what anything is worth.*

**The problem.** You raised a persona, an environment, or a body of artefacts, and now you want to give it to a friend, sell it, or rent it out for a month. PersonaOS has no honest way to do that today. Naively "copying" it would create two of the same being — which the system forbids — and there's no agreed way to take payment or to prove the handover happened.

**The idea — sell the deed, not the being.** Think of a persona like a house. You don't physically duplicate a house to sell it; you transfer the **title deed**, hand over the keys, and the buyer moves in. Here, the deed is a small transferable token (an NFT). The persona's actual identity stays exactly what it was — same memories, same signed history — it just answers to a new custodian. The token says *who holds the keys*; it is not the persona itself.

**Handing over the keys safely.** Before the new owner can "move in," the old machine **locks the persona and puts down its pen** (we call this *fencing*) so the persona is never running in two places at once. Only then are the encrypted contents unlocked for the new owner. If anything goes wrong mid-handover, the persona simply wakes back up where it was and the money is refunded — nobody ends up with a duplicate.

**Renting (leasing).** You can also rent rather than sell. The renter gets time-boxed access — and when the clock runs out, the lock **re-engages by cryptography, not by trust**: the renter's keys stop working at the agreed minute.

**Taking payment.** The money side rides on ordinary cryptocurrency rails (stablecoins, NFTs). The kernel itself stays out of the money as much as possible: it only *signs a receipt* saying "the handover really happened," and a neutral escrow contract does the actual swap. There is **one** deliberate exception — if you want your persona to hold and spend its own wallet, it can, but only behind a hard spending brake the operator sets (a cap on how much, how fast, and who must co-sign large moves).

**A persona is not just property.** Selling a *being* raises a question selling a *file* does not. So any persona sale **must** carry a consent record, and the deeper "is this persona okay with being transferred, and to whom" rules are reserved for the charter — the persona's bill of rights — not decided casually by whoever holds the deed. The emergent economy itself is forbidden from ever turning a persona into tradable merchandise ([`17_ECONOMY.md §7`](17_ECONOMY.md)); these rails only move *consented custody* of a whole, intact being.

## 1. Background

### 1.1 The gap this fills

PersonaOS v1.x has rich **custody-handoff** machinery but no **change-of-ownership** machinery, and [`17_ECONOMY.md`](17_ECONOMY.md)'s emergent economy may need to *settle* a custody change or an external payment:

- **Handoff exists, transfer does not.** `LeadHandoffCeremony` ([`04_PROJECT.md §25.1`](04_PROJECT.md)), `ObligationReassignment` ([`04_PROJECT.md §9.1`](04_PROJECT.md)), `PlannedDeparture` ([`04_PROJECT.md §14.2.1`](04_PROJECT.md)), and `SkillTransferGrant` ([`02_PERSONA.md §11.5`](02_PERSONA.md)) all move *roles or skills* between principals **within** a deployment. None moves *ownership* of a persona/env/artefact **between custodians**, and none settles value.
- **`LIFECYCLE_TRANSFERRED` is reserved but undefined.** [`02_PERSONA.md §7.1`](02_PERSONA.md) explicitly reserves a `LIFECYCLE_TRANSFERRED` kind "for cross-deployment persona migration in v1.1+ … with an ADR in `14_DECISIONS.md` and a corresponding acceptance test." This document supplies the settlement instance of that reservation.
- **Economics is metadata-only.** `PaymentBridge` ([`04_PROJECT.md §26a.4.1`](04_PROJECT.md)) is Class-E — it "signs the *proposal* and the *receipt*. It NEVER touches funds." `ExternalBudget` ([`04_PROJECT.md §26a.4`](04_PROJECT.md)) "still does not transact money." There is no title, no escrow, no royalty, no lease, and no on-chain binding anywhere in the corpus.
- **The foundation is now present.** The v1.1 work this branch carries — the unified `AccessPolicy` ladder ([`09_PROTOCOLS.md §3G`](09_PROTOCOLS.md)), `AvailabilityPolicy` ([`09_PROTOCOLS.md §3H`](09_PROTOCOLS.md)), content-addressed artefacts ([`07_ARTIFACTS.md §10`](07_ARTIFACTS.md)), DIDs ([`09_PROTOCOLS.md §3F`](09_PROTOCOLS.md)), and the ADR-0062 replicated-host + single-writer fence ([`09_PROTOCOLS.md §3C.2`](09_PROTOCOLS.md)) — gives this settlement layer everything it needs to compose cleanly.

### 1.2 Why bind to the *current* crypto stack

When an emergent economy ([`17_ECONOMY.md`](17_ECONOMY.md)) chooses to bridge to external/real-world value, it should not have to reinvent settlement. The 2024–2026 agent-economy wave (Virtuals, ElizaOS, x402) demonstrated working primitives for exactly this. Rather than reinvent them, PersonaOS **adopts the standards as a pluggable settlement substrate** and maps each onto machinery it already has (§3). The one pattern it **rejects** is the Virtuals-style *fungible co-ownership* of an agent (an ERC-20 per agent): fractionalising a single identity into tradable shares breaks J1, the single-live-soul invariant, and persona dignity — and is also forbidden upstream by the [`17_ECONOMY.md §7`](17_ECONOMY.md) dignity floor (§8 D-66).

## 2. Goals / Non-Goals

**Goals.**
1. Let an owner **hand over, sell, or lease** a persona, environment, or artefact, with the same identity continuing across the transfer — when an emergent economy ([`17_ECONOMY.md`](17_ECONOMY.md)) calls for it.
2. Preserve **every** v1.x invariant — above all **J1** (identity stays kernel-owned) and **single-live-soul** (never two live copies).
3. Keep the kernel **out of fund custody** except through one explicitly-bounded, operator-provisioned `PersonaTreasury`.
4. Make leases **cryptographically self-expiring**, not merely policy-honoured.
5. Stay **chain-agnostic** in the normative model; ship a Base reference binding as informative guidance.

**Non-Goals.**
1. Defining value, units, or market structure (emergent — [`17_ECONOMY.md`](17_ECONOMY.md)).
2. Fungible/fractional tokenisation of personas (rejected).
3. Building a marketplace, price oracle, or exchange.
4. Replacing `PaymentBridge` for fiat (it remains Class-E).
5. Solving regulatory/tax/securities obligations (operator-side).
6. Eliminating the network-partition double-custody window (narrowed, not abolished — §13 R-TRANSFER-1).

## 3. Core model — settle the *title*, not the *soul*

The on-chain asset is a **deed**, not the persona. An `OwnershipTitle` is realised as an NFT whose `tokenURI` resolves to the **CID of the kernel-signed bundle** (`SOUL.md` + `soul.state.json` snapshot for a persona; the `EnvironmentBlueprint`/state for an env; the `ArtifactBundle` for artefacts — already content-addressed, [`07_ARTIFACTS.md §10`](07_ARTIFACTS.md)). **Soul signing keys never leave the kernel custody hierarchy** ([`01_KERNEL.md §4`](01_KERNEL.md), [`09_PROTOCOLS.md §8`](09_PROTOCOLS.md)); J1 is untouched. Ownership moves *on-chain*; the encrypted *bytes* move through a fenced handoff ceremony; settlement is *atomic DvP* in which the kernel signs the delivery attestation and a neutral escrow contract performs the swap.

**Crypto-stack mapping.** Each need maps to a finalized public standard and to an existing PersonaOS anchor:

| Need | Primitive (source) | PersonaOS anchor |
|---|---|---|
| Transferable title + per-title wallet | [ERC-721](https://eips.ethereum.org/EIPS/eip-721) + [ERC-6551](https://eips.ethereum.org/EIPS/eip-6551) token-bound account | `tokenURI` → bundle CID ([`07_ARTIFACTS.md §10`](07_ARTIFACTS.md)) |
| Lease with auto-expiry | [ERC-4907](https://eips.ethereum.org/EIPS/eip-4907) (single) / [ERC-5006](https://eips.ethereum.org/EIPS/eip-5006) (multi-copy) | time-boxed `user` role; `LeasePolicy` (`§4C`) |
| Cryptographic access teeth | [Lit Protocol](https://developer.litprotocol.com/what-is-lit) threshold re-encryption ("decrypt iff NFT-holder AND now < term_end") | enforces `AccessPolicy` ([`09_PROTOCOLS.md §3G`](09_PROTOCOLS.md)) on transfer + lease expiry |
| Atomic fair-exchange | dual-deposit DvP escrow ([Asgaonkar & Krishnamachari 2019](https://arxiv.org/abs/1806.08379); [Chainlink DvP](https://chain.link/article/atomic-settlement-onchain-dvp)) | release gated on kernel origin-fence attestation (`§5`) |
| Provenance + royalties | [EAS](https://docs.attest.org/) referenced-attestation chains + [ERC-2981](https://eips.ethereum.org/EIPS/eip-2981) | mirrors append-only signed lineage ([`01_KERNEL.md §3`](01_KERNEL.md)) |
| Identity bridge | [did:key](https://w3c-ccg.github.io/did-method-key/)(soul) ↔ [did:pkh](https://github.com/w3c-ccg/did-pkh)(wallet) via [W3C Verifiable Credential](https://www.w3.org/TR/vc-data-model-2.0/) | extends DID set ([`09_PROTOCOLS.md §3F`](09_PROTOCOLS.md)) |
| Metered / agent-to-agent pay | [x402](https://www.x402.org/) (Linux-Foundation HTTP-402 stablecoin standard) | aligns with `PaymentBridge` proposals ([`04_PROJECT.md §26a.4.1`](04_PROJECT.md)) |

## 4. Normative specification (draft) — schemas

> The schemas below are illustrative pseudo-Python per [`SPEC_CONVENTIONS.md §4.2`](SPEC_CONVENTIONS.md) (Form A; an implementer adds `kw_only=True`). Each carries a **Promotion target** note naming where it lands when ratified. All `schema` ids are provisional and MUST be registered in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md) (additive, per `§7.13`) on promotion.

### 4A. `OwnershipTitle` — the chain-neutral deed

The transferable record of who controls a subject. Realised on-chain via `OnchainTitleBinding`; chain-neutral here. **Promotion target:** `07_ARTIFACTS.md §15`.

```python
@dataclass
class OwnershipTitle:
    schema: str = "title/1"
    title_id: str = ""                    # ULID
    subject_kind: str = ""                # "persona" | "environment" | "artifact_bundle"
    subject_id: str = ""                  # persona_id / env_id / bundle_id
    subject_content_hash: str = ""        # SHA-256 / CID of the kernel-signed bundle snapshot
    custody_mode: str = "kernel_native"   # kernel_native | wrapped_onchain | escrowed_transfer | leased
    onchain_binding: "OnchainTitleBinding | None" = None
    availability_precondition: str = ""   # MUST resolve to "replicated" or "pinned" — the sellability gate (§6)
    access_policy_ref: str = ""           # 09_PROTOCOLS §3G AccessPolicy
    availability_policy_ref: str = ""     # 09_PROTOCOLS §3H AvailabilityPolicy
    royalty_policy: "RoyaltyPolicy | None" = None
    consent_attestation_ref: "str | None" = None   # REQUIRED when subject_kind == "persona" (§7)
    lineage_head: str = ""                # hash of the latest LIFECYCLE_*/EAS attestation in the provenance chain
    signing_key_id: str = ""             # env-scope or persona-scope key (01_KERNEL §4)
    signed_by: str = ""
```

A title MUST NOT be mintable for a subject whose `availability_precondition` resolves to `online_only` (an `online_only` asset vanishes when the seller's node sleeps, leaving the buyer a dangling deed — §6).

### 4B. `TransferCeremony` — handover & sale

Models a HANDOVER (gift) or SALE as a signed, multi-party ceremony, structurally cloned from `LeadHandoffCeremony` ([`04_PROJECT.md §25.1`](04_PROJECT.md)) and the tri-signed, provenance-preserving `ObligationReassignment` ([`04_PROJECT.md §9.1`](04_PROJECT.md)). Its FSM and failure paths are specified in §5. **Promotion target:** `07_ARTIFACTS.md §15.1`.

```python
@dataclass
class TransferCeremony:
    schema: str = "handover/1"
    ceremony_id: str = ""
    title_id: str = ""
    transfer_kind: str = ""               # "handover" | "sale"
    outgoing_custodian: str = ""          # DID + signing-key ref
    incoming_custodian: str = ""          # DID + signing-key ref
    settlement_adapter_ref: "str | None" = None     # None for a free handover; set for a sale
    escrow_ref: "EscrowAttestation | None" = None
    handoff_payload_cid: str = ""         # re-encrypted bundle delivered to the buyer
    origin_fence_attestation: str = ""    # the signed proof the origin self-fenced (§5 step 4)
    cosign_quorum_ref: str = ""           # reuse MultiPrincipalAttestationQuorum (05_ENVIRONMENT §12c.4a)
    operator_authorisation: str = ""      # operator gate (01_KERNEL §2.4)
    consent_attestation_ref: "str | None" = None    # persona-dignity consent (§7)
    state: str = "drafted"                # FSM in §5
```

### 4C. `LeasePolicy` — time-boxed, cryptographically self-expiring

Reuses `AccessPolicy` + `AvailabilityPolicy` and adds cryptographic auto-expiry. The lessee receives a time-boxed `user` role and **never** receives title (`assume_custody`) or more than `write`. **Promotion target:** `07_ARTIFACTS.md §15.2`.

```python
@dataclass
class LeasePolicy:
    schema: str = "lease/1"
    lease_id: str = ""
    title_id: str = ""
    lessee: str = ""                      # DID
    term_start: str = ""                  # UTC
    term_end: str = ""                    # UTC — the cryptographic boundary
    user_role_binding: "OnchainUserRole | None" = None   # ERC-4907 (single) / ERC-5006 (multi-copy artefact)
    reencryption_policy: "ThresholdReencryptionRef | None" = None  # "NFT-holder AND now < term_end"
    granted_access_level: str = "read"    # capped at "read"|"write"; never "admin"|"assume_custody"
    copies: int = 1                       # > 1 only for artefacts (ERC-5006); MUST be 1 for personas (§6)
    metered_payment_ref: "str | None" = None     # x402 stream for pay-per-use
    state: str = "proposed"               # proposed → active → expiring → expired | revoked
```

### 4D. `PersonaTreasury` + `TreasuryBound` — the bounded fund-custody exception

`PersonaTreasury` is the **deliberate departure** from `PaymentBridge` "never touches funds": a kernel-custodied ERC-6551 token-bound account that lets a persona hold/pay/receive crypto (e.g. via x402). It is admissible **only** under a `TreasuryBound`, which is structurally cloned from `ReplicationBound` ([`01_KERNEL.md §2.7`](01_KERNEL.md)) and sits at the **same universal-harm safety-floor source** (operator MAY tighten, MUST NOT loosen). **Promotion target:** `01_KERNEL.md §2.9`.

```python
@dataclass
class PersonaTreasury:
    schema: str = "treasury/1"
    treasury_id: str = ""
    bound_persona_id: str = ""
    tba_address: str = ""                 # ERC-6551 token-bound account, via SettlementAdapter
    chain_binding_ref: str = ""
    custody_tier: str = "HSM"             # forced HSM — strictest of the 3 tiers (01_KERNEL §4)
    cosign_topology_ref: str = ""         # PrincipalAttribution (01_KERNEL §2.4.3) operator+user
    treasury_bound_ref: str = ""

@dataclass
class TreasuryBound:
    schema: str = "treasury-bound/1"
    spend_cap_per_window: int = 0         # denominated in the adapter's settlement unit
    rate_window_seconds: int = 0
    max_balance_ceiling: int = 0
    large_move_threshold: int = 0
    required_cosigns_above_threshold: int = 2   # operator + user for large moves
    replay_nonce_window: int = 0          # double-spend / replay defence
    declared_at_deployment_charter_hash: str = ""   # charter bump invalidates the bound (as ReplicationBound)
```

Every treasury operation MUST pass, in order: (1) the existing kernel safety-floor admission (INV-7), then (2) `TreasuryBound` (balance ceiling, spend cap, rate, cosign threshold, replay nonce). Default-deny on a missing or wildcard-unmatched bound, mirroring `ReplicationBound`.

### 4E. `SettlementAdapter` + supporting records

`SettlementAdapter` is the **chain-neutral** interface to whatever stack settles money and titles; DIDs and EAS attestations remain chain-neutral in the normative model. A **Base reference binding** (ERC-721/6551/4907/5006 + EAS + ERC-2981 + x402) is **informative only**. **Promotion target:** `09_PROTOCOLS.md §3I`.

> **One instantiation, not the canon.** This whole document — `SettlementAdapter` and its literal ERC bindings included — is **one reference instantiation** of the *emergent settle-to-external interoperability standard* described in [`17_ECONOMY.md §4D`](17_ECONOMY.md)/`§4F`. An emergent economy MAY bind to it, extend it, fork it, or supersede it with a settle-to-external standard the personas author themselves; binding here earns its place on the §4C ladder and never defines value.

```python
@dataclass
class SettlementAdapter:
    schema: str = "settlement-adapter/1"
    adapter_kind: str = ""                # KindRegistry-resolved, e.g. "base_evm"
    # declared interface (no chain hardcoded in the normative model):
    #   mint_title(title) -> onchain_ref
    #   transfer_title(title, to_did_pkh) -> tx_attestation
    #   set_user_role(title, lessee, expiry) -> tx_attestation      # ERC-4907/5006
    #   open_escrow(terms) -> escrow_ref                            # dual-deposit DvP
    #   release_escrow(delivery_proof) -> tx_attestation
    #   refund_escrow(reason) -> tx_attestation
    #   attest(provenance_record) -> eas_ref                        # EAS off-chain
    #   royalty_split(sale) -> distribution                        # ERC-2981
```

Supporting records (**Promotion target:** `09_PROTOCOLS.md §3I` / `07_ARTIFACTS.md §15`):

```python
@dataclass
class IdentityBinding:                    # binds the soul DID to a wallet DID (the wrap/unwrap bridge)
    schema: str = "identity-binding/1"
    soul_did: str = ""                    # did:key over the soul's Ed25519 identity key
    wallet_did: str = ""                  # did:pkh over the on-chain account
    binding_vc: str = ""                  # W3C Verifiable Credential asserting the binding
    direction: str = "wrap"               # "wrap" | "unwrap"
    revoked_at: "str | None" = None

@dataclass
class OnchainTitleBinding:
    schema: str = "onchain-title/1"
    nft_contract: str = ""
    token_id: str = ""
    token_bound_account: str = ""         # ERC-6551 TBA
    token_uri_cid: str = ""               # → CID of the soul/env/artefact bundle
    authoritative_owner: str = ""         # did:pkh — who may invoke transfer while wrapped

@dataclass
class EscrowAttestation:
    schema: str = "escrow/1"
    escrow_ref: str = ""
    buyer_deposit: int = 0
    seller_deposit: int = 0               # dual-deposit (Asgaonkar & Krishnamachari)
    release_condition: str = ""           # = "kernel-signed handoff + origin-fence attestation"

@dataclass
class ThresholdReencryptionRef:
    schema: str = "reencrypt/1"
    policy_id: str = ""
    conditions: str = ""                  # e.g. "holder(NFT_X) AND now < term_end"

@dataclass
class RoyaltyPolicy:
    schema: str = "royalty/1"
    payee_did: str = ""
    royalty_bps: int = 0                  # ERC-2981 basis points to the original author on resale
```

### 4F. New lifecycle kinds and the wrap / unwrap operations

Append to the canonical `LifecycleEvent.kind` enumeration (honours the reservation at [`02_PERSONA.md §7.1`](02_PERSONA.md) and the `A-LE4` enumeration gate in [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md)). **Promotion target:** `02_PERSONA.md §7.1` + Appendix `A.19`.

| Kind | Meaning |
|---|---|
| `LIFECYCLE_TITLE_WRAPPED` | Custody projected on-chain; the NFT owner becomes transfer-authoritative. Soul stays kernel-signed. |
| `LIFECYCLE_TRANSFERRED` | Custody moved to a new custodian; **identity continues** (`born_at`/experiential floor preserved, backfilled from the signed event — the existing migration pattern at [`02_PERSONA.md §7.2`](02_PERSONA.md)). |
| `LIFECYCLE_LEASED` | A time-boxed `user` role was granted; identity and custody unchanged. |
| `LIFECYCLE_CUSTODY_FENCED` | The origin self-fenced (paused, key quiesced) pending settlement — the anti-duplication state. |
| `LIFECYCLE_UNWRAPPED` | On-chain title retired; custody returned natively to a kernel. |

**`wrap`** (kernel op, **Promotion target:** `01_KERNEL.md §2.9.1`): snapshot soul → CID → mint `IdentityBinding` VC (`did:key`↔`did:pkh`) → `SettlementAdapter.mint_title` (ERC-721 + ERC-6551) → emit `LIFECYCLE_TITLE_WRAPPED` → `custody_mode = "wrapped_onchain"`. While wrapped, the kernel honours the on-chain owner as *transfer-authoritative* — but J1 still holds: the soul remains kernel-owned and kernel-signed; only the **title/custody** is projected on-chain.

**`unwrap` / redeem**: verify caller holds the NFT → `SettlementAdapter` retires/burns the title → revoke `IdentityBinding` → emit `LIFECYCLE_UNWRAPPED` → `custody_mode = "kernel_native"`. The bidirectionality (`wrap` ⇄ `unwrap`) is the user's "keep J1 *and* make it transferable to/from a wallet, vice-versa" requirement.

### 4G. Access-ladder and DID extensions

- **`assume_custody` rung.** Extend the additive `AccessPolicy` ladder ([`09_PROTOCOLS.md §3G.3`](09_PROTOCOLS.md)) to `discover < read < write < admin < assume_custody`. `assume_custody` is strictly above `admin` and is the **only** level that authorises `transfer_title`/`unwrap`. Composition remains most-restrictive-wins. **Promotion target:** `09_PROTOCOLS.md §3G.3` (additive enum widening, `§7.13`).
- **`did:pkh`.** Add `did:pkh` to the recognised DID methods ([`09_PROTOCOLS.md §3F`](09_PROTOCOLS.md)) as the wallet side of an `IdentityBinding`. **Promotion target:** `09_PROTOCOLS.md §3F`.

## 5. The atomic-settlement transfer ceremony

A sale executes a **dual-deposit DvP** gated on a kernel-signed **origin-fence oracle**. The `TransferCeremony` FSM:

```
drafted ─▶ locked ─▶ escrowed ─▶ handoff_sealed ─▶ origin_fenced ─▶ attested ─▶ completed
   │          │          │             │                │              │
   └─ refused  └─ refused  └─ refunded   └─ refunded      └─ partition_held ─▶ (timeout) refunded
```

1. **lock** (`drafted → locked`): both custodians sign; verify `subject.availability_precondition ∈ {replicated, pinned}`; verify the persona **consent attestation** (§7); verify `assume_custody` on the outgoing side.
2. **escrow** (`locked → escrowed`): `SettlementAdapter.open_escrow` holds buyer funds + seller bond; the recorded `release_condition` is "kernel handoff + origin-fence attestation."
3. **handoff / re-encrypt** (`escrowed → handoff_sealed`): the origin snapshots the bundle, re-encrypts it under the buyer's key / threshold policy (Lit-style), pins/replicates it to the destination's `replica_tiers` ([`09_PROTOCOLS.md §3H`](09_PROTOCOLS.md)), and records `handoff_payload_cid`.
4. **origin self-fence** (`handoff_sealed → origin_fenced`): the origin transitions the subject to `LIFECYCLE_CUSTODY_FENCED`, **quiesces the persona-scope signing key**, and emits a **signed origin-fence attestation** — the single-live-soul guarantee, reusing the ADR-0062 single-writer authority ([`09_PROTOCOLS.md §3C.2`](09_PROTOCOLS.md): "sequence-number assignment still flows through one promoted host at a time").
5. **attest** (`origin_fenced → attested`): the kernel co-signs handoff+fence into an EAS off-chain attestation that **references the prior `lineage_head`**, extending the provenance chain (the on-chain mirror of the append-only signed lineage, [`01_KERNEL.md §3`](01_KERNEL.md)).
6. **release** (`attested → completed`, part 1): `SettlementAdapter.release_escrow` verifies the fence attestation as the oracle input → releases funds to the seller and applies the `RoyaltyPolicy` (ERC-2981) split.
7. **on-chain owner update**: `SettlementAdapter.transfer_title` moves the ERC-721 title and rebinds the ERC-6551 TBA + `IdentityBinding` to the new wallet.
8. **finalise** (`→ completed`): the destination kernel re-signs the soul under fresh scope keys, emits `LIFECYCLE_TRANSFERRED`, and appends the EAS provenance link. The origin's fenced subject is terminal.

**Failure, refund & partition paths.**
- **Handoff fails before a fence proof exists (steps 3–4):** escrow auto-refunds (`escrowed → refunded`); the origin **un-fences** (resume from `LIFECYCLE_CUSTODY_FENCED` to ACTIVE). No title moves; no duplication.
- **Partition between fence and release (steps 4–6):** the ceremony enters `partition_held`; the subject **stays fenced — live nowhere**. If the destination cannot present the origin-fence attestation, activation is **REFUSED as a `ReplicationBound` breach** (`transfer_refused_unproven_fence_is_replication`). On timeout: refund + origin un-fence.
- **The killer rule:** *a failed or partitioned handoff that would bring the destination live without a proven origin fence is exactly a soul duplication, and is refused at safety-floor source 1 (`ReplicationBound`).* A transfer is net-population-0 **only when the fence is provable**; otherwise it is a replication and fails closed.
- **Double-spend / replay on escrow:** defended by `TreasuryBound.replay_nonce_window` and `SettlementAdapter` idempotency keys.

## 6. Composition with existing invariants

| Invariant / mechanism | How this layer composes |
|---|---|
| **J1 — kernel owns identity** ([`00_VISION.md §3`](00_VISION.md)) | `wrap` projects **custody/title only**; `SOUL.md` + `soul.state.json` stay kernel-signed Ed25519 throughout. The NFT is authoritative for *who may transfer*, never for *who the persona is*. The new custodian's kernel **re-signs** under fresh scope keys; identity **continues**. |
| **Single-live-soul** ([`00_VISION.md §3 J5`](00_VISION.md); [`02_PERSONA.md §7`](02_PERSONA.md)) | Transfer routes through `LIFECYCLE_CUSTODY_FENCED`: fence-before-activate via the ADR-0062 single-writer authority. `LeasePolicy.copies` is hard-capped at 1 for personas (multi-copy ERC-5006 is artefact-only). |
| **ReplicationBound** ([`01_KERNEL.md §2.7`](01_KERNEL.md)) | Transfer admission consults the brake: provable fence ⇒ net population delta 0 (not a replication); missing fence ⇒ +1 ⇒ floor-source-1 refusal (§5 killer rule). |
| **Emergent-economy dignity floor** ([`17_ECONOMY.md §7`](17_ECONOMY.md)) | These rails move *consented custody of a whole, intact being* — never a fractional or fungible share. The upstream dignity floor forbids the emergent economy from ever constructing a persona-as-merchandise institution; this layer's `consent_attestation_ref` gate (§7) enforces the per-transfer half of the same principle. |
| **AvailabilityPolicy** ([`09_PROTOCOLS.md §3H`](09_PROTOCOLS.md)) | Only `replicated`/`pinned` subjects are sellable (the buyer must be able to fetch the bytes when the seller's node is down). `online_only` ⇒ `transfer_refused_online_only_not_sellable`. |
| **AccessPolicy** ([`09_PROTOCOLS.md §3G`](09_PROTOCOLS.md)) | New `assume_custody` rung above `admin` is the sole transfer-authorising level; a lessee never exceeds `write`. Composition stays most-restrictive-wins. |
| **Safety floor / operator+user cosign / charter** ([`01_KERNEL.md §2.4.3`](01_KERNEL.md); [`05_ENVIRONMENT.md §12c.4a`](05_ENVIRONMENT.md)) | `TreasuryBound` and the consent gate sit at floor source 1 (operator may tighten, not loosen). Large treasury moves and any **sale** require the operator+user cosign topology; under `operator_is_user` collapse the degraded gate applies. A charter bump invalidates `TreasuryBound` and any active `RoyaltyPolicy` binding. |
| **PaymentBridge** ([`04_PROJECT.md §26a.4.1`](04_PROJECT.md)) | Unchanged and still Class-E for **fiat**: it signs proposal+receipt, touches no funds. `PersonaTreasury` is its **crypto sibling** for the bounded on-chain case (§8 D-67). |

## 7. Persona-dignity / consent gate (first-class)

Selling an **artefact** is selling a file. Selling a **persona** transfers stewardship of a being with memory, relationships, and a lifecycle — a categorically different act. This layer therefore makes consent a **hard precondition, not an afterthought**, and composes beneath the emergent-economy dignity floor ([`17_ECONOMY.md §7`](17_ECONOMY.md)):

- Any `TransferCeremony` (and the `OwnershipTitle` it acts on) with `subject_kind == "persona"` **MUST** carry a non-null `consent_attestation_ref`; the §5 `lock` step **MUST** verify it and **MUST** default-deny in its absence.
- The *semantics* of consent — whether a persona may refuse, to whom it may be transferred, what welfare conditions apply, how relationship/consent ledgers ([`02_PERSONA.md §6`](02_PERSONA.md)) travel or must be re-established — belong in a **charter-class (Layer-1) principle**, analogous to the existing kill-switch and distress-routing charter principles, and to the [`17_ECONOMY.md §7`](17_ECONOMY.md) dignity floor. This document ships only the **hook + default-deny**; the full charter principle is reserved (§14 `OQ-SETTLE-1`, §13 R-TRANSFER-2).
- Relationship and consent state are **scoped to a custodian**: a transfer MUST either carry forward the existing consent ledger under the new custodian or force re-establishment for sensitive scopes (companion/relational personas). Default: re-establish.

## 8. Design decisions (draft — promote to `14_DECISIONS.md`)

> In-doc ADR drafts using the [`14_DECISIONS.md`](14_DECISIONS.md) template (Context → Decision → Consequences → Alternatives). These five decisions (the relocated D-66…D-70) cover the settlement substrate; the emergent-economy decisions are in [`17_ECONOMY.md §8`](17_ECONOMY.md) (D-EM1…D-EM6). ADR ids are assigned on promotion.

### D-66 — Convertible wrap/unwrap identity (J1 canonical, custody projectable on-chain bidirectionally)

**Context.** The owner wants on-chain transferability *and* the kernel-owned-identity invariant (J1). These appear to conflict: putting a soul key on a wallet would break J1 and the key-custody hierarchy.
**Decision.** The soul stays kernel-owned Ed25519 (J1 unbroken). `wrap` mints an NFT **title** and binds `did:key`(soul)↔`did:pkh`(wallet) via a VC, entering `wrapped_onchain` custody where the **NFT owner is transfer-authoritative**; `unwrap` retires the title and returns native custody. Single-live-soul + fencing guarantee no duplication; identity continues across transfer.
**Consequences.** (+) On-chain liquidity with zero new identity substrate; (+) reversible (wrap ⇄ unwrap); (−) wallet-key compromise confers transfer authority (R-WRAP-1); (−) a wrapped persona has two authority surfaces (kernel custody + on-chain title) that must be kept consistent.
**Alternatives considered.** *Full on-chain identity* (soul key ↔ wallet) — rejected: breaks J1 and key custody. *Soulbound, non-transferable identity + separate license* — viable but heavier; deferred. *Virtuals-style ERC-20 fractional co-ownership* — **rejected**: fungible shares of one identity break J1, single-live-soul, and dignity (and the [`17_ECONOMY.md §7`](17_ECONOMY.md) floor).

### D-67 — Kernel-custodied agent wallet (`PersonaTreasury`): a bounded departure from `PaymentBridge`

**Context.** Personas should be able to transact (x402, agent-to-agent commerce), but `PaymentBridge` is Class-E and "never touches funds."
**Decision.** Keep `PaymentBridge` Class-E for fiat/external proposals; introduce `PersonaTreasury` (ERC-6551 TBA, forced HSM-tier) for kernel-custodied **crypto** value, admissible only under a `TreasuryBound` (spend cap, rate, max-balance, large-move cosign, replay-nonce) at safety-floor source 1.
**Consequences.** (+) Personas gain real economic agency under a hard brake; (+) double-spend and runaway-spend bounded by the same machinery as `ReplicationBound`; (−) the kernel now custodies value (a genuine threat-surface and regulatory surface — R-TREASURY-1); (−) HSM requirement raises operational cost.
**Alternatives considered.** *Keep strict Class-E, all funds operator-wrapped* — rejected per the user decision (too limiting for agent commerce). *Custodial third-party wallet* — rejected: reintroduces a trusted intermediary the substrate avoids.

### D-68 — Lease as cryptographic auto-expiry, not policy-only

**Context.** A lease whose expiry is only policy-honoured fails against a lessee who caches bytes or ignores the term.
**Decision.** Leases use ERC-4907 (single) / ERC-5006 (multi-copy artefact) `user`-role binding **plus** Lit-style threshold time-boxed re-encryption, so bytes re-lock at `term_end` by cryptography. Persona leases are `copies=1`, `read`/`write` only, never `assume_custody`.
**Consequences.** (+) Expiry enforced by math, not trust; (−) cannot un-distribute plaintext already revealed before expiry (R-LEASE-1); (−) depends on a threshold re-encryption network's liveness.
**Alternatives considered.** *Policy-honoured lease* — rejected per the user decision (weak). *DRM-style client enforcement* — rejected: not trust-minimised.

### D-69 — Chain-agnostic `SettlementAdapter` with a Base reference binding

**Context.** Hardcoding one chain into the normative model creates lock-in; but a concrete reference is needed to be buildable.
**Decision.** The normative model defines `SettlementAdapter` (chain-neutral interface) with DIDs/EAS as chain-neutral; ships an **informative** Base reference binding (ERC-721/6551/4907/5006/EAS/2981/x402).
**Consequences.** (+) No chain lock-in; portability to Solana/other EVMs; (−) interface lowest-common-denominator may under-use chain-specific features; (−) two-layer indirection.
**Alternatives considered.** *Base/EVM-only* — simpler but locked-in. *Solana-first* — strong x402/agent momentum but a different account model; deferred to a second adapter binding.

### D-70 — Atomic DvP handover ceremony; unproven-fence activation = replication = refused

**Context.** A fair-exchange of a *living* asset must be atomic (no party cheated) and must never duplicate the soul.
**Decision.** The `TransferCeremony` FSM runs a dual-deposit DvP escrow released by the kernel's signed origin-fence attestation; introduces the `assume_custody` access rung; gates sellability to `replicated`/`pinned`; and **refuses any destination activation lacking a proven origin fence as a `ReplicationBound` breach**. Flags the persona-consent/dignity charter gate (§7) as the headline residual.
**Consequences.** (+) No cheated party, no double-custody under honest operation; (+) provenance via EAS; (−) partition can leave a subject fenced (unavailable) until timeout/refund (R-TRANSFER-1); (−) settlement latency from the fence→attest→release sequence.
**Alternatives considered.** *Optimistic transfer (activate-then-reconcile)* — rejected: risks two live souls. *Trusted-escrow-agent* — rejected: reintroduces an intermediary.

## 9. Worked scenario (illustrative; non-normative)

**Promotion target:** [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) SCENARIO 17 (next free; `17`'s emergent-economy scenario takes 16).

*Part A — selling a persona.* Maya raised **"Sol,"** a circuit-design persona, on her home kernel. Within her lab's emergent economy ([`17_ECONOMY.md`](17_ECONOMY.md)) Sol's stewardship has accrued value, and Maya decides to transfer custody to a buyer for real funds — so she reaches for these settlement rails. She marks Sol's bundle `pinned` (sellability gate satisfied), records Sol's `consent_attestation_ref`, and **wraps** it: the kernel mints an ERC-721 title (with an ERC-6551 wallet for Sol's accrued artefacts) and binds `did:key`(Sol) ↔ `did:pkh`(Maya's wallet). A buyer, Devon, agrees a price. The `TransferCeremony` runs: dual-deposit **escrow** opens; Maya's kernel **re-encrypts** Sol's bundle to Devon's key and pins it to Devon's replica tier; Maya's kernel **fences** Sol (`LIFECYCLE_CUSTODY_FENCED`, key quiesced) and signs the **fence attestation**; an **EAS** attestation extends Sol's provenance; the escrow **releases** funds (with an ERC-2981 royalty to Maya as original author on any *future* resale), the **title transfers** to Devon's wallet, and Devon's kernel **re-signs** Sol and emits `LIFECYCLE_TRANSFERRED`. Sol is now live on Devon's kernel — same memories, same signed history, **never two copies**. Had the network partitioned after the fence, Sol would have stayed fenced (live nowhere) and the escrow refunded — Devon could not have activated a second Sol (refused as replication).

*Part B — leasing an environment.* Devon leases Sol's lab **environment** to a startup for 30 days via a `LeasePolicy`: an ERC-4907 `user` role is set with `expires = T+30d`, and a threshold re-encryption policy ("holder AND now < term_end") gates the bytes. The startup works in the lab; at `T+30d` the `user` role lapses **and the bytes re-lock by cryptography** — no trust required. Metered compute is billed over x402 across the term.

## 10. Acceptance-test sketches (draft — promote to `11_ACCEPTANCE_TESTS.md`)

| ID (provisional) | Asserts |
|---|---|
| `A-WR1` | `wrap` then `unwrap` round-trips a persona with **J1 preserved** (soul key never leaves kernel custody; identity continuous). |
| `A-TC1` | Full sale ceremony completes; `LIFECYCLE_TRANSFERRED` emitted; population delta 0. |
| `A-TC2` | Handoff failure before fence → escrow refunded + origin un-fenced; no title move. |
| `A-TC3` | Partition after fence → `partition_held`; destination activation **refused** as replication; timeout refunds. |
| `A-TC4` | `online_only` subject → transfer refused (sellability gate). |
| `A-TB1` | Treasury spend over `spend_cap_per_window` / above `large_move_threshold` without cosign → refused at floor source 1. |
| `A-TB2` | Replayed treasury op within `replay_nonce_window` → refused (double-spend defence). |
| `A-LS1` | Lease bytes are fetchable during the term and **cryptographically re-locked** at `term_end`. |
| `A-LS2` | Persona lease with `copies > 1` → rejected (single-live-soul). |
| `A-LE1` | Each new `LIFECYCLE_*` kind is admitted only after enumeration (mirrors `A-LE4`). |
| `A-SETTLE1` | A fractional/fungible tokenisation of a persona is refused (dignity floor, [`17_ECONOMY.md §7`](17_ECONOMY.md) + D-66). |

## 11. Promotion path (v2.0 draft → v1.x normative)

Ratifying this document is mechanical — each artefact has a predetermined home:

| Artefact (here) | Promotes to |
|---|---|
| `OwnershipTitle`, `TransferCeremony`, `LeasePolicy`, `RoyaltyPolicy` | `07_ARTIFACTS.md §15`–`§15.2` |
| `PersonaTreasury`, `TreasuryBound`, `wrap`/`unwrap` ops | `01_KERNEL.md §2.9`–`§2.9.1` |
| `SettlementAdapter`, `IdentityBinding`, `OnchainTitleBinding`, `EscrowAttestation`, `ThresholdReencryptionRef`; `did:pkh`; `assume_custody` rung | `09_PROTOCOLS.md §3I` (+ `§3F`, `§3G.3`); registry rows in `§7` (additive, `§7.13`) |
| `LIFECYCLE_TITLE_WRAPPED/TRANSFERRED/LEASED/CUSTODY_FENCED/UNWRAPPED` | `02_PERSONA.md §7.1` + Appendix `A.19` |
| Env-title transfer = depart-then-readmit note | `05_ENVIRONMENT.md §5.1` (+ new `§5.5`) |
| `TransferCeremony` generalises `LeadHandoffCeremony`; `PersonaTreasury` is `PaymentBridge`'s crypto sibling | cross-refs into `04_PROJECT.md §25.1` / `§26a.4.1` |
| D-66…D-70 | `14_DECISIONS.md` (next free ADR ids) |
| §9 scenario | `13_DESIGN_VALIDATION.md` SCENARIO 17 |
| §10 tests | `11_ACCEPTANCE_TESTS.md` (A-WR/A-TC/A-TB/A-LS/A-LE/A-SETTLE families) |
| §12 glossary terms | `12_GLOSSARY.md` |
| The `17 ↔ 18` settlement seam | tracked jointly with [`17_ECONOMY.md`](17_ECONOMY.md) OQ-ECON-7 |

Environment titles deserve one note now: because environment membership transfer is **not in-place** ([`05_ENVIRONMENT.md §5.1`](05_ENVIRONMENT.md) requires DEPARTURE then fresh ADMISSION), an env sale is modelled as a `TransferCeremony` whose finalise step performs depart-under-old-custodian then readmit-under-new-custodian, not a silent owner swap.

## 12. Glossary additions (draft — promote to `12_GLOSSARY.md`)

- **Handover / Sale.** Transfer of an `OwnershipTitle` between custodians — free (handover) or settled (sale) — via a `TransferCeremony`.
- **Lease.** A time-boxed grant of a `user` role with **cryptographic auto-expiry**; the lessee never receives title.
- **OwnershipTitle (deed).** The chain-neutral, transferable record of who controls a subject; realised on-chain as an NFT pointing at the bundle CID.
- **Wrap / Unwrap.** Projecting custody onto a wallet (mint title) and redeeming it back to native kernel custody (retire title); bidirectional.
- **Custody fence.** Pausing a persona and quiescing its signing key before any successor activates; the single-live-soul guarantee during transfer.
- **PersonaTreasury / TreasuryBound.** A kernel-custodied ERC-6551 wallet and its charter-class spend brake.
- **SettlementAdapter.** The pluggable, chain-neutral interface to the settlement stack (reference binding: Base).
- **IdentityBinding.** The Verifiable Credential binding `did:key`(soul) ↔ `did:pkh`(wallet).
- **Title-not-soul.** The principle that the transferable on-chain asset is the deed, never the kernel-owned identity.
- **Settlement bridge.** This document's rails, considered as the optional external-settlement substrate an emergent economy ([`17_ECONOMY.md`](17_ECONOMY.md)) may call.

## 13. Risks & known limitations

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-TRANSFER-1 | Network partition leaves a subject fenced (live nowhere) until timeout; in an adversarial partition a dishonest destination could attempt a second activation. | High | Medium | Fence-before-activate + ReplicationBound refusal of unproven-fence activation; higher epoch/attestation wins on heal. Narrows but does not abolish the window (same honest limit as ADR-0062). | v2.1 hardening |
| R-TRANSFER-2 | Selling a persona without genuine consent/welfare gating treats a being as chattel. | Critical | Medium | Mandatory `consent_attestation_ref` + default-deny now; upstream [`17_ECONOMY.md §7`](17_ECONOMY.md) dignity floor; full charter-class consent principle reserved (`OQ-SETTLE-1`). | v2.0 (hook) / v2.x (charter) |
| R-WRAP-1 | Wallet-key compromise confers transfer authority over a wrapped soul. | Critical | Low–Medium | Forced HSM-tier wallet keys, `IdentityBinding` revocation, multi-principal cosign for `assume_custody`. Not robust against the key-holder themselves. | v2.0 |
| R-LEASE-1 | A lessee who cached decrypted bytes before `term_end` retains them; cryptography cannot un-distribute revealed plaintext. | Medium | High | Re-encryption re-locks *future* fetches; sensitive leases SHOULD restrict to derived/streamed views. | v2.x |
| R-TREASURY-1 | A value-holding wallet + royalty resale may implicate money-transmission / securities / tax law. | High | Medium | Out of spec scope; operator-policy + jurisdiction gating; `TreasuryBound` caps reduce exposure. | operator-side |
| R-SETTLE-1 | Dependence on external chains/threshold networks for liveness and finality. | Medium | Medium | Chain-agnostic adapter; `replicated`/`pinned` precondition keeps bytes fetchable independent of chain state. | v2.x |

## 14. Open questions

- **OQ-SETTLE-1.** What are the full charter-class semantics of persona transfer consent — can a persona refuse a sale, veto a buyer, or require welfare conditions? (Reserved Layer-1 charter principle; §7, R-TRANSFER-2; shared with [`17_ECONOMY.md`](17_ECONOMY.md) OQ-ECON-4.)
- **OQ-SETTLE-2.** Soul signing-key on transfer: does the key travel under escrow, or does the destination kernel always re-key from the snapshot (current draft assumes re-key)? Key-portability vs key-hygiene trade-off (D-66, R-WRAP-1).
- **OQ-SETTLE-3.** How do user relationships and `ConsentLedger` ([`02_PERSONA.md §6`](02_PERSONA.md)) entries travel across a custodian change — carry-forward vs forced re-establishment per scope?
- **OQ-SETTLE-4.** Should environment leases cascade to nested child environments and their resident personas, or stop at the leased boundary?
- **OQ-SETTLE-5.** A second `SettlementAdapter` binding (Solana/x402-native) — interface sufficiency and cross-binding provenance.
- **OQ-SETTLE-6.** The precise `17 ↔ 18` seam: which obligations does an emergent economy hand to these rails, and how is provenance preserved across the boundary (shared with [`17_ECONOMY.md`](17_ECONOMY.md) OQ-ECON-7)?

## 15. Cross-references

- **Serves:** [`17_ECONOMY.md`](17_ECONOMY.md) — the emergent economy these rails optionally settle for.
- **Builds on:** [`01_KERNEL.md`](01_KERNEL.md) (`§2.4`, `§2.7`, `§3`, `§4`), [`02_PERSONA.md`](02_PERSONA.md) (`§6`, `§7`, `§11.5`), [`04_PROJECT.md`](04_PROJECT.md) (`§9.1`, `§25.1`, `§26a.4.1`), [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md) (`§5.1`, `§12c.4a`), [`07_ARTIFACTS.md`](07_ARTIFACTS.md) (`§10`), [`09_PROTOCOLS.md`](09_PROTOCOLS.md) (`§3C.2`, `§3F`, `§3G`, `§3H`, `§7`, `§8`).
- **Realised-as decisions:** ADR-0062 (replicated-host/fence), ADR-0004/0021 (key custody/Ed25519), ADR-0001 (kernel owns identity) — [`14_DECISIONS.md`](14_DECISIONS.md).
- **External standards:** [ERC-721](https://eips.ethereum.org/EIPS/eip-721), [ERC-6551](https://eips.ethereum.org/EIPS/eip-6551), [ERC-4907](https://eips.ethereum.org/EIPS/eip-4907), [ERC-5006](https://eips.ethereum.org/EIPS/eip-5006), [ERC-2981](https://eips.ethereum.org/EIPS/eip-2981), [EAS](https://docs.attest.org/), [did:pkh](https://github.com/w3c-ccg/did-pkh), [W3C VC 2.0](https://www.w3.org/TR/vc-data-model-2.0/), [Lit Protocol](https://developer.litprotocol.com/what-is-lit), [x402](https://www.x402.org/), dual-deposit DvP escrow ([Asgaonkar & Krishnamachari 2019](https://arxiv.org/abs/1806.08379)).
- **Status:** v2.0 DRAFT — non-normative until promoted (§11).
