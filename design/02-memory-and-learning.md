# 2. Memory, context, and learning

[Design index](README.md) · [Previous: identity](01-personas-and-identity.md) · [Next: work](03-work-and-cooperation.md)

## Three things that must not become one

**Work state** records what is currently agreed, required, blocked, or adopted. **Evidence** records what was actually observed, produced, or checked. **Persona memory** records what a persona retains and how it interprets that experience.

A fragment saying “the result passed” cannot replace the actual review. A friendly summary cannot erase an unresolved finding. An ordinary document does not automatically become learned knowledge merely because it is stored.

The design supports learning through persistent, selected context. It does not assume automatic model-weight training, perfect recall, or guaranteed improvement.

## A fragment's information contract

| Information | Why it matters |
|---|---|
| Owner and author | Identifies whose interpretation it is and who can revise or share it. |
| Content and title | States the actual lesson, procedure, preference, or concern. |
| Selection trigger | Explains situations in which it may be relevant. |
| Authored organization | Retrieval cues and relationships to other owned fragments make a useful prompt part discoverable without copying the entire old task. Relationships do not automatically select a fragment. |
| Character at authorship | Links an LLM-authored fragment to the persona and character revision supplied to that decision. Attribution does not mechanically establish a writing style or correctness. |
| Sources and source type | Distinguishes direct experience, another participant's report, supplied documents, and inference. |
| Applicability and assumptions | Limits where the interpretation may be used. |
| Uncertainty and counterevidence | Prevents a retained mistake from becoming unquestionable truth. |
| Revisions and supersession | Preserves what changed and which earlier interpretation is replaced. |
| Visibility and retention | Controls who may read it, where it may travel, and when its content must be restricted or removed. |
| Later use | Distinguishes requested retrieval, actual inclusion in context, subsequent action, and assessed outcome. |

A numerical confidence label is not a calibrated probability unless evidence establishes that meaning. Skills may be procedural fragments with supporting tool and outcome evidence; they do not need a separate credential engine. Learning work can use ordinary work and environments rather than a compulsory curriculum system.

## Example: a useful but limited lesson

**Title:** Recheck dependent outputs when an adopted source changes.

**Content:** Before treating a derived summary or calculation as current, identify the source version behind it. A result checked for an older source needs an applicability decision after a relevant change.

**Origin:** In the illustrative house example, a schedule still described the prior model after a layout revision. A reviewer found the mismatch, and the author regenerated the schedule.

**Applicability:** Version-dependent work such as documents, datasets, and coordinated design outputs.

**Limitation:** A dependency record may be incomplete. Uncertain impact requires broader revalidation, not an assumption that nothing else changed.

This is an authored example, not a memory produced by a live persona. It demonstrates what a fragment should communicate without prescribing a serialization format.

## The learning loop

A persona observes an event, interprets its significance, and decides whether anything is worth retaining. It may create, revise, combine, restrict, or stop selecting a fragment. Required work evidence remains available even when no fragment is authored.

The current context is also the cue for the next context. In every decision the persona considers what new observations and active prompt fragments imply for learning, organization and retrieval. It chooses whether to retain, revise, relate or stop using a fragment, and can author a focused retrieval query and concise handoff for its next decision. No change is a valid judgment when nothing useful was learned. This responsibility does not require a database write, separate reflection call or ceremonial checklist after every action.

Fragments are reusable prompt parts written by the persona's current LLM decision. Their sentences should sound like that persona: character, prior experience, perspective and uncertainty inform phrasing and interpretation. The runtime must not substitute a generic background author, append decorative trait labels, rewrite all fragments when character changes, or treat personality as permission to distort facts. Retain the character-at-authorship reference; a later persona revision may choose to reinterpret and revise an earlier lesson. Operator-supplied prose must not be presented as LLM-authored learning.

Authorized retrieval uses the current need, authored handoff and query, active fragments and their authored relationships, alongside consequential feedback. These are bounded cues, not automatic selection or an instruction to follow every linked lesson. The persona assesses applicability and chooses what enters its next context. Current authority and obligations remain independently available. Curation must not import another run's private handoff or lose source restrictions.

In a new task, retained fragments remain organized in the persona's authorized index. A mature persona can discover and select an applicable procedure early, then act without replaying the original investigation. It still checks new conditions and may reject or correct that procedure. Fewer turns and better results are outcomes to measure, not guarantees conferred by age or fragment count. The persona acts, the outcome is assessed, and new evidence can challenge the lesson.

![Experience may become selected memory; later action and independent assessment determine whether a learning claim is supported.](../assets/visuals/diagram-05-learning-loop.svg)

