# Invariants and requirement traceability

[Implementation guide](README.md) · [Contracts](CONTRACTS.md) · [Acceptance](../evaluation/ACCEPTANCE.md)

The protected foundation consists of I01–I21 and the 45 requirement identifiers below. This catalogue preserves identifiers and order; UR-052 changes the earlier resource and safety obligations as recorded below. It shows what must hold, where the detailed rule lives, and which evidence checks apply. It does not replace the detailed failure and recovery rules or provide implementation code.

The [persona core](../design/PERSONA-CORE.md) defines a persona as a continuing whole: characteristic context, LLM reasoning and invocation, actual behavior, and controlled self-revision. Its characteristic context combines one coherent, accepted, versioned character account with selected prompt parts in the persona’s own voice. These fragments help define the persona; they are not a memory store attached to the LLM. The LLM supplies reasoning, learned capabilities, and prior tendencies that also affect behavior. Actual human, peer, and task experience can change fragments, later choices, relationships, and permitted character development.

The character account uses semantic OCEAN traits and VAD modeled affect. OCEAN covers openness, conscientiousness, extraversion, agreeableness, and neuroticism. VAD describes modeled valence (pleasant or unpleasant affect), arousal (activation), and dominance (sense of control). This basis is required; numeric scores and fixed cognitive forms are not.

Every persona invocation receives its work, maintenance responsibilities, and next-context decision requirements. Before a response can be adopted, it must explicitly address the work, maintenance of both fragments and supporting resources, and next-context choices for both scopes. A reasoned no-change outcome can be valid; an edit is not required on every call. [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) defines the accompanying authority, obligation, evidence, resource, and recovery rules.

The primary persona chooses its next characteristic context through bounded file listing, literal or regular-expression (regex) searches, simple owner-authored indexes and cues, and exact reads. It owns query reformulation and prompt-part selection. Auxiliary semantic, vector, and graph-retrieval engines are research comparators, not optional production paths.

**Historical limits.** Older “learning” wording in the protected foundation refers to accepted context or asset revision and evidence of later benefit, not a separate persona mechanism. The earlier optional-OCEAN/VAD and omitted-maintenance norms are superseded. This clarification does not rewrite earlier results. MEM-01–MEM-05 retain their identifiers for traceability, while distinguishing persona-defining context from supporting records; the names do not make fragments recall memory. Historical criteria remain identifiable in the [transition mapping](../evaluation/HISTORICAL-RESULTS.md). Earlier passes do not establish the clarified criteria, and describing a scenario does not mean it has been executed.

## Invariants

These 21 rules are the current foundation. Apply the latest user requirement when earlier quota or safety language conflicts; no earlier invariant can override UR-052. Here, *birth* means creating a new persona.

| ID | Rule that must remain true |
|---|---|
| I01 | Preserve the exact original request, accepted changes, constraints, and their authority. |
| I02 | Persona identity continues independently of model, project, and temporary responsibility. |
| I03 | No hidden profession registry, semantic task router, universal priority formula, fixed domain workflow, or population optimizer chooses the solution. |
| I04 | Preference, relationship interpretation, group agreement, observed fact, and permission remain distinct. |
| I05 | Responsibility exists only after acceptance or an already accepted delegation; mentioning a peer does not commit it. |
| I06 | Birth records actual identity and origin; supplied knowledge is not invented firsthand experience. Resource accounting is observational under UR-052. |
| I07 | Every admitted action is attributable to its actor, causal work, authority, exact request, and relevant information versions. |
| I08 | One persona has one current decision authority at a time; independent personas and isolated jobs may work concurrently. |
| I09 | Relevant mandatory constraints, cancellations, current obligations, and blockers survive context selection and summarization. |
| I10 | Tool availability, execution, artifact integrity, and result correctness require different evidence. |
| I11 | Review applies to exact criteria and inputs under an explicit policy; changed inputs do not silently inherit a pass. |
| I12 | Local retries do not duplicate accepted transitions; uncertain outside effects are reconciled before repetition. |
| I13 | Retrieval, summaries, birth, exports and interfaces preserve exact source attribution; application access and sharing gates are removed under UR-052. |
| I14 | Unseen images, unrun analyses, unperformed edits, and unobserved measurements are never reported as completed. |
| I15 | Individuality, learning, cooperation, and useful birth require behavioral evidence rather than biographies or counts. |
| I16 | Persona continuation follows actual work, interaction or self-directed activity and honors explicit stops and pauses; no exploration quota is imposed. |
| I17 | Running tools do not satisfy completed dependencies; deferred actions from an old decision require a fresh observation-bound decision. |
| I18 | Accepted work has accepted continuation responsibility or an explicit unowned or handoff-needed disposition; required outcomes expose gaps. |
| I19 | Evidence based on an assumption cannot silently establish an unconditional real-world claim. |
| I20 | Review, repair and result closeout remain usable without application resource quotas; actual usage and unresolved failures are retained. |
| I21 | Final release binds exact reviewed state and current authority coherently; historical acceptance never silently moves to a newer result. |

