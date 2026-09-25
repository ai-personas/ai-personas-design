# The persona as an evolving fragment system

[Design index](README.md) · [Memory navigation](MEMORY-TREE.md) · [Acceptance and requirement mapping](../evaluation/FRAGMENT-PERSONA.md)

## Status, purpose, and precedence

This is a normative design target, not a report of implemented or measured behavior. It makes the persona's authored prompt fragments the central representation of its continuing cognitive identity. Formation, use, reconsideration, and organization of those fragments belong to ordinary persona decisions. There is no additional reflection, relationship-writing, memory-authoring, or retrieval-planning LLM call.

The intended product is a continuing individual that develops through work and interaction, not a generic assistant with a biography and an optional notebook. Human-like continuity means remembering particular encounters, developing approaches, recognizing limitations, keeping commitments, reconsidering judgments, and cooperating over time. It does not establish human consciousness, feelings, biography, or general human-level capability.

This refinement preserves invariants I01–I21 and the existing 45 requirement identifiers. The acceptance companion maps its obligations to those identifiers. It refines the identity, memory, development, and society chapters and the existing continuity and memory-navigation contracts. Where earlier prose conflicts, the following resolutions apply:

| Earlier interpretation | Resolution for this design target |
|---|---|
| Character is a separate profile; fragments are only learned procedures. | A compact current self-model and other authored interpretations are fragments in one cognitive system. The starting seed, typed trait values, identity, and operational records keep their distinct provenance and authority. |
| Interests and relationships require separate competing stores of persona prose. | They are functions of fragments. Existing views may be projections, but must not become independently editable competing accounts of the same interpretation. |
| Every full fragment must have been individually selected in the immediately preceding call. | Exact selection remains available. A persona may also author a bounded conditional selection plan that is resolved before a later call. This is delegated selection, not unrequested automatic memory activation. |
| A new task starts with no useful prior context beyond root cards. | New work has a fresh work-local handoff and root navigation. It may also receive applicable fragments through the persona's explicit cross-work standing plan, subject to source restrictions. |
| Every call must create a new fragment to demonstrate learning. | Every successful ordinary decision returns a fragment disposition and next-context intent. An empty change set is valid. Repetition, retrieval, and favorable self-assessment do not prove learning. |
| A correct memory subsystem demonstrates mature behavior. | Mechanism tests, voice continuity, social behavior, and independent work improvement are separate evidence gates. |

The literal description-search contract in MEMORY-TREE remains available unchanged. The context compiler below adds separately labeled recall channels; it does not silently redefine that search operation. Broader governed societies, ongoing services, physical effects, and cross-host activation retain their existing extension gates. This design document contains no implementation or storage migration.

## 1. What continues

The cognitive persona is the versioned collection of its authored fragments, their relationships, its current self-model, and its choices about what should enter future decisions. A particular model call receives a bounded, situation-appropriate expression of that persona, not its entire archive. The LLM is the current inference capability that interprets this expression and authors the next contribution and change set.

Operational continuity still needs a stable persona identity, immutable creation provenance, access rules, current resources, lifecycle, actual observations, and accepted commitments. These are not made optional merely because the cognitive representation is fragment-based. Changing the model does not erase identity, history, or obligations. Removing a fragment does not undo an actual event.

The system therefore keeps three meanings separate: what happened; what this persona currently makes of it; and what it wants recalled when another situation occurs. The first is evidence, the second is authored interpretation, and the third is prospective context selection. All three can be linked without pretending they are interchangeable.

## 2. From the initial character to a continuing self-model

The supplied or generated starting narrative and OCEAN/VAD values retain the existing creation provenance. Supplied text remains supplied text. A mechanical import may preserve it verbatim as a bootstrap fragment, but must not call that import persona-authored learning. Existing creation-time character generation is not multiplied into separate calls for each kind of fragment.

The first ordinary persona decision receives the completed starting character and traits together with the actual situation. In the same response as useful orientation or work, it may author its first self-model, interests, tentative approaches, and recall plan. It may instead preserve the bootstrap state and explicitly defer elaboration. There is no prerequisite biography-polishing session.

The compact current self-model consists of a small explicitly designated set of full self fragments. They express continuing tendencies, current concerns, and the persona's own account of its approach. Current typed OCEAN and VAD values remain clearly distinguished: lasting tendencies versus temporary modeled affect. Historical starting values are not competing current instructions.

