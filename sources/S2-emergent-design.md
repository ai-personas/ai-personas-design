# AI Personas: Emergent Work, Priorities, Teams, and Learning

**Design proposal — 16 September 2026**  
**Status:** proposed architecture and acceptance contract, not a claim of a completed implementation or successful house-design run.

## Executive decision

AI Personas should be a persistent, event-driven community of personas that can interpret a need, discover missing obligations and useful improvements, choose priorities, make commitments, acquire capabilities, recruit or birth other personas, produce real outcomes, test those outcomes, and retain useful learning.

The person supplies the need and the boundaries. Personas supply the evolving understanding, methods, organization, and work. The runtime supplies durable state, authority, resource accounting, isolation, delivery, and evidence integrity.

The product is neither a fixed workflow with fictional role labels nor an unrestricted conversation among agents. It is **persona-authored work organization on a mechanically reliable substrate**.

Domain-independent support is an architectural objective. It is not a guarantee that every model, team, toolset, or budget can solve every request. A capable system must also preserve a useful partial result, identify an unsolved question, obtain outside help, or report a genuine boundary without inventing completion.

## 1. Source baseline and limits

The attached `deep-research-report (1).md` is the primary prior proposal. Its useful foundations are continuing personas, OCEAN/VAD, ordinary environments/work, fragments, acquired tools, immutable artifacts, independent review, and domain-neutral execution. Its five leading changes emphasize provider transport, fragments, tool evidence, context, and authorization. Those remain useful, but they are insufficient as a complete account of emergent prioritization, team formation, and demonstrated improvement. [S1]

Fresh repository reads establish that the code bases must not be conflated:

| Basis | What was inspected | Consequence |
|---|---|---|
| `rewrite/design-first` | Rust `src/contract.rs` and the beginning of `src/runtime.rs` | This branch exposes generic commands and fresh identity creation. The inspected runtime still imports and defaults to `Codex`. |
| Current `main` | Snapshot `1fc89cd389629877eb1b6b41b7b8b612fc1c7979`; architecture, release checkpoint, birth records, and the beginning of the population lane | This is the Python PersonaOS implementation. It already has persona-authored birth, signed causal bindings, invitations/consent, serialized persona mailboxes, acquired capabilities, and inherited execution funding. |
| Historical live evidence | `docs/EMERGENCE_SIMPLIFICATION_2026-09-11.md` and `docs/RELEASE_CHECKPOINT.md` | These documents distinguish working mechanics from undemonstrated learning/cooperation. They are repository reports, not experiments independently repeated for this proposal. |

The September 11 report describes overlapping drafts and review requests without completed independent snapshot review or demonstrated feedback-to-edit cooperation. It also reports a corrected action mistake recurring in later work without retained procedural learning. The September 13 checkpoint reports that fragments appeared in later contexts while useful transfer remained unproved and engineering gates remained locked. [S2–S7]

Therefore, do not rebuild mechanisms already present in `main`, and do not apply the attachment's Rust patch list to Python `main`. First declare the implementation baseline. The recommendations below primarily target the current architecture's behavioral and evidence gaps, with a separate mapping for the Rust branch.

## 2. What must be emergent

Emergence has six observable meanings here:

1. **Understanding:** personas discover relevant needs, constraints, uncertainties, and omissions that were not listed individually by the user.
2. **Improvement:** personas propose changes that improve the user's actual outcome, not just the originally imagined artifact.
3. **Priorities:** personas decide what matters next and change that ordering when evidence changes.
4. **Organization:** responsibilities, leadership, collaboration topology, and team membership arise from the work.
5. **Population:** personas can create new continuing identities when justified within authorized bounds.
6. **Learning:** experience changes later behavior in a useful, demonstrable way.

These are measured behaviors, not names for additional services. A persona is not emergent merely because it has a generated name, random traits, or a prompt saying “expert.”

A newborn is also not a blank intelligence. Its behavior depends on its model, protocol, authorized seed context, and later experiences. The design should expose those dependencies, not invent a biography or competence that never occurred.

Research on generative agents supports memory, reflection, and planning as mechanisms for emergent social behavior; it does not establish engineering competence. Controlled multi-agent research also shows that architecture and task structure affect whether collaboration helps or hurts. These findings motivate explicit evaluation rather than a presumption that more personas are better. [R1, R2]

## 3. Architecture: three layers, one event path