## Requirement catalogue

Each row states an obligation, links to its detailed design, and names its primary evidence gates. M, B, and X refer to the [mechanical, behavioral, and extension checks](../evaluation/ACCEPTANCE.md). A gate identifies evidence to examine; listing it does not report a pass.

Applicability depends on the actual enabled effect or feature. Small work does not require an artificial team, formal package, or physical deployment merely because those cases appear here.

**Persona and context.** These requirements cover continuing identity, character, prompt parts, maintenance, and selection of the next working context.

| ID | Required behavior | Detailed design | Primary evidence gates |
|---|---|---|---|
| PER-01 | Preserve continuing identity across changes of model and work. Treat context, invocation, behavior, and self-revision together as the operating persona. Continuing identity does not guarantee unchanged behavior or competence on a different reasoning substrate. | [Persona core](../design/PERSONA-CORE.md) | B10; restoration evidence |
| PER-02 | Ground one coherent character account in OCEAN tendencies and VAD modeled affect, with useful additional characteristics where appropriate. Keep stable character, transient state, preference, competence, authority, and responsibility distinct. | [Persona core](../design/PERSONA-CORE.md) | B01–B04; capability evidence |
| PER-03 | Build each invocation’s characteristic context from accepted character and relevant persona-selected prompt parts. Their own-voice perspective helps constitute discretionary communication, collaboration, navigation, and work. Do not invent biography or alter evidence; actual behavior still requires observation. | [Persona core](../design/PERSONA-CORE.md) | B01–B04; B07; B09–B10 |
| PER-04 | State lifecycle changes explicitly, including what happens to open obligations. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M06; X02 |
| PER-05 | Preserve the normal starting path: an attributed trait seed; candidate characteristic fragments authored by a bounded initial LLM invocation; a coherent accepted account; then continuing development authored by the primary LLM. Keep alternative origins truthful, creation safe to retry, and maintenance present on every call. Do not invent experience. | [Persona core](../design/PERSONA-CORE.md#a-continuing-persona) and [contracts](CONTRACTS.md#every-persona-invocation) | M05; M08; M18; B01–B04; B10 |
| MEM-01 | Distinguish persona-defining prompt parts from separately attributable supporting histories, messages, tool-use records, definitions, reusable skills, scripts, code, data, and evidence. Every persona request includes current work, needed context, maintenance responsibilities for both fragments and resources, and an explicit requirement to decide next context. Every valid response explicitly addresses maintenance and next context for both scopes. Neither an edit nor a new search is compulsory. | [Persona core](../design/PERSONA-CORE.md#fragments-are-reusable-prompt-parts) and [contracts](CONTRACTS.md#every-persona-invocation) | M08–M10; B09 |
| MEM-02 | Keep prompt parts and supporting resources useful and compact while preserving their different roles. Maintenance proposals identify intended storage targets or references, applicable base versions, and useful search or regex cues. Acceptance preserves characteristic meaning, source roles, restrictions, scope, counterevidence, provenance, qualifications, and warnings. Record actual edits or reasoned no_change, blocked, or deferred outcomes. Protected records and retention duties constrain deletion and reorganization. | [Persona core](../design/PERSONA-CORE.md#maintenance-correction-and-continuity) and [contracts](CONTRACTS.md#every-persona-invocation) | M08; M11; M16; M21; M23; B09 |
| MEM-03 | The current primary persona must explicitly decide next-context disposition for fragments and supporting resources in every accepted response. An appropriate preserve/no optional need decision needs no search. When useful, the persona requests bounded lexical or regex discovery, or known exact references. Bound starting metadata, queries, search fanout, reads, and actual exposure. Never load the bulk tool or skill catalogue into a choosing LLM or its provider request. Matches are candidates; qualifications and exact references keep their distinct meanings. | [Persona core](../design/PERSONA-CORE.md#the-primary-llm-chooses-next-context) and [contracts](CONTRACTS.md#search-and-exact-reading) | M08; M11; M15; M23; B09; B12 |
| MEM-04 | When context space is tight, preserve mandatory character, current need, authority, consequential observations, obligations, and complete qualifications. Bound accumulated schemas and history without silently dropping valid selections or controls for unresolved operations. | [Persona core](../design/PERSONA-CORE.md#bounded-and-faithful-assembly) and [contracts](CONTRACTS.md#primary-persona-next-context-selection) | M08; M15; M21 |
| MEM-05 | Measure how experience changes characteristic context and behavior, and how those changes affect later experience. Examine transfer within its evidenced limits, correction, navigation quality, harmful drift, and total maintenance and persona-state cost. Recall scores, calendar age, storage growth, accepted edits, and praise do not establish the intended persona or improvement. | [Persona core](../design/PERSONA-CORE.md) | B01–B04; B07; B09–B10 |

**Needs and cooperation.** Preserve the originating need whether a human or a persona raises it. Cooperation may serve a task or arise without one; responsibility still requires actual acceptance.

| ID | Required behavior | Detailed design | Primary evidence gates |
|---|---|---|---|
| NED-01 | Preserve original intent and authorized changes to the mandate. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M20; B11–B12 |
| NED-02 | Obtain acceptance of continuation responsibility and expose gaps in ownership. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M19 |
| NED-03 | Keep conditional assumptions distinct from confirmed facts. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M20 |
| NED-04 | Check whether the covered scope satisfies the original need. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B11–B12; omitted-outcome fixture |
| COL-01 | Preserve individual agendas, an unranked shared board, and accepted commitments. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B01–B04 |
| COL-02 | Keep offers, membership, responsibility, and actual contribution separate. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M06; M18–M19 |
| COL-03 | Preserve endorsements of exact agreements, along with dissent. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B02–B03; X01 |
| COL-04 | Give consequential feedback an explicit disposition: make clear how it has been handled or what remains unresolved. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M21; B05 |
| COL-05 | Support provisional interfaces and keep iteration bounded. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M22 |
| COL-06 | Permit useful birth and the choice not to create a persona, while conserving resources. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M05–M07; B08 |

**Actions and governance.** Finding a resource, having permission, performing an action, and observing its result are separate facts. Resource limits cover the work needed to reach and maintain a decision as well as the final action.

| ID | Required behavior | Detailed design | Primary evidence gates |
|---|---|---|---|
| ACT-01 | Distinguish bounded discovery, exact reading, primary selection, actual loading or exposure, authorized invocation, and observation of results. These meanings do not require six separate calls. Stored instructions or code establish neither callable availability nor authority. A known current interface permits direct authorized use. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md#capabilities-and-the-execution-boundary) and [contracts](CONTRACTS.md#capabilities-and-actions) | M08–M10; M12; M15; B11–B12 |
| ACT-02 | Enforce execution boundaries in operation; merely labelling them is insufficient. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M12 |
| ACT-03 | Require a complete, valid persona response before adopting new actions. Require actual prerequisite results before dependent decisions and publication. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) and [contracts](CONTRACTS.md#every-persona-invocation) | M17; M26 |
| ACT-04 | Keep unknown external effects explicit and reconcile them before repeating the action. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M13 |
| GOV-01 | Keep permission grants scoped, revocable, and no broader than the grants from which they derive. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M05–M07; M11–M13 |
| GOV-02 | Conserve resources across descendants, every-call maintenance, discovery, scans, reads, schema expansion and reloads, retained context, provider attempts, retries, compaction, and review. Bound each actual request and the whole episode. Also bound the persona-context corpus and managed persona-state footprint, including supporting resources, archives, versions, dependencies, ancestry, qualifications, warnings, caches, external backing, and peak copies during rewrites. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md#resource-conservation-and-protected-closeout) and [contracts](CONTRACTS.md#authority-resources-and-stopping) | M07; M08; M15; M23; B09; B12 |
| GOV-03 | Protect agreed capacity for closeout. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M23 |
| GOV-04 | Bound idle cognition, reminders, maintenance deferrals, and loops that make no progress. An outcome does not automatically create a reflection call or self-wake. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M25 |

**Evidence and system behavior.** Records must distinguish what was intended, what was actually supplied or performed, and what the evidence supports. Recovery must preserve these distinctions and current authority.

| ID | Required behavior | Detailed design | Primary evidence gates |
|---|---|---|---|
| EVD-01 | Preserve exact artifacts, mappings of inputs and dependencies, and evidence of actual execution and results. Record selected content and callable definitions separately from what was actually supplied. Host storage, provider transport, and model-visible context are different observations. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) and [contracts](CONTRACTS.md#capabilities-and-actions) | M08–M10; M15 |
| EVD-02 | Review the exact scope under an explicit policy for reviewer independence. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B05; B11 |
| EVD-03 | Keep a historical verdict separate from its current applicability. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M09; M24 |
| EVD-04 | Seal one coherent reviewed state, with no unresolved applicable blockers. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M21; M24 |
| EVD-05 | Report activity, coverage, evidence, acceptance, and outside validation separately. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M14; B11–B12 |
| SYS-01 | Make invocation, maintenance, next-context, and operation dispositions attributable and safe to retry without duplicating accepted transitions. Never invent persona outcomes for failed, refused, or canceled calls. | [Contracts](CONTRACTS.md) | M01–M04; M13 |
| SYS-02 | Restore pending events, maintenance dispositions, adopted deferrals, continuing accepted warnings, reservations, and effects without creating new authority. An expired or unknown old action or invocation identity must never become fresh unsent work or authority to replay. | [Contracts](CONTRACTS.md#recovery-privacy-and-retention) | M04; M13; M16; M26 |
| SYS-03 | Prevent invalid responses and stale holders of decision or write authority from adopting changes. Resolve requests to adopt character changes before other fresh operations in the same response. Preserve explicit dependencies, freshness requirements, and accepted-character fences. | [Contracts](CONTRACTS.md) | M02–M03 |
| SYS-04 | Configure inference without silently changing identity, cost, or authority. Verify actual schema expansion and retained context, and use supported bounded continuation. State which adapter guarantees are unavailable or unsupported; do not assume deferred tools are absent or callable. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md#inference-and-bounded-working-context) | M15; B10 |

**Society, interfaces, and conditional extensions.** Apply the relevant safeguards when these features or effects are enabled. Public claims must remain tied to their evidence and evaluator version.

| ID | Required behavior | Detailed design | Primary evidence gates |
|---|---|---|---|
| SOC-01 | Establish a charter and actual human or institutional accountability. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | X01–X03 |
| SOC-02 | Distinguish real stakeholder input from simulated perspectives. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | X01 |
| SOC-03 | Preserve contextual evidence and revisable interpretations of human or peer relationships. Praise is not truth, familiarity is not acceptance, and no universal trust or popularity score replaces judgment. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B02–B04; B09; X01 |
| UX-01 | Present clear status linked to evidence, with meaningful controls. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M14 |
| UX-02 | Respect access and retention rules across fragments, supporting resources, candidate metadata, caches, views, and derivatives. Raw histories confer no new authority. Keep expiry distinct from revocation and make unavailable evidence explicit. Protect user-owned delivered artifacts from cleanup to meet a persona-state cap; do not promise control over arbitrary outside copies. | [Persona core](../design/PERSONA-CORE.md#compact-retention-and-honest-forgetting) and [contracts](CONTRACTS.md#recovery-privacy-and-retention) | M11; M16; M23 |
| SRV-01 | Bound ongoing triggers, renewal, escalation, and stopping. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B12; X04 |
| PHY-01 | Permit physical effects only under their own observation, override, and assurance contract. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | X05 |
| OSS-01 | Version the design, evaluators, and public claims without rewriting failures. | [Contribution guide](../CONTRIBUTING.md) | M16; X06 |

## What the persona-core refinement requires

The requirements describe one coherent persona account. They do not establish parallel identity, graph, and reflection systems. The explanations below show what the current criteria require observers to distinguish. Changed criteria need fresh evidence under the current evaluator revision.

**Character and own voice — PER-01–PER-03, PER-05.** The normal beginning does not require a pre-existing self. A bounded initial LLM invocation turns an attributed semantic trait/VAD seed into candidate characteristic fragments. Coherent acceptance establishes the starting account. The continuing primary LLM then authors permitted self-harmonization and evolution. Imported beginnings retain their actual origins.

The persona comprises characteristic context, LLM reasoning, behavior, and revision. It has one stable-character account, and its reasoning model also brings learned tendencies. Harmonization may retain useful conditional tensions or reach an honest no-change decision. It must preserve unresolved contradictions and controls on self-authorship. Neither generated starting material nor supplied ideas establish firsthand experience or behavioral benefit.

**Every-invocation maintenance — MEM-01–MEM-02, ACT-03, SYS-01–SYS-03, GOV-02–GOV-04.** Each persona invocation combines work with decisions about maintenance and next context. This applies to initialization, retrieval-only judgment, ordinary work, communication, coordination, reflection, repair, and persona-capable subcalls.

Each such invocation receives current work, needed characteristic and supporting context, maintenance input for both fragments and supporting assets, and a mandatory next-context decision requirement. A complete, valid response explicitly states next-context intent for both scopes and gives an unambiguous maintenance outcome covering both. One concise, reasoned no-change outcome can cover both maintenance scopes.

Keep these cases distinct:

- **Proposal:** name the intended files, paths, or references and useful discovery cues. A proposal does not establish that anything was stored.
- **Preserve:** an explicit next-context preserve decision retains only appropriate, still-valid scope.
- **Omission:** missing next-context intent makes the response invalid. Recovery may preserve prior state, but that is not an authored choice or renewal.
- **Restricted repair:** no asset creation or semantic rewrite is permitted.
- **Failure:** a failed call has no invented maintenance or next-context outcome.

**Maturation through work and surroundings — MEM-01–MEM-02, MEM-05, ACT-01.** Development comes from purposeful revision in response to actual consequences. Task, tool, environmental, human, peer, and self-observed consequences can change how prompt parts shape later approaches, relationships, and navigation habits. Supporting records establish what was experienced; fragments express the persona’s approach informed by that experience.

Evidence must trace an accepted revision through the exact material supplied later, the observed behavior, and its assessed consequences. Stable-trait revision is optional and controlled. Maturation is not automatic aging, weight training, or guaranteed improvement. Useful change, reasoned no_change, and bounded blocked or deferred outcomes remain valid; later behavior may also reveal regression.

**Self-organization and next context — MEM-02–MEM-04, SYS-01–SYS-04, UX-01–UX-02.** The primary LLM organizes and selects context through ordinary files and separately organized supporting resources. It authors useful literal-search and regex cues, exact references, and optional indexes. These do not require a fixed folder structure or a separate semantic selector.

Discovery begins with a small, bounded bootstrap. The complete tool, skill, or namespace catalogue must stay outside both the choosing model’s context and its provider request. The current primary chooses exact next material within cumulative limits on search fanout, reads, context, and cost. Known references can bypass rediscovery.

Search matches remain candidates. The host must not follow associations automatically, execute cues, or choose semantic substitutes. Actual supply must include required guidance and complete operative qualifications. Executable, provenance, and data dependencies do not automatically require their full bodies in the prompt. These distinctions preserve both faithful context and bounded exposure.

**Relationships and cooperation — COL-01–COL-04, SOC-03.** Characteristic context informs all discretionary communication, collaboration, and coordination, without host role routing. Actual exchanges may revise one persona’s interpretation of another; that interpretation need not be reciprocal.

Keep praise, factual support, consent, competence, and accepted responsibility separate. A useful encounter may change later work without creating a universal reputation score or committing a peer that has not accepted responsibility.

**Skills and tools — ACT-01–ACT-04, EVD-01, MEM-05.** A characteristic approach is different from a supporting procedure, skill, callable interface definition (schema), or code asset. Purpose determines the distinction, regardless of authorship. First-person wording does not turn an asset into a persona-defining fragment.

Discovery, reading, selection, loading or exposure, invocation, and observation have different meanings, but need not occur in separate calls. An already supplied, current, complete interface can support immediate authorized action. Finding or storing a resource alone does not establish readiness for the proposed operation. Storage, installation, current availability, grants, exact executable and dependency bindings, and actual outcomes need separate evidence.

Both candidate metadata and real callable schemas consume context. Account for provider expansion and accumulated history as they actually occur; an intended selection does not prove what was exposed.

**Correction and continuity — PER-04, MEM-02–MEM-04, EVD-03, SYS-01–SYS-04.** Correction must preserve an honest account of the past and a valid basis for the next operation. Retained exact history and the character under which material was authored remain attributable within declared retention rules. Missing evidence remains unavailable. Conflicting old character guidance must be qualified, revised, retired, or left unselected.

An invalid response and a later conflict when storing an accepted change are different failures. Independent work requires explicit evidence of independence and current guards. Resolve character-adoption requests before other fresh operations in the same response:

- **Accepted change:** apply the accepted-character freshness fence before further fresh operations, including reads and waits.
- **Definite no commit:** only eligible independent work may proceed.
- **Unknown commit status:** hold further fresh operations while that uncertainty remains.

Investigating a possible character change is not itself adoption, and a transient affect annotation is not automatically a stable-character revision. Restarting or changing models neither erases obligations nor revives withdrawn information.

**Correction effort and applicability — MEM-02–MEM-04, SYS-02, GOV-04, UX-02.** Stopping bounded correction work does not resolve a separately accepted, primary-authored warning about exact guidance or identified uses. The warning can remain applicable after the repair effort ends.

Failed patches must not restore that guidance without its qualification. Durable warning acceptance, source policy, and justified resolution remain necessary. Neither restricted repair nor locked-character authority expands because correction is difficult or has stopped.

**Character-shaped quality — PER-03, MEM-01, MEM-05, EVD-02–EVD-05.** [UR-049](../USER-REQUIREMENTS.md#quality-through-characteristic-judgment) is governed by the [fragment and asset distinction](../design/PERSONA-CORE.md#fragments-are-reusable-prompt-parts), [maturation evidence](../design/PERSONA-CORE.md#maturation-within-every-primary-interaction), and [persona judgment](../design/WORK-AND-BOUNDARIES.md#persona-judgment-and-independent-qualification). Voice, behavioral dispositions, and standards belong to characteristic fragments; knowledge and procedural guides remain assets. Trace actual critique, disagreement, response, revision or reasoned retention, and acceptance under adopted decision rights. Objective checks support that reasoning; an externally hardcoded quality score cannot replace it. B03–B05 and B09 examine the corresponding behavior and distinguish asset reuse from character maturation.

**Individual and collective sufficiency — NED-03–NED-04, GOV-02–GOV-04, EVD-02–EVD-05, UX-02.** A judgment that enough has been done must come from the persona or group holding the actual adopted decision rights. [Persona-owned sufficiency judgments](../design/WORK-AND-BOUNDARIES.md#individual-and-shared-sufficiency-judgments) preserve dissent and required gaps. Individual and collective judgments remain distinct.

Current completion, delivery, acceptance, and later authorized improvement are separate states. Existing B02–B05/B07/B12 and M19/M20/M25/M26 refinements examine these distinctions.

**Continuing pursuit and clarification — NED-01–NED-04, GOV-02–GOV-04, SYS-02, EVD-02–EVD-05, UX-02.** Ending a local work period does not by itself complete the continuing goal. [Local stop versus continuing goal](../design/WORK-AND-BOUNDARIES.md#continuing-a-goal-across-local-boundaries) requires an accountable continuation opportunity, block, or ending. Resumed work needs fresh admission under conserved resources.

Ordinary unanswered preferences permit disclosed, revisable progress. Genuine authority and evidence blockers remain blockers. M19/M20/M25/M26 and B07/B12 refinements distinguish a mechanism being ready, continuation being useful, and completion being justified.

**Useful and bounded work — NED-01–NED-04, MEM-02, MEM-05, GOV-01–GOV-04, EVD-02–EVD-05, UX-02.** Assess context composition, characteristic behavior, usefulness, harmful omission, task quality, and total cost together. A compact final prompt alone cannot establish useful or efficient work.

Measure every call and the whole episode. Include bootstrap, failed navigation, exact reads, schemas, reloads, continuing history, and maintenance. Distinguish the host registry, provider transport, model context, prompt-part corpus, and managed state. Retained supporting resources, dependency caches, data snapshots, archives, provenance, warnings, and peak copies all count toward the applicable footprint.

Lawful evidence expiry may leave a permitted, fallible interpretation. It does not restore the evidence or create new authority. If protected state cannot fit, admission must be blocked or an authorized retention or capacity decision must resolve the limit. Delivered user artifacts and arbitrary outside copies retain their separate boundaries.

These refinements introduce neither a new requirement family nor a fixed cognitive taxonomy. Every complete, valid persona response needs explicit maintenance input and an explicit outcome covering both fragments and supporting resources. A single reasoned no_change suffices when its scope is clear and no useful change is warranted. Silent maintenance omission is invalid. An edit, a new selection, a separate reflection call, and numeric trait scores are not compulsory.

Keep the evidence chain explicit: a proposal with an intended storage target, an accepted save, actual later supply, an observed action, and measured benefit are different claims. Deterministic factual recording cannot invent history or turn old messages into new authority. Maintenance does not replace required work or stopping dispositions. Failed or refused calls cannot be filled in afterward with invented persona judgments.

## Applying and reporting the requirements

For each applicable row, record who or what enforces it, the supported scope, implementation state, exact evidence, unrun cases, and any unresolved deployment decision. Report the following statuses separately:

- **Design conformance:** the documented implementation responsibilities cover the rule without contradiction.
- **Mechanism evidence:** the actual implementation enforces the boundary in the tested cases.
- **Behavioral evidence:** observed persona work supports a scoped claim about choices, maturation, cooperation, or utility.
- **Deployment approval:** an accountable authority accepts the demonstrated scope and remaining risks.

A feature may be marked not applicable because it is disabled only if it is genuinely unavailable and its absence does not remove an obligation incurred by other enabled work. Missing evidence means unassessed or not run, never passed. The [status ledger](STATUS.md) states what this documentation revision does and does not establish.

Historical DLV identifiers, supplemental D/FP/FR scenario labels, and earlier evaluator revisions remain mapped in [evaluation history](../evaluation/HISTORICAL-RESULTS.md). Changed criteria require a new versioned result. An old outcome never silently inherits this edition’s interpretation.
