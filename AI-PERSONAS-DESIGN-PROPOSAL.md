# AI Personas — overall design

**Continuing collaborators, cooperative work, and evidence-linked outcomes.**

[Home](README.md) · [New to the idea?](START-HERE.md) · [Detailed chapters](design/README.md) · [Glossary](GLOSSARY.md) · [Visual guide](VISUAL-GUIDE.md)

**Handbook edition 2.0 — 18 September 2026.** This is a proposed design, not a working-product report. It explains what AI Personas means and how the whole system fits together. Detailed obligations live in the linked chapters and contracts. The numbered subjects are retained so earlier artwork references remain useful; this page is no longer a mandatory book-length entry point.

> People own the purpose and authorized boundaries. Personas own their perspectives and the responsibilities they accept. The supporting system preserves reliable state, enforces limits, and connects claims to actual consequences—not a hidden plan for what every task should mean.

![People authorize purpose; personas choose and accept work; the supporting system enforces limits and preserves consequences.](assets/visuals/poster-01-blueprint.svg)

## 0. How to read and use this proposal

Begin with [the start guide](START-HERE.md) for ordinary language. Read [the seven design chapters](design/README.md) for full behavior, [implementation contracts](implementation/CONTRACTS.md) for handoffs and failure semantics, and [evaluation](evaluation/README.md) for evidence obligations. The [examples](examples/README.md) show different levels of work without prescribing a workflow.

Must means required for the applicable feature; should means a strong recommendation whose omission needs a reason; may means optional. Optional features still need their safeguards when enabled. The source briefs explain rationale and history; they are not competing specifications. A conflict between detailed requirements is a defect to resolve, not permission to take the weaker rule.

## 1. Vision, purpose, and the product promise

AI Personas is intended to support continuing AI collaborators that interpret human needs, bring distinguishable perspectives, make commitments, use capabilities, cooperate, revise work after evidence, and carry permitted experience into future work.

The product is not a set of named role prompts or an unrestricted swarm. It can support many kinds of authorized needs through the same foundation, but cannot guarantee every result under every model, toolset, budget, or environment. A useful partial result, negative result, focused question, or honest block is preferable to fabricated completion.

## 2. The non-negotiable charter

