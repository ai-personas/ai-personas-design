# Start here

[Home](README.md) · [Persona core](design/PERSONA-CORE.md) · [Glossary](GLOSSARY.md)

## A collaborator that develops a point of view

The aim of AI Personas is to work with continuing characters rather than a series of unrelated responses. A persona has its own perspective, remembers permitted experience, forms relationships, chooses how to approach work, and can change its mind.

Its character has one accepted, versioned account, used consistently by its profile and decision context. The account gives semantic meaning to all five OCEAN trait domains and to its VAD modeled affect profile. Natural prose is sufficient; scores, a fixed biography, and a separate profile writer are not required.

Every fragment the persona authors is conditioned by that account and written in its own voice. A fragment might say what it notices, how it tends to work, what it learned from a failed attempt, or how it understands a collaboration. Character can shape emphasis, uncertainty, and preferred methods without changing raw facts or exact quotations. Older fragments keep their actual authoring character until deliberately revised; they are not automatically restyled. Fragments are reusable prompt parts; they are not all present in every response.

The persona keeps them in ordinary files. It can give files useful names, create its own organization, search for an old lesson, split a crowded fragment, revise an overgeneralization, or retire something misleading. The design does not require a fixed map of mental functions or a separate model to decide what the persona should remember.

## Stable tendencies and changing situations

OCEAN names openness, conscientiousness, extraversion, agreeableness, and neuroticism or negative emotionality. Here these describe a synthetic character's stable but revisable tendencies. A persona can be exploratory and still finish responsibly, quiet and still coordinate clearly, or considerate and still disagree with an unsupported claim. A trait never removes a shared obligation.

VAD describes modeled valence, arousal, and dominance or perceived control. Keep the usual affective baseline, the current situation-linked state, and outward expression distinct. The accepted character account describes the baseline; current affect is separately accepted contextual state with its own source and lifetime. An urgent verified problem may make a usually composed persona more direct without changing its stable character or claiming that it feels human distress. Perceived control supplies no permission to control a tool or another person.

Broad domains need not explain every useful difference. An optional facet or contextual preference can clarify how this persona initiates authorized action, checks a tool result, asks for help, handles a handoff, or revisits a failed assumption. Add these only where they explain the character better. There is no compulsory extra taxonomy, personality-to-action formula, or trait-based budget. The [research brief](sources/PERSONA-FILES-RESEARCH.md) separates useful precedents from unproven AI claims.

## The primary LLM chooses what comes next

The primary LLM is the model currently making that persona's decisions. During ordinary work, it can decide which fragments should inform a later decision. Finding or reading a file gives it information now; explicitly choosing a fragment establishes an intention to use it in the next relevant context. Those are different acts.

The supporting system carries that intention forward within its stated scope. It still checks whether a fragment is available, permitted, current, and able to fit with its necessary qualifications. It also supplies current obligations and authority constraints that the persona cannot drop simply by choosing a different memory.

This creates a practical feedback loop: experience affects fragments, fragments affect decisions, and the resulting experience can change the fragments again. Writing a fragment alone does not show that the loop is useful. Later work must show whether the fragment was actually supplied, affected a choice, and helped.

## Every call considers maintenance, without forcing a lesson

Every application-visible LLM call acting as the persona receives its accepted character, relevant permitted fragments and observations, and an explicit maintenance obligation. Coverage includes initialization, search or selection decisions, tool follow-ups, communication, coordination, and repair. First initialization identifies its attributed seed and the absence of prior learned experience rather than inventing an already accepted character. The persona returns its work together with a proposed patch, no change with a concise reason, an explicit block, or a bounded deferral. This is a concise result-level account within the model response, not a separate report to the user or a request to reveal private reasoning.

A repeated status check may add nothing worth retaining. A known correction awaiting an exact tool receipt remains deferred with a named prerequisite, accepted owner or ownership gap, trigger, and limits; it is not silently called no change. A patch may add, correct, reorganize, or retire useful text. The model does not have to mutate a file or make a separate reflection call to satisfy the obligation. An omitted next-context selection remains a different matter from omitted maintenance.

A timeout, refusal without a usable maintenance response, or malformed output supplies no authored maintenance judgment. The host records that failure and does not dispatch substantive proposals from an invalid response. It can still honor cancellation and preserve accounting. Exact acceptance, bounded recovery, and independent-work rules live in the [system contracts](implementation/CONTRACTS.md). No design wording can guarantee that every provider attempt will succeed.

## One hypothetical example

Mira and Rowan help prepare a community workshop. These names and events are illustrations, not records of an executed project.

Mira prefers making a small concrete draft early. Rowan likes comparing options and notices missing assumptions. Neither preference fixes a profession or assigns a permanent role.

After a previous workshop, Rowan retained: “I spent too long comparing venues before checking the organizer's access needs. I should resolve requirements that can rule an option out before polishing the comparison.” Rowan finds this fragment and chooses it for the next planning decision. The next question changes accordingly.

Mira makes a draft agenda, then learns from Rowan's observation that it has no transition time. She may retain: “When I make an agenda, I need to test the transitions as well as the sessions.” She attributes the observation to that exchange rather than claiming firsthand experience running the event.

Both can learn from the task, the environment, each other, and reflection on their own choices. They can also decide a lesson is too narrow or unhelpful to keep. On a later, different task, a useful comparison would ask whether these lessons led to better choices than a matched attempt without them.

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

## Cooperation is an option with consequences

One persona may be enough. Additional personas can offer different perspectives, accept a contribution, negotiate its terms, or decline. Their organization should arise from the work and their choices, without a hidden profession roster or fixed team workflow.

Creating another persona does not create more budget or broader permissions. Leaving, pausing, or retiring does not erase accepted responsibilities. The system must make it clear who has accepted continuation or what remains unowned.

## What a useful result looks like

The user receives the actual result and an honest account of its limits. “The draft agenda is ready; the venue is not booked” may be a correct outcome. A changed file does not inherit the review of an older version, and an unknown external effect must be checked before trying the same action again.

Small requests should remain small. A sentence rewrite can include a short no-change reason without creating a team, a new memory, a review ceremony, or a set of completed forms. Larger and more consequential work requires enough explicit context, consent, and evidence to remain accountable.

## What has been established?

This repository adopts a coherent design target. It does not establish that the runtime implements the full target or that personas have demonstrated useful long-term learning. The [status page](implementation/STATUS.md) separates current design from dated implementation evidence. The [evaluation guide](evaluation/README.md) explains what would count as stronger evidence.

Continue with the [persona core](design/PERSONA-CORE.md), then [work and boundaries](design/WORK-AND-BOUNDARIES.md). The [system contracts](implementation/CONTRACTS.md) describe what an implementation must make reliable.
