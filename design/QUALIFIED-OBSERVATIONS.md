# Qualified observations, without a memory-management detour

[Design index](README.md) · [Personal fragment graph](FRAGMENT-PERSONA.md) · [Decision efficiency](DECISION-EFFICIENCY.md)

## Status and purpose

This normative clarification applies the existing requirement that a correction
travels with its method to **full observations**, not only deliberately active
memory. It preserves the existing invariants, requirement identifiers, privacy,
resource bounds and persona-owned choices. It introduces neither an additional
workflow phase nor an automatic memory writer. The checks below are design
requirements to demonstrate, not claims about an implementation or measured
savings.

A persona may read a retained method to answer a question immediately. Requiring
another decision to activate that method in future memory before receiving its
necessary qualifications confuses two distinct choices: what to observe now and
what to keep attending to later. A technically successful read is not a useful
observation when it silently leaves behind an essential correction.

## One qualification boundary for full context

When a current full fragment is supplied through an explicit read, its authored
required corrections and prerequisites must travel with it. The same rule
applies when the actual full read is recovered through its receipt. The context
compiler must preserve exact versions and the complete transitive required
bundle. It must not require another model call, a semantic selector, or a
separate persistent memory selection merely to obtain those qualifications.

The rule does not activate arbitrary neighbors. Preview cards, search matches,
optional associations, prose mentioning a fragment, and unread archive references
remain insufficient to select full text. An explicitly recovered observation
must not become a pretext to search the persona's whole history. Existing
current-character and independently selected context remain protected.

A read is an observation, not endorsement, application, retained learning or an
instruction to change future recall. The compiler must not rewrite the graph,
change active selections or delegation, or manufacture an authoring decision.
It should distinguish read-derived qualification from explicit selection in its
admission evidence. Original observations remain immutable and attributable.

## Exactness and failure

The root must correspond to the actual full observation and current permitted
fragment version. An older receipt is not permission to substitute a newer
method. The receiving persona, each graph endpoint, every required fragment and
the applicable source policy must be checked. Private recall must not reopen in
a context explicitly restricted to work-readable information.

Required bundles are indivisible. A stale, withdrawn, inaccessible or oversized
required endpoint must not silently produce a partial method presented as usable.
The implementation must report the blocked qualification, withhold the affected
usable bundle, or use its existing bounded context-recovery path. No unavailable
payload, guessed replacement or new authority may be inferred from that failure.
Recheck versions and permissions at admission, not only during assembly.

An implementation must bound traversal and total context, and deduplicate exact
fragments shared by several observations. Observation-derived qualifications
must not create a permanent selection or fetch old receipts absent from the
current context. As long as a method remains supplied as usable full text, its
necessary qualifications cannot be dropped solely to reduce the token count.

## Acceptance cases

| Case | Required observation |
|---|---|
| One read, chained qualifications | Reading a method supplies its correction and that correction's prerequisite in the next decision, without a second read, selector or persistent selection. |
| Receipt recovery and repetition | Recovering that full read supplies the same exact bundle. Duplicate reads do not duplicate full fragments. Removing the read from current context does not cause a hidden history search. |
| Preview and unrelated content | A graph card, optional association, copied object in a document, tool output or failed read does not activate full memory. |
| Revision and access changes | A changed root is not silently upgraded. A changed or withdrawn required endpoint blocks partial admission. Work-readable-only context does not reopen private recall. |
| Bounds and preservation | Excessive bundles fail explicitly. Ordinary unqualified reads add no qualification context. Compiled observations do not mutate persistent memory, graph, budget or original receipts. |
| Useful result at total cost | The delivered answer uses the relevant complete procedure, or correctly declines an inapplicable one. Report all primary and selector calls, known input/output tokens, retries and uncertain exposure, not only prompt size. |

Use both a matching-scope task and a different-scope control. Check the declared
case against the frozen corpus before any paid run. A setup mismatch discovered
later remains a setup error; an appropriate refusal cannot retroactively turn it
into a predeclared success case.

Compilation, provider receipt, actual application and improved task outcomes are
separate evidence levels. A larger single context may be cheaper overall when it
removes repeated navigation or a wrong answer, but that is a hypothesis until
measured. Compare total cost at equivalent correctness and delivery quality.
Neither fewer tokens in a failed arm nor successful selector transport alone
establishes useful efficiency.
