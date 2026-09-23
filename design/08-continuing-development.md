# 8. Continuing character, experience, and exploration

[Design index](README.md) · [Identity](01-personas-and-identity.md) · [Learning](02-memory-and-learning.md) · [Acceptance](../evaluation/CONTINUING-DEVELOPMENT.md)

## Purpose and status

A persona should develop a continuing way of approaching work. Its starting dispositions, authored interests, relevant experience, relationships, accepted obligations, and current situation can influence what it notices, investigates, tries, questions, retains, and does next. The system supplies authorized memory, tools, opportunities, and execution; the persona chooses the substantive direction.

This chapter defines required behavior, not a claim that an implementation has delivered it. Character included in a request proves inclusion, not behavioral influence. Retained content proves retention, not learning benefit. The acceptance record must distinguish mechanisms, observed choices, and independently assessed outcomes.

The rules extend the identity, memory, cooperation, authority, and evidence chapters. They do not introduce professions, a domain workflow, a central planner, compulsory exploration stages, or a second autonomous runtime.

## CD-01 — Starting conditions and current state

A user may supply narrative character and any OCEAN or VAD values at creation. Missing numeric values must be initialized once, uniformly within the documented ranges: OCEAN from zero to one and VAD from minus one to one. Explicit zero and both endpoints are valid supplied values. Invalid values are rejected rather than clamped, replaced, or silently randomized. Omitted narrative character is unspecified, not a fabricated biography.

The initializer must preserve its generator version, reproducibility seed, actual values, and each field's origin. This is synthetic initialization, not a scientifically validated population distribution. Initial profile values are separate from references to supplied seed material; choosing material does not copy a sponsor's identity or authorize reading private sources.

The initial snapshot is immutable. Current narrative, dispositions, affect, and authorship policy are separate continuing state. A creation retry returns the same accepted identity and initialization. Reloading a view, restarting a node, accepting another invitation, or changing an environment must not rerandomize an existing persona. An imported history with missing provenance must be described as missing; restoration must not invent an earlier seed.

## CD-02 — Self-authorship and operator control

Creation offers **Let this persona shape its character**, enabled by default. When enabled, the persona may revise its narrative character, OCEAN, and VAD through attributed updates. When disabled, those fields remain user-controlled. Learning methods, retaining experience, and authoring work-specific judgments remain possible, but another field must not become a hidden override for the locked profile.

The operator has a separate attributed path to edit current profile values and the policy. An operator edit must never be recorded as the persona's own decision. Edits preserve the original seed, earlier versions, actual author and operation, changed fields, and an explanation. Experience-based claims need relevant accessible evidence; initial preferences need not invent experience to justify themselves.

Profile or policy changes invalidate decisions that observed the previous profile before additional actions can be admitted. Exact retries return their original receipts; suppressed actions are not replayed by re-enabling self-authorship. A policy edit grants neither resources nor an automatic wake.

During its first funded orientation the persona should consider its seed and record a concise initial approach or an explicit deferral. A name and portrait remain optional. Orientation must not require repeated biography-polishing calls before useful work. With a locked profile, the approach or deferral belongs in separately attributed working state, not a forbidden character edit.

## CD-03 — Distinct continuing state

| State | Purpose | Boundary |
|---|---|---|
| Starting seed | Attributed initial conditions. | Never retroactively rewritten. |
| Current character and OCEAN | Continuing tendencies and preferences. | Not fixed roles, numerical authority, or competence. |
| Current VAD | Situation-sensitive modeled affect. | Not enduring disposition or a claim of subjective experience. |
| Interests and open questions | What the persona wants to understand or improve. | Interest does not authorize expenditure or establish capability. |
| Learned fragments | Reusable interpretations, procedures, and cautions. | Experience, applicability, limitations, and correction remain explicit. |
| Relationship interpretations | Directional understanding of interactions with named participants. | Not shared consensus, permission, or another participant's private memory. |
| Current commitments | Responsibilities actually accepted. | Obligations remain despite preference, inactivity, or an unfinished handoff. |
| Demonstrated capability | Successful operations under stated conditions. | A trial is not a professional qualification or universal skill. |

