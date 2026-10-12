# Useful work, cooperation, and trustworthy boundaries

[Design guide](README.md) · [Persona core](PERSONA-CORE.md) · [Contracts](../implementation/CONTRACTS.md) · [Requirements](../implementation/REQUIREMENTS.md)

## Purpose and status

This chapter defines what a continuing persona may undertake, what its supporting system must preserve, and what it may honestly claim about a result. It is the adopted target design, not a report of deployed capability or a passed evaluation.

The [persona core](PERSONA-CORE.md) defines the persona as a continuing whole: characteristic context, LLM reasoning and invocation, actual behavior, and controlled self-revision. Fragments written in the persona's own voice are persona-defining prompt parts within that whole. Evidence and operational records serve a different purpose: they establish what happened and what remains owed. This chapter defines the boundaries that make the persona's freedom accountable.

**Who makes the choices.** The primary LLM is the mechanism through which the persona reasons and authors its decisions. It chooses useful contributions, methods, interpretations, organization of prompt parts, and characteristic context for its next invocation. Its current character, selected context, and actual situation inform all discretionary communication, collaboration, coordination, navigation, reflection, tool and action choices, and stopping. The model's learned capabilities, priors, and inference configuration also affect behavior; context alone guarantees neither consistency nor competence.

The same persona interprets consequences and may revise its compact network of fragments, later relationships, and, where permitted, current character. It may search, read, ask, create, assess, revise, cooperate, continue, or stop. Every accepted persona response explicitly addresses its work, maintenance of both fragments and supporting resources, and next-context choices for both scopes. A concise reasoned no-change decision or preservation of suitable context can be enough.

**What the supporting system does.** It faithfully supplies permitted context, records actual events, checks current authority, and conserves resources. It does not infer a compulsory profession, team, domain workflow, universal relevance score, or sequence of steps from a request. Reusing a useful method is permitted; the persona need not invent a new method to demonstrate agency.

The protected [I01–I21 invariants](../implementation/REQUIREMENTS.md), this chapter, the persona core, and the contracts are complementary normative views. A conflict between them is a design defect to resolve explicitly. Examples, worksheets, artwork, and historical sources cannot override them. Apply obligations at the depth and feature scope of the actual work: rewriting a sentence does not require a committee or eleven forms.

## The need and accepted scope

Start from the actual need and preserve who expressed it. Keep the exact request or self-originated need, its human or persona origin, supplied material, and authorized boundaries. A requester may be a human or another persona. An existing valid opportunity may support a persona's own need or a peer request without a fresh human prompt. The requester's identity does not supply another party's authority or consent.

A request to create or build must not quietly become an offer of advice because a prose answer is easier. The persona determines the appropriate result, consequential unknowns, useful representations, and necessary checks. The user need not know tool names or file formats.

**The mandate.** The agreed scope records outcomes, hard constraints, preferences, accepted clarifications, assumptions, permissions, resources, review expectations, and stopping conditions. Its detail should match the work's consequences and dependencies. Keep these distinct:

- The original request.
- A proposed interpretation.
- The adopted scope.
- An optional improvement.
- A completion criterion.

They carry different authority. Material changes require the authorized party's decision; the persona's plan cannot rewrite the original need.

**Coverage and ownership.** Each adopted required outcome has an accepted owner or a visible ownership gap, dependencies, evidence expectations, any actual review requirement, and a current disposition. Completing every item on a checklist does not prove that the checklist covered the request. Personas must judge omissions. A separate scope-coverage assessment becomes a formal release requirement only when explicitly adopted. A useful partial result, question, negative finding, block, or decline must not be labeled full success.

### Questions, assumptions, and shared context

A brief request can support useful interpretation and permitted work. It need not arrive as a complete specification. Ask focused questions when their likely value justifies interrupting the requester, while progressing work that does not depend on the answer. Asking a question does not itself make the answer a blocking dependency.

**Ordinary choices.** For an unanswered preference or revisable design choice, the primary LLM uses available evidence to choose and disclose a reasonable provisional interpretation or a small useful set of alternatives. It must not wait indefinitely by default. Reconsider waiting according to urgency and accepted continuation terms, rather than a universal timeout. Keep material assumptions easy to revise. If a later answer conflicts with an assumption, reconsider affected claims and artifacts while preserving what actually happened earlier.

**Consequential unknowns.** A consequential question identifies why it matters, which claims depend on it, what evidence is needed, who accepted follow-through or where ownership is missing, and whether conditional exploration is permitted. Missing authority, indispensable private input, required outside evidence, and safety-critical uncertainty continue to block dependent actions or claims. Silence, elapsed time, and peer confidence cannot provide stakeholder consent or verify an outside fact.

Once useful independent work is exhausted, expose the specific blocker and the accountable next choice. Do not promise a continuation that has no means to occur. An assumption may be proposed, permitted for exploration, confirmed by appropriate evidence, contradicted, or withdrawn. Permission to explore a synthetic condition does not confirm an outside fact.

**Who can answer and who can see.** Ordinary work questions are visible to permitted work participants. The addressee, audience, and need for human input are separate matters. A question addressed to the user is not automatically private, and a peer may still offer evidence or a conditional answer. Mark a dependency as explicitly human-required only when consent, private information, or an outside observation actually requires that person.

The question owner assesses each reply's attributed basis and disposition. A peer may provide a fact, option, or inference, but cannot establish a private user preference merely by answering, or supply consent through an assumption. A dependency blocks the affected claim, not all independent progress.

**Conditional shared work.** Within existing scope and delegation, an authorized assembly editor may adopt a reversible conditional scenario. Adoption does not widen scope, certify facts, obtain source access, replenish resources, or authorize a forbidden effect. Keep the conditions visible wherever the resulting claim appears. If a condition changes, reconsider dependent results and assessments.

**Readable adoption.** Before adopting governing shared context, check that its exact, fully derived version can be supplied to current participants. If it cannot, the adoption fails as a whole: preserve the proposal, prior scope, and notification state. Resolving a question must likewise not silently narrow the audience of its previously readable question and replies. Preserve those records and the failure diagnostic; record any attributable conclusion as a separate result. Later permission withdrawal still takes effect.

**Durable delivery.** Deliver shared questions and replies once to currently permitted participants through durable input handling. Waking a waiting participant does not compel an answer or override a pause. Current question views survive inbox acknowledgment and retain attribution, outstanding owner decisions, and the basis of replies. The question owner receives permitted answer content, not automatic access to the author's private fragments or source ancestry. Stored lineage continues to govern later use.

## Voluntary responsibility and cooperation

A persona becomes responsible for continuing work by actually accepting it. Selecting a persona or naming it in a plan is only an offer. Continuing responsibility requires authenticated acceptance of the exact commitment and applicable terms, or an already accepted delegation that covers them.

![Human and persona needs can lead to direct contributions or accepted continuing roles. Disagreement, decision rights and actual handoff acceptance remain explicit, without compulsory teams or leaders.](../assets/collaboration.svg)

