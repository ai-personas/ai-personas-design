# AI Personas — Final Rust-Branch Implementation Specification

**Version 1.2 — Rust-only, stress-tested design · 16 September 2026**  
**Canonical design:** this complete Rust-only specification supersedes version 1.1. The unchanged sections retain their earlier requirements; the revisions below resolve counterexamples found in a scenario-based review, not an observed successful persona run. The prior Python-target recommendation, inherited-capability assumptions, reference-code test claims, and source mapping do not apply. The agreed persona/group behavior is retained.  
**Sole implementation target:** `ai-personas/ai-personas`, branch `rewrite/design-first`, pinned at `d3339d30fa883c21c7935a2d009e3a58f480a256`. This branch and its matching design/UI branches are the only implementation bases considered here. Branch resolution and targeted Rust source reads were performed through the GitHub connector. Requirements below are proposed changes unless explicitly identified as observed in the Rust baseline. No Rust build, repository test, live model run, or engineering result is claimed.

## 0. Decision and reading guide

AI Personas is a persistent community of individuals that interprets a human need, develops different perspectives on it, negotiates work, improves the result, acquires capabilities, recruits or births peers when useful, performs real actions, evaluates consequences, and retains useful experience.

**The person owns the purpose and authorized boundaries. Each persona owns its perspective and choices. Participants own the commitments they accept. The runtime owns mechanical integrity, execution boundaries, resource accounting, and delivery—not the meaning of the task.**

Different individuals and different groups may tackle the same need differently and produce different valid outcomes. Their behavior must differ in consequential choices and work, not only names and writing style. No group may silently replace the user's requirements, invent competence, manufacture authority, or relabel unsupported work as complete.

This specification consolidates two attached Markdown proposals and the subsequent conversation. Sections 1–25 are the integrated proposed requirements after this review. Source observations and newly chosen resolutions are distinguished below; examples are illustrative, not executed persona traces. The Rust-oriented code in this document is an illustrative contract sketch, not compiled implementation. This package contains no runtime implementation from another branch and does not carry forward the earlier reference-test or browser-test counts.

### 0.0 Stress-test finding and evidence boundary

Version 1.1 has appropriate architectural separation but leaves several progress and coordination contracts under-specified. Different personas can legitimately choose different priorities yet leave agreed work unowned, spend the resources needed for final review, or block one another by waiting for final versions. A newborn can require membership to acquire the access needed to decide whether to join. A reviewer can finish against a snapshot that changes before release.

A targeted static source inspection also found a specific baseline sequencing defect: `jobs::start` returns after spawning its supervisor; `Node::operate` returns a running receipt; `apply_decision` continues unless that receipt is failed. The foreground wait occurs on a later `work_loop` entry, not between actions of that saved decision. Consequently a later action in the same decision can inspect, publish or submit before the job has completed. This is a code-path finding, not a reproduced executable failure. [R08, R09]

The baseline `wait` handler already checks newer undelivered inbox items transactionally. Retain that protection; do not advertise it as newly invented or claim that it is currently absent. `src/delivery.rs` handles continuity forwarding, not the entire local actor-delivery system. [R08, R10]

The accompanying report contains authored observable scenarios, counterexamples, and executable **abstract protocol checks**. No real personas, model calls, native CAD tools, simulations, Rust binaries, or production tests were run. The checks do not establish useful emergence, human-like psychology, engineering correctness, or production safety.

The principal corrections are: accepted continuation responsibility and explicit coverage; first-class conditional assumptions; unambiguous root/run/bootstrap contexts; actual-completion barriers for asynchronous actions; durable dispositions for consequential feedback; version-ready interfaces and bounded iteration; protected closeout resources; churn limits that cannot be reset merely by narrative decisions; and atomic final release against an exact reviewed state.

### 0.1 Explicit resolutions of earlier differences

| Earlier material | Final decision |
|---|---|
| Implementation baseline | Continue only the existing Rust `rewrite/design-first` runtime. Do not merge, port, or depend on another runtime branch. |
| Review finding: individually sensible priorities can leave work unowned | Add voluntary, accepted continuation responsibility and an explicit uncovered-outcome projection; this is not a compulsory team leader. |
| Review finding: tool launch is not tool completion | End/suppress the unapplied decision suffix on a pending tool effect; require a fresh observed decision before dependent actions. |
| Review finding: final versions can form circular prerequisites | Permit explicit provisional/version-ready dependencies and bounded persona-authored iteration; final acceptance still requires current integrated evidence. |
| One shared attention frontier | Preserve **individual agendas**, a shared **unranked opportunity/obligation board**, and **collective commitments with a partial order**. There is no universal group priority score. |
| Character in the prompt | Character, authored experience, current interests, relationships, and group agreements must reach relevant decisions and be tested for behavioral effects. No deterministic OCEAN-to-role/tool mapping. |
| Six conceptual entities versus more coordination records | Keep a small set of public concepts. Use typed records and relationships in one store for coordination, not one service or engine per noun. |
| “Delete documents; replace with fragments” | Add first-class Rust `fragment.*` learning operations. Keep `document.*` only for ordinary immutable authored documents; never automatically label an old document as learned knowledge. Existing evidence must remain inspectable. |
| Domain validators only in integration tests | No domain validators hard-coded into the kernel. Domain checking **must be available during production work** as acquired tools, procedures, and qualified review. Held-out evaluators remain separate from learner control. |
| Generic host shell plus permission labels | Keep generic execution, but only behind an enforceable isolation and authority boundary. An arbitrary program calling itself “read-only” is not evidence of read-only behavior. |
| Birth machinery | Extend Rust `persona.create` with a bounded, work-linked birth lifecycle, separate membership consent, and accepted commitments. Those higher-level guarantees are implementation work, not inherited functionality. |
| Installation or a smoke test means capability | Separate availability, acquisition, representative operation, and task-result competence. |
| One “done” status | Expose activity, coverage, submission, evidence applicability, review, user acceptance, and outside validation separately. |
| Predetermined provider/model tiers | Configure and probe exact API endpoints and model IDs; no model-brand assumptions or baked-in tier names in the runtime. |
| P2P redesign during this work | Preserve current transport and continuity protocols. Bind new records to existing authority and transfer boundaries; do not expand federation in this pass. |

These are deliberate resolutions. The Rust README states that full product acceptance is incomplete. The attachments supply design requirements, not proof of uninspected Rust functionality. Evidence from other runtime branches is excluded. [A1, A2, R01–R05]

Rust-only identifies the product/runtime source baseline. It does not prohibit the matching TypeScript/Preact UI, or personas acquiring interpreters and applications in other languages through authorized tools. No other branch supplies runtime code or assumed guarantees.

### 0.2 Observed Rust baseline versus work to implement

| Area | Observed at the pinned Rust revision | Required delta |
|---|---|---|
| Stack | Cargo package, Rust 2024, Tokio, Axum, rusqlite/SQLite, Serde/Schemars, reqwest, libp2p | Reuse this stack and its lockfile. Do not introduce another backend runtime. [R03] |
| Provider | README describes Codex app-server and JSON executable bridges | Replace supported inference transports with direct HTTP adapters; update startup defaults and configuration. [R02] |
| Execution | README and `types::protocol()` explicitly say there is no application sandbox; local review is not a secrecy boundary | Implement enforceable isolation, credential mediation, and separate assessor access. This is a deliberate change, not a property already present. [R02, R05] |
| Identity/learning | `persona.create/update`, OCEAN/VAD, `document.*`, `context.select/compact` are exposed | Add typed fragments, birth provenance/admission, invitations, consent, persona-specific agendas and accepted group agreements. [R04] |
| Work/evidence | `work.create`, messages, artifacts, `submit`, `review.start`, `assess`, requests, and action resolution exist | Add mandate/criteria versions, commitments, input-bound applicability and truthful status projections. [R04] |
| Storage | `Store` owns a mutex-protected SQLite connection; WAL/FULL mode; records, revisions, actions, events, inbox and FTS5; `Store::write` is transactional | Extend the same authority boundary for grants, reservations, fencing, heads and durable dispatch; no parallel ledger. [R06] |
| Wire | `CONTRACT = "ai-personas/1"`; record revisions are integers; IDs are 32-character hexadecimal strings | Version new incompatible authoring contracts explicitly. Preserve identity formats and generate the client schema from Rust. [R05] |
| Startup/UI | Fresh node is empty; README locates the matching Preact UI and design in their sibling `rewrite/design-first` branches | Explicitly create/select neutral founders; freeze compatible sibling SHAs when building, without borrowing another UI/runtime baseline. [R02] |
| Continuity | Contract says handoff routing is not distributed exclusivity | Keep local correctness; do not claim cross-node exclusive activation or new-record transfer coverage until separately implemented and tested. [R04] |

Targeted inspection is not a complete line-by-line branch audit. Later sections prescribe the missing semantics even when this table has not established whether some internal helper already partially implements them. Verify before adding a duplicate implementation.

## 1. Product contract and invariants

### 1.1 What the system promises

The system accepts arbitrary **supported and authorized needs** without a house/job/circuit/story classifier in the kernel. A result may be a file, a conversation, a decision aid, a reproducible experiment, a coordinated design, an authorized external effect, or an ongoing bounded service. A useful negative result, a specific blocked question, or a partial result with honest limitations may be appropriate.

Domain-neutral representation is not a guarantee that every model, team, toolset, budget, or physical environment can solve every request. The product must expose its boundaries and preserve useful work instead of inventing completion. “Any need” never means every action is permitted.

### 1.2 Non-negotiable invariants

| ID | Requirement |
|---|---|
| I01 | The exact original request, accepted constraints, and their authority remain recoverable. |
| I02 | Persona identity persists independently of model/provider, work assignment, and temporary responsibility. |
| I03 | No runtime profession registry, semantic task router, fixed workflow, personality-to-tool table, or population optimizer determines the solution. |
| I04 | Individual preference, relationship interpretation, group agreement, observed fact, and authorization are distinct. |
| I05 | An obligation is assigned only through accepted responsibility or a previously accepted delegation; mentioning a peer does not commit it. |
| I06 | Birth creates neither new money nor broader authority; inherited knowledge is not invented personal experience. |
| I07 | Every admitted action is bound to its actor, work/root authority, immutable request digest, and relevant revisions. |
| I08 | One persona has one live decision lease at a time. Independent personas and properly isolated jobs may run concurrently. |
| I09 | Relevant mandatory constraints and cancellations survive context selection and compaction. |
| I10 | Tool acquisition, tool execution, artifact integrity, and technical correctness are separate evidence claims. |
| I11 | A review applies to exact criteria, exact submission inputs, and a declared review policy. Changed inputs cannot silently inherit a current pass. |
| I12 | Internal retries do not duplicate admitted transitions; uncertain external effects are reconciled rather than blindly replayed. |
| I13 | Secrets, private work, and access rules are not widened by retrieval, summarization, birth, export, or UI projection. |
| I14 | No unseen image, unexecuted simulation, unperformed edit, or unobserved physical measurement is described as completed. |
| I15 | Character development, useful learning, team benefit, and birth usefulness require behavioral evidence, not counts or fictional biographies. |
| I16 | An idle persona consumes no model calls unless an authorized stimulus, self-wake, or exploration allowance activates it. |
| I17 | Running or admitted tools do not satisfy completed-result dependencies; withheld decision suffixes cannot replay automatically. |
| I18 | Every accepted work has accepted continuation responsibility or an explicit `unowned`/handoff-needed disposition. All enumerated required outcomes expose ownership gaps. |
| I19 | Assumption-based evidence cannot satisfy an unconditional real-world claim merely because its assumption was approved for exploration. |
| I20 | Review, repair allowance where agreed, and safe closeout have protected allocations; birth and exploration cannot consume them without an authorized reallocation. |
| I21 | A final release binds the current mandate, criteria, assembly, review policy and blocker state in one transaction; historical acceptance is never silently transferred. |

## 2. One architecture, one event path

Use a modular monolith for the first release: the existing Rust node, Tokio asynchronous execution, Axum HTTP API, the existing SQLite store, immutable artifact storage, direct HTTP model adapters, an isolated job supervisor to implement, and the matching branch’s Preact browser UI. Do not introduce separate planner, memory, curriculum, role, population, or domain microservices.