Persona-scoped interests and relationship interpretations remain discoverable across work; work-scoped agendas remain scoped to their work. Ownership, authorship, visibility, and source restrictions apply to both. Leaving a work does not automatically erase personal state or carry that work's access into the next environment.

## CD-04 — Character-informed choices and retrieval

Character may inform which uncertainty receives attention, whether to establish a baseline or investigate alternatives, when to consult or challenge a peer, what evidence could change a judgment, what is worth retaining, and whether to persist, change method, or stop. These are possible choices to observe, not stereotypes to require.

Accuracy, honesty, essential verification, user constraints, and accepted obligations apply at every trait value. Low conscientiousness does not authorize carelessness. High dominance does not create authority over peers. A persona may choose any suitable method or tool under its actual permissions.

Every decision receives current profile and policy, relevant personal interests and work agenda, accepted obligations, consequential observations, applicable selected lessons and limitations, attributed relationship context, exploration opportunities, and current resource facts. Mandatory authority and obligation information remain separate from optional historical context.

Initial retrieval remains lexical and supports persona-authored query expansion and pagination. It includes interests, agenda, relationship context, and explicit investigation questions without displacing task and corrective-feedback coverage. Candidate previews, selection, exact inclusion in a dispatched request, and later action are different events. Compact admission references should connect a choice to the state it received without archiving raw model transport or private reasoning.

## CD-05 — Exact experience and authored interpretation

Experience can include a successful or failed tool trial, a limitation, a peer correction, clarification, collaboration, a failed substantive check, or a lesson becoming inapplicable. Expose consequential observations with exact references in the next ordinary decision where possible.

An evidence reference identifies either an exact record version or an exact retained action receipt by action identity and receipt digest. The digest identifies a defined preserved receipt representation, not a mutable current projection or a manually asserted success. Current access and inherited source restrictions are rechecked on use. Referencing an execution must not require manufacturing an extra artifact solely for citation.

An observed failure can support learning about that failure. An uncertain effect supports an uncertainty finding, not a claim that the intended action succeeded or failed. A later reconciliation does not silently rewrite the earlier observation. Superseded evidence may explain history, but cannot establish that an old method remains applicable now. Inaccessible evidence is not silently replaced by a newer or public source.

A persona-authored experience review records interpretation or disposition: retain, revise, decline retention, defer, or make no lasting change. Retained-change links must resolve to actual attributable profile, fragment, or perspective revisions. Linking a record must not itself author that change or establish improvement. Temporary affect and lasting development remain distinct. A trait-number change is not evidence of growth.

This is a relationship among situation, attention, action, observation, interpretation, retained change, and later use, not a mandatory sequence of calls. Trivial successful commands and unchanged retries must not produce an automatic stream of lessons.

## CD-06 — Authorized exploration

Active-work investigation may use the work's existing purpose, authority, and funding. Optional personal exploration between tasks is disabled until the operator explicitly enables it for a persona, permitted environment, controlling resource root, finite episode allowance, finite recurrence allowance, and expiry. An omitted allowance or expiry is not unlimited permission.

The persona chooses the question and proposed experiment. The scheduler determines when an authorized episode can run, not the domain solution. An episode uses ordinary work and participation runs, remains visible to the user, and has an explicit stopping condition. It can end with a useful negative finding, partial understanding, or an honest decision to stop.

Policy changes require operator authority and attribution. A persona cannot increase allowances, change the controlling root to evade spending, extend expiry, or reopen a cancelled episode. Funding is conserved under the existing root, including protected finishing capacity. Enabling exploration never creates money, execution permission, accounts, or extra inference capacity.

## CD-07 — Durable opportunities without idle loops

The opportunity, authorized trigger, and resulting ordinary work/run identity must be durably connected. Claiming a trigger and creating its episode are one accepted transition. Concurrent delivery or restart cannot create duplicate work, inference, or external execution from the same trigger. Recovery observes already-created work and receipts instead of launching a replacement.

At the actual start, recheck policy generation, enabled state, expiry, environment access, persona availability, current funding, and recurrence capacity. A stale trigger is cancelled or visibly blocked, never admitted under an earlier allowance. Pausing or disabling prevents subsequent starts. Cancelling an episode also uses ordinary run/job cancellation semantics; already observed effects are not rolled back or forgotten.

