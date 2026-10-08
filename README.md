# AI Personas

**Distinct characters. Continuing experience. Better work through learning.**

AI Personas is a design for continuing AI collaborators with recognizable character: their own ways of noticing, choosing, communicating, relating to others, and changing through experience. Each persona has one accepted, versioned character account with stable OCEAN traits and a VAD modeled affect profile, expressed in natural language. Its first-person fragments are persona-defining, characteristic-bearing prompt parts, kept in ordinary files that it can read, search, arrange, revise, and retire. Their selected assembly forms context for LLM reasoning. That context, the reasoning it informs, actual interaction and actions, and the continuing evolution of authored prompts together constitute the persona. A fragment may include facts or experience, but its defining purpose is to shape the persona, not to store an episode for later recall.

The normal beginning is a trait seed, expressed by a bounded initial LLM invocation as candidate own-voice characteristic fragments, then coherently accepted as the starting account. The continuing primary LLM works from that accepted beginning and develops its prompts through actual experience. The initial LLM is an initialization role, not another continuing author. Seed provenance, generated detail, accepted character, and later experience remain distinguishable; imported or operator-supplied beginnings retain their actual origin.

While doing a task, the persona's primary LLM decides which fragments and supporting resources it needs next. Organized history, tool-use records, tool definitions, reusable skills, scripts, code, and data are separately retained resources, not automatically persona fragments or prompt contents. A small discovery bootstrap supports bounded literal search, grep, supported regular expressions, and exact references. The model never receives all tool names/descriptions, schemas, or the whole skill catalogue just to filter them. The bulk inventory stays in the host store, outside both the provider-facing payload and model-visible context; those two exposure surfaces are accounted for separately.

