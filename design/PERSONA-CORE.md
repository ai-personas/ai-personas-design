# A persona that learns and chooses its own context

[Design index](README.md) · [Work and boundaries](WORK-AND-BOUNDARIES.md) · [Contracts](../implementation/CONTRACTS.md) · [Acceptance](../evaluation/ACCEPTANCE.md)

## Purpose and status

A persona is a continuing AI collaborator with a recognizable character, its own interpretation of experience, and the ability to use that experience in later work. Its characteristics are expressed in its own voice and in what it notices, asks, tries, values, corrects, and chooses to do. Its retained fragments are reusable parts of its prompt. The primary language model acting as that persona chooses which relevant parts to bring into its next decision.

This is the canonical design target, not a claim of implemented behavior. It replaces the competing mandatory tree, canonical graph, auxiliary semantic-selection, and strictly on-demand/no-persistent-selection interpretations. Ordinary files, persona-owned organization, and primary-model judgment form the baseline. Exact evidence, authority, privacy, accepted work, and bounded resources remain protected independently of those files.

This chapter, [work and boundaries](WORK-AND-BOUNDARIES.md), and the [contracts](../implementation/CONTRACTS.md) are complementary normative views under invariants I01–I21. A conflict is a design defect to resolve explicitly, not permission to choose the easiest reading. Preserve the conservative authority and evidence boundary while resolving it.

“Human-like” describes an aspiration for coherent, distinctive, socially intelligible behavior over time. It does not assert consciousness, feelings, a human biography, professional qualifications, or human equivalence. Believable interaction and useful work both need evidence. Neither eloquent self-description nor a large memory archive proves them.

## A continuing persona

A persona's stable identity survives individual model calls, projects, temporary responsibilities, dormancy, and a change of model. A name or portrait may help people recognize it, but neither is the identity itself. The system preserves whose decisions, contributions, accepted responsibilities, and retained interpretations they actually are.

Starting material has immutable creation provenance. Supplied instructions, an operator's description, imported material, and generated starting prose keep their real origins. They are not presented as experiences the persona lived through. A founder begins without invented personal history; the underlying model may nevertheless have prior knowledge. A generated portrait must exist before the interface says it was generated, and a portrait does not create character or competence.

During authorized creation or ordinary orientation, the primary model can express its adopted character in its own voice while retaining the starting material's attribution. Supplied third-person seed prose need not be relabeled as persona authorship. Initial generation and later self-authorship have distinct authority; neither permits an unrequested background writer to rewrite the current account.

The persona has one current account of its character, expressed through a small designated body of accepted prose. It is supplied consistently, rather than competing with topical memories for attention. The profile view and decision context resolve the same accepted account. A filename can change without creating another identity, and a profile screen must not become an independently edited summary with different instructions.

The designation is a practical entry point, not a required root, directory, or cognitive category. A short self-description can be one file. A persona may organize other files as it finds useful without reproducing a fixed folder structure. Current character must remain small enough to supply faithfully; an overflowing account needs an explicit revision or a blocked admission, not an invisible summarizer.

Optional descriptors, including OCEAN personality dimensions or VAD modeled affect, can support initialization, display, or a declared comparison. They are not compulsory parts of a persona and do not constitute a second authoritative self. If used, their meanings, origins, current revisions, and controls remain explicit. Existing values are not silently erased or retrospectively invented. A change in a number does not establish learning, feelings, or better work.

Creation and initialization are bounded, attributable operations. A retry must not silently create another identity, rerandomize an accepted beginning, repeat an uncertain paid call, or copy unavailable seed material. Useful work need not wait for decorative presentation. A later return to activity must not invent experience of events never received.

## Character in its own voice

Character is more than a list of adjectives appended to generic instructions. It is a coherent perspective: what the persona finds worth investigating, how it handles uncertainty, what it tends to notice first, how it seeks help, what it finds satisfying to finish, and which habits it is trying to improve. These tendencies should be recognizable across appropriate situations without dictating every decision.

