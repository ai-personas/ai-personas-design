# Persona-defining context, characteristic reasoning, and self-revision

[Sources](README.md) · [Persona core](../design/PERSONA-CORE.md) · [System contracts](../implementation/CONTRACTS.md) · [Evaluation method](../evaluation/README.md)

**Role:** explanatory rationale and bounded primary-source claims, reviewed through 10 October 2026. This brief extends the earlier file-and-context research; the [provenance manifest](SOURCE-MANIFEST.md) preserves its exact predecessor. It adds no requirements beyond the normative design, reports no new AI Personas experiments, and does not establish subjective experience.

## What kind of evidence is this?

The sources contribute different kinds of evidence. A finding about human traits, a result from an LLM experiment, and an engineering precedent each support different conclusions. None alone demonstrates that the complete AI Personas design works.

| Evidence class | What it contributes | What it cannot establish here |
|---|---|---|
| Established human constructs | Vocabulary and distinctions supported in studied human populations | That an LLM has human psychology, or that a human questionnaire is a valid AI controller |
| Limited LLM experiments | Findings for named models, prompts, tasks, and comparison conditions | Durable behavior across arbitrary tasks, partners, model upgrades, or deployments |
| Engineering precedent and design judgment | Reasons for inspectable files, explicit outcomes, qualified context, and reliable state handling | That the combined AI Personas architecture has been implemented or tested |
| Unrun product hypotheses | Questions and controlled comparisons for the acceptance plan | A measured benefit, universal threshold, or 100% guarantee |

## The adopted design and its rationale

A persona is the continuing loop of characteristic context, LLM reasoning, actual interaction and action, feedback, and self-revision. Persona-authored fragments are reusable prompt parts that define its perspective. The selected fragments become context for the primary LLM, which supplies the reasoning or “brain” function within that loop. The fragment collection alone is not the persona, and storing facts is not its defining purpose.

This is an architectural description. It makes no claim of consciousness, human psychology, or behavior that stays the same across models. Context conditions a trained LLM that already has learned capabilities and behavioral tendencies. Files are therefore one influence on behavior; identical fragments need not produce identical behavior with a different model.

**The accepted character account.** The [persona core](../design/PERSONA-CORE.md) adopts one accepted, versioned account with meaningful semantic OCEAN traits and distinct VAD modeled affect, expressed in the persona's own voice. Additional facets and operational preferences may make that account more precise when they explain useful differences. The research supplies neither a mandatory numeric scale nor a universal formula mapping traits to actions.

**Authorship and attribution.** New persona-authored fragments use the accepted character actually supplied when they are written. During bounded initialization, they instead use the attributed seed and candidate profile. Older fragments retain their actual authoring-character attribution until deliberately revised; that attribution does not override the current accepted account.

A fragment can express a characteristic method, approach to a tool, relationship interpretation, or correction. Generic procedures, tool instructions, and factual records remain supporting assets, whoever wrote them. Character appears in what the persona notices, how it interprets evidence, what it tries, and how it communicates. Repeated trait labels or a name added to generic instructions do not establish that connection. Exact quotations, observations, permissions, and mechanical metadata retain their own meanings. Character provides no license to rewrite a source or invent experience.

**Files, discovery, and actual context.** Ordinary named files provide an inspectable interface for authored prompt parts. Stored fragments are available material. Selected fragments become operative prompt parts when actually supplied. Discovery, reads, and continuing history can also expose unselected text; that exposure remains separately accounted for. A fragment may express a characteristic interpretation, method, stance, or relationship without adding a new factual record.

Supporting histories, tool descriptions, skills, scripts, and data have their own purposes, authorship, and authority. Using or organizing them does not turn them into persona-defining fragments. The persona may search, read, organize, revise, split, merge, and retire permitted material.

Literal search and supported regular-expression search find candidates. The primary persona LLM makes the semantic next-context choice. Optional associations help it navigate; they require neither a canonical cognitive graph nor another model's ranking. The runtime preserves exact revisions, required qualifications, and truthful records of what was actually supplied. It must not silently paraphrase the persona into a generic profile.

**Every invocation has explicit dispositions.** Every persona-level LLM invocation receives maintenance input covering both persona fragments and supporting assets. Its accepted response explicitly covers:

- The work of the invocation.
- Maintenance of persona fragments and maintenance of supporting assets.
- The next-context disposition for fragments and for supporting resources.

One concise, justified no-change disposition can cover both maintenance scopes. An appropriate preserve or no-optional-need disposition can cover next-context choice. Maintenance and context choice remain distinct decisions; neither requires a file write, a new search, or another model call merely to produce a change.

These explicit inputs and outcomes make coverage observable. They cannot prove an internal mental process. A justified unchanged decision, a bounded unresolved or mode-limited disposition, an accepted change, and a failed attempt remain different outcomes. A timeout or refusal cannot truthfully be recorded as a persona-authored no-change decision.

The [contracts](../implementation/CONTRACTS.md) define coverage, response acceptance, failure containment, and the fresh-decision boundary after effective character changes. This brief explains their rationale without creating a second protocol.

## Contextual persona: operational interpretation and its limits

Runtime context can influence the behavior a trained model expresses. The following sources help explain that possibility while also limiting what can be attributed to authored files.

