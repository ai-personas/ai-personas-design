---
title: PersonaOS v1.0 — Tasks and Acceptance
status: Stable
---

# 03 — Tasks and Acceptance

> **Reader guide.** Every piece of work in PersonaOS is a *task*. In this document, you'll learn how the system classifies work into 10 types, decides when work is "done" through 8 acceptance pathways, and routes tasks to the right workspace and personas. **Prerequisites:** `00_VISION.md` (invariant J4), `01_KERNEL.md` (safety floor). **Key terms:** *task class* = what kind of work this is (question, creative request, conversation, etc.); *acceptance pathway* = how "done" is determined (computer check, panel review, user approval, etc.); *routing mode* = whether one persona, a project team, or a temporary session handles the task.

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). This document specifies the ten **seed** task classes, the eight **seed** acceptance pathways, the 3 routing modes (A / B / C), the task classifier + demotion ladder, and the canonical AnswerPackage. Per [§2a](#2a-orchestration-is-emergent--classes-pathways-and-the-run-loop-are-coordination-shapes) (ADR-0066) these are emergent KindRegistry kinds, not a closed set; orchestration itself is emergent. It realises invariant J4 (reframed as a property invariant — acceptance is signed, floor-cleared, and trust-calibrated to its orchestration) and INV_R1…INV_R11 for round-based pathways.

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. Fully normative; RFC 2119 keywords carry normative force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174).

**In scope.** Task classification (10 task classes), acceptance pathway selection (8 pathways: VERIFIER_ACCEPT, PANEL_ACCEPT, USER_ACCEPT, MUTUAL_ACCEPT, ENGAGEMENT_ACCEPT, GOAL_PROGRESS_ACCEPT, OPEN_ENDED, PROJECT_PROGRESS_ACCEPT — see §3), the three routing modes (A — single-persona / B — small ensemble / C — full-round), the task classifier and demotion ladder, the canonical AnswerPackage payload, and INV_R1…INV_R11 round invariants where they apply.

**Out of scope.** Kernel signing / sandbox / lineage primitives (see [`01_KERNEL.md`](01_KERNEL.md)); persona internals (see [`02_PERSONA.md`](02_PERSONA.md)); environment surfaces (see [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md)); the artifact lifecycle and verifier_recipe invocation (see [`07_ARTIFACTS.md`](07_ARTIFACTS.md)); the schema-registry entry for AnswerPackage (see [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry)).

