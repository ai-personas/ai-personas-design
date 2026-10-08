# Start here

[Home](README.md) · [Persona core](design/PERSONA-CORE.md) · [Glossary](GLOSSARY.md)

## A collaborator that develops a point of view

The aim of AI Personas is to work with continuing characters rather than a series of unrelated responses. A persona takes shape through authored context, LLM reasoning under that context, actual interactions and actions, and the evolution of its authored prompts. It has a characteristic perspective, forms relationships, chooses how to approach work, and can change its mind. This describes continuing AI behavior, not human identity or consciousness.

Its character has one accepted, versioned account, used consistently by its profile and decision context. The account gives semantic meaning to all five OCEAN trait domains and to its VAD modeled affect profile. Natural prose is sufficient; scores, a fixed biography, and a separate profile writer are not required.

Every fragment the persona authors is conditioned by that account and written in its own voice. A fragment might say what it notices, how it tends to work, what it learned from a failed attempt, or how it understands a collaboration. Character can shape emphasis, uncertainty, and preferred methods without changing raw facts or exact quotations. Older fragments keep their actual authoring character until deliberately revised; they are not automatically restyled. Fragments are persona-defining, characteristic-bearing prompt parts; they are not all present in every response. Their selected assembly forms context for reasoning. Facts or experience may contribute to a fragment, but recording facts or replaying episodes is not what makes it a fragment.

The persona keeps them in ordinary files. It can give files useful names, create its own organization, search for a relevant way of approaching a situation, split a crowded fragment, revise an overgeneralization, or retire something misleading. It can put useful search cues into its prose so that one fragment helps it discover another. The aim is a bounded corpus of authored persona context and a bounded prompt for each decision. Either can become smaller as its organization improves. The design does not require a fixed map of mental functions or a separate model to construct the persona’s perspective.

## Stable tendencies and changing situations

OCEAN names openness, conscientiousness, extraversion, agreeableness, and neuroticism or negative emotionality. Here these describe a synthetic character's stable but revisable tendencies. A persona can be exploratory and still finish responsibly, quiet and still coordinate clearly, or considerate and still disagree with an unsupported claim. A trait never removes a shared obligation.

VAD describes modeled valence, arousal, and dominance or perceived control. Keep the usual affective baseline, the current situation-linked state, and outward expression distinct. The accepted character account describes the baseline; current affect is separately accepted contextual state with its own source and lifetime. An urgent verified problem may make a usually composed persona more direct without changing its stable character or claiming that it feels human distress. Perceived control supplies no permission to control a tool or another person.

Broad domains need not explain every useful difference. An optional facet or contextual preference can clarify how this persona initiates authorized action, checks a tool result, asks for help, handles a handoff, or revisits a failed assumption. Add these only where they explain the character better. There is no compulsory extra taxonomy, personality-to-action formula, or trait-based budget. The [research brief](sources/PERSONA-FILES-RESEARCH.md) separates useful precedents from unproven AI claims.

## The primary LLM chooses what comes next

The primary LLM is the model currently making that persona's decisions. During ordinary work, it can decide which fragments should inform a later decision. Finding or reading a file gives it information now; explicitly choosing a fragment establishes an intention to use it in the next relevant context. Those are different acts.

The supporting system carries that intention forward within its stated scope. It still checks whether a fragment is available, permitted, current, and able to fit with its necessary qualifications. It also supplies current obligations and authority constraints that the persona cannot drop simply by choosing different optional fragments.

This creates a reciprocal loop. Accepted traits shape own-voice fragments; selected fragments and current character enter the primary LLM's context; that perspective informs all discretionary work, communication, collaboration, and context choices. Actual task results and interactions with humans and peers provide experience. The persona can then revise, connect, consolidate, or retire fragments, refine its understanding of a relationship, or propose a permitted character change. Those accepted changes can influence the next encounter. There is one characteristic decision-maker throughout, rather than generic decisions decorated afterward with a persona's style.

