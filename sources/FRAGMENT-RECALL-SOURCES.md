# Sources for optional semantic fragment selection

[Design](../design/FRAGMENT-RECALL.md) · [Acceptance](../evaluation/FRAGMENT-RECALL.md)

**Checked: 2026-09-25.** These are public primary vendor sources consulted for the design. They document capabilities and limitations, not execution evidence for AI Personas. The architecture, graph policy, provisional shortlist sizes, and acceptance cases are design choices made here. No private implementation source, credentials, or customer execution data is reproduced.

## Documented capabilities

[TypeSafe API reference](https://docs.typesafe.ai/api) describes typed evaluations over supplied state. Choice selects one option and returns its distribution; Score and Noul have different semantics. Question instructions can contain structured candidate-specific information. A question map key routes the answer but is not sent as semantic content to the model. This supports explicit, candidate-local questions. It does not make the service a graph database, full-text index, or fragment writer.

[TypeSafe re-ranking example](https://docs.typesafe.ai/cookbooks/rerank_typesafe) illustrates evaluating retrieved passages for relevance. It motivates narrowing the collection before semantic assessment. It does not measure candidate recall, privacy, or benefit for a persona's own fragment graph.

[Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) describes several questions evaluated in one request, with code combining the returned assessments. The design uses independent candidate judgments; it does not assume one answer becomes another question's state within the same batch. Vendor latency descriptions are not guarantees for this workload.

## Limits that shape the design

[Confidence](https://docs.typesafe.ai/confidence) explains that the confidence field is derived from the returned probability distribution. It is not an independent correctness test. The design therefore requires domain evaluation and explicit unknown outcomes instead of treating a high number as factual verification.

[Jev 1.13 limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13), labeled by the vendor as reviewed on 2026-09-17, describe difficulties with numerical precision, date comparison, indirection, distracting state, adversarial input, and generation. This motivates keeping identity, access, arithmetic, and budget checks in code; using compact atomic questions; and retaining the primary LLM as the sole generative persona author. Prompt injection remains a relevant assessment failure mode despite typed outputs. These version-specific limits must be rechecked for another model release.

## Versioning and operational assumptions

[Models](https://docs.typesafe.ai/models) documents versioned model identifiers, moving aliases, input constraints, and deployment pricing. Its current table identifies Jev 1.13.0 and text-only input. It distinguishes the overall request limit from the shared-state-plus-largest-question limit. A deployment must check both using its actual configured model rather than assuming a short candidate count guarantees fit.

The same page states that current customization is through supplied state and questions rather than per-account fine-tuning. A common selector therefore does not contain the persona's private identity by default. Per-persona fragments, authorized request state, and recall policy remain essential.

The design deliberately does not freeze a vendor price, rate limit, or latency into the architecture. Operations must use current approved metadata, reported usage, and separately measured costs. A moving alias is not a pinned version. Data processing terms and retention promises require their own approval; vendor product documentation is not a grant to disclose private fragments.

## What these sources do not establish

They do not prove that semantic selection beats indexed retrieval alone, that a fragment description is faithful, that a candidate judged relevant is true, that a character will influence every action, or that a persona will mature. Those are separate questions in the acceptance suite. The 24-candidate and 48-question illustration is a local evaluation proposal, not a vendor service limit or measured result.