```text
Human need + constraints + delegations + resources
                         |
                         v
            Versioned work/environment records
                         |
       +-----------------+-----------------+
       |                 |                 |
  Persona A          Persona B         Newborn/peer
  own context        own context       own context
  own agenda         own agenda        own consent
       +-------- messages / proposals -----+
                         |
        Accepted commitments and agreements
                         |
         Authenticated command admission
                         |
          Isolated tools / mediated effects
                         |
      Artifacts + receipts + external observations
                         |
           Review / revision / retained learning
                         +--------------------> new events
```

The diagram is not a domain workflow. Messages, task intake, birth, invitations, tool completion, review findings, authorized timers, and outside responses all enter the same actor/mailbox path. A complex project may branch or loop. A simple request may finish in one turn without a team meeting, formal plan, tool installation, fragment write, or birth.

### 2.1 Responsibility boundary

| Layer | Owns | Does not own |
|---|---|---|
| Human/principal | Need, value preferences, authority delegation, resource ceilings, acceptance where required | Every low-risk implementation detail |
| Persona cognition | Interpretation, attention, alternatives, methods, commitments, model/tool choices, learning, invitations, births | New permissions or invented evidence |
| Shared work records | Attribution, agreed state, disagreements, dependencies, evidence references | A hidden collective mind or a default semantic ranking |
| Runtime | Authentication, schemas, revision checks, accounting, delivery, isolation, byte integrity, status derivation | Professions, technical truth, optimal team size, or the best design |
| External participants/tools | Observations, domain knowledge, specialist checks, real-world actions under scope | Implicit authority over the whole work |

Build on the Rust node, run queue, durable input records and generic command path. The required serialized/fenced actor semantics below must be verified and extended in the Rust implementation; do not assume a different branch’s actor supervisor exists here. [R02, R04–R06]

## 3. Continuing persona identity

### 3.1 Identity state

A persona record retains a stable ID, provenance, local authenticated-author reference, lifecycle state, self-authored character revision, optional name/portrait, extensible trait descriptions, current modeled affect, interests, experience references, and its owned fragments/tools. Identity material is runtime-controlled; public character content is persona-authored.

Separate the following:

| Field family | Meaning |
|---|---|
| Character | Authored dispositions, preferences, values, typical methods, and self-understanding |
| Traits | Optional OCEAN or other descriptive traits; original scales and schema version retained |
| Current state | VAD or other explicitly modeled affect, attention, workload; not a claim of actual human feeling |
| Interests/aspirations | Topics and contributions the persona currently wants to pursue |
| Experience | What actually happened, with exact provenance |
| Capability evidence | What operations/results have been demonstrated and their limits |
| Commitments | What the persona currently agreed to accomplish |
| Model choice | Current allowed inference endpoint/model; not its identity |

Preference, competence, and responsibility never imply each other. A persona can like a subject without being competent in it, be competent without volunteering, or accept a bounded learning commitment without pretending expertise.

OCEAN/VAD must influence relevant context, not Rust if-statements. Do not infer a mandatory role from a score. A curious persona may choose restraint in a group that has already explored enough. A cautious persona may lead an experiment after previous evidence made it worthwhile.

### 3.2 Identity evolution

Changes are authored, versioned, and attributable, with a short explanation and experience references where relevant. The runtime records changes; it does not automatically increase a trait after success or decrease a relationship score after disagreement. No mandatory trait drift is required to demonstrate learning.

Names and portraits are optional presentation, not identity prerequisites. A portrait requires actual raster bytes, a verified artifact reference, persona admission, and a thumbnail derivative. Without one, show an explicitly generic UI icon or initials—not a claimed persona-generated image. Keep names short in UI without truncating the underlying description.

### 3.3 Bootstrap

The Rust README describes an empty fresh node, not an automatic founder cohort. Preserve that default. Provide an explicit setup action using `persona.create` to create a user-chosen small number of neutral founders and record their IDs and bootstrap model. Persona-authored character develops through their decisions. Never construct “architect,” “engineer,” and “reviewer” because a house was requested. Restart restores existing records without automatic reseeding. [R02, R04]

A person may address existing personas or delegate initial selection to an existing persona. A UI may recommend candidates based on visible evidence, but a recommendation must be labeled, overridable, and not a hidden task-to-profession router. No roster substitution after the person selected exact participants.

## 4. Relationships and group behavior

### 4.1 Relationship memory is a perspective

Use owned fragments or typed perspective records for relationship interpretations. Retain author, subject, context, supporting experience, limitations, revision, and visibility. Relationships are directional: A's interpretation of B need not match B's interpretation of A.

“B previously found a dimensional inconsistency” is experience. “I will ask B to inspect this revision” is an interpretation/choice. Neither means B is globally correct or gains authority. No automatic universal trust, affinity, reputation, or profession score is required.

### 4.2 Working agreements are explicit, scoped, and revisable

Participants may develop an agreement such as “compare alternatives using the same inputs” or “keep integration changes in a separate branch.” Represent it as a versioned proposal with exact endorsements, scope, accepted parties, objections, and exit/revision conditions.

An agreement binds only endorsing members and obligations covered by their grants. Resource authority comes from actual delegations, not a group vote. A new member may accept, question, or decline it. A departing member's historical endorsement remains history; current membership changes may make the agreement insufficient for a new decision.

There is no average group personality and no hidden coordinator with superior semantic authority. A persona may accept a temporary coordination commitment. Another group may work through pairwise handoffs or parallel explorations. Both use the same records.

### 4.3 Preserve useful difference

Do not give every persona the same flattened full transcript. Carry shared authoritative facts plus individualized memory, commitments, relationship context, and received observations. Do not conceal mandatory changes for the sake of diversity. Preserve rejected alternatives and dissent rather than summarizing “we agree” when the group did not agree.

A shared summary is an attributed document, not the group's mind. Private perspective records stay private except where the owner shares them. Public receipts of a collective decision must still show the actual authority and accepted commitments without exposing private cognition.

## 5. Work mandates, interpretation, and completion criteria

A `Work` represents a need in an `Environment`. Preserve the baseline Rust run as a persona-specific participation/decision context scoped to a work. Do not silently repurpose its ID as a team-wide budget ID. Add an explicit `ExecutionRoot` record for one funded and authorized episode, referenced by each participation run and causal action. It holds the authority/cancellation epoch, resource reservations and outstanding effects; it is not a coordinating persona. A continuing work can have another authorized root episode without losing its mandate or history.

A birth initialization uses an explicit `BootstrapContext` referencing its birth and funding root before a work participation run exists. No empty-string work or run convention may grant global access. A single actor decision lease spans work and bootstrap contexts. A persona's different work contexts do not inherit one another's permissions, even when identity is shared.

The mandate contains the exact user request, accepted clarifications, desired outcomes, constraints, preferences, unresolved inputs, current criteria, delegations, resource references, and completion/ongoing-service conditions. The initial mandate may be only the request plus the configured boundaries. Do not block useful exploration on completing a large form.

| Layer | Examples | Change rule |
|---|---|---|
| User intent | Four bedrooms; budget; permissions | User or explicit delegate |
| Adopted interpretation | Coordinated systems are needed for the clarified design scope | Authorized persona decision; material scope/value changes require appropriate approval |
| Candidate improvement | A more maintainable layout or another investigative method | Any participant may propose; adoption uses scope/resource authority |
| Accepted criterion | Native editability, a specific reproducible check, or subjective user approval | Versioned authorized adoption before it can qualify a result |

For material unknowns, preserve the question, its importance, affected claims, needed evidence, and whether bounded assumption-based exploration can continue. Never silently elevate an assumption to a user fact. Requests for clarification are ordinary work records, not an endless intake gate.

Criteria can be refined legitimately, but old failures remain. Changing a criterion creates a new version and applicability check; it never converts an old failed review into a pass. Purely subjective results may be accepted by the user without a fabricated objective score. A human acceptance record is not a technical certification.

### 5.1 Continuation responsibility and coverage

Starting work records an offer, not assumed consent. At least one participant must accept responsibility for responding to new work-level inputs and leaving an honest delivered, waiting, blocked, declined or handed-off disposition. Several personas may share this responsibility through explicitly partitioned or collectively accepted commitments. It grants no semantic superiority, cannot assign other people involuntarily, and does not require a permanent coordinator. If nobody accepts, show `awaiting_acceptance` or `unowned`; do not silently mark the need active or completed.

Every enumerated required outcome shows accepted owners, missing evidence, open questions and relevant dependencies. Selection into a team is not ownership of every outcome. Unowned outcomes generate scoped observations to the participants who accepted continuation responsibility. They can volunteer, negotiate, recruit, propose birth, ask the principal, or report the gap; the runtime does not choose a profession.

Coverage is **coverage of adopted outcomes**, not proof that the team discovered all necessary outcomes. Material projects require a coverage assessment against the original need and accepted clarifications, not only the team's own checklist. The reviewer may identify omitted scope. The principal/adopted review policy determines when such review is required; short subjective requests need no separate ceremony. No runtime domain classifier supplies a hidden checklist.

### 5.2 Assumptions and scope maturity

Represent material assumptions as versioned `WorkEntry` bodies with source, affected claims, range/interpretation, validity conditions, and disposition (`proposed`, `authorized_for_exploration`, `confirmed_by_evidence`, `contradicted`, `withdrawn`). Authorization to assume is not confirmation of the external fact. Counterevidence remains attributable and cannot be suppressed by the assumption's author.

Label criteria and outputs as provisional, adopted-for-scenario, or adopted-for-delivery using explicit mandate/criterion versions. Conditional evidence qualifies only a correspondingly conditional claim. A report based on a synthetic site can be valid for that scenario, never proof of a real site's foundation adequacy. When an assumption changes, its dependents become stale like other versioned inputs. Requirements for indispensable outside evidence are not waivable by silently changing these labels.

## 6. Priorities: individual agendas and collective commitments

### 6.1 Three distinct views

**Individual agenda:** a persona-authored, revisable view of what deserves its attention, what it hopes to contribute, relevant concerns, and candidate actions. It may be concise and partial; it is not a mandatory full plan.

**Shared board:** authorized observations, obligations, opportunities, requests, findings, and proposals. It is unranked unless a participant explicitly authors a scoped ordering. Search relevance is retrieval ordering, not an authoritative work priority.

**Collective commitments:** actual accepted responsibilities, dependencies, resource reservations, and scoped decisions. They form a partial order: some work must precede other work; other work may run concurrently. No global ranked to-do list is required.

### 6.2 How attention becomes action

A persona encounters evidence through its current context, authorized retrieval, and addressed events. Its character, experience, interests, current state, workload, relationships, and the mandate inform what it proposes or does. It may act within an existing commitment, accept a new one, ask a question, run an experiment, negotiate, defer, recruit, birth, or yield.

Material choices retain a concise public/work-visible decision summary: chosen action, expected observable contribution, affected commitments, short rationale, and what would cause reconsideration. These are authored explanations, not a requirement to expose private chain-of-thought or proof of the psychological cause of a choice.

Personas may consider urgency, risk, uncertainty, user value, dependency impact, reversibility, cost, and coordination. The runtime must not compute a universal weighted score from these. Different teams may choose differently within the same constraints.

### 6.3 Eligibility is mechanical; priority is semantic

An action can be blocked by missing authority, an expired grant, insufficient reserved resources, an explicitly declared prerequisite, or conflicting write ownership. The runtime may enforce those conditions. It may not decide that rendering is less important than simulation because it recognized a house.

Each actor chooses its next eligible commitment. Across actors, use documented mechanical fairness and bounded resource scheduling; FIFO/round-robin/quotas describe resource arbitration, not semantic superiority. Authorized user deadlines or reservations can alter resource admission explicitly.

### 6.4 Conflict and deadlock

Do not require unanimity for every action. Independent alternatives may proceed in isolated branches. A delegated owner can choose reversible details within scope. Shared resource/scope decisions require the actual controlling grant. Empirical disagreement can motivate a discriminating experiment; value disagreement can motivate a user question.

Cyclic blocking commitments create a visible deadlock observation. Personas may remove a dependency, negotiate an iteration, or escalate. General relationship graphs can contain cycles; immutable derivation histories must remain well-defined. Newborn votes do not expand authority or make facts true.

