# Contributing to the AI Personas design

[Home](README.md) · [Decisions](DESIGN-DECISIONS.md) · [Worksheets](templates/README.md)

Contributions should help a reader understand the purpose, required behavior, reasons, boundaries, and evidence of AI Personas without needing the author's private context. This repository is a design reference, not an implementation tutorial.

## What belongs here

Plain-language design requirements, responsibility and lifecycle descriptions, interface behavior, conceptual relationships, user journeys, worked examples, decision rationale, accessible diagrams, failure scenarios, and evaluation criteria belong here. Describe information and behavior in prose or tables rather than programming-language structures.

Application code, command tutorials, pseudocode, configuration samples, request or response payloads, embedded diagram-source blocks, executable validation scripts, and branch-specific patch plans do not belong in the current design reading surface. Put implementation artifacts and their tests in the appropriate implementation project. SVG files are editable artwork, not examples of application logic.

## Choose the right home

| Contribution | Home |
|---|---|
| Explanation for a first-time reader | Start guide or glossary. |
| Required behavior and failure handling | Relevant design chapter and, where needed, system contract. |
| New or changed obligation | Requirement index and affected acceptance scenarios. |
| Rationale or a resolved tradeoff | Design decisions and relevant source brief. |
| Illustrative journey | Worked examples, explicitly labeled hypothetical. |
| Reusable authoring aid | Worksheets, without making every field mandatory for small work. |
| Artwork | Editable visual assets, visual guide, alt text, and matching prose. |
| Actual evaluation evidence | Exact configuration and observations in the implementation's evidence records; link a scoped report rather than inventing results here. |

## Authority and consistency

Invariants protect the foundation. Detailed chapters and implementation contracts define behavior. The requirement index points to those rules; acceptance scenarios exercise them. Overview, source briefs, examples, worksheets, and artwork explain rather than override them.

A conflict between detailed requirements is a design defect. Identify it, preserve the safer authority and evidence boundary, and document a resolution. Do not use an outdated historical source to weaken current restrictions.

## A useful change proposal

State the reader or product problem, affected requirements, motivating evidence or counterexample, proposed rule, alternatives, expected consequences, and evaluation plan. Distinguish an editorial clarification from a changed obligation, a new extension, or a deployment-specific choice.

Preserve identifiers. A replacement requirement should record what it supersedes and why. A changed evaluator must preserve earlier results under their original criteria. Update affected examples, glossary terms, diagrams, and source mappings in the same coherent change.

## Review before accepting a change

Read the change as someone who has not seen the previous conversation. Define unfamiliar terms on first use or link the glossary. Explain the normal path, refusal or failure path, recovery or stopping behavior, and evidence needed. Avoid claims that source material or a test description proves a working product.

Check relative links, heading anchors, image paths, tables, and all mentioned identifiers. Ensure every new document is reachable from an appropriate index. Remove session-only download links and opaque citations. Keep paths portable rather than requiring a local computer or development setup.

For artwork, preserve labels, source-section references, accessible descriptions, and a full text explanation. Inspect the actual visual at a useful size after editing; do not remove a refusal, decline, or revalidation path just to simplify the drawing. Unchanged historical artwork should not be represented as freshly rendered or validated.

## Sources and evidence

When a factual or research claim needs external support, cite an accessible primary source and identify the precise claim, date, and limitation. A historical observation about an implementation is not a current audit. A proposed scenario is not an executed result.

Use [source provenance](sources/SOURCE-MANIFEST.md) to preserve historical material without requiring readers to study old code. Rewritten briefs must not inherit integrity claims belonging to different historical bytes.

## Rights and governance

Do not add private project data, credentials, proprietary material without rights, or invented professional endorsements. Do not choose or imply a repository license on behalf of its owner. The deployment decision register explicitly leaves licensing and contribution terms for owner approval.

Adoption authority remains with the repository's authorized maintainers. An accepted documentation contribution changes the design reference; it does not establish that the corresponding behavior exists in a runtime or is suitable for deployment.