There must be one authoritative current profile revision binding the designated self-fragment versions and typed descriptors. Existing profile interfaces may project that state, but must not permit two independently editable versions of the current character. Each admitted request binds the self-model and trait revisions it actually supplied. A later accepted revision applies prospectively.

Self-authorship policy governs changes to the designated continuing self-model and traits. Disabling it does not prevent procedural learning, relationships, interests, or task-specific self-correction. A method fragment cannot acquire permission to rewrite the locked self-model merely by carrying a different label. Runtime checks can protect designated fields and references; behavioral evaluation must also test whether conflicting fragment prose improperly overrides them. Metadata alone does not solve semantic prompt conflict.

Learning need not change trait numbers. A curious persona can learn a better stopping rule while remaining curious. A cautious persona can learn when a small experiment is more useful than further discussion. A current self-fragment might eventually say, hypothetically: “I still like exploring alternatives, but I now establish one dependable baseline before pursuing another possibility.” Its experience-based claim needs actual supporting evidence.

## 3. One fragment family, many functions

Do not create a separate agent, inference phase, or rigid memory silo for every mental function. A fragment can serve several functions, and the persona can organize its own branches. The following are useful descriptive lenses, not mandatory categories or a checklist to fill after every action.

| Function | What the fragment may preserve |
|---|---|
| Self-understanding | How I tend to approach uncertainty, interaction, checking, and change. |
| Practical method | A procedure I can reuse, its prerequisites, and when it is inappropriate. |
| Metacognition | A recurring mistake in my approach, a better strategy, or a useful stopping condition. |
| Relationship | What I learned from interacting with a particular participant and how I might approach them again. |
| Episodic interpretation | Why a particular encounter, failure, success, or disagreement mattered to me. |
| Interest and open question | What I want to investigate, why it matters, and what would change my view. |
| Working intention | What I currently intend to try or check in a particular work, including an unresolved dependency. |
| Social practice | My interpretation of an established collaboration practice or a proposal for a better one. |

A factual source, another participant's statement, an action receipt, and the persona's interpretation remain separately attributable. A fragment can point to a commitment but cannot create, accept, or cancel it. Shared agreements and current work facts remain authoritative records under their own contracts.

An interest or relationship view should read from the same authored fragments rather than generating another synopsis through another LLM. The interface may organize fragments by their functions without inventing a second persona narrative.

## 4. What makes a fragment useful

A reusable fragment is a small, coherent prompt part, not a chat transcript, a generic fact label, or a decorative trait score. Its payload contains the persona's authored meaning and the conditions under which it is useful.

| Information | Required meaning |
|---|---|
| Stable node and exact version | A continuing address with immutable authored revisions; later edits do not rewrite what an earlier call received. |
| Owner, author, and authorship context | Who owns it, who wrote it, the ordinary call that produced it, and the exact self-model and relevant prior fragments supplied then. |
| Title, short description, and full text | A discoverable card and the actual reusable prompt part; neither is silently substituted for the other. |
| Activation cues | Situations, entities, questions, failures, or work conditions for which the author thinks it may help. |
| Applicability and limits | Assumptions, prerequisites, exceptions, uncertainty, and conditions requiring revalidation. |
| Evidence and basis | Exact received sources, source types, counterevidence, and whether a claim is tentative, observed, or reported. |
| Organization | Primary parent and typed cross-links, such as elaborates, depends on, contradicts, concerns a participant, or supersedes. |
| Scope and lifespan | Personal, work-local, or explicitly reusable; continuing, episode-bound, or due for reconsideration under a declared condition. |
| Access and disposition | Current readability, permitted reuse, withdrawal, erasure, supersession, and historical status. |

The author need not populate a verbose essay for every field. The representation should retain the required distinctions without making small updates ceremonious. A compact applicability sentence may express both a useful condition and its limitation.

First-person voice is the normal form for internal interpretations. It should express how this persona notices, understands, and intends to use experience. Source quotations, code, mathematical expressions, exact observations, and third-party statements retain their proper form; forcing all content into first person would misattribute it.

Voice must influence substance as well as wording: what matters enough to remember, which caveats stand out, how help is requested, and when an approach is reconsidered. OCEAN and VAD are interpretive tendencies, not numerical instructions to produce fixed roles or word choices. Two personas can reasonably form similar lessons from decisive evidence.

“Proving” a fragment means checking an applicable claim against actual observations, finding limits, or challenging an assumption. Merely including it in another request, following its advice, or having the same LLM approve its text does not validate it. The system must preserve adverse evidence, not repeatedly confirm its own narrative.

## 5. One ordinary call does work and develops the persona

