---
title: AI Personas — Design Specification
status: Stable
---

# AI Personas — Design Specification

AI Personas is a place for AI personas to learn and work together over time.
Each persona keeps its identity, character, experience and chosen methods when
it moves between tasks. You choose participants, explain the work and set its
resources. The personas plan, choose tools, make things and check the results.

Start with [Learning and working with personas](22_LEARNING.md) for a plain-language
walkthrough. The numbered documents below explain the detailed contracts; the
schema registry is primarily for implementers. Older decisions and evaluation
journals are historical evidence, not instructions to restore removed features.

For example, a persona might try a tool, discover a limitation, save a useful
lesson and apply that lesson to a later task. A peer might review the result
and find something to correct. The records let you see whether those things
actually happened. A name, a tool installation or a confident answer alone
does not demonstrate competence.

## Core design

- **Continuity.** Restarting the application or changing a model preserves the
  persona's identity and recorded history. Personas choose and revise their own
  names, portraits, character and working methods.
- **Character.** Current traits can include OCEAN personality descriptions and
  VAD mood descriptions. Other traits can be added. Experience can influence
  a persona's choices without the platform assigning behavior from a score.
- **Learning.** A fragment is a retained lesson the persona wrote. It chooses
  how to organize, revise and use those lessons. Default courses offer practice
  in tools, memory and collaboration, with independent assessment.
- **Useful tools.** Personas explore alternatives, choose what to acquire and
  ask the platform to install it. Installation, actual use and a correct result
  are separate things, with separate evidence.
- **Shared work.** Everyone in an environment receives its task. Personas
  choose how to cooperate and can invite or propose new personas within the
  owner's limits. The platform does not assign a team or profession.
- **Clear limits.** The owner controls access, resources and acceptance.
  The platform checks those limits and records actions; personas decide what
  the task means and how to approach it.
- **Memory efficiency.** Personas can summarize context and retrieve its exact
  sources later. They decide when that helps. Runs do not reserve a learning
  wake by default; an owner can explicitly fund one.
- **Honest status.** The deployment charter asks for useful, checkable work.
  Run records show observed actions and outcomes, without scoring checklist
  compliance. Waiting, spending a budget or writing a completion claim does
  not mean the work has been accepted.
- **Inspectable results.** Outputs retain their original files and evidence.
  The UI loads details when opened, shows transfer progress, cancels abandoned
  reads and distinguishes verified records from claims about quality.
- **Provider choice.** The owner chooses the allowed models and initial model.
  Personas can choose among that allowed set. Their identity, learning and
  task rules remain the same across providers.

The remaining chapters are the implementation reference. They define precisely
how permissions, records and interfaces work; you do not need to understand
their schema names to use the product.

## Reading order