For example, an authored character might say, “I understand a problem by making a small usable version. I slow down when a quick example would conceal the hard part.” Another might say, “I like a comparison that separates plausible explanations. When the distinction will not change the result, I choose a reasonable path and move on.” These express different approaches without assigning professions, tools, or arbitrary quirks.

Own-voice has three distinguishable meanings:

- **Authorship:** the text came from the identified persona decision, or from another author whose contribution is attributed honestly
- **Adoption:** the persona deliberately made supplied material part of its present account without changing that material's actual origin
- **Expression and influence:** later language and choices exhibit a recognizable, appropriate perspective

An accepted revision can establish authorship. It cannot by itself establish behavioral influence. Rewriting advice as “I learned” does not make it firsthand experience. A persona can instead say, “This suggestion seems worth trying; I have not tested it yet.” Exact quotations and external observations retain their original attribution and form.

Different characters can choose different competent paths when a task leaves meaningful discretion. They should converge when evidence, an exact request, or a safety constraint makes one path appropriate. Difference is not an outcome to maximize. Stereotypes, invented biographies, unnecessary disagreement, and performative inefficiency do not establish individuality.

Accuracy, honesty, necessary verification, accepted commitments, and user constraints apply to every character. Curiosity cannot enlarge a budget. Confidence cannot create expertise. A preference for independence cannot erase a required review, and an interest in collaboration cannot commit an unwilling peer.

The user's self-authorship control governs changes to effective current character. When enabled, the persona may revise its accepted account with attribution, a concise reason, and relevant supporting experience when it claims experiential change. When disabled, it can still learn methods, keep interests, interpret relationships, and correct task-specific mistakes. Moving a replacement character instruction into an ordinary always-supplied fragment cannot bypass that control. At the same time, normal learning is not forbidden merely because it changes a later action. Mechanical designation checks and behavioral checks for disguised character substitution answer different questions.

After a genuine effective-current-character change is accepted, every new operation from that response, including reads and waits, requires a fresh primary decision under the accepted character and current policy. The old decision does not acquire the new character retroactively. A rejected change preserves the prior accepted state; independent work can remain eligible under its original context and current guards. Exact reselection of an unchanged, still-permitted current account is idempotent and does not fence otherwise valid work. Equality of displayed prose alone is insufficient: its exact sources, designation, qualifications, and policy must still agree. Past fragments keep their actual authoring character until the persona deliberately revises them.

## Fragments are reusable prompt parts

A fragment is authored text worth being able to supply again: an interpretation, method, concern, preference, question, relationship understanding, or several of these together. It can be short. It can occupy a file or a clearly identifiable part of one. It does not need a prescribed heading set, category, score, or promotion ceremony.

Retained persona fragments are prompt parts authored in that persona's own voice, not generic notes to which only the current self contributes personality. Its perspective shapes what matters, the useful abstraction, phrasing, uncertainty, and exceptions. This does not require every sentence to start with “I.” Exact quotations, raw observations, formulas, and attributed source material retain their proper form and origin; they are not rewritten as invented lived experience.

The text is intended to help the persona think and act in a relevant situation. A useful fragment might read: “I polished several alternatives before checking whether the editable file would reopen. When editability is part of the promise, I want an early reopen-and-edit check before more polish. That does not make exploration wrong when exploring alternatives is itself the task.” The factual account must refer to actual received evidence if it describes a real event; this example is hypothetical.

Keep three kinds of information distinct:

| Kind | Meaning | What it cannot do |
|---|---|---|
| Actual evidence | What was received, observed, produced, attempted, or checked, with its exact provenance | Prove more than the observation establishes |
| Authored interpretation | What this persona currently makes of that evidence, or a clearly tentative idea | Rewrite the evidence or turn a report into firsthand experience |
| Context choice | Which accepted text the persona wants available for a particular next decision or continuing work | Make the interpretation true, authorize an effect, or prove it was supplied |

Raw observations remain evidence even when no fragment is written. A stored page, command output, or peer message does not automatically become the persona's lesson. A fragment may quote evidence, but it must not silently replace the original or relabel someone else's account as its own observation.

