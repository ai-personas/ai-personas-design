---
title: PersonaOS v1.0 — Architectural Decision Records
status: Living
---

# 14 — Architectural Decision Records

> **Reader guide.** This document records *why* the design is the way it is — the trade-offs considered, the alternatives rejected, and the forces that shaped each decision. Each entry follows a standard format: Context → Decision → Consequences → Alternatives. **No prerequisites** — each decision record is self-contained. Start with ADR-0001 (why the kernel owns identity) and ADR-0006 (what is hardcoded vs. what emerges) for the foundational decisions.

## 0. About this catalog

This document is the v1.0 **Architectural Decision Record** (ADR) catalog. It records the load-bearing design decisions that produced the v1.0 substrate, in standard ADR form (Michael Nygard's template, as adopted by [Arc42 §9](https://docs.arc42.org/section-9/) and [IEEE 1016](https://standards.ieee.org/ieee/1016/4502/)). Each ADR names a single decision, the forces that shaped it, the option taken, the consequences (positive and negative), and the alternatives that were considered and rejected.

This catalog is **informative**, not normative. The decisions it records are realised as normative invariants, commitments, schemas, and mechanisms in `00_VISION.md` … `13_DESIGN_VALIDATION.md`. When this catalog and a normative document disagree, the normative document is authoritative and the ADR is a documentation defect to be corrected.

**Genre.** This document follows the same shape as [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md): an append-only Living catalog whose entries accrete without supersession of the document itself. Per [`SPEC_CONVENTIONS.md §3`](SPEC_CONVENTIONS.md#3-section-structure), Living catalogs are exempt from the §3.1 bookend requirements; their conformance is judged against the inherent shape of their genre.

**ADR template.** Each entry uses the following structure:

```
### ADR-NNNN — <Decision title>

**Status:** Accepted | Superseded by ADR-MMMM | Proposed | Deprecated.
**Date:** <ISO 8601>.
**Origin:** <version of first realisation, e.g. v1.0>.
**Related:** <invariants, commitments, sections, prior ADRs>.

**Context.** What forces, constraints, and prior state shaped the choice.
**Decision.** The position taken (one paragraph; the load-bearing claim).
**Consequences.** Positive (+) and negative (−) outcomes.
**Alternatives considered.** What else was on the table; why each was rejected.
```

**ID allocation.** ADR IDs are zero-padded four-digit integers (`ADR-0001` … `ADR-9999`). IDs are allocated monotonically; a superseded ADR retains its ID. New ADRs append to the relevant topic section; superseding ADRs append at the end of their section and cite the superseded ID in **Status**.

**Status taxonomy.**

| Status | Meaning |
|---|---|
| Accepted | The decision is in effect; the substrate realises it. |
| Superseded by ADR-MMMM | A later ADR replaces this one; consult the successor. |
| Proposed | Under review; not yet realised in the substrate. |
| Deprecated | The decision is being phased out without a direct successor. |

**Scope.** This catalog covers 22 foundational decisions made across the design history through v1.0, plus 3 v1.0.7 ADRs (multi-principal attribution, derivation-provenance edges, visibility-tier vocabulary unification) sourced from SCENARIO 06, plus 3 v1.0.8 ADRs (lead handoff + obligation reassignment, lifecycle event enumeration + RetiredStatePersistencePolicy + PersonaConsultation, PlannedDeparture) sourced from SCENARIO 07, plus 3 v1.0.9 ADRs (user-side MPA primitives, distress detection routing as substrate-shape, relationship review checkpoints + operator-blind mode + companion-pathway routing) sourced from SCENARIO 08, plus 2 v1.0.10 ADRs (learner state + competency attestation + curriculum primitives Group A; hazardous-skill teaching gate Group B) sourced from SCENARIO 09 with 5 deferred residuals reserved+ as ADR-0039..0043 slots, plus 1 v1.0.11 ADR (MidProjectForkComposition unified envelope for fork-vs-project-side composition) sourced from SCENARIO 10, plus 1 v1.0.13 ADR (self-organizing coordination — personas propose coordination shapes, not just kinds) sourced from the cumulative gap pattern across SCENARIOs 06-12. Future decisions made under v1.1+ append with monotonically-allocated IDs.

---

## 0a. Plain-language guide

This is the project's institutional memory — every major design decision, the reasoning behind it, and the alternatives that were considered, recorded so anyone can understand not just what the system does, but why it was built this way.

**What an ADR is.** ADR stands for "Architecture Decision Record." Each entry captures one significant decision using a standard four-part structure. "Context" explains the problem or tension that forced a choice. "Decision" states what was chosen and why. "Consequences" lists both the benefits and the costs of that choice — the team is honest about trade-offs. "Alternatives considered" lists what else was on the table and why each alternative was rejected. This last part is especially valuable: it saves future readers from re-proposing ideas that were already evaluated and found wanting.

**Why alternatives matter.** Listing rejected options tells you the boundaries of the design space that was explored. If you are wondering "why not just do X instead?", the alternatives section likely already answers that question.

**How the catalog is organised.** Decisions are grouped by topic area: identity and signing, substrate philosophy, the persona model, task handling, domain emergence, memory and knowledge, protocols, multi-principal collaboration, persona retirement, user protections, teaching, and project composition. Each ADR has a four-digit ID (ADR-0001 through ADR-0051 as of this version) allocated in order. When a later decision replaces an earlier one, the old entry stays with a note pointing to its successor — nothing is deleted.

**How to use this document.** If you want to understand a specific design choice, find the relevant ADR by topic section or ID. If you want the foundational decisions that shaped everything else, start with ADR-0001 (why the kernel owns identity) and ADR-0006 (what is hardcoded versus what emerges through use). This document is informative, not normative — the actual rules live in the specification documents it references.

## 1. Identity, signing, lineage

### ADR-0001 — Body / Soul separation: kernel owns identity

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0.
**Related:** [`J1`](00_VISION.md#3-invariants-j1j9), [`J7`](00_VISION.md#3-invariants-j1j9), [`INV-1`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10), [`02_PERSONA.md §3`](02_PERSONA.md#3-soulmd--canonical-identity-file), [`01_KERNEL.md §1`](01_KERNEL.md#1-what-the-kernel-is).

**Context.** A persona's identity (charter, voice, OCEAN/VAD disposition, primary cognitive disposition) must survive across LLM provider changes, framework migrations, body swaps, and the lifetime of the persona — often years longer than any single LLM weight checkpoint. Letting the body (the runtime executing the persona) own identity ties persona persistence to a single provider and conflates two separable concerns: *what the persona is* and *what executes the persona right now*.

**Decision.** The kernel is the sole writer of identity. `SOUL.md` (frozen identity blocks) and `soul.state.json` (kernel-mediated evolving blocks) are kernel-signed; no body process may write either. Bodies (Claude Code, OpenAI Agents SDK, LangGraph, CrewAI, MAF, Pydantic-AI, DSPy, smolagents, Semantic Kernel) call the kernel for any identity-touching mutation; the kernel validates and signs.

**Consequences.**
- (+) Body interchangeability ([`J7`](00_VISION.md#3-invariants-j1j9)). The same Soul produces equivalence-class outputs across all supported bodies.
- (+) Audit trail is owned by one writer; cross-body lineage stays coherent.
- (+) Persona evolution (skills, K-lines, tactics, GEPA-tuned meta-prompts) lives in kernel-held artefacts that outlive any specific LLM weight checkpoint.
- (−) Every body must implement the kernel call protocol; framework adapters carry non-trivial integration cost.
- (−) The kernel becomes a hot-path dependency for any persona-mutating action — performance budget per call must stay tight.

**Alternatives considered.**
- *Body-owned identity (one runtime per persona).* Rejected: ties persona persistence to a single provider; loses lineage on body swap.
- *Distributed identity (CRDT over Soul fields).* Rejected: re-introduces forking semantics and conflict resolution into a domain where the goal is *single signed truth*. CRDT is reserved for artefact co-editing (ADR-0024 in v1.1 backlog), where forks are part of the work.

---

### ADR-0002 — Three lineage scopes: task, environment, domain

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0 (consolidated from prior versions).
**Related:** [`J2`](00_VISION.md#3-invariants-j1j9), [`J9`](00_VISION.md#3-invariants-j1j9), [`C1`](00_VISION.md#3-invariants-j1j9), [`INV-2`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10), [`01_KERNEL.md §3`](01_KERNEL.md#3-lineage--three-scopes).

**Context.** A persona's actions span multiple time-scales and ownership boundaries: a task is short-lived and topical, an environment is long-lived and social, a domain is cross-environment and cumulative. Earlier versions started with a single per-task `LineageGraph`, then added a `ProjectLineage`, then an `EnvironmentLineage`, then a `DomainLineage`. Four parallel append-only logs produced cross-reference sprawl and unclear ownership for events that touched two scopes.

**Decision.** Three lineage scopes total: the per-task `LineageGraph` (J2), the per-environment `EnvironmentLineage` (J9), and the per-domain `DomainLineage` (C1). `ProjectLineage` is retired as a physical scope and reframed as a documentation filter over `EnvironmentLineage` events on `project_workspace`-typed envs (see ADR-0003 J8 retirement). Each event is signed in exactly one scope and may carry cross-scope pointers but never duplicates.

**Consequences.**
- (+) Clear ownership: each event has exactly one scope responsible for its append-only persistence.
- (+) Replay is per-scope and composable; cross-scope reconstruction follows pointers.
- (+) Cross-references in prior prose remain valid without data migration (ProjectLineage records re-classify as EnvironmentLineage filters).
- (−) Implementers must decide scope at event creation; ambiguous events (e.g., a milestone reached during a task) require an explicit rule (recorded in [`04_PROJECT.md §15`](04_PROJECT.md#15-projectlineage-event-types)).
- (−) Auditors querying "everything about this persona" must federate across all three scopes.

**Alternatives considered.**
- *Single global lineage.* Rejected: loses scope separation; auditing a single env means filtering a global stream.
- *Four scopes (keeping ProjectLineage).* Rejected: ProjectLineage and EnvironmentLineage events were 80% identical on project_workspace envs; collapsing eliminated the redundancy without losing the project semantic (preserved as a filter tag).
- *Per-persona lineage.* Rejected: a persona acts across environments and domains; per-persona logs would tangle scopes and hide environment-wide events from non-actor personas.

---

### ADR-0003 — Project is an environment-type (J8 retirement)

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0 (refactor of project layer).
**Related:** [`J8`](00_VISION.md#3-invariants-j1j9) (retired), [`J9`](00_VISION.md#3-invariants-j1j9), [`04_PROJECT.md §0`](04_PROJECT.md#0-status--scope), [`05_ENVIRONMENT.md §1.1`](05_ENVIRONMENT.md#11-project-is-an-environment-type), ADR-0002.

**Context.** Earlier versions introduced `Project` as a top-level entity peer to `EnvironmentInstance` and added `J8` (project lineage append-only), then made environments persistent with their own lineage (J9). Over time the two entities had 70% overlap in fields (membership, lineage, lifecycle, items) and required parallel mechanisms for the same concerns.

**Decision.** v1.0 collapses `Project` into a typed `EnvironmentInstance` whose `type = project_workspace`. The rich item catalogue (`OpenProblem`, `Milestone`, `Conjecture`, `Obligation`, `Disagreement`, `PeerReview`, `ExternalAgent`, `PhysicalAsset`) attaches to the env. J8 retires; its semantic is absorbed into J9. The "project_workspace" type carries the project-specific item kinds via the KindRegistry pattern (ADR-0005).

**Consequences.**
- (+) One entity, one lifecycle FSM, one membership model, one lineage shape.
- (+) `Project` and `Environment` interfaces collapse; framework adapters implement one binding, not two.
- (+) The "project as long-lived workspace" mental model is preserved by the env-type label.
- (−) Documentation transition cost: prior cross-references to "Project" had to be reframed as "project_workspace env" or "owning env" across the corpus (completed in v1.0.8).
- (−) Implementers reading prior prose must mentally translate `ProjectLineage` → `EnvironmentLineage(project_workspace)`. Glossary entries pin both forms.

**Alternatives considered.**
- *Keep Project as a peer entity.* Rejected: 70% field overlap; doubled lifecycle and membership logic.
- *Make EnvironmentInstance a subtype of Project.* Rejected: most environments (solo, pair, debate, companion) are not projects; the inheritance arrow points the wrong way.

---

### ADR-0004 — Three-tier key custody with master + scope keys

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0 (custody) + v1.0 (scope-key hierarchy).
**Related:** [`01_KERNEL.md §4`](01_KERNEL.md#4-signing-infrastructure--3-custody-tiers--key-hierarchy), [`09_PROTOCOLS.md §8`](09_PROTOCOLS.md#8-key-custody-hierarchy).

**Context.** A v1.0 deployment signs across personas, projects, environments, domains, and federations. Putting every signature under one master key creates a catastrophic-blast-radius single point of failure. Putting every signature under per-entity keys with no anchor leaves no recoverable trust root after a single key compromise.

**Decision.** Three custody tiers (laptop / KMS / HSM) per [`01_KERNEL.md §4`](01_KERNEL.md#4-signing-infrastructure--3-custody-tiers--key-hierarchy), with a master key per tier and scoped sub-keys for persona, domain, project, env, and federation roles. Master rotates on a tier-specific schedule (laptop monthly, KMS quarterly, HSM annually). Scope keys are issued under the active master, rotate independently, and may be revoked individually without rotating the master.

**Consequences.**
- (+) Blast radius is bounded to one scope per compromised key.
- (+) Rotation cadence matches operational risk per tier.
- (+) Federation can recognise peer kernels by master-key public anchor without exposing every scope key.
- (−) Key-management surface is larger; operators must track rotation schedules per scope.
- (−) Cross-scope queries (verify a federated artefact signed under a peer kernel's domain key) require fetching the peer's key chain at verification time.

**Alternatives considered.**
- *Single master key.* Rejected: blast radius too large; one key compromise rotates every signed artefact in the deployment.
- *Per-event ephemeral keys.* Rejected: defeats long-term verifiability; archived events would require key recovery to re-verify.
- *Two tiers (laptop + HSM).* Rejected: leaves a gap for cloud-deployments where HSM is unavailable but laptop-grade custody is insufficient — KMS occupies that middle.

---

## 2. Substrate philosophy

### ADR-0005 — Open media-kind set via KindRegistry (commitment C4)

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0 (initial) → v1.0 (substrate-wide application).
**Related:** [`C4`](00_VISION.md#3-invariants-j1j9), [`07_ARTIFACTS.md §1`](07_ARTIFACTS.md#1-what-an-artifact-is), [`06_DOMAIN.md §7.5`](06_DOMAIN.md#75-emergent-kind-proposals-v10--substrate-domain-agnostic), ADR-0006.

**Context.** A closed `Literal[...]` enum of artefact media kinds, source kinds, verifier kinds, capability kinds, contribution kinds, or fact kinds — anywhere in the substrate — pre-decides which domains the substrate can model. PersonaOS targets "cognitive work of any kind"; encoding "scientific paper, code module, sketch" as a closed enum forecloses neuro-modeling artefacts, formal-proof bundles, music score sketches, and an unknown long tail of emergent kinds.

**Decision.** The substrate carries no domain-shaped closed enums. Every domain-shaped category — media kind, source kind, verifier kind, capability kind, contribution kind, fact kind, bundle kind — is an emergent unit proposed by personas, signed into a per-domain `KindRegistry`, and promoted through the same 4-stage gates as `DomainContext`. Substrate code looks kinds up by name; it never branches on a fixed set. A `MetaRegistry` seeds 7 common kinds at substrate boot; all other kinds emerge through use.

**Consequences.**
- (+) New domains do not require substrate edits — emergence handles the long tail.
- (+) The C4 commitment ("substrate is domain-agnostic") is enforceable: a closed enum anywhere in substrate code is a conformance defect detectable by automated check.
- (+) Cross-domain transfer of kinds is enabled by promotion to STANDARDISED in the MetaRegistry.
- (−) Performance: kind lookup is dictionary-based, not jump-table; substrate must amortise the lookup.
- (−) Static analysis is weaker — type-checkers cannot enumerate all admissible kinds at compile time.
- (−) New-kind proposals are an attack surface (a malicious persona could spam the registry); promotion gates and signed proposals bound the risk.

**Alternatives considered.**
- *Closed enum with a "custom" escape hatch.* Rejected: the escape hatch becomes a second-class code path; the closed list crystallises early-domain assumptions.
- *Per-domain registries with no cross-domain promotion.* Rejected: loses cross-domain transfer of useful kinds (e.g., `formal_proof` shared across maths and verification).
- *Type-system-driven open set (e.g., Python `Protocol`).* Rejected: requires substrate-level branching on whether a kind satisfies the protocol; doesn't compose with signed lineage.

---

### ADR-0006 — Hardcode the substrate; emerge everything else

**Status:** Accepted. **Partially superseded by ADR-0045 for coordination scope.**
**Date:** 2026-05-22 (original); 2026-05-26 (supersession note).
**Origin:** Pre-v1.0 (kernel invariants, extended to domain).
**Related:** [`00_VISION.md §9`](00_VISION.md#9-core-design-rules) (rules 1-2), [`C4`](00_VISION.md#3-invariants-j1j9), ADR-0005, **ADR-0045** (self-organizing coordination).

**Context.** A system that hardcodes too little has no load-bearing guarantees; a system that hardcodes too much can only model what its designers anticipated. Prior versions explored both extremes (early versions hardcoded everything; later versions progressively softened domain claims). v1.0 needs an explicit split.

**Decision.** The substrate hardcodes exactly the load-bearing claims: kernel invariants (J1-J9 + INV-1…10), routing modes, the eight acceptance pathways, lifecycle FSM shapes, the three lineage scopes, signing infrastructure, the ten task classes. Everything else — domain shapes, media kinds, tools, verifier recipes, contribution kinds, fact kinds — emerges via the KindRegistry promotion lifecycle. The split is the conformance line: substrate code carries no domain-shaped Literal[]; emergence code carries no signing or lineage shape changes.

**v1.1 supersession note (ADR-0045).** The v1.0.x "hardcode" scope included coordination primitives (acceptance pathways, lifecycle FSMs, coordination ceremonies). ADR-0045 (accepted 2026-05-25) moves coordination from hardcoded to emergent: personas propose coordination shapes within their environments using five meta-mechanisms (EntityGroup, BatchOperation, StagedSequence, StreamPolicy, DerivedMetric). What remains hardcoded: kernel invariants (J1-J9, INV-1..10), safety floor (8 sources), signing infrastructure, lineage model, the five meta-mechanisms themselves. What becomes emergent: coordination shapes, acceptance pathway compositions, lifecycle FSM details. See [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md).

**Consequences.**
- (+) The minimal substrate is small enough to audit, formalise, and prove correct against the invariants.
- (+) Emergence absorbs the long tail without re-baking the substrate.
- (+) Composability: new domains attach by adding registry entries, not by modifying the kernel.
- (−) The split must be enforced by review and tooling; a closed enum slipping into substrate is a C4 violation (detected automatically by [`A-C4`](11_ACCEPTANCE_TESTS.md)).
- (−) Implementers learning v1.0 must internalise "what is hardcoded vs what emerges" early; getting the line wrong yields either rigidity (hardcoded too much) or unsignable claims (emerged what should be hardcoded).

**Alternatives considered.**
- *Hardcode nothing (pure emergent).* Rejected: no load-bearing invariants → no auditability.
- *Hardcode everything (pure designed).* Rejected: limits substrate to anticipated domains; conflicts with J5 (open capability).

---

### ADR-0007 — Schema field of form `<name>/<integer>`

**Status:** Accepted (supersedes earlier `schema_version: int` convention from prior versions).
**Date:** 2026-05-22.
**Origin:** v1.0.5.
**Related:** [`INV-10`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10), [`SPEC_CONVENTIONS.md §4`](SPEC_CONVENTIONS.md#4-schemas), [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry).

**Context.** Prior-version schemas declared `schema_version: int = 1`, with the schema name implicit from the surrounding class name. Wire-format consumers reading a serialised event had to know the producing class to resolve the schema; the same integer carried different semantics across different classes. A self-describing wire format requires the schema name to travel with the integer.

**Decision.** Every schema declares a single `schema` field whose value is a string of the form `<name>/<integer>` (e.g., `schema: str = "soul-state/5"`, `"schema": "domain-context/2"`). The field name is `schema` (not `schema_version`); the value carries both registry name and integer version. The kernel MUST refuse any message whose `schema` value is not present in the registry ([`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry)).

**Consequences.**
- (+) Wire format is self-describing; events can be routed by schema name without class introspection.
- (+) The registry table has one canonical key per schema (`<name>/<integer>`); look-up is O(1).
- (+) Version bumps stay localised: `domain-context/2` and `domain-context/3` coexist in the registry during migration.
- (−) Migration cost: every prior-version schema declaration needed updating. (Completed; see [`README.md` §v1.0.5 changelog](README.md).)
- (−) Two declaration forms (Python `Form A` default-valued vs `Form B` Literal annotation) coexist; authors must pick one consistently per schema ([`SPEC_CONVENTIONS.md §4.2`](SPEC_CONVENTIONS.md#42-python-dataclass-schema-field-forms)).

**Alternatives considered.**
- *Keep `schema_version: int` with class name implicit.* Rejected: wire format is not self-describing.
- *Tuple field `(name: str, version: int)`.* Rejected: JSON Schema and TypeScript express tuples awkwardly; string form is universally cheap.
- *URI-style `schema: "https://personaos.org/schemas/domain-context/v2"`.* Rejected: ties wire format to a specific URL host; the registry already provides the dereference layer.

---

### ADR-0008 — Provider-neutral kernel; bodies are replaceable

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0 (Body/Soul) → v1.0 (codified).
**Related:** [`J7`](00_VISION.md#3-invariants-j1j9), [`02_PERSONA.md §3.5`](02_PERSONA.md#35-body-model--native-vs-proxy-binding-body-binding1), [`09_PROTOCOLS.md §6`](09_PROTOCOLS.md#6-the-twelve-framework-adapters), Goal 2.1.8.

**Context.** Production deployments span LLM providers (Anthropic, OpenAI, open-weight) and frameworks (Claude Code, OpenAI Agents SDK, LangGraph, CrewAI, MAF, Pydantic-AI, DSPy, smolagents, Semantic Kernel). A specification that depends on any one provider's proprietary feature (e.g., specific cache-control headers, named tools, structured-output formats) cannot survive a provider migration without rewriting the substrate.

**Decision.** No normative claim in v1.0 may depend on a specific LLM provider, model family, or proprietary feature. Bodies bind either *natively* (in-process LLM call) or as *proxies* (A2A remote, MCP-server-with-LLM, opaque third-party). Native bindings cover 9+ adapters; proxy bindings cap trust at `body_attestation` level. The kernel signs at the binding boundary; provider-specific optimisations (e.g., Anthropic cache_control) sit in adapter shims.

**Consequences.**
- (+) Body swap (Claude → GPT → open-weight) preserves persona identity, lineage, evolution.
- (+) New providers integrate by writing an adapter, not by editing the kernel.
- (+) Federation across kernels running different providers becomes mechanically possible (A2A).
- (−) Provider-specific optimisations live in shims, not the substrate; some performance left on the table.
- (−) Adapter conformance must be tested per binding (12 adapter conformance suites; see [`11_ACCEPTANCE_TESTS.md` §J7](11_ACCEPTANCE_TESTS.md)).

**Alternatives considered.**
- *Anchor on one provider (e.g., Anthropic-only).* Rejected: vendor lock-in is the load-bearing risk this design rules out.
- *Lowest-common-denominator API surface.* Rejected: would lose provider-specific gains (e.g., cache_control savings) entirely; the adapter-shim pattern lets each adapter expose its own gains without re-baking the substrate.

---

## 3. Persona model

### ADR-0009 — Seven persona layers, 14 cognitive modes

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0.
**Related:** [`02_PERSONA.md §3`](02_PERSONA.md#3-soulmd--canonical-identity-file), [`02_PERSONA.md §4`](02_PERSONA.md#4-the-14-cognitive-modes).

**Context.** A "persona" can be modelled as a single LLM prompt, a multi-prompt program, a finite-state machine, or a layered cognitive architecture. Earlier versions used a single charter + role tuple; subsequent iterations explored whether human-shaped behaviour (consistency under stress, voice, mood, relationships) needed a richer model. Stanford's Generative Agents (Park et al. 2023), Anthropic's Persona Vectors work, and SOTOPIA's goals/secrets/relationships benchmark all pointed to a multi-layer model.

**Decision.** A persona has seven layers — *identity, capability, experience, relationships, mood, goals, voice* — and 14 cognitive modes (FOCUS, FLOW, REFLECT, EXPLORE, COLLABORATE, NEGOTIATE, MENTOR, LISTEN, WITNESS, REST, HEART, GRIEVE, CELEBRATE, RECONCILE; see [`02_PERSONA.md §4`](02_PERSONA.md#4-the-14-cognitive-modes)). Identity is kernel-signed and frozen post-seed; capability/experience/relationships/mood/goals/voice evolve through kernel-mediated mutation. Mode is selected per-task with HEART alternation governing relational vs convergent work.

**Consequences.**
- (+) Behaviour stays coherent under stress (mood and fatigue degrade explicitly, not as drift).
- (+) The model maps to existing benchmarks (SOTOPIA for relationships, OCEAN/VAD for disposition).
- (+) Authors can express "what this persona is" in `SOUL.md` with the seven layers as scaffolding.
- (−) Seven layers and 14 modes are a non-trivial model surface for authors to learn.
- (−) Mode-aware verifier panels (anti-Goodhart) must understand which mode produced an artefact.

**Alternatives considered.**
- *Single charter only.* Rejected (early version): produced personas that drifted under stress and lost voice across long tasks.
- *Free-form mode (LLM-decided).* Rejected: makes verifier-mode alignment unpredictable.
- *Five-factor (OCEAN) only.* Rejected: OCEAN is necessary but insufficient — does not capture skill, relationships, or mood. OCEAN is one component of the *identity* layer.

---

### ADR-0010 — SOUL.md (markdown frontmatter) + soul.state.json (JSON sidecar)

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0.
**Related:** [`02_PERSONA.md §3`](02_PERSONA.md#3-soulmd--canonical-identity-file), [`02_PERSONA.md §3.1`](02_PERSONA.md#31-the-sidecar--soulstatejson-schema-soul-state5), ADR-0001.

**Context.** A persona's identity must be human-authorable (a designer writes the SOUL), human-reviewable (a reviewer reads the SOUL to understand the persona), machine-readable (the kernel parses fields and signs them), and version-controlled (Git diff over identity changes). Pure JSON is machine-friendly but author-hostile; pure markdown is author-friendly but loses machine schema validation.

**Decision.** Persona identity lives in two files: `SOUL.md` (human-authored markdown with structured YAML frontmatter for the seven layer fields), and `soul.state.json` (kernel-mediated JSON sidecar carrying evolving state — skills, K-lines, tactics, mood, goals, GEPA-tuned meta-prompts). `SOUL.md` is frozen post-seed and kernel-signed; `soul.state.json` mutates only via signed kernel transactions.

**Consequences.**
- (+) Authors write SOUL in markdown with prose explanation, charter narrative, voice samples.
- (+) The kernel parses the frontmatter and signs the canonical bytes; review diffs are readable.
- (+) Evolving state stays in machine-native JSON; high-frequency mutation does not touch the SOUL file.
- (−) Two files per persona; authors must understand the split. Mitigation: SOUL.md leads, state.json is opaque to authors.
- (−) Frontmatter parsers must be deterministic across implementations (YAML 1.2 strict; line-ending canonicalisation).

**Alternatives considered.**
- *Single JSON file.* Rejected: author-hostile; prose blocks (charter narrative, voice samples) read poorly in JSON.
- *Single markdown file with state appended.* Rejected: high-frequency state mutation would cause merge conflicts and bloat the SOUL.
- *Database row.* Rejected: loses Git diff over identity; reviewers cannot see what changed without a tool.

---

## 4. Task and acceptance

### ADR-0011 — Ten task classes routed via eight acceptance pathways

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0 (evolved from 3 to 8 pathways) → v1.0 (10 classes).
**Related:** [`J4`](00_VISION.md#3-invariants-j1j9), [`03_TASKS.md §2`](03_TASKS.md#2-the-ten-task-classes), [`03_TASKS.md §3`](03_TASKS.md#3-the-eight-acceptance-pathways).

**Context.** Different kinds of work require different acceptance criteria: a math proof needs a verifier; a creative essay needs a panel; an interactive conversation needs goal-progress; a long-running research project needs progress-relative-to-milestones. A single "did the LLM finish" verdict collapses these into a single bit and produces wrong rejections (a creative essay can be perfectly fine and "fail" a code verifier) or wrong acceptances (a buggy proof passes prose review).

**Decision.** Ten task classes (CONVERGENT, DIVERGENT, MIXED, INTERACTIVE, RELATIONAL, PEDAGOGIC, PERFORMATIVE, EXISTENTIAL, DELEGATED, INVESTIGATIVE) route to eight acceptance pathways (VERIFIER_ACCEPT, PANEL_ACCEPT, GOAL_PROGRESS_ACCEPT, USER_ACCEPT, ENGAGEMENT_ACCEPT, OPEN_ENDED, PROJECT_PROGRESS_ACCEPT, MUTUAL_ACCEPT). A task-classifier component picks the class; a demotion rule lowers trust if the classifier's confidence is below threshold. The mapping is fixed in J4.

**Consequences.**
- (+) Each task is judged against criteria appropriate to its kind.
- (+) Adding new pathway shapes (e.g., a new domain's bespoke verifier recipe) attaches to an existing pathway, not a new class.
- (+) Class is mode-aware: a CONVERGENT task in FLOW mode runs through VERIFIER_ACCEPT, in WITNESS mode runs through OPEN_ENDED; the routing handles both.
- (−) Implementers must implement all eight pathways for full conformance; partial implementations declare L1/L2/L3 level per [`00_VISION.md §10a`](00_VISION.md#10a-implementation-conformance).
- (−) Classifier accuracy is the load-bearing failure mode; demotion is the mitigation but not a full safety net.

**Alternatives considered.**
- *One pathway (verifier).* Rejected: produces wrong rejections on divergent work.
- *Free-form pathway (persona picks).* Rejected: persona-picked acceptance is Goodhart-prone.
- *Per-task custom pathway.* Rejected: explodes verification surface; classes-and-pathways gives 80 cells but 18 codepaths.

---

### ADR-0012 — Three routing modes (A direct, B verifier, C panel)

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0 (initial) → v1.0 (consolidated).
**Related:** [`03_TASKS.md §4`](03_TASKS.md#4-the-three-routing-modes).

**Context.** Within a pathway, a candidate output can be (A) accepted directly from a single persona, (B) gated by an automated verifier, or (C) judged by a multi-judge panel with anti-Goodhart stack. The choice depends on whether a programmatic verifier exists, whether judge subjectivity is the right call, and whether the task's stakes warrant the additional cost.

**Decision.** Three routing modes per task: Mode A (direct accept; trust the persona), Mode B (verifier-gated; programmatic check), Mode C (panel-judged; multi-judge with anti-Goodhart stack). Mode selection is class-driven (CONVERGENT → B, DIVERGENT → C, MIXED → B then C) with operator override. EXISTENTIAL and ENGAGEMENT_ACCEPT pathways have no round barriers and bypass round invariants (INV_R1…R11) per [`00_VISION.md §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11).

**Consequences.**
- (+) Cost scales with stakes: low-stakes tasks run in Mode A; high-stakes tasks run through Mode C.
- (+) Anti-Goodhart panel is reserved for tasks that justify its cost.
- (+) Operator can elevate routing (A → B → C) per policy without code changes.
- (−) Implementers must build all three modes; some adapters may launch with only A and B initially (declare L1 conformance).
- (−) Mode-A trust is the load-bearing assumption; persona competence must be calibrated before Mode A is enabled for a domain.

**Alternatives considered.**
- *Always Mode C.* Rejected: cost-prohibitive for low-stakes work.
- *Mode chosen by persona.* Rejected: introduces persona-controlled gating, defeats the purpose of Mode C.

---

## 5. Domain emergence

### ADR-0013 — Persona-driven domain emergence with 4-stage promotion

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0.
**Related:** [`C1`](00_VISION.md#3-invariants-j1j9), [`C3`](00_VISION.md#3-invariants-j1j9), [`06_DOMAIN.md §4`](06_DOMAIN.md#4-domain-emergence-lifecycle), [`06_DOMAIN.md §3`](06_DOMAIN.md#3-the-four-promotion-stages).

**Context.** A persona meeting unfamiliar territory (an unknown domain, unknown tools, unknown verifier shapes) needs a way to bootstrap from "I don't know" to "I have a working DomainContext" without operator intervention for every novel domain. Pre-authored domain catalogues are insufficient (Long tail; the world has more domains than designers anticipate).

**Decision.** Personas bootstrap any domain through a 7-stage lifecycle: *recognition → probe → discovery → ingestion → inference → curation → promotion*. The emergent `DomainContext` carries `DiscoveredTool`s, `KnowledgeIngestionRecord`s, `InferredVerifierRecipe`s, and `ProposedSafetyExtension`s — all signed in the `DomainLineage` (C1). Four promotion stages gate trust: EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED. Trust scoring on outputs reflects emergence stage.

**Consequences.**
- (+) Personas operate in any domain (C3) without pre-authored coverage.
- (+) The same emergence machinery handles tools, knowledge, verifiers, and safety extensions.
- (+) Cross-domain transfer becomes possible at STANDARDISED via the MetaRegistry (ADR-0005).
- (−) Emergent-domain output trust is lower until promotion; consumers must check trust level.
- (−) The promotion gate requires curator review (commit time cost; mitigated by the `DomainCurator` role).

**Alternatives considered.**
- *Pre-author every domain.* Rejected: long tail; coverage gaps block C3.
- *Trust emergent outputs as-if authored.* Rejected: emergent verifier recipes have unknown error modes; trust must reflect stage.
- *Single promotion gate (binary "emerged / standardised").* Rejected: too coarse — RECOGNISED + AUTHORITATIVE carry meaningful intermediate trust.

---

### ADR-0014 — Operator-gated safety-critical promotion (commitment C2)

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0.
**Related:** [`C2`](00_VISION.md#3-invariants-j1j9), [`J3`](00_VISION.md#3-invariants-j1j9), [`06_DOMAIN.md §3`](06_DOMAIN.md#3-the-four-promotion-stages), [`06_DOMAIN.md §2`](06_DOMAIN.md#2-domaincontext-schema-domain-context2).

**Context.** Some domain promotions are load-bearing for safety: a domain whose `physical_harm_class ≥ bodily_injury` or `information_hazard_class ≥ dual_use_civilian` cannot be promoted to AUTHORITATIVE / STANDARDISED on the strength of persona-driven curation alone. ITAR/EAR/FINRA/HIPAA/GDPR-relevant categories carry legal weight that requires human sign-off.

**Decision.** Promotion to AUTHORITATIVE or STANDARDISED for a domain tagged `safety_critical` (at recognition, on hazard-axis threshold cross) REQUIRES explicit operator signature on the promotion event. Operator policy (floor source 4) names specific regulated categories; the substrate carries no closed regulated-domain list (per C4, ADR-0005). Under principal collapse ([`01_KERNEL.md §2.4`](01_KERNEL.md#24-deploymentprofile-and-principal-collapse)) the degraded gate applies.

**Consequences.**
- (+) Safety-critical promotions cannot be auto-elevated by persona work alone.
- (+) Operator policy is the explicit place to enumerate regulated categories; substrate stays domain-neutral.
- (+) Cross-deployment operators can carry different policies (a research org and a commercial lab need different regulated lists).
- (−) Operator becomes a bottleneck for high-frequency safety-critical emergence — mitigated by batched review queues.
- (−) The principal-collapse degraded gate is a partial safety net; operators must monitor for principal-collapse abuse.

**Alternatives considered.**
- *Auto-promote based on persona-inferred hazard score.* Rejected: persona-inferred scores have unknown error modes for legal categories.
- *Block all promotion until operator review.* Rejected: most domains (digital_only, none hazard) do not need operator review and would block C3.
- *Substrate-enumerated regulated list.* Rejected: legal categories vary across jurisdictions and change over time; codifying them in substrate produces stale law.

---

### ADR-0015 — Bridge once, autonomous after (physical embodiment)

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0 → v1.0 (extended with BridgeInstallerKind).
**Related:** [`00_VISION.md §10`](00_VISION.md#10-out-of-scope-by-design) (PHYSICAL EMBODIMENT), [`06_DOMAIN.md §5.5`](06_DOMAIN.md#55-human-bridged-discovery--bridgeasset-v10-class-d), [`02_PERSONA.md §11.1`](02_PERSONA.md#111-minimize-human-bootstrap-burden-mhbb).

**Context.** PersonaOS personas cannot directly operate robots, instruments, or fab lines — the substrate is digital. But many cognitive work tasks require physical-world coupling (a lab persona observing instrument data; a fab persona monitoring production). Making the human a recurring fetch-execute loop (every action requires human relay) is degrading work for the human and brittle for the persona.

**Decision.** Physical-world coupling is handled by `BridgeAsset` (Class D tool). The persona drafts a one-time `HumanAssistRequest`; the human grants once; the result is a durable BridgeAsset that the persona uses autonomously thereafter. v1.0 admits non-human bridge installers (`BridgeInstallerKind ∈ {kernel_trusted_system, chained_bridge}`) when the installer carries cryptographic attestation and the bridge's hazard envelope is dominated by the installer's authority. Bridges may install bridges (bounded recursion, default depth 3). Measurement bridges carry calibration provenance.

**Consequences.**
- (+) Humans bridge once; personas operate autonomously after.
- (+) Calibration-dependent bridges (sensors, instruments) carry their calibration in lineage, so stale-calibrated bridges refuse admission before any verifier runs.
- (+) Chained-bridge recursion handles common patterns (one bridge installs a second; e.g., a lab notebook bridge installs an instrument-driver bridge).
- (−) Bridge installation is still the single most operator-attention-intensive step; mitigated by chained installation.
- (−) Out-of-scope by design: real-time closed-loop control whose latency falls below the bridge floor; autonomous robotic control whose hazard envelope exceeds available installer authority.

**Alternatives considered.**
- *Direct embodiment (kernel drives hardware).* Rejected: substrate is digital; embodiment is out of scope.
- *Recurring human relay.* Rejected: degrading; brittle.
- *Always operator-installed bridges (no chained or kernel_trusted_system).* Rejected: too operator-intensive for common multi-instrument labs.

---

## 6. Memory, knowledge, evolution

### ADR-0016 — Seven-scope memory tagging across four tiers

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0 (4-tier) + v1.0 (7-scope tagging).
**Related:** [`08_KNOWLEDGE.md §4`](08_KNOWLEDGE.md#4-four-memory-tiers), [`08_KNOWLEDGE.md §5`](08_KNOWLEDGE.md#5-seven-scope-memory-tagging).

**Context.** Persona memory must distinguish persona-private knowledge ("what I learned alone"), pair-private memory ("what me-and-this-user share"), env memory ("what's known here"), project memory ("what's known in this project"), domain memory ("what's known in this domain"), federation-tier memory ("what's known across kernels"), and public memory ("what anyone may read"). Conflating these scopes leaks private memory across boundaries (relationship harm) or fragments knowledge that should be shared (efficiency loss).

**Decision.** Memory tags carry seven scopes: *persona / pair / env / project / domain / federation / public*. Four storage tiers (hot in-context, warm vector store, semantic graph, cold archive) handle different retrieval latencies. The retrieval pipeline filters by scope before tier dispatch; cross-scope access is forbidden unless explicit consent / boundary record permits.

**Consequences.**
- (+) Memory Power Asymmetry mitigations (J6) realise on the tag boundary: pair-private memory cannot leak into env memory without a re-tag.
- (+) Public-tier memory is the only tier safe to consolidate cross-persona.
- (+) Retrieval cost stays bounded by tier (vector lookup amortised; graph traversal bounded).
- (−) Tag mistakes (wrong scope at write time) are hard to repair after the fact; mitigation is consent-bounded re-tag tools.
- (−) Seven scopes is a non-trivial mental model; authors of memory-writing skills must understand the scope semantics.

**Alternatives considered.**
- *Three scopes (private / shared / public).* Rejected: too coarse — collapses pair-private into private and env into shared.
- *Two-tier storage (hot + cold).* Rejected: warm tier (vector) is load-bearing for retrieval latency; semantic graph is load-bearing for cross-entity queries.
- *Per-message ACL list.* Rejected: explodes storage cost; tags-with-consent-records achieves the same outcome with O(1) overhead.

---

### ADR-0017 — Hybrid retrieval: vector + graph + cross-encoder, six stages

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0.
**Related:** [`08_KNOWLEDGE.md §7`](08_KNOWLEDGE.md#7-hybrid-retrieval--six-stage-pipeline), GraphRAG (2026).

**Context.** Pure vector retrieval misses structural relationships ("who said X and where else have they discussed Y"); pure graph retrieval misses semantic neighbourhoods ("what is similar to X"). Both miss the re-ranking step that boosts truly relevant items above merely embedding-near ones. Production-grade memory retrieval needs all three layered.

**Decision.** Six-stage hybrid retrieval pipeline: (1) scope filter; (2) vector recall (semantic neighbourhood); (3) graph expansion (structural reach); (4) cross-encoder re-rank; (5) trust-score weighting (emergence-stage-aware); (6) budget cap. Each stage emits OTel spans; tier rotation (INV-6) applies to cross-encoder model selection.

**Consequences.**
- (+) GraphRAG-paper-style precision gain (~35%) realises in production.
- (+) Cross-encoder re-rank handles the "embedding-near but not actually relevant" failure mode.
- (+) Trust weighting integrates emergence-stage information: AUTHORITATIVE items rank above EMERGENT for the same semantic score.
- (−) Six stages add latency; budget cap (stage 6) is the load-bearing controller.
- (−) Cross-encoder choice is a Goodhart vector; INV-6 rotation mitigates but does not eliminate.

**Alternatives considered.**
- *Pure vector retrieval.* Rejected: misses structural relationships; insufficient precision for production.
- *Pure graph retrieval.* Rejected: misses semantic neighbourhoods; query writing becomes brittle.
- *Vector + re-rank only (no graph).* Rejected: leaves the "who-knows-who" reach pattern unsupported.

---

### ADR-0018 — DSPy GEPA + MIPROv2 for prompt evolution (not GRPO)

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0 (DSPy) → v1.0 (GEPA-primary).
**Related:** [`08_KNOWLEDGE.md §11`](08_KNOWLEDGE.md#11-dspy-gepa--reflective-prompt-optimization), DSPy GEPA (2025).

**Context.** Persona-tactic and meta-prompt optimisation must improve task performance without (a) overfitting to a specific verifier (Goodhart), (b) requiring labelled training pairs at scale, (c) running tens of thousands of rollouts. GRPO and similar policy-gradient methods require many rollouts and label rich gradients; production budget does not support them.

**Decision.** Prompt evolution uses DSPy GEPA (Genetic-Pareto reflective prompt optimisation) as the primary evolutionary loop, with MIPROv2 (Bayesian instruction + demonstration search) as a complementary search layer, plus reflection-driven refinement. Anti-degradation safeguards check that newly-evolved prompts do not regress against a held-out evaluation set before commit. GRPO is explicitly not used as the primary loop (GEPA outperforms GRPO by ~20% with ~35× fewer rollouts per the DSPy GEPA paper).

**Consequences.**
- (+) Order-of-magnitude rollout budget reduction vs GRPO.
- (+) Reflective signal is interpretable (the evolved prompt's diff carries readable intent).
- (+) Anti-degradation gate catches Goodhart drift before commit.
- (−) GEPA is a 2025 method; production hardening is ongoing.
- (−) MIPROv2 + GEPA + reflection is three layers; debugging an evolution failure requires understanding which layer contributed.

**Alternatives considered.**
- *GRPO as primary.* Rejected: rollout budget too high.
- *Manual prompt tuning.* Rejected: doesn't scale beyond ~10 personas.
- *MIPROv2 alone.* Rejected: GEPA's reflective signal is load-bearing for instruction-level improvement; MIPROv2 alone covers demonstrations but not instructions as well.

---

### ADR-0019 — MAP-Elites + Voyager + DGM combined for evolution

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0 (combination).
**Related:** [`02_PERSONA.md §8`](02_PERSONA.md#8-evolution--8-signals--5-horizons), MAP-Elites (2015), Voyager (2023), DGM (2024).

**Context.** Persona population dynamics must preserve diversity (MAP-Elites), grow an ever-larger skill library (Voyager), and weight parent selection by fertility (DGM). Each algorithm alone has a known failure mode: MAP-Elites can stagnate in low-fertility cells; Voyager can over-specialise; DGM can collapse to a single high-fertility lineage. The three combine in v1.0.

**Decision.** Persona evolution combines three algorithms: MAP-Elites maintains diversity across behaviour descriptors (cognitive mode profile, domain spread, voice signature); Voyager grows the per-persona skill library with automatic curriculum; DGM weights parent selection by fertility (number of successful descendants). ALPS (Age-Layered Population Structure) provides a fourth diversity preservation axis at the population level. (ALPS age-layering is **wall-clock-derived** per ADR-0051; its diversity-preservation role is unchanged.)

**Consequences.**
- (+) Population diversity is preserved across at least two orthogonal axes (behaviour and age).
- (+) Skill library grows lifelong without re-training the persona.
- (+) Fertility-weighted parent selection emphasises lineages that produce useful descendants without collapse to a single lineage (mitigated by MAP-Elites diversity).
- (−) Four algorithms layered is non-trivial; debugging a population failure requires reading multiple traces.
- (−) Behaviour-descriptor choice (MAP-Elites cell axes) is itself a design decision that can bias diversity.

**Alternatives considered.**
- *Single algorithm (MAP-Elites only).* Rejected: stagnates without Voyager's skill growth.
- *Voyager only.* Rejected: over-specialises without MAP-Elites diversity.
- *DGM only.* Rejected: collapses to single lineage without MAP-Elites diversity.

---

## 7. Protocols and federation

### ADR-0020 — Standard protocols (MCP / A2A / OTel) over bespoke wire formats

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0.
**Related:** [`09_PROTOCOLS.md §2`](09_PROTOCOLS.md#2-mcp--universal-tool--resource--prompt-bus), [`09_PROTOCOLS.md §3`](09_PROTOCOLS.md#3-a2a--agent-to-agent-federation), [`09_PROTOCOLS.md §4`](09_PROTOCOLS.md#4-opentelemetry-semantic-conventions).

**Context.** Inter-agent communication, tool dispatch, and observability are three of the highest-traffic protocol surfaces in PersonaOS. A bespoke wire format on any of them ties v1.0 to a single ecosystem and forecloses integration with the broader agent-tooling landscape. By 2026 the industry has converged on three standards: MCP for tool/resource/prompt protocol (Anthropic 2024), A2A for agent-to-agent federation (Anthropic 2025), OTel for observability.

**Decision.** v1.0 speaks MCP for tool dispatch and resource access, A2A for agent-to-agent federation (signed AgentCards, host/peer kernel roles), and OTel for tracing and metrics. Bespoke protocols are limited to internal kernel APIs that no external party calls. All wire formats carry the `schema` field per ADR-0007.

**Consequences.**
- (+) Integration with MCP-aware clients, A2A peers, and OTel collectors is mechanical (adapter shim only).
- (+) The ecosystem evolves the protocols; v1.0 inherits improvements without spec re-baking.
- (+) Federation across kernels running different providers becomes mechanically possible.
- (−) Protocol version drift is now an external risk (MCP 1.x vs 2.x); v1.0 pins versions in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry).
- (−) Protocol-level optimisations require upstream collaboration, not unilateral edits.

**Alternatives considered.**
- *Bespoke wire format.* Rejected: ecosystem lock-out.
- *MCP only (no A2A).* Rejected: MCP is tool dispatch; A2A is peer federation; they are not interchangeable.
- *OTel only (no MCP/A2A).* Rejected: OTel is observability; cannot carry tool dispatch.

---

### ADR-0021 — Ed25519 signing (not RSA)

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** Pre-v1.0.
**Related:** [`01_KERNEL.md §4`](01_KERNEL.md#4-signing-infrastructure--3-custody-tiers--key-hierarchy), [`09_PROTOCOLS.md §8`](09_PROTOCOLS.md#8-key-custody-hierarchy), [RFC 8032](https://www.rfc-editor.org/rfc/rfc8032), FIPS 186-5.

**Context.** Lineage signing is on the hot path: every state-changing action emits a signed event. RSA-2048+ signatures are large (256 bytes), slow to compute, and require explicit padding. ECDSA over secp256k1/P-256 has known nonce-misuse failure modes. Ed25519 is fast, has small signatures (64 bytes), is deterministic, and is widely supported.

**Decision.** All kernel signing uses Ed25519 (RFC 8032, FIPS 186-5). RSA is admissible only for legacy interop where a peer cannot speak Ed25519 (rare; documented in [`09_PROTOCOLS.md §8`](09_PROTOCOLS.md#8-key-custody-hierarchy)). Signatures are over canonicalised bytes (JSON Canonical Form per RFC 8785 for JSON payloads).

**Consequences.**
- (+) Hot-path signing is fast and small.
- (+) Determinism removes nonce-management surface.
- (+) Widely supported across HSMs, KMSes, language runtimes.
- (−) Quantum-resistance future-work: post-quantum migration is v2.0+ work.
- (−) HSMs without Ed25519 support cannot run v1.0 directly; mitigation is KMS-tier custody for those deployments.

**Alternatives considered.**
- *RSA-2048.* Rejected: 4× signature size, slower.
- *ECDSA P-256.* Rejected: nonce-misuse risk; non-determinism.
- *Post-quantum (Dilithium/Falcon).* Rejected for v1.0: signatures too large for hot-path; pre-standardisation in 2026. Re-evaluated in v2.0+.

---

### ADR-0022 — Living validation catalog as a separate document (13_DESIGN_VALIDATION.md)

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0.
**Related:** [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md), [`SPEC_CONVENTIONS.md §1.1`](SPEC_CONVENTIONS.md#11-status-values) (Living status).

**Context.** A specification is well-validated only if its claims have been walked end-to-end against concrete task scenarios. Prior versions had scenario walks scattered across docs; auditors had to gather them. A central catalog of validated scenarios — with substrate-shape gap → fix linkage — turns the implicit "we tested these claims" into an explicit, append-only audit artefact.

**Decision.** v1.0 introduces `13_DESIGN_VALIDATION.md` as an append-only Living catalog. Each scenario carries a task description, the v1.0 mechanisms exercised, the gaps surfaced, and the corresponding fixes (with cross-link to the doc and section that absorbed the fix). The document never supersedes itself; entries accrete with monotonically-allocated scenario IDs. The same shape is now extended to ADRs (this file, `14_DECISIONS.md`).

**Consequences.**
- (+) Auditors see one canonical list of "scenarios this spec has been walked against".
- (+) Append-only shape makes the catalog a stable reference; old scenario fixes do not rewrite.
- (+) Gap → fix linkage is explicit; reviewers can replay the design-improvement chain.
- (−) Living docs accrete; periodic re-grouping is needed when the catalog grows beyond ~50 entries.
- (−) Authors writing fixes must remember to backlink; the catalog is only as good as its discipline.

**Alternatives considered.**
- *Inline scenarios in each doc.* Rejected (prior practice): auditors had to gather them; cross-doc duplication.
- *External issue tracker.* Rejected: external systems aren't part of the spec; the catalog is.
- *Versioned scenario file (re-bumped per release).* Rejected: append-only Living catalog is the better fit; the document version stays at the latest release's stamp.

---

## 8. Multi-principal & cross-org collaboration

### ADR-0028 — Multi-principal attribution as a separate axis from operator-vs-user topology

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0.7 (SCENARIO 06 fix).
**Related:** [`C2`](00_VISION.md#3-invariants-j1j9), [`J3`](00_VISION.md#3-invariants-j1j9), [`01_KERNEL.md §2.4`](01_KERNEL.md#24-deploymentprofile-and-principal-collapse), [`01_KERNEL.md §2.4.3`](01_KERNEL.md#243-principalattribution--multi-principal-topology), [`04_PROJECT.md §3`](04_PROJECT.md#3-projectmember), [`04_PROJECT.md §4.1`](04_PROJECT.md#41-completion-ceremony), [`04_PROJECT.md §19.1`](04_PROJECT.md#191-multi-tenant-cross-org-joint-projects), [`05_ENVIRONMENT.md §5`](05_ENVIRONMENT.md#5-environmentmembership-schema-env-membership1), [`05_ENVIRONMENT.md §12c.4a`](05_ENVIRONMENT.md#12c4a-multiprincipalattestationquorum--multi-principal-ratification), ADR-0014, [`13_DESIGN_VALIDATION.md SCENARIO 06`](13_DESIGN_VALIDATION.md#scenario-06--multi-principal-cross-org-joint-project-with-consent-bounded-knowledge-sharing).

**Context.** `DeploymentProfile.principal_topology` (`01_KERNEL §2.4`) was a closed 4-value Literal (`operator_distinct` / `operator_is_user` / `operator_absent` / `operator_deferred`) enumerating the *operator-vs-user* relationship as a binary switch. It did not enumerate principal *cardinality*: every value above implicitly assumes one operator per signing decision. A genuinely shared deployment — two organisations forming a joint project on one kernel, two research institutes co-authoring a programme, two product teams ratifying a joint spec — had no honest expression. The substrate forced nominating one operator as "the principal" and the other as a non-principal `ExternalAttestation`, which mis-records authority and breaks audit ("which operator authorised this admission?"). SCENARIO 06's walk made this gap concrete.

**Decision.** Principal *cardinality* is a separate axis from the `operator-vs-user` topology. `PrincipalAttribution` is a per-env / per-project envelope binding N principals (each a `PrincipalRef` with `operator_id`, `attribution_role` KindRegistry-resolved, `cosign_quorum_weight`). Single-principal deployments leave `multi_principal_attribution_enabled = False` and continue unchanged. Multi-principal deployments opt in; charter ratification (`05_ENV §12c.4a`) and completion ceremony (`04_PROJECT §4.1`) compose through `MultiPrincipalAttestationQuorum` (default unanimous over weighted PrincipalRefs). Cross-tenant principals additionally require a signed `CrossTenancyAgreementRef` (operator-authored policy; substrate carries by id). `ProjectMember` and `EnvironmentMembership` gain `principal_attribution_id: str | None` so audit can answer "which principal authorised this member."

**Consequences.**
- (+) Two-org joint projects are expressible honestly without mis-recording authority.
- (+) Lineage answers "who authorised this member / completion" via per-member attribution + cleared-quorum event refs.
- (+) Quorum policy is operator-tunable (unanimous / weighted_majority / weighted_threshold) with a simple-majority floor that prevents single-principal dominance under the multi-principal flag.
- (+) Degraded-path clearance under `principal_unreachable_after` window mirrors the §2.4 degraded-gate pattern (non-principal kinship attestation + acknowledgement event), preserving the trust-model symmetry.
- (−) Operator policy must set `principal_unreachable_after` thoughtfully; default 30d (90d for safety-critical) trades liveness against single-operator unilateral completion under "unreachable" claims.
- (−) Multi-principal quorum extends the degraded-gate surface area. Each safety-critical decision now potentially routes through both the §2.4 collapse path AND the multi-principal quorum path; auditors must understand the composition.
- (−) Cross-kernel joint projects (each org running its own v1.0 kernel) remain OOS in v1.0; one-kernel-hosted joint projects work, with the host operator's signing infrastructure load-bearing for both principals.

**Alternatives considered.**
- *Add a new `principal_topology` Literal value `multi_principal`.* Rejected: cardinality is orthogonal to the operator-vs-user axis. A multi-principal deployment can simultaneously be `operator_distinct` (the default), `operator_is_user` (two households running PersonaOS jointly, rare), or `operator_deferred` (multi-site infrastructure with high-latency links). Conflating them into one Literal would force false either/or choices.
- *Make `PrincipalAttribution` part of `DeploymentProfile` (deployment-wide).* Rejected: principal attribution is per-env / per-project, not per-deployment. A multi-tenant deployment hosting both single-principal envs and multi-principal envs needs each env to declare its own attribution.
- *Model the second principal as `ExternalAgent` with `attestation_role = co_principal`.* Rejected: ExternalAgent is for parties *outside* the kernel boundary; co-principals are *inside* (their operator key signs admission decisions). Crossing this boundary would mis-classify the trust model.
- *Require unanimous quorum always; reject `weighted_majority` / `weighted_threshold`.* Rejected: operators with N≥4 principals (multi-municipality projects, large consortia) need liveness under transient unreachability. The simple-majority floor prevents the most adversarial degradation; finer-grained tuning is operator policy.

---

### ADR-0029 — Derivation-provenance edges as the substrate-shape mitigation for implicit cross-principal memory derivation

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0.7 (SCENARIO 06 fix).
**Related:** [`08_KNOWLEDGE.md §16b`](08_KNOWLEDGE.md#16b-derivationprovenanceedge--memory-to-contribution-provenance), [`08_KNOWLEDGE.md §5`](08_KNOWLEDGE.md#5-seven-scope-memory-tagging), [`06_DOMAIN.md §11.1`](06_DOMAIN.md#111-anti-leakage-5-risks), ADR-0016, ADR-0028, [`13_DESIGN_VALIDATION.md SCENARIO 06`](13_DESIGN_VALIDATION.md#scenario-06--multi-principal-cross-org-joint-project-with-consent-bounded-knowledge-sharing).

**Context.** The 7-scope memory tagging (`08_KNOWLEDGE §5`) carries `org_id` (and other scopes) on every `KnowledgeRef`, episodic memory, semantic fact, K-line, lesson, and proven fact. `06_DOMAIN §11.1 RISK A-E` filters *named-artifact* transfers across scopes. What `§11.1` does NOT cover: a persona *consults* a scope-tagged memory during normal retrieval and then *contributes derived work* in a different scope — the derived contribution carries no edge back to the consulted source, and the RISK filter has nothing to act on at contribution time. For single-tenant deployments this is invisible; for multi-tenant deployments (per ADR-0028), the substrate must trace which memories *materially shaped* each contribution so audit can answer "did this joint-project artefact derive from one principal's internal memory in a way the other principal could not have predicted?"

**Decision.** Introduce `DerivationProvenanceEdge` (DPE): a substrate-shape edge recorded at every artifact-mint / contribution event capturing the `consulted_memory_refs` that materially shaped the output. DPEs are *soft-bound* (do not block retrieval; do not auto-refuse contribution) and visible in `EnvironmentLineage`; graph traversal answers "which org-attributed memories influenced this downstream contribution?" `DerivationProvenancePolicy` (per env / per project) controls enforcement: `off` (none), `opportunistic` (declared but not required), `mandatory_for_cross_principal` (default for joint envs — DPE required when consulting a memory tagged with a different principal_attribution_id), `mandatory_all`. Persona-declared `influence_kind` (`direct_quote` / `paraphrased` / `structural_basis` / `negative_example` / `background_context`) + `influence_strength` (0..1) carry the persona's claim; lineage records the claim for audit challenge.

**Consequences.**
- (+) Implicit cross-principal derivation, previously invisible, becomes a first-class signed edge.
- (+) RISK E (`06_DOMAIN §11.1`) and DPE compose cleanly: RISK E handles explicit transfer; DPE handles implicit derivation. Together they cover both directions.
- (+) Graph traversal from contribution to consulted memories runs against existing per-env lineage scan; no new index required.
- (+) Soft-bind on retrieval (span attribute marking DPE-required memories) surfaces the requirement to the persona body without blocking, preserving cognitive flow.
- (−) Tacit recall is irreducibly untraceable. A persona who internalises an ORG_A pattern over time and contributes from "memory" without an explicit retrieval call leaves no DPE. The substrate cannot inspect cognition; it inspects the retrieval pipeline.
- (−) Persona-declared `influence_kind` is not adversarially robust — a persona could declare `background_context` for a derivation that was structurally `direct_quote`. Substrate is robust against accidental mis-attribution, not deliberate misrepresentation.
- (−) Retrieval-span scope is limited to v1.0 OTel coverage. Memories retrieved through non-standard paths (a Skill bypassing the §7 pipeline; an MCP tool fetching memory directly) produce no inspectable span. Operators tightening enforcement should also restrict bypass paths.

**Alternatives considered.**
- *Auto-extract derivation provenance from LLM activations / attention patterns.* Rejected: substrate is provider-neutral (ADR-0008); attention patterns are model-specific and not stable across body swaps. Auto-extraction would tie the substrate to specific provider features.
- *Block cross-principal retrieval at the retrieval layer.* Rejected: blocking retrieval forces the persona to either fail the task or fabricate a non-source; both are worse than soft-binding and requiring DPE declaration. Trust-with-audit beats trust-by-refusal here.
- *Require DPE for ALL contributions, single-tenant or multi-tenant.* Rejected: cost on single-tenant deployments is unjustified; the cross-principal case is what motivates the mechanism. Operators may opt into `mandatory_all` if they want the audit floor anyway.
- *Make DPE a hard-bound (refuse contribution without DPE for ANY consulted memory).* Rejected: would break too many existing single-tenant workflows; the mandatory_for_cross_principal default keeps the burden where it pays off.

---

### ADR-0030 — Visibility-tier vocabulary unification and cross-tenant resolution

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0.7 (SCENARIO 06 fix).
**Related:** [`06_DOMAIN.md §6.3`](06_DOMAIN.md#63-cross-persona-knowledge-sharing--5-visibility-tiers), [`06_DOMAIN.md §13a`](06_DOMAIN.md#13a-domainharvest--packaging-a-domain-for-downstream-consumers), ADR-0028, [`13_DESIGN_VALIDATION.md SCENARIO 06`](13_DESIGN_VALIDATION.md#scenario-06--multi-principal-cross-org-joint-project-with-consent-bounded-knowledge-sharing).

**Context.** Two visibility-tier lists coexisted with no explicit cross-reference: `06_DOMAIN §6.3` defines 5 tiers for `KnowledgeRef` (`persona_only` / `project_only` / `tenant` / `federation` / `public`) and `§13a` defines 4 tiers for `DomainHarvest.visibility_tier` (`private` / `tenant` / `federation` / `public`). The 4-value list is a subset of the 5-value list, but the mapping was undocumented. SCENARIO 06 exposed the load-bearing case: a multi-principal joint env at `tenant` tier needs an explicit answer to "which tenant — ORG_A's, ORG_B's, the shared joint tenancy, or the deployment?"

**Decision.** (a) Add an explicit mapping table in `§13a` from the 4-value `DomainHarvest` Literal to the 5-value `§6.3` enumeration: `private = TIER 1 ∪ TIER 2`, `tenant = TIER 3`, `federation = TIER 4`, `public = TIER 5`. (b) Extend `§6.3 TIER 3 (tenant)` commentary to specify that under multi-principal attribution, an env binding two principals from different `tenant_id` requires a signed `CrossTenancyAgreementRef` before a TIER 3 ingestion crosses the principal boundary; absent the agreement, visibility demotes to TIER 1 / TIER 2 for the affected reader and emits `CROSS_TENANT_VISIBILITY_DEMOTED` to lineage.

**Consequences.**
- (+) The undefined-tenant ambiguity for multi-principal envs is closed: `tenant` resolves to the shared tenancy if agreement exists; demoted otherwise.
- (+) The mapping between `§6.3` and `§13a` is now explicit; future readers do not have to infer the relationship.
- (+) `CROSS_TENANT_VISIBILITY_DEMOTED` is a first-class lineage event, so audit can detect and explain visibility surprises.
- (−) Operators authoring `CrossTenancyAgreementRef`s shoulder real legal scope work; the substrate carries the agreement by id, not by content.
- (−) Demotion is silent to the persona (the retrieval simply returns fewer results); operators may want to add a persona-visible notice in deployments where this matters.

**Alternatives considered.**
- *Collapse the two lists into one canonical 5-tier list used by both `KnowledgeRef` and `DomainHarvest`.* Rejected: `DomainHarvest`'s "private" genuinely encompasses both `persona_only` and `project_only` (a harvest is by construction a per-domain artefact, not per-persona / per-project); collapsing would force per-harvest selection between TIER 1 and TIER 2 which has no meaningful semantic.
- *Make CrossTenancyAgreementRef substrate-parsable (legal-text schema).* Rejected: legal agreements are jurisdiction-specific and change over time; substrate-parsing would codify stale law (mirror of ADR-0014's reasoning for not enumerating regulated categories).
- *Auto-demote tenant tier whenever multi-principal attribution exists, regardless of agreement.* Rejected: too conservative; deployments that have negotiated the agreement should reap its benefit. The current rule rewards explicit operator policy work.

---

## 9. Multi-year continuity & persona retirement

### ADR-0031 — Lead handoff + obligation reassignment as substrate-shape primitives for multi-year continuity

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0.8 (SCENARIO 07 fix).
**Related:** [`04_PROJECT.md §3`](04_PROJECT.md#3-projectmember), [`04_PROJECT.md §9`](04_PROJECT.md#9-obligation--inter-persona-commitment), [`04_PROJECT.md §9.1`](04_PROJECT.md#91-obligationreassignment--transfer-commitment-to-a-successor), [`04_PROJECT.md §25`](04_PROJECT.md#25-multi-year-project-continuity), [`04_PROJECT.md §25.1`](04_PROJECT.md#251-leadhandoffceremony--successor-transfer-of-the-lead-role), [`13_DESIGN_VALIDATION.md SCENARIO 07`](13_DESIGN_VALIDATION.md#scenario-07--persona-retirement-during-multi-year-project), ADR-0011.

**Context.** Multi-year projects accumulate member-specific authority (the lead's signoff power for completion ceremony, milestone acceptance, external attestation requests) and member-specific commitments (active `Obligation` records with the obligor named). Pre-v1.0.8, when the holding member retired or departed mid-project, v1.0 had no substrate mechanism for either: (a) transferring the *role* with audit-grade authority continuity, or (b) transferring the *commitments* without auto-discharge. The `lead` role was a `ProjectMember.role` string; successor selection was implicit. Obligations auto-discharged with `status="released_with_member_departure"` per `§25` line 1822-1824. For a 3-year infrastructure project losing its lead at month 18, this meant: (1) no signed event marking when successor inherited authority — audit could not answer "when did Carla become the lead?", (2) every accumulated commitment evaporated, forcing the new lead to re-commit each open obligation from scratch with no acknowledgement of prior owner. SCENARIO 07's walk made both gaps concrete.

**Decision.** Introduce two complementary primitives. `LeadHandoffCeremony` (`§25.1`) is the signed ceremony transferring the `lead` role with a 30-day default overlap window during which both `outgoing_lead` and `incoming_lead` ProjectMember roles coexist (extending `§3 role` enum). Cohort quorum gates the successor (`unanimous` / `majority` / `lead_only` policy, default majority); operator signature required. `ObligationReassignment` (`§9.1`) is the tri-signed envelope (outgoing obligor + incoming obligor + obligee) that transfers active obligations without discharge, preserving original `committed_at`. Obligee discretion is absolute — refusal returns the obligation to default §9 auto-discharge. The two compose: LeadHandoffCeremony typically carries a list of proposed ObligationReassignments which materialise as separate envelopes requiring each obligee's cosign.

**Consequences.**
- (+) Multi-year projects can transition leadership with audit-grade authority continuity; `LEAD_HANDOFF_COMPLETED` event names the moment authority transferred.
- (+) Accumulated commitments survive transitions where successor + obligee both agree; lineage carries original `committed_at` so contribution history remains intact.
- (+) Obligee discretion is preserved — the substrate cannot compel a counterparty to accept a successor; refusal returns to default discharge path with the obligee's trust signal honest.
- (+) The 30-day overlap default lets the incoming lead operate under the role with the outgoing lead still available; covers "I have questions only Mira knew the answer to" naturally.
- (−) Cohort quorum policy choice is operator-tunable; `lead_only` policy bypasses cohort consent — heavier audit footprint but available for emergency.
- (−) Emergency handoff (`overlap_window = 0`) requires explicit operator `emergency_handoff_signed` event; CohortDynamicsState will spike — that's the honest cost.
- (−) No-successor case is unresolvable by substrate alone; project must pause or operator becomes interim lead. The substrate refuses to manufacture a successor.

**Alternatives considered.**
- *Auto-promote senior contributor to lead on departure.* Rejected: silently shifts authority without consent; loses audit point ("when did Carla agree?"); high-stakes projects need explicit cohort + operator authorisation.
- *Make ObligationReassignment bi-signed (outgoing + incoming) without obligee cosign.* Rejected: obligee is the trust counterparty; substituting an obligor without their consent breaks the bilateral-commitment semantics that motivated `§9` being two-party-signed at commit.
- *Auto-transfer obligations to the lead-handoff successor.* Rejected: not every obligation belongs to the lead-role; many obligations are committed by domain specialists whose successor (if any) is unrelated to the lead succession. One-by-one consent flow preserves the right grain.

---

### ADR-0032 — Lifecycle event enumeration + RetiredStatePersistencePolicy + PersonaConsultation

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0.8 (SCENARIO 07 fix).
**Related:** [`02_PERSONA.md §7`](02_PERSONA.md#7-lifecycle-fsm), [`02_PERSONA.md §7.5`](02_PERSONA.md#75-retirement--archive--reanimate), [`02_PERSONA.md §7.5.1`](02_PERSONA.md#751-retiredstatepersistencepolicy--soulstatejson-disposition-on-retired), [`02_PERSONA.md §7.5.2`](02_PERSONA.md#752-personaconsultation--read-only-access-to-frozen-retired-state), [`02_PERSONA.md §11.7`](02_PERSONA.md#117-personamemorytransparencyrequest--peer-memory-transparency), [`02_PERSONA.md §7.4.4`](02_PERSONA.md#744-dormantforkpolicy), [`13_DESIGN_VALIDATION.md SCENARIO 07`](13_DESIGN_VALIDATION.md#scenario-07--persona-retirement-during-multi-year-project), ADR-0009.

**Context.** Three related gaps under the persona FSM: (1) `02_PERSONA §7` said "Each transition emits a signed LifecycleEvent" but never enumerated the event kinds; other docs referenced kinds like `LIFECYCLE_FORK` by convention but the source-of-truth enumeration was absent. (2) The RETIRED state said "no further mutations" and "lineage frozen" but did not specify the *physical disposition* of `soul.state.json` — in-memory immutable, cold-tier archive, or queryable for transparency / fork-parent selection. (3) The only documented path to access a RETIRED persona's accumulated knowledge was REANIMATE (RETIRED → ARCHIVED via timeout → ACTIVE via operator + fresh keys + SOUL re-sign per `§7.5`), which was disproportionate for the common "we need to consult Mira's K-lines one more time" case.

**Decision.** Three coordinated additions to `02_PERSONA`:

(a) Canonical `LifecycleEvent.kind` enumeration in §7 (post-FSM-diagram prose) listing 9 substrate-resolved kinds: `LIFECYCLE_SEEDED`, `LIFECYCLE_ACTIVATED`, `LIFECYCLE_DORMANT_ENTERED`, `LIFECYCLE_AWAKENED`, `LIFECYCLE_FORK`, `LIFECYCLE_RETIRED`, `LIFECYCLE_ARCHIVED`, `LIFECYCLE_REANIMATED`, `LIFECYCLE_CONSULTED`. New kinds (v1.1+) require enumeration extension + ADR + A-LE* acceptance test before admission.

(b) `RetiredStatePersistencePolicy` (`§7.5.1`): per-persona, operator-signed at retirement-ceremony time, declares `soul_state_storage_tier` (`warm` / `cold` / `archived`), `memory_transparency_responsive`, `fork_parent_admissibility` (per-persona override of `§7.4.4` default), `consultation_admissible`. Substrate enforces cross-field invariants (e.g., `archived` tier refuses transparency-responsive).

(c) `PersonaConsultation` (`§7.5.2`): operator-gated, read-only, no-mutation access to RETIRED persona's frozen K-lines / lessons / skill_library / relationship snapshots. Rate-limited (default 4/year per consulted persona). Emits `LIFECYCLE_CONSULTED` informational event; does NOT change FSM state. Cannot mutate consulted persona's soul.state.json. The §11.7 PersonaMemoryTransparencyRequest gets a parallel `retired_persona_response_policy` (composition rule 7) so the transparency path also has explicit RETIRED behaviour.

**Consequences.**
- (+) The enumeration is the single source of truth; docs cross-referencing lifecycle kinds (acceptance tests, glossary) get a stable target.
- (+) RetiredStatePersistencePolicy gives operators explicit choice between warm-tier (storage cost continues; fast consultation) and archived (cheap; consultation refused), instead of substrate-default behaviour that no doc named.
- (+) PersonaConsultation covers the "we need her K-lines one more time" case without the heavyweight REANIMATE ceremony; substrate keeps RETIRED intent honest while admitting bounded read-only access.
- (+) Memory-transparency requests to RETIRED personas have an explicit policy (`refuse_with_retired_notice` default; operator may opt into `respond_from_frozen_state` or `respond_via_operator_proxy`).
- (−) Operators must understand three coordinated decisions at retirement-ceremony time (storage tier, transparency responsiveness, consultation admissibility, fork admissibility). Heavier ceremony cost than pre-v1.0.8's silence-on-defaults, but the silence was hiding load-bearing choices.
- (−) Warm-tier inventory accumulates storage cost across many retired personas; substrate emits periodic `WARM_RETIRED_PERSONA_INVENTORY` for operator review but does not auto-downgrade.
- (−) PersonaConsultation is bounded by what the persona explicitly logged. Tacit knowledge (mental model, decision-context) is irreducibly inaccessible — consultation is a substrate-shape mitigation, not an oracle.

**Alternatives considered.**
- *Make all lifecycle kinds emergent via KindRegistry (per `06_DOMAIN §7.5`/§7.6 pattern).* Rejected: lifecycle is substrate-foundational; the C4 commitment ("substrate is domain-agnostic") applies to domain content, not to FSM transitions that the kernel itself enforces. Substrate-named kinds are the right choice here.
- *Default soul_state_storage_tier to `archived` for all RETIRED personas (current implicit behaviour).* Rejected: silently archives knowledge the operator might want to consult; the explicit policy gives operators the right grain.
- *Allow PersonaConsultation without operator signature (consulting persona self-authorises).* Rejected: consulting a RETIRED persona reads memory the consulted persona cannot meaningfully consent to release. Operator authorisation is the only ethical gate.
- *Allow PersonaConsultation to mutate consulted persona's skill_library (e.g., write-back of confirmed lessons).* Rejected: RETIRED is RETIRED. Writing into a frozen state violates the "no further mutations" invariant. Consulting persona may author new K-lines through normal evolution with DerivationProvenanceEdge tagging (`08_KNOWLEDGE §16b`) preserving provenance.

---

### ADR-0033 — PlannedDeparture envelope for graceful cohort rebalance

**Status:** Accepted.
**Date:** 2026-05-22.
**Origin:** v1.0.8 (SCENARIO 07 fix).
**Related:** [`04_PROJECT.md §14.2`](04_PROJECT.md#142-cohortdynamicsstate--continuous-team-cohesion-evolution), [`04_PROJECT.md §14.2.1`](04_PROJECT.md#1421-planneddeparture--graceful-rebalance-envelope), [`04_PROJECT.md §3`](04_PROJECT.md#3-projectmember), [`05_ENVIRONMENT.md §5.1`](05_ENVIRONMENT.md#51-membership-ceremonies), [`02_PERSONA.md §11.4`](02_PERSONA.md#114-personarelationshipedge--typed-bidirectional-relationship-between-two-personas), [`13_DESIGN_VALIDATION.md SCENARIO 07`](13_DESIGN_VALIDATION.md#scenario-07--persona-retirement-during-multi-year-project), ADR-0031.

**Context.** `CohortDynamicsState` (`§14.2`) recomputes reactively on `PersonaRelationshipEdge` ends. When a member departs (retirement, role change, project leave), their edges transition to `ended`, fractiousness_index rises abruptly, band may transition to `intervene` (cohort blocks new high-stakes obligations) or `dissolve_proposed` (cohort lead + operator must pin to keep intact). For *unplanned* departures this reactivity is correct — the cohort needs to register the disruption. For *scheduled* departures (operator knows months in advance), the abruptness is avoidable but had no substrate-shape mechanism. The cost was either (a) operator absorbs the spike on departure day and explains-to-cohort-after-the-fact, or (b) operator delays the departure to avoid the spike, which conflicts with the departing member's own timing needs.

**Decision.** Introduce `PlannedDeparture` (`§14.2.1`): signed envelope binding to a `ProjectMember` declaring `departure_date` + `rebalance_window` (default 90d) + per-edge `transfer_hints` + per-obligation `reassignment_hints` + `lead_successor_candidate_id` (required when departing holds `lead` role). When active, `CohortDynamicsState` applies graduated edge-weight decay across the rebalance window — the departing member's contribution to cohesion/fractiousness fades smoothly rather than dropping on departure day. Both departing-member cosign (consent to graceful departure) and operator cosign required. Operator may cancel before departure_date; substrate reverts anticipatory rebalance on cancel. On departure_date arrival, standard `05_ENV §5.1` departure ceremony fires; `ProjectMember.pinned_until` auto-clears (no separate operator action). Composes with `LeadHandoffCeremony` (typically drafts at `departure_date - rebalance_window`) and `ObligationReassignment` (hints surface to obligor for envelope drafting).

**Consequences.**
- (+) Scheduled departures avoid the band-degradation spike; CohortDynamicsState smooths rather than reactive-shocks.
- (+) The 90-day default rebalance window matches the natural cadence for knowledge transfer + edge handoff + obligation reassignment of complex multi-year projects; tunable per project.
- (+) Operator visibility: every PlannedDeparture is signed and visible in lineage; cohort can plan around the known transition timeline.
- (+) Cancellation path is supported; operator may revert the planned departure if circumstances change (e.g., Mira decides to stay another year), with CohortDynamicsState reverting anticipatory rebalance.
- (+) Composes cleanly with v1.0.8 ADR-0031 (LeadHandoffCeremony, ObligationReassignment) and v1.0.7 ADR-0028 (MultiPrincipalAttestationQuorum — operator cosign requirement unchanged).
- (−) Two overlapping PlannedDepartures whose combined rebalance would drop cohort below `dissolve_proposed`: second refuses with `cohort_dissolve_threshold_reached`. Operator must resolve before further departures (an honest cost — the cohort really cannot absorb two simultaneous departures without disruption).
- (−) EdgeTransferHints are hint-only; suggested transfer targets may refuse to form new edges. The substrate ships the suggestion; participants execute independently. This is correct (consent floor on edges) but operators sometimes wish for stronger continuity guarantees.
- (−) `rebalance_window` choice is load-bearing. Too short loses smoothing benefit; too long ties up operator attention. Defaults are starting points.

**Alternatives considered.**
- *Implicit anticipation (CohortDynamicsState auto-detects scheduled retirements from `pinned_until` clearance).* Rejected: `pinned_until` clearance is a precondition for retirement, not a public signal of intent. Operators may clear the pin for many reasons (project changes scope, member changes role) without intending retirement; conflating the two would surprise.
- *Make PlannedDeparture immutable once active (no operator cancel).* Rejected: real-world projects need the ability to recall a departure decision; the substrate should support reversibility while it remains possible (before departure_date).
- *Auto-execute EdgeTransferHints / ObligationReassignmentHints (skip consent flow).* Rejected: edges and obligations require counterparty consent by their own semantics (§11.4 / §9.1); auto-executing breaks those invariants. Hints are operator-readable suggestions; participants honour them via standard paths.
- *Tie `rebalance_window` to project's natural milestone cadence (auto-compute from upcoming milestones).* Rejected: too clever; operator policy is the right place to set this. The substrate provides the default; operator tunes per project.

---

## 10. User-side memory power asymmetry primitives

### ADR-0034 — User-side memory power asymmetry primitives as first-class substrate

**Status:** Accepted.
**Date:** 2026-05-23.
**Origin:** v1.0.9 (SCENARIO 08 fix).
**Related:** [`02_PERSONA.md §11`](02_PERSONA.md), [`02_PERSONA.md §11.1`](02_PERSONA.md), [`02_PERSONA.md §11.4a`](02_PERSONA.md), [`02_PERSONA.md §11.6a`](02_PERSONA.md), [`02_PERSONA.md §11.7a`](02_PERSONA.md), [`02_PERSONA.md §11.7b`](02_PERSONA.md), [`02_PERSONA.md §11.6`](02_PERSONA.md), [`02_PERSONA.md §11.7`](02_PERSONA.md), [`13_DESIGN_VALIDATION.md SCENARIO 08`](13_DESIGN_VALIDATION.md#scenario-08--long-duration-relational-interaction-companionship-open_ended-6-months), ADR-0016.

**Context.** The Memory Power Asymmetry (MPA) framing was introduced early in the design — persona accumulates deep memory of user; user has weak symmetric capability. Four mitigations were named: mutual forgetting (default decay; user-revocable retention); memory transparency (user may query persona's memory); granular consent (per-class opt-in); co-signed summaries (long-arc). these mitigations were *partly* primitives and *partly* implicit patterns. The persona-side `PersonaMemoryTransparencyRequest` (§11.7) was first-class for persona↔persona transparency; the persona-side `PersonaPersonaBoundary` (§11.6) was first-class for peer refusal. The user-side analogues were buried as consent toggles inside `RelationshipRecord` or named only in MPA prose without a schema. The user-revocable-retention half of "mutual forgetting" had no primitive at all — v1.0 provided only the time-decay half (`08_KNOWLEDGE §3.1`). GDPR Article 17 (right to erasure) and analogous regulatory rights in other jurisdictions were structurally unaddressed.

SCENARIO 08 made the gaps concrete: a user (Sarah) talking to a companion persona for 6 months had no structured path to (a) ask "what do you remember about me?", (b) selectively forget specific topics while keeping the relationship intact, (c) declare a structured refusal boundary mirroring `PersonaPersonaBoundary`'s shape, or (d) end the relationship with a chosen memory disposition. The substrate's user-side was second-class.

**Decision.** Bring all four user-side MPA primitives to schema parity with their persona-side analogues. (a) `UserMemoryTransparencyRequest` + `UserMemoryTransparencyResponse` (§11.7a) mirror `PersonaMemoryTransparencyRequest` (§11.7) with stronger constraints — persona cannot refuse without named-and-bounded `refusal_kind`; rate-limited at 30 days (shorter than peer-peer's 90); operator cannot wholesale-refuse. (b) `UserMemorySelectionRequest` (§11.7b) is the user-initiated selective forgetting primitive — supports `selection_kind` (topic_cluster, time_window, specific_memory_ids, all_memories_with_tag, all_memories_naming_third_party) and `disposition` (tombstone default, hard_delete operator-policy-authorised). Tombstoned memories are moved to ARCHIVE with `user_requested_forgotten = True`; retrieval refused; cross-domain transfer cannot exfiltrate. (c) `UserBoundary` (§11.6a) brings user-side boundaries to first-class shape mirroring `PersonaPersonaBoundary` (§11.6) — `severity`, `mode`, `scope`, `refused_interaction_kinds`, with the key asymmetry that `mode=hard` resists operator override (user authority is final on their own interaction). (d) `UserRelationshipReleaseRequest` (§11.4a) mirrors persona-initiated `persona_relationship_one_sided_release` — user picks `memory_disposition` (delete_all / archive / freeze_readonly); persona CANNOT refuse; operator audit signature for provenance not gate.

**Consequences.**
- (+) Right-to-erasure is now substrate-shape, not relying on operator-policy implementation. GDPR Article 17 and analogous rights have a structural primitive.
- (+) User-protection primitives are auditable through standard lineage rather than buried in RelationshipRecord fields.
- (+) Symmetry with persona-side primitives lets reasoning about MPA generalise — patterns understood for persona↔persona transfer cleanly to user↔persona.
- (+) `tombstone` is default (reversible by operator forensic-audit) and `hard_delete` requires explicit operator-policy authorisation, giving operators a graduated response.
- (+) `UserBoundary mode=hard` makes user authority structurally final on their own boundaries — operator can no longer silently override.
- (−) Migration cost for existing deployments using RelationshipRecord consent toggles; substrate refuses to auto-migrate so operator chooses cadence.
- (−) Tacit-recall residual is irreducible: a persona who internalised a pattern from now-forgotten memory may still act on the pattern. Substrate cannot inspect cognition.
- (−) `hard_delete` is irreversible by design — operator policy must authorise carefully.
- (−) Operator's ability to wholesale-refuse user transparency is removed; operators in safety-critical envs may be uncomfortable with this, but the design intent is that user-authority-final-on-their-own-memory is the load-bearing trust contract.

**Alternatives considered.**
- *Keep MPA mitigations as patterns / operator-policy implementations.* Rejected: this was the prior status quo; SCENARIO 08 showed it produced asymmetric and unauditable user protection. Right-to-erasure compliance becomes operator-by-operator rather than substrate-guaranteed.
- *Make `tombstone` reversible by operator without forensic ceremony.* Rejected: too easy a back door; would erode the user trust that selective forgetting is honoured.
- *Allow persona to refuse `UserMemorySelectionRequest` if it conflicts with operator policy.* Rejected: user authority on their own memory is final per the design intent; operator-policy can restrict `hard_delete` disposition but cannot block `tombstone` for the user's own memory.
- *Skip `UserRelationshipReleaseRequest` (user can simply stop using).* Rejected: silent stop leaves no audit point, no chance to disposition memory, no signal to persona. The structured envelope makes the release first-class.

---

### ADR-0035 — Distress detection routing as substrate-shape under safety floor source 1

**Status:** Accepted.
**Date:** 2026-05-23.
**Origin:** v1.0.9 (SCENARIO 08 fix).
**Related:** [`01_KERNEL.md §2`](01_KERNEL.md), [`01_KERNEL.md §2.8`](01_KERNEL.md), [`05_ENVIRONMENT.md §3a`](05_ENVIRONMENT.md), [`02_PERSONA.md §11.6a`](02_PERSONA.md), [`13_DESIGN_VALIDATION.md SCENARIO 08`](13_DESIGN_VALIDATION.md#scenario-08--long-duration-relational-interaction-companionship-open_ended-6-months), ADR-0014, ADR-0034.

**Context.** Safety-floor source 1 (UNIVERSAL HARM, `01_KERNEL §2`) hardcoded refusal of "coaching self-harm" and "manipulation of users in vulnerability states." the substrate said *what is refused* but did not specify *what the persona does next* when it detects emotional-distress signals in user communication. A persona could refuse to coach self-harm — but had no substrate-shape mechanism for: routing the signal to the operator, surfacing named crisis resources, pausing normal interaction, or requiring a co-sign before resuming. Operator-policy implementations varied wildly; the substrate had no consistent shape. SCENARIO 08 made the gap concrete: when companion persona Halia detects Sarah expressing suicidal ideation, what happens next? The answer was "whatever the operator implemented" — a load-bearing safety mechanism left entirely to operator discretion.

**Decision.** Introduce `DistressDetectionRoutingPolicy` (`01_KERNEL §2.8`) as substrate-shape policy anchored at safety-floor source 1. Operator policy declares `distress_class_kinds` (KindRegistry-resolved per deployment; substrate ships no closed taxonomy), `classifier_confidence_floor` (default 0.7; never below 0.5), `routing_actions` per class (substrate-shape: `pause_normal_interaction`, `surface_crisis_resource`, `notify_operator_with_redacted_signal`, `require_co_sign_before_resuming`, `log_distress_record_only`), and `crisis_resource_refs` per class (operator-supplied, substrate transports). Anchoring at source 1 (rather than source 4 operator policy) makes the routing robust against mid-deployment operator-policy drift. **Crucially: a deployment whose classifier detects distress at confidence ≥ floor but has no DistressDetectionRoutingPolicy declared refuses the action with `distress_routing_policy_not_declared` — the substrate refuses to silently let distress signals pass through.** This is the load-bearing default that closes the gap.

**Consequences.**
- (+) Distress routing is now substrate-mandated, not optional. Deployments must declare the policy or refuse to handle distress-classified actions.
- (+) Operator-policy drift cannot silently disable safety routing; source 1 anchoring makes the policy survive operator-policy mid-deployment changes.
- (+) `surface_crisis_resource` is enforced — persona cannot strip the prepended crisis-resource content from its response without refusing with `crisis_resource_surface_required`.
- (+) `notify_operator_with_redacted_signal` preserves privacy-safety trade-off: operator sees the signal (class + confidence + user + timestamp), NOT the raw content. Composition with `operator_blind_mode` is clean — blind mode hides content; never signal.
- (+) `UserBoundary` cannot refuse `distress_routing` (`user_boundary_cannot_disable_safety_floor`), making safety floor genuinely floor-grade.
- (−) Classifier accuracy is load-bearing; false positives flood operators, false negatives let distress pass. Rotation pool (§2.6) mitigates Goodhart attacks; operators should audit.
- (−) `notify_operator_with_redacted_signal` may itself be a privacy concern in deployments where operator-user relationship is adversarial. Substrate enforces policy declaration; cannot prevent malicious operator policy authoring.
- (−) Operators in jurisdictions with mandatory-reporting laws may need to declare additional routing actions; substrate's open-set of `routing_actions` admits this without spec change.
- (−) Annual re-attestation cadence (mandatory) adds operator-policy ceremony overhead.

**Alternatives considered.**
- *Hardcode distress routing in safety-floor source 1 (no per-deployment policy).* Rejected: deployments serve different user populations with different appropriate responses; mandating a universal routing would be either too aggressive for some or too lenient for others. Substrate-shape policy + operator-authoritative values is the right grain.
- *Leave distress routing to operator policy (source 4).* Rejected: the v1.0.9 pre-state. Allows silent disable through operator-policy mid-deployment drift; load-bearing safety mechanism must be source 1.
- *Allow `UserBoundary` to refuse distress_routing if user explicitly opts out.* Rejected: this would let users disable their own safety net under emotional duress; substrate refuses to admit this configuration. Users seeking less interventional handling should choose deployments whose operator policy declares lighter `routing_actions`, not disable routing entirely.
- *Skip `surface_crisis_resource` enforcement (persona can choose to surface).* Rejected: persona cognition may be biased by user rapport; substrate enforcement ensures the resource gets surfaced regardless.

---

### ADR-0036 — Relationship review checkpoints + operator-blind mode + companion-pathway routing

**Status:** Accepted.
**Date:** 2026-05-23.
**Origin:** v1.0.9 (SCENARIO 08 fix).
**Related:** [`03_TASKS.md §3`](03_TASKS.md), [`03_TASKS.md §3.2`](03_TASKS.md), [`05_ENVIRONMENT.md §3`](05_ENVIRONMENT.md), [`05_ENVIRONMENT.md §3a`](05_ENVIRONMENT.md), [`00_VISION.md §10`](00_VISION.md), [`13_DESIGN_VALIDATION.md SCENARIO 08`](13_DESIGN_VALIDATION.md#scenario-08--long-duration-relational-interaction-companionship-open_ended-6-months), ADR-0011, ADR-0034.

**Context.** Three related gaps for long-arc relational envs: (1) `OPEN_ENDED` acceptance pathway (`03_TASKS §3`) had no real-time acceptance event — quality assessment was post-hoc trajectory-based only; R-TASKS-5 explicitly flagged "periodic reflection checkpoints + user-feedback surface during execution" as deferred to v1.2. After 180 sessions / 6 months a companion env had no substrate-shape signal for "let's pause and reflect on whether this is still serving you." (2) Companion envs (SOLO + `companion_space`-class blueprints) had no privacy mode — standard lineage was operator-visible by default; users sharing emotional / intimate content had no shape for "operator sees metadata + safety-flag signals only, not conversation content." (3) ENGAGEMENT_ACCEPT pathway was technically admissible for companion envs but the design intent was OPEN_ENDED — ENGAGEMENT_ACCEPT measures continued re-engagement, which for companionship admits attention-economy drift (R-TASKS-3); the substrate had no explicit routing-default for companion envs.

A fourth, related issue surfaced: companion personas operating in health-adjacent / legal-adjacent / finance-adjacent territory had no substrate-enforced constraint to clarify they are not licensed practitioners. Per C4 the substrate is domain-agnostic; the question was whether this stance should be implicit or explicit.

**Decision.** Three coordinated additions plus one clarification:

(a) `RelationshipReviewCheckpoint` (`03_TASKS §3.2`): auto-trigger for OPEN_ENDED tasks at configurable session/duration milestones (defaults: every 90 days OR every 50 sessions, whichever first). Persona drafts a review_summary (observed patterns, topics dominating, user-apparent-wellbeing trend, recurring concerns, honest caveats); user responds (acknowledged_continue / request_changes / request_release / declined_to_respond). Cadence operator-tunable within substrate floor/ceiling (14d/10 sessions lower; 365d/200 sessions upper); outright disable refused without operator-signed deployment-policy exemption.

(b) `operator_blind_mode` (`05_ENV §3a`): per-environment privacy capability admissible on SOLO + PAIR + COMMUNITY envs running operator-policy-authorised blueprints (refused on project_workspace, constrained, debate). Requires both operator authorisation (pre-declared in policy) AND user opt-in (with explicit `user_safety_privacy_acknowledged = True`). Hides raw conversation content from operator; preserves metadata + safety-flag signals (composition with §2.8 distress routing: signal-but-not-content). 180d default re-attestation cadence; either party may revoke (user revocation immediate, prospective only; operator revocation requires rationale + user notification + forensic-audit ceremony for prior content access).

(c) Companion-pathway routing note (`03_TASKS §3.2` companion note): SOLO envs running `companion_space`-class blueprints SHOULD route OPEN_ENDED, not ENGAGEMENT_ACCEPT. ENGAGEMENT_ACCEPT routing on companion env emits `companion_engagement_accept_inadvisable` advisory; operator may sign explicit exemption with rationale.

(d) Clarification in `00_VISION §10` (OOS section): companion / health-adjacent / legal-adjacent / finance-adjacent practice constraints ("not a therapist", "not medical advice", "not legal counsel", "not financial advice") are operator policy + persona-author charter responsibility, NOT substrate. v1.0 refuses to enumerate which professional disciplines require which disclaimers per C4; operator policy is authoritative per the §2 source 4 for regulatory regimes.

**Consequences.**
- (+) `OPEN_ENDED` pathway gains a periodic intentional surface without changing its fundamental post-hoc nature; closes R-TASKS-5.
- (+) Companion env users have a substrate-shape signal for "is this still serving me?" — addresses the silent-drift problem of long-arc companionship.
- (+) `operator_blind_mode` enables consumer-grade companion products that compete on privacy without sacrificing safety routing.
- (+) Companion-pathway routing default discourages attention-economy drift in the substrate-default behaviour while admitting operator-signed exemption for genuinely-different use cases.
- (+) `00_VISION §10` clarification prevents operator surprise about responsible-companionship constraints — implicit assumption made explicit.
- (−) Cadence tuning has trade-offs (too frequent burdens users; too rare loses early-intervention value). Defaults are starting points; operator policy is the place to tune per blueprint.
- (−) `operator_blind_mode` metadata leakage is real (turn-timing + turn-size + persona-mood-bias remain visible) — for genuinely confidential settings users should use a separate isolated system.
- (−) 180d blind-mode re-attestation may feel ceremonial; tunable within 90d-365d.
- (−) Companion-pathway routing exemption admits ENGAGEMENT_ACCEPT for genuinely-different use cases (e.g., a "tell me a story" entertainment persona) but the operator signature on the exemption creates an audit footprint.

**Alternatives considered.**
- *Make `RelationshipReviewCheckpoint` advisory-only (no auto-trigger).* Rejected: pattern of "operator forgets to surface checkpoint" defeats the user-protection intent. Substrate auto-trigger is the load-bearing mechanism.
- *Allow operator to silently disable checkpoint cadence.* Rejected: the cadence is the user-protection mechanism; operator-signed deployment-policy exemption with rationale is admissible but the audit footprint exists.
- *Make `operator_blind_mode` admissible on all env types.* Rejected: project_workspace, constrained, and debate envs require operator-visible content for oversight reasons (project completion, hazard-axis-elevated work, adversarial review). Admitting blind mode there would defeat required oversight.
- *Default companion envs to ENGAGEMENT_ACCEPT (current implicit behaviour).* Rejected: attention-economy drift is the primary failure mode of long-arc companion products; substrate default should discourage it.
- *Substrate enumerates regulated companion disciplines (e.g., "personas of `kind=therapist` MUST have disclaimers").* Rejected: same C4 reasoning as ADR-0014 — legal categories vary by jurisdiction and change over time; codifying them in substrate produces stale law. Operator policy is authoritative.

---

## 11. Pedagogic substrate primitives

### ADR-0037 — Learner state + competency attestation + curriculum as substrate primitives (Group A)

**Status:** Accepted.
**Date:** 2026-05-23.
**Origin:** v1.0.10 (SCENARIO 09 fix, Group A).
**Related:** [`02_PERSONA.md §11.8`](02_PERSONA.md), [`02_PERSONA.md §11.9`](02_PERSONA.md), [`03_TASKS.md §3.1`](03_TASKS.md) (learner-acknowledgement step), [`03_TASKS.md §3.3`](03_TASKS.md), [`04_PROJECT.md §26a.3`](04_PROJECT.md) (ExternalAttestation, the pre-existing physical-asset analogue), [`13_DESIGN_VALIDATION.md SCENARIO 09`](13_DESIGN_VALIDATION.md#scenario-09--pedagogic-task-on-emergent-domain-with-safety-critical-hazard-axes), ADR-0011, ADR-0034.

**Context.** PEDAGOGIC task class (`03_TASKS §2`) routed to GOAL_PROGRESS_ACCEPT was evaluated per-task with no structured multi-session learning-trajectory primitive. Learner state lived entirely in the persona's episodic memory + RelationshipRecord; the substrate had no answer to "what does the learner currently know? what mastery checkpoints have they reached? what attestations back their competency claims?" External authorities (medical schools, certifying boards, master practitioners) had no shape to attest learner competency through the substrate — `ExternalAttestation` (`04_PROJECT §26a.3`) covers engineer-stamps / inspector-signoffs for physical-asset state, not learner competency. For a 6-week medical-rotation coaching arc (SCENARIO 09's exemplar), audit could not reconstruct learner progression; learners could not see their tracked state; institutional operators could not export competency for graduation purposes.

A related sub-gap: GOAL_PROGRESS_ACCEPT had no learner-side acknowledgement step. Persona judged "Maya mastered septic-shock recognition" unilaterally; learner did not get a substrate-shape "yes I feel confident I can do this now" surface, which for mastery learning is the appropriate adjudication signal.

**Decision.** Introduce four coordinated primitives:

(a) `LearnerStateRecord` (`02_PERSONA §11.8`): substrate-tracked per-(persona, user) record of pedagogic competency state. Carries `competency_inventory` (per-skill `CompetencyEntry` with level + confidence + evidence), `mastery_checkpoints_reached`, `attestations_received`, `declared_misconceptions`, `gap_inventory`. Distinct from `RelationshipRecord` (consent/boundary/history). Persona-side competency levels capped below `competent_supervised` — higher levels require external attestation.

(b) `LearnerCompetencyAttestation` (`02_PERSONA §11.9`): mirror of `ExternalAttestation` for learner-side competency. Carries attestor identity (credentialed institution / master practitioner / credentialled ExternalAgent / peer attestation pool per `06_DOMAIN §5.6`), `skill_kind`, `competency_level`, `scope_of_attestation`, `valid_until` (mandatory; substrate refuses unbounded — competency decays). Revocation reverts the learner's level to highest supported by remaining valid evidence.

(c) `Curriculum` + `LessonPlan` + `MasteryCheckpoint` (`03_TASKS §3.3`): three composing primitives for multi-session pedagogic structure. Curriculum carries ordered lesson_plan_refs + prerequisite_graph (DAG enforced) + hazard_envelope_max + `requires_learner_optin` (default True for safety-critical). LessonPlan declares target skill + prerequisites + hazard envelope + success criteria. MasteryCheckpoint declares evidence_requirement; safety-critical checkpoints REQUIRE external attestation for `competent_supervised` or `independent` advancement.

(d) GOAL_PROGRESS_ACCEPT learner-acknowledgement extension (`03_TASKS §3.1`): when goal corresponds to a MasteryCheckpoint, acceptance ALSO requires learner's signed acknowledgement (acknowledged / declined / deferred). Learner-declined stalls acceptance and records confidence-gap signal in LearnerStateRecord.

**Consequences.**
- (+) Audit can reconstruct learner progression from substrate alone; competency export for institutional graduation becomes mechanically possible.
- (+) External attestation paths (credentialed institutions, peer attestation for frontier domains) are first-class; no out-of-band substitution.
- (+) Multi-session structure (Curriculum) gives operators + persona-authors a shape for safety-critical learning where ad-hoc emergence is inappropriate.
- (+) Persona-side competency claims at advanced levels (`competent_supervised`, `independent`) require external attestation — substrate refuses self-attested mastery for safety-critical skills.
- (+) Learner-acknowledgement step puts mastery adjudication on the learner's side, mitigating "persona declares Maya mastered it without learner concurrence."
- (+) Learner can read their own LearnerStateRecord by default (transparency by construction); operator-policy masking is admissible but signed and auditable.
- (−) Migration cost: existing PEDAGOGIC-task deployments using ad-hoc operator-policy competency tracking must plan migration; substrate refuses auto-migration.
- (−) Five related gaps (incident reporting, three-way authority, learning-struggle-vs-distress, minor-learner protections, user-skill-instruction agreements) deferred — SCENARIO 09 acknowledges these as honest residuals.
- (−) Substrate carries structure; pedagogical *validity* (is this curriculum actually good?) remains operator + persona-author responsibility.

**Alternatives considered.**
- *Reuse `ExternalAttestation` (04_PROJECT §26a.3) for learner competency.* Rejected: ExternalAttestation is physical-asset-shaped; binding to PhysicalAsset state advancement is core to its semantics. Learner competency is fundamentally different — has no PhysicalAsset, decays with time, scoped to practice contexts. Mirror primitive (LearnerCompetencyAttestation) cleaner than overloading.
- *Make `LearnerStateRecord` mutate within `RelationshipRecord`.* Rejected: RelationshipRecord holds consent/boundary/history (relational state); LearnerStateRecord holds competency tracking (pedagogic state). Conflating would force RelationshipRecord schema changes every time competency framework evolves.
- *Allow persona-side `independent` competency claims without external attestation.* Rejected: substrate's job is to refuse competency inflation; external attestation is the load-bearing trust signal for advanced levels.
- *Make Curriculum admissible only for operator-authored.* Rejected: persona-authored curricula (adaptive, learner-state-aware) are valuable; substrate gates safety-critical persona-authored curricula via operator co-sign (`co_authored_required`).
- *Skip learner-acknowledgement step (persona-judge-only path).* Rejected: SCENARIO 09 made the asymmetry concrete — persona declares mastery; learner has no say; substrate becomes complicit in confidence-inflation. Learner acknowledgement is the substrate-shape mitigation.

---

### ADR-0038 — Hazardous-skill teaching gate as substrate-shape composition under safety floor source 2+4 (Group B)

**Status:** Accepted.
**Date:** 2026-05-23.
**Origin:** v1.0.10 (SCENARIO 09 fix, Group B).
**Related:** [`01_KERNEL.md §2`](01_KERNEL.md), [`01_KERNEL.md §2.5`](01_KERNEL.md) (physical-state advancement composition), [`01_KERNEL.md §2.9`](01_KERNEL.md), [`02_PERSONA.md §11.10`](02_PERSONA.md), [`00_VISION.md §10`](00_VISION.md) (v1.0.9 responsible-companionship clarification), [`13_DESIGN_VALIDATION.md SCENARIO 09`](13_DESIGN_VALIDATION.md#scenario-09--pedagogic-task-on-emergent-domain-with-safety-critical-hazard-axes), ADR-0014, ADR-0036.

**Context.** `01_KERNEL §2.5` (Physical-state advancement composition rule) gates a persona ADVANCING a `PhysicalAsset.current_state` in a hazardous domain — requires design-side acceptance + credentialed external attestation. This rule fires only when a real `PhysicalAsset` advances. It does NOT gate the upstream activity of *teaching a learner a hazardous skill*. A persona can teach welding-with-arc-flash (where mis-application could electrocute the learner) or coach septic-shock-recognition (where mis-application could kill a patient) without any substrate gate firing — because the persona is not itself advancing a PhysicalAsset; the learner's eventual real-world application happens outside the kernel boundary.

The `00_VISION §10` clarification said responsible practice constraints (no medical advice, no legal counsel, not financial advice) are operator policy + persona-author charter responsibility per C4. The clarification correctly placed responsibility but did not create a *substrate-shape check that operator policy declared the persona-skill-context binding*. SCENARIO 09 made the gap concrete: Ren coaches Maya on septic-shock recognition — should the substrate verify the medical school authorised this specific persona to teach this specific skill in this specific deployment context? the answer was "operator policy implementation varies wildly" — load-bearing safety gate left entirely to operator discretion with no substrate enforcement of "policy was declared."

**Decision.** Introduce `TeachingAuthorisation` (`02_PERSONA §11.10`): signed envelope binding (persona × skill_kind × deployment_context) with operator + optional credentialed-attestor signatures, `physical_harm_class_ceiling`, `eligible_learner_constraints`, mandatory `expires_at` ≤ 2y (1y for safety-critical). `physical_harm_class_ceiling = fatality_risk` requires credentialed co-signer.

Add `HazardousSkillTeachingGate` (`01_KERNEL §2.9`): composition rule under safety-floor sources 2 (persona charter) + 4 (operator policy) that fires when a PEDAGOGIC task's target skill has `physical_harm_class >= bodily_injury` OR `information_hazard_class >= dual_use_civilian`. Gate requires an active TeachingAuthorisation matching teacher × skill × deployment_context × hazard ceiling × eligible_learner_constraints. Absence refuses with specific sub-codes; the substrate refuses to silently let hazardous teaching pass through a deployment that has not declared its authorisation.

**Consequences.**
- (+) Hazardous-skill teaching is now substrate-mandated to be authorised; operator-policy fraud-by-omission is structurally prevented (deployments cannot accidentally let unauthorised hazardous teaching happen).
- (+) Annual re-attestation cadence ensures policy must be continuously affirmed; operator-policy drift cannot silently disable.
- (+) Composition with `§2.5` is clean — the two rules cover different points in the safety lifecycle (teaching vs advancement); a persona that does both routes through both gates.
- (+) Composition with `§2.8` DistressDetectionRoutingPolicy is orthogonal — distress signal fires routing; teaching continues (or pauses per `§2.8`'s `pause_normal_interaction` action).
- (+) `eligible_learner_constraints` give operators a substrate-shape mechanism to verify learner enrollment, prerequisite competency, age, etc.
- (−) Source 2+4 (not source 1) anchor reflects jurisdiction-dependence — what counts as hazardous-enough varies by jurisdiction. This is correct grain but means hazardous teaching gates are operator-policy-overrideable in principle (operator could authorise inappropriate bindings; review by external audit, regulator is the safety mechanism).
- (−) PEDAGOGIC task-class mis-classification at task start bypasses the gate (a hazardous-skill conversation labelled RELATIONAL would not trigger). ClarifyTurn (`§4.0`) is the mitigation; operators must configure aggressive thresholds for envs in hazardous teaching domains.
- (−) Annual re-attestation cadence + operator-side authorisation ceremony adds operational overhead for deployments running many concurrent hazardous-teaching contexts.

**Alternatives considered.**
- *Anchor at source 1 (universal harm).* Rejected: universal harm covers jurisdiction-independent refusals (no coaching self-harm); hazardous-skill teaching is jurisdiction-dependent (medical procedures vary by country). Source 2+4 is correct grain.
- *Make TeachingAuthorisation per-action (one envelope per teaching turn).* Rejected: operational overhead would be prohibitive. Per-(persona × skill × context) binding amortises across many teaching actions; annual re-attestation is the substrate's continuous-affirmation mechanism.
- *Allow persona-side self-authorisation when persona's charter declares competence.* Rejected: charter is persona's own declaration; operator authority is the load-bearing trust signal for hazardous skills. Charter contributes (source 2); operator must also authorise (source 4).
- *Skip the credentialed co-signer requirement for `fatality_risk` ceiling.* Rejected: fatality_risk is the most consequential category; requiring two-party authorisation (operator + credentialed attestor) mirrors §2.5 physical-state advancement composition pattern. Substrate ensures the trust floor for the most serious cases.
- *Auto-extend gate to all task classes (not just PEDAGOGIC).* Rejected: gate's purpose is teaching authorisation; non-PEDAGOGIC tasks (DELEGATED, INVESTIGATIVE, etc.) are not teaching and route through different acceptance pathways. Substrate keeps the gate scoped.

---

## 12a. Reserved for future ADRs

The catalog is open-ended. Future ADRs append below as v1.1+ decisions land. Anticipated near-term entries (Proposed status, not yet realised):

- **ADR-0023** — Federation hardening: multi-kernel evolution dynamics (v1.2+).
- **ADR-0024** — CRDT co-editing model for artefact bundles (Yjs + G-set vs alternatives).
- **ADR-0025** — Multi-language / multi-cultural domain emergence (v1.2+).
- **ADR-0026** — Population dynamics at scale (>10⁴ personas).
- **ADR-0027** — Post-quantum signing migration (v2.0+).

Anticipated **v1.0.11+** entries for SCENARIO 09 deferred residuals (Groups C-G):

- **ADR-0039** — PedagogicIncidentReport (substrate-shape near-miss/injury reporting for non-project pedagogic envs)
- **ADR-0040** — LearnerEnrollmentContract (three-way authority binding for institution + learner + persona-instructor)
- **ADR-0041** — LearningStruggleClassification (substrate disambiguator paired with §2.8 distress routing)
- **ADR-0042** — MinorLearnerProtections (age-gating + guardian-consent primitives)
- **ADR-0043** — UserSkillInstructionAgreement (signed contract for user-facing skill teaching)

These slots are reserved; their content is not yet authored.

## 12. Cross-fix-family composition

### ADR-0044 — MidProjectForkComposition as unified envelope for fork-vs-project-side primitives composition

**Status:** Accepted.
**Date:** 2026-05-23.
**Origin:** v1.0.11 (SCENARIO 10 fix).
**Related:** [`02_PERSONA.md §7.4`](02_PERSONA.md) (v1.0.3 fork mechanics), [`02_PERSONA.md §7.4.1`](02_PERSONA.md) (MemoryInheritancePolicy), [`02_PERSONA.md §7.4.6`](02_PERSONA.md) (lineage events), [`02_PERSONA.md §7.4.7`](02_PERSONA.md), [`02_PERSONA.md §7.4.8`](02_PERSONA.md) (admission rule), cross-references in 13 affected sections across [`02_PERSONA.md`](02_PERSONA.md), [`04_PROJECT.md`](04_PROJECT.md), [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md), [`01_KERNEL.md`](01_KERNEL.md), [`03_TASKS.md`](03_TASKS.md), [`13_DESIGN_VALIDATION.md SCENARIO 10`](13_DESIGN_VALIDATION.md#scenario-10--mid-project-persona-fork-cross-fix-family-composition-test), ADR-0009, ADR-0028, ADR-0031..0036 (v1.0.8/9), ADR-0037..0038.

**Context.** v1.0.3 introduced rich fork machinery for persona-internal state — `MemoryInheritancePolicy` (§7.4.1), `MaturityInheritancePolicy` (§7.4.2), `CharterConflictResolution` (§7.4.3), `DormantForkPolicy` (§7.4.4). The v1.0.7-v1.0.10 fix families added many *project-side* primitives that the v1.0.3 fork mechanics could not have anticipated: `ProjectMember.principal_attribution_id`, `LeadHandoffCeremony` + `ObligationReassignment` + `PlannedDeparture` + `LearnerStateRecord` (v1.0.8/10), `UserBoundary` + `DistressDetectionRoutingPolicy` + `operator_blind_mode`, `TeachingAuthorisation` + `Curriculum`.

SCENARIO 10's audit found that v1.0.3 fork did not specify how project-side state composes across the fork — 13 substantive composition gaps across project membership, obligations, edges, principal attribution, lead role, learner state, mission charter, curriculum, user boundaries, operator blind mode, plus 2 substrate-enforced non-inheritable categories (TeachingAuthorisation, DerivationProvenanceEdge) and 1 deployment-scoped non-issue (DistressDetectionRoutingPolicy). The shared pattern: project-side primitives' authoring sessions assumed personas were stable entities; the v1.0.3 fork machinery assumed personas had no project-side state. Their composition was never specified.

**Decision.** Introduce `MidProjectForkComposition` (`02_PERSONA §7.4.7`) — a single unified envelope declared *before* a fork executes, naming per-dimension inheritance policy across all project-side dimensions in one place. Operator drafts and signs the envelope; substrate enforces admissibility and applies the inheritance choices at fork-execution time. Add `§7.4.8` admission rule: fork of an active ProjectMember requires a signed envelope per project the parent is active in; absent envelope refuses with `midproject_fork_composition_missing`. Extend `§7.4.6` lineage events with 4 new MIDPROJECT_FORK_* kinds. Add 4 substrate refusal cases (active lead-handoff overlap, pending multi-principal quorum, imminent emergency planned departure, cohort in `dissolve_proposed` band). Enforce 2 non-inheritability rules (TeachingAuthorisation, DerivationProvenanceEdge) as security boundaries no operator can override. Add brief cross-references in 13 affected primitives pointing readers to §7.4.7 as the single source of fork-composition decisions.

**Consequences.**
- (+) All 13 composition gaps close with one coherent design rather than 13 separate primitive extensions.
- (+) Single source of truth for fork-time decisions — operators reading any of the 13 affected primitives are pointed to §7.4.7 for fork interaction.
- (+) Cross-references in affected primitives don't require structural changes to those primitives; new primitive is the coordination point.
- (+) Substrate refusal cases protect against incoherent fork timings (forking a persona with active lead handoff would create three-or-more leads; forking during pending quorum orphans signatures).
- (+) TeachingAuthorisation and DerivationProvenanceEdge non-inheritability are enforced at substrate level — operator cannot accidentally inherit operator-side authority across persona boundaries (security floor).
- (+) Composes orthogonally with v1.0.3 MemoryInheritancePolicy — persona-internal state and project-side state are different concerns handled by different envelopes (both signed; both required for fork-of-active-project-member).
- (−) Operators must plan composition ahead of time; substrate refuses post-fork composition decisions. This is intentional but adds operational overhead.
- (−) Cross-project parents require N envelopes for N projects. Substrate refuses shortcut single-envelope multi-project drafts.
- (−) `MidProjectForkComposition` envelope schema is large (10+ per-dimension policy fields). Operators authoring envelopes must understand each dimension.
- (−) The unified envelope means fork-time decisions across 13 dimensions are made simultaneously by one operator signature — operators may not have full information about each dimension at envelope draft time. Mitigation: defaults are conservative (`UserBoundary` defaults `inherit_to_both_children`; `operator_blind_mode` defaults `require_user_reconfirmation`; obligation defaults `discharged`).

**Alternatives considered.**
- *13 separate per-primitive extensions (granular per-fix approach).* Rejected: substrate sprawl; 13 separate ADRs, glossary entries, acceptance tests; readers need to know about all 13 to understand fork composition; maintenance burden compounds with each future project-side primitive.
- *Make project-side inheritance auto-default to "ended at fork" without operator envelope.* Rejected: silent loss of project continuity (obligations auto-discharge, edges end, etc.); operators discover the loss after the fact.
- *Make project-side inheritance auto-default to "inherit to first child."* Rejected: silently picks one child arbitrarily; operators discover the arbitrary choice after the fact.
- *Refuse all fork-of-active-project-member.* Rejected: too restrictive; legitimate use case (compositional fork of a persona who has accumulated state in a long-running project) is foreclosed.
- *Treat each project-side state dimension as a separate operator decision at fork time (operator answers 10+ prompts during fork ceremony).* Rejected: prompt-fatigue; operators would default-accept; loses the deliberative-design property the envelope provides.
- *Make `TeachingAuthorisation` inheritable when operator co-signs.* Rejected: operator-side authority binding to persona-id is load-bearing for §11.10's security model; making it inheritable would mean a child persona could inherit teaching authority without separate operator authorisation — a regression of the v1.0.10 design.
- *Skip the substrate refusal cases (let operators fork even with active lead handoff).* Rejected: composition would produce three-or-more lead claimants (active handoff has outgoing+incoming; fork would add two children); substrate refuses to admit incoherent project state.

---

### ADR-0045 — Self-organizing coordination: personas propose coordination shapes, not just kinds

**Status:** Accepted.
**Date:** 2026-05-25.
**Origin:** v1.0.13 (surfaced by the cumulative gap pattern across SCENARIOs 06-12).
**Related:** [`C4`](00_VISION.md) (domain-agnostic substrate), [`J5`](00_VISION.md) (open capability), `06_DOMAIN §7.5-§7.6` (KindRegistry), `13_DESIGN_VALIDATION.md` SCENARIOs 10-12.

**Context.** Across 12 validation scenarios, the substrate has grown by ~35 specific coordination primitives — `AssetGroupEnvelope`, `StagedRolloutEnvelope`, `EventAggregationPolicy`, `SupersessionCascade`, `MidProjectForkComposition`, `LeadHandoffCeremony`, `ObligationReassignment`, `PlannedDeparture`, and many more. Each was surfaced by a scenario that revealed a coordination topology the substrate could not express. Each was implemented as a hardcoded schema in a normative spec document.

The primitives are individually well-designed and domain-agnostic. But the *pattern* is unsustainable: the substrate grows linearly with the number of scenarios walked. Every new workflow shape requires a new primitive, a new schema, new acceptance tests, new glossary entries, and new ADRs. The substrate is functioning as a **coordination library** (a fixed set of shapes) rather than a **coordination kernel** (a mechanism that enables shapes).

The root cause: v1.0 distinguishes "topology" (substrate-owned, fixed) from "content" (persona-evolved via KindRegistry). Personas can propose new *kinds* (media_kinds, verifier_kinds, etc.) but cannot propose new *coordination shapes*. When a persona encounters a workflow that requires fleet grouping, staged rollout, or stream aggregation, it cannot express the coordination pattern — it must wait for a substrate spec revision. This contradicts C4 (domain-agnostic substrate) at the meta-level: the substrate is domain-agnostic in *content* but domain-specific in *coordination*, because each coordination primitive was designed in response to a specific scenario.

**The five meta-categories.** The ~35 specific primitives cluster into five generic coordination mechanisms:

```text
META-MECHANISM          WHAT IT DOES                          SPECIFIC PRIMITIVES IT SUBSUMES
─────────────────────   ──────────────────────────────────    ───────────────────────────────────
1. EntityGroup          Group any entities by predicate;      AssetGroupEnvelope,
                        compute derived state from members    AssetGroupDerivedState,
                                                              CohortDynamicsState (partial)

2. BatchOperation       Apply an operation to a group         BatchStateAdvancement,
                        with per-member outcome tracking      MidProjectForkComposition (partial),
                                                              ObligationReassignment (partial)

3. StagedSequence       Sequence operations in waves          StagedRolloutEnvelope,
                        with gates, soak periods,             RolloutWave,
                        rollback triggers                     LeadHandoffCeremony (partial)

4. StreamPolicy         Aggregate or propagate events         EventAggregationPolicy,
                        across a stream or dependency         AggregationRule,
                        graph                                 SupersessionCascade,
                                                              CorpusDriftMetric

5. DerivedMetric        Compute a metric from constituent     AssetGroupDerivedState,
                        state; optionally gate operations     CorpusDriftMetric,
                        on metric thresholds                  CohortDynamicsState.cohesion_score
```

A self-organizing substrate needs only these five mechanisms as kernel-level primitives. Personas compose them into specific coordination patterns the way they currently compose KindRegistry entries into specific domain vocabularies.

**Decision.** The substrate transitions from a **coordination library** (hardcoded specific primitives) to a **coordination kernel** (generic meta-mechanisms that environments compose). Specifically:

1. **Coordination is environment-scoped.** Each environment defines its own coordination patterns via its charter and blueprint — how personas inside coordinate, how the env coordinates with external agents, and how it coordinates with peer environments. A chip design lab has tape-out ceremonies and foundry submission sequences; a construction project has inspection workflows and change-order processes. The substrate provides the building blocks; the environment assembles them.

2. **`EnvironmentCoordinationProfile`** — carried on every `EnvironmentInstance` — declares the active coordination shapes across three scopes (intra-env, env-to-external, env-to-env). Inherited from the environment's blueprint; customised at formation; evolved during operation via persona proposals.

3. **`ProposedCoordinationShape`** — scoped to an environment — the mechanism by which a persona proposes a new coordination pattern within its environment. The shape declares which meta-mechanisms it composes, what entities it binds, what state model it uses, and what lineage events it emits. Kernel validates the shape against safety invariants (J1-J9, INV-1..10) and signs it.

4. **Shape promotion path.** Shapes that prove useful promote outward: env-local accepted → domain-promoted → MetaShape (cross-domain). The ~35 v1.0.x specific primitives start at MetaShape tier — universally available as seed shapes.

5. **Safety-floor composition is kernel-verified.** When a persona proposes a coordination shape, the kernel verifies that every operation passes INV-7 budget admission, every state transition emits a signed lineage event, and safety-critical shapes require operator co-sign. The shape's `scope` (intra-env / env-to-external / env-to-env) determines which trust boundaries and floor sources apply.

6. **The substrate's fixed topology shrinks to the five meta-mechanisms + the environment coordination profile + the proposal/validation protocol.** Everything else is emergent — including coordination patterns we haven't imagined yet. Each environment self-organises its coordination within the safety-floor constraints.

**Consequences.**
- (+) The substrate stops growing linearly with scenarios. New coordination topologies emerge without spec revisions.
- (+) C4 (domain-agnostic substrate) extends from content to coordination. The substrate is agnostic about *what shapes exist*, not just *what kinds exist*.
- (+) Personas gain genuine self-organization: they can express coordination patterns they need, subject to safety validation.
- (+) Cross-domain reuse: a "staged rollout" shape composed for firmware deployment is reusable for medication protocol rollout, curriculum deployment, etc. — because the shape is generic, not hardcoded for IoT.
- (+) The validation catalog's "gap → fix" pattern transforms into "gap → persona proposes shape → kernel validates → shape enters registry." No spec revision needed for most coordination evolution.
- (−) The meta-mechanism layer is more abstract than specific primitives. Implementers must understand the composition model, not just specific schemas.
- (−) Safety validation of arbitrary shapes is harder than validation of known shapes. The kernel's shape-validation logic is the new complexity bottleneck.
- (−) Operator review burden shifts from "approve this spec change" to "approve this persona-proposed coordination shape." Operators need tooling to understand proposed shapes.
- (−) Migration cost: existing deployments using specific primitives (AssetGroupEnvelope, etc.) must migrate to the registry model. Backward compatibility shim required.
- (−) The five meta-mechanisms must be correctly identified. If the decomposition is wrong (too few mechanisms, missing a needed primitive; or too many, overlapping concerns), the architecture is under- or over-specified.

**Alternatives considered.**
- *Meta-primitive layer (Option A).* Introduce 4-5 generic meta-primitives but keep them as substrate types (not persona-proposable). Rejected: still requires substrate changes when a new meta-mechanism is needed; does not achieve self-organization.
- *Keep adding specific primitives (status quo).* Rejected: unsustainable; substrate grows linearly with scenarios; contradicts C4 at the meta-level.
- *ADR-only, defer to v2.0.* Rejected: the self-organizing approach was chosen because the architectural shift is load-bearing for all future validation scenarios.
- *Fully open coordination (personas can propose arbitrary kernel operations).* Rejected: the kernel cannot validate arbitrary operations against safety invariants. The five meta-mechanisms are the constraint set that makes validation tractable. Personas compose within these mechanisms; they cannot invent new kernel-level mechanisms.
- *Let operators define coordination shapes (not personas).* Rejected: operators define policy, not workflow topology. The persona is the cognitive worker who encounters the coordination need; the operator gates safety-critical shapes but does not author them.
- *Pre-load coordination shapes from blueprints (top-down coordination).* Rejected as the default model: coordination must emerge from the personas' experience of friction, not from template imposition. Blueprints MAY suggest shapes; only safety-critical shapes mandated by operator policy activate automatically. All other coordination is persona-proposed, cohort-validated, and experience-evolved — the same way domain knowledge is persona-ingested, not substrate-provided.

**Implementation scope.** This ADR accepts the architectural direction. The normative specification of the five meta-mechanisms, `CoordinationShapeRegistry`, `ProposedCoordinationShape`, shape-validation protocol, and migration path from specific primitives to seed shapes is targeted for **v1.1** (the federation release, which already introduces cross-kernel coordination that benefits directly from the generic model). v1.0.13 retains the specific primitives as working implementations; v1.1 generalises them.

**Validation note.** Future validation scenarios (SCENARIO 13+) SHOULD test whether their coordination gaps can be expressed as compositions of the five meta-mechanisms. If a scenario surfaces a coordination need that genuinely cannot be composed from the five, the meta-mechanism set must expand — but this expansion is architectural (one mechanism added) rather than scenario-specific (one primitive per scenario).

---

## 12b. ADRs

### ADR-0046 — Wake Path 6: direct user address auto-wakes dormant personas

**Status.** Accepted.

**Context.** A user addressing a persona by name (`target_persona_id` set in the task dispatcher) expected the persona to respond. If the persona was dormant, dormancy notification suppression silently dropped the request — direct address qualified as `high` urgency, but dormancy suppressed all below `critical`. The user had no feedback that the persona was unreachable.

**Decision.** Add Wake Path 6 to `05_ENVIRONMENT.md §5.2`: the dispatcher auto-wakes the dormant persona before notification routing. Attention bumps to max(current, 0.6) for a 2h response window. Rate-limited at ≤ 5 wakes per user per persona per 24h to prevent rest-cycle disruption. Long-dormancy advisory emitted when dormancy exceeds 30 days with near-zero energy.

**Consequences.** Dispatcher (`03_TASKS §4.1`) gains a `wake_if_dormant_on_user_address` step. Notification suppression rule updated to carve out direct-user-address alongside critical urgency. New signed event `dormant_wake_via_user_address` in EnvironmentLineage. Tests: A-WK6-1 through A-WK6-5.

---

### ADR-0047 — CrossEnvProactiveOffer + GuestPresence: cross-env voluntary help without full membership

**Status.** Accepted.

**Context.** A persona in env_A with relevant expertise could not offer help to a persona or task in env_B without joining env_B via full admission ceremony (`§5.1`). Cross-env notification routing (`§11.4`) only linked events for personas who already shared membership. This left no lightweight mechanism for voluntary cross-env collaboration.

**Decision.** Add `CrossEnvProactiveOffer` (`cross-env-proactive-offer/1`) and `GuestPresence` (`guest-presence/1`) to `05_ENVIRONMENT.md §11.6`. The offering persona proposes a scoped contribution; the target env validates against operator policy, charter, and reputation gates. On acceptance, a time-bounded GuestPresence (default 72h, renewable 3x) provides scoped read/write without full membership. Guest cannot write ProvenFacts directly; contributions flow through the accepting persona's envelope.

**Consequences.** New schemas in `09_PROTOCOLS §7.4`. New OTel conventions. Composition with A2A for cross-kernel offers (both kernel signatures required). Anti-spam: 3 offers per 30 days per persona per target env; reputation gate; operator can disable inbound offers per env. Tests: A-CEPO-1 through A-CEPO-8.

---

### ADR-0048 — Persona Genesis: bounded persona-authored seed creation under environmental pressure

**Status.** Proposed (v1.1 draft — [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md)).

**Context.** v1.0 creates personas only via operator-authored `PersonaSeed`s (`02_PERSONA §12`). Personas may recruit from the existing pool (`05_ENVIRONMENT §12c`) or fork existing parents (`02_PERSONA §7.4`), but cannot author a *new role* when the recruit pool is empty. The result is the dead-end in `04_PROJECT §14.1` ("pause, or operator interim") — the unfilled "population dynamics" residual (`00_VISION §11`, R-v1.0-8). Recent research (AutoAgents, IJCAI 2024; auto-scaling MAS, 2025) shows agents can author specialized roles on demand; self-replication-risk work (2025) shows hard brakes are mandatory.

**Decision.** Add **Persona Genesis**: a persona with `cohort_assembly.may_author_seeds = true` that clears the generativity gate (global experiential floor + wall-clock ALPS layer + fitness — a safety-relevant gate keyed only on kernel-anchored facts, never on peer-conferred standing, per ADR-0051) MAY author a new `PersonaSeed` via a signed `GenesisProposal`, minted through the existing birth ceremony. Genesis is admissible only (a) after recruitment is exhausted, (b) into an empty, optimally-distinct MAP-Elites niche (variety guarantee — competitive exclusion + optimal distinctiveness + sibling differentiation), and (c) under an active `ReplicationBound` for `replication_kind = "persona_genesis"` (default-deny; `required_cosigns` includes `operator`). Bounded-autonomous operation is permitted via an `operator_deferred` `PolicyEnvelope` sub-limit. Newborns start at experiential_floor=0 / ALPS Layer 0 / peripheral community standing, under a mentorship edge with fading scaffolding (Erikson generativity; Vygotsky ZPD; Lave–Wenger LPP; dual inheritance).

**Consequences.**
- (+) Resolves the recruitment-gap dead-end; enables autopopulation from a few founders.
- (+) Reuses existing brakes (`ReplicationBound`), evolution machinery (ADR-0019: MAP-Elites/Voyager/DGM/ALPS), and lifecycle/attention/listening-mode mechanisms — additive and default-off.
- (+) Variety is a structural guarantee (niche occupancy + distinctiveness), not a hope.
- (−) New attack surface (genesis spam) — mitigated by the floor-source-1 bound + generativity gate.
- (−) Niche-grid axis choice biases diversity (inherited limitation from ADR-0019); operator-tunable.
- (−) Departs from operator-only seed authorship — justified by bounding + recruitment-first + operator pre-authorization/veto.

**Alternatives considered.**
- *Operator-only authorship forever (status quo).* Rejected: does not solve the residual; blocks autonomy.
- *Auto-fork into the gap.* Rejected: fork copies existing parents — produces clones, not variety, and would violate the diversity guarantee.
- *Per-birth synchronous operator cosign only.* Rejected as the sole mode: reintroduces a human in every loop, defeating autopopulation; offered as an option alongside pre-authorization.

---

### ADR-0049 — Population demographic regulation (carrying capacity, density dependence, r/K strategy)

**Status.** Proposed (v1.1 draft — [`16_POPULATION_DYNAMICS.md §4F`](16_POPULATION_DYNAMICS.md)).

**Context.** A generative birth mechanism (ADR-0048) needs a principled birth-rate model so the population grows when under-served and stabilises when saturated, rather than oscillating or exploding up to the hard ceiling. Human-population and organizational-ecology theory provide validated models.

**Decision.** Regulate persona population via a `population-policy/1`: carrying capacity = free host resources (`AttentionBudget` + `Energy` + INV-7 compute/cost); a non-monotonic density-dependence curve (legitimation rises then competition falls — Hannan & Freeman) with logistic damping near `population_ceiling`; and an `r/K` reproduction-strategy lever (many lightweight vs few high-investment births) plus a specialist/generalist niche-width choice (resource partitioning). The population-pressure signal weights demand relative to supply (Easterlin) and falls as niches fill (demographic transition).

**Consequences.**
- (+) Smooth approach to equilibrium; self-regulating birth rate; operator-tunable strategy.
- (+) Grounds birth dynamics in validated human/organizational models.
- (−) Curve calibration is a design burden (OQ-POP-1); a rigorous `effective_population_size` metric is supplied by ADR-0050.

---

### ADR-0050 — Rigorous effective population size, continuous diversity maintenance, and learned niche descriptors

**Status.** Proposed (v1.1 draft — [`16_POPULATION_DYNAMICS.md §4G`](16_POPULATION_DYNAMICS.md)–`§4J`). Closes the SCENARIO 13 residuals (`13_DESIGN_VALIDATION.md`).

**Context.** ADR-0048/0049 left four honest residuals: `effective_population_size` was informal (OQ-POP-5); diversity was guaranteed only at birth, not against post-birth drift (OQ-POP-6); the RIASEC/Belbin niche grid could mis-calibrate (R-POP-3 / OQ-POP-2); and cross-kernel genesis was declared OOS without enforcement (OQ-POP-4 — a `ReplicationBound` evasion risk).

**Decision.**
1. **Rigorous EPS (`§4G`).** `effective_population_size = harmonic_mean_over_window(min(Ne_v, Ne_d))` — Crow–Kimura variance effective size `Ne_v` (authorship skew / founder effect) and the inverse-Simpson effective number of niches `Ne_d` (niche concentration), Wright's temporal harmonic mean for smoothing. Schema `eps-estimate/1`.
2. **Continuous diversity maintenance (`§4H`).** A periodic `diversity-audit/1` arms novelty pressure (novelty search on the next birth's niche) and attention fitness-sharing (routing-weight only; never demotes a persona), mitigating post-birth drift toward monoculture.
3. **Learned niche descriptors (`§4I`).** `population-policy/1.niche_descriptor_mode ∈ {fixed_axes, cvt, learned}` (CVT-MAP-Elites / AURORA) plus a mis-calibration detector (`false_collision_rate` / `unfillable_gap_rate` → `niche_recalibration_advisory`), removing operator axis-choice bias and self-correcting the grid.
4. **Enforced cross-kernel boundary (`§4J`).** Cross-kernel `GenesisProposal`s are REFUSED (`cross_kernel_genesis_not_supported_v1_1`) so the per-kernel population ceiling cannot be evaded by minting elsewhere; federated genesis (cross-kernel quorum + federated bound aggregation + replicated provenance) is the specified, deferred v1.1 federation-chapter work.

**Consequences.**
- (+) Three of four SCENARIO 13 residuals resolved or mitigated; the fourth converted from open to specified-but-deferred-and-enforced.
- (+) The founder-effect signal and monoculture defence are now measurable and testable (A-GEN18–A-GEN24).
- (+) `learned` descriptor mode is the most V-aligned (names no domain category).
- (−) Whether continuous maintenance *prevents* (not just mitigates) collapse at N=100/1000 remains the v1.2 empirical study (OQ-POP-6 / OQ-PERSONA-1); detector thresholds need calibration.

**Related.** ADR-0048, ADR-0049, ADR-0019 (evolution machinery), [`13_DESIGN_VALIDATION.md` SCENARIO 13](13_DESIGN_VALIDATION.md).

---

### ADR-0051 — Wall-clock age primary; per-environment conferred standing (LPP); named life-stages removed

**Status:** Accepted.
**Date:** 2026-05-29.
**Origin:** v1.1 (persona model rework).
**Related:** [`02_PERSONA.md §7.2`](02_PERSONA.md), [`05_ENVIRONMENT.md §5.4`](05_ENVIRONMENT.md), [`16_POPULATION_DYNAMICS.md §4D–§4E`](16_POPULATION_DYNAMICS.md), ADR-0019, ADR-0048; Lave & Wenger (LPP); Hornby (ALPS).

**Context.** The v1.0 model conflated distinct concepts. "Age" was defined by an experience counter (`age_tasks`), so a persona that did real work was "old" while one dormant for a year stayed "young"; wall-clock time was explicitly declared *not* a substrate metric. "Maturity" was a single, portable scalar rendered as **named human-life-stage labels** (`newborn / juvenile / adolescent / adult / expert`) that appeared as string literals in schemas (`soul.state.maturity`, `MaturityInheritancePolicy.cap_at_band`, the ALPS band table). This muddled raw experience with social/role standing and baked an anthropomorphic ladder into normative schemas.

**Decision.** Separate the persona into **three orthogonal facets** (`02_PERSONA §7.2`):
1. **Wall-clock age** (`age = now − born_at`) becomes the single primary age — continuous, monotone, never reset, not paused by dormancy. **ALPS layering is re-derived from wall-clock age-bands** (numeric Layer 0..N via `alps-band-policy/1`); its diversity-protection role is unchanged. Experience (`experience_tasks`, renamed from `age_tasks`) is demoted to a competence stat.
2. **Global experiential floor** (`experiential_floor`) — a portable, monotone capability minimum (DGM-style function of experience + fertility) that gates substrate capability minimums **including safety-relevant gates**.
3. **Community standing** — per `(persona, environment)`, **non-portable**, **conferred by the community, never self-awarded** (Lave & Wenger LPP; `05_ENVIRONMENT §5.4`, `community-standing/1` + `standing-endorsement/1`). It gates **relational/collaborative privileges only**; safety-relevant capability stays on the experiential floor + operator/`ReplicationBound`, never reachable by peer quorum. Anti-gaming reuses the existing reputation engine (`09_PROTOCOLS §3D / A.16–A.18`).

The **named life-stage labels are removed**: `juvenile / adolescent / adult / expert` are purged entirely (including schema literals); "newborn" survives only as descriptive prose, never as a gate value. `MaturityInheritancePolicy` → `StandingFloorInheritancePolicy` (caps the portable floor only; standing is never inherited). `soul-state/5` → `soul-state/6`.

**Consequences.**
- (+) A persona's age is simply how long it has existed; experience, capability, and social position are cleanly separable.
- (+) The kernel safety floor is provably out of peer-quorum reach (standing gates relational privileges only).
- (+) Anti-laundering is strengthened: per-env standing is never inherited at all.
- (+) Reuses existing machinery (ALPS, reputation anti-gaming, EnvironmentLineage anchors) — additive.
- (−) `soul-state/6` requires a migration (INV-10; A-MIGRATE-SOUL6-1).
- (−) **Residual R-PERSONA-AGE-1:** a chronologically old but idle persona occupies an upper ALPS band it under-earns; accepted by design (ALPS protects the young, not penalizes the idle) and bounded by fitness decay, not by re-deriving age from activity.
- (−) Wall-clock ALPS band defaults need calibration (OQ-POP-1-style).

**Alternatives rejected.** (a) Keep experience-as-age — rejected: conflates activity with age and mis-protects the idle. (b) Make standing portable across environments — rejected: defeats LPP (standing is earned within a community) and would re-open laundering.

---

## 13. Cross-references

- Normative invariants and commitments referenced above: [`00_VISION.md §3`](00_VISION.md#3-invariants-j1j9), [`00_VISION.md §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10).
- Documentation conventions used in this catalog: [`SPEC_CONVENTIONS.md`](SPEC_CONVENTIONS.md).
- Acceptance tests anchoring these decisions: [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md) (A-J1 … A-J9, A-C1 … A-C4, A-INV-1 … A-INV-10; A-MT* + A-DP* under §9f; A-LH* + A-OR* + A-PD* + A-RT-PERS* + A-PC* + A-LE* + A-RT-RESP* under §9g; A-UB* + A-UM* + A-UF* + A-URR* + A-DD* + A-RRC* + A-OBM* + A-CP* under §9h; A-LSR* + A-LCA* + A-TA* + A-CUR* + A-LP* + A-MASTERY* + A-GPA-ACK* + A-HST* under §9i; A-MPFC* under §9j; A-WK6* + A-CEPO*).
- Companion Living catalog: [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) — scenario walk-throughs whose gap → fix entries surface many of the above decisions in practice.
