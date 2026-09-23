# Design chapters

[Home](../README.md) · [Start here](../START-HERE.md) · [Glossary](../GLOSSARY.md)

These chapters are the detailed design reference. They state intended behavior, not observed product capabilities. Read them in order for a complete account, or enter through the question that matters to you.

| Chapter | Question it answers |
|---|---|
| [1. Personas and identity](01-personas-and-identity.md) | What continues over time, and how can a persona join, pause, or leave? |
| [2. Memory and learning](02-memory-and-learning.md) | What can be retained, how does it reach a decision, and what would show that it helped? |
| [3. Work and cooperation](03-work-and-cooperation.md) | How do needs become accepted responsibilities without fixed roles or hidden planning? |
| [4. Capabilities and action](04-capabilities-and-action.md) | How do choices produce real, bounded effects and recover from failures? |
| [5. Authority and resources](05-authority-and-resources.md) | Who may authorize what, and how does the system remain within its limits? |
| [6. Evidence and completion](06-evidence-and-completion.md) | What counts as a supported result, and how is an exact release kept honest? |
| [7. Human experience and society](07-experience-and-society.md) | What should people see and control, and what changes for communities or services? |

[Character, experience, and self-directed activity](PERSONA-DEVELOPMENT.md) is the normative cross-cutting refinement for starting profiles, self-authorship, continuing interests, exact experience, bounded personal exploration, accountable stopping, and their behavioral evaluations. It refines the corresponding identity, learning, cooperation, activity, resource, evidence, and interface rules without introducing a prescribed domain workflow. Its intended behavior is not a claim of deployed capability.

The [organization clarification](03-work-and-cooperation.md#how-organization-emerges) explains how decisions and cooperation remain persona-owned. The [delivery review](DELIVERABLE-PRODUCTION.md) is an explanatory correction and reading map, not an additional normative chapter or production engine.

## How to read a requirement

**Must** describes a necessary condition for the applicable feature. **Should** describes a strong recommendation; an implementation records a reason when it takes a different approach. **May** describes an option. Optional does not mean exempt from safeguards once enabled.

The [invariants and requirement index](../implementation/REQUIREMENTS.md) identify the rules and their evaluation links. The [contracts](../implementation/CONTRACTS.md) make cross-component handoffs explicit. Neither a worksheet nor a diagram introduces additional mandatory workflow stages. The [development acceptance rules](PERSONA-DEVELOPMENT.md#acceptance-and-limits-of-conclusions) additionally identify the checks required for the cross-cutting refinement.

## Authority within this handbook

The invariants are the protected foundation. These chapters, the explicitly normative development refinement, and the implementation contracts define detailed behavior. The requirement index points to them; acceptance scenarios test them. The overview, examples, diagrams, and source briefs explain them rather than override them.

A contradiction between detailed requirements is a design defect to resolve and record, not permission to select the easiest reading. Do not broaden authority or weaken an evidence claim while that conflict is unresolved. Changes follow the [contribution guide](../CONTRIBUTING.md).

## Proposed extensions

E1 organizes functional embodiment and persona profiles. E2 adds community charters, representation, and appeals. E3 adds sensitive human-facing safeguards. E4 expands ongoing services and physical interfaces. E5 packages worksheets, identifiers, and conformance profiles. E6 covers contribution and evidence governance. These preserve the earlier proposal's explicit extension status; they are not silently presented as deployed features. The narrow optional-personal-exploration rules in the development refinement do not enable broader ongoing services or physical interfaces.

A basic persistent collaborator does not require a persona society, population growth, or a physical body. A deployment enabling those features must satisfy their applicable contracts and extension checks.
