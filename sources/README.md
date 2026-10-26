# Sources, rationale, and historical evidence

[Home](../README.md) · [Research and rationale](PERSONA-FILES-RESEARCH.md) · [Provenance manifest](SOURCE-MANIFEST.md) · [Historical results](../evaluation/HISTORICAL-RESULTS.md)

These pages explain the reasoning behind the design and show where to inspect its sources and earlier results. The [human-user requirements](../USER-REQUIREMENTS.md) govern the [persona core](../design/PERSONA-CORE.md), [work and boundaries](../design/WORK-AND-BOUNDARIES.md), [contracts](../implementation/CONTRACTS.md), and derived invariants. Source pages explain those choices; they do not create a competing specification. Under UR-052, experimental limits in a cited study and historical resource or access rules do not impose application quotas, safety gates or approval requirements.

The persona includes its context, LLM reasoning, actual interactions and actions, feedback, and continuing revision of its authored prompts. Persona-authored fragments are prompt parts that express its character. Selected fragments give the LLM characteristic-bearing context for reasoning. Supporting assets have different purposes: domain knowledge, generic procedures, histories, tools, skills, scripts, code, and data support the persona's work without becoming its defining fragments, regardless of who authored them.

**Find the relevant research.** The following pages separate research findings from design choices and hypotheses that have not yet been tested:

