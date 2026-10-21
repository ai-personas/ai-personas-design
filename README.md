# AI Personas

AI Personas is a design for continuing AI collaborators with recognizable ways of noticing, deciding, communicating, and working with others. A persona uses a small selection of its own character and behavior prompts, together with relevant supporting material. The same language model does the work, chooses what it needs next, and considers useful revisions from actual experience. Development is possible; improvement is not guaranteed.

**Choose a reading path:** [Start with an everyday explanation](START-HERE.md), [explore the visual guide](VISUAL-GUIDE.md), or [go to the exact design rules](design/README.md). This repository specifies a design; [implementation status](implementation/STATUS.md) states what has actually been established.

<details>
<summary>Detailed introduction: character, assets, initialization, and current design status</summary>

**Distinct characters. Continuing experience. Useful maturation through work.**

AI Personas is a design for continuing AI collaborators with recognizable character: their own ways of noticing, choosing, communicating, relating to others, and changing through experience. Personas are general-purpose. Their traits shape how they approach different tasks; they do not assign a preset profession or establish competence. Competence must still be established for the proposed work.

Each persona has one accepted, versioned character account, expressed in natural language. It covers OCEAN traits—openness, conscientiousness, extraversion, agreeableness, and neuroticism—and a VAD profile of modeled valence (positive or negative tone), activation, and perceived control. These semantic descriptions are required; numerical scores are not.

**Fragments define character.** A fragment is a first-person prompt part that expresses the persona’s characteristic behavior, perspective, or voice. Fragments live in ordinary files that the persona can read, search, arrange, revise, and retire. Selected fragments become context for a large language model (LLM). That context, the reasoning it informs, actual interactions and actions, and the continuing evolution of authored prompts together constitute the persona. Facts or experience may inform a fragment, but its defining purpose is to shape the persona, not to store an episode for later recall.

**The normal beginning is an attributed trait seed.** A bounded initial LLM invocation expresses that seed as candidate fragments in the persona’s own voice. The candidates must form a coherent accepted starting account before continuing authorship proceeds. The primary LLM then works from that account and develops its prompts through actual experience. The initial LLM has an initialization role; it is not another continuing author. Seed provenance, generated starting detail, accepted character, and later experience remain distinguishable. Generated detail is not evidence of prior experience. Imported or operator-supplied beginnings retain their actual origin.

**Supporting assets have a different purpose.** Plain domain knowledge, generic technical procedures, organized history, tool-use records, tool definitions, reusable skills, scripts, code, and data are retained separately as supporting assets. This remains true whether the persona or someone else authored them. First-person wording or inclusion in a prompt does not turn an asset into character. Assets may guide authorized task execution, but they neither become persona-defining instructions nor grant authority.

While working, the primary LLM decides which fragments and supporting resources it needs next. It starts discovery with a small, bounded set of information. It can use literal text search, grep, supported regular expressions, and exact references. The model must never receive all tool names and descriptions, schemas, or the whole skill catalogue merely to filter them—even on the first choosing call. The host, meaning the system supporting the persona, keeps the bulk inventory outside both the provider-facing payload and the context visible to the model.

