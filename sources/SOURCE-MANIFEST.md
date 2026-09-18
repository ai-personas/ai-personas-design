# Source provenance and editorial map

[Source guide](README.md) · [Design decisions](../DESIGN-DECISIONS.md) · [Change history](../CHANGELOG.md)

## What is current

Handbook edition 2.0 rewrites the five source paths as code-free design briefs. **Their current bytes are not the original attachments.** The filenames preserve navigation continuity, not competing specification versions. Current requirements live in the [design chapters](../design/README.md), [contracts](../implementation/CONTRACTS.md), and [invariants and index](../implementation/REQUIREMENTS.md).

## Exact historical inputs

The baseline for this refactor is design-repository commit **0c96694303e344ef976150a4d544f3ca57f77d33**. The links below are pinned to that commit, not a moving branch. They are optional historical references; understanding or implementing this design does not require reading them.

| Historical input | Original attachment name recorded in the prior manifest | Current code-free destination |
|---|---|---|
| [Original S1 report](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/S1-prior-research-report.md) | deep-research-report(2).md | [Foundations](S1-prior-research-report.md) |
| [Original S2 proposal](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/S2-emergent-design.md) | AI-PERSONAS-EMERGENT-DESIGN(1)(2).md | [Emergence](S2-emergent-design.md) |
| [Original S3 v1.1](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/S3-specification-v1.1.md) | AI-PERSONAS-RUST-FINAL-SPEC(1)(2).md | [Architecture rationale](S3-specification-v1.1.md) |
| [Original S4 v1.2](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/S4-specification-v1.2.md) | AI-PERSONAS-RUST-SPEC-v1.2(1)(2).md | [Reliability safeguards](S4-specification-v1.2.md) |
| [Original S5 review](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/S5-stress-test-report.md) | STRESS-TEST-REPORT(1)(2).md | [Stress scenarios](S5-stress-test-report.md) |
| [Earlier complete proposal](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/AI-PERSONAS-DESIGN-PROPOSAL.md) | Consolidated design proposal with visual integration | [Current overview](../AI-PERSONAS-DESIGN-PROPOSAL.md) and detailed chapters |

The original attachments' integrity hashes remain available in the [historical source manifest](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/SOURCE-MANIFEST.md). They must not be presented as fingerprints of the rewritten briefs.

## How material was consolidated

| Inherited material | Treatment in this edition |
|---|---|
| Persistent identity, six concepts, fragments, capabilities, context, and a readable interface | Explained in the start guide and design chapters. |
| Emergent understanding, priorities, organization, population, and learning | Preserved as goals requiring observable evidence, including no-birth restraint. |
| v1.2 corrections to v1.1 | Preserved conceptually: continuation, assumptions, orientation, completion barriers, findings, iteration, closeout, finite activity, and exact release. |
| I01–I21, the requirement catalogue, and M/B/X acceptance identifiers | Retained in consolidated, cross-linked indexes. |
| E1–E6 extensions | Explicitly proposed; not silently represented as implemented or scientifically established. |
| Runtime stacks, branch patch instructions, providers, prices, and authentication details | Removed from current design prose; future implementations make and verify their own deployment choices. |
| Code snippets, diagram markup blocks, command tutorials, and session-only links | Removed from the current Markdown reading experience. Rendered SVG artwork and text explanations remain. |
| Historical packaging and visual-validation records | Retained in Git history, not presented as current product-test results. The current inventory is human-readable in the visual guide. |

## Evidence and authority

S4 historically superseded S3's ambiguous conceptual rules. This edition's requirement hierarchy is explained in [the design guide](../design/README.md). Source summaries, examples, and historical code never override a current permission or evidence boundary.

The earlier reports included observations about a separate AI Personas runtime. Those observations remain historical and are not refreshed by this documentation refactor. The code-free implementation guide states required behavior without claiming that any existing runtime already provides it.

The supplied ideas motivate the design; live implementation evidence must support claims of competence, learning, cooperation, safety, and deployment suitability. Source provenance records where an idea came from, not proof that the idea works.
