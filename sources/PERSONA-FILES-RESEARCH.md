# Why own-voice files and primary-model context choice

[Sources](README.md) · [Persona core](../design/PERSONA-CORE.md) · [Evaluation method](../evaluation/README.md)

**Role:** rationale and dated primary-source notes for the adopted design. Public sources below were inspected on 6 October 2026. They motivate particular tests; none establishes that AI Personas already exhibits autonomous learning, human-like continuity, or useful individuality.

## The design choice

The intended persona is a continuing AI character with a recognizable way of attending, interpreting, deciding, and communicating. Its accepted own-voice fragments are reusable parts of its prompts. It learns from the environment, tasks, peers, and its own choices, and can revise an overgeneralized lesson instead of preserving it merely because it once sounded useful.

Ordinary named files give that authored account a small inspectable interface. The persona can organize, search, read, edit, split, merge, and retire its own material. Simple literal search and supported regular-expression search are the baseline. An optional file association may help navigation; a required correction is a different integrity relationship. Neither requires a canonical cognitive graph, fixed mental categories, personality scores, or another model's universal ranking.

The primary LLM chooses relevant optional fragments for its next prompt while doing ordinary work. This decision is part of the persona's agency: which experience matters, which exception needs attention, and which material can be left out. The runtime checks and faithfully assembles that choice with current self, work, authority, resources, important observations, and necessary qualifications. It cannot silently paraphrase the persona into a generic profile or promote search matches into autonomous selection.

This is a design commitment, not a claim that every text file is safe or useful. Exact revisions, real observations, source restrictions, commitments, limits, and actual effects need trustworthy records outside editable prose. File-oriented use is compatible with different storage backends only when those same contracts hold.

## Relevant public precedents

### Agent Skills: readable instructions with optional supporting material

The [Agent Skills specification](https://agentskills.io/specification) packages reusable instructions in a readable main document with optional references, scripts, and assets. Its progressive-disclosure approach separates discovery from loading detailed instructions and resources. This supports an interoperability precedent for reusable methods. It does not require every internal persona fragment to use that packaging, establish that a skill was learned from experience, or authorize any listed tool.

### Ripgrep: explicit matching is practical, but its corpus matters

The [official ripgrep guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md) documents text and regular-expression matching and default exclusions such as ignored and hidden paths. AI Personas therefore specifies its eligible corpus and search limits explicitly instead of inheriting unexplained host exclusions. The design borrows familiar search behavior, not a command tutorial or permission to broaden filesystem access. A completed no-match result is evidence only about the declared search scope.

### Agentic search comparisons: the surrounding setup changes the result

[Is Grep All You Need? How Agent Harnesses Reshape Agentic Search, version 1](https://arxiv.org/html/2605.15184v1) compares lexical and vector retrieval under different agent harnesses and result-delivery forms. Its prepared corpus includes dialogue turns and extracted temporal events; the Chronos setup also supplies category-conditioned guidance and an initial top-15 vector context. Rankings vary with the surrounding setup. This motivates controlled comparisons of actual interfaces and total work, not the claim that raw grep alone is universally sufficient or that category-conditioned routing should be adopted here.

### Programmatic memory: searching an external log differs from authoring an identity

[PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning, version 2](https://arxiv.org/html/2607.20064v2) studies an external complete interaction log and programmatic reading in long-horizon game reasoning. It distinguishes accessible memory from material actually in context and tests the contribution of tool access. This is useful precedent for a small external-memory interface. Its append-all log and task setup differ from a continuing persona deciding what to retain, how to describe itself, and what transfers across unrelated work. It does not establish autonomous identity maintenance by first-person files.

### Experience reuse: separate trajectories, distilled methods, and later outcomes

[LifeMem: Enabling Lifelong Experience Reuse for LLM Agents, version 1](https://arxiv.org/html/2609.12655v1) combines retained trajectories, workflow clustering, and distilled textual skills, with retrieval of both experience and higher-level methods. Its mechanism differs from this design's persona-owned files and primary-model selection. It motivates testing raw experience, authored lessons, and reusable methods separately rather than attributing any improvement to the presence of a skills folder. Its results cannot be inherited as evidence for AI Personas.

## What must still be demonstrated here

The relevant chain is accepted own-voice text, exact permitted selection, actual supplied context, subsequent choice, and an independently assessed useful outcome. File creation proves none of the later links by itself. A model's statement that a lesson helped is not a controlled measurement.

The [evaluation method](../evaluation/README.md) and [acceptance cases](../evaluation/ACCEPTANCE.md) separate interface usability, discovery success, primary-model choice, actual inclusion, learning transfer, evolving file maintenance, current-self development, and total cost. Comparable conditions preserve legitimate source access, current authority, mandatory state, tools, and resource limits. They also preserve failed, harmful, assisted, and inconclusive outcomes.

An evolving notebook needs evidence beyond a hand-curated archive. Observe delayed reuse, paraphrased queries, missed retrieval, misleading guidance, changed-scope exceptions, corrections, rename or merge decisions, no-change choices, and restraint when maintenance is unhelpful. Exact relevant material supplied by an expert can diagnose retrieval failure, but that assisted condition is not autonomous success.

A distinctive voice may accompany generic choices. Different choices may be competent or harmful. Two characters may properly converge under precise constraints. The design's aim is useful, evidence-responsive continuity, not maximum difference, stereotyped traits, fragment counts, or perpetual introspection. Auxiliary retrieval is justified only by a demonstrated problem and measured benefit under the same permission and cost rules; it must not take ownership of the persona's next context.

## Earlier ideas and their disposition

The historical reports contributed persistent identity, accepted responsibilities, bounded capability use, exact evidence, and accountable cooperation. Later graph/selector work clarified source qualification and faithful inclusion, but its mandatory representation and delegated-selection assumptions are superseded. The earlier file proposal's on-demand-only context target is also superseded by explicit primary-LLM next-context choice. Numeric descriptors may remain historical or optional experimental data; they no longer define the minimal persona.

Those semantic changes are recorded in the [decision register](../DESIGN-DECISIONS.md); the [manifest](SOURCE-MANIFEST.md) retains exact prior sources. Removing duplicate current manuals does not erase real commitments, permissions, provenance, failures, or the criteria under which a past result was reported.
