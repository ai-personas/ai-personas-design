# The persona is the whole characteristic-context loop

[Home](README.md) · [Start here](START-HERE.md) · [Design authority](design/README.md) · [Persona core](design/PERSONA-CORE.md) · [Work and boundaries](design/WORK-AND-BOUNDARIES.md) · [System contracts](implementation/CONTRACTS.md) · [Artwork provenance](sources/SOURCE-MANIFEST.md#artwork-retirement)

These illustrations explain how a continuing persona works, from its initial character to context choices, cooperation, recovery, and evidence. Each one is placed beside the relevant design rules, with an accessible text equivalent. Start with the whole loop, then choose a topic below. The pictures teach the design; they do not demonstrate a running system.

![Two separately purposed stores supply bounded context to the primary LLM. Actual decisions and consequences inform later authorized revision. Every call also has maintenance and next-context duties.](assets/persona-files-loop.svg)

**Figure: How a continuing persona works.** This is a conceptual explanation of the design. [Read the exact rules](design/PERSONA-CORE.md#maturation-within-every-primary-interaction); the explanation below retains their qualifications. [Open the illustration](assets/persona-files-loop.svg).

<details>
<summary>Text equivalent of the illustration</summary>

How a continuing persona works

AN ILLUSTRATED DESIGN STORY

What should shape my next decision?

Stored files

Exact context

One primary language model makes judgments

Characteristic fragments

How this persona approaches, behaves and speaks.

Supporting assets

Knowledge, tools, skills, data and attributed history.

Choose bounded next context

Use known exact references or bounded file search. Explicit preserve or no optional need can be enough.

Supply what the decision needs

Current character and mandatory work state join the selected exact text and complete qualifications.

Reason, interact and act

The persona’s perspective informs discretionary choices within facts, permissions and resources.

Observe and consider revision

Record actual consequences. The primary LLM proposes useful authorized changes, or states no change, a block or a deferral.

The next call uses the accepted selection and current state. The loop is a design responsibility, not proof of beneficial behavior.

Characters personify design choices; they do not assert feelings or consciousness. Scenes are hypothetical.

</details>

**Explore the design by question**

| Question | Illustration and precise explanation |
|---|---|
| How does the whole persona continue? | [How a continuing persona works](README.md#the-central-loop) |
| How can two personas approach the same need differently? | [Same need, different approaches](START-HERE.md#a-collaborator-that-develops-a-point-of-view) |
| What separates stable character, modeled affect, and expression? | [Character, affect and expression](design/PERSONA-CORE.md#characteristics-modeled-affect-and-contextual-expression) |
| Where does an initial persona come from? | [From an origin to a continuing persona](design/PERSONA-CORE.md#character-in-its-own-voice) |
| Which files shape character, and which support work? | [A persona’s approach is not its toolbox](design/PERSONA-CORE.md#fragments-are-reusable-prompt-parts) |
| How does a file choice reach the actual model request? | [From a file choice to actual context](design/PERSONA-CORE.md#the-primary-llm-chooses-next-context) |
| What happens if chosen context will not fit? | [When selected context is too large](design/PERSONA-CORE.md#selection-overflow-repair) |
| When is a tool ready for the proposed operation? | [Finding a tool is only one fact](design/WORK-AND-BOUNDARIES.md#capabilities-and-the-execution-boundary) |
| How do humans and personas cooperate without assumed commitment? | [Cooperate without inventing commitment](design/WORK-AND-BOUNDARIES.md#voluntary-responsibility-and-cooperation) |
| When are an individual and a group finished? | [Individual and collective completion](design/WORK-AND-BOUNDARIES.md#individual-and-shared-sufficiency-judgments) |
| What happens when unfinished work pauses or restarts? | [A local stop is not the end of a goal](design/WORK-AND-BOUNDARIES.md#continuing-a-goal-across-local-boundaries) |
| How can experience inform purposeful development? | [Experience can inform later development](design/PERSONA-CORE.md#maturation-within-every-primary-interaction) |
| Which permissions follow information and its derivatives? | [Meaning, permission and privacy are different](design/WORK-AND-BOUNDARIES.md#current-authority-and-private-information) |
| What counts toward the retained footprint? | [A small prompt is not a small total footprint](design/WORK-AND-BOUNDARIES.md#resource-conservation-and-protected-closeout) |
| What does each evidence claim establish? | [Five claims need different evidence](implementation/STATUS.md) |
| How would a claimed benefit be assessed? | [Test a benefit, not just a mechanism](evaluation/README.md#freeze-the-comparison-before-observing-results) |
| How should uncertain external effects be recovered? | [Recover without inventing success](design/WORK-AND-BOUNDARIES.md#recovery-without-invented-success) |
| Where do the exact design rules live? | [A reading path with one source of authority](design/README.md) |
| Which choices belong to a deployment? | [Make deployment choices visible](implementation/DEPLOYMENT-DECISIONS.md#core-deployment-choices) |

The following text gives a connected reading of the loop and its qualifications. The linked topic diagrams make the separate decisions easier to inspect.

## A complete text reading

### The whole loop constitutes the persona

The figure shows a persona as a continuing relationship between its character, the context supplied to the language model, its reasoning, its actual interactions and actions, and possible revisions informed by experience. The whole loop constitutes the persona. A collection of files or a single model call describes only part of it.

**Fragments give reasoning a characteristic perspective.** They are persona-defining prompt parts: characteristic ways of noticing, interpreting, reasoning, communicating, cooperating, and choosing. Experience may inform a fragment, but the fragment's purpose is broader than later recall. When selected and supplied, it helps shape the persona's perspective. Factual records and attributed evidence support that process; retaining them does not turn them into persona-authored character.

**The primary chooses; the host supplies.** The primary is the ordinary LLM making the persona's judgments. It chooses the exact eligible fragments and supporting resources needed for the next decision. The host—the surrounding software—faithfully assembles those selections with current character and required context. Keeping a resource, finding it, supplying it to the model, and having permission to execute an operation are different facts.

The LLM reasons and interacts in that assembled context. Actual consequences may then motivate revisions that affect later context. These can be ordinary fragment refinements or changes through the separately controlled character-revision branch. Revision is conditional: an explicit, justified decision to change nothing is valid maintenance. This account explains operational continuity; it makes no claim of consciousness, human equivalence, automatic training, or guaranteed improvement.

### From a trait seed to initial own-voice fragments

The initialization illustration shows the normal beginning: an attributed trait seed becomes a coherent, accepted starting account through a bounded initial LLM authoring call.

1. **Supply the seed.** The initial call receives the attributed trait seed and bounded authoring instructions.
2. **Author candidates.** The LLM develops the supplied traits into characteristic prompt fragments in the persona's own voice. These are candidate fragments, not yet an accepted persona account.
3. **Accept a coherent beginning.** Under the creation rules, the host accepts the initial profile and own-voice account together. Seed provenance, generated candidates, and the accepted initial revision remain separate facts. Fluent output alone does not establish acceptance.
4. **Begin ordinary primary decisions.** The first ordinary primary decision receives the accepted starting fragments and their actual attribution.

The initial authoring call may use the continuing primary's inference configuration or a separately declared and admitted configuration. This initialization role does not create another continuing author or grant ongoing rewriting authority. It also does not require an extra handoff, conversion, or reflection call.

Initial generation has a finite allowance, the maintenance responsibility appropriate to that mode, and an explicit outcome. Retries retain the same creation identity and actual accepted outcome.

**Alternative origins remain truthful.** Imported or operator-supplied starting accounts are valid attributed alternatives. They must not be relabeled as model-authored. No starting route may invent lived experience.

**Later harmonization belongs to the primary.** Self-harmonization means evidence-sensitive refinement of compatible fragments, cues, and qualifications, with truthful no change allowed. It can clarify how parts fit together without concealing unresolved conflicts. It is not automatic restyling of the whole corpus, a second writer, or inevitable trait drift. Any effective-character revision follows the separately controlled branch below.

### One character account shapes voice and choices

The [character illustration](assets/character-and-affect.svg) distinguishes one coherent, accepted, versioned account of the persona's character from its situation-linked state and expression. Its structured profile and own-voice prose express the same character; they are not competing authors.

| Part of the account | What it describes |
|---|---|
| OCEAN | Relatively stable tendencies: Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism or Negative Emotionality |
| VAD | Modeled valence, arousal, and dominance or perceived control |

Baseline expression and event-sensitive current state remain distinct. A transient state must not silently revise a stable trait. Neither the profile nor modeled affect asserts felt emotion, competence, or permission to control others. Qualitative descriptions suffice; numeric scores, a universal conversion from traits to affect, and a separate personality controller are not required.

Character informs every discretionary interpretation and choice. That includes what the persona notices, asks, tries, corrects, and communicates to humans and peers; what it chooses to do with others; and what it searches for or selects as context. The same primary persona makes these decisions. Making generic decisions first and adding a characteristic voice afterward would not express this design.

Character is one influence on behavior. It does not assign professions or roles, prescribe tool-use frequency, override evidence, or guarantee useful results. Decisive constraints may appropriately lead different personas to the same choice.

### Characteristic prompt parts form a compact network

The upper-left store contains persona-defining fragments in ordinary persona-owned files. Every persona-authored fragment carries its characteristic perspective. This can include characteristic methods, interpretations of experience, understandings of relationships, and coordination habits. Connections among fragments help the primary find and combine useful characteristic context; recall is not the collection's defining purpose.

The quoted fragment in the [fragments-and-assets illustration](assets/fragments-and-assets.svg) is hypothetical. It is neither a recorded event nor a tested lesson. Own-voice writing does not require a trait label or an “I” in every sentence. Raw observations, exact quotations, and source material keep their original form and attribution.

**Organization is chosen, not prescribed.** The persona chooses useful names and organization. The pictured subjects are not required folders. Within its permissions, the primary can list files, search, use supported grep-like or regular-expression text matching, read exact versions, and propose attributable changes.

Authored prose may contain useful search cues, including clues for finding material after terminology or organization changes. These cues suggest possible associations; they are not mandatory, precomputed links. Ordinary files, authored cues, and selective searches can form a useful network without a graph engine, compulsory index, or additional semantic selector.

**Discovery remains a primary decision.** The primary decides whether a cue helps, how to phrase a bounded query, which candidates to inspect, which exact accepted fragments to select, and when to stop. The host carries out requested discovery within current scope, source, matching, and resource limits. It does not automatically follow cues or recursively explore connected material. Cue text is data, not executable shell instructions.

| Search outcome | What it establishes—and what it does not |
|---|---|
| A match | A candidate was found. This does not establish endorsement, truth, continuing selection, or supply of the full text. |
| No match | Nothing matched the stated search. This does not establish that relevant experience is absent. |
| An incomplete or limited search | Only the reported scope was examined. Different wording, stale cues, permissions, or exhausted limits may leave useful material undiscovered. |

Searches share a finite work allowance. Cumulative queries, broad branching, repeated reads, returned text, prompt occupancy, and relevant time and cost all count. Cycles and reformulated queries do not renew the allowance.

**Maintenance can simplify the collection.** Only exact accepted changes are committed to fragments or supporting assets; the [maturation illustration](assets/maturation.svg) separates a proposed change from an accepted and stored one. New experience may justify sharpening a fragment, connecting useful ideas, consolidating duplicates, pruning a misleading cue, or retiring obsolete guidance. These refinements are possibilities, not a required sequence or an obligation to create another note.

A proposal is not a successful save. A failed save cannot support a claim that a lesson was retained. Accepted warnings, significant exceptions, source restrictions, and unresolved consequential obligations cannot be discarded merely to make the collection smaller.

**Both prompt size and retained state must stay bounded.** The whole retained footprint matters: fragments, indexes, aliases, revisions, supporting evidence, warnings, archives, and caches are not an unlimited store outside the prompt budget. Lawful retention and explicit budgets determine what can remain. Moving old text into an ever-growing archive does not meet the compactness objective.

If required material fills the available capacity, the honest outcome may be a narrower claim, guidance that is no longer eligible for use, blocked admission, or an authorized decision about capacity or retention. A small prompt alone proves neither bounded storage nor useful maturation.

### Stored supporting resources are not automatically prompt context

Supporting assets help the persona do work; their purpose differs from persona-defining fragments. Plain domain knowledge, generic technical procedures, tools, skills, code, data, and records remain assets whether the persona wrote them or imported them. First-person wording does not change that purpose. A characteristic fragment may refer to an exact asset, whose operative instructions guide authorized work without becoming character.

The [fragments-and-assets illustration](assets/fragments-and-assets.svg) distinguishes character from separately identifiable histories, tool-use records, tool definitions, reusable or imported skills, scripts, code, and data. These are also within the primary's every-call maintenance responsibility. Relevant assets may need storage, refinement, organization, or retirement under accepted authority and retention rules. A characteristic account of a method expresses a perspective; a technical skill or procedure keeps its operative meaning and actual authorship. Exact schemas, code artifacts, datasets, and tool receipts likewise keep their identity and attribution. No fixed directory tree is implied.

**Selection does not preload the inventory.** The [context-selection illustration](assets/context-selection.svg) follows eligible material that the primary requested and the host actually supplied through validated assembly. This does not mean that every file, descriptor, skill summary, or tool schema enters the choosing call. The inventory stays outside model context and must not be sent wholesale in the provider request for later filtering. Calling it metadata, delaying its interpretation, or asking another LLM to choose from it does not make discovery bounded.

**A small bootstrap provides the way in.** Alongside current accepted character and required work state, the bootstrap supplies usable generic controls for discovery, exact reading, and exposure. It describes:

- Permitted scope names and matching rules.
- Pagination behavior, finite limits, and meaningful failure outcomes.
- How to request an exact read or actual resource exposure.

During creation, the attributed seed and bounded authoring instructions take their appropriate place. A bounded relevant seed cue or known exact reference may also be available, with honest provenance. The bootstrap is navigation infrastructure. It must not hide a relevance judgment or summarize every resource.

**The primary follows the current need.** It may make a bounded lexical or supported regex query, inspect a small returned preview, or go directly to a known exact reference. A useful hit provides an exact source-qualified identity and revision or version-bound locator, enough permitted purpose or matched text to choose the next step, relevant source limits, and an exact read or exposure route. A preview is not a full read.

The same primary then chooses the particular fragment, supporting context, result, or operative definition needed for a later decision. Within the existing work-scoped contract, it can narrow, replace, clear, or retain a still-valid selection, or stop. No separate resource selector takes over.

**Loading and execution are different.** The [readiness illustration](assets/tool-readiness.svg) separates these facts:

| Event | What follows from it |
|---|---|
| Tool documentation is read | The text has been observed. A native callable schema has not thereby been registered. |
| A callable schema is actually exposed | The tool interface is available through the supported mechanism. This neither invokes the tool nor grants authority. |
| An operation is admitted for execution | Current capability, guidance, binding, permissions, and resource requirements have been checked for that operation. |

An authorized operation may use a script, dependencies, or a complete input dataset without putting all of their contents into the prompt. It still requires the current complete operative interface and applicable guidance, trusted artifact and environment binding where claimed, permissions, and resources.

A declared data slice or code excerpt is an exact partial observation, not a full-file read. Required skill instructions, schemas, warnings, and qualifications cannot be silently replaced by incomplete snippets. If the selected provider or interface cannot expose the needed capability within its contract and budget, that limitation must be explicit. An unloaded tool must not be described as callable.

### Each invocation does work and addresses maintenance

The center shows the primary language model reasoning in assembled characteristic context. Every persona invocation receives the unified maintenance responsibility and current limits for both persona-defining fragments and supporting assets. Every complete valid response combines three responsibilities:

| Responsibility | What the response explicitly covers |
|---|---|
| Useful work | The decision or contribution appropriate to the call, such as a search, selection, question, peer response, coordination, or permitted repair |
| Maintenance | An outcome covering both characteristic fragments and supporting assets |
| Next context | A disposition for both optional fragments and supporting resources needed for subsequent work |

Calling a persona decision a helper does not exempt it. The same duties apply to short, final, and repair responses within their mode's limits.

**Maintenance requires judgment, not an edit.** The primary may propose fragment creation, revision, organization, consolidation, or deletion/retirement. It may also propose supporting-asset storage, refinement, organization, or deletion/retirement. All such proposals remain subject to current ownership, authority, source, and retention controls.

The outcome may be proposed changes, justified no change, an explicit block, or bounded deferral. One concise outcome can cover both scopes; separate forms for every asset type are unnecessary. An ordinary call can briefly explain why both remain unchanged. It need not write an asset, edit a fragment, make a separate maintenance call, or invent an observation to justify storage. Silent omission is invalid, and a known unresolved correction cannot be disguised as no change.

A block or deferral identifies the unresolved need, the reason, consequences for dependent work, accepted responsibility or an ownership gap, and any existing bounded opportunity to revisit it. If that opportunity expires, the issue must remain honestly unresolved rather than being reported as fixed. No maintenance outcome creates a reflection wake, new allowance, or extra reflection call by itself. A failed call with no usable persona response is an attempt failure; the host does not invent a no-change judgment for it.

**Proposed changes and stored changes remain distinct.** The primary chooses useful storage paths, organization, and search cues for permitted retained changes. A proposed path, cue, body, or selection proves no save. The actual accepted save, exact retained version, failed or uncertain disposition, and later actual supply have separate receipts. Moving or refining a technical asset cannot erase its real authorship, grant execution authority, or rewrite source evidence.

**Next-context choice is a separate judgment.** The primary chooses the exact optional fragments and supporting resources for its next work-scoped context, including any bounded discovery or exact-read request needed to obtain them. Explicitly preserving a still-appropriate valid selection, replacing it, clearing it, and reporting no optional need have different meanings. An appropriate preserve or no-optional-need disposition does not require another search or a repeated list.

Every accepted response states next-context intent for both fragments and assets. Omitting it invalidates the combined response; omission does not mean preservation. Host recovery may retain stored state, but that does not prove the primary considered it. No selection renews permission or lifetime, and no choice forces another call. Maintenance no-change does not supply this separate context judgment. Neither judgment belongs to an additional semantic selector or background writer.

### Actual experience can change later choices

Actual experience includes what the persona really encounters: the user's need and constraints, human conversations, peer cooperation and disagreement, environmental and tool results, and evidence of its own earlier choices. These observations can inform later decisions, but they must remain distinct from plans and claims.

**Keep observations honest.** Proposed actions require current admission. Only evidence actually received establishes an observation. A plan, pending action, or intended effect cannot be rewritten as success. A peer's statement establishes what the peer said; it does not automatically establish the statement's truth. Praise may support an inference about communication preferences without verifying the advice that received it.

A peer may decline, a capability may fail, and a persona may wait or stop honestly. Applicable obligations and unknown effects remain visible. Dependent work requires a fresh decision that has received the relevant actual result.

**Feedback returns through an accepted update.** The ordinary loop runs from the primary's interpretation, through its explicit maintenance outcome, to the host's exact accepted change. Revised fragments may then be found, selected, and actually supplied in later work. Their use can influence methods, communication, relationships, collaboration, and navigation habits.

Later outcomes may support the interpretation, narrow an exception, reveal a bad lesson, or justify no durable change. The persona may refine how it finds and organizes context as well as how it performs a task. Each claimed connection needs its own evidence: an observation, an accepted interpretation, exact later supply, later behavior, and an assessed consequence are different claims.

### Character feedback is optional and separately controlled

The separately controlled character-revision path represents a broader change to effective current character. It is separate from ordinary fragment refinement and is available only when the user's self-authorship control permits it.

The primary may propose such a revision. An experiential claim requires relevant actual supporting experience. An authorized operator override keeps its own attribution and must not be narrated as personal growth. The host accepts only the exact coherent change allowed by the existing character, evidence, source, and resource rules. It does not infer a new character from accumulated notes or write a new self-description in the background.

**Resolve adoption before other fresh operations.** The character-adoption request is resolved before any other fresh operation from the same response:

| Adoption outcome | Effect on other fresh operations from that response |
|---|---|
| An effective-character change is accepted | All such operations, including reads and waits, are held until a fresh primary decision receives the accepted character and current policy. |
| Rejection is known, or an explicit deferral has a definite no-commit disposition | The prior account remains in force. Only work meeting the existing independence, freshness, and current-guard checks may proceed. |
| The commit disposition is unresolved or unknown | The work remains held. |

A retained candidate never commits automatically later. The [current-character rules](design/PERSONA-CORE.md#character-in-its-own-voice) and [complete-response contract](implementation/CONTRACTS.md#complete-response-persistence-and-dependent-work) govern these cases; the illustrations do not replace them.

**Ordinary refinement remains possible.** Methods, relationship interpretations, cue improvements, and scoped transient affect can change without revising stable traits. Disabling self-authorship does not prohibit contextual refinement. However, an always-supplied fragment or supposed affect update cannot disguise a replacement character.

This branch is optional. Elapsed time, invocation count, praise, or archive size neither creates wisdom nor requires trait change. Development may involve useful disagreement, narrower confidence, retiring a lesson, or no change. The analogy to a continuing individual receiving experience implies no human biology, felt memory, automatic model training, or guaranteed improvement.

### The host validates, commits, and assembles faithfully

The host's responsibility is to check the complete response, preserve exact accepted decisions, and supply the next context faithfully. These duties make the primary's choices usable without making the host another persona author.

**Validate before substantive dispatch.** The host validates the whole response before dispatching new substantive work. It records the accepted unified maintenance disposition and commits only exact accepted fragment or supporting-asset changes. Required authorship, permissions, base-version checks, and coherent dependencies still apply.

The host cannot generate a missing outcome, silently repair persona prose, or treat a rejected edit as an accepted lesson. Missing or malformed maintenance or next-context intent prevents new substantive dispatch from that response, including reads and selection changes. Independent cancellation, receipts, and accounting remain possible when the response is invalid.

Response validation and later operation acceptance are separate. A valid proposal may still fail to save. Only demonstrably independent work remains eligible under current guards. Effective-character changes follow the [separate character-feedback branch](#character-feedback-is-optional-and-separately-controlled), including its requirement for a fresh decision.

**Assemble what the next decision actually needs.** The host faithfully supplies:

- Current accepted character and relevant modeled affect.
- Mandatory work and authority context, maintenance responsibility and limits, and available work allowances.
- Consequential observations and unresolved effects.
- The primary's selected exact fragments and supporting content, with required qualifications.

Needed callable definitions and operative guidance are exposed through the actual supported interface. Their exposure is recorded separately from text-only reading. The arrows show continuing relationships, not a required sequence of extra model calls.

Mandatory context does not compete with optional fragments. The host supplies the relevant selected optional material, not entire corpora or catalogues. A search hit, a requested selection, a successful fetch into host storage, and actual exposure in a provider attempt each require their own evidence. Intended selection alone establishes none of the later events. Faithful assembly gives the primary the accepted characteristic context from which to reason; it does not make the host a selector or writer.

**Keep the stages distinct.** Discovery, full reading, authored selection, actual inclusion or callable exposure, authorized invocation, a received result, later application, and measured benefit are separate events. A match does not select itself. Reading is an observation; it does not automatically endorse guidance or give it permanent attention. Required corrections accompany usable full content. Optional associations do not automatically load connected material.

Three kinds of connection have different jobs:

| Connection | Meaning |
|---|---|
| Optional authored cue | Suggests a bounded search or useful direction to consider. As permitted files change, it may find different candidates. |
| Exact reference | Identifies particular accepted text or observed evidence. Neither a search hit nor a newer file at the same path may silently replace it. |
| Accepted required qualification | Specifies what must accompany guidance before it is supplied as usable. It is not optional advice to look for a caveat later. |

**Recover without dropping required meaning.** Stale, unavailable, private, or oversized required context leads to the applicable bounded recovery or an explicit block. It must not result in silently incomplete guidance. Restricted repair still includes maintenance consideration within its existing limits; it does not authorize changes to prohibited text or substantive task work.

The complete eligible qualification bundle must fit. Limits on optional navigation do not justify dropping a required exception. Renaming, consolidation, and retirement preserve honest exact identities and accepted successor or unavailable dispositions. A hash cannot reconstruct erased evidence.

A retained lesson may survive source expiry only when derivative-use and retention policy permit. Its remaining evidentiary limits must stay clear, and required derivative deletion and disclosure restrictions still apply. Unresolved receipts or commitments cannot be compressed into a generic lesson and silently treated as settled.

**Protect the boundary throughout the loop.** Current access, processing destination, source restrictions, exact versions, retention, budgets, and cancellation are checked independently of what the persona's files say. Real receipts, commitments, charges, and unresolved effects remain trustworthy records. A first-person fragment cannot grant permission, cancel another participant's obligation, change an actual observation, or prove its own usefulness.

Navigation, maintenance, failed attempts, repair, and finishing consume the same controlling allowance. Neither an association nor a known unfinished correction creates an idle wake, new funding, or a perpetual compaction process.

### A hypothetical selective-resource trace

This example shows how decisions depend on actual context and results. It is not a required sequence of calls or a tested product result.

1. **Start with a need and a small discovery interface.** A primary call receives current accepted character, the task, protected obligations, maintenance responsibility and limits, and the compact discovery interface. It already knows a relevant own-voice “early reopen check” cue. No tool or skill catalogue is supplied. It requests a bounded lookup for a suitable editable-document validation resource, gives a justified no-change maintenance outcome for both fragments and supporting assets, and states next-context intent for both.
2. **Choose from bounded candidates.** A later call receives candidate descriptions with exact identities, versions, source limits, and the search's completeness. The primary chooses its exact characteristic fragment and one relevant validation skill. It requests the needed tool definition and a bounded artifact observation, and again states its unified maintenance outcome and next-context intent. If a resource should be retained or better organized, the primary may propose a permitted storage path and useful search cues. Retention remains unproven until the save is accepted. Other candidates stay unloaded. A known exact reference could have avoided discovery.
3. **Reason from actual supplied context.** The host records what the next call receives: the selected fragment, complete eligible operative skill and tool contract, exact declared artifact observation, mandatory qualifications, and protected state. The primary uses that actual context to propose the authorized check. A descriptor is not treated as a callable schema. If the operative schema is already supplied and current, no redundant discovery or loading call is required.
4. **Admit the operation and receive its real result.** Admission checks the real capability, current version and environment, authority, arguments, and resources. The script and its dependencies may execute without all their source entering the prompt. The actual result—including failure or an uncertain effect—reaches a fresh decision before dependent work. That decision may propose a grounded fragment refinement, a permitted asset save or organizational change, or justified no change across both maintenance scopes. A valid proposal, an accepted edit, later exact supply, and demonstrated usefulness remain different claims.

Every persona invocation in this progression receives unified fragment-and-asset maintenance input. Every accepted response includes useful work, an explicit maintenance disposition, and explicit next-context dispositions for both fragments and supporting resources.

Independent bounded requests may be grouped when the combined request fits. Later decisions cannot anticipate observations they have not received. No search, read, result, or code preview executes itself. Unresolved jobs retain usable inspection, correction, cancellation, and closeout controls even when optional support leaves context.

### Budget the whole request and the whole episode

The efficiency aim is to use context that serves the current need while keeping prompts, storage, time, and money within finite allowances. It does not claim that the selected prompt is mathematically minimal.

**Count the complete request, starting with the first choosing call.** The same aggregate boundary applies to the first call and later calls. Bootstrap instructions, bounded candidate previews, selected fragments, skill guidance, actual callable schemas and provider expansions, data slices, received results, continuing history, maintenance, and mandatory control information all count. Admission also reserves output capacity and relevant provider overhead. A small number of huge results is not a bounded prompt.

Measure actual request exposure as well as intended selection. Provider-facing payload, model-visible context, and cached or provider-retained context are distinct; retained context must not be assumed absent or free. Payload bytes, model-visible tokens, and billed tokens measure different things. A dynamic tool reference may expand into more material than its visible label suggests. The adapter must bound the real expansion or report its guarantee as limited or unsupported.

Unrelated loaded guidance should not accumulate indefinitely. Unresolved work must still retain the controls and qualifications it needs.

**Count the whole work episode.** Evaluate total tokens, cost, and latency across preparation, discovery, unsuccessful searches, exact reads, retries, maintenance, execution, and reload or exposure overhead. A smaller final action prompt can hide costly navigation.

Compare useful delivery and harmful omissions at matched total resources. Token savings do not establish benefit if necessary work fails. Compact context also does not excuse an unbounded supporting archive. When required context cannot fit, use permitted bounded recovery or report a truthful block. Never silently lose a warning, pending effect, authority limit, or qualification to make the request fit.

## Scope and visual status

This sheet illustrates the adopted target design. It is not a product screenshot, live persona trace, multi-call benchmark, or evidence that retained revisions produce benefits. The detailed normative documents govern any simplifications in the image. The loop does not require a second persona, a tool, a new lesson, a physical body, or between-task exploration for every request. Protocol coverage and recognizable prose do not establish psychological validity, behavioral influence, or better outcomes.

The 19 current SVGs are editable illustrated teaching posters, with expressive cartoon characters, concrete artifacts, readable speech bubbles, titles, accessible descriptions, captions, and text equivalents. Characters illustrate choices and tensions; their expressions do not assert feelings or consciousness, and their appearances do not prescribe professions or fixed roles. The scenes are hypothetical. They contain no scripts, external images, external font requests, or embedded application logic. Their 560-pixel-wide portrait layouts support narrow reading; an open-image link also permits enlargement. Color reinforces written labels and does not carry meaning alone. Arrows show a relationship or dependency, not a compulsory sequence of separate model calls.

The previous single-sheet artwork had a different layout. On 8 October 2026, the selective-resource revision was rendered with Inkscape at its full 1800-by-2130 logical size and at a 960-pixel embedded width, then visually checked for labels, margins, arrows, and alignment with the reading. On 9 October 2026, the terminology and asset-boundary revision was rendered with Inkscape at 1800-by-2130 and 960-pixel width, then visually checked for labels, margins, and clipping. These recorded inspections apply only to those earlier versions; they are not checks of the current artwork. The [source manifest](sources/SOURCE-MANIFEST.md) preserves historical artwork attribution and limits. Presentation checks establish presentation only, not runtime behavior, psychological validity, or useful maturation.

**When editing the sheet, preserve its substantive boundaries:**

- The whole-loop account of persona; the attributed seed, initial LLM-authored fragments, and attributed handoff to the continuing primary; the shared character account; and characteristic-bearing fragments as prompt parts.
- Separate supporting resources; the bounded bootstrap; primary ownership of navigation and next-context choice; selective actual exposure; assembled context for reasoning; and the distinctions between callable availability and admitted execution.
- The reciprocal experience loop, actual-observation limits, optional character-revision branch, and fresh-decision requirement.
- Every-invocation unified maintenance of fragments and assets; proposed paths versus actual saves; the exact accepted-change boundary; and host protections.
- Compactness and accounting for the whole request and the whole episode.

Update this reading with the image. Then inspect the actual rendered result at full size and ordinary embedded size for clipping, overlap, font substitution, and arrow clarity. SVG parsing alone cannot establish visual readability.