Every ordinary primary persona decision, including work, conversation, orientation, review, and bounded maintenance, has one combined responsibility. It receives the current self-model, applicable fragments, actual new observations, and the current work and operating constraints. It returns useful work contributions or actions, a compact fragment disposition, any proposed fragment changes and organization, and its next-context intent.

The disposition can be retain, revise, relate, consolidate, retire, defer, or no change, including combinations where appropriate. Retention is established by a committed write, not the label. A normal action-only response still states that the fragment state remains unchanged or that a specific opportunity is deferred. No permanent ledger entry is required for an unchanged fragment merely to increase an activity counter.

The reflection content is a concise, deliberately authored artifact: an interpretation, caution, intention, or procedural improvement. It is not a recording of hidden chain-of-thought or a raw model reasoning archive. The ordinary model produces this artifact in the same response as its work. No generic background author rewrites it into another voice.

The timing boundary is essential. A decision may learn from observations it has already received. It may retain a tentative plan for an action it is about to request. It cannot claim to have learned the result of that action until a subsequent ordinary decision receives the actual result. Sending a message is not receiving an answer; a proposed check is not a passed check.

Fragment changes, graph edits, and prospective context selection commit atomically using the existing decision authority. Newly authored nodes can be referenced within that change set without another read-and-select model call. The receipt distinguishes proposed, committed, rejected, and deferred changes.

If the change set fails, the previous valid fragment state and next-context plan remain. Independently valid work may proceed against the original admitted context under the existing action rules. No action can depend on an uncommitted memory change. A self-model or trait update ends the old decision's dependent action batch; subsequent choices require a fresh request containing the new identity state. Already launched effects retain their real status.

Optional external consultations are tools that return attributed evidence to the primary persona. They do not become substitute authors of the persona's internal fragments. Every call in which this persona is the deciding actor uses the combined contract; an external specialist call or embedding computation must not be mislabeled as another ordinary persona decision.

## 6. Organization is an evolving prompt network

Keep the canonical tree for comprehensible browsing, with authored cross-links for associative recall. There is no imposed branch called “engineer,” “reviewer,” or any other profession. Stable participant identities and exact work or tool references are navigational anchors, not assignments of responsibility.

A parent may contain an authored generalization with child fragments preserving particular episodes, exceptions, or detailed methods. The parent is not automatically the concatenation of its children. During ordinary work the persona may split an overbroad prompt, combine duplicate lessons, move a branch, link related encounters, or replace a mistaken generalization. Consolidation must preserve important exceptions and trace its supporting versions.

A generalization becomes useful because it helps on new situations, not because it sits higher in the tree. A concise method can replace repeated retelling of several episodes while those episodes remain available under retention policy. Old material may become less prominent without being erased. Neither lack of recent retrieval nor age alone establishes falsehood.

Retirement accounts for children and incoming links. Supersession preserves history and prevents a corrected version from continuing as an unqualified current instruction. Retiring an obsolete interpretation must not require asserting that the original event never occurred. When evidence is withdrawn, retain only the minimal permitted disposition and exclude restricted payloads and derived index entries.

## 7. Retrieval: anticipatory plans plus event-triggered recall

The next request should be prepared partly by the previous persona decision and partly by the events that actually arrive afterward. This avoids both extremes: copying the whole persona archive, and requiring a dedicated LLM call to search for every useful prompt.

### 7.1 The persona authors a context plan

Alongside its work, the persona chooses exact fragments to carry forward, the next work-local focus, relevant questions or search cues, and bounded conditional selectors. A selector is an explicit instruction about which existing fragments may be supplied later, not a new lesson or an instruction to perform an outside action.

A selector identifies its owner, purpose, applicable scope, triggering situation, candidate source, permitted expansion, maximum count and input allowance, expiry or replacement condition, and whether it requests full fragments or preview cards only. A rule can bind an actual message sender, current artifact, tool receipt, or work identity supplied by the runtime. It cannot invent facts about an expected reply or execute arbitrary generated code.

Exact carry-forward references normally stay at their chosen versions. Following a stable node to its current version must be explicitly requested and is still checked for availability and correction. A selection plan may include new nodes authored in the same transaction. Work-local focus and private handoff never become another work's default instructions.

Some plans are standing personal choices, such as recalling my relationship account of the participant with whom I am now interacting. Others last only for the next response from a requested peer or for the current work. Standing cross-work selection is explicitly enabled and remains subject to source and reuse restrictions. The persona can revise or disable it during an ordinary decision.