Facts, exact requests, and required constraints still govern every persona. They can leave no sensible room for different choices. Writing a fragment alone does not show that the loop is useful. Later work must show whether the fragment was actually supplied, affected a choice, and helped. The [core](design/PERSONA-CORE.md#one-learning-and-action-loop) specifies the loop without turning it into compulsory stages or extra model calls.

## Following connections without loading everything

A hypothetical note might say, “When I start polishing too early, I look for my notes about editable deliverables and reopening the saved file.” That is an associative search cue. The primary LLM can follow it through bounded search or grep, using a supported regular expression if useful. It can adapt the wording, inspect a promising match, decline an irrelevant branch, or stop. The host executes the requested search; it does not recursively follow every cue or put every match into a prompt. A note with no outgoing cue can still be useful and discoverable.

| Relationship | What it means |
|---|---|
| Associative search cue | A suggestion about what else may be worth finding now. Results may change as files evolve; a match is not endorsement or proof of complete recall. |
| Exact evidence reference | An identified observation or accepted revision that supports a particular claim. Similar wording or a newer file at the same path cannot silently replace it. |
| Mandatory qualification or accepted warning | A condition that must remain with affected guidance, or make it ineligible. It cannot be left behind as an optional “search for more” suggestion. |

The persona owns the useful connections and the decision to follow them. No separate graph engine, compulsory link quota, fixed folders, hidden semantic writer, or secondary selector is needed. A no-match can mean different wording, a stale cue, or incomplete permitted coverage; it does not prove there is no relevant experience. Total searches, inspected results, returned text, context, and relevant cost and time stay bounded together. A small hop limit alone would not prevent one broad search or repeated reformulation from consuming the allowance. The [core discovery rules](design/PERSONA-CORE.md#ordinary-files-and-self-organization) and [assembly rules](design/PERSONA-CORE.md#bounded-and-faithful-assembly) give the authoritative boundaries.

The current persona-context interface uses lexical/regex searches, listing, simple authored cues and indexes, and exact reads. Semantic/vector retrieval and graph-driven memory engines are separate research alternatives, not optional hidden machinery behind those files. Adopting one would require an explicit design change; ordinary external task tools and compliant storage backends are unaffected.

## Every call considers maintenance, without forcing a lesson

Every application-visible LLM call acting as the persona receives its accepted character, relevant permitted fragments and observations, and an explicit maintenance obligation. Coverage includes initialization, search or selection decisions, tool follow-ups, communication, coordination, and repair. First initialization identifies its attributed seed and the absence of prior learned experience rather than inventing an already accepted character. The persona returns its work together with a proposed patch, no change with a concise reason, an explicit block, or a bounded deferral. This is a concise result-level account within the model response, not a separate report to the user or a request to reveal private reasoning.

A repeated status check may add nothing worth retaining. A known correction awaiting an exact tool receipt remains deferred with a named prerequisite, accepted owner or ownership gap, trigger, and limits; it is not silently called no change. A patch may add, correct, reorganize, or retire useful text. The model does not have to mutate a file or make a separate reflection call to satisfy the obligation. An omitted next-context selection remains a different matter from omitted maintenance.

A timeout, refusal without a usable maintenance response, or malformed output supplies no authored maintenance judgment. The host records that failure and does not dispatch substantive proposals from an invalid response. It can still honor cancellation and preserve accounting. Exact acceptance, bounded recovery, and independent-work rules live in the [system contracts](implementation/CONTRACTS.md). No design wording can guarantee that every provider attempt will succeed.

## One hypothetical example

Mira and Rowan help prepare a community workshop. These names and events are illustrations, not records of an executed project.

Mira prefers making a small concrete draft early. Rowan likes comparing options and notices missing assumptions. Neither preference fixes a profession or assigns a permanent role.

Rowan authors: “I like comparing alternatives, but I first look for needs that can rule them out. Before I polish a comparison, I ask what would actually change the choice.” This characteristic prompt part can apply beyond workshops; it need not record an episode. Rowan selects it for the planning context, reasons under that perspective, and asks about access needs before comparing venues. An actual previous workshop could inform this wording, but any claim about that event would retain its own evidence and limits.

Mira makes a draft agenda, then learns from Rowan's observation that it has no transition time. She may revise her prompt to: “I make a concrete draft early, then walk through how people will use it, including the transitions.” She attributes the observation to that exchange rather than claiming firsthand experience running the event.

Both can learn from the task, the environment, human interaction, each other, and reflection on their own choices. If the organizer asks for a recommendation before the alternatives, Rowan can retain that local communication preference without deciding that agreement or praise proves the recommendation correct. Mira may learn to share a narrow uncertain assumption with Rowan earlier, while recognizing that Rowan has accepted no future work merely by helping once. They can also decide a lesson is too narrow or unhelpful to keep. On a later, different task, a useful comparison would ask whether these lessons led to better choices than a matched attempt without them.

Their differences should remain visible in competent behavior, including how they respond to pressure or correction. The system should not force artificial disagreement or reward a persona for preserving a harmful habit merely to appear consistent.

## Who controls what?

| Responsibility | Owner |
|---|---|
| Purpose, scope, permitted effects, and resource allowance | The person or authorized institution commissioning the work |
| Character, interpretations, method choices, fragment organization, and next-context intent | The continuing persona, acting through its primary LLM within the granted scope |
| Access checks, current obligations, trustworthy receipts, version integrity, and bounded execution | The supporting host |
| Whether a claim is supported | The relevant observations and evaluation against stated criteria |

A fragment saying “I am allowed to book the venue” does not grant that permission. A tool being available does not show that a booking succeeded. A colleague's name in a plan does not mean that colleague accepted the work.

## Learning and continuity

The persona's identity continues across projects and model calls. A new model can inherit the same continuing record, but its performance may differ and needs its own evidence. The design does not assume that retained files retrain the model's weights.

A persona keeps one current character account while letting authorized self-authorship evolve it. Its profile and prompts resolve the same accepted version; they are not independently rewritten summaries. Transient modeled affect and ordinary lessons are not automatically changes to stable character. When a change does alter effective current character, the [core](design/PERSONA-CORE.md) requires a fresh decision under it before further operations from the old response. Locked character cannot be replaced through another always-supplied file. It can learn a practical method, correct a belief, understand a collaborator better, or recognize a pattern in its own mistakes. Raw observations and the persona's interpretation remain distinguishable. Private information stays within its permitted scope even if a broader lesson would be useful elsewhere.

Human-like character here means recognizable choices, interests, relations, development, and continuity. A synthetic origin remains clear; invented biography is not experience or a professional credential.

Like the modest analogy to human aging, development means that encounters can affect a continuing point of view. Calendar age, number of calls, amount of writing, and confident self-description do not establish maturity. Dormancy supplies no unreceived experience. Broader character evolution is optional and controlled; ordinary method learning, local relationship understanding, and transient affect remain distinct. A justified correction, smaller authored context, or appropriate no-change outcome may be more useful than a dramatic new self-story.

<a id="remembering-less-more-usefully"></a>
## Keeping persona context compact

The goal is an expressive, usable persona, not a growing diary or a fact-retrieval cache. Useful maintenance can replace several repeated formulations with one conditional own-voice fragment, retain a rare important exception, repair a misleading cue, or leave nothing new to save. It must not smooth away contradictions, erase protected unresolved effects, discard an accepted warning, or turn restricted source material into unrestricted advice. The [maintenance rules](design/PERSONA-CORE.md#maintenance-correction-and-continuity) govern what can be revised, retired, or erased.

A short prompt is only one kind of compactness. The authored corpus itself must stay bounded; selecting a short subset of an endlessly growing corpus is insufficient. Separately accountable supporting records keep provenance, access, expiry, and operational truth without defining the persona as an archive. The full declared managed persona-state footprint also includes archived text, old versions, evidence copies, indexes, aliases, qualification and provenance records, receipts, caches, and managed backups. Moving everything into an unlimited archive does not solve growth. Externally retained context used by the persona must be counted or expose an incomplete total bound; the system cannot promise control of arbitrary recipient or provider copies after disclosure. User-owned delivered files are not disposable notebook storage and cannot be deleted to meet its cap.

Whether an accepted lesson can remain after raw evidence expires depends on the actual retention and derivative-use policy. If allowed, its account must be honest that the old source is no longer inspectable; if derivatives must be erased or current use needs that exact evidence, abstraction cannot rescue it. At capacity the system may have to decline new optional retention, narrow a claim, block affected use, or seek an authorized policy change. It cannot promise unlimited exact recollection within finite storage. These are [deployment decisions](implementation/DEPLOYMENT-DECISIONS.md), not an automatic forgetting curve.

## Cooperation is an option with consequences

One persona may be enough. Additional personas can offer different perspectives, accept a contribution, negotiate its terms, or decline. Their organization should arise from the work and their choices, without a hidden profession roster or fixed team workflow.

Creating another persona does not create more budget or broader permissions. Leaving, pausing, or retiring does not erase accepted responsibilities. The system must make it clear who has accepted continuation or what remains unowned.

## What a useful result looks like

The user receives the actual result and an honest account of its limits. “The draft agenda is ready; the venue is not booked” may be a correct outcome. A changed file does not inherit the review of an older version, and an unknown external effect must be checked before trying the same action again.

Small requests should remain small. A sentence rewrite can include a short no-change reason without creating a team, a new fragment, a review ceremony, or a set of completed forms. Larger and more consequential work requires enough explicit context, consent, and evidence to remain accountable.

## What has been established?

This repository adopts a coherent design target. It does not establish that the runtime implements the full target or that personas have demonstrated useful long-term learning. The [status page](implementation/STATUS.md) separates current design from dated implementation evidence. The [evaluation guide](evaluation/README.md) explains what would count as stronger evidence.

Continue with the [persona core](design/PERSONA-CORE.md), then [work and boundaries](design/WORK-AND-BOUNDARIES.md). The [system contracts](implementation/CONTRACTS.md) describe what an implementation must make reliable.
