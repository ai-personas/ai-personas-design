# Design reference

[Home](../README.md) · [Start here](../START-HERE.md) · [Decisions](../DESIGN-DECISIONS.md)

This branch has one target design: continuing personas with one accepted, versioned character account covering semantic OCEAN traits and a VAD modeled affect profile. Every authored fragment is character-conditioned and own-voice, kept in ordinary files. The primary LLM chooses relevant next context and returns an explicit fragment-maintenance disposition in every accepted persona invocation, alongside its other work. The older graph-first, auxiliary-selector, and file-proposal manuals are retired from the active reading surface.

## Three complementary views

| Document | Its responsibility |
|---|---|
| [Persona core](PERSONA-CORE.md) | Identity, semantic traits and modeled affect, character-conditioned fragments, every-invocation maintenance, learning, and persona-owned next-context choice |
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

Required semantic coverage is not a required numeric scorecard. All five OCEAN domains and all three VAD dimensions have meaning in the accepted character account; additional facets or operational tendencies are optional when useful. Stable traits, transient affect, expression, capability, and authority remain distinguishable. Files and fragments have no compulsory folder taxonomy or mental-function tree.

Every application-visible persona LLM invocation receives maintenance input, and every accepted output supplies a patch, no change with a reason, blocked, or bounded deferred disposition. This does not require a mutation, a new selection, or a separate reflection call. Failed attempts retain honest host status rather than fabricated persona judgments. The core and contracts define the exact scope and failure behavior.

Precise host records for permissions, evidence, ownership, current work, and resource accounting are still necessary where their meanings apply. Simpler cognitive representation does not mean ambiguous operational boundaries.

The 8 October refinement explicitly supersedes the 7 October interpretation that OCEAN/VAD descriptors and an explicit maintenance response could both be omitted. It preserves the earlier rejection of compulsory numeric scales, forced lessons, and auxiliary authors. [Design decisions](../DESIGN-DECISIONS.md) and [history](../CHANGELOG.md) explain the change without revising earlier results.

## Scope and extensions

A basic continuing persona does not require multiple-persona society, births, continuous background exploration, an ongoing service, or a physical body. The conditional boundaries for those features remain in [work and boundaries](WORK-AND-BOUNDARIES.md) and [deployment decisions](../implementation/DEPLOYMENT-DECISIONS.md).

The historical E1–E6 labels remain attributable in the [decision register](../DESIGN-DECISIONS.md) and [historical evaluation map](../evaluation/HISTORICAL-RESULTS.md). They do not establish that any optional feature is deployed or approved for a specific use.

The [source manifest](../sources/SOURCE-MANIFEST.md) locates retired documents at immutable revisions. [Contributing](../CONTRIBUTING.md) explains how to change the current design without recreating competing manuals.
