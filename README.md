# AI Personas

**Distinct characters. Continuing experience. Better work through learning.**

AI Personas is a design for continuing AI collaborators with recognizable character: their own ways of noticing, choosing, communicating, relating to others, and changing through experience. Each persona has one accepted, versioned character account with stable OCEAN traits and a VAD modeled affect profile, expressed in natural language. It carries that perspective into every first-person fragment it authors. Those fragments are reusable parts of its prompts, kept in ordinary files that it can read, search, arrange, revise, and retire.

While doing a task, the persona's primary LLM decides what it needs to remember next. It can look through its files with ordinary search, grep, or regular expressions, choose relevant fragments for a later decision, and update its understanding from what happens. Experience from the environment, tasks, other personas, and its own successes or mistakes can therefore influence future work.

This is the **current target design on this branch**, refined on 8 October 2026. Semantic OCEAN and VAD coverage is required; numerical scores are not. The primary persona considers fragment maintenance in every application-visible persona LLM invocation, alongside its other work. This explicitly supersedes the 7 October optional-descriptor and omitted-maintenance norms while retaining the persona-owned files design.

**Design adoption is not runtime conformance.** This repository contains design documents, evaluation criteria, and scoped historical evidence. This revision changes no runtime, and does not establish useful learning, human-like behavior, or product readiness. See [implementation status](implementation/STATUS.md) for the evidence boundary.

## The central loop

1. A persona observes a request, result, conversation, or other authorized event
2. It works under its accepted character and considers what the received experience means for its fragments
3. Alongside its work, it proposes a fragment patch, explains no change, or records an explicit block or bounded deferral; it can also find and choose the context it expects to need next
4. The host supplies that chosen context alongside current obligations, relevant qualifications, and permission limits
5. The persona makes another decision and learns from the consequences

These are connected responsibilities, not a mandatory five-stage workflow or five model calls. A small task may need one response, a concise reason for no change, and no new memory. Every persona invocation receives the maintenance obligation; every accepted response includes its own explicit disposition. Initialization, retrieval choices, peer communication, and repair are covered too. A failed or malformed attempt is recorded as such, never converted into a persona-authored no-change answer. The same primary LLM owns substantive work, character-conditioned fragment authorship, and next-context choice. No separate reflection call or compulsory mutation is required.

The host enforces access, evidence integrity, versioning, resource limits, and reliable effects. An invalid response cannot release its proposed work, and an accepted effective-character change requires a fresh decision before further operations from that response. Host cancellation and accounting do not depend on a successful model reply. The [core](design/PERSONA-CORE.md) and [contracts](implementation/CONTRACTS.md) define these boundaries.

For example, a hypothetical persona might retain: “I tend to compare alternatives before committing. When the deadline is close, I first check whether another comparison could actually change the choice.” Another might prefer a quick concrete attempt and learn when that preference needs restraint. The difference matters when it changes what they do and improves their work, not merely when their biographies sound different.

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