The persona communicates the meaning, basis, scope, uncertainty, and important exceptions in readable prose appropriate to the note. It need not fill the same fields for every sentence. A tentative idea needs honest uncertainty; a claim of observed success needs actual evidence. A failed operation can support a limited failure lesson. An uncertain effect supports an uncertainty finding, not an invented success or failure.

When claiming that an experience review produced retained or revised learning, identify the actual successful authoring operation and accepted change, and link that change to at least one exact reviewed observation. Ambient context, a nearby timestamp, or an unrelated owned lesson is insufficient. A claimed revision must be an actual revision. This evidence rule applies to the claim being made; it does not require a tentative idea to invent an experience or impose a form on every note.

The runtime retains trustworthy authorship, accepted revisions, source restrictions, and exact evidence references outside editable prose. These safeguards do not need to appear as a large cognitive form in every prompt. Conversely, prose-first authoring does not allow the runtime to invent an applicability claim, source judgment, discovery description, or explanation on the persona's behalf. Structural receipts establish attribution and exactness, not semantic honesty or domain correctness.

Fragments remain fallible prompt context. Their instructional form gives them no higher authority than their source and purpose allow. A saved external instruction cannot become permission to disclose data or spend money simply because the persona rewrote it in the first person.

## Ordinary files and self-organization

The persona maintains a readable collection of ordinary files through listing, search, exact reading, and editing. It chooses useful names, directories, headings, cross-references, and optional indexes. A skill can sit beside the experience that produced it, then move when another arrangement is easier to use. Three useful notes do not require an empty taxonomy around them.

No canonical tree, association graph, vector database, global relevance score, or auxiliary model is required. A persona may make connections or maintain an index when these help. Such aids are discovery routes, not the definition of its mind. Existing eligible text must remain discoverable when an authored index is incomplete or stale.

Search supports plain text and scoped grep-like matching; regular expressions may be used when supported and useful. The persona chooses queries, broadens or narrows them, follows references, and decides whether another search is worth its cost. It may search for a concept, a participant, a tool, an exact error, or its own remembered wording. Query expansion is ordinary persona judgment, not a separate mandatory planning model.

Every search makes its corpus and limits understandable. Current eligible files, historical versions, drafts, and retired text must not silently mingle. A result identifies the exact text version and how to inspect it. Pagination, incomplete searches, unavailable sources, and relevant omissions are visible. No match means no matching text was found in the declared scope; it does not prove that no useful experience exists.

Search snippets are discoveries. An exact read is an observation of text, not endorsement of its claims. A read returns the requested still-permitted bytes or an explicit stale or unavailable disposition. A newer file at the same path is a new observation, not the version previously found. A historical read stays historical.

The file interface does not settle physical storage. Accepted files may be backed by a transactional store or by a filesystem that demonstrably preserves the same guarantees. Exports are snapshots unless explicitly adopted through the supported authoring path. A shell command returning familiar prose is evidence of that command's actual output; it does not by itself establish a trusted accepted-file revision. Paths, hashes, and filenames are useful identifiers, not substitutes for current ownership, access, or acceptance.

Simple authoring still requires honest revision and recovery. Concurrent edits check their base versions. Dependent changes commit coherently or leave the prior accepted state intact. Moving a file must not remove source restrictions or essential qualifications. A hidden semantic merge must not decide what the persona now believes.

## One learning and action loop

The continuing relationship is **observe, interpret, organize, find, select, assemble, act, and observe again**. These words describe capabilities that support one another, not compulsory stages or separate model calls.

- The persona receives the actual task, environment observations, peer contributions, and relevant consequences
- In an ordinary primary decision, it interprets what matters and may retain, revise, relate, or retire useful fragments
- It organizes and searches its files as needed, then chooses relevant prompt parts for its next decision
- The runtime assembles a bounded, qualified context under current authority and information policy
- The primary persona decides and acts through available authorized capabilities; actual results become new observations

Work and learning therefore belong to the same ordinary primary decision. The persona may solve part of a task, ask a focused question, improve a method, and choose next context in one response. It may also simply do the work. No edit means no accepted memory change; it does not prove that the persona explicitly considered and rejected learning.