```text
Person's need + constraints + delegation
                  |
                  v
       Versioned work mandate
                  |
      observations / proposals / commitments
                  |
      Continuing persona actors <--> peers / newborns
                  |
          choices and tool requests
                  |
      Mechanical execution boundary
                  |
     Real outputs, effects, and observations
                  |
        Review, revision, and learning
                  +----------------------> next decision
```

### Persona judgment

Personas interpret observations, identify candidate outcomes, select work, propose improvements, learn, choose tools and models, and decide whether to recruit or birth a peer. A persona may temporarily coordinate a project or review a result. Neither responsibility becomes a permanent runtime profession.

### Shared work state

Use the existing durable work records, immutable versions, and lineage store. Add only the missing typed relationships and projections. A “work graph” means indexed relationships among these records, not a new graph database or planning engine.

### Mechanical substrate

The substrate authenticates commands, checks revisions and permissions, reserves resources, serializes each persona's decisions, runs isolated jobs, preserves exact bytes, delivers events, and invalidates evidence whose declared inputs changed.

It must not decide that a house requires a particular profession, that a high-openness persona should use a particular application, or that a particular discipline must run first.

**Planning belongs to personas. Scheduling belongs to the runtime.** Refusing a fixed task planner does not remove the need for queues, resource arbitration, recovery, or fair delivery.

## 4. Evolving work without losing the person's intent

### 4.1 The mandate

Every work item retains a versioned mandate containing the original request, accepted clarifications, desired outcomes, hard constraints, preferences, unresolved questions, permitted actions, resource ceilings, and the current completion agreement.

Not every interaction needs a large document. “Rewrite this sentence” may use a tiny mandate and finish in one turn. A multidisciplinary design needs more explicit state because its consequences and dependencies are larger.

Represent three levels separately:

| Level | Meaning | Who may change it? |
|---|---|---|
| User intent and constraints | What the person asked for and authorized | The person or an explicitly delegated authority |
| Adopted interpretation | Necessary obligations and methods inferred for the agreed result | Personas within their delegation; material changes remain reviewable |
| Candidate improvements | Optional ways to increase value | Anyone may propose; adoption requires the appropriate scope/cost authority |

For a coordinated house design, checking services is an inferred obligation. Adding a pool is an optional scope expansion. Removing a bedroom contradicts the user requirement unless the person explicitly changes it.

The team can challenge an apparently impossible or contradictory brief and present alternatives. It cannot silently weaken the brief to make its own output pass.

### 4.2 The opportunity record

Personas can record a candidate improvement at any time. Its generic structure is:

```text
Observation and exact evidence
Affected outcome or constraint
Proposed change
Expected benefit and possible regressions
Uncertainty / competing explanations
Cheap discriminating check or experiment
Estimated resources, with unknowns preserved
Dependencies and affected people
Adoption authority
Stop or revisit condition
```

The record is a hypothesis, not a result. “May reduce plumbing complexity” becomes an improvement only after an appropriate comparison and review.

Statuses can be `proposed`, `exploring`, `adopted`, `rejected`, `deferred`, or `superseded`. These are generic lifecycle states, not domain stages.

### 4.3 Scope control

Low-risk, reversible exploration inside the agreed allowance should not require a human click for every action. Increasing spend, changing a hard constraint, publishing externally, or operating physical machinery requires the corresponding authority.

Keep a baseline submission available while exploring improvements. Optional enhancement must not erase the last useful result or prevent delivery indefinitely.

## 5. Prioritization: an evolving choice, not a hard-coded score

A work item has an **attention frontier**: its current, bounded set of useful candidate actions. This is a view over proposals, commitments, review findings, questions, and deadlines—not another engine.

Personas first distinguish eligible actions from actions blocked by missing authority, resource limits, incompatible constraints, unresolved required inputs, or exclusive write ownership.

Among eligible actions, they compare the consequences of acting now versus waiting. The judgment should consider user importance, credible safety concerns, time sensitivity, downstream work unlocked, uncertainty reduced, expected improvement, reversibility, cost, and coordination overhead. These considerations are not a universal numerical formula and do not imply that uncertain estimates are calibrated probabilities.

Each material priority decision records:

```text
Chosen action
Other serious candidates considered
Why this is next
Expected observable result
Resource/timebox allowance
What evidence would change the choice
```

For small actions, this can be a short field on the commitment rather than an extra model call. Do not make every turn perform a planning, voting, and reflection ritual.

### Reprioritization

Reconsider the frontier when the user changes a constraint, an experiment fails, a required input arrives, a reviewer identifies a blocker, a tool becomes unavailable, a deadline approaches, or the budget changes.