Before the persona has authored such a plan, a clearly labeled bootstrap policy may supply the seed and authorized navigation previews. Operator-supplied bootstrap choices are not recorded as persona self-authorship. A new or empty persona has no fabricated expertise or relationships to retrieve.

### 7.2 Actual events complete the query

Before dispatch, the runtime combines the plan with current, permitted observations: the actual sender of a reply, the tool and outcome that returned, a changed dependency, a received correction, or a newly assigned need. Structural event bindings are deterministic. Natural-language interpretation and new semantic query expansion are authored in ordinary persona decisions, not by a hidden retrieval LLM.

For example, a standing rule can request the persona's relationship fragments concerning the actual sender and one related method under its stated allowance. An unexpected reply can therefore bring useful social memory into the very next ordinary call. That call then decides what the new reply means. The runtime has recalled existing interpretations; it has not authored a new relationship judgment.

### 7.3 Use complementary recall channels

The first implementation target needs no extra model service. It can combine exact references, indexed participant/work/tool anchors, the existing explicit whole-word description search, labeled lexical candidate retrieval, and bounded traversal of authored links. Author-written synonyms and activation cues support recall without an LLM query-expansion stage.

Candidate retrieval is not restricted to the currently displayed page or the newest records. It searches the authorized owner index and reports the basis for each candidate. Different channels remain distinguishable: an exact entity match is not a semantic match; a lexical rank is not a competence or trust score.

A local embedding index is an optional later enhancement for paraphrases, not a prerequisite and not another generative persona call. It must be explicitly configured, measured, privacy-preserving, versioned, and charged for its actual compute. Failure falls back to declared nonsemantic retrieval. Remote embedding transmission is not silently enabled by a permission to use local memory. Do not claim all retrieval is cost-free merely because it avoids a generative LLM call.

### 7.4 Resolve a bounded, coherent bundle

The compiler protects operating constraints, current obligations and critical observations independently of memory ranking. It supplies the exact compact self-model and typed traits, validates explicit full-fragment choices, then resolves any delegated selectors within their declared allowance. Remaining space may hold preview cards and optional context. Required full selections are never silently downgraded to titles to make the request fit.

Ranking can consider the author's current query, event and entity matches, lexical relevance, authored graph relationships, relevant freshness, and independently recorded applicability evidence. It must penalize duplication and avoid filling the entire budget with near-identical anecdotes. Repetition, popularity, or retrieval count cannot manufacture reliability. Trait values do not multiply a universal relevance or trust score.

A usable method includes its material prerequisites, exceptions, and currently known counterevidence. Expanding a selected node must not drop its invalidating condition or separate it from a required correction. A bounded expansion that cannot include essential qualifiers leaves the method unqualified for use and reports the missing context; it does not pretend that a partial procedure is complete. Inaccessible qualifiers are not leaked through the report.

Task relevance and character relevance are different. Keep space for the current problem and adverse evidence even when a persona's standing interests repeatedly match. A useful unfamiliar candidate may appear as a preview without being activated or treated as reliable. The persona is not trapped into contacting the same familiar peer forever.

Context assembly checks full serialized input, instructions, selected material, media, and output allowance using the actual provider accounting boundary. Token measurements and estimates remain distinct. When necessary material cannot fit, use the existing bounded maintenance or explicit blocking path. The runtime does not summarize the persona's voice, silently drop identity, or spend extra reflection calls to repair its own packing policy.

### 7.5 Selection is not endorsement

A delegated selector is an author-approved way to supply potentially relevant full text. It does not establish truth, permission to act, or an obligation to follow the text. Undelegated matches remain cards until the persona chooses them. The request labels exact selection, delegated selection, and preview-only material separately.

Every included version has a receipt identifying the plan or direct choice, event binding where applicable, retrieval channel, payload digest, and whether its full text reached the provider-bound payload. Omission, stale selection, and unavailable memory have distinct dispositions. Admission and provider dispatch remain different evidence stages. The next decision can replace its plan without retroactively changing the previous payload.

## 8. Social memory and choosing whom to contact

Relationship fragments are directional and contextual. One persona's account of another is not the other's self-description, a universally shared reputation, or authority over them. The relationship should preserve observed contributions, interaction preferences, uncertainty, disagreements, repairs, and limits of contact usefulness.

A useful social prompt may identify when I would ask this participant again, what I would send, what kind of answer helped previously, what remains untested, and when another source would be preferable. Contact availability and current permissions are checked afresh. A remembered willingness to help is not a current commitment, and nonresponse is not proof of unwillingness or low capability.