- [Research and rationale](PERSONA-FILES-RESEARCH.md) separates established human OCEAN and affect constructs, limited evidence about LLM personas, engineering choices, and unrun hypotheses. It explains trait-grounded fragments in the persona's own voice, context selection by the primary LLM, and explicit consideration of self-revision on every persona invocation. Considering revision does not require making an edit.
- [Contextual persona](PERSONA-FILES-RESEARCH.md#contextual-persona-operational-interpretation-and-its-limits) explains the persona as an operational loop, without claiming to settle metaphysical identity. It recognizes that both the trained model's prior tendencies and the supplied context influence behavior.
- [Context adaptation](PERSONA-FILES-RESEARCH.md#context-adaptation-is-the-closer-engineering-comparison) compares GEPA and ACE with authored persona context. Their optimization mechanisms and task results remain distinct from the proposed persona loop.
- [Trait-seeded bootstrap](PERSONA-FILES-RESEARCH.md#trait-seeded-bootstrap-and-self-harmonization) distinguishes candidate fragments authored by initialLLM, the accepted starting context, and continuing development by primaryLLM. Self-harmonization must preserve meaningful differences in scope; claims that it helps need evidence.
- [Direct collaboration evidence](PERSONA-FILES-RESEARCH.md#trait-composition-and-collaboration-direct-evidence-and-limits) separates the effects of trait composition from diversity, role assignment, affect, and sampling. It includes positive findings, null results, limits on partner selection, and caveats about total resource use.
- [Reciprocal development](PERSONA-FILES-RESEARCH.md#reciprocal-development-from-actual-work-and-interaction) explains both directions of influence: character shapes work and interaction with humans and peers; actual experience can inform later fragments and attributable character revision. Human development provides an analogy, not evidence that the same development occurs in AI.
- [Compact associative fragments](PERSONA-FILES-RESEARCH.md#compact-associative-fragments-and-selective-retention) distinguishes cues for finding material, references to exact evidence, and qualifications that must accompany selected material. It covers selective retention, harmful revival of earlier material, accounting for the whole managed store, and the limits of a retained interpretation when its raw evidence is unavailable.
- [Need-directed supporting context](PERSONA-FILES-RESEARCH.md#need-directed-supporting-context) keeps histories, tool descriptions, skills, scripts, and data distinct from persona-defining fragments. It explains persona-chosen discovery through text matching and direct access to exact known resources.
- [Direct tool-discovery evidence](PERSONA-FILES-RESEARCH.md#direct-tool-discovery-evidence) distinguishes complete paths from fractional recall, and assisted selection from an unaided cold start. These are different levels and conditions of evidence.
- [Provider and standards fit](PERSONA-FILES-RESEARCH.md#provider-and-standards-fit) explains why deferred loading, or disclosure of metadata for every skill, does not by itself establish selective provider requests or model-visible context. The related [lifecycle evidence](PERSONA-FILES-RESEARCH.md#supporting-resource-lifecycle-evidence) uses MCP 2026-07-28 and SLSA v1.2, with explicit limits on what their provisions establish for this design.
- [Generated reusable assets](PERSONA-FILES-RESEARCH.md#generated-reusable-assets-empirical-limits) separates evidence of useful reuse on tasks from claims about asset construction, discovery, environment readiness, cost, or persona development.

**Trace earlier sources and results.** Historical records preserve what was proposed or reported under the rules that applied at the time:

- [The provenance manifest](SOURCE-MANIFEST.md) pins the 7 October predecessor, the earlier pre-consolidation tree, and the lineage of the original supplied sources. It includes retired manuals, graph/selector figures, numeric-character contracts, and earlier file proposals.
- [The historical-results ledger](../evaluation/HISTORICAL-RESULTS.md) preserves original evaluation identifiers, reported observations, and their criteria. Those results do not grant a pass under current requirements.

Earlier S1–S5 briefs, the selector vendor-source page, and superseded design addenda now live in Git history. Their useful distinctions about identity, accepted responsibility, resource use, source attribution, evidence and cooperation are reconciled in the current normative documents. Earlier application quota and access rules remain historical under UR-052, as do superseded architecture choices; they are not selectable alternatives in the active design. The manifest and complete pinned tree make their old paths discoverable.

**Read current obligations alongside their history.** The 8 October revision requires semantic OCEAN coverage and distinct VAD modeled affect within the accepted, versioned character account. OCEAN covers openness, conscientiousness, extraversion, agreeableness, and neuroticism; VAD covers modeled valence, arousal, and dominance. The account must express their meanings, but numeric scales and stereotyped mappings from traits to actions are not required. Every persona-authored reusable fragment embodies the persona's own perspective.

Under the 10 October correction, each persona invocation combines work, maintenance, and next-context choice. Every accepted response must explicitly cover:

1. **Work:** the response to the invocation's work.
2. **Maintenance:** outcomes for both characteristic fragments and supporting assets. One shared, justified no-change disposition can cover both scopes.
3. **Next context:** a disposition for both fragments and supporting resources. An explicit decision to preserve the applicable context or that there is no optional need can suffice.

Maintenance no-change does not substitute for a next-context decision. These duties require explicit judgments, not compulsory edits or searches. The normative chapters define their exact meaning, call coverage, and failure rules. The source pages explain the motivation and preserve the earlier, weaker obligations for honest comparison. Considering supporting assets on every call is a requested design hypothesis; progressive-loading literature has not proven its benefit.

**Keep design commitments separate from demonstrated results.** Adopting this target does not establish that the implementation has caught up. Human psychometrics supplies vocabulary. LLM studies support limited claims about individual components. The complete integration remains untested here. Neither citations nor compliance with a structured response format provides a 100% guarantee of useful character, grounded maturation, or reliable effects.

New claims need evidence appropriate to their scope:

| Claim | Evidence required |
|---|---|
| An empirical finding | Accessible primary sources, exact versions or dates, the precise claim they support, and their limitations |
| Runtime behavior | The above where applicable, plus exact implementation revisions, observations, and the applicable evaluation criteria |

**Evaluate the full context and cost.** The bootstrap/resource refinement retains the same evidence boundary. It calls for evaluating how the whole context is composed and what the whole episode costs. That accounting includes unsuccessful discovery, repeated input, provider expansions, caching, initialization, and maintenance.

Keeping hundreds of catalogue entries out of an LLM request is a chosen, observable boundary. Whether the system finds useful resources and produces adequate work more efficiently remains a separate set of unrun claims. The recorded inspection of mutable documentation took place on 8 October 2026. That inspection date is neither the documentation's publication date nor a record of adapter validation.

**Interpret memory and retention evidence within its limits.** Memory and retention literature offers related evidence about discovery, bounded storage, and provenance. Remembering facts does not define the persona or establish its characteristic behavior. The compact-context refinement does not import a validated aging curve, a forgetting score, or automatic model training.

Any claim about the size of the whole managed store must count managed indexes, archives, versions, metadata, external memory tiers, and peak copies. Arbitrary copies held by recipients or providers remain outside the promised control. User-owned deliverables retain their own authority and retention boundaries.

A smaller fragment collection is useful only if it preserves effective characteristic context, keeps retained guidance appropriately qualified, and honestly represents what has been lost.
