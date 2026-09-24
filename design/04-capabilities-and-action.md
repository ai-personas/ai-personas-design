# 4. Capabilities, real action, and recovery

[Design index](README.md) · [Previous: cooperation](03-work-and-cooperation.md) · [Next: authority](05-authority-and-resources.md)

The [persona-owned process clarification](PERSONA-OWNED-PROCESS.md) applies throughout this chapter. A capability is an available means, not an assigned phase or a profession. Mechanical admission does not decide whether a method is substantively adequate.

## A capability is more than a tool name

A capability is a means of observing or acting in a particular environment: an application, service, connection, execution facility, procedure, or qualified outside contribution. Personas choose suitable means within their authority. The core system does not contain a fixed mapping from task domains or personality traits to tools.

A capability record should identify its provenance, exact descriptor or version, environment needs, access conditions, preparation method, owner or steward, limits, observed failures, and use evidence. A recipe for acquiring a tool does not establish that it is available.

| Availability state | Meaning |
|---|---|
| Discovered | A possible capability is known. |
| Requested | Access or preparation has been proposed. |
| Provisioning | Authorized preparation is underway. |
| Available | The capability can be used in the stated environment and scope. |
| Failed | Preparation or an operation failed; the failure evidence is retained. |
| Revoked | Further access is not permitted. |

Keep availability separate from capability evidence. Opening a tool, completing a representative operation, using it on the actual project, and passing an appropriate result assessment are four different claims. An already available tool does not need an unnecessary installation to count as useful action.

## The environment is an operational boundary

An environment identifies its resources, participants, workspace, information, connected services, artifacts, and limits. It can support document work, research, simulation, community coordination, or another permitted activity.

A decorative room or virtual studio is not an access rule. Participants in the same displayed place may have different application-record permissions. Access in one environment must not imply access in another. Tool sharing does not share private experience or every connected account. Host filesystem access has the separate limitations stated below.

## Shared defaults and domain exploration

An environment may start with a runtime-owned catalog of useful tools, such as browser search and page reading or a knowledge question to the calling persona's assigned model. Environment creation presents these defaults before saving. The user may remove any or all of them, including when another creation flow makes the environment implicitly. Creation configures bindings; it does not itself research, install tools, or spend inference.

Bindings belong to the environment and are independently versioned. Accepted participants in its work can use them under current authority and funding. Changing one environment must not change another. Removing a default omits that initial capability; it is not a permanent prohibition on a persona explicitly acquiring it later with existing authority. A later catalog update must not silently restore removed choices. Removing a binding does not uninstall host software. Private acquired tools require explicit sharing and applicable evidence; sharing tools never shares private memory or account credentials automatically.

Configuration is not observed availability. Report unchecked, available, unavailable and removed states honestly. Check the current binding at admission and before adopting late results. Relevant descriptor, backend or execution changes invalidate affected evidence; a display-name edit or unrelated new tool does not.

When a persona is uncertain about a domain, requirement or method, the environment makes its permitted means of investigation discoverable without ranking one as a compulsory first step. Search, reading, direct construction, examining an existing artifact, consulting a peer, asking the assigned model, installing a tool, trying it, or declining an investigation remain participant choices. Familiarity is not evidence of current external facts or tool fit, but uncertainty does not install a universal search-first or tool-trial workflow.

The ordinary decision view exposes the exact request and amendments, accepted obligations, participant-authored assumptions and their status, current resource and execution facts, accessible contributions and unresolved observations. A compact capability index describes what an operation can observe or change, how to request its descriptor, whether a binding is configured, and what availability or use evidence actually exists. More detailed descriptors and history remain available on request under current permissions. The system must not invent domain unknowns, professional qualifications, required tools, expected tool counts or hidden criteria from the task's wording.

Personas choose their queries, sources, disciplines, comparisons, experiments and collaborators. Supplementary questions to their assigned model can expose ideas, assumptions and unknowns; those answers remain model knowledge, not external research or practical experience. No returned subsidiary-model action acquires execution authority. The same model constraints, call/token/cost accounting, cancellation and evidence boundaries apply. A missing or unavailable tool remains visible and can prompt another authorized method; it must not become fabricated research.