Finding a resource does not authorize its execution. [Following connections without loading everything](START-HERE.md#following-connections-without-loading-everything) explains direct-resource paths, context selection, and accounting across a whole episode. The [context contract](implementation/CONTRACTS.md#primary-persona-next-context-selection) and [working-context boundary](design/WORK-AND-BOUNDARIES.md#inference-and-bounded-working-context) govern those choices and limits.

This is the **current target design**, refined through 10 October 2026. Every application-visible persona LLM invocation combines work, characteristic-fragment maintenance, supporting-resource maintenance, and explicit choice of next fragment/resource context. Preserving an appropriate choice or stating no optional need is valid. Missing next-context intent is invalid; it is not an implicit choice. This design explicitly supersedes the 7 October optional-descriptor and omitted-maintenance norms while retaining the persona-owned files design.

**Design adoption is not runtime conformance.** This repository contains design documents, evaluation criteria, and scoped historical evidence. This revision changes no runtime. It does not establish useful maturation, human-like behavior, or product readiness. See [implementation status](implementation/STATUS.md) for the evidence boundary.

Maturation means that the same primary LLM considers work, fragment and asset maintenance, and bounded next-context choice in each interaction. It requires neither a forced edit nor a separate learner. The aim is a persona that becomes more useful through experience across work and interaction while expressing recognizable character. [Stage-matched evaluation](evaluation/README.md#whole-persona-development-checkpoints) and [three-persona checkpoints](examples/WORKED-EXAMPLES.md#whole-persona-checkpoints-without-forced-trait-drift) distinguish useful maturation from style alone, forced trait change, and regression.

</details>

## The central loop

Character informs what the persona does, and actual consequences can inform what it revises. The loop connects these responsibilities:

![Two separately purposed stores supply bounded context to the primary LLM. Actual decisions and consequences inform later authorized revision. Every call also has maintenance and next-context duties.](assets/persona-files-loop.svg)

**Figure: How a continuing persona works.** This is a conceptual explanation of the design. [Read the exact rules](design/PERSONA-CORE.md#maturation-within-every-primary-interaction); the explanation below retains their qualifications. [Open the illustration](assets/persona-files-loop.svg).

<details>
<summary>Text equivalent of the illustration</summary>

How a continuing persona works

AN ILLUSTRATED DESIGN STORY

What should shape my next decision?

Stored files

Exact context

One primary language model makes judgments

Characteristic fragments

How this persona approaches, behaves and speaks.

Supporting assets

Knowledge, tools, skills, data and attributed history.

Choose bounded next context

Use known exact references or bounded file search. Explicit preserve or no optional need can be enough.

Supply what the decision needs

Current character and mandatory work state join the selected exact text and complete qualifications.

Reason, interact and act

The persona’s perspective informs discretionary choices within facts, permissions and resources.

Observe and consider revision

Record actual consequences. The primary LLM proposes useful authorized changes, or states no change, a block or a deferral.

The next call uses the accepted selection and current state. The loop is a design responsibility, not proof of beneficial behavior.

Characters personify design choices; they do not assert feelings or consciousness. Scenes are hypothetical.

</details>

1. An attributed trait seed becomes initial LLM-authored candidate fragments and a coherent accepted starting account.
2. The primary LLM receives its current character, selected fragments, and selected supporting resources, alongside the actual need, observations, and protected constraints.
3. That perspective informs every discretionary choice: task methods, attention, communication with humans and peers, collaboration, context navigation, and maintenance.
4. Work and social interaction produce actual consequences. These may support, challenge, or leave the persona’s understanding unchanged.
5. The persona maintains fragments and supporting resources where useful, explicitly states what remains unchanged or unresolved, and chooses what should inform its next decision.

Meaningful experience may also change how the persona understands a particular relationship. Where the user’s self-authorship control permits it, experience may support an explicit revision of current character.

Self-harmonization means making prompt parts coherent and usable together. It preserves useful tensions and keeps unresolved contradictions visible. It does not require wholesale rewriting or make different personas alike. The [core maturation loop](design/PERSONA-CORE.md#maturation-within-every-primary-interaction) governs this reciprocal development.

The analogy to aging describes continuity shaped by experience. Elapsed time, invocation counts, and automatic model-weight training do not constitute that development, and wisdom is not guaranteed. Development may narrow a claim, correct a habit, simplify authored context, or reveal a regression.

**Every accepted response covers the whole responsibility.** These are connected duties, not a mandatory five-stage workflow or five model calls. Each persona invocation receives the maintenance obligation. Each accepted response must explicitly cover:

| Responsibility | What the response must cover |
|---|---|
| Work | The result or current disposition of the work |
| Fragment maintenance | A proposed change, a reasoned no-change decision, or an explicit unresolved disposition |
| Supporting-resource maintenance | The same maintenance decision for supporting assets |
| Next fragment context | An exact choice, appropriate preservation of an existing choice, or an explicit statement of no optional need |
| Next supporting-resource context | An explicit choice for supporting resources on the same basis |

A small task may need only one response, a concise joint reason for no change across both maintenance scopes, and an appropriate preserve or no-optional-need choice for both context scopes. No new fragment, search, separate reflection call, or compulsory mutation is required. A maintenance no-change decision does not replace the next-context decision. Known unresolved work must remain visible rather than being described as no change.

These duties also apply to initialization, retrieval choices, peer communication, and repair. A failed or malformed attempt is recorded as such; it must never be converted into a persona-authored no-change answer. The same primary LLM owns substantive work, character-conditioned fragments, supporting-resource maintenance, and next-context choice.

**Proposing a change is different from storing it.** Maintenance proposals identify authorized storage files or paths and useful search or regex cues where appropriate. A proposed save, an accepted edit, and a receipt confirming actual storage are distinct facts. Histories and receipts preserve real observations rather than invented events. External skills, code, and data retain their real authorship.

**The host enforces the boundaries.** It is responsible for access, evidence integrity, versioning, resource limits, and reliable effects. It must validate the response before releasing proposed substantive work; an invalid response cannot release that work. After an accepted effective-character change, a fresh decision is required before further operations from that response, including reads and waits. Host cancellation and accounting do not depend on a successful model reply. The [core](design/PERSONA-CORE.md) and [contracts](implementation/CONTRACTS.md) define these boundaries.

For example, a hypothetical persona might retain: “I tend to compare alternatives before committing. When the deadline is close, I first check whether another comparison could actually change the choice.” Another might prefer a quick concrete attempt and recognize when that preference needs restraint. These differences matter when they change behavior and improve work. Distinct biographies alone do not demonstrate that benefit.

## A compact network of useful fragments

A fragment can contain a cue that helps the persona find related material later. The primary LLM decides whether to follow the cue, which candidates to inspect, what to select, and when to stop. Connections can emerge through these searches. They do not require fixed folders, a separate graph engine, automatic host traversal, a hidden semantic writer or selector, or an outgoing link on every note.

The current persona-context navigation target uses searches chosen by the primary LLM: lexical searches that match text, supported regular expressions, simple authored cues and indexes, listing, and exact reads. Semantic/vector or graph-driven memory retrieval belongs to separate research comparisons. Adopting it would require an explicit design change. This restriction does not change the role of ordinary external task tools or compliant physical storage choices.

**A cue, a source reference, and a required warning do different jobs.**

| Relationship | Purpose | Limit |
|---|---|---|
| Associative search cue | Suggests where to look | A match supplies a candidate, not evidence or an accepted selection |
| Exact evidence reference | Identifies what a claim rests on | A search match cannot replace the exact evidence |
| Mandatory qualification or accepted warning | Constrains whether guidance can be supplied as usable | Optional navigation cannot omit the required qualification or warning |

The [file and context rules](design/PERSONA-CORE.md#ordinary-files-and-self-organization) preserve these distinctions.

**Compactness has several separate boundaries.** The design distinguishes the bounded corpus of authored persona context, the actual assembled prompt, and the full managed persona-state footprint. That full footprint includes archives, old versions, evidence, and supporting metadata; a small prompt alone does not establish a small retained system.

Supporting records must preserve provenance, access, expiry, qualifications, and accountability. Those responsibilities do not make the records characteristic fragments. Externally retained context must be counted, or the claimed bound must be disclosed as incomplete. The system cannot promise control over arbitrary copies held by recipients or providers.

User-owned delivered artifacts cannot be deleted, modified, or revoked to meet a notebook cap, or used as an uncounted archive. A retained lesson may outlive its raw evidence only when the actual retention and derivative-use policy permits that survival. The persona must remain honest about what can still be verified; a digest does not restore the source text.

The [retention rules](design/PERSONA-CORE.md#compact-retention-and-honest-forgetting) and [deployment choices](implementation/DEPLOYMENT-DECISIONS.md) govern these tradeoffs. Compression does not erase protected effects, source restrictions, or accepted warnings.

## Read the design

Choose a starting point based on the question you want to answer. The linked documents provide the detailed rules and evidence boundaries.

| If you want to understand… | Read… |
|---|---|
| The idea in everyday language | [Start here](START-HERE.md) |
| The user's consolidated product and design requirements | [User requirements](USER-REQUIREMENTS.md) |
| Character, fragments, maturation, and next-context choice | [Persona core](design/PERSONA-CORE.md) |
| Work, relationships, authority, resources, and honest outcomes | [Work and boundaries](design/WORK-AND-BOUNDARIES.md) |
| What the supporting system must guarantee | [System contracts](implementation/CONTRACTS.md), including [JSON text and matching surfaces](implementation/CONTRACTS.md#json-text-and-matching-surfaces) |
| How to test the claims | [Evaluation guide](evaluation/README.md) and [acceptance](evaluation/ACCEPTANCE.md) |
| Why this design replaced the earlier alternatives | [Design decisions](DESIGN-DECISIONS.md) and [source provenance](sources/SOURCE-MANIFEST.md) |

The [design index](design/README.md) defines document authority. [Requirements](implementation/REQUIREMENTS.md) preserve the protected invariants and requirement identifiers. [Worked examples](examples/WORKED-EXAMPLES.md), the [visual guide](VISUAL-GUIDE.md), [glossary](GLOSSARY.md), and optional [worksheets](templates/README.md) explain the same design.

## What remains essential

Character shapes choices, but it does not supply competence, evidence, or permission. OCEAN describes relatively stable dispositions. VAD describes modeled valence, activation, and perceived control. Context can change modeled affect and outward expression without rewriting stable traits. Neither framework measures actual feelings or supplies a formula for choosing tools, collaborators, or effort. Optional facets and contextual preferences may help explain those choices when useful.

People authorize purposes and effects. Personas choose and accept work within that authority. Distinct character does not create expertise, consent, money, or permission. Revising an interpretation does not turn it into an observed fact. Cooperation requires actual acceptance of responsibility, and a finished result requires appropriate evidence.

“Human-like” describes recognizable traits, choices, relationships, maturation, and continuity. It does not require a claim of consciousness or human equivalence. The design should be judged by useful behavior, faithful evidence, and the resources it consumes.

You do not need a previous conversation, implementation setup, or private attachment to read this repository. Earlier specifications, artwork, and result criteria remain accessible through [immutable historical references](sources/SOURCE-MANIFEST.md). They are historical material, not additional active manuals. The [change history](CHANGELOG.md) records this consolidation. Contributions follow the [contribution guide](CONTRIBUTING.md).