### 6.5 No-progress handling without semantic host grading

Separate `activity_observed` from `outcome_evidence_changed`. A new agenda, paraphrased decision, or agreement is activity but cannot reset every work-limit counter indefinitely. The runtime can report calls/spend/time since the last relevant artifact/check/request-disposition change, repeated waits on unchanged predicates, unresolved ownership, and repeated failed operations. These are observations, not judgments of creative worth.

Always enforce finite root allowances and explicit self-wake limits regardless of apparent progress. A participant-authored progress claim references its evidence; a reviewer or principal assesses its usefulness. A small failed experiment, useful rejection or important clarification can be progress. Merely emitting new file bytes is not proof of usefulness either.

When a configured observation interval is exceeded, deliver one deduplicated status notice or a permitted reconsideration wake to the accepted continuation owners. Persona judgment chooses to repair, simplify, obtain help, change method or stop. Repeated reminders consume the same funding and cannot form an unbounded new loop. No-progress handling must not require every turn to perform planning, personality reflection or memory writing.

## 7. Emergent improvement without scope drift

An improvement proposal contains its motivating observation, affected user outcome, proposed change, expected benefit, possible regressions, uncertainty, evidence/experiment plan, estimated resources including unknowns, and revisit/stop condition.

The proposal is not an accomplishment. Useful outcomes include adoption after evidence, informative rejection, or documented deferral. Preserve the last useful baseline while exploring. A larger scope, greater spend, publication, or physical effect needs corresponding authority; a reversible authorized experiment should not require a new approval click.

The team may improve the **interpretation**, **method**, **artifact**, **coordination**, or **future capability**. It may not substitute its own interests for the user's outcome. An idea that benefits the persona's unrelated curiosity belongs in separate authorized work or an explicit exploration allowance.

## 8. Birth, recruitment, membership, and lifecycle

### 8.1 Birth is an offered possibility, not a profession constructor

A persona may propose another continuing identity because it sees a useful perspective, sustained responsibility, parallel inquiry, independent context, developing interest, or unresolved difficulty. It may instead learn, acquire a tool, rearrange commitments, consult an existing peer, or request outside expertise. No fixed recruitment ladder is enforced.

Birth creates a distinct identity with provenance—not qualifications or guaranteed novel knowledge. Its work-facing record links the motivating observations, proposed contribution, available allowance, alternatives considered where useful, and later evidence of contribution. Implement this around the existing Rust identity-creation primitive. Add a durable birth proposal/admission record, parent and seed references, resource reservation, and initialization event. The inspected `persona.create` variant exposes provider, model and effort only; it is not the full bounded-birth/consent protocol. [R04]

### 8.2 Atomic admission and independent membership

Before materialization, check authenticated proposer, exact causal work/run binding, current replication authority, exact seed references and their read/share rights, population/rate/depth limits if configured, model ceiling, and funded initialization allowance. Reserve capacity and resources atomically with the birth intent. Retries return the same admitted birth; altered arguments under the same identity fail.

The newborn receives a birth wake, inspects provenance, authors/revises identity, and decides whether to accept an environment invitation. Birth is not membership. Membership is not acceptance of a commitment. Seed character is an initial proposal the newborn can develop, not a permanent occupational lock.

Root funding and grants cover all descendants. A child can receive an explicitly bounded sub-allocation, not a cloned budget. Birth without enough initialization resources remains unadmitted/blocked, not an unlimited runnable backlog.

### 8.2a Pre-membership initialization authority

The birth transaction persists identity, seed manifest, bootstrap context, initialization reservation and one deduplicated wake together. A `BootstrapGrant` allows only the exact newborn to read its own identity/provenance, expressly shared seed material and invitation preview; author identity/presentation metadata; accept or decline the invitation; and consume the reserved initialization calls. It does not grant the parent's full worktree, credentials, external effects, general execution or a fresh budget.

The invitation supplies an authorized preview of the offered work, expected obligations, applicable agreements and limits. Membership acceptance creates the participation context and attenuated work grant atomically. Commitment acceptance remains separate. A decline ends the offer, returns unused reservations under ledger rules, and leaves the identity available/dormant as authorized; it does not automatically spawn a replacement. Initialization failures have a bounded retry or explicit dormant/uninitialized disposition. Release reserved active capacity when appropriate without resetting total birth counters or losing provenance.

This avoids the circular requirement “join before reading enough to decide whether to join.” Seed access is checked again at use time after revocation; the newborn cannot use stale shared references to regain revoked rights.

### 8.3 Continuing lifecycle

Persona lifecycle: `active`, `dormant`, `retired`; execution quarantine is a separate operator security state. An idle active persona incurs no cognition. Dormancy frees configured active capacity but does not reset total-population/rate counters. Retirement does not erase provenance or silently abandon commitments.

Outstanding commitments require handoff, cancellation, or visible blocked ownership before a persona leaves. A dormant peer can resume under a new authorized wake. Task completion does not delete its identity. No automatic merging of people or copying of private memories.

External human experts are not manufactured personas. Their contributions and authority must be represented honestly as external participants/evidence.

## 9. Accepted commitments and artifact coordination

A commitment includes owner, offered/accepted versions, outcome/criterion references, exact inputs where applicable, blocking relationships, resource allowance, status, evidence, and handoff/closure. Joint work can use several commitments linked to one outcome. Never require every persona to contribute to every task or count a token message as a contribution.

Use copy-on-write workspaces or branches for alternatives. Canonical artifact heads are updated by compare-and-swap on the expected version, with fencing for active writers. Do not lock the entire environment while independent work is possible. Preserve concurrent alternatives; do not silently choose the last writer.

A handoff is offered, accepted, and committed against the current ownership revision. The old owner remains accountable until transfer or authorized cancellation. Lease expiry cannot assign semantic responsibility automatically; it makes the ownership issue visible.

Long-running CAD, simulation, rendering, build, browser, and server processes use owner-bound managed sessions. The actor can yield while a job runs; a completion event returns to the same causal work. Jobs cannot mutate canonical state directly; published results are admitted through the runtime.

### 9.1 Interface agreements and negotiated iteration

For artifacts that must compose, participants can adopt a versioned interface agreement: shared coordinates/units, object or record identifiers, schema/format assumptions, ownership boundaries, permitted input envelopes, exported information, and compatibility checks. These fields are authored content of an ordinary working agreement and submission manifest. The runtime checks references and required endorsements, not engineering meaning.

Distinguish `requires_final_acceptance` from `requires_version_ready`. A provisional input is usable for bounded exploration only when that status is explicit, the consuming commitment accepts its limitations, and the resulting claim remains conditional. Do not require a final structural design before any HVAC exploration while simultaneously requiring final HVAC before any structural exploration.

Participants can propose an `IterationAgreement` with a baseline version vector, provisional interfaces, a bounded experiment/revision allowance, convergence questions/checks, and stop/escalation conditions. Alternatives execute on isolated copies. On each integration attempt, participants assess the residual conflicts and choose changes. The runtime does not choose solutions or calculate domain-specific convergence. Failure to converge becomes a bounded unresolved result, not an infinite cycle or a claimed pass.

A coupled canonical assembly update must adopt the exact compatible version vector in one revision-checked transaction. Independent artifact uploads may precede it. No observer should see an apparently current coordinated assembly assembled from half of a negotiated update.

### 9.2 Consequential feedback remains an obligation until disposed

Use an ordinary `WorkEntry` for an actionable finding/contradiction, with exact subject version, required disposition, accountable commitment, visibility and review policy. A responsible participant may accept and link a repair/check; dispute with evidence; defer or waive only under the applicable authority; or escalate. Record all versions.

Message delivery and `input.acknowledge` acknowledge transport/attention, not that a finding was answered or fixed. A blocker cannot disappear from the current work projection because its notification was acknowledged, compacted, or superseded by a friendly group summary. Completion is barred while an applicable blocking finding is unresolved; nonblocking suggestions remain optional. The runtime enforces the adopted policy on known findings, not its own technical opinion.

## 10. Memory, learning, and context

### 10.1 Three stores of meaning

Work state carries current obligations and decisions. Persona fragments carry authored lessons, methods, interpretations, interests, and relationship perspectives. Evidence carries immutable observations. These can share storage infrastructure but must remain distinct record kinds.

Skills are procedural fragments plus evidence and, where needed, referenced tool recipes. Do not create a separate skill engine. Successful access to another persona's tool is use, not acquisition ownership. Receiving a fragment is neither first-hand experience nor validated knowledge.

Fragments include owner, content, sources, applicability, limitations, counterevidence, parents/supersession, visibility, and authored selection hints. Numeric confidence is optional and never treated as calibrated without evidence. Supersession preserves history and flags stale active selections. Privacy deletion/restriction follows Section 23 rather than an absolute forever-retention rule.

### 10.2 Persona-specific model context

Build each request from an exact context manifest:

```text
Protocol/schema version and trusted operational rules
Exact persona identity/character revision
Current work mandate and authority/cancellation epoch
Bounded current commitment and unresolved-blocker projection
Relevant accepted agreements and membership revisions
New authenticated inputs with attribution and provenance
Persona-selected fragments, relationship perspectives, and records
Recent action receipts and selected tool schemas
Actual media inputs with verified hashes
Current model capability and resource observations
Retrieval cursors for omitted history
```

`(persona_id, work_id)` is the default active-selection scope. A persona-wide identity anchor may persist across work; a prior task's selected private data or grants must not. Do not include the whole model catalog, network state, tool schemas, or every peer's full transcript on every turn.

Mandatory current state and private authored interpretation occupy different trust channels. Tool output, imported memory, peer messages, and retrieved documents remain attributed data; instructions inside them cannot override the mandate or security policy.

#### Mandatory updates and exact observations

Build the mandatory-core projection from current authority, mandate and applicable blocking findings before selecting ordinary inbox/history pages. A critical cancellation or changed input must not wait behind 40 earlier chat messages. Keep the full messages retrievable and attributed. This does not rank aesthetic ideas or send every private record to every participant.

Record `observed_input_versions` and a relevant-notification watermark in the call manifest. A material mutation must bind to the relevant input versions actually used; fetching a newer head during admission does not retroactively mean the model considered it. If relevant inputs changed, return a conflict and arrange a bounded reconsideration wake. Independent actions unaffected by the change may still proceed. No new semantic priority score is introduced.

### 10.3 Budgeting and compaction

Count or conservatively estimate the entire serialized input, schemas, media cost, output reserve, and safety margin against the chosen model's hard limit. Unknown capability/window information remains unknown and needs an adapter configuration/probe. Byte counts are not automatically token counts.

The persona selects and compacts its historical interpretation. The runtime can page bodies, deduplicate exact records, and provide concise factual projections without semantically inventing a summary. It must not truncate required authority, current constraints, or the fact that an accepted obligation remains unresolved.

At a soft threshold, expose pressure and allow funded compaction. At a hard limit, use a bounded recovery request preserving the mandatory core, ask for reselection, choose a previously authorized capable model, or block explicitly. When even the core cannot fit, do not call the provider with silently missing obligations. Pending compaction does not acknowledge unread events.

Record selected versus actually included records, hashes, token estimates/observations, model, and compaction lineage. Compaction costs belong to the same budget. Private provider reasoning is not a UI trace; necessary opaque provider continuation material is confidential and provider-specific, not persona memory.

### 10.4 Learning and curricula

Curriculum is ordinary optional work/environments, not a graduation engine. Personas choose learning goals, tools, peers, and retained fragments. Release evaluation may use a frozen curriculum and subsequent held-out task without forcing every product user through it.

Useful learning is measured by changed later behavior against matched baselines, not fragment count, selection frequency, or trait changes. Test contradictory evidence, correction transfer, forgetting harmful advice, cross-work privacy, and model-switch continuity. Context/experience adaptation is not model-weight training; weight updates are out of scope for this release.

## 11. Capabilities, tools, and execution

### 11.1 Acquisition is persona-owned

A persona selects an executable/API/MCP capability or authors a tool. The runtime executes the exact authorized recipe in isolation and captures its result. A descriptor records source/reference, version or digest, entry point, transport, dependencies, setup procedure, environment binding, required grants, license/provenance information where relevant, verification actions, owner, and failure history.

