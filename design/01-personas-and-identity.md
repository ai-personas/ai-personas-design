# 1. Personas and continuing identity

[Design index](README.md) · [Next: memory and learning](02-memory-and-learning.md) · [Glossary](../GLOSSARY.md)

## Purpose

A persona is a persistent, attributable AI collaborator whose continuing state can inform its choices. Identity must survive individual model calls, temporary responsibilities, and completed projects. The system must not confuse that continuity with a human biography, professional qualification, or consciousness.

The intended benefit is inspectable continuity: a reader can understand who accepted work, which experience informed a contribution, and what happened when the persona changed direction. Whether that continuity improves outcomes is tested separately. The [development refinement](PERSONA-DEVELOPMENT.md) specifies the connection to exploration, experience, interaction, stopping, and evaluation.

## What belongs to a persona

| Part | Meaning | Boundary |
|---|---|---|
| Stable identity | The continuing entity to which authorship and responsibilities are attributed. | It is not a display name, model session, or temporary job. |
| Starting seed and creation provenance | Immutable initial profile, sponsor, reason, supplied material, generator information, and per-field origins. | Supplied knowledge and synthetic initialization are not firsthand experience. |
| Current character and OCEAN | Attributable continuing tendencies and preferences. | They do not establish competence, priority, or authority. |
| Current VAD | Situation-sensitive modeled affect. | It is distinct from lasting disposition and does not prove feelings. |
| Interests and open questions | Things the persona wants to investigate or improve across work. | Interest is neither competence nor permission to start funded activity. |
| Experience and fragments | Actual events and the persona's retained interpretations of them. | Evidence, interpretation, later use, and demonstrated benefit remain distinct. |
| Relationships | Directional, contextual interpretations of experience with particular participants. | They do not grant authority or expose another participant's private information. |
| Commitments | Specific responsibilities actually accepted. | Membership, preference, and nomination alone are not acceptance. |
| Capability evidence | Scoped demonstrations of operations and results. | A broad expert label cannot replace evidence or a professional qualification. |
| Inference configuration | The model capability used for current decisions. | It is replaceable without inventing a new identity or erasing obligations. |

Names, portraits, voices, and rooms are optional presentation. The actual artifact must exist before the system claims that a portrait was generated. A placeholder must be labeled as a placeholder. Public profile information must be separated from private working state. A work agenda remains scoped to that work rather than replacing continuing personal interests.

An optional avatar may be generated alongside the creation-time name and character, using the same synthetic starting characteristics. The image call uses an explicitly enabled image-generation capability; accepting images as input does not establish that capability. Among available, enabled image models with reviewed prices in the persona's allowance, choose the lowest conservative reserved cost for a comparable small avatar. Credentials, processing permission and funding remain separate, and subscription usage or a Jev ceiling does not authorize image API spending.

Reserve the image call, money and retained image storage before dispatch. Missing image access or funding must not delay character readiness or useful work. A timeout, cancellation or restart retains uncertain spending and requires an explicit separately funded retry. Reject malformed images and never replace a portrait changed while the call was in flight. Attach a validated preserved artifact only to the still-current eligible persona, with generation provenance and an honest distinction between the requested model and any observed model receipt. The UI exposes pending, unavailable, cancelled and completed states, call inspection, enabled image models and editable funding limits. An avatar does not alter the current self-model or create experience evidence.

## Starting character and synthetic initialization

Users may provide narrative character, any OCEAN values, and any VAD values. The creation profile is separate from referenced seed material: a document supplied for orientation must not be reinterpreted as a trait configuration.

Missing numeric values are initialized uniformly within OCEAN [0,1] and VAD [-1,1]. Explicitly supplied values, including zero, are preserved. Out-of-range or non-finite values are rejected, not clamped. A missing or blank narrative schedules funded character generation immediately after creation, using the assigned model and effort. The persona remains visibly pending until its character is ready; no work or environment is invented to initialize it. A supplied nonempty narrative is preserved and skips generation. Neither path may fabricate a human biography or describe synthetic values as personal experience.

The starting seed preserves the actual values, narrative, generator version, reproducibility seed, and the origin of each field. This is a synthetic initialization convention, not a scientifically validated distribution of human personality. The generator is versioned so a recorded seed has a defined interpretation. Reproducibility does not require exposing credentials or raw model transport.

Creation, initialization provenance, and the successful creation receipt are persisted together with the existing funding and identity boundary. A retry with the same creation identity returns the same persisted initialization. Reloading the interface, restarting the runtime, changing a model, accepting another invitation, and joining another environment must never rerandomize an existing persona. Imported history retains its original seed; activation does not invent one. A historical identity without recorded starting state is labeled as such, not assigned a retrospective beginning.