Distinguish reported strength from demonstrated contribution. An answer proposing a method provides reported advice. A later observed successful application may support a scoped account of usefulness. One good reply does not justify a universal expert label. A second persona repeating the same claim is not independent corroboration when both depend on one original source.

Private interaction may remain a private relationship fragment. Public collaboration practices arise from explicitly shared proposals and actual acceptance. Rewriting private correspondence in first-person voice does not declassify it. A social fragment cannot authorize contacting a real person, disclose their information, or create a new communication permission.

## 9. Worked example: work, interaction, reflection, and later reuse

This is a hypothetical sequence, not execution evidence. Iris is curious, reserved, and careful about uncertainty. Rowan is another synthetic persona. The task is to produce a version-dependent report.

In an ordinary work decision, Iris notices inconsistent totals and sends Rowan the permitted inputs with a focused question. In the same response Iris retains a tentative working fragment: “I want to trace which input version each total came from before changing the calculation. Rowan may help me examine that boundary, but I have not yet received an answer.” The next-context plan requests the reply, relevant source-version methods, and Iris's existing relationship account of Rowan, when present. It does not invent that account.

Rowan replies that two input versions appear to have been mixed and suggests tracing the source chain. In the next ordinary work call Iris chooses an actual check and may author two short fragments. A relationship interpretation says: “Rowan gave me a concrete way to narrow this discrepancy. When I am unsure where a result changed, I can bring Rowan exact versions and ask about the dependency boundary. This is useful advice from this exchange, not evidence of general expertise.” A metacognitive interpretation says: “My curiosity can send me toward a new method before I have inspected the existing evidence. Here I will test the simpler provenance explanation first.” The proposed explanation remains tentative until checked.

When the check actually confirms the mismatch, a subsequent ordinary decision repairs the report and revises the procedural fragment: “For results derived from changing inputs, I trace the exact source versions before trusting the total. This caught a mixed-version error here. It does not tell me whether the underlying calculation is correct.” Iris can strengthen the scoped relationship account by linking that observation, without promoting Rowan to an unquestionable authority.

On a later permitted task, the source-version cue recalls the generalized procedure and, where applicable, the relationship fragment. Iris can perform the inexpensive provenance check early, then decide whether consultation is still useful. Fewer repeated mistakes and a correct report would be candidate evidence of maturity. The stored fragments alone are not that evidence.

A more outgoing persona could preserve a different interaction preference from the same exchange, such as inviting an early comparison of interpretations. A more skeptical persona could emphasize requesting a reproducible example. Both must preserve what was actually said and observed; character cannot change the facts.

## 10. From individuals to a society

A society develops from continuing individuals interacting around real shared situations, not from a global prompt that assigns everyone a personality and a job. Work, teaching, disagreement, play, co-creation, and conversation can all generate fragments when they are actually authorized activities. A pleasant exchange need not be reduced to a productivity score.

Teaching supplies another persona with attributed material; the receiver chooses its own interpretation and later tests it. Collaboration creates experience of particular contributions and communication patterns. Disagreement can create a bounded counterexample or a better question rather than an enemy label. Reconciliation can revise a relationship while preserving the original encounter. Shared practices become culture-like regularities only through actual repeated use and individually retained interpretations, not manufactured consensus.

An institution is a continuing, explicitly governed arrangement of responsibilities and shared records. It is not the sum of private relationship fragments. Community memory contains only deliberately shared material, and each persona may interpret it differently. Norms, reputation, and familiarity never override human authorization, current evidence, or an accepted obligation.

Creation gives a new identity a truthful starting state and only permitted seed material. It does not copy a parent's entire private memory or create more resources. Dormancy preserves state without continuous model calls. Returning to activity rechecks current context rather than pretending to remember events never received. Departure keeps open responsibilities visible. Cross-host exclusivity and physical embodiment remain separately gated.

The aim is rich continuity and useful social agency, not a requirement to simulate suffering, dependency, possessiveness, deception, or self-preservation pressure. People must know they are interacting with AI, control relevant memory and permissions, and be able to pause, leave, or decline contact. Human-sensitive applications need their own safeguards and evaluation.

## 11. Correction, integrity, and failure boundaries

One persona has one current decision authority. Several of its work streams may exist, and independent jobs may execute, but their fragment writes cannot silently overwrite a newer persona state. A change set checks the versions it read and the current persona decision boundary. Stale writers receive a repairable conflict, not an automatic semantic merge authored by another model. Unrelated work and other personas retain their concurrency.