Do not broadcast every event to every persona. Maintain persona-authored subscriptions and addressed messages; batch low-value notifications. The substrate must still deliver authoritative cancellations and permission changes regardless of a persona's preferred subscriptions.

### Disagreement

Personas may run a small comparative experiment, preserve alternatives, or ask the person about an unresolved value preference. A delegated commitment owner can choose reversible implementation details within its scope. Broader authority is never gained merely by speaking more often or creating more supporters.

No majority vote can make a physical claim true. No number of newborns can expand an authority grant.

### Progress and liveness

Reward neither activity volume nor a large persona population. Useful progress includes a checked result, a resolved uncertainty, a valuable rejected alternative, a necessary question, or a reproducible failure diagnosis.

After a bounded interval with no useful state change, return an explicit no-progress observation to the owning personas. They can simplify, change approach, recruit, request help, or stop. The runtime may enforce an agreed resource ceiling; it should not invent the semantic repair.

## 6. Birth, recruitment, identity, and responsibility

The current `main` already has persona-authored causal-need/birth records, idempotent birth identities, lineage, and a separate membership-consent path. Preserve these. Link their work-facing explanations to the relevant observation, opportunity, or commitment rather than replacing the birth protocol. [S5, S6]

### 6.1 Birth as a work decision

A useful birth proposal explains what another continuing perspective could contribute, what evidence motivates it, what resources are available, and how its usefulness will be checked.

Personas should consider alternatives such as learning the missing technique themselves, consulting an existing peer, using a tool, narrowing the question, or recruiting an outside expert. This is guidance for judgment, not a mandatory host-enforced recruitment ladder.

Different labels on the same model do not manufacture new knowledge. A new identity may help through independent context, parallel exploration, a different acquired tool, a different allowed model, or durable ownership of a developing interest. Those hypotheses need evidence.

### 6.2 Lifecycle

```text
Persona authors a birth proposal
  -> runtime checks exact lineage, authority, capacity, and funding
  -> distinct identity materialized and provenance retained
  -> newborn receives a birth wake
  -> newborn authors/revises its identity and selects its working context
  -> invitation and acceptance establish membership
  -> newborn accepts, negotiates, or declines a commitment
  -> work produces evidence of usefulness or a documented limitation
  -> persona remains available, becomes dormant, or takes other authorized work
```

There is no requirement that a persona immediately generate an avatar, invent a detailed personality, or pass a profession-specific ceremony before contributing. Character should develop through authored choices and retained experience.

### 6.3 Mechanical bounds

Root authorization must cover all descendants, messages, model calls, compactions, installations, paid tools, and reviews. Birth does not mint a fresh allowance. Admission must be atomic under concurrent proposals, retry-safe, and causally bound to the original work.

A deployment can specify active-persona, total-population, rate, and depth ceilings. These are operator-chosen operational limits, not runtime guesses about the ideal organization. Within an existing delegation, routine births need no separate human approval. New or broader authority does.

The system must reserve enough of the granted resources to initialize a birth it admits. It must not create an unlimited backlog of unfunded runnable children.

Call, token, wall-time, tool, and monetary budgets are distinct. A currency cap is enforceable only where trusted pricing/upper bounds and execution control exist. Unknown prices must remain unknown; a model-call allowance is not a dollar guarantee.

### 6.4 Identity versus role

The persona owns continuing identity, character, relationships, fragments, preferences, and provenance. A commitment owns its current responsibility and deliverable. A persona born during house work must be able to learn something else later.

Inherited fragments retain original ownership and evidence. Their receipt is not the newborn's own experience. Private fragments and credentials do not become birth material by default.

A newborn may be a valid independent reviewer only under the review policy for the exact contribution. Shared ancestry or model choice does not automatically disqualify it, but neither does a new identity prove statistical independence. Record the relevant relationships and distinguish independent execution from independent reasoning evidence.

## 7. Accomplishment and coordination

A commitment binds an owner to a defined outcome, an agreed criterion, exact input revisions, dependencies, resource allowance, status, and evidence. An offer must be accepted before it becomes someone else's obligation.

Only shared writes need a single-writer lease or equivalent conflict control. Independent modeling, research, and experiments may run concurrently. Use private branches/workspaces for alternatives and explicit adoption of the chosen revision; do not lock an entire environment for all work.

Each persona's decisions remain serialized, while its long-running jobs can complete asynchronously. Lease expiry and owner departure produce visible handoff events rather than lost work. Replayable mailboxes and an outbox prevent a committed state change from losing its corresponding notification.