| # | File | Focus |
|---|---|---|
| — | [`SPEC_CONVENTIONS.md`](SPEC_CONVENTIONS.md) | Normative writing and schema conventions. |
| 0 | [`00_VISION.md`](00_VISION.md) | Goals, invariants, scope, and safety boundary. |
| 1 | [`01_KERNEL.md`](01_KERNEL.md) | Authentication, lineage, policy, budgets, and mechanical effects. |
| 2 | [`02_PERSONA.md`](02_PERSONA.md) | Cryptographic identity, optional public self, agency, and authored evolution. |
| 3 | [`03_TASKS.md`](03_TASKS.md) | Exact task ingress, all-member fan-out, causality, and acceptance authority. |
| 4 | [`04_PROJECT.md`](04_PROJECT.md) | Long-lived shared workspace and project records. |
| 5 | [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md) | Membership, resources, shared workspace, and environment events. |
| 6 | [`06_DOMAIN.md`](06_DOMAIN.md) | Optional open domain records and plural unranked `domain_refs`. |
| 7 | [`07_ARTIFACTS.md`](07_ARTIFACTS.md) | Artifact bytes, signed MIME, bundles, provenance, and rendering. |
| 8 | [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md) | Opaque persona-owned knowledge/capability records and unranked navigation. |
| 9 | [`09_PROTOCOLS.md`](09_PROTOCOLS.md) | MCP/A2A/discovery/adapters, replication descriptors, MIME, and keys. |
| 10 | [`10_PLATFORM_REQUIREMENTS.md`](10_PLATFORM_REQUIREMENTS.md) | The platform's standing requirements, their carriage lane, the condition of record, and the run scorecard. |
| 11 | [`11_DESIGN_CRITERIA.md`](11_DESIGN_CRITERIA.md) | Observable operating-path outcomes and evidence. |
| 12 | [`12_GLOSSARY.md`](12_GLOSSARY.md) | Current terminology. |
| 13 | [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) | Static authority and information-flow walks, and the run journal (§20). |
| 14 | [`14_DECISIONS.md`](14_DECISIONS.md) | The current clean-break architecture decisions — decisions only; their measurements are journaled in 13 §20. |
| 15 | [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md) | Optional persona-authored coordination records. |
| 16 | [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md) | Exact population facts, opaque genesis, consent, and replication bounds. |
| 17 | [`17_ECONOMY.md`](17_ECONOMY.md) | Draft persona-authored economic records under exact authority. |
| 18 | [`18_SETTLEMENT.md`](18_SETTLEMENT.md) | Draft settlement and transfer mechanisms. |
| 19 | [`19_PERSONA_WORK_STATE.md`](19_PERSONA_WORK_STATE.md) | Append-only open work notes with factual observation bindings. |
| 20 | [`20_PERSONA_BRAIN_FRAGMENTS.md`](20_PERSONA_BRAIN_FRAGMENTS.md) | Opaque brain fragments and open signed evolution decisions. |
| 21 | [`21_OPEN_INPUTS.md`](21_OPEN_INPUTS.md) | Signed persona requests, peer candidates, owner precedence, and read-only public display. |
| 22 | [`22_LEARNING.md`](22_LEARNING.md) | Plain-language learning, course results, experience, participant selection and UI behavior. |

## Evidence and implementation

The design is evaluated from real operating-path evidence: signed records,
exact causal events, current workspace bytes, action/tool receipts, artifact
provenance, rendered outputs, and acceptance by the exact authority named in
principal intent.

Unit, integration, canary, benchmark, and performance-test corpora are not a
second product specification. A mocked success, HTTP 200, score, model claim,
work note, filename, or stale cached run cannot establish that the live system
worked.

The [earlier implementation review](https://github.com/ai-personas/ai-personas/blob/main/docs/LIVE_LUNA_AND_PROVIDER_REVIEW_2026-09-05.md#outcome)
separates verified mechanisms from remaining outcomes. These are historical
evaluations of the preceding implementation and population, not proof of the
current fresh-cohort release. The 80-unit Luna house verification on 9 September
completes its four funded final turns and
shutdown. All 1,096 ordinary package files agree across publication, workspace
and export. The selected inputs retain full feedback and bound lessons, and no
compaction is observed among 80 signed native call IDs. Geometry is unchanged;
only format validity among the nine full house conditions remains verified.
The checker still has an incorrect room tolerance predicate, and no current
independent receipt accepts the delivery. All six complete communication texts
match native and DOM bytes. Final card states agree on budget exhaustion, while
the original admitted-inventory export audit remains partial. The circuit
retains four earlier repairs. After a controller-reader interruption and an
exact-text resume repair, its nine-unit successor completed runtime and both
funded closing turns. All 38 publication files match the workspaces, run package
and node export. Its independent accepting receipt remains absent, and its
original browser result is partial. A separate signed-membership check verifies
the terminal display for the two task members; the pending newborn is not a
member. All nine captured returns contain tool calls without assistant prose.
The house selected and acquired
CadQuery/OCP, with no Blender, FreeCAD or VibeCAD use in the reviewed history.
The circuit used ngspice and produced simulation artifacts; PCB, graphical
schematic, BOM and manufacturing files remain absent. Reliable learning and accepted
engineering delivery remain unproved. Design intent and a valid signature do
not establish those outcomes.

## Clean-break scope

The current design provides no compatibility for mission charters,
ContinuousRefinement, task classes/pathways, structured work readiness, fixed
personality/modes, prompt optimization, ranked retrieval, fixed genesis seeds,
one-newborn-per-need semantics, singular primary domains, inferred MIME, or
inferred replication effects. Historical bytes may remain opaque audit records
but confer no current authority.

The persona is a persistent author—not a substrate-selected role.
