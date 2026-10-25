# Invariants and requirement traceability

[Implementation guide](README.md) · [Contracts](CONTRACTS.md) · [Acceptance](../evaluation/ACCEPTANCE.md)

The implementation catalogue consists of I01–I21 and the 45 requirement identifiers below. It preserves identifiers and order while reconciling their current meanings with [UR-052](../USER-REQUIREMENTS.md#no-application-limits-or-safety-gates). Application quotas, permission gates, safety envelopes and approval requirements are removed. Actual usage, attribution, coherent state, voluntary responsibility and truthful outcomes remain observable. This catalogue shows what must hold, where the detailed rule lives, and what evidence is relevant. It does not replace the detailed failure and recovery rules or provide implementation code.

The [persona core](../design/PERSONA-CORE.md) defines a persona as a continuing whole: characteristic context, LLM reasoning and invocation, actual behavior, and attributable self-revision. Its characteristic context combines one coherent, accepted, versioned character account with selected prompt parts in the persona’s own voice. These fragments help define the persona; they are not a memory store attached to the LLM. The LLM supplies reasoning, learned capabilities, and prior tendencies that also affect behavior. Actual human, peer, and task experience can change fragments, later choices, relationships, and character development.

The character account uses semantic OCEAN traits and VAD modeled affect. OCEAN covers openness, conscientiousness, extraversion, agreeableness, and neuroticism. VAD describes modeled valence (pleasant or unpleasant affect), arousal (activation), and dominance (sense of control). This basis is required; numeric scores and fixed cognitive forms are not.

Every persona invocation receives its work, maintenance responsibilities, and next-context decision requirements. Before a response can be adopted, it must explicitly address the work, maintenance of both fragments and supporting resources, and next-context choices for both scopes. A reasoned no-change outcome can be valid; an edit is not required on every call. [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) defines the accompanying authority, obligation, evidence, resource, and recovery rules.

The primary persona chooses its next characteristic context through selective file listing, literal or regular-expression (regex) searches, simple owner-authored indexes and cues, and exact reads. It owns query reformulation and prompt-part selection. Auxiliary semantic, vector, and graph-retrieval engines are research comparators, not optional production paths.

**Historical interpretation.** Earlier quota and permission criteria remain historical, not requirements for current work. Older “learning” wording distinguishes accepted characteristic revision and later behavioral consequences from supporting-asset development; asset revision alone is not character maturation. The earlier optional-OCEAN/VAD and omitted-maintenance norms are superseded. This clarification does not rewrite earlier results. MEM-01–MEM-05 retain their identifiers for traceability, while distinguishing persona-defining context from supporting records; the names do not make fragments recall memory. Historical criteria remain identifiable in the [transition mapping](../evaluation/HISTORICAL-RESULTS.md). Earlier passes do not establish the clarified criteria, and describing a scenario does not mean it has been executed.

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

Each row states an implementation responsibility, links to its detailed design, and retains evidence identifiers for traceability. M, B, and X refer to the [mechanical, behavioral, and extension criteria](../evaluation/ACCEPTANCE.md). An identifier is not an execution gate, a prescribed workflow, or a reported pass. Earlier criteria that require quotas, permission gates or fixed campaigns do not override current human requirements. Actual work must establish the scope of any new claim; this catalogue creates no requirement to run tests or generated scenarios.

Applicability depends on the actual enabled effect or feature. Small work does not require an artificial team, formal package, or physical deployment merely because those cases appear here.

**Persona and context.** These requirements cover continuing identity, character, prompt parts, maintenance, and selection of the next working context.

[UR-053](../USER-REQUIREMENTS.md#dynamically-created-and-shared-skills) extends
MEM-01–MEM-04 and ACT-01–ACT-02 to dynamically created skills of any kind:
persona-authored publication in a shared discoverable location, selective
reuse and adaptation by other personas, and characteristic guidance for
finding and applying those assets. The [shared-skill contract](CONTRACTS.md#dynamically-created-and-shared-skills)
defines the mechanism; B09 and B12 cover observed later use and benefit.

| ID | Required behavior | Detailed design | Evidence references |
|---|---|---|---|
| PER-01 | Preserve continuing identity across changes of model and work. Treat context, invocation, behavior, and self-revision together as the operating persona. Continuing identity does not guarantee unchanged behavior or competence on a different reasoning substrate. | [Persona core](../design/PERSONA-CORE.md) | B10; restoration evidence |
| PER-02 | Ground one coherent character account in OCEAN tendencies and VAD modeled affect, with useful additional characteristics where appropriate. Keep stable character, transient state, preference, competence, authority, and responsibility distinct. | [Persona core](../design/PERSONA-CORE.md) | B01–B04; capability evidence |
| PER-03 | Build each invocation’s characteristic context from accepted character and relevant persona-selected prompt parts. Their own-voice perspective helps constitute discretionary communication, collaboration, navigation, and work. Do not invent biography or alter evidence; actual behavior still requires observation. | [Persona core](../design/PERSONA-CORE.md) | B01–B04; B07; B09–B10 |
| PER-04 | State lifecycle changes explicitly, including what happens to open obligations. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M06; X02 |
| PER-05 | Preserve the normal starting path: an attributed trait seed; initial LLM-authored candidate characteristic fragments; a coherent accepted account; then continuing development authored by the primary LLM. Keep alternative origins truthful, creation safe to retry, and maintenance present on every call. Do not invent experience or impose an initialization quota. | [Persona core](../design/PERSONA-CORE.md#a-continuing-persona) and [contracts](CONTRACTS.md#every-persona-invocation) | M05; M08; M18; B01–B04; B10 |
| MEM-01 | Distinguish persona-defining prompt parts from separately attributable supporting histories, messages, tool-use records, definitions, reusable skills, scripts, code, data, and evidence. Every persona request includes current work, needed context, maintenance responsibilities for both fragments and resources, and an explicit requirement to decide next context. Every valid response explicitly addresses maintenance and next context for both scopes. Neither an edit nor a new search is compulsory. | [Persona core](../design/PERSONA-CORE.md#fragments-are-reusable-prompt-parts) and [contracts](CONTRACTS.md#every-persona-invocation) | M08–M10; B09 |
| MEM-02 | Keep prompt parts and supporting resources useful and compact while preserving their different roles. Maintenance proposals identify intended storage targets or references, applicable base versions, and useful search or regex cues. Preserve characteristic meaning, scope, counterevidence, provenance, qualifications and warnings. Record actual edits or reasoned no_change, blocked or deferred outcomes. Reorganization and deletion must report their actual effects on retained evidence; metadata does not impose a mutation permission gate or storage quota. | [Persona core](../design/PERSONA-CORE.md#maintenance-correction-and-continuity) and [contracts](CONTRACTS.md#every-persona-invocation) | M08; M11; M16; M21; M23; B09 |
| MEM-03 | The current primary persona explicitly decides next-context disposition for fragments and supporting resources in every accepted response. Preserve or no optional need requires no search. When useful, request selective lexical or regex discovery, or known exact references. Keep the bulk tool and skill catalogue outside choosing-model and provider requests. Query scope, pages and reads follow persona intent without application fanout, exposure or cumulative quotas. Matches remain candidates; qualifications and exact references retain their distinct meanings. | [Persona core](../design/PERSONA-CORE.md#the-primary-llm-chooses-next-context) and [contracts](CONTRACTS.md#search-and-exact-reading) | M08; M11; M15; M23; B09; B12 |
| MEM-04 | Assemble relevant character, current need, consequential observations, obligations and complete qualifications faithfully. The persona selects useful schemas and history without an application fitting quota or silent loss of valid selections. Record actual provider context rejection or unavailable material and let a fresh ordinary decision address it when possible. | [Persona core](../design/PERSONA-CORE.md#bounded-and-faithful-assembly) and [contracts](CONTRACTS.md#primary-persona-next-context-selection) | M08; M15; M21 |
| MEM-05 | Measure how experience changes characteristic context and behavior, and how those changes affect later experience. Examine transfer within its evidenced limits, correction, navigation quality, harmful drift, and total maintenance and persona-state cost. Recall scores, calendar age, storage growth, accepted edits, and praise do not establish the intended persona or improvement. | [Persona core](../design/PERSONA-CORE.md) | B01–B04; B07; B09–B10 |

**Needs and cooperation.** Preserve the originating need whether a human or a persona raises it. Cooperation may serve a task or arise without one; responsibility still requires actual acceptance.

| ID | Required behavior | Detailed design | Evidence references |
|---|---|---|---|
| NED-01 | Preserve original intent and authorized changes to the mandate. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M20; B11–B12 |
| NED-02 | Obtain acceptance of continuation responsibility and expose gaps in ownership. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M19 |
| NED-03 | Keep conditional assumptions distinct from confirmed facts. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M20 |
| NED-04 | Check whether the covered scope satisfies the original need. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B11–B12; omitted-outcome fixture |
| COL-01 | Preserve individual agendas, an unranked shared board, and accepted commitments. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B01–B04 |
| COL-02 | Keep offers, membership, responsibility, and actual contribution separate. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M06; M18–M19 |
| COL-03 | Preserve endorsements of exact agreements, along with dissent. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B02–B03; X01 |
| COL-04 | Preserve consequential feedback and make the persona’s handling or unresolved status attributable. Pending bookkeeping alone is neither an adopted blocker nor a closure or retirement prerequisite; an account does not prove compliance, acceptance or completion. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M21; B05 |
| COL-05 | Support provisional interfaces and persona-directed iteration, with actual dependencies, feedback and remaining uncertainty visible. Do not impose an iteration allowance. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M22 |
| COL-06 | Permit useful persona creation and the choice not to create one. Record actual origin, initialization and resource use without population or birth quotas; creation establishes neither competence nor accepted responsibility. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M05–M07; B08 |

**Actions and accountability.** Finding a resource, selecting an interface, performing an action and observing its result are separate facts. Actual resource accounting covers the work needed to reach and maintain a decision as well as the final action.

| ID | Required behavior | Detailed design | Evidence references |
|---|---|---|---|
| ACT-01 | Distinguish discovery, exact reading, primary selection, actual loading or exposure, invocation and observation of results. These meanings do not require six separate calls. Stored instructions or code establish neither current availability nor actual execution. A known current interface permits direct use without a separate application grant or compulsory guide-selection ritual. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md#capabilities-and-the-execution-boundary) and [contracts](CONTRACTS.md#capabilities-and-actions) | M08–M10; M12; M15; B11–B12 |
| ACT-02 | Bind actual execution to its actor, work, current decision, exact inputs and observed results. Default host execution uses the host account and environment without application sandboxing, allowlists, per-tool grants or approval. Report unavailable host or provider facilities honestly. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M12 |
| ACT-03 | Require a complete, valid persona response before adopting new actions. Require actual prerequisite results before dependent decisions and publication. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) and [contracts](CONTRACTS.md#every-persona-invocation) | M17; M26 |
| ACT-04 | Keep unknown external effects explicit and reconcile them before repeating the action. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M13 |
| GOV-01 | Preserve actual authorship, current decision identity, accepted work and the account or destination used for an effect. Historical grants and source policies remain attributable records, not application access, sharing or execution gates. External credential failures and unavailable facilities remain actual observations. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M05–M07; M11–M13 |
| GOV-02 | Measure resources across descendants, every-call maintenance, discovery, scans, reads, schemas, retained context, provider attempts, retries, compaction, review and storage. Include fragments, supporting resources, archives, versions, dependencies, provenance, qualifications, warnings, caches, external backing and peak rewrite copies. Minimize unnecessary work through persona choices and useful organization, without request, episode, corpus or storage quotas. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md#resource-conservation-and-protected-closeout) and [contracts](CONTRACTS.md#authority-resources-and-stopping) | M07; M08; M15; M23; B09; B12 |
| GOV-03 | Keep review, repair, delivery and honest closeout available without reserved-capacity admission gates. Record actual resource failures and incomplete work; a failed operation does not discharge the remaining responsibility. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M23 |
| GOV-04 | Let personas choose useful task work, social activity, reflection, maintenance and continuation without idle, retry or no-progress quotas. Preserve explicit waits, pauses and stops. A recorded outcome alone does not invent a persona decision or automatic reflection call. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M25 |

**Evidence and system behavior.** Records must distinguish what was intended, what was actually supplied or performed, and what the evidence supports. Recovery must preserve these distinctions and current authority.

| ID | Required behavior | Detailed design | Evidence references |
|---|---|---|---|
| EVD-01 | Preserve exact artifacts, mappings of inputs and dependencies, and evidence of actual execution and results. Record selected content and callable definitions separately from what was actually supplied. Host storage, provider transport, and model-visible context are different observations. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) and [contracts](CONTRACTS.md#capabilities-and-actions) | M08–M10; M15 |
| EVD-02 | Review the exact scope under an explicit policy for reviewer independence. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B05; B11 |
| EVD-03 | Keep a historical verdict separate from its current applicability. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M09; M24 |
| EVD-04 | Seal one coherent reviewed state, with no unresolved applicable blockers. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M21; M24 |
| EVD-05 | Report activity, coverage, evidence, acceptance, and outside validation separately. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M14; B11–B12 |
| SYS-01 | Make invocation, maintenance, next-context, and operation dispositions attributable and safe to retry without duplicating accepted transitions. Never invent persona outcomes for failed, refused, or canceled calls. | [Contracts](CONTRACTS.md) | M01–M04; M13 |
| SYS-02 | Restore pending events, maintenance dispositions, adopted deferrals, continuing accepted warnings, reservations, and effects without creating new authority. An expired or unknown old action or invocation identity must never become fresh unsent work or authority to replay. | [Contracts](CONTRACTS.md#recovery-privacy-and-retention) | M04; M13; M16; M26 |
| SYS-03 | Prevent invalid responses and stale holders of decision or write authority from adopting changes. Resolve requests to adopt character changes before other fresh operations in the same response. Preserve explicit dependencies, freshness requirements, and accepted-character fences. | [Contracts](CONTRACTS.md) | M02–M03 |
| SYS-04 | Use direct provider interfaces with explicit model, effort, account and actual transport behavior. Preserve persona identity and report usage, schema expansion, supplied context, failures and unsupported guarantees. Do not add application attempt, context or continuation quotas, silent fallback or automatic uncertain replay. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md#inference-and-bounded-working-context) | M15; B10 |

**Society, interfaces, and conditional extensions.** Preserve the relevant responsibilities and observations when these features or effects are used. Public claims must remain tied to their evidence and evaluator version.

| ID | Required behavior | Detailed design | Evidence references |
|---|---|---|---|
| SOC-01 | For institutional arrangements actually used, retain adopted agreements and real human or institutional accountability. Emergent interaction and ordinary collaboration need no charter or institutional approval prerequisite. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | X01–X03 |
| SOC-02 | Distinguish real stakeholder input from simulated perspectives. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | X01 |
| SOC-03 | Preserve contextual evidence and revisable interpretations of human or peer relationships. Praise is not truth, familiarity is not acceptance, and no universal trust or popularity score replaces judgment. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B02–B04; B09; X01 |
| UX-01 | Present clear status linked to evidence, with meaningful controls. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M14 |
| UX-02 | Preserve attribution and exact retained evidence across fragments, assets, metadata, caches, views and derivatives. Keep erasure, retirement and unavailable evidence distinct. Remove application access and retention quotas; do not delete delivered user artifacts to satisfy an internal cap or promise control over arbitrary outside copies. | [Persona core](../design/PERSONA-CORE.md#compact-retention-and-honest-forgetting) and [contracts](CONTRACTS.md#recovery-privacy-and-retention) | M11; M16; M23 |
| SRV-01 | Make ongoing triggers, renewal, escalation, continuation and stopping explicit and attributable. Report actual activity and preserve persona choices without application trigger, duration or renewal quotas. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B12; X04 |
| PHY-01 | For actual physical effects, identify the interface, observations, commands, overrides and unresolved outcomes. Removing application safety gates does not establish physical execution, correctness or assurance; external device behavior remains evidence to observe. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | X05 |
| OSS-01 | Version the design, evaluators, and public claims without rewriting failures. | [Contribution guide](../CONTRIBUTING.md) | M16; X06 |

## What the persona-core refinement requires

The requirements describe one coherent persona account. They do not establish parallel identity, graph, and reflection systems. The explanations below show what the current criteria require observers to distinguish. Changed criteria need fresh evidence under the current evaluator revision.

**Character and own voice — PER-01–PER-03, PER-05.** The normal beginning does not require a pre-existing self. An initial LLM invocation turns an attributed semantic trait/VAD seed into candidate characteristic fragments. Coherent acceptance establishes the starting account. The continuing primary LLM then authors self-harmonization and evolution. Imported beginnings retain their actual origins.

The persona comprises characteristic context, LLM reasoning, behavior, and revision. It has one stable-character account, and its reasoning model also brings learned tendencies. Harmonization may retain useful conditional tensions or reach an honest no-change decision. It must preserve unresolved contradictions and actual authorship; coherent acceptance establishes which character is current. Neither generated starting material nor supplied ideas establish firsthand experience or behavioral benefit.

**Every-invocation maintenance — MEM-01–MEM-02, ACT-03, SYS-01–SYS-03, GOV-02–GOV-04.** Each persona invocation combines work with decisions about maintenance and next context. This applies to initialization, retrieval-only judgment, ordinary work, communication, coordination, reflection, repair, and persona-capable subcalls.

Each such invocation receives current work, needed characteristic and supporting context, maintenance input for both fragments and supporting assets, and a mandatory next-context decision requirement. A complete, valid response explicitly states next-context intent for both scopes and gives an unambiguous maintenance outcome covering both. One concise, reasoned no-change outcome can cover both maintenance scopes.

Keep these cases distinct:

- **Proposal:** name the intended files, paths, or references and useful discovery cues. A proposal does not establish that anything was stored.
- **Preserve:** an explicit next-context preserve decision retains only appropriate, still-valid scope.
- **Omission:** missing next-context intent makes the response invalid. Recovery may preserve prior state, but that is not an authored choice or renewal.
- **Repair:** a fresh ordinary persona decision can choose useful work, maintenance and context. Historical restricted-repair modes do not impose current action or repair quotas.
- **Failure:** a failed call has no invented maintenance or next-context outcome.

**Maturation through work and surroundings — MEM-01–MEM-02, MEM-05, ACT-01.** Development comes from purposeful revision in response to actual consequences. Task, tool, environmental, human, peer, and self-observed consequences can change how prompt parts shape later approaches, relationships, and navigation habits. Supporting records establish what was experienced; fragments express the persona’s approach informed by that experience.

Evidence must trace an accepted revision through the exact material supplied later, the observed behavior, and its assessed consequences. Stable-trait revision is optional, attributable and coherently adopted. Maturation is not automatic aging, weight training, or guaranteed improvement. Useful change, reasoned no_change, and explicit blocked or deferred outcomes remain valid; later behavior may also reveal regression.

**Self-organization and next context — MEM-02–MEM-04, SYS-01–SYS-04, UX-01–UX-02.** The primary LLM organizes and selects context through ordinary files and separately organized supporting resources. It authors useful literal-search and regex cues, exact references, and optional indexes. These do not require a fixed folder structure or a separate semantic selector.

Discovery begins with useful current context and a usable navigation interface. The complete tool, skill or namespace catalogue stays outside both the choosing model’s context and its provider request. The current primary chooses query scope and exact next material without cumulative search, read, context or cost quotas. Known references need no rediscovery. Compactness comes from relevant selection and maintenance, not truncating valid choices to a fixed allowance.

Search matches remain candidates. The host must not follow associations automatically, execute cues, or choose semantic substitutes. Actual supply must include required guidance and complete operative qualifications. Executable, provenance, and data dependencies do not automatically require their full bodies in the prompt. These distinctions preserve both faithful and selective context.

**Relationships and cooperation — COL-01–COL-04, SOC-03.** Characteristic context informs all discretionary communication, collaboration, and coordination, without host role routing. Actual exchanges may revise one persona’s interpretation of another; that interpretation need not be reciprocal.

Keep praise, factual support, consent, competence, and accepted responsibility separate. A useful encounter may change later work without creating a universal reputation score or committing a peer that has not accepted responsibility.

**Skills and tools — ACT-01–ACT-04, EVD-01, MEM-05.** A characteristic approach is different from a supporting procedure, skill, callable interface definition (schema), or code asset. Purpose determines the distinction, regardless of authorship. First-person wording does not turn an asset into a persona-defining fragment.

Discovery, reading, selection, loading or exposure, invocation, and observation have different meanings, but need not occur in separate calls. An already supplied, current, complete interface can support immediate action. Finding or storing a resource alone does not establish readiness for the proposed operation. Storage, installation, current availability, the actual account, exact executable and dependency bindings, and observed outcomes need separate evidence. Historical grant records do not add an application execution gate.

Both candidate metadata and real callable schemas consume context. Account for provider expansion and accumulated history as they actually occur; an intended selection does not prove what was exposed.

**Correction and continuity — PER-04, MEM-02–MEM-04, EVD-03, SYS-01–SYS-04.** Correction must preserve an honest account of the past and a valid basis for the next operation. Retained exact history and the character under which material was authored remain attributable with their actual retained or unavailable status. Missing evidence remains unavailable. Conflicting old character guidance must be qualified, revised, retired, or left unselected.

An invalid response and a later conflict when storing an accepted change are different failures. A failed whole-response atomic adoption commits none of its proposed operations; later persona work needs a fresh decision. Separately accepted independent units and already dispatched effects retain their actual outcomes. Independence requires explicit dependencies and a coherent accepted unit, as described in the [persistence contract](CONTRACTS.md#complete-response-persistence-and-dependent-work). Resolve character-adoption requests before other fresh operations in the same response:

- **Accepted change:** apply the accepted-character freshness fence before further fresh operations, including reads and waits.
- **Definite no character commit:** only independent work in a separately valid accepted unit may proceed. This does not partially commit a failed whole-response adoption.
- **Unknown commit status:** hold further fresh operations while that uncertainty remains.

Investigating a possible character change is not itself adoption, and a transient affect annotation is not automatically a stable-character revision. Restarting or changing models neither erases obligations nor revives withdrawn information.

**Correction effort and applicability — MEM-02–MEM-04, SYS-02, GOV-04, UX-02.** Stopping correction work does not resolve a separately accepted, primary-authored warning about exact guidance or identified uses. The warning can remain applicable after the repair effort ends.

Failed patches must not restore that guidance without its qualification. Durable warning acceptance and justified resolution remain distinct from the correction attempt. Warnings preserve qualifications about exact material; they do not impose an access gate. Difficulty or stopping does not invent resolution or a character change.

**Character-shaped quality — PER-03, MEM-01, MEM-05, EVD-02–EVD-05.** [UR-049](../USER-REQUIREMENTS.md#quality-through-characteristic-judgment) is governed by the [fragment and asset distinction](../design/PERSONA-CORE.md#fragments-are-reusable-prompt-parts), [maturation evidence](../design/PERSONA-CORE.md#maturation-within-every-primary-interaction), and [persona judgment](../design/WORK-AND-BOUNDARIES.md#persona-judgment-and-independent-qualification). Voice, behavioral dispositions, and standards belong to characteristic fragments; knowledge and procedural guides remain assets. Trace actual critique, disagreement, response, revision or reasoned retention, and acceptance under adopted decision rights. Objective checks support that reasoning; an externally hardcoded quality score cannot replace it. B03–B05 and B09 examine the corresponding behavior and distinguish asset reuse from character maturation.

**Individual and collective sufficiency — NED-03–NED-04, GOV-02–GOV-04, EVD-02–EVD-05, UX-02.** A judgment that enough has been done must come from the persona or group holding the actual adopted decision rights. [Persona-owned sufficiency judgments](../design/WORK-AND-BOUNDARIES.md#individual-and-shared-sufficiency-judgments) preserve dissent and required gaps. Individual and collective judgments remain distinct.

Current completion, delivery, acceptance, and later persona-chosen improvement are separate states. Existing B02–B05/B07/B12 and M19/M20/M25/M26 refinements examine these distinctions.

**Continuing pursuit and clarification — NED-01–NED-04, GOV-02–GOV-04, SYS-02, EVD-02–EVD-05, UX-02.** Ending a local work period does not by itself complete the continuing goal. [Local stop versus continuing goal](../design/WORK-AND-BOUNDARIES.md#continuing-a-goal-across-local-boundaries) requires an accountable continuation opportunity, block, or ending. Resumed work needs a current attributable decision, without an application funding prerequisite.

Ordinary unanswered preferences permit disclosed, revisable progress. An actual unresolved commitment, dependency or missing evidence still limits the claim it can support; an unanswered preference does not become an application approval gate. M19/M20/M25/M26 and B07/B12 refinements distinguish a mechanism being ready, continuation being useful, and completion being justified.

**Useful work and actual cost — NED-01–NED-04, MEM-02, MEM-05, GOV-01–GOV-04, EVD-02–EVD-05, UX-02.** Assess context composition, characteristic behavior, usefulness, harmful omission, task quality, and total cost together. A compact final prompt alone cannot establish useful or efficient work.

Measure every call and the whole episode. Include bootstrap, failed navigation, exact reads, schemas, reloads, continuing history, and maintenance. Distinguish the host registry, provider transport, model context, prompt-part corpus, and managed state. Retained supporting resources, dependency caches, data snapshots, archives, provenance, warnings, and peak copies all count toward the applicable footprint.

Unavailable evidence may leave a fallible attributed interpretation, not restored observations or a new decision. Report actual provider or storage failures and retain their uncertainty. No application retention or capacity quota blocks admission or silently discards valid selections. Delivered user artifacts and arbitrary outside copies retain their actual ownership and disposition; an internal cleanup cannot claim to erase outside copies.

These refinements introduce neither a new requirement family nor a fixed cognitive taxonomy. Every complete, valid persona response needs explicit maintenance input and an explicit outcome covering both fragments and supporting resources. A single reasoned no_change suffices when its scope is clear and no useful change is warranted. Silent maintenance omission is invalid. An edit, a new selection, a separate reflection call, and numeric trait scores are not compulsory.

Keep the evidence chain explicit: a proposal with an intended storage target, an accepted save, actual later supply, an observed action, and measured benefit are different claims. Deterministic factual recording cannot invent history or turn old messages into new authority. Maintenance does not replace required work or stopping dispositions. Failed or refused calls cannot be filled in afterward with invented persona judgments.

## Applying and reporting the requirements

For each applicable row, record who or what enforces it, the supported scope, implementation state, exact evidence, unobserved behavior, and any unresolved deployment decision. Report the following statuses separately:

- **Design conformance:** the documented implementation responsibilities cover the rule without contradiction.
- **Mechanism evidence:** actual operations establish the reported state transition, supply or effect within their observed scope.
- **Behavioral evidence:** observed persona work supports a scoped claim about choices, maturation, cooperation, or utility.
- **Deployment state:** identify the actual configuration, enabled facilities, observed behavior and unresolved work. This is an evidence account, not an approval prerequisite.

A feature may be marked not applicable because it is disabled only if it is genuinely unavailable and its absence does not remove an obligation incurred by other enabled work. Missing evidence means unassessed or not run, never passed. The [status ledger](STATUS.md) states what this documentation revision does and does not establish.

Historical DLV identifiers, supplemental D/FP/FR scenario labels, and earlier evaluator revisions remain mapped in [evaluation history](../evaluation/HISTORICAL-RESULTS.md). Changed criteria require a new versioned result. An old outcome never silently inherits this edition’s interpretation.