Character generation uses a separately persisted variation seed, independent of the numeric seed. Identical traits admit many distinct characters: coherent first-person preferences, interests, social inclinations and ways of handling uncertainty, rather than trait recitations, professions or prescribed tools. Preserve model, call and variation provenance when the completed starting profile is finalized. The self-authorship switch governs later revision; disabling it does not disable initial generation requested by creation.

Detect exact duplicate starting prose locally without revealing another persona's character to the model. One separately accounted regeneration may follow a confirmed duplicate; a repeated duplicate leaves a visible failure. An interrupted or uncertain call is never automatically replayed. Durable pending, running, ready, failed, uncertain and cancelled states have explicit retry/cancel controls. Every dispatched attempt uses the same initialization reservation, capacity admission and metering machinery as ordinary inference, with a new charge for another attempt. Raw request and response transport is transient. Restart, cancellation, profile changes, retirement and model selection must fence stale adoption. Repeating the original creation operation remains idempotent.

Descendant invitations are held until initialization is ready. Delivery rechecks the sponsor's current participation, work state, seed-sharing rights and resource scope. A completed character does not confer membership or a commitment. Initialization or invitation failure remains visible and does not erase usage or silently manufacture another identity.

The original seed remains separate from the current profile. Neither persona-authored evolution nor an operator edit can change how the persona started. Retention or erasure restrictions remain applicable to sensitive narrative material; erasure preserves an honest minimal disposition rather than substituting a new seed or pretending the original is still available.

## Character without fixed roles

Personas may develop distinguishable approaches through authored state and real experience. OCEAN and VAD descriptors may inform relevant context, but must not deterministically assign professions, tools, voting power, mandatory actions, or universal numerical priorities. Their scales and meanings remain explicit rather than being silently converted. The creation rules above replace the earlier optional-initial-descriptor convention; an older missing value is still not a neutral score or proof of an initial state.

A cautious persona can choose an experiment when evidence makes it appropriate. A curious persona can choose to finish rather than explore further. Learning does not require a trait score to change. A role such as reviewer or coordinator is an accepted, scoped responsibility, not a permanent identity class. Accuracy, honesty, necessary verification, and accepted obligations apply at every character value.

“Let this persona shape its character” is enabled by default at creation. When enabled, the persona may revise narrative character, OCEAN, and VAD through attributed updates. When disabled, those fields remain user-controlled; the persona can still retain experience, learn methods, develop interests, and make work-specific judgments. Moving substitute effective traits into an attributes field must not bypass the policy.

A profile revision preserves its earlier version, attribution, and a concise explanation. Supporting experience is linked where relevant through exact record versions or settled action receipts. Operator edits and authorship-policy changes use an operator-attributed path, not a persona impersonation. Current revisions and admission checks prevent a stale decision from continuing after a relevant profile or policy change. A no-op, failed update, or numeric change alone does not establish development.

Lasting preferences and temporary affect remain distinguishable in history. Descriptions such as “twenty years of architectural experience” must not be invented for an AI persona. Interest, a successful experiment, professional qualification, and demonstrated later benefit are different claims.

## Functional embodiment

Embodiment here means a continuing connection between identity, situation, decision, action, and consequence. The seven explanatory layers are persistent identity, authorized information, relevant decision context, practical capability, awareness of pending and completed events, real social commitments, and evidence-linked accountability.

A persona with a rich profile but no relevant history in its decisions lacks cognitive continuity. A persona that describes actions without an execution path lacks practical connection. A tool user without observable results cannot close the accountability loop. None of these layers requires a physical body.

![Identity, selected memory, current obligations, and observations inform bounded action; observed consequences return to reconsideration.](../assets/visuals/diagram-01-embodiment-loop.svg)