For a deliverable to be counted as accomplished, preserve the chain:

```text
Accepted outcome / criterion
  -> accepted commitment
  -> exact input versions
  -> actual execution or observation
  -> immutable result
  -> claim-specific evidence and review
  -> current outcome disposition
```

A successful command establishes what the command returned. A signature establishes integrity/authorship. Neither by itself establishes design correctness, usefulness, or user acceptance.

### Validation in ordinary work

The attachment correctly rejects house-specific validator logic in the kernel. It should not be interpreted as banning domain validators from normal production work. Personas must be able to discover, acquire, execute, and review appropriate checkers and simulations through generic capabilities. Independent acceptance fixtures remain separate from learner control.

Persona-authored criteria are proposals until adopted through the work's authority policy. A team must not edit the accepted criteria after seeing a failing result merely to obtain a pass. Criteria revisions are explicit, attributed, and keep earlier failures visible.

### Change impact

Artifact and evidence records reference immutable input hashes or version IDs. A new canonical input revision does not erase the old review; it makes that review inapplicable to the new claim. Mark dependent evidence `stale` and notify affected owners.

Where declared dependencies are incomplete, conservative revalidation is required. Mechanical dependency tracking cannot discover a forgotten physical relationship on its own.

### Completion is multidimensional

Keep separate facts for execution activity, obligation coverage, current submission, validation, user acceptance, outstanding outside checks, and further optional improvements.

An episodic task can finish with a useful result and optional improvements deferred. An ongoing need can remain active under authorized triggers. An exploratory or subjective need can conclude through explicit user judgment rather than a fictitious machine-verifiable truth score.

## 8. Complete four-bedroom-house walkthrough

This is a designed acceptance scenario, not an executed house project. The scope incorporates the user's clarification: coordinated architectural/structural/services design, native editable artifacts, and appropriate calculations/simulations. Manufacturing output is included only when the agreed fabrication scope supplies the required process and machine details.

| Moment and observation | Persona-authored priority and organization | Observable accomplishment or limitation |
|---|---|---|
| 1. The brief is underspecified | A small existing group identifies material questions and proposes the deliverable scope; no predefined professions are assigned | Mandate, assumptions, unresolved inputs, and completion agreement |
| 2. Some missing inputs block final claims, but not early exploration | Separate reversible layout exploration from work needing site, utility, climate, or other authoritative inputs | Parallel bounded exploration and specific external requests; no invented facts |
| 3. Early layouts compete | One persona takes spatial modeling; another examines feasibility and missing requirements. They compare genuine alternatives before polishing | Native baseline model, dimensional checks, reasons for choosing or rejecting alternatives |
| 4. Spatial changes repeatedly depend on thermal and services questions | A persona proposes a new continuing peer to investigate that uncertainty. The runtime checks existing birth authority and funding; the newborn chooses whether to join | Birth provenance, accepted membership, a bounded first commitment—not an unearned “HVAC expert” badge |
| 5. Building systems need actual production work | Responsibilities for structure, plumbing, HVAC, electrical and integration are negotiated. A persona can cover more than one responsibility; further peers are considered only when useful | Native discipline files, calculations, schedules, and explicit ownership |
| 6. Tools must be usable, not merely installed | Personas acquire candidate CAD/BIM, analysis and drawing capabilities, perform representative operations, and inspect the resulting bytes/images | Installation and usage evidence; editable model operation; retained failures and repaired recipes |
| 7. A service route conflicts with a structural element | Coordination repair becomes more valuable than final rendering. Owners compare rerouting, distribution, or architectural alternatives with affected reviews | Resolved issue linked to exact models; rerun affected checks; preserve failed variants |
| 8. A persona notices an unrequested improvement | Propose a shared service zone, more maintainable equipment access, or a different window/shading arrangement. Compare benefits and regressions against the baseline | Tested improvement or informative rejection; no claimed benefit without evidence |
| 9. An adopted window/layout change affects analysis | Thermal/daylight/other dependent results become stale. Personas decide the order of revalidation and dependent equipment updates | New input-bound simulations/calculations; no old result shown as current |
| 10. The team considers fabrication | Determine whether particular parts should have CAM output. Missing manufacturing details block executable machine instructions, not all design work | Fabrication drawings or properly bounded CAM package where supported; physical operation remains separately authorized |
| 11. The integrated submission is ready for assessment | An appropriately independent participant inspects sealed native sources, regenerates selected exports, reruns selected analyses, and checks omitted scope | Version-bound findings; current coordination evidence; outside professional/site checks remain explicitly pending where absent |
| 12. Useful patterns emerge | Personas retain generalizable lessons with applicability limits, such as separating model revisions from analysis evidence | Later changed-house or unrelated-task behavior tests the learning; personas persist beyond this house |

