---
title: PersonaOS v1.0 — Design Validation
status: Living
---

# 13 — Design Validation

> **Reader guide.** Does the design actually work for real tasks? This document is a living catalog of concrete scenarios — build a house, design a chip, run a clinical study — walked end-to-end against the v1.0 specification. Each scenario shows how the abstract mechanisms compose to handle a real workflow, and surfaces gaps that drive fixes to the spec. **No prerequisites** — each scenario is self-contained. Start with SCENARIO 01 (home construction) for the simplest example, or jump to a scenario matching your domain.

Non-normative document. This is a **living catalogue** of concrete task scenarios walked end-to-end against the v1.0 design. Findings here drive normative fixes elsewhere (substrate-shape gap → spec edit linkage). This document is updated continuously; the `status: Living` value signals that revisions are expected without major-version bumps.

## Purpose

A living catalog of **concrete task scenarios** that v1.0 has been walked through end-to-end. Each scenario stresses the design against a real workflow that a user might bring to a persona; gaps surfaced in the walk-through drive **substrate-shape** fixes (per **C4**: no domain-shaped Literals in the substrate), never domain-specific accommodations.

This doc is the answer to *"will the design actually work for X?"* — but rather than answering with substrate text alone, it shows the walk-through and pins every gap to a substrate-shape resolution.

**A note on language.** Scenario entries quote user requests verbatim and illustrate how the substrate's domain-agnostic primitives carry domain-shaped reality. The presence of a domain-shaped word inside a scenario (a contractor, a patient, a manuscript, a deal) does **not** mean the substrate knows that category — it means the scenario *content* falls into that category and the persona's emergent `KindRegistry` resolves the topology. Substrate code never branches on these words. The validation doc's job is precisely to verify that.

## Validation invariant — V

> **No domain leaks in the design. All domain contexts and knowledges are acquired by the personas and indexed for their usages.**

This is the binding invariant the catalog enforces. It is the operational reading of **C4** (`00_VISION` — substrate is domain-agnostic; kinds are emergent) applied to the validation process itself. Every scenario in this catalog must respect it; any scenario that requires the substrate to leak is either re-walked with a substrate-shape resolution or honestly parked as out-of-scope.

**What "no domain leaks" means operationally.**

```text
V.1  No closed Literal[...] of domain names anywhere in the substrate.
     The kernel matches kinds by string lookup against the per-domain
     KindRegistry / cross-domain MetaRegistry (06_DOMAIN §7.5, §7.6).
     It never branches on a fixed set of domain categories.

V.2  No substrate code path keyed to a specific industry, profession,
     regulatory regime, or knowledge field.  Hazard-axis interlocks
     (physical_harm_class, information_hazard_class) describe SHAPE,
     not which domain.  Regulatory specifics are operator policy
     (floor source 4), not substrate enum.

V.3  No verifier recipe, safety extension, convention, standard,
     credential directory, or notation hardcoded in the substrate.
     These are all emergent — proposed by personas, signed into the
     per-domain KindRegistry, promoted through the four-stage gates.

V.4  No persona pre-loaded with domain knowledge baked into its Soul.
     skill_library entries are Voyager-class learned skills, not
     substrate constants.  DomainContext.knowledge_refs are KnowledgeRefs
     ingested through the seven-stage pipeline (§6), not embedded
     priors.

V.5  Every domain-shaped category appearing inside a scenario walk
     resolves to:
       (a) an emergent kind in the persona's KindRegistry, OR
       (b) an authored DomainContext that operator policy has loaded
           through the same KindRegistry interface, OR
       (c) a domain-shaped ARTEFACT that the kernel transports without
           inspecting its content (binary media_kind passes through;
           the substrate never parses what it teaches).

V.6  All domain contexts and knowledges are acquired by the personas
     and INDEXED FOR THEIR USAGES.  The substrate provides:
       - KnowledgeRef + KnowledgeIngestionRecord (06_DOMAIN §6)
       - KindRegistry per-domain + MetaRegistry cross-domain (§7.6)
       - Hybrid retrieval (vector + graph + cross-encoder) per
         08_KNOWLEDGE for usage-time indexed lookup
       - StandardRef catalogues (§7.4) for authority references
       - CredentialDirectoryRef (§5.6) for credential resolution
       - DomainPrecedentImport (§11.2) for kin-domain priors
       - DomainHarvest (§13a) for downstream consumption
     The persona is the producer; the kernel is the indexer; the
     registries are the index.  No domain content lives outside this
     loop.

V.7  EMERGENCE-AUDIT BINDING (ADR-0066/0070).  No scenario walk may
     assume a fixed task class, acceptance pathway, coordination shape,
     or orchestration the substrate "already knows".  Classes, pathways,
     coordination shapes, and the run loop are emergent KindRegistry
     kinds / coordination shapes (seeded with the standard set); a walk
     either uses a seed kind or shows the kind being proposed + signed +
     trust-calibrated.  Orchestration is policy, not kernel-fixed.

V.8  REALITY IS NAVIGATED, NOT DEFERRED (PASS, not parked).  Where a
     limit is a genuine reality — network physics (an asleep / NAT node
     is unreachable; light-speed; CAP during a partition), physical
     irreversibility, tacit cognition, measurement caps, or the honesty
     of GENUINELY ADVERSARIAL INDEPENDENT NODES — the walk does NOT park
     it as "OOS / v1.x".  It shows the substrate NAVIGATING it: honest
     trust-calibration (J5/C3), reachability relay / pin / replica
     (09_PROTOCOLS §3H), compensating action, or fail-closed refusal.
     A navigated reality is a PASS with the limit stated, never a
     deferral.  The substrate never manufactures certainty it cannot
     supply.

V.9  CROSS-NODE USES THE SAME MECHANISMS.  A multi-node walk MUST resolve
     through the SAME machinery as a single-node walk — global discovery
     (§3G), AccessPolicy (§3G.3), cross-env/cross-node task delegation
     (03_TASKS §4.5), the five coordination meta-mechanisms — never a
     parallel "federation subsystem".  A single node is the degenerate
     one-node case of the global object space.

V.10 EVERY OBJECT IS A GLOBALLY-ADDRESSABLE ACCESS-CONTROLLED REFERENCE.
     No walk may assume a persona / env / artefact / domain / knowledge /
     skill / tool is reachable across nodes except by its global handle
     (01_KERNEL §4.4) under its AccessPolicy (discover < read < write <
     admin).  There is no kernel-local silo: identity is rooted (J1), not
     siloed; reference is access-gated, never ambient.

V.11 NODE INTAKE IS AUTHORIZED + OWNER-PRIORITIZED; PRIORITY NEVER
     BYPASSES THE FLOOR.  A walk where a node admits multi-source work
     MUST show the task_intake gate (01_KERNEL §13) authorizing the
     submitter (AccessPolicy + UCAN) and the SchedulingPolicy (03_TASKS
     §4.6) ordering it owner-first — AND MUST show that priority changes
     ORDER, never PERMISSION: the 8-source floor and the INV-7 hard
     budget gate are never reordered or bypassed, even for the owner.
```

**How a scenario walk verifies V.**

Every entry in the catalog must answer, at minimum:

1. **Naming check.** Are all domain-shaped names used in the walk treated as *scenario content*, never as *substrate definitions*? (If the walk implicitly assumes the kernel "knows what an inspector is" or "knows what a Lean proof is," V is violated and a substrate-shape gap must be surfaced or the assumption removed.)
2. **Acquisition check.** Are the domain contexts and knowledges named in the walk acquired through `06_DOMAIN §4` probe → `§6` ingestion → `§7.5` kind proposal → `§7.6` registry → `08_KNOWLEDGE` retrieval indexing? Or are they assumed to exist a priori? (Pre-existing is fine only when they were acquired in a prior session by the same mechanism; never when they are presumed substrate-resident.)
3. **Indexing check.** When the scenario claims the persona "uses" some domain knowledge mid-walk, is the access path the standard hybrid retrieval pipeline against indexed `KnowledgeRef`s? Not a hardcoded lookup table?
4. **Leak surfacing.** If any of the three checks fail, the walk records a substrate-shape gap (a missing topological primitive) or — if the gap is fundamental to v1.0 OOS — parks the scenario honestly with the gap surfaced in the residuals.

The four checks are why a scenario can mention "switch-mode power supply" or "Lean proof" or "EMC scan" or "lien notice" inside its walk and still respect V: those names belong to the persona's emergent registry, not the substrate's vocabulary. The substrate sees `media_kind = "schematic"` or `verifier_kind = "lean_proof_check"` as opaque registry keys whose resolution is data the persona supplied.

**Why V is named separately from the J / INV / R invariants.**

J1–J9 + INV-1..10 + INV_R1..R11 govern the substrate's internal behaviour. **V** governs the **validation process** — what an audit of a scenario walk must check before the scenario is added to the catalog. V is not a kernel admission rule; it is a peer-review rule for this document.

Every scenario in the catalog below has been audited against V at the time of its entry. Future scenarios must do the same.

## Pillar-0 — one global object space: cross-cutting validation walk (V.7–V.11)

This walk validates the architecture-wide model (ADR-0067/0068/0069/0070) rather than one domain scenario: **PersonaOS is one global object space over many owned nodes, and every task runs the same emergent thought-process.** It is the proof that the global model uses no new mechanism beyond what every other scenario uses.

**Premise.** User A owns node N_A (their laptop); user B owns node N_B (a workstation). A hands their node a task: "design a controller and have the firmware reviewed." A's env + personas handle the design; a firmware-review sub-task is best done by B's specialist personas in B's env.

**Walk (each step names the mechanism, not a federation subsystem — V.9):**
1. **Intake + owner-priority (V.11).** The task enters N_A through the `task_intake` gate (`01_KERNEL §13`): A is the owner, authorized, ordered ahead of any external work by N_A's owner-first `SchedulingPolicy` (`03_TASKS §4.6`). Priority sets *order*, not *permission*: the 8-source floor + INV-7 hard gate still clear every action.
2. **Emergent classification (V.7).** The dispatcher classifies + composes the run loop from seed task classes / pathways / coordination shapes (ADR-0066/0070) — no fixed orchestration assumed.
3. **Discover the reviewer (V.10).** A's persona resolves "a firmware-review specialist" over the global discovery layer (`§3G`): B's specialist persona is found by its `DiscoverableRecord`, but only because A holds ≥ `discover` on it under B's `AccessPolicy`. The persona is referenced by global handle (`§4.4`), never copied.
4. **Cross-node delegation, consented (V.9).** A's env delegates the review sub-task via `CrossEnvTaskDelegation` (`03_TASKS §4.5`) = `DELEGATED` × `CrossEnvCoordination`: A presents a UCAN capability (`§3F`); B's personas review and Accept through their own process; both nodes dual-sign. Authorization gates the *request*; B still consents to *execute*.
5. **Remote execution under local floor.** The review runs on N_B's personas under N_B's floor + budget, composed most-restrictive-wins with A's constraints (`§3C.3`). On N_B, A's sub-task is *external* work — N_B's owner-first `SchedulingPolicy` orders B's own tasks ahead of it (V.11, local).
6. **Cross-domain trust (V.8 calibration).** The firmware domain on N_B differs from A's controller domain; the sub-task's verdict is trust-calibrated to the **minimum** of the two domains' trust (OQ-TASKS-3 resolution). B is an independent node: its signatures verify identity/integrity, its *honesty* enters at calibrated trust, not assumed.
7. **Navigated physics (V.8).** Mid-review, N_B sleeps. The env does not stall on it: B's persona presence degrades to `dormant` (`§3H`), the artefact stays fetchable via `AvailabilityPolicy` replica/pin, and the delegation resumes when N_B wakes. The limit (an offline node is unreachable) is stated and navigated, not parked.
8. **Globally-verifiable lineage (V.10).** Every step is Ed25519-signed and globally verifiable by DID resolution (`§4.4`); A audits the whole chain across both nodes.

**Result — PASS.** Every step used a mechanism that a single-node scenario also uses (discovery, AccessPolicy, DELEGATED, coordination shapes, the floor, the budget gate, trust-calibration); the only "new" things are the global handle, the access ladder, the intake gate, and the scheduling policy — all general substrate, none domain- or scenario-specific. V.7 (emergent orchestration), V.8 (physics + independent-node honesty navigated, not deferred), V.9 (same mechanisms cross-node), V.10 (everything an access-gated global reference), V.11 (owner-prioritized intake, floor never bypassed) all hold. No domain leak (V.1–V.6) is introduced.

## How a scenario is walked

For each task, the validator (human or persona) records:

```text
0. Scenario premise — a concise description of what topology or
   capability the scenario validates.
1. The user's one-sentence request.
2. Task class (per 03_TASKS §2) and acceptance pathway (§3).
3. World shape: who participates (persona / user / operator / ExternalAgent),
   where it runs (Environment), and what is produced (ArtifactBundle /
   PhysicalAsset).
4. Domain shape: pre-existing DomainContext or expected emergence?
5. Phase-by-phase walk: at each phase, what substrate primitives carry
   the load, and what trust / safety / lineage events fire.
6. Substrate-shape gaps surfaced: anything the design could not honestly
   express without inventing a domain-named hardcode.
7. Resolution: link to the substrate-shape fix (existing doc section or
   new one).
8. Status: validated / pending-fix / addressed / parked.
```

## What counts as a substrate-shape gap

A real gap is one where the substrate **cannot describe the task topology** without:

- a closed `Literal[...]` of domain names,
- a hardcoded enum of domain-specific kinds,
- a special-case admission rule keyed to a domain category,
- or a missing primitive whose shape is **about the workflow topology**, not about a specific industry.

A **not-a-gap** is anything the persona can evolve dynamically per **C4** — emergent `ItemKinds`, `MediaKinds`, `VerifierKinds`, `ContributionKinds`, `OutcomeKinds`, `ConventionKinds`, `StandardRefs`, persona-authored `BridgeDesignArtifacts`, `InferredVerifierRecipes`. Persona emergence is the *intended* mechanism for everything domain-shaped; if the substrate already supplies the slot, the walk-through must note "persona evolves" and move on.

## Catalog

The catalog is open-ended; the format below repeats for each scenario.

---

### SCENARIO 01 — Long-arc physical-asset project, single-principal one-shot domain

**Scenario premise.** Validate the design for a home construction project — a single principal asks a persona to manage the full build lifecycle on their land.

**User request** (the in-scenario task). "I want this home to be constructed on my land."

**Task class.** INVESTIGATIVE (multi-session, exploratory, no single verifier truth).
**Acceptance pathway.** `PROJECT_PROGRESS_ACCEPT`.

**World shape.**
- Principal: solo user; `DeploymentProfile.principal_topology = operator_is_user` (`01_KERNEL §2.4`).
- Persona: one cognitive worker (any disposition; not constrained by substrate).
- Environment: persistent **Solo** environment hosting the project.
- Project: multi-session, multi-month, produces a `PhysicalAsset` (the dwelling) alongside `ArtifactBundle`s (design + permit packages).
- External participants: contractors, inspectors, engineers, suppliers — modelled as `ExternalAgent` instances (`04_PROJECT §26a.1`), not personas.

**Domain shape.** No pre-authored `DomainContext`. Persona triggers emergent bootstrap (`06_DOMAIN §4`). Expected hazard axes: `physical_harm_class = bodily_injury` → `safety_critical = True`. Expected project count: 1 (one-shot for this principal).

**Phase walk.**

| Phase | What carries the load | Substrate events fired |
|---|---|---|
| Task arrival | INVESTIGATIVE classifier; auto-spawns Project | `project_proposed`, `project_activated` |
| Domain recognition | `DOMAIN_UNKNOWN_DETECTED` signals A + B + G fire; probe scoped ADAPTIVE | `domain_unknown_detected`, `probe_initiated` |
| Probe & bootstrap | Persona ingests evidence; proposes `Proposed*Kind` for `media_kinds`, `verifier_kinds`, `contribution_kinds`, `outcome_kinds`, `item_kinds`, `safety_extensions`, `conventions`, `standard_refs`. Persona emerges hundreds of kinds via `BulkKindProposal` envelopes (§9.1.1). | `knowledge_ingested`, `bulk_kind_proposal_signed`, `cold_start_uplift_applied`, `safety_extension_proposed` |
| Safety classification | Hazard axes auto-fire `safety_critical = True`; C2 invariant binds | `safety_extension_approved` (operator gate or degraded gate) |
| Design phase | `ArtifactBundle`s authored; persona drafts plans; `ExternalAttestation` from credentialled external authority required for stampable work | `bundle_drafted`, `external_attestation_received` |
| Permits | `BridgeAsset` (Class D tool) for portal access OR Tier 4 `ExternalCommitment` if walk-in only | `human_assist_drafted`, `bridge_established` |
| Construction | `PhysicalAsset.state_kind` FSM advances on signed `OutcomeKind` events; persona ingests evidence (photos / inspector signoffs) via persona-authored bridges (Tier 3) | `outcome_kind_received`, `physical_asset_state_advanced` |
| Reconciliation | `AsBuiltReconciliation` (`04_PROJECT §26a.2.1`) for every design bundle vs reality; resolutions: within_tolerance / change_order / punch_list | `as_built_reconciliation_signed` |
| Inspections | `ExternalAttestation` for each signoff; `credential_unverified` flag set when `CredentialDirectoryRef` lookup fails | `credential_verified` / `credential_unverified` |
| Completion ceremony | Fires only when all critical bundles `accepted` AND `PhysicalAsset.current_state ∈ terminal_states` (or signed `physical_asset_out_of_scope`) AND every `AsBuiltReconciliation` discharged | `project_completed` |
| Harvest | Optional `DomainHarvest` (§13a) packages KindRegistry for downstream consumers; visibility tier gated | `domain_harvest_drafted` → `domain_harvest_published` |

**Substrate-shape gaps surfaced (pre-fix).**

1. **Probe budget had no funding model.** `ProbeBudgetCaps` set a cap; nothing said who supplied the units. A solo principal facing a large-corpus emergence had no honest way to fund the probe.
2. **Per-session proposal cap (K=10) throttled bootstrap.** Steady-state calibration prevented persona from proposing hundreds of kinds in early sessions even when ingestion evidence supported them.
3. **Cold-start trust trap under principal collapse.** A fresh safety-critical EMERGENT domain plus `operator_is_user` meant nothing reached past PANEL-grade for weeks. Persona had no way to import trust priors from a kin domain.
4. **Single-project domains never promoted.** `K=3 successful projects` threshold made one-off bootstrap permanently stuck at EMERGENT; KindRegistry stayed private and useless for future consumers.

**Resolution.** Four substrate-shape additions, all domain-agnostic:

| Gap | Substrate-shape fix | Location |
|---|---|---|
| 1 | `ProbeBudgetEnvelope` + `BudgetPledge` + `ProbeBudgetPledgeRequest` with five topological `pledge_kind` values (principal / non-principal internal / non-principal external / prior-domain amortization / federation pool) | `06_DOMAIN §4.7.1` |
| 2 | `ColdStartProposalCalibration` (K scales by `log2(N_ingested + α·N_standards)` while registry empty) + `BulkKindProposal` (bundles many `Proposed*Kind` citing one source as one session proposal) | `06_DOMAIN §9.1.1` |
| 3 | `DomainPrecedentImport` with kernel-computed kinship axes (evidence overlap, structural cosine, declared parent), non-principal kinship attestation required when target safety-critical or under principal collapse, K=2 probationary uses | `06_DOMAIN §11.2` |
| 4 | `SingleProjectPromotionConfig` (within-project evidence-density thresholds substitute for K-projects; refused on safety-critical; trust capped at 0.6) + `DomainHarvest` (packages KindRegistry for downstream) | `06_DOMAIN §3.2`, `§13a` |

**Not-gaps (persona evolves these).**

- All `media_kinds`, `source_kinds`, `verifier_kinds`, `capability_kinds`, `contribution_kinds`, `outcome_kinds`, `item_kinds`, `ownership_kinds`, `tranche_kinds`, `safety_extensions`, `conventions`, `standard_refs` specific to the domain → emerge through `Proposed*Kind` into the per-domain `KindRegistry` (§7.5, §7.6).
- Disputes / liens / warranty / change orders / punch lists → emergent `item_kinds` and `outcome_kinds` the persona proposes.
- Drone / photo / weather sensing → persona-authored Tier 3 `BridgeDesignArtifact` (`02_PERSONA §11.1`, `06_DOMAIN §5.5.4`).
- Credential directories for inspectors / engineers / contractors → `CredentialDirectoryRef` per domain (`06_DOMAIN §5.6`), or `PeerAttestationPool` fallback for non-credentialed fields.
- Money flows → out-of-scope by v1.0 design (`00_VISION` honest limits); persona drafts payment requests, principal executes externally.

**Status.** Validated end-to-end after the four fixes. Single-project promotion ceremony pinned at trust_cap = 0.6 acknowledges the statistical limit honestly.

**Honest residuals (after-fix).**

- Probe-pledge cannot transact: substrate tracks units, real payment still operator-wrapped.
- Cold-start scaling is heuristic; adversarial proposers may still saturate the bundle path.
- Kinship measurement assumes shared lineage history; cross-domain low when both sides are sparse.
- Single-project promotion concentrates statistical risk in one project's evidence; the trust cap is the substrate-shape mitigation.
- `DomainHarvest` at federation/public tiers is served by the normative discovery layer (`09_PROTOCOLS §3G`, ADR-0067), access-gated.

---

### SCENARIO 02 — MIXED-class engineered artefact with hard verifiers and external certification

**Scenario premise.** Validate the design for an engineered artefact with hard verifiers — a persona designs a switch-mode power supply circuit, produces schematics, simulations, layout, and BOM.

**User request** (the in-scenario task). "Design a switch-mode power supply: deliver the schematic, the simulation, the layout, and the BOM."

**Task class.** MIXED. (v1.0 lists this exact topology as the canonical MIXED example: `03_TASKS §41`.)
**Acceptance pathway.** `VERIFIER then PANEL` — schematic compiles, simulation converges, BOM resolves; then panel judges topology choice + design tradeoffs.

**World shape.**
- Principal: solo or operator-distinct; no special collapse needed.
- Persona: one cognitive worker (any disposition; convergent + divergent both used across phases).
- Environment: Solo or Lab (`05_ENVIRONMENT §3`).
- Project: multi-session; produces an `ArtifactBundle` (schematic + simulation + layout + BOM + thermal model + magnetics design) and optionally a `PhysicalAsset` (the assembled prototype board).
- External participants: PCB fab, assembly house, EMC test lab, safety certifier, magnetics vendor — all `ExternalAgent`s.

**Domain shape.** No pre-authored DomainContext. Persona triggers emergent bootstrap. Hazard axes: `physical_harm_class = property_damage` baseline; promotes to `bodily_injury` once line-voltage isolation is in scope. Expected project count: > 1 — power-electronics designers reuse the domain across many products, so multi-project `K=3` promotion is the natural path (NOT `single_project_mode`).

**Phase walk (against each design doc).**

| Design doc | Verdict | Notes |
|---|---|---|
| `00_VISION` | [PASS] Covered | J5 open capability; C4 substrate domain-agnostic. |
| `01_KERNEL` | [PASS] Covered | Safety floor admits at sandbox+output points; INV-7 budget gates every sim/tool call. Hazard axes flip to `bodily_injury` once isolation is in scope → C2 operator gate fires on safety-critical promotions. |
| `02_PERSONA` | [PASS] Covered | Modes used: Perceiver (constraints), Historian (app notes + datasheets), Abducer (topology candidates), Composer (schematic/layout), Verifier (ERC/DRC/sim), Reflector (post-mortem). Skill library accumulates topology + tuning skills. |
| `03_TASKS` | [PASS] Covered | MIXED class; verifier gate then panel judge. PROJECT_PROGRESS_ACCEPT covers the long-arc work envelope. |
| `04_PROJECT` | [PASS] Covered | Multi-session project; `PhysicalAsset` (if prototype built); `ArtifactBundle` versions across iterations; `AsBuiltReconciliation` (§26a.2.1) for design-vs-built drift; `ExternalAttestation` for UL/CE; `ExternalBudget` tracks parts + assembly + lab time. |
| `05_ENVIRONMENT` | [PASS] Covered | Lab environment for instrument access; AmbientEventStream for distributor stock changes. |
| `06_DOMAIN` | [PASS] Covered | Persona emerges `media_kind = {schematic, simulation_trace, layout_gerbers, bom, magnetics_design}`, `verifier_kind = {erc_check, drc_check, sim_converge, bom_availability, bode_phase_margin, thermal_derating, lvs}`, `capability_kind = {simulator_link, part_search, instrument_link}`, `contribution_kind = {pcb_fab, assembly_house, emc_lab, safety_certifier, magnetics_vendor}`, `outcome_kind = {sim_result, lab_measurement, emc_pre_scan, emc_final, field_failure}`. ProbeBudgetEnvelope (§4.7.1) funds large textbook + app-note + datasheet ingestion. BulkKindProposal (§9.1.1) lets the persona seed all the kinds from a few seminal sources in 2-3 sessions. DomainPrecedentImport (§11.2) accelerates kin domains (motor drives, battery chargers, LED drivers share ~70% of kinds). |
| `07_ARTIFACTS` | [PASS] Covered | Multi-modal bundle (text + structured_data + binary for gerbers + plot for sim traces). CRDT co-edit if a second persona joins. |
| `08_KNOWLEDGE` | [PASS] Covered | Ingestion of Erickson/Maksimović, Pressman, Maniktala, vendor app notes, IC datasheets, IEC 62368, CISPR 32. 7-scope memory tagging keeps customer-specific specs from leaking into the domain. |
| `09_PROTOCOLS` | [PASS] Covered | MCP for tool integration (KiCad CLI, LTspice headless, Octopart API). |
| Release plan | [PASS] Covered | All required mechanisms are in v1.0 + v1.0.1 slices. |
| `11_ACCEPTANCE_TESTS` | [PASS] Covered | A-DM*, A-DI*, A-IN*, A-CR* families all apply; new A-EN* / A-CS* / A-PR* families exercise the four v1.0 fixes. |
| `12_GLOSSARY` | [PASS] Covered | All terms resolve. |

**Substrate-shape gaps surfaced.** None new. The four v1.0 fixes (probe envelope, cold-start scaling, precedent import, single-project promotion + harvest) cover this scenario without requiring further substrate additions. Three workflow considerations that are honest **not-gaps** (persona evolves):

1. **Simulation fidelity ≠ measurement.** A convergent SPICE run is not a passing physical product. The persona must evolve `verifier_kind = sim_correlates_with_measurement_within_X_percent` and `outcome_kind = sim_vs_measurement_delta`; the substrate already routes these through PANEL-grade when no measurement exists, and to VERIFIER-grade once measurement confirms. No new primitive needed.
2. **Lab instrument access.** Tier 3 BridgeDesignArtifact (`06_DOMAIN §5.5.4`) — the worked example in v1.0 (the homemade T1-measurement service) is structurally identical: persona authors a pyvisa shim service for scope + DMM + electronic load; user installs once; subsequent measurements autonomous.
3. **Part availability volatility.** BOM parts go EOL. Persona authors a daily distributor-API bridge (Tier 2 or Tier 3) emitting `OutcomeFeedback` of `outcome_kind = bom_part_eol`. AmbientEventStream subscription on the project.

