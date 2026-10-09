# Design reference

[Home](../README.md) · [Start here](../START-HERE.md) · [Decisions](../DESIGN-DECISIONS.md)

This branch has one target design: continuing personas with one accepted, versioned character account covering semantic OCEAN traits and a VAD modeled affect profile. Every authored fragment is a persona-defining, characteristic-bearing prompt part in the persona’s own voice, kept in ordinary files. Their selected assembly is context for LLM reasoning; context, reasoning, actual interaction/actions, and evolving authored prompts together constitute the persona. Experience or facts may inform fragments without defining them as episodic memory or a retrieval cache. Current character and selected fragments inform all discretionary work, communication, collaboration, and context choices; actual task, human, and peer experience can in turn revise fragments, relationships, and permitted character. The primary LLM navigates a compact network of useful authored cues, chooses relevant next context, and returns explicit fragment and supporting-resource maintenance in every accepted persona invocation alongside its work and next-context choice. The older graph-first, auxiliary-selector, and file-proposal manuals are retired from the active reading surface.

The normal beginning is an attributed trait seed expressed by a bounded initial LLM invocation as candidate own-voice fragments, coherently accepted before continuing primary authorship. Self-harmonization preserves useful distinctions and honest conflicts while making usable prompts coherent. The same primary LLM also selects supporting context from separately stored domain knowledge, generic technical procedures, histories, tool-use records, definitions, skills, scripts, code, and data; these assets retain their own meaning and provenance regardless of who authored them. First-person styling does not turn an asset into a characteristic fragment.

## Three complementary views

| Document | Its responsibility |
|---|---|
| [Persona core](PERSONA-CORE.md) | Seeded initialization, identity, semantic traits and modeled affect, reciprocal development, compact character-conditioned fragments, bounded discovery, every-invocation maintenance, and primary-owned fragment/resource selection |
| [Work and boundaries](WORK-AND-BOUNDARIES.md) | Accepted work, cooperation, real actions, selective capability context, authority, resources, evidence, recovery, and conditional extensions |
| [System contracts](../implementation/CONTRACTS.md) | Observable initialization, discovery/read, selection/exposure, execution, and recovery guarantees that make those choices and boundaries reliable |

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

Use the authoritative sections for the detailed rules:

- Character and development: [traits and modeled affect](PERSONA-CORE.md#characteristics-modeled-affect-and-contextual-expression), [own-voice authorship and character controls](PERSONA-CORE.md#character-in-its-own-voice), and [the work and maturation loop](PERSONA-CORE.md#maturation-within-every-primary-interaction)
- Navigation and context choice: [search and exact reading](../implementation/CONTRACTS.md#search-and-exact-reading) and [primary-persona selection](../implementation/CONTRACTS.md#primary-persona-next-context-selection)
- Bootstrap, exposure, and cost: [bounded working context](WORK-AND-BOUNDARIES.md#inference-and-bounded-working-context) and [faithful assembly](PERSONA-CORE.md#bounded-and-faithful-assembly)
- Maintenance and retained state: [every-invocation responsibilities](../implementation/CONTRACTS.md#every-persona-invocation) and [compact retention](PERSONA-CORE.md#compact-retention-and-honest-forgetting)
- Resource availability and authorized execution: [capabilities and actions](../implementation/CONTRACTS.md#capabilities-and-actions)

Precise host records for permissions, evidence, ownership, current work, and resource accounting are still necessary where their meanings apply. Simpler cognitive representation does not mean ambiguous operational boundaries.

The 8 October refinement explicitly supersedes the 7 October interpretation that OCEAN/VAD descriptors and an explicit maintenance response could both be omitted. It preserves the earlier rejection of compulsory numeric scales, forced lessons, and auxiliary authors. [Design decisions](../DESIGN-DECISIONS.md) and [history](../CHANGELOG.md) explain the change without revising earlier results.

## Scope and extensions

A basic continuing persona does not require multiple-persona society, births, continuous background exploration, an ongoing service, or a physical body. The conditional boundaries for those features remain in [work and boundaries](WORK-AND-BOUNDARIES.md) and [deployment decisions](../implementation/DEPLOYMENT-DECISIONS.md).

The historical E1–E6 labels remain attributable in the [decision register](../DESIGN-DECISIONS.md) and [historical evaluation map](../evaluation/HISTORICAL-RESULTS.md). They do not establish that any optional feature is deployed or approved for a specific use.

The [source manifest](../sources/SOURCE-MANIFEST.md) locates retired documents at immutable revisions. [Contributing](../CONTRIBUTING.md) explains how to change the current design without recreating competing manuals.