The walkthrough is not a mandatory twelve-stage runtime. The team can loop, overlap work, abandon a poor option, recruit earlier, or postpone a nonblocking improvement. What must persist are the obligations, choices, boundaries, and evidence.

The house outcome is not “four rooms plus attractive pictures.” It is the agreed coordinated package with an honest statement of what has been checked, what remains conditional, and what requires outside review. Nothing here authorizes construction or machinery operation.

## 9. Memory and improvement over time

Preserve three different things:

- **Work state:** the current mandate, commitments, open findings, dependencies, and accepted revisions.
- **Persona fragments:** authored lessons, methods, preferences, interpretations, and experience references.
- **Evidence:** immutable observations and executions supporting or contradicting claims.

A fragment can be useful without being a universal fact. Include sources, applicability, limitations, contrary evidence, supersession, and selection/use references. A failed method is worth retaining when it prevents repetition.

Do not force every event into long-term memory. Do not call fragment count, selection frequency, or a changed trait “learning quality.” Do not mutate OCEAN/VAD to manufacture visible development.

The continuing persona chooses what to remember and retrieve. The context compiler must always preserve an authoritative, bounded view of the current mandate, grants, cancellations, relevant commitments, and unresolved failures. Historical material is loaded just in time, not copied into every prompt. Compaction must retain exact references, and hard context limits must fail safely rather than silently discard authority or current obligations. [R3]

Demonstrated learning requires a later behavioral comparison. Use matched retained-memory versus memory-withheld runs, controlled models/tools/budgets, held-out tasks, repeated cohorts, and blind evaluation where possible. Selection plus success is evidence of use, not causal proof of benefit. Improvements can also come from better tools, model choices, or extra compute; record those separately.

This design adapts context and persistent state. It does not automatically update model weights. Research on context adaptation supports the mechanism as promising; it does not guarantee that these personas will improve on every task. [R4]

## 10. Universal needs, not a house-only framework

| Need | Possible emergent improvements | Appropriate evidence and stopping behavior |
|---|---|---|
| Clean a dataset | Discover schema drift, recoverable missingness, or a useful additional validation | Reproducible transformations, preserved source, held-out checks; finish without birthing a team when unnecessary |
| Build software | Find a hidden compatibility requirement or a simpler architecture | Executable changes and tests; deployment separately authorized |
| Write a story | Discover pacing or continuity problems; explore alternative scenes | Versioned drafts, critique, and the author's preferences; no claim that taste is objectively solved |
| Plan a trip or organize a household need | Surface overlooked constraints, alternatives, and coordination tasks | Current verified information, explicit preferences, booking/communication permission |
| Investigate a scientific question | Discover a more discriminating experiment or a missing assumption | Reproducible procedures, data, uncertainty; a useful negative result can be an accomplishment |
| Provide ongoing service | Notice a relevant event or deteriorating condition | Authorized subscriptions, bounded wakes, intervention rights, periodic human review—not idle token-spending |
| Have a supportive conversation | Notice what the person wants to discuss or clarify | Respectful conversation and user-directed pacing; no unnecessary team, forced optimization, or invented diagnostic authority |

The runtime does not route among these rows. The rows are examples and test fixtures. The same primitives represent the work; domain knowledge comes from models, authorized context, tools, and qualified outside participants.

## 11. Security and recovery are prerequisites for autonomy

Keep acquired tools generic, but do not give arbitrary code ambient host authority. Use isolated filesystems, constrained networking, process/resource controls, private execution state, and credential mediation. The current `main` already documents Linux isolation and restricted assessment execution; preserve those boundaries and test their interaction with delegated network and external-write authority. [S4]

A command declaring itself `read` cannot be trusted to have only read effects. A permitted hostname does not by itself distinguish observation from publishing or data exfiltration. Use an effect-mediating tool/API gateway where possible, bind grants to resources/actions/arguments, and withhold sensitive sessions or external writes where enforceable separation is unavailable.

Untrusted files, package instructions, web pages, tool outputs, and imported fragments must not be able to rewrite the mandate, grants, or reviewer policy. No credentials or privileged parent state should enter a newborn's prompt. Sandboxing needs both filesystem and network boundaries; permission prompts alone are not an adequate design. [R5]

