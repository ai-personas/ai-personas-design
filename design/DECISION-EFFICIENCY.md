# Decision efficiency and bounded working context

[Design chapters](README.md) · [Capabilities](04-capabilities-and-action.md) · [Resources](05-authority-and-resources.md) · [Completion](06-evidence-and-completion.md)

This is a clarification of proportional work, capability discovery, resource accounting, and evidence-backed completion. It does not add a task workflow, a new requirement identifier, or a claim of measured product performance.

## Durable does not mean present in every prompt

A persona's continuing identity, permitted experience, and accepted responsibilities are durable. That does not require every previously encountered capability's full calling instructions to remain in every later decision. The action archive and the current decision context serve different purposes.

An implementation should keep a bounded working set of capability instructions: general primitives, instructions needed to observe or stop current effects, and recently requested or used capabilities. Older instructions remain discoverable under current permissions. Removing instructions from a prompt neither erases history nor forgets a lesson, withdraws a commitment, grants access, or completes work.

The boundary must be visible. A persona must be able to tell which capabilities are immediately usable and how to obtain an available capability's complete current instructions. Successfully requested instructions must remain usable for the following decision, including when several are requested together. A retention limit must not turn already-paid discovery into an immediate rediscovery loop. Restart and history projection must preserve this behavior from durable records, rather than relying on a process-local cache.

Availability is checked against current authority. Historical use or discovery does not authorize a capability after permission changes. Failed or foreign discovery must not silently change another persona's working set. Observation, cancellation, and recovery instructions needed for an existing effect must not require speculative rediscovery merely because an older contract left the ordinary working set.

A smaller working set may require later rediscovery. Its bounds are engineering choices to validate, not universal values prescribed by this handbook. A smaller prompt is not an improvement when the extra calls cost more, delay delivery, or reduce the quality of the result.

## Preserve the information that makes work accountable

This distinction concerns reusable capability instructions, not permission to drop substantive evidence. Current human input, accepted obligations, cancellation, authority and funding limits, selected learning, exact selected sources, adverse observations, and unresolved effects retain their existing protections. Capability-instruction eviction must not become a second, hidden memory-selection policy.

The persona continues to choose its methods and collaborators. No task text, profession, personality trait, or hidden workflow should choose an enforced capability sequence. The [fragment-recall design](FRAGMENT-RECALL.md) still places learning authorship in ordinary primary decisions; efficiency does not justify a second generative memory writer or unmetered selection.

## Useful delivery, not successful bookkeeping

A simple request may be satisfied by a direct, attributable answer. A task needing a document, file, tool result, or permission requires the corresponding actual result and evidence. Neither successful internal updates nor a private activity summary substitutes for delivery to the intended recipient. Yielding is distinct from completing the task.

The evaluation must inspect the delivered result, not only whether the response parsed or the action journal accepted it. Extra coordination or learning activity is justified by its contribution to the requested outcome, not by the number of personas, fragments, actions, or status messages it produces. This preserves optional cooperation and continuing learning without making every small task pay for a team process.

## Evaluate the whole task

Compare the same requests under matched models, permissions, allowances, and evaluation criteria. Include a fresh short request, sustained work after many different capabilities have been used, a multi-capability discovery batch, a restart, a permission change, and a failed effect needing observation or cancellation.

| Question | Evidence needed |
|---|---|
| Did the person receive a useful result? | Inspect the actual answer or exact artifact against the request; retain failures and incomplete outcomes. |
| Did context remain bounded? | Measure capability instructions separately from evidence, selected learning, and other prompt sections over short and long histories. |
| Did discovery remain usable? | Demonstrate next-decision use, deliberate rediscovery, restart recovery, and rejection after permission removal. |
| Was the task cheaper overall? | Count every primary, discovery-related, retry, failed, and authorized selector call, including input and output usage, latency, and uncertain exposure. |
| Did savings preserve quality? | Compare completion, correctness, source fidelity, and useful character or learning effects, not merely message or fragment counts. |

Report serialized bytes, tokenizer estimates, enforced reservation bounds, provider-reported usage, and monetary charges separately. A byte reduction or smaller reservation is not a billed-token measurement. Compile checks, deterministic runtime tests, synthetic provider tests, and live behavioral acceptance are separate kinds of evidence. No one category establishes the others.