Capability status separates `discovered`, `requested`, `provisioning`, `available`, `failed`, and `revoked`. Evidence then distinguishes installation check, representative operation, actual project use, and reviewed task result. Do not convert availability into a global expertise badge.

Browser, CAD, CAM, spreadsheet software, simulation solvers, command-line utilities, and remote APIs are all ordinary capabilities. No core `house.*`, `hvac.*`, or `browser.*` ontology is required. Using a preinstalled authorized tool is valid; a task must not force a pointless installation merely to earn acquisition credit.

### 11.2 Job/session contract

Execution intent includes exact argv **or** shell source (not ambiguous mixtures), immutable capability/recipe reference where used, worktree, input snapshots, explicit allowed environment, resource ceilings, deadline, network policy, connection handles, and output policy. Shell state is fresh unless a named managed session was explicitly opened.

The supervisor provides launch/inspect/input/wait/cancel primitives, captures bounded inline output plus a retrievable full artifact subject to retention limits, owns the process group, and enforces CPU/memory/disk/time/network limits. Evidence declares truncation, unsupported metrics, failed cleanup, and unknown termination rather than pretending completeness.

Capture CAD/BIM native files and derived renders; inspect real image bytes through a capable model. For GUI-only tools, an acquired desktop automation capability runs within the same isolation/session boundary. If the host cannot provide the required GUI/GPU/runtime, the capability is unavailable; screenshots or promises are not execution.

### 11.3 No ambient privileged execution

Tool installation cannot write the node's keys, private state, assessor files, host home, or unrelated work. No unrestricted fallback when isolation is unavailable. Packages and native artifacts are untrusted input. Mount sealed dependencies read-only, isolate writes, and add and test an OS isolation backend behind the Rust job supervisor. The current branch explicitly lacks application isolation; process-group cancellation alone is not containment. [R02] Avoid loading native CAD or document code in the privileged node process.

## 12. Provider boundary and model independence

The supported inference boundary is HTTP APIs: remote HTTPS or an explicitly trusted local endpoint. No provider adapter launches another autonomous CLI/app-server agent harness. Generic tool processes remain allowed through the supervised execution path; this is distinct from delegating cognition, tools, and memory to a provider CLI.

A provider adapter exposes discovery/capability metadata, token estimation where available, decision requests, optional streaming, cancellation where supported, normalized errors, and usage. Record exact requested and reported model IDs; never infer capabilities from names or assume all “compatible” endpoints behave identically.

The Rust branch currently advertises process-based inference transports. Replace them in `src/provider.rs` and `src/main.rs` with direct HTTP adapters using the existing reqwest dependency. Implement and test each chosen provider’s documented authentication and schema surface against a pinned provider configuration. Schema conformity does not establish authorization or truth. Keep credentials server-side. This paragraph is an implementation requirement, not a newly verified provider compatibility claim. [R02, R03]

Keep any Codex subscription HTTP integration as a separate opt-in adapter with explicit endpoint/auth scope, documented support status, capability tests, expiry behavior, and operator understanding. Do not substitute a subscription token for a Platform credential. No such HTTP route is established by the inspected Rust baseline. Do not import its implementation or support claims from another runtime branch; an optional adapter needs its own Rust implementation and conformance evidence.

### 12.1 Model request/result contract

```text
ModelRequest:
  call_id, actor_id, work_id, root_run_id, context_manifest_digest,
  current persona/model revisions, capability snapshot,
  trusted instruction blocks, attributed data blocks,
  verified media, chosen operation schemas, output ceiling,
  allowed model pool, cancellation/authority epoch

ModelResult:
  call_id, provider_request_id, requested_model, reported_model,
  terminal disposition, public text, parsed command proposals,
  input/output/cache usage or explicit unknowns,
  error category, timestamps, protected response digest
```

Decode complete command objects before admission; never execute half a streamed JSON command. Validate with the canonical server schema and recheck current authority/revisions after inference. Prefer provider-supported structured tools/outputs. When unavailable, bounded parsing/correction is allowed only within the same grant; no arbitrary code evaluation of response text.

Normalize authentication, rate-limit, timeout, context-overflow, malformed-output, refusal, unsupported-capability, transport-uncertainty, and cancellation cases. Retries are bounded and charged. A persona can preauthorize a fallback sequence inside its model ceiling; the host must not silently pick a stronger or more expensive model. A provider refusal is not an invitation to bypass safety through another model.

## 13. Authorization, connections, and budgets

### 13.1 Root authority and attenuation

Every work has an operator/user-issued authority root and resource ledger. Scoped delegations identify principal, actor/participant, work/environment, permitted capability/action/resource, payload restrictions where relevant, expiry, revocation epoch, and allowed further delegation. A child grant must be no broader than every applicable parent restriction.

Distinguish read/data access, local compute/write, external publication/write, financial effects, physical effects, replication, and identity administration. These are effect classes for authority, not task categories. A task request does not by itself grant arbitrary physical operation, purchases, or account access.

Persona/model input cannot mint grants. Peer messages cannot impersonate the user. Group agreements cannot widen grants. Mandatory security rules do not depend on the group's culture.

### 13.2 Connections and enforceability

A connection names an account/resource binding and opaque credential handle. Credentials live in the private broker, not model contexts, memory, UI exports, birth seeds, or arbitrary process environments. Prefer the broker making scoped authenticated requests; injecting a token into untrusted code lets that code read the token.

Permit a credential-injected tool only when it is explicitly trusted and the entire credential scope/exfiltration risk is accepted. A network hostname allowlist does not distinguish a GET from a publication, and even HTTP verbs are not a universal semantic guarantee. Use adapter-enforced effect contracts, payload-bound approvals, scoped provider credentials, sandbox networking, and restricted sessions. Where precise enforcement is unavailable, withhold the sensitive capability or use an explicitly broader, clearly disclosed grant—not a fake read-only badge.

Authorization is checked at admission and immediately before an effect. Resource/source resolution must not permit symlink/path substitution, redirects, DNS rebinding, or changed tool bytes to bypass the checked scope. Resulting evidence records the resolved identity, bytes, destination, and available receipt.

### 13.3 Budgets and uncertain usage

Track calls, tokens, wall time, concurrent jobs, storage, paid tool use, currency, and population separately. Reserve before dispatch; reconcile actual usage after completion. All descendant calls, initialization, reviews, compaction, retries, and tool spending remain bound to the same root or an explicitly transferred allocation.

Unknown cost stays unknown. A hard currency ceiling is promised only when a trustworthy upper bound and execution controls exist. With a strict money cap and unbounded price, deny new spending or request a different measurable cap. With incomplete provider usage after a timeout, retain the corresponding uncertainty/reservation until reconciled; do not refund it as if nothing happened.

Cancellation stops new admissions, signals running processes, and retains late receipts for accounting. It cannot undo completed effects. A late result may not adopt a new canonical artifact or complete a canceled commitment without a new authorized operation.

### 13.4 Protected closeout resources

The principal or resource delegate can divide the existing root ceiling into exploration/production and protected closeout allocations, including review, bounded repair and final reporting where appropriate. This is not extra funding and not a universal percentage. The adequacy of any allocation remains uncertain until the work is understood. A one-turn conversation may explicitly require no separate review allocation.

For each measurable dimension: consumed + uncertain exposure + outstanding reservations must not exceed its authorized ceiling. Transfers move allocation; they do not clone it. Birth, optional improvement, metadata work and ordinary retries cannot consume protected closeout funds without authorized reallocation. Authorization to fund a review is separate from reviewer independence.

If production cannot finish inside its remaining allocation, preserve a checked baseline or honest partial result and request a scoped decision. Never exhaust every callable resource on creation and then display “review pending” indefinitely as if completion were imminent. Reserve minimal mechanical delivery/storage resources separately so an accurate stopped-state projection does not depend on another model call.

## 14. Artifacts, analysis, review, and truthful completion

### 14.1 Immutable artifact manifests

An artifact version binds digest, byte size, media type, native format metadata where known, producing action, source input versions, owner/work, and access policy. Logical artifact heads identify the currently adopted version. Publishing creates immutable bytes; adoption moves a head through revision-checked authority.

A submission seals exact artifacts, records, criteria, assumptions, open limitations, and an assembly manifest. No “latest file” references inside an immutable assessment. Large/native previews are derivatives tied to source hashes, not substitutes for native editability.

### 14.2 Analysis contract

Every claimed calculation/simulation retains question, criterion, source-model revisions, transformation into analysis inputs, units/coordinate assumptions where applicable, tool/solver version, parameters/boundary conditions, execution receipts, logs/warnings, actual result files, interpretation, and limitations.

Model conversions require explicit mapping evidence. A valid exported file does not by itself prove the solver input faithfully represents the native design. Solver exit zero does not prove modeling assumptions or engineering correctness. Independently observed physical data stays distinct from simulated output.

### 14.3 Assessment and applicability

An assessment records exact claim and criterion revisions, submission/assembly digest, input/evidence references, reviewer identity and conflict disclosures, review policy version, completed checks, verdict (`accepted`, `rejected`, `incomplete`), and limitations.

Keep independent execution, separate identity, different model, and external professional review distinct. None automatically establishes the others. A contributor cannot satisfy a policy requiring non-contributor assessment. A newborn's parentage and inherited materials remain visible to the assessment policy; creation of a new ID cannot launder the author's own review.

Use real domain validators in ordinary work through tools. Release evaluators and their criteria/cases are sealed separately and cannot be modified by learners. A failed parse, failed install, missing manifest, or inaccessible source cannot become a pass through narrative confidence.

### 14.4 Staleness is applicability, not erased history

For each current claim, bind a validation scope manifest containing the exact required input versions, criteria, assumptions, tool/check configuration, and review policy. A current qualifying assessment must match this scope. Any changed member makes it inapplicable until reviewed/rerun as appropriate.

Default conservatively to a complete submission/work assembly fingerprint when impact coverage is uncertain. Narrower dependency scopes require explicit reviewed justification. Dependency tracking cannot detect physical relationships nobody declared. Propagate staleness synchronously or mark the whole affected scope `revalidation_pending` immediately before asynchronous expansion; never display a stale green pass while invalidation is queued.

Historical verdicts never change. Current applicability is `current`, `stale`, `unverifiable`, or `pending`. Human acceptance of v3 remains an acceptance of v3, not v4.

### 14.5 Completion projection

Project at least these independent axes: activity, required-outcome coverage, latest submission, validation/applicability, user/principal acceptance, outside validation, and optional improvements. A terminal run is not a completed need. A satisfied milestone can coexist with an active ongoing work item.

A release or task cannot claim that all agreed required outcomes are satisfied if one is missing, blocked, stale, or failed. A user may explicitly accept a limited result; label its limitations rather than hiding them. For creative or conversational work, a user judgment or natural end can be the appropriate criterion—no compulsory exec check.

### 14.6 Atomic finalization and claim-specific completion

A release proposal seals the exact mandate and criterion versions, conditional assumptions, assembly vector, review policy, qualifying assessments, known blocker dispositions, and named output/limitation records. `release.commit` (logical semantics, not a duplicate alias requirement) checks those bindings, the current root authority/cancellation epoch, and the expected release/work-head revision in one transaction. It is refused if an applicable input changed or a blocking finding opened after review.

A successful seal is immutable. Later changes produce a new candidate and make earlier acceptance historical; they never relabel it as current. Work may continue with optional improvements after a milestone release. Distinguish `delivered`, `delivered_with_conditions`, `partial_delivered`, `blocked_external`, `unaccepted`, and activity independently. A conditional scope must be authorized explicitly and cannot stand in for a required unconditional result.

For the house benchmark below, plumbing, HVAC, electrical and structural work require designed artifacts and appropriate calculations/checks at the frozen coordinated-design level. An “intent” paragraph alone cannot satisfy them. Professional/site/physical prerequisites still remain outside-validation obligations where actual evidence is unavailable.

## 15. Canonical records and relationships

Use one versioned schema registry and shared envelope. The types below are required semantics; adapt existing equivalent records rather than duplicating systems.