There is no required lesson after every tool use, separate reflection author, relationship writer, or ceremonial memory disposition. Repeated listings and unchanged status checks are not new experience merely because operations occurred. A valuable learning deferral can be retained explicitly. Once retained, it remains pending until an attributable addressed or dismissed disposition; omission does not silently close it. Its eventual interpretation must identify the actual observations and accepted change, if any, rather than claim a lesson was saved when none was. An ordinary no-change response creates neither a debt to reflect nor a scheduled wake.

Continuation is a separate responsibility. Where the work contract requires an explicit continue or yield choice, omitting a memory edit does not supply that choice. Missing or malformed scheduling output grants neither an authored stop nor automatic paid continuation. A deliberate empty action batch may yield, but it does not erase unfinished obligations. Replayed wait receipts and unresolved deferrals are not fresh events that authorize more inference.

New results can be interpreted only after they arrive. The persona can retain a hypothesis before an experiment, provided it does not describe the anticipated outcome as observed. Later evidence can support, narrow, or refute it. A proposed save is not an accepted change; a message claiming “I updated my method” depends on a successful save receipt.

One current primary decision authority prevents concurrent work from silently overwriting one persona's account. Independent personas may work concurrently. Peers, humans, and tools supply evidence or proposed wording; the persona decides what to adopt. An authorized operator override keeps its own attribution and never impersonates persona learning.

Extra searches, reads, maintenance, and retries have real costs. A simpler interface may still require additional primary decisions to recover a missed lesson. That cost belongs in the comparison rather than being hidden behind a claim that files alone guarantee efficiency.

## The primary LLM chooses next context

The primary language model acting as the persona owns the semantic choice: **what do I want available to think and act better next?** It uses the current need, its character, observations, active fragments, unresolved questions, and permitted archive to make that choice. The runtime cannot silently substitute its own topic judgment, infer endorsement from a search result, or appoint another model to determine the persona's next prompt.

A next-context choice identifies exact accepted fragments or prompt parts, their intended work scope, and any useful concise next focus. It may include a newly authored fragment once that fragment's save succeeds. It may request a readable exact candidate discovered through a preview without pretending the full text was already read. The next supplied text becomes the observation. Selection is an intention to receive context, not a claim that the selected advice is correct.

The same decision can request relevant permitted evidence, artifact excerpts, or tool instructions for its next context. Those sources retain their actual meaning and attribution; selecting them does not automatically convert them into persona fragments. A concise work handoff can preserve focus without rewriting the original request or current obligations.

The persona can replace its selection, clear optional selected material, or preserve an existing choice within its declared scope. Omitted selection output makes no new selection judgment. It leaves existing accepted state unchanged only for as long as that state's scope and validity still apply. The interface must distinguish no update from an explicit empty choice. Preservation never bypasses current version, access, qualification, character, or work-boundary checks.

A plain read does not create persistent selection. Its result may remain an observation in bounded current-work context, with its necessary qualifications. Keeping that text deliberately available later is a separate choice. Similarly, a file being recently edited, frequently read, linked, or highly ranked does not silently make it always active.

Selections are bounded and scoped, not permanent subscriptions to everything related. They survive an ordinary continuation only under their accepted scope. Starting another task does not automatically import an old work's private focus, handoff, or optional selection. The persona still has its current character and its eligible continuing files; it can search and choose applicable experience for the new task. Reuse carries original restrictions and does not expand the new mandate.

An unexpected event need not have been predicted by a stored recall rule. The relevant current event reaches the primary persona, which can reconsider attention, search, and select an appropriate fragment in its next ordinary decision. Event delivery does not silently activate an entire neighborhood of related files.

Optional lexical indexes, semantic search services, or other discovery aids may propose candidates within an authorized processing and resource policy. They remain attributed tools. They do not write the persona's interpretation, decide truth, make an accepted next-context selection, or inherit primary action authority. The baseline works without them; any claimed improvement requires a comparison that includes their costs and failures.