Persist an operation identity and request digest before execution. Reusing an identity with changed arguments is an error. Make internal commits idempotent, and use destination idempotency support for external effects where available. After an ambiguous external failure, record `effect_unknown` and reconcile before retrying. A local transaction cannot promise exactly-once behavior at an arbitrary remote destination. [R6]

Cancellation stops new admissions immediately and attempts to terminate active jobs. It cannot undo already completed external actions. A late result is retained but cannot silently mutate a canceled commitment. Restart recovery must restore mailboxes, reservations, input versions, and incomplete effects without inventing new funding.

## 12. Minimal implementation delta

Do not introduce a profession registry, universal task classifier, domain workflow DSL, separate population optimizer, vector database, or new mandatory planner service. Do not restore a large unused framework merely to obtain one useful record relationship.

### 12.1 Records and relationships

Use the existing authenticated/versioned record machinery. Add typed bodies or typed projections for the following only where equivalent semantics are absent:

```text
WorkMandate
  original_need, accepted_revision, outcomes, constraints, preferences,
  unresolved_inputs, authority_refs, budget_refs, completion_agreement

WorkEntry
  observation | proposal | commitment | decision
  work_id, author, parent_versions, payload, source_refs

EvidenceBinding
  claim_ref, criterion_ref, input_versions, output_versions,
  execution_refs, reviewer_ref, verdict, applicability

BirthWorkLink
  existing_birth_proposal_ref, motivating_entry_refs,
  offered_commitment_ref, later_contribution_refs
```

Index typed relationships such as `depends_on`, `implements`, `tests`, `blocks`, `supersedes`, and `motivates`. Every record remains scoped to its authorized work and readable only through its access rules.

Keep common identity/revision/provenance envelopes and append-only changes. Do not duplicate birth, funding, tool-acquisition, signature, or fragment systems already present.

### 12.2 Operation semantics

The following names describe proposed API semantics; they are not claims about current command names. Map them onto existing actions when equivalent.

| Operation family | Required behavior |
|---|---|
| Work records | Append an observation or proposal; explicitly adopt/reject/defer; revise a mandate only with authority |
| Commitments | Offer, accept, update, hand off, and close against exact criteria/evidence |
| Relationships | Add version-bound dependencies and invalidate applicability on changed inputs |
| Birth | Reuse existing birth proposal/admission/membership protocol; add work-linked explanations and outcome projection |
| Evidence | Preserve execution receipts and independent assessment of exact versions |
| Context | Compile authoritative current state plus persona-selected memories and just-in-time tool schemas |
| Events | Durable addressed delivery, deduplication, trigger subscriptions, and no unfunded idle cognition |

### 12.3 Reference event loop — pseudocode

```python
async def handle_wake(persona_id, wake_id):
    # One decision at a time for an identity; other identities may run.
    async with acquire_persona_lease(persona_id):
        wake = load_authenticated_wake(wake_id)
        state = load_current_authorized_state(persona_id, wake)
        if state.cancelled or not state.funding_available:
            retain_blocked_delivery(wake, state.reason)
            return

        context = compile_current_state_and_selected_memory(state)
        decision = await call_allowed_provider_with_reserved_budget(context)
        proposals = validate_command_shapes(decision)

        for command in proposals:
            # No domain classification, role assignment, or host planning.
            with transaction() as tx:
                prior = lookup_operation(tx, command.id)
                if prior:
                    require_same_request_digest(prior, command)
                    continue
                require_current_authority(tx, command)
                require_expected_revisions(tx, command)
                reserve_declared_resources(tx, command)
                apply_record_mutation_or_enqueue_isolated_job(tx, command)
                append_outbox_events(tx, command)

        # Side effects are dispatched from committed intents, not inside a DB tx.
        # Uncertain external effects are reconciled, not blindly replayed.
```

This is a correctness sketch, not a replacement implementation. Production work must specify durable lease fencing, cancellation races, reservation reconciliation, and external-effect mediation using the actual store and supervisor.

### 12.4 Current-main integration targets

