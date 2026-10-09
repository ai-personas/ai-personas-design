# Contributing to the AI Personas design

[Home](README.md) · [Design authority](design/README.md) · [Decisions](DESIGN-DECISIONS.md)

Contributions should make the current design understandable without private conversations, implementation setup, or earlier attachments. This is a design reference, not an implementation tutorial.

## What belongs here

Plain-language requirements, rationale, responsibilities, interface behavior, lifecycle and failure descriptions, hypothetical journeys, source limitations, accessible artwork, and evaluation criteria belong here. Describe information and behavior in prose or tables.

Application code, command tutorials, pseudocode, configuration samples, request or response payloads, embedded diagram-source blocks, executable validation scripts, and branch-specific patch plans do not belong in the active design surface. Put implementation artifacts and their tests in the relevant implementation project. SVG files are editable artwork, not examples of application logic.

Fragments are persona-defining, characteristic-bearing prompt parts. Selected assembly provides context for LLM reasoning; context, reasoning, actual interaction/actions, and evolution of authored prompts together constitute the persona. Review conceptual claims against that account, rather than treating fragments as episodic memory, a fact store, or RAG under a new name. Facts and experience may inform a fragment without defining its purpose. Plain domain knowledge and generic technical procedures are assets whether the persona or another author writes them; tools, skills, code, data and records retain their supporting roles. Classify by purpose, not authorship or first-person styling. Characteristic approaches can refer to exact technical assets without duplicating those assets as character. First-person fragment examples may illustrate how a persona understands itself or its experience. Label invented examples as hypothetical. Do not turn a convenient example layout into a compulsory schema.

Keep the normal beginning clear: attributed trait seed, bounded initial LLM-authored candidate fragments, coherent accepted starting account, and continuing primary-LLM self-harmonization. Preserve genuine alternative origins without calling supplied text generated. Generated starting detail is not user testimony or prior experience. Harmonization can clarify scope and retain useful tensions or no change; it cannot conceal unresolved contradictions, restyle the corpus automatically, or override character controls.

## Give each subject one authoritative home

| Contribution | Home |
|---|---|
| Persona meaning, character, fragment representation, maturation, or next-context choice | [Persona core](design/PERSONA-CORE.md) |
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

Read the change as someone who has not seen the previous conversation. Define unfamiliar terms or link the glossary. Explain the normal case, refusal or failure, recovery or stopping, and evidence needed. Keep small work proportional; do not require a fragment edit, team, assessment, or completed worksheet merely because an example shows one. Every persona invocation still needs maintenance input and an explicit accepted-response disposition. A concise no-change reason is compatible with small work; silent omission is not.

Check relative links, heading anchors, image paths, tables, mentioned identifiers, and reachability from the indexes. Keep paths portable. Remove session-only links, private local paths, opaque citations, credentials, and private project data. Avoid factual claims that a document edit or test description proves a working product.

When editing artwork, preserve relevant boundaries and a full text explanation. Inspect the actual rendered visual at a useful size. Do not claim that old artwork was newly validated, and do not leave a retired cognitive architecture looking like the current picture.

## Review character and maintenance changes

Keep one accepted, versioned character account with required semantic OCEAN traits and VAD modeled affect. A profile, prompt view, or display must not become another author. Distinguish stable traits, transient affect, outward expression, optional contextual tendencies, skills, and permissions. Do not smuggle in mandatory numeric scores, arbitrary extra axes, deterministic tool-use rules, or an invented psychology claim. All persona-authored fragments carry the owner's character; factual records and exact source quotations keep their own attribution and form.

Check initialization, search and selection calls, task decisions, tool follow-ups, peer communication, coordination, maintenance, and every model-based repair path. Renaming a persona decision as a helper does not exempt it. Keep deterministic host recovery and bounded non-persona utilities distinct from persona inference. Do not claim application control over provider-internal processing that the interface does not expose.

Each persona call combines work, characteristic-fragment maintenance, supporting-resource maintenance, and next fragment/resource choice. Review that the explicit maintenance disposition covers both scopes; one short joint no-change reason can suffice. Proposals for permitted creation, storage, refinement, organization, or deletion identify authorized files/paths and useful discovery cues or regex where appropriate, without a fixed folder taxonomy. Proposed, accepted, and actually stored changes stay distinct. Histories, messages, and tool receipts preserve real observations; a model-generated account cannot fabricate events or relabel imported assets as its own authored character. Next-context omission preserves only an already-valid selection within its original scope/lifetime; it neither renews it nor forces another call.

Distinguish a proposed patch, reasoned no change, explicit block, bounded deferral, and a failed attempt that produced no usable decision. Preserve known unresolved candidates rather than disguising them as no change. Validate the whole response before substantive dispatch, while retaining independent host cancellation, receipts, and accounting. Preserve the existing fresh-decision fence after effective-character changes, including reads and waits, without treating every transient affect annotation as a stable-character revision. Use the [core](design/PERSONA-CORE.md) and [contracts](implementation/CONTRACTS.md) for the actual acceptance and independence rules.

The 7 October optional-descriptor and omitted-maintenance norms are explicitly superseded. Preserve those decisions and their evaluator limitations as history; do not restore them through a worksheet, source summary, or an old test pass. A code-free document check cannot demonstrate every-call runtime coverage or psychological realism.

## Review development, navigation, and compactness changes

