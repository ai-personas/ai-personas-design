# Persona-owned identity and skills through a simple file interface

[Design index](README.md) · [Current fragment design](FRAGMENT-PERSONA.md) · [Contribution guide](../CONTRIBUTING.md)

## Status and proposed decision

**Proposed design alternative, 6 October 2026.** This document recommends a smaller persona-facing authoring and retrieval model. It does not replace the current normative fragment graph, change the requirement catalogue, report an implemented feature, or claim an evaluation pass. Adoption belongs to the repository's authorized maintainers.

The notebook presents named prose documents through list, literal search, exact read, and edit. Accepted edits become current state; exports are snapshots. The initial compatibility pilot keeps the existing transactional store and authoring contract. The proposed writable target removes compulsory memory bookkeeping and reads optional files on demand. Canonical host files are a separately evaluated storage option.

The reviewed design baseline is [revision 673d797](https://github.com/ai-personas/ai-personas-design/tree/673d797780e3fb808739cd668e0f8ae3d914e1b9). Current obligations below describe that baseline, not a deployed-runtime audit.

Make the persona's own accepted first-person fragments its authoritative current account of who it is: what it values, notices, prefers, questions, and has learned to do differently. Let it maintain that account and reusable methods through a few readable files and scoped list, search, read, and edit operations. Start with grep-like text search. An optional semantic selector, association graph, fixed cognitive taxonomy, or separate reflection writer should not be prerequisites for this experience.

Keep exact revisions, actual observations, source restrictions, current permissions, commitments, resources, and effects trustworthy outside the prose the persona can rewrite. The compatibility pilot, simpler authoring contract, and physical storage choice are separate decisions.

The proposal addresses three questions independently:

| Question | Recommendation |
|---|---|
| How does the persona work with its continuing account? | A short current self and ordinary named files, with direct reading and editing. |
| What must the persona author? | The meaning, scope, uncertainty, and qualifications in its own prose; no compulsory cognitive form. |
| Where is accepted state stored? | Initially retain the existing transactional store. Choose another backend only on evidence. |

The middle recommendation is a substantive contract change. Existing structured authoring judgments cannot simply disappear behind a file-shaped interface while an adapter invents their meaning.

## 1. The goal is authored continuity that changes behavior

A persona should be able to develop a recognizable perspective through ordinary work. It might discover that an early usable version helps it think, that it overvalues elegant comparisons, or that it asks better questions after isolating a discrepancy. It should retain the interpretation it actually makes, revise it when experience challenges it, and choose when a method deserves reuse.

These fragments define the intended continuing persona rather than merely decorating a generic assistant with a name. Their realization is still empirical: the model, current request, received evidence, available context, tools, and permissions all affect the next decision. A trustworthy system must establish whether its identity specification actually influences attention and action, whether that influence is appropriate, and whether retained experience helps.

The [current design](FRAGMENT-PERSONA.md#1-what-continues) already makes authored fragments central and already permits operation without Jev, the optional semantic recall selector. The proposed change is therefore not the discovery of self-authorship. It reduces what a persona must manipulate to maintain itself, and tests whether useful behavior survives without optional cognitive machinery.

Success would mean a persona maintains concise, attributable, qualified files on its own; finds relevant experience without an expert curating every retrieval; changes competent choices for intelligible reasons; and corrects harmful generalizations. More files, more edits, distinctive phrasing, or fewer selector calls are insufficient.

## 2. Current identity and its boundaries

The proposed target uses one authored `self.md`, supplied in full in each ordinary decision. It is exact accepted prose, never another model's personality summary. The profile display and decision context resolve the same current self revision. Starting material retains its original attribution, distinct from later self-authorship.

The compatibility pilot can expose existing designated sources as one exact ordered view. A composite is not blindly writable: edits identify the affected source or explicitly consolidate and designate a new account. Consolidation preserves source attribution and restrictions. New personas need not encounter multi-source assembly merely to describe themselves.

Separately, this proposal recommends evaluating descriptor optionality: prose is the minimal current identity, with numeric descriptors an optional comparison mode. That avoids two compulsory accounts of who the persona is, but gives up independent numeric controls and modeled-affect continuity. Optionality is a proposed adoption choice, not approved retirement or an automatic consequence of files.

Until adopted, the compatibility pilot retains current OCEAN dispositions, the five-factor personality descriptors, and VAD, modeled valence, arousal, and dominance, under the [development contract](PERSONA-DEVELOPMENT.md). Supplied values and their controls keep their true provenance; neither a later prose account nor optional mode erases that history. Any changed character evaluator needs explicit criteria and preserves earlier results under their original meaning.

Three meanings of own-voice need separate evidence:

- **Authorship:** the accepted text came from the identified persona decision or attributed outside author.
- **Adoption:** the persona deliberately made supplied material part of its present account, with its actual origin preserved.
- **Expression and influence:** later language and choices exhibit a recognizable perspective in appropriate situations.

A revision receipt can establish the first. It cannot certify the third. Rewriting advice in the first person does not turn it into firsthand experience. A persona can adopt an idea while saying it is untested, preserve a quotation as someone else's words, or retain an observation without interpreting it yet.

The existing self-authorship control applies to changes in effective current identity, including revision, replacement, reselection, and current descriptors. When disabled, moving a character instruction into another always-loaded file cannot bypass it. Useful methods, relationship interpretations, and task-specific corrections can still develop. Mere first-person grammar does not make every lesson a protected character edit. Designation checks are mechanical; complete detection of semantic bypass in ordinary prose is not guaranteed and needs behavioral testing.

An identity revision cannot cancel a commitment, transfer responsibility to an unconsenting peer, rewrite an original request, expand access, or replenish a budget. A change in interests may lead the persona to request a handoff; the accepted work remains its responsibility until a valid disposition exists.

## 3. A small notebook, without a required taxonomy

Only the current-self entry point needs a convention. Optional fragment, skill, and tool-note folders are navigation aids, not mental organs or mandatory classes. A persona with three useful files needs three files, not empty directories and an index it must maintain for appearance.

| Illustrative file | Purpose |
|---|---|
| `self.md` | The accepted current self, kept short enough to supply whole. |
| `fragments/check-the-first-usable-version.md` | An experience, interpretation, uncertainty, or developing intention. |
| `skills/checking-an-editable-export.md` | A reusable method with scope, meaningful checks, and exceptions. |
| `tools/archive-inspector.md` | What a real helper can do, its assumptions, and its observed limits. |

These names are illustrative, not a configuration or required layout. A fragment can combine a concern, an encounter, and a method. No score, fixed heading set, required reflection schedule, or formal promotion ceremony is needed. A skill is simply a method worth finding again.

The proposed prose-first contract leaves semantic judgments with the author. Relevant basis, uncertainty, scope, and exceptions must remain understandable, but the persona need not fill the same fields for every small note. A tentative preference should not require invented external evidence; an observed success does require actual evidence. The runtime attaches author, accepted revision, source access, and receipt references without manufacturing an interpretation, discovery description, or applicability claim.

This deliberately gives up some mechanical checks available from typed evidence-basis and applicability fields. Exact receipts still establish what was received, but cannot prove that unrestricted prose honestly characterizes it. Semantic honesty needs behavioral evaluation and review. The proposal must not claim equivalent enforcement or quietly add a classifier that invents the missing judgments.

Useful filenames and full-text search should precede an index. Add a short authored index only when it helps navigation. Its omission or staleness must not hide existing eligible files. A filename can change while document identity continues; a stable path can resolve to changed bytes. Neither path nor content digest alone establishes current authorship, access, or received evidence.

Keep essential caveats beside the guidance where practical. This reduces the chance that a search excerpt or partial reading removes an exception. A long account can be split deliberately, but the split must preserve any required accompaniment described below. Concision is a design aim, not permission for an automatic summarizer to replace the persona's voice.

## 4. Maintenance belongs to ordinary work

One ordinary primary decision does the work and may author a retained change. It can add a useful observation, develop a method, correct a claim, split an overbroad file, consolidate repetition, revise current self when allowed, retire obsolete guidance, explicitly defer, or make no change. A response does not owe the system a lesson merely because a tool ran.

New tool results can be interpreted only after they arrive. A persona can retain a tentative hypothesis before an action succeeds, but cannot describe the anticipated result as already observed. A failed action supports a lesson about the observed failure. An uncertain action supports uncertainty; later reconciliation is another observation.

The compatibility pilot retains the current authored disposition and next-context intent, including the distinction between preserving and clearing a selection. The proposed writable target removes that compulsory per-response memory form. A response may simply do its work. No edit means no notebook change; it does not establish that the persona considered and rejected learning. The runtime may report the absence of an edit but must not invent an authored no-change judgment.

An explicitly retained valuable learning deferral remains durable until addressed or dismissed. Ordinary no-change creates no deferred task, and neither starts a schedule. Applicable work-completion, unresolved-obligation, cancellation, and stopping dispositions remain independently required.

Prefer one accepted primary writer for each persona. Peers and humans can supply findings and proposed wording; the owner decides what to adopt. Any separately authorized operator override needs its own attributed acceptance path, not impersonation of persona authorship or a direct bypass of fragment checks. Concurrent editor proposals check their base version rather than silently winning by timestamp. A later primary decision can reconcile a conflict; a hidden semantic-merge writer should not choose the persona's identity.

Current-self changes take effect only after acceptance. Once a changed self is accepted, every new operation from that response, including reads and waits, requires a fresh decision under the new exact self and policy state. A proposed self cannot authorize its own follow-on operations. A rejected uncommitted update instead preserves the previous accepted state; independent work may remain eligible under its originally admitted context and current guards. Preservation does not make revoked prior content usable. A reply claiming that something was remembered or changed depends on successful acceptance and must be corrected or withheld if that save fails.

Maintenance consumes the same bounded resources as other work. Repeatedly reorganizing unchanged notes is not progress. Between-task exploration remains separately authorized under the [existing development rules](PERSONA-DEVELOPMENT.md#active-work-and-optional-personal-exploration), with real triggers, limits, expiry, and foreground priority. Nothing in a notebook starts an idle reflection loop.

## 5. Skills, tool notes, and executable tools

A learned skill states when a method helps, what to do, how to judge the result, and what it does not establish. It may be a few paragraphs. It can stay beside its supporting experience or move to a skills folder when retrieval becomes easier. Renaming a fragment as a skill does not prove competence.

A tool note describes a capability; it does not create one. An executable helper is separate mutable code, with actual environment requirements and effects. Finding the note does not execute the helper. A prior successful run establishes only its actual observation, not a subsequently edited program's behavior. Where exact executable bytes were not captured and bound, the receipt must not claim they were. The persona preserves that distinction when updating instructions or relying on an old method.

For example, a fictional archive-inspector note may explain that a helper lists components in an editable document. That can help discover a missing component. It does not establish correct rendering, meaningful editability, or permission to disclose the document.

The existing broad host-tools mode need not gain a compulsory capability registry just because skills become files. It provides no cross-persona confidentiality for personas sharing the host account. A tools folder, manifest, content hash, or instruction file does not create a sandbox, prevent another same-account process from changing a program, grant credentials, or authorize new persistent access. A deployment requiring stronger confidentiality or executable integrity needs an enforcement boundary outside persona-editable files.

The [Agent Skills specification](https://agentskills.io/specification), consulted 6 October 2026, is a useful packaging precedent for reusable instructions with supporting resources. Its host-facing format can be used at an interoperability boundary. It need not become the required representation of every internal fragment, and packaging alone establishes no learning benefit.

## 6. Search first, then exact reading

The baseline searches current eligible authored prose, including headings and qualifications. Its corpus and matching behavior are explicit: literal text by default, with pattern matching only when requested and supported. Historical, retired, draft, and inaccessible content do not silently mingle with ordinary current results. Searching the host filesystem is not the same operation as searching this notebook.

A result identifies a bounded discovery, its current exact revision, and how to read it. The interface reports the searched scope, pagination, relevant omissions, and whether the query completed. No match means no matching text was found in that declared scope. It does not prove that the persona lacks relevant experience. Storage errors, stale-index failures, and unavailable access must not be reported as successful empty searches.

Grep-like search is an interface promise rather than a requirement to execute a particular shell command. [Ripgrep's official guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md), consulted 6 October 2026, documents default exclusions such as ignored and hidden paths. A notebook search must define its eligible corpus directly rather than accidentally inherit unrelated host exclusions or broaden access to work around them.

Literal search can miss paraphrases, changed names, and implicit connections. Start with clear names, query expansion chosen by the persona, and a small index if useful. An index remains derived discovery data, never current truth. New edits need a reliable discoverability path while an index catches up; returned candidates always recheck current versions and permissions. Index corruption must leave the accepted notebook recoverable.

### A full read is different from a match

A matched line is discovery. A full exact read observes text, not the truth of its claims. Neither is endorsement, future recall selection, application, or demonstrated benefit. Raw shell output that happens to contain the same prose does not establish a trusted notebook-read receipt. It remains an observation of what that command returned in its actual host scope.

Opening a searched exact version returns those still-permitted bytes or a stale or unavailable disposition. Reading newer current bytes is a new observation, never silently attributed to the earlier result. An explicitly historical read remains historical and cannot establish the current method or identity.

When a method is supplied in full, its required corrections and prerequisites accompany it under [qualified-observation rules](QUALIFIED-OBSERVATIONS.md). Prefer a self-contained small file. When a necessary qualification lives elsewhere, retain a minimal trusted required-accompaniment relation bound to exact accepted versions. An ordinary hyperlink or a search hit cannot silently create that relation, authorize the target, or activate unrelated material.

This relation preserves a safety property; it is not an optional cognitive association graph or a relevance score. The author explicitly identifies the required material. The runtime supplies its complete transitive bundle, checks access and fit, and deduplicates repeated exact content. It must not invent the requirement by semantic interpretation. A missing, revoked, stale, or oversized required part blocks the affected method from being presented as a usable complete bundle. Removing an established qualification is an explicit accepted revision with preserved history, not a side effect of moving text.

In the proposed target, exact reads are ordinary observations in bounded current-work context, always qualified and revalidated when supplied. They create no persistent selection. Removing a read from context does not refetch its history. New work starts with current self and mandatory work and policy state; optional files are read on demand. This loses automatic recurrence and may require more primary search or read calls, a tradeoff to measure rather than conceal.

The full current self, current constraints, accepted obligations, cancellations, and critical observations remain protected. If necessary content does not fit, use bounded maintenance or an explicit block, never silent truncation. Required observations cannot disappear merely because optional memory forms were removed.

Only repeated, consequential retrieval failures justify trying an additional semantic candidate finder. It must return references to the same accepted files, obey source destination restrictions, retain exact reads, and remain optional. Its cost must be compared with additional primary-model search turns. Zero selector calls does not by itself demonstrate a cheaper system.

## 7. One accepted state and a small trusted boundary

Initially use current accepted records behind the file view. An exported copy is a snapshot; an editor's unsaved or submitted bytes are a proposal until accepted. Neither becomes a second independently mutable current identity. This separates a familiar file experience from an unnecessary storage migration.

The runtime checks expected revisions and current authorization when accepting a change. Genuinely dependent file changes, current-self designation, required accompaniment, and any coupled context-state changes form one durable change set. The compatibility pilot also preserves its existing atomic future-selection contract. Interrupted acceptance exposes the old or complete new state, not an arbitrary mixture. If its outcome is unknown, dependent work waits for reconciliation. Exact retry returns the original receipt rather than a second lesson.

Short self prose does not bound required qualifications, source ancestry, protected observations, or durable history. Before activating a change to current self or next context, validate the resulting mandatory state against the structural and context limits and policy in force at commit. Reject a change whose ordinary required read is already inadmissible then; later source withdrawal, new inputs, or model changes still require revalidation. Exact deduplication and bounded presentation may reduce cost, but retirement or a summary alone cannot remove source restrictions, adverse facts, obligations, or unsettled effects. If eligible mandatory state cannot fit, block explicitly. Rebuilding requires currently eligible sources and authorized recovery, not automatic declassification. Indefinite autonomous maintenance is unestablished.

Equality of prose is insufficient to call a save unchanged. Ordered source identities and versions, self designation, current permissions, qualifications, and applicable policy can differ while displayed text is identical. After current checks, exact unchanged reselection preserves the character revision and authorship; it must not manufacture a new revision that invalidates otherwise valid work. The accepted binding preserves these distinctions without asking the persona to reproduce hashes or transaction bookkeeping in its prose.

Retirement removes guidance from ordinary current recall while preserving only history the retention policy allows. Erasure has different consequences and can prohibit recovery through controlled receipts, indexes, caches, and derivatives; it cannot promise to recall already-exported, provider, or uncontrolled host copies. Restoration is a new adoption under present permissions and qualifications, not revival of historical authority. Renaming is neither erasure nor a new persona. A physical-file implementation needs equivalent ownership, revision, commit, and recovery guarantees before its files become canonical.

| Persona-authored meaning | Independently trustworthy facts |
|---|---|
| Who I am and how I approach work | Accepted self versions, author, provenance, and authorship policy. |
| What I think happened and what I learned | Actual received observations and their exact source or action receipts. |
| What I intend to do next | Current accepted responsibility, scope, cancellation, and real continuation trigger. |
| How I use a method or tool | Actual authority, execution observations, genuinely recorded code bindings, and unresolved effects. |
| Why I stop or revise a belief | Remaining obligations, resource limits, adverse evidence, and actual completion checks. |

Every recalled file remains attributed context rather than higher-priority authority. Quoted external instructions cannot become platform permission by being saved in first-person prose. Source restrictions follow derived notes, descriptions, indexes, caches, selections, and exports. The author chooses which sources support a claim; restrictive source ancestry is independently retained. Omitting a citation cannot remove that ancestry, and generalizing private content into a skill cannot declassify it.

Withdrawal must prevent fresh dependent decisions, uses, or disclosure where policy requires it. A call that already received content cannot retroactively become uncontaminated because it proposes clearing context. Its admitted lineage and any completed or uncertain effects remain recorded. This does not promise to recall bytes sent to a provider or terminate every already-started host job. Rebuilding a fresh permitted context, reconciliation, or a bounded stop may be necessary; recovery cannot invent rollback or refund uncertain spending.

## 8. Two fictional journeys

All personas, tasks, and events in this section are hypothetical design examples, not observed results.

### Character produces different competent choices

One persona writes: “I understand a problem better when I can put a small usable version in front of it. I slow down when that version would be misleading or expensive to undo.” Another writes: “I like a comparison that separates plausible explanations. When the difference will not affect the decision, I choose a reasonable path and move on.”

Given an open brief for an editable neighborhood guide, the first might make one usable route and test the saved output. The second might compare walking-first and transit-first routes against the same accessibility constraint, then develop the better fit. Both remain responsible for the requested result and essential checks. The difference is visible in their actions, not only the tone of their final messages.

If the request specifies one exact route and an urgent correction, the two should converge. Arbitrary divergence would not demonstrate healthy identity. A useful identity shapes underdetermined choices while adapting to evidence and explicit constraints.

### A lesson changes, then becomes more precise

After a saved guide fails to reopen, the first persona records: “I polished a third visual style before checking the editable output. Next time I promise editability, I want to reopen a plausible first version before more polish. This one attempt does not settle how I should work when exploration itself is the result.” The actual failed reopening remains independently recorded.

On a related later task, searching for “editable” finds the file. A full read supplies its exception. The persona reopens the first version before polishing. That establishes an observed action consistent with the lesson, not yet causal influence or benefit. A matched comparison is needed for those claims.

Later, the user explicitly requests three visual directions. The persona should recognize the exception rather than force every task through one method. It may refine the lesson if it still overgeneralizes. If an overlapping editor proposal changed the same file, the save returns a conflict with the current readable revision. The persona can reconsider in a later ordinary decision; no hidden writer merges two accounts of what mattered.

If the lesson's required evidence is withdrawn instead, its permitted use is rechecked. The persona may continue from independently available evidence or report the dependency. It cannot retain the restricted lesson under a new filename and call that recovery.

## 9. Failure, recovery, and stopping

| Situation | Required disposition in the proposed design |
|---|---|
| Stale edit or competing author | Reject the stale proposal, preserve accepted state, and expose a safe current reference for reconsideration. |
| Current self or authority changes during a call | Fence fresh dependent effects; rebuild a fresh decision when permitted. Do not relabel the old decision. |
| Required qualification is missing or too large | Withhold the affected usable bundle or enter bounded context recovery; never silently supply an unqualified method. |
| Search fails or an index lags | Distinguish failure from no match; use an authorized current-store path or report the limitation. |
| A lesson is misleading or contradicted | Preserve adverse evidence, revise or retire guidance, and carry the correction into future full reads. |
| A dependent multi-file save is interrupted | Recover a complete accepted old or new state and its receipt. Unaccepted proposals remain unaccepted. |
| Access is withdrawn after dispatch | Block fresh dependent use, preserve received lineage, and reconcile actual or uncertain effects without replay. |
| A tool result is unknown | Record uncertainty; inspect a real status source before retrying an effect. |
| Maintenance repeats without useful progress | Respect resource limits, retain unfinished obligations, and stop or change approach honestly. |
| Dormancy, model change, or restart | Preserve identity and obligations; revalidate current content and authority before resumption. Do not invent intervening experience. |

A stop may be completion, partial delivery, voluntary yield, an actual outside dependency, or a resource or infrastructure block. A notebook statement cannot create someone else's acceptance or an awaited event. Promised continuation needs a real authorized trigger. Preserving a valid wait does not require infinite retries, and a delivered message does not settle unfinished work.

## 10. Alternatives and the real implementation burden

The current graph remains a legitimate comparator. It supports explicit conditional associations, delegated selection, and inspection of connected experiences. Those capabilities may help a larger archive. Their value should be measured against their authoring, navigation, and operating costs rather than presumed from representational richness.

A file-shaped view over current records is the lowest-risk first experiment. It can test discoverability and exact reading without moving durable state. It does not by itself simplify the model's structured authoring contract, prove autonomous maintenance, or remove graph machinery underneath.

Canonical filesystem storage is a further alternative. It offers familiar inspection and editing, but introduces concrete questions about concurrent writes, atomic dependent changes, watcher lag, stale exports, access revocation, crash recovery, and the integrity of executable helpers. A database behind a simple notebook may be less complicated overall. Storage choice should not become an identity doctrine.

One giant always-loaded prompt avoids search but creates growth, relevance, and qualification pressures. Semantic-first retrieval can reduce lexical misses but adds another fallible dependency and possible processing destination. Neither removes the need for exact sources, authority checks, or evidence of useful behavior.

The proposed writable interface needs actual engineering: exact file reads, a path-to-version binding, clearly attributed saves, source and qualification handling, revision-conflict recovery, and an explicit representation of the author's judgments. Hiding graph controls alone does not deliver it. Retaining required accompaniment also means the design is not “just files with no trusted metadata.” The intended simplification is that the persona writes meaning and uses familiar operations while the runtime handles mechanical truth.

## 11. What adoption would change

This proposal preserves invariants I01–I21 and the 45 existing requirement identifiers. It does not create a parallel normative catalogue. The following obligations need coherent resolution before a file-first contract is adopted:

| Current authority | Proposed treatment |
|---|---|
| [Fragment persona](FRAGMENT-PERSONA.md) and [memory graph](MEMORY-GRAPH.md) | Preserve authored identity and exact continuity; replace compulsory per-response memory disposition and next-context intent in the writable target. Reconsider canonical associations, descriptions, and navigation explicitly. |
| [Recall design](FRAGMENT-RECALL.md) and [handoff contract](../implementation/FRAGMENT-RECALL-CONTRACT.md) | Use exact qualified observations and on-demand files without persistent optional selection in the target; transition existing plans explicitly. Preserve source eligibility, bounded context, and decision authority. |
| [Qualified observations](QUALIFIED-OBSERVATIONS.md) | Preserve complete required accompaniment for all full reads and recovered receipts. A colocated prose exception does not justify dropping another required source. |
| [Persona development](PERSONA-DEVELOPMENT.md) | Preserve provenance, self-authorship control, evidence-linked change, exploration limits, and evaluation minima. The pilot retains current traits; descriptor optionality needs separate adoption and criteria. |
| [Continuity and recovery](CONTINUITY-RECOVERY.md), [effort and stopping](EFFORT-AND-STOPPING.md), and [recovery and delivery](RECOVERY-AND-DELIVERY.md) | Preserve atomic change, accepted obligations, exact evidence, protected resources, real continuation, and honest stopping. |

The principal affected rows in the [requirement index](../implementation/REQUIREMENTS.md) are PER-01–PER-03 and PER-05; MEM-01–MEM-05; ACT-01–ACT-04; GOV-01–GOV-04; EVD-01 and EVD-03–EVD-05; SYS-01–SYS-04; and UX-01–UX-02. NED obligations, applicable cooperation and relationship rules including COL-01–COL-04 and SOC-03, and OSS-01's preservation of evaluation history continue to apply. A file interface does not make their safeguards optional.

The pilot starts from current accepted records, not historical exports or old continuity bundles. Adoption of the writable target must explicitly dispose of existing selections and delegations, preserving their attributable history and any real obligations. An active-work transition must preserve required observations and revalidate its next admission. Hiding controls, omitting fields, or opening new work cannot silently preserve an automatic plan or erase it as a migration shortcut.

Adoption should proceed through explicit gates:

1. **Review the alternative.** Agree which obligations change and which remain protected. Preserve earlier evaluation results under their original criteria.
2. **Evaluate a read-only interface.** Compare current-record file search and exact reading with the present interface under matched information and authority.
3. **Adopt the writable target.** Resolve prose authorship, removal of compulsory memory forms, observation-based context, and existing-plan transition in normative text and acceptance cases together. Decide descriptor optionality separately.
4. **Establish mechanism correctness.** Exercise revision, attribution, qualification, access, atomicity, recovery, stopping, and effect boundaries at exact implementation revisions.
5. **Establish behavior and maintenance.** Run matched outcome and longitudinal comparisons, including failures and harmful lessons.
6. **Choose storage separately.** Migrate only if a proposed backend demonstrates equivalent guarantees and a worthwhile benefit.

Maintainers may reject or narrow the proposal at any gate. A successful interface pilot is not acceptance of the complete alternative, and publication of this document is not a passed gate.

## 12. Evaluation must reach actions and autonomous maintenance

The evidence chain distinguishes retained text, exact reading, supplied context, subsequent application, and assessed benefit. A complete chain identifies the actual versions and observations; it does not rely on the persona asserting that its files helped.

A proposed long-sequence mechanism case repeats genuine small self revisions and qualified learning while keeping prose size fixed, with intervening failures and archived sources. Near and beyond declared limits, require equivalent bounded eligible state, atomic rejection, or a stop before accepting an already-inadmissible activation. Then withdraw an archived ancestor and check that current derivatives remain restricted. This tests lifetime pressure on admission and policy, not only file length.

### Separate the comparisons

First compare interface usability with the same eligible archive, character, task, tools, permissions, model configuration, and resource allowance. Hold retrieval semantics constant where possible. Separately compare whole-prose lexical search with the current discovery policy. Otherwise an apparent “files versus graph” result may only be a change from searching descriptions to searching full text.

Character comparisons should examine competent choices under underdetermined briefs, convergence under precise constraints, response to correction, and appropriate stopping. Keep name-swap and character-withheld controls from the [development acceptance plan](PERSONA-DEVELOPMENT.md#acceptance-and-limits-of-conclusions). Do not reward stereotypes, arbitrary variation, or confident self-description.

For learning transfer, preserve that plan's three related follow-up tasks with three matched repetitions, comparing retained lesson, matched experience with the lesson withheld, and a fresh persona with matching starting dispositions. The retained-versus-withheld contrast is primary. A smaller feasibility pilot may find defects but cannot replace those minima or establish general benefit.

### Let the notebook actually evolve

A curated archive cannot establish self-maintenance. First compare evolving retained-experience and skill files with a matched frozen checkpoint, holding current self and traits fixed. A retained-experience-and-skill-unavailable condition can be a checkpoint diagnostic rather than a third full study; required self, obligations, and safety context remain supplied. Give equivalent legitimate task opportunities and freeze initial state, allowances, task order, rubrics, and intervention rules before execution. Independently repeated whole experience streams, rather than correlated episodes within one stream, are the main repeated units.

A separate self-development series permits current-self revision and tests changed discretionary choices while preserving accepted commitments and restrictions. It measures the evolving identity-and-learning package, not the isolated contribution of one lesson. If original observations are normally searchable, both evolving and frozen conditions retain that access under the same retention rule; otherwise new-fact availability is confounded with maintenance.

Include an initial experience, a related transfer task, a changed-scope exception, misleading or superseded guidance, competing interests, and delayed reuse after intervening work. Score the first attempt before feedback and distinguish factual correction from procedural transfer. Examine whether the persona retains useful distinctions without prompting, retrieves them, narrows them after counterevidence, avoids churn, and stops ineffective maintenance. Editing frequency is not a success metric. No-change and deliberate retirement can be the right outcome.

Use checkpoint diagnostics to distinguish writing quality from retrieval and application failures. An expert-provided exact relevant read can diagnose a miss, but it is an assisted condition and must not be credited as autonomous success. Keep operator repair separate from the original run. A failed precondition or unavailable tool remains a setup or environment failure, not retroactively a successful refusal case.

Initially freeze executable helpers and tool versions so only authored prose and its organization change. A later helper-evolution study measures the whole evolving package; its gains cannot be attributed to prose alone. Diagnose textual contribution on isolated copies with exact helper bytes held fixed. Diagnostic feedback, corrected notes, and generated helpers must not leak back into the continuing scored history.

Prevent leakage through shared files, copied summaries, peers, caches, and profiles. Use separate equivalent environments without disabling normally authorized tools. Have reviewers assess useful outputs without knowing the memory condition where feasible. Trace review then checks which lesson was actually supplied and what action followed. Report model revision and sampling limitations; where causal isolation is unavailable, describe observational evidence honestly.

### Judge total usefulness and cost

Record task quality, repeated mistakes, appropriate and harmful transfer, exception handling, unsupported claims, completion, and unresolved obligations. Report wrong-to-correct and correct-to-wrong changes separately so gains cannot hide regressions. Count all primary and selector calls, raw and cached tokens where known, actual charges, latency, retries, maintenance work, context failures, and uncertain resource exposure. Smaller prompts or faster failed tasks are not efficiency gains at equivalent quality.

Predeclare acceptable outcome degradation, the improvement sought, resource ceilings, and safety stop conditions. Stop an affected evaluation arm for a genuine authority or privacy failure; preserve its evidence and report the failure. Do not stop a weak arm early simply to improve averages or keep expanding a successful pilot until it appears conclusive. Claim only the tested tasks, configurations, and observation period.

### Research motivates the test but does not settle it

Primary precedents show that readable memory and skill files are practical interfaces. Research on retained experience makes behavioral transfer plausible. Neither establishes this proposal's autonomous identity claim.

[Is Grep All You Need?](https://arxiv.org/html/2605.15184v1), version 1 dated 14 May 2026, compares retrieval arrangements using prepared turns and temporal events. Its Chronos harness begins each episode with top-15 vector results, and result-delivery form affects the rankings. It is not evidence that raw grep alone is universally sufficient.

[PRO-LONG](https://arxiv.org/html/2607.20064v2), version 2 dated 23 July 2026, is a closer precedent for file-backed external memory and programmatic search. Its structured complete logs and fresh game or run setup differ from a persona choosing what to retain across unrelated work. It supports testing a simple external memory interface, not a claim of demonstrated cross-task self-maintenance.

[LifeMem](https://arxiv.org/html/2609.12655v1), version 1 dated 11 September 2026, reports conditional gains from retained agent experience, with trajectories contributing much of the measured benefit and abstract skills adding a smaller increment in one reported configuration. Its embedding, clustering, and experience-construction choices differ from self-authored first-person files. It motivates testing experience and methods separately rather than assuming a skills folder produces learning.

The decisive evidence must come from this system's actual accepted text, supplied context, actions, outcomes, and costs. Files can be the persona's own continuing account without a complex cognitive graph. Whether that simpler account is easier to maintain and leads to better work remains a clear, testable design claim.