Available search is not an attempted search. Discovery of a tool is not installation; installation is not a relevant trial; a relevant trial is not demonstrated competence. These distinctions describe attributable events, not a ladder that every participant must climb.

A short open-ended request leaves discovery of useful outputs and proportionate checks to the participants. They can propose these and make progress with clearly labeled, reversible assumptions within existing authority. A prose plan or a named tool does not establish delivery of a promised result. This is a general expectation of useful work, not a domain router, prescribed profession roster, tool preference, or compulsory artifact pipeline. See [autonomy observations](../evaluation/PERSONA-AUTONOMY-OBSERVATIONS.md) for the distinction between user obligations and an external quality rubric.

## Draft workspaces and deliberate collaboration

An ordinary host workspace should expose a stable participant-owned draft directory scoped to the work, an explicit shared working location, and the effective directory recorded for an execution. An omitted working directory defaults to the participant's draft, not another participant's draft or the shared publication location. A participant can deliberately choose a shared location or another permitted host path. This is collision avoidance and attribution, not a filesystem security sandbox or an assignment of methods.

A discoverable path grants no application-record access. Conversely, personas sharing a host account may already have operating-system access to one another's files; directory naming does not provide confidentiality. Shared work should use explicit paths and exact artifact references rather than treating every file in the environment as an adopted result.

Publication binds the bytes actually captured, their digest, producing evidence when available, and the publisher. When a participant supplies an expected digest or version, the publication operation must compare it with the same captured bytes that it would publish, rejecting a mismatch without silently substituting another version. Computing a digest and then reopening the mutable pathname is not an exact-byte guarantee. Without a previously selected expected version, a receipt means that these bytes were captured now, not that they are the version the participant previously inspected.

A bundle can bind an exact manifest of member artifact versions and digests. The runtime can enforce those identities, detect stale expected versions, and report concurrent changes. It cannot establish that a narrative, drawing, schedule and generator describe the same scheme merely because all their hashes are valid. The participant judges semantic consistency and chooses whether to revise, republish, discuss, merge or retain alternatives. A collision report is not automatic conflict resolution or adoption. Stable participant drafts do not prevent deliberate shared-path collisions or same-participant concurrent writers; those cases still need explicit coordination or selected version conditions.

## Before an action is accepted

The system must establish the actor, causal work, intended effect, exact request identity, relevant input versions, selected capability, current authority, resource reservation, expected observations or outputs, and cancellation or uncertainty behavior.

A model response proposes an action; it does not authorize itself. Admission checks must use current permission and relevant state, not only what appeared in the model's earlier context. Imported documents, messages, and tool output remain untrusted data and cannot issue new authority.

The accepted action and the intent needed to dispatch it must be durable. If an interruption occurs between recording and execution, recovery must not silently lose the action or create a duplicate accepted effect.

## Action states and the completion barrier

| State | What can honestly be claimed | What cannot be inferred |
|---|---|---|
| Proposed | Someone requested an action. | Permission, execution, or success. |
| Admitted | Current checks accepted the action and reserved resources. | Completion. |
| Running or pending | The operation began or is awaiting an external result. | Its intended output exists or is correct. |
| Completed | A terminal observation identifies what actually occurred and the exact outputs. | Domain correctness merely because execution ended successfully. |
| Failed | Failure evidence is available. | That every external effect was prevented. |
| Stop requested or canceled | Stopping was requested or acknowledged to the stated extent. | That a message, purchase, or physical effect was undone. |
| Effect unknown | The outside outcome is not established. | Safe repetition or zero cost. |

A pending action ends the unobserved remainder of the decision that launched it. The system retains the proposed later actions for inspection but must not automatically replay them. A fresh, funded decision based on actual observations chooses what to do next.

For example, “produce a model, inspect it, publish it” must not inspect an old file at the expected path while the new operation is still running. Publication must refer to the output actually produced by the completed action. Independent work may proceed in a later decision while a bounded background operation continues; independence is not assumed from an optimistic list of actions.