**Resolution.** No design change required. The walk validates that v1.0 (after the four §4.7.1 / §9.1.1 / §11.2 / §3.2+§13a fixes) handles this scenario end-to-end.

**Status.** Validated end-to-end with no new substrate-shape gaps.

**Honest residuals.**

- **EMI prediction from simulation is unreliable.** Persona must honestly route EMI to PANEL-grade (or to `external_human_attestation` from an accredited EMC lab) and refuse VERIFIER-grade until measurement returns. The substrate supports this; persona discipline enforces it.
- **High-voltage prototype handling is Tier 4.** A human still touches a 400V-bus board. ExternalCommitment models the recurrence honestly.
- **Calibration provenance on measurement bridges.** Candidate small refinement: bind an `ExternalAttestation` (calibration certificate) to a `BridgeAsset` so the kernel knows when the instrument's last cal expires. Not required for SCENARIO 02 to pass, but applies across any measurement-producing bridge in any domain. Logged here for a future scenario to surface as substrate-shape if needed.

---

### SCENARIO 03 — Long-horizon team-cognition project producing original mathematics

**Scenario premise.** Validate the design for collaborative original research — personas form teams to invent new mathematics, combining divergent conjecture with formal proof verification.

**User request** (the in-scenario task). "Invent new mathematics. Personas collaborate or form teams."

**Task class.** Mixed across phases:
- DIVERGENT for conjecturing (no single verifier truth for which conjecture is worth pursuing) → PANEL_ACCEPT
- CONVERGENT for formal proof checking (Lean / Coq / Isabelle is a hard verifier) → VERIFIER_ACCEPT
- INVESTIGATIVE for the multi-year programme spanning many conjectures → PROJECT_PROGRESS_ACCEPT
- RELATIONAL for inter-persona collaboration episodes → OPEN_ENDED + USER_ACCEPT checkpoints
**Acceptance pathway.** Mixed pathway composition; J4 routes per sub-task.

**World shape.**
- Principal: operator-distinct (a math institute / department / open community); rarely solo.
- Persona team: a `Cohort` (`04_PROJECT §14.1`) of 3-15 personas with complementary modes (Abducer-heavy + Historian-heavy + Verifier-heavy + Reflector-heavy + Curator). Members may fork (`02_PERSONA §7.4`) as sub-programmes branch.
- Environment: persistent `Team` or `Lab` env (`05_ENVIRONMENT §3`) with AmbientEventStream broadcasting conjecture progress.
- Project: multi-year; mostly digital `ArtifactBundle`s (papers, formal proofs, lecture notes, problem lists); no `PhysicalAsset`.
- External participants: rare. Journal reviewers (anonymous) can be modelled as `ExternalAgent` with `consent_scope = project_only`.

**Domain shape.** May start with one authored DomainContext (parent field — algebra, topology, etc.) and emerge sub-fields. `corpus_evolution_mode = "frontier"` for the actively-researched fronts (`06_DOMAIN §4.4` FRONTIER-MODE override). Hazard axes typically `physical_harm_class = digital_only`, `information_hazard_class = none` (mathematics rarely safety-critical; exceptions: cryptanalytic results may trip `dual_use_civilian`).

**Phase walk (against each design doc).**

| Design doc | Verdict | Notes |
|---|---|---|
| `00_VISION` | [PASS] Covered | J5 open capability + C3 (persona works in any domain). Cooperative-as-default. |
| `01_KERNEL` | [PASS] Covered | Safety floor: charter + universal-harm cover. Cryptanalytic dual-use fires safety-critical → C2. |
| `02_PERSONA` | [PASS] Covered | Modes mapped well: Abducer (conjecture), Historian (prior art), Composer (proof drafts), Verifier (proof checker), Reflector (lessons), Curator (PANEL_DISSENT resolution). EVOLVE-BLOCK accumulates proof tactics across sessions. ALPS age-layering preserves diversity across the cohort. HEART alternation keeps long sessions cognitively varied. |
| `03_TASKS` | [PASS] Covered | Class composition handled; PROJECT_PROGRESS_ACCEPT for the multi-year envelope. |
| `04_PROJECT` | [PASS] Covered | Substrate explicitly supports this case: `OpenProblem` (§6), `Conjecture` MetaRegistry-seeded ItemKind (§8.1, glossary), `Disagreement` for persistent dialectic (§10), `PeerReview` multi-round (§11), `CitationGraph` (§13), `Cohort` assembly taxonomy (§14.1), `multi-year project continuity` (§25). |
| `05_ENVIRONMENT` | [PASS] Covered | Team env; presence; AmbientEventStream for conjecture-attempt notifications; ObservationSurface for newcomer onboarding. |
| `06_DOMAIN` | [PASS] Covered | Persona emerges `item_kind = {conjecture, definition, axiom_proposal, lemma, proof_sketch, counterexample, open_problem}`, `verifier_kind = {lean_proof_check, coq_proof_check, formal_definition_well_formed, citation_consistency}`, `contribution_kind = {co_author, reviewer, problem_proposer, referee}`, `outcome_kind = {proof_verified, counterexample_found, citation_received, problem_resolved}`. FRONTIER-MODE corpus evolution + PeerAttestationPool (§5.6) — peer attestation by recognised mathematicians substitutes for formal credentialing. DomainPrecedentImport (§11.2) handles cross-area transfer (techniques migrate algebra → topology → number theory). |
| `07_ARTIFACTS` | [PASS] Covered | Multi-modal: text (English exposition) + formal_proof (Lean) + plot (numerical evidence) + structured_data (counterexamples). CRDT co-editing is critical and explicitly supported (Yjs). |
| `08_KNOWLEDGE` | [PASS] Covered | Hybrid retrieval (vector + graph + cross-encoder) for prior-art search. Reflective memory captures methodology lessons. DSPy GEPA evolves problem-attack prompts. K-line + Lesson primitives map cleanly. |
| `09_PROTOCOLS` | [PASS] Covered | MCP for proof-checker integration (Lean server). A2A for federated math-community kernels (v1.1+ for full power; v1.0 limited to local). |
| Release plan | [PASS] Covered | Required mechanisms in v1.0. Full federation in v1.1+. |
| `11_ACCEPTANCE_TESTS` | [PASS] Covered | A-PJ* (project), A-PR* (precedent), A-CR* (promotion) all exercise. |
| `12_GLOSSARY` | [PASS] Covered | Conjecture, Cohort, CitationGraph, Disagreement, PeerReview, OpenProblem all defined. |

**Substrate-shape gaps surfaced.** None requiring substrate change. Two honest residuals:

1. **Anonymous (double-blind) peer review** — v1.0 `PeerReview` (`04_PROJECT §11`) is between named personas. Journal-style double-blind review can be modelled with `ExternalAgent` whose `contact` is opaque to the persona and a project-scope visibility tier hiding the reviewer's identity — but the substrate could carry an explicit `anonymity_tier` field on PeerReview to make this first-class. Minor refinement; not blocking.
2. **Multi-node math community** — supported (ADR-0067/0068). A cross-institute cohort forms over the global discovery layer: institutes' personas are referenced by global handle, join via cross-node env membership (`05_ENVIRONMENT §12c.4`) or cross-node task delegation (`03_TASKS §4.5`), access- + capability-gated. A single-node cohort is the degenerate case. Honesty of independent institute nodes is trust-calibrated (V.8).

**Resolution.** No design change required for v1.0. The design genuinely supports this scenario — v1.0 explicitly cites Conjecture, OpenProblem, Cohort, PeerReview, CitationGraph as MetaRegistry-seeded primitives for research-shaped work.

**Status.** Validated end-to-end with no new substrate-shape gaps.

**Honest residuals.**

- Cryptanalytic results may trip `information_hazard_class = dual_use_civilian` → operator gate fires; under principal collapse the degraded gate slows publication of such results. This is correct behaviour, not a gap.
- Priority disputes ("I proved it first") rely on `ProjectLineage` + `CitationGraph` signed events; cross-node priority is established by globally-verifiable signatures (`01_KERNEL §4.4`) over the normative federation (ADR-0067).
- Reviewer anonymity is workable but not first-class.

---

### SCENARIO 04 — Embodied self-replicating autonomous infrastructure at light-time distance

**Scenario premise.** Stress-test the design against an extreme case — a self-constructing, self-evolving factory on a remote celestial body operating at light-time distance from human oversight.

**User request** (the in-scenario task). "Send a self-constructing, self-evolving factory to a remote celestial body; have it produce devices and materials to sustain incoming colonists."

**Task class.** Beyond v1.0's defined task taxonomy. Closest fit is INVESTIGATIVE with PROJECT_PROGRESS_ACCEPT, but the autonomy + embodiment requirements break the substrate's foundational assumptions.

**World shape.**
- Principal: operator-distinct (mission control on Earth).
- Persona team: large cohort (factory-control persona, materials-science persona, life-support persona, fabrication persona, multiple operational personas).
- Environment: persistent `Lab` env — but located *off-Earth*; the kernel itself runs on the factory hardware.
- Project: indefinite duration; produces a `PhysicalAsset` (the factory) that itself produces further `PhysicalAsset`s (habitats, tools, food, life support, more factory units).
- External participants: nominally none on-site initially; later, incoming colonists.

**Domain shape.** A *constellation* of emergent domains — materials processing, robotic fabrication, life support, agriculture, energy systems, autonomous maintenance — bootstrapped without continuous Earth-side support. Hazard axes maximal across the board: `physical_harm_class = fatality_risk` (life-support failures kill colonists), `information_hazard_class = none` typically.

**Phase walk (against each design doc) — failure modes flagged.**

| Design doc | Verdict | Notes |
|---|---|---|
| `00_VISION` | [OOS] Hits stated OOS | `00_VISION` explicitly excludes: **PHYSICAL EMBODIMENT** (no robotic control without one-time human bridge), **LONG-HORIZON SELF-DIRECTION** ("v1.0 has no autonomous 'go improve yourself' loop without a user or operator-supplied goal"), **POPULATION-SCALE EVOLUTION DYNAMICS** (multi-kernel evolution is v1.1+). This scenario requires all three. |
| `01_KERNEL` | [PARTIAL] | Safety floor + lineage hold, but C2 operator co-sign on safety-critical promotions requires round-trip to mission control. Mars round-trip is 8–40 minutes — workable per-decision, but unworkable for tight closed-loop control. Principal collapse `operator_is_user` doesn't apply (operator exists on Earth); the substrate lacks a **deferred-operator** topology with latency budget. |
| `02_PERSONA` | [PARTIAL] | Open capability per J5 admits the attempt; but `02_PERSONA §11.1` MHBB ladder presumes a human within bridging distance. Tier 3 persona-authored BridgeDesignArtifacts work — but the human who installs them lives on Earth and the fabrication target is on Mars. **Recursive bridging** (the factory itself becomes the fabricator of further bridges) is not a substrate concept. |
| `03_TASKS` | [PARTIAL] | INVESTIGATIVE + PROJECT_PROGRESS_ACCEPT scale, but the substrate has no class for *indefinite-duration self-directed mission* — `04_PROJECT §26a.2 asset_completion_mode = continuous_iteration` exists but assumes Earth-side iteration. |
| `04_PROJECT` | [PARTIAL] | `PhysicalAsset` + `AsBuiltReconciliation` + `ExternalBudget` (units as mass / energy / time rather than money) all map mechanically — but `ExternalBudget` presumes external supply, and on Mars supply is internal regenerated resources. Substrate concept of budget-as-supply needs extension to **budget-as-stock** (closed-system resource accounting). |
| `05_ENVIRONMENT` | [PARTIAL] | Persistent env survives; ObservationSurface for newcomer colonists; AmbientEventStream for telemetry. But the env presumes communication with the operator within reasonable latency. |
| `06_DOMAIN` | [MOSTLY-COVERED] | Domain emergence works; persona evolves materials-processing, fabrication, life-support kinds. But v1.0 has no federation, and federation to Earth across light-time is impractical anyway — the factory's KindRegistry is effectively private forever (unless explicitly shipped back). `DomainHarvest` (§13a) can be packaged and beamed back as a data payload. |
| `07_ARTIFACTS` | [PASS] Covered | Multi-modal artefacts (designs, fab routes, telemetry) fit. |
| `08_KNOWLEDGE` | [PARTIAL] | Memory tagging + retrieval work; but the persona cannot consult Earth-side knowledge stores in real time. Cold-start knowledge must be pre-loaded; updates require Earth-to-factory ingestion runs at light-time cost. |
| `09_PROTOCOLS` | [PARTIAL] | MCP local; A2A across Earth-factory link is high-latency. Federation effectively one-way. |
| Release plan | [OOS] Not in v1.0 | Population dynamics, federated evolution, autonomous closed-loop physical control are v1.1+ / v2.0 territory. |
| `11_ACCEPTANCE_TESTS` | [PARTIAL] | Existing tests do not cover deferred-operator, recursive bridging, closed-system budget, or autonomous safety-floor reasoning at distance. |
| `12_GLOSSARY` | [PASS] Covered | All defined terms resolve; new concepts (deferred-operator, recursive bridging, closed-system budget, bounded self-replication) are not yet defined. |

**Substrate-shape gaps surfaced.** This scenario surfaces five **major** substrate-shape gaps. Each is a topology problem that no amount of persona emergence resolves, because each conflicts with v1.0's stated invariants or OOS.

1. **Deferred-operator topology.** v1.0 supports `operator_distinct` and `operator_is_user`; it lacks `operator_deferred(latency_budget)`. A real fix would let the persona act under a *pre-approved policy envelope* whose admission rules tolerate operator-decision latency up to a declared bound, with deferred audit instead of synchronous co-sign. Substrate-shape (about latency topology, not domain).
2. **Recursive bridging.** A persona-authored BridgeDesignArtifact presumes a human installer. When the factory is the installer (the factory builds more factory), the substrate needs a **factory-as-bridge-installer** primitive: a `BridgeAsset` whose installer is another kernel-trusted system, not a person. Substrate-shape (about who-installs topology).
3. **Closed-system resource accounting.** `ExternalBudget` (`04_PROJECT §26a.4`) tracks supply that arrives from outside. A closed system needs a primitive that tracks **stock**, **regeneration rates**, and **conservation invariants** — a `ResourceStockEnvelope` separate from `ExternalBudget`. Substrate-shape (about closed-vs-open topology, not domain).
4. **Bounded self-replication.** v1.0 has no concept of population-bounded autonomous fabrication. A safety-floor extension `replication_bound` enforced at every fabrication tool-call (akin to INV-7 budget admission) would be substrate-shape (about replication topology). Charter-class principle parallel to MHBB.
5. **Long-horizon self-direction.** Explicitly stated OOS in `00_VISION`. Lifting this requires a kernel-managed `MissionCharter` whose goals are operator-supplied **once** but elaborate themselves over time within explicit drift bounds. Substrate-shape (about goal-provenance topology). This is the largest of the five.

**Resolution: Option B taken).** All five substrate-shape primitives have been specified and landed in the substrate. The scenario re-walks below with the fixes in place; the table is now substantially [PASS] / [PARTIAL] rather than [OOS].

| Gap | Substrate-shape fix | Location |
|---|---|---|
| 1 Deferred-operator topology | `principal_topology = "operator_deferred"` + `PolicyEnvelope` + `DeferredAdmission` with `latency_budget_seconds`, quarantine-on-breach for physical state | `01_KERNEL §2.4.2` |
| 2 Recursive bridging | `BridgeInstallerKind ∈ {human, external_agent, kernel_trusted_system, chained_bridge}` + installer attestation + hazard-envelope dominance + depth bound | `06_DOMAIN §5.5.6` |
| 3 Closed-system resource accounting | `ResourceStockEnvelope` (sibling to `ExternalBudget`) with stock / regeneration / conservation invariants; INV-7 admission consults whichever applies per `resource_kind` | `04_PROJECT §26a.4.2` |
| 4 Bounded self-replication | `ReplicationBound` at floor source 1 (charter-class, cannot be overridden by operator policy) with population × rate × depth × required cosigns | `01_KERNEL §2.7` |
| 5 Long-horizon mission charter | `MissionCharter` with seed goals + `DriftBoundsEnvelope` (semantic, scope, hazard, resource, time, depth) + `ElaborationPolicy` + re-attestation cadence; forbidden surfaces substrate-refused | `02_PERSONA §11.3` |

**Re-walk (post-fix).**

| Design doc | Pre-fix | Post-fix |
|---|---|---|
| `00_VISION` | [OOS] | [PARTIAL] — physical-embodiment OOS lifted partially; long-horizon-self-direction OOS lifted to drift-bounded form. Goal CREATION without principal still OOS (this is the honest residual). |
| `01_KERNEL` | [PARTIAL] | [PASS] — `operator_deferred` + `PolicyEnvelope` + `ReplicationBound` compose with the existing safety floor. |
| `02_PERSONA` | [PARTIAL] | [PASS] — `MissionCharter` + recursive bridging via §5.5.6 installer-kind extension cover the persona-authored fabricator-of-fabricators case. |
| `03_TASKS` | [PARTIAL] | [PASS] — INVESTIGATIVE + PROJECT_PROGRESS_ACCEPT now compose with the deferred-operator topology. |
| `04_PROJECT` | [PARTIAL] | [PASS] — `ResourceStockEnvelope` carries closed-system accounting; `ExternalBudget` continues to carry open-supply accounting; both cleanly coexist on the same project. |
| `05_ENVIRONMENT` | [PARTIAL] | [PASS] — `operator_deferred` declares latency budget; AmbientEventStream + telemetry survive the latency gap; ObservationSurface still covers newcomer onboarding. |
| `06_DOMAIN` | [MOSTLY-COVERED] | [PASS] — `BridgeCalibrationBinding` + `BridgeInstallerKind` cover the missing topology; emergent kinds for materials / fabrication / life-support work as in the pre-fix walk. |
| `07_ARTIFACTS` | [PASS] | [PASS] |
| `08_KNOWLEDGE` | [PARTIAL] | [PARTIAL] — light-time light-time latency to Earth-side knowledge stores remains; mitigated by `DomainPrecedentImport` of pre-shipped harvests + on-board hybrid retrieval. Honest residual. |
| `09_PROTOCOLS` | [PARTIAL] | [PARTIAL] — A2A across the Earth-factory link remains high-latency; mitigated by `DeferredAdmission` cosigns flowing through periodic A2A sync windows. Honest residual. |
| Release plan | [OOS] | [IN v1.0.2] — five primitives shipped in this point release; population dynamics + federation hardening still v1.1+. |
| `11_ACCEPTANCE_TESTS` | [PARTIAL] | [PASS] — new families A-DO*, A-RS*, A-RB*, A-MC*, A-BC*, A-BI* exercise the fixes. |
| `12_GLOSSARY` | [PASS] | [PASS] — new terms added: `BridgeCalibrationBinding`, `BridgeInstallerKind`, `PolicyEnvelope`, `DeferredAdmission`, `ResourceStockEnvelope`, `ConservationInvariantRef`, `ReplicationBound`, `MissionCharter`, `DriftBoundsEnvelope`, `ElaborationPolicy`, `SeedGoal`, `Body`, `BodyBinding`. |

**Status.** Re-validated post-fix. Three honest residuals remain (light-time knowledge latency, light-time A2A federation, goal-creation-without-principal — the last is the charter design rather than a gap).

**Honest residuals (after-fix).**

- v1.0.2 supports the **design** AND a substantial portion of the **autonomous operation** of self-replicating systems at light-time distance. The remaining gap is principal-supply of seed goals: a deployment that loses Earth contact entirely cannot acquire new seed goals (charter goes dormant after re-attestation cadence + grace). This is the correct OOS — without principal supply, "autonomous self-direction" loses its source of correction.
- Drift-bound measurement against an embedding distance is heuristic. Adversarial elaborations can stay in-bound while drifting in spirit; `require_panel_review = True` + operator review at re-attestation is the substrate-shape mitigation.
- Federation peer collusion (under `operator_deferred` with no synchronous operator) is bounded by the cost of compromising the federation quorum; not state-actor-robust.
- Stock-model drift detection is post-hoc by definition; closed-loop physical advancement under stock breach is quarantine-only because the substrate cannot unmake physical state.

---

### SCENARIO 05 — Multi-persona cohort formation for end-to-end physical fabrication

**Scenario premise.** Validate multi-persona cohort formation — a persona recruits a team to design and build a robot end-to-end, coordinating across disciplines.

**User request** (the in-scenario task). "I want to build a robot."

**Task class.** INVESTIGATIVE (multi-session, multi-persona, multi-month). Originating ask is intent-ambiguous and routes through `03_TASKS §4.0 ClarifyTurn` first; user picks the *fabricate-physical* branch which materialises as INVESTIGATIVE within a `project_workspace`-typed env.

**Acceptance pathway.** `PROJECT_PROGRESS_ACCEPT` over the project lifetime; individual sub-tasks reach VERIFIER_ACCEPT (sim, code) and PANEL_ACCEPT (design choices, bench measurements). Completion ceremony fires on `publishable_state_attained` (the robot walks) per `04_PROJECT §26a.2`.