New user work has scheduling priority over optional exploration. Background activity cannot consume protected closeout resources. An unresolved opportunity can remain visible without generating calls. An unchanged status message, reworded summary, or repeated reference to the same event is not a new opportunity.

Experience review normally rides the next ordinary decision. A separate funded reconsideration episode requires a permitted policy and a new consequential event with stable evidence identity. Neither a pending interest nor an empty inbox is an automatic inference loop.

## CD-08 — Accountable stopping and substantive correction

A stop distinguishes an outside dependency, another participant's accepted contribution, a scheduled exploration opportunity, voluntary yielding with unfinished work, partial delivery with gaps, a result with applicable checks complete, and a resource/tool/runtime block. A missing human answer blocks only the dependent portion; peers may help under explicit assumptions without supplying human consent.

Before a continuation owner stops, its context must clearly include unresolved obligations, current findings, pending opportunities, and relevant unanswered questions. Submission and successful message delivery cannot suppress them. Waiting is legitimate and does not require infinite retries. Remaining ownership and the authorized future trigger remain visible. An unsupported completion claim is not silently accepted.

A working interpretation or proposed check is persona-authored, not a rewrite of the user's request. Review records identify what was actually examined, the exact version, what a check establishes, untested claims, and repair or investigation needs. Findings reach the responsible owner and remain pending until explicit disposition. Producing a corrected artifact does not automatically resolve a finding against its predecessor.

Viewing an actual rendering differs from parsing a file or reading labels. Execution and image-observation evidence must identify what was really available to the reviewer. The runtime enforces links, freshness, ownership, and honest transitions; it does not become a domain judge.

## CD-09 — Research and tool learning

Search and page reading remain shared environment tools, removable at creation. Availability and failure observations are backend-specific. Blocked access, no results, unrecognized responses, transport failure, and the persona's judgment of irrelevant results remain distinct. A successful HTTP response is not successful research.

Preserve the actual query and attributed original-source links. One search-engine failure does not establish that another configured backend or direct page reading is unavailable. An optional operator-configured HTTP search backend may return normalized results. Credentials remain outside persona context; redirects must not silently forward credentials to another endpoint. No account creation, purchase, or automatic authority expansion follows failure.

Personas may identify needed capabilities, investigate candidates, choose representative trials, prepare tools under enabled host authority, observe outcomes, retain useful steps and limitations, and recheck applicability later. These are available activities, not compulsory stages. No application or profession is hard-coded into the general mechanism.

## CD-10 — Human visibility and completion evidence

Creation controls distinguish supplied values from missing values that will be initialized, show the enabled-by-default self-authorship choice, and expose optional exploration only with its required funding and schedule controls. Current-state views distinguish the seed, current profile, authors and reasons for changes, interests, experiments and observed outcomes, retained lessons, later uses, permitted relationship interpretations, and current exploration stopping condition.

Use separate labels for **tried**, **retained**, **used later**, and **benefit evaluated**. Do not display a generic learned-skills count that conflates these facts. History, evidence, and artifact viewers load on demand with pagination and released previews; raw JSON and model transport are not the normal experience.

Mechanism correctness, observed character influence, and demonstrated outcome improvement have separate acceptance gates. More profile prose, changed numbers, installed tools, or artifact counts cannot substitute for the [matched character, transfer, and minimal-brief evaluations](../evaluation/CONTINUING-DEVELOPMENT.md).

## Rationale and alternatives

One persisted seed makes starting conditions attributable without prescribing a role. Independent current state permits development without rewriting the past. A user-controlled authorship switch preserves authority without preventing learning. Personal perspectives provide continuity without merging private memories. Exact receipt references reduce retention friction without weakening evidence or access checks. Ordinary work/run episodes avoid a second runtime and conserve existing authority and accounting.

Fixed trait-to-tool mappings, compulsory lesson writing, automatic background polling, and richer prompting alone were rejected as substitutes: they either remove persona choice, invent learning, create idle expenditure, or fail to establish the required mechanisms and outcomes.