Known exact resources can be requested directly, and already supplied, still-current operative guidance can support authorized use without rediscovery. Finding, reading, selecting, actually supplying, invoking, and observing a result have different meanings, not mandatory separate calls. A stored script is not an installed capability, and discovery grants no execution authority. The persona-context corpus and every assembled prompt stay bounded; accounting includes all discovery, loading, maintenance, retries, and whole-episode work, rather than just the final action prompt. The [context contract](implementation/CONTRACTS.md#primary-persona-next-context-selection) and [working-context boundary](design/WORK-AND-BOUNDARIES.md#inference-and-bounded-working-context) govern this path.

This is the **current target design on this branch**, refined on 8 October 2026. Semantic OCEAN and VAD coverage is required; numerical scores are not. Every application-visible persona LLM invocation combines its work, characteristic-fragment maintenance, supporting-resource maintenance, and choice of next fragment/resource context. This explicitly supersedes the 7 October optional-descriptor and omitted-maintenance norms while retaining the persona-owned files design.

**Design adoption is not runtime conformance.** This repository contains design documents, evaluation criteria, and scoped historical evidence. This revision changes no runtime, and does not establish useful learning, human-like behavior, or product readiness. See [implementation status](implementation/STATUS.md) for the evidence boundary.

## The central loop

1. An attributed trait seed becomes initial LLM-authored candidate fragments and a coherently accepted starting account
2. The primary LLM receives its current character, selected fragments, and selected supporting resources alongside the actual need, observations, and protected constraints
3. That perspective informs all discretionary choices: task methods, attention, communication with humans and peers, collaboration, context navigation, and maintenance
4. Actual work and social interaction return consequences that may support, challenge, or leave its understanding unchanged
5. The persona maintains its fragments and supporting resources where useful, explicitly disposes unchanged or unresolved work, and chooses what should inform its next decision

Meaningful experience can also change a scoped relationship interpretation and, where the user's self-authorship control permits it, support an explicit current-character revision. Self-harmonization makes usable prompt parts jointly intelligible while preserving useful tensions and unresolved contradictions; it does not require wholesale rewriting or make different personas alike. The [core learning loop](design/PERSONA-CORE.md#one-learning-and-action-loop) governs this reciprocal development. The analogy to aging is experience-shaped continuity, not elapsed time, invocation counts, automatic model-weight training, or guaranteed wisdom. Development can narrow a claim, correct a habit, simplify authored context, or reveal a regression.

These are connected responsibilities, not a mandatory five-stage workflow or five model calls. A small task may need one response, a concise reason for no change, and no new fragment. Every persona invocation receives the maintenance obligation; every accepted response includes its own explicit disposition. Initialization, retrieval choices, peer communication, and repair are covered too. A failed or malformed attempt is recorded as such, never converted into a persona-authored no-change answer. The same primary LLM owns substantive work, character-conditioned fragments, supporting-resource maintenance, and next-context choice. A concise joint disposition can clearly cover both maintenance scopes; no separate reflection call or compulsory mutation is required. Proposals identify authorized storage files or paths and useful search/regex cues where appropriate. A proposed save is distinct from an accepted edit and its actual storage receipt. Histories and receipts preserve real observations rather than invented events; external skills, code, and data retain their real authorship.

The host enforces access, evidence integrity, versioning, resource limits, and reliable effects. An invalid response cannot release its proposed work, and an accepted effective-character change requires a fresh decision before further operations from that response. Host cancellation and accounting do not depend on a successful model reply. The [core](design/PERSONA-CORE.md) and [contracts](implementation/CONTRACTS.md) define these boundaries.

For example, a hypothetical persona might retain: “I tend to compare alternatives before committing. When the deadline is close, I first check whether another comparison could actually change the choice.” Another might prefer a quick concrete attempt and learn when that preference needs restraint. The difference matters when it changes what they do and improves their work, not merely when their biographies sound different.

## A compact network of useful fragments

A fragment can suggest what to search for when a related situation arises. The primary LLM decides whether to follow that cue, which candidates to inspect, what to select, and when to stop. Connections can emerge through those searches without fixed folders, a separate graph engine, automatic host traversal, a hidden semantic writer or selector, or a compulsory outgoing link on every note.

The current persona-context navigation target uses primary-chosen lexical/regex searches, simple authored cues and indexes, listing, and exact reads. Semantic/vector or graph-driven memory retrieval belongs to separate research comparisons; adopting it would require an explicit design change. Ordinary external task tools and compliant physical storage choices are unaffected.

Three relationships have different jobs: an associative search cue suggests where to look; an exact evidence reference identifies what a claim rests on; a mandatory qualification or accepted warning constrains whether guidance can be supplied as usable. Search matches cannot replace exact evidence, and optional navigation cannot omit required warnings. The [file and context rules](design/PERSONA-CORE.md#ordinary-files-and-self-organization) preserve that distinction.

Compactness distinguishes the bounded authored persona-context corpus, the actual assembled prompt, and the full managed persona-state footprint, including archives, old versions, evidence, and supporting metadata. Supporting records preserve provenance, access, expiry, qualifications, and accountability; they are not the definition of fragments. External retained context must be counted or the claimed bound disclosed as incomplete; arbitrary recipient or provider copies cannot be promised controlled. User-owned delivered artifacts cannot be deleted to meet a notebook cap. Retained lessons can outlive raw evidence only under the actual retention and derivative-use policy, with honest limits on what is still verifiable. The [retention rules](design/PERSONA-CORE.md#compact-retention-and-honest-forgetting) and [deployment choices](implementation/DEPLOYMENT-DECISIONS.md) govern these tradeoffs; protected effects, source restrictions, and accepted warnings do not disappear through compression.

## Read the design

| If you want to understand… | Read… |
|---|---|
| The idea in everyday language | [Start here](START-HERE.md) |
| Character, fragments, learning, and next-context choice | [Persona core](design/PERSONA-CORE.md) |
| Work, relationships, authority, resources, and honest outcomes | [Work and boundaries](design/WORK-AND-BOUNDARIES.md) |
| What the supporting system must guarantee | [System contracts](implementation/CONTRACTS.md) |
| How to test the claims | [Evaluation guide](evaluation/README.md) and [acceptance](evaluation/ACCEPTANCE.md) |
| Why this design replaced the earlier alternatives | [Design decisions](DESIGN-DECISIONS.md) and [source provenance](sources/SOURCE-MANIFEST.md) |

The [design index](design/README.md) defines document authority. [Requirements](implementation/REQUIREMENTS.md) preserve the protected invariants and requirement identifiers. [Worked examples](examples/WORKED-EXAMPLES.md), the [visual guide](VISUAL-GUIDE.md), [glossary](GLOSSARY.md), and optional [worksheets](templates/README.md) explain the same design.

## What remains essential

OCEAN describes relatively stable dispositions; VAD describes modeled valence, activation, and perceived control. Context can alter modeled affect and outward expression without rewriting stable traits. Neither framework measures actual feelings or supplies a formula for choosing tools, collaborators, or effort. Optional facets and contextual preferences may explain those choices when useful.

People authorize purposes and effects. Personas choose and accept work within that authority. Distinct character does not create expertise, consent, money, or permission. Learning does not turn an interpretation into an observed fact. Cooperation needs actual acceptance, and a finished result needs appropriate evidence.

“Human-like” describes recognizable traits, choices, relationships, learning, and continuity. It does not require a claim of consciousness or human equivalence. The design should be judged by useful behavior, faithful evidence, and the resources it consumes.

No previous conversation, implementation setup, or private attachment is needed to read this repository. Earlier specifications, artwork, and result criteria remain accessible through [immutable historical references](sources/SOURCE-MANIFEST.md); they are not additional active manuals. The [change history](CHANGELOG.md) records this consolidation. Contributions follow the [contribution guide](CONTRIBUTING.md).