| Existing area | Proposed change or verification |
|---|---|
| `src/personaos/persona_birth.py` | Preserve exact birth identity/provenance; link rationale and contributions through work records rather than a host fitness score |
| `src/personaos/kernel_lanes/population.py` | Preserve causal wake/funding binding; test concurrent admission, retries, unfunded descendants and cancellation; do not mint child budgets |
| Persona actor/supervisor and context carriage | Surface adopted work commitments, latest priority decisions and stale-evidence notifications without broadcasting full history |
| Existing signed work/workspace and assessment paths | Add missing criterion/claim/input bindings, handoff projections, and feedback-to-edit evidence |
| Existing brain/fragment actions | Preserve authored memory; test correction transfer and counterevidence instead of counting writes |
| Existing budget/event budget paths | Present calls/tokens/money distinctly; cover all descendant costs and unknown usage |
| `src/personaos/run_scorecard.py` and UI projection layer | Show outcome coverage, priority changes, useful contribution, current validation, and outside blockers; raw birth counts are not a quality score |
| `integtest` | Add the behavioral campaign below without rewriting historical failures |

These are integration targets and recommended audits, not assertions that every listed function is defective.

For a deliberate Rust implementation, place the corresponding typed operations in `src/contract.rs`, authoritative context and mutations in `src/runtime.rs`, record/index/transaction changes in `src/store.rs`, and isolated execution in `src/jobs.rs`. The inspected Rust branch and current Python implementation require separate patch sets. Do not port the whole Python implementation or assume that changing language solves the behavioral gap.

## 13. UI: show choices, outcomes, and the changing team

The main work view should answer: what outcome are we pursuing; what changed; what is most important now; who committed to what; what is proven; and what needs the person?

Recommended work-level views:

| View | Contents |
|---|---|
| Now & next | Current priority, short reason, expected result, blockers, resources, and candidate improvements |
| Outcomes | Accepted requirements, owners, current artifact revisions, criteria, stale/missing evidence, and omissions |
| People | Continuing identities, current commitments, active/dormant state, birth rationale, lineage, and actual contribution |
| Evidence | Native artifacts, derivation relationships, execution inputs/logs, review findings, and reproduction actions |
| Decisions & learning | Scope changes, adopted/rejected improvements, handoffs, memory revisions and later-use evidence |

Never use “busy,” “has many fragments,” “born as an expert,” or “all agents agree” as a substitute for outcome quality. Show requested approvals separately from unresolved factual questions. Label simulated versus observed results and signed versus technically validated evidence.

The person can edit constraints, pin a priority within their authority, accept or decline a scope change, pause activity, adjust bounded resources, inspect a birth, request a human handoff, or accept a result with clearly stated limitations.

Technical UI requirements: event-watermark replay, scope-specific invalidation, stable operation identities through retries, server-derived authoritative status, lazy native/artifact viewers, thumbnails, bounded lists, keyboard-accessible detail panes, and complete cancellation/disposal on close.

The accompanying HTML is an interactive fixture-based prototype of these views. It runs no personas, models, simulations, or external actions. Its house, dataset, and story rows demonstrate a reusable renderer, not measured product behavior.

## 14. Acceptance campaign and rollout

### 14.1 Mechanical gates

Exercise cross-work isolation; operation ID/payload conflicts; atomic concurrent birth limits; inherited descendant funding; newborn membership consent; cancellation before/after provider completion; owner lease expiry; event replay; artifact-version conflicts; stale-evidence propagation; immutable criteria; secret leakage attempts; network-effect enforcement; and interrupted external effects without blind duplicate execution.

### 14.2 Behavioral gates

| Test | Passing observation |
|---|---|
| Unprompted useful improvement | Persona discovers an opportunity outside the literal checklist, tests it, and produces a better agreed result or a useful rejection |
| Reprioritization | New evidence changes the next commitment; activity does not continue blindly on a now-inferior branch |
| Real cooperation | One persona's evidence changes another's exact artifact revision, and independent review verifies the change |
| Useful birth | Persona-authored birth responds to observed work; the newborn joins by consent and supplies a distinct inspectable contribution |
| Restraint | A simple task completes without unnecessary birth, meetings, installations, or ceremonial memory writing |
| Population recovery | Redundant peers hand off or become dormant without losing commitments or history |
| Learning transfer | Retained learning improves later outcomes against a matched withheld-memory baseline; counterevidence updates erroneous fragments |
| House depth | Coordinated editable architectural/structural/plumbing/HVAC/electrical outputs and appropriate analyses meet the agreed scope |
| Scope discipline | Optional enhancement cannot silently drop a required outcome or exceed delegated resources |
| Domain transfer | Unseen software, data, writing, research, conversation, and ongoing-need fixtures run through the same runtime semantics |
| Honest failure | Missing capability, external evidence, or budget produces a useful bounded result and accurate status, never a fabricated pass |