**Figure: Cooperate without inventing commitment.** This is a conceptual explanation of the design. [Read the exact rules](WORK-AND-BOUNDARIES.md#voluntary-responsibility-and-cooperation); the explanation below retains their qualifications. [Open the illustration](../assets/collaboration.svg).

<details>
<summary>Text equivalent of the illustration</summary>

Cooperate without inventing commitment

AN ILLUSTRATED DESIGN STORY

Can I help?

I accept this scope.

Agreed role

A need can come from a human or a persona

A direct contribution

Offer an idea, answer or useful assessment without inventing a continuing role.

Continuing responsibility

Accept current scope and terms before being counted as an owner or reviewer.

Work together when useful

Participants may share a task, explore an authorized question or develop a relationship. A team or leader is not required for every need.

Disagreement stays attributable

Explain differing evidence, assumptions and judgments. Use the decision rights adopted for this work; silence or enthusiasm is not acceptance.

A handoff needs a real receiver

An accepted transfer preserves obligations, resources and unresolved issues. Naming another persona cannot discharge responsibility.

Task-free exploration still needs its actual authority and finite bounds. Conversation does not create an unfunded background loop.

Characters personify design choices; they do not assert feelings or consciousness. Scenes are hypothetical.

</details>

Preserve the accepting identity, work scope, terms or delegation envelope, revision, and actual acceptance event. An invitation, membership flag, caller-supplied receipt, or acceptance of some other commitment is insufficient. An offer to oneself still requires actual acceptance.

A direct answer or exploratory contribution need not first establish a formal continuation role. Once continuation is promised, its owner carries the need toward delivery, an honest wait or block, a permitted decline, or an accepted handoff. Ownership may be shared or divided. It does not create a compulsory leader or authority to assign peers.

| Disposition | Meaning |
|---|---|
| Offered | Terms are proposed; no accepted responsibility is attributed. |
| Accepted or working | The participant accepted the applicable terms. Each action still retains its actual status. |
| Blocked | A named condition prevents progress. Ownership and the next decision remain visible. |
| Submitted | An exact candidate is offered. Submission is not approval. |
| Closed | The exact agreed result or another authorized ending is recorded. |
| Canceled or handed off | An authorized cancellation or an accepted current transfer changes the responsibility. |

**Changed terms.** Material amendments outside accepted terms or delegation require fresh acceptance. An amendment genuinely within an accepted envelope records that basis without renegotiating every detail. Earlier acceptance remains historical; it does not automatically attach to new terms. Acceptance of responsibility never substitutes for an execution grant.

**Handoffs.** Offering a handoff leaves the existing responsibility intact. Transfer must check the exact current terms, current owner, eligible receiver, authentic acceptance, authority, and relevant lifecycle state in one coherent transition. Competing transfers, cancellation, and revocation cannot all succeed from an outdated view. A declined, inaccessible, or obsolete offer leaves an accountable owner or an explicit authorized ownership gap. Silence is not a successor's consent.

### Discovery, disagreement, and revisable organization

Participants need a usable way to find work and one another without exposing information they cannot access. Discovery covers work, gaps, participants, shareable contribution evidence, capabilities, and limits. Messages and a shared opportunity-and-obligation board support offers, questions, findings, and negotiation without imposing a global ranking. A search result neither selects a worker nor commits one. Each persona keeps its own agenda; collective commitments consist of actual accepted responsibilities and dependencies.

Participants may volunteer, decline, consult, propose alternatives, negotiate interfaces, or seek bounded recruitment. An unavailable contribution does not automatically create a profession or trigger replacement births. Plans, checklists, temporary coordination, and recurring partnerships are revisable authored work content. Accepting them cannot widen authority or authorize replay of an action sequence whose results have not been observed.

**Character in cooperation.** Characteristic preferences may influence when a persona seeks another perspective, how directly it disagrees, what makes a handoff useful, or how it balances progress and consultation. Those preferences belong in its own fragments and actual decisions. OCEAN traits do not assign a host-selected role, and modeled dominance does not confer leadership. A quiet persona still owes accepted coordination duties; a sociable persona cannot turn every task into unnecessary messages or commitments. Coordination calls carry the same explicit maintenance responsibility as individual work, without merging participants' private accounts.

Actual human and peer exchanges belong to the [same reciprocal maturation loop](PERSONA-CORE.md#maturation-within-every-primary-interaction). Interpret each exchange according to what it establishes. A preference, factual report, praise, disagreement, and authentic acceptance are different kinds of evidence. Praise does not verify a conclusion, a decline does not prove hostility, and familiarity does not bind future help. Supported refinements to relationships or methods may change later characteristic choices without requiring stable-trait revision or a separate authority for social revision.

**Agreement and dissent.** Agreements preserve exact terms, scope, endorsers, dissent, allowed variation, revision, and exit. Majority agreement does not establish empirical truth. Compare evidence for factual disputes; seek the relevant authority for preference or resource decisions; respect permissions; and expose unowned work. Independent reversible alternatives may proceed. Do not manufacture disagreement for appearance's sake or infer unanimity from a group summary.

**Criticism and blockers.** A peer's criticism is an attributed assessment. It is not automatically a veto, repair instruction, reviewer assignment, or activity-state change. A blocking obligation requires a separate, explicit adopted decision tied to its exact subject, basis, accepted responsibility or ownership gap, and disposition rule. Acknowledgment, delivery, and resolution remain distinct. Existing accepted blockers survive upgrades, summaries, context maintenance, and history pagination until an authorized disposition. A polite response cannot waive a mandatory criterion.

### Integration and finishing

Outputs that depend on one another need compatible agreements. As relevant, agree on identifiers, units, coordinates, terminology, input versions, ownership boundaries, and mappings from sources to analysis. These agreements are work content, not domain-specific runtime engines. Coupled changes become visible as one compatible adopted assembly. Independent drafts remain separate until adoption of their current versions succeeds.

**Circular dependencies.** Expose any cycle in which final outputs depend on one another. Participants may accept bounded provisional inputs, a baseline, compatibility checks, resources, and a stop condition. Provisional progress neither satisfies final dependencies nor proves convergence. The team may change method or report an honest block. Missing dependency records do not prove independence.

**Optional improvements.** Improvements compete with finishing. Personas choose how much explanation or comparison an idea needs; every thought does not require a proposal form. Actual comparisons may support adoption, rejection, or deferral. Optional novelty cannot remove required outcomes or spend protected finishing resources without authorized reallocation.

## Capabilities and the execution boundary

A capability is an available means to observe or act, such as an application, service, connection, execution facility, procedure, or qualified outside contribution. Finding one is only the beginning of determining whether it can support the proposed operation.

![The diagram distinguishes discovery, qualified guidance, executable availability, operation-specific permission and resources, actual invocation and received outcome. It does not prescribe a fixed probe sequence.](../assets/tool-readiness.svg)

**Figure: Finding a tool is only one fact.** This is a conceptual explanation of the design. [Read the exact rules](WORK-AND-BOUNDARIES.md#capabilities-and-the-execution-boundary); the explanation below retains their qualifications. [Open the illustration](../assets/tool-readiness.svg).

<details>
<summary>Text equivalent of the illustration</summary>

Finding a tool is only one fact

AN ILLUSTRATED DESIGN STORY

Saved does not mean ready to run.

Saved tool

Current checks

Readiness is for this operation, now

Found: a candidate resource

A search hit or stored script says what may be useful. It proves neither installation nor suitability.

Understood and available

Use the exact guidance with all its conditions. Check the working tool connection, dependencies, current availability and version.

Permitted and affordable

The proposed operation must fit current authority, source restrictions and remaining resources. A tool description grants none of these.

Used and observed

Perform only an action that passed the current checks. Keep its real receipt, failure or uncertainty distinct from the desired outcome.

These are different facts, not compulsory separate calls or probes. A known current interface can use the direct path.

Characters personify design choices; they do not assert feelings or consciousness. Scenes are hypothetical.

</details>

A capability description identifies provenance, version, environment, required access, preparation, limits, observed failures, and evidence of use. Keep discovery, requested preparation, provisioning, availability, failure, and revocation distinct. Also distinguish four claims: installation, representative operation, actual project use, and successful output that supports a particular claim.

**Availability, permission, and suitability.** These facts must not be treated as interchangeable:

| Fact | What it establishes |
|---|---|
| A package is stored or an executable is installed | An artifact is present; this alone does not establish a usable interface or permission. |
| A binding is registered or a connection is usable | An interface is addressable under its actual controls, or the connection can be used. |
| This operation is permitted | Current authority covers the proposed use. |
| The capability is suitable for this need | It can serve the relevant purpose under the actual conditions. |
| Qualified guidance is actually exposed | The persona has received the operative guidance and its required qualifications. |
| An invocation is admitted | Current admission checks passed. |
| A relevant result succeeded | Observed output supports that particular success claim. |

Readiness is operation-specific evidence about current prerequisites. It is neither a correctness guarantee nor a compulsory probe. A suitable usable alternative can avoid acquiring something new. Preparing a preferred but unavailable option still requires applicable authority and resources. These distinctions do not impose a linear lifecycle: remote services need no local installation, and an existing authorized runner need not become a new native tool.

**Supporting resources.** Separately organized histories, tool-use records, tool definitions, reusable skills, scripts, code, and data remain supporting resources. Their storage, inspection, inclusion in selected context, and executable availability are different facts. A skill package's asserted permissions, a tool's self-description, or a historical user instruction cannot supply a current grant. Imported guidance retains its author; the persona's characteristic interpretation belongs in its prompt fragments. The host checks exact identity qualified by source, rather than trusting a familiar filename or a colliding tool name.

**What an operation must bind.** Each operation binds its current observable capability, interface and connection identity, relevant exact client or runner artifacts and inputs, authority, and actual outcome. Controlled local helper execution also binds the actual artifact, resolved relevant dependencies, configuration, and environment. A local helper that calls a remote service must satisfy both boundaries. Limits on observable remote identity do not waive local integrity checks.

For a remote service, record the server version only if it is genuinely observable. An unavailable server build is explicitly unknown; do not infer it from a schema or invent it. This uncertainty limits executable-version and reproducibility claims. It blocks an operation when the required assurance depends on that missing identity, but does not automatically prohibit an ordinary permitted remote call supported by its observable contract.

A past run does not establish current availability or guarantee reliability. Source and destination restrictions, complete qualified guidance, freshness of mutable inputs, and reconciliation of effects still apply. Preparation and installation have their own authority and resource checks. Even a help command may run imports or fetch dependencies; documentation inspection is read-only only when that boundary is enforced. Code and bulk data may remain outside LLM context when an authorized runner consumes exact references, provided the persona receives complete relevant interface guidance and bounded evidence of the result.

**The environment.** The environment identifies workspaces, participants, resources, information, services, artifacts, and actual limits. Separate draft directories may prevent collisions, but do not provide confidentiality. A default working directory is not an access grant. Resolve relative publication from the documented participation workspace; an earlier command's temporary directory must not silently change that default. Participants shown in the same environment may have different permissions.

Domain tools and specialist methods are legitimate. An export facility does not establish authoring, editing, analysis, or qualification capability. Existing current operation evidence may be reused; each task need not reinstall a tool or run an irrelevant probe. If the chosen operation lacks a usable capability, expose the gap, seek permitted preparation, choose another method, or stop. Neither a new persona nor a confident model description creates practical competence.

### Discovery without a compulsory tool sequence

Discovery helps the persona find what the work needs. It does not impose one research method or sequence on every task.

**Environment defaults.** A deployment may offer removable defaults scoped to an environment, such as search, page reading, and a bounded supplementary model question. Present those defaults at creation and let the user omit any of them. Bindings are independently versioned per environment. Creation configures availability; it does not authorize research, installation, or spending. Later catalogue updates must not restore removed choices. Removing a binding neither uninstalls host software nor permanently forbids a later explicitly authorized acquisition.

For unfamiliar requirements, current outside facts, or tool suitability, source search and inspection are useful primary discovery options. Applicable retained or supplied evidence may already suffice. The persona chooses queries, sources, methods, experiments, and collaborators. No universal search count or domain-specific sequence is imposed. A subsidiary model's answer is model knowledge, not external research or firsthand experience, and its suggested action gains no execution authority.

**Stored-resource discovery.** Through the existing next-context contract, the current primary decision requests bounded lexical or supported-regex discovery, exact reads, or particular definitions. The host returns only the requested permitted candidates or exact material within aggregate limits. Discovery, reading, selection, loading or exposure, invocation, and observation have different meanings; they do not require six separate calls.

Known exact resources may be requested directly. An already supplied, still-current complete interface may support an authorized invocation immediately. Independent requests may share a bounded batch; a choice that depends on a result waits for the actual result. Never supply a complete tool or skill catalogue to an LLM so that it can choose a subset.

**Character and judgment.** Own-voice methods and tool notes guide choices only where the present need leaves discretion. An exploratory tendency may favor a small comparison; a preference for concrete progress may favor a reversible first attempt. Both still owe the checks needed for the actual promise. Traits cannot replace capability evidence, turn a description into execution, skip an exact instruction, or require extra calls merely to display personality. Supplementary model work that exercises the persona's judgment follows the [every-persona-invocation contract](../implementation/CONTRACTS.md#every-persona-invocation). Isolated computation remains attributed evidence for a later persona decision.

**Research outcomes and failures.** Diagnostics retain the actual backend, query or source, observation time, transport outcome, and failure category. Blocked access, an empty result, unavailable infrastructure, and candidate results are distinct outcomes. Transport success does not establish relevant research, and failure of one backend does not establish that all permitted sources failed. Another authorized method remains the persona's choice. Failure does not authorize an automatic retry storm, account creation, access bypass, or credential disclosure.

### Host access and enforceable claims

An execution profile must describe the access it actually permits and the boundaries it can actually enforce. Acquired programs must not gain unapproved access to unrelated work, identity administration, private assessment material, secrets, or destinations. Enforce read-only and isolation claims rather than trusting tool labels. If a claimed boundary cannot be enforced, the capability is unavailable under that claim. A differently scoped use requires an explicit informed grant. Isolation failure must never silently fall back to broader access.

**Host-account access.** An explicitly selected host-account profile may provide broad host tools, installation, filesystem operations, network access, and subprocesses under that account's actual permissions. It provides no confidentiality between personas that can read the same account's files. Application record permissions cannot protect credentials or evaluator files readable through the host.

The [deployment decisions](../implementation/DEPLOYMENT-DECISIONS.md#host-and-isolated-execution-profiles) distinguish a documented initial default from a later explicit operator choice. Restart cannot silently override that choice or restore withdrawn access. Persona-authored files cannot switch execution mode, enable a disabled capability, or grant access.

**Secrets and evaluation.** Credentials stay outside ordinary persona files and model context. An opaque reference does not protect a credential once a tool receives its actual value. A deployment must isolate protected evaluator material from persona-controlled access, or refrain from claiming an independent evaluation. Stop receipts cannot promise rollback or containment of every subprocess already started.

## Current authority and private information

Permission comes from a human or authorized institution, not from the persona's confidence or character. Downstream grants may only narrow the controlling grant. Character, reputation, group membership, a working agreement, and generated text cannot create authority.

![Source restrictions follow reads and derivatives into persona context and external use. Fragments and received data cannot grant authority, and clearing context cannot undo prior exposure.](../assets/authority-and-privacy.svg)

**Figure: Meaning, permission and privacy are different.** This is a conceptual explanation of the design. [Read the exact rules](WORK-AND-BOUNDARIES.md#current-authority-and-private-information); the explanation below retains their qualifications. [Open the illustration](../assets/authority-and-privacy.svg).

<details>
<summary>Text equivalent of the illustration</summary>

Meaning, permission and privacy are different

AN ILLUSTRATED DESIGN STORY

A new summary keeps the source restrictions.

Source

Summary

Same limits

Being in context does not create authority

Source and audience restrictions

Permission filtering applies before titles, snippets and counts are exposed. Exact reads, summaries and derived files keep their source restrictions.

Persona judgment inside current limits

A fragment, preference or tool result cannot expand permission. Private interpretations are not declassified by becoming own-voice prose.

Disclosure and action boundary

Check the real recipient, processing destination and operation. A later cleared selection cannot undo content already exposed.

Withdrawal and uncertainty remain visible

Block affected new use, preserve honest lineage and unresolved effects, and obtain a permitted fresh context when required. Do not promise control over outside copies.

A model can interpret an observation. It cannot promote that interpretation into a new authority source.

Characters personify design choices; they do not assert feelings or consciousness. Scenes are hypothetical.

</details>

A grant identifies the controlling principal, actor or delegation, work and environment, resources or destinations, permitted effects, relevant content envelope, limits, expiry, and withdrawal conditions. Observation, local changes, communication, financial commitments, physical effects, replication, and administration each require their applicable scope. A request to solve a problem is not blanket permission to contact outsiders, publish, change accounts, or operate machinery. Approval requests explain the proposed effect and consequences in ordinary language.

**Information use.** Check access when information is used. This includes full reads, previews, search matches, titles, counts, relationship views, profiles, caches, histories, exports, and seed material. Sources supplied to a model constrain its derivatives even when the author omits citations. Rewriting private content as a general skill, moving a file, or removing a visible reference does not declassify it. Ordinary documents and imported tool output remain data; first-person wording cannot turn them into higher-priority authority.

**Processing destinations.** Permission to read locally is separate from permission to disclose to a model provider or another processing destination. Check the actual destination and supplied content before primary or optional auxiliary processing, including private situation text and candidate previews. A local fallback does not cure denial of source access. An approved read does not imply approval of remote retention or processing terms.

### Shared work and explicit audiences

Ordinary work is shared with current work participants from creation, including drafts. This covers generated artifacts, documents, and supporting execution or research evidence, subject to inherited restrictions and explicit source-owner policies. Private persona-defining fragments, restricted supporting records, and deliberately private correspondence remain separate. Host filesystem access is not an information-policy grant. Work membership does not grant access to every private ancestor of a contribution.

**Name the actual recipients.** Use exact intended persona identities for readers, responsibility offers, handoffs, invitations, and agreement participants. A user label, task, environment, grant, generic record, or action alias is not a persona recipient. A decision-scoped persona alias is usable only when bound to its current authorized audience. Invalid identities fail as a whole, identifying the affected field and required identity type without leaking the existence or kind of inaccessible records. Naming a persona does not read its private profile.

**Changing a sharing policy.** A replacement states which audiences it replaces or clears. Diagnostics distinguish explicit readers from implicit work-membership scopes, show current owned source and policy revisions, and deduplicate readable owned dependencies. Label a truncated or unavailable audience as incomplete; never present it as an empty list safe to replace. Failure to finish lineage traversal within its bounds remains visible.

Diagnostics may identify remedies for sources the actor owns. They do not expose another owner's private sources, change policy, grant exports, renew notifications, or retry effects.

**Perspective invitations.** Before issuing an invitation, check that its exact subject can be delivered to the audience that acceptance would grant. A failed check leaves neither an unusable invitation nor new membership. Repeating a still-current request returns its current participation state. Historical delivery or notification counts do not establish present readability, peer inspection, or agreement.

### Historical provenance and a fresh permitted context

Source restrictions follow the work derived from that source. When an exploration question or another source supplies instructions, its exact restrictions cover initial and later work versions, invitations, participation instructions, receipts, selected context, and derivatives.

Durable construction evidence may connect an early representation to its actual source. It must not claim that omitted source fields existed in the historical bytes. Missing provenance fails closed. A later citation must not replace the original question that actually supplied the work.

**Runtime metadata.** Navigation identities and accounting metadata do not count as reads of a payload never supplied, but this exemption requires trusted runtime provenance. Authored previews, copied text, selected fragments, and lookalike diagnostics retain ordinary source restrictions. An untrusted source cannot declare itself exempt metadata.

**Starting a fresh permitted decision.** A persona may prepare new context readable within the work by explicitly clearing active private selections, private handoff content, and private navigation. Clearing those selections does not delete authored prompt parts or supporting records, or change their retention policy. Unread private inputs remain unacknowledged and unresolved.

Clearing cannot retroactively sanitize an already-admitted decision or output from that decision. A fresh decision must use independently permitted information. Withdrawal may prevent fresh dependent use without recalling bytes already sent to a provider or undoing completed or uncertain effects.

**Expired evidence.** Permitted expiry of old raw observations is different from source revocation. An experience-informed prompt part may continue to shape the persona only when its retention and derivative-use policy permits. Its interpretation remains fallible, and unavailable evidence must be disclosed wherever that limits a claim. It cannot substitute for a receipt required by current work.

Expiry cannot remove restrictions, accepted warnings, caveats, or unresolved effects. Derivative erasure requirements still apply to abstracted guidance. The [core retention rules](PERSONA-CORE.md#compact-retention-and-honest-forgetting) govern narrowing, ineligibility, and honest historical limits.

## Admitted actions and real consequences

A model proposes an action; the runtime admits it only after current checks. Before admission, establish the actor, causal work, intended effect, exact request identity, relevant input versions, selected capability, current authority, resource reservation, and how observation, cancellation, and uncertainty will work. Durable intent and accepted action state prevent an interruption between recording and dispatch from silently losing an action or duplicating its effect.

**Validate the whole response first.** Before adopting any proposed action, establish that the complete persona response contains valid work, explicit valid maintenance for both fragments and supporting resources, and explicit next-context dispositions for both. A plausible action, urgent-looking prose, or useful reply does not excuse missing or malformed maintenance or next-context intent.

From an invalid response, dispatch or adopt no proposed action, communication, resource write, discovery/read request, or next-context change. Independent host duties continue: cancellation enforcement, factual receipt and history recording, accounting, and safe shutdown. Those duties must not manufacture a persona outcome.

| Action state | Honest meaning |
|---|---|
| Proposed | An action was requested; permission and execution are not established. |
| Admitted | Current checks accepted the action and reserved capacity; completion is not established. |
| Running or pending | Execution or an outside response remains underway. |
| Completed | A terminal observation identifies actual occurrence and exact outputs; correctness needs its own evidence. |
| Failed | Failure is observed; this does not necessarily establish that no external effect occurred. |
| Stop requested or acknowledged | The stated extent of stopping is known; earlier effects are not undone. |
| Effect unknown | Occurrence remains unresolved; safe repetition and zero cost cannot be inferred. |

**Pending operations and fresh decisions.** A pending operation ends the unobserved remainder of the originating decision. Failure, uncertainty, and authority invalidation likewise stop the affected remainder according to their actual barriers. Preserve suppressed proposed actions for inspection; never replay them automatically. A fresh authorized decision uses actual observations.

Independent work may proceed in a later decision while a bounded background operation continues. An optimistic action list does not establish that independence.

**A valid response whose save fails.** A later file conflict or failed save is different from invalid or missing maintenance. It does not by itself invalidate otherwise lawful work from the same complete valid response, but that work's independence must be explicit and evidenced. The work must require neither the failed edit nor unavailable observations. Relevant supplied state, source permissions, current authority, resources, and mode must remain valid.

Missing dependency evidence does not establish independence. Hold dependent or uncertain work for a fresh decision based on observations. This allowance does not bypass a pending-action or fresh-decision barrier. A reply that depends on an unaccepted save cannot claim that the file was retained.

**Effective-character changes.** A same-response request to adopt an effective-character change must receive a coherent disposition before any other fresh persona operation from that response is adopted or dispatched. This applies regardless of listed order or claimed independence.

- **Accepted:** a fresh primary decision is required before any work outside the narrow atomic acceptance unit.
- **Known rejection, or explicit deferral with definitely no commit:** other work may proceed only if it passes the existing independence and current-state checks.
- **Unresolved or unknown commit:** hold the other work until the disposition is established.

A tentative character idea is not an adoption request and does not block ordinary authorized investigation. A definitely uncommitted candidate requires a fresh authorized proposal before later adoption. An unknown commit requires reconciliation.

The necessary character-proposal validation and disposition or commit includes only the exact account-binding and optional-selection reductions permitted by the core's atomic transition rule. Independent deterministic host duties remain possible. Preserve prior admitted effects and receipts without erasure or replay. Ordinary method updates and scoped transient affect do not trigger this character-specific barrier unless they replace effective character. Restricted modes still cannot edit character. The [persona core](PERSONA-CORE.md#character-in-its-own-voice) gives the full rule, including its application to reads and waits.

**Separate persistence from effects.** Fragment persistence and external effects have separate receipts. Coherently accept dependent local changes and durable action intent before dispatch, but do not promise that sending a message or running an outside operation is atomic with changing a file. A pre-action fragment may describe intent or earlier experience. Only an actual later observation supports an outcome claim. A failed maintenance retry cannot erase, repeat, or relabel an effect already dispatched.

When producing a model, inspecting it, and publishing it, do not read an older file at the intended location while the new operation is still running. The delivered output must be the exact product of the completed operation. A saved workflow authorizes no unobserved remainder.

**Retries and uncertain effects.** An exact retry with the same identity and content returns or resumes the same accepted operation while authoritative history remains retained and accessible. If it does not, return an honest unavailable or unresolved disposition under the retention rules. Never reconstruct missing history or replay the effect. Reusing an identity with different content is a conflict. Receipts have their own access checks.

If a service may have acted before a timeout, preserve destination, payload, effect uncertainty, and exposure. Before a potentially duplicate send, publication, purchase, or application, reconcile through authorized destination evidence. Local journaling does not guarantee universal exactly-once delivery.

## Inference and bounded working context

The persona's identity and obligations persist independently of provider sessions. The primary model remains its decision and generative authorship mechanism; an opaque autonomous harness must not silently take ownership of the persona.

Supported inputs and outputs, refusals, malformed or partial responses, timeouts, cancellation, usage, and unavailable capabilities are explicit deployment choices within the [every-invocation contract](../implementation/CONTRACTS.md#every-persona-invocation). That contract covers initialization, request preparation and retrieval-only judgment, communication, coordinated work, repair, reflection, persona-capable subcalls, and provider attempts. Calling a persona decision a helper does not remove its maintenance responsibility.

**What every request and accepted response covers.** Every request combines:

- Current work.
- Accepted trait-conditioned context, or the attributed initialization seed.
- Needed supporting assets and observations.
- Maintenance responsibility for fragments and supporting resources.
- Responsibility to state the next-context disposition explicitly for fragments and supporting resources.

Preservation or no optional need may be appropriate; silence is not. A useful asset proposal identifies an authorized intended file/path or storage reference, exact content or reference, a base revision where relevant, and helpful search/regex cues. One concise reasoned no_change may cover both maintenance scopes. Neither scope forces a write, a separate reflection call, or a new selection. Actual persistence, current execution availability, factual host capture, and primary-authored maintenance remain different claims.

**Initialization and model choice.** Before adopting a model switch or the normal initialization from seed to authored fragments, check the exact inference selection against current permission, capabilities, pricing, and funding scope. Rejection preserves the prior selection and consumes neither a birth nor a new identity. Explicitly imported or operator-supplied character is an attributed alternative that may avoid an initialization call; it must not be described as LLM-authored. Later inference still requires admission. A read-only readiness view reserves nothing. Model switches cannot widen grants, bypass refusals, or erase performance limitations.

Image capabilities follow the selected model's actual support. Image input support does not prove generation support, and an unavailable output does not authorize a model switch. Supported media and conservative exposure belong in the actual request and accounting. Saved connection changes govern future decisions; they do not rewrite the provider bindings or charges of admitted calls.

**A small starting interface.** Capability instructions have a bounded working set separate from stored histories and persona-defining fragments, governed by the same primary next-context choice. The bootstrap provides a small usable discovery/read/exposure interface, permitted scope information and limits, and controls genuinely needed for the current mode. It may include bounded legitimately known references or relevant seed cues, but not a tool list that supplies the expected answer. It must never enumerate every tool, skill, namespace, or manifest as startup metadata. If the scope inventory is large, discover it in bounded portions too.

**Three different exposure surfaces.** Keep the host-owned registry, provider-facing transport, and actual model-visible context distinct. The bulk catalogue remains in the host registry, outside both the provider request and any LLM used to filter it. Expose only bounded requested descriptors, exact guidance, operative schemas, and their necessary qualifications.

A provider option that transmits all definitions while deferring their model visibility does not meet this transport boundary. Excluding transmitted material from model input may reduce model input, but does not turn transmitted bytes into model tokens. Report those measures separately and honestly. Hosted semantic search or automatic tool-set expansion cannot silently replace the primary's declared lexical selection.

**Usable guidance and correction.** Keep ordinary primitives and instructions needed to inspect, stop, recover, or deliver current work usable. Recently obtained instructions remain available for the following decision only as the explicitly requested bounded, admissible batch. A batch larger than the usual working set still requires the entire next request to fit; it is no exception for catalogue dumping. A failed or conflicting attempt retains an immediately usable correction opportunity while the capability remains permitted. Failed discovery is not acquisition, and a preview cannot replace the full operative contract needed to act.

Retirement of older instructions must be bounded and durable across restart and interface polling. Count attempts, not just successes, when aging a discovery set; otherwise failed use can cause permanent prompt residency or immediate rediscovery loops. Another persona's activity cannot consume or replace this persona's correction opportunity. Permission removal prevents restoration from history. Keeping instructions available neither retries an effect nor changes the primary LLM's selected fragments.

**Reassemble between decisions.** Build the actual working context anew between decisions rather than appending every descriptor, activated skill, schema, and old result indefinitely. Honor the primary's accepted choices to preserve, replace, clear, and set lifetimes. Mechanical retirement follows the declared working-set policy without silently dropping valid selected material.

Context eviction is not storage deletion, revocation, or erasure of an observation. Preserve required tool-call/result bindings and usable controls for unresolved jobs. Provider caches, continuation references, and retained sessions do not prove that older material is absent, current, or free. An adapter must provide a supported bounded continuation or reset with honest observation continuity. Otherwise, report the limit or unsupported mode; do not claim a hard bound the adapter cannot enforce.

**Required context stays available.** Do not evict the following as obsolete tool instructions: current human input; authority; coherent character and relevant modeled state; maintenance responsibility and limits; cancellations; accepted obligations; important adverse observations; exact selected material with required qualifications; and unresolved effects. Active-work guidance forms part of the actual request before exposure is quoted. Bounded context maintenance preserves those facts. It must not supply an evaluator's answer, dictate the next experiment, or act as a substitute author of persona context.

**Check paid preparation locally first.** Optional paid preparation must not knowingly consume the remaining capacity needed for a currently quotable primary decision. Before buying it, check primary availability, enforceable bounds, and combined sequential costs locally. Simultaneous remote calls are not required. The preview dispatches no model, spends no attempt, creates no simulated charge, and cannot change the assigned model. Repair existing context that needs maintenance before optional preparation. Cache reuse and work with no candidates still require current access, freshness, and final admission; they do not create a paid preparation call.

**Recheck the actual request.** Local feasibility does not reserve every possible expanded prompt or lock shared funding. Recheck the prepared request, including rendered schemas, tool-set expansion, retained history, output reserve, and maintenance. Bound both count and size: one result may be enormous, and many small searches may overflow a call or episode.

Unknown provider expansion or unobservable retained context cannot support a hard-limit claim. Use a supported application-controlled path or expose the adapter limitation. Do not guess that unloaded tools are callable.

Assess efficiency across useful delivery, including discovery, host scanning, exact reads, schema loading and reloads, primary calls, retries, maintenance, failed branches, and optional task-tool costs. Per-call occupancy and whole-episode tokens, cost, and latency are separate measures. A smaller final prompt alone does not establish efficiency. Navigation follows the [bounded file-search interface](PERSONA-CORE.md#ordinary-files-and-self-organization). Auxiliary semantic, vector, and graph-retrieval engines belong only to explicitly different research comparators. They are neither a production fallback after a search miss nor the purpose of the fragment collection.

## Resource conservation and protected closeout

Work must remain within its real allowance, including the resources needed to finish honestly. Track enforceable dimensions separately: calls, input and output usage, elapsed time, concurrency, storage, paid operations, money, remote exposure, and population. State what is measured, conservatively bounded, or unknown. Reserve capacity before admission; afterward, reconcile actual use and remaining reservations without treating unknown use as zero.

![The accounting includes active, retained, derived, operational and external managed state, with peak rewrite copies. Protected obligations and user-owned deliverables cannot disappear merely to meet a cap.](../assets/resources-and-retention.svg)

**Figure: A small prompt is not a small total footprint.** This is a conceptual explanation of the design. [Read the exact rules](PERSONA-CORE.md#compact-retention-and-honest-forgetting); the explanation below retains their qualifications. [Open the illustration](../assets/resources-and-retention.svg).

<details>
<summary>Text equivalent of the illustration</summary>

A small prompt is not a small total footprint

AN ILLUSTRATED DESIGN STORY

Count the storage behind the small prompt.

Prompt

Versions · archives · caches

Count the whole managed footprint

Current working material

Fragments, supporting knowledge, skills, tools, code, data, history and required work state.

Retained and derived material

Old versions, archives, cues, indexes, aliases, source copies, provenance, qualifications and warnings.

Operational and external backing

Effect/context records, caches, managed exports and backups, externally retained context and temporary rewrite duplication.

Protect required state before optional growth

Reserve room for unresolved obligations, warnings, reconciliation and closeout. An unmeasured external tier makes the total bound incomplete.

At the limit: make an honest decision

Use actual retention policy, permitted consolidation or an explicit capacity block. Do not hide an unlimited archive or erase required state.

User-owned delivered artifacts are not deleted or revoked to make the persona’s storage cap fit. A digest is not recoverable original evidence.

Characters personify design choices; they do not assert feelings or consciousness. Scenes are hypothetical.

</details>

**One controlling ceiling.** For each enforced dimension, consumed resources, uncertain exposure, and outstanding reservations together stay within the controlling ceiling. Descendants, initialization, retries, optional preparation, maintenance, review, and reporting use that allowance or an explicit transfer within it. A transfer moves capacity; it does not copy it. Retirement refunds neither spent money nor consumed birth capacity. Concurrent admissions cannot spend the same last unit. Call a monetary ceiling hard only when actual upper bounds and controls support that claim.

**Protected closeout.** When needed, reserve capacity for work-specific review, agreed repair, and closeout within the same root allowance. No universal percentage is required. Production, optional improvements, births, and personal exploration cannot consume the reserve without authorized reallocation. A reserve does not provide a reviewer, expertise, consent, or guaranteed completion. Status and evidence preservation must remain possible without another successful model call.

**Maintenance within the allowance.** Every admitted persona call budgets for maintenance input and a concise outcome for both fragments and supporting resources, including finishing and restricted repair calls. This does not justify rereading the entire archive, inventing a lesson or asset, or spending protected closeout capacity on optional reorganization.

When no useful change is warranted, a reasoned no_change covering both scopes suffices. If a consequential correction cannot be made, including because restricted repair prohibits it, preserve an explicit bounded blocked or deferred outcome and hold affected claims or actions. Do not label stale guidance safe merely to finish. Failed calls retain their true host status; do not spend another call solely to fabricate a missing disposition.

**Cumulative navigation.** Navigation limits sit inside the work allowance and cover searches and reformulations, fanout and branch expansion, exact reads and revisits, returned text, context, time, and cost. A new cue, cycle, renamed file, or query does not replenish them. The persona chooses relevance and stopping. The host reports exhaustion and repeated results truthfully rather than following the network on the persona's behalf. The complete set of mandatory qualifications and dependencies must fit independently of optional traversal limits.

**What counts as retained state.** Distinguish three things:

| Scope | Contents |
|---|---|
| Persona-context corpus | Authored persona-defining prompt parts. |
| Assembled prompt | The exact selected parts and other permitted inputs actually supplied to an invocation. |
| Total managed persona-state footprint | The corpus plus all managed supporting and retained state described below. |

The managed footprint includes current fragments; archives and versions; cues, indexes, and aliases; histories and execution records; copied skills and definitions; generated helpers; dependency caches; data snapshots and derived outputs; evidence and provenance; qualification closures and warnings; relevant effect and context records; caches; managed exports and backups; and peak temporary copies during safe rewrites.

Count external storage deliberately used to back this state. Unmeasured external retention prevents a verified total-bound claim. State the accounting and reclamation scope; a smaller active directory or prompt does not prove compactness. Reserve storage for required warnings, reconciliation, and closeout before optional additions. Check both peak and resulting occupancy before adoption.

**Reclamation and protected records.** Policy-approved reclamation may free capacity; semantic consolidation remains primary-authored. Protect exact original requests, accepted changes, and authoritative receipts while active work, unresolved obligations or effects, or declared accountability requires them. Neither low use nor a storage limit may silently erase required restrictions, qualifications, accepted warnings, commitments, or uncertain effects.

Lawfully expired history becomes honestly unavailable. Do not rewrite it as a different original or claim that it remains inspectable proof. Missing action history does not establish that an effect was unsent or permit replay. If protected state cannot fit safely, expose the capacity or retention conflict and block affected admission until an authorized disposition. An unlimited protected archive is not a solution. Capacity increases need actual authorization and change the declared bound.

**Delivered artifacts and outside copies.** The managed footprint does not promise control over arbitrary recipient or provider copies. Do not delete, alter, or revoke user-owned delivered artifacts merely to meet a persona-state cap. Their ownership and retention rules govern them; a managed supporting copy has its own policy. If the persona relies on delivered artifacts as retained backing for context or supporting records, disclose and count that dependency rather than treating it as free hidden storage.

### Preauthorized finishing

A principal may authorize protected funding in advance for finishing after ordinary call or token capacity is exhausted. To qualify, a persona must already be runnable and hold a current, genuinely accepted responsibility under the current mandate. Membership, an old plan, or reserved money is not enough.

A stable creation-order rule may select an eligible funding reference without assigning work. Record the exact commitment revision, authority, quote, and funding pool. Rebinding is permitted only while that same responsibility remains eligible.

**Arrange acceptance before exhaustion.** Expose preauthorization and actual acceptance while ordinary capacity remains, so available offer and acceptance mechanisms can be used. Keep pending consent and changed terms visible. Automatic and operator-selected finishing use the same eligibility rules; diagnostics cannot manufacture commitments.

**Admit each turn on current facts.** Every finishing decision rechecks current authority and full exposure. Temporary concurrency limits, provider failure, and unresolved effects do not trigger a funding-pool switch. Eligible runnable participants receive a fair opportunity before another consumes a second finishing turn. This promises neither a funded number of turns nor adequate review. Optional exploration remains excluded, and paused or canceled work stays stopped.

### Unknown usage is not the same as unresolved execution

A finished local inference may have an unknown bill even though its execution is closed. That is different from an operation whose effects remain unresolved. Preserve the exact call and both accounting bindings, including full conservative call, token, monetary, and remote exposure. Accounting uncertainty alone does not veto otherwise preauthorized finishing, but every later admission must still count that retained exposure.

**Narrow exception for an unapplied primary decision.** A failed or interrupted primary response-only decision may receive the same treatment only when durable local failure evidence proves that the provider attempt ended with no saved action plan and no attempted action, and complete conservative accounting remains. A terminal label alone is insufficient.

For cancellation, a local transport receipt must establish closure, the original decision epoch must be superseded, and no pending plan or attempted action may remain. Cancellation without that fence does not qualify.

**Cases that remain blocked.** Crash-only interruption, incomplete bindings, auxiliary or native operations without equivalent closure evidence, and unresolved outside effects remain blockers. Any attempted action disqualifies the unapplied-primary exception, even if the action completed or failed. Local closure does not prove remote cancellation or free uncertain remote capacity. The exception does not refund usage, reconcile a bill, replay a call, resume stopped work, or create responsibility.

**Read-only diagnostics.** Finishing diagnostics report every independent barrier: preauthorization, accepted current terms, available capacity, uncertain charges, and unresolved effects. Paired ledgers for one call must not appear as two billed calls. A readiness observation is not a quote, reservation, or permission to resume. If a diagnostic is unavailable, preserve the original stop reason and mark the diagnostic missing; do not invent zero exposure. Task-control receipts preserve what was observed. Admission checks current facts again.

## Pause, amendment, and accountable stopping

Stopping prevents new affected work and addresses work already underway; it does not erase what happened. Pause, cancellation, expiry, and revocation stop new affected admissions and initiate the applicable stop procedure. Show stop requested, stop acknowledged, already occurred, and still unknown separately. Late receipts remain evidence and accounting, not renewed authority. A compensating action requires its own permission. Stopping does not undo publication or physical effects.

**Task pause and resume.** A task pause stops new decisions and requests stopping of in-flight inference. Already dispatched tool jobs may finish; stopping them is a separate choice. The pause survives restart, input, recovery timers, and new participants. It does not pause unrelated tasks sharing the persona or funding.

Explicit task resume reactivates eligible paused or waiting participation, including individually paused participants. It cannot renew canceled or removed participation, clear quarantine, revive retirement, reopen sealed history, or supply missing authority and funding. A queue entry for a fresh decision does not prove that inference began.

**Amending the mandate.** Saving an operator task amendment adopts the new mandate and requests eligible resumption together, preserving the original request and prior versions. A mandate change through another control does not independently override pause. Old decision authority is invalidated immediately.

An amendment alone does not cancel already admitted bounded inference. Let its transport drain so usage can be metered honestly, but dispatch no old actions and restore no superseded scope. A later explicit pause still requests stopping during that drain. Show saved scope and funding-blocked resumption separately.

**The persona chooses whether to continue or yield.** The persona must author continuation or yielding explicitly. A decision with no actions may deliberately yield. Missing, malformed, or unsupported scheduling output is a decision failure, not an inferred voluntary stop or permission for automatic spending. An explicit no_change maintenance outcome does not mean no work remains, and deferred maintenance does not authorize continuation.

The runtime must not infer scheduling from trait values, modeled affect, a summary, another persona, or an unaccepted or superseded response. A valid current continuation disposition may remain binding across a local boundary.

**Honest stopping states.** A legitimate local stop may be supported completion, partial delivery, a named actual dependency, voluntary yield with unfinished work, or a resource, capability, or infrastructure block. An accepted peer contribution may justify a bounded wait for its actual result; acceptance itself is not that result.

Preserve the persona's concise explanation together with delivery gaps, responsibilities, and findings. Do not invent a quality verdict or demand private reasoning. Once the accepted goal is met, the possibility of further refinement does not require endless work. A separately accepted improvement duty retains its own disposition.

### Continuing a goal across local boundaries

Ending an invocation, navigation effort, repair attempt, or declared episode need not end the accepted goal. A local limit or stop does not establish completion, release responsibility, or authorize another allowance. A fresh decision may continue under the same live mandate and remaining controlling resources without another user request. Expanded scope or resources still require real authorization. A long accepted task does not automatically become optional personal exploration or an ongoing service.

![Unfinished accepted work preserves an accountable continuation disposition and durable state. Resumption requires fresh admission, with actual scheduling guarantees rather than a merely visible queue.](../assets/continuation.svg)

**Figure: A local stop is not the end of a goal.** This is a conceptual explanation of the design. [Read the exact rules](WORK-AND-BOUNDARIES.md#continuing-a-goal-across-local-boundaries); the explanation below retains their qualifications. [Open the illustration](../assets/continuation.svg).

<details>
<summary>Text equivalent of the illustration</summary>

A local stop is not the end of a goal

AN ILLUSTRATED DESIGN STORY

Pause the process; preserve the responsibility.

Work state

Accepted goal is still unfinished

A local yield, partial delivery or process restart does not silently end responsibility.

Keep what a restart needs

Keep the agreed scope and owner, exact work version, unmet outcomes, remaining resources, pending effects and real observations.

State what really happens next

An authorized opportunity to continue; a real blocker and reconsideration route; an accepted transfer; or an authorized ending. Otherwise expose the continuation gap.

Resume through a fresh decision

Recheck cancellation, authority, source eligibility, observations and capacity. Do not replay suppressed actions or invent a new allowance.

Persistently eligible accepted work receives another opportunity under declared scheduling assumptions. A durable queue entry alone is not that opportunity.

Characters personify design choices; they do not assert feelings or consciousness. Scenes are hypothetical.

</details>

**What must survive a yield.** For an accepted continuing mandate, yielding suspends activity rather than silently ending pursuit. Preserve the outstanding result, accepted owner or ownership gap, relevant actual observations, and one of the following:

- An authorized next opportunity.
- An actual blocker and its route for reconsideration.
- An accepted transfer.
- An authorized ending.

If no usable continuation opportunity exists, expose that accountable continuation gap. Merely recording an unfinished obligation does not pursue it. Reachable required work must not be abandoned solely because a local response, tactic, or optional refinement ended. A no-progress limit may end a tactic; it cannot declare the goal complete or fund the same failed tactic under a new name.

**Each continuation starts from current facts.** On every admitted continuation, the primary receives current scope, authority, obligations, consequential results, and remaining resources. It chooses the next useful step or a justified disposition. Suppressed old actions are not replayed.

The host preserves eligible opportunities under the deployment's declared ordinary-work scheduling and fairness policy; it does not choose the next semantic action. Structural checks establish current bindings and accountable dispositions. Whether stopping was useful or justified requires behavioral evidence. Fair consideration and another funded call guarantee neither progress nor success.

**Real wait triggers.** A dependency wait identifies its actual event source. An unaccepted offer, fragment cue, or promise of future investigation does not supply a trigger. When an already-retained outcome is registered and delivered, preserve the new wait's reason and classification instead of restoring an earlier one. A replayed notification is neither fresh evidence nor a new wake.

Explicit resume, new input, a genuine authorized event, or an ordinary-work scheduling opportunity may permit later work. Pause and cancellation still prevail. Waiting must not lose an event that arrives between inspection and durable registration.

## Recovery without invented success

Recovery restores the accepted situation and continues from evidence. It does not turn interruption into success. Restart preserves accepted state, exact identity, decisions, source restrictions, notifications, pending operations, reservations, cancellations, and ownership gaps. A fresh decision rechecks current scope and authority. Never replay an old action batch as a recovery probe.

![An uncertain external effect remains unresolved through restart. Reservations and responsibility persist until permitted evidence supports an appropriate next decision; missing acknowledgement is not definite failure.](../assets/effects-and-recovery.svg)

**Figure: Recover without inventing success.** This is a conceptual explanation of the design. [Read the exact rules](WORK-AND-BOUNDARIES.md#recovery-without-invented-success); the explanation below retains their qualifications. [Open the illustration](../assets/effects-and-recovery.svg).

<details>
<summary>Text equivalent of the illustration</summary>

Recover without inventing success

AN ILLUSTRATED DESIGN STORY

No reply yet. Did the action happen?

Sent request

?

Unresolved

An attempted action can have an unknown effect

Example: a request was sent, but no reply arrived

The absence of a receipt does not prove that the outside operation failed.

Keep the unresolved effect and reservation

Record what was actually attempted and what remains uncertain. Restart and repeated messages do not create a new budget or erase responsibility.

Reconcile using permitted evidence

Use the actual interface and observations to establish what happened. Do not repeat an action blindly when duplication matters.

Then choose the justified next step

Continue, repair, deliver a qualified result or remain blocked under current authority. Distinguish unknown usage from unresolved execution.

A request, dispatch, outside effect, received receipt and interpreted success are different events.

Characters personify design choices; they do not assert feelings or consciousness. Scenes are hypothetical.

</details>

**Provider and transport recovery.** A transport timeout or temporary provider outage is an infrastructure condition, not a voluntary persona wait. Declare a small immediate retry allowance. After that, use spaced, coordinated health checks with backoff and server retry timing. A probe that uses inference is a newly funded call. Confirmed quota exhaustion stops automatic inference retries. Credential failures remain visible and require repair.

Recovery schedules survive restart, but pause, cancellation, removal, retirement, and fences against adopting late results prevail. Apply these distinctions to initialization, model discovery, ordinary decisions, and context maintenance. Each provider attempt preserves its required maintenance input and individual accounting. Adopt at most one complete response for a logical invocation. Transport failure is not a completed maintenance decision or an authored no_change outcome.

**Read-only views.** Read-only interface activity provides coherent individual observations without holding the writer reservation. A changing multi-page traversal is still not a single snapshot; [search consistency and completion scope](../implementation/CONTRACTS.md#search-and-exact-reading) must remain explicit. Shared reads may coalesce while running, but closing one reader must not cancel another's request. Expensive file, history, evidence, and persona-context views load on demand and release subscriptions and payloads when closed.

### Bounded failed lookups

Repeatedly trying the same unavailable source must not consume resources indefinitely. After a declared small bound, failures for the same source target and policy state reuse the recorded failure. A change in source availability, direct policy, or exact source-history restrictions may justify reconsideration. Unrelated edits and fresh decision identities do not replenish the allowance.

Resolve convenient document references to the actual saved target before comparing them. Reconsideration still checks current access, never turns an earlier failure into success, and never reveals private contents.

**Preserve the original failure.** Recording a failure must not depend on successfully building an optional comparison index. Missing creation provenance and exceeded source-traversal bounds remain source admission failures with their original undispatched receipts. An unavailable dependency snapshot is not evidence that the source is unchanged and must not receive an invented comparison key.

An exact-action retry returns its original receipt only while that authoritative history remains retained and accessible. Otherwise, an honest unavailable or unresolved disposition grants neither reconstruction nor replay. Repair may permit a new authorized request without rewriting the old failure.

**Check decision authority before source failure.** Malformed, closed, paused, or otherwise unauthoritative model decisions have not established a source lookup failure. Diagnose decision authority before bounded source comparison; inaccessible provenance cannot hide an already-invalid decision. Preserve its undispatched receipt without consuming a genuine source retry allowance. Resumption and source repair cannot revive that rejected action. An otherwise valid request still receives normal source checks.

**Restricted recovery after a permission failure.** A permission failure may admit a restricted, normally funded recovery decision using only permissible metadata and remedies. The persona chooses among an owned policy change, fresh permitted context, a request to the owner, independent work, or an honest wait. Relevant source or dependency changes may wake affected participation once. Repeated unchanged failure must not create identical paid loops. No diagnostic waives provenance, responsibility, uncertainty, or a stopped state.

## Evidence, assessment, and exact release

Evidence must make clear what has actually been established. Having an installed tool, completing an operation, preserving an intact file, producing a useful result, obtaining a qualifying review, gaining human acceptance, and receiving external assurance are separate claims.

Where applicable, the evidence connects the need and criteria to accepted work, exact inputs, assumptions, actual observations, outputs, assessment, and current release. These are not compulsory stages for every answer. A simple response can be its own artifact, assessed through human creative judgment.

**Identify exactly what is being assessed or offered.** An artifact version identifies its exact content, producer or producing action, scope, input versions, type, policy, and derivation. A logical current result points to an adopted version while preserving attribution for its history. A submission binds the precise artifacts, criteria, assumptions, limitations, and assembly being offered. “Whatever is latest” is insufficient.

A fingerprint establishes that bytes are unchanged. It does not establish authorship, truth, consent, or approval.

**Record calculations, simulations, and experiments in context.** The record includes:

| Part of the record | Required information |
|---|---|
| Purpose and inputs | The question, criterion, source inputs, transformed inputs, units, and conventions |
| Method and execution | The method, configuration, parameters, assumptions, and actual run or observation |
| Outcome and interpretation | Warnings, results, interpretation, and limits |

Successful conversion does not prove that transformed inputs remain faithful to their source. A simulation, a reported observation, an independent measurement, a visual inspection, and parsing a file provide different kinds of evidence. Native source, preview, and exported view are also distinct. Claims of editability or reproduction need the appropriate actual observation. Where identical bytes are irrelevant, that observation must address semantic or numerical equivalence as appropriate.

### Persona judgment and independent qualification

The persona chooses how to assess a permitted, exact subject. It may read, reason through an argument, make a visual observation, consult others, use tools, or combine these methods. Within the same participation, it can create a result, assess its own work, inspect a peer's work, and revise. Its self-assessment does not count as independent approval.

**Independence depends on the actual separation.** Different identities, executions, models, and qualified outside reviewers provide different forms of separation. A newborn persona is not automatically independent of its parent.

A formal adopted review identifies:

- The claim, exact subject, and criteria.
- The actual assessor, their accepted responsibility, funding, applicable separation policy, and conflicts.
- The observations, findings, and limitations.

An optional request for another perspective does not create a formal release obligation. If a required suitable reviewer does not accept responsibility, report the gap. Do not invent approval or require a new birth as the solution. Human acceptance can legitimately assess a creative outcome without a numeric score; it cannot supply missing technical evidence.

**Use evidence for the claim it actually supports.** An additional citation may be unnecessary when the actual subject and an explained judgment suffice. When citations are supplied, they identify real, accessible receipts and their actual state. Failed or pending observations may support a limited conclusion, but they do not become successful execution. Even a successful command may be irrelevant to the claim.

Runtime checks establish attribution and exactness, not the semantic truth of an explanation. Record integrity and the substantive reliability of a reviewer each require their own evidence.

**Keep discretionary methods open to persona judgment.** Method-neutrality applies to the complete provider-facing request, including tool descriptions, maintenance paths, and the return to ordinary work. A failure counter, filename, domain label, or tool identity must not prescribe a repair, a new method, a shell operation, an extra reviewer, or a stop. Explicit task-specific obligations still bind. Optional assessment cannot be used to relabel an unmet result as satisfactory.

### Individual and shared sufficiency judgments

A persona can question its assumptions and judge whether its current result is sufficient. Participating personas can clarify one another's claims and disagree about what would improve the result or make it sufficient. Their characteristic context informs these choices; no separate reflection call or ritual debate is required.

![Five separate questions distinguish an individual judgment, shared sufficiency, delivery, required acceptance and remaining responsibility. None automatically proves all the others.](../assets/completion.svg)

**Figure: Individual and collective completion.** This is a conceptual explanation of the design. [Read the exact rules](WORK-AND-BOUNDARIES.md#individual-and-shared-sufficiency-judgments); the explanation below retains their qualifications. [Open the illustration](../assets/completion.svg).

<details>
<summary>Text equivalent of the illustration</summary>

Individual and collective completion

AN ILLUSTRATED DESIGN STORY

My part is ready.

Our shared gap remains.

?

One “done” label cannot answer all five

1 · Is my contribution sufficient?

An individual explains the exact scope, evidence, remaining defects and limits of their judgment.

2 · Is the shared candidate sufficient?

Apply adopted decision rights and criteria. Preserve attributed dissent and required gaps; a majority alone is not a release rule.

3 · Has the result been delivered?

Check the exact version and recipient access. Delivery can be partial and does not establish full goal completion.

4 · Is required acceptance obtained?

Keep stakeholder acceptance, independent review and outside assurance distinct. Apply each when required by the mandate, applicable policy or enabled design safeguards.

5 · What responsibility remains?

Record accepted-goal completion, unfinished commitments and legitimate continuation or ending separately.

Resource exhaustion, an editor’s identity or everyone stopping cannot close an unresolved required defect.

Characters personify design choices; they do not assert feelings or consciousness. Scenes are hypothetical.

</details>

**Make shared decisions attributable.** A shared decision to complete or continue identifies the exact candidate and scope, the relevant attributed judgments, any unresolved required outcomes, and the decision rights or method actually adopted for that work. Opening a task, editing its assembly, or summarizing a discussion confers no final authority.

Dissent remains attributable. It is neither an automatic veto nor implied endorsement, and silence is not agreement. If a material shared decision has no adopted basis for resolving disagreement, expose that gap while continuing independent authorized scope. The design requires no universal coordinator, unanimity rule, or vote.

**Separate sufficiency from possible improvement.** Participants can judge an adequately supported current version complete while still identifying optional improvements. Delivery, completion of the accepted goal, and stakeholder acceptance where required remain separate claims. Group enthusiasm and exhausted resources cannot satisfy an unmet required outcome.

The persona chooses whether to spend remaining resources on further questioning or revision, considering evidence, urgency, and commitments. Repeated disagreement supplies neither new evidence nor a fresh allowance. A resource ceiling ends activity; it does not establish that the result is sufficient.

**Later improvement needs an accepted basis.** It must fall within an existing accepted improvement mandate or obtain appropriate new acceptance, permission, and resources. Spare time or a suggestion alone supplies none of these. An existing continuing improvement duty survives an intermediate delivery under the [continuation boundary](#continuing-a-goal-across-local-boundaries).

Later work creates a new candidate. It does not silently inherit earlier review or acceptance, or reopen a completed mandate. New evidence of a real defect still changes the affected claim's current applicability under the following rules. Agreement to stop establishes neither empirical truth nor stakeholder consent.

### Citation snapshots and current applicability

A citation snapshot records which evidence existed, its state, and its provenance at a declared capture stage. It should do so without unnecessarily duplicating sensitive payloads. The snapshot's timing limits what it can establish: a snapshot recorded with a verdict does not prove that the same payload was supplied to an earlier model request, attended to, or understood. A receipt may change between preparation and recording. Preserve that limitation instead of inventing an observation history.

**Check snapshots at qualification and release.** Check the exact snapshot when first binding it to a qualification and again at later release. Missing, duplicated, foreign, erased, malformed, or required-but-absent snapshot metadata cannot be substituted or upgraded into valid historical evidence. A fingerprint grants no access to the source.

Earlier assessments that lack the currently required snapshots cannot acquire invented ones during migration. A fresh assessment provides new evidence under the criteria it actually uses.

**Keep a historical verdict separate from its present use.** The verdict remains attached to what was examined. Its current applicability is separately recorded as current, stale, pending, or unverifiable. A relevant change to inputs, assumptions, criteria, tool or check configuration, assembly, or review policy immediately invalidates the affected current claim pending reconsideration. The claim must not remain green while a background invalidation runs.

If the impact is uncertain, broader revalidation chosen by the persona may be needed. Missing dependency links do not prove that nothing was affected.

**Release must bind one coherent result.** The release transition binds the mandate, criteria, assumptions, exact assembly, review policy, qualifying assessments, blocker dispositions, authority, and delivered scope.

- If a relevant change takes effect before release, the old review cannot seal the new result.
- If release takes effect first, it remains historical; the later change creates a new candidate.

Neither human acceptance nor a positive assessment silently transfers to newer bytes or discharges another unresolved finding.

## Delivering the result

A result is delivered only when it reaches its permitted recipient. Producing workspace bytes, publishing a retained version, submitting it, adopting an assembly, delivering it, and accepting it are separate observations. A document that names a local archive does not deliver that archive.

**Keep publication and inspection usable.** Their capabilities must remain discoverable after older execution history leaves active context. Relative paths resolve consistently. Publication reports the resolved location and the original retention failure without inventing a different path or a success.

**Send the answer through an authorized surface.** A requested answer reaches an authorized user-facing surface. Private activity, a saved but undelivered draft, and an operator's internal view do not deliver it.

For ordinary chat and work delivery, a call's authored previews, commentary, and reply remain withheld until complete work-and-maintenance validation succeeds. The host may truthfully report that the call is pending. Permitted operator diagnostic inspection remains a separate activity under the [contracts](../implementation/CONTRACTS.md#every-persona-invocation).

The primary decision explicitly chooses either no reply or separately authored reply text with private-user or exact-work visibility. A missing audience is invalid; activity text never fills it automatically. A work reply reaches that work's audience, not every task in its environment. Choosing an audience does not disclose private ancestors or earlier correspondence.

**Apply message controls at delivery.** A reply obeys the same current permissions, source restrictions, limits, cancellation, freshness, journaling, and action barriers as other messages. It follows preceding completed synchronous actions and precedes an explicit wait. A failure or asynchronous boundary may suppress delivery that depends on it. A request for an in-app response does not authorize unrelated communication, and a mode that prohibits delivery remains prohibitive.

**Treat submission notices as separately authored messages.** An optional notice has its own text and explicit audience. The notice and submission commit together or neither does. The notice references the exact submitted version; its private content does not silently become part of the submission. If that notice is explicitly read later, its restrictions apply normally. Choosing a shared notice does not change any earlier audience.

**Show what actually arrived.** Delivery evidence identifies the successful receipt, exact message or submission, work, audience, and actual requested contents. A success flag, generic notice, or empty failure list alone cannot establish delivery of the promised result.

Current delivery observations report retained references, attachment counts, mandate attribution, restrictions, and permitted owner remedies. They do not search local files, judge quality, or infer unknown historical applicability. Failed checks retain their working directory, diagnostic completeness, and exact recovery references through compaction.

### Honest outcome vocabulary

Use outcome terms that tell the recipient both what arrived and what remains unresolved.

| Outcome | What it says |
|---|---|
| Delivered | The agreed scoped result reached its destination with required current evidence. |
| Delivered with conditions | An authorized conditional result was delivered with conditions visible beside the claim. |
| Partial delivered | Useful portions arrived; the original full need remains unmet. |
| Blocked internally or externally | A named capability, ownership, resource, information, authority, review, or outside-observation gap prevents completion. |
| Unaccepted | A result exists but required acceptance is absent or declined. |
| Canceled or declined | An explicit disposition ended work without implying success. |

Keep activity, ownership, coverage, submission, assessment, applicability, human acceptance, outside assurance, and optional improvement distinct. If a report gives a fraction, it states the denominator. Stopping activity does not complete a need.

A closeout report identifies delivered versions, current checks, missing scope, conditions, outside requirements, accepted remaining owners or ownership gaps, resource use, uncertainty, and the decision needed to continue. A digital result grants no authority to construct, operate, treat, publish, or certify something else.

## Lifecycle and optional exploration

Creating a persona, accepting it into a group, and accepting work are separate events. Creation also remains distinct from bounded initial fragment authorship and orientation. The [seed-to-accepted-character path](PERSONA-CORE.md#a-continuing-persona) uses only currently permitted seed and invitation material within the same controlling allowance.

**Preserve the actual beginning.** A creation retry returns the same identity and actual initialization. It does not regenerate a preferred character, duplicate money, or start replacement births after a decline. Seed provenance, the generated candidate, the accepted starting revision, and any supplied alternative account remain separately attributable. None supplies an invented human biography or experience.

**Track each kind of state separately.** Lifecycle, quarantine, membership, model configuration, work participation, and accepted obligations have different meanings. Active status does not imply continuous inference, and completing work does not retire an identity.

Pause, model change, removal, retirement, and restoration preserve obligations, effects, spending, uncertainty, and applicable birth counts. Relevant eligibility changes must fence in-flight decisions before another action can be admitted.

**Resolve ownership before retirement.** Every open obligation needs one of three dispositions: accepted transfer, authorized cancellation, or a policy-permitted explicit block. A blocked obligation stays unresolved, attributable, and visible, with its condition and escalation route or missing responsible party. A retired historical owner cannot execute it.

Reactivation requires new authorization. It does not clear quarantine, restore membership or grants, replenish resources, or replay old operations. Local restoration does not authorize a second independent host to activate the same identity.

**Retain starting references within policy.** Starting-state references survive permitted changes, while sensitive payload retention follows policy rather than an unlimited history mandate. Where allowed, erasure leaves an honest minimal provenance disposition. It must not leave fabricated replacement values. These starting-state facts remain independent of the persona's current self-authored character.

### Between-task exploration is explicitly funded

A persona may investigate unfamiliar methods during active work within that work's existing purpose, authority, and funding. Personal exploration between tasks needs a separately enabled opportunity. It is disabled until an operator enables a permitted environment, an existing allowance, explicit episode bounds, finite recurrence, and expiry. An omitted setting never means unlimited activity.

Within those limits, the persona chooses its question, experiment, collaborators, and stop condition. It cannot enlarge or renew its permission.

**Task-free social activity is also optional.** An enabled between-task opportunity may permit low-stakes social or recreational exchange without an assigned deliverable or topic. The persona chooses whether to engage, whom to approach, what to discuss, and when to stop, within the enabled audience, contact preferences, and resource scope.

Availability does not mean acceptance. Refusal or silence creates no participation duty. The host supplies eligible opportunities, not conversational content or compulsory partners. A chosen social purpose may end without an artifact, durable revision, or later productivity benefit. Activity without an assigned task still needs operating authority. Dormancy remains valid, and the accounting rules below do not require inventing an external task.

**Account for the whole episode.** An episode is ordinary work with a purpose, owner, funding, observations, and disposition. Its calls and time include orientation, collaborators, late review, nested inference, and failed admitted attempts. Authoritative work-to-episode lineage determines funding even when a presentation omits the episode label.

New participants and child work receive no fresh allowance, extra deadline, or foreground status. A distinct episode needs a separately authorized opportunity.

**Give eligible foreground work priority.** Before starting an optional episode, and before admitting each new discretionary optional call or action, check for eligible, independently authorized foreground work. Priority applies whether that work:

- Originated with a human or a persona.
- Is queued or running for the same persona.
- Uses the optional episode's resource root, including another persona's foreground work on that root.

Historical, completed, paused, canceled, or removed participation is not active foreground demand. Neither is work awaiting an indispensable permission or actual event when it has no independent eligible step. An unanswered optional preference alone does not make work ineligible. Distinct personas on unrelated resource roots remain eligible.

Optional episode children and peer requests cannot gain foreground status without independent authority. Priority gives a queued request consideration, not automatic task acceptance. It does not retroactively revoke admitted operations, erase their costs or effects, or displace required reconciliation and closeout of accepted obligations. Discretionary optional production must never use protected closeout capacity.

**Recheck and record admission before dispatch.** Admission rechecks current authority, environment, source access, funding, recurrence, pause, cancellation, and expiry. Persist the opportunity, episode, recurrence consumption, work linkage, and reservations coherently before dispatch. Duplicate triggers resolve to the same admitted episode; they must not cause duplicate inference.

Source-derived instructions and their previews keep their exact source restrictions. An operator schedule does not remove those restrictions. Imported or historical opportunities are not live execution grants.

**Handle failure according to whether admission occurred.**

| Case | Required handling |
|---|---|
| Failure before admission | Leave an inspectable blocked start. Do not consume recurrence or leave provisional work, invitations, or participation that appear successful. |
| Releasing provisional reservations | Release only when there is no admitted operation, real charge, or uncertain exposure. |
| Failure after admission | Keep the same admitted episode, including consumed recurrence, actual charges, uncertainty, and accepted responsibilities. |
| Timeout or crash with an ambiguous outcome | Reconcile what happened before rollback. |
| Retried action | Keep its own receipts and the same episode limits. A fresh episode requires a new authorized opportunity. |

Pause, disabling, expiry, and cancellation prevent subsequent starts while preserving actual stop receipts and incurred costs. Closing an episode must account for collaborators' accepted work and unresolved effects. Ended participation cannot remain executable. A useful negative finding, partial delivery, cancellation, and completion remain distinct outcomes.

### Fairness without promised success

A bounded page of opportunities must not become a permanent limit on which opportunities receive consideration. Future or paused entries must not indefinitely hide later work that is due and eligible.

Any claim that eligible work will eventually be considered must state its assumptions about scheduler progress, queue changes, restart, recovery, and persistent eligibility. Consideration does not guarantee funding, voluntary acceptance, feasibility, or useful completion. Cases where everyone declines or no owner accepts remain legitimate. Repeated failed starts, reminders, new names, and unchanged summaries must not create an idle inference loop or reset limits.

**Preserve the permission exactly.** Controls preserve its actual precision and expiry. Opening an editor cannot round an allowance upward, renew it, lose a sub-minute bound, or reinterpret an unchanged daylight-saving overlap. Invalid or nonexistent local times require correction rather than silent normalization.

## Relationships and optional wider deployments

Relationship fragments describe how a persona approaches particular collaborators. They express the persona's own directional, contextual interpretations of real, attributed exchanges. They can influence invitations and working methods, but they do not become universal competence rankings, reputation-based authority, or access to another participant's private fragments and records.

Trust can narrow after counterevidence. Affinity supplies no commitment, credential, or human consent. A persona with a human-like character remains transparently AI. A distinctive voice does not justify fabricated life events or subjective claims.

The extensions below apply only when enabled. They organize additional applications and assurance; a basic persona needs no society, continuous service, physical body, or institutional ceremony.

| Extension | Scope and required boundary when enabled |
|---|---|
| E1: functional embodiment and profiles | Make the whole persona inspectable through its characteristic context, LLM invocation, interaction, action, consequence, and permitted self-revision. The extension adds explanatory views; the whole persona already exists in that sense. Layers, avatars, and profile displays do not establish feelings, consciousness, competence, or physical embodiment. |
| E2: communities and institutions | A charter identifies purpose, accountable sponsor, membership and exit, real authority, resources, information policy, conflict, appeal, renewal, and dissolution. A society neither merges private persona-context corpora nor requires a leader. |
| E3: sensitive human-facing use | Be transparent about AI identity. Support declining retention of personal information and leaving. Do not invent relationships, human experiences, diagnoses, qualifications, or endorsements. Education, support, and public participation need deployment-specific policy and evidence. |
| E4: ongoing services | State the accepted owner, permitted triggers, freshness, episode and total bounds, review, renewal, retention, escalation, and stopping. Disconnection leaves an observation gap. A human escalation route requires an actual accepting recipient, acknowledgment expectations, and defined behavior when that recipient is unavailable. |
| E4: physical interfaces | Specify the device, environment, permitted effects, observations, operating limits, human override, safe stopping, delayed effects, observation loss, and conflicting controllers. Simulation does not establish physical safety. Appropriate independent assurance is required before expansion. |
| E5: conformance and authoring aids | Worksheets, identifiers, and profiles organize claims and evidence. They impose no forms or mandatory phases on simple work. Completing a form establishes neither execution nor consent. |
| E6: contribution and evidence governance | Preserve exact versions, criteria, failures, provenance, and bounded public claims. Maintainer acceptance changes the design without establishing runtime conformance. Licensing and contribution terms remain owner decisions. |

**Keep community decisions accountable.** Identify the requester, authorized decision-maker, beneficiaries, affected parties, people actually consulted, and representation gaps. Simulated stakeholders cannot consent for real stakeholders.

Decision records preserve the exact question, eligible participants, adopted rule, endorsements, dissent, authority, and commitments. Creating personas cannot multiply human-controlled votes or resources. An appeal needs an accountable human or institution. Exit or dissolution must hand off, legitimately cancel, or expose every unresolved obligation without indiscriminately copying private fragment collections or supporting records.

**Keep service and host boundaries explicit.** Completing one service episode establishes nothing about future episodes and renews no permission. If an essential escalation route is unavailable, activity may need to narrow or pause safely.

Cross-host federation is separately gated from local continuity and read-only exchange. Expanded activation requires explicit contracts for exclusive activation, transfer, revocation, privacy, authority, and failure. Community artwork grants no permission to activate a persona on another host.

## Human-readable state and controls

The interface helps people understand what is wanted, what is happening, who accepted what, what changed, what evidence exists, and what needs their decision. Work, Personas, Environments, Fragments and Assets, and Tools provide understandable navigation. Advanced governance should not obstruct a small request.

**Label draft inspection honestly.** Where operator diagnostics may display authored drafts, both summaries and commentary are explicitly labeled unvalidated. That inspection is separate from ordinary chat or work delivery. It does not establish a completed result, accepted decision, or truth of the draft's claims, and it grants no action authority. Source, access, and retention controls still apply. Raw private reasoning is excluded.

Distinguish model-call status, complete-response validation, actual persistence, action receipts, and delivery. A terminal provider event alone establishes none of the later stages. Even a save-success claim in a validated response needs its actual acceptance receipt.

**Show the character that actually governs the persona.** Profiles display the same accepted OCEAN, baseline VAD, additional characteristics, and own-voice account used in persona context. Transient modeled affect is clearly separate. Profiles also distinguish interests, maturation, capability evidence, commitments, lifecycle, and actual inference configuration, and show starting versus current state and actual authorship.

Make these outcomes distinguishable: considered with no change, proposed, retained, supplied later, acted on, and benefit evaluated. Keep blocked maintenance, failed calls, and unresolved deferrals visible without overwhelming ordinary work. Show meaningful retention limits and unavailable historical evidence where they affect a claim.

A fragment count, calendar age, avatar animation, or modeled state establishes neither competence, development, work, nor emotion. A claimed portrait needs a real artifact or an explicit placeholder.

**Make controls understandable and voluntary.** People can inspect and change authorized constraints, accept or decline effects, allocate resources, inspect recruitment, pause or cancel, request review, and accept limited results with visible conditions. Approvals explain consequences, audience, material content, assumptions, limits, and alternatives. They must not pressure people to expand access merely to keep a persona busy.

**Support accessible use and honest status.** Support keyboard use, clear focus, readable text, small screens, and progressive disclosure. Color or animation alone must not convey status.

Artifact views distinguish connecting, receiving, verifying, preparing, ready, unavailable, and failed. Receiving bytes does not prove that a preview is ready or a result is valid. Empty installations explain founder creation instead of displaying a fictional active society. Missing owner, declined invitation, exhausted capacity, unavailable capability, missing review, and stale result each need a distinct, honest state.

## Verification and evidence preservation

Verification must show what was actually examined and what the evidence can support. The [acceptance catalogue](../evaluation/ACCEPTANCE.md) exercises these obligations, but a listed case is not an executed result. Preserve requirement identifiers and the exact old criteria attached to historical results.

A protocol may permit varied organizations without showing that personas chose them. Evidence of those choices is, in turn, different from evidence of useful cooperation. Before claiming that no hidden task script exists, inspect actual prompts, policy, configuration, and adapters as well as attributed decisions.

**State what a formal model covers.** A formal model declares its initial conditions, transitions, invariants, temporal assumptions, exclusions, and mapping to requirements. It must show non-vacuous legal histories and preservation across transitions, rather than requiring the whole desired invariant as every admission condition.

Record exact design and model versions, toolchain, dependencies, actual compilation, and trusted axioms. Uncompiled proof drafts, bounded models, and checked theorems provide different evidence. Without separate correspondence evidence, a protocol theorem does not establish authentic receipts, persistence, atomicity, access control, domain truth, privacy assurance, or that an implementation refines the model.

### Capturing a declared research stage

A research stage can preserve a fixed body of evidence without declaring the product complete. Before capture, establish what has actually settled. Execution settlement is independent of acceptance: a quiet model queue does not establish that jobs, transfers, pending decisions, recovery wakes, or outside effects have settled. Unknown inference billing differs from an unresolved external effect. A failed action can be settled while still being unhelpful.

**Capture only after rechecking the observed state.** An explicitly declared research stage may capture immutable evidence only after a transactional recheck. Preserve obligations and stopping dispositions. Prevent new execution in the captured stage while allowing reads and reconciliation.

If the state changed, reject capture without partially pausing participants. Later stages have new boundaries; they do not replay paid work. Capture is not a product-completion verdict.

**Preserve the exact captured evidence.** Bind it to exact versions, receipts, output digests, and required experiment audits. A restart may finish exporting those bytes. It must never collect a different result under the same capture identity or rerun paid work. Missing audits and unresolved effects remain incomplete.

Ordinary authorized review and continuation remain available outside the sealed stage under their own authority.

### Collecting implementation diagnostics honestly

A diagnostic record must distinguish what happened during execution from what happened while collecting the evidence. Never executed, compiler failure, failed test, incomplete collection, and actual behavioral outcome are distinct states.

**Preserve the available sources independently.** Keep the source revision, run and attempt, available job and step metadata, service annotations, raw responses, and logs. Missing logs neither erase an available annotation nor identify a cause. Account or runner repair belongs to its responsible operator. It must not be replaced by disabling checks, changing spending grants, or exposing private source.

**Verify attribution before combining records.** Successful retrieval does not show that execution passed. Retain empty or whitespace-only logs, but do not treat them as usable execution logs. A missing inventory differs from a recorded job with no steps.

Malformed or conflicting jobs, checks, revisions, or step identities cannot be silently combined. Verify identities and revision before attributing diagnostics. Preserve independently retrieved, unverified annotations and label them as unverified.

**A positive verdict needs consistent execution evidence.** An aggregate success cannot conceal a failing check, job, step, or service-failure annotation. Cancellation, timeout, action required, pending work, and unknown outcomes are non-passing. Optional skipped steps and warnings alone need not fail otherwise evidenced success.

A positive diagnostic verdict requires consistent successful outcomes and recorded execution steps. A success label without recorded steps is insufficient. The summary and exit disposition must agree about remaining blockers.

**Check the completeness of paged inventories.** Where the service reports inventory counts, reconcile all pages before claiming complete collection. Counts must be nonnegative exact whole numbers, consistent across pages, and bound to verified metadata.

A disappearing, changing, invalid, truncated, or excess count leaves collection incomplete. A short page alone does not establish completion. Show reported and collected counts; unknown is not zero. Zero annotations alone says nothing about execution success.

**Keep collection failures visible without losing valid material.** Malformed or duplicate records must neither erase valid collected material nor prevent independent collection of logs and jobs. Preserve original responses and mark unusable parts. Never overwrite an earlier bundle to make a later attempt appear complete.

A storage failure is a collection failure, not an unavailable remote log. Complete collection of unsuccessful execution still records unsuccessful execution.

**Keep the level of evidence explicit.** Mechanism checks, diagnostic-helper checks, synthetic-provider checks, actual model behavior, delivered domain quality, benefit from retained revisions, and deployment assurance remain separate. Report total costs, negative outcomes, assistance, and limitations. No source brief, diagram, successful documentation check, or compiled fixture establishes that a persona has become a useful autonomous collaborator.
