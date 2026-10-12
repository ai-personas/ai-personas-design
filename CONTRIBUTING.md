# Contributing to the AI Personas design

[Home](README.md) · [Design authority](design/README.md) · [Decisions](DESIGN-DECISIONS.md)

Contributions should help readers understand the current design without private conversations, implementation setup, or earlier attachments. Write for people who need to understand what the system means, does, and requires. This repository is a design reference, not an implementation tutorial.

## What belongs here

Explain the design in plain language, using prose or tables. Appropriate content includes requirements, rationale, responsibilities, interface behavior, lifecycle and failure descriptions, hypothetical journeys, source limitations, accessible artwork, and evaluation criteria.

Keep application code and implementation instructions in the relevant implementation project, together with their tests. The active design surface must not contain command tutorials, pseudocode, configuration samples, request or response payloads, embedded diagram-source blocks, executable validation scripts, or branch-specific patch plans. SVG files are editable artwork, not examples of application logic.

**Explain what constitutes a persona.** A fragment is a prompt part that carries the persona's character, behavior, or voice. Selected fragments provide context for LLM reasoning. That context, the reasoning, actual interactions and actions, and the evolution of authored prompts together constitute the persona. Review conceptual claims against this full account. Do not reduce the persona to wording style or treat fragments as episodic memory, a fact store, or retrieval-augmented generation (RAG) under another name.

Facts and experience may inform a fragment without defining its purpose. Plain domain knowledge and generic technical procedures are supporting assets, whether written by the persona or another author. Tools, skills, code, data, and records also retain their supporting roles. Classify material by its purpose, not its authorship or use of first-person language. A fragment can describe a characteristic approach and refer to an exact technical asset without copying that asset into the persona's character.

First-person fragment examples may illustrate how a persona understands itself or its experience. Label invented examples as hypothetical, and do not turn a convenient example layout into a compulsory schema.

**Show the normal beginning accurately.** Start with an attributed trait seed. A bounded initial LLM invocation authors candidate fragments, which become a coherent accepted starting account before continuing authorship by the primary LLM. Preserve genuine alternative origins: supplied text must not be called generated, and generated starting details must not be presented as user testimony or prior experience.

Continuing self-harmonization means reviewing the persona's authored material for coherence. It can clarify scope, retain useful tensions, or conclude that no change is needed. It cannot conceal unresolved contradictions, automatically restyle the corpus, or override character controls.

## Give each subject one authoritative home

Put each rule in the document responsible for that subject. Use the other documents to explain, trace, or evaluate it without creating competing requirements.

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

Resolve a conflict by integrating the rule into its proper home and updating every affected consequence. Do not add another competing normative manual. A source brief, worksheet, or diagram may explain a rule, but cannot create a hidden obligation.

## Authority and consistency

