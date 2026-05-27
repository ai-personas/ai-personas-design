---
title: PersonaOS v1.0 — Artifacts
status: Stable
---

# 07 — Artifacts

> **Reader guide.** Artifacts are the things AI Personas produce — documents, code, schematics, datasets, formal proofs. In this document, you'll learn how artifacts are structured, versioned, co-edited by multiple personas, and verified before delivery. The key design principle: artifact types are NOT hardcoded — new types emerge as personas encounter new kinds of work. **Prerequisites:** `06_DOMAIN.md` (KindRegistry), `01_KERNEL.md` (signing). **Key terms:** *ArtifactBundle* = a multi-file deliverable (like a design package); *media_kind* = the type of an artifact (open, not a fixed list); *CRDT* = a method for merging concurrent edits automatically.

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). This document specifies the Artifact entity (open media-kind set resolved via KindRegistry), ArtifactBundle, CRDT co-editing (Yjs + G-set), the lifecycle FSM (draft → review → verified → accepted → shipped), verifier_recipe invocation, and co-signing.

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. Fully normative; RFC 2119 keywords carry normative force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174).

**In scope.** The Artifact entity with its open media-kind set (resolved via the KindRegistry — physical paper, schematic, BOM, code module, proof, netlist, sim report, audio, video, dataset, plus any emergent kind), the ArtifactBundle aggregation, CRDT co-editing semantics (Yjs operations + G-set for append-only references), the artifact lifecycle FSM (draft → review → verified → accepted → shipped), `verifier_recipe` declaration and invocation, and the co-signing protocol that binds artifact verdicts to lineage.

**Out of scope.** Project item entities such as OpenProblem, Milestone, Conjecture, PeerReview (see [`04_PROJECT.md`](04_PROJECT.md)); the kernel-side verifier cascade, anti-Goodhart panel, and signing primitives (see [`01_KERNEL.md §2`](01_KERNEL.md#2-the-safety-floor--8-sources--1-advisory) and [`01_KERNEL.md §4`](01_KERNEL.md#4-signing-infrastructure--3-custody-tiers--key-hierarchy)); the schema-registry entries for artifact / bundle / verifier_recipe (see [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry)).

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

Each domain defines a verification recipe -- a sequence of automated checks tailored to the kind of work. For code, that means running tests. For electronics, checking electrical rules. For math, running the proof checker. Stages run in order; if any fails, the bundle cannot advance.

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

VerifierInvocations are appended to bundle's `verifier_invocations` and to ProjectLineage. Rotation per v1.0 §08 applies.

**Tests:** A-AB5 (verifier_recipe invocation appends VerifierInvocation entries; verdicts feed state transition), A-AB6 (AnswerPackage referencing bundle returns primary artifact + state). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 8. AnswerPackage referencing bundles

v1.0 AnswerPackage (v1.0 §03 §5) carries `artifact_bundle_ref` and `artifact_bundle_state`:

*The AnswerPackage includes a reference to the artifact bundle and its current lifecycle state alongside the acceptance pathway and structured outcomes.*

**Technical detail:** See [A.10](#appendix-a10).

An AnswerPackage with `artifact_bundle_ref=None` is backwards-compatible.

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

Artifact lives **above** any single env; project-scoped.

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

## 16a. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-ARTIFACTS-1 | Domain-aware CRDT merge plugins (R-ARTIFACTS-2): what's the plugin contract? Per-artifact-kind merge function, or per-domain merge policy? | Artifact authors | v1.1 plugin contract. |
| OQ-ARTIFACTS-2 | Binary-artifact co-edit (R-ARTIFACTS-3): explicitly out of v1.0 scope, but should we define the fork-on-edit lifecycle to make eventual co-edit non-breaking? | Artifact authors | v1.2 fork-on-edit design. |
| OQ-ARTIFACTS-3 | External-reference verification (R-ARTIFACTS-5): does the substrate cache the verified content, or only the hash? Storage / privacy / freshness trade-offs. | — | v1.1 cache policy. |
| OQ-ARTIFACTS-4 | Bundle state-transition deadlocks (R-ARTIFACTS-6): per-step deadline defaults — by bundle type, by signatory role, by content size? | Artifact authors | v1.1 deadline defaults. |
| OQ-ARTIFACTS-5 | `rendered_view_ref` retention: when the persona-authored content_ref changes, do we keep stale renders, auto-invalidate, or background-refresh? | — | v1.1 render lifecycle. |

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
        VerifierInvocation entries; verdicts feed state transition.
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
    schema: str = "artifact-bundle/1"
    bundle_id: str
    project_id: str
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
    verifier_invocations: list[VerifierInvocation]
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
verified     verifier_recipe ran and accepted
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
                              → verified | accepted (review passes)

VERIFIED
  verifier_recipe_invoked    verifier_passed
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
        result = run_stage(stage, bundle)
        invocations.append(VerifierInvocation(stage_id, result, ts, signed))
        if not result.passed:
            return VerifierResult.failed(invocations)
    
    return VerifierResult.passed(invocations)
```

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