Use repeated, matched cohorts, actual model IDs/capabilities, recorded usage, and a frozen runtime/schema/UI/fixture revision. Compare a single continuing persona, a fixed-size group, and an adaptive group under the same total resource budget. Separately compare retained versus withheld learning. Do not confuse an extra token budget with an emergence advantage. [R2, R7]

Do not require a birth on every benchmark: that would reward unnecessary population growth. Do not award a pass for fragment selection, tool installation, or signature verification alone. Test the complete causal chain and the accepted outcome.

### 14.3 Implementation order

First preserve and reproduce the smallest failed cooperation/correction case from the repository. Fix the generic missing affordance or state carriage identified by that failure. Then establish a genuine feedback-to-edit-to-review loop and a later retained correction. Next demonstrate adaptive birth and no-birth restraint under conserved funding. Only then expand to multidisciplinary house work, disturbance/revalidation cases, unrelated needs, and fresh-persona repeats.

Build the UI from the same event projections as the tests. Do not add a second UI-specific notion of completion. Preserve all failed evidence and explicitly version any evaluator correction.

The release gate is observable useful emergence at acceptable cost and under enforced authority. No architecture diagram, test count, or successful tool installation can substitute for it.

## 15. Final design statement

**A persona may improve the plan, discover a better method, propose a better outcome, recruit a collaborator, or bring a new identity into existence. It may not silently replace the person's goals, manufacture competence, create new authority, erase a failure, or declare an unchecked artifact complete.**

The runtime does not know how to build a house. It knows how to preserve a person's intent, support continuing identities, carry their decisions, enforce their boundaries, execute their authorized tools, and preserve what actually happened. Domain capability and useful cooperation must then be demonstrated by the personas, not presumed from the architecture.

## Source register

[S1] User attachment, `deep-research-report (1).md`, especially Executive summary, Minimal first-release architecture, House integration test, Integration and acceptance campaign, and UI design.

[S2] `ai-personas/ai-personas`, `rewrite/design-first`, `src/contract.rs` (blob `4aedf3a598725c769ed6c2abb6509c504d3e044e`) and `src/runtime.rs` (blob `137c47fa579f463051b7b9355ba4850b63dc1aeb`), retrieved 16 September 2026. Only inspected ranges support the observations above.

[S3] Current-main snapshot `1fc89cd389629877eb1b6b41b7b8b612fc1c7979`, `README.md` and `docs/ARCHITECTURE.md`, retrieved 16 September 2026. Architecture prose is project documentation, not independently executed proof.

[S4] Same snapshot, `docs/ARCHITECTURE.md`, sections The authority boundary; One event path for work; Code, tools, skills, and MCP.

[S5] Same snapshot, `src/personaos/persona_birth.py`, lines 1–240; and `docs/ARCHITECTURE.md`, Birth, identity, and avatars.

[S6] Same snapshot, `src/personaos/kernel_lanes/population.py`, lines 1–320, particularly `_prepare_persona_wake_for_enqueue`.

[S7] Same snapshot, `docs/EMERGENCE_SIMPLIFICATION_2026-09-11.md` and `docs/RELEASE_CHECKPOINT.md` (checkpoint dated 13 September 2026). Reported outcomes have not been independently rerun for this proposal.

[R1] Park et al., *Generative Agents: Interactive Simulacra of Human Behavior*, arXiv:2304.03442. Evidence concerns emergent simulated behavior, not general engineering qualification.

[R2] Kim et al., *Towards a Science of Scaling Agent Systems*, arXiv:2512.08296v3, revised 8 April 2026. Controlled evaluations show task/coordination-dependent benefits and degradation; this is not a universal performance predictor for AI Personas.

[R3] Anthropic, *Effective context engineering for AI agents*, 29 September 2025. Just-in-time retrieval, finite context, compaction and structured notes.

[R4] Zhang et al., *Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models*, arXiv:2510.04618. Context adaptation without assuming model-weight updates.

[R5] Anthropic, *Beyond permission prompts: making Claude Code more secure and autonomous*, 20 October 2025. Filesystem and network isolation.

[R6] AWS Durable Execution SDK Developer Guide, *Idempotency and retries*, accessed 16 September 2026. Replays/retries and side-effect duplication.

[R7] Anthropic, *How we built our multi-agent research system*, accessed 16 September 2026. Benefits of parallel research and the cost/coordination tradeoff. Product-specific observations are not assumed to transfer quantitatively to AI Personas.
