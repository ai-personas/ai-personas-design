# Useful decisions within a bounded context

[Design handbook](../README.md) ·
[Fragment recall](../design/FRAGMENT-RECALL.md)

This is an evaluation clarification of existing usability, resource, evidence,
and autonomy requirements. It adds no invariant or required task workflow and
reports no implemented, tested, or measured product behavior.

## Optimize the cost of a useful result

The object of optimization is a delivered result that meets the stated need,
not the smallest individual prompt. An implementation can reduce prompt bytes
while making work more expensive through tool guessing, repeated discovery,
suppressed actions, unnecessary clarification, or repeated decisions with no
new observation. Conversely, a small amount of stable contract guidance can be
worth its input cost when it avoids those failures. Neither proposition proves
a measured benefit for a particular model.

Compare matched tasks at exact implementation, model, and configuration
revisions. Preserve the same permission and funding boundaries. Report result
quality alongside total input and output tokens, cached input where documented,
all auxiliary inference and tool costs, first useful delivery latency,
discovery-only decisions, failed and suppressed actions, and unresolved work.
Byte counts, configured exposure bounds, and provider-reported usage are
separate measurements. More activity, retained fragments, or personas is not
itself success.

## A loaded operation must be usable

A bounded command working set may replace a complete command catalog. A loaded
operation nevertheless needs enough meaning to use its typed arguments:
what it does, which identities and versions its arguments name, whether it
replaces or appends state, and which effects require a later observation.
Required qualifications and prohibitions must not disappear when schema
annotations are compressed or old discovery receipts leave the context.

Descriptions should have one authoritative source. An implementation may
supply compact semantic notes alongside a constrained response schema instead
of duplicating full schemas and their nested definitions. It must not truncate
a qualification to satisfy an arbitrary character target or promote task text
to trusted tool instructions. Specialized authoring details may remain
available on demand. Current permission and capability checks still apply.

When an explicit participation already establishes the context for an ordinary
operation, the model should not be structurally forced to spend a separate
primary decision discovering only that operation's syntax. For example, a
persona explicitly invited to assess supplied material should be able to
express a judgment in its first authorized review decision, or choose not to.
This is access to an affordance, not automatic review, role assignment, truth,
acceptance, or completion. An unrelated task should not inherit every possible
specialized operation.

## Supplemental acceptance scenarios

| Scenario | Required observation |
|---|---|
| Small text request | The persona can deliver the requested text without mandatory planning, document discovery, delegation, or a second generative reflection call. Quality and total usage are recorded. |
| Explicit review with material already supplied | Its first authorized review decision can express the relevant judgment or an honest limitation without mandatory syntax discovery. A judgment is not forced and creates no release authority. |
| Loaded tool with easily confused identifiers | The encoded request retains the distinction between record, version, action, grouping, and permission references that the operation actually requires. Test argument interpretation, not just schema round trips. |
| Compaction and restart | A still-loaded operation remains usable without the old discovery receipt. Unloaded operations remain discoverable. The archive, explicit selections, obligations, and spending are unchanged. |
| Capability or mode narrows | Old successful discovery and semantic notes cannot restore unavailable operations. Orientation and recovery modes retain their distinct boundaries. |
| Contract compression | Inspect the actual provider-bound instructions and response schema. Confirm semantic guidance and strict validation together; reject tests that examine only an earlier internal catalog. |
| Cost comparison | Count every primary and auxiliary call through useful delivery or an explicit unresolved result. Report failures and quality regressions as well as savings. |

A deterministic request test demonstrates availability and preservation, not
that a model understood the instruction. A local HTTP fixture demonstrates
encoding, not live provider acceptance. Behavioral evaluation must include
multiple tasks, failure cases, and repeated trials; do not label a synthetic
pass as proof of useful token efficiency.