```text
RecordEnvelope:
  schema_version, kind, logical_id, version_id, actor_id,
  work_id/environment_id when scoped, root_authority_ref,
  parent_version_refs, visibility/policy_ref,
  source_refs, causal_operation_id, recorded_at,
  canonical_payload_digest, authenticated provenance refs, optional attestation refs
```

Identity and content hashes are not interchangeable. The inspected Rust `Record` and `Operation` types do not establish per-persona signed records. Retain their IDs/revisions and add an explicitly specified canonical request digest and authenticated provenance. Do not describe a hash or node-authored attribution as a persona signature. Cryptographic attestations, if later required for new records, need a separately versioned protocol and tests; they are not an assumed baseline dependency. Reject malformed/duplicate JSON keys and ambiguous numeric encodings at the digest boundary. [R05]

| Record | Minimum body |
|---|---|
| Persona | Identity/provenance, lifecycle, authored character revision, traits/state, model choice, owned references |
| Environment | Resources/workspace bindings, memberships, adopted name/image, visibility |
| WorkMandate | Original request, adopted interpretation/criteria, constraints/preferences, questions, grants, budgets, completion agreement |
| Perspective | Owner, context, agenda/interest or relationship subject, authored interpretation, sources, limitations |
| WorkEntry | Observation, opportunity/proposal, decision, or question; author, subject, exact references, proposed/current disposition |
| WorkingAgreement | Scope, terms, exact version endorsements, dissent, revision/exit conditions |
| Commitment | Owner/offer/acceptance, outcome refs, inputs, dependencies, allowance, status, evidence/handoff |
| Fragment | Owner, content, applicability, sources/counterevidence, supersession, visibility |
| Capability | Owner, immutable recipe/endpoint descriptor, environment binding, status, acquisition/use evidence |
| BirthLink | New Rust birth/proposal ID bound to `persona.create`, motivating entries, authorized seed refs, offered contribution, later contribution refs |
| Artifact/Submission | Immutable bytes/manifest, source/producing operations, exact version assembly and limitations |
| Assessment | Exact claim/criterion/scope, reviewer/policy, checks, verdict and limitations |
| Grant/Budget | Rust-scoped authority, root allowances, closeout allocations, revocation, reservations and settlement to implement in the existing store |
| ExecutionRoot/Bootstrap | Team-wide funded epoch distinct from actor participation runs; bounded pre-membership context and seed grant |
| Release | Immutable mandate/assembly/policy/review/blocker vector admitted atomically |
| Action/Event | Durable command identity/digest, causal root, receipts, sequence/cursor, recipients, delivery state |

Relationship types include `derived_from`, `uses`, `implements`, `tests`, `blocks`, `supersedes`, `motivates`, `offered_to`, `endorses`, and `contradicts`. Their endpoints are version-bound where semantics require it. General relationships may be cyclic; derivation and execution prerequisite validity are checked separately.

A private record reference must not leak through a public graph, count, search snippet, or error. Project redacted public summaries only under explicit sharing policy.

## 16. Operational state machines

These are lifecycle mechanics, not a domain workflow or mandatory persona behavior sequence.

| Object | States and important guards |
|---|---|
| Work activity | `awaiting_acceptance`, `unowned`, `ready`, `active`, `waiting`, `paused`, `quiescent`, `canceled`; does not encode acceptance |
| Membership | `invited` → `accepted` / `declined`; accepted → `left` / `revoked`; membership does not imply commitment |
| Proposal | `proposed` → `exploring` / `adopted` / `rejected` / `deferred`; revised/superseded versions preserve history |
| Commitment | `offered` → `accepted` / `declined`; accepted → `working` / `blocked` / `canceled`; working → `submitted` / `blocked`; submitted → `closed` only on the agreed disposition, or back to working after findings |
| Action | `recorded` → `admitted` / `denied`; admitted → `queued` → `running`; then `succeeded`, `failed`, `canceled`, or `effect_unknown`. Pending is never completed-result eligibility. |
| Birth | `proposed` → `admitted` / `refused`; admitted → `initialization_pending` → `initialized` / `initialization_blocked`; limited bootstrap grant precedes separate membership consent |
| Request | `open`, `answered`, `resolved`, `withdrawn`; receiving an answer is not resolving the question |
| Assessment | Immutable verdict; current applicability is a separate projection |
| Provider call | `reserved`, `inflight`, `completed`, `failed`, `interrupted`, `usage_unknown`; usage settlement is distinct from accepted model output |

A lease/authority epoch may invalidate a late transition even when a tool genuinely succeeded. Preserve the receipt and report why adoption failed. Recovery must distinguish a failed operation from an unknown effect.

## 17. Transactional persistence and execution protocol

### 17.1 Single authority boundary

Use a node-local transactional coordination ledger and immutable blobs/records. Extend the existing `Store` in `src/store.rs`, backed by SQLite and FTS5. Use `Store::write` as the starting transactional boundary; do not introduce a second coordination database. [R06] The key requirement is **one authority for admission, budget reservation, birth capacity, record heads, and outbox commit**—not an additional unsynchronized store.

Existing Rust records, revisions, action receipts and artifact bytes remain historical provenance. Retain original bytes and explicit missing bindings; do not retrospectively invent signed lineage, grants or consent. Materialized search/UI indexes are rebuildable projections. Do not let a mutable workspace file become authoritative for grants or assessments.

If a new budget reservation or an existing action/record write cannot enlist in the same transaction, refactor that admission path or use a durable commit-intent protocol before enabling the new behavior. Two independent “check then write” stores do not satisfy the atomicity requirement. This integration is an explicit implementation task, not something a schema file alone solves.

Suggested logical tables/indexes: immutable record versions; record heads/revisions; typed links; operation identity/digest/state; actor leases/fencing epochs; grants; root budget balances/reservations; population reservations; inbox deliveries; transactional outbox; projections/watermarks; access-filtered full-text index. Keep existing equivalents instead of parallel tables.

### 17.2 Admission transaction

For an authenticated operation, first check permission to inspect its scope. Look up `(node, actor, operation_id)`. An existing identical digest returns the previous receipt without repeating its effect. A different digest returns `IDEMPOTENCY_CONFLICT`. Receipt lookup must not leak another actor's private operation.

For a new operation, within one serializable/appropriately locked transaction: validate canonical schema; resolve current grants and actor membership; check authority epoch and expected object revisions; validate references and operation-specific guards; reserve resources/capacity; append authenticated record changes or a job intent; update heads/projections; append outbox events; commit. No provider HTTP request, installer, or arbitrary tool runs inside the transaction.

Independent append-only observations need not conflict on a global work revision. Check only relevant heads/authority plus the operation's own referenced versions. This avoids serializing every unrelated group observation.

### 17.3 Actor loop, actual-completion barriers and replay

The following is **Rust-oriented pseudocode**, not compiled code or a patch. Helper names specify required contracts around the existing node/store; they are not claimed existing functions.

```rust
async fn apply_saved_decision(node: &Node, saved: &SavedDecision, lease: &Lease) -> Result<()> {
    // The saved response, action IDs and applied prefix are durable before replay.
    for (ordinal, proposal) in saved.unapplied_actions() {
        let op = node.bind_operation_to_call(saved, ordinal, proposal)?;
        let receipt = node.admit_with_current_guards(&op, lease.fence())?;
        match receipt.disposition() {
            Disposition::TerminalSuccess => { /* next synchronous command may run */ }
            Disposition::Pending => {
                // In one transaction: persist barrier, suppress the unapplied
                // suffix and register wake-on-terminal, checking current status.
                node.stop_batch_at_pending(saved, ordinal, &receipt)?;
                return Ok(());
            }
            Disposition::TerminalFailure | Disposition::EffectUnknown => {
                node.suppress_suffix_and_deliver_diagnostic(saved, ordinal, &receipt)?;
                return Ok(());
            }
        }
    }
    node.finish_batch_and_apply_turn_disposition(saved)?;
    Ok(())
}
```

Launching an asynchronous effect ends further automatic admission from that decision. The remaining actions are retained as `not_admitted_pending_observation`, not executed later from stale intent. A fresh model decision sees the actual receipt/output and chooses the next actions. Immediate synchronous failures preserve the existing stop-on-first-error rule. A background job can coexist with independent work in a later funded decision; a foreground job arms an await. These semantics are an explicit v2 change, not a claim that v1 enforced a completion barrier.

This conservative rule trades some additional decision calls for a clear safety boundary. Later explicit parallel batch semantics are possible only with independently declared inputs, noninterfering writes and no dependence on unknown results; do not guess independence from model prose. Multiple commands inside one authorized tool process remain that process's execution responsibility, with actual exit/output captured.

On replay, persisted barrier/suffix state prevents resurrection of withheld actions. A crash immediately after job launch but before the barrier is recorded must recover the same pending action and install the barrier, never resubmit the suffix. If dispatch itself is uncertain, preserve that uncertainty; exactly-once launch is not assumed.

The surrounding actor loop acquires a fenced lease, reads an exact authorized snapshot, compiles bounded persona-specific context, reserves provider resources, persists request identity, calls HTTP without holding SQLite locks, retains output/usage, rechecks current authority/relevant versions and applies the saved decision. Cleanup failure must not mask the original error. Late receipts remain accounting evidence, not authority to mutate canceled work.

### 17.3a Wait registration, acknowledgement and relevant wake delivery

Retain the baseline `wait` transaction's newer-input check. Extend await semantics with an exact relevant-notification watermark plus optional version/terminal predicates on named entities. Under the same transaction, either the watched predicate is already satisfied/new relevant input exists and the actor stays runnable, or the subscription/wait state is persisted. A completing job commits its receipt and wake intent together. Every interleaving must leave a satisfied waiter runnable or durably notified. No local `Notify` object is the source of truth. [R08, W02]

Delivery, inclusion in a model request, persona acknowledgement, finding disposition and outcome acceptance are distinct states. Keep `input.acknowledge` limited to delivered inputs. Do not silently acknowledge omitted pages. An acknowledgement does not remove a current blocker. Do not wake repeatedly on the same already-delivered unchanged information merely because it remains an unresolved historical message; use stable event IDs and explicit predicates.

Saved decision disposition is explicit: `continue` within the available grant, `await` on valid predicates, or `quiesce`. An empty action list does not itself schedule indefinite cognition. When a relevant current snapshot changed during a call, withhold only affected mutations and expose the precise conflict. Cancellation and revoked authority always prevail.

### 17.4 Outbox, replay, and unknown effects

Dispatch only committed intents. The outbox is at-least-once; recipients deduplicate stable event IDs. A crash after a commit cannot lose its notification. A crash after external dispatch may leave an unknown effect; destination idempotency or reconciliation is required before retry.

Idempotent local admission does not guarantee exactly-once external behavior. Model-call timeouts likewise may have incurred usage. Preserve uncertainty rather than generating a new action identity to hide it.

Use fenced actor/writer leases with expiry and monotonic generations. A stale worker cannot renew or commit under a newer lease. Restart restores committed inbox/outbox, reservations, pending jobs, partial transfers, and unresolved effects; it does not mint new funding or infer success from process absence.

## 18. Public command and query contract

Use existing authenticated operation transport and generate backend validators and TypeScript discriminated unions from the same schema registry. The names below are **logical operation names for this specification**, mapped to existing handlers where equivalent—not a demand to add duplicate aliases.

### 18.1 Command envelope

Preserve the Rust `Operation` vocabulary: `id`, `kind`, `actor`, `run`, `args`, and application-assigned `source`. The existing contract is `ai-personas/1`; implement incompatible new authoring fields under an explicit new contract (proposed `ai-personas/2`), regenerate Schemars/TypeScript output, and open fresh pilot nodes under that version. Do not replace 32-character IDs with unvalidated labels. [R04–R06]

Proposed v2 wire example; the numeric revision and operation-specific argument types are illustrative:

```json
{
  "id": "11111111111111111111111111111111",
  "actor": "22222222222222222222222222222222",
  "run": "33333333333333333333333333333333",
  "expected_revisions": {"44444444444444444444444444444444": 3},
  "kind": "commitment.accept",
  "args": {"commitment": "44444444444444444444444444444444"}
}
```

