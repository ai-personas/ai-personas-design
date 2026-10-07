# Contributing to the AI Personas design

[Home](README.md) · [Design authority](design/README.md) · [Decisions](DESIGN-DECISIONS.md)

Contributions should make the current design understandable without private conversations, implementation setup, or earlier attachments. This is a design reference, not an implementation tutorial.

## What belongs here

Plain-language requirements, rationale, responsibilities, interface behavior, lifecycle and failure descriptions, hypothetical journeys, source limitations, accessible artwork, and evaluation criteria belong here. Describe information and behavior in prose or tables.

Application code, command tutorials, pseudocode, configuration samples, request or response payloads, embedded diagram-source blocks, executable validation scripts, and branch-specific patch plans do not belong in the active design surface. Put implementation artifacts and their tests in the relevant implementation project. SVG files are editable artwork, not examples of application logic.

First-person fragment examples may illustrate how a persona understands itself or its experience. Label invented examples as hypothetical. Do not turn a convenient example layout into a compulsory schema.

## Give each subject one authoritative home

| Contribution | Home |
|---|---|
| Persona meaning, character, fragment representation, learning, or next-context choice | [Persona core](design/PERSONA-CORE.md) |
| Work, cooperation, action, authority, resources, evidence, recovery, or conditional scope | [Work and boundaries](design/WORK-AND-BOUNDARIES.md) |
| Observable host responsibilities and handoffs | [System contracts](implementation/CONTRACTS.md) |
| Requirement traceability | [Requirements](implementation/REQUIREMENTS.md) |
| Evidence needed or a changed success criterion | [Evaluation](evaluation/README.md) and [acceptance](evaluation/ACCEPTANCE.md) |
| Resolved rationale or a compatibility change | [Design decisions](DESIGN-DECISIONS.md) |
| Current limits and dated implementation evidence | [Status](implementation/STATUS.md) and [historical results](evaluation/HISTORICAL-RESULTS.md) |
| Source provenance or a bounded external research claim | [Sources](sources/README.md) |
| Hypothetical illustration or reusable aid | [Examples](examples/WORKED-EXAMPLES.md) or [worksheets](templates/README.md) |

Do not solve a conflict by adding another competing normative manual. Integrate the rule where it belongs and update its consequences everywhere affected. A source brief, worksheet, or diagram may explain a rule, but cannot create a hidden obligation.

## Authority and consistency

The [design index](design/README.md#authority-within-the-repository) states the canonical authority order. I01–I21 protect the foundation. Persona core, work and boundaries, and system contracts are complementary normative views. The catalogue traces them and acceptance scenarios test them. Explanatory and historical material does not override them.

A conflict is a design defect, not permission to select the easiest reading. Preserve conservative authority, privacy, resource, and evidence boundaries while resolving it. A retrieved fragment or persona preference cannot expand the authority to make an external change.

## Propose the actual change

State the reader or product problem, current rule, motivating evidence or counterexample, proposed rule, alternatives, consequences, affected identifiers, and evaluation plan. Distinguish editorial clarification, changed obligation, optional experiment, and deployment-specific choice.

Preserve identifiers where their meaning remains continuous. If their meaning changes, record the change and preserve the old evaluator revision. If a requirement is retired, explicitly map its useful obligations or explain what is deliberately superseded. Do not reuse an old identifier for an unrelated rule or silently change a success criterion to make an old result pass.

Removing a redundant document is useful when its necessary content has a clear home. Git history and immutable source links preserve historical manuals; the active repository should not retain a duplicate obsolete tree or a collection of contradictory pages with small warning banners.

## Review the whole affected reading path

Read the change as someone who has not seen the previous conversation. Define unfamiliar terms or link the glossary. Explain the normal case, refusal or failure, recovery or stopping, and evidence needed. Keep small work proportional; do not require a memory write, team, assessment, or completed worksheet merely because an example shows one.

Check relative links, heading anchors, image paths, tables, mentioned identifiers, and reachability from the indexes. Keep paths portable. Remove session-only links, private local paths, opaque citations, credentials, and private project data. Avoid factual claims that a document edit or test description proves a working product.

When editing artwork, preserve relevant boundaries and a full text explanation. Inspect the actual rendered visual at a useful size. Do not claim that old artwork was newly validated, and do not leave a retired cognitive architecture looking like the current picture.

## Sources and results

Support external factual claims with an accessible primary source, the specific claim, and its relevant date and limitation. Evidence about another system motivates a hypothesis; it does not demonstrate AI Personas behavior. A source's interface feature is not automatically evidence of learning or lower total cost.

Keep actual results tied to their exact configuration, evaluator, inputs, and scope. Preserve failures and limitations. Separate implemented mechanisms, mechanically tested behavior, demonstrated persona benefit, and approval for a deployment. Source integrity claims belong to exact bytes; rewritten summaries must not inherit them.

## Rights and governance

Do not include private or proprietary material without rights, invented credentials or endorsements, or sensitive data unrelated to the design. Do not choose a license or contribution agreement for the owner. Those choices remain explicit [deployment and governance decisions](implementation/DEPLOYMENT-DECISIONS.md).

Authorized maintainers adopt design changes. Publication of a coherent design reference does not establish runtime conformance or authorize a deployment.