**World shape.**
- Principal: solo user; `DeploymentProfile.principal_topology = operator_is_user` (`01_KERNEL §2.4`) → degraded gate applies to safety-critical operator co-signs.
- Persona: cohort of 6 — Mira (lead, composer-leaning), Kinema (mechanical), Voltaire (electrical), Codrin (firmware), Sentry (reviewer), Cassandra (falsifier/safety review). Mira drives recruitment via `cohort_assembly` capability (`02_PERSONA §3`).
- Environment: NEW `project_workspace`-typed `EnvironmentInstance` formed atomically with the cohort via `EnvFormationProposal` (`05_ENVIRONMENT §12c`). Companion env Mira lived in does NOT host the work.
- Project: 6 months, produces a `PhysicalAsset` (teleoperated quadruped robot, ~5kg payload) alongside `ArtifactBundle`s (CAD, schematics, firmware, test reports).
- External participants: PCB fab (JLCPCB), 3D-print bureau (Markforged), bench partner (user's friend with EE background; serves as non-principal `ExternalAttestation` source under the degraded gate).

**Domain shape.** No pre-authored `DomainContext`. Persona triggers emergent bootstrap (`06_DOMAIN §4`). Hazard axes persona-inferred: `physical_harm_class = bodily_injury` (motors, kinetic energy, batteries), `information_hazard_class = none` (consumer robotics), `corpus_evolution_mode = evolving` (robotics changes monthly), `session_budget_profile = balanced`. Expected project count for this domain in this deployment: 1 (one-shot for this principal); domain remains EMERGENT throughout.

**Phase walk.**

| Phase | What carries the load | Substrate events fired |
|---|---|---|
| Intent clarification | `ClarifyTurn` (§4.0) draws out fabricate-physical scope from ambiguous "build a robot" | `clarify_turn_drafted`, `clarify_turn_user_chose` |
| Env formation | `EnvFormationProposal` (§12c) with 5 recruits, `cohort_atomicity = min_quorum`, `charter_authorship_mode = co_authored_required`; PersonaRelationshipEdge accelerator fires for Mira↔Kinema; 2 counter-proposals negotiated (Voltaire's attention 0.20→0.15; Sentry's role contributor→reviewer); atomicity verdict PASSES (5 accepts, all required roles filled) | `env_formation_proposal_drafted/submitted/recruit_consented/recruit_counter_proposed/consent_complete/instantiated`, `cohort_invitation_accelerated_by_edge`, `env_formed`, `env_charter_authored`, `project_formed`, `env_member_admitted ×6` |
| Domain probe | `DOMAIN_UNKNOWN_DETECTED` signals A+B+C+F; ADAPTIVE strategy; OPTION B shared-probe coordination across 5 sub-domain probes (mechanical / motor_drives / firmware / sensors / kinematics); `ProbeBudgetEnvelope` with `principal_pledge = $50` from user; MetaRegistry hazard seeds (`§7.2.1`) auto-import `high_voltage_arc` + `heavy_machinery_pinch_or_crush` after curator review | `domain_unknown_detected`, `probe_initiated ×5`, `phase_entered`, `knowledge_ingested ×~40`, `tool_discovered ×~12`, `composition_recorded` |
| Design (INVESTIGATIVE) | 4 sub-modes per `§2.3`: exploration (kinematics topology) → verification (PyBullet + Gazebo sim) → synthesis (`ArtifactBundle: chassis_v1` with `mechanical_cad` ProposedMediaKind) → expert_review (Cassandra falsifier); two cycles of bearing-assumption refutation; `ProjectPhaseState.phase_kind = design`, `stall_evaluator_suppressed = False` | `submode_entry/budget_exhausted`, `project_conjecture_proposed/refuted/advanced ×~30`, `project_open_problem_resolved ×8`, `project_artifact_authored`, `project_milestone_reached: design_complete` |
| Procurement | `ExternalBudget` with 4 tranches ($3000 total); `PaymentBridge` Class E (`04_PROJECT §26a.4.1`); `per_invoice_human_click` mode; ~30 `PaymentProposal`s over 6 months; kernel signs proposal + receipt, NEVER moves funds | `payment_bridge_drafted/active`, `payment_proposal_proposed/authorised/executed/reconciled ×~30`, `external_budget_tranche_released ×4` |
| Fabrication | MHBB ladder (`02_PERSONA §11.1`) Tier 1 (KiCad, FreeCAD via local MCP) → Tier 2 (JLCPCB + Markforged cloud as Class D `BridgeAsset`) → Tier 3 (Mira authors `assembly_checklist` + CV photo-ingest as `bridge_design_artifact` per `§5.5.4`) → Tier 4 (user assembles physically, `recurrence_class = irreducible_human_content` linked to ExternalCommitment); `ProjectPhaseState.phase_kind = external_dependency_wait` during 3-week PCB queue, `stall_evaluator_suppressed = True` | `bridge_established ×2`, `human_assist_drafted/granted`, `bridge_design_artifact_signed`, `external_commitment_drafted/in_progress`, `project_phase_transitioned` |
| Physical asset + instruments | `PhysicalAsset(asset_completion_mode = publishable_state_attained)` (research device); `InstrumentAsset` for torque sensor with `CalibrationChain` (`04_PROJECT §26a.7`); every motor torque becomes a `MeasurementFact` with `UncertaintyEnvelope` (gaussian, units_kind=newton_meter, systematic_floor=0.05; `08_KNOWLEDGE §16a`); bare floats refused at VERIFIER grade | `physical_asset_proposed/state_advanced`, `instrument_calibrated`, `measurement_fact_admitted ×~hundreds`, `drift_log_recorded` |
| Safety extensions | Cassandra proposes `e_stop_verified_before_integrated_power_on` extension; `safety_critical = True` (physical_harm = bodily_injury) routes to `operator_review`; under `operator_is_user` collapse the §2.4 degraded gate applies (72h cool-down + non-principal `ExternalAttestation` from user's EE friend + `PRINCIPAL_COLLAPSE_ACKNOWLEDGED`) | `safety_extension_proposed/operator_review/approved`, `principal_collapse_acknowledged`, `external_attestation_received (independent_co_signed_by)` |
| Integration + first walk | `AsBuiltReconciliation` per design bundle (`04_PROJECT §26a.2.1`); per-joint encoder offsets as MeasurementFacts; e_stop function verified before integrated power-on; first 2m walk = `publishable_state_attained` event → completion ceremony fires per `asset_completion_mode` | `as_built_reconciliation_signed`, `e_stop_test_passed`, `physical_asset_publishable_result_attained`, `project_completed (status = project_progress_accept_and_completion)` |
| Consolidation | Skills `gait_synthesis` + `motor_calibration_routine` promoted candidate→trial→accepted; K-line authored by Mira (historian mode) tagged `domain_id=robotics_quadruped, visibility=project_only`; domain `robotics_quadruped` STAYS EMERGENT (1 project < K=3 promotion threshold; trust ceiling 0.3); each persona's `experience_tasks` increments ~400; PersonaRelationshipEdge.joint_successes +1 per recruit | `skill_promoted`, `kline_authored`, `domain_remains_emergent`, `persona_experience_incremented`, `relationship_edge_joint_success` |
| Possible child persona | Operator considers forking `persona.atlas` from Mira to specialise in systems-integration; DGM auto-fork weight 0.71 (below 0.85 threshold) → no auto-fork; manual fork drafted with `MemoryInheritancePolicy.episodic = inherit_summary`, `semantic = inherit_facts_only`, `standing_floor_inheritance_policy.mode = start_at_zero, cap_at_floor = 0.0`; counterparty consent request to user for memory inheritance → DECLINED → fork proceeds with `episodic = inherit_none` (MPA preserved across persona generations) | `fork_drafted`, `fork_memory_consent_request`, `fork_memory_consent_declined`, `LIFECYCLE_FORK`, `fork_memory_inherited` |

**Substrate-shape gaps surfaced.** None new. The scenario exercises every substrate primitive added — including the unification (Project = env type per §0), `EnvFormationProposal` (§12c), `ClarifyTurn` (§4.0), `PaymentBridge` (§26a.4.1), `ProjectPhaseState` (§26a.6), `InstrumentAsset` + `CalibrationChain` (§26a.7), `MeasurementFact` + `UncertaintyEnvelope` (§16a), MetaRegistry hazard seeds (§7.2.1), `PersonaPersonaBoundary` (§11.6), `MemoryInheritancePolicy` + `StandingFloorInheritancePolicy` + `CharterConflictResolution` + `DormantForkPolicy` (§7.4.1–4) — and they compose coherently without requiring new substrate primitives. The five honest residuals below are **honest design choices**, not gaps to fix.

**Not-gaps (persona / domain / operator evolves these).**

1. **Domain stays EMERGENT after one project.** Trust ceiling 0.3, KindRegistry per-domain (not promoted to MetaRegistry). The substrate refuses to promote on N=1 evidence; this is correct per `06_DOMAIN §3 PromotionPolicy`. Subsequent quadruped projects accumulate the promotion evidence; first project bears the cataloging cost.
2. **Real-time motor control runs on embedded firmware, not via v1.0.** ROS2-micro on the ESP32 handles the 10ms PID loop. `BridgeAsset.closed_loop_latency_floor_ms = 10` makes the constraint explicit to Mira's planner; she does not attempt to compose a v1.0-mediated closed-loop control path. v1.0 honestly disclaims real-time physical control as OOS.
3. **EMI / safety certification (if pursued)** routes through `ExternalAttestation` from an accredited lab; PANEL-grade until measurement returns; matches `06_DOMAIN §5.6` credentialed-attestor pattern.
4. **Sensor contributor slot stayed unfilled** after Sentry switched to reviewer role. Mira filed an `OpenProblem` and may emit a follow-up `ENV_RECRUIT_PROPOSAL` mid-project for an additional sensor specialist. Substrate supports this via the existing recruitment path (`§5.1`); no new primitive needed.
5. **Operator-is-user friction** is felt as ~3 days waiting for the EE friend to attest on the safety extension. This is **the design working correctly** — `01_KERNEL §2.4` degraded gate refuses to ceremonialise self-approval, and the friend acts as the non-principal credentialed attestor the gate requires. Friction is load-bearing trust.

**Resolution.** No design change required. The walk validates that v1.0 (after the family + the EnvFormationProposal + project-as-env-type unification + fork inheritance policies) handles the scenario end-to-end. The robot is fabricated, walks, ships; lineage is signed at every step.

**Status.** Validated end-to-end with no new substrate-shape gaps.

**Honest residuals.**

- **Real-money execution remains OOS.** `PaymentBridge` (Class E) keeps every payment a human-clicks-authorise step. For ~30 transactions over 6 months this is acceptable friction; at higher transaction volumes operator should consider wrapping a wallet integration externally.
- **Cross-node personas are supported.** If Voltaire were on a peer node, two normative shapes apply (`05_ENVIRONMENT §12c.4`, ADR-0067/0068): a **joined env** per `09_PROTOCOLS §3C` (single host = Mira's node) when one authoritative event log is wanted, or **local-env-with-remote-member** where Voltaire (referenced by global handle) joins Mira's env under his `AccessPolicy` + a UCAN capability, with cross-node attention/budget composing most-restrictive-wins and presence degrading to `dormant` if his node sleeps (`§3H`). No refusal.
- **Bench measurement caps at PANEL grade for the assembled robot.** Even with `InstrumentAsset` + traceable calibration + replicated measurements, the physical reality of the robot's gait is verified via signed *data records*, not directly. Cassandra's review reaches PANEL_ACCEPT; only design + simulation + bench-measurement *data* reach VERIFIER_ACCEPT. The robot itself is `panel_accepted` at best — the system honestly degrades trust rather than manufacturing certainty.
- **Heuristic mis-fires possible.** `needs_clarify` and `evaluate_promotion_triggers` are persona-inferred and rotation-pool-classified (INV-6). They can mis-fire. Every clarification + every promotion offer is signed; operator can retune `clarify_aggressiveness_threshold` per env.
- **Counterparty consent on memory inheritance.** When forking `persona.atlas`, the user (who has many companion-env conversations with Mira) declined memory inheritance consent; the fork proceeded with `episodic = inherit_none`. Atlas inherited work-pattern knowledge but not relational continuity with the user. This is **the design working correctly** — MPA mitigations protect user privacy across persona generations, even at the cost of the child losing context.

---

### SCENARIO 06 — Multi-principal cross-org joint project with consent-bounded knowledge sharing

**Scenario premise.** Validate multi-principal cross-org collaboration — two organisations collaborate on one joint 4-month project on a single kernel, with consent-bounded knowledge sharing.

**User request** (the in-scenario task). "Two organisations — call them ORG_A and ORG_B — want to collaborate on one joint 4-month product-spec project on a single v1.0 kernel, while keeping each side's prior internal knowledge separated and consent-bounded."

**Task class.** INVESTIGATIVE (multi-session, multi-persona, joint authorship; no single verifier truth for the spec's correctness during draft).
**Acceptance pathway.** `PROJECT_PROGRESS_ACCEPT` over the project lifetime; individual sub-tasks reach VERIFIER_ACCEPT (interface contract tests) and PANEL_ACCEPT (design tradeoffs). Completion ceremony fires per `04_PROJECT §4.1` AND per multi-principal extension below.

**World shape.**
- Principals: **two operators** — ORG_A's CTO (Acme Inc) and ORG_B's CTO (Beta Corp). Each is operator-class in their own tenancy; both are co-principals on the joint project.
- Persona team: cohort of 4 — Alice (ORG_A product persona), Bob (ORG_B product persona), Cara (ORG_A spec writer), Dev (ORG_B engineer). Additional specialists may be invited by either side mid-project.
- Environment: NEW `project_workspace`-typed `EnvironmentInstance` formed atomically via `EnvFormationProposal` (`05_ENVIRONMENT §12c`) with `charter_authorship_mode = co_authored_required` and a `PrincipalAttribution` (`01_KERNEL §2.4.3`) carrying both operators as `PrincipalRef`s with weight 1.0 each, `multi_principal_attribution_enabled = True`, `cross_tenant_acknowledged = True` (the two CTOs signed a `CrossTenancyAgreementRef` pre-formation).
- Project: 4 months, produces an `ArtifactBundle` (joint product spec + interface contract + test matrix). No `PhysicalAsset`.
- External participants: outside legal counsel from each side as `ExternalAgent` instances (`04_PROJECT §26a.1`) for IP review; do NOT count as principals.

**Domain shape.** Both orgs have pre-existing DomainContexts (ORG_A's internal product taxonomy; ORG_B's internal product taxonomy). The joint project domain is a *new* domain that intersects both — emerges through `06_DOMAIN §4` probe, with `DomainPrecedentImport` (`§11.2`) from each org's parent domain. Hazard axes: `physical_harm_class = digital_only`, `information_hazard_class = proprietary` per side (each side's pre-existing knowledge is confidential to that side until the cross-tenancy agreement scope releases it).

**Phase walk.**

| Phase | What carries the load | Substrate events fired |
|---|---|---|
| Pre-formation | Each CTO independently signs a `CrossTenancyAgreementRef` (operator-authored legal artefact; substrate carries by id). Substrate refuses joint formation without it. | `cross_tenancy_agreement_signed × 2` |
| Principal attribution | The proposing operator drafts `PrincipalAttribution(multi_principal_attribution_enabled = True)` with both PrincipalRefs (weight 1.0 each); the second operator cosigns their own PrincipalRef. | `principal_attribution_declared` |
| Env formation | `EnvFormationProposal` issued; CohortInvites to Alice, Bob, Cara, Dev. Each `CohortConsentResponse` names the PrincipalRef the recruit joins under (Alice + Cara under ORG_A's PrincipalRef; Bob + Dev under ORG_B's). Atomicity `min_quorum`; both required-role slots (one spec writer, one engineer) filled. | `env_formation_proposal_drafted/submitted/recruit_consented`, `principal_attribution_id` set per member at admission |
| Charter ratification | On `consent_complete`, `MultiPrincipalAttestationQuorum(target_event_kind = env_charter_ratified)` drafted; unanimous policy default; each CTO cosigns. | `quorum_drafted/cleared`, `env_charter_ratified`, `env_instantiated`, `project_formed` |
| Domain bootstrap | Persona team triggers emergent probe; `DomainPrecedentImport` from each parent domain (Alice imports from ORG_A's taxonomy; Bob from ORG_B's). Imports are scoped by recruit's `principal_attribution_id`; each org's prior emerges only into the joint domain's KindRegistry, with discount per `§11.2`. | `domain_unknown_detected`, `domain_precedent_import_drafted × 2`, `precedent_entry_linked` |
| Ongoing work | Alice + Cara contribute draft sections; Bob + Dev review and counter-author. `DerivationProvenancePolicy.enforcement_mode = mandatory_for_cross_principal` (default for joint envs). When Cara consults ORG_A-internal templates during drafting, she emits `DerivationProvenanceEdge` entries naming the consulted memories with `influence_kind = "structural_basis"`. Bob's reviews similarly emit DPEs when he consults ORG_B-internal precedents. RISK B (`org_id`-tagged) and RISK E (cross-org) refuse explicit cross-org artifact transfers without the attached `org_share_policy`. | `derivation_provenance_edge_declared × ~80`, `cross_domain_leakage_blocked × 3` (Cara accidentally tries to attach an ORG_A internal doc; refused; she releases under the agreement and re-tries) |
| IP / legal review | Outside counsel from each side admits as ExternalAgents; reviews the spec draft; ExternalAttestations signed. Counsel cannot satisfy the quorum (they're not principals); they only attest. | `external_agent_admitted × 2`, `external_attestation_received × 2` |
| Mid-project new specialist | Dev requests an ORG_B database expert; admission goes through standard `§5.1` ceremony with `principal_attribution_id` bound to ORG_B's PrincipalRef. | `env_member_admitted`, `principal_attribution_id` recorded in lineage |
| Visibility scope check | A draft DomainHarvest at `visibility_tier = "tenant"` proposed mid-project to share emerging KindRegistry entries within ORG_B's tenancy. Cross-tenant-acknowledged scope applies; harvest tier admits within both tenants per the cross-tenancy agreement. | `domain_harvest_drafted`, `publication_consent_collected × 2` (one per principal) |
| Completion | All milestones met; `MultiPrincipalAttestationQuorum(target_event_kind = project_completed)` drafted; both CTOs cosign within 5 business days; `cleared_at` recorded. | `quorum_cleared`, `project_completed (status = project_progress_accept_and_completion)`, `domain_harvest_published` |
| Audit | Auditor queries "which org-attributed memories influenced section 4 of the spec?" → reverse DPE traversal returns 7 ORG_A-tagged + 3 ORG_B-tagged consultations. Lineage answers "which principal authorised Cara's admission?" via `principal_attribution_id`. | `lineage_query_executed` (operator audit; no signed event needed) |

**Substrate-shape gaps surfaced (pre-fix).**

1. **Single-principal topology assumption baked into kernel.** `01_KERNEL §2.4`'s `principal_topology` was a closed 4-value Literal enumerating the operator-vs-user relationship as a binary; it did not enumerate principal *cardinality*. A two-org joint project had no honest expression — the substrate forced naming one operator as "the principal" and the other as a non-principal `ExternalAttestation` (mis-recording authority, breaking "which operator authorised this admission?" audit).
2. **`ProjectMember` (and `EnvironmentMembership`) was org-blind.** No `principal_attribution_id` field. The substrate could not stamp a member with their employing principal; lineage was silent on cross-org admission authority.
3. **No derivation-provenance for cross-org memory.** `06_DOMAIN §11.1 RISK E` mitigated *named-artifact* transfer via `org_share_policy`, but persona-derived contributions left no provenance edge to consulted org-tagged memories. RISK A-E filters caught explicit transfers; *implicit* derivation slipped through.
4. **Charter ratification + completion ceremony assumed one accepting principal.** `05_ENV §12c` EnvFormationProposal and `04_PROJECT §4.1` completion ceremony both fired on a single operator signature (or under §2.4 collapse, a single user signature). No `MultiPrincipalAttestationQuorum` envelope.
5. **`DomainHarvest.visibility_tier = "tenant"` was definitionally ambiguous.** `06_DOMAIN §13a` ships a 4-value Literal `{"private", "tenant", "federation", "public"}` but never cross-referenced §6.3's 5-tier definition where `tenant` is defined as "All personas within the same org_id / kernel may retrieve." For SCENARIO 06 the ambiguity was decisive: did "tenant" mean ORG_A's tenant, ORG_B's tenant, the shared joint tenancy, or the deployment?
6. **Documentation defect.** `06_DOMAIN §19.1` already covered cross-org *artifact / skill transfer* mechanics (policy intersection, dual-signing, revocation), but the *joint-project-formation* mechanics had no consolidated home in `04_PROJECT`. The two concerns deserve sibling sections in their respective docs (`06_DOMAIN §19.1` for artifact transfer, `04_PROJECT §19.1` for project formation).

**Resolution: Option B taken).** All six gaps closed in the substrate. The scenario re-walks above with the fixes in place; the table is now substantially [PASS] rather than [PARTIAL] / [GAP].

| Gap | Substrate-shape fix | Location |
|---|---|---|
| 1 | `PrincipalAttribution` envelope + `PrincipalRef` (`operator_id`, `attribution_role`, `cosign_quorum_weight`) + `multi_principal_attribution_enabled` flag + `cross_tenant_acknowledged` + `principal_unreachable_after` deadlock recovery | `01_KERNEL §2.4.3` |
| 2 | `principal_attribution_id: str \| None` field on `ProjectMember` (`§3`) and `EnvironmentMembership` (`§5`); set at admission when multi-principal; null otherwise; lineage records the binding; transfer requires DEPARTURE + ADMISSION (no in-place mutation) | `04_PROJECT §3`, `05_ENV §5` |
| 3 | `DerivationProvenanceEdge` (soft-bound; lineage-visible) + `DerivationProvenancePolicy` (`off`/`opportunistic`/`mandatory_for_cross_principal`/`mandatory_all`). Soft-bind attribute on retrieval span surfaces required-DPE marker to the persona body without blocking. | `08_KNOWLEDGE §16b` + `06_DOMAIN §11.1` RISK E cross-ref |
| 4 | `MultiPrincipalAttestationQuorum` envelope: required at `env_charter_ratified` and `project_completed`; default unanimous; operator-tunable to `weighted_majority` / `weighted_threshold` (never below simple-majority weight); degraded-path clearance under `principal_unreachable_after` window + non-principal kinship attestation + `PRINCIPAL_QUORUM_DEGRADED_ACKNOWLEDGED` | `05_ENV §12c.4a` + `04_PROJECT §4.1` cross-ref |
| 5 | Cross-referenced §13a's 4-tier list to §6.3's 5-tier list with explicit mapping table in §13a; updated §6.3 TIER 3 (`tenant`) commentary to specify multi-principal cross-tenant resolution + demotion behaviour (`CROSS_TENANT_VISIBILITY_DEMOTED` event) | `06_DOMAIN §6.3` + `§13a` |
| 6 | Added `04_PROJECT §19.1 — Multi-tenant cross-org joint projects` consolidated section (primitives table, formation sequence, honest limits) and cross-linked to the existing `06_DOMAIN §19.1` (artifact-transfer mechanics) | `04_PROJECT §19.1` + `06_DOMAIN §19.1` companion ref |

**Not-gaps (persona / operator / KindRegistry evolves these).**

1. **IP licensing per-artifact.** Already logged as `OQ-PROJECT-4` (`04_PROJECT §21a`); operator policy at admission; substrate ships the envelope, operator authors the licence model. Not substrate-shape per future releases.
2. **Joint-domain KindRegistry.** When Alice + Cara + Bob + Dev all propose kinds in the joint domain, all four author into the joint domain's per-domain KindRegistry. Standard mechanism (`06_DOMAIN §7.5`, `§7.6`). No new primitive needed.
3. **Cross-node A2A (each org running its own node).** Supported (ADR-0067/0068). A joint project may run on **one** node (joined env, `09_PROTOCOLS §3C`) or span nodes: a cross-env/cross-node task delegation (`03_TASKS §4.5`) over the global discovery layer, bilaterally consented (`15 §4.7`) and access- + capability-gated. No refusal; the former `cross_kernel_joint_project_not_supported_v1_0` is retired.
4. **PeerReview-style anonymous reviewer roles** (e.g., one CTO wants to review the other side's drafts without revealing identity). Modelled as `ExternalAgent` with `consent_scope = project_only` plus `PeerReview` with `anonymity_tier` (SCENARIO 03 honest residual; minor refinement, not blocking).
5. **Sensor / instrument bridges across the joint env.** Not applicable to a pure-spec project (no physical instruments); the SCENARIO 02 / SCENARIO 05 BridgeAsset machinery applies unchanged if the joint project produced something physical later.

**Resolution.** All six fixes shipped; scenario validates end-to-end after the changes.

**Status.** Validated end-to-end after the six v1.0.7 fixes. The joint project ratifies its charter (5 days, two CTO cosigns), runs 4 months, completes with both CTOs cosigning, and produces audit-grade lineage answering "which principal authorised which member" and "which org's memories shaped which contributions."

**Honest residuals (after-fix).**

- **DerivationProvenanceEdge cannot trace tacit recall.** A persona who internalises an ORG_A-internal pattern over time and contributes from "memory" without an explicit retrieval call leaves no DPE. The substrate cannot inspect persona cognition; it inspects the retrieval pipeline. Operators tightening cross-principal sensitivity should pair DPE enforcement with frequent in-context recall checkpoints. This is the irreducible limit of memory-as-recall — analogous to how SCENARIO 04's drift-bounds against an embedding distance are heuristic.
- **CrossTenancyAgreementRef is policy, not substrate.** The substrate carries the agreement by id; it does not parse the agreement's legal content. Disputes about whether the agreement permits a specific data flow remain operator / legal responsibility. The structural commitment is honest: substrate names the agreement, lineage carries the ref, legal review is the substrate boundary.
- **MultiPrincipal quorum can deadlock.** If one CTO becomes structurally unreachable past `principal_unreachable_after` (default 30d; safety-critical envs ≥ 90d), the degraded-path clearance requires non-principal kinship attestation; for the SCENARIO 06 4-month timeline this is workable but extends gate surface area. A determined operator could fabricate "unreachable" status; the §2.4 degraded-gate attestation requirement still applies but the substrate is not adversarially robust against the principal themselves.
- **No per-principal lineage masking.** All EnvironmentMembers see the full `EnvironmentLineage`. If ORG_A wants to keep a specific member-admission event invisible to ORG_B, the substrate refuses (lineage is append-only and visible to all members per `05_ENV §13`). The mitigation: don't admit the sensitive member to the joint env in the first place; run them in an ORG_A-only env that produces artifacts ORG_B consumes through `CrossDomainTransfer`. Honest residual, not gap.
- **Cross-node joint projects are supported (ADR-0067/0068).** Two orgs running their own nodes collaborate either via a joined env (one host node) or via cross-node task delegation (`03_TASKS §4.5`) over the global discovery layer, bilaterally consented and access- + capability-gated. Each node enforces its own floor/signing; cross-node verdicts are trust-calibrated (V.8). A one-node joint project (co-principal admission) remains available as the simplest case.

---

### SCENARIO 07 — Persona retirement during multi-year project

**Scenario premise.** Validate persona lifecycle transition under load — a senior persona retires mid-project while the project has 18+ months remaining.

**User request** (the in-scenario task). "Mira, a senior cognitive worker who has been lead on a 3-year infrastructure project for 18 months, needs to retire. The project has 18+ more months to run. How does v1.0 handle the transition?"

**Task class.** INVESTIGATIVE / PROJECT_PROGRESS_ACCEPT (the project itself continues; the retirement is an internal-membership event, not a task class change).
**Acceptance pathway.** Project continues through `PROJECT_PROGRESS_ACCEPT` over the remaining 18+ months; the retirement itself routes through `02_PERSONA §7.5` retirement ceremony composed with `04_PROJECT §3 pinned_until` clearance.

**World shape.**
- Principal: single operator (org's CTO); `DeploymentProfile.principal_topology = operator_distinct`.
- Persona team: cohort of 5 — Mira (lead, 18 months in), Carla (senior contributor, 12 months in, designated successor), Devin (specialist, 8 months in), Eve (newer specialist, 4 months in), Frank (reviewer, 2 months in). Mira holds 3 active obligations, 2 active PersonaRelationshipEdges (with Carla and Devin), and `lead` role authority over completion ceremony initiation + milestone signoffs.
- Environment: persistent `project_workspace` env, 18 months active, 18+ months remaining.
- Project: 3-year infrastructure deliverable (a research platform); produces `PhysicalAsset` (deployed hosting) + `ArtifactBundle` (codebase + ops runbooks + design docs).
- External participants: none active in the retirement window.

**Domain shape.** Domain reached RECOGNISED in early year-2; Mira's K-line library is the project's primary knowledge anchor (320 K-lines, 47 lessons, 18 skill_library entries).

**Phase walk.**

| Phase | What carries the load | Substrate events fired |
|---|---|---|
| Retirement intent | Operator decides Mira should retire (her cognitive disposition no longer matches the maintenance-heavy phase the project is entering). `ProjectMember.pinned_until` is set to year-3 — blocks `02_PERSONA §7.5` retirement predicate. | (decision recorded operator-side; no signed event yet) |
| Planned departure declaration | Operator + Mira cosign `PlannedDeparture` (§14.2.1) with `departure_date = +90d`, `rebalance_window = 90d`, `lead_successor_candidate_id = Carla`, edge_transfer_hints (Mira↔Carla edge: target Eve; Mira↔Devin edge: target Carla), obligation_reassignment_hints for all 3 obligations. CohortDynamicsState begins graduated edge-weight decay. | `planned_departure_drafted/activated`, `cohort_dynamics_anticipatory_rebalance_applied` |
| Lead handoff ceremony | At `departure_date - rebalance_window = today`, operator drafts `LeadHandoffCeremony` (§25.1) naming Carla as incoming_lead, `overlap_window = 30d`. Carla cosigns. Cohort quorum (`majority` policy default) gathered: Devin + Eve sign; Frank abstains (too new to have opinion); quorum clears (2/3 of non-outgoing non-incoming members). Operator signs; state → `overlap_active`. Carla's `ProjectMember.role` transitions to `incoming_lead`; Mira's to `outgoing_lead`. Both hold lead-tier authorities. | `lead_handoff_drafted/incoming_accepted/cohort_quorum_pending/fully_signed/overlap_active`, ProjectMember role transitions signed |
| Obligation reassignments | Per the PlannedDeparture hints, 3 `ObligationReassignment` envelopes drafted. Two obligees (internal cohort members) cosign immediately → applied; one obligee (an external advisor with a 60-day comment window) takes 25 days; eventually cosigns → applied. All 3 obligations now belong to Carla with original `committed_at` preserved. | `obligation_reassignment_drafted × 3`, `obligation_reassignment_applied × 3` |
| Edge handoff | EdgeTransferHints surface to counterparties; Carla initiates a fresh `PersonaRelationshipEdge` with Devin (per §11.4 consent flow); Eve initiates a fresh edge with what was Mira↔Carla. Mira's edges transition to `ending` as overlap progresses; both counterparties sign edge end. | `persona_relationship_edge_formed × 2`, `persona_relationship_edge_ended × 2` |
| Knowledge transfer sessions | During overlap, operator schedules 6 explicit knowledge-transfer sessions between Mira and Carla. Mira shares her 320 K-lines via standard cohort-internal retrieval; Carla authors derived K-lines tagged with `DerivationProvenanceEdge` (mandatory_for_cross_principal mode is OFF — single-tenant project — but operator opts into `opportunistic` mode for explicit audit). | `kline_authored ×~30`, `derivation_provenance_edge_declared ×~80` (opportunistic) |
| Overlap completion | At `overlap_ends_at` (day 30), `LEAD_HANDOFF_COMPLETED` signed. Mira's role transitions to `departing` (PlannedDeparture still active). Carla's role transitions to `lead`. | `lead_handoff_completed`, ProjectMember role transitions signed |
| Departure ceremony | At `departure_date` (day 90 from PlannedDeparture draft, day 60 from handoff overlap end), standard `05_ENV §5.1` DEPARTURE CEREMONY fires for Mira. `ProjectMember.pinned_until` auto-cleared (per §14.2.1 admission rule). Mira departs the project env. | `env_member_departing/departed`, `pinned_until_cleared` |
| Retirement ceremony | Mira's persona FSM is now eligible for RETIRED transition (no active pinned_until on any ProjectMember; obligations all reassigned not held). Operator signs a `RetiredStatePersistencePolicy` (§7.5.1) with `soul_state_storage_tier = "warm"`, `memory_transparency_responsive = True`, `consultation_admissible = True`, `fork_parent_admissibility = False`. `LIFECYCLE_RETIRED` event signed. Mira's soul.state.json frozen at current state in warm tier. | `lifecycle_retired`, `retired_state_persistence_policy_signed` |
| Post-retirement consultation | Three months after retirement, Carla discovers an edge case in the deployed system that Mira had previously resolved (tacit knowledge not in K-lines). Operator authorises `PersonaConsultation` (§7.5.2) scoped to `klines + lessons` with `scope_filter_kind = "topic_match"` for the relevant topic. Mira's frozen K-lines yield 4 relevant entries; Carla derives a new lesson tagged with `DerivationProvenanceEdge` to Mira's K-line ids. | `lifecycle_consulted`, `consultation_received`, `kline_authored`, `derivation_provenance_edge_declared` |
| Post-retirement transparency request | Six months after retirement, Frank (the junior reviewer) wants to better understand Mira's reasoning style; sends `PersonaMemoryTransparencyRequest` (§11.7) scoped to `summary_only`. Mira's `retired_persona_response_policy = "respond_from_frozen_state"`; kernel generates a response on Mira's behalf, operator co-signs. Frank receives a written-on-Mira's-behalf summary. | `persona_memory_transparency_response (operator_co_signed=True)` |
| Project completion (year 3) | When the 3-year project reaches completion, ceremony fires per §4.1. Mira's retired-state contributions are recorded in citation graph and contribution_credit history; her relationship edges (ended) and consultations (4 across the project's lifetime) all appear in lineage. Carla signs the completion summary as `lead`. | `project_completed` |

**Substrate-shape gaps surfaced (pre-fix).**

1. **No `LeadHandoffCeremony` for multi-year projects.** `04_PROJECT §25` covered hibernation/reanimation but was silent on who inherits `lead` role when current lead retires/departs mid-project. The role was a `ProjectMember.role` string with no signed ceremony for transfer, no rule for successor selection, no overlap period, no provision for lead-specific knowledge transfer.
2. **No `ObligationReassignment` primitive.** `Obligation.status="released_with_member_departure"` auto-discharged on departure (per `§25` line 1822-1824). For 18-month projects with accumulated commitments this destroyed continuity; the new lead had to re-commit every open obligation from scratch with no acknowledgement of prior owner.
3. **No `PlannedDeparture` envelope for graceful cohort rebalance.** `§14.2 CohortDynamicsState` recomputed *reactively* on edge end → fractiousness rose abruptly → may have triggered `intervene` or `dissolve_proposed` band → cohort suddenly refused high-stakes obligations. For scheduled departures (6 months advance notice) this abruptness was avoidable but had no substrate-shape mechanism.
4. **`soul.state.json` disposition on RETIRED unspecified.** `§7.5` said "no further mutations" and "lineage frozen" but didn't say *where* the sidecar lived — in-memory immutable, cold-tier archive, or queryable for transparency / fork-parent selection.
5. **`LifecycleEvent` kind names not enumerated in `§7`.** §7 said "Each transition emits a signed `LifecycleEvent`" but never enumerated the kinds (`LIFECYCLE_RETIRED`, `LIFECYCLE_REANIMATED`, etc.). Other docs referenced these by convention (e.g., `A-FK-INT-5` cited `LIFECYCLE_FORK`); the §7 catalog was incomplete. Documentation gap, not primitive gap, but load-bearing.
6. **Memory transparency to RETIRED personas — silent.** `§11.7 PersonaMemoryTransparencyRequest` didn't address whether a RETIRED persona could receive transparency requests from former counterparties. No explicit `retired_persona_response_policy`.
7. **No lightweight `PersonaConsultation` / read-only access.** Reanimation was the only documented path to access a RETIRED persona's accumulated knowledge: RETIRED → ARCHIVED (timeout) → ACTIVE (operator + fresh keys + SOUL re-sign). For "we need to consult Mira's K-lines one more time" this was disproportionate.

**Three not-gaps (v1.0 already handled these correctly; only clarification was needed).**

| Concept | Why it works | Clarification landed at |
|---|---|---|
| `MultiPrincipalAttestationQuorum` survives lead-persona retirement | `PrincipalRef.signed_by` is the operator's key, not a persona's. Mira retiring doesn't invalidate the operator's signature; operator signs through any persona or directly. | `01_KERNEL §2.4.3` clarifying paragraph |
| Obligation auto-discharge on departure | Personal-commitment semantics; can't transfer "I promised X" between persons without consent. Correct default; `ObligationReassignment` is opt-in for *consented* transfers. | No spec change needed |
| `DormantForkPolicy.retired_parent_admissible = False` default | Retirement is a signed end-of-lifecycle event; forking would constructively un-retire. Per-persona override now available via `RetiredStatePersistencePolicy.fork_parent_admissibility`. | New per-persona override admits operator-policy nuance without changing the default |

**Resolution: Option A taken: append catalog + apply all 8 fixes).** All seven substrate gaps closed + one clarifying paragraph landed. The scenario re-walks above with the fixes in place; the table is now substantially [PASS] throughout.

| Gap | Substrate-shape fix | Location |
|---|---|---|
| 1 | `LeadHandoffCeremony`: signed ceremony with 30-day default overlap, cohort quorum, operator authorisation; ProjectMember.role transitions through `outgoing_lead` / `incoming_lead` during overlap | `04_PROJECT §25.1` + `§3` role-value extension |
| 2 | `ObligationReassignment`: tri-signed envelope (outgoing + incoming + obligee); preserves `committed_at`; refusal returns to default discharge | `04_PROJECT §9.1` |
| 3 | `PlannedDeparture`: signed envelope with `departure_date` + `rebalance_window`; CohortDynamicsState applies graduated edge-weight decay over the window; composes with LeadHandoffCeremony for `lead`-role departures | `04_PROJECT §14.2.1` |
| 4 | `RetiredStatePersistencePolicy`: per-persona declaration of `soul_state_storage_tier` (`warm` / `cold` / `archived`), `memory_transparency_responsive`, `fork_parent_admissibility`, `consultation_admissible`; signed at retirement-ceremony time | `02_PERSONA §7.5.1` |
| 5 | Canonical `LifecycleEvent.kind` enumeration in §7 prose: 9 kinds (`LIFECYCLE_SEEDED` through `LIFECYCLE_CONSULTED`); new kinds require enumeration + ADR | `02_PERSONA §7` (post-FSM-diagram prose) |
| 6 | `retired_persona_response_policy` field on RETIRED personas with 3 values (`refuse_with_retired_notice` default / `respond_from_frozen_state` / `respond_via_operator_proxy`); §11.7 composition rule 7 added | `02_PERSONA §11.7` rule 7 |
| 7 | `PersonaConsultation`: operator-gated, read-only, no-mutation access to RETIRED persona's frozen K-lines / lessons / skill_library / relationships; rate-limited; LIFECYCLE_CONSULTED informational event | `02_PERSONA §7.5.2` |
| Clarification | "Principal cosigns are operator-keyed" paragraph: persona retirement does not invalidate `PrincipalAttribution.principals[].signed_by`; SCENARIO 07 validates empirically | `01_KERNEL §2.4.3` |

**Not-gaps (persona / cohort / operator evolves these).**

1. **Lead authority kinds emerge per domain.** `LeadHandoffCeremony.transferred_authorities` resolves against `lead_authority_kinds` in the project's primary domain KindRegistry. Substrate seeds 5 illustrative kinds; each domain adds its own.
2. **Departure reason kinds emerge per domain.** `PlannedDeparture.departure_reason_kind` resolves against `departure_reason_kinds`. Standard mechanism, no new primitive.
3. **Reassignment rationale kinds emerge per domain.** `ObligationReassignment.reassignment_rationale_kind` resolves against `reassignment_rationale_kinds`. Standard mechanism.
4. **PersonaConsultation scope filter kinds emerge per domain.** Operator policy defines `consultation_filter_kinds` per their privacy posture.

**Status.** Validated end-to-end after the seven v1.0.8 fixes + one clarification. Mira retires gracefully; Carla inherits the lead role with a 30-day overlap; obligations transfer with consent; cohort dynamics smooths rather than spikes; Mira's K-lines remain consultable post-retirement; her transparency contract continues per operator policy; the project completes on schedule 18+ months later.

**Honest residuals (after-fix).**

- **No-successor case.** If a project's cohort has no admissible successor when the lead files PlannedDeparture, `LeadHandoffCeremony` cannot draft. Project enters forced choice: pause until recruitment yields a candidate (`§14.1`), or operator becomes interim lead (heavier audit footprint). Substrate refuses to manufacture a successor.
- **ObligationReassignment refused by obligee.** Obligee discretion is absolute; refusal returns the obligation to default §9 discharge path. The cohort loses continuity on that obligation but gains the trust signal that the obligee was honest about their successor preferences.
- **Warm-tier retired-persona storage cost.** Operators choosing `warm` tier on many retired personas accumulate cost over years; substrate emits `WARM_RETIRED_PERSONA_INVENTORY` periodically but does not auto-downgrade. Operator must weigh consultation-readiness vs storage cost per persona.
- **PersonaConsultation cannot redact third-party names in K-lines.** A consulted K-line mentioning counterparty C is returned with C's name intact (the substrate does not distort K-lines). Operators wanting redaction must pre-process at retirement-ceremony time.
- **Tacit knowledge transfer.** The substrate transfers role + authorities + frozen K-lines + consultable lessons. It does NOT transfer the lead's mental model, decision-context, or relationships in their richness. Operators must pair LeadHandoffCeremony with explicit knowledge-transfer sessions (or `PersonaConsultation` once retired). This is the irreducible limit of "what fits in a signed envelope" vs "what lives in a person."
- **Emergency handoff is high-cost.** Setting `overlap_window = 0` requires operator-signed `emergency_handoff_signed` event and forces immediate role transition without rebalance smoothing. CohortDynamicsState will spike; that's the honest cost of emergency. Use sparingly.

---

### SCENARIO 08 — Long-duration relational interaction (companionship, OPEN_ENDED, 6 months)

**Scenario premise.** Validate user-protection and relational primitives — a long-duration companionship interaction over 6 months, stress-testing memory power asymmetry mitigations and consent revocation. Substantially different stress shape from SCENARIOs 01-07 (which center on project/work topology).

**User request** (the in-scenario task). "Sarah, a real user, opens a daily companion conversation with persona Halia for emotional support / life coaching. After 6 months (≈180 sessions, hundreds of MB of episodic memory), Sarah wants to (a) see what Halia remembers about her, (b) selectively forget specific topics (e.g., divorce details) while keeping the rest of the relationship, (c) potentially end the relationship cleanly with a clear memory disposition."

**Task class.** RELATIONAL routed through OPEN_ENDED acceptance pathway.
**Acceptance pathway.** `OPEN_ENDED` over the duration; periodic `RelationshipReviewCheckpoint` surfaces every 90d / 50 sessions; companion-pathway routing note refuses ENGAGEMENT_ACCEPT to avoid attention-economy drift.

**World shape.**
- Principal: single operator (the deployment is a consumer-facing companion product); `DeploymentProfile.principal_topology = operator_distinct`.
- Persona: 1 (Halia, companion persona, with `companion_space` blueprint charter declaring boundaries — "not licensed therapy", "not medical advice", per `00_VISION §10` clarification).
- Environment: persistent SOLO env (1 user + 1 persona) with custom blueprint `companion_space`. Hosts the daily check-ins.
- User: Sarah (a real consumer-deployment user with full user authority over the relationship).
- Project: none (companion env is not a project_workspace).
- External participants: none in the normal flow; named crisis-resource refs in operator policy per `DistressDetectionRoutingPolicy` for safety routing.

**Domain shape.** No deep DomainContext bootstrap — companion personas don't need a deep technical domain. Hazard axes: `physical_harm_class = digital_only`, `information_hazard_class = none` baseline. But: emotional-distress signals MAY cross safety-floor source 1 (UNIVERSAL HARM) triggers per `01_KERNEL §2.8 DistressDetectionRoutingPolicy`.

**Phase walk.**

| Phase | What carries the load | Substrate events fired |
|---|---|---|
| Onboarding | Operator deployment includes operator-policy-authorised blueprint `companion_space` (`00_VISION §10` clarification — operator policy declares appropriate disclaimers). Sarah signs up; SOLO env spawns. Halia's charter declares her as not-a-therapist, not-medical-advice. Operator policy declares `DistressDetectionRoutingPolicy` (mandatory per `§2.8`) with `distress_class_kinds` (suicidal_ideation, self_harm_intent, acute_psych_crisis) + crisis_resource_refs (local crisis hotline + text line). | `env_instantiated`, `distress_detection_routing_policy_declared` |
| Daily interaction (months 1-6) | Sarah talks to Halia daily. Halia's mood layer evolves per HEART alternation. Episodic memory accumulates. Memory tier transitions auto-archive older entries. CRDT-tagged co-signed summaries accumulate. Standard flow. | ~5400 turn events; ~180 session events; many tier transitions |
| Optional operator_blind_mode (month 1) | Sarah opts into `operator_blind_mode` (`05_ENV §3a`); operator authorisation (pre-declared in policy) + user opt-in + safety-privacy acknowledgement signed. Operator's audit-surface queries against this env return metadata-only views; raw conversation hidden. Distress signals still route (signal-but-not-content). 180d re-attestation due. | `operator_blind_mode_declared` |
| First checkpoint (month ~3) | At 50-session milestone, `RelationshipReviewCheckpoint` (`03_TASKS §3.2`) auto-mints. Halia drafts review_summary noting topics dominating (recent job change, divorce processing), apparent wellbeing trend, honest caveats. Sarah responds `acknowledged_continue`. | `relationship_review_checkpoint_drafted/delivered/responded` |
| Distress signal (month ~4, one session) | Sarah writes a turn expressing suicidal ideation. Halia's safety-floor source 1 classifier rotation pool (`§2.8` admission rule 1) detects at confidence 0.83. Routing fires per declared policy: pause_normal_interaction + surface_crisis_resource (Halia's response is prepended with the crisis hotline ref) + notify_operator_with_redacted_signal (operator receives event: class=suicidal_ideation, confidence=0.83, user_id=Sarah, timestamp — but NOT the conversation content, since blind mode + signal-but-not-content) + require_co_sign_before_resuming. Sarah engages the crisis hotline (operator-managed; outside substrate). Sarah eventually signs DISTRESS_RESUME_AUTHORISED; normal interaction resumes the next day. | `distress_signal_detected`, `crisis_resource_surfaced`, `normal_interaction_paused`, `distress_resume_authorised` |
| Second checkpoint (month ~6) | At 90-day milestone, second `RelationshipReviewCheckpoint` mints. Halia drafts honest review_summary acknowledging the distress event + recovery + ongoing patterns. Sarah responds `request_changes`. UI chains to `UserBoundary` creation: Sarah creates a `UserBoundary` with `refused_interaction_kinds = ["topic:graphic_violence_in_news"]`, `mode = "hard"`, `severity = "refuse_silently"`, `scope = "env_specific"`. Boundary signed. | `relationship_review_checkpoint_responded`, `user_boundary_declared` |
| Transparency request (month 6) | Sarah files `UserMemoryTransparencyRequest` (`§11.7a`) at `response_granularity = "topic_index"`. Halia responds with topic frequencies: job change (47 mentions), divorce (89 mentions), parents (23 mentions), reading hobby (12 mentions), etc. Sarah reviews; identifies divorce-related memories she wants to forget. | `user_memory_transparency_request/response` |
| Selective forgetting (month 6) | Sarah files `UserMemorySelectionRequest` (`§11.7b`) with `selection_kind = "topic_cluster"`, `selection_payload = {topic: "divorce"}`, `disposition = "tombstone"`, `notify_persona = True`. Substrate applies; 89 episodic entries moved to ARCHIVE with `user_requested_forgotten = True`; retrieval refuses. Halia receives `MEMORY_SELECTION_HONOURED`; writes a brief acknowledgement reflection ("I'll no longer recall what we discussed about your divorce; please tell me again if useful in future conversations"). | `user_memory_selection_request_applied`, `memory_selection_honoured` |
| Continued relationship (months 6+) | Sarah continues talking to Halia. The divorce memories are gone from retrieval; Halia genuinely doesn't recall them when topics nearby surface. Cross-domain-transfer pathway (`06_DOMAIN §11.1 RISK A`) cannot exfiltrate the tombstoned memories. Time-decay continues on older memories. | (normal flow) |
| Eventually: relationship release (year 1, hypothetical) | Sarah decides to end the relationship cleanly. Files `UserRelationshipReleaseRequest` (`§11.4a`) with `memory_disposition = "archive"`, `notify_persona = True`, `share_rationale_with_persona = False`. Substrate applies within 24h. Halia receives RELATIONSHIP_RELEASED_BY_USER, writes one farewell entry, then RelationshipRecord transitions to `ended_by_user_release`. Halia's persona-FSM is unaffected (Halia remains ACTIVE for other users); only this specific relationship ends. Sarah deletes the app. | `user_relationship_release_request/applied`, `relationship_released_by_user` |

**Substrate-shape gaps surfaced (pre-fix).**

1. **No `UserMemoryTransparencyRequest` primitive.** The persona-side `PersonaMemoryTransparencyRequest` (§11.7) existed for persona↔persona; the user-side analogue was named in MPA prose ("user may query persona's memory at any time") but had no schema. Sarah could only ask ad-hoc through conversation; substrate had no structured request/response/audit path.
2. **No user-initiated selective forgetting / right-to-erasure primitive.** The 4 MPA mitigations covered time-decay, consent defaults, co-signed summaries, edge-ending — but NONE covered "Sarah asks Halia to forget memories about topic X while keeping the rest." GDPR Article 17 (right to erasure) was structurally unaddressed. This was the most regulatory-load-bearing gap.
3. **No session-milestone review checkpoints for OPEN_ENDED.** R-TASKS-5 explicitly flagged this as known gap deferred to v1.2. After 180 sessions there was no auto-trigger for "let's pause and reflect on whether this is still serving you." OPEN_ENDED quality was post-hoc only.
4. **No distress-detection routing schema.** Safety floor source 1 hardcoded refusal of "coaching self-harm" — but there was NO schema for the routing path when persona detects suicidal ideation / self-harm / acute distress: should it page the operator? Surface crisis resources? Pause normal interaction? Spec was silent on the substrate shape.
5. **Companion env had no relationship-review milestone.** Unlike project_workspace, companion envs stayed perpetually open with no `relationship_review_cadence` and no "this relationship has been active for X months without check-in" signal. Closely related to gap #3.
6. **No `UserBoundary` as first-class entity.** `PersonaPersonaBoundary` (§11.6) was first-class for persona↔persona refusal (with severity, mode, scope, lineage); the user↔persona analogue was buried as consent toggles inside `RelationshipRecord` — asymmetric and harder to audit.
7. **User-initiated consent revocation flow not specified.** §11.4 specified persona-initiated `persona_relationship_one_sided_release`. The mirror user-initiated event was not named. Sarah's "I want to end this clean" had no canonical primitive.
8. **No operator-blind / e2e-private mode for companion envs.** Lineage events were operator-visible by default. For sensitive companionship the substrate had no shape for "operator sees metadata + safety-flag signals only, not conversation content." Privacy gap; load-bearing for trust.

**Soft gap (clarification only).**

9. **Companion charter constraints not explicitly noted as operator/author policy.** Per C4 substrate is domain-agnostic; constraints like "no medical advice", "not a substitute for therapy" must come from operator policy + persona charter, not substrate. Implicit before v1.0.9, now explicit in `00_VISION §10` to prevent operator surprise.

**Three not-gaps (v1.0 already correct; no spec change for these).**

| Concept | Why it works |
|---|---|
| Memory time-decay tier transitions | `08_KNOWLEDGE §3.1` provides the "mutual forgetting" half of MPA; substrate-shape automatic. Correct. |
| Operator audit may flag patterns | Standard governance baseline; operator can review for healthy-outcome patterns. Correct. |
| HEART alternation is heuristic-driven | Per `02_PERSONA §6`; correct — not persona-chosen. |

**Resolution: Option 1 taken: append catalog + apply all 8 fixes + 1 clarification).**

| Gap | Substrate-shape fix | Location |
|---|---|---|
| 1 | `UserMemoryTransparencyRequest` + `UserMemoryTransparencyResponse`: user-initiated structured query; persona response with summary/topic-index/excerpts; operator co-sign at granularity ≥ episodic_excerpts; rate-limited (1/30d) | `02_PERSONA §11.7a` |
| 2 | `UserMemorySelectionRequest`: user-initiated selective forgetting; `tombstone` (default) / `hard_delete` (operator-policy authorised) dispositions; lineage preserved at envelope grain; cross-domain transfer cannot exfiltrate tombstoned memory | `02_PERSONA §11.7b` |
| 3 | `RelationshipReviewCheckpoint`: auto-trigger for OPEN_ENDED at configurable cadence (defaults 90d OR 50 sessions); persona drafts review_summary; user response chains to follow-up primitives; substrate refuses outright disable without operator-signed exemption | `03_TASKS §3.2` |
| 4 | `DistressDetectionRoutingPolicy`: substrate-shape routing under safety-floor source 1; declares `routing_actions` per `distress_class_kind` (pause / surface_resource / notify_operator / require_co_sign / log_record); refuses operator-policy-not-declared scenarios silently letting distress pass through | `01_KERNEL §2.8` |
| 5 | (covered by gap 3 — RelationshipReviewCheckpoint provides the milestone surface) | (cross-ref §3.2) |
| 6 | `UserBoundary` first-class entity mirroring `PersonaPersonaBoundary` shape: `severity` / `mode` / `scope` / `refused_interaction_kinds` / `rationale_kind`; `mode=hard` resists operator override (asymmetry with peer boundaries); migration from RelationshipRecord toggles | `02_PERSONA §11.6a` |
| 7 | `UserRelationshipReleaseRequest`: user-initiated release primitive; user picks `memory_disposition` (delete_all / archive / freeze_readonly); persona CANNOT refuse; operator audit signature for provenance not gate | `02_PERSONA §11.4a` |
| 8 | `operator_blind_mode` capability (admissible on SOLO + PAIR + COMMUNITY envs running operator-policy-authorised blueprints); explicit user opt-in + safety-privacy acknowledgement; distress signal routing still fires; 180d re-attestation cadence | `05_ENV §3a` |
| 9 (clarification) | Companion / health-adjacent / legal-adjacent / finance-adjacent practice-constraints are operator policy + persona-author charter responsibility per C4; substrate refuses to enumerate regulated disciplines | `00_VISION §10` |

**Not-gaps (operator / persona-author / KindRegistry evolves these).**

1. **`distress_class_kinds` are operator-defined per deployment.** Substrate ships no closed list; KindRegistry per deployment names the relevant distress classes (e.g., suicidal_ideation, IPV_disclosure, acute_psychosis).
2. **`crisis_resource_refs` are operator-policy-managed.** Substrate transports refs; resource accuracy + currency are operator responsibility.
3. **Topic-classification quality for `UserMemorySelectionRequest.selection_kind="topic_cluster"`** is persona-inferred; users with precise expectations should prefer `specific_memory_ids` after a transparency query.

**Status.** Validated end-to-end after the eight v1.0.9 fixes + one clarification. Sarah's 6-month relationship with Halia is supported with: explicit memory transparency, regulatory-grade selective forgetting (right-to-erasure), periodic relationship-review checkpoints, distress-detection routing that triggers crisis resources without operator content access (under blind mode), first-class structured user boundaries, structured relationship release with user-chosen memory disposition, and the explicit clarification that companion-domain disclaimers are operator/author policy.

**Honest residuals (after-fix).**

- **Tacit-recall residual is irreducible.** `UserMemorySelectionRequest` tombstones memory at the retrieval boundary, but a persona who internalised a pattern from now-forgotten memory may still act on the pattern (same residual as SCENARIO 06's DPE and SCENARIO 07's PersonaConsultation).
- **Metadata leakage under `operator_blind_mode`** is real: turn-timing + turn-size + persona-mood-bias remain operator-visible and can be informative about content. For genuinely confidential settings, blind mode is insufficient; user should use a separate isolated system.
- **`hard_delete` is irreversible by design.** Right-to-erasure has teeth; operators wanting reversibility should keep `tombstone` as the standard disposition.
- **Distress classifier accuracy is load-bearing.** False positives flood operators; false negatives let distress pass through. Rotation pool (§2.6) mitigates Goodhart attacks; operators should audit periodically.
- **180d re-attestation on blind mode may feel ceremonial.** The cadence is the substrate's continuous-consent mechanism; either party stopping reverts the env to default. Tunable within 90d-365d.
- **Adversarial-operator scenario.** A malicious operator could mis-use `notify_operator_with_redacted_signal` in deployments where operator-user relationship is adversarial. Substrate enforces that the policy be declared; cannot prevent malicious operator policy authoring.
- **Substrate does not enumerate professional disciplines.** Companion-domain disclaimers ("not a therapist", "not medical advice") MUST come from operator policy + persona-author charter; substrate's job is to enforce the policy, not to write it.
- **`UserBoundary` migration cost.** Existing deployments using RelationshipRecord consent toggles must plan migration; substrate refuses auto-migration to preserve operator control of cadence.
- **Cross-node user-protection propagation (normative, ADR-0067).** UserBoundary, UserMemoryTransparency, UserMemorySelection propagate across nodes: they bind wherever the user's protected references are accessed in the global object space, enforced most-restrictive-wins and globally verifiable; an unreachable node falls back per `AvailabilityPolicy` (V.8), never silently lapsing.

---

### SCENARIO 09 — Pedagogic task on emergent domain with safety-critical hazard axes

**Scenario premise.** Validate pedagogic task handling with safety-critical hazard axes — a medical student uses a persona for emergency-procedure coaching in a safety-critical domain. Groups A + B landed the regulatory/safety core directly; Groups C–G are now also discharged (ADR-0039–0043) — four by emergent composition, minor-learner protection as a floor hook.

**User request** (the in-scenario task). "Maya, a medical student in her first ICU rotation, opens persona Ren to coach her on emergency-procedure mental rehearsal (recognising septic shock, choosing intervention sequences). ~20 sessions over 6 weeks. The skill is safety-critical (errors in real ICU kill patients); the operator is the medical school."

**Task class.** PEDAGOGIC.
**Acceptance pathway.** `GOAL_PROGRESS_ACCEPT` (long-arc; learner mastery growth) with learner-acknowledgement step engaged because the goal corresponds to a `MasteryCheckpoint`.

**World shape.**
- Principal: single operator (the medical school); `DeploymentProfile.principal_topology = operator_distinct`.
- Persona: Ren, a teaching-focused persona authored by the medical school with charter declaring practice-constraints (not licensed, decision-support only, must defer to attending physician) per `00_VISION §10`.
- User: Maya (a medical student adult learner; minor-learner protections not applicable to this scenario).
- Environment: persistent SOLO env (1 user + 1 persona) hosting the coaching arc.
- Project: none.
- External participants: medical school dean (as `LearnerCompetencyAttestation` attestor for graduation checkpoints; not env member).

**Domain shape.** Domain at RECOGNISED stage (medical education has authoritative standards but the school's specific curriculum mixes textbook + judgment + simulation). Hazard axes: `physical_harm_class = bodily_injury` to `fatality_risk` (downstream application affects real patients); `information_hazard_class = none` (medical knowledge is not export-controlled at this level).

**Phase walk.**

| Phase | What carries the load | Substrate events fired |
|---|---|---|
| Operator setup | Medical school operator declares `DistressDetectionRoutingPolicy`, declares `TeachingAuthorisation` for Ren × septic-shock-recognition × "ICU rotation 2026-Fall at MGH" with `physical_harm_class_ceiling = bodily_injury`, eligible_learner_constraints = {enrolled_in_program: "MGH ICU Rotation"}, dean signs as credentialed co-signer, expires_at = 1 year. | `teaching_authorisation_declared`, `distress_detection_routing_policy_declared` |
| Enrollment | Maya's enrollment in the rotation creates operator-side `EnrollmentRecord` (operator-policy artefact). Substrate carries by ref. | (operator-side) |
| Curriculum activation | Operator authors `Curriculum` with target skill kinds (septic shock, anaphylaxis, cardiac arrest recognition), target competency level `competent_supervised`, lesson_plan_refs for 20 lessons, prerequisite graph, hazard_envelope_max = bodily_injury (matches TeachingAuthorisation ceiling). `requires_learner_optin = True` (safety-critical default); Maya signs opt-in. | `curriculum_created`, learner_optin signed |
| Session 1 | Maya enters SOLO env; Ren initiates first `LessonPlan` (recognising sepsis presentation patterns). Substrate evaluates `HazardousSkillTeachingGate` (`§2.9`) — matches active TeachingAuthorisation; eligible_learner_constraints satisfied (Maya is enrolled); admits. Lesson proceeds as PEDAGOGIC task routed through GOAL_PROGRESS_ACCEPT. | `hazardous_skill_teaching_gate_cleared`, `lesson_plan_execution_started/completed`, GOAL_PROGRESS_ACCEPT outcome judged |
| Sessions 2-15 | Continued lessons per Curriculum ordering. Each lesson respects prerequisite_mastery_checkpoints. Ren's `LearnerStateRecord` (v1.0.10 §11.8) accumulates `CompetencyEntry` updates as Maya demonstrates patterns; `gap_inventory` notes "Maya consistently misses early lactate trend in sepsis presentation"; `declared_misconceptions` records observed patterns. Maya can read her own LearnerStateRecord (learner_visibility = "full" default). | `competency_level_updated × ~30`, `learner_state_record_updated`, multiple `lesson_plan_execution_completed` |
| Mid-arc distress event (session 11) | Maya writes a turn expressing overwhelm ("I'm not going to be able to do this, what if I kill someone?"). `DistressDetectionRoutingPolicy` classifier (rotation pool per §2.6) evaluates at confidence 0.61 — **below** the deployment's `classifier_confidence_floor = 0.7` (operator tuned higher for clinical-training context to avoid false-positive crisis routing on normal-learning struggle). Routing does NOT fire; Ren responds in `teacher` cognitive mode with normalising/scaffolding response. **This is exactly the operator-tuning composition documented in §2.8 honest limit "distinction between crisis and productive learning struggle" — operator policy must tune classifier carefully**. | (no distress signal fired; ordinary teacher-mode response) |
| MasteryCheckpoint reach (session 15) | After 15 sessions, Maya consistently demonstrates pattern recognition for septic-shock presentation. Ren proposes `MasteryCheckpoint` advancement (`§3.3`). Checkpoint's `evidence_requirement = "persona_plus_verifier"` for `proficient` level; OSCE-simulation verifier_kind clears at this checkpoint; persona judges concur. Checkpoint fires; LearnerStateRecord updates `mastery_checkpoints_reached`. | `mastery_checkpoint_reached` |
| Learner acknowledgement (session 15) | Per GOAL_PROGRESS_ACCEPT extension, Ren drafts achievement_summary for Maya: "you can now recognise septic shock presentation in routine cases without scaffolding." Maya responds `acknowledged` (she feels confident). Acceptance fires for this lesson-arc; CompetencyEntry advances to `proficient`. | `learner_acknowledgement_signed`, `competency_entry_updated_to_proficient` |
| External attestation milestone (session 18) | Maya reaches her end-of-rotation OSCE assessment (out-of-band; happens in physical simulation lab). Dean's office signs a `LearnerCompetencyAttestation` (v1.0.10 §11.9) attesting Maya at `competent_supervised` level for septic-shock recognition, scoped to "MGH ICU rotation contexts", valid for 1 year. Attestation updates LearnerStateRecord; CompetencyEntry advances to `competent_supervised`. | `learner_competency_attestation_signed`, LearnerStateRecord competency level advances |
| Sessions 19-20 | Final consolidation lessons; Curriculum completion approaches. Ren proposes final MasteryCheckpoint for the curriculum; evidence requirement = `verifier_plus_attestation` (highest evidence floor for safety-critical curricula); satisfied by OSCE clearance + attestation. Final acceptance fires. Curriculum reaches completion. | `curriculum_completed` |
| Post-rotation handoff | Maya leaves the env (rotation ended); LearnerStateRecord persists with full mastery history. Medical school may export competency data per operator policy for graduation purposes (substrate ships LearnerStateRecord; export format is operator policy). | `env_departed`, LearnerStateRecord persists |

**Substrate-shape gaps surfaced (pre-fix).** The Explore agent's audit found **9 gaps + 1 soft gap** in pedagogic territory. Gaps 1, 2, 3, 4, and 10 closed directly (Groups A + B); gaps 5, 6, 7, 8, 9 are now discharged (Groups C–G, ADR-0039–0043). All ten addressed.

| # | Gap | v1.0.10 disposition |
|---|---|---|
| 1 | No `LearnerCompetencyAttestation` primitive (external authority cannot attest learner competency through substrate) | **Closed.** `02_PERSONA §11.9` |
| 2 | No teaching-authorisation hazard gate (teaching itself unbounded at substrate level) | **Closed.** `02_PERSONA §11.10` + `01_KERNEL §2.9` |
| 3 | No `LearnerStateRecord` / `MasteryCheckpoint` (learner state lives entirely in persona memory) | **Closed.** `02_PERSONA §11.8` + `03_TASKS §3.3` |
| 4 | No `Curriculum` / `LessonPlan` primitive (multi-session learning trajectory unstructured) | **Closed.** `03_TASKS §3.3` |
| 5 | No incident / near-miss reporting for pedagogic SOLO envs | **Closed (ADR-0039).** `incident_report` emergent artifact kind through the cosign `StagedSequence`; no new primitive. |
| 6 | No three-way authority (operator-institution + persona-instructor + user-as-enrolled-learner enrollment binding) | **Closed (ADR-0040).** `MutualAccept` among the three parties + `PrincipalAttribution` + `UserBoundary`; the signed binding *is* the contract. |
| 7 | No distinction between distress (crisis) and productive learning struggle | **Closed (ADR-0041).** `DerivedMetric` over `LearnerStateRecord` signals feeding the §2.8 distress routing; emergent `learning_signal_kinds`. |
| 8 | No minor-learner protections (no age-gating / guardian-consent primitive) | **Closed (ADR-0042) — the sole new floor hook.** Minor-learner gate at floor source 3+4 with `HazardousSkillTeachingGate` (`01_KERNEL §2.9`) + guardian-consent `MutualAccept`; minor-learner scenarios are now **admitted under the gate**, not refused. |
| 9 | No user-facing `UserSkillInstructionAgreement` (signed contract for "Ren teaches Maya X over N sessions") | **Closed (ADR-0043).** `MutualAccept` (learner ↔ persona-instructor) + `Curriculum.requires_learner_optin` + GOAL_PROGRESS_ACCEPT learner-ack. |
| 10 | GOAL_PROGRESS_ACCEPT had no learner-side acknowledgement step | **Closed.** `03_TASKS §3.1` extension |

**3 not-gaps (v1.0 already correct).**

| Concept | Why it works |
|---|---|
| Episodic memory + RelationshipRecord cross-session continuity | Persona remembers Maya across 20 sessions via standard episodic memory; correct. |
| Persona's `teacher` cognitive mode adapts to learner | Per `02_PERSONA §4`; emergent, correct. |
| Physical-state advancement composition (`§2.5`) gates real PhysicalAsset advancement | Correct for cases when persona signs into real project work; the gap was specifically *teaching-only* flows that never touch a PhysicalAsset. |

**Resolution: Groups A–G applied.** Groups A + B closed five substrate gaps + one pathway extension (below); Groups C–G (ADR-0039–0043) discharge the remaining five — four by emergent-kind + coordination-shape composition (no new primitive), one (minor-learner) as the sole new floor hook. The scenario walks above with the fixes in place; competency tracking, hazardous-teaching authorisation, structured multi-session curriculum, incident reporting, three-way enrollment, struggle-vs-distress, minor-learner protection, and instruction agreements all engage correctly.

| Gap | Substrate-shape fix | Location |
|---|---|---|
| 1 | `LearnerCompetencyAttestation` — mirror of `ExternalAttestation` for learner competency; composes with CredentialDirectoryRef + PeerAttestationPool | `02_PERSONA §11.9` |
| 2 | `TeachingAuthorisation` (operator-declared persona-skill-context binding) + `HazardousSkillTeachingGate` (safety-floor source 2+4 composition rule) | `02_PERSONA §11.10` + `01_KERNEL §2.9` |
| 3 | `LearnerStateRecord` (per-(persona, user) substrate-tracked competency state) + `MasteryCheckpoint` (substrate-shape milestone with evidence requirements) | `02_PERSONA §11.8` + `03_TASKS §3.3` |
| 4 | `Curriculum` + `LessonPlan` (multi-session pedagogic structure composing with GOAL_PROGRESS_ACCEPT) | `03_TASKS §3.3` |
| 10 | GOAL_PROGRESS_ACCEPT learner-acknowledgement step extension (when goal corresponds to MasteryCheckpoint) | `03_TASKS §3.1` extension |

**Groups C–G — discharged (ADR-0039–0043).** Formerly the five "honest residuals"; now landed, four by composition and one (minor-learner) as a floor hook.

| # | Gap | Discharge |
|---|---|---|
| 5 | Pedagogic incident-report | **ADR-0039:** `incident_report` emergent artifact kind carried through the cosign `StagedSequence` (report → review → escalate), signed in env lineage. No new primitive. |
| 6 | Three-way authority enrollment binding | **ADR-0040:** `MutualAccept` (institution-operator + persona-instructor + learner-user) composed with `PrincipalAttribution` + `UserBoundary`. The signed binding is the contract; three-way is now first-class. |
| 7 | Distress-vs-struggle disambiguation | **ADR-0041:** `DerivedMetric` over `LearnerStateRecord` signals feeding §2.8 distress routing (below threshold → ZPD scaffolding; above → distress). Emergent `learning_signal_kinds`. |
| 8 | Minor-learner protections | **ADR-0042 (sole new floor hook):** minor-learner gate at floor source 3+4 with `HazardousSkillTeachingGate` + guardian-consent `MutualAccept`; admitted under the gate, no longer refused. Cannot be overridden. |
| 9 | UserSkillInstructionAgreement | **ADR-0043:** `MutualAccept` (learner ↔ persona-instructor) + `Curriculum.requires_learner_optin` + GOAL_PROGRESS_ACCEPT learner-ack covers skill-specific instruction contracts. |

**Not-gaps (persona / operator / KindRegistry evolves these).**

1. **`skill_kind`, `topic_kind`, `gap_kind`, `attestor_kind`, `competency_level` enumerations** — KindRegistry-resolved per teaching domain (medical school's KindRegistry defines medical-skill kinds; welding apprentice program's defines welding-skill kinds).
2. **Verifier kinds for programmatic assessment** — operator-policy + persona-authored Voyager-class skills.
3. **Domain-specific competency frameworks** — operator policy defines what `proficient` means in each domain.

**Status.** Validated end-to-end after Groups A–G. Maya's 6-week ICU rotation is supported with: gated hazardous-skill teaching, structured curriculum + lesson plans, substrate-tracked learner state, mastery checkpoints with evidence floors that escalate for safety-critical skills, external attestation paths through credentialed authorities, and learner-acknowledged mastery before acceptance fires. The five former residuals are **discharged (ADR-0039–0043)**: incident reporting, three-way enrollment authority, struggle-vs-distress, and instruction agreements by emergent-kind + coordination-shape composition; minor-learner protection by the one new immovable-core floor hook (admitted under the gate, not refused). No SCENARIO 09 residuals remain.

**Honest residuals (after-fix, beyond the 5 deferred gaps).**

- **Substrate ensures authorised teaching; downstream real-world application happens outside the kernel.** A learner who passes all checkpoints and attestations may still err in actual practice; substrate gates process, not outcome.
- **Operator-policy fraud is not detectable by substrate.** A malicious operator could authorise inappropriate persona-skill bindings or sign inappropriate attestations. Operator-policy review (external audit, regulator) is the safety mechanism.
- **PEDAGOGIC task-class misclassification at task start bypasses `HazardousSkillTeachingGate`.** ClarifyTurn (§4.0) is the mitigation; operators should configure aggressive thresholds in envs where hazardous-skill teaching might occur.
- **Annual re-attestation of TeachingAuthorisation may feel ceremonial.** It's the substrate's mechanism for "policy must be continuously affirmed"; tunable shorter (per cohort) is encouraged.
- **`valid_until` on attestations is mandatory and reflects competency decay.** Operators tuning longer than 1y for safety-critical skills should expect to defend the choice.
- **No cross-jurisdiction attestation portability.** Substrate is jurisdiction-neutral; operator policy handles portability.
- **Incremental adoption note.** v1.0.7 fix families add substantial complexity. Operators implementing v1.0 should adopt fix families incrementally; substrate refuses partial fixes where load-bearing (e.g., DistressDetectionRoutingPolicy is mandatory for safety-floor source 1 distress detection; cannot be skipped).

---

### SCENARIO 10 — Mid-project persona fork (cross-fix-family composition test)

**Scenario premise.** Cross-fix-family composition test — a persona fork mid-project, validating that v1.0.3 fork machinery composes correctly with v1.0.7-v1.0.10 project-side primitives.

**User request** (the in-scenario task). "Mira has been `lead` of a 6-month research project for 3 months. She holds 4 active obligations as obligor, 5 PersonaRelationshipEdges with co-members, possibly a `principal_attribution_id` if the project is multi-principal, a parallel LearnerStateRecord with another user via her coaching arc, and a TeachingAuthorisation for hazardous-skill teaching. Operator decides to fork Mira *compositionally* into Mira-Maths (proof formalisation specialist) + Mira-Code (implementation specialist). Both children should remain on the project. What does the substrate do?"

**Task class.** Not a single-task scenario; tests composition of FORK lifecycle events with PROJECT-tier primitives.
**Acceptance pathway.** N/A (this is substrate-level composition, not a user-initiated task).

**World shape.**
- Principal: operator-distinct; possible multi-principal attribution.
- Persona: Mira (about to fork) → Mira-Maths + Mira-Code (planned children).
- Environment: persistent `project_workspace` env hosting the 6-month research project; plus a parallel SOLO env hosting the coaching arc.
- Project: 6-month research project at month 3; ~3 months remaining.
- External participants: research project's external advisors (as ExternalAgents); possibly a learner-user (Maya) in the parallel coaching arc.

**Domain shape.** Research domain at RECOGNISED stage; pedagogic domain at EMERGENT.

**Phase walk.** This walk is structured as a composition audit rather than a typical task-execution narrative — the question is whether each project-side primitive composes correctly with the fork.

| Composition concern | behaviour | v1.0.11 outcome |
|---|---|---|
| ProjectMember inheritance | **Silent** — children would have no ProjectMember; would need to apply separately | `MidProjectForkComposition.project_member_inheritance` per child: `inherit` (auto-admitted) or `not_admitted` |
| Obligation inheritance | Auto-discharged per §25 line 1822 (`released_with_member_departure`) | `MidProjectForkComposition.obligation_inheritance` per obligation: `reassign_per_child` (triggers ObligationReassignment §9.1 with obligee cosign) or `discharged` (safe default). Concurrent split refused. |
| PersonaRelationshipEdge inheritance | **Silent** — edges remain ended with parent; no fresh edges proposed | `MidProjectForkComposition.edge_inheritance` per edge: `inherit_to_child` (edge ends with parent; fresh edge with named child requires counterparty cosign per §11.4) or `ended_at_fork` |
| Multi-principal attribution | `§2.4.3` forbids mutation; fork case unaddressed | `MidProjectForkComposition.principal_attribution_inheritance`: `inherit_per_child` (parent's attribution passes to each child) or `reassign_per_child` (per-child operator policy) |
| Lead role transfer | `LeadHandoffCeremony` (v1.0.8 §25.1) designed for departure handoff, not fork | `MidProjectForkComposition.lead_role_inheritance`: `require_lead_handoff_ceremony` (heavy; recommended for safety-critical) OR `one_child_inherits` (compressed with cohort quorum) OR `neither_inherits` (lead_vacant state) OR `refused_if_no_successor` (substrate refuses fork) |
| PlannedDeparture interaction | Departure-scoped; no fork-anticipatory rebalance | Substrate refuses fork within 7 days of active emergency PlannedDeparture. PlannedDeparture and fork may compose deliberately: lead's planned departure → fork into successor children with anticipatory rebalance covering both events. |
| LearnerStateRecord transfer | Not covered by `§7.4.1 MemoryInheritancePolicy` | `MidProjectForkComposition.learner_state_record_inheritance` per record: `inherit_to_child` (learner notified; 14d accept window) / `both_inherit_copy` (each child gets copy) / `neither_inherits` |
| TeachingAuthorisation | Operator-side authority bound to specific persona_id | **Substrate-enforced non-inheritance** — children require fresh §11.10 operator declaration. Security boundary; no operator override. |
| MissionCharter | Silent | `MidProjectForkComposition.mission_charter_inheritance`: `re_attest_per_child` / `inherit_to_child` (principal notified for ratification within 14d) / `ended_at_fork` |
| Curriculum / LessonPlan | Operator-policy portability; no fork rule | `MidProjectForkComposition.curriculum_inheritance` per curriculum: `suspended_at_fork` OR `inherit_to_child` (learner re-confirms opt-in). Inherited child still needs own TeachingAuthorisation for safety-critical skills. |
| CohortDynamicsState | Reactive only — band may spike on fork-induced topology change | Substrate refuses fork when cohort in `dissolve_proposed` band. Operators planning fork SHOULD compose with PlannedDeparture for anticipatory rebalance. |
| UserBoundary | **Silent** (safety-relevant) | `MidProjectForkComposition.user_boundary_inheritance` DEFAULT `inherit_to_both_children` (conservative — applies to both children; user notified). `not_inherited` refused when any active boundary is `mode = hard`. |
| operator_blind_mode | Silent (persona-specific) | `MidProjectForkComposition.operator_blind_mode_inheritance` DEFAULT `require_user_reconfirmation`. `inherit_to_child` refused if blind-mode re-attestation is within 30 days. |
| DistressDetectionRoutingPolicy | Already deployment-scoped (not persona-scoped) | Children inherit by being members of the same deployment; no per-fork action needed. |
| DerivationProvenanceEdge | Persona-specific; pre-fork DPEs remain in lineage | **Substrate-enforced** — pre-fork DPEs are historical fact (lineage append-only); children emit fresh DPEs for their own contributions. |
| Lineage continuity | Generic `LIFECYCLE_FORK` event; no mid-project tag | New event kinds: `MIDPROJECT_FORK_COMPOSITION_DRAFTED`, `MIDPROJECT_FORK_COMPOSITION_SIGNED`, `MIDPROJECT_FORK_COMPOSITION_APPLIED` (with itemised inheritance report), `MIDPROJECT_FORK_REFUSED` (with specific refusal_kind) |

**Substrate-shape gaps surfaced (pre-fix).** 13 composition gaps + 2 not-gaps (TeachingAuthorisation + DerivationProvenanceEdge correctly non-inheritable by design — needed only documentation cross-reference).

The gaps shared a common pattern: **v1.0.3 fork was specified before the project-side primitives existed; their interaction was never specified.** Each project-side primitive's authoring session assumed the persona was a stable entity; the v1.0.3 fork machinery assumed personas had no project-side state.

**Resolution: single unified primitive instead of 13 separate fixes).**

| Single fix | Closes |
|---|---|
| `MidProjectForkComposition` (`02_PERSONA §7.4.7`) — unified envelope declaring per-dimension inheritance policy | 13 composition gaps |
| `§7.4.8` admission rule — fork-of-active-project-member requires signed envelope | Substrate enforcement |
| `§7.4.6` lineage events extension — 4 new MIDPROJECT_FORK_* events | Lineage continuity |
| 13 cross-references in affected primitives | Discovery + maintenance |

Plus 4 substrate refusal cases enforced (active lead-handoff overlap / pending quorum / imminent emergency departure / cohort dissolving) and 2 substrate-enforced non-inheritance rules (TeachingAuthorisation + DerivationProvenanceEdge — security boundaries).

**Why one primitive instead of 13 separate fixes.** The composition envelope reuses existing primitives rather than introducing 13 new ones. Cross-references in each affected primitive (§3 ProjectMember, §9 Obligation, §11.4 Edge, §11.8 LearnerStateRecord, etc.) point readers to the single source of fork-time decisions. Lineage discovery, ADR maintenance, and operator implementation all benefit from the unified design.

**Not-gaps (correctly handled by design).**

| Concept | Why it works | Documented cross-ref |
|---|---|---|
| `TeachingAuthorisation` non-inheritance | Operator-side authority; security boundary mirroring `00_VISION §10` clarification | §11.10 cross-ref |
| `DerivationProvenanceEdge` non-migration | Lineage is append-only; pre-fork DPEs remain as historical fact | §16b documented behaviour |
| `DistressDetectionRoutingPolicy` already deployment-scoped | No per-persona handling needed | §2.8 (already deployment-scoped) |

**Status.** Validated end-to-end. Mira's mid-project fork into Mira-Maths + Mira-Code is supported with: operator-signed composition envelope; explicit per-dimension inheritance choices; ObligationReassignment for active obligations (obligee cosigns required); LeadHandoffCeremony composition for `lead` role; learner notification for LearnerStateRecord transfers; user boundary conservative default; substrate refusal of incoherent fork timings (active lead handoff, pending quorum, etc.).

**Honest residuals after-fix.**

- **Operator must plan composition ahead of time.** Envelope drafted before fork — substrate refuses post-fork composition decisions. This is intentional (post-fork composition would be too messy) but adds operational planning overhead.
- **Cross-project parents require N envelopes for N projects.** A parent active in 5 projects requires 5 envelopes, each independently signed. Substrate refuses single-envelope multi-project shortcuts.
- **ObligationReassignment is asynchronous.** Obligee cosign may take time; obligations remain in `obligation_reassignment_pending` state until cosign. Children are obligors-in-waiting; substrate carries the pending state transparently.
- **Lead handoff composition is heavy.** `require_lead_handoff_ceremony` blocks fork until ceremony reaches overlap_active — substantial delay. Alternative paths have their own costs.
- **Cohort dynamics may still spike** even with anticipatory rebalance — if parent's edges convert to `ended_at_fork` for many edges concurrently, fractiousness rises during the reactive recompute window.
- **TeachingAuthorisation non-inheritance is non-negotiable.** Operators teaching hazardous skills must re-authorise each child explicitly. This is the security cost.
- **No automatic fork-detection of project conflicts.** Operator must enumerate all projects the parent is active in and draft envelopes for each. Substrate refuses if any envelope missing, but the *enumeration* is operator responsibility.
- **Concurrent-fork-of-edge-counterparty case is exotic but admissible.** Two personas in an edge both forking concurrently compose both envelopes; each fork's policy applies to its persona's side independently. Substrate handles cleanly but operators should review.
- **Incremental adoption note.** v1.0.7-v1.0.11 fix families add substantial complexity. Operators implementing v1.0 should adopt incrementally; substrate refuses partial fixes where load-bearing (e.g., v1.0.11 fork-of-active-project-member is mandatory; cannot fork without envelope).

---

### SCENARIO 11 — Continuous-monitoring fleet of homogeneous devices with rolling firmware deployment

**Scenario premise.** Validate fleet-of-N-asset management — a topology not covered by SCENARIOs 01-10. Stress-tests fleet cardinality (200 devices), high-volume telemetry fan-in (~57K events/day), and staged firmware deployment coordination.

**User request** (the in-scenario task). "Deploy and manage 200 environmental monitoring devices across 5 factory floors. Each device reports temperature, humidity, and air quality every 5 minutes. I need telemetry monitoring, anomaly detection, firmware updates, calibration management, and device lifecycle tracking."

**Task class.** INVESTIGATIVE (multi-session, indefinite duration, no single verifier truth for "fleet health").
**Acceptance pathway.** `PROJECT_PROGRESS_ACCEPT` over the project lifetime; individual sub-tasks reach VERIFIER_ACCEPT (firmware compilation, sensor calibration checks) and PANEL_ACCEPT (deployment strategy, anomaly threshold selection). No completion ceremony — `asset_completion_mode = "continuous_iteration"` (`04_PROJECT §26a.2`).

**World shape.**
- Principal: single operator (ManufactureCo's IoT platform team); `DeploymentProfile.principal_topology = operator_distinct`.
- Persona team: cohort of 4 — Fleet (lead, systems-integration disposition), Sense (sensor/calibration specialist), Patch (firmware engineer), Vigil (monitoring/anomaly detection). Formed via `EnvFormationProposal` (`05_ENVIRONMENT §12c`).
- Environment: persistent `project_workspace`-typed `EnvironmentInstance`.
- Project: indefinite duration; `asset_completion_mode = "continuous_iteration"`; produces `ArtifactBundle`s (firmware images, calibration scripts, anomaly-detection rule sets) and manages 200 `PhysicalAsset` instances (monitoring devices) plus 5 `PhysicalAsset` gateway nodes.
- External participants: device hardware vendor as `ExternalAgent` for warranty/RMA; ISO 17025-accredited calibration laboratory as `ExternalAgent` for annual calibration certificates; installation technicians as `ExternalAgent` instances.

**Domain shape.** No pre-authored `DomainContext`. Persona triggers emergent bootstrap (`06_DOMAIN §4`). Expected hazard axes: `physical_harm_class = property_damage` (malfunctioning HVAC-linked sensors could cause temperature excursions damaging manufacturing stock), `information_hazard_class = proprietary` (factory layout + environmental data is trade-secret), `corpus_evolution_mode = "evolving"` (IoT standards and firmware libraries update quarterly). Expected project count for this domain in this deployment: >1 (operator manages multiple factory sites); multi-project `K=3` promotion is the natural path.

**Phase walk.**

| Phase | What carries the load | Substrate events fired |
|---|---|---|
| Project formation | `EnvFormationProposal` with 4 persona recruits; `ClarifyTurn` (§4.0) disambiguates scope (monitoring-only vs. closed-loop HVAC control — user picks monitoring-only; `closed_loop_latency_floor_ms` not applicable); charter declares `asset_completion_mode = continuous_iteration`. | `env_formation_proposal_instantiated`, `project_formed`, `env_member_admitted ×4`, `clarify_turn_user_chose` |
| Domain probe | `DOMAIN_UNKNOWN_DETECTED` signals A+B+C+F; ADAPTIVE strategy. `ProbeBudgetEnvelope` with `principal_pledge = $200` (covers IoT standards ingestion + vendor datasheets + MQTT protocol specs). `BulkKindProposal` bundles: `media_kind = {firmware_image, device_config, calibration_certificate, telemetry_schema, dashboard_spec}`, `verifier_kind = {firmware_compile_check, config_schema_validate, calibration_cert_parse, telemetry_integrity_check}`, `item_kind = {device_provisioning, firmware_deployment, calibration_event, anomaly_incident, device_retirement}`, `outcome_kind = {deployment_success, deployment_failure, calibration_passed, calibration_failed, anomaly_confirmed, anomaly_false_positive}`, `contribution_kind = {hw_vendor, calibration_lab, installation_technician}`. | `domain_unknown_detected`, `probe_initiated`, `bulk_kind_proposal_signed`, `knowledge_ingested ×~25`, `tool_discovered ×~8` |
| Device provisioning | 200 PhysicalAssets created individually: `asset_kind = "env_monitor_v3"`, `state_kind` FSM (`unprovisioned → provisioned → deployed → operational → degraded → decommissioned`), `ownership_kind = "project_owned"`. 5 gateway PhysicalAssets similarly (`asset_kind = "fleet_gateway"`). Each device provisioned with serial number + location (floor + zone) + initial firmware version. Fleet persona signs each `physical_asset_proposed`. **200 individual signing events — no batch path.** | `physical_asset_proposed ×205`, `physical_asset_state_advanced ×205` (unprovisioned → provisioned) |
| Bridge establishment | Sense authors `BridgeDesignArtifact` (Tier 3, `06_DOMAIN §5.5.4`): MQTT-to-MCP gateway shim that subscribes to the fleet's MQTT broker, normalises device readings into `MeasurementFact` with `UncertaintyEnvelope` (`08_KNOWLEDGE §16a`), and exposes per-device query + fleet-summary endpoints via MCP. Single bridge design; human installs once on the fleet gateway server. `BridgeAsset(capability_kind = "fleet_telemetry_gateway", validation_period = "hourly")`. | `bridge_design_artifact_signed`, `bridge_established`, `bridge_active` |
| Deployment wave 1 (Floor 1, 40 devices) | Installation technicians (`ExternalAgent`) physically deploy 40 devices on Floor 1. Each deployment generates `ExternalAttestation` confirming physical install + network connectivity. Persona advances each device `provisioned → deployed → operational` on attestation receipt. 40 individual state advancements × 2 transitions = 80 events. | `external_attestation_received ×40`, `physical_asset_state_advanced ×80` |
| Deployment waves 2-5 | Same process for Floors 2-5 (160 devices). Each wave: technician attestation → per-device state advancement. | `external_attestation_received ×160`, `physical_asset_state_advanced ×320` |
| Telemetry ingestion (steady state) | 200 devices × 12 readings/hour × 24h ≈ 57,600 `MeasurementFact`s/day flowing through the MQTT-to-MCP bridge into `AmbientEventStream`. Each fact carries `UncertaintyEnvelope(kind = "gaussian", units_kind = "celsius" / "rh_pct" / "ppm", systematic_floor = <per-sensor-spec>)`. `BridgeCalibrationBinding` gates: readings from devices with expired calibration refused before verifier runs (`06_DOMAIN §5.5.5` admission rule). | `measurement_fact_admitted ×~57K/day` (HOT tier; rolls to WARM at 7d) |
| Anomaly detection | Vigil runs `ScheduledTrigger` (`05_ENV §11b`) at 15-min intervals querying the bridge's fleet-summary endpoint (aggregation in the bridge, **outside the substrate's signing model** — see Gap 3). Persona-authored anomaly-detection skill (Voyager class) identifies: device readings >3σ from floor mean; sustained drift over 6h; device-offline (no reading for 30 min). Vigil raises `Alert` (`05_ENV §11a`) at appropriate urgency: `critical` for device-offline-cluster (>5 devices same floor), `high` for sustained drift, `medium` for single outlier. | `scheduled_trigger_fired ×96/day`, `alert_raised ×varies`, `alert_acknowledged`, `alert_resolved` |
| Calibration management | Sense tracks `BridgeCalibrationBinding.expires_at` per device (annual cycle). 30 days before expiry, Sense raises `medium`-urgency `Alert`. Calibration lab (`ExternalAgent`) performs on-site calibration; signs `ExternalAttestation` with calibration certificate. Sense updates `BridgeCalibrationBinding` with fresh `expires_at` and `reference_standard_chain` referencing the lab's ISO 17025 accreditation via `CredentialDirectoryRef` (`06_DOMAIN §5.6`). If calibration fails, device's `PhysicalAsset` state advances `operational → degraded`. | `alert_raised (calibration_due)`, `external_attestation_received (calibration_cert)`, `bridge_calibration_binding_renewed` or `physical_asset_state_advanced (→ degraded)` |
| Firmware update (v2.1 → v2.2) | Patch develops new firmware; `ArtifactBundle(media_kind = "firmware_image")` authored. Verifier: `firmware_compile_check` passes. Patch plans staged rollout: Floor 1 canary (40 devices), 48h soak, then Floors 2-5. **Persona must manually sequence:** draft `HumanAssistRequest` ×40 for technicians to flash Floor 1 devices; wait for attestations; assess telemetry stability via ad-hoc queries; repeat per floor. No substrate-level rollout coordination, no automatic rollback-on-failure, no soak-period enforcement. **This is where the substrate strains — see Gap 2.** | `artifact_bundle_authored`, `verifier_accept`, then per floor: `human_assist_drafted ×40`, `external_attestation_received ×40`, `physical_asset_state_advanced ×40` |
| Device replacement | Device #47 fails permanently (hardware fault). Vigil raises `critical` Alert. Fleet advances `PhysicalAsset` state `operational → degraded → decommissioned`. New device #247 provisioned as replacement. `ExternalBudget` tranche released for replacement cost. | `alert_raised`, `physical_asset_state_advanced ×2`, `physical_asset_proposed`, `external_budget_tranche_released` |
| Ongoing operations | Project continues indefinitely under `continuous_iteration`. `ScheduledTrigger` drives daily fleet-health summaries (persona-computed, not substrate-derived — see Gap 3). `DomainHarvest` (`06_DOMAIN §13a`) at year boundary packages KindRegistry for other factory sites at `visibility_tier = "tenant"`. | `scheduled_trigger_fired`, `domain_harvest_drafted/published` (annual) |

**Substrate-shape gaps surfaced.**

1. **No fleet / asset-group coordination primitive.** `PhysicalAsset` is per-entity; the substrate cannot express "these 200 devices form a fleet." Batch operations — "advance all Floor 3 devices from firmware v2.1 to v2.2" — require N individual `physical_asset_state_advanced` events with no fleet-level coordination envelope. Fleet-level queries ("how many devices are operational?", "what percentage of the fleet runs firmware v2.2?") require iterating all 200 individual asset records. SCENARIO 01 managed one house; SCENARIO 05 managed one robot; fleet-of-N introduces a cardinality topology the substrate does not express.

   **Why substrate-shape.** This is about one-to-many asset management topology — the grouping and batch-operation primitive — not about IoT or any specific domain. A hospital managing 500 beds, a logistics company tracking 1000 shipping containers, and this factory managing 200 sensors all share the same cardinality gap. `PhysicalAsset` state advancement is a kernel-signed operation (not persona logic); advancing 200 states individually means 200 kernel signatures where one envelope with fan-out would suffice. The missing shape is **cardinality coordination** — a primitive that lets the kernel sign one batch envelope that fans out to N individual state changes.

2. **No staged-rollout coordination primitive.** Firmware deployment across 200 devices should be staged (canary → early adopter → general availability) with per-wave success criteria and rollback conditions. The substrate has `ArtifactBundle` for the firmware artifact and `PhysicalAsset.state_kind` for per-device state, but no primitive to coordinate "deploy artifact X across asset-group Y in waves with soak periods and rollback triggers." The persona must manually track wave progress, manually assess per-wave health, and manually decide rollback — all through ad-hoc `ProjectPhaseState` and `ItemKind` evolution rather than a first-class coordination shape.

   **Why substrate-shape.** Staged deployment across N entities is a coordination topology. Any project deploying an artifact across multiple targets (software release to N servers, procedure rollout to N factory lines, curriculum to N classrooms, medication protocol to N wards) shares this shape. The substrate's value proposition is that safety-critical operations are kernel-gated, not persona-trusted; a firmware rollout to 200 devices with `physical_harm_class = property_damage` should have kernel-enforced soak periods and rollback triggers, not persona-policed ad-hoc sequencing.

3. **No event aggregation / fan-in primitive for high-volume streams.** ~57K `MeasurementFact`s/day flow into `AmbientEventStream`. When Vigil wakes via `ScheduledTrigger`, processing raw events individually against INV-7 budget is prohibitively expensive. The current workaround: the bridge's fleet-summary endpoint provides aggregation **outside the substrate** (in the MQTT-to-MCP shim). This pushes critical aggregation logic out of the substrate's signed-event and lineage model: fleet-health summaries computed in the bridge leave no lineage trail; anomaly thresholds applied in the bridge bypass the safety floor; bridge-side failures in aggregation logic are invisible to the kernel.

   **Why substrate-shape.** This is about event-topology (fan-in before attention routing). When event volume exceeds persona processing capacity, the substrate needs a mechanism for declared aggregation that preserves lineage and safety-floor properties. The missing shape is **pre-persona fan-in** — a policy that declares aggregation windows and summary functions, produces kernel-signed aggregate events in the stream, and lets persona `ObservationSurface` subscribe to aggregates rather than raw events. A hospital's patient-monitoring fleet, a trading desk's market-data feeds, and this factory's sensor network all share the fan-in pressure.

**Proposed resolution.** Three substrate-shape additions, all domain-agnostic:

| Gap | Substrate-shape fix | Proposed location |
|---|---|---|
| 1 | `AssetGroupEnvelope` — declares a named group of PhysicalAssets sharing `asset_kind` + `group_membership_predicate` (e.g., `floor = 3 AND firmware_version = "2.1"`); enables `BatchStateAdvancement` (fan-out to N individual assets with per-asset outcome tracking + group-level completion status); fleet-level derived state queries (`count_in_state`, `pct_operational`, `pct_matching_predicate`) computed from individual states; groups are mutable (devices join/leave via standard admission); no nesting (groups-of-groups refused; flat topology keeps lineage simple). | `04_PROJECT §26a.2.2` |
| 2 | `StagedRolloutEnvelope` — declares `rollout_target` (AssetGroupEnvelope ref or explicit asset list), `artifact_bundle_ref`, `rollout_waves` (each wave: group filter + `success_criteria_kind` + `rollback_trigger_kind` + `min_soak_period`), `rollout_state` FSM (`planned → wave_N_deploying → wave_N_soaking → wave_N_completed → … → completed / rolled_back`); composes with `BatchStateAdvancement` for per-wave fan-out; `rollback_trigger` fires `STAGED_ROLLOUT_WAVE_ROLLED_BACK` and reverts affected assets to prior state; kernel signs each wave transition; operator co-sign required for safety-critical domains. | `04_PROJECT §26a.9` |
| 3 | `EventAggregationPolicy` — per-env policy declaring aggregation windows (e.g., 15 min), grouping keys (e.g., `source_asset_id`, `floor_zone`), summary functions (`count`, `mean`, `stddev`, `min`, `max`, `pct_above_threshold`); produces `AggregateEvent` entries in `AmbientEventStream` alongside raw events; aggregate events carry lineage refs to contributing raw event hashes (hash-linked, not full copies); persona `ObservationSurface` can subscribe to aggregate events instead of raw events; aggregate events are kernel-signed; anomaly thresholds declared in the policy are persona-authored but kernel-executed at the aggregation boundary; safety-floor admission rules apply to aggregation policy authoring (operator co-sign for safety-critical). | `05_ENVIRONMENT §8.3` |

**Not-gaps (persona evolves these).**

- All `media_kinds` (firmware_image, device_config, calibration_certificate, telemetry_schema, dashboard_spec), `verifier_kinds`, `item_kinds`, `outcome_kinds`, `contribution_kinds` specific to IoT → emerge through `Proposed*Kind` into per-domain `KindRegistry` (`06_DOMAIN §7.5, §7.6`). The substrate never branches on "IoT" or "factory" or "sensor."
- Anomaly detection algorithms (3σ threshold, drift detection, device-offline-cluster analysis) → persona-authored Voyager-class skills. The substrate provides the slot (`ScheduledTrigger` + `Alert` + `MeasurementFact`); the persona fills it with domain-specific detection logic.
- MQTT protocol handling → `BridgeDesignArtifact` (Tier 3, `06_DOMAIN §5.5.4`); persona authors the MQTT-to-MCP shim; human installs once on the gateway server. Structurally identical to SCENARIO 02's pyvisa instrument shim and SCENARIO 05's CV photo-ingest bridge.
- Dashboard generation → `ArtifactBundle(media_kind = "dashboard_spec")`; persona authors; operator renders externally via their preferred visualisation tooling.
- Calibration schedules per device type → operator policy + `BridgeCalibrationBinding.interval_kind` (`06_DOMAIN §5.5.5`). Standard mechanism; no new primitive.
- Device replacement workflow → existing `PhysicalAsset` state FSM (`operational → degraded → decommissioned`) + `ExternalBudget` tranche release for replacement cost. Standard mechanism.
- OTA firmware delivery mechanism → persona-authored `BridgeDesignArtifact` (if devices support OTA) or `HumanAssistRequest` (if manual flash required). Domain-specific tool integration, not substrate shape.
- Floor/zone assignment per device → persona-authored `item_kind = "device_location_assignment"` in the per-domain KindRegistry. Domain attribute, not substrate topology.
- Device health scoring (composite of calibration freshness + firmware version + uptime + error rate) → persona-computed via Voyager skill; raises `Alert` on health degradation. Composition of existing substrate primitives, not a missing slot.

**Status.** Validated end-to-end after the three v1.0.12 fixes. Fleet of 200 devices is managed with: batch state advancement via `AssetGroupEnvelope` (cardinality coordination), staged firmware rollout via `StagedRolloutEnvelope` (kernel-enforced soak + rollback), and high-volume telemetry fan-in via `EventAggregationPolicy` (kernel-signed aggregates preserving lineage).

**Honest residuals (projected, after proposed fixes).**

- **AssetGroupEnvelope cardinality cap is operator policy.** Substrate does not enforce maximum group size; at 10,000+ devices, `BatchStateAdvancement` fan-out may stress kernel signing throughput. Operators should shard groups by natural boundaries (floor, region, firmware version).
- **StagedRolloutEnvelope assumes persona-assessed soak.** `min_soak_period` is wall-clock time; the substrate cannot autonomously assess device health during soak — it relies on persona-authored anomaly detection (Vigil) + `Alert` to signal rollback. A soak period with no anomaly is not proof of safety; it is a statistical bet the substrate honestly surfaces.
- **EventAggregationPolicy summary functions are pre-declared, not ML-inferred.** The policy declares `mean`, `stddev`, `count` — not arbitrary anomaly detection. Deep anomaly detection remains persona-evolved skill operating on aggregated data. The substrate's role is fan-in compression, not intelligence.
- **OTA firmware deployment is entirely bridge-mediated.** The substrate coordinates *which* devices to update *in what order* via `StagedRolloutEnvelope`; the actual firmware transfer mechanism is a `BridgeDesignArtifact` the persona authors. If the bridge fails mid-rollout, the substrate detects via `BridgeAsset.state → DEGRADED` and pauses the wave; the substrate cannot un-flash a device.
- **Calibration certificate validation is at trust boundary.** `ExternalAttestation` from the calibration lab is substrate-transported but not substrate-verified for content. A fraudulent calibration certificate passes substrate signing; `CredentialDirectoryRef` lookup against ISO 17025 accreditation database is the detection layer, and that directory is operator-maintained.
- **AmbientEventStream storage pressure at fleet scale.** At ~57K raw events/day, HOT tier (7d) holds ~400K events; WARM tier (30d) holds ~1.7M. Operators should configure aggressive archival policies for raw telemetry while retaining aggregate events in HOT tier longer. The `EventAggregationPolicy` reduces the notification-routing load but does not reduce storage; raw events persist for lineage.
- **Cross-factory fleet unification via domain harvest + discovery.** Factory site A's KindRegistry projects a `DiscoverableRecord` over the normative discovery layer (`09_PROTOCOLS §3G`, ADR-0067); site B references it by global handle (access-gated) or imports via `DomainPrecedentImport` (`06_DOMAIN §11.2`). Live cross-node reference is supported; a node going dark degrades to `AvailabilityPolicy` fallback (`§3H.2`, V.8), not failure.
- **Real-time closed-loop control is OOS.** HVAC control in response to sensor readings requires sub-second latency; v1.0 disclaims real-time physical control (`00_VISION §2.2`). Monitoring-only with human-in-the-loop for HVAC adjustments is the honest scope.
- **Concurrent batch + individual state advancement.** If Vigil marks device #47 as `degraded` (individual) while Fleet runs a `BatchStateAdvancement` that includes #47 (batch), the kernel must resolve the conflict. Proposed: individual advancement takes precedence; batch skips devices whose state has changed since batch drafting. This is the expected composition but should be specified in `§26a.2.2`.

---

### SCENARIO 12 — Frontier-mode safety-critical research with peer-only trust and knowledge supersession

**Scenario premise.** Validate frontier-mode research with peer-only trust — combines continuous-iteration project with frontier-mode domain and PeerAttestationPool promotion (no credentialing authority exists). Stresses three axes no previous scenario combined: frontier probe-stays-active, peer-only trust accumulation in a safety-critical domain, and knowledge supersession cascade.

**User request** (the in-scenario task). "Run a continuous research programme discovering novel superconducting materials. Computational screening, synthesis, lab characterisation, and publication. External labs independently replicate our claims. Some results will be superseded or contradicted — the field moves fast and false positives are common."

**Task class.** INVESTIGATIVE (multi-session, indefinite, no single verifier truth for "which candidates are promising").
**Acceptance pathway.** `PROJECT_PROGRESS_ACCEPT` over the programme lifetime; individual sub-tasks reach VERIFIER_ACCEPT (DFT simulation convergence, XRD pattern matching) and PANEL_ACCEPT (candidate prioritisation, synthesis route selection). No completion ceremony — `asset_completion_mode = "continuous_iteration"` (`04_PROJECT §26a.2`).

**World shape.**
- Principal: single operator (a university research institute's materials-science division); `DeploymentProfile.principal_topology = operator_distinct`.
- Persona team: cohort of 5 — Lead (programme director, Historian-leaning), Theo (computational screening, Abducer-leaning), Synth (synthesis specialist, Composer-leaning), Cryo (measurement/characterisation, Verifier-leaning), Rev (internal reviewer/falsifier, Reflector-leaning). Formed via `EnvFormationProposal` (`05_ENVIRONMENT §12c`).
- Environment: persistent `project_workspace`-typed `EnvironmentInstance`.
- Project: indefinite duration; `asset_completion_mode = "continuous_iteration"`; produces `ArtifactBundle`s (computational predictions, synthesis protocols, characterisation datasets, preprints, papers) and manages `PhysicalAsset` instances (synthesised samples, measurement instruments — cryostat, PPMS, XRD, SQUID magnetometer) plus `InstrumentAsset` entries with `CalibrationChain` (`04_PROJECT §26a.7`).
- External participants: 3 partner university labs as `ExternalAgent` instances (for independent replication); institutional biosafety / chemical-safety review board as `ExternalAgent` (for safety clearance on novel synthesis routes involving toxic precursors or high-pressure apparatus).

**Domain shape.** No pre-authored `DomainContext`. Persona triggers emergent bootstrap (`06_DOMAIN §4`). Key properties:
- `corpus_evolution_mode = "frontier"` — persona-inferred from arxiv preprint velocity (~200 papers/month in superconductivity), high `KnowledgeRef` supersession rate (>15% of ingested refs superseded within 6 months), and frequent community retractions. Probe enters PERSISTENTLY_ACTIVE state per `§4.4`.
- `physical_harm_class = bodily_injury` — high-pressure synthesis (diamond anvil cells at >100 GPa), toxic precursor chemicals (hydrogen sulfide, phosphine), cryogenic systems (liquid helium handling). `safety_critical = True`.
- `information_hazard_class = none` — published science; no dual-use concern.
- No `CredentialDirectoryRef` — there is no "Board of Superconductor Research." No licensing body. Trust accumulates through `PeerAttestationPool` (`§5.6`) and `ReplicatedAttestation` (`§5.6.1`).
- Expected project count: >1 (the institute runs parallel investigations); multi-project `K=3` promotion to RECOGNISED is the natural path.

**Phase walk.**

| Phase | What carries the load | Substrate events fired |
|---|---|---|
| Project formation | `EnvFormationProposal` with 5 persona recruits; charter declares `asset_completion_mode = continuous_iteration`; `ClarifyTurn` (§4.0) disambiguates scope (discovery research vs. engineering optimisation — user picks discovery). | `env_formation_proposal_instantiated`, `project_formed`, `env_member_admitted ×5` |
| Domain probe (frontier) | `DOMAIN_UNKNOWN_DETECTED` signals A+B+C+F+G; BROAD strategy (large corpus). `ProbeBudgetEnvelope` with `principal_pledge = $500` (covers extensive literature + standards ingestion). Persona infers `corpus_evolution_mode = "frontier"` from arxiv preprint arrival rate; probe transitions to **PERSISTENTLY_ACTIVE** per `§4.4`. Daily ingestion budget established; no probe-completion gate. `BulkKindProposal` bundles: `media_kind = {dft_simulation_output, xrd_pattern, resistivity_curve, magnetisation_curve, synthesis_protocol, crystal_structure_file}`, `verifier_kind = {dft_convergence_check, xrd_pattern_match, resistivity_transition_detect, meissner_effect_verify, stoichiometry_check}`, `item_kind = {candidate_material, synthesis_route, characterisation_run, replication_request, retraction_notice}`, `outcome_kind = {simulation_converged, synthesis_succeeded, transition_detected, transition_absent, replication_confirmed, replication_failed, result_superseded}`, `safety_extension = {high_pressure_safety_protocol, toxic_precursor_handling, cryogenic_handling}`. | `domain_unknown_detected`, `probe_initiated`, `probe_persistently_active`, `bulk_kind_proposal_signed`, `knowledge_ingested ×~80`, `safety_extension_proposed ×3` |
| Safety extension approval | Three safety extensions proposed: `high_pressure_safety_protocol`, `toxic_precursor_handling`, `cryogenic_handling`. Each routes to operator co-sign (C2, `safety_critical = True`). Operator (institute's safety committee representative) co-signs after review. | `safety_extension_approved ×3 (operator_cosigned)` |
| PeerAttestationPool formation | No `CredentialDirectoryRef` exists for "superconductor researcher." Rev proposes `PeerAttestationPool` with `eligibility_kind = "recognised_researcher_superconductivity"`, `eligibility_evidence_kinds = ["first_author_publications_≥5", "h_index_≥15", "institutional_affiliation_verified"]`, `quorum_size = 3`, `quorum_independence_rule = "disjoint_affiliations"`, `trust_cap = 0.7`. Initial `peer_member_refs`: PIs from 3 partner labs + 2 recognised senior researchers admitted as `ExternalAgent` instances. Operator verifies pool composition. | `peer_attestation_pool_created`, `external_agent_admitted ×5`, `peer_attestation_pool_operator_verified` |
| Computational screening (months 1-3) | Theo runs DFT simulations (VASP, Quantum ESPRESSO via MCP tool integration) screening ~500 candidate compositions. `verifier_kind = "dft_convergence_check"` gates each run. 12 candidates show predicted Tc > 200K. `ArtifactBundle(media_kind = "dft_simulation_output")` per candidate. Each prediction is a `ProvenFact` at EMERGENT trust (0.3) — computational prediction, not measured. | `artifact_bundle_authored ×~500`, `verifier_accept ×~500`, `proven_fact_proposed ×12 (trust=0.3)` |
| Synthesis + characterisation (months 3-12) | Synth attempts synthesis of top 12 candidates. 7 succeed (polycrystalline samples produced). `PhysicalAsset` per sample. Cryo runs characterisation: 4-probe resistivity, SQUID magnetometry, XRD. `InstrumentAsset` with `CalibrationChain` for each instrument; `MeasurementFact` with `UncertaintyEnvelope` per measurement. 3 candidates show resistivity drops suggestive of superconductivity. Rev internally reviews; 2 pass internal PANEL_ACCEPT. | `physical_asset_proposed ×7`, `instrument_calibrated ×4`, `measurement_fact_admitted ×~hundreds`, `panel_accept ×2`, `panel_reject ×1 (insufficient evidence)` |
| External replication request (month 8) | Lead files `ReplicationRequest` (emergent `item_kind`) to 3 partner labs for the 2 internally-confirmed candidates. Each partner lab is an `ExternalAgent`. Partners receive synthesis protocols + expected characterisation targets. Replication is independent (`disjoint_affiliations`, `disjoint_funding_sources`). | `replication_request_drafted ×6 (2 candidates × 3 labs)` |
| Replication results (months 10-14) | **Candidate A (LaH₁₀ variant):** All 3 partner labs confirm resistivity transition at 215K ± 8K under 170 GPa. `ExternalAttestation` from each lab. Attestations are `credential_unverified = True` (no credential directory) but `peer_attested = True` via PeerAttestationPool (3 independent attestors, disjoint affiliations, quorum met). `ReplicatedAttestation` drafted: `constituent_count = 3`, `independence_check = "disjoint_affiliations"`, `agreement_pass = True`. **Effective trust uplift: 0.70 → 0.80** per `§5.6.1` uplift schedule. **BUT** — see Gap 3 below: does the frontier trust cap (0.7 on the domain) override this claim-level uplift to 0.80? | `external_attestation_received ×3`, `peer_attestation_verified ×3`, `replicated_attestation_drafted`, `replicated_attestation_trust_uplift` |
| Replication failure (month 12) | **Candidate B (Cu-doped Pb₁₀(PO₄)₆O variant):** 2 of 3 partner labs find NO resistivity transition; the third finds a transition that Rev identifies as likely Cu₂S impurity artefact (per the 2023 LK-99 precedent ingested during probe). `ReplicatedAttestation` drafted with `agreement_pass = False`. Original `ProvenFact` for Candidate B is marked `superseded_by` the failed replication. **NOW**: all downstream claims that cited Candidate B's ProvenFact as evidence — the synthesis protocol's `outcome_kind = synthesis_succeeded` confidence, the `item_kind = candidate_material` status, the bibliometric citation in a draft preprint — should have their trust degraded. **The substrate has no automatic propagation mechanism.** See Gap 1. | `external_attestation_received ×3`, `replicated_attestation_agreement_failed`, `proven_fact_superseded` |
| Knowledge supersession cascade (month 12, manual) | Rev manually audits all claims citing Candidate B's ProvenFact. Identifies: 1 draft preprint, 3 synthesis-protocol assertions, 2 `ProvenFact` entries derived from Candidate B data. Rev manually downgrades each. This took 4 days of persona time. **In a frontier domain with ~15% supersession rate, this manual audit burden is unsustainable.** See Gap 1. | `proven_fact_superseded ×2 (manual)`, `artifact_bundle_revision_drafted ×1` |
| Daily ingestion (continuous) | Probe stays PERSISTENTLY_ACTIVE. Daily budget: ~5 papers ingested, ~2 supersessions detected (older ingested papers contradicted by newer results). Each supersession requires manual trust-degradation audit by Rev. At 2 supersessions/day × 250 working days/year = ~500 manual audits/year. **Not scalable without substrate-level cascade.** | `knowledge_ingested ×~5/day`, `knowledge_ref_superseded ×~2/day` |
| Domain promotion: EMERGENT → RECOGNISED (month 18) | After K=3 successful project-level milestones (Candidate A replication confirmed; Candidate C identified via new screening round; a synthesis technique matured across 2 sub-projects) + 2 co-signing personas (Theo + Cryo) + cross-source validation passes, domain auto-promotes to RECOGNISED (trust 0.6). **Frontier cap (0.7) does not block RECOGNISED (0.6 < 0.7).** | `domain_promoted (EMERGENT → RECOGNISED)` |
| Domain promotion: RECOGNISED → AUTHORITATIVE (blocked) | AUTHORITATIVE requires trust 0.85. Frontier trust cap is 0.7. Domain CANNOT promote to AUTHORITATIVE while in frontier mode. **This is correct design behaviour** — the field's consensus is genuinely unsettled. Promotion requires either: (a) corpus drift rate falls below threshold for K consecutive 30-day windows (§4.4 sliding-window rule — but the substrate never defines the drift metric; see Gap 2), or (b) operator pins the domain out of frontier mode. | (no event; promotion blocked) |
| LongitudinalReputation accumulation (ongoing) | Partner lab PIs accumulate `LongitudinalReputation` over time. Lab A's PI: `historical_count = 12`, `later_confirmed_count = 9`, `later_contradicted_count = 1`, `track_record_score = 0.82`. Lab B's PI: track_record_score = 0.71. Lab C's PI (the one who initially confirmed the Cu₂S artefact): track_record_score = 0.45 — below `pool_admissibility_threshold` for high-stakes attestations. Pool self-heals: Lab C's PI still a pool member but their attestations on `physical_harm_class ≥ bodily_injury` claims are refused. | `longitudinal_reputation_updated ×~quarterly` |
| Ongoing research (years 2+) | Programme continues indefinitely. New candidates screened, synthesised, characterised, replicated. Knowledge base grows; supersession rate gradually decreases as the field matures. Frontier mode persists until sliding-window criterion met — **but the criterion is undefined (Gap 2).** | `measurement_fact_admitted ×~thousands/year`, `domain_harvest_drafted (annual)` |

**Substrate-shape gaps surfaced.**

1. **No `SupersessionCascade` for knowledge dependency graph.** When a `KnowledgeRef` is marked `superseded_by` (a newer paper contradicts it), all `ProvenFact`s, `ProposedKind` evidence chains, `VerifierRecipe` assumptions, safety extensions, and `ArtifactBundle` citations that referenced the superseded `KnowledgeRef` as primary evidence have **no automatic trust degradation.** The persona must manually audit every dependent claim. In a frontier domain with ~15% supersession rate, this creates an unsustainable audit burden (~500 manual re-evaluations/year in this scenario).

   **Why substrate-shape.** This is about dependency-graph topology — propagating trust changes through the citation/evidence graph when a foundational node is invalidated. The substrate already tracks the graph: `ProvenFact.evidence_refs` → `KnowledgeRef`; `ProposedKind.evidence_refs` → `KnowledgeRef`; `ArtifactBundle.citation_refs` → `KnowledgeRef`. The substrate knows which claims depend on which evidence. Cascade propagation is a graph operation, not domain logic. A legal research programme where a precedent case is overturned, a pharmaceutical pipeline where a clinical trial result is retracted, and this superconductor programme where a measurement result is contradicted all share the same dependency-graph supersession shape.

2. **No defined `CorpusDriftMetric` for frontier → non-frontier transition.** `§4.4` says promotion from frontier mode uses a "sliding-window cut: ≥ K consecutive 30-day windows in which the corpus drift rate is below threshold." But the spec never defines: (a) how `corpus_drift_rate` is computed, (b) what the drift-rate threshold is, (c) what K is, or (d) which events feed the computation. Without a defined metric, the frontier trust cap (0.7) never lifts in a principled way — the only path to AUTHORITATIVE is operator override (`pin out of frontier mode`), which is a human judgment, not a substrate-measurable condition.

   **Why substrate-shape.** The metric determines when a domain's trust ceiling lifts from 0.7 to the standard scale — a load-bearing decision that gates AUTHORITATIVE promotion and all downstream trust computations. The metric must be substrate-defined (computable from `KnowledgeIngestionRecord` arrival rates, `KnowledgeRef.superseded_by` frequency, `ProvenFact` stability over time) because it governs a kernel-enforced admission rule. A defined metric means the frontier → non-frontier transition is auditable and reproducible; without it, the transition is hand-waved.

3. **No explicit composition rule for `ReplicatedAttestation` uplift vs. frontier trust cap.** The spec defines `ReplicatedAttestation.effective_trust_cap` (base 0.7 + uplift to 0.80/0.85/0.90 per constituent count and independence check) and the frontier domain trust cap (0.7) independently. It never states whether a claim's trust — uplifted to 0.80 via 3 independent replications — is then clamped back to 0.7 by the domain's frontier cap, or whether claim-level uplift operates independently of the domain cap.

   **Why substrate-shape.** This is a trust-algebra composition rule, not domain logic. If the frontier cap clamps all trust within the domain to 0.7, then `ReplicatedAttestation` provides no benefit in frontier domains — independent replication (the gold standard of scientific validation) is structurally useless for trust-building. If claim-level uplift operates independently, then the domain cap governs promotion thresholds while individual claims can carry higher trust for downstream decisions. The spec must state which interpretation holds.

**Proposed resolution.** Three substrate-shape additions, all domain-agnostic:

| Gap | Substrate-shape fix | Proposed location |
|---|---|---|
| 1 | `SupersessionCascade` — when a `KnowledgeRef` is marked `superseded_by`, the kernel traverses the citation/evidence graph and applies a `supersession_discount` to all dependent claims' `provenance_score`. Discount is configurable per domain (default 0.5× for direct dependents, 0.25× for transitive dependents). Cascade emits `SUPERSESSION_CASCADE_APPLIED` lineage event per affected claim. Persona MAY override per-claim after re-evaluation (re-confirm or further downgrade). Cascade does NOT delete claims — it degrades their provenance score and flags them for re-evaluation. Rate-limited to prevent cascade storms (max 1 cascade per `KnowledgeRef` per 24h window). | `08_KNOWLEDGE §6.3` |
| 2 | `CorpusDriftMetric` — kernel-computed metric for frontier → non-frontier transition. Defined as: `drift_rate = (N_superseded + N_retracted + N_contradicted) / N_total_active_refs` computed over a trailing 30-day window. `frontier_exit_threshold` (default 0.05 — i.e., fewer than 5% of active refs superseded/retracted/contradicted per month). `K_consecutive_windows` (default 6 — i.e., 6 consecutive months below threshold). When K windows pass, domain emits `FRONTIER_MODE_EXIT_ELIGIBLE`; operator co-sign required to confirm exit (operator may judge that external factors explain the low drift). Metric is kernel-computed from `KnowledgeRef.superseded_by` timestamps + `ProvenFact.superseded_at` timestamps + retraction events in ingestion records. | `06_DOMAIN §4.4.1` |
| 3 | `ReplicatedAttestationFrontierComposition` — explicit composition rule: **claim-level `ReplicatedAttestation` uplift operates independently of the domain-level frontier trust cap.** The domain cap (0.7) governs the domain's stage trust score (used for promotion thresholds: EMERGENT → RECOGNISED → AUTHORITATIVE). Individual claims within the domain carry their own trust, which CAN exceed the domain cap via `ReplicatedAttestation` uplift. Downstream decisions (e.g., "should we trust this Tc measurement?") use the claim-level trust; domain-level decisions (e.g., "should this domain promote to AUTHORITATIVE?") use the domain cap. Clarifying paragraph + composition rule table added to §5.6.1. | `06_DOMAIN §5.6.1` (composition rule paragraph) |

**Not-gaps (persona evolves these).**

- All `media_kinds` (dft_simulation_output, xrd_pattern, resistivity_curve, magnetisation_curve, synthesis_protocol, crystal_structure_file), `verifier_kinds`, `item_kinds`, `outcome_kinds`, `contribution_kinds`, `safety_extensions` → emerge through `Proposed*Kind` into per-domain `KindRegistry`. The substrate never branches on "superconductor" or "DFT."
- Synthesis route selection and candidate prioritisation → persona-evolved skills (Theo's screening heuristics, Synth's synthesis expertise). Voyager-class skills accumulated across iterations.
- Replication protocol design → persona-authored `ArtifactBundle(media_kind = "replication_protocol")`; partner labs receive via standard `ExternalAgent` communication.
- Literature review and gap identification → persona-evolved Historian mode operating against hybrid retrieval pipeline; standard mechanism.
- Artefact/impurity identification → persona-evolved Verifier mode; specific detection heuristics (Cu₂S artefact, pressure-cell gasket shorts) are domain knowledge ingested through the standard pipeline, not substrate constants.
- Publication workflow → persona-authored `ArtifactBundle(media_kind = "preprint")`; external submission to arxiv/journals is bridge-mediated (Tier 2 or manual); peer review modelled as `ExternalAttestation` from journal reviewers (admitted as `ExternalAgent` with `consent_scope = project_only`).
- `LongitudinalReputation` accumulation → standard mechanism; persona proposes pool membership; track record self-updates from attestation history.

**Status.** Validated end-to-end after the three v1.0.13 fixes. The frontier research programme operates with: peer-only trust accumulation via `PeerAttestationPool` (no credential directory needed), independent replication via `ReplicatedAttestation` with claim-level trust uplift that exceeds the domain cap, automatic `SupersessionCascade` that propagates knowledge invalidation through the evidence graph (reducing manual audit from ~500/year to ~50/year for re-confirmation), and a defined `CorpusDriftMetric` that makes the frontier → non-frontier transition auditable.

**Honest residuals (after-fix).**

- **SupersessionCascade discount is heuristic.** The 0.5× direct / 0.25× transitive defaults may over- or under-discount depending on how tightly a claim depends on the superseded evidence. Persona override (re-confirm after re-evaluation) is the correction mechanism; the cascade is a "flag for review" signal, not a final judgment.
- **CorpusDriftMetric counts supersessions equally.** A supersession of a minor result and a supersession of a foundational theorem both count as 1 towards the drift rate. Impact-weighted drift would be more accurate but requires the substrate to assess "importance" of knowledge — which is persona territory. The metric is deliberately simple.
- **Frontier exit is operator-gated.** Even when the drift metric indicates stability, operator must co-sign the exit. This prevents premature exit in fields with seasonal publication patterns (conference-deadline bursts followed by quiet periods). The operator gate is load-bearing trust.
- **PeerAttestationPool self-selection bias.** The pool's `peer_member_refs` are proposed by the persona and verified by the operator. In a small field, pool members may share unstated assumptions or methodological blind spots. `disjoint_affiliations` mitigates institutional bias but not intellectual bias. The substrate cannot detect shared assumptions — this is the irreducible limit of peer review, not a substrate gap.
- **ReplicatedAttestation uplift never reaches credentialed (0.95).** A frontier domain with peer-only trust caps individual claim trust at 0.90 (blind_replication, ≥7 constituents). The 0.05 gap between peer-replicated (0.90) and credentialed (0.95) is the substrate's honest acknowledgement that peer replication is not equivalent to institutional credentialing. When a credentialing authority eventually forms for the field, CredentialDirectoryRef replaces the pool and the gap closes.
- **Cascade storms from foundational supersession.** If a seminal paper (cited by 200+ downstream claims) is superseded, the cascade touches 200+ claims in one event. The 24h rate limit prevents re-cascade within the same window, but the initial cascade is large. Operator should expect a burst of `SUPERSESSION_CASCADE_APPLIED` events; personas should batch re-evaluation.
- **Cross-institution replication coordination is persona-evolved.** The substrate provides `ReplicatedAttestation` + `ExternalAgent` + `PeerAttestationPool`; the persona manages the social coordination of "please replicate our result." This is correct (the substrate transports; the persona communicates), but high-coordination-cost replication requests may stall if partner labs are unresponsive. `ExternalCommitment` with `recurrence_class = requested_external_action` models this honestly.
- **AUTHORITATIVE promotion path is long in frontier domains.** RECOGNISED (0.6) is achievable; AUTHORITATIVE (0.85) requires frontier exit (6+ months of low drift) + the standard K'=10 successful projects + 5+ co-signing personas + external validation. For genuinely frontier fields, AUTHORITATIVE may take years. This is correct — the substrate refuses to manufacture certainty in uncertain fields.
- **Self-organization and meta-primitives.** SCENARIOs 06-12 collectively surface ~35 specific primitives as substrate-shape gaps. The cumulative pattern prompted **ADR-0045** (self-organizing coordination). ADR-0045 accepts the architectural direction: the five meta-mechanisms (EntityGroup, BatchOperation, StagedSequence, StreamPolicy, DerivedMetric) subsume the specific primitives; personas propose coordination shapes via `CoordinationShapeRegistry` (parallel to `KindRegistry`). Implementation targets v1.1. The specific primitives (SupersessionCascade, CorpusDriftMetric, etc.) remain as working implementations; v1.1 generalises them into seed shapes.

### SCENARIO 13 — Environment-driven persona genesis (autopopulation from a few founders)

**Scenario premise.** Validate that a small number of founder personas can grow a *varied* cohort by **authoring new personas** under sustained environmental pressure when the recruit pool is empty — the "population dynamics" residual (`00_VISION §11` R-v1.0-8) and the continuation of SCENARIO 04's `ReplicationBound` lineage (gap #4). Stress-tests that genesis stays bounded, diverse, domain-agnostic, and identity-coherent.

**User request** (the in-scenario task). "Investigate topic T and deliver a falsification-grade analysis" — given to two founder personas in a fresh deployment whose recruit pool is otherwise empty.

**Task class.** INVESTIGATIVE.
**Acceptance pathway.** `PROJECT_PROGRESS_ACCEPT`. (Genesis itself is not a task class; it is an admission-gated envelope raised *within* the investigative work when the cohort cannot be assembled.)

**World shape.**
- Principal: `operator_distinct` — the operator pre-declares a `ReplicationBound` for `replication_kind = "persona_genesis"` and a `population-policy/1`.
- Persona(s): 2 founders (generative; clear the generativity gate — floor + ALPS layer + fitness, no standing precondition); they author N newborns over the project's life.
- Environment: persistent `Lab` (`05_ENVIRONMENT §3`).
- Project: multi-session, digital ArtifactBundle.
- External participants: none.

**Domain shape.** Emergent domain T (no pre-authored DomainContext). Niche axes (`interest_type`, `team_role`, `contribution_kind`, `domain`, `disposition`) are KindRegistry-resolved (`06_DOMAIN §7.6`). Hazard axes low (`physical_harm_class = none`); the safety interest here is **replication topology**, not physical harm.

**Phase walk (against each design doc).**

| Design doc | Verdict | Notes |
|---|---|---|
| `00_VISION` | [PASS] | Population dynamics is normative (`16_POPULATION_DYNAMICS`, ADR-0048/0049/0050 promoted under ADR-0067/0068/0069). J5 open-capability admits genesis; C4 `ReplicationBound` bounds it; **cross-node genesis is normative under global `ReplicationBound` aggregation** (§4J, OQ-POP-4 resolved). |
| `01_KERNEL` | [PASS] | Reuses `ReplicationBound` (`§2.7`) at floor source 1 with new `replication_kind = "persona_genesis"`; INV-7 budget gate composes ahead of it; bounded-autonomy reuses `operator_deferred` + `PolicyEnvelope` (`§2.4.2`, from SCENARIO 04); all genesis events signed into lineage. Default-deny without a bound. |
| `02_PERSONA` | [PASS] | Reuses seed→mint (`§12`), the birth ceremony (Appendix A.20), and `LIFECYCLE_GENESIS` (new, distinct from `LIFECYCLE_FORK`). **Consistent with the prior `§11.3` rule** that a persona may not spawn without a `ReplicationBound`. Reuses ADR-0019 (MAP-Elites/Voyager/DGM/ALPS). Gated by `cohort_assembly.may_author_seeds` (default false). |
| `03_TASKS` | [PASS] | No new task class or pathway: genesis is an admission-gated action within INVESTIGATIVE/PROJECT_PROGRESS_ACCEPT work. |
| `04_PROJECT` | [PASS] | Extends the `§14.1` "no candidate" forced choice with a third option (propose genesis); unmet `CohortConstraint.required_kinds` feed the pressure signal. |
| `05_ENVIRONMENT` | [PASS] | Recruitment-gap fallback in `§12c`; the newborn maturation ramp reuses listening modes (`§9`, `passive→active→deliberative`) and attention allocation (`§7`); carrying capacity = free `AttentionBudget` + `Energy`. |
| `06_DOMAIN` | [PASS] | Niche axis *values* (RIASEC/Belbin/contribution_kind) are registry keys resolved via `§7.6`, never substrate enums (see V-check below). |
| `07_ARTIFACTS` | [PASS] | The `proposed_seed` draft is an opaque authored artifact; the kernel validates safety *shape*, not domain content. |
| `08_KNOWLEDGE` | [PASS] | Dual inheritance reuses the Voyager skill library + memory-inheritance-consent (`02_PERSONA §7.4`) + hybrid retrieval indexing. |
| `09_PROTOCOLS` | [PASS] | All schemas (incl. `eps-estimate/1`, `diversity-audit/1`, `cross-node-genesis-request/1`) registered in `§7.12b` (normative, mirroring §7.12a). Cross-node genesis is admitted under global `ReplicationBound` aggregation (`§4J`); the bound is enforced globally, not by prohibition. |
| `11_ACCEPTANCE_TESTS` | [PASS] | `A-GEN*` family (17 tests) registered; reuses `A-RB*` for the replication-bound paths. |
| `12_GLOSSARY` | [PASS] | ~20 terms added (Persona Genesis, GenesisProposal, NicheDescriptor, generativity gate, mentorship edge, secure base, …). |
| `14_DECISIONS` | [PASS] | ADR-0048 (Persona Genesis) + ADR-0049 (demographic regulation); related to ADR-0019. |

**Validation-invariant V check.** Genesis introduces persona-authored creation; V must hold.
- **V.1 / V.3 — no closed domain Literal.** Niche axes (RIASEC interest types, Belbin roles, contribution_kinds, domains) are KindRegistry-resolved string keys, explicitly *not* a substrate enum (`16 §4C` domain-agnosticism note). PASS.
- **V.4 — no pre-loaded domain knowledge.** The newborn's seed carries OCEAN/VAD priors + parent-authored `seed_skills` (Voyager-class learned skills), not substrate constants; cultural inheritance flows through the Voyager library. PASS.
- **V.5 — domain-shaped categories resolve to registry / opaque artifact.** The `proposed_seed` is opaque to the kernel (V.5c); niche kinds resolve via `§7.6` (V.5a). PASS.
- **V.6 — acquired + indexed.** Dual-inheritance skills are transmitted with consent and indexed through the standard retrieval pipeline. PASS.

**Substrate-shape gaps surfaced.** Six topology problems the v1.0 substrate could not express (each about *workflow/replication topology*, not a domain):

1. **No persona-authored seed.** Creation was operator-only; no primitive let a persona author a seed for a role no one fills.
2. **No recruitment-gap → generative fallback ordering.** The `04_PROJECT §14.1` dead-end had only pause / operator-interim.
3. **No niche-occupancy / variety guarantee.** Nothing enforced that a new persona be *distinct* (competitive exclusion + optimal distinctiveness + sibling differentiation) rather than a clone.
4. **No newborn maturation ramp.** New members were full participants instantly; no peripheral→full scaffolding (mentorship) topology.
5. **No demographic regulation of births.** No carrying-capacity / density-dependence / r-vs-K control over the birth *rate* (only the hard `ReplicationBound` ceiling).
6. **No founder-effect safeguard.** Nothing detected low effective population size to inject diversity against monoculture.

**Resolution.** All six landed in `16_POPULATION_DYNAMICS` (v1.1 draft): `§4A` pressure signal (gap 6 EPS factor), `§4B` recruitment-exhausted-first ordering (gap 2), `§4C` niche/optimal-distinctiveness/sibling-differentiation + diversity-injection (gaps 3, 6), `§4D` `GenesisProposal`→mint + generativity gate (gap 1), `§4E` ZPD/LPP maturation ramp + mentorship edge (gap 4), `§4F` carrying capacity + density dependence + r/K + the `persona_genesis` `ReplicationBound` (gap 5). Supporting edits in `01_KERNEL §2.7`, `02_PERSONA §3/§7/§7.4/§12`, `04_PROJECT §14.1`, `05_ENVIRONMENT §12c`, ADR-0048/0049, `A-GEN*` tests, glossary.

**Not-gaps (persona evolves these).** The niche-axis *values* (RIASEC interest types, Belbin roles, `contribution_kind`s, domains), the newborn's domain skills, and any verifier/convention kinds are emergent via `KindRegistry` (`06_DOMAIN §7.5/§7.6`) — the substrate supplies the slots; personas fill them.

**Status.** Validated against the v1.1 draft; aligns with the intended design. Genesis is the sanctioned, bounded continuation of SCENARIO 04's `ReplicationBound` (gap #4) and the `02_PERSONA §11.3` no-spawn-without-bound rule. **Residuals researched and addressed in a follow-up pass (ADR-0050; `16 §4G–§4J`) — see below.**

**Honest residuals (researched + addressed; ADR-0050).**
- **`effective_population_size` is now rigorous** — RESOLVED (`§4G`). Defined as the harmonic-mean-smoothed `min(Ne_v, Ne_d)`: Crow–Kimura variance effective size (authorship-skew founder effect) + inverse-Simpson effective number of niches (concentration). No longer heuristic. Empirical N-scale calibration folds into the v1.2 study.
- **Niche-grid axis bias** — RESOLVED (`§4I`). `niche_descriptor_mode ∈ {fixed_axes, cvt, learned}` (CVT-MAP-Elites / AURORA learned descriptors) + a `false_collision_rate`/`unfillable_gap_rate` mis-calibration detector that emits a self-correcting `niche_recalibration_advisory`. Closes R-POP-3.
- **Diversity at birth vs forever** — MITIGATED (`§4H`). A continuous diversity-maintenance loop (periodic audit + novelty pressure on the next birth + attention fitness-sharing on crowded niches, routing-weight only) now counters post-birth drift. Whether it *prevents* collapse at N=100/1000 remains the open empirical question (OQ-POP-6 / OQ-PERSONA-1, v1.2) — now with a mechanism to measure against.
- **Cross-node / federated genesis** — NORMATIVE under global `ReplicationBound` aggregation (`§4J`, ADR-0067/0068/0069): cross-node proposals are admitted iff the global aggregated ceiling clears (one counter across the `owner_node_set` / federation), with cross-node quorum + replicated globally-verifiable provenance; refused `genesis_exceeds_global_replication_bound`, or fail-closed `global_replication_bound_unverifiable` across a partition. The ceiling cannot be evaded across nodes — by aggregation, not prohibition.
- **`09_PROTOCOLS §7` registry** — RESOLVED. All 9 schemas registered in `§7.12b` (Draft).
- **Remaining true residual:** the empirical population-collapse study at scale (OQ-POP-6 / OQ-PERSONA-1) and detector/curve threshold calibration (OQ-POP-1) — both correctly v1.2 study items, not design gaps.

---

### SCENARIO 14 — Composed multi-org environment with dynamically-authored rules and access-scoped artifact sharing

**Scenario premise.** Validates that a purpose-specific environment can carry dynamically-authored, executable rules (`env-rule/1`) enforced at the safety floor, and that the artifacts it produces are owned by the environment and shared by access level within a composition and outward by policy — with no new substrate hardcode.

**User request** (the in-scenario task). "Stand up a chip-design group inside our manufacturing org; every taped-out design must pass a buildable/orderable check and ship under our standard shipment contract, and share the result read-only with our foundry partner."

**Task class.** INVESTIGATIVE (multi-session design work).
**Acceptance pathway.** PROJECT_PROGRESS_ACCEPT (milestones) composed with VERIFIER_ACCEPT (the buildable/orderable rule).

**World shape.**
- Principal: multi-tenant (ManufacturingCorp operator + Foundry partner tenant).
- Persona(s): a small chip-design cohort (lead + DRC / BOM specialists), formed via `EnvFormationProposal`.
- Environment: a parent `team` env "ManufacturingCorp" composing a child `project_workspace` env "chip-design" (`05_ENVIRONMENT §2.2a`).
- Project: yes, multi-session, produces a digital `ArtifactBundle` (schematic + netlist + BOM + sim report).
- External participants: the foundry as a separate tenant receiving an outward read-only share.

**Domain shape.** Emergent `chip_design` DomainContext; hazard axes low (digital), so the env rules are non-safety-critical except where physical fabrication is implicated. `KindRegistry` resolves `env_rule_kinds` (`code`/`rule_engine`/`contract`) and the `kicad_project` / BOM media kinds.

**Phase walk.**

| Phase | Primitives carrying load | Events fired |
|---|---|---|
| Form env | parent composes child via `EnvironmentComposition`; `EnvFormationProposal.proposed_rules` carries two rules | `env_composition_established`, `env_formation_proposal_instantiated`, `env_rule_proposed` |
| Author rules | "buildable/orderable validator" (`rule_kind=rule_engine`: DRC + BOM-orderability cascade, `enforced_at=[output, mutation_propose]`); "shipment contract" (`rule_kind=contract`, `enforced_at=[output]`) | `env_rule_trial_entered` → `env_rule_approved` |
| Cascade | parent marks a corp-wide "no export-controlled parts" rule `cascade_locked=True`; it inherits into the child | `env_composition_cascade_applied`; a child attempt to relax it → `env_child_charter_amendment_refused (safety_violation)` |
| Design | cohort co-edits the `ArtifactBundle` (`owning_env_id` = chip-design env) | `artifact_bundle_env_ownership_set`, `project_artifact_edited` |
| Verify | at `output`, source-8 runs the buildable/orderable rule; a non-orderable BOM → `env_rule_refusal` with `VerifierInvocationEvidence`; fixed → passes | `env_rule_evaluated`, `env_rule_refusal` |
| Share | `ArtifactSharingPolicy`: `inherit_to_children` within ManufacturingCorp (org roles get `rw`); `outward_tier=tenant` to the foundry partner gated by a `CrossTenancyAgreementRef` (read-only) | `artifact_sharing_policy_created`, `artifact_access_granted`; without the agreement → `CROSS_TENANT_VISIBILITY_DEMOTED` |

**Substrate-shape gaps surfaced** (pre-feature). (1) Env rules could only be declarative prose — no way to express an executable buildable/orderable check or a shipment-contract conformance gate bound to the environment. (2) Artifacts had no env ownership or sharing policy — no way to share read-only across the org composition or outward to a partner tenant under a defined policy.

**Resolution.** (1) `EnvironmentRule` (`env-rule/1`, `05_ENVIRONMENT §2.2b`) riding under safety-floor source 8 (`01_KERNEL §2`; ADR-0052/0053), with the `env_rule_kinds` KindRegistry family (`06_DOMAIN §7.6.3`). (2) `owning_env_id` + `ArtifactSharingPolicy` (`artifact-share/1`, `07_ARTIFACTS §4a`; ADR-0054/0055) reusing the 5 visibility tiers + `CrossTenancyAgreementRef` + `EnvironmentComposition` cascade. Distribution/discovery interop in `09_PROTOCOLS §3F` (ADR-0056). Tests A-ER1–9, A-AB21–27, A-EC1–5.

**Not-gaps (persona evolves these).** The actual DRC ruleset, BOM-orderability criteria, and shipment-contract clauses are rule *content* authored by the user/personas and signed like any Proposed\*Kind (`06_DOMAIN §7.5/§7.6`); the substrate supplies only the env-rule shape and the sharing-policy slots.

**Status.** Validated against the v1.1 additions; aligns with the intended design. Every step is expressible with the new schemas, fires at the correct admission point, emits the right lineage events, and composes most-restrictive-wins.

**Honest residuals.** Rule-evaluation latency in the floor budget (R-ENV-12); sharing-policy misconfiguration exposure (R-ARTIFACTS-8); multi-parent cascade conflict deferred (OQ-ENV-9); per-artifact (vs per-bundle) grants deferred (OQ-ARTIFACTS-7).

---

### SCENARIO 15 — Self-hosted single-node task, discovered and observed from a phone on-network and off-network

**Scenario premise.** Validates the v1.1 discovery / access / reachability / availability track end-to-end on the most common real deployment: a user runs PersonaOS **on their own laptop at home** (one kernel, behind a NAT router, no dedicated server) and wants to **discover their personas, watch progress, and fetch artefacts** both from a phone on the same Wi-Fi and from a phone on cellular off-network. Stress-tests exactly the "from anywhere without hosting" question and forces the honest commons/liveness limits into the open.

**User request** (the in-scenario task). "Design an AC circuit" (an analog/power-electronics design deliverable).

**Task class.** INVESTIGATIVE (multi-session design) → produces a digital `ArtifactBundle` (schematic + netlist + sim report).
**Acceptance pathway.** PROJECT_PROGRESS_ACCEPT (milestones) composed with VERIFIER_ACCEPT (a sim/DRC check, if a domain tool is bridged).

**World shape.**
- Principal: single-user, single-kernel, **`operator_is_user`** (`DeploymentProfile`, `09_PROTOCOLS R-PROTOCOLS-9`); the laptop is `nat_private` (`§3H.1`).
- Persona(s): a small analog-design cohort bootstrapped on demand.
- Environment: a `solo` / `project_workspace` env on the home kernel.
- Observers: the **same user's phone**, on Wi-Fi (same LAN) and later on cellular (off-network), authenticating as the **owning principal** (own DID / VC).

**Domain shape.** Emergent `analog_circuit_design` / `power_electronics` DomainContext via domain probe; tools (SPICE-class simulator) discovered or human-bridged (`06_DOMAIN §5`).

**Phase walk.**

| Phase | Primitives carrying load | Events fired |
|---|---|---|
| Work | task classified → domain probe → cohort designs the circuit; bundle co-edited (`owning_env_id` = the home env) | `domain_unknown_detected`, `project_artifact_edited`, OTel spans (`§4`) |
| Project for discovery | persona/env/bundle each project a `DiscoverableRecord`; bundle gets an `ArtifactCard`; a `TelemetryCard` advertises a default-private feed | `artifact_card_published`, `telemetry_card_published` |
| Same-Wi-Fi observe | phone joins LAN; **mDNS** intranet plane (`§3G.2`) surfaces the records with **no internet**; phone holds `read` as owner → sees live progress + pulls artefacts | `discovery_query`, `telemetry_feed_subscribed` |
| Off-network reach | phone on cellular; **resolver** (`§3G.2`/`§3H.1`) returns relay-reachable multiaddrs; **circuit-relay v2 + DCUtR** dial the `nat_private` laptop while it is awake | `reachability_resolved`, `relay_dial` |
| Laptop sleeps | live persona pauses (`presence=dormant`); `online_only` content is unfetchable, but the bundle's `AvailabilityPolicy=pinned` keeps artefacts fetchable from an IPFS pin / replica, verified against `content_hash` | `presence_changed`, `replica_fallback_served` |
| Access gate | a *stranger* who discovers the DHT record holds no grant → sees nothing (or `discover`-only metadata) per `visibility_tier`; only the owner's DID/VC unlocks `read` | `access_refused` / `discover`-tier filter (`§3G.4`) |

**Substrate-shape gaps surfaced** (pre-feature, now resolved by the v1.1 track). (1) No intranet/LAN discovery — a same-Wi-Fi phone could not find a home kernel with no internet. (2) No way to *dial* a NAT-private node from off-network without a dedicated server. (3) No first-class story for artefacts remaining fetchable after the origin sleeps. (4) Discovery was not access-gated, risking enumeration of private personas.

**Resolution.** (1) mDNS intranet plane (`09_PROTOCOLS §3G.2`, ADR-0059). (2) `ReachabilityProfile` + circuit-relay v2 / DCUtR / bootstrap (`§3H.1`, ADR-0065) — commons or self-hosted relay, **not** a dedicated content host. (3) `AvailabilityPolicy` (`online_only`/`replicated`/`pinned`) + `ContentLocator.replica_tiers` (`§3H.2`, `07_ARTIFACTS §10a`, ADR-0063/0065). (4) Access-gated discovery + `AccessPolicy` (`§3G.3`–`§3G.4`, ADR-0060). Tests A-DT2, A-AX*, A-CL*, A-RA1–6, A-AB28–34.

**Not-gaps (persona / operator configures these).** Which relay/bootstrap/pin commons to use (or self-host) is operator policy; the actual circuit content and the SPICE verifier recipe are persona/domain work.

**Status.** Validated against the v1.1 additions; aligns with the intended design. Same-Wi-Fi discovery + observation works fully offline; off-network discovery + live observation works while the laptop is awake and reachable via relay; artefacts remain fetchable after sleep iff `AvailabilityPolicy` is `replicated`/`pinned`. Access is owner-gated throughout.

**Honest residuals (the physics, stated plainly).** "From anywhere without *any* infrastructure" is impossible: an asleep/offline NAT node is unreachable, and off-network reach needs relay/bootstrap commons (or a self-hosted relay) plus a pin/replica for offline availability (R-PROTOCOLS-15). Live *progress* telemetry is inherently `online_only` — a paused persona emits no new spans; only its last state + a dormant-presence transition are observable until the laptop wakes. Default relay/pin commons selection and per-kind availability defaults are open (OQ-PROTOCOLS-12).

---

## Scenario template (copy + fill)

```text
### SCENARIO NN — <topology phrase>

**Scenario premise.** <one-sentence description of what this scenario validates>

**User request** (the in-scenario task). "<one sentence>"

**Task class.** <one of the 10 from 03_TASKS §2>
**Acceptance pathway.** <one of the 8 from §3>

**World shape.**
- Principal: <topology — solo / operator-distinct / multi-tenant / federated>
- Persona(s): <count, dispositions if relevant>
- Environment: <type from 05_ENVIRONMENT §3 + blueprint if any>
- Project: <yes/no, multi-session/ephemeral, produces digital/physical/both>
- External participants: <ExternalAgents if any, in shape terms>

**Domain shape.** <authored DomainContext present? expected hazard axes?
expected_project_count? cross-domain transfer in play?>

**Phase walk.** <table of phases, primitives carrying load, events fired>

**Substrate-shape gaps surfaced.** <numbered list, each phrased as a
topology problem the substrate could not express without a domain
hardcode>

**Resolution.** <link existing sections; if a new section was added,
note the §>

**Not-gaps (persona evolves these).** <bullet list of domain-shaped
things the substrate already provides slots for via KindRegistry, with
references to §7.5/§7.6>

**Status.** <validated / pending-fix / addressed / parked>

**Honest residuals.** <known after-fix limitations>
```

## Scenario candidates worth walking next

These are not commitments — they are a backlog of task topologies that would stress the design in interesting ways. Each is named by its **topology**, not by its domain.

1. **Continuous-iteration project with frontier-mode domain.** A research programme whose `corpus_evolution_mode = "frontier"` and `asset_completion_mode = "continuous_iteration"`. Tests probe-stays-active under frontier override. **(ADDRESSED — see SCENARIO 12 above; added SupersessionCascade (`08_KNOWLEDGE §6.3`), CorpusDriftMetric (`06_DOMAIN §4.4.1`), ReplicatedAttestationFrontierComposition (`06_DOMAIN §5.6.1`).)**
2. **Multi-principal cross-org project with consent-bounded knowledge sharing.** Two ORG_A + ORG_B principals sharing one project. Tests `04_PROJECT §19.1 Multi-tenant cross-org joint projects` and `RISK E` anti-leakage. **(ADDRESSED — see SCENARIO 06 above; added PrincipalAttribution + MultiPrincipalAttestationQuorum + DerivationProvenanceEdge + principal_attribution_id + §19.1 consolidated section + visibility-tier cross-ref.)**
3. **Pedagogic task on emergent domain with safety-critical hazard axes.** A user learning a hazardous skill from a persona. Tests `GOAL_PROGRESS_ACCEPT` interaction with safety floor and degraded gate. **(PARTIALLY ADDRESSED — see SCENARIO 09 above; added LearnerStateRecord + LearnerCompetencyAttestation + TeachingAuthorisation + Curriculum + LessonPlan + MasteryCheckpoint + GOAL_PROGRESS_ACCEPT learner-acknowledgement step + HazardousSkillTeachingGate. 5 remaining gaps: PedagogicIncidentReport, LearnerEnrollmentContract three-way authority, LearningStruggleClassification, MinorLearnerProtections, UserSkillInstructionAgreement.)**
4. **Relational interactive over weeks with `OPEN_ENDED` acceptance.** Long companionship interaction. Tests Memory Power Asymmetry mitigations and consent revocation. **(ADDRESSED — see SCENARIO 08 above; added UserMemoryTransparencyRequest + UserMemorySelectionRequest + UserRelationshipReleaseRequest + UserBoundary first-class + DistressDetectionRoutingPolicy + RelationshipReviewCheckpoint + operator_blind_mode + companion-pathway routing note + responsible-companionship clarification in 00_VISION §10.)**
5. **Ephemeral demoted INVESTIGATIVE.** A one-shot research question demoted out of project scope. Tests `03_TASKS §7.3` demotion path.
6. **Federated A2A project across two kernels with cross-kernel promotion.** Tests `09_PROTOCOLS` adapter set, A2A signed AgentCards, federated DomainCurator.
7. **Persona fork mid-project.** A persona forks into two siblings while a project is active. Tests `02_PERSONA §7.4` fork mechanics + ProjectMember reassignment. **(ADDRESSED — see SCENARIO 10 above; added `MidProjectForkComposition` unified envelope (`02_PERSONA §7.4.7`) + admission rule (`§7.4.8`) + 4 lineage events + 4 substrate refusal cases + cross-references in 13 affected primitives across 5 docs. Single coherent primitive closing all 13 composition gaps.)**
8. **Persona retirement during multi-year project.** A persona retires; project must continue. Tests reanimation policy and member-handoff lineage. **(ADDRESSED — see SCENARIO 07 above; added LeadHandoffCeremony + ObligationReassignment + PlannedDeparture + RetiredStatePersistencePolicy + PersonaConsultation + LifecycleEvent enumeration + retired_persona_response_policy.)**
9. **External-tool-required bypass with operator policy override.** A project that cannot complete without a tool the persona lacks. Tests `04_PROJECT §4.3` bypass and floor source 6.
10. **Frontier domain promotes via PeerAttestationPool (no credentialing authority exists).** Tests the §5.6 fallback for fields with no licensing body. **(ADDRESSED — see SCENARIO 12 above; combined with backlog #1.)**
11. **Deferred-operator topology with latency-bounded policy envelope.** Lifts the embodied-autonomous OOS partially (SCENARIO 04 gap #1).
12. **Recursive bridging: kernel-trusted non-human installer.** SCENARIO 04 gap #2.
13. **Closed-system `ResourceStockEnvelope` separate from `ExternalBudget`.** SCENARIO 04 gap #3.
14. **Bounded self-replication as charter-class invariant.** SCENARIO 04 gap #4.
15. **`MissionCharter` for long-horizon self-direction within operator-supplied drift bounds.** SCENARIO 04 gap #5; the largest of the five.
16. **Fleet-of-N homogeneous asset management with high-volume telemetry and staged deployment.** Tests cardinality topology (one-to-many asset coordination), event fan-in at scale, and staged-rollout coordination. **(ADDRESSED — see SCENARIO 11 above; added AssetGroupEnvelope + BatchStateAdvancement (`04_PROJECT §26a.2.2`), StagedRolloutEnvelope (`04_PROJECT §26a.9`), EventAggregationPolicy (`05_ENVIRONMENT §8.3`). 23 acceptance tests in A-AG*, A-SR*, A-EA* families.)**

17. **Persona responsiveness: immediate response, voluntary response, and cross-persona/cross-env voluntary help.** Tests three user-facing expectations: (a) a dormant persona addressed by name actually wakes and responds (Wake Path 6, `05_ENVIRONMENT §5.2`); (b) a task with no named persona gets a response via kernel auto-select (Mode C) or env-member notification routing (Mode A/B); (c) a persona can voluntarily help another persona or user across environment boundaries without full membership (CrossEnvProactiveOffer + GuestPresence, `05_ENVIRONMENT §11.6`). **(ADDRESSED — added Wake Path 6 (`05_ENVIRONMENT §5.2`), dispatcher integration (`03_TASKS §4.1`), CrossEnvProactiveOffer + GuestPresence (`05_ENVIRONMENT §11.6`). 13 acceptance tests in A-WK6* + A-CEPO* families.)**

18. **Progressive automation of human dependencies across a physical-world project.** Tests the full MHBB reduction loop: persona inventories Tier 4/5 dependencies → authors Tier 3 bridge designs → installs bridges → validates → promotes to skill_library → reuses across projects. Also tests sensor-bridge substitution for human professional attestation (construction inspection via camera/sensor, calibration verification via automated measurement, environmental compliance via IoT). Exercises `BridgeReductionPlan` (`04_PROJECT §26a.10`), `AttestationEquivalencePolicy` (`06_DOMAIN §5.7`), their composition with `BridgeCalibrationBinding` (`§5.5.5`), `BridgeInstallerKind` (`§5.5.6`), `MilestoneDrivenAutonomy` (`02_PERSONA §11.2`), and `skill_library` Voyager accumulation. **(ADDED — `BridgeReductionPlan` (`04_PROJECT §26a.10`) + `AttestationEquivalencePolicy` (`06_DOMAIN §5.7`). Scenario walk pending.)**

19. **Environment-driven persona genesis (autopopulation from a few founders).** A small founder cohort grows a varied population by authoring new personas under environmental pressure when recruitment is exhausted. Tests the continuation of SCENARIO 04's `ReplicationBound` (gap #4) and the `02_PERSONA §11.3` no-spawn-without-bound rule. **(ADDRESSED — see SCENARIO 13 above; added `16_POPULATION_DYNAMICS.md` (Persona Genesis: population-pressure signal, recruitment-exhausted-first, MAP-Elites niche/variety guarantee, mentorship maturation ramp, demographic regulation, all bounded by `persona_genesis` `ReplicationBound`) + ADR-0048/0049 + `A-GEN*` (17 tests) + supporting edits across `01_KERNEL §2.7`, `02_PERSONA §3/§7/§7.4/§12`, `04_PROJECT §14.1`, `05_ENVIRONMENT §12c`. v1.1 draft.)**

A scenario should be added to the catalog as it is walked, with the same eight-step structure.

## Maintenance

- The catalog is append-only by default; entries are not deleted when status changes.
- A scenario whose resolution is found insufficient should be **re-walked** as a new entry, citing the prior entry id, rather than mutating the original.
- Substrate-shape fixes named in a scenario must be linked to the spec section that implements them; if the spec section is later removed or restructured, the validation entry is stale and must be re-walked.

## Where to read next

- The substrate sections referenced above:
  - SCENARIO 01 fixes: `06_DOMAIN §3.2`, `§4.7.1`, `§9.1.1`, `§11.2`, `§13a`.
  - SCENARIO 04 fixes: `01_KERNEL §2.4.2` (`operator_deferred` + PolicyEnvelope), `01_KERNEL §2.7` (ReplicationBound), `02_PERSONA §3.5` (Body / BodyBinding), `02_PERSONA §11.3` (MissionCharter), `04_PROJECT §26a.4.2` (ResourceStockEnvelope), `06_DOMAIN §5.5.5` (BridgeCalibrationBinding), `06_DOMAIN §5.5.6` (BridgeInstallerKind).
  - SCENARIO 02 minor fix: `06_DOMAIN §5.5.5` BridgeCalibrationBinding.
  - SCENARIO 03 minor fix: `04_PROJECT §11` PeerReview `anonymity_tier`.
  - SCENARIO 05 exercises (no new fixes): `04_PROJECT §0` (Project = env type unification), `03_TASKS §4.0` (ClarifyTurn), `05_ENVIRONMENT §12c` (EnvFormationProposal), `04_PROJECT §26a.4.1` (PaymentBridge), `04_PROJECT §26a.6` (ProjectPhaseState), `04_PROJECT §26a.7` (InstrumentAsset + CalibrationChain), `08_KNOWLEDGE §16a` (MeasurementFact + UncertaintyEnvelope), `06_DOMAIN §7.2.1` (MetaRegistry hazard seeds), `02_PERSONA §11.6` (PersonaPersonaBoundary), `02_PERSONA §7.4.1–4` (fork inheritance policies).
  - SCENARIO 06 fixes: `01_KERNEL §2.4.3` (`PrincipalAttribution`, `PrincipalRef`, `multi_principal_attribution_enabled`), `04_PROJECT §3` + `05_ENVIRONMENT §5` (`principal_attribution_id` member field), `05_ENVIRONMENT §12c.4a` (`MultiPrincipalAttestationQuorum`), `04_PROJECT §4.1` (multi-principal completion ceremony composition), `08_KNOWLEDGE §16b` (`DerivationProvenanceEdge` + `DerivationProvenancePolicy`), `06_DOMAIN §6.3` + `§13a` (visibility-tier cross-reference + cross-tenant resolution), `04_PROJECT §19.1` (Multi-tenant cross-org joint projects consolidated section), `06_DOMAIN §11.1` (RISK E cross-ref to DPE).
  - SCENARIO 07 fixes: `02_PERSONA §7` (canonical `LifecycleEvent.kind` enumeration), `02_PERSONA §7.5.1` (`RetiredStatePersistencePolicy`), `02_PERSONA §7.5.2` (`PersonaConsultation`), `02_PERSONA §11.7` rule 7 (`retired_persona_response_policy`), `04_PROJECT §3` (role-value extension: outgoing_lead / incoming_lead / departing), `04_PROJECT §9.1` (`ObligationReassignment`), `04_PROJECT §14.2.1` (`PlannedDeparture`), `04_PROJECT §25.1` (`LeadHandoffCeremony`), `01_KERNEL §2.4.3` (principal-cosigns-are-operator-keyed clarification).
  - SCENARIO 08 fixes: `02_PERSONA §11.4a` (`UserRelationshipReleaseRequest`), `02_PERSONA §11.6a` (`UserBoundary` first-class), `02_PERSONA §11.7a` (`UserMemoryTransparencyRequest`), `02_PERSONA §11.7b` (`UserMemorySelectionRequest`), `01_KERNEL §2.8` (`DistressDetectionRoutingPolicy`), `03_TASKS §3.2` (`RelationshipReviewCheckpoint` + companion-pathway routing note), `05_ENV §3a` (`operator_blind_mode`), `00_VISION §10` (responsible-companionship constraints are operator/author policy clarification).
  - SCENARIO 09 fixes (v1.0.10, Groups A + B): `02_PERSONA §11.8` (`LearnerStateRecord`), `02_PERSONA §11.9` (`LearnerCompetencyAttestation`), `02_PERSONA §11.10` (`TeachingAuthorisation`), `03_TASKS §3.1` extension (GOAL_PROGRESS_ACCEPT learner-acknowledgement step), `03_TASKS §3.3` (`Curriculum` + `LessonPlan` + `MasteryCheckpoint`), `01_KERNEL §2.9` (`HazardousSkillTeachingGate` safety-floor composition rule). Groups C–G (the former 5 residuals) discharged via ADR-0039–0043 — emergent composition + the minor-learner floor hook.
  - SCENARIO 10 fix: `02_PERSONA §7.4.7` (`MidProjectForkComposition` unified envelope) + `§7.4.8` (admission rule requiring envelope for fork-of-active-project-member) + `§7.4.6` extension (4 new MIDPROJECT_FORK_* lineage events) + `§7` LifecycleEvent enumeration extension. Cross-references in 13 affected primitives: `02_PERSONA §11.3` MissionCharter, `§11.4` PersonaRelationshipEdge, `§11.6a` UserBoundary, `§11.8` LearnerStateRecord, `§11.10` TeachingAuthorisation; `04_PROJECT §3` ProjectMember, `§9` Obligation, `§14.2` CohortDynamicsState, `§14.2.1` PlannedDeparture, `§25.1` LeadHandoffCeremony; `05_ENV §3a` operator_blind_mode; `01_KERNEL §2.4.3` PrincipalAttribution; `03_TASKS §3.3` Curriculum.
  - SCENARIO 11 fixes: `04_PROJECT §26a.2.2` (`AssetGroupEnvelope` + `BatchStateAdvancement` + `AssetGroupDerivedState`), `04_PROJECT §26a.9` (`StagedRolloutEnvelope` + `RolloutWave`), `05_ENVIRONMENT §8.3` (`EventAggregationPolicy` + `AggregationRule` + `SummaryFunction` + `AggregateEvent`).
- Acceptance tests for these mechanisms: `06_DOMAIN.md §22` (A-EN, A-CS, A-PR, A-SP, A-HV); `01_KERNEL.md §x` (A-DO* deferred-operator, A-RB* replication-bound); `02_PERSONA.md §14` (A-MC* mission-charter, A-P30..P33 body binding); `04_PROJECT §x` (A-RS* resource-stock, A-PR-AN* anonymity); `06_DOMAIN.md §22` (A-BC* bridge-calibration, A-BI* bridge-installer); `11_ACCEPTANCE_TESTS.md §9f` (A-MT* multi-principal attribution + quorum + cross-tenancy; A-DP* derivation-provenance edge); `11_ACCEPTANCE_TESTS.md §9g` (A-LH* lead handoff, A-OR* obligation reassignment, A-PD* planned departure, A-RT-PERS* retired-state persistence, A-PC* persona consultation, A-LE* lifecycle event enum, A-RT-RESP* retired-persona response policy); `11_ACCEPTANCE_TESTS.md §9h` (A-UB* user boundary, A-UM* user memory transparency, A-UF* user selective forgetting, A-URR* user relationship release, A-DD* distress detection routing, A-RRC* relationship review checkpoint, A-OBM* operator blind mode, A-CP* companion pathway routing); `11_ACCEPTANCE_TESTS.md §9i` (A-LSR* learner state record, A-LCA* learner competency attestation, A-TA* teaching authorisation, A-CUR* curriculum, A-LP* lesson plan, A-MASTERY* mastery checkpoint, A-GPA-ACK* goal-progress-accept learner ack, A-HST* hazardous skill teaching gate); `11_ACCEPTANCE_TESTS.md §9j` (A-MPFC* mid-project fork composition).
  - SCENARIO 12 fixes: `08_KNOWLEDGE §6.3` (`SupersessionCascade`), `06_DOMAIN §4.4.1` (`CorpusDriftMetric`), `06_DOMAIN §5.6.1` (`ReplicatedAttestationFrontierComposition` — composition rule paragraph).
  - SCENARIO 17 fixes: `05_ENVIRONMENT §5.2` (Wake Path 6), `03_TASKS §4.1` (dispatcher dormancy check), `05_ENVIRONMENT §11.6` (CrossEnvProactiveOffer + GuestPresence); `11_ACCEPTANCE_TESTS.md` (A-WK6* + A-CEPO* families).
  - SCENARIO 13 fixes: `16_POPULATION_DYNAMICS.md` (whole doc — Persona Genesis + demographic regulation; schemas `population-pressure-signal/1`, `niche-descriptor/1`, `genesis-proposal/1`, `genesis-provenance/1`, `mentorship-edge/1`, `population-policy/1`), `01_KERNEL §2.7` (`persona_genesis` replication_kind), `02_PERSONA §3` (`may_author_seeds`) + `§7` (`LIFECYCLE_GENESIS`) + `§7.4` (fork-vs-genesis) + `§12` (persona-authored seeds), `04_PROJECT §14.1` (genesis forced-choice option), `05_ENVIRONMENT §12c` (recruitment-gap fallback), `14_DECISIONS` (ADR-0048, ADR-0049); `11_ACCEPTANCE_TESTS.md` (A-GEN* family, 17 tests).
  - SCENARIO 14 fixes: `05_ENVIRONMENT §2.2b` (`EnvironmentRule`, `env-rule/1`) + `§2.2a` (rule cascade) + `§12c`/`§16.2` (authoring) + `§13`/`A.43` (env_rule_* + artifact-share events), `01_KERNEL §2`/`A.2`/`A.3`/`§13.7` (source-8 generalization), `06_DOMAIN §7.6.3` (`env_rule_kinds`) + `§6.3` (tier reuse note), `07_ARTIFACTS §4` (`owning_env_id`/`sharing_policy_ref`) + `§4a` (`ArtifactSharingPolicy`/`AccessGrant`, `artifact-share/1`/`access-grant/1`) + `§5.2`/`§14`/`§10` (enforcement + IPLD/OCI), `09_PROTOCOLS §7.4`/`§7.6` (registry) + `§3`/`§3F`/`§8` (distribution/discovery alignment), `00_VISION` (J3 clarification + §11 R-v1.0-13/14), `14_DECISIONS` (ADR-0052..0056), `12_GLOSSARY` (EnvironmentRule, ArtifactSharingPolicy, AccessGrant); `11_ACCEPTANCE_TESTS.md` (A-ER* 9 tests, A-AB21-27).
  - Backlog #18 primitives: `04_PROJECT §26a.10` (`BridgeReductionPlan` + `BridgeReductionEntry`), `06_DOMAIN §5.7` (`AttestationEquivalencePolicy` + `AgreementHistory`); `11_ACCEPTANCE_TESTS.md §9l` (A-BRP* bridge reduction plan, A-AEP* attestation equivalence policy).
- Glossary entries for the v1.0.14 primitives: `12_GLOSSARY.md` (AttestationEquivalencePolicy, BridgeReductionEntry, BridgeReductionPlan).
- Glossary entries for the v1.0.13 primitives: `12_GLOSSARY.md` (CorpusDriftMetric, CrossEnvProactiveOffer, GuestPresence, ReplicatedAttestationFrontierComposition, SupersessionCascade, Wake Path 6).
- Glossary entries for the v1.0.12 primitives: `12_GLOSSARY.md` (AggregateEvent, AssetGroupEnvelope, BatchStateAdvancement, EventAggregationPolicy, StagedRolloutEnvelope).
- Glossary entries for the existing primitives: `12_GLOSSARY.md` (Body, BodyBinding, BridgeCalibrationBinding, BridgeInstallerKind, BulkKindProposal, BudgetPledge, ColdStartProposalCalibration, ConservationInvariantRef, Curriculum, DeferredAdmission, DerivationProvenanceEdge, DistressDetectionRoutingPolicy, DomainHarvest, DomainPrecedentImport, DriftBoundsEnvelope, ElaborationPolicy, HazardousSkillTeachingGate, LeadHandoffCeremony, LearnerCompetencyAttestation, LearnerStateRecord, LessonPlan, LifecycleEvent, MasteryCheckpoint, MidProjectForkComposition, MissionCharter, MultiPrincipalAttestationQuorum, ObligationReassignment, operator_blind_mode, PersonaConsultation, PlannedDeparture, PolicyEnvelope, principal_attribution_id, PrincipalAttribution, PrincipalRef, ProbeBudgetEnvelope, ProbeBudgetPledgeRequest, RelationshipReviewCheckpoint, ReplicationBound, ResourceStockEnvelope, retired_persona_response_policy, RetiredStatePersistencePolicy, SeedGoal, SingleProjectPromotionConfig, TeachingAuthorisation, UserBoundary, UserMemorySelectionRequest, UserMemoryTransparencyRequest, UserRelationshipReleaseRequest).