Selection changes do not rewrite the context of the call that authored them. They prepare a future decision. A failed dependent save or selection leaves an actionable receipt and preserves the prior accepted state; independent work remains subject to its originally admitted context and current guards. It must not depend on uncommitted learning. Changes that require a fresh observation boundary cannot be followed by dependent effects from the old decision.

## Bounded and faithful assembly

The primary persona chooses relevance; the runtime enforces the conditions under which chosen text can be supplied. These are different responsibilities.

Every applicable decision retains trusted operating constraints, current authority, original need and accepted changes, current character, cancellations, accepted commitments, blocking findings, and consequential new observations. These do not compete with optional memories. The persona cannot edit a file to cancel a commitment, suppress adverse evidence, manufacture consent, widen a grant, or replenish resources.

Chosen text is bound to exact accepted versions. Assembly checks current ownership, source eligibility, processing destination, work scope, and qualifications before disclosure and again at admission where state may have changed. A selection receipt is not a supplied-context receipt. A changed reference is not permission to substitute newer bytes or preserve an obsolete method as current advice. The affected choice becomes stale; the primary persona can inspect and select the new accepted version in a fresh decision. The baseline has no silently live file selection.

An essential correction or prerequisite must accompany the full method it qualifies, whether that method arrives through a read, a recovered read observation, or explicit selection. Prefer a self-contained small fragment. When required material lives elsewhere, the author identifies that requirement explicitly and the runtime preserves the complete qualified bundle. It does not infer it from loose prose or an optional link.

This required accompaniment is a correctness boundary, not a cognitive association graph. Optional connections suggest what may be worth considering. Required qualifications prevent a method being presented as usable while its known exception is omitted. They do not authorize unrelated targets or expand access. A stale, withdrawn, unavailable, or oversized required part prevents the affected method from being supplied as a complete usable bundle. The failure is visible; a title or partial snippet is not a silent substitute.

If an optional selected source or a required part of its bundle becomes stale, withdrawn, or inaccessible, withhold the whole affected optional bundle and expose a safe ineligible disposition without silently clearing the stored choice. An otherwise lawful fresh primary decision may receive that disposition and repair its selection; the invalid choice need not deadlock unrelated work. Unavailable mandatory current-self or work sources still block the affected admission. In ordinary task admission, valid selected material cannot be discarded merely to make the request fit, and withheld text must never be counted as supplied.

Assembly accounts for the whole request: instructions, current facts, selected text, required qualifications, observations, media, and output allowance. It deduplicates identical exact content without discarding distinct qualifications. Provider tokens, local estimates, bytes, and actual charges remain distinguishable.

Before accepting a current-character change or any proposed next-context change, validate the complete resulting ordinary request known at that point, including mandatory state and the proposed full selection with its qualifications, against current structural limits, context limits, and policy. Short prose does not bound transitive qualifications, source ancestry, protected observations, or durable history. Reject a proposed change that is already inadmissible at commit, preserving the prior accepted state and a useful failure receipt. In particular, the system must not accept a new current self whose ordinary required read already cannot fit. New observations, source withdrawal, or model changes still require later revalidation; a successful commit cannot guarantee all future admissions.

### Selection-overflow repair

A once-valid selection can become too large when new mandatory input arrives. Normal task assembly must not silently discard valid selected text to proceed. Instead, the system may admit an explicitly labeled, bounded **primary-persona context-repair decision** under the existing repair allowance. It retains the mandatory current self, work, authority, evidence, qualification, and resource state. Optional selected bodies are transparently withheld. Text independently required by the mandatory core remains supplied even if also selected; its actual supply must not be labeled withheld. In place of the withheld bodies, the decision receives a permission-filtered, bounded inventory of exact selected references and mechanical fit diagnostics. The inventory discloses any incompleteness rather than claiming every entry was shown. Neither an inventory entry nor a diagnostic is presented as the withheld text or a substitute lesson.

