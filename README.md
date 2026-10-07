# AI Personas

**Distinct characters. Continuing experience. Better work through learning.**

AI Personas is a design for continuing AI collaborators with recognizable character: their own ways of noticing, choosing, communicating, relating to others, and changing through experience. Each persona expresses that developing perspective in first-person fragments it owns. Those fragments are reusable parts of its prompts, kept in ordinary files that it can read, search, arrange, revise, and retire.

While doing a task, the persona's primary LLM decides what it needs to remember next. It can look through its files with ordinary search, grep, or regular expressions, choose relevant fragments for a later decision, and update its understanding from what happens. Experience from the environment, tasks, other personas, and its own successes or mistakes can therefore influence future work.

This is the **current target design on this branch**. The earlier graph-first and auxiliary-selector designs have been consolidated into it. It is no longer an optional file-interface proposal beside those designs.

**Design adoption is not runtime conformance.** This repository contains design documents, evaluation criteria, and scoped historical evidence. This revision changes no runtime, and does not establish useful learning, human-like behavior, or product readiness. See [implementation status](implementation/STATUS.md) for the evidence boundary.

## The central loop

1. A persona observes a request, result, conversation, or other authorized event
2. It works on the task and interprets what that experience means to it
3. It may write or reorganize first-person fragments, then find and choose the context it expects to need next
4. The host supplies that chosen context alongside current obligations, relevant qualifications, and permission limits
5. The persona makes another decision and learns from the consequences

These are connected responsibilities, not a mandatory five-stage workflow or five model calls. A small task may need one response and no new memory. The same primary LLM owns substantive work, fragment authorship, and next-context choice. The host enforces access, evidence integrity, resource limits, and reliable effects; it does not secretly choose the persona's character or method.

For example, one persona might retain: “I tend to compare alternatives before committing. When the deadline is close, I first check whether another comparison could actually change the choice.” Another might prefer a quick concrete attempt and learn when that preference needs restraint. The difference matters when it changes what they do and improves their work, not merely when their biographies sound different.

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

People authorize purposes and effects. Personas choose and accept work within that authority. Distinct character does not create expertise, consent, money, or permission. Learning does not turn an interpretation into an observed fact. Cooperation needs actual acceptance, and a finished result needs appropriate evidence.

“Human-like” describes recognizable traits, choices, relationships, learning, and continuity. It does not require a claim of consciousness or human equivalence. The design should be judged by useful behavior, faithful evidence, and the resources it consumes.

No previous conversation, implementation setup, or private attachment is needed to read this repository. Earlier specifications, artwork, and result criteria remain accessible through [immutable historical references](sources/SOURCE-MANIFEST.md); they are not additional active manuals. The [change history](CHANGELOG.md) records this consolidation. Contributions follow the [contribution guide](CONTRIBUTING.md).