[Full text reading](../VISUAL-GUIDE.md#d05-the-learning-loop).

## Current obligations are not optional memories

Every relevant decision must receive the trusted operating constraints, current mandate and authority, applicable cancellations, accepted commitments, blocking findings, and critical new observations. The persona may select historical fragments, older alternatives, relationship interpretations, and additional tool detail within its allowance.

A summary must not turn an assumption into a fact, omit a blocker, widen a grant, or mark unread material as handled. Critical current information must not wait indefinitely behind ordinary conversation history or a persona's preferred subscriptions.

Different personas should receive their own relevant history alongside shared authoritative facts. Giving everyone one flattened transcript defeats the distinction between individual and collective context. Concealing a cancellation to preserve diversity is equally wrong.

## Context pressure and inference limits

The system must account for the full input, required instructions, selected records, media, and output allowance. Estimates must be distinguished from measured usage. It must not silently equate character or byte counts with a model's input units.

At a soft limit, a persona may compact or reselect history. At a hard limit, the system uses a bounded recovery path, an already authorized compatible inference capability, or an explicit block. It must not silently discard current permissions, obligations, or cancellations just to fit the request.

When the mandatory core cannot fit, the current decision is blocked pending restructuring or an authorized capability change. Historical material remains retrievable within access limits. Selected material is not recorded as included unless it actually reached the decision.

The inference capability's supported inputs must be known or explicitly unknown. A description of an image does not prove that the model received or inspected the image. Model refusal, partial output, and failure are visible states, not occasions to fabricate a completed action.

## Private memory and shared knowledge

Sharing is explicit. A community may maintain attributable documents, evidence, and shared fragments; it does not receive a merged private mind. Different personas may retain different interpretations of one event while the work record identifies the agreement actually adopted.

Access controls apply to retrieval, search snippets, relationships, summaries, profiles, exports, and newborn seed material. Derived content follows source restrictions unless an authorized transformation establishes another sharing policy. A public biography cannot disclose a private task to make a persona appear credible.

Correction, restriction, and retention rules apply to original content and derivatives, including indexes, previews, and backups. Historical accountability may preserve a minimal non-content record without keeping sensitive payloads forever. The system must state the limits of recall or deletion for material already exported beyond its control.

If a source is revoked or discredited, affected fragments and future selections need an explicit disposition. Historical provenance is not permission to keep using inaccessible material.

Search-led domain exploration can become learning when a persona connects
attributed sources to actual trials, observes results and limitations, and authors
an applicable lesson. A retrieved page, a model explanation, an installed program
and a retained lesson are distinct facts. Later tasks should be able to discover
relevant owned lessons across the authorized index, not only the most recent
records. Bounded previews do not select a lesson or prove that it was used.

### Bounded maintenance with a usable continuation

Context recovery must retain current obligations, unread inputs, selected material,
character context, failure facts, and uncertain actions independently of an ordinary
history-compaction cursor. A bounded recovery path may provide at most two normally
funded, same-model maintenance decisions in one pressure episode, using a smaller
maintenance-only operation contract. This supersedes the earlier one-decision
option: a necessary read must not consume the only opportunity to author a handoff.
Reads, failed selections, and failed or uncertain admitted inference spend an
attempt under the ordinary accounting rules. Local quotation and pre-admission
rejection do not.

The first decision should compact when possible; the second can observe an essential
read or repair an unsuccessful selection. Neither is a free retry or a guarantee
that the core can fit. After the bound is spent, another hard-overflow request
blocks with an actionable explanation. An ordinary admissible request may still
observe failures and continue. Its arrival, a restart, new input, or a changed
history cursor does not refresh the maintenance allowance while pressure persists.
Only a known ordinary request below the pressure threshold ends that episode.
Unknown exposure is not evidence that pressure ended. Previously stored spent state in the current contract counts as already used; malformed or unknown active state must fail conservatively. The first release need not maintain earlier experimental storage formats or implement compatibility migrations.

Context selection or compaction ends the saved batch so subsequent action follows
a fresh observation. The runtime does not summarize on the persona's behalf,
refund usage, widen authority, or switch the assigned model to force admission.
A mandatory core that still cannot fit is an explicit block. Provider authorization,
model, and transport failures retain their own meaning rather than being relabeled
as context overflow.

The current context exposes the existing history boundary and newest own journal
action separately from older receipts deliberately appended to the selection.
The persona chooses a newer boundary covered by its handoff; repeating or moving
backward is a visible no-progress failure, not successful compaction. Selection-only
changes do not require moving history. A history/record selection action in the same
response must preserve that response's explicit learned-memory choice, including
an empty choice. It must not accidentally erase the lessons just selected by the
persona's combined learning response. None of these mechanics resolve adverse facts,
uncertain effects or current obligations.

### Compact continuity without fabricated learning

When optional discovery previews are removed, retain a short,
source-independent reminder to preserve current commitments, attributable peer
findings, disagreements and source references. It must not prescribe a next trial,
method switch, tool or quality checklist. Compaction is not a verdict or a
resolution; the reminder is not a source receipt, a selected fragment, or a claim
that learning occurred.
Keep bounded exact learning evidence pointers already received under current
permissions, including adverse observations and relevant replies; compact their
explanatory prose before dropping learning opportunities. Do not introduce
unread private identifiers or omitted material merely to make a reminder useful.
Exact evidence must still satisfy received-source and current-access checks. Selected lessons and actual feedback remain subject to the ordinary
mandatory-context and source-access rules.

A privacy-denied peer delivery must not be repaired by deleting lineage,
paraphrasing restricted content, or treating compaction as a fresh permission.
Use explicit source-owner authorization or independently obtained, appropriately
shared evidence; otherwise preserve the concrete dependency and wait. Evaluate
these boundaries together with [method and learning continuity](../evaluation/METHOD-CONTINUITY.md),
without mistaking a passing preparation test for behavioral improvement.

## What would show useful learning?

| Observation | Supported conclusion | Not yet established |
|---|---|---|
| A fragment exists | Something was retained. | It is correct or useful. |
| A fragment was selected | The persona requested it. | It fit in the actual decision context. |
| A fragment was included | The decision received it. | It caused a later choice. |
| A related action followed | There is an inspectable use chain. | The result improved because of that memory. |
| A matched retained-versus-withheld comparison favors retention | Evidence supports benefit under those conditions. | Universal benefit on future work. |

Freeze relevant task information, initial state, tools, inference configuration, total resources, and assessment rules. Do not credit stronger tools, extra effort, a changed evaluator, or a leaked successful solution as learning. Include harmful-memory and correction cases, not only successful transfer.

See MEM-01–MEM-05, SYS-04, and UX-02 in the [requirements](../implementation/REQUIREMENTS.md), and the [learning-transfer example](../examples/WORKED-EXAMPLES.md#a-learning-transfer-comparison).

## Same-decision learning and handoff

An ordinary persona decision includes a compact authored continuity object:
next focus and explicit continue/wait intent; retain, revise, organize, no-change or defer disposition with a brief
reason; any fragment changes; and next-context references, retrieval cue and
handoff. This is a decision contract, not an additional reflection phase or an
extra inference call. Orientation and context maintenance share this learning
contract. Useful untested abstractions can be retained as tentative, with honest
uncertainty; task completion is not a prerequisite. No-change is valid when no
new idea is worth retaining through this persona's character. Fragment counts and character narration
are not progress measures. Each retained fragment is constructed by the persona's
LLM in its own voice with its admitted character, actual evidence, applicability,
limitations and counterevidence. Attribution alone does not verify voice or truth.

The runtime attempts these changes and next-context selection atomically before
the decision's effects. A new or revised fragment can select its own
resulting identity in that transaction. Replay uses one deterministic operation
identity. Invalid evidence, ownership or selection rolls back the whole change
and supplies an actionable receipt for repair. Independent actions may still run
against the original admitted context, subject to their ordinary scope, source,
dependency and pause checks; failed learning cannot grant authority or provide
evidence. A failed next-context update must not force identical paid retries or
prevent a voluntary wait. The current call keeps
its already admitted sources and authority; future selection cannot retroactively
change what it saw. A new focus or retrieval cue invalidates a stale compiled
request. Discard and scope changes clear the old handoff and cues together.

Visual inspection selections are usable evidence references: they identify the
exact image version, purpose and originating work, retaining the image's source
restrictions. Selecting an image is not itself a visual finding. The persona
must distinguish that selection from what it actually observed and learned.

Private memory can explicitly permit **procedural reuse** in later shared work
without granting access to its record or original work files. This permission
applies only to generalized procedures whose ancestry is shareable work, including
its shared discussions, or other
authorized procedural learning. Confidential facts, private correspondence,
restricted supplied material, withdrawal and erasure remain restrictive. Calling
content a procedure cannot declassify it. New work still checks applicability;
there is no automatic global publication or selection of a persona's memory.

## Memory navigation contract

[Persona-authored memory navigation](MEMORY-GRAPH.md) specifies the owned graph, same-call work and learning, authored connection conditions, exact selection and delegated recall, and the storage boundary. Graph neighborhoods have no required parent, root, or category; tool discovery remains separate.