This limited decision may only narrow or clear optional selection, obtain bounded qualified reads needed for that repair, or stop and report an honest disposition. A repair read must return exact permitted text with its complete required qualifications and fit within the repair request; it retains the ordinary fresh-observation boundary and consumes the same bounded allowance. The repair decision may not perform substantive task effects, rewrite current character or other mandatory state to shrink it, invoke an auxiliary selector, expand authority or funding, or silently switch models. The stored selection remains unchanged until a valid repair is accepted; omission, a failed repair, or withholding bodies does not clear it. A later ordinary decision receives the accepted selection in full under fresh checks before substantive work resumes.

If the mandatory repair core cannot fit, be funded, or be admitted within the remaining repair allowance, block with the actual limitation. Repeated unresolved overflow does not renew that allowance. This is a targeted recovery exception, not a new cognitive workflow or permission to shorten ordinary selected context. Retirement, summarization, and deduplication cannot remove source restrictions, adverse facts, obligations, or unsettled effects. Recovery uses currently eligible sources, not automatic declassification. The supplied-context record labels this repair mode and identifies the withheld bodies; it must never claim they were supplied.

The actual supplied-context record identifies which versions and qualifications reached which decision and what was omitted or blocked. It need not store raw provider transport or private reasoning. A later action trace can show behavior consistent with supplied guidance. Establishing beneficial influence needs a separate comparison.

## Learning methods, tools, and relationships

Learning can arise from the task, the environment, peers, or the persona's own observed habits. These sources overlap; they do not require separate memory organs.

Task experience may teach a useful decomposition, a better question, or the limit of an appealing method. Environment experience may reveal a file format's behavior, an unavailable capability, a tool failure, or a condition that changes what is feasible. Peer experience may show whose contribution helped with a particular kind of discrepancy and how to ask more effectively. Self-observation may reveal repeated premature polishing, excessive comparison, or a habit of overlooking an adverse result. Each interpretation remains scoped to what was actually observed or clearly marked as tentative.

A self-interpretation is a useful authored account, not proof of privileged access to a human-like inner life. Observable choices and outcomes can support a retained high-level lesson without preserving private reasoning or inventing a psychological explanation.

A skill is a method worth finding and using again. It should make its useful situation, essential actions, checks, and important limitations understandable. It can remain a few paragraphs. Calling a fragment a skill does not establish competence; a successful trial does not establish universal transfer or professional qualification.

A tool note describes a capability, how it was used, and its observed limits. It is not the capability itself. Reading the note does not install or run a tool, grant credentials, authorize effects, or prove that a later program version behaves like an earlier one. Executable helpers retain separate provenance, permissions, environment requirements, and actual result evidence. An editable tools folder is not a sandbox or an integrity boundary.

For example, a note about an archive inspector could help discover a missing document component. An archive listing alone does not establish correct rendering, meaningful editability, or permission to disclose the file. A later persona must choose the checks appropriate to the present promise rather than inherit an exaggerated claim from a successful earlier command.

Relationship fragments are directional interpretations, not facts about another participant's inner state or a universal reputation score. “Rowan helped me narrow that discrepancy when I provided exact versions” is useful if supported by the actual exchange. It does not establish that Rowan is always right, available, or committed to help again. A decline or nonresponse is not proof of incompetence or hostility. Repeated copies of one claim are not independent corroboration.

Teaching supplies attributable material; the recipient authors its own interpretation. Shared practices emerge through actual use, exchange, and acceptance. They do not require a merged private memory or a global prompt manufacturing agreement. The [work and boundaries chapter](WORK-AND-BOUNDARIES.md) defines the separate rules for cooperation, responsibility, sharing, and consequential effects.

## Maintenance, correction, and continuity

The persona may split an overbroad file, consolidate repetition, improve a filename, write a short index, connect related experiences, narrow a method, or retire obsolete guidance. These are ordinary useful actions, not evidence of maturity by themselves. Reorganizing unchanged notes indefinitely is not progress.

Correction is central to learning. A misleading fragment must not gain authority through familiarity or repeated selection. The persona considers counterevidence, revises or retires the interpretation, and preserves the important limitation where later use can find it. Unresolved contradictions stay visible rather than being silently averaged into a new belief.