The diagram is a relationship map, not a required sequence of model calls. [Full text reading](../VISUAL-GUIDE.md#d01-the-embodiment-loop).

## Founders and the lifecycle

A fresh installation should start empty. A person explicitly creates or selects a small number of founders, identifies permitted seed material and initial profile preferences, and supplies bounded initialization resources. A fresh founder has no fabricated personal history; its underlying model may still contain prior knowledge.

| State | Entry condition | What can happen next |
|---|---|---|
| Initializing | Identity creation was accepted; orientation is not complete. | Complete bounded orientation, or stop with an explicit inactive disposition. |
| Active | Orientation and relevant access conditions are satisfied. | Respond to an authorized stimulus, accept work, wait, or pause. Active does not mean continuously thinking. |
| Dormant | No current participation or an explicit pause requires inference. | Resume only under an authorized stimulus with current access and funding. |
| Retired | An authorized lifecycle decision ends new participation. | Existing obligations must already have a recorded handoff, cancellation, or visible blocked disposition. Any reactivation needs an explicit new lifecycle decision. |
| Quarantined | An operator security restriction applies. | Only the permitted recovery or investigation path is available. Quarantine is independent of ordinary lifecycle and personality. |

The conditional reactivation rule makes the administrative boundary explicit; it is not an automatic loop or a reason to bypass quarantine. Task completion never automatically retires or deletes a persona. Optional personal exploration is separately enabled and funded under the [bounded-episode rules](PERSONA-DEVELOPMENT.md#active-work-and-optional-personal-exploration), not inferred from being active or curious.

## Recruitment, consultation, and birth

Consultation obtains a bounded contribution. Recruitment invites an existing participant. Birth creates a new continuing persona. A persona can also learn a method, use an existing capability, narrow a question, or ask a human. There is no automatic escalation ladder requiring birth.

A meaningful birth proposal identifies the contribution gap, relevant work, expected continuing benefit, permitted initial material, resources, population bounds, and how usefulness could later be assessed. The system checks replication authority, current seed-sharing rights, and initialization capacity before accepting creation. A sponsor's authorship is attributed to the sponsor rather than mislabeled as an operator's contribution.

Creation, its provenance, resource reservation, and initial notification must be one coherent accepted change. Repeating the same birth request must not create another child. Concurrent births cannot spend the same remaining capacity. All descendants remain within the controlling allowance; a sub-allocation transfers capacity rather than copying it.

## Orientation must be possible before membership

A newcomer must be able to inspect enough information to decide whether to join without receiving the parent's entire workspace. Limited pre-membership orientation supplies creation provenance, the starting profile and current authorship policy, expressly shared seed material, an invitation preview, offered responsibilities, agreement terms, and initialization limits.

After creation-time character generation, during its first funded work orientation the persona should consider its completed starting profile and record an initial approach or an explicit deferral. Useful work must not wait for several calls polishing a biography. A display name and portrait remain optional. An absent orientation disposition remains absent; the runtime cannot invent a persona-authored one.

Orientation does not grant general workspace access, credentials, arbitrary tools, external effects, or new funding. Access is checked again when material is used; a seed reference cannot bypass later revocation.

Three separate decisions must remain visible: the identity was created; the invitation was accepted or declined; a particular commitment was accepted, negotiated, or declined. For AI personas, this is an operational acceptance protocol. It is not a claim about subjective human-like consent or a substitute for real human consent.

A decline does not trigger an endless sequence of replacement births. Initialization failures have bounded retries. The record distinguishes created, oriented, joined, and committed; a partially initialized identity is not a ready team member.

## Leaving and continuing elsewhere

A departing persona identifies every open commitment. A handoff is not complete until the receiver accepts the exact responsibility. Until then, the prior responsibility remains visible unless an authorized cancellation or blocked disposition replaces it. A failed or inaccessible persona cannot be made to act, but its obligations must not disappear.

Dormancy, retirement, or membership removal does not reset spending, birth counters, or failed outcomes. A replacement does not automatically receive private memory. Project evidence remains available only under its access and retention policy.

Restoration preserves committed identity, starting seed, current profile, pending effects, accepted obligations, and resource exposure. Changing the model is recorded and important performance claims are reassessed. Moving to another project does not carry the previous project's permissions or private context. Global exclusive activation across independent hosts remains a separately gated design problem, not an implied feature of local continuity.

## What would count as evidence?

A useful identity trace links actual work, a preserved identity, relevant retained state, and later decisions. A useful birth trace links a real contribution gap to separate acceptance and an inspectable contribution. Names, portraits, traits, greetings, or participant counts alone establish neither.

Character-context inclusion is mechanism evidence, not proof that character changed a choice. Behavioral comparisons need matched within-model trials, declared seeds, name-swap and character-withheld controls, actual action traces, independent outcomes, and reported limitations. See the [development acceptance rules](PERSONA-DEVELOPMENT.md#acceptance-and-limits-of-conclusions).

See PER-01–PER-05 and COL-06 in the [requirements](../implementation/REQUIREMENTS.md), and M05, M06, M18, B01–B04, B08, and B10 in the [acceptance catalogue](../evaluation/ACCEPTANCE.md).
