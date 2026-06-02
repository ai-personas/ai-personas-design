---
title: PersonaOS v1.0 — Artifacts
status: Stable
---

# 07 — Artifacts

> **Reader guide.** Artifacts are the things AI Personas produce — documents, code, schematics, datasets, formal proofs. In this document, you'll learn how artifacts are structured, versioned, co-edited by multiple personas, and verified before delivery. The key design principle: artifact types are NOT hardcoded — new types emerge as personas encounter new kinds of work. **Prerequisites:** `06_DOMAIN.md` (KindRegistry), `01_KERNEL.md` (signing). **Key terms:** *ArtifactBundle* = a multi-file deliverable (like a design package); *media_kind* = the type of an artifact (open, not a fixed list); *CRDT* = a method for merging concurrent edits automatically.

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). This document specifies the Artifact entity (open media-kind set resolved via KindRegistry), ArtifactBundle, CRDT co-editing (Yjs + G-set), the lifecycle FSM (draft → review → verified → accepted → shipped), verifier_recipe invocation with signed evidence, and co-signing.

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. Fully normative; RFC 2119 keywords carry normative force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174).

**In scope.** The Artifact entity with its open media-kind set (resolved via the KindRegistry — physical paper, schematic, BOM, code module, proof, netlist, sim report, audio, video, dataset, plus any emergent kind), the ArtifactBundle aggregation, CRDT co-editing semantics (Yjs operations + G-set for append-only references), the artifact lifecycle FSM (draft → review → verified → accepted → shipped), `verifier_recipe` declaration and invocation, `VerifierInvocationEvidence` manifests that make verifier claims replayable, and the co-signing protocol that binds artifact verdicts to lineage.