Use the [design index](design/README.md#authority-within-the-repository) to determine authority. I01–I21 protect the foundation. Persona core, work and boundaries, and system contracts provide complementary normative views: together, they state the governing requirements. The requirement catalogue traces those requirements, and acceptance scenarios test them. Explanatory and historical material cannot override them.

Treat a conflict as a design defect to resolve. It does not permit choosing the easiest reading. Preserve conservative authority, privacy, resource, and evidence boundaries during resolution. Neither a retrieved fragment nor a persona preference can expand permission to make an external change.

## Propose the actual change

Make the proposal concrete enough for a reader to assess both the change and its consequences. Include:

- The reader or product problem, the current rule, and the motivating evidence or counterexample.
- The proposed rule and the alternatives considered.
- The consequences, affected identifiers, and evaluation plan.

State whether the proposal is an editorial clarification, a changed obligation, an optional experiment, or a deployment-specific choice. Do not leave readers to infer which kind of change they are reviewing.

**Preserve requirement history.** Keep identifiers when their meaning remains continuous. If an identifier's meaning changes, record the change and preserve the old evaluator revision. When retiring a requirement, map its useful obligations to their new homes or explain what is deliberately superseded. Do not reuse an old identifier for an unrelated rule or silently change a success criterion to make an old result pass.

**Remove duplication without losing content.** A redundant document can be removed once its necessary content has a clear home. Git history and immutable source links preserve historical manuals. The active repository should not retain an obsolete duplicate tree or contradictory pages distinguished only by small warning banners.

## Review the whole affected reading path

Read the changed material as someone who has not seen the previous conversation. Define unfamiliar terms or link the glossary. Explain normal behavior, refusal or failure, recovery or stopping, and the evidence needed to assess the result.

Keep small work proportional. An example that uses a fragment edit, team, assessment, or completed worksheet does not make those steps mandatory. Every persona invocation still needs the input required to decide maintenance and next context. Every accepted response must explicitly state its disposition for both responsibilities. A concise, reasoned no-change decision is compatible with small work; silent omission is not.

**Check navigation and publication details.** Verify relative links, heading anchors, image paths, tables, mentioned identifiers, and reachability from the indexes. Keep paths portable. Remove session-only links, private local paths, opaque citations, credentials, and private project data. Do not claim that editing a document or describing a test proves a working product.

**Review the artwork itself.** When editing artwork, preserve the relevant boundaries and a full text explanation. Inspect the actual rendered visual at a useful size. Do not claim that old artwork was newly validated, or leave a retired cognitive architecture looking like the current design.

## Review character and maintenance changes

Keep character coherent across the persona's prompts and decisions. There must be one accepted, versioned character account with required semantic OCEAN traits and VAD modeled affect. OCEAN names openness, conscientiousness, extraversion, agreeableness, and neuroticism. VAD describes modeled affect through valence, arousal, and dominance: pleasantness, activation, and a modeled sense of control. These are semantic descriptions; mandatory numeric scores must not be introduced.

A profile, prompt view, or display must not become another author. Keep stable traits, transient affect, outward expression, optional contextual tendencies, skills, and permissions distinct. Do not introduce arbitrary extra axes, deterministic tool-use rules, or invented psychology claims. All persona-authored fragments carry their owner's character. Factual records and exact source quotations retain their own attribution and form.

**Check every persona decision path.** Review initialization, search and selection calls, task decisions, tool follow-ups, peer communication, coordination, maintenance, and every model-based repair path. Calling a persona decision a “helper” does not exempt it. Keep deterministic host recovery and bounded non-persona utilities distinct from persona inference. Do not claim application control over provider-internal processing that the interface does not expose.

**Check all five responsibilities in each call.** Each persona call combines work, maintenance, and choice of the next context. Every accepted response must explicitly cover the following responsibilities; the table is a review aid, not a required response layout.

| Responsibility | What the response must cover |
|---|---|
| Work | The work of this call and its outcome or current disposition |
| Characteristic-fragment maintenance | An explicit disposition for maintaining persona-defining fragments |
| Supporting-resource maintenance | An explicit disposition for maintaining supporting assets |
| Next fragment context | An explicit decision about fragments for the next context |
| Next supporting-resource context | An explicit decision about supporting resources for the next context |

One short, joint no-change reason can cover both maintenance scopes. For next context, an appropriate explicit decision to preserve context or state that there is no optional need can suffice. These decisions do not force an edit, a new search, an extra call, or a repeated list. Maintenance no-change and next-context choice remain separate decisions.

These requirements apply to short, final, and repair calls as well. Omission invalidates the response. Recovery from prior state is neither an authored judgment nor a renewal of that judgment.

**Make maintenance proposals reviewable.** Proposals for permitted creation, storage, refinement, organization, or deletion identify authorized files or paths. Include useful discovery cues or regular expressions (regex, patterns for matching text) where appropriate, without imposing a fixed folder taxonomy. Keep proposed, accepted, and actually stored changes distinct.

Histories, messages, and tool receipts preserve real observations. A model-generated account cannot fabricate events or relabel imported assets as its own authored character.

**Keep outcomes and acceptance separate.** Distinguish a proposed patch, reasoned no change, explicit block, bounded deferral, and a failed attempt that produced no usable decision. Preserve known unresolved candidates instead of disguising them as no change.

Validate the whole response before substantive dispatch. Keep independent host cancellation, receipts, and accounting available. Preserve the existing fresh-decision fence after effective-character changes, including reads and waits, without treating every transient affect annotation as a stable-character revision. Use the [core](design/PERSONA-CORE.md) and [contracts](implementation/CONTRACTS.md) for the actual acceptance and independence rules.

**Keep superseded rules historical.** The 7 October optional-descriptor and omitted-maintenance norms are explicitly superseded. Preserve those decisions and their evaluator limitations as history. Do not restore them through a worksheet, source summary, or old test pass. A code-free document check cannot demonstrate every-call runtime coverage or psychological realism.

## Review development, navigation, and compactness changes

Review how the persona changes, finds material, and keeps useful context within limits. Both the authored persona-context corpus and each assembled prompt must remain bounded. Useful self-organization can reduce either while preserving characteristic distinctions. Supporting evidence and operational records retain provenance, expiry, access, and accountability; they do not become the persona's defining representation.

**Show how character and experience affect each other.** Make the full relationship visible:

1. Accepted traits shape fragments in the persona's own voice.
2. Selected fragments and current character reach the primary LLM.
3. That perspective informs all discretionary task decisions, human and peer communication, collaboration, navigation, and maintenance choices.
4. Actual consequences can support revised fragments, scoped relationships, and permitted evolution of current character.

Do not reduce persona behavior to a decorative rewrite after generic decisions have already been made. Traits also cannot override facts or mandatory constraints. Maturation involves purposeful revision and organization, with possible no change or regression. An aging analogy explains continuity shaped by experience; it does not mean that elapsed time, counts, or model weight training produce wisdom or guaranteed improvement. Methods, transient state, relationship interpretations, and effective-character revisions retain their different controls.

**Keep search cues distinct from evidence and conditions.** Associative search cues help locate related material. Exact evidence references identify supporting evidence. Dependencies on mandatory qualifications or accepted warnings preserve conditions that must remain attached to relevant material. Do not blur these roles.

The primary LLM authors useful cues and chooses whether and how to search or use supported patterns within bounded lexical or regex discovery. A search match supplies a candidate, not endorsement or accepted selection. A cue is data, not executable shell content or authority. Do not add automatic host traversal, a graph engine, a hidden semantic author or selector, forced outgoing links, or fixed folders.

Sparse notes and incomplete indexes must remain understandable. Report no match, partial search, and missing exact evidence as different outcomes.

**Apply the same selection rules to supporting resources.** The primary LLM also owns selection of separately retained histories, tool-use records, tool definitions, skills, scripts, code, and data. Preserve their actual authorship. An imported skill or raw receipt is not persona prose in its own voice.

Start discovery with a small, bounded bootstrap: the initial information needed to begin finding relevant resources. Never give an LLM the entire catalogue of tool names and descriptions, schemas, or skill summaries to filter. Review the first choosing call as well as later calls.

Keep three things distinct: the host's registry, the payload sent to the provider, and the context visible to the model. The bulk catalogue stays outside both the provider-facing payload and model-visible context. Descriptors, indexes, hidden provider expansion, and retained session context cannot bypass those bounds.

**Assess readiness for the proposed operation.** Preserve direct routes to known references and known-current guidance. Discovery, reading, selection, actual loading or exposure, invocation, and observed results are different facts. They do not require separate calls merely to keep those facts distinct.

Finding a resource supplies no authority to use it. A saved script is not necessarily installed or currently runnable. Review actual versions, executable bindings, dependencies, permissions, freshness, changed resources, and returned observations at their existing boundaries.

Execution, provenance, and data dependencies need not all be prompt contents. Required operative qualifications—the conditions and limits needed for the operation—cannot be silently reduced to snippets. Treat running a help command as execution, not as an inert document read.

**Account for the whole navigation effort.** Depth and returned hits alone do not measure navigation cost. All of the following consume the declared allowance:

- Discovery: bootstrap information and descriptors, scans, repeated queries, broad fanout across many candidates or paths, and candidate reads.
- Context supply: returned text, actual tool and schema exposure, context, and loading overhead.
- Continuing effort: time, cost, maintenance, and failed or retried branches.

Inspect each complete provider attempt and the totals for the whole episode. Payload bytes, model-visible tokens, and billed tokens are distinct measures. A smaller final action prompt does not establish savings or useful quality.

Stopping optional discovery cannot silently truncate required qualifications. Renames, splits, merges, stale cues, changed terminology, cycles, and access withdrawal need honest outcomes. Do not introduce a hidden semantic redirect or automatic fallback to another service.

**Count all managed retained state.** Review compactness against the whole declared managed persona-state footprint, not just the latest fragment bodies. Include:

- Current bodies and cues, archives, old revisions, and source copies.
- Aliases, indexes, provenance, qualifications, and accepted warnings.
- Effect and context receipts, and caches.
- Managed exports and backups, externally retained context, and temporary duplication during rewrites where applicable.

If an externally retained context tier cannot be measured, disclose that the bound is incomplete. Do not promise control over arbitrary copies held by recipients or providers. Do not delete, modify, or revoke user-owned delivered artifacts to meet a notebook cap, or quietly use those artifacts as an uncounted archive.

**Respect retention limits and unresolved obligations.** Before saying that a lesson survives expired raw evidence, check the actual retention and derivative-use policy. Where survival is permitted, retain honest limits on what the remaining material can prove. Abstraction neither declassifies restricted input nor overrides a requirement to erase derivatives. A digest is not recoverable source text.

Protected unresolved effects, accepted warnings, current obligations, significant exceptions, and unresolved contradictions cannot disappear through consolidation, low retrieval frequency, or decay based only on time. Capacity can genuinely block admission or retention. Do not hide that blocker behind an unlimited history store or an invented resolution.

**Keep the rules and their evidence in their established homes.** The [core](design/PERSONA-CORE.md), [contracts](implementation/CONTRACTS.md), and [deployment decisions](implementation/DEPLOYMENT-DECISIONS.md) own these rules and choices. Extend their existing traceability and evaluation rather than adding a competing persona-context protocol.

Distinguish an accepted edit, faithful consolidation, successful retrieval, actual supply, later behavior, useful transfer, and broader development. Evidence for one does not automatically establish the others. Source studies can motivate comparisons; they cannot grant this architecture a pass.

## Sources and results

Make external claims traceable and keep their limits visible. Support each factual claim with an accessible primary source, the specific claim it supports, and the relevant date and limitation. Evidence about another system can motivate a hypothesis, but does not demonstrate AI Personas behavior. An interface feature described by a source is not automatically evidence of beneficial maturation or lower total cost.

Tie actual results to their exact configuration, evaluator, inputs, and scope. Preserve failures and limitations. Keep four claims separate: a mechanism was implemented, behavior was mechanically tested, persona benefit was demonstrated, and a deployment was approved.

Source integrity claims apply to exact bytes. Rewritten summaries must not inherit those claims.

## Rights and governance

Include material only within the rights and governance boundaries that apply to it. Do not include private or proprietary material without rights, invented credentials or endorsements, or sensitive data unrelated to the design.

Do not choose a license or contribution agreement for the owner. Those choices remain explicit [deployment and governance decisions](implementation/DEPLOYMENT-DECISIONS.md).

Authorized maintainers adopt design changes. Publishing a coherent design reference does not establish runtime conformance or authorize a deployment.