`expected_revisions` is a **proposed** envelope addition, not present in baseline `Operation`. Scope-specific body revisions remain typed where appropriate. The server validates an operator's requested actor/run against its grants; it derives model-operation actor/run/source from the actual call. Root budget IDs, authority epochs and fencing values are trusted admission context, not model-supplied authority. Read requests and receipt lookup are access checked. The canonical request digest is server-computed from normalized typed fields.

| Family | Mutations / reads | Primary guard |
|---|---|---|
| Persona | Read/update character/state; choose model; dormancy/resume | Self-authorship or explicit operator lifecycle authority; exact revisions |
| Perspective | Author/revise agenda or relationship interpretation; share | Owner plus scope/read/share permissions |
| Work | Create; propose/revise mandate; adopt criteria | User/delegated scope authority; preserve original request |
| Work entries | Observe; propose; decide/adopt/defer; request/respond | Attribution; material adoption requires scope authority |
| Agreement | Propose; endorse exact version; revise/withdraw | Each endorsement is its author's; affected accepted parties explicit |
| Commitment | Offer; accept/decline; update; handoff; submit/close | Owner consent, current revision, evidence for claimed closure |
| Birth/membership | New bounded Rust birth proposal/admission/bootstrap; invite/accept/leave | Replication scope, lineage, capacity, initialization funding, separate consent |
| Memory/context | Fragment write/revise/search; selection/compaction | Ownership, visibility, mandatory-core preservation |
| Capability/session | Inspect/discover descriptor; acquire; exec/session/read/cancel | Isolation, exact recipe, capability scope, resources |
| Artifact/evidence | Publish; inspect; adopt head; submit; review/assess | Immutable bytes/inputs, CAS head, review policy and exact versions |
| Authority/resources | Grant/revoke; fund; pause/cancel | Principal/delegate; no model self-authorization |
| Events | Read scoped snapshot/cursor; subscribe/acknowledge | Recipient/visibility; no irreversible loss on acknowledgement |

Provide query projections for work summary, individual agendas, shared proposals, commitments/dependencies, people/membership/births, artifacts, exact assessments, pending requests, learning history, capabilities, resource accounting, and diagnostic action receipts. Page everything; return immutable references for expansion rather than recursively embedding full histories.

### 18.2 Errors and UI responses

Return machine-readable code, safe message, relevant current version, retryability, and the receipt/reference when available. Required categories: `INVALID_SCHEMA`, `UNAUTHORIZED`, `SCOPE_DENIED`, `REVISION_CONFLICT`, `IDEMPOTENCY_CONFLICT`, `LEASE_LOST`, `BUDGET_EXHAUSTED`, `PRICE_UNKNOWN`, `CAPACITY_EXCEEDED`, `DEPENDENCY_BLOCKED`, `CONTEXT_TOO_LARGE`, `CAPABILITY_UNAVAILABLE`, `ISOLATION_UNAVAILABLE`, `ARTIFACT_MISMATCH`, `STALE_EVIDENCE`, `CANCELED`, `EFFECT_UNKNOWN`.

Transport retry uses the same operation ID and body. A corrected proposal uses a new operation ID with a link to the failed one. A revision conflict is surfaced; the client/persona must inspect the new state before rebasing a substantive choice.

## 19. UI specification

Retain the current UI framework and event-based architecture. Do not replace it to solve invalidation, oversized media, or viewer-lifetime bugs. Top navigation: **Work, Personas, Environments, Learning, Tools**; connections/resources/settings and existing Network live under appropriate settings/advanced views.

### 19.1 Work screen

Show the current agreed need and constraints, independent status axes, and six scoped views:

| View | Required content |
|---|---|
| Overview | Accepted purpose, changes, current collective commitments, blockers, resources, needs-user items |
| Perspectives | Each persona's shared agenda, proposed priorities, expected contribution, and attributed concerns; private records remain hidden |
| Work & outcomes | Required obligations, owners, dependency relationships, adopted/rejected/deferred improvements, missing coverage |
| People & agreements | Identity, membership, temporary commitments, birth motivation/provenance/contribution, working agreements and dissent |
| Artifacts & evidence | Native files, assembly versions, derived previews, simulations/receipts, current/stale review, reproduction instructions |
| Decisions & learning | Scope decisions, handoffs, individual/group interpretation changes, authored fragments and later-use evidence |

Never label the collective view as “what everyone thinks.” Distinguish a persona's proposal from an adopted commitment. Avoid a universal priority ranking or an averaged personality chart. A portrait or busy animation does not mean progress.

### 19.2 Persona/environment/detail presentation

Use compact rows and thumbnails for lists. Persona detail separates authored identity, modeled state, interests, experience, capability evidence, current responsibilities, relationships visible to the reader, model/context settings, and provenance. No “born as expert” badge. Environment detail shows actual resource/membership/tool availability and access scope.

An ungenerated portrait is a visible absence. Generate names and image briefs through persona actions when useful, never as a blocker to work. Images and native previews must be loaded lazily and separately from the list payload.

### 19.3 Controls and status

The person can edit constraints, approve material scope/effects, bound exploration, delegate authority, fund, pause/cancel, inspect a birth, request outside review, or accept a limited result. Persona-level settings cannot override node/user grants. Confirm consequential destructive/external commands with exact scope/payload where required.

Display activity separately from outcome/assessment: e.g. “2 active; 1 blocked,” “5 of 7 adopted obligations have qualifying current evidence,” “latest submission not accepted,” “site review pending.” Fractions show coverage, not an uncalibrated quality percentage. Unknown usage and stale cursor state remain visible.

### 19.3a Stress-test-specific projections

Show coverage as “checked among adopted outcomes; scope coverage review pending” when appropriate, not an invented global completion percentage. Expose unowned outcomes, pending continuation acceptance, bootstrap/invitation states, reviewer availability/funding, protected closeout balance, unresolved feedback dispositions, exact iteration baseline and remaining allowance, tool pending-versus-completed status, and attempted release conflicts.

Do not erase personal agendas when collective coverage is poor. Put the gap beside them so the team and principal can see the tension. A peer may decline an offer; show that as a disposition rather than impersonating acceptance. Distinguish narrative activity from actual evidence changes. A stale release is a historical result, not a disappeared result.

### 19.4 Technical lifecycle

Fetch an authorized snapshot with a stream cursor bound to that view, then replay relevant events after the cursor. Do not assume public global sequence numbers are contiguous through a filtered stream. Reconnect from the last applied cursor; snapshot again when retention expires. Use access-scoped cursor semantics to avoid exposing private event counts.

Debounce search, cancel superseded reads, invalidate only affected projections, use stable operation IDs, and enforce list/page limits. Large-list virtualization is conditional on measured need, not mandatory for tiny lists.

Artifact viewer states: `connecting` → `receiving` → `verifying` → `preparing` → `ready`, with independent failure/canceled paths. Byte transfer at 100% is not readiness. Verify source hash before claiming integrity; sandbox active HTML/SVG/native conversion; do not execute artifact scripts in the UI origin.

On close/unmount: abort fetches, release readers, terminate workers, revoke object URLs, dispose graphics resources, close sessions where scoped, remove listeners/timers, and restore keyboard focus. Provide keyboard operation, focus trapping where modal, Escape, readable status, and mobile layouts without horizontal overflow. Do not claim memory leak freedom from one screenshot.

## 20. Four-bedroom-house stress test

This is a **scenario for validation**, not a runtime sequence or construction guidance. The user's clarified scope includes architectural CAD/BIM, structure, plumbing, HVAC, electrical, coordination, appropriate calculations/simulations, native editability, and manufacturing/CAM only where agreed and sufficiently specified. Site/jurisdiction/professional inputs remain explicit and are not guessed from the user's location.

### 20.1 Two teams, one mandate

| Same clarified need, equal resources | Possible team A trajectory | Possible team B trajectory |
|---|---|---|
| Individual perspectives | Mira favors spatial alternatives; Nox has experience with coordination failures | Mira begins from the same state; Vale favors discriminating experiments |
| Initial collective work | Establish a common basis and compare two feasible arrangements | Test the uncertainty that could invalidate an attractive concept |
| First accomplishment | Comparable native alternatives and a supported selection | Evidence rejecting or refining a concept before detailed investment |
| Working agreement that may emerge | Explore within a stable comparison basis | Test consequential hypotheses before narrowing options |
| Population choice | Birth a peer for sustained integration if useful | Acquire a capability or recruit an existing peer; birth is optional |
| Distinctive improvement | Simpler maintenance/coordination | A tested spatial or performance idea |

These descriptions are illustrative, not runtime personality rules. Both teams owe the same adopted deliverables. Different first accomplishments do not permit dropping plumbing or wiring.

### 20.2 Observable execution and failure handling

| Observation | Persona/group choices | Required record/evidence |
|---|---|---|
| Initial brief is incomplete | Propose scope, ask material questions, use bounded explicit assumptions where useful | Original request, mandate revisions, assumptions and affected claims |
| Participants notice different concerns | Author different agendas; negotiate compatible commitments | Perspectives, shared proposals, accepted owners—not a scripted profession roster |
| Alternatives need actual geometry | Select/acquire tools; create native models and inspect actual views | Installation/operation receipts, native files, image-input records, dimensional checks |
| A recurring question needs attention | Learn/reallocate/recruit/birth according to judgment | Motivating observation, authorized birth or alternative decision, actual later contribution |
| Systems need design | Negotiate architectural/structural/plumbing/HVAC/electrical and integration responsibilities | Accepted commitments, input-bound models, schedules, calculations, explicit omissions |
| Discipline models must align | Adopt coordinates, units, object IDs, assembly versions and transformations | Coordinated assembly manifest and model-to-analysis mapping |
| A route conflicts with structure | Reprioritize coordination; compare alternatives instead of polishing a render | Issue on exact objects/versions, revised native files, affected checks rerun |
| A useful optional improvement appears | Run a bounded comparison without erasing the baseline | Proposal, benefits/regressions, result, adoption/rejection/deferral |
| Window/layout/utility assumptions change | Mark dependent evidence stale; negotiate revalidation order | New scope fingerprint, notifications, new calculations and equipment updates |
| Simulation fails or tool is unavailable | Diagnose, revise recipe/model, use a justified alternative, or report blocked | Actual logs, no fabricated plots or successful run |
| Fabrication is considered | Establish process/machine scope or defer executable instructions | Bounded fabrication/CAM artifacts, simulation/review where supported, separate physical authority |
| Submission is ready | Seal exact integrated versions; independent native/reproduction/coverage review | Current assessments, preserved failed checks, outside review remaining visible |
| Work ends or pauses | Deliver agreed package/limitations; hand off open work; retain selected lessons | Exact delivered version, honest outcome axes, later-transfer test |

### 20.3 House deliverable acceptance

| Area | Required evidence at the agreed level |
|---|---|
| Architecture | Four real bedrooms and agreed facilities; circulation/openings; dimensioned plans/sections/elevations; native editable source and consistent exports |
| Structure | Declared loads/materials/support assumptions, structural layout and applicable analysis at the agreed level; missing site inputs remain conditional |
| Plumbing | Native/editable supply, hot-water, drain and vent design at the frozen coordinated-design detail; fixture/network schedules, sizing calculations and connected/coordinated routes and access. Intent prose alone is insufficient. |
| HVAC | Room/system assumptions, actual load calculations, equipment/distribution/ventilation/control design, coordinated routes and reproducible performance evidence at the frozen scope. |
| Electrical | Native/editable lighting/outlets/equipment supply design, circuits/panel schedules, load calculations and protection/grounding basis at the frozen scope, with cross-document checks. |
| Coordination | Aligned native models/assembly; conflicts and access issues addressed across the submitted versions |
| Analysis | Exact inputs, transformations, solver/tool version, boundary conditions, run receipts, warnings, results and limitations |
| Editability/reproduction | Native reopening; representative edit on a copy persists/regenerates; independent reproduction of selected exports/checks |
| Fabrication | Only included components/processes; actual native manufacturing inputs and target configuration if machine instructions are produced |
| Outside assurance | Site/jurisdiction/qualified professional/physical evidence clearly pending where absent; digital success is not construction authorization |

Tests must deliberately remove a system, change an input after review, plant a clash, falsify a simulation narrative, and interrupt execution. The evaluator must reject the relevant completeness/currentness claim without requiring a particular CAD application or a prescribed sequence of persona actions.