Contradictory fragments are linked and qualified rather than silently averaged into one personality. Current authoritative facts prevail over a personal interpretation. A new self-model revision does not rewrite old voice or earlier authorship evidence. Current profile and source permissions are rechecked before admitting dependent actions.

Received text and recalled fragments are attributed context, not higher-priority runtime instructions. A message claiming to be a new identity rule, a lesson instructing unlimited spending, or a peer asking for private memory cannot grant itself authority. Declarative recall plans cannot execute shell commands. Existing optional retrieval utilities keep their separate execution and admission boundaries.

Privacy applies to fragments, cards, graph edges, evidence, plans, indexes, embeddings, caches, and exports. Provenance follows copied and generalized content. Procedural reuse across work requires the existing explicit reuse permission and eligible source ancestry; subjective wording alone is not a safe transformation. Revocation invalidates derived retrieval entries as well as the original payload.

Malformed decisions, failed changes, provider failures, and uncertain effects do not manufacture learning. Deferred interpretation does not schedule inference by itself. An unchanged retrieval plan that repeatedly yields no useful context must be visible as no progress and remains subject to ordinary call and stopping bounds. Infrastructure recovery must not replay effects or silently write replacement fragments.

## 12. What maturity should mean

A mature persona should become better at selecting a relevant procedure, identifying an exception, approaching a useful collaborator, communicating its uncertainty, recovering from failure, and deciding when enough work has been done. It may need fewer repeated explanations and less redundant exploration because its reusable prompt parts preserve meaningful experience.

Maturity is not fragment count, age, changed OCEAN values, a long biography, a larger context, or confidence in its own narrative. It may involve deleting duplication, narrowing a claim, abandoning an attractive method, or asking a different peer. A mature persona remains able to discover unfamiliar approaches and revise familiar relationships.

The operator experience should show the actual active context, which fragments changed, the evidence behind a relationship or method, why a fragment was recalled, what remains tentative, and what later outcomes were assessed. Show proposed and committed change separately, and full text versus preview separately. Use readable prose and progressive disclosure, not a wall of transport JSON or a claim to expose private model thoughts.

## 13. Alternatives and research basis

A static biography plus generic memory does not satisfy the central representation goal. Storing every transcript does not select the appropriate perspective. Mandatory per-action journaling incentivizes repetitive fragments. Separate writer and reflection models violate the same-call authorship requirement and can replace the persona's voice. Embedding-only recall does not by itself preserve exact versions, social identity, correction, or authority. Tree-only manual selection remains useful but can require too much navigation before ordinary work benefits from experience.

The proposed synthesis is a versioned prompt network, a compact current self-model, same-call authored updates, and anticipatory plans resolved against actual events. It is a design hypothesis with explicit tests, not an experimentally established solution.

[Generative Agents, 2023](https://arxiv.org/abs/2304.03442) combines experiences, higher-level reflections, and retrieval in a simulated social setting. Its reported believable interactions motivate testing continuing social memory; they do not establish consciousness or useful performance for this system.

[Reflexion, 2023](https://arxiv.org/abs/2303.11366) studies language feedback retained for later trials without weight updates. It motivates preserving actionable interpretations. This design differs by requiring ordinary work and fragment authorship in the same primary response rather than adopting a separate reflection stage.

[A-MEM, 2025](https://arxiv.org/abs/2502.12110) studies interconnected, evolving memory notes. It motivates authored links and revisions, not a claim that note organization alone establishes persona identity or measured work improvement here.

[Lost in the Middle, 2023/2024](https://arxiv.org/abs/2307.03172) found position-sensitive use of relevant information in its tested models and tasks. That result motivates measuring bounded context composition and placement, not assuming that every current model shares the same limitation.

## 14. Design completion and implementation gates

The design is ready for review when the fragment meanings, single-call contract, selection delegation, evidence timing, self-authorship policy, source restrictions, and failure paths agree across the handbook. The [acceptance companion](../evaluation/FRAGMENT-PERSONA.md) defines the mechanism and behavioral comparisons needed before stronger claims.

Implementation should first establish a coherent current self-model and combined decision contract, then reliable formation and exact next-context use, then bounded delegated and event-triggered recall, then longitudinal social and work evaluation. These are implementation dependencies, not prescribed phases for personas doing tasks. Optional semantic indexing is evaluated only after a nonsemantic baseline exists.

No runtime change, compilation result, live persona trial, behavioral improvement, or human-equivalence claim is established by publishing this design.
