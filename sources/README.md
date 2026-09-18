# Design sources: the reasons behind the handbook

[Home](../README.md) · [Design decisions](../DESIGN-DECISIONS.md) · [Provenance manifest](SOURCE-MANIFEST.md)

Here, a **design source** is a readable account of the ideas, constraints, alternatives, and failure cases that informed AI Personas. These are not application source files, programming examples, or additional competing specifications.

The five briefs below replace the old code-heavy reports in the current reading experience. Their historical filenames remain stable for existing links, but their contents are newly edited design explanations. They are not unchanged copies of the original attachments. The [manifest](SOURCE-MANIFEST.md) links to exact originals in Git history for optional provenance review.

| Source | Design question | Main contribution |
|---|---|---|
| [S1 — Foundations](S1-prior-research-report.md) | What is the smallest useful conceptual foundation? | Continuing identity, six concepts, ordinary work, memory, capabilities, and a comprehensible experience. |
| [S2 — Emergence](S2-emergent-design.md) | What should arise from work rather than be scripted? | Understanding, improvement, priorities, organization, population, and learning. |
| [S3 — Architecture rationale](S3-specification-v1.1.md) | Where do judgment and enforcement belong? | Distinct responsibilities, individual agendas, accepted commitments, and implementation-independent boundaries. |
| [S4 — Reliability safeguards](S4-specification-v1.2.md) | What prevents convincing activity from masquerading as completion? | Accepted continuation, bounded orientation, actual-completion barriers, current evidence, and safe closeout. |
| [S5 — Stress scenarios](S5-stress-test-report.md) | How can the design fail, and what would reveal it? | Counterexamples, observable corrections, and the boundary between a scenario and a measured result. |

## How these sources relate to requirements

The detailed [design chapters](../design/README.md), [contracts](../implementation/CONTRACTS.md), and [invariants](../implementation/REQUIREMENTS.md) define this edition's intended behavior. Source briefs explain why; they do not override those rules. Examples and artwork are explanatory, not separate authorities.

Historically, the v1.2 specification resolved ambiguities in v1.1. This edition preserves those conceptual resolutions while removing old programming-language instructions and unverified claims about current runtime branches. It does not direct changes to another repository or claim that another implementation is compliant.

## What was intentionally not carried forward

The current sources omit implementation snippets, command syntax, historical patch plans, provider and authentication advice, stale model or pricing assertions, session-only download links, and unresolved chat citation tokens. None is needed to understand the design. Removing them is not a claim that their underlying technical questions have been answered for every future deployment.

External research claims from earlier reports are not silently republished as verified facts. A future evidence-based addition should identify an accessible primary source, its date, the precise supported claim, and its limitations. Product behavior still needs evaluation in the actual implementation.