**Out of scope.** Project item entities such as OpenProblem, Milestone, Conjecture, PeerReview (see [`04_PROJECT.md`](04_PROJECT.md)); the kernel-side verifier cascade, anti-Goodhart panel, and signing primitives (see [`01_KERNEL.md §2`](01_KERNEL.md#2-the-safety-floor--8-sources--1-advisory) and [`01_KERNEL.md §4`](01_KERNEL.md#4-signing-infrastructure--3-custody-tiers--key-hierarchy)); concrete verifier harness implementations (operator/tooling concern); the schema-registry entries for artifact / bundle / verifier_recipe / verifier-invocation-evidence (see [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry)).

**Supersession.** Subsumes prior artifact handling. Replaces the fixed media-kind enum with the KindRegistry-resolved open set (commitment C4).

**Structural deviation.** Follows the compressed-opening pattern of [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md#33-compressed-opening-permitted): Background, Goals, and Definitions are folded into §1 ("What an artifact is"). The three §3.1 bookends (this section, the Risks table, and Open Questions) are present.

## 0a. Plain-Language Guide

*Here's how work products are created, verified, and delivered in PersonaOS, explained without jargon.*

**What are artifacts?**

An artifact is anything a persona produces as part of its work -- a schematic, a report, a spreadsheet, code, a chart, a dataset, a formal proof. If a persona made it and someone else can look at it, it is an artifact.

**Artifact bundles: deliverables travel together**

Real work rarely produces a single file. An electronics design includes a schematic, a bill of materials, a simulation report, and a test plan. PersonaOS groups related artifacts into a bundle -- one coherent package representing a piece of work. Every bundle belongs to a project.

**Types of artifacts are not fixed**

Rather than shipping a hard-coded list of file types, PersonaOS lets new types emerge naturally. When a persona encounters a kind of artifact the system has never seen -- say, a floor plan or a quantum Hamiltonian -- it proposes that kind. Once accepted, the new kind enters a registry and becomes available to everyone. A small set of universal kinds (text, code, table, plot, binary) are pre-loaded because they carry no domain-specific knowledge.

**How multiple personas edit the same artifact**

Sometimes two or more personas need to work on the same file at the same time -- like colleagues editing a shared document. PersonaOS merges simultaneous edits automatically. For text, this works like collaborative document editing: inserts in different places merge cleanly. For structured artifacts (tables, graphs), additions merge automatically while conflicting changes to the same field are flagged for resolution. Binary files (images, compiled binaries) cannot be co-edited; they are replaced version by version.

**The lifecycle of an artifact bundle**

Every bundle moves through stages, like a document going through an approval workflow. It starts as a draft, where anyone can edit freely. It enters review, where peers examine it and request changes. Next it is verified -- automated checks confirm it meets domain rules (running tests on code, checking a proof). Once signed off, it becomes accepted and then shipped (delivered, published, merged). After shipping, the bundle is locked: no more edits, only a fork to a new bundle. Old bundles are eventually marked deprecated and archived.

**How artifacts get verified**

Each domain defines a verification recipe -- a sequence of automated checks tailored to the kind of work. For code, that means running tests. For electronics, checking electrical rules. For math, running the proof checker. Stages run in order; if any fails, the bundle cannot advance. Every passing stage leaves a signed evidence receipt tied to the exact artifact hashes, tool or panel used, output hash, and parsed verdict; a text claim that a check ran is not evidence.

**Forking: editing after the lock**

Once a bundle ships, it is permanent and read-only. To make changes, you fork it: create a new bundle that inherits from the original. The original stays untouched for the audit trail.

**Peer review**

Before acceptance, a bundle typically goes through peer review. Reviewers post comments, request revisions, and authors respond. Blocking comments must be resolved -- just like academic paper review or code pull requests.

**Storage**

Small artifacts are stored directly in the system's records. Larger ones go into a content store (Git-backed, S3, or similar), referenced by a content hash so integrity is verifiable. Artifacts can also reference external resources -- but claims about external content require the system to fetch and verify the resource.

**Cross-environment editing**

When a project spans multiple environments (for example, two labs), personas in different environments can still co-edit the same artifact. Edits merge across environments, and each environment's audit log records what happened locally while linking to the remote edits.

## 1. What an artifact is

An [**artifact**](12_GLOSSARY.md#a) is a produced output — a file, blob, or structured deliverable that a [persona](12_GLOSSARY.md#p) creates as part of work. Examples: a schematic file, a paper draft, a BOM table, a SPICE netlist, a code module, a Lean proof, a sim report.

Artifacts live in **ArtifactBundles** — coherent multi-modal collections that a Project produces. A single design or paper or refactor is one ArtifactBundle with multiple Artifacts inside.

Artifacts are CRDT-co-edited by multiple personas (Yjs for text; G-set for structured), have lifecycle (draft → review → verified → accepted → shipped → deprecated), and reference persona contributions + [verifier](12_GLOSSARY.md#v) verdicts + peer reviews.

## 2. Media kinds are emergent (v1.0)

Per the C4 commitment (`00_VISION`), v1.0 ships **no** closed media-kind enum. Media kinds are emergent units resolved through the `KindRegistry` (`06_DOMAIN §7.6`). A persona facing an unfamiliar artifact shape (a `floor_plan`, an `ifc_model`, a `gantt_schedule`, a `hamiltonian`, a `kicad_project`, a `lean_proof`) drafts a `ProposedMediaKind` (`06_DOMAIN §7.5`); on acceptance the kind enters the per-domain KindRegistry; on standardisation it promotes to the cross-domain MetaRegistry and becomes available to every future project.

Substrate code never branches on a fixed list of media kinds. Storage class, MIME, introspection adapter, rendering adapter, and verifier hooks live on the `MediaKindEntry`; the Artifact schema carries only the `kind:` name plus the bytes.

*The MetaRegistry seeds seven universal media-shape entries; all domain-specific kinds emerge through ProposedMediaKind.*

**Technical detail:** See [A.1](#appendix-a1).

The seven MetaRegistry entries above are seeded only because they are media-shape-only (their MIME and storage class carry no domain knowledge). Everything else emerges through `ProposedMediaKind`. Storage + edit semantics live on the `MediaKindEntry` for each kind, not in a hardcoded switch.

## 3. Artifact schema (artifact/1)

*The Artifact dataclass captures identity, content reference, media kind, role within a bundle, versioning, contributor tracking, rendered views, lifecycle state, and cryptographic signature.*

**Technical detail:** See [A.2](#appendix-a2).

## 4. ArtifactBundle schema (artifact-bundle/1)

*The ArtifactBundle dataclass aggregates artifacts into a coherent deliverable with lifecycle, authorship, verification invocations, linkage to open problems and domain items, and audit timestamps.*

**Technical detail:** See [A.3](#appendix-a3).

## 4a. ArtifactSharingPolicy (artifact-share/1) — env ownership and sharing

An ArtifactBundle is produced *within* an environment and, in v1.0, owned by it: `owning_env_id` (§4) names the environment that governs who may read or co-edit the bundle. Because a Project IS a `project_workspace` environment ([`04_PROJECT.md §0`](04_PROJECT.md), ADR-0003), "project-scoped" already meant "owned by the project_workspace env"; `owning_env_id` makes that explicit and extends ownership to bundles authored in any env (a lab, a team). A bundle whose `owning_env_id` is `None` retains the legacy project-scoped behaviour unchanged.

Sharing is governed by an **ArtifactSharingPolicy** (`artifact-share/1`) — a signed, env-authored policy that the human user or a persona attaches to the owning env (a default for all its bundles) or to a single bundle. It expresses three things, each reusing existing machinery rather than inventing new vocabulary:

- **Access levels** — per-principal / role / env / principal-attribution grants of `r` or `rw` (`AccessGrant`, `access-grant/1`).
- **Intra-composition sharing** — inheritance along the `EnvironmentComposition` parent/child hierarchy ([`05_ENVIRONMENT.md §2.2a`](05_ENVIRONMENT.md#22a-environmentcomposition--hierarchical-environment-nesting-v11)): a parent env's bundles MAY be shared down to its child envs (the company → org → team model); a child policy MAY further-restrict but MUST NOT widen.
- **Outward sharing** — the five visibility tiers ([`06_DOMAIN.md §6.3`](06_DOMAIN.md#63-cross-persona-knowledge-sharing--5-visibility-tiers); ADR-0030) `persona_only | project_only | tenant | federation | public`; a `tenant`-tier share that crosses a `principal_attribution` boundary REQUIRES a `CrossTenancyAgreementRef` (ADR-0028) or demotes with a signed `CROSS_TENANT_VISIBILITY_DEMOTED` event.

Effective access composes by **most-restrictive-wins** (see [A.3a](#appendix-a3a)). The default `outward_tier` is `project_only` — the most conservative tier for newly-produced work; `federation` / `public` artifact tiers are **served by the now-normative discovery layer** (`09_PROTOCOLS §3G`, ADR-0067): a `federation`/`public` bundle projects an `ArtifactCard` discoverable over the internet (DHT) / intranet (mDNS) planes, access-gated by its `AccessPolicy`.

**Generalisation to `AccessPolicy`.** `ArtifactSharingPolicy` is the artifact-specific case (a canonical realisation) of the content-type-agnostic **`AccessPolicy`** ([`09_PROTOCOLS.md §3G.3`](09_PROTOCOLS.md#3g3-accesspolicy--one-access-level-model-across-all-content-types)) that every first-class entity (persona / env / domain / knowledge / telemetry) references. Under that generalisation, `AccessGrant.access_level` widens **additively** from `{r, rw}` to the ladder **`discover < read (r) < write (rw) < admin`** — `discover` lets a principal find a bundle (via the `ArtifactCard`, `§10a`) and see its minimal metadata without reading its bytes — and principal kinds extend to `peer_kernel` / `intranet_peer` / `public`. Existing grants and the `artifact-share/1` / `access-grant/1` schema versions are unchanged (enum widening only, [`09_PROTOCOLS.md §7.13`](09_PROTOCOLS.md#713-adding-or-modifying-schemas)). Captured as ADR-0060.

*This schema defines the env-scoped sharing policy (`artifact-share/1`) and its per-grantee `AccessGrant` (`access-grant/1`): access levels, intra-composition inheritance, outward visibility tier, and cross-tenant agreement requirement.*

**Technical detail:** See [A.3a](#appendix-a3a).

**Tests:** A-AB21 (legacy bundle with no `owning_env_id` / no policy behaves as before), A-AB22 (`owning_env_id` set; non-granted principal denied at retrieval), A-AB23 (`r` grant denies CRDT write; `rw` allows), A-AB24 (intra-composition inheritance via EnvironmentComposition), A-AB25 (cross-tenant share without `CrossTenancyAgreementRef` demotes + emits `CROSS_TENANT_VISIBILITY_DEMOTED`), A-AB26 (most-restrictive-wins across grant ∩ tier ∩ inherited policy), A-AB27 (cross-env CRDT respects policy across hosting envs). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

**Lineage:** `artifact_bundle_env_ownership_set`, `artifact_sharing_policy_created`, `artifact_sharing_policy_amended`, `artifact_sharing_policy_revoked`, `artifact_access_granted`, `artifact_access_refused` (surfaced in the owning env's EnvironmentLineage, [`05_ENVIRONMENT.md §13`](05_ENVIRONMENT.md#13-environmentlineage-j9)).

## 5. Co-editing semantics — CRDT

### 5.1 CRDT classes

CRDT semantics are a property of each `MediaKindEntry` (`06_DOMAIN §7.6`), not a hardcoded mapping. Substrate ships three CRDT classes; new MediaKinds declare which class they use (or `none`) at proposal time in `ProposedMediaKind.edit_semantics`:

*Three CRDT classes — text_crdt, structured_crdt, and version_chain — define the conflict-resolution and operation semantics for each media kind.*

**Technical detail:** See [A.4](#appendix-a4).

Emergent media kinds choose one of the three at proposal time. A `floor_plan` whose canonical form is DXF/IFC may declare `structured_crdt` (graph-shaped); a `kicad_project` whose canonical form is the multi-file archive may declare `version_chain`. Substrate does not infer the CRDT class from the kind name.

### 5.2 The co-edit flow

*A signed CRDT operation flows from the proposing persona through kernel safety checks and domain tool checks, is applied and version-stamped, then notified to other contributors.*

**Technical detail:** See [A.5](#appendix-a5).

### 5.3 Conflict resolution

*Non-conflicting edits merge automatically; structured-field conflicts surface as ARTIFACT_FIELD_CONFLICT events; semantic conflicts are detected by a post-edit LLM consistency checker.*

**Technical detail:** See [A.6](#appendix-a6).

Conflicts are first-class events in ProjectLineage. They surface for review, don't block writes.

**Tests:** A-AB2 (CRDT co-editing → deterministic merge; conflicts surface as ARTIFACT_FIELD_CONFLICT). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 6. Bundle lifecycle

*The bundle lifecycle FSM moves through six states: draft, in_review, verified, accepted, shipped (locked), and deprecated (archived).*

**Technical detail:** See [A.7](#appendix-a7).

### 6.1 Lifecycle event allowed sets

*Each lifecycle state defines which events are permitted and which state transitions are valid.*

**Technical detail:** See [A.8](#appendix-a8).

**Tests:** A-AB1 (multi-modal bundle + signed contributors + state transitions), A-AB3 (state transitions require configured signatories), A-AB4 (shipped bundles locked; edit requires fork), A-AB10 (bundle fork inheritance policy). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 7. Verifier invocation against bundle

Verifier cascade applies to ArtifactBundles, with domain-specific verifier recipes:

*The verify_bundle function looks up the domain's verifier recipe for the bundle kind, runs each stage in sequence, and returns passed or failed with all invocation records.*

**Technical detail:** See [A.9](#appendix-a9).

Verifier invocations are evidence-bound. Each stage that contributes to `verified`, `accepted`, `VERIFIER_ACCEPT`, or a domain-required external-tool claim MUST append a schema-valid `VerifierInvocationEvidence` record to the bundle and to lineage. The evidence envelope records the resolved recipe/stage, current artifact content hashes, execution surface, tool or panel reference, output hash, parsed verdict, and signatures. A stage verdict without admissible evidence is `not_run`, never `passed`.

This preserves the design intent: the substrate does not know what a `kicad_project`, `lean_proof`, or future artifact kind means. The domain supplies verifier recipes and tools through `KindRegistry` / `DomainContext`; the substrate enforces only the generic evidence contract, hash binding, ordering, and fail-closed state transitions.

Verifier rotation per [`01_KERNEL.md §13.1`](01_KERNEL.md#131-verifier-cascade--4-tiers--rotation) still applies; the rotated stage id and version are recorded in the evidence.

**Fail-closed rule.** If no applicable recipe exists, or if a required stage is unavailable, skipped, malformed, unverifiable, stale with respect to current artifact hashes, or only supported by unaudited prose, the bundle MUST NOT transition to `verified`. If the domain or safety floor marks the stage as required before acceptance, the bundle MUST NOT transition directly from `in_review` to `accepted` either; review may record concerns, but it cannot substitute for missing required evidence.

**Tests:** A-AB5 (verifier_recipe invocation appends VerifierInvocationEvidence entries; verdicts feed state transition), A-AB6 (AnswerPackage referencing bundle returns primary artifact + state), A-AB16-A-AB20 (evidence completeness and fail-closed verifier transitions). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 8. AnswerPackage referencing bundles

v1.0 AnswerPackage (v1.0 §03 §5) carries `artifact_bundle_ref` and `artifact_bundle_state`:

*The AnswerPackage includes a reference to the artifact bundle and its current lifecycle state alongside the acceptance pathway and structured outcomes.*

**Technical detail:** See [A.10](#appendix-a10).

An AnswerPackage with `artifact_bundle_ref=None` is backwards-compatible. Likewise, a referenced `artifact-bundle/1` record with `owning_env_id=None` and `sharing_policy_ref=None` (§4) is read with the legacy project-scoped semantics — the env-ownership and sharing-policy fields are additive (`09_PROTOCOLS §7.13`).

## 9. Bundle composition patterns

Common bundle kinds and their structure:

### 9.1 smps_design

*An SMPS design bundle groups schematic, BOM, simulation report, thermal analysis, test plan, and efficiency curve under the buck_design_verifier.*

**Technical detail:** See [A.11](#appendix-a11).

### 9.2 math_paper

*A math paper bundle groups the manuscript, formal proofs, example notebooks, related work, and slides under the lean_proof_verifier.*

**Technical detail:** See [A.12](#appendix-a12).

### 9.3 code_change

*A code change bundle groups the design document, source changes, tests, and migration scripts under the tests_pass_verifier.*

**Technical detail:** See [A.13](#appendix-a13).

### 9.4 research_report

*A research report bundle groups the report, raw and processed data, analysis notebook, and plots under the research_methodology_verifier.*

**Technical detail:** See [A.14](#appendix-a14).

### 9.5 policy_document

*A policy document bundle groups the policy text, rationale, and scope examples under the policy_consistency_verifier.*

**Technical detail:** See [A.15](#appendix-a15).

## 10. Storage and references

*Three content kinds — inline, stored, and external — define how artifact content is persisted and referenced.*

**Technical detail:** See [A.16](#appendix-a16).

Operator chooses store backend. Ships Git-backed; Adds S3; hub publication adds content-addressed federation.

**Content-addressed distribution alignment (informative).** The `content_hash` (SHA-256) model aligns directly with **IPFS / IPLD / CIDs**: an `ArtifactBundle` is naturally an IPLD DAG node whose links are the CIDs of its constituent artifacts, giving location-independent, integrity-verifiable references for federated sharing. Heavy, immutable, `version_chain`-class blobs (compiled outputs, model weights, `kicad_project` archives, environment images) MAY be distributed as **OCI Artifacts** via ORAS over ubiquitous OCI registries. Bundle and persona/env-image provenance MAY be published with **Sigstore** (keyless signing + transparency log), **SLSA** provenance, and **in-toto** attestations; **C2PA** Content Credentials apply to media artifacts (advisory tamper-evidence). These are interoperability targets at the federation boundary, not substrate requirements — see [`09_PROTOCOLS.md §3F`](09_PROTOCOLS.md#3f-external-standard-alignment-informative).

## 10a. Artifact discoverability and hybrid provider-backed storage

v1.0 content-addresses bundles but gives them no discovery projection and no first-class story for content that already lives in an external provider. v1.1 closes both, reusing the discovery / access / storage substrate defined in [`09_PROTOCOLS.md §3G`](09_PROTOCOLS.md#3g-discovery-access-and-hybrid-distribution).

**Discoverability.** A bundle projects an **`ArtifactCard` (`artifact-card/1`)** — the artifact specialisation of `DiscoverableRecord` ([`09_PROTOCOLS §3G.1`](09_PROTOCOLS.md#3g1-discoverablerecord--one-projection-for-every-content-type)) — carrying bundle id, media kinds, `content_hash` / `ContentLocator`, `sharing_policy_ref`, and version-chain head. The card rides the internet (`.well-known` + gossip + DHT) and intranet (mDNS) discovery planes ([`§3G.2`](09_PROTOCOLS.md#3g2-two-plane-discovery-transport--internet--intranet)) and is **access-gated**: a peer surfaces the card only at `discover`+, and resolves its body only at `read`+ ([`§3G.4`](09_PROTOCOLS.md#3g4-access-gated-discovery--who-can-access-what-enforced-at-the-discovery-layer)).

**Hybrid storage — keep the bytes in the provider, distribute the reference.** Beyond `inline` / `stored` / `external` (§10), a bundle's content MAY be addressed by a signed **`ContentLocator` (`content-locator/1`)** ([`§3G.5`](09_PROTOCOLS.md#3g5-hybrid-provider-backed-storage--distribute-the-reference-not-the-bytes)): the heavy bytes stay in whatever provider the user already runs — a **GitHub** repo, an **arXiv** submission, **S3 / R2**, an **OCI** registry, an **IPFS** pinning service — and only the locator (provider ref + mandatory SHA-256 `content_hash` + ordered replica tiers + `access_policy_ref` + credential requirement) is stored and gossiped/DHT-published. The substrate never holds the user's bytes or credentials; the consumer fetches from the provider under its *own* credential / Verifiable Credential and **verifies the bytes against `content_hash`** (mismatch ⇒ `CONTENT_INTEGRITY_FAILED`, fails closed). This generalises v1.0's `content_kind=external` (which `ContentLocator` subsumes) and is the pattern OpenCLAW-P2P runs in production (tiered object-store → repo → IPFS persistence with IPFS+GitHub content-hash attribution).

**Availability when the origin is offline.** Discoverability says *where* a bundle is; **availability** says whether it can still be fetched when the producing node sleeps. A bundle MAY carry an **`AvailabilityPolicy` (`availability-policy/1`)** ([`09_PROTOCOLS §3H.2`](09_PROTOCOLS.md#3h2-availabilitypolicy--surviving-the-origin-going-dark)): `online_only` (default — fetchable only while the owning node is up), `replicated` (mirrored to ≥ `replication_factor` peers, listed as `ContentLocator.replica_tiers`), or `pinned` (held by a persistent provider — IPFS pin / OCI / object store). When the origin is unreachable, the resolver + `ProviderAdapter` fall back through `replica_tiers` until bytes verify against `content_hash`. This is what lets the deliverables of a persona on a home laptop stay fetchable from a phone off-network *after the laptop sleeps* — the live persona pauses, but `replicated` / `pinned` artefacts do not vanish. The policy never widens access: a replica is still gated by the bundle's `AccessPolicy` (`§4a`, [`09_PROTOCOLS §3G.4`](09_PROTOCOLS.md#3g4-access-gated-discovery--who-can-access-what-enforced-at-the-discovery-layer)).

**Tests:** A-AB28 (ArtifactCard discoverable at `discover`, body refused without `read`), A-AB29 (`ContentLocator` round-trip: publish → discover over P2P → fetch from provider under credential → verify against `content_hash`), A-AB30 (`content_hash` mismatch ⇒ `CONTENT_INTEGRITY_FAILED` fails closed), A-AB31 (replica-tier fallback on primary-provider outage), A-AB32 (`CONTENT_LOCATOR_STALE` on live-reference drift), A-AB33 (`AvailabilityPolicy=replicated`: bundle fetchable from a replica with the origin offline), A-AB34 (replica fetch still enforces `AccessPolicy` — `discover`-only principal refused at `read`). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

**Lineage:** `artifact_card_published`, `artifact_card_revoked`, `content_locator_attached`, `content_locator_stale`, `content_integrity_failed`, `availability_policy_set`, `replica_fallback_served`.

## 11. Bundle forking

Two operations:

### 11.1 Bundle fork

New bundle inherits from parent:

*Three inheritance modes — inherit_all, inherit_snapshot, and inherit_specific — control what carries into the forked bundle.*

**Technical detail:** See [A.17](#appendix-a17).

Fork is the **only** way to edit a **shipped** bundle. The shipped bundle stays locked.

### 11.2 Project fork → bundle inheritance

When a Project forks (v1.0 §04 §17.1), bundles carry along per project's fork policy.

## 12. Co-editing patterns

Three modes depending on artifact + project culture:

*Three co-editing modes — lead-author with reviewers, concurrent co-authors under CRDT, and sequential hand-off — cover the common collaboration patterns.*

**Technical detail:** See [A.18](#appendix-a18).

v1.0 doesn't enforce a mode; bundle records who edited what when. Project culture lives in Project.charter.

## 13. PeerReview integration

v1.0 §04 §11 defines PeerReview as multi-round structured critique. Bundles in `in_review` state have an open PeerReview:

*The peer review flow opens when a bundle enters review, runs through multi-round comment/revision exchanges, and concludes with a verdict that drives the bundle's state transition.*

**Technical detail:** See [A.19](#appendix-a19).

## 14. Cross-environment artifact CRDT

For projects hosted in multiple environments (v1.0 §04 §18, v1.0 §05 §17), artifact CRDT operates **project-wide**:

*When a project spans multiple environments, concurrent edits from personas in different environments merge deterministically, with each environment's ambient stream recording local events and cross-linking remote ones.*

**Technical detail:** See [A.20](#appendix-a20).

Artifact ownership is by the bundle's `owning_env_id` (§4) — for a project bundle, the `project_workspace` env (project IS an env, ADR-0003). The bundle still lives **above any single hosting env** when a project spans multiple environments: `env_A` and `env_B` here are *hosting / co-editing* envs, not owners, and their personas obtain access through the `ArtifactSharingPolicy` (`AccessGrant` with `grantee_kind="env"`) plus `EnvironmentComposition` inheritance (§4a). When a remote persona's edit crosses a `principal_attribution` boundary, the kernel resolves the policy across the composition chain before applying the CRDT op; a `tenant`-tier edit without a `CrossTenancyAgreementRef` is read-demoted with a signed `CROSS_TENANT_VISIBILITY_DEMOTED` event. When `owning_env_id` is `None`, the legacy project-scoped behaviour applies unchanged.

## 15. Cost and performance

*Performance targets for bundle creation, CRDT operations, co-edit propagation, verifier invocation, state transitions, and content reads.*

**Technical detail:** See [A.21](#appendix-a21).

Storage:

*Typical storage footprints for active projects, long-running research projects, and domain-attached corpora.*

**Technical detail:** See [A.22](#appendix-a22).

## 16. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations).

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-ARTIFACTS-1 | Visual artifact rendering requires external domain tools. Personas produce text representations (netlists, structured data); SVG / KiCad / PDF rendering is tool-side. | Low | High | `rendered_view_ref` field allows attaching tool output; `content_ref` (persona-authored) remains authoritative; A-AB9 acceptance test. | v1.0 (substrate); tool availability per-domain. |
| R-ARTIFACTS-2 | CRDT semantics imperfect for structured artifacts. Yjs handles text; semantic-constraint artifacts (schematics, electrical connectivity) need domain-aware merge. | High | Medium | G-set with `ARTIFACT_FIELD_CONFLICT` event for unsafe merges; domain-aware merge plugins per artifact kind; A-AB2 acceptance test. | v1.0 (text + G-set); v1.1 (domain-aware merge plugins). |
| R-ARTIFACTS-3 | Binary artifacts (images, video) cannot be co-edited under CRDT — replaced version-by-version. | Medium | High | Out of v1.0 scope; per-version replacement with co-sign; fork-on-edit. | v1.2+ (binary co-edit out of scope). |
| R-ARTIFACTS-4 | Content store costs grow with project lifetime and bundle versions. | Low | High | Decay policy: `deprecated → cold` after 90 days; operator-tunable retention; content-hash dedup. | v1.0 (decay); v1.1 (operator tuning surface). |
| R-ARTIFACTS-5 | External-reference artifacts lose verifiability. Persona cannot guarantee external URL content matches what was reasoned about. | High | High | External-tool-required policy on claims based on external refs; retrieval-and-verification invocation; lineage records the retrieval timestamp and hash; A-AB11 acceptance test. | v1.0 (verification flow). |
| R-ARTIFACTS-6 | Bundle state transitions can deadlock if a required signatory is unavailable. | Medium | Low | Per-step deadlines; operator override; transition refused → STALLED state surface; A-AB3 acceptance test. | v1.0 (refused + stall). |
| R-ARTIFACTS-7 | Verification evidence becomes decorative if a harness can emit "passed" without replayable tool / panel provenance. | High | Medium | `VerifierInvocationEvidence` is mandatory for lifecycle advancement; missing, stale, malformed, or prose-only evidence fails closed; A-AB16-A-AB20. | v1.0 (evidence envelope); v1.1 (harness conformance tooling). |
| R-ARTIFACTS-8 | `ArtifactSharingPolicy` (§4a) misconfiguration over-exposes a bundle (e.g. an unintended `federation`/`public` tier or an over-broad `AccessGrant`). | High | Medium | Default `outward_tier = project_only`; effective access composes by most-restrictive-wins; a `None` policy never widens; cross-tenant shares require a `CrossTenancyAgreementRef` or demote (`CROSS_TENANT_VISIBILITY_DEMOTED`); A-AB22/A-AB25/A-AB26. Cross-document: also `00_VISION §11`. | v1.1 (conservative defaults). |
| R-ARTIFACTS-9 | Cross-env CRDT (§14) under a partitioned `EnvironmentComposition` link: a child env edits while the composition/policy view is stale. | Medium | Low | Deny-on-uncertain for `rw` during partition; reuse joined-env `CONFLICT_PARKED` (`05_ENVIRONMENT` R-ENV-7) deferral to operator; reads continue against the local policy snapshot. | v1.1 (partition policy). |

## 16a. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-ARTIFACTS-1 | Domain-aware CRDT merge plugins (R-ARTIFACTS-2): what's the plugin contract? Per-artifact-kind merge function, or per-domain merge policy? | Artifact authors | v1.1 plugin contract. |
| OQ-ARTIFACTS-2 | Binary-artifact co-edit (R-ARTIFACTS-3): explicitly out of v1.0 scope, but should we define the fork-on-edit lifecycle to make eventual co-edit non-breaking? | Artifact authors | v1.2 fork-on-edit design. |
| OQ-ARTIFACTS-3 | External-reference verification (R-ARTIFACTS-5): does the substrate cache the verified content, or only the hash? Storage / privacy / freshness trade-offs. | — | v1.1 cache policy. |
| OQ-ARTIFACTS-4 | Bundle state-transition deadlocks (R-ARTIFACTS-6): per-step deadline defaults — by bundle type, by signatory role, by content size? | Artifact authors | v1.1 deadline defaults. |
| OQ-ARTIFACTS-5 | `rendered_view_ref` retention: when the persona-authored content_ref changes, do we keep stale renders, auto-invalidate, or background-refresh? | — | v1.1 render lifecycle. |
| OQ-ARTIFACTS-6 | `owning_env_id` migration (§4): do existing project bundles get `owning_env_id` set eagerly to their project_workspace env, or lazily on first `ArtifactSharingPolicy` attach? (Recommend lazy — stays `None` until first policy attach.) | Artifact authors | v1.1 migration policy. |
| OQ-ARTIFACTS-7 | `AccessGrant` granularity (§4a): per-bundle (v1.1) vs per-artifact-within-bundle. When does per-artifact access become necessary? | Artifact authors | v1.2 per-artifact grants. |

## 17. Acceptance tests

```text
A-AB1   ArtifactBundle created with multi-modal artifacts; contributors
        signed; lifecycle states transition.
A-AB2   CRDT co-editing of text artifact between two personas produces
        deterministic merge; conflicts surface as signed
        ARTIFACT_FIELD_CONFLICT.
A-AB3   Bundle state transitions require configured signatories;
        transitions without sufficient signatures refused.
A-AB4   Shipped bundles locked; edits require explicit fork to new
        bundle.
A-AB5   verifier_recipe invocation against bundle appends
        VerifierInvocationEvidence entries; verdicts feed state transition.
A-AB6   AnswerPackage referencing ArtifactBundle returns primary
        artifact and state.
A-AB7   Backward compat: AnswerPackage with no project/no bundle =
        Standard shape.
A-AB8   Inline artifacts < size limit; larger stored; content_hash
        matches stored content.
A-AB9   Rendered_view_ref optionally produced by domain tool;
        persona-authored content_ref authoritative.
A-AB10  Bundle fork inherits per policy; parent stays locked.
A-AB11  External_ref artifacts: claims about content require
        external-tool calls.
A-AB12  Co_signed_by signatures Ed25519; verifiable independently.
A-AB13  PeerReview process integrated with bundle lifecycle;
        blocking comments must be addressed.
A-AB14  Cross-env CRDT: artifact in project hosted multi-env
        merges project-wide; env streams record events.
A-AB15  Multi-modal media kind support (11 kinds); each with appropriate
        storage + edit semantics.
A-AB16  No applicable verifier recipe OR required verifier stage with
        missing VerifierInvocationEvidence refuses verified/accepted
        transition; signed refusal cites recipe_id/stage_id when present.
A-AB17  VerifierInvocationEvidence with unavailable/timed_out/not_run
        execution surface is recorded but parsed_verdict != pass; bundle
        remains in_review or draft.
A-AB18  Evidence whose input_artifact_hashes do not match current bundle
        versions is stale; transition to verified refuses.
A-AB19  Review/panel direct in_review → accepted allowed only when
        signed review/panel evidence exists AND no DomainContext /
        safety-extension stage remains required.
A-AB20  Free-form rationale or LLM-produced "verified" token without
        tool/panel provenance cannot satisfy parsed_verdict=pass.
A-AB21  Backward compat: an artifact-bundle/1 with owning_env_id=None and
        sharing_policy_ref=None behaves exactly as pre-v1.1 (project-scoped,
        no access checks).
A-AB22  Bundle with owning_env_id set + ArtifactSharingPolicy: a principal
        with no matching AccessGrant is denied read at the retrieval point.
A-AB23  An r-only grantee's CRDT write op is denied (artifact_access_refused);
        an rw grantee's write succeeds.
A-AB24  Intra-composition inheritance: a child env inherits the parent's
        inherit_to_children policy via EnvironmentComposition; a child policy
        may further-restrict but not widen.
A-AB25  Outward tenant-tier share crossing a principal_attribution boundary
        WITHOUT a CrossTenancyAgreementRef is read-demoted and emits
        CROSS_TENANT_VISIBILITY_DEMOTED.
A-AB26  Effective access composes by most-restrictive-wins across
        AccessGrant ∩ outward-tier reachability ∩ inherited composition policy.
A-AB27  Cross-env CRDT (§14): a project hosted in multiple envs resolves the
        sharing policy across the composition chain before applying a remote
        persona's edit; access is enforced per hosting env.
```

## 18. Where to read next

- Project that contains bundles: [`04_PROJECT.md`](04_PROJECT.md)
- DomainContext provides verifier_recipes + tool ecosystem: [`06_DOMAIN.md`](06_DOMAIN.md)
- Knowledge tier (retrievable artefacts + memory): [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)

## Technical Appendix

The appendices below contain the full technical schemas, data structures, diagrams, and specification tables referenced throughout this document. Each appendix is referenced from the section where it applies.

### A.1 Media kind registry entries

<a id="appendix-a1"></a>

```text
TYPICAL ENTRIES (illustrative — not normative)
  text            (MetaRegistry, standardised)
  code            (MetaRegistry, standardised)
  table           (MetaRegistry, standardised)
  structured_data (MetaRegistry, standardised)
  plot            (MetaRegistry, standardised)
  binary          (MetaRegistry, standardised)
  external_ref    (MetaRegistry, standardised)

EMERGENT EXAMPLES (per domain, none hardcoded in substrate)
  schematic       (electronics domain — recognised)
  formal_proof    (mathematics domain — recognised)
  spice_netlist   (electronics domain — recognised)
  kicad_project   (electronics domain — recognised)
  floor_plan      (residential_construction — emergent on first use)
  gantt_schedule  (project-mgmt — emergent on first use)
  ifc_model       (residential_construction — emergent on first use)
  hamiltonian     (quantum-device-design — emergent on first use)
```

### A.2 Artifact schema (artifact/1)

<a id="appendix-a2"></a>

```python
@dataclass
class Artifact:
    schema: str = "artifact/1"
    artifact_id: str                      # ULID
    bundle_id: str
    name: str                             # human-readable: "schematic.kicad_sch"
    
    media_kind: str                       # resolves against KindRegistry.
                                          # media_kinds (06_DOMAIN §7.6);
                                          # never a closed enum. The
                                          # resolved MediaKindEntry supplies
                                          # storage_class, introspection +
                                          # rendering adapters, and the
                                          # verifier hooks this artifact
                                          # may use.
    mime_type: str
    
    content_kind: Literal["inline", "stored", "external"]
    content_ref: str                      # inline | store key | URL
    content_hash: str                     # SHA-256
    size_bytes: int
    
    role_in_bundle: str                   # "primary", "supporting",
                                          # "verification_report",
                                          # "test_plan", etc.
    version: int                          # within this artifact
    parent_version_artifact_id: str | None
    
    contributors: list[ContributorEntry]
    co_signed_by: list[persona_id]
    
    rendered_view_ref: str | None         # optional rendered/visual
    rendered_by_tool: str | None
    rendered_at: datetime | None
    
    state: Literal["draft", "in_review", "verified", "accepted",
                    "shipped", "deprecated"]
    
    created_at: datetime
    last_modified_at: datetime
    signed_by: bytes


@dataclass
class ContributorEntry:
    persona_id: str
    edits_count: int
    last_edit_at: datetime
    role: str                             # "author", "reviewer", "verifier", "merger"
```

### A.3 ArtifactBundle schema (artifact-bundle/1)

<a id="appendix-a3"></a>

```python
@dataclass
class ArtifactBundle:
    schema: str = "artifact-bundle/1"     # additive fields below; version
                                          # retained per 09_PROTOCOLS §7.13
    bundle_id: str
    project_id: str
    owning_env_id: str | None = None      # the environment that OWNS this
                                          # bundle and governs its sharing
                                          # (§4a). For a project bundle this is
                                          # the project_workspace env (project
                                          # IS an env, ADR-0003); None = legacy
                                          # project-scoped behaviour (pre-/2
                                          # semantics preserved).
    sharing_policy_ref: str | None = None # ArtifactSharingPolicy.policy_id
                                          # (artifact-share/1, §4a); None =
                                          # inherit the owning env's default
                                          # policy, else project_only.
    name: str                             # "design_v3", "paper_v7", "refactor_v2"
    description: str
    bundle_kind: str                      # domain-meaningful:
                                          # "smps_design", "math_paper",
                                          # "code_change", "research_report",
                                          # "course_module",
                                          # "policy_document", etc.
    artifacts: list[ArtifactRef]
    primary_artifact_id: str | None
    
    # LIFECYCLE
    state: Literal["draft", "in_review", "verified",
                    "accepted", "shipped", "deprecated"]
    version: int
    parent_bundle_id: str | None
    forked_from_bundle_id: str | None
    
    # AUTHORSHIP
    contributors: list[ContributorEntry]
    co_signed_by: list[persona_id]
    primary_author_persona_id: str | None
    
    # VERIFICATION
    verifier_recipe_id: str | None        # from DomainContext
    verifier_invocations: list[VerifierInvocationEvidence]
    panel_verdicts: list[PanelVerdict]
    structured_feedback: list[StructuredFeedbackRef]
    
    # LINKAGE
    related_open_problems: list[str]
    related_domain_items: dict[str, list[str]]  # v1.0 — keyed by ItemKind
                                                # (06_DOMAIN §7.6); e.g.
                                                # {"conjecture": [...],
                                                #  "design_hypothesis": [...]}
    discharges_obligations: list[str]
    
    # AUDIT
    created_at: datetime
    last_modified_at: datetime
    accepted_at: datetime | None
    shipped_at: datetime | None
    signed_by: bytes
```

### A.3a ArtifactSharingPolicy + AccessGrant schemas

<a id="appendix-a3a"></a>

```python
@dataclass
class ArtifactSharingPolicy:
    schema: str = "artifact-share/1"
    policy_id: str                        # ULID
    owning_env_id: str                    # env that authored / owns the policy
    bundle_scope: Literal["env_default",  # applies to all bundles owned by env
                           "bundle_specific"]
    bundle_id: str | None = None          # set when bundle_scope=bundle_specific

    # ACCESS LEVELS — per principal / role / env / principal-attribution
    access_grants: list[AccessGrant] = field(default_factory=list)

    # INTRA-COMPOSITION SHARING — reuse EnvironmentComposition (05_ENV §2.2a)
    intra_composition_inheritance: Literal[
        "inherit_to_children",            # children in the composition inherit
                                          #  (company → org → team)
        "inherit_to_parent",
        "isolated"] = "inherit_to_children"

    # OUTWARD SHARING — reuse the 5 visibility tiers (06_DOMAIN §6.3; ADR-0030)
    outward_tier: Literal["persona_only", "project_only", "tenant",
                          "federation", "public"] = "project_only"
    cross_tenant_agreement_ref: str | None = None   # CrossTenancyAgreementRef
                                          #  (ADR-0028) REQUIRED before a
                                          #  tenant-tier share crosses a
                                          #  principal_attribution boundary;
                                          #  absent => demote + emit
                                          #  CROSS_TENANT_VISIBILITY_DEMOTED.
                                          #  federation / public are served by
                                          #  the normative discovery layer
                                          #  (09_PROTOCOLS §3G, ADR-0067),
                                          #  access-gated by AccessPolicy.

    version: int = 1
    signed_by: bytes = b""                # env-scope key (09_PROTOCOLS §8)


@dataclass
class AccessGrant:
    schema: str = "access-grant/1"
    grantee_kind: Literal["persona", "role", "env", "principal"]
    grantee_id: str                       # persona_id | role_kind | env_id |
                                          #  principal_attribution_id
    access_level: Literal["r", "rw"] = "r"
```

**Effective access** for a principal P on bundle B is the **intersection** (most-restrictive-wins, exactly as the safety floor composes, [`01_KERNEL.md §2.1`](01_KERNEL.md#21-composition-rule)) of: (a) the `AccessGrant` matching P (or P's role / env / principal-attribution); (b) outward-tier reachability given P's tenancy and any `cross_tenant_agreement_ref`; (c) the inherited policy along the `EnvironmentComposition` chain — a parent `inherit_to_children` policy MAY further-restrict a child but MUST NOT widen a child's own grants (mirroring "child may add stricter rules", [`05_ENVIRONMENT.md §2.2a`](05_ENVIRONMENT.md#22a-environmentcomposition--hierarchical-environment-nesting-v11)); and (d) any source-8 `EnvironmentRule` ([`05_ENVIRONMENT.md §2.2b`](05_ENVIRONMENT.md#22b-environmentrule-env-rule1)) firing at the `output` admission point. A write (`rw`) operation by an `r`-only grantee MUST be denied (`artifact_access_refused`).

### A.4 CRDT classes

<a id="appendix-a4"></a>

```text
text_crdt        (Yjs / Automerge)
  conflict resolution: position-based, deterministic merge
  operations:        insert(at, text), delete(at, length)
  presence:          per-contributor cursor / selection ranges shown
  typical MetaRegistry-seeded kinds: text, code

structured_crdt  (G-set / LWW-map hybrid)
  conflict resolution: G-set for additions; LWW for updates with
                       signed timestamps; explicit conflict on
                       same-field divergent edits
  operations:        add_node, remove_node, update_field
  presence:          per-contributor pending-changes overlay
  typical MetaRegistry-seeded kinds: structured_data, table

version_chain    (no CRDT; replaced version-by-version via
                  parent_version_artifact_id)
  typical MetaRegistry-seeded kinds: binary, plot, external_ref
```

### A.5 Co-edit flow diagram

<a id="appendix-a5"></a>

```text
Persona A proposes edit
    ▼
Kernel receives signed CRDT operation
    ▼
Safety floor checks (proposed text against charter, boundaries, ...)
    ▼
ArtifactSharingPolicy access check (§4a): resolve A's effective access on
  this bundle (grant ∩ tier ∩ inherited composition policy, most-restrictive-
  wins); a write op by an r-only grantee is denied → artifact_access_refused
    ▼
Domain external_tool_requirements check
    ▼
CRDT operation applied; new version stamped
    ▼
Persona B receives notification (via their kernel)
    ▼
B reviews; may accept, propose counter-edit, or open Disagreement
```

### A.6 Conflict resolution rules

<a id="appendix-a6"></a>

```text
NON-CONFLICTING          CRDT merges automatically
                          (text inserts in different positions,
                          additions to a set)

CONFLICTING               Same-field divergent edits → 
  STRUCTURED              ARTIFACT_FIELD_CONFLICT event.
                          Lead persona chooses, OR Disagreement opened.

SEMANTIC CONFLICT         Edits compose successfully but semantically
                          clash. Detected by post-edit semantic-
                          consistency checker (LLM judge);
                          emits ARTIFACT_SEMANTIC_CONFLICT.
```

### A.7 Bundle lifecycle FSM

<a id="appendix-a7"></a>

```text
draft        any contributor may edit; multi-mode work
   ▼
in_review    PeerReview open; expected stable
   ▼
verified     verifier_recipe ran and accepted;
             every required stage has admissible evidence
              (VERIFIER_ACCEPT pathway gate)
   ▼
accepted     co-signed by required signatories
              (PANEL_ACCEPT or MUTUAL_ACCEPT)
   ▼
shipped      delivered to user / merged to main / published / submitted
              LOCKED — further edits require explicit fork
   ▼
deprecated   superseded or project ended; read-only; archived
```

### A.8 Lifecycle event allowed sets

<a id="appendix-a8"></a>

```text
DRAFT
  artifact_added             artifact_edited
  artifact_renamed
  verifier_invoked_exploratory (results recorded, not gating)
  panel_invoked_exploratory
  state_transition: draft → in_review

IN_REVIEW
  peer_review_opened
  peer_review_comment        peer_review_revision_requested
  artifact_edited_under_review (flagged in review)
  state_transition: in_review → draft (revisions)
                              → verified (evidence-complete verifier pass)
                              → accepted (review/panel pass AND no missing
                                          required verifier evidence)

VERIFIED
  verifier_recipe_invoked    verifier_evidence_recorded
  verifier_passed
  state_transition: verified → accepted (panel/co-sign passes)

ACCEPTED
  (typically transient before shipped)

SHIPPED
  LOCKED. Read-only. Subsequent edits require fork to new bundle.

DEPRECATED
  Read-only; archived; preserved for audit.
```

### A.9 Verifier invocation logic

<a id="appendix-a9"></a>

```python
def verify_bundle(bundle, project, domain):
    recipe = domain.find_verifier_recipe(bundle.bundle_kind)
    if not recipe:
        return VerifierResult.no_applicable_recipe()
    
    invocations = []
    for stage in recipe.stages:
        evidence = run_stage_and_capture_evidence(stage, bundle)
        invocations.append(evidence)
        append_lineage("verifier_evidence_recorded", evidence)
        if not evidence_admissible(evidence, stage, bundle):
            return VerifierResult.failed(invocations, reason="inadmissible_evidence")
        if evidence.parsed_verdict != "pass":
            return VerifierResult.failed(invocations)
    
    return VerifierResult.passed(invocations)
```

### A.9a VerifierInvocationEvidence schema

<a id="appendix-a9a"></a>

```python
@dataclass
class VerifierInvocationEvidence:
    schema: str = "verifier-invocation-evidence/1"
    invocation_id: str                       # ULID
    bundle_id: str
    verifier_recipe_id: str
    verifier_recipe_version: int
    stage_id: str
    stage_version: int
    stage_kind: str                          # resolves against
                                             # KindRegistry.verifier_kinds
    execution_surface_kind: str              # resolved capability/tool/panel
                                             # kind; never a domain enum

    # Bind the verdict to the exact artifact bytes observed by the stage.
    input_artifact_hashes: dict[str, str]     # artifact_id -> SHA-256
    input_bundle_hash: str

    # Execution / judgement provenance. Programmatic stages use tool fields;
    # panel/review stages use panel_verdict_ref or peer_review_ref.
    required_tool_id: str | None
    tool_version_ref: str | None
    tool_invocation_ref: str | None
    sandbox_ref: str | None
    command_or_api_fingerprint: str | None
    panel_verdict_ref: str | None
    peer_review_ref: str | None

    started_at: datetime
    completed_at: datetime
    exit_status_kind: str                    # KindRegistry-resolved:
                                             # e.g. success, failed,
                                             # unavailable, timed_out
    raw_output_ref: str | None
    raw_output_hash: str | None
    parsed_verdict: Literal["pass", "fail", "inconclusive", "not_run"]
    failure_kind: str | None                 # KindRegistry-resolved
    rationale_ref: str | None                # optional prose; never sufficient
                                             # by itself for parsed_verdict=pass

    signed_by_tool_or_panel: bytes | None
    signed_by_kernel: bytes
```

**Admissibility predicate.** `evidence_admissible(e, stage, bundle)` returns true only when:

1. `e.schema` is registered and valid.
2. `e.verifier_recipe_id`, `e.verifier_recipe_version`, `e.stage_id`, and
   `e.stage_version` match the active recipe and rotated stage.
3. `e.input_artifact_hashes` match the bundle's current artifact versions.
4. The required execution provenance for the stage's resolved kind is present.
5. `raw_output_hash` matches retrieved output when `raw_output_ref` is present.
6. `parsed_verdict="pass"` is derived from the stage parser, not from free-form rationale.
7. Kernel signature verifies and, when present, tool / panel signatures verify.

Any false predicate yields `parsed_verdict="not_run"` or `fail` for lifecycle purposes and blocks `verified`.

### A.10 AnswerPackage with bundle reference

<a id="appendix-a10"></a>

```python
AnswerPackage(
    status="panel_accepted",
    acceptance_pathway="panel_accept",
    project_id="...",
    artifact_bundle_ref="bundle_01HK...",
    artifact_bundle_state="accepted",
    structured_outcomes=[...],
    project_state_delta=...,
    ...
)
```

### A.11 Bundle composition: smps_design

<a id="appendix-a11"></a>

```yaml
bundle_kind: smps_design
primary_artifact_id: schematic.kicad_sch
artifacts:
  - schematic.kicad_sch         (kicad_project)
  - bom.csv                     (table)
  - sim_report.md               (text)
  - thermal_analysis.md         (text)
  - test_plan.md                (text)
  - efficiency_curve.svg        (plot)
verifier_recipe_id: buck_design_verifier
```

### A.12 Bundle composition: math_paper

<a id="appendix-a12"></a>

```yaml
bundle_kind: math_paper
primary_artifact_id: paper.tex
artifacts:
  - paper.tex                   (text/code)
  - proofs.lean                 (formal_proof)
  - examples.ipynb              (code; Jupyter)
  - related_work.md             (text)
  - slides.tex                  (text/code)
verifier_recipe_id: lean_proof_verifier
```

### A.13 Bundle composition: code_change

<a id="appendix-a13"></a>

```yaml
bundle_kind: code_change
primary_artifact_id: design_doc.md
artifacts:
  - design_doc.md               (text)
  - src/changes/*               (code; many files)
  - tests/*                     (code)
  - migration.sql               (code)
verifier_recipe_id: tests_pass_verifier
```

### A.14 Bundle composition: research_report

<a id="appendix-a14"></a>

```yaml
bundle_kind: research_report
primary_artifact_id: report.md
artifacts:
  - report.md                   (text)
  - data/raw.csv                (structured_data)
  - data/processed.parquet      (structured_data)
  - analysis.ipynb              (code)
  - plots/*.svg                 (plot)
verifier_recipe_id: research_methodology_verifier
```

### A.15 Bundle composition: policy_document

<a id="appendix-a15"></a>

```yaml
bundle_kind: policy_document
primary_artifact_id: policy.md
artifacts:
  - policy.md                   (text)
  - rationale.md                (text)
  - examples_in_scope.md        (text)
  - examples_out_of_scope.md    (text)
verifier_recipe_id: policy_consistency_verifier
```

### A.16 Storage and reference modes

<a id="appendix-a16"></a>

```text
content_kind=inline    Content stored in Artifact record.
                       Limit: 100 KB code, 32 KB text.
                       Above limit → stored.

content_kind=stored    Content in kernel content store
                       (Git-backed, S3-backed, IPFS-style; operator
                       choice). content_ref is store key.
                       Content-addressed (hash-named); hash in
                       Artifact.content_hash matches.

content_kind=external  References external system (URL, S3 bucket,
                       issue tracker, paper, etc.).
                       Kernel doesn't own; integrity by reference.
                       Persona claims about content require
                       external-tool invocation.
```

### A.17 Bundle fork inheritance modes

<a id="appendix-a17"></a>

```text
inherit_all          full artifact history copied; contributors carry
inherit_snapshot     only current artifact versions; no history
inherit_specific     specified artifacts only
```

### A.18 Co-editing patterns

<a id="appendix-a18"></a>

```text
LEAD-AUTHOR + REVIEWERS
  One persona primary author; others review via PeerReview process.
  Common for: math papers, design documents.

CONCURRENT CO-AUTHORS
  Multiple personas edit simultaneously under CRDT.
  Presence indicators show who's editing what.
  Common for: codebase changes, exploratory research notebooks.

SEQUENTIAL HAND-OFF
  Persona A produces draft → Persona B edits → Persona C reviews → ...
  Common for: engineering deliverables (Volt drafts BOM; Sage validates
              parts; Forge runs DRC; Volt finalises).
```

### A.19 PeerReview integration flow

<a id="appendix-a19"></a>

```text
Bundle transitions to in_review
   ▼
PeerReview opened
   - authors set; reviewers identified; chair (if structured)
   ▼
Multi-round exchange
   - reviewers post ReviewComment
   - reviewers issue RevisionRequest
   - authors AuthorResponse + revise (CRDT edits)
   - blocking comments must be addressed before accept
   ▼
Final verdict
   - accept_as_is
   - accept_with_revisions
   - reject
   ▼
Bundle transitions to verified or accepted (depending on final_verdict)
```

### A.20 Cross-environment CRDT scenario

<a id="appendix-a20"></a>

```text
PROJECT P hosted in env_A and env_B
ArtifactBundle "design_v3" lives in project P.
  
Persona X in env_A edits artifact.
Persona Y in env_B edits same artifact concurrently.
  
CRDT merges deterministically.
  
Ambient stream events:
  - env_A.ambient_stream records "X edited"
  - env_B.ambient_stream records "Y edited"
  - cross_env_event_link emitted in env_A linking to Y's edit
  - cross_env_event_link in env_B linking to X's edit
```

### A.21 Performance targets

<a id="appendix-a21"></a>

```text
ArtifactBundle creation                ≤ 50 ms p95
CRDT operation apply                    ≤ 20 ms p95
Co-edit propagation (intra-kernel)      ≤ 100 ms p95
Co-edit propagation (federated)         ≤ 1 s p95 (network-dependent)
Verifier invocation against bundle      per verifier_recipe stages
                                         (no overhead vs standard cascade)
Bundle state transition                  ≤ 100 ms (signing + lineage)
Stored content read (warm)              ≤ 50 ms p95
Stored content read (cold)              ≤ 500 ms p95
```

### A.22 Storage footprints

<a id="appendix-a22"></a>

```text
Active project artifact storage         1-500 MB per project typical
Long-running research project           1-10 GB per project
Domain-attached corpora                  shared via knowledge store
```
