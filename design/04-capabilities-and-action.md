# 4. Capabilities, real action, and recovery

[Design index](README.md) · [Previous: cooperation](03-work-and-cooperation.md) · [Next: authority](05-authority-and-resources.md)

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

A decorative room or virtual studio is not an access rule. Participants in the same displayed place may have different permissions. Access in one environment must not imply access in another. Tool sharing does not share private experience or every connected account.

## Shared defaults and domain exploration

An environment may start with a runtime-owned catalog of useful tools, such as
browser search and page reading or a knowledge question to the calling persona's
assigned model. Environment creation presents these defaults before saving. The
user may remove any or all of them, including when another creation flow makes
the environment implicitly. Creation configures bindings; it does not itself
research, install tools, or spend inference.

Bindings belong to the environment and are independently versioned. Accepted
participants in its work can use them under current authority and funding.
Changing one environment must not change another. Removing a default omits that
initial capability; it is not a permanent prohibition on a persona explicitly
acquiring it later with existing authority. A later catalog update must not
silently restore removed choices. Removing a binding does not uninstall host
software. Private acquired tools require explicit sharing and applicable evidence;
sharing tools never shares private memory or account credentials automatically.

Configuration is not observed availability. Report unchecked, available,
unavailable and removed states honestly. Check the current binding at admission
and before adopting late results. Relevant descriptor, backend or execution
changes invalidate affected evidence; a display-name edit or unrelated new tool
does not.

For unfamiliar domains and unclear requirements, available search tools are the
primary way to investigate what is needed. Personas choose their queries,
sources, disciplines, comparisons, experiments and collaborators. Supplementary
questions to their assigned model can expose ideas, assumptions and unknowns;
those answers remain model knowledge, not external research or practical
experience. No returned subsidiary-model action acquires execution authority.
The same model constraints, call/token/cost accounting, cancellation and evidence
boundaries apply. A missing or unavailable tool remains visible and can prompt
another authorized method; it must not become fabricated research.

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

## Safe execution is not a label

Acquired programs and imported artifacts must not gain ambient access to operator secrets, unrelated work, identity administration, private assessment material, or unrestricted destinations. Read-only claims must be enforced, not accepted because a tool describes itself that way.

When a required boundary cannot be enforced, the capability is unavailable under that safety claim. Any differently scoped use requires an explicit, informed grant and a truthful description of the actual boundary; there is no silent unrestricted fallback. Credentials remain outside ordinary persona memory and model context.

The design prescribes observable isolation properties, not a particular operating system, container, database, or programming language. Stopping a process is not equivalent to limiting what it could access before it stopped.

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

The system may report repeated waits, unchanged dependencies, repeated failures, elapsed resources, or missing owners. Personas or authorized reviewers decide the meaningful response: simplify, ask, change method, seek help, reallocate with authority, or stop.

Narrative updates, reminders, rewritten agendas, and new file bytes must not reset finite limits. A failed experiment or a necessary question can still be useful progress. Reporting a stopped state and preserving evidence must not require one more successful inference call after the allowance is exhausted.

The stopped-state report identifies the original need, delivered portions, open responsibilities, accepted owners or gaps, failures, uncertain effects, usage, and the decision needed to resume. “The agent stopped” is not a sufficient explanation of what the user received.

See ACT-01–ACT-04 and SYS-01–SYS-04 in the [requirements](../implementation/REQUIREMENTS.md), the [action contracts](../implementation/CONTRACTS.md#actions-and-observations), and the [external-action example](../examples/WORKED-EXAMPLES.md#an-external-action-with-an-uncertain-result).