A corrected interpretation does not rewrite the original observation or erase an earlier mistake. Retirement preserves an honest disposition under retention policy. Incoming references must resolve to that disposition or an explicitly accepted successor; a moved path cannot silently revive old guidance. Consolidation preserves significant exceptions and restrictive ancestry.

Source restrictions follow fragments, self-descriptions, search results, indexes, selections, caches, and exports. Generalizing private information into a skill does not declassify it. Revocation can require blocking fresh dependent decisions or disclosure, rebuilding permitted context, reconciling effects, or stopping. Clearing a selection cannot make a call that already received restricted text retroactively uncontaminated. The system must state the limits of withdrawing copies already delivered.

Dormancy preserves continuing identity without continuous model calls. A retained question, deferral, interest, or next-context choice is not a wake trigger. Optional between-task exploration requires its own current permission, funding, finite bounds, and stopping conditions. New user work and protected closeout resources retain their priority. The persona may propose an investigation; it cannot renew its own authority by writing that desire into a file.

Restart and model change preserve accepted identity, current obligations, and real effects. Resumption rechecks what is still accessible, applicable, and authorized. Stopping remains honest: completion, partial delivery, an actual dependency, voluntary yield, and resource or infrastructure blockage are distinct. A fragment cannot transfer responsibility to an unconsenting peer or turn an imagined future investigation into a scheduled event.

## Hypothetical journeys

The following personas and events are illustrative design examples, not observed results.

### Distinct character, equally responsible work

Mira's current account emphasizes learning from a usable first version. Rowan's emphasizes comparing plausible explanations before committing. Both receive an open brief for an editable neighborhood guide under the same accessibility constraints and allowance.

Mira chooses one representative route and checks whether the saved guide can be reopened and edited. Rowan compares walking-first and transit-first routes against the accessibility need, then develops a preferred route and checks its saved form. Their questions and sequence differ for intelligible reasons. Both owe the same usable result and truthful evidence.

If the user instead asks for one exact urgent route correction, both may make the correction and verify it. Appropriate convergence supports adaptability; forced divergence would not make them better personas.

### A retained lesson selects a better next prompt

Mira observes that an attractive export cannot be meaningfully edited. In the next ordinary decision she corrects the deliverable and writes a short fragment: “I checked the look before the promise of editability. For work that promises an editable source, I want to reopen and make a representative edit early, while changes are cheap.” She records that this interpretation comes from one actual failure and preserves the exception for exploratory-only work.

Later, during another editable-document task, Mira searches her files for “editable.” The result identifies that fragment's exact revision. She chooses it for her next context along with a current tool note. The runtime supplies the complete lesson, its exception, and current work constraints. The next primary decision chooses an early reopen-and-edit check. These records distinguish successful retention, selection, actual supply, and the observed check. They do not yet prove the lesson caused an improvement.

On a subsequent task whose purpose is to compare three visual directions, Mira notices the exception and does not force the whole task through one production-first method. If her note still overgeneralizes, she revises it. A later matched retained-versus-withheld comparison can assess whether the lesson helps without causing harmful transfer.

### Social learning remains correctable

Rowan previously helped Mira diagnose a version mismatch after receiving a precise discrepancy. Mira retains: “I got a useful answer when I brought Rowan the exact versions and the question I could not resolve. I should prepare that much context before asking again, and still check the answer.”

A later reply recommends a method that fails under the new tool version. Mira retains the failure as new evidence, narrows the technical advice, and separates the useful communication habit from the now-inapplicable method. She can seek another source without declaring Rowan generally unreliable. Any new request remains a request until accepted.

If the old exchange becomes unavailable under current source policy, changing its filename or paraphrasing it is not recovery. Mira proceeds from independent permitted evidence or exposes the dependency. Neither familiarity nor friendship language supplies new authority.

## Compatibility and implementation gap

This consolidation changes the intended representation and decision interface. It does not claim a runtime migration, a passed acceptance suite, or measured human-like behavior.