Keep both the authored persona-context corpus and each assembled prompt bounded; useful self-organization can reduce either while preserving characteristic distinctions. Supporting evidence and operational records retain provenance, expiry, access, and accountability, without becoming the persona’s defining representation. Make the reciprocal account visible: accepted traits shape own-voice fragments; selected fragments and current character reach the primary LLM; that perspective informs all discretionary task, human/peer communication, collaboration, navigation, and maintenance choices; actual consequences can support revised fragments, scoped relationships, and permitted current-character evolution. Avoid both a decorative persona rewrite after generic decisions and a claim that traits override facts or mandatory constraints. An aging analogy explains experience-shaped continuity, not elapsed time, counts, weight training, or inevitable wisdom. Methods, transient state, relationship interpretations, and effective-character revisions keep their different controls.

Keep associative search cues, exact evidence references, and mandatory qualification or accepted-warning dependencies distinguishable. The primary LLM authors useful cues and chooses whether and how to search or use supported patterns. A search match supplies a candidate, not endorsement or accepted selection. A cue is data, not executable shell content or authority. Do not add automatic host traversal, a graph engine, hidden semantic author/selector, forced outgoing links, or fixed folders. Sparse notes and incomplete indexes must remain understandable; no-match, partial search, and missing exact evidence are different outcomes.

Apply the same primary-owned selection contract to separately retained histories, tool-use records, tool definitions, skills, scripts, code, and data. Preserve their actual authorship; an imported skill or raw receipt is not own-voice persona prose. Start discovery with a small bounded bootstrap, never the entire catalogue of tool names/descriptions, schemas, or skill summaries for an LLM to filter. Check the first choosing call as well as later calls, and distinguish the host registry, provider-facing payload, and model-visible context. The bulk catalogue stays outside both exposure surfaces. Descriptors, indexes, hidden provider expansion, and retained session context cannot bypass those bounds.

Preserve direct known-reference and known-current-guidance fast paths. Discovery, reading, selection, actual loading/exposure, invocation, and observed results are different facts, not mandatory separate calls. Resource finding supplies no authority; a saved script is not installed or currently runnable. Review actual versions, executable bindings, dependencies, permissions, freshness, changed resources, and returned observations at their existing boundaries. Execution/provenance/data dependencies need not all be prompt contents, but required operative qualifications cannot be silently reduced to snippets. Do not execute help commands as though they were inert document reads.

Review cumulative navigation rather than just depth or returned hits: bootstrap and descriptors, scans, repeated queries, broad fanout, candidate reads, returned text, actual tool/schema exposure, context, loading overhead, time, cost, maintenance, and failed or retried branches all consume the declared allowance. Inspect both each complete provider attempt and whole-episode totals; payload bytes, model-visible tokens, and billed tokens are distinct measures. A smaller final action prompt does not establish savings or useful quality. Stopping optional discovery cannot silently truncate required qualifications. Rename, split, merge, stale cue, changed terminology, cycles, and access withdrawal need honest outcomes, without a hidden semantic redirect or automatic fallback to another service.

Review compactness against the whole declared managed persona-state footprint, including current bodies and cues, archives, old revisions, source copies, aliases, indexes, provenance, qualifications, accepted warnings, effect and context receipts, caches, managed exports/backups, externally retained context, and temporary rewrite duplication where applicable. If an externally retained context tier cannot be measured, expose the incomplete bound. Do not promise control over arbitrary recipient/provider copies. Do not delete, modify, or revoke user-owned delivered artifacts to meet a notebook cap, or quietly use them as an uncounted archive.

Check actual retention and derivative-use policy before describing a lesson as surviving expired raw evidence. Permitted survival preserves honest evidentiary limits; abstraction neither declassifies restricted input nor overrides derivative erasure. A digest is not recoverable source text. Protected unresolved effects, accepted warnings, current obligations, significant exceptions, and unresolved contradictions cannot disappear through consolidation, low retrieval frequency, or time-only decay. Capacity can create a real admission or retention blocker; do not solve it with an unlimited history store or invented resolution.

The [core](design/PERSONA-CORE.md), [contracts](implementation/CONTRACTS.md), and [deployment decisions](implementation/DEPLOYMENT-DECISIONS.md) are the homes for these rules and choices. Extend their existing traceability and evaluation rather than add a competing persona-context protocol. Distinguish an accepted edit, faithful consolidation, successful retrieval, actual supply, later behavior, useful transfer, and broader development. Source studies can motivate comparisons; they cannot grant this architecture a pass.

## Sources and results

Support external factual claims with an accessible primary source, the specific claim, and its relevant date and limitation. Evidence about another system motivates a hypothesis; it does not demonstrate AI Personas behavior. A source's interface feature is not automatically evidence of beneficial maturation or lower total cost.

Keep actual results tied to their exact configuration, evaluator, inputs, and scope. Preserve failures and limitations. Separate implemented mechanisms, mechanically tested behavior, demonstrated persona benefit, and approval for a deployment. Source integrity claims belong to exact bytes; rewritten summaries must not inherit them.

## Rights and governance

Do not include private or proprietary material without rights, invented credentials or endorsements, or sensitive data unrelated to the design. Do not choose a license or contribution agreement for the owner. Those choices remain explicit [deployment and governance decisions](implementation/DEPLOYMENT-DECISIONS.md).

Authorized maintainers adopt design changes. Publication of a coherent design reference does not establish runtime conformance or authorize a deployment.