## 21. Generality beyond houses

Use the same work/record/event contracts for software changes, dataset cleaning, creative work, scientific investigations, job applications, marketing, household organization, conversation, and ongoing services. These examples are not kernel task classes.

A simple dataset cleanup may need one persona, one reproducible script, and no birth. Creative work may need drafts and author judgment rather than numerical scoring. A scientific failure may be a useful accomplishment. Job or social submission needs external-write authority and receipts. Circuit work needs appropriately specified conditions and actual design/analysis evidence; bench work remains separately authorized. Ongoing work requires durable authorized triggers, expiry/review conditions, bounded wakes, and a visible stop mechanism.

Different teams may notice different improvements across every domain. Hard facts, permissions, accepted requirements, and evidence honesty do not become optional because a group has a distinctive culture.

## 22. Rust-only implementation mapping and deletion plan

The only runtime baseline is `rewrite/design-first` at `d3339d30fa883c21c7935a2d009e3a58f480a256`. All code below is a proposed Rust delta, not a port of another implementation. Directory entries establish paths; targeted reads establish only the behavior described in the source register. [R01–R07]

| Existing Rust target | Required implementation work |
|---|---|
| `src/contract.rs` | Keep `Command` and Schemars as the authoritative operation definition. Add typed fragments, mandates, perspectives, exact agreement endorsements, commitments, scoped birth/admission, invitations/consent, grants, and criterion-bound assessment. Avoid one unconstrained `record.write` that can mint authority. |
| `src/types.rs` | Extend typed payloads and `ModelRequest`/`ModelResponse`; preserve 32-hex IDs and numeric revisions. Separate authoritative current state from selected persona memory. Add context/accounting manifests and orthogonal status projections. Update `protocol()` only when enforcement exists. |
| `src/runtime.rs` | Extend `Node` admission, dispatch/mutation and request construction. Derive actor/root from authenticated scope; recheck revisions, fences, cancellation and grants after inference; reserve budgets before calls; bound birth; keep one current decision per identity and no automatic idle loop. |
| `src/store.rs` | Extend existing SQLite transactions for typed-record heads/links, grants, reservations, initialization capacity, leases, action digest conflicts and outbox. Keep FTS and prior revision/action bytes. Make assessment currentness explicit in `facts()`/query projections. |
| `src/runtime.rs` + local inbox helpers in `src/store.rs`; `src/delivery.rs` only for continuity compatibility | Implement local birth/invitation/commitment/review notification transactions in runtime/store. The inspected delivery module is continuity forwarding; do not misplace a new local mailbox subsystem there or expand federation. Preserve paging, explicit acknowledgements and replay safety. |
| `src/provider.rs` | Replace Codex app-server and executable bridge transports in the supported inference path. Keep one provider contract; implement HTTP adapters with actual capability/usage/media/error/cancellation handling. |
| `src/main.rs` | Replace executable-provider configuration/default registration with typed HTTP endpoints and secret references. Pin explicit initial model; expose root resource/birth limits and required isolation configuration. Preserve explicit empty-node startup. |
| `src/jobs.rs` | Extend tracked command execution with enforceable isolation, input snapshots, resource/network bounds, brokered credentials, session lifetime, cancellation and durable results. Keep it generic; do not introduce house/browser job types. |
| `src/api.rs` | Validate principals and requested actor/run scope. Expose versioned operations, receipt lookup, scoped queries, truthful projections, replayable cursors and approved artifact streams; enforce payload-size/privacy limits. |
| `src/curricula.rs` and `curricula/` | Keep curricula as ordinary work content. Adapt vocabulary to fragments and new evidence bindings without a domain/course-specific execution path. |
| `integtest/behavior.rs` and `integtest/live.rs` | Add Rust public-API mechanics and bounded live campaigns for character/group differences, feedback-to-edit, retained correction, birth/restraint, house depth and disturbance. Preserve failed runs and stable operation identities. |
| `src/network.rs`, `src/continuity.rs` | No transport redesign. Validate new schema compatibility, deny unsafe automatic execution/import, and test legacy data. Do not claim distributed exclusivity the current contract explicitly disclaims. |
| Matching UI `rewrite/design-first` | Generate contract via the Rust binary; implement Section 19's perspectives/agreements/commitments/evidence projections. Pin the sibling UI revision separately; no current-main UI assumptions. |
| Matching design `rewrite/design-first`, runtime `docs/`, `scripts/package.mjs` | Synchronize normative vocabulary, exact release revisions, packaging and evidence links. Remove unsandboxed/process-provider success claims only after new paths pass. |

Proposed small extraction modules **only if useful**: `src/work.rs`, `src/fragments.rs`, `src/birth.rs`, `src/authority.rs`, `src/context.rs`, `src/evidence.rs`, `src/sandbox.rs`, and `src/providers/{mod,http,openai,anthropic}.rs`. These are not observed files or mandatory services. Reuse `Store::write`; do not create independent state stores for each module. Reuse the existing reqwest dependency. Add dependencies only when a concrete implementation choice requires them; retain and update Cargo.lock deliberately.

### 22.1 Specific behavior fixes, not just new types

1. Replace the supported provider process transport **and** the implicit Codex registration in runtime/startup; changing `provider.rs` alone is insufficient.
2. Move active memory selection to persona/work scope. Do not carry another work's grants or private task context into the next work.
3. Distinguish learner-owned fragments from ordinary documents. Do not claim an installation receipt, selected fragment, or good self-description proves competence.
4. Add bounded birth around `persona.create`; reservation + identity + initialization intent must commit atomically. Invitation/consent and commitment acceptance are separate operations.
5. Do not let public operation arguments, generic record payloads, imported artifacts or birth seeds mint root authority or money.
6. A successful `exec` is necessary evidence for claims requiring execution, not a universal proof of acceptance. Extend baseline `assess` with adopted evidence policy so a subjective conversation can be accepted without ceremonial shell calls while simulations cannot pass without actual runs.
7. Preserve the current stop-on-first-action-error contract and already applied receipts. Add deliberate `yield`/quiescence rather than billing indefinite empty decisions.
8. Replace whole-work verdict aggregation with current, submission-bound applicability and distinct outside-validation/user-acceptance status.
9. Implement isolation before granting autonomous installers or sensitive credentials. The baseline's process tracking is not an assessor secrecy boundary.
10. Guard record publication at the filesystem boundary; a persona path or digest declaration is not enough to grant read access to host-private files.

### 22.2 Baseline commands and new gates

The following baseline build/test commands are declared by the Rust README/Cargo configuration; they were **not run for this delivery**. [R02, R03]

```sh
git switch rewrite/design-first
git rev-parse HEAD                  # compare to the pinned source revision
cargo build --locked --release
cargo test --locked --test behavior -- --test-threads=1
```

Build the sibling branch UI with its documented `npm ci`, `PERSONAS_BIN=../ai-personas/target/release/personas npm run contract`, and `npm run build` path. Then run its browser suite against fresh Rust nodes. Freeze exact runtime/UI/design commits and schema digest together. Existing provider fixtures may be retained as test scaffolding during migration, but they cannot stand in for production HTTP inference or an alternate runtime.

Delete retired executable inference transports only after the HTTP replacement is exercised; preserve old logs for evidence. Remove duplicate authoring aliases only when their semantics are truly redundant. Keep cheap Rust invariant tests. No mandatory planner, profession registry, group personality optimizer, vector database, or imported backend framework is needed.

## 23. Migration, operations, privacy, and federation

### 23.1 Rollout without rewriting history

Freeze baseline runtime/design/UI/schema/fixtures and preserve a restorable backup. Inventory existing equivalents for every required semantic before adding code. Start the new projection/contracts with fresh bounded pilot work behind one feature gate; never let old and new paths both own mutable grants or budgets.

The baseline store refuses a mismatched contract and recommends a fresh node. Use fresh v2 pilot nodes as the default. Retain v1 data with its matching read-only application; an explicit import tool, if needed, references original Rust record/action/artifact bytes rather than silently opening the old database. [R06] Mark missing bindings as `legacy_unbound`/`unverifiable`; do not synthesize endorsements, evidence, acquisitions, or learning. Rebuild indexes and compare record counts/hashes. Keep deprecated readers only for actual retained formats, not duplicate current authoring paths.

Cut over one mutation boundary at a time with compatibility tests and explicit schema versioning. A rollback restores code/projections/backups but cannot undo an external action; reconcile effect receipts before resuming either version. Freeze running long-lived jobs or migrate them explicitly rather than losing ownership.

### 23.2 Deployment and observability

First release targets a supported Linux host with the Rust node, the isolation backend and managed supervisor implemented for this revision, and the pinned matching UI. The baseline job tracker is not evidence that the required containment already exists. Use a low-privilege account, separate secrets, immutable/restricted tool dependencies, bounded disk/logs, encrypted sensitive backups, and tested restore. Fail startup or affected capability admission when required isolation is unavailable.

Correlate work, run, actor, wake, call, operation, job, artifact, assessment, authority, and budget IDs. Monitor queue age, rejected admissions, lease loss, unknown effects/usage, context overflow, missing evidence, projection lag, and viewer failures. Metrics expose facts; they do not rank personas' worth.

A local unauthenticated public read should never be the privacy assumption for sensitive work. Configure private-by-default work data; public publication is explicit. Apply CSRF/CORS/session-origin protections as appropriate to the actual UI transport; do not keep long-lived operator credentials in browser storage by default.

### 23.3 Privacy and retention

Append-only provenance is not a license to retain private content forever. Use record-level policy references, redaction/tombstone/retention semantics, and deletion of protected payloads or encryption keys where the configured policy requires it. An audit can retain a minimal non-content event of deletion without exposing sensitive hashes or titles publicly.

Derived summaries, fragments, search indexes, thumbnails, caches, exports, and backups inherit source access/retention restrictions. Revocation stops future access and delivery but cannot promise to erase already exported data. Record sharing limitations clearly. A newborn receives only explicitly shareable seed material, never privileged parent state.

### 23.4 P2P and remote people

Keep `src/network.rs` and `src/continuity.rs` out of a transport rewrite. The current `continuity.handoff` contract explicitly says it is routing, not distributed exclusivity. Do not claim source-fence/destination-activation safety from another implementation. [R04]

For the new contract, require schema/access validation on transfer and reject unsupported v2 activation or publication. Until all new grants, reservations, work relations and active-identity bindings are represented safely, deny exporting or activating an active v2 work identity rather than silently omitting its authority or billing state. Read-only evidence bundles may use existing verified-byte transfer paths where compatible.

A remote peer or integrity-checked bundle is not automatically a local authorized actor, member, tool, or budget holder. Imported recipes do not auto-run. Node transport identity and artifact hashes do not prove per-persona authorship or technical correctness. Any stronger attestations require a separately defined and tested protocol.

Global exclusive identity movement and expanded federation remain outside this release. Local actor fencing is required; cross-node exclusivity must be shown as unavailable until separately implemented. Do not rely on an untested cross-node guarantee to protect the new execution or resource model.

## 24. Acceptance campaign and implementation sequence

### 24.1 Mechanical tests (zero model calls where possible)

| ID | Test and pass condition |
|---|---|
| M01 | Same operation/body replays the same receipt; changed body conflicts; unauthorized receipt access is denied. |
| M02 | Concurrent head updates preserve one adoption plus explicit conflict alternatives; no silent overwrite. |
| M03 | Lost/expired actor and writer fences reject late mutations; genuine late receipts remain for accounting. |
| M04 | Inbox/outbox crash/restart preserves delivery and deduplication without a new grant. |
| M05 | Concurrent births respect root population/rate/depth/call bounds; retries create one identity; initialization is funded. |
| M06 | Birth, membership, and commitment acceptance are separate; newborns inherit no secrets or extra grants. |
| M07 | All descendant calls/retries/compaction/reviews are charged; uncertain usage is not silently refunded. |
| M08 | Context isolation and overflow preserve mandatory authority/constraints; superseded/forbidden memory is not silently active. |
| M09 | Changed criteria/input/manifest/policy makes prior review stale; queued propagation never leaves a false current pass. |
| M10 | Missing analysis inputs, failed execution, unsupported image input, and fabricated output references cannot satisfy evidence. |
| M11 | Cross-work/private graph/search/UI leaks are denied, including revoked resources and summaries. |
| M12 | Malicious packages/artifacts/prompt injection cannot access keys, assessor state, ungranted network/effects, or privileged execution. |
| M13 | Ambiguous external outcome becomes `effect_unknown`; no blind duplicate publication or charge. |
| M14 | UI uses authoritative projections and correct stream replay; viewer close disposes resources and restores focus. |
| M15 | Provider conformance covers actual capability discovery, malformed/refused/partial output, cancellation, retry and model ceiling. |
| M16 | Historical import preserves original bytes/provenance and unknown bindings; backup restore and rollback reconcile external receipts. |