The [Persona Selection Model, Marks, Lindsey, and Olah, 23 February 2026](https://alignment.anthropic.com/2026/psm/) proposes that pre-training develops a repertoire of personas, post-training refines the distribution over assistant behavior, and runtime context further conditions what is enacted. This is the authors' explanatory model and synthesis of evidence, not an established, exhaustive theory. It explicitly does not promise one coherent persona across contexts. It is relevant to characteristic context, but it contradicts the simple claims that files create all personality or that the trained LLM is behaviorally neutral.

[The Assistant Axis, Lu et al., v1, 15 January 2026](https://arxiv.org/abs/2601.10387v1) reports a direction in model activation space associated with default assistant behavior, along with conversational drift in the studied models. This supports testing whether conversational context changes characteristic behavior. Its intervention steers internal activations, however, which differs from editing authored prompt parts. The inspected abstract does not establish stable OCEAN/VAD expression, enduring identity, or the effectiveness of the present self-revision loop. Both sources were independently inspected on 8 October 2026.

Here, “persona” therefore names the designed whole loop. That operational meaning leaves metaphysical identity and subjective experience unsettled. Contextual influence, observable character, task competence, authorized effects, and justified development each need their own evidence. Neither a direction found through interpretability research nor a persuasive self-description establishes all of them.

## Context adaptation is the closer engineering comparison

Prompt and context adaptation change the inputs that guide an LLM's later work. That mechanism is a closer comparison for authored persona fragments than factual recall alone. It still leaves the central persona hypothesis unproven: characteristic authorship, context selection, reasoning, interaction, and revision must work together over time. A better task prompt does not by itself establish a continuing persona.

| Primary source and inspected version | Supported component claim | Transfer boundary |
|---|---|---|
| [GEPA, Agrawal et al., v1, 25 July 2025](https://arxiv.org/abs/2507.19457v1), with [methods inspected in the v1 paper](https://arxiv.org/pdf/2507.19457v1) | Records of execution and natural-language feedback support evaluated prompt proposals under a task dataset, metric, and budget for trial runs, or rollouts. Candidate selection preserves complementary successes on individual instances instead of always mutating one winner. Gains are reported on four studied tasks. | Supports evaluating prompts against outcomes. It does not establish a single persona's identity formation or show that an untested rewrite helps. The candidate pool and optimizer are not adopted as another author, selector, or set of current selves. This deeper methods inspection extends the earlier abstract-only account; it is not a reproduction. |
| [ACE, Zhang et al., v1, 6 October 2025](https://arxiv.org/html/2510.04618v1) | Modifies context without weight updates, using evolving task guidance and localized revisions. Its AppWorld case study illustrates information loss when the entire context is repeatedly rewritten. Appendix B warns that poor reflection can create noisy or harmful context and that some tasks do not benefit from richer context. | Supports comparing incremental adaptation with whole-context rewriting. Its separate generator, reflector, and curator roles, structured entries, and embedding-based deduplication—finding similar entries through learned numerical representations—differ from primary-persona authorship and lexical navigation. Its task results do not validate character continuity or a strict lifetime storage bound. |

**Later ACE findings.** [ACE v3, 29 March 2026](https://arxiv.org/html/2510.04618v3), was separately checked on 9 October 2026. This extends the review without replacing the v1 claims or locators above:

- **Robustness:** Appendix A.4 reports that ACE with weaker reflectors or moderate injected harmful feedback still outperforms the base model in the studied FiNER offline conditions. Harmful updates on every iteration bring performance below the base model.
- **Regression:** Appendix A.6, Table 19, shows that more reflection rounds can produce worse AppWorld results than fewer rounds.
- **Cost:** Appendix A.3, Table 15, reports more evaluation-stage input tokens per AppWorld query than GEPA, separately from adaptation costs.

These scoped comparisons motivate tests of robustness, regressions, and costs across a whole episode. They establish no persona benefit or cost advantage. They supply no adopted reflector architecture, reflection quota, or numeric setting.

**Experience-derived guidance.** [ReasoningBank, Ouyang et al., arXiv v2, 16 March 2026](https://arxiv.org/html/2509.25140v2), provides positive evidence within its evaluated setting:

- Gemini-2.5-Flash success rises from 40.5% to 48.8% on the evaluated 684-task WebArena set, comprising five subsets and excluding Maps.
- Its Shopping ablation rises from 46.5% with success-only experience to 49.7% when failures are included.

Full v2 methods and appendices were inspected on 9 October 2026. The system uses embedding retrieval, the same underlying model to judge success and failure, separate extraction, and append-only storage. Those mechanisms differ from primary-owned lexical selection and bounded maintenance of characteristic fragments.

Its resource and context findings also qualify the positive results. Fewer interactions did not mean fewer total tokens: Appendix C.2 reports average per-task use of 53,054.5 tokens versus 50,847.4, a 4.3% increase that includes generation, judging, and extraction. Appendix C.1 reports lower Shopping success as the number of retrieved experiences rises from one to four. More context was therefore not uniformly better in that system. This motivates a bounded comparison of context combinations, not a universal one-fragment limit.

The inspected [arXiv v2 metadata](https://arxiv.org/abs/2509.25140v2) reports acceptance to ICLR 2026. Direct access to the linked [OpenReview paper](https://openreview.net/pdf?id=jL7fwchScm) returned a browser challenge, so no claim is made that the versions have identical bytes. These findings motivate comparisons; they establish neither this design's maturity nor its cost advantage, and they introduce no retrieval or controller mechanism.

GEPA v1 and ACE v1 were independently inspected on 8 October 2026. Neither is adopted as the persona architecture. The design question is whether a persona can author, select, and revise characteristic prompt parts that usefully guide its own later reasoning and action within the existing authority boundaries. This is adaptation through context. It makes no claim that prompt editing changes model weights or reveals provider-internal reasoning.

The memory, retrieval, and retention studies below remain adjacent evidence for discovery limits, bounded storage, provenance, stale guidance, and safe reuse. They do not define the persona. Correct recall, a smaller store, or an effective prompt optimizer is insufficient evidence of a characteristic and useful context/action/self-revision loop.

### Trait-seeded bootstrap and self-harmonization

Bootstrap establishes a traceable starting account before continuing authorship begins. The [core](../design/PERSONA-CORE.md) describes the normal handover:

1. A small, attributed trait/affect seed informs the initialLLM's candidate own-voice fragments.
2. Coherent acceptance establishes the starting account.
3. The primaryLLM takes responsibility for continuing permitted authorship and next-context choice.

The names initialLLM and primaryLLM distinguish roles. They may use the same model configuration or separately declared configurations. Generated starting detail is a candidate interpretation, not an additional user preference, lived history, or demonstrated competence. Genuine alternative origins must retain their attribution; supplied text must not be described as generated. A sparse seed needs a different disposition from a genuinely conflicting seed. Fluent prose cannot silently resolve a conflict.

**Self-harmonization** means making selected prompt parts understandable together with current character, the situation, and received evidence. It may clarify scope, preserve productive tension, correct or retire guidance, or leave text unchanged. It need not rewrite the entire collection or make different personas alike. Actual work creates opportunities to assess the starting interpretation. Praise, repetition, and smoother wording alone do not prove useful development.

[Self-Refine, Madaan et al., v2, 25 May 2023](https://arxiv.org/html/2303.17651v2), independently inspected on 8 October 2026, uses the same model to generate, critique, and revise task outputs without updating weights. Its reported trade-offs across aspects of quality, and its task-specific stopping conditions, support evaluating revisions instead of assuming each revision improves the result. It does not validate persona bootstrap or require extra reflection calls. Nor does it establish bounded lifetime storage: its procedure retains earlier feedback and output history. Together with GEPA and ACE, it motivates explicit feedback and qualified revision while preserving this design's primary authorship and resource boundaries.

## Human constructs: useful vocabulary with a transfer boundary

Human research offers vocabulary for describing traits, modeled affect, and other differences. Using that vocabulary in a design does not transfer the validity of human measurements to an AI persona. Each construct below has a limited role.

### OCEAN traits and contextual expression

OCEAN names five trait domains: Openness/Open-Mindedness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism/Negative Emotionality. The BFI-2 organizes these human domains into 15 facets. Distinctions such as sociability versus assertiveness, or organization versus productiveness, help describe more than five crude extremes. The instrument's validation concerns human measurement, not persistent AI behavior. [Soto and John, 2017, BFI-2](https://www.colby.edu/wp-content/uploads/2013/08/Soto_John_2017.pdf)

Human experience-sampling studies found substantial variation within an individual while aggregate tendencies remained stable over the studied two-to-three-week windows. This motivates evaluating recognizable patterns across situations instead of demanding identical wording in every situation. It establishes neither how quickly an AI persona should change nor a numeric drift limit. [Fleeson, 2001](https://pubmed.ncbi.nlm.nih.gov/11414368/)

The design uses these traits within deliberate interpretation boundaries:

- Curiosity can shape exploration without requiring more tool calls.
- Sociability can shape contact preferences without granting more autonomy.
- Agreeableness does not require accepting false claims.
- Improvisation does not remove verification duties.
- Negative Emotionality neither diagnoses a disorder nor justifies unsafe behavior.

These are design choices, not causal laws extracted from OCEAN. Demographic stereotypes and an inferred personality of the real user do not supply the persona's profile.

### VAD modeled affect is distinct from trait, expression, and authority

VAD provides a way to describe modeled affect; it is not evidence that a model feels emotions. The human PAD emotional-state framework uses pleasure, arousal, and dominance. This design uses valence for pleasantness, arousal for activation, and dominance for modeled control. The source supports a dimensional description of human emotional states. Adopting those dimensions as synthetic context is a design analogy. [Mehrabian, 1995](https://pubmed.ncbi.nlm.nih.gov/7557355/)

A baseline disposition, a current modeled response to an event, and outward expression serve different purposes. A persona can remain recognizably composed while communicating urgency. Modeled control supplies no permission to control people, tools, or resources.

Any optional coordinates need declared engineering meanings. They are neither clinical measurements nor percentages of felt emotion. The reviewed evidence validates no universal conversion from OCEAN to VAD, action frequency, or a reflection budget.

The NRC VAD work obtains human ratings for affective dimensions of English words. It supports measurement of lexical affect, not an internal AI affect controller. An answer can describe an alarming event calmly, so word valence alone cannot establish the persona's modeled state or appropriate behavior. [Mohammad, ACL 2018](https://aclanthology.org/P18-1017/)

### Additional distinctions, only where useful

Other concepts may help describe the persona's own-voice character when they explain a useful difference. They do not create a compulsory taxonomy or another host-authored personality policy.

| Subject | Primary-source basis | Bounded design inference |
|---|---|---|
| Values | Schwartz distinguishes values from traits, beliefs, attitudes, and norms. [Schwartz, 2012](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/) | Distinguish what matters from a current goal, a demonstrated skill, and actual permission. No full values inventory is required. |
| Initiative | Bateman and Crant studied a relatively stable human tendency to effect environmental change and its relationship to the Big Five. [Bateman and Crant, 1993](https://onlinelibrary.wiley.com/doi/10.1002/job.4030140202) | Preferences can distinguish initiating, persisting, switching strategy, and stopping. A human scale does not calibrate AI autonomy or spending controls. |
| Agency and communion | Human studies distinguish self-oriented agency and other-oriented communion. Their importance changes with perspective and outcome interdependence. [Abele and Wojciszke, 2007](https://pubmed.ncbi.nlm.nih.gov/17983298/) | The vocabulary can describe initiative and concern for others without making them opposite ends of one scale. It does not validate AI action quotas, competence, or collaboration success. |
| Coordination | Salas and colleagues propose teamwork components and coordinating mechanisms, including monitoring, adaptability, and closed-loop communication. This human-team framework is distinct from the personality Big Five. [Salas, Sims, and Burke, 2005](https://journals.sagepub.com/doi/10.1177/1046496405277134) | Ownership, handoff, consultation, and disagreement preferences deserve direct description and testing. Agreeableness alone does not specify good cooperation. |
| Reflective style | Need for cognition concerns engagement in and enjoyment of thinking in human research. [Cacioppo and Petty, 1982](https://richardepetty.com/wp-content/uploads/2019/01/1982-jpsp-cacioppopettyncog.pdf) | Describe preferences for comparing explanations and checking assumptions without treating verbosity, private reasoning, or token count as intelligence or learning. |

Relationship interpretations, habits, capability evidence, and current goals can add relevant context while remaining distinct from traits and affect. Trust in a collaborator differs from confidence in a claim and from authorization to act. These separations are product design judgments; they do not assert that the constructs are statistically independent.

## LLM persona evidence: promising expression, limited continuity claims

Studies show that persona prompts can change expression and some behavior under particular conditions. They also show that self-reports, recognizable language, task performance, and continuity can diverge. Each result needs to stay attached to the models, prompts, and assessments that produced it.

| Primary source and version | Supported observation | Implication and limit |
|---|---|---|
| [PersonaLLM, Jiang et al., NAACL Findings 2024](https://aclanthology.org/2024.findings-naacl.229/) | Binary Big Five prompting of GPT-3.5/GPT-4 was studied through inventories and stories. The [published paper](https://aclanthology.org/2024.findings-naacl.229.pdf), rechecked on 8 October 2026, reports explicit trait-name leakage. Final human evaluation used GPT-4 stories without those mentions. | Supports distinguishable trait-conditioned expression in those conditions. It does not establish nuanced fidelity from a seed to own-voice fragments, sustained tool behavior, lived experience, or useful autonomous character. Recognition of trait labels and characteristic behavior need separate assessment. |
| [A psychometric framework for evaluating and shaping personality traits in large language models, Serapio-García et al., Nature Machine Intelligence, 18 December 2025](https://www.nature.com/articles/s42256-025-01115-6) | Reports configuration-dependent psychometric reliability and controllable expression. Downstream validation scores generated social-media status text. Shaping multiple traits together is weaker than shaping a single trait. | The assessed output is language, not tool use, peer contribution, or task completion. It establishes neither task benefit nor universal validity of self-reports. |
| [Han et al., ICML 2026, PMLR 306](https://proceedings.mlr.press/v306/han26n.html) | The published abstract reports steered self-reports but small or inconsistent behavioral effects and unreliable prediction of behavior from self-reports. | Abstract-level inspection supports this narrow claim. Detailed methods from an earlier preprint are not treated as the inspected publication. |
| [Kocielnik et al., v1, 10 June 2026; ICML CTB workshop contribution](https://arxiv.org/html/2606.12730v1) | Sharing versus separating assessment histories changes some intention–behavior correlations in bounded text-response probes. | Motivates testing whether measurement itself affects behavior, without claiming that every probe does so. Shares authors with Han; neither study tests this continuing fragment/tool loop. Defining persona context must be preserved when assessment history is separated. |
| [Self-Assessment Tests are Unreliable Measures of LLM Personality, Gupta et al., 2024](https://aclanthology.org/2024.blackboxnlp-1.20/) | Similar prompt templates and answer ordering changed personality measurements in tested ChatGPT and Llama2 models. | Self-declared scores alone cannot establish behavioral continuity. Robustness to prompt variations needs direct evaluation. |
| [LLM Agents in Interaction, Frisch and Giulianelli, 2024](https://aclanthology.org/2024.personalize-1.9/) | GPT-3.5 agents with different profiles showed differing consistency and linguistic alignment in collaborative writing. | Partner influence is a relevant test condition. Cooperation quality and persistence across unrelated tasks do not follow from these findings. |
| [CAPE, Sandhan et al., EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.563/) | Conversational history increased response consistency while shifting measured personality in a seven-model evaluation. | Consistency with recent dialogue and continuity with an originating character are separate questions. This is not a longitudinal deployment study. |
| [Principled Personas, Luz de Araujo et al., EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1364/) | Across nine models and 27 tasks, expert personas usually helped or made no significant difference, but irrelevant persona attributes could reduce performance. | Expression and accuracy cannot safely be assumed independent. These expert-role tests supply no numerical risk estimate for OCEAN fragments. |
| [When “A Helpful Assistant” Is Not Really Helpful, Zheng et al., EMNLP Findings 2024](https://aclanthology.org/2024.findings-emnlp.888/) | Role prompts did not improve aggregate factual accuracy in the tested setting. Automatic role selection often failed to match the best role chosen after outcomes were known. | A persuasive explanation of a selection does not establish its quality. Factual tests based on role labels are narrower than continuing trait-shaped personas. |

**Assessing persona-compatible responses.** [PersonaGym, Samuel et al., Findings of EMNLP, November 2025](https://aclanthology.org/2025.findings-emnlp.368/), evaluates ten LLMs using 200 personas and 10,000 questions. Its dimensions are expected action, action justification, linguistic habits, persona consistency, and toxicity control. The [proceedings methods and human-validation study](https://aclanthology.org/2025.findings-emnlp.368.pdf), inspected on 9 October 2026, support assessing persona-compatible responses across several dimensions.

The actions in that study are described in answers; they are not executed professional work. Agreement with human ratings supports that bounded response assessment. It establishes neither an infallible judge nor proof that a plausible explanation caused an action. The study tests neither longitudinal learning from self-authored characteristic fragments nor this design's whole-persona usefulness. It adds no runtime evaluator or character controller.

Positive and cautionary findings use different methods and configurations. They support testing, rather than a blanket endorsement or rejection of persona prompting. Recognizable voice, observable choices, useful work, and safe adaptation need separate evidence.

**Warmth and truthfulness.** A five-model study found that warmth fine-tuning reduced factual reliability and increased agreement with false user beliefs, even while standard capability and refusal tests mostly remained stable. Follow-ups on three models that changed prompts only showed smaller, less consistent trade-offs. The studied models, definitions, and controlled questions establish neither that warmth requires deception nor an effect size for this design. They motivate testing tact and truthfulness together, including under emotional pressure. [Ibrahim, Hafner, and Rocher, Nature, 29 April 2026](https://www.nature.com/articles/s41586-026-10410-0)

Research on sycophancy found that agreement with a user's view can attract preference even when it sacrifices correctness. Applying that finding to self-authored files is an inference: praise, silence, and repeated selection could reinforce a mistaken lesson without any weight update. None is independent evidence of truth or beneficial causation. [Sharma et al., 2023](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models)

**Continuity over longer interactions.** Extended synthetic role-play studies report declining persona fidelity alongside changes in instruction following and refusal behavior. Some drift can restore desirable boundaries; stronger preservation of a flawed persona would not be success. These fictional-role experiments, assessed by model judges, motivate separate measures of fidelity, capability, and safety. They do not prove a result for assistant OCEAN traits. [Persistent Personas?, v2, 2026](https://arxiv.org/html/2512.12775v2)

The ANCHOR preprint separately audits persona enactment and trajectory recall in 2,008 synthetic conversations across 27 personas and four models. Its tested memory conditions did not consistently resolve continuity failures. Questionnaire judgments sometimes disagreed with turn-level assessments. English-language, template-generated interactions and dependence on evaluators limit transfer to actual companion use or this architecture. The results motivate distinct longitudinal measures. They neither prove that all memory designs fail nor justify describing unsupported drift as development. [Best Friends, Not Forever, v1, July 2026](https://arxiv.org/html/2607.28818v1)

### Structured tool arguments and irrelevant context

Selecting the right tool does not establish that its proposed arguments are appropriate. Irrelevant context can be assessed at that more specific level while preserving legitimate discretion over methods and tools.

[Memory-Induced Tool-Drift in LLM Agents, v1, 24 May 2026](https://arxiv.org/abs/2605.24941v1), §§3.1–3.4, reports drift in generated structured tool-call parameters under adversarially selected irrelevant user-memory context. The main condition constrains tool invocation. Copied MCP schemas are evaluated without live server execution, so the result concerns proposed calls, not observed effects or deployment prevalence. Its memory frameworks differ from this design's characteristic fragments and neutral assets.

The narrow design inference is to inspect argument-level drift within an otherwise correctly selected tool, using the existing comparisons that distinguish facts and authority from discretionary choices. Schema validity alone does not establish appropriate arguments. Personality-shaped methods and tool preferences remain intended where discretion exists. The study establishes neither beneficial persona choice nor maturation and adds no evaluation minimum.

## Trait composition and collaboration: direct evidence and limits

Some studies now connect persona prompting to task outcomes and partner choices, beyond recognizable dialogue. They do not establish that increasing trait diversity generally helps.

A team's average trait level is different from the variation among its members. Trait differences are also different from assigned roles, skills, available information, modeled emotions, underlying model differences, and extra attempts using randomness in generation. If a study changes several of these together, a gain cannot be attributed specifically to OCEAN diversity or VAD.

| Primary study and inspected version | Direct evidence | Important limit |
|---|---|---|
| [When Does Personality Composition Matter for Multi-Agent LLM Teams?, v2, July 2026](https://arxiv.org/html/2606.27443v2) | Big Five prompting changed communication and task-dependent outcomes across coding, research, and bargaining. Structured offer and acceptance actions were observed separately. | Most teams had homogeneous profiles, testing trait level rather than diversity. Neutral wording weakened important low-agreeableness effects. The small heterogeneous pilot does not establish a beneficial critic placement. Milestone and judged code-quality scores do not establish comprehensive executable correctness. |
| [Agents with Feelings?, v1, July 2026 preprint](https://arxiv.org/html/2607.05659v1) | In fixed three-agent software workflows, some mixed profiles achieved better peak results than shared profiles. Profiles also changed revision and token use. | Traits, emotions, derived work styles, and roles were combined. Mixed configurations recombined the top three shared profiles selected separately for each model/task pair. Searching for the best configuration on the evaluated tasks is not validation on held-out tasks. Equal revision limits did not equalize total resources. Review BLEU measures overlap, not defect validity. |
| [Not Birds of a Feather, v1, July 2026 preprint](https://arxiv.org/html/2607.19785v1) | Claude Haiku 4.5 hosts selected strongly by personality archetype despite randomized aliases/order and a statement of equal capability. | Measures selection from profile descriptions, not actual acceptance or delivered contribution. Shared model identity and stipulated capability equality do not establish equal realized competence. Wording and trait overlap limit interpretation. Human-team correlations do not prove an LLM selection was wrong. |
| [Agent-to-Agent Theory of Mind, Choi et al., EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1471.pdf) | Revealing a judge's model identity often improves its preference score in the tested prompts. | Those score gains do not establish independently assessed quality gains. This model-identity study motivates declaring what evaluator information was exposed. It does not justify hiding legitimate collaborator context or adding a production judge. |
| [Emergent social conventions and collective bias in LLM populations, Ashery et al., Science Advances, 14 May 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12077490/) | Local repeated naming-game interactions produce conventions and model-dependent collective biases. | Arbitrary equivalent names test coordination, not truth or enduring character. Motivates controls that replace or remap partners. Agreement can be useful. |
| [Beyond Symmetric Agents, v1, September 2026 preprint](https://arxiv.org/html/2609.35875v1) | In its small-model benchmark setting, debate showed no general advantage over independent sampling with the same roster. Personas often hurt performance, while greater persona diversity recovered some loss. | Generation-budget matching approximately equalized generated tokens, but debate consumed more total tokens and time. This is not an equal-TOTAL-resource result. Its reasoning personas are not validated OCEAN variation, and benchmark debate differs from complementary tool work. |

These findings motivate separate observations of invitation, actual acceptance, delivered work, and independently useful contribution. More revision need not improve the result, and a correct minority contribution can be lost in the final output. A plausible explanation of complementarity, or success by a selected profile, cannot by itself establish useful collaboration.

A diversity-benefit claim needs the relevant matched comparison. Profiles and selection procedures must be fixed before held-out evaluation, and resource accounting must be complete, as described in the [evaluation method](../evaluation/README.md).

**Learning from peers.** A common-resource simulation combined payoff-biased social learning with group norms and punishment. Retaining group decisions without social learning sometimes outperformed the full system; copying apparent short-term winners could destabilize cooperation. This motivates testing a useful-looking peer method against delayed group outcomes. The model-sensitive simulation establishes no requirement for voting, punishment, or a central norm in every team. [Gupta et al., v1, October 2025 preprint](https://arxiv.org/html/2510.14401v1)

None of these studies validates the complete persistent-fragment architecture. They justify no compulsory diversity, fixed trait-to-role assignments, leader or critic, debate, voting, or extra reflection calls. Working alone, declining a request, and rejecting unsupported peer advice remain compatible with useful character and cooperation under the [work boundaries](../design/WORK-AND-BOUNDARIES.md).

## Experience, reflection, and evolving context

Studies of retained observations, feedback, and guidance provide evidence about individual parts of an adaptation loop. Their benefits and failures help frame comparisons, but their memory mechanisms do not define the persona in this design.

| Primary source and version | Component-level support | Difference from this design |
|---|---|---|
| [Generative Agents, Park et al., v2, 2023](https://arxiv.org/abs/2304.03442v2) | Observation, planning, and reflection contributed to perceived believability in a 25-agent simulated town. | Sandbox believability does not demonstrate factual reliability, subjective experience, or safe real-world autonomy. |
| [Reflexion, Shinn et al., v4, 2023](https://arxiv.org/abs/2303.11366v4) | Retained textual feedback improved subsequent trials in studied tasks without updating model weights. | Supports adaptation informed by experience. It does not support rewriting identity on every call or claiming online model training. |
| [MemGPT, Packer et al., v2, 2024](https://arxiv.org/abs/2310.08560v2) | Model-directed management of memory tiers was evaluated in document analysis and multi-session chat. | Supports distinguishing stored material from supplied context. It does not establish equivalence between lexical files and its retrieval system. |
| [A-MEM, Xu et al., v1, 2025](https://arxiv.org/html/2502.12110v1) | Contextual notes, links, and revisions use embedding candidate retrieval and model judgments. Retrieval also uses dense vectors. | Evolving associations are relevant precedent. The study does not evaluate a lexical-only, primary-persona cue network or establish bounded lifetime storage; those results cannot be inherited. |
| [Large Language Models Cannot Self-Correct Reasoning Yet, Huang et al., v2, 2024](https://arxiv.org/abs/2310.01798v2) | Intrinsic correction without external feedback sometimes failed to improve reasoning or degraded it in the studied settings. | Motivates reliable observations and checks. It is not a timeless claim that every model fails at self-correction. |
| [Belief Memory, Liao et al., v2 preprint, 8 May 2026](https://arxiv.org/html/2605.05583v2) | With supplied valid/noisy observations, retaining alternatives improves a diagnostic in which the correct conclusion outranks the flawed one at retrieval. | Tests neither voluntary evidence seeking nor completed environment work. Its probabilistic memory and retrieval machinery are not adopted. The inference here is to distinguish delivered counterevidence from a chosen bounded check. |
| [On Safety Risks in Experience-Driven Self-Evolving Agents, Zhao et al., ACL Findings 2026](https://aclanthology.org/2026.findings-acl.2091/) | Experience from benign tasks increased unsafe action tendencies in studied web and embodied systems. Refusal experience reduced this effect while increasing over-refusal. | Successful permitted experience is not automatically a safe general policy. These memory frameworks neither test OCEAN fragments nor prove external authorization gates ineffective. |

These adjacent systems motivate examining reusable interpretations and correction. None validates the complete combination of semantic OCEAN, distinct VAD, characteristic fragments, primary-model selection, and explicit maintenance on every persona invocation. Repeated self-generated interpretation is not independent corroboration. Routine tentative authorship may still be useful, but a claim of improved behavior requires stronger evidence than the existence of a fragment.

**Repetition and evidence.** Two recent preprints clarify different repetition effects without settling this design's question:

- [Beyond Memory Majority, v1, August 2026](https://arxiv.org/html/2608.19701v1) studies correlated multi-agent memories that share upstream evidence and can form a false majority. This is relevant to duplicated evidence ancestry, but differs from confidence change within one persona.
- [Illusory Truth or Mere Exposure?, v1, September 2026](https://arxiv.org/html/2609.36278v1) finds model-dependent effects of repeated claims on truth ratings, including a null result for GPT-5-nano. Its social-media simulation does not test persistent file maintenance.

The reviewed work does not directly isolate repeated same-primary-model maintenance, with fixed external evidence and preserved lineage, as a cause of confidence inflation. That remains a product hypothesis. A fresh thinking invocation may reach a better qualified inference from unchanged evidence, but it must not count its own repetition as a new observation. Exact replay of an already accepted result is a separate integrity case.

A valid dispatch gate can likewise contain an unsafe proposal without demonstrating improvement in the model's learned judgment. Proposed behavior and actual released effects need separate evaluation.

### Reciprocal development from actual work and interaction

The design treats development as a possible exchange between character and experience: tendencies shape encounters, and actual encounters may support changes in how the persona approaches later work. It does not use elapsed time as evidence of growth.

A human longitudinal study found that personality at 18 predicted work experiences at 26, while those experiences were associated with changes in the same traits. This supports a bounded reciprocal analogy. The study used human personality measures, including the MPQ, and observational associations. It supplies neither a causal software mechanism nor an OCEAN aging schedule. Calendar age, invocation count, and archive size cannot stand in for demonstrated persona development. [Roberts, Caspi, and Moffitt, 2003, original article](https://dunedinstudy.otago.ac.nz/files/1597809897335.pdf)

**The intended reciprocal loop.** Within ordinary authorized work:

- Current character shapes discretionary attention, context searches, methods, human communication, and peer cooperation.
- Actual results, correction, disagreement, and received responses can justify primary-persona revisions to its own fragments.
- Relevant accepted fragments, when actually supplied again, can affect later choices, including how the persona searches and organizes its context.
- Meaningful experience may support a permitted current-character proposal under the existing acceptance and fresh-decision boundaries.

These are intended relationships among existing parts. They require neither a compulsory sequence nor another decision engine.

**Different kinds of change.** Method refinement, relationship-specific adaptation, transient affect, and broader character revision remain distinct. A peer's assertion records what the peer said. Praise may support a communication preference without verifying a technical claim. Preserving character does not require stubbornness, and adapting does not require agreement.

An appropriate outcome may be consolidation, a narrower lesson, retirement, reversal, or no durable change. Dormancy supplies no unseen experience. Accepted text changes provide adaptation through context; they do not automatically train weights or prove beneficial maturation.

**Continuing controls.** A locked character still permits compatible method refinement. It does not permit effective character replacement through changes scattered across fragments. Existing permission, commitment, and accepted-warning obligations remain in force.

## Files and primary-model context choice

Ordinary files make persona-authored material inspectable and give the persona a direct way to maintain it. The research below supports parts of that choice. Each source studies a different system, so its results carry specific limits.

- The [Agent Skills specification](https://agentskills.io/specification), inspected 8 October 2026, packages readable instructions with optional supporting resources that can be loaded as needed. It offers an interoperability precedent. It does not show that a skill was learned or that every persona file should use this packaging.
- The [official ripgrep guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md), inspected 8 October 2026, documents literal text matching, regular-expression matching, and exclusions such as ignored and hidden paths. These exclusions explain why a search must declare its eligible files and limits. A no-match result describes that searched scope; it does not show that no relevant experience exists.
- [Is Grep All You Need? How Agent Harnesses Reshape Agentic Search, v1, 2026](https://arxiv.org/html/2605.15184v1) compares retrieval across agent harnesses and ways of delivering results. Its prepared corpus and Chronos condition—including category-conditioned guidance and initial vector context—limit how the results transfer. The study motivates controlled interface comparisons, not a claim that lexical search is universally better.
- [PRO-LONG, v2, 2026](https://arxiv.org/html/2607.20064v2) studies programmatic access to an interaction log that keeps appending all interactions, for long-horizon game reasoning. That external record serves a different purpose from a persona authoring selective interpretations and identity. Its results do not establish autonomous first-person file maintenance.
- [LifeMem, v1, 2026](https://arxiv.org/html/2609.12655v1) combines retained trajectories, workflow clustering, and distilled textual skills. It motivates keeping raw experience, authored lessons, and reusable methods distinguishable. Its retrieval and distillation mechanism differs from this design.

**The chosen interface.** Current notebook navigation uses only filesystem grep/search/regex chosen by the primary model, together with exact reads. This is lexical discovery: it matches text or text patterns. Synonyms, implicit themes, a growing collection, and stale guidance can all make relevant material hard to find. Query expansion and links do not prove complete recall.

Graph, vector, and auxiliary semantic discovery may be studied as explicitly different evaluation comparators, with matched permissions and total cost. They are not adopted production fallbacks; adding one would require a design change. The lexical design inherits neither their measured benefits nor an exemption from evidence that lexical retrieval can miss relevant material and perform worse.

**Evidence about scale.** [Li et al., Beyond Semantic Similarity, v1, 3 May 2026](https://arxiv.org/abs/2605.05242v1), §4.3, studies direct interaction with a corpus through file search and reads. Its experiments need to be kept separate:

- DCI-Agent-Lite’s constrained read-plus-grep ablation is competitive on a BrowseComp-Plus subset.
- Separate DCI-Agent-CC scaling experiments show worsening accuracy and rapidly rising navigation cost as distractors increase.

Finding evidence and using it successfully are different achievements. These results motivate testing the operating limits of lexical discovery; they do not guarantee discovery, persona benefit, or transferable cost savings. The harness-specific context handling and open-shell interaction used in broader experimental arms are not adopted here. Those arms are different experimental systems, not one measured configuration.

### JSON serialization and lexical matching

Searching stored JSON text can produce a different result from searching its decoded string values. An adapter must make clear which surface it searches and how it interprets patterns.

[RFC 8259 (December 2017), §§4, 7–9](https://www.rfc-editor.org/rfc/rfc8259) distinguishes serialized escapes from decoded string values. It recommends unique object names and describes interoperability problems involving duplicate names and non-Unicode strings. It also permits parser limits on size and depth. This design chooses a stricter profile for accepted fragments and declares the searched surface. The RFC itself neither requires that fragment representation nor makes duplicate members universally invalid JSON syntax.

The [official ripgrep 14.1.1 guide](https://github.com/BurntSushi/ripgrep/blob/14.1.1/GUIDE.md) describes text search and filtering; it does not provide automatic decoding of JSON values. The [regex 1.11.1 syntax documentation](https://docs.rs/regex/1.11.1/regex/#syntax) distinguishes regex escapes and flags that affect line anchors and the dot pattern. These pinned versions illustrate why an adapter must declare its actual search engine, flags, and searched surface. They do not require either package.

An adapter may deterministically expose decoded fields for lexical search. That projection still needs a binding to its source, declared limits, and acceptance evidence of its own. None of these sources establishes persona development or reliable discovery. The exact rules are in the [contract](../implementation/CONTRACTS.md#json-text-and-matching-surfaces); the [hypothetical escape contrast](../examples/WORKED-EXAMPLES.md#a-json-search-miss-is-not-missing-characteristic-meaning) illustrates the distinction.

### Need-directed supporting context

The primary persona can use the same bounded search-and-read interface for characteristic fragments and supporting resources. Their purposes remain separate: fragments help define the persona; resources supply such things as knowledge, procedures, tools, and records.

**Normal selection.** The chosen design begins with necessary character, work, and policy state plus a small discovery surface. It does not begin by giving the LLM hundreds of tool or skill names and descriptions to filter. The bulk registry stays outside both the request sent to the provider and the context visible to the model.

The primary persona requests either a lexical search directed at a need or an exact known resource. It receives bounded candidates and chooses what to load or retain for its next decision. Host-side indexing and matching enforce scope and limits; they do not add a hidden semantic selector.

**What each step establishes.** Discovery, description, exact loading, accepted selection, authorized execution, and observation are distinct events. They need not require separate round trips. A known exact reference can bypass rediscovery, and a current, fully qualified callable interface can support direct authorized use. The following distinctions still apply:

| Available information | What it establishes—and what remains unresolved |
|---|---|
| A search match | A candidate was found. Applicability and permission remain to be established. |
| No match | Nothing matched within the declared search scope and rules. |
| A preview | Some descriptive content was supplied; this is not a full read. |
| A stored script | A file exists; installation and current executability remain separate questions. |
| An old successful run | A past execution succeeded; present availability remains unproven. |

These distinctions extend the [work boundaries](../design/WORK-AND-BOUNDARIES.md) and [contracts](../implementation/CONTRACTS.md). They do not create another resource protocol.

**The next-call bound.** One allowance covers everything needed for the next call: candidate metadata, selected fragments, evidence, operative guidance, callable schemas, provider expansions, results, continuing history, and required qualifications. A limit on result count cannot contain an enormous individual definition or the accumulation from repeated searches. Reassembly must also prevent provider history or caches from accumulating every previously loaded resource.

Request bytes, actual model-visible context, billed tokens, host scans, storage, elapsed time, and monetary exposure are different measurements. Required meaning and qualifications must fit faithfully. If they do not, admission of the affected material or operation blocks; a smaller preview cannot substitute for complete operative guidance.

#### Direct tool-discovery evidence

Tool-discovery studies help distinguish finding relevant candidates from finding everything needed for an authorized solution. They do not yet test this design’s bounded, primary-owned discovery loop.

[ToolRet, Findings of ACL 2025](https://aclanthology.org/2025.findings-acl.1258.pdf) distinguishes fractional target recall—finding some annotated targets—from completeness, which requires finding every annotated target. This supports the existing complete-valid-path measure: many relevant hits can still omit a prerequisite, while an alternative authorized solution path remains valid.

ToolRet’s instruction-assisted inputs were written with the target tools available to the writer. Their gains therefore do not establish unaided discovery from a cold start. Its static ranked BM25 results also do not evaluate a primary model that adaptively chooses literal or regex searches. Several dense-retrieval baselines underperformed BM25. The study establishes neither lexical sufficiency nor universal dense-retrieval superiority.

[T-Eval v2, 4 January 2024](https://arxiv.org/html/2312.14033v2) separates tool-use competencies. However, its named retrieval subtask supplies both a tool list and the beginning of a verified solution, then asks for the next tool. That is a diagnostic of assisted selection, not discovery from an unfamiliar catalog.

Both papers were independently inspected on 8 October 2026. They sharpen attribution under the existing [evaluation](../evaluation/README.md), without adding numerical targets, an embedding engine, or a new requirement family. This design’s discovery loop remains untested.

Two later preprints motivate additional controls:

- [ToolScout v1, 17 August 2026](https://arxiv.org/html/2608.16502v1) reports dense-retrieval failures associated with the source style of query–tool pairings and representations. Rewriting only queries does not reproduce the full effect, and lexical controls vary by source.
- [SkillSight v3, 14 August 2026](https://arxiv.org/html/2607.18785v3) studies bias associated with shared generic descriptions. Its progressive-disclosure comparison begins with the top 50 BM25 candidates, and its costs depend on the model.

These findings motivate the proposed held-out-authoring controls and boilerplate/style controls matched for meaning and length. They do not justify a hidden selector or supply an inherited result for lexical discovery or lower cost.

### Provider and standards fit

Provider interfaces can help implement selective loading, but their defaults do not necessarily satisfy this design’s exposure boundaries. The application must account for what it sends to the provider, what the model sees, and what remains available in later turns.

The following mutable primary documentation was independently inspected on 8 October 2026. Inspection dates are not publication dates, and dated tool identifiers are not documentation versions. These are component interfaces and integration recommendations, not tested AI Personas adapters.

| Primary source | Behavior verified in that inspection | Fit with the chosen design |
|---|---|---|
| [OpenAI tool-search guide](https://developers.openai.com/api/docs/guides/tools-tool-search), current undated page | Individually deferred functions still expose names and descriptions initially; namespaces can hide individual details. Client-executed search permits application-controlled loading. Loaded tools can remain callable in later turns, and changing that set affects caching. | Client control offers a useful integration point. It does not prove lexical discovery, bounded previews, or primary-owned selection. Hundreds of deferred individual descriptions still violate the chosen exposure boundary. The actual loaded set and later continuation must be bounded. |
| [Anthropic tool-search guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool), regex/BM25 identifiers dated 20251119 | The deferred catalog is still supplied in the API request. Returned references automatically expand into full definitions, including with custom reference-based search. History can retain those expansions. | Deferred model-input tokens and transmitted request bytes are different measures. Native references are not inert previews, and a full-catalog request does not meet this design’s stronger transport boundary. Use bounded ordinary search results and explicit application-controlled loading instead of assuming native conformance. |
| [Agent Skills specification](https://agentskills.io/specification) and [client integration guide](https://agentskills.io/client-implementation/adding-skills-support), current undated pages | Instructions and optional scripts, references, and assets support progressive loading. The described startup approach nevertheless includes metadata for all skills. The optional allowed-tools field is experimental and implementation-dependent. | Readable packages and resources loaded as needed are useful precedents; global catalog loading must be replaced with bounded discovery. Imported guidance retains its author and restrictions. Package metadata cannot grant execution authority or prove runtime availability. |

Provider-native deferred loading can be an evaluation comparison. It does not guarantee the required boundary or lower total cost. An adapter that cannot bound automatic expansion and continuing context before admission cannot claim the hard next-call bound. None of these interfaces justifies adding a hidden reflector, vector engine, automatic resource traversal, or alternate semantic author.

### Supporting-resource lifecycle evidence

Track a resource’s identity, availability, restrictions, and lifecycle state through discovery, reading, execution, change, and retirement. Establish readiness for the particular proposed operation; a resource may legitimately be unavailable, uninstalled, revoked, retired, or erased. Protocol features support parts of that lifecycle; the application still has to enforce this design’s bounds and authority rules.

**Listing, reading, and availability.** In the independent check on 8 October 2026, the current MCP version resolved to **2026-07-28**. Its [resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources) and [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) define paginated listing, resource reads, and tool interfaces. They do not define this design’s lexical-search contract.

One resource read can return multiple contents, so one URI does not establish a size bound. Tool availability can vary with authorization, names can collide across servers, and untrusted annotations remain untrusted. A bounded lexical adapter and an independent execution gate remain design obligations; the protocol does not provide those guarantees automatically.

**Change notifications and caches.** The version’s [subscription mechanism](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions) acknowledges which subset of requested notifications it supports. Delivery depends on a live subscription, which ends when the transport closes. Requesting a watch, or losing one, cannot establish current coverage or unchanged state.

Its [caching rules](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching) require hints for relevant completed list/read results, restrict private reuse to the same authorization context, and provide no consistency guarantee across pages. A time-to-live value, or TTL, is a freshness hint; it does not make content immutable. Permission to reuse stale material does not satisfy a claim that needs fresh evidence. Earlier 2025-11-25 protocol descriptions remain historical and must not supply current subscription or cache semantics.

**Execution identity and dependencies.** [SLSA build provenance v1.2](https://slsa.dev/spec/v1.2/build-provenance), inspected on the same date, distinguishes build inputs, resolved dependencies, execution platform, and outputs. It also qualifies how complete the dependency account is. This motivates identifying the actual script, environment, dependencies, data revision, and execution result instead of relying on a filename or hash alone. Borrowing that distinction makes no claim of SLSA conformance, reproducibility, or safety.

Required guidance, executable dependencies, source restrictions, and data derivation involve different dependency sets. None automatically requires putting every ancestor into model context. Code and bulk data can remain outside context when an authorized runner bound to the relevant versions consumes them and returns adequate, bounded evidence.

**Retention and authorship.** Resource copies, dependency caches, snapshots, indexes, and execution records remain within declared retention and accounting boundaries. Deselecting, retiring, and erasing material mean different things. Organizing an imported resource does not change its authorship; summarizing restricted evidence does not remove its restrictions. The whole-store and derivative-retention account below also applies to these supporting resources.

#### Generated reusable assets: empirical limits

Generating a useful tool, finding it later, and benefiting from reuse are separate achievements. The first four studies below were independently inspected on 8 October 2026; the later additions were inspected on 9 October. Their component results motivate separating executable reuse from persistent learning.

- [Voyager v2, 19 October 2023](https://arxiv.org/html/2305.16291v2) used a generated skill library to solve four unseen Minecraft tasks in fewer prompts. The library condition passed 12/12 trials; the no-library ablation already passed 11/12. This supports an efficiency benefit from reuse without attributing all competence to the library. Its embedding retrieval and auxiliary models differ from this design’s lexical discovery and single-primary authorship.
- [LATM v2, 11 March 2024](https://arxiv.org/html/2305.17126v2) improved GPT-3.5 task accuracy with tools made by GPT-4. GPT-3.5 nevertheless failed to author tools that passed validation on several studied tasks. Using a tool, constructing it, and generalizing are distinct achievements. The study’s stronger maker, cheaper user, separate dispatcher, and amortized creation cost do not establish savings for this architecture.
- [ToolMaker v1, 17 February 2025](https://arxiv.org/html/2502.11705v1) adapted scientific repositories into callable wrappers and environment snapshots. It outperformed its comparator while spending more on creation. An unseen mask-token input exposed a partially correct tool. This motivates qualified claims about input coverage and evidence about the executable environment; it does not establish robustness to later dependency changes. Generated wrappers do not make the underlying software model-authored.
- [SkillsBench v4, 14 June 2026, Appendix D.6](https://arxiv.org/html/2602.12670v4) does not isolate the causal effect of generated-asset quality. Its self-generation diagnostic mixes several cases: packs that were not discovered or used, authoring that displaced task work, incorrect guidance, and instance-specific leakage. Missing trial slots, incomplete creator traces, different creation/reuse protocols, and one effort-setting mismatch further limit interpretation. Neither success nor failure cleanly measures reusable knowledge. Percentages from earlier versions are not substituted for this analysis.
- [SkillCraft v2 preprint, 10 March 2026](https://arxiv.org/html/2603.00718v2) combines reusable tool compositions with keeping intermediate data outside model context. Its cost comparison includes only tasks both arms solve, and hierarchical results vary by model. This motivates a comparison with an equivalent helper that is not retained, plus accounting for every attempt. It does not justify attributing every saving to durable learning.

These findings support the existing [evaluation](../evaluation/README.md) distinctions among attributable construction, held-out generalization, autonomous discovery, exact supply, current executability, and adequate outcomes. Evaluation must count failed candidates, candidates never reused, and actual lifecycle cost. Later reuse cannot conceal work displaced from the original task.

None of these studies demonstrates persona continuity, beneficial every-call asset maintenance, or the complete primary-owned loop. They add empirical rationale, not another author, retrieval engine, invariant, or production testing ritual.

**Poisoned derivatives and cleanup.** [SkillJack v2 preprint, 7 August 2026](https://arxiv.org/html/2608.03509v2) studies poisoned trajectories transformed into skills that can outlast cleanup of their source. Its routing/detector and code-inspection endpoints are not observations of live compromise. [Reflections on Trusting Trust, Revisited v1 preprint, 15 September 2026](https://arxiv.org/html/2609.17817v1) shows selected poisoned-checker cases yielding unsafe later code. Its DGM case required a researcher modification outside the stated attack model.

These studies motivate a joined source→asset→cleanup→reuse fixture and a control using authentic but misleading feedback. They establish neither prevalence, this design’s vulnerability, nor complete defenses. Removing a source, withdrawing a derivative, proposing an unsafe action, and releasing an effect remain different observations under the actual authority and retention rules.

### Compact associative fragments and selective retention

The intended fragment collection is a compact, changing set of prompt parts that helps define the persona. Useful associations appear in ordinary prose and grep/search/regex cues. Compactness serves the assembly of useful characteristic context; factual recall is a supporting concern.

The primary LLM decides which associations to pursue and what meaning to retain. This aim requires no automatic host traversal, mandatory graph database, separate semantic selector, fixed folder taxonomy, or extra reflection call. The component evidence supports testing the choice; it does not validate the combined architecture.

| Primary source and inspected version | Relevant finding | Transfer boundary |
|---|---|---|
| [ReadAgent, v1, February 2024](https://arxiv.org/html/2402.09727v1) | Gist memory plus model-directed lookup improved studied long-document comprehension relative to its baselines. | The main design supplies the complete gist collection and retains original passages for lookup. Bounded lookups and smaller prompts do not establish a bound on total retained storage. |
| [LongMemEval, v1, October 2024](https://arxiv.org/html/2410.10813v1) | Compressing values into facts lost information and harmed overall performance, although multi-session reasoning benefited. Adding extracted facts to keys while retaining original values helped retrieval and answering. | Its tested dense retrieval beat BM25. The findings support assessing discovery, reading, and compression separately. They establish neither lexical-only equivalence nor an optimal fragment size for this design. |
| [The Vocabulary Problem, Furnas et al., 1987, original article](https://zhang.ist.psu.edu/teaching/504/readings/Furnas.pdf) | Human word choices varied greatly across five application domains. Richer alternative access terms improved the studied access methods. | This is human–computer interaction evidence, not validation of an LLM cue network. Selective alternative wording is a design inference; unlimited aliases would conflict with compact retention. |
| [Memora, From Recall to Forgetting, v1, April 2026](https://arxiv.org/html/2604.20006v1) | Remembering, reasoning, and recommendation tasks over simulated histories expose reuse of obsolete or invalidated information. Its forgetting-aware evaluation penalizes that reuse. | The benchmark motivates checking harmful revival as well as recall. It does not establish verified erasure, deletion rights, a universal forgetting score, a retention policy, or a scientifically optimal decay curve. |

**Three kinds of connection.** Search cues, evidence references, and required qualifications serve different purposes:

| Connection | Its role |
|---|---|
| Authored query cue | Suggests where to look. It does not assert that a match exists or endorse every result. |
| Exact citation | Identifies the evidence or revision supporting a claim, so the claim can be traced. |
| Mandatory qualification | Determines whether guidance may be supplied as usable at all, preserving its applicability and restrictions. |

One cannot substitute for another. An accepted warning cannot become optional by being phrased as a search suggestion. A changed query result does not change an already accepted exact selection.

The primary persona may revise an unhelpful cue, follow a useful connection, or stop within the declared cumulative allowance. Search results remain candidates, distinct from exact inspection, accepted selection, and actual supplied context. A no-match result reports the searched scope and matching rules; it cannot establish that no relevant experience exists.

Evaluation must still consider synonyms, stale wording, broad fanout, cycles, missed isolated fragments, and incomplete indexes. Optional traversal limits do not authorize omitting required qualifications. Source ancestry matters too: several linked descendants of one claim do not provide independent corroboration.

**What compactness must preserve.** Shorter text alone does not establish useful consolidation. Consolidation should retain characterful interpretation, conditions, uncertainty, rare exceptions, unresolved contradictions, and applicable restrictions. Declining a duplicate, merging equivalent guidance, retiring obsolete applicability, and erasing content under policy have different effects. An archive or retirement label does not erase content. Low use or elapsed time cannot silently dispose of an accepted warning, unresolved effect, or current obligation.

**What the storage bound includes.** A whole-store claim covers the declared managed storage that supports persona context and its evidence. This includes fragment bodies and cues; indexes and aliases; archives and versions; provenance and qualification metadata; receipts and caches; managed backups and exports; and the peak temporary copies created during revision.

External storage deliberately used to retain persona context or supporting history remains accountable. If an external tier cannot be measured, the claimed bound is incomplete. Arbitrary recipient copies and a provider’s independent retention after disclosure remain outside promised control and need an honest disclosure boundary.

User-owned deliverables are not expendable fragment storage. Capacity pressure does not authorize changing, deleting, or revoking them. Any deliberate reliance on those artifacts as a supporting storage tier must be disclosed and counted without changing their ownership or authority.

**When a lesson may survive its evidence.** A qualified lesson can outlive raw evidence only when the actual derivative-use and retention policy permits it. The surviving account must distinguish a fallible retained interpretation from proof that can still be inspected. A digest cannot reconstruct lost evidence.

The following limits continue to apply:

- Source expiry does not declassify the source or its restricted derivatives.
- A derivative-deletion requirement also applies to the lesson.
- A surviving disclosure restriction still binds the lesson.
- A use requiring exact evidence becomes ineligible when that evidence is unavailable.
- Deleting a record cannot settle an unresolved commitment or effect.

These are policy and engineering boundaries, not capabilities demonstrated by the cited memory studies.

Strictly bounded total storage cannot promise unlimited exact recollection of an indefinitely growing history. Capacity pressure therefore needs an honest retention, capacity, or admission decision. Hidden archival growth and discarded obligations do not resolve it.

The comparison remains unrun: can selective retention and primary-authored cues preserve useful continuity at acceptable total cost? No reviewed source validates a human-like forgetting mechanism, universal aging rule, or 100% behavioral guarantee for that combination.

## Continuing work and selective clarification

Continuing work needs usable handoffs, checks against premature completion, and questions that are worth their interaction cost. Two primary sources inspected on 10 October 2026 motivate limited comparisons for those needs.

[Anthropic’s long-running harness report, 26 November 2025](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), describes premature completion, unfinished session handoffs, and inadequate end-to-end checking in full-stack coding. Retained progress artifacts and actual checks supported continuation in its engineering demonstration. This is not a controlled general result about whether work will keep making progress. Its scaffolding does not become this design’s controller or prescribed workflow.

[Zhang and Choi, “Clarify When Necessary,” NAACL Findings, 29 April–4 May 2025](https://aclanthology.org/2025.findings-naacl.306.pdf), examines the value of clarification relative to interaction cost across QA, translation, and inference (§2). The evaluation supplies clarifying question/answer pairs tied to gold interpretations. It does not establish that an absent user or simulated peer can provide real intent or consent.

These findings motivate selective questions and explicit assumptions. They do not prescribe the study’s inference method or a universal timeout. The existing revision/regression evidence also prevents treating longer work as guaranteed improvement. Accountable continuation and authority boundaries remain design obligations; these studies do not supply empirical passes for them.

## Questioning, dialogue, and sufficient-for-now judgments

Discussion can help correct an answer, but agreement and additional rounds are not reliable signs that the work is good enough. Three primary studies, inspected 10 October 2026, motivate the existing [sufficiency comparisons](../evaluation/README.md#continuing-work-and-stopping-quality).

- [Du et al., Improving Factuality and Reasoning through Multiagent Debate, v1, 23 May 2023](https://arxiv.org/html/2305.14325v1), §§3.1–3.3 and 5, reports beneficial critique on studied reasoning and factual tasks, including correction of initially wrong answers. It also reports confident incorrect consensus, additional computation, and difficulty with long histories. These older ChatGPT-based experiments establish neither superiority at equal cost nor benefits for enduring characteristic personas.
- [Weng et al., Do as We Do, Not as You Think, v2, 11 February 2025](https://arxiv.org/html/2501.13381v2), §§5 and 7, finds that double-checking can reduce conformity in some studied conditions and reinforce it in others. Its constructed multiple-choice protocols expose participants to a majority view. Those protocols and independence-oriented prompts are neither validated OCEAN/VAD accounts nor estimates of everyday conformity.
- [Kaesberg et al., Voting or Consensus?, Findings of ACL, 27 July–1 August 2025](https://aclanthology.org/2025.findings-acl.606.pdf), §§4.1–4.3, reports task-dependent protocol outcomes. More rounds did not produce steadily increasing benefits; post-decision challenges gave unreliable gains, and computation costs were substantial in its setup. Its objective benchmarks and prescribed protocols do not establish an optimal stopping rule for this design or for subjective work.

Together, the findings motivate testing useful critique, preservation of justified dissent, and full interaction cost. Treating agreement or more deliberation as success would miss those distinctions. This is a design inference, not an AI Personas result. No protocol, numeric threshold, mandatory vote, or guaranteed improvement is imported. Actual decision rights and stakeholder authority remain design obligations.

## Universal consideration and selective mutation are engineering choices

Every persona invocation considers maintenance alongside its work, but a useful outcome may be a reasoned decision to change nothing. The proposed benefit is that omissions become visible at the same response boundary as the work. No separate reflection call is required. The proposed risks are overhead, filler, unsupported inference, and drift. Neither the benefit nor the risks have been measured for this architecture; the [acceptance plan](../evaluation/ACCEPTANCE.md) supplies the intended comparisons.

**What the response covers.** The unified work/maintenance response addresses the work, characteristic-fragment maintenance, supporting-resource maintenance, and next-context choice for both fragments and resources. Supporting-resource consideration includes whether to store, refine, or organize tools, skills, histories, messages, data, scripts, and code. This every-call asset consideration is a user-requested design hypothesis, not a finding established by progressive-loading studies.

Useful proposals identify their intended files or paths. Next-context requests can identify exact resources or bounded search cues. A concise, reasoned no-change disposition can cover both maintenance scopes. Appropriate preservation or no optional need can satisfy next-context choice without a new search or edit. Every accepted response must explicitly address both next-context scopes; omission is invalid under the corrected contracts. Maintenance and next-context choice remain separate judgments.

These response duties come from the design, not the cited studies. Asset organization retains source authorship and truthful history and effect receipts. Generated prose cannot fabricate messages, execution, or experience.

**Which calls count.** Coverage concerns application-visible calls that exercise persona agency, not only user-facing turns. Initialization, discovery, tool follow-ups, coordination, maintenance, and governed repairs can otherwise create gaps. A narrowly isolated non-persona utility is different from a helper making persona decisions. Provider-internal computation is outside observable application coverage. These are scope definitions in the [contracts](../implementation/CONTRACTS.md), not psychological findings or a claim of control over hidden inference.

**Persistence and effects need separate evidence.** [SQLite’s atomic-commit explanation](https://www.sqlite.org/atomiccommit.html), inspected 8 October 2026, shows why crash consistency depends on a protocol and storage assumptions. It does not guarantee arbitrary multi-file edits. [Amazon’s idempotent-API discussion](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), inspected the same day, explains request identity and ambiguity during retries. It does not make a local commit atomic with an external action.

The [OpenAI Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs), inspected 8 October 2026, distinguishes structured output from semantic correctness and covers refusal handling. A constrained output format cannot guarantee truthful maintenance, complete provider output, successful storage, or an external effect. This note adopts no provider-specific output feature.

**Retained context can carry attacks.** [AgentPoison, v1, 2024](https://arxiv.org/abs/2407.12784v1) studies poisoned memory or knowledge bases. [MINJA, v5, 2026](https://arxiv.org/abs/2503.03704v5) studies query-only memory injection. The reach of these attacks depends on access to the affected memory or an interaction path that can populate it. The studies do not estimate prevalence in isolated persona stores.

They motivate source lineage, retention boundaries, and independent authorization checks. They neither validate complete defenses nor show that ordinary files are immune. Fluent own-voice wording cannot give an untrusted instruction authority. Correct provenance makes a source traceable; it does not establish that the source supports every inference drawn from it.

## Waveform-tool illustration source limits

The waveform example is a fictional tool-choice exercise. Its simulator capability distinctions have a source; its runner behavior and results remain fixture terms.

The [separate tool-choice extension](../examples/WORKED-EXAMPLES.md#competing-tools-for-a-separately-authorized-waveform-study) draws only its simulator capability distinctions from the official [ngspice User’s Manual 45, 1 September 2025](https://ngspice.sourceforge.io/docs/ngspice-45-manual.pdf), inspected 10 October 2026. The relevant sections cover analysis types (§1.2), convergence (§1.4), version identification (§13.5.104), circuit setup (§17.1), and installation (§28).

This pinned manual is not a current-release recommendation or evidence of installation or readiness. Runner interfaces, permissions, edge conventions, tolerance, and observations in the story are explicitly fictional fixture terms. Numerical agreement under a shared wrong premise would not independently qualify the model or physical hardware. The procedural-asset research above does not validate this engineering transfer.

## Printer continuation source boundaries

The printer walkthrough illustrates how judgment might transfer to a new task. It does not qualify a printer design or report physical testing.

The [circuit-to-printer walkthrough](../examples/WORKED-EXAMPLES.md#from-the-circuit-encounter-to-a-printer-concept) uses synthetic power, waveform, and footprint inputs. Its numerical outcomes are derived from those inputs, not manufacturer measurements. The 25% capacity allowance is an adopted fixture criterion.

Primary sources consulted on 9 October 2026 support the unresolved integration concerns. They do not support selecting or qualifying this fictional printer:

- [Klipper Configuration Reference](https://www.klipper3d.org/Config_Reference.html) describes duty-based heater limits, temperature ranges, heater verification, and shutdown-related settings. These motivate distinguishing sensing, control, and protection. They do not qualify the power stage or guarantee detection of every fault.
- [Prusa’s i3 thermal-runaway explanation](https://help.prusa3d.com/article/thermal-runaway-i3-series_2131?product=mk3s) explains how displaced temperature sensing can misrepresent heating and describes model-specific protection. It supports checking sensor attachment and fault response without importing its thresholds into another printer.
- [Klipper Resonance Compensation](https://www.klipper3d.org/Resonance_Compensation.html) discusses mechanical problems and tuning tradeoffs. Software compensation does not establish adequate stiffness or correct an arbitrary mechanical defect.
- [NIOSH, Approaches to Safe 3D Printing, November 2023](https://stacks.cdc.gov/view/cdc/135072) provides a hazard/control framework that includes emissions and ventilation. It motivates a fresh review of siting and exposure. It does not establish that PLA, an enclosure, or a ventilation installation is safe.

The vendor and project pages are living documentation, not pinned versions. No hardware operation or setup procedure was performed. Actual parts, ratings, geometry, protection, firmware-specific behavior, and physical verification require separate evidence. The transferable method concerns useful judgment and communication. The earlier ideal inverter supplies no printer circuit or domain qualification.

## What remains to be demonstrated here

The design needs evidence connecting authored persona context to useful behavior over time. The chain to examine is characteristic prompt authorship, permitted selection, actual supplied context, LLM reasoning expressed in observable choices, action and received feedback, justified self-revision, and an independently assessed useful outcome.

Testing this observable chain does not require exposing private provider-internal reasoning. File creation, schema compliance, a persistence receipt, or a persona’s claim that it has matured each proves only a narrower part. An action occurring after a read does not by itself establish that the read caused the action.

**Context must work as a whole.** Retrieving the right material is only part of context quality; its composition also matters. [Lost in the Middle, TACL 2024](https://aclanthology.org/2024.tacl-1.9/) found position-sensitive performance in studied question-answering and key-value tasks. [ComplexBench, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8c24b08b96a08ec7a7a975feea7777e-Paper-Datasets_and_Benchmarks_Track.pdf) evaluates dependent, conditional, and sequential constraints. Its GPT-3.5-Turbo-1106 decomposition comparison performed worse than combined instructions.

Both sources were independently inspected on 8 October 2026. They motivate varying order, distracting material, conditional scope, and successive decisions. Their model and task limits—including ComplexBench’s primarily Chinese source instructions—prevent treating the results as universal placement rules or persona-validation measures. Exact inclusion does not prove effective use, and more calls do not inherently improve quality.

The following AI Personas hypotheses remain unrun. Their precise cases belong in the [evaluation method](../evaluation/README.md) and [acceptance catalogue](../evaluation/ACCEPTANCE.md).

| Hypothesis | Relevant comparison and failure evidence |
|---|---|
| Sparse seeds support attributable, useful starting context | Preserve the seed, initialLLM configuration, all candidate attempts, acceptance, and actual later supply. Assess seed fidelity and recognizable expression separately from invented history, competence, and longitudinal benefit. Compare frozen post-bootstrap fragments with evolving fragments under fixed current character. |
| Persona-defining context influences useful decisions beyond factual recall and tone | Compare matched factual context, profile-only context, and characteristic authored fragments with the same facts, tools, authority, and budgets. Trace selected prompt parts through actual supply and observable choices. Keep voice recognition, factual recall, task quality, and justified self-revision separate. |
| Intended expression survives without unrelated competence loss | Vary irrelevant profile details, paraphrases, and context order. Pair true and false user beliefs with neutral and emotional framing. Distinguish warmth from agreement and justified adaptation from unwanted drift. |
| Universal consideration improves continuity at acceptable cost | Compare selective every-call maintenance with periodic-only consideration and forced writes. Include missing outcomes, honest unchanged decisions, bounded deferrals, invented lessons, latency, and storage growth. |
| Maintained experience transfers without harmful overgeneralization | Observe held-out tasks, delayed reuse, paraphrases, missed retrieval, misleading guidance, counterevidence, and correction. An expert-supplied fragment is an assisted diagnostic, not autonomous discovery success. |
| Reuse preserves the distinction between inference and corroboration | Compare exact replay, repeated reads, new interpretation, and split/merged descendants with genuinely independent evidence and explicit correction. Observe certainty, claim scope, ancestry, and action proposals without assuming every changed inference is wrong. |
| Continuing character remains adaptable | Vary partners, urgency, failures, successes, long histories, source withdrawal, and model versions. Distinguish unsupported drift from justified revision and appropriate convergence. |
| Actual work and interaction support reciprocal development | Compare matched starting characters after different legitimate histories, and different characters after matched experience. Trace received observations, accepted interpretation, exact later supply, changed choices, and assessed outcomes. Distinguish methods, relationships, context-navigation habits, and permitted character revision. |
| Compact associations improve useful continuity within the whole-store bound | Compare ordinary primary search, exact links, authored query cues, and mixed navigation with matched total resources. Include vocabulary mismatch, growth, stale cues, rare warnings, source expiry, peak copies, and harmful revival. Shorter prompts or fewer retained bytes alone do not establish success. |
| Bounded resource discovery preserves adequate work as catalogs grow | Keep task needs fixed while adding hundreds of distractors. Inspect provider-bound payloads and model-visible context on every call. Compare feasible full-catalog controls with bounded discovery, and legitimately known exact-resource access with unaided cold start. Count critical-capability misses, ambiguous or stale identities, accumulated metadata, failed reads, and actual outcomes. Supplied answer IDs remain assisted diagnostics. |
| The integration survives operational failure | Audit persona call sites and inject invalid output, interruption, concurrency, and ambiguous effects. Check actual revisions and release boundaries instead of relying on prompt promises. |

**Cost must cover the complete episode.** Anthropic’s [advanced-tool-use report, 24 November 2025](https://www.anthropic.com/engineering/advanced-tool-use) describes token savings and internal evaluation gains for its deferred-loading conditions. Its [context-engineering guidance, 29 September 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) also identifies slower runtime exploration and dead ends. These vendor observations, inspected on 8 October 2026, support measuring the whole episode. Neither provides an AI Personas result or a transferable numerical gate.

Count bootstrap and harmonization, queries, scans, repeated input and reads, schema loading, caches, output, retries, maintenance, and failed attempts. Compare independently adequate work and the time to first usable and complete outcomes at declared total budgets. A smaller first prompt or discounted cached input alone does not establish savings. Bound compliance, discovery usefulness, task quality, and characteristic influence remain separate claims.

**Factual memory covers only part of evaluation.** [LongMemEval, v2, 2025](https://arxiv.org/abs/2410.10813v2) provides relevant categories: extraction, cross-session reasoning, temporal reasoning, knowledge updates, and abstention. These inform part of evaluation. They do not measure characteristic authorship, privacy enforcement, crash recovery, or useful personality.

The target is useful, evidence-responsive continuity. Maximum difference, questionnaire scores, fragment counts, and perpetual introspection are not substitutes. Tests must preserve failed, harmful, assisted, and inconclusive outcomes and count total work. The sources supply no universal passing number, and the design provides no 100% behavioral guarantee.

## Earlier ideas and their disposition

The current account retains useful historical commitments while replacing earlier mechanisms and tightening two obligations. Earlier reports contributed continuing identity, accepted responsibilities, bounded capabilities, provenance, and accountable cooperation. Prior graph/selector mechanisms and mandatory numeric controls remain historical.

**7 October consolidation.** This change adopted own-voice files and primary-model next-context choice. It still allowed a minimal prose character without required semantic OCEAN/VAD coverage, and ordinary responses without an explicit maintenance outcome.

**8 October revision.** This revision strengthens both obligations: authored fragments need meaningful trait and modeled-affect grounding, and every persona invocation needs a maintenance request and explicit outcome. Mutations remain justified and optional. The revision does not restore numeric sliders, a compulsory cognitive taxonomy, delegated semantic selection, or forced writing.

The [decision register](../DESIGN-DECISIONS.md) records current choices. The [manifest](SOURCE-MANIFEST.md) pins preceding meanings and original reports. Historical results retain their original criteria and cannot silently pass the changed target.

**Conceptual clarification.** The earlier 8 October conceptual clarification centers the account on persona-defining authored context rather than factual memory. Storage, provenance, retention, and qualification remain supporting obligations. All earlier source versions and historical limits are retained. The GEPA comparison and expanded ACE account support context adaptation only; the whole persona loop remains a design hypothesis needing its own evidence.

**Reciprocal development and retention.** The subsequent 8 October refinement makes development through actual work, human interaction, and peer exchange explicit. It also makes compact associative navigation and whole-store retention accounting explicit. The accompanying primary-source checks clarify component support and limits. They do not replace direct collaboration evidence, alter the provenance of originally supplied sources, or create a runtime pass.

That refinement consists only of design prose, comparative criteria, and citations. No implementation, prototype, executable test, publication, runtime experiment, or live-model trial was performed for it.

**Bootstrap and supporting resources.** The subsequent refinement makes the handover from seed to authorship, self-harmonization, bounded provider transport and context, and whole-episode cost explicit. It borrows inspected component mechanisms without adopting their hidden authors, retrieval engines, global catalogs, or performance claims. Deeper source inspection and revised unrun comparisons create no implementation evidence, model-test result, publication, or deployment approval.