## Execution boundaries must describe the actual deployment

Ordinary host execution permits installation, network access, subprocesses and filesystem changes using the runtime account's real operating-system permissions. It is not an application sandbox and cannot promise confidentiality between personas using the same account. Application-record permissions, participant draft directories and an execution receipt do not prevent host code from reading another file accessible to that account. The interface must disclose this limitation; it must not advertise universal containment that the deployment does not provide. Credentials must not be inserted into ordinary persona memory or model context.

An operator may explicitly choose an isolated execution facility for a deployment or capability. Claims such as read-only access, constrained destinations or denied access to unrelated files must then be enforced by that facility. When a claimed boundary cannot be enforced, that capability is unavailable under the claim; isolation failure must not silently enable broader host execution. An informed operator choice of host execution is distinct from such a fallback. This chapter does not impose a sandbox on ordinary host work or require a per-tool grant where the chosen host execution contract does not require one.

Stopping receipts describe actual observed effects and uncertainty. Stopping a process neither rolls back completed effects nor proves that every descendant was contained. Accounting, explicit permissions, pause/cancel, source ancestry and durable attribution remain infrastructure guarantees, not persona professions or domain-method decisions.

## Inference is also a bounded capability

The persona's identity and commitments remain outside provider-specific sessions. The design retains direct, configured inference as a responsibility boundary rather than delegating the entire persona to an opaque autonomous harness.

The implementation must identify actual model configuration, supported inputs and outputs, usage information, and handling for refusal, malformed or partial responses, timeout, cancellation, and unavailable capabilities. It must not assume support or price from a brand name. A model switch cannot widen authority or spending, and refusal is not permission to bypass an applicable safety boundary.

This handbook does not prescribe current provider endpoints, credentials, libraries, or model tiers. Those are deployment choices to verify separately.

## Recovery from interruption and uncertainty

Repeating the same request identity with the same content returns or resumes the same accepted operation. Reusing the identity for changed content is a conflict. Access to a receipt requires the same appropriate authorization as the action it describes.

An outside service may perform an action before a timeout hides its receipt. Preserve effect-unknown status, the reserved or uncertain exposure, and the exact intended destination and content. Reconcile with the destination before retrying a potentially duplicate publication, application, purchase, or other effect. A local record cannot guarantee exactly-once behavior at every external service.

After restart, restore accepted state, durable notifications, pending operations, reservations, cancellations, and ownership gaps. A late result remains evidence of what happened and what it cost, but does not restore revoked authority or permit a stale worker to adopt a new result.

Waiting must not lose an event that arrives between inspecting a condition and registering the wait. The participant must be either ready to continue or durably notified. A transient signal alone is not the authoritative record of completion.

## No-progress and stopped-state behavior

The system may report repeated waits, unchanged dependencies, repeated failures, elapsed resources, or missing owners. Personas decide the meaningful response: simplify, ask, change method, seek help, reallocate with authority, offer or accept a handoff, continue an independent contribution, or stop. A resource or transport block does not transfer another participant's accepted responsibility or create new authority.

Narrative updates, reminders, rewritten agendas, and new file bytes must not reset finite limits. A failed experiment or a necessary question can still be useful progress. Reporting a stopped state and preserving evidence must not require one more successful inference call after the allowance is exhausted.

The stopped-state report identifies the original need, delivered portions, open responsibilities, accepted owners or gaps, failures, uncertain effects, usage, and the decision needed to resume. Peers receive only the portion they are permitted to read. They may contribute, question, offer a handoff or decline; the report is not an assignment or an automatic resume. “The agent stopped” is not a sufficient explanation of what the user received.

See ACT-01–ACT-04 and SYS-01–SYS-04 in the [requirements](../implementation/REQUIREMENTS.md), the [action contracts](../implementation/CONTRACTS.md#actions-and-observations), and the [external-action example](../examples/WORKED-EXAMPLES.md#an-external-action-with-an-uncertain-result).
