# Design reference

[Home](../README.md) · [Start here](../START-HERE.md) · [Decisions](../DESIGN-DECISIONS.md)

This branch has one target design: continuing personas expressed in persona-owned first-person fragments, organized in ordinary files, with the primary LLM choosing relevant next context as part of doing work. The older graph-first, auxiliary-selector, and file-proposal manuals are retired from the active reading surface.

## Three complementary views

| Document | Its responsibility |
|---|---|
| [Persona core](PERSONA-CORE.md) | Identity, character, fragments, self-organization, learning, and persona-owned next-context choice |
| [Work and boundaries](WORK-AND-BOUNDARIES.md) | Accepted work, cooperation, real actions, authority, resources, evidence, recovery, and conditional extensions |
| [System contracts](../implementation/CONTRACTS.md) | The observable guarantees that make those choices and boundaries reliable |

These documents specify intended behavior. A document's presence, a diagram, or an acceptance scenario is not implementation evidence. See [status](../implementation/STATUS.md).

## Authority within the repository

1. The protected [I01–I21 invariants](../implementation/REQUIREMENTS.md) govern applicable actions and transitions
2. The persona core, work and boundaries, and system contracts are complementary normative views of that foundation. They define meaning, constraints, and handoffs together
3. The remaining requirement catalogue traces those obligations; the [acceptance catalogue](../evaluation/ACCEPTANCE.md) states what must be examined to support them. Neither is an abbreviated override of the detailed rule
4. Guides, examples, glossary, worksheets, artwork, research summaries, decisions, and historical reports explain the design or its evidence. They do not independently grant permission, prescribe an additional workflow, or establish conformance

There is no last-file-wins rule. A contradiction between normative documents is a defect to resolve through one recorded decision and coherent updates. Until resolved, preserve the conservative authority, privacy, resource, and evidence boundaries. Historical documents and past passes cannot weaken current restrictions or claim compliance with revised criteria.

Inside a runtime, authoritative instructions and current accepted obligations remain outside the persona's optional fragment selection. A persona-authored statement, retrieved file, or search result cannot become a new authority source merely because it is included in context.

## Reading obligations

**Must** states a condition required for the applicable feature. **Should** is a strong recommendation whose exception needs a reason. **May** describes an option. Optional features remain subject to their safeguards when enabled.

Prose fragments do not require every persona to adopt a fixed set of folders, fields, mental functions, or personality scores. Precise host records for permissions, evidence, ownership, current work, and resource accounting are still necessary where their meanings apply. Simpler cognitive representation does not mean ambiguous operational boundaries.

## Scope and extensions

A basic continuing persona does not require multiple-persona society, births, continuous background exploration, an ongoing service, or a physical body. The conditional boundaries for those features remain in [work and boundaries](WORK-AND-BOUNDARIES.md) and [deployment decisions](../implementation/DEPLOYMENT-DECISIONS.md).

The historical E1–E6 labels remain attributable in the [decision register](../DESIGN-DECISIONS.md) and [historical evaluation map](../evaluation/HISTORICAL-RESULTS.md). They do not establish that any optional feature is deployed or approved for a specific use.

The [source manifest](../sources/SOURCE-MANIFEST.md) locates retired documents at immutable revisions. [Contributing](../CONTRIBUTING.md) explains how to change the current design without recreating competing manuals.