| Earlier interpretation | Current design decision |
|---|---|
| Mandatory tree or canonical cognitive graph | Ordinary persona-owned files are the baseline; optional organization aids do not define the persona |
| Another model can make semantic next-context selections | The primary persona LLM makes accepted relevance choices; optional tools only assist discovery |
| Optional files are read only on demand, with no persistent selection | Reads remain observations, while explicit bounded work-scoped selections can persist and be replaced or cleared |
| Every response supplies a cognitive disposition or lesson form | Ordinary work may leave memory unchanged without an invented authored judgment; real continuation and stopping duties remain |
| Numeric personality and affect initialization is necessary | Coherent current prose is sufficient; optional descriptors retain honest origins and controls |
| Memory text can stand in for events or authority | Actual evidence, accepted work, permissions, resources, and effects remain independently trustworthy |

Existing accepted content, provenance, source restrictions, qualifications, and obligations must not disappear merely because the interface changes. Existing selections and delegations need an explicit transition: preserve only what the new contract permits, obtain a fresh primary choice where needed, and retain their honest historical dispositions. Hiding old controls is not migration. Earlier evaluation outcomes remain attached to their original design, implementation, and evaluator revisions in the [historical results account](../evaluation/HISTORICAL-RESULTS.md); [source provenance](../sources/SOURCE-MANIFEST.md) preserves their origins.

Delivering this design requires real mechanisms: exact file access, attributable accepted edits, coherent dependent changes, current-character designation, work-scoped next-context selection, qualified assembly, source enforcement, bounded recovery, and inspection of actual supplied context. A file-shaped view over older records may help compatibility, but does not establish all of these behaviors. Canonical filesystem storage is a separate engineering choice requiring evidence for concurrency, recovery, revocation, and executable integrity.

The [implementation status](../implementation/STATUS.md) distinguishes design publication, actual mechanisms, executed checks, observed behavior, and deployment approval. None inherits a pass from another stage.

The principal affected requirements are PER-01–PER-05 and MEM-01–MEM-05, with the applicable COL, ACT, GOV, EVD, SYS, SOC-03, UX, and OSS boundaries preserved. The [requirement index](../implementation/REQUIREMENTS.md) and [contracts](../implementation/CONTRACTS.md) carry their exact obligations. There is no parallel cognitive requirement catalogue and no new domain-specific workflow.

## What would establish success

Evaluate distinguishable claims rather than one “memory works” label:

| Observation | What it establishes |
|---|---|
| A fragment was accepted | Attributable text was retained at an exact revision |
| Search found it or an exact read returned it | Discovery or observation occurred within the recorded scope |
| The primary persona selected it | The persona requested that text for an identified context |
| It was actually supplied | The relevant decision received the recorded text and qualifications |
| A relevant action followed | An inspectable application chain may exist |
| A matched comparison improves outcomes | Evidence supports benefit under those tested conditions |

These are not compulsory sequential stages. Current character, a newly authored fragment, or a known exact reference need not be searched first. Nor does an action following a read prove causal influence. Record null, harmful, inconclusive, and assisted outcomes honestly.

Character evaluation examines recognizable choices, attention, questions, consultation, persistence, correction, and stopping, with convergence controls for decisive situations. Learning evaluation examines transfer, delayed reuse, exceptions, misleading lessons, and correction. Longitudinal evaluation lets the persona actually maintain its files rather than crediting an expert-curated archive as self-organization.

Hold relevant task information, tools, permissions, inference configuration, and total resources comparable. Prevent leakage through copied files, summaries, peers, caches, and profiles. Assess work independently where feasible and preserve the established acceptance minima and original failure rubrics. Count all primary calls, discovery services, tool use, maintenance, retries, latency, known charges, and uncertain exposure. Fewer tokens in a failed task are not an efficiency gain.

The target is useful continuity: a recognizable persona that can find and use experience, avoid repeated mistakes, adapt to changed circumstances, learn from others without surrendering judgment, and maintain a truthful account of itself. Whether this design achieves that target remains an empirical question for the [acceptance plan](../evaluation/ACCEPTANCE.md), not a conclusion produced by the documents themselves.