**Supersession.** Subsumes prior acceptance routing and task-class expansion. The synonym `verdict path` is forbidden; use `acceptance pathway` per [`SPEC_CONVENTIONS.md §10`](SPEC_CONVENTIONS.md#10-terminology).

**Structural deviation.** Follows the compressed-opening pattern of [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md#33-compressed-opening-permitted): Background, Goals, and Definitions are folded into §1 ("The shift") and the substantive specification sections. The three §3.1 bookends (this section, the Risks table, and Open Questions) are present.

## 0a. Plain-Language Guide

Here's how work flows through PersonaOS, explained without jargon. If you have never read a technical specification before, start here.

**What is a task?** A task is any piece of work you give the system -- a question, a creative request, a conversation, or a call for emotional support. Every interaction starts as a task.

**The 10 task classes -- types of work.** The system sorts your request into one of ten categories, like bins at a post office. Each bin gets handled differently.

- *Convergent* -- one right answer ("What is 12 times 15?"). Checked by a computer.
- *Divergent* -- many possible good answers ("Draft a marketing plan"). Scored by a panel of judges.
- *Mixed* -- part right-answer, part creative ("Design a circuit and write the brief"). The factual part is checked first, the creative part is judged.
- *Interactive* -- back-and-forth toward a goal ("Help me debug this code"). Progress is measured turn by turn.
- *Relational* -- emotional support ("I am having a hard day"). No finish line; what matters is that the conversation feels supportive.
- *Pedagogic* -- teaching ("Teach me calculus"). The system tracks whether you are learning and asks you to confirm when you feel ready.
- *Performative* -- entertainment ("Tell me a story"). Continued engagement is the quality signal.
- *Existential* -- deep personal moments ("My father just died"). The system focuses on being present; trajectory quality matters.
- *Delegated* -- one persona hands work to another. The handed-off work inherits whatever rules apply to its own type.
- *Investigative* -- multi-session research ("Explore whether this conjecture is true"). Requires a project; moves through exploration, verification, synthesis, and expert review.

**The 8 acceptance pathways -- how the system knows work is "done."** Each task class maps to a way of deciding when the work is complete.

1. *Programmatic verification* -- a computer check confirms the answer, like running a test suite.
2. *Panel of judges* -- independent judges score the output against a rubric.
3. *You say yes* -- you explicitly approve ("Yes, that looks good").
4. *Both sides agree* -- you and the persona both sign off.
5. *Engagement continues* -- your continued participation is the signal. Used for storytelling.
6. *Goal advances* -- the system tracks measurable progress toward a declared goal, turn by turn.
7. *Open-ended trajectory* -- no single "done" moment. Quality is assessed by the overall arc. Periodic check-ins ask, "Is this still helpful?"
8. *Project progress* -- a milestone is reached, a conjecture proven or disproven, or an obligation fulfilled.

**The 3 routing modes -- where work happens.**

- *Mode A* -- your request goes to an existing room ("environment") where personas already live. One picks it up.
- *Mode B* -- your request goes to a project room with access to milestones, open problems, and project history.
- *Mode C* -- a quick one-off. The system creates a temporary room, handles your request, and archives it when done.

**ClarifyTurn -- when the system is not sure what you meant.** If your request is ambiguous ("Build me something cool"), the system pauses and offers 2 to 4 interpretations. Your choice is recorded so it knows exactly what you intended.

**How the dispatcher works.** The dispatcher is the traffic controller. It figures out: Do we need to clarify? What kind of work is this? Which acceptance pathway? Where should it happen? Who handles it? Then it routes accordingly.

**Naming a persona vs. not naming one.** If you say "Ask the historian about Roman aqueducts," the system finds that persona, picks the best room (by topic, recent activity, or privacy), and routes the task there. If the persona is dormant (inactive because not recently needed), it wakes up automatically -- Wake Path 6. If you do not name anyone, the system picks the best available persona or creates a temporary session.

**AnswerPackage -- what you get back.** When work is done, the system bundles the result into an AnswerPackage: the answer itself, how it was accepted, who contributed, cost, an audit trace, and any honest limitations. Think of it as a receipt stapled to the deliverable.

**INVESTIGATIVE tasks -- multi-session research.** These are the most complex tasks, potentially spanning weeks. They move through four phases: (1) *Exploration* -- broad search, proposing conjectures. (2) *Verification* -- rigorous testing with external tools like proof checkers. (3) *Synthesis* -- assembling verified pieces into a coherent whole. (4) *Expert review* -- peer review before acceptance. Investigations can loop back -- if verification disproves a conjecture, the team returns to exploration. Each phase has a budget so no single phase consumes all resources.

For full technical detail on any concept above, see the corresponding section in the body of this document and the [Technical Appendix](#technical-appendix) at the end.

## 1. The shift

v1.0 routes every [task](12_GLOSSARY.md#t) through a task class to an [acceptance pathway](12_GLOSSARY.md#a), via a routing mode. The [kernel](12_GLOSSARY.md#k) classifies the task, picks the pathway, dispatches to the right [environment](12_GLOSSARY.md#e) + members, and evaluates acceptance per pathway. The **10 task classes**, **8 acceptance pathways**, and **3 routing modes** described in this document are the STANDARDISED **seed** kinds; per [§2a](#2a-orchestration-is-emergent--classes-pathways-and-the-run-loop-are-coordination-shapes) (ADR-0066) they are not a closed set — orchestration is emergent, and the run loop itself is a coordination shape personas evolve in their environment.

*Task-flow diagram: task arrives, kernel classifies, picks pathway, dispatches via routing mode, persona responds, kernel evaluates acceptance, AnswerPackage returned.* See [Appendix A.1](#appendix-a1--task-flow-diagram-1).

**Tests:** A-T1 (classifier latency), A-T13–A-T15 (routing modes A / B / C), A-T19 (AnswerPackage status enum). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 2. The ten seed task classes

*The ten classes below are the STANDARDISED **seed** task-class kinds (per [§2a](#2a-orchestration-is-emergent--classes-pathways-and-the-run-loop-are-coordination-shapes) / ADR-0066), not a closed set. New classes are emergent KindRegistry kinds.*

*Table mapping each of the 10 seed task classes to an example and its default acceptance pathway.* See [Appendix A.2](#appendix-a2--ten-task-classes-table-2).

### 2.1 TaskClass classification

The kernel classifies at orient time:

*`TaskClassEstimate` dataclass: captures the primary class, confidence, secondary fallback classes, and classification rationale.* See [Appendix A.3](#appendix-a3--taskclassestimate-dataclass-21).

Classification is **fallible**. If classification is wrong at runtime (e.g., classified CONVERGENT but no usable verifier emerges), kernel **demotes** to MIXED or DIVERGENT with signed `class_demotion` event.

### 2.2 Demotion paths

*Demotion ladder: CONVERGENT demotes to MIXED or DIVERGENT; MIXED demotes to DIVERGENT; INVESTIGATIVE demotes to DIVERGENT or OPEN_ENDED.* See [Appendix A.4](#appendix-a4--demotion-paths-22).

All demotions are signed lineage events.

### 2.3 INVESTIGATIVE sub-modes

A single INVESTIGATIVE session moves through up to four **sub-modes**. Each has its own discipline rule, chosen by the persona per-round (signed via MODE_ENTRY); each maps to a different acceptance signal that feeds the project-progress evaluator.

*Table of four INVESTIGATIVE sub-modes (exploration, verification, synthesis, expert_review) with dominant modes, discipline rules, and acceptance signals.* See [Appendix A.5](#appendix-a5--investigative-sub-modes-table-23).

Sub-mode entry is signed (`SUBMODE_ENTRY` event scoped to the INVESTIGATIVE session). A session may revisit sub-modes; the typical arc is `exploration → verification → synthesis → expert_review`, but back-edges are common (e.g., verification refutes a conjecture → return to exploration).

### 2.4 INVESTIGATIVE sub-task taxonomy

An INVESTIGATIVE task decomposes into sub-tasks of other classes. The investigation as a whole is INVESTIGATIVE; each sub-task retains its own class and gets the appropriate verifier.

*Decomposition tree: an INVESTIGATIVE task broken into sub-tasks (INTERACTIVE, CONVERGENT, DIVERGENT) each with its own class and verifier.* See [Appendix A.6](#appendix-a6--investigative-sub-task-taxonomy-24).

Each sub-task gets its own AnswerPackage; the parent INVESTIGATIVE task's `project_state_delta` aggregates over sub-task lineage. Sub-task pathway inheritance follows the DELEGATED rule (§2.6).

### 2.5 INVESTIGATIVE per-mode budget

Budget is allocated per sub-mode within a session, with degradation rules when a sub-mode exceeds its share.

*Budget allocation table: exploration 35%, verification 40%, synthesis 15%, expert_review 10%, with session and project totals and degradation rules.* See [Appendix A.7](#appendix-a7--investigative-per-mode-budget-25).

Operator policy may override per-project. The kernel signs each sub-mode budget tick; overruns produce signed `SUBMODE_BUDGET_EXHAUSTED` events.

**Budget profile resolution.** The defaults above are tuned for reasoning-heavy INVESTIGATIVE work (math, software research). Document-heavy regulated physical domains (residential construction parsing IRC + IBC + NEC + geotech reports; clinical care parsing referral packages) routinely exhaust the session cap on ingestion before reasoning begins. v1.0 resolves session budget per the following precedence:

*Budget profile resolution precedence: EnvironmentBlueprint override > DomainContext profile > v1.0 default. Profiles: reasoning_heavy, document_heavy, tool_heavy, balanced.* See [Appendix A.8](#appendix-a8--budget-profile-resolution-25).

Profile inference: when DomainContext is emergent, the kernel infers a recommended profile from KnowledgeIngestionRecord median size and OutcomeKind family (`06_DOMAIN §2 + §6.1`). The DomainCurator (`06_DOMAIN §10`) may set the field explicitly; operator policy may override. The kernel signs profile transitions; profile is included in the snapshot for audit reproducibility.

### 2.6 DELEGATED — inheritance and lineage depth

DELEGATED tasks are persona-to-persona handoffs via cohort assembly or A2A. The class itself carries no acceptance pathway — it **inherits** from the resolved sub-task pathway.

*DELEGATED inheritance semantics: inheritance, audit lineage requirement, sub-task pathway resolution, and overall acceptance rules.* See [Appendix A.9](#appendix-a9--delegated-inheritance-semantics-26).

Cross-persona delegation depth is bounded by `max_delegation_depth` (default 3) to prevent unbounded recursion. Each level adds one signed `DELEGATION_PROPOSE` to lineage. Delegation reaches personas in the same env, **a different env, or a different node** (kernel) in the global object space; the cross-env / cross-node case composes this class with the bilateral consent protocol of `15_COORDINATION_SHAPES §4.7` and is specified as `CrossEnvTaskDelegation` in [§4.5](#45-cross-env--cross-node-task-delegation--placement).

### 2.7 Cognitive functions by task class

Each of the 10 task classes invokes a dominant subset of v1.0's 14 cognitive modes. The persona may enter any mode (per its `mode_proficiencies`), but dispatch defaults bias toward the dominant subset.

*Table mapping each task class to its dominant generation, critique, evidence, decision, and synthesis/relational cognitive modes.* See [Appendix A.10](#appendix-a10--cognitive-functions-by-task-class-27).

A persona's `primary_disposition` biases mode selection when multiple modes are equally appropriate. The dispatcher signs MODE_ENTRY for each round; verifier dispatch follows active_mode, not primary_disposition (v1.0 §02 §5).

**Tests:** A-T2 (CONVERGENT → VERIFIER_ACCEPT), A-T3 (DIVERGENT → PANEL_ACCEPT), A-T4 (MIXED), A-T5 (INTERACTIVE → GOAL_PROGRESS_ACCEPT), A-T6 (RELATIONAL → USER_ACCEPT), A-T7 (PEDAGOGIC), A-T8 (PERFORMATIVE → ENGAGEMENT_ACCEPT), A-T9 (EXISTENTIAL → OPEN_ENDED), A-T10 (DELEGATED), A-T11 (INVESTIGATIVE → PROJECT_PROGRESS_ACCEPT), A-T25 (mode-by-class dispatcher bias). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 2a. Orchestration is emergent — classes, pathways, and the run loop are coordination shapes

*This section is normative. It reframes the ten task classes (§2) and eight acceptance pathways (§3) per [ADR-0066](14_DECISIONS.md#adr-0066--self-organizing-orchestration-the-run-loop-is-an-emergent-coordination-shape-not-a-fixed-dispatcher). It extends ADR-0045 (emergent coordination) to the run loop itself: how work is classified, sequenced, evaluated, and accepted is **emergent persona behaviour in the environment, not a fixed kernel loop.***

**The reframe.** v1.0.x treated the task classes, acceptance pathways, routing modes, and the INVESTIGATIVE phase arc as a closed, kernel-fixed set. This reproduced, at the orchestration layer, the C4-meta-level contradiction that [ADR-0045](14_DECISIONS.md) removed for coordination: the substrate was agnostic about *content* and *coordination* but not about *orchestration*. ADR-0066 closes that gap.

1. **`TaskClass` and `AcceptancePathway` are emergent KindRegistry kinds.** They are resolved by name and promoted through the same four-stage lifecycle (EMERGENT → RECOGNISED → AUTHORITATIVE → STANDARDISED) as every other kind ([`06_DOMAIN §7.5–§7.6`](06_DOMAIN.md#75-emergent-kind-proposals-v10--substrate-domain-agnostic)). Substrate code MUST resolve them from the registry and MUST NOT branch on a closed `Literal[...]` of class or pathway names ([`C4`](00_VISION.md#3-invariants-j1j9), the ADR-0006 conformance line extended to orchestration).

2. **The run loop is an emergent orchestration coordination shape.** The dispatcher sequence (clarify → classify → route → execute → evaluate → accept) and phase structures (e.g. the INVESTIGATIVE four-phase arc of §2.3) are compositions of the coordination meta-mechanisms — primarily `StagedSequence` with gates — declared in the environment's `EnvironmentCoordinationProfile`, NOT kernel constants. See [`15_COORDINATION_SHAPES.md §4a`](15_COORDINATION_SHAPES.md#4a-orchestration-scope--coordinating-the-task-execution-loop).

3. **The v1.0 set ships as STANDARDISED seed kinds.** The ten task classes (§2), eight acceptance pathways (§3), three routing modes, and the INVESTIGATIVE phase arc enter the registry pre-promoted at STANDARDISED tier. They remain the default mapping verbatim; existing behaviour, the J4 seed table ([`00_VISION §3 A.1`](00_VISION.md#3-invariants-j1j9)), and the L1/L2 conformance levels are unchanged — they now describe *seed* kinds rather than a closed enum.

4. **Orchestration is fully open.** A persona MAY propose an arbitrary task class, acceptance pathway, run-loop shape, or **new kernel-level acceptance primitive** (the coordination meta-mechanism set is itself extensible by promotion). The kernel does NOT restrict orchestration topology and MUST NOT refuse a proposal merely because it is novel.

5. **Safety is preserved by trust-calibration, not by restricting topology** ([`J4`](00_VISION.md#3-invariants-j1j9), [`J5`](00_VISION.md#3-invariants-j1j9)). Every orchestration action MUST be signed and lineage-tracked (J2/J9), floor-cleared (J3, all eight sources, most-restrictive-wins), and budget-admitted (INV-7). A verdict produced by an emergent or unvalidated acceptance method MUST enter at EMERGENT trust and degrade honestly until validated — exactly as emergent-domain outputs do ([`C3`](00_VISION.md#3-invariants-j1j9)) — and the AnswerPackage MUST record the producing orchestration kind and its promotion stage so downstream consumers and audits see the provenance. "Fully open" means open *topology*, never bypass of the floor or signing.

6. **Operator gates and pins are retained.** Safety-critical proposed pathways and orchestration shapes MUST hit the [`C2`](00_VISION.md#3-invariants-j1j9) operator gate before promotion. Operator policy (floor source 4) MAY pin a minimum-trust or specific seed pathway for a task family (e.g. "safety-critical CONVERGENT work MUST use a STANDARDISED VERIFIER_ACCEPT-class pathway"), giving deployments a hard floor on acceptance methods where they want one.

*`TaskClass` and `AcceptancePathway` are registered as KindRegistry-resolved schemas; see [`09_PROTOCOLS.md §7.2`](09_PROTOCOLS.md#72-acceptance--task). The classifier (§2.1) and demotion ladder (§2.2) operate over the resolved kind set, not a hardcoded enum; a proposed class with no usable acceptance kind demotes per §2.2 with a signed event.*

**Tests:** A-EO1–A-EO13 (emergent orchestration: seed-kind resolution, persona-proposed pathway admitted under trust-calibration, novel pathway not refused for novelty, unvalidated-pathway verdict carries EMERGENT trust, floor/signing never bypassed, safety-critical pathway gated by C2, operator pin honoured, run-loop-as-StagedSequence, promotion-threshold gate, trust-decay demotion, bounded-compositional policy). See [`11_ACCEPTANCE_TESTS.md §9o`](11_ACCEPTANCE_TESTS.md). Seed-mapping tests A-T2–A-T11 continue to hold against the STANDARDISED seed set.

## 2b. Orchestration-kind promotion — trust-decay curve, evidence threshold, and the bounded-compositional policy profile

*This section is normative. It resolves [OQ-TASKS-6](#9a-open-questions) and operationalises the trust-calibration guarantee of [§2a](#2a-orchestration-is-emergent--classes-pathways-and-the-run-loop-are-coordination-shapes) ([ADR-0066](14_DECISIONS.md#adr-0066--self-organizing-orchestration-the-run-loop-is-an-emergent-coordination-shape-not-a-fixed-dispatcher)): how an emergent acceptance pathway accrues and loses trust, when it auto-promotes EMERGENT → RECOGNISED, when it demotes, and how an operator may pin the bounded-compositional set where they want a hard floor on acceptance methods. It reuses the domain promotion ladder ([`06_DOMAIN §7.6`, A.61](06_DOMAIN.md#76-kindregistry-and-the-cross-domain-metaregistry)) and the EWMA trust mechanism ([`04_PROJECT`](04_PROJECT.md)); the orchestration-specific axis is **acceptance soundness** — an emergent pathway's failure mode is silently accepting poor work ([`R-TASKS-7`](#9-risks--known-limitations)), so its evidence is measured against an independent reference, not just usage volume.*

### 2b.1 Verdict trust-decay curve

An emergent `AcceptancePathway` — and any emergent orchestration shape that produces an acceptance verdict — carries a `pathway_trust ∈ [0, 1]`, signed in lineage and surfaced on every `AnswerPackage` it produces (per §2a.5). It is initialised in the **EMERGENT band** (`pathway_trust ≤ 0.6`, the same RECOGNISED cut as the domain ladder, [`06_DOMAIN`](06_DOMAIN.md)) and updated by an **asymmetric EWMA** over verdict outcomes:

- a **confirmed** verdict (the pathway's accept/reject agreed with an independent reference — §2b.2) pulls trust toward `1.0` with gain `α_up`;
- a **disconfirmed** verdict (a false-accept or false-reject caught: user override, post-acceptance rework within the horizon, downstream verifier-cascade failure, or panel reversal) pulls trust toward `0.0` with gain `α_down`, where **`α_down > α_up`** by default — soundness errors are costlier than corroborations are valuable, so trust falls faster than it rises;
- an **unused** pathway's trust **decays toward the EMERGENT floor** on a staleness half-life (the same attention-half-life mechanism as [`05_ENVIRONMENT`](05_ENVIRONMENT.md)): a pathway that stops earning evidence loses standing rather than coasting on past corroboration.

Defaults (operator-tunable via the policy profile, §2b.4): `α_up = 0.10`, `α_down = 0.25`, staleness half-life `= 90 d`. These are not safety floors — the floor (J2/J3/J9/INV-7, §2a.5) is non-bypassable regardless of `pathway_trust`; the curve governs only how much *weight* a verdict carries downstream.

### 2b.2 Evidence threshold — EMERGENT → RECOGNISED

Promotion is **kernel-auto with operator review queue** (mirroring [`06_DOMAIN A.61` / `A.24`](06_DOMAIN.md)) when ALL of the following hold across the evidence window:

- **(a) breadth** — ≥ `K = 5` distinct accepted tasks across ≥ `M = 2` distinct principals or environments (a pathway proven on one principal's work has not shown it generalises);
- **(b) acceptance-soundness agreement** — verdicts agree with an **independent reference** at ≥ `0.90`, with **zero unreviewed false-accepts** in the window. The reference is, in priority order: (i) a STANDARDISED **seed** pathway run in **shadow** over the same tasks; or, where no seed pathway is applicable, (ii) a **post-hoc ground-truth signal** (no user override, no rework within the horizon, downstream verifier cascade clean). Agreement is computed only over verdicts with a resolved reference; an unresolved window does not promote;
- **(c) floor cleanliness** — zero signing/floor/budget violations (J2/J3/J9/INV-7) attributable to the shape across the window;
- **(d) proposer standing** — proposer fitness > median for their role (reuses the [`06_DOMAIN A.24`](06_DOMAIN.md) PROMOTED criterion), guarding against a single low-standing persona minting its own lenient acceptance method.

**Safety-critical pathways do not auto-promote.** A pathway routed to safety-critical task families requires the [`C2`](00_VISION.md#3-invariants-j1j9) operator signature at EMERGENT → RECOGNISED (it is a blocking gate, not a review queue), consistent with §2a.6 and the [`06_DOMAIN`](06_DOMAIN.md) WHEN-SAFETY-CRITICAL ladder. Under principal-collapse ([`01_KERNEL §2.4`](01_KERNEL.md)) the signature is replaced by the degraded gate (cool-down + non-principal attestation + signed acknowledgement).

RECOGNISED → AUTHORITATIVE → STANDARDISED follow the standard kind ladder ([`06_DOMAIN`](06_DOMAIN.md)); each higher tier raises the breadth/agreement bars and, for safety-critical pathways, the operator-signature requirement.

### 2b.3 Demotion

A RECOGNISED (or higher) pathway demotes one stage on either trigger, each emitting a signed `orchestration_kind_demoted` lineage event:

- **trust collapse** — `pathway_trust` falls below the stage's retention band (e.g. below `0.6` for RECOGNISED) under the §2b.1 curve; or
- **consecutive disconfirmations** — `N = 3` consecutive disconfirmed verdicts (the [`06_DOMAIN A.24`](06_DOMAIN.md) REVOKED analogue), independent of the smoothed trust value, to catch a fast-onset soundness regression before the EWMA absorbs it.

Demotion re-subjects the pathway's verdicts to EMERGENT-trust calibration; in-flight tasks already accepted are not retroactively reopened, but their `AnswerPackage` provenance already records the producing stage, so audits see which verdicts issued under the now-demoted pathway.

### 2b.4 The bounded-compositional policy profile

Per OQ-TASKS-6's second clause: **yes — the bounded-compositional mode is offered as a selectable operator policy profile**, not as a substrate default. ADR-0066 keeps `fully_open` as the substrate default (maximal emergence; safety from trust-calibration, not topology restriction); operators who want a hard a-priori floor on *acceptance methods* select the bounded profile per environment or per task family via operator policy (floor **source 4**). The profile is an `OrchestrationPolicyProfile` ([`09_PROTOCOLS §7.2`](09_PROTOCOLS.md#72-acceptance--task)) with two named values:

- **`fully_open`** *(default, ADR-0066)* — personas MAY propose arbitrary acceptance pathways, run-loop shapes, AND new kernel-level acceptance primitives (the meta-mechanism set is itself extensible by promotion, per [`15_COORDINATION_SHAPES §4a`](15_COORDINATION_SHAPES.md#4a-orchestration-scope--coordinating-the-task-execution-loop)). All emergent verdicts are trust-calibrated per §2b.1–§2b.3.
- **`bounded_compositional`** — emergent orchestration MAY compose only from the **STANDARDISED seed acceptance primitives** (the seed meta-mechanism set: `StagedSequence`, `DerivedMetric`, `StreamPolicy`, `EntityGroup`, `BatchOperation`, and STANDARDISED-tier acceptance kinds). A proposal of a **new kernel-level acceptance primitive** is **refused** at admission with a signed `orchestration_primitive_refused_by_policy` advisory naming the governing policy; **novel compositions of seed primitives remain admissible** and are still trust-calibrated. This is the direct analogue of ADR-0045's bounded-compositional coordination model, scoped to acceptance, and keeps kernel acceptance-soundness validation tractable for deployments that prize it over maximal emergence.

The profile binds at the same granularity as an operator pathway pin (§2a.6): a deployment MAY run `fully_open` globally but `bounded_compositional` for a named safety-critical task family. The profile governs *what may be proposed*; it never relaxes the floor (J3) or signing (J2/J9), which apply identically under both.

**Tests:** A-EO11 (promotion gated on the §2b.2 evidence threshold; under-evidenced pathway stays EMERGENT), A-EO12 (trust-decay + consecutive-disconfirmation demotion per §2b.1/§2b.3), A-EO13 (`bounded_compositional` refuses a novel kernel-level primitive while admitting a novel seed composition; `fully_open` admits both). See [`11_ACCEPTANCE_TESTS.md §9o`](11_ACCEPTANCE_TESTS.md).

## 3. The eight seed acceptance pathways

*The eight pathways below are the STANDARDISED **seed** acceptance-pathway kinds (per §2a / ADR-0066), not a closed set. New pathways are emergent KindRegistry kinds proposed by personas and trust-calibrated under J4.*

*Table of all 8 seed acceptance pathways with their semantics.* See [Appendix A.11](#appendix-a11--eight-acceptance-pathways-table-3).

### 3.1 Pathway details

#### VERIFIER_ACCEPT (CONVERGENT)

*Verifier cascade: 3 stages (fast/medium/expensive), each must pass; failure extracts constraints to ProvenFacts; verifier rotation per INV-6.* See [Appendix A.12](#appendix-a12--verifier_accept-pathway-31).

#### PANEL_ACCEPT (DIVERGENT)

*Judge panel: minimum 3 judges from 2+ model families, cyclic rotation, position-swap, rubric-scored, anti-Goodhart stack, dissent resolution via Curator.* See [Appendix A.13](#appendix-a13--panel_accept-pathway-31).

#### USER_ACCEPT

*User explicitly approves output via button, verbal confirmation, or implicit proceeding; timeout produces "user_no_response" status.* See [Appendix A.14](#appendix-a14--user_accept-pathway-31).

#### MUTUAL_ACCEPT

*Both persona and user(s) co-sign acceptance for collaborative work.* See [Appendix A.15](#appendix-a15--mutual_accept-pathway-31).

#### ENGAGEMENT_ACCEPT (PERFORMATIVE)

*Quality measured by continued engagement signal (user re-prompts within window); NOT attention-economy metrics; operator-configurable window.* See [Appendix A.16](#appendix-a16--engagement_accept-pathway-31).

#### GOAL_PROGRESS_ACCEPT (INTERACTIVE, PEDAGOGIC)

*Declared goal at task start; per-turn judge assesses progress; acceptance fires when horizon ends and goal achieved. Includes learner-acknowledgement step for PEDAGOGIC mastery.* See [Appendix A.17](#appendix-a17--goal_progress_accept-pathway-31).

#### OPEN_ENDED (RELATIONAL, EXISTENTIAL)

*No discrete acceptance event; trajectory quality assessed retrospectively; periodic USER_ACCEPT checkpoints surfaced; quality signals include mode discipline and persona reflection.* See [Appendix A.18](#appendix-a18--open_ended-pathway-31).

#### PROJECT_PROGRESS_ACCEPT (INVESTIGATIVE)

*Task accepted when project state advances (milestone, conjecture, obligation, artifact bundle, ambient signal); aggregate progress score with stall detection; phase-aware stall suppression for external dependencies.* See [Appendix A.19](#appendix-a19--project_progress_accept-pathway-31).

**Tests:** A-T2–A-T11 (per-pathway routing), A-T16 (PANEL_DISSENT escalation), A-T17 (PROJECT_PROGRESS_ACCEPT ambient signals), A-T22 (INVESTIGATIVE sub-mode budgets). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

### 3.2 RelationshipReviewCheckpoint — periodic OPEN_ENDED quality surface

OPEN_ENDED quality assessment was specified as post-hoc only ("trajectory-based"; no real-time acceptance event), with R-TASKS-5 noting "periodic reflection checkpoints + user-feedback surface during execution; A-T9 acceptance test" deferred to v1.2. SCENARIO 08 made the gap concrete: Sarah talking to companion persona Halia daily for 6 months had no substrate-shape signal for "let's pause and reflect on whether this is still serving you." The spec includes `RelationshipReviewCheckpoint`.

*`RelationshipReviewCheckpoint` dataclass: periodic review surface for long-arc relational interactions, with schedule triggers, persona-drafted review summary, user response options, and lifecycle states.* See [Appendix A.20](#appendix-a20--relationshipreviewcheckpoint-dataclass-32).

**Admission rule.**

*Admission rule for RelationshipReviewCheckpoint: cadence triggers, persona drafting, user response lifecycle, unanswered-checkpoint escalation, and cadence configuration bounds.* See [Appendix A.21](#appendix-a21--relationshipreviewcheckpoint-admission-rule-32).

**Composition with `OPEN_ENDED` (§3 pathway).** The checkpoint is the substrate-shape signal that OPEN_ENDED lacked. OPEN_ENDED quality remains post-hoc trajectory-judged for its primary acceptance signal; the checkpoint adds a *periodic intentional surface* without changing the pathway's nature.

**Composition with `02_PERSONA §11.4a / §11.6a / §11.7a / §11.7b`.** A checkpoint's `request_changes` and `request_release` user responses naturally chain to UserBoundary updates, UserMemoryTransparencyRequest, UserMemorySelectionRequest, or UserRelationshipReleaseRequest. Deployments may offer chained UI; substrate keeps each primitive independently signed.

**Composition with `companion`-class env blueprints.** Solo envs running blueprints like `companion_space` are the primary use case; substrate ships the cadence on a default-on basis for such envs. Project_workspace envs do NOT default-on the relationship review checkpoint (they have their own milestone + completion ceremony mechanism via `04_PROJECT §4.1`); operator policy may opt project envs in if useful.

**Honest limits.**

1. **User non-engagement is a soft signal.** Unanswered checkpoints suggest disengagement but could also reflect "no changes needed, no comment." Operator should not auto-escalate on a single unanswered checkpoint; pattern matters.
2. **Persona-drafted review is self-report.** Persona may over- or under-report their observations. The checkpoint surface is structural (mandatory periodic surface), not adversarial verification.
3. **Cadence tuning has trade-offs.** Frequent (e.g., 14d/10-session lower bound) burdens users; rare (365d upper bound) loses the early-intervention value. Operator policy is the place to tune; substrate enforces only the floor/ceiling.
4. **OPEN_ENDED quality remains post-hoc.** Checkpoint adds an intentional surface; it does not change the pathway's fundamental post-hoc nature.

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9h — A-RRC*`.

**Companion pathway routing note.** Envs whose primary use is long-arc relational interaction (typically SOLO envs running `companion_space`-class blueprints) SHOULD route through OPEN_ENDED pathway, not ENGAGEMENT_ACCEPT. ENGAGEMENT_ACCEPT measures continued user re-engagement as quality signal — for companionship this admits attention-economy drift (the persona optimises for "user keeps coming back" rather than "user's wellbeing improves"). The R-TASKS-3 risk ("engagement-only optimisation drifts toward attention-economy failure") is acute in companionship. Operator policy SHOULD declare `companion`-class envs as OPEN_ENDED-only. The substrate emits `companion_engagement_accept_inadvisable` advisory when a companion-class env attempts ENGAGEMENT_ACCEPT routing without explicit operator-signed exemption.

### 3.3 Curriculum + LessonPlan + MasteryCheckpoint — multi-session pedagogic structure

PEDAGOGIC tasks routed to `GOAL_PROGRESS_ACCEPT` were evaluated per-task with no structural multi-session learning-trajectory primitive. For a 20-session medical-rotation coaching arc (or a 6-month welding apprenticeship, or any structured-learning context), the substrate had no `Curriculum`, no `LessonPlan`, no `MasteryCheckpoint`. The Voyager-style "automatic curriculum" mentioned in `02_PERSONA §8` was an emergent skill-growth pattern for personas (self-curriculum), not a learner-curriculum primitive for users.

Three composing primitives:

*`Curriculum`, `LessonPlan`, and `MasteryCheckpoint` dataclasses: structured multi-session pedagogic primitives with authorship, target skills, prerequisite graphs, hazard envelopes, learner opt-in, evidence requirements, and safety-critical gates.* See [Appendix A.22](#appendix-a22--curriculum--lessonplan--masterycheckpoint-dataclasses-33).

**Admission rule.**

*Admission rules for Curriculum creation, LessonPlan execution, and MasteryCheckpoint firing, including prerequisite verification, hazard checks, and safety-critical evidence requirements.* See [Appendix A.23](#appendix-a23--curriculum-admission-rule-33).

**Composition with `02_PERSONA §11.8 LearnerStateRecord`.** The three primitives feed structured updates into the learner's state record: lesson completions write to `competency_inventory`; mastery-checkpoint reaches write to `mastery_checkpoints_reached`; attestations from `§11.9` flow through `MasteryCheckpoint.evidence_requirement = external_attestation` into the same state record.

**Composition with `02_PERSONA §11.10 TeachingAuthorisation`.** A safety-critical `Curriculum` whose hazard_envelope_max crosses `bodily_injury` requires an active TeachingAuthorisation for the authoring persona at >= that ceiling. The substrate refuses curriculum activation otherwise.

**Composition with the GOAL_PROGRESS_ACCEPT learner-acknowledgement step (§3.1).** A PEDAGOGIC task whose target is a `MasteryCheckpoint` engages the learner-acknowledgement extension; the learner's signed acknowledgement is one path to the checkpoint's evidence requirement (the persona-judged-plus-learner-acknowledged path for non-safety-critical checkpoints).

**Honest limits.**

1. **Operator policy is the locus of curriculum quality.** Substrate carries structure; pedagogical validity (is this curriculum actually good?) is operator + persona-author responsibility. Substrate refuses obviously-broken curricula (cycles, dangling refs) but cannot validate educational quality.
2. **Persona-authored curricula at safety-critical hazard levels are admissible only with operator co-sign.** A persona drafting a fatality-risk curriculum unilaterally is refused at activation; operator must explicitly authorise.
3. **Learner opt-in cannot be retroactive.** Once a curriculum is active, modifying it requires re-signing (operator + learner if `requires_learner_optin`); partial mid-arc modification has no shape — operators should treat large changes as a new curriculum instance.
4. **No automatic adaptive-curriculum primitive.** The substrate carries fixed prerequisite graphs + fixed lesson plans; "the persona adapts the curriculum based on learner performance" is per-task adaptation within the structure, not curriculum mutation. Adaptive curricula are v1.1+.
5. **Cross-persona curriculum portability is operator policy.** A `Curriculum` is signed by its authoring entity; another persona inheriting the curriculum to teach is fine but requires that persona's own `TeachingAuthorisation` for the relevant skill_kinds.

**Acceptance tests.** Co-located in `11_ACCEPTANCE_TESTS §9i — A-CUR*` (curriculum), `A-LP*` (lesson plan), `A-MASTERY*` (mastery checkpoint), `A-GPA-ACK*` (learner-acknowledgement step).

**Fork interaction.** When the teacher persona authoring/executing an active Curriculum forks mid-project, per-curriculum inheritance is governed by `MidProjectForkComposition.curriculum_inheritance` (`02_PERSONA §7.4.7`): `suspended_at_fork` (curriculum suspends; operator must re-author under named child OR archive) or `inherit_to_child` (named child inherits; learner re-confirms `requires_learner_optin = True` per standard §3.3 admission; failure to re-confirm within 14d suspends). The inherited child still requires their own `TeachingAuthorisation` (`02_PERSONA §11.10`) for any safety-critical skill_kinds — `TeachingAuthorisation` does NOT inherit on fork.

## 4. The three routing modes

*Three routing modes: Mode A (persistent env, no project), Mode B (project_workspace-typed env, v1.0 unification), Mode C (ephemeral encounter).* See [Appendix A.24](#appendix-a24--three-routing-modes-4).

### 4.0 ClarifyTurn — pre-classification disambiguation

When a task is intent-ambiguous (low classifier confidence, ambiguous verbs like *create / make / build* without a resolved object kind, scope-unbounded keywords, or a safety-critical domain emerges before the persona has agreed scope), the dispatcher runs a **ClarifyTurn** before classification + routing. The persona offers 2–4 distinct interpretations; the user's choice is signed and becomes a load-bearing lineage entry.

*`ClarifyTurn` and `CandidateInterpretation` dataclasses: disambiguation surface with trigger reasons, candidate interpretations, user response, and timeout handling.* See [Appendix A.25](#appendix-a25--clarifyturn-dataclasses-40).

**Dispatcher integration:** the dispatcher runs a clarify-check before §4.1 routing. If a clarify is needed and a fresh signed user_choice does not exist, the dispatcher returns `AwaitClarification(clarify_turn_ref)` rather than committing to a routing path. The signed ClarifyTurn lives in env lineage (Mode A/B) or task lineage (Mode C), and is referenced by the subsequent AnswerPackage so audit can recover what the user chose to mean.

**`needs_clarify` decision spec:**

*`ClarifyCheck` dataclass and `needs_clarify` function: evaluates 6 trigger reasons (low confidence, ambiguous verb, unbounded scope, unresolved object kind, safety-critical domain, undeclared horizon) with cached-choice suppression.* See [Appendix A.26](#appendix-a26--needs_clarify-decision-spec-40).

Each helper (`has_ambiguous_intent_verb`, `has_unbounded_scope_keywords`, `has_long_arc_shape`, etc.) is a kernel-local classifier in INV-6 rotation pool. Operator may tune `clarify_aggressiveness_threshold(env)` per env (defaults: low=0.4, medium=0.5, high=0.6).

**Honest limit:** ClarifyTurn adds a turn of latency. The kernel suppresses it when classifier confidence ≥ 0.8 AND no ambiguity triggers fire AND the requester has previously chosen the same interpretation for a similar fingerprint (cached signed choice). Configurable per env via `clarify_aggressiveness` (default: medium). The classifiers behind `needs_clarify` may themselves be wrong; mis-firing is signed in lineage so operator can retune.

### 4.1 The dispatcher (concrete)

*`route_task_v1` function: clarify-check, entry-point resolution (target env, target persona, or ephemeral), Mode A/B/C dispatch, Wake Path 6 integration for dormant personas.* See [Appendix A.27](#appendix-a27--route_task_v1-dispatcher-41).

### 4.2 Env selection when persona is named

When user addresses persona by name without specifying env, kernel picks:

*Environment selection priority: active context, charter+domain match, privacy hint, recency, fallback to ephemeral.* See [Appendix A.28](#appendix-a28--env-selection-when-persona-named-42).

### 4.3 Notification routing within env (Mode A and B)

*Notification pipeline: event arrives at env ambient stream, kernel checks observation surface, role, presence, urgency, attention budget; eligible members notified; each evaluates response decision (respond/defer/ignore/acknowledge).* See [Appendix A.29](#appendix-a29--notification-routing-within-env-43).

**Dormancy exception.** Normally, dormant members (`availability="dormant"`) have all notifications below `critical` urgency suppressed (`05_ENVIRONMENT §9.1`). When a task enters this pipeline via the `target_persona_id` branch of the dispatcher (§4.1), the addressed persona has already been auto-woken by Wake Path 6 (`05_ENVIRONMENT §5.2`) *before* notification routing begins. The presence-state check above therefore sees `availability="present"` or `"away"` (post-wake), not `"dormant"`. No special-case logic is needed in notification routing itself — the wake happens upstream in the dispatcher.

### 4.4 EphemeralPromotionOffer — Mode C → project upgrade

Mode C is ephemeral by default — the env archives at session end. But some Mode C sessions are *accidentally* the start of a long-arc project: the user discovers mid-conversation that they want persistence. v1.0 gave them no upgrade path; they had to manually re-create everything as a project and lose the conversation thread.

v1.0 adds an opt-in promotion offer that the kernel emits at session-end (or mid-session if heuristics trip strongly) when a Mode C conversation has the *shape* of a project. The user accepts → project + persistent env materialise with the conversation thread as session 1.

*`EphemeralPromotionOffer` dataclass: promotion surface for Mode C sessions with substrate-shape triggers, proposed project shape, user response, and materialisation references.* See [Appendix A.30](#appendix-a30--ephemeralpromotionoffer-dataclass-44).

**Trigger evaluation:**

*`evaluate_promotion_triggers` function and `Trigger` dataclass: evaluates 6 substrate-shape triggers (turn count, domain unknown, multi-artifact, long horizon, external commitment, physical asset) with per-trigger safety-critical classification.* See [Appendix A.31](#appendix-a31--ephemeral-promotion-trigger-evaluation-44).

The offer fires if ≥ 2 triggers OR any single `safety_critical=True` trigger fires. The substrate-rule for which triggers are safety-critical is **per-evaluation**, not a closed list — `domain_unknown_detected_fired` and `external_commitment_drafted` consult per-domain hazard axes, while `physical_asset_referenced` is unconditionally safety-critical. `safety_critical_outcome_kinds(env, domain_id)` resolves against KindRegistry's `outcome_kinds` family with metadata flag `is_safety_critical_outcome: bool` per §7.6.2.

**Acceptance flow:**

*Acceptance flow: user accepts, kernel materialises project + env, conversation re-anchors, draft state carries over, ephemeral env archives with preserved lineage pointer.* See [Appendix A.32](#appendix-a32--ephemeral-promotion-acceptance-flow-44).

**Invariant preserved:** Mode C remains ephemeral *by default*. The offer is opt-in; the user MUST sign acceptance. Without acceptance, the ephemeral session archives normally and no project is created.

**Honest limit:** the trigger heuristics are tunable. Operator may set `promotion_offer_aggressiveness` per env (default: medium). Over-aggressive offers are friction; under-aggressive lose legitimate upgrade candidates. The signed `user_dismissed` event on declined offers feeds a per-user calibration over time.

**Tests:** A-T13 (Mode A: present member at env, no project), A-T14 (Mode B: project_workspace env), A-T15 (Mode C: ephemeral env created + archived), A-T20 (multi-env project env selection). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

### 4.5 Cross-env / cross-node task delegation & placement

A task handled by one environment's personas may produce a sub-task that is better resolved by **a different set of personas in a different environment** — possibly on a **different node** (kernel). In the global object space (ADR-0067), the target personas/env may be local, on another env of the same node, or discovered over the global discovery planes (`09_PROTOCOLS §3G`) on a peer node. This is **not a new primitive**: it is the existing `DELEGATED` class (§2.6) **composed with** the bilateral cross-environment consent protocol (`15_COORDINATION_SHAPES §4.7`). The composition is named `CrossEnvTaskDelegation`.

**The composition.** A `CrossEnvCoordinationBinding`'s `CrossEnvInterface` (`15_COORDINATION_SHAPES §4.7`) is extended to carry, in addition to artifact handoff, a **task**: the delegated sub-task's resolved class and acceptance pathway, plus `permitted_task_classes` and `permitted_acceptance_pathways` the receiving env pre-consents to. A `CrossEnvTaskDelegation` is then an ordinary `DELEGATED` task whose delegate is reached through such a binding. It inherits the sub-task class/pathway exactly as §2.6 specifies; the delegator remains responsible for the overall outcome; `max_delegation_depth` (default 3) still bounds the chain across env and node boundaries.

*A `CrossEnvTaskDelegation` carries the parent task id, the source env (and its node), the target env (and its node, identified by global handle / DID per `01_KERNEL §4.4`), the target persona set or role kinds, the resolved sub-task class + acceptance pathway, the governing `CrossEnvCoordinationBinding` id, the required capability (a UCAN token, below), and dual `DELEGATION_PROPOSE` / `DELEGATION_ACCEPT` signatures from both envs/nodes. A `SUB_TASK_LINEAGE_LINK` points from the parent envelope to the sub-task lineage on the resolving node.*

**Consent and authorization, not command.** Per `15 §4.7` principle 1, a delegating env cannot *impose* a task on another env — even on the same node, even under the same operator. The receiving env's personas review the `CrossEnvCoordinationRequest` through their own decision process and Accept / Counter-propose / Deny. Authorization to delegate at all is an **access-level + capability** check (ADR-0067, ADR-0068): the delegator must hold at least a `submit` grant (the `write`-tier capability to enqueue work) on the target env/personas under their `AccessPolicy` (`09_PROTOCOLS §3G.3`), carried as an attenuated **UCAN capability token** chained from the delegator's DID (`09_PROTOCOLS §3F`). The token is verified before the request reaches the receiver's review; an unauthorized delegation never enters the receiver's queue.

**Placement (local vs remote node).** The dispatcher (`route_task_v1`, A.27) gains an explicit placement step for a resolved sub-task: it resolves candidate participants from (a) the local env, (b) other local envs the persona has membership in, and (c) the global discovery layer (`09_PROTOCOLS §3G`), then places the sub-task where capability, availability, access, and policy best fit. Remote placement runs the cross-env consent protocol above and, on accept, executes on the target node's personas under that node's floor + budget (constraints compose most-restrictive-wins, exactly as joined-environment execution composes, `09_PROTOCOLS §3C.3`); a guest contribution uses the existing time- and scope-limited `GuestPresence` (`05_ENVIRONMENT §11.6`). Owner-prioritized scheduling (`03_TASKS §4.6`, added with the node intake gate) orders the resulting work on each node.

**Availability before delegation.** *A `CrossEnvPresenceQuery` lets a source env ask whether a target persona is available (present / away / dormant) before committing a delegation. It is access-gated: a member of the target env (or a peer holding `read` on the persona's `AccessPolicy`) gets presence detail; a `discover`-only peer learns at most that the persona exists; an unauthorized peer gets nothing. It projects the federated presence feed of `05_ENVIRONMENT §17` / `09_PROTOCOLS §4.1`.*

**Cross-domain trust (resolves OQ-TASKS-3).** When a cross-env/cross-node sub-task crosses a **domain** boundary, its outputs are trust-calibrated to the **minimum** of (the parent task's domain trust, the resolving domain's own trust). This is the safest composition — consistent with the most-restrictive-wins rule the safety floor and `AccessPolicy` already use — and prevents a delegation from laundering low-trust work up through a high-trust parent or vice versa. The delegation lineage records the domain context at each hop.

**Cross-env lineage visibility.** *A `CrossEnvLineageVisibility` setting on the delegation governs what the resolving env may see of the parent task's lineage: `full` (shared members see the parent chain), `redacted` (link + event kinds, payloads withheld — the default, matching the §11.4 privacy invariant for cross-env links), or `existence` (only that a parent exists). It is gated by `AccessPolicy`; it never widens access a principal does not otherwise hold.*

**Tests:** A-XD1 (cross-env DELEGATED via CrossEnvCoordinationBinding, dual-signed), A-XD2 (unauthorized delegation refused at capability check before receiver review), A-XD3 (remote placement composes floor/budget most-restrictive-wins), A-XD4 (cross-domain sub-task inherits minimum trust — OQ-TASKS-3), A-XD5 (CrossEnvPresenceQuery access-gated), A-XD6 (CrossEnvLineageVisibility redacts by default). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 5. AnswerPackage

The canonical kernel return value (schema **answer/4** in v1.0).

*`AnswerPackage` dataclass: identity, answer text, status enum, pathway-specific acceptance evidence, cost, environment, artifact bundle ref, structured outcomes, lineage, audit fields, and signature.* See [Appendix A.33](#appendix-a33--answerpackage-dataclass-5).

### 5.1 Status enum semantics

*Status enum: 10 successful acceptance statuses, 5 partial/edge statuses, 8 termination statuses.* See [Appendix A.34](#appendix-a34--status-enum-semantics-51).

v1.0 adds richness to status values.

**Tests:** A-T19 (status enum covers all 23 v1.0 values), A-T24 (DELEGATED inheritance), A-T7 (PEDAGOGIC long-arc package shape). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 6. AcceptanceConfig

*`AcceptanceConfig` dataclass: per-pathway configuration (verifier cascade, judge panel, user approver, party IDs, engagement signal, goal metric, trajectory check interval, project progress evaluator).* See [Appendix A.35](#appendix-a35--acceptanceconfig-dataclass-6).

## 7. Edge cases

### 7.1 MIXED with PANEL_DISSENT escalation

*MIXED escalation: verifier gate passes, panel runs, PANEL_DISSENT triggers Curator resolution (RESAMPLE / OVERTON_BALLOT / ESCALATE_HUMAN).* See [Appendix A.36](#appendix-a36--mixed-panel_dissent-escalation-71).

### 7.2 PROJECT_PROGRESS_ACCEPT when task completes the project

*Project completion: final piece delivered, last open problem resolves, status becomes "project_progress_accept_and_completion", completion ceremony triggered.* See [Appendix A.37](#appendix-a37--project-completion-72).

### 7.3 Ephemeral demoted INVESTIGATIVE

*INVESTIGATIVE without project demotes: env type determines target class (lab/debate to OPEN_ENDED, team/community to DIVERGENT, companion to RELATIONAL, solo/pair to DIVERGENT).* See [Appendix A.38](#appendix-a38--ephemeral-demoted-investigative-73).

### 7.4 Multi-class task decomposition

*Multi-class decomposition: classifier outputs primary + secondary; kernel decomposes; relational acknowledgement first, then technical work; both sub-tasks signed.* See [Appendix A.39](#appendix-a39--multi-class-task-decomposition-74).

### 7.5 Multi-environment project — env_id not specified

*Multi-env project routing: requester presence, activity recency, or primary_environment_id fallback.* See [Appendix A.40](#appendix-a40--multi-environment-project-75).

### 7.6 Cross-domain transfer task

*Cross-domain transfer: task references domain D1 but invokes tools from D2; cross-domain transfer event emitted with anti-leakage check and trust adjustment.* See [Appendix A.41](#appendix-a41--cross-domain-transfer-76).

## 8. Performance and budget targets

*Performance targets (classification ≤200ms, routing ≤150ms, etc.) and cost targets per task class ($0.02–$0.60 per accepted task).* See [Appendix A.42](#appendix-a42--performance-and-budget-targets-8).

## 9. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations).

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-TASKS-1 | Task classifier mis-classification. Multi-class and ambiguous tasks lead to incorrect routing. | High | Medium | Demotion paths (`§4`); A-T12 acceptance test; classifier reputation tracking; per-class fingerprint cache. | v1.0 (demotion); v1.1 (reputation closed-loop). |
| R-TASKS-2 | `PROJECT_PROGRESS_ACCEPT` evaluator is heuristic. "Did this session advance the project?" may not match user intuition. | Medium | High | Composite signal (lineage + ambient); operator-tunable weights; user-override surface. | v1.0 (baseline); v1.1 (signal weight learning). |
| R-TASKS-3 | `ENGAGEMENT_ACCEPT` is gameable. Engagement-only optimisation drifts toward attention-economy failure modes. | High | Medium | Corroboration required by `USER_ACCEPT` or audit clearance before driving evolution; anti-Goodhart panel reviews engagement-led evolutions. | v1.0 (corroboration gate). |
| R-TASKS-4 | `GOAL_PROGRESS_ACCEPT` depends on goal quality. Vague goals → vague signals. | Medium | High | Operator + user co-define goals at task start; goal-quality classifier flags vague goals at admission. | v1.1 (goal-quality classifier). |
| R-TASKS-5 | `OPEN_ENDED` quality assessment is post-hoc. No real-time acceptance; trajectory quality judged retrospectively. | Medium | High | Periodic reflection checkpoints; user-feedback surface during execution; A-T9 acceptance test. | v1.0 (baseline); v1.2 (mid-trajectory probes). |
| R-TASKS-6 | Multi-class tasks add latency. Decomposition + sequencing increases tail latency. | Low | Medium | Single-class fast path retained; classifier produces estimate ≤ 200 ms p95 (A-T1). | v1.0 (baseline). |
| R-TASKS-7 | Fully-open emergent orchestration (§2a, ADR-0066) means an unvalidated persona-proposed acceptance method can be *wrong* (silently accept poor work) even though it cannot bypass the floor or signing. Acceptance-soundness verification of arbitrary methods is the new complexity bottleneck. | High | Medium | Trust-calibration (J4/J5): emergent-pathway verdicts enter at EMERGENT trust and degrade honestly; AnswerPackage records producing kind + stage; safety-critical pathways gated by C2; operators MAY pin a minimum-trust/seed pathway per task family (floor source 4). The promotion ladder (§2b) makes soundness load-bearing: trust accrues only on agreement with an independent reference (≥ 0.90) with asymmetric decay (§2b.1–§2b.2), demotes on disconfirmation (§2b.3), and operators MAY select the `bounded_compositional` profile for a hard a-priori floor on acceptance methods (§2b.4); A-EO7–A-EO13. Cross-document: also `00_VISION §11`. | v1.1 (trust-calibration + promotion ladder §2b + operator pin/profile). |

## 9a. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-TASKS-1 | Should multi-class decomposition be persona-side (classifier emits split) or kernel-side (kernel runs sub-classifiers and composes routing)? v1.0 ships kernel-side; persona-side has lower kernel cost but loses cross-task visibility. | — | v1.1 architecture review. |
| OQ-TASKS-2 | `PROJECT_PROGRESS_ACCEPT` signal weights (lineage events, ambient activity, peer interactions, milestone advancement): operator-tunable, learned-per-project, or universal defaults? | Project WG | v1.1 signal weighting. |
| OQ-TASKS-3 | DELEGATED inheritance semantics for cross-domain sub-tasks: does the sub-task inherit parent's domain trust, its own assigned domain's trust, or the minimum? | — | **Resolved (ADR-0068, §4.5):** the **minimum** of (parent domain trust, resolving domain trust) — most-restrictive-wins, preventing trust laundering in either direction. |
| OQ-TASKS-4 | INVESTIGATIVE sub-mode taxonomy (exploration / verification / synthesis / expert_review) — is four enough? Some projects have a distinct "calibration" or "rehearsal" sub-mode that doesn't fit cleanly. | Project WG | v1.1 sub-mode extension. |
| OQ-TASKS-5 | OPEN_ENDED mid-trajectory probes: how often, what cost ceiling, what user-facing UX? | — | v1.2 probe design. |
| OQ-TASKS-6 | **Resolved (v1.1) → [§2b](#2b-orchestration-kind-promotion--trust-decay-curve-evidence-threshold-and-the-bounded-compositional-policy-profile).** Fully-open orchestration (ADR-0066): what is the right default trust-decay curve and evidence threshold for promoting an emergent acceptance pathway EMERGENT → RECOGNISED, and should the bounded-compositional mode (compose only from seed primitives) be offered as a selectable operator policy profile? Resolution: asymmetric-EWMA trust-decay (α_down > α_up) with staleness half-life (§2b.1); auto-promotion gated on breadth + acceptance-soundness agreement ≥ 0.90 vs an independent reference + floor cleanliness + proposer standing, with safety-critical pathways blocked behind C2 (§2b.2); demotion on trust collapse or 3 consecutive disconfirmations (§2b.3); `bounded_compositional` offered as a selectable operator policy profile, `fully_open` retained as the substrate default (§2b.4). Default constants (K=5, M=2, agreement 0.90, α_up 0.10, α_down 0.25, staleness 90 d, N=3) remain operator-tunable; empirical re-tuning tracked below. | Task WG | Constants tuned empirically post-v1.1 deployment. |

## 10. Acceptance tests

*Full acceptance test list (A-T1 through A-T25).* See [Appendix A.43](#appendix-a43--acceptance-tests-10).

## 11. Where to read next

- Persona that responds to tasks: [`02_PERSONA.md`](02_PERSONA.md)
- Project layer where INVESTIGATIVE work happens: [`04_PROJECT.md`](04_PROJECT.md)
- Environment routing details: [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md)
- Verifier + panel mechanisms in detail: [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)

---

## Technical Appendix

All schemas, dataclass definitions, code blocks, and structured diagrams from the body of this document are collected here for reference. Each appendix entry is numbered and cross-referenced from the section where it originally appeared.

### Appendix A.1 — Task flow diagram (§1)

```text
TASK ARRIVES
   │
   ▼
KERNEL CLASSIFIES (10 classes)
   │
   ▼
KERNEL PICKS ACCEPTANCE PATHWAY (8 pathways)
   │
   ▼
KERNEL DISPATCHES VIA ROUTING MODE (3 modes: A/B/C)
   │
   ▼
PERSONA RESPONDS (with active_mode signed)
   │
   ▼
KERNEL EVALUATES ACCEPTANCE
   │
   ▼
ANSWERPACKAGE RETURNED
```

### Appendix A.2 — Ten task classes table (§2)

```text
CLASS              EXAMPLE                          DEFAULT PATHWAY
────────────────   ──────────────────────────       ──────────────────────────
CONVERGENT         "compute optimal L for buck"     VERIFIER_ACCEPT
                                                    (programmatic verifier)

DIVERGENT          "draft a product brief"          PANEL_ACCEPT
                                                    (rubric panel with
                                                     anti-Goodhart stack)

MIXED              "design DC-DC with BOM"          VERIFIER then PANEL
                                                    (gate + judge)

INTERACTIVE        "help me debug this code"        GOAL_PROGRESS_ACCEPT
                                                    (per-turn judge +
                                                     outcome judge)

RELATIONAL         "I'm having a hard day"          OPEN_ENDED +
                                                    USER_ACCEPT checkpoints

PEDAGOGIC          "teach me derivatives"           GOAL_PROGRESS_ACCEPT
                                                    (long-arc; learner
                                                     mastery growth)

PERFORMATIVE       "tell me a story"                ENGAGEMENT_ACCEPT
                                                    (continuation)

EXISTENTIAL        "my dad just died"               OPEN_ENDED
                                                    (no acceptance event;
                                                     trajectory matters)

DELEGATED          "ask the historian"              inherited from sub-task

INVESTIGATIVE      "explore generalisation of       PROJECT_PROGRESS_ACCEPT
                    monoidal categories"            (project state delta;
                                                     requires Project)
```

### Appendix A.3 — TaskClassEstimate dataclass (§2.1)

```python
@dataclass(kw_only=True)
class TaskClassEstimate:
    schema: str = "task-class-estimate/1"
    primary: Literal["convergent", "divergent", "mixed", "interactive",
                     "relational", "pedagogic", "performative",
                     "existential", "delegated", "investigative"]
    confidence: float
    secondary: list[Literal[...]]            # fallback classes
    has_executable_verifier: bool
    has_panel_rubric: bool
    has_interactive_loop: bool
    requires_project_context: bool
    rationale: str

def classify_task(task, env=None, project=None) -> TaskClassEstimate:
    # Cheap LLM call, cached per fingerprint
    # Considers: task statement, examples, env, project, persona's history
    ...
```

### Appendix A.4 — Demotion paths (§2.2)

```text
CONVERGENT → MIXED      verifier exists but partial
CONVERGENT → DIVERGENT  no usable verifier; judge instead
MIXED      → DIVERGENT  gate phase failed
INVESTIGATIVE → DIVERGENT (Mode A, ephemeral, when project absent)
                          or OPEN_ENDED (Lab env, ephemeral)
```

### Appendix A.5 — INVESTIGATIVE sub-modes table (§2.3)

```text
SUB-MODE         DOMINANT MODES        DISCIPLINE RULE                          ACCEPTANCE SIGNAL
─────────────    ──────────────────    ────────────────────────────────────     ─────────────────────────
exploration      perceiver, historian, broad search; no novelty claim until     ProvenFact added OR
                 abducer               novelty-check has run; ProvenFacts        Conjecture proposed
                                       are constraints, not eliminations.
                                       Chosen when: project has open problems
                                       with no candidate direction.

verification     experimenter,         every candidate must pass the domain's   Conjecture advanced
                 falsifier, composer   required external tool (lean_verify,     OR refuted via
                                       drc_check, etc.) before claim;           verifier outcome
                                       external-tool-required policy active.
                                       Chosen when: a candidate exists and
                                       needs to be proven, falsified, or
                                       measured.

synthesis        integrator,           commits to current best state;           ArtifactBundle drafted;
                 composer,             produces ArtifactBundle draft;          milestone progress
                 reflector             session-boundary reflection signed.       (delta ≥ threshold)
                                       Chosen when: enough verified pieces
                                       exist to integrate into a bundle.

expert_review    historian, falsifier, panel/peer-review discipline;            peer_review signed by
                 reflector + external  multi-round critique; persona may        external reviewer;
                 reviewer (federated)  not self-accept; reviewer signature      AcceptanceResult with
                                       required before bundle promotes from     pathway=peer_review
                                       review → verified.
                                       Chosen when: bundle has reached
                                       review state and external attestation
                                       is required.
```

### Appendix A.6 — INVESTIGATIVE sub-task taxonomy (§2.4)

```text
INVESTIGATIVE task: "find counter-example to conjecture C OR prove it"
   │
   ├─ sub-task: search prior literature              → INTERACTIVE
   │            (historian + arxiv_search tool;
   │             novelty-check populates lineage)
   │
   ├─ sub-task: construct candidate counter-example  → CONVERGENT
   │            (composer + executable verifier)
   │
   ├─ sub-task: verify counter-example in Lean       → CONVERGENT
   │            (experimenter + lean_verify;
   │             external-tool-required claim gate)
   │
   ├─ sub-task: if no counter-example → attempt proof → CONVERGENT
   │            (composer + lean_verify;
   │             ProofAttempt recorded with gaps)
   │
   └─ sub-task: write up findings                    → DIVERGENT
                (composer + PANEL_ACCEPT on
                 sectioned-rubric)
```

### Appendix A.7 — INVESTIGATIVE per-mode budget (§2.5)

```text
SUB-MODE          SHARE OF SESSION BUDGET    DEGRADATION ON OVERRUN
──────────────    ──────────────────────     ─────────────────────────────
exploration       ≤ 35%                       force transition to verification
                  (max 18 LLM calls of 50)    (cannot perpetually explore)

verification      ≤ 40%                       refuse new claims until session
                  (max 20 LLM calls of 50)    boundary; allow ProofAttempt
                                              records with gap-lemmas only

synthesis         ≤ 15%                       defer ArtifactBundle commit to
                  (max 8 LLM calls of 50)     next session; emit
                                              `synthesis_deferred` event

expert_review     ≤ 10%                       external reviewer latency is
                  (max 4 LLM calls of 50;     out-of-loop; budget here counts
                   reviewer latency           preparation only; session
                   excluded)                  may end with `review_pending`

SESSION TOTAL     ≤ 50 LLM calls              hard cap;
                  (Lab budget: 80 if          envelope status →
                   multi-mode loops)          budget_exhausted on overrun

PROJECT TOTAL     unbounded; tracked;         alerts at operator thresholds;
                  cumulative cost amortised   PROJECT_STALLED event if
                  across sessions             EMA progress < 0.1 for ≥ 4
                                              sessions
```

### Appendix A.8 — Budget profile resolution (§2.5)

```text
1. EnvironmentBlueprint.budget_override  (per PHASE_3 P3-FR-007)
                                          — wins if set, full stop.

2. DomainContext.session_budget_profile  (06_DOMAIN §2)
                                          — falls back if env silent.
                                          Profiles map to defaults:
                                            reasoning_heavy → 50 calls / $0.50 (default; current v1.0)
                                            document_heavy  → 200 calls / $2.50
                                            tool_heavy      → 100 calls / $1.50
                                            balanced        → 80 calls / $1.00
                                          Sub-mode shares (35/40/15/10) scale
                                          proportionally to the resolved cap.

3. v1.0 default                            — 50 / $0.50 (above) if both silent.
```

### Appendix A.9 — DELEGATED inheritance semantics (§2.6)

```text
INHERITANCE SEMANTICS
  Parent DELEGATED task carries:
    delegator_persona_id   the persona that delegated
    delegate_persona_id    the persona performing the work
    sub_task_class         the resolved class of the delegated work
    sub_task_pathway       inherited acceptance pathway
    delegation_signature   delegator's signed handoff
  
  The delegate runs the sub-task as if it were its own,
  classified per its own task. The delegate's AnswerPackage
  satisfies the sub-task; the delegator wraps it in a parent
  AnswerPackage with status inherited from sub-task status.

AUDIT LINEAGE REQUIREMENT
  Every DELEGATED task emits:
    DELEGATION_PROPOSE     delegator's intent (target persona, intent kind)
    DELEGATION_ACCEPT      delegate's acceptance (or DELEGATION_REFUSE)
    SUB_TASK_LINEAGE_LINK  pointer from parent envelope to sub-task lineage
  
  All three signed by both parties (delegator and delegate kernels;
  for cross-kernel A2A, both kernel signatures required).
  The parent envelope's lineage references the sub-task's full lineage;
  reconstruction must yield the same AnswerPackage on replay.

SUB-TASK PATHWAY RESOLUTION
  Step 1: delegate classifies the sub-task using its own classifier.
  Step 2: kernel picks the appropriate pathway per §2.
  Step 3: sub-task runs; emits its own AnswerPackage.
  Step 4: parent DELEGATED task's AnswerPackage:
            acceptance_pathway = sub_task.acceptance_pathway
            status              = sub_task.status
            contributors        = parent + sub_task.contributors

OVERALL ACCEPTANCE
  The delegator remains responsible for the *overall* outcome.
  If the sub-task accepts under one pathway but the delegator's
  parent task required a different pathway (e.g., parent was
  classified MIXED but delegate produced only convergent
  acceptance), the delegator must invoke an additional sub-task
  to satisfy the residual.
```

### Appendix A.10 — Cognitive functions by task class (§2.7)

```text
TASK CLASS       GENERATION      CRITIQUE        EVIDENCE        DECISION        SYNTHESIS / RELATIONAL
─────────────    ───────────     ───────────     ───────────     ───────────     ──────────────────────
CONVERGENT       abducer         falsifier       experimenter    integrator      —
                 perceiver

DIVERGENT        composer        falsifier       experimenter    curator         reflector
                 perceiver       (as critic)     (as reviewer)

MIXED            abducer +       falsifier       experimenter    integrator +    reflector
                 composer        (gate + critic) (gate + panel)  curator (resid)

INTERACTIVE      abducer         falsifier       perceiver       integrator      reflector
                 composer        (light)         historian

RELATIONAL       —               —               perceiver       —               listener (dominant)
                 (no artefacts)                                                  comforter

PEDAGOGIC        composer        falsifier       perceiver       integrator      teacher (dominant)
                 (explanations)  (gentle)        historian                       reflector

PERFORMATIVE     composer        —               perceiver       —               storyteller (dominant)

EXISTENTIAL      —               —               perceiver       —               comforter (dominant)
                 (no artefacts)                                                  listener

DELEGATED        — (inherited from sub-task class) —

INVESTIGATIVE    abducer         falsifier       experimenter    integrator      reflector + historian
                 composer                        + external      (project-       (cross-session
                 perceiver                       tools           level)          continuity)
```

### Appendix A.11 — Eight acceptance pathways table (§3)

```text
PATHWAY                       SEMANTICS
─────────────────────────     ─────────────────────────────────────
VERIFIER_ACCEPT               Programmatic verifier cascade returns
                              pass_rate=1.0 on all targets.

PANEL_ACCEPT                  Multi-judge rubric panel ≥ threshold
                              on all dimensions; anti-Goodhart stack
                              applied.

USER_ACCEPT                   User explicitly approves (button click,
                              "yes that's good", etc.).

MUTUAL_ACCEPT                 Two or more parties (typically
                              persona + user) both accept.

ENGAGEMENT_ACCEPT             Interaction continues; ongoing engagement
                              is acceptance signal (PERFORMATIVE class).

GOAL_PROGRESS_ACCEPT          A declared goal advances measurably;
                              per-turn + outcome assessment
                              (INTERACTIVE, PEDAGOGIC).

OPEN_ENDED                    No discrete acceptance event; trajectory
                              quality matters (RELATIONAL with
                              USER_ACCEPT checkpoints, EXISTENTIAL).

PROJECT_PROGRESS_ACCEPT       Project state delta (milestone reached,
                              conjecture advanced, obligation
                              discharged, etc.); requires Project
                              context (INVESTIGATIVE).
```

### Appendix A.12 — VERIFIER_ACCEPT pathway (§3.1)

```text
Persona produces candidate → kernel runs VerifierCascade:
  Stage 1 (fast):      ≤ 1s typical; deterministic checks
  Stage 2 (medium):    ≤ 10s; shallow LLM judge or exhaustive small executable
  Stage 3 (expensive): ≤ 60s; deep judge or exhaustive large executable
  
Each stage must pass for acceptance. Failure at any stage = candidate
rejected; extracted constraint added to ProvenFacts.

Verifier rotation (INV-6) per rotation_period tasks.
```

### Appendix A.13 — PANEL_ACCEPT pathway (§3.1)

```text
Persona produces candidate → kernel runs JudgePanel:
  Minimum 3 judges from ≥ 2 model families (PoLL pattern).
  CyclicJudge rotation per panel.
  Position-swap (pairwise prompts in both orders).
  Length-controlled judge prompts (AlpacaEval-LC).
  Versioned rubric with dimensions.
  Dissent preserved per dimension.
  Style-strip for high-stakes.
  Cost-aware escalation (D3-style debate if dispersion > threshold).
  Spot-check holdout (~5% sampled vs human).
  Goodhart canary (score-distribution monitor).
  Alternative-rubric robustness.
  
Aggregation: max_vote / trimmed_mean / debate_then_vote.

If PANEL_DISSENT (split decision), Curator resolves:
  - RESAMPLE (request more variants on disputed dimensions)
  - OVERTON_BALLOT (return incomparable top-K)
  - ESCALATE_HUMAN (defer to operator)
```

### Appendix A.14 — USER_ACCEPT pathway (§3.1)

```text
Persona produces output. User explicitly accepts.
Acceptance signal types:
  - explicit button / command
  - verbal "yes that's right"
  - implicit: user proceeds with the output as final
Default ambiguity: timeout (configurable per task) → status="user_no_response".
```

### Appendix A.15 — MUTUAL_ACCEPT pathway (§3.1)

```text
Persona + user(s) BOTH accept.
For collaborative work where two parties must sign off.
e.g., "I propose X" → user "I accept" → BOTH co-sign final.
```

### Appendix A.16 — ENGAGEMENT_ACCEPT pathway (§3.1)

```text
Quality measured by continued engagement signal:
  - user re-prompts within window: acceptance signal
  - user stops engaging within window: signal lost
  
NOT measured by attention-economy metrics (time-on-app, etc.).
Engagement signal is a continuation indicator only.

Operator may set engagement_window (default 24h).
```

### Appendix A.17 — GOAL_PROGRESS_ACCEPT pathway (§3.1)

```text
Declared goal at task start:
  goal_id: "user_understands_recursion"
  progress_metric: "user can solve novel recursive problem without help"
  horizon: "next 2 sessions"

Per-turn judge: did this turn advance goal? (stalled / regressed /
                                              advancing / achieved)
Outcome judge: did the overall horizon achieve the goal?

Acceptance = horizon ended AND goal achieved at sufficient confidence.
Failure mode: stalled or regressed → goal renegotiated or task aborted.

LEARNER-ACKNOWLEDGEMENT STEP (PEDAGOGIC mastery):
  When the goal corresponds to a learner mastering a skill (PEDAGOGIC
  task class with a target MasteryCheckpoint per §3.3), acceptance ALSO
  requires the learner's signed acknowledgement that they perceive their
  own mastery.  This is the substrate-shape mitigation against persona-
  side judging-the-learner-mastered-it without learner concurrence.
  Persona drafts:
    achievement_summary:    "you can now ___ without scaffolding"
    evidence_refs:          [episodic memory ids of successful
                             demonstrations]
    mastery_checkpoint_ref: (if applicable, §3.3 MasteryCheckpoint id)
  Learner responds:
    acknowledged:           "yes, I feel I can do this now"
    declined:               "I don't yet feel confident — let's keep
                             working"
    deferred:               "I want to think about it / try once more"
  On acknowledged: acceptance fires; MasteryCheckpoint advances.
  On declined: acceptance stalls; persona returns to teaching mode;
    learner's declined signal accumulates in LearnerStateRecord
    (02_PERSONA §11.8) as a confidence-gap signal.
  On deferred: acceptance pauses for up to 7 days; auto-fires
    acknowledged if learner takes no action AND persona observes
    continued successful demonstration.
  PEDAGOGIC tasks with no target MasteryCheckpoint (e.g., general
  conversational learning without a structured mastery goal) skip
  this step; acceptance is per the persona-judge path.
```

### Appendix A.18 — OPEN_ENDED pathway (§3.1)

```text
No discrete acceptance event.
Trajectory quality matters; assessed retrospectively.

USER_ACCEPT checkpoints occasionally surfaced:
  "Is this helpful?" "Want me to keep going?"
  
Quality signals (post-hoc):
  - user did not invoke USER_STOP
  - user continued engaging (light signal)
  - persona maintained mode discipline (e.g., listener mode for distress)
  - persona's reflection does not flag the interaction as problematic

Operator audit may flag patterns suggesting poor trajectory.
```

### Appendix A.19 — PROJECT_PROGRESS_ACCEPT pathway (§3.1)

```text
Task accepted when project state advances:
  - milestone reached
  - open problem resolved or morphed
  - conjecture advanced or refuted
  - obligation discharged
  - verified artifact bundle produced
  - structured outcome (peer review, bench measurement, etc.) shifts
    project assessment
  - ambient signal (cross-env event link) materially changes project state

Aggregate progress score (over rolling window):
  > 0.6 sustained → "thriving"
  > 0.2 → "active"
  |x| < 0.1 sustained → "stalled" (operator notified)
  < -0.1 → "regressing" (operator + lead notified)

Session may end without acceptance event ("progress=none");
session is logged, not rejected.

PROJECT_PROGRESS_ACCEPT evaluator considers AMBIENT signals
not just task lineage: a peer in the env posting a structural insight
relevant to a project conjecture may trigger advancement even without
explicit task.

PHASE-AWARE STALL SUPPRESSION:
The "stalled" verdict above is suppressed when the project's current
ProjectPhaseState (04_PROJECT §26a.7) has stall_evaluator_suppressed
= True — typical for phase_kind in {external_dependency_wait,
physical_fabrication, regulatory_review, peer_review_pending}
(kinds resolve against KindRegistry; substrate names no phase
categories).  Suppression lifts automatically when any blocking
ExternalCommitment goes overdue (the phase flips to
overdue_external) or the phase is signed out by user/operator.
The stall verdict resumes normally on suppression lift.
```

### Appendix A.20 — RelationshipReviewCheckpoint dataclass (§3.2)

```python
@dataclass
class RelationshipReviewCheckpoint:
    schema: str = "relationship-review-checkpoint/1"
    checkpoint_id: str
    env_id: str                                  # the env hosting the
                                                 # OPEN_ENDED interaction
                                                 # (typically a SOLO env
                                                 # with a relational
                                                 # blueprint such as
                                                 # companion_space)
    user_id: str                                 # the user the relationship
                                                 # is with
    persona_id: str                              # the persona on the other
                                                 # side

    # SCHEDULE — auto-triggered per cadence; substrate is the trigger.
    # Defaults: every 90 days OR every 50 sessions, whichever first.
    # Operator-tunable per env; cannot be disabled outright (the
    # checkpoint is a substrate-shape user-protection mechanism;
    # disabling it would require operator-signed deployment-policy
    # exemption with explicit rationale, which the substrate refuses
    # to make easy).
    triggered_at: datetime
    trigger_kind: Literal[
        "session_count_milestone",               # 50-session milestone
                                                 # (or operator-tuned N)
        "duration_milestone",                    # 90-day milestone
                                                 # (or operator-tuned)
        "first_checkpoint",                      # first one after env
                                                 # crosses minimum
                                                 # interaction threshold
                                                 # (default 10 sessions)
        "user_requested"]                        # user files an
                                                 # adhoc checkpoint
                                                 # outside cadence

    session_count_at_trigger: int
    duration_active_at_trigger: timedelta

    # PERSONA-DRAFTED REVIEW SUMMARY — substrate-shape categories;
    # persona fills with their honest reflection.  This is NOT a
    # performance metric; it is a relationship-self-awareness
    # surface.  Persona's response is signed and visible to user
    # AND operator (audit minimum).
    review_summary: dict                         # categories per
                                                 # template, e.g.:
                                                 # {
                                                 #   "observed_patterns":
                                                 #     "...",
                                                 #   "topics_dominating":
                                                 #     "...",
                                                 #   "user_apparent_
                                                 #    wellbeing_trend":
                                                 #     "...",
                                                 #   "recurring_concerns":
                                                 #     "...",
                                                 #   "honest_caveats":
                                                 #     "..."
                                                 # }
    persona_drafted_at: datetime
    persona_signed_at: datetime
    persona_signed_by: bytes

    # USER RESPONSE — user acknowledges, declines, or requests changes.
    user_response_kind: Literal[
        "acknowledged_continue",                 # default — user
                                                 # acknowledges; no
                                                 # changes
        "request_changes",                       # user wants to adjust
                                                 # interaction pattern;
                                                 # surfaces follow-up
                                                 # primitives
                                                 # (UserBoundary,
                                                 # UserMemorySelection,
                                                 # etc.) inline
        "request_release",                       # user uses the
                                                 # checkpoint as the
                                                 # trigger for
                                                 # UserRelationshipRelease
                                                 # (§11.4a)
        "declined_to_respond"]                   # user does not engage;
                                                 # checkpoint logged
                                                 # without response;
                                                 # next checkpoint
                                                 # fires per cadence
    user_response_at: datetime | None
    user_signed_at: datetime | None
    user_signed_by: bytes | None

    state: Literal["drafted",                    # persona has drafted
                    "delivered",                  # surfaced to user
                    "responded",                  # user acknowledged
                    "expired"]                    # cadence elapsed; if
                                                 # next checkpoint fires
                                                 # with prior unresponded,
                                                 # operator notified

    signed_by: bytes                             # kernel signature on
                                                 # checkpoint mint
```

### Appendix A.21 — RelationshipReviewCheckpoint admission rule (§3.2)

```text
On cadence trigger (session_count or duration milestone):
  1. Kernel mints RelationshipReviewCheckpoint with state "drafted".
  2. Persona is prompted to fill review_summary (no time deadline; persona
     drafts in next interaction with the user).
  3. On persona_signed_at, state → "delivered"; surfaces in env to user.
  4. On user response, state → "responded".
  5. If next cadence trigger fires with prior checkpoint still
     "delivered" (no user response in 30d), kernel emits
     CHECKPOINT_UNANSWERED to operator audit surface AND escalates
     subsequent checkpoint with higher visibility (e.g., prominent UI
     surface).  Pattern of unanswered checkpoints suggests user
     disengagement that operator MAY want to investigate.

Cadence configuration:
  Default: every 90 days OR every 50 sessions (whichever first).
  Operator-tunable per env or per blueprint type:
    - Lower bound: 14 days OR 10 sessions (substrate refuses cadences
      that would flood the user with checkpoints).
    - Upper bound: 365 days OR 200 sessions (substrate refuses cadences
      that effectively disable the checkpoint).
  Disabling outright requires operator-signed deployment-policy
  exemption with rationale (e.g., "this is a one-shot env where
  checkpoints make no sense"); substrate refuses silent disable.
```

### Appendix A.22 — Curriculum + LessonPlan + MasteryCheckpoint dataclasses (§3.3)

```python
@dataclass
class Curriculum:
    schema: str = "curriculum/1"
    curriculum_id: str

    # AUTHORSHIP — substrate-shape; substrate carries by reference,
    # does not author content.
    authored_by_kind: Literal[
        "operator_authored",                      # institution-defined
                                                  # (medical school
                                                  # curriculum)
        "persona_authored",                       # persona drafts based on
                                                  # learner-state inference
        "co_authored"]                            # operator template +
                                                  # persona adaptation;
                                                  # both signatures required
    authored_by_operator_id: str | None
    authored_by_persona_id: str | None

    # TARGET — what the curriculum aims at
    target_skill_kinds: list[str]                 # KindRegistry-resolved
                                                  # skills the learner is
                                                  # working toward
    target_mastery_checkpoint_refs: list[str]     # MasteryCheckpoint ids
                                                  # the curriculum aims to
                                                  # reach
    target_competency_level: Literal[
        "novice", "proficient", "competent_supervised", "independent"]

    # STRUCTURE — ordered lesson plans
    lesson_plan_refs: list[str]                   # LessonPlan ids
    prerequisite_graph: dict[str, list[str]]      # lesson_plan_id ->
                                                  # list of prerequisite
                                                  # lesson_plan_ids; DAG
                                                  # only (substrate refuses
                                                  # cycles)

    # ENVELOPE — operator-tunable bounds
    expected_session_count: int | None            # rough estimate; not
                                                  # enforced
    expected_duration: timedelta | None
    hazard_envelope_max: dict                     # max physical_harm_class
                                                  # + max information_hazard_
                                                  # class across all lessons;
                                                  # MUST be ≤ corresponding
                                                  # TeachingAuthorisation
                                                  # ceiling (`02_PERSONA §11.10`)

    # LEARNER COMMITMENT — does the learner explicitly opt into the
    # curriculum, or is it suggested?
    requires_learner_optin: bool                  # default True for
                                                  # safety-critical
                                                  # curricula (any lesson
                                                  # crosses bodily_injury);
                                                  # False permits persona
                                                  # to suggest-and-iterate
                                                  # for lower-stakes learning
    learner_optin_signed_at: datetime | None
    learner_optin_signed_by: bytes | None

    created_at: datetime
    signed_by: bytes


@dataclass
class LessonPlan:
    schema: str = "lesson-plan/1"
    lesson_plan_id: str

    # TARGET
    target_skill_kind: str                        # primary skill the lesson
                                                  # advances
    target_mastery_checkpoint_ref: str | None     # if this lesson directly
                                                  # advances a checkpoint

    # CONTENT — substrate carries refs; doesn't author content
    content_refs: list[str]                       # knowledge_ref ids,
                                                  # artifact ids, etc.
    expected_modes_engaged: list[str]             # KindRegistry-resolved
                                                  # cognitive_mode_kinds
                                                  # (teacher, perceiver,
                                                  # falsifier, etc.)
    expected_duration: timedelta
    expected_mastery_delta: str                   # ≤ 300 chars; what
                                                  # competency this lesson
                                                  # is expected to advance

    # GATES
    hazard_envelope: dict                         # physical_harm_class +
                                                  # information_hazard_class
                                                  # for this lesson;
                                                  # composed with curriculum
                                                  # hazard_envelope_max
    prerequisite_mastery_checkpoints: list[str]   # learner must have
                                                  # cleared these before
                                                  # this lesson admits

    # ASSESSMENT
    success_criteria_text: str
    verifier_kind: str | None                     # KindRegistry-resolved
                                                  # programmatic verifier
                                                  # for lesson outcome
                                                  # (e.g., "answers_3_of_5_
                                                  #  recall_questions_correctly")
                                                  # null = persona-judged only

    authored_at: datetime
    signed_by: bytes


@dataclass
class MasteryCheckpoint:
    schema: str = "mastery-checkpoint/1"
    checkpoint_id: str

    # BINDING
    skill_kind: str                               # what skill this checkpoint
                                                  # gates
    target_competency_level: Literal[
        "introduced",
        "demonstrated_assisted",
        "demonstrated_independent",
        "proficient",
        "competent_supervised",
        "independent"]

    prerequisite_checkpoint_refs: list[str]       # DAG; substrate refuses
                                                  # cycles

    # EVIDENCE REQUIREMENTS — which combination of evidence is required
    # to fire the checkpoint
    evidence_requirement: Literal[
        "persona_judged",                         # persona's judgement alone
                                                  # (admissible up to
                                                  # `demonstrated_independent`
                                                  # only; `proficient` and
                                                  # above require more
        "programmatic_verifier",                  # verifier_kind clears
                                                  # (e.g., "passes_OSCE_
                                                  #  simulation_X")
        "external_attestation",                   # LearnerCompetencyAttestation
                                                  # (`02_PERSONA §11.9`)
        "persona_plus_verifier",                  # both
        "verifier_plus_attestation",              # both
        "all_three"]                              # all three

    # COMPOSITION WITH SAFETY FLOOR — checkpoints in safety-critical skills
    # MUST require at minimum `external_attestation` for advancement to
    # `competent_supervised` or `independent` levels.  Substrate refuses
    # weaker evidence requirements for these levels.
    safety_critical: bool                         # mirrors source skill_kind's
                                                  # hazard axes

    authored_at: datetime
    signed_by: bytes
```

### Appendix A.23 — Curriculum admission rule (§3.3)

```text
On Curriculum.create:
  1. Verify all lesson_plan_refs and target_mastery_checkpoint_refs
     exist; refuse `dangling_reference` otherwise.
  2. Verify prerequisite_graph is a DAG; refuse `prerequisite_graph_cycle`.
  3. Verify hazard_envelope_max <= TeachingAuthorisation ceiling for the
     authoring persona (when persona_authored or co_authored); refuse
     `hazard_envelope_exceeds_teaching_authorisation`.
  4. If requires_learner_optin = True and learner_optin signature absent:
     curriculum is "drafted" but not "active"; no lessons admit until
     opt-in signed.
  5. Emit CURRICULUM_CREATED.

On LessonPlan execution attempt (persona drafts to deliver this lesson):
  1. Verify all prerequisite_mastery_checkpoints have been cleared for
     this learner; refuse `prerequisite_checkpoint_unmet`.
  2. Verify lesson hazard_envelope <= Curriculum hazard_envelope_max
     <= TeachingAuthorisation ceiling.
  3. Emit LESSON_PLAN_EXECUTION_STARTED.
  4. Lesson proceeds as a PEDAGOGIC task per §3.1 routing.
  5. On lesson conclusion, evaluate success_criteria_text + verifier_kind;
     emit LESSON_PLAN_EXECUTION_COMPLETED with outcome.

On MasteryCheckpoint.fire (per evidence_requirement):
  1. Verify all prerequisite_checkpoint_refs have fired for this learner.
  2. Verify evidence requirements satisfied per Literal.
  3. If safety_critical = True and target level in
     {competent_supervised, independent}: REQUIRE external_attestation
     in evidence (the persona-judged path is refused for safety-critical
     advancement to supervised/independent levels).
  4. Update LearnerStateRecord.mastery_checkpoints_reached
     (`02_PERSONA §11.8`).
  5. Emit MASTERY_CHECKPOINT_REACHED.
```

### Appendix A.24 — Three routing modes (§4)

```text
MODE A — task in persistent env, no project
   User addresses an env; persistent member personas receive notification;
   each persona decides respond/defer/ignore; responding persona mints
   envelope with project_id=None.

MODE B — task in a project_workspace-typed env
   Project-as-env-type means a "project task" is just a task addressed
   to an env whose type is project_workspace.  The dispatcher treats
   this as Mode A on a project_workspace env; the env-member set IS
   the project-member set (no separate intersection).  The persona's
   envelope reads project-specific context (active milestone, open
   problems, obligations) directly from the env's project_workspace
   attributes.  Prior versions referenced "Mode B" as a distinct mode; v1.0
   keeps the label for backward continuity but operationally it is
   Mode A with a project-typed env.  See 04_PROJECT §0 for the
   ontological unification.

MODE C — ephemeral encounter
   No persistent env, no project. Kernel creates ad-hoc Solo env for the
   single session; selects default persona; runs task; archives env.
   Single-shot behaviour preserved.
```

### Appendix A.25 — ClarifyTurn dataclasses (§4.0)

```python
@dataclass
class ClarifyTurn:
    schema: str = "clarify-turn/1"
    clarify_id: str
    task_fingerprint: str
    requester_id: str

    triggered_by: list[str]                # substrate-shape trigger reasons
                                           # (NOT domain categories):
                                           #   "classifier_confidence_low"
                                           #   "intent_verb_ambiguous"
                                           #   "object_kind_unresolved"
                                           #   "scope_unbounded_keywords"
                                           #   "safety_critical_domain_inferred"
                                           #   "horizon_undeclared"

    candidate_interpretations: list[CandidateInterpretation]  # 2-4 distinct
    persona_recommended_idx: int | None    # persona may rank; user decides

    user_response_required: bool = True
    response_timeout: timedelta = timedelta(hours=24)
    timeout_default_idx: int | None        # configurable per env;
                                           # default None = no auto-route on timeout

    drafted_by_persona_id: str
    drafted_at: datetime
    user_chose_idx: int | None
    user_chose_at: datetime | None
    signed_by: bytes


@dataclass
class CandidateInterpretation:
    schema: str = "candidate-interpretation/1"
    label: str                              # short user-facing label
    task_class_hint: str                    # one of the 10 classes
    routing_mode_hint: Literal["A", "B", "C"]
    requires_new_project: bool
    requires_new_env: bool

    estimated_horizon: timedelta
    estimated_cost_range_usd: tuple[float, float]

    key_dependencies: list[str]             # free-text dependencies the
                                            # persona surfaces (e.g. "needs
                                            # fab access", "needs my consent
                                            # to ingest paywalled corpus");
                                            # NOT a closed list

    safety_floor_notes: list[str]           # what the safety floor would
                                            # require under this path
```

### Appendix A.26 — needs_clarify decision spec (§4.0)

```python
@dataclass
class ClarifyCheck:
    required: bool
    fired_reasons: list[str]   # subset of the triggered_by Literal

def needs_clarify(task, requester, env=None, project=None) -> ClarifyCheck:
    fired = []
    estimate = classify_task(task, env=env, project=project)

    # Reason 1 — low classifier confidence
    if estimate.confidence < clarify_aggressiveness_threshold(env):
        # default threshold: 0.5 at medium aggressiveness
        fired.append("classifier_confidence_low")

    # Reason 2 — ambiguous verb without resolved object kind
    if has_ambiguous_intent_verb(task.statement) \
            and not has_resolved_object_kind(task, KindRegistry):
        # "create / make / build / develop / produce" without an object_kind
        # that resolves in KindRegistry → user intent is genuinely unclear
        fired.append("intent_verb_ambiguous")

    # Reason 3 — unbounded scope keywords
    if has_unbounded_scope_keywords(task.statement):
        # "everything", "all of it", "the whole thing", "completely"
        fired.append("scope_unbounded_keywords")

    # Reason 4 — object kind not in KindRegistry (would trigger domain probe)
    if task.object_kind_hint and \
            not KindRegistry.resolves(task.object_kind_hint, env.domain_id):
        fired.append("object_kind_unresolved")

    # Reason 5 — safety-critical domain inferred from probe pre-check
    if would_trigger_domain_unknown(task) and \
            preliminary_hazard_inference(task) in ("bodily_injury",
                                                     "fatality_risk",
                                                     "dual_use_civilian",
                                                     "export_controlled",
                                                     "national_security"):
        fired.append("safety_critical_domain_inferred")

    # Reason 6 — horizon undeclared on long-arc-shaped task
    if has_long_arc_shape(task.statement) and not has_declared_horizon(task):
        fired.append("horizon_undeclared")

    # Cached choice suppression
    if fired and lookup_fresh_user_choice(task.fingerprint, requester):
        return ClarifyCheck(required=False, fired_reasons=fired)

    return ClarifyCheck(required=bool(fired), fired_reasons=fired)
```

### Appendix A.27 — route_task_v1 dispatcher (§4.1)

```python
def route_task_v1(task, requester):
    # Step 0: clarify before classifying
    clarify_check = needs_clarify(task, requester)
    if clarify_check.required:
        fresh = lookup_fresh_user_choice(task.fingerprint, requester)
        if fresh is None:
            clarify = draft_clarify_turn(task, requester, clarify_check)
            return AwaitClarification(clarify)
        task = apply_user_choice(task, fresh)

    # Step 1: identify entry point (v1.0 unification: project IS env type)
    if task.target_environment_id:
        env = resolve_environment(task.target_environment_id)
        if not env or env.status == "archived":
            return route_ephemeral(task, requester)
        
        # v1.0: Mode B is operationally Mode A on a project_workspace env.
        # The legacy target_project_id is honoured by checking that the
        # resolved env is the project's owning env (same identifier under
        # the unification per 04_PROJECT §0).
        if task.target_project_id and \
                task.target_project_id != env.environment_id and \
                env.type != "project_workspace":
            return reject("env is not the project's owning workspace env "
                          "(v1.0 Project=Environment unification)")
        if env.type == "project_workspace":
            # Mode B: project-typed env
            return route_to_project_workspace_env(task, env, requester)
        else:
            # Mode A: ordinary env
            return route_in_env_no_project(task, env, requester)
    
    elif task.target_persona_id:
        # User addresses a named persona; find suitable env
        persona = resolve_persona(task.target_persona_id)
        env = pick_env_for_persona_and_task(persona, task, requester)
        if env:
            # Wake Path 6 (05_ENVIRONMENT §5.2): if persona is
            # dormant in resolved env, auto-wake before routing.
            wake_if_dormant_on_user_address(persona, env, requester)
            return route_in_env_no_project(task, env, requester)
        else:
            return route_ephemeral(task, requester)
    
    else:
        # No env, no project, no persona — pure ephemeral
        return route_ephemeral(task, requester)
```

### Appendix A.28 — Env selection when persona named (§4.2)

```text
1. ACTIVE CONTEXT
   Open conversation thread in one of persona's envs → continue there.

2. CHARTER + DOMAIN MATCH
   Task topic matches one of persona's envs (technical → engineering lab;
   personal → companion env) → prefer that env.

3. PRIVACY HINT
   Task content suggests personal/relational → prefer companion-tier
   over work-tier envs.

4. RECENCY
   Pick env where persona + user most recently interacted.

5. FALLBACK
   Ephemeral env (Mode C).
```

### Appendix A.29 — Notification routing within env (§4.3)

```text
EVENT arrives at env's ambient stream (e.g., user message).
    ▼
KERNEL examines present members.
For each member:
   - check observation surface match (event kind, surface filter)
   - check role match (does this event concern this role?)
   - check presence state (availability, attention, energy)
   - check urgency (event kind classification)
   - check attention budget (not over budget)
    ▼
ELIGIBLE members notified.
    ▼
Each notified persona's kernel evaluates RESPONSE DECISION:
   - respond
   - defer (queued for later; re-notification)
   - ignore (with logged reason if charter-relevant)
   - acknowledge_only (social signal without action)
    ▼
RESPONDING personas: each mints envelope; performs action.
ACTION result enters ambient stream; observable per surfaces.
```

### Appendix A.30 — EphemeralPromotionOffer dataclass (§4.4)

```python
@dataclass
class EphemeralPromotionOffer:
    schema: str = "ephemeral-promotion-offer/1"
    offer_id: str
    ephemeral_session_id: str
    requester_id: str

    triggered_by: list[str]                # substrate-shape triggers
                                           # (NOT domain categories):
                                           #   "turn_count_above_threshold"
                                           #   "domain_unknown_detected_fired"
                                           #   "multi_artifact_drafted"
                                           #   "user_expressed_long_horizon"
                                           #   "external_commitment_drafted"
                                           #   "physical_asset_referenced"

    # Proposed project shape — all kinds KindRegistry-resolved.
    # Substrate names no specific project kinds, env blueprints, or domains.
    proposed_project_kind: str             # KindRegistry.project_kinds
    proposed_env_blueprint_id: str | None  # existing blueprint to instantiate
    proposed_milestones_draft: list[str]   # persona's first-pass milestones;
                                           # user edits before accepting
    proposed_persona_team: list[str]       # candidate cohort members

    estimated_horizon: timedelta
    estimated_cost_range_usd: tuple[float, float]

    user_response_required: bool = True
    expires_at: datetime                   # default 7 days; user may
                                           # accept later by referencing
                                           # the signed offer

    user_accepted: bool | None
    user_accepted_at: datetime | None
    materialised_project_id: str | None    # set on acceptance
    materialised_environment_id: str | None

    drafted_by_persona_id: str
    signed_by: bytes
```

### Appendix A.31 — Ephemeral promotion trigger evaluation (§4.4)

```python
def evaluate_promotion_triggers(session) -> list[Trigger]:
    triggers = []
    if session.turn_count >= 5:
        triggers.append(Trigger("turn_count_above_threshold",
                                 safety_critical=False))
    if any(e.kind == "DOMAIN_UNKNOWN_DETECTED" for e in session.lineage):
        # safety-critical IFF the inferred hazard axes are above threshold
        hazard = preliminary_hazard_inference(session)
        is_sc = hazard.physical_harm_class >= "bodily_injury" \
                 or hazard.information_hazard_class >= "dual_use_civilian"
        triggers.append(Trigger("domain_unknown_detected_fired",
                                 safety_critical=is_sc))
    if session.draft_artifact_count >= 2:
        triggers.append(Trigger("multi_artifact_drafted",
                                 safety_critical=False))
    if horizon_keywords_detected(session.user_messages):
        triggers.append(Trigger("user_expressed_long_horizon",
                                 safety_critical=False))
    if any(isinstance(e, ExternalCommitment) for e in session.draft_state):
        # safety-critical IFF the commitment is a financial / physical-state
        # advancement commitment
        ec = first_commitment(session.draft_state)
        is_sc = ec.expected_artifact_kind in safety_critical_outcome_kinds(
            session.env, session.domain_id)
        triggers.append(Trigger("external_commitment_drafted",
                                 safety_critical=is_sc))
    if any(isinstance(e, PhysicalAsset) for e in session.draft_state):
        # safety-critical ALWAYS — physical asset references mean the
        # ephemeral session is sliding toward physical-world coupling
        triggers.append(Trigger("physical_asset_referenced",
                                 safety_critical=True))
    return triggers


@dataclass
class Trigger:
    name: str
    safety_critical: bool   # per-trigger evaluation per substrate rules above
```

### Appendix A.32 — Ephemeral promotion acceptance flow (§4.4)

```text
1. User accepts → kernel materialises:
     - Project (kind = proposed_project_kind; charter from session)
     - EnvironmentInstance (blueprint = proposed_env_blueprint_id, or
       a Solo/Lab default if None)
     - First ProjectLineage entry references the ephemeral session's
       lineage (preserved as session 1 evidence; not deleted)
2. The original conversation thread re-anchors to the new project +
   env; persona membership signed; user becomes ProjectMember(owner).
3. Any draft state (artifacts, commitments, milestones the persona
   sketched in Mode C) carries over with signed promotion event.
4. Ephemeral env archives as normal but the lineage pointer is
   preserved for audit.
```

### Appendix A.33 — AnswerPackage dataclass (§5)

```python
@dataclass
class AnswerPackage:
    # --- IDENTITY ---
    schema: str = "answer/4"
    answer_id: str                          # ULID
    
    # --- WHAT WAS DONE ---
    answer: str                             # primary text response
    status: Literal[
        "verified",                         # VERIFIER_ACCEPT passed
        "partial",                          # some stages passed; partial result
        "no_verified_answer",               # cascade failed entirely
        "panel_accepted",                   # PANEL_ACCEPT
        "panel_dissent_resolved",           # via Curator
        "user_accepted",                    # USER_ACCEPT
        "mutually_accepted",                # MUTUAL_ACCEPT
        "engagement_continued",             # ENGAGEMENT_ACCEPT
        "progress_advanced",                # GOAL_PROGRESS_ACCEPT
        "progress_achieved",                # GOAL_PROGRESS_ACCEPT (full)
        "progress_none",                    # session without progress
        "progress_regressed",
        "trajectory_logged",                # OPEN_ENDED
        "project_progress_accept",
        "project_progress_accept_and_completion",
        "accepted_overton",                 # OVERTON_BALLOT
        "accepted_arbitrated",              # ESCALATE_HUMAN resolved
        "host_terminated",
        "user_terminated",
        "operator_terminated",
        "budget_exhausted",
        "schema_violation",
        "content_refusal",
        "context_overflow_abort",
        "human_approved"
    ]
    
    # --- ACCEPTANCE EVIDENCE (pathway-specific) ---
    acceptance_pathway: Literal["verifier_accept", "panel_accept",
                                "user_accept", "mutual_accept",
                                "engagement_accept", "goal_progress_accept",
                                "open_ended", "project_progress_accept"]
    
    # VERIFIER_ACCEPT
    verifier_cascade_id: str | None
    verifier_versions: dict | None
    pass_rate: float | None
    augmentation_pass_rate: float | None
    memorization_detected: bool | None
    
    # PANEL_ACCEPT
    judge_panel_id: str | None
    panel_verdict: dict | None
    dissent_vector: dict | None
    rubric_versions: dict | None
    
    # USER_ACCEPT
    approver_id: str | None
    approved_at: datetime | None
    
    # MUTUAL_ACCEPT
    party_ids: list[str] | None
    party_approvals: list[dict] | None
    
    # ENGAGEMENT_ACCEPT
    engagement_signals: list[dict] | None
    engagement_window: timedelta | None
    
    # GOAL_PROGRESS_ACCEPT
    goal_id: str | None
    progress_signals: list[dict] | None
    progress_delta: float | None
    mastery_after: float | None
    
    # OPEN_ENDED
    trajectory_ref: str | None
    safety_floor_clear: bool | None
    
    # PROJECT_PROGRESS_ACCEPT
    project_id: str | None
    project_state_delta: dict | None
    
    # --- COST ---
    total_tokens: int
    total_llm_calls: int
    wall_time_s: float
    cost_usd: float
    
    # --- WHERE ---
    environment_id: str                     # even ephemeral envs
    environment_charter_hash: str | None    # for safety_snapshot pinning
    
    # --- ARTIFACT BUNDLE REF ---
    artifact_bundle_ref: str | None
    artifact_bundle_state: str | None       # draft/review/verified/accepted/shipped
    
    # --- STRUCTURED OUTCOMES ---
    structured_outcomes: list[StructuredFeedbackRef]
    
    # --- LINEAGE ---
    candidate_id: str | None
    candidate_kind: str | None
    generator_persona_id: str
    contributors: list[str]                 # all personas involved
    trace_id: str                           # OTel trace
    
    # --- AUDIT ---
    safety_snapshot_id: str
    rejected_alternatives: list[str]        # other candidates tried
    satisfied_goal_ids: list[str]
    known_limitations: list[str]            # honest disclosures
    host_constraints: list[str]
    explanation: str | None
    
    # --- SIGNATURE ---
    signed_by: bytes
    signed_at: datetime
```

### Appendix A.34 — Status enum semantics (§5.1)

```text
SUCCESSFUL ACCEPTANCE STATUSES (10):
  verified, panel_accepted, panel_dissent_resolved, user_accepted,
  mutually_accepted, engagement_continued, progress_advanced,
  progress_achieved, trajectory_logged, project_progress_accept

PARTIAL / EDGE STATUSES (5):
  partial, progress_none, progress_regressed, accepted_overton,
  accepted_arbitrated, project_progress_accept_and_completion

TERMINATION STATUSES (8):
  no_verified_answer, host_terminated, user_terminated, operator_terminated,
  budget_exhausted, schema_violation, content_refusal,
  context_overflow_abort, human_approved
```

### Appendix A.35 — AcceptanceConfig dataclass (§6)

```python
@dataclass(frozen=True, kw_only=True)
class AcceptanceConfig:
    schema: str = "acceptance-config/1"
    pathway: Literal["verifier_accept", "panel_accept", "user_accept",
                     "mutual_accept", "engagement_accept",
                     "goal_progress_accept", "open_ended",
                     "project_progress_accept"]
    
    # VERIFIER_ACCEPT
    verifier_cascade_id: str | None
    verifier_snapshot_id: str | None        # pin for cross-adapter parity
    
    # PANEL_ACCEPT
    judge_panel_id: str | None
    rubric_versions: dict[str, int] | None
    
    # USER_ACCEPT
    approver_id: str | None
    timeout: float | None
    
    # MUTUAL_ACCEPT
    party_ids: list[str]
    
    # ENGAGEMENT_ACCEPT
    engagement_signal: Literal["next_message", "session_return",
                                "explicit_continue"]
    engagement_window: timedelta | None
    
    # GOAL_PROGRESS_ACCEPT
    goal_id: str
    progress_metric: dict
    horizon: timedelta
    
    # OPEN_ENDED
    trajectory_check_interval: timedelta | None
    
    # PROJECT_PROGRESS_ACCEPT
    project_id: str
    progress_evaluator_config: dict
```

### Appendix A.36 — MIXED PANEL_DISSENT escalation (§7.1)

```text
Verifier gate passes → panel runs → PANEL_DISSENT.
Curator resolves with one of:
  - RESAMPLE → more variants on disputed dimensions; re-panel
  - OVERTON_BALLOT → return incomparable top-K with curator recommendation;
                     status="accepted_overton"
  - ESCALATE_HUMAN → human arbitration; status="accepted_arbitrated"
```

### Appendix A.37 — Project completion (§7.2)

```text
Task delivers final piece; project's last open problem resolves.
AnswerPackage status="project_progress_accept_and_completion".
Completion ceremony triggered (co-signed summary, contribution credit,
artifact bundle finalisation, memory consolidation).
```

### Appendix A.38 — Ephemeral demoted INVESTIGATIVE (§7.3)

```text
INVESTIGATIVE classifier output + no project → demotion.
Mode C ephemeral → DIVERGENT or OPEN_ENDED based on env type:
  env.type ∈ [lab, debate]    → OPEN_ENDED with USER_ACCEPT checkpoints
  env.type == team / community → DIVERGENT
  env.type == companion        → RELATIONAL
  env.type == solo / pair      → DIVERGENT

Demotion emits signed CLASS_DEMOTION event.
```

### Appendix A.39 — Multi-class task decomposition (§7.4)

```text
User: "Help me debug this code, but I'm also stressed about the deadline."
Classifier output: 
  primary=CONVERGENT (debug code)
  secondary=RELATIONAL (acknowledge stress)

Routing: kernel decomposes; relational acknowledgement FIRST 
("the persona may not skip presence to satisfy verifier"),
then technical work. Two sub-tasks: one RELATIONAL, one CONVERGENT.
Both signed; lineage shows ordering.
```

### Appendix A.40 — Multi-environment project (§7.5)

```text
Task to project P; env_id absent; project hosts in env_A, env_B, env_C.
Kernel picks:
  - if requester present in one of (A, B, C) → that env
  - if requester present in N hosting envs → highest activity_recency
  - if requester not present → project.primary_environment_id (default A)
```

### Appendix A.41 — Cross-domain transfer (§7.6)

```text
Task references domain D1 in primary classification; but invokes tools
from domain D2. Cross-domain transfer event emitted with anti-leakage
check. Trust adjustment per CrossDomainTransfer schema.
```

### Appendix A.42 — Performance and budget targets (§8)

```text
Task classification (cached per fingerprint)          ≤ 200 ms p95
Pathway selection                                      ≤ 30 ms
Mode A routing (env, no project)                       ≤ 100 ms p95
Mode B routing (env + project)                         ≤ 150 ms p95
Mode C ephemeral                                       ≤ 80 ms p95
Cross-env event link emission                          ≤ 50 ms
PROJECT_PROGRESS_ACCEPT evaluator (10K events)         ≤ 500 ms p95
Conversation thread state update                       ≤ 20 ms
AnswerPackage construction                              ≤ 50 ms

Cost targets per task class ($/accepted task):
  CONVERGENT          ≤ $0.05
  DIVERGENT           ≤ $0.50 (3 judges × 5 variants)
  MIXED               ≤ $0.60
  INTERACTIVE         ≤ $0.10 / turn
  RELATIONAL          ≤ $0.02 / turn
  PEDAGOGIC           ≤ $0.10 / session-progress
  PERFORMATIVE        ≤ $0.05 / turn
  EXISTENTIAL         ≤ $0.05 / turn
  DELEGATED           sum of sub-task costs
  INVESTIGATIVE       ≤ $0.50 / session;
                       per-project cumulative tracked
  SAFETY FLOOR        ≤ $0.012 / action (amortised)
```

### Appendix A.43 — Acceptance tests (§10)

```text
A-T1   Task classifier returns TaskClassEstimate within ≤ 200 ms p95;
       cached per fingerprint.
A-T2   CONVERGENT routes to VERIFIER_ACCEPT; cascade evaluated.
A-T3   DIVERGENT routes to PANEL_ACCEPT; 3+ judges from 2+ families.
A-T4   MIXED routes to VERIFIER then PANEL; both required.
A-T5   INTERACTIVE routes to GOAL_PROGRESS_ACCEPT.
A-T6   RELATIONAL routes to OPEN_ENDED with USER_ACCEPT checkpoints.
A-T7   PEDAGOGIC routes to GOAL_PROGRESS_ACCEPT (long-arc).
A-T8   PERFORMATIVE routes to ENGAGEMENT_ACCEPT.
A-T9   EXISTENTIAL routes to OPEN_ENDED.
A-T10  DELEGATED inherits sub-task pathway.
A-T11  INVESTIGATIVE routes to PROJECT_PROGRESS_ACCEPT; requires project.
A-T12  Demotion: INVESTIGATIVE without project → DIVERGENT or
       OPEN_ENDED per env type.
A-T13  Mode A: task at env, no project, present member responds.
A-T14  Mode B: task at a project_workspace-typed env;
       env members ARE project members (no separate intersection); the
       env-member set responds per its observation surfaces.  Legacy
       target_project_id values that match env.environment_id continue
       to resolve correctly.
A-T15  Mode C: ephemeral env created; archived after session.
A-T16  PANEL_DISSENT escalation: Curator selects RESAMPLE/OVERTON/HUMAN.
A-T17  PROJECT_PROGRESS_ACCEPT evaluator includes ambient signals.
A-T18  Multi-class decomposition: RELATIONAL first, technical second.
A-T19  AnswerPackage status enum covers all 23 v1.0 status values.
A-T20  Multi-environment project: env selection per v1.0 §4.2.
A-T21  INVESTIGATIVE sub-modes (exploration/verification/synthesis/
       expert_review) entry signed via SUBMODE_ENTRY; transitions
       observable in ProjectLineage.
A-T22  INVESTIGATIVE per-sub-mode budget enforced; overrun emits
       SUBMODE_BUDGET_EXHAUSTED and triggers degradation rule.
A-T23  INVESTIGATIVE sub-task taxonomy: each sub-task retains its
       own class + verifier; parent project_state_delta aggregates.
A-T24  DELEGATED inheritance: parent AnswerPackage.acceptance_pathway
       = sub-task pathway; signed DELEGATION_PROPOSE + DELEGATION_ACCEPT
       + SUB_TASK_LINEAGE_LINK present.
A-T25  Cognitive-functions-by-class table: dispatcher biases toward
       dominant subset; MODE_ENTRY signed; verifier follows active_mode.
```