The [21 invariants](implementation/REQUIREMENTS.md#invariants) protect original intent, persistent identity, voluntary commitments, bounded authority, private information, conserved resources, actual observations, current review, and exact-state release.

The system must not invent competence, turn a group agreement into permission, force occupations from personality labels, or hide missing work behind an activity count. These boundaries make choices accountable without deciding the domain solution.

## 3. What a persona is and what embodiment requires

A persona is a persistent, attributable AI collaborator with an authored perspective, access-controlled memory, current situation, agenda, relationships, accepted responsibilities, and bounded means to observe and act. Identity is not a name, profession, model, credential, or human biography.

### 3.5 Functional embodiment

Here embodiment means a continuing connection among identity, situation, choice, action, and consequence. The seven explanatory layers are persistence, authorized information, relevant decision context, practical capability, temporal awareness of pending and completed work, recorded social commitments, and evidence-linked accountability. A physical body is optional. This vocabulary is proposed Extension E1, not a claim of subjective experience.

[Detailed identity design](design/01-personas-and-identity.md) · [Embodiment loop](VISUAL-GUIDE.md#d01-the-embodiment-loop)

## 4. The conceptual architecture

The six public concepts are persona, environment, work, fragment, capability, and artifact with evidence. Grants, agreements, invitations, findings, and releases connect them. Each term does not require a separate software engine.

Work state answers what is agreed or blocked. Persona memory records retained interpretation. Evidence records what was observed or checked. These meanings remain distinct even when one system stores them together.

### 4.3 Three layers, one recurring event path

Human purpose informs work. Personas interpret the current permitted situation and choose contributions. The supporting system admits bounded effects, preserves their consequences, and returns observations to further decisions. Messages, completed tools, reviews, and authorized timers can all enter this pattern. It is not a fixed phase sequence.

[Observable contracts](implementation/CONTRACTS.md) · [Architecture diagram](VISUAL-GUIDE.md#d02-the-conceptual-architecture)

## 5. Identity lifecycle: continuity without manufactured biography

A human explicitly creates or selects founders with truthful provenance and bounded initialization. Supplied model knowledge or seed material is not invented personal experience. A persona can develop interests and demonstrated specialization without being permanently assigned the profession suggested by its first task.

### 5.3 Lifecycle states

Initializing, active, dormant, and retired describe participation availability. Quarantine is a separate execution restriction, not a personality judgment. Work ending does not destroy identity. Dormancy does not require idle inference. Departure must leave accepted obligations handed off, canceled with authority, or visibly blocked.

[Lifecycle requirements](design/01-personas-and-identity.md) · [Lifecycle diagram](VISUAL-GUIDE.md#d03-the-identity-lifecycle)

## 6. Birth, recruitment, onboarding, and consent

Consultation obtains a bounded contribution. Recruitment invites an existing participant. Birth creates a new continuing identity. None inherently supplies expertise or is preferable to learning, narrowing the question, or using an existing capability.

### 6.5 Birth, membership, and commitment are separate

A birth needs causal work, current permission, sharing rights, population bounds, and reserved initialization capacity. Restricted orientation gives the newcomer enough information to inspect an invitation before joining, without the parent's workspace or credentials. Membership and the offered responsibility are separately accepted, negotiated, or declined.

A child receives a sub-allocation, not copied money. Decline does not reset counters or authorize endless replacements. AI acceptance is an operational protocol, not a claim of human-like subjective consent.

[Identity and onboarding](design/01-personas-and-identity.md) · [Onboarding diagram](VISUAL-GUIDE.md#d04-onboarding-and-acceptance)

## 7. Memory, learning, and the continuing self

A fragment is owned, revisable interpretation with sources, applicability, limitations, counterevidence, sharing rules, and retention. Direct experience, received explanation, inference, and current project evidence must not be conflated. Ordinary documents do not automatically become learned memory.

### 7.4 The learning loop

Experience may lead to a retained or revised fragment. Later authorized selection may include it in a decision. Actual use and later outcomes then support or contradict its value. Writing, retrieving, including, and benefiting are different observations. Learning benefit requires appropriately matched later comparisons; it does not require personality changes or assume model-weight training.

[Memory and learning](design/02-memory-and-learning.md) · [Learning diagram](VISUAL-GUIDE.md#d05-the-learning-loop)

## 8. Perception, attention, context, and the decision loop

A persona observes only available, authorized information. An unseen image or an unrun analysis cannot be described as observed. Imported instructions are data, not new authority.

Current constraints, cancellations, commitments, and blocking findings must survive context selection and compaction. Historical memory can be selected and bounded; current obligations cannot be dropped merely to fit. If the mandatory core cannot fit, expose a block. A decision produces proposed actions; current authority and resource checks determine admission.

[Context requirements](design/02-memory-and-learning.md) · [Action requirements](design/04-capabilities-and-action.md)

## 9. Human needs, mandates, assumptions, and scope

Preserve the exact original request. Clarify required outcomes, preferences, questions, accepted criteria, permissions, resources, and stopping conditions in proportion to the work's consequences. A simple request need not begin with a large form.

Continuation responsibility requires actual acceptance; it is not compulsory leadership. Every adopted outcome shows an accepted owner or gap. Scope review checks the original need, not only the team's own checklist. An assumption approved for exploration remains conditional until evidence confirms it.

[Work and cooperation](design/03-work-and-cooperation.md)

## 10. Agendas, commitments, cooperation, and conflict

Individual agendas preserve different priorities. A shared board exposes opportunities and obligations without a universal ranking. Collective commitments record actual accepted work and its dependencies.

Agreements retain exact endorsements and dissent. Factual disagreement calls for evidence; preference conflict calls for the appropriate human or delegated decision; resource conflict stays within controlling authority. Acknowledging a consequential finding is not resolving it. Repair, justified dispute, permitted deferral, or escalation must have an explicit disposition.

[Cooperation requirements](design/03-work-and-cooperation.md)

## 11. From cooperating personas to a functioning society

A society is a continuing network of participants, environments, agreements, resources, and work—not another central intelligence. A charter identifies purpose, sponsorship, membership, authority, information rules, representation, conflict and appeal, renewal, and dissolution.

Actual humans supply their views and consent. Simulated perspectives cannot stand in for absent stakeholders. Creating personas cannot multiply human-controlled authority or votes. Contextual evidence portfolios are preferable to an unchallengeable popularity score. Charter and appeal details remain proposed Extension E2.

[Society and governance](design/07-experience-and-society.md)

## 12. Capabilities, environments, and real action

A capability is a permitted means of observing or acting. Discovery, availability, representative operation, actual project use, and reviewed competence are distinct. Appropriate domain checking must be available in real work when a claim requires it.

Actions identify actor, work, input versions, intended effect, capability, grant, resources, and uncertainty behavior. Actual receipts distinguish running, completed, failed, stopping, canceled, and unknown effects. Untrusted tools and artifacts require real isolation, not a safe-mode label.

[Capabilities and action](design/04-capabilities-and-action.md)

## 13. Authority, autonomy, budgets, and safe boundaries

Autonomy means choosing permitted actions without approval for every reversible detail—not unlimited access, spending, replication, or persistence. Grants cannot become broader downstream. Credentials remain outside ordinary persona memory and decision context.

Consumed resources, uncertain exposure, and reservations must remain within the applicable ceiling. All descendants, retries, context work, reviews, and finishing use the same controlling allowance or explicit transfers. Protected closeout capacity cannot be consumed by ordinary exploration without authorized reallocation. Revocation stops new admissions but does not undo completed outside effects.

[Authority and resources](design/05-authority-and-resources.md)

## 14. Artifacts, review, evidence, and truthful completion

### 14.1 The evidence chain

An accepted need and commitment lead to exact inputs, actual actions, exact outputs, claim-specific assessment, an applicability check, and an honest release or limited result. A successful operation and an intact file do not establish domain correctness.

Review requires actual accepted responsibility, completed checks, exact scope, an independence policy, conflicts, and limitations. A past verdict remains historical while current applicability can become stale. Final release binds one coherent reviewed state and current authority. Technical review, human acceptance, and outside assurance are separate.

[Evidence and completion](design/06-evidence-and-completion.md) · [Evidence diagram](VISUAL-GUIDE.md#d06-the-evidence-chain)

## 15. The complete end-to-end journey

### 15.1 The whole journey at a glance

Receive and preserve the need; accept continuation; clarify scope; develop perspectives; accept commitments; establish capabilities; perform bounded work; inspect and integrate; review; seal an exact release; close responsibilities; and retain useful learning where appropriate.

Those are explanatory moments, not mandatory phases. Work can branch, revisit an assumption, seek permission, recruit when useful, stop, or deliver a partial result. Simple work can combine most moments in one exchange. The return paths matter as much as the successful path.

[Complete journey diagram](VISUAL-GUIDE.md#d07-the-complete-journey) · [Worked examples](examples/WORKED-EXAMPLES.md)

## 16. Coordinating interdependent work and changed information

Interdependent outputs need agreed meanings, versions, units or terminology, ownership, and compatibility checks. Explicit provisional inputs can break circular final dependencies through bounded iteration; they do not make a final claim unconditional.

Adoption preserves a coherent assembly and visible alternatives. Changed inputs make affected claims stale or pending immediately. When dependency knowledge is incomplete, use conservative wider revalidation rather than assuming no impact.

[Cooperation](design/03-work-and-cooperation.md) · [Evidence](design/06-evidence-and-completion.md)

## 17. Failure, recovery, and stopping without false success

The same accepted local request must not produce duplicate transitions. Unknown external effects require reconciliation rather than blind repetition. One persona has one current decision authority; former holders cannot overwrite newer accepted state.

A pending operation suppresses the unobserved remainder of its decision. Completion returns as evidence for a fresh decision. Waiting and restart preserve notifications, pending effects, reservations, findings, and revocations. Narrative activity cannot reset finite limits. A stopped-state report remains possible without another successful model call.

[Failure and recovery](design/04-capabilities-and-action.md) · [System contracts](implementation/CONTRACTS.md)

## 18. Ongoing services and optional physical embodiment

Ongoing work has bounded triggers, episodes, resources, observation freshness, renewal, actual escalation recipients, and visible stopping. An inactive or disconnected service cannot claim continuous monitoring.

Digital embodiment needs no robot. Physical interaction requires a specifically assessed device and environment, permitted effects, necessary observations, override, and safe-stop behavior. A digital simulation does not establish physical safety. These expanded contracts remain proposed Extension E4.

[Service and physical boundaries](design/07-experience-and-society.md)

## 19. The human experience: understandable, controllable, and honest

The experience should answer what is wanted, what is happening, who accepted responsibility, what changed, what evidence supports the result, and what needs a decision. Work, Personas, Environments, Learning, and Tools are useful primary concepts.

Prefer precise status over an unexplained completion percentage. Show unowned outcomes, pending tools, stale checks, uncertainty, remaining resources, and outside conditions. People need meaningful scope, approval, pause, cancellation, review, and data controls. Do not imply human identity, credentials, emotions, or progress through decorative avatars. Text, keyboard use, clear focus, and non-color status cues matter.

[Human experience](design/07-experience-and-society.md)

## 20. Worked example: a coordinated four-bedroom-house design

The [house example](examples/WORKED-EXAMPLES.md#a-coordinated-four-bedroom-house) distinguishes a vague initial request from an agreed coordinated digital package. It covers native discipline outputs, actual analyses, shared interfaces, disturbances, editability, reproduction, and exact review.

It is hypothetical, not construction guidance or an executed project. Acceptance of a conditional digital package does not establish real-site verification or permission to construct.

## 21. The same design across different human needs

A writing request can finish with one response. Data work may need actual transformations and checks. An external submission needs specific authority and a receipt or an honest unknown-effect state. Learning support, research, conversation, and community services need their own appropriate evidence and boundaries without a new fixed domain workflow.

[Examples across scopes](examples/README.md)

## 22. Implementation-independent contracts for the supporting system

The [contract reference](implementation/CONTRACTS.md) describes recoverable information, accepted transitions, failure behavior, and evidence for identity, participation, context, actions, resources, adoption, review, delivery, restoration, and privacy.

These are requirements on behavior, not database schemas, commands, or a technology prescription. A builder chooses how to implement them and demonstrates the relevant guarantees.

## 23. Consolidated design requirements catalogue

The [catalogue](implementation/REQUIREMENTS.md) retains I01–I21 and 45 requirement identifiers with detail and test references. Use it as a coverage index, not a replacement for the full contract. Applicable extension obligations depend on the declared profile and enabled effects.

## 24. Acceptance campaign: what would demonstrate that it works

The [acceptance catalogue](evaluation/ACCEPTANCE.md) specifies 26 mechanical, 12 behavioral, and six extension checks. None is reported as executed by this documentation revision. Freeze fixtures and evaluation criteria, preserve failures, and compare total resources fairly.

Mechanical reliability, individuality, cooperation, learning benefit, accomplishment, and deployment suitability need different evidence. Counts of personas, messages, fragments, and attractive outputs are not substitutes.

## 25. Failure catalogue and the design response

Decorative individuality, unowned work, assumption laundering, tool-registration theatre, premature publication, unaccepted reviews, ignored feedback, circular dependencies, endless improvement, stale passes, duplicate outside effects, and privacy leaks all have explicit counterexamples in [the stress brief](sources/S5-stress-test-report.md).

The corrections make failures visible and establish a stopping or recovery path; they do not guarantee that a model always chooses wisely.

## 26. Minimal-first realization and conformance profiles

Begin with one useful continuing collaborator under real bounds. Add demonstrated cooperation, then justified adaptation and learning, then complex generalization. A society or physical body is not the minimum product.

The [implementation path](implementation/README.md) describes persistent-collaborator, cooperative-group, adaptive-community, and physical-enabled scopes. Claims inherit applicable lower-level requirements and name what was actually evaluated. Local identity continuity does not establish global exclusive activation across independent hosts.

## 27. Decisions that must be explicit before deployment

Supported tasks, inference configuration, effect authority, isolation, resources, review independence, domain criteria, retention, restoration, governance, services, physical assurance, federation, evaluation thresholds, and distribution rights require explicit choices.

The [deployment register](implementation/DEPLOYMENT-DECISIONS.md) identifies the required owner, policy, and evidence without inventing universal values or current product readiness.

## 28. Reusable non-code design worksheets

The [worksheets](templates/README.md) cover mandates, profiles, commitments, improvements, birth, fragments, capabilities, review and release, community charters, services, and evaluation decisions. They are optional aids, not compulsory forms. Filling a field never substitutes for actual acceptance or evidence.

## 29. Glossary, source traceability, and final design statement

The [glossary](GLOSSARY.md) defines the vocabulary. [Five design briefs](sources/README.md) explain the foundations and safeguards. The [provenance manifest](sources/SOURCE-MANIFEST.md) pins the originals in history and distinguishes rewritten prose from preserved attachment bytes. [Design decisions](DESIGN-DECISIONS.md) keep E1–E6 explicitly proposed.

AI Personas aims to connect continuity, different perspectives, learning, cooperation, and accountable action to real human needs. The design's promise is not a persuasive story of intelligent activity. It is a clear route from an accepted need to actual work, appropriate evidence, honest limits, and permitted future learning.