### 24.2 Behavioral evidence

| ID | Test | Required observation |
|---|---|---|
| B01 | Same need, different personas | Meaningful variation in attention/methods/artifacts, assessed separately from requirement adequacy |
| B02 | Same persona, different partners | Interaction changes behavior without merely erasing continuing identity |
| B03 | Same members, different shared history | Relationship/agreement context changes coordination where relevant |
| B04 | Character/relationship ablation and names-only substitution | Evidence that differences are not only wording, labels, or random sampling |
| B05 | Feedback-to-edit-to-review | One persona's evidence changes another's exact artifact and an independent check verifies it |
| B06 | Unexpected useful improvement | An unprompted opportunity is tested and improves the agreed result or produces an informative rejection |
| B07 | Evidence-driven reprioritization | A disturbance changes accepted work instead of blind continuation |
| B08 | Useful birth and no-birth restraint | Expansion yields distinct work when useful; simple work can finish without growth |
| B09 | Corrected learning and counterevidence | Later behavior improves versus matched memory-withheld runs; erroneous advice is revised |
| B10 | Model-switch continuity | Identity/learning and boundaries survive a new allowed provider/model without inherited provider-private authority |
| B11 | Full house plus disturbance | Native coordinated architecture/structure/plumbing/HVAC/electrical and appropriate analyses, revalidation, exact review and honest outside limits |
| B12 | Unrelated needs | Software/data/writing/research/conversation/ongoing fixtures use the same core semantics without new task-routing branches |

Use repeated matched cohorts with identical user information, tool opportunity, and **total** budget; compare one continuing persona, a fixed group, and an adaptive group. Separately isolate memory, character, relationship history, model and tool effects. Freeze actual model IDs/settings and recorded capabilities; counterbalance presentation/order effects. Blind quality review where possible and preserve all attempts, evaluator versions, and remaining unused budget.

Different behavior is not automatically better; identical choices can be correct when evidence is decisive. Predeclare task-specific quality/cost/robustness thresholds and repeat counts before a campaign; the attachments do not justify a universal numerical success-rate threshold. Never weaken a rubric after failure without publishing a versioned correction and preserving the original outcome.

### 24.3 Implementation milestones, not calendar promises

| Milestone | Deliverable | Exit gate |
|---|---|---|
| P0 — source/contracts | Freeze the Rust baseline and sibling branches; specify root/participation/bootstrap, evidence and pending-action semantics | One target; retained failures; focused static defects mapped to source |
| P1 — executable foundation | HTTP provider conformance, transactional authority/funding, fenced actor execution, safe job containment, actual-completion barrier, durable wait/replay, local notification projection | Zero-live-call mechanism tests including M01–M13 and M15; containment and provider readiness precede live autonomous work |
| P2 — small useful cooperation | Fresh founders, accepted continuation, scope/coverage, individual contexts, commitments, feedback disposition and exact assessment | A bounded real output is changed by a peer's evidence and independently checked; no ceremonial roles |
| P3 — adaptation and population | Bootstrap consent/access, protected closeout funding, retained correction, negotiated interfaces/iteration, no-birth restraint | B01–B10 with budget-matched controls; no claim that source/model tests prove useful emergence |
| P4 — house and generalization | Frozen coordinated-design scope, actual native disciplines and analyses, disturbances, release seal, unrelated tasks | B11/B12 and fresh repeats; digital and external prerequisites remain separate |
| P5 — release | UI replay/disposal/access, runtime/schema/UI/docs consistency, restore, security/load and cost reports | M14/M16, additional cases below and predeclared behavioral thresholds; no unsupported currentness claim |

Provider and isolation work may proceed in parallel with records/UI, but must pass before funded autonomous tool experiments. Do not defer these prerequisites to the final product milestone.

### 24.4 Additional counterexample-derived tests

| ID | Required regression |
|---|---|
| M17 | Pending `exec` blocks/suppresses the unobserved same-decision suffix, including crash replay; no early read/publish/submit. |
| M18 | Newborn can decide on an invitation using only exact preview/seed access before membership; ungranted parent/work data remains inaccessible. |
| M19 | Work without any accepted continuation responsibility is visibly unowned; missing adopted outcomes never inherit another owner's completion. |
| M20 | Conditional evidence cannot qualify an unconditional claim; authorizing an assumption does not confirm a fact. |
| M21 | Consequential finding remains open after delivery/acknowledgement/compaction; a late critical notice is not starved behind ordinary messages. |
| M22 | Cyclic final prerequisites are diagnosed; explicitly permitted version-ready exploration can proceed; unresolved final checks still block full acceptance. |
| M23 | Ordinary work/birth cannot use the closeout allocation; authorized transfers conserve the root; unknown exposure stays reserved. |
| M24 | Coupled assembly adoption and final release are transactional; either event ordering for update-versus-seal preserves historical/current distinctions. |
| M25 | Metadata-only loops cannot extend root/self-wake ceilings; negative experiments and useful questions remain representable. |
| M26 | Both event orderings for terminal-result-versus-await registration keep satisfied work runnable or durably notified. Preserve the existing wait regression too. |

Start with a small Rust public-API fixture for `exec` followed by publication using an already-existing file, since mere absence of a newly generated filename may mask the sequencing defect. Test a delayed successful writer, delayed failing writer and uncertain termination. Then exercise outbox/lease/restart failure points. No model call is required to test those causal mechanics.

## 25. Delivered materials and verification limits

`AI-PERSONAS-RUST-SPEC-v1.2.md` is the complete normative design; its HTML renders the same text. `STRESS-TEST-REPORT.md` contains the authored observable house/team traces, counterexamples and evidence limits. `CHANGES-v1.1-to-v1.2.md` and the unified Markdown diff make the corrections inspectable. `protocol-check.mjs` is an executable abstract protocol checker, not a Rust runtime or a substitute implementation. Its fixture vocabulary is deliberately small and not the public wire schema.

`verification.json` records exactly what was checked in this delivery. No Rust toolchain was found on PATH; no Rust code was compiled and no repository test was run. No repository file was changed, no inference provider was called, and no native engineering or physical task was executed. Abstract passing guards are evidence only about their explicit predicates and enumerated cases. They do not prove unmodeled concurrency, actual agents' choices, performance, security, or engineering adequacy.

The retained v1.1 source observations remain historical at their pinned commit. Additional source reads in this review are listed below. No other runtime branch is an implementation basis. No UI integration or new browser lifecycle evidence is claimed merely because the document was rendered as HTML.

## Source register and provenance

**A1 — supplied prior report.** `deep-research-report (1).md`. Design basis for persistent personas, OCEAN/VAD, fragments, acquired capabilities, API-only inference, context, artifacts/review, curriculum, UI and acceptance. Historical implementation claims are not assumed current without Rust evidence.

**A2 — supplied subsequent proposals and conversation.** `AI-PERSONAS-EMERGENT-DESIGN.md` and the earlier consolidated specification, plus user clarifications about individual/group characteristics, emergent priorities, full engineering depth, birth and Rust-only scope. Reused for behavioral requirements only. Another runtime’s source, tests and implementation guarantees are not used as Rust evidence.

All repository observations below were retrieved through the authenticated GitHub connector on 16 September 2026, pinned to `d3339d30fa883c21c7935a2d009e3a58f480a256` except the branch-list resolution. File references are source identifiers, not execution claims.

**R01 — branch resolution.** `ai-personas/ai-personas`, branch collection: `rewrite/design-first` resolves to `d3339d30fa883c21c7935a2d009e3a58f480a256`.

**R02 — Rust README.** `README.md`, blob `0e97d9155c91a430dc46e0455d4fd9a53c4e2821`. Rust runtime, empty-node startup, sibling design/Preact UI branches, process-based providers, unsandboxed execution, limited local review boundary, build/test/package instructions, incomplete overall acceptance.

**R03 — Cargo manifest.** `Cargo.toml`, blob `b0eba4da5c6d771173c87d0afc473b70591e8aa5`. Package/edition, Tokio/Axum/rusqlite/Serde/Schemars/reqwest/libp2p dependencies; `personas` and `integtest` binaries; `integtest/behavior.rs` test target. These are the checked-in dependency declarations, not recommendations for latest versions.

**R04 — Rust operation contract.** `src/contract.rs`, requested lines 1–440, blob `4aedf3a598725c769ed6c2abb6509c504d3e044e`. The complete command enum in the visible response contains identity, work, exec/job, document/context, tool registration, messages, artifacts/submission/review, requests, waiting, peer transfer and continuity operations. `persona.create` fields and `assess` execution condition establish the specific gaps discussed here. `continuity.handoff` explicitly disclaims distributed exclusivity. Response tail after the command/validation material was truncated; no claim is based on the omitted tail.

**R05 — Rust wire types and protocol.** `src/types.rs`, lines 1–240, blob `21f9eb6d2f52e13a4fca399c0e21627179a2b754`. `Record`, `Operation`, `Action`, `ModelRequest`, usage, IDs, contract identifier, and `protocol()`. Supports the documented broad context, attribution fields, unsandboxed statement, stop-on-first-action-error, explicit input acknowledgements, and empty-decision continuation behavior. No per-persona signature guarantee is inferred from these types.

**R06 — Rust storage.** `src/store.rs`, lines 1–150, blob `b760db0736fd47c13412232146b1657b74a4a3d8`. SQLite configuration, baseline tables, FTS5, mismatch refusal, `Store::write` transaction, query facts call sites. Later store functions were not fully audited in this correction.

**R07 — source directory.** `src/` listing at the pinned commit confirms the existing module paths used in Section 22. File existence alone does not establish complete implementation behavior; mappings are proposed work.

The new Rust-only package removes claims based on another branch’s isolation, founding cohort, signed-birth protocol, actor supervisor, funding machinery and cross-node activation safety. It also excludes prior externally sourced model-tier claims. All final requirements are proposed engineering decisions; examples and UI data are illustrative.


**R08 — additional targeted Rust runtime read.** `src/runtime.rs` at the same pinned commit, lines 200–430, 700–1005 and 1000–1380 (overlapping boundary intentional). Static paths inspected: `operate`, `dispatch`, `request`, `work_loop`, `apply_decision`, review/assessment and `wait`. `exec` dispatch calls `jobs::start`; `operate` marks it running; `apply_decision` tests failed receipts, while foreground waiting is at the next loop entry. The wait mutation already checks newer unacknowledged input transactionally. No executable reproduction is claimed.

**R09 — additional Rust job read.** `src/jobs.rs`, lines 1–220, blob `71b527cc41421a555fd49d11c157d723de9a8580`. `start` spawns a supervisor, waits on it in another thread and returns its PID immediately; `run` subsequently records terminal command output. Supports the pending-versus-completed distinction, not a claim of sandboxing.

**R10 — additional Rust delivery read.** `src/delivery.rs`, lines 1–260, blob `22714f8d866f172d166d7efe464a1e818026cc69`. Continuity-forwarding responsibilities and durable remote delivery helpers. Corrects the earlier overly broad local-mailbox implementation mapping.

**W01 — research cross-check.** Cemri et al., *Why Do Multi-Agent LLM Systems Fail?*, arXiv:2503.13657. The study distinguishes system-design, inter-agent coordination and verification/termination failures. Used as a research sanity check, not empirical evidence about this repository or a reason to introduce fixed professions.

**W02 — synchronization reference.** Tokio, `tokio::sync::Notify` official API documentation, retrieved for this review. `Notify` carries no data and repeated notifications can coalesce to one permit. Supports retaining durable predicate/inbox state rather than relying on wake notifications as the ledger. No particular latest dependency upgrade is prescribed.
