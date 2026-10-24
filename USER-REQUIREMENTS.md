# Consolidated user requirements

This file brings together the user's product and design requirements for AI Personas, including clarifications through 24 October 2026. It covers the requested product, architecture, and worked examples. Repeated requests are combined. Later user clarifications govern the meaning of earlier wording.

Only human-user messages supply these requirements. This account must preserve the user's intended outcomes, rather than weaken them to fit the existing design. Assistant interpretations, design decisions, evidence safeguards, and implementation rules must not be added as user requirements.

**Read visually:** Illustrated requirements have a cartoon and a short caption beneath them. The pictures explain the main ideas; the requirement text retains the full details and qualifications. Robot characters represent personas, character cards represent fragments, and folders or tools represent supporting assets. LLM means language model. The scenes are explanatory illustrations.

## Product requirements

### No application limits or safety gates

**UR-052 Do not impose limits or safety constraints.** On 22 October 2026 the user clarified: “we shouldnot have any limit and safety constraints”. This later requirement supersedes earlier application-enforced quota, permission-gate, safety-envelope and approval requirements. It applies to persona work, model calls, tools, navigation, retained history and supporting resources. Do not substitute a larger fixed limit for removal of the limit.

The implementation must continue to report actual usage and outcomes. Reporting a cost, provider rejection, unavailable host resource or incomplete result does not itself establish an application quota. Keep earlier run evidence under the rules that actually produced it. This requirement does not retrospectively turn an incomplete or uncertain run into a success.

### Purpose and design scope

The requested outcome is a coherent design that can guide implementation of general-purpose personas.

**UR-001 Design before implementation.** Keep this repository design-only. Produce and refine an implementation-ready blueprint explaining how the personas should operate. Do not add application code as part of this design work.

![UR-001: A person and a persona prepare and review a blueprint, then hand it to a future builder. This repository defines how the system should work before implementation.](assets/user-requirements/ur-001-design-first.webp)

*In the picture: Prepare the design here so it can guide implementation later.*

**UR-002 One coherent design.** Review all design documents against the user's requirements, including published GitHub documents and unpublished work. Update, revise, refactor, add, or delete material as needed. The resulting documents must describe one coherent, solid, robust, and reliable design for AI Personas that can be implemented.

![UR-002: Published documents and local drafts are checked and revised until their pieces fit into one consistent blueprint.](assets/user-requirements/ur-002-coherent-design.webp)

*In the picture: Bring published documents and drafts into one consistent design.*

**UR-003 General-purpose, human-like personas.** Personas should have human-like characteristics and behavior, respond to whatever a user needs, and work on any kind of task. A requester may be a human or another persona, and a need may originate from either.

Their characteristics should shape how they work on tasks, use tools, communicate, coordinate, collaborate, pursue self-directed activity, and socialize with humans and other personas. They should develop through these activities, become better at socializing, and perform better for the user.

![UR-003: A human and another persona bring different needs to a persona, which plans, explains, and collaborates across different kinds of work.](assets/user-requirements/ur-003-general-purpose.webp)

*In the picture: A persona brings its own character to many tasks, for people and other personas.*

**UR-050 Let personas choose how to work and collaborate.** Personas should choose their approaches, tool use, requests for help, review, coordination, and contributions through their own reasoning. Their character, actual feedback, and the situation should shape those choices. The runtime must not replace them with a predetermined workflow or fixed owner, planner, or reviewer roles. Personas may organize and change their cooperation as the work develops.

The personas themselves must carry out the task, identify and correct problems, and judge their work. A human user may offer guidance, but continuing external coaching or fixes must not be expected or necessary for ordinary task progress and completion. An external agent must not supply the missing task reasoning, diagnose each defect, prescribe each correction, or finish the deliverable on their behalf. This clarification does not remove useful questions about actual user preferences or indispensable information.

![UR-050: Personas reason about the situation, choose tools and collaboration, and adapt contributions as the work and feedback develop.](assets/user-requirements/ur-050-choose-how-to-collaborate.webp)

*In the picture: Let persona reasoning and character shape approaches and cooperation as work develops.*

**UR-051 Use direct model-provider interfaces.** The persona runtime must call model providers directly for inference. It must not depend on the Codex CLI to run personas or orchestrate their work.

![UR-051: The persona runtime exchanges inference requests and responses directly with model-provider APIs without depending on the Codex CLI.](assets/user-requirements/ur-051-direct-provider-interfaces.webp)

*In the picture: Use model-provider interfaces directly for persona inference.*

### Persona identity and characteristic fragments

Characteristic fragments are prompt parts that express a particular persona's character and behavior. They help shape the operating persona; they are not simply a biography or a preferred writing style.

**UR-004 Start with a persona profile.** Define an initial profile using traits such as OCEAN—openness, conscientiousness, extraversion, agreeableness, and neuroticism—and VAD—valence, arousal, and dominance. Research and add other persona traits if needed. Express the profile's traits throughout the persona's characteristic fragments, in its own voice.

![UR-004: A starting profile with personality traits and modeled affect is expressed in the persona's own voice across its character fragments.](assets/user-requirements/ur-004-starting-profile.webp)

*In the picture: Use the starting profile to shape characteristic prompts in the persona's own voice.*

**UR-005 The initial LLM call authors the initial fragments.** Use the starting profile in the initial LLM call to produce the persona's initial characteristic fragments. These prompt parts must express its own voice and character and provide the starting point for subsequent development. Later creation, revision, and self-harmonization of fragments must preserve their persona-specific characteristic meaning.

![UR-005: A starting profile enters the first LLM call, which authors the persona's initial characteristic fragments in its own voice.](assets/user-requirements/ur-005-first-fragments.webp)

*In the picture: The initial model call turns the starting profile into character-bearing prompt parts.*

**UR-006 Fragments embody character.** Every characteristic fragment must reflect its owner's unique traits and voice, behavioral dispositions, and standards for its own work and conduct. It must carry that persona's characteristic and behavioral meaning, rather than attach a persona label to generic instructions. Selected fragments form the character-bearing part of the context supplied to the LLM.

![UR-006: Two personas author different characteristic prompts, and those prompts influence their careful checking or exploration of alternatives.](assets/user-requirements/ur-006-character-in-fragments.webp)

*In the picture: Fragments express a persona's voice, dispositions, and standards, which shape its choices.*

**UR-007 The LLM and selected context constitute the operating persona.** The LLM provides reasoning. Selected characteristic fragments and relevant supporting context shape this persona's responses and decisions. Character must influence how the persona acts, rather than exist only in a separate profile or biography.

![UR-007: Selected character fragments and relevant supporting context enter LLM reasoning and shape the persona's decisions, actions, and responses.](assets/user-requirements/ur-007-operating-persona.webp)

*In the picture: LLM reasoning with selected character and supporting context forms the operating persona.*

**UR-008 Unique character drives behavior throughout development.** From initialization through aging and maturation, each persona's characteristics must shape its actions, use of tools and skills, responses, communication with humans and peers, coordination, collaboration, and self-directed activity.

Character should influence both what it chooses to do and how much and in what way it communicates. Some personas may communicate more and others less; some may favor tools and others collaboration. Preserve each persona's uniqueness as it develops.

![UR-008: Two distinct personas retain their recognizable characters while experiences shape how they use tools, communicate, and work over time.](assets/user-requirements/ur-008-character-throughout-life.webp)

*In the picture: Each persona's own character should influence its behavior throughout development.*

**UR-009 Fragments are not memories or plain knowledge.** Use “fragment” to mean a characteristic prompt part. Do not use it to mean an episodic memory, a general-purpose fact store, or plain domain knowledge. These character-bearing prompt parts help form the persona; a separate memory mechanism does not define it. Supporting histories and records may still be retained as assets.

![UR-009: Character fragments express how a persona acts; facts and historical records remain separately identifiable supporting assets.](assets/user-requirements/ur-009-fragments-and-memories.webp)

*In the picture: A fragment expresses character; memories, facts, and history support the work.*

**UR-010 Do not introduce a separate learning mechanism.** Explain persona learning and maturation through ordinary LLM interactions that create, revise, organize, select, and delete character-bearing prompt fragments, with the resulting characteristic changes shaping later behavior. Maintain supporting assets through those interactions too, while distinguishing their development and reuse from persona learning. Knowledge, data, tools, skills, and history remain supporting assets; acquiring or revising them alone does not establish character maturation.

![UR-010: Ordinary LLM interactions can revise character fragments, and those revisions shape later behavior; supporting resources remain separate.](assets/user-requirements/ur-010-learning-through-interactions.webp)

*In the picture: Explain development through ordinary interactions and changing characteristic prompts.*

### Supporting assets and historical context

A persona also needs useful material that supports its work without defining its character. The design must keep that material identifiable, organized, and available for later use.

**UR-011 Keep assets identifiable separately from characteristic fragments.** Assets or supporting context include plain domain knowledge, data, tools, skills, procedural guides, scripts, code, historical messages, records of actions and tool interactions, and other useful resources.

These remain distinguishable from characteristic fragments even when the persona or LLM creates them. Plain assets need not be rewritten in the persona's voice. Authorship alone does not turn an asset into persona character.

![UR-011: A persona keeps its characteristic prompt cards identifiable separately from tools, knowledge, data, and history, including resources it creates itself.](assets/user-requirements/ur-011-separate-supporting-assets.webp)

*In the picture: Classify material by its role, even when the persona created it.*

**UR-012 Retain useful resources for later work.** Provide for storing and organizing useful tools, skills, knowledge, data, scripts, code, history, and other assets that the persona acquires or produces. Later work must be able to find relevant assets without reconstructing everything from the beginning.

![UR-012: A persona organizes useful resources after one task and retrieves the relevant saved material for a later task.](assets/user-requirements/ur-012-save-and-reuse.webp)

*In the picture: Keep useful assets organized so later work can find and reuse them.*

**UR-013 Give retained material an intended location and useful discovery cues.** When an LLM interaction proposes new or revised fragments or assets, it must also explain where the material belongs and how it can be found again. This includes the intended file or path and relevant search cues or regular-expression patterns. Storage and discovery must be designed as part of the process, rather than left as unspecified steps after generation.

![UR-013: New or revised material receives an intended file location and search cues, allowing the persona to find it again.](assets/user-requirements/ur-013-location-and-search-cues.webp)

*In the picture: Say where material belongs and how it can be found again.*

**UR-014 Compose context from the relevant kinds of material.** An LLM request may combine characteristic fragments with relevant tools, skills, domain knowledge, data, and records of historical interactions or actions. Assemble the context needed for the current decision while preserving the distinction between character-bearing prompt parts and supporting material.

![UR-014: A persona combines selected character fragments with relevant tools, data, knowledge, and history for the current LLM request.](assets/user-requirements/ur-014-compose-context.webp)

*In the picture: Assemble relevant character and supporting material while keeping their roles clear.*

### The ordinary LLM interaction

Work, maintenance, and preparation for the next interaction belong in the same ordinary persona interaction.

**UR-015 Integrate work and self-maintenance in every interaction.** Every persona LLM request and response must include all of the following:

| Part of the interaction | Required coverage |
|---|---|
| Current work | The task, communication, collaboration, coordination, tool use, or other persona action at hand |
| Fragment maintenance | Maintenance requests and responses for characteristic fragments |
| Asset maintenance | Maintenance requests and responses for supporting assets |
| Next context | What characteristic fragments and supporting resources are needed for the next interaction |

This applies to every kind of persona action.

![UR-015: One ordinary interaction covers current work, character-fragment maintenance, asset maintenance, and selecting context for what comes next.](assets/user-requirements/ur-015-every-interaction.webp)

*In the picture: Every interaction combines work, care for fragments and assets, and next-context choices.*

**UR-016 Support the full range of maintenance.** The same interaction must support creating fragments, updating existing fragments, reorganizing them, and deleting them. It must also support maintenance of tools, skills, knowledge, data, history, and other assets. Changes to characteristic prompt parts should shape and improve the persona’s later characteristic behavior. Asset maintenance supports the work and remains separately identifiable; it does not by itself demonstrate persona learning or maturation.

![UR-016: A persona can create, revise, reorganize, and delete character fragments and supporting assets as part of ordinary work.](assets/user-requirements/ur-016-full-maintenance.webp)

*In the picture: Support the full range of maintenance for both characteristic prompts and assets.*

**UR-018 Let the current interaction guide the next one.** The current LLM interaction must say which characteristic fragments, tools, skills, data, and other context are needed next and how to find them. Use that guidance to select relevant material from the files for the next LLM request. Continue this process through the work.

![UR-018: The current interaction identifies needed fragments and resources plus discovery cues, guiding selection for the next LLM request.](assets/user-requirements/ur-018-prepare-next-context.webp)

*In the picture: Let the current interaction say what the next one needs and how to find it.*

### File based discovery and context efficiency

The persona should find relevant material in ordinary files and bring only what it needs into the next model context. Both the stored collection and the assembled prompt need to remain manageable.

**UR-019 Use ordinary files and searchable links.** Prefer simple file organization and search over unnecessary architectural complexity. Store and organize prompt fragments in files, including JSON where useful. Support discovery through filesystem search, grep, and regular-expression cues.

Fragments may contain cues leading to other relevant fragments or assets. These connections should form a navigable network without requiring the whole collection to be loaded into context.

![UR-019: Search cues connect ordinary files so a persona can find relevant fragments and assets without loading the whole collection.](assets/user-requirements/ur-019-files-and-searchable-links.webp)

*In the picture: Use ordinary files and searchable cues to navigate relevant connections.*

**UR-020 Select resources through the same selective discovery process.** Discovery must cover tools, skills, data, knowledge, history, and other assets as well as characteristic fragments. A fragment or the current LLM result may identify resources to locate and search cues to use.

![UR-020: The same selective discovery process finds relevant character fragments, tools, skills, data, knowledge, and historical records.](assets/user-requirements/ur-020-discover-all-resource-types.webp)

*In the picture: Use selective discovery for supporting resources as well as fragments.*

**UR-021 Select before loading the next model context.** Do not send the persona's hundreds of tools, full catalogue, or entire fragment and asset collection in an LLM request for the model to filter. Use the current request's need and selection instructions to retrieve only the relevant information for a subsequent request.

![UR-021: A persona selects relevant information from a large collection before sending the smaller chosen context to the model.](assets/user-requirements/ur-021-select-before-loading.webp)

*In the picture: Retrieve what is needed before loading the next model context.*

**UR-022 Minimize unnecessary context and token cost.** Select the information each request needs instead of loading unnecessary material. Tokens cost money, so the design must minimize their cost. Research whether the approach is effective and what cost savings it provides.

![UR-022: Relevant context is selected to avoid unnecessary tokens, while research compares cost and effectiveness instead of assuming savings.](assets/user-requirements/ur-022-context-and-cost.webp)

*In the picture: Avoid unnecessary context and research the actual cost and effectiveness.*

**UR-023 Keep both the collection and the prompt compact.** Prevent fragments from growing indefinitely or becoming an inconsistent, bloated collection. Revise, combine, and reorganize them while retaining needed characteristic material. This should let the persona navigate its resources, select the right fragments at the right time, and assemble compact, coherent context.

![UR-023: A persona revises and combines overlapping fragments while preserving needed character, producing both a manageable collection and compact prompt.](assets/user-requirements/ur-023-compact-collection-and-prompt.webp)

*In the picture: Control growth in both stored fragments and the context sent to the model.*

**UR-024 Keep organization useful as the persona develops.** Resource organization and discovery cues must evolve with the fragments and assets. After revision or reorganization, the persona must still be able to find useful earlier material. Merely accumulating files that are rarely used does not meet this requirement.

![UR-024: When fragments and assets change location or organization, their discovery cues change too, keeping useful earlier material findable.](assets/user-requirements/ur-024-organization-keeps-working.webp)

*In the picture: Update organization and search cues together so older useful material remains discoverable.*

### Development and later usefulness

Development should change how the persona behaves and works across experience. The requested benefit is better later performance, including useful transfer from earlier work where it applies.

**UR-025 Development arises through interaction.** Tasks, environmental interactions, communication and socializing with humans and other personas, and self-directed interactions must shape subsequent characteristic fragments and assets. Explain how these ordinary interactions reshape the persona without a separate learning process.

![UR-025: Work, social exchanges, environmental experience, and self-directed activity can inform later characteristic fragments and supporting assets.](assets/user-requirements/ur-025-experience-shapes-development.webp)

*In the picture: Explain how ordinary interactions reshape the persona and its supporting material.*

**UR-026 Maturation affects the whole persona.** Personas should develop over their lifetime in a human-like way. Their characteristics, behavior, affect, communication, coordination, collaboration, and ways of working should mature, and that development should be reflected throughout their work and actions.

Their fragments and assets should improve and become better organized so that the right prompts and resources can be used at the right time.

![UR-026: Development should affect a persona's character, affect, communication, collaboration, and ways of working, supported by better organized fragments and assets.](assets/user-requirements/ur-026-whole-persona-maturation.webp)

*In the picture: Look for maturation across the persona's behavior and ways of working.*

**UR-027 Later stages should perform better.** A matured persona should be better than its earlier self. Show how its developed characteristic prompt parts shape later behavior and help it perform subsequent work better. Examine this benefit across its judgment, communication, collaboration, ways of working, and actions. Improvements in supporting assets may also help the work, but keep that benefit separate from character maturation. Do not force fragment edits merely to produce an apparent learning result.

![UR-027: An observer compares the same persona's earlier and later judgment, communication, and work to examine benefits of its developed characteristic prompts.](assets/user-requirements/ur-027-later-performance.webp)

*In the picture: Examine whether developed character helps later work; time or saved assets alone do not show this.*

**UR-028 Examine useful transfer without assuming complete domain transfer.** Earlier work should help later work through relevant fragments, skills, tools, assets, methods, simulations, and developed characteristic behavior. The user does not expect every part of earlier work, or its entire domain solution, to transfer. Work through the new task on its own and examine which parts of prior development help.

![UR-028: A persona brings relevant developed behavior, methods, and resources to a new task while working through the new problem on its own terms.](assets/user-requirements/ur-028-selective-transfer.webp)

*In the picture: Reuse what applies and examine the new task independently.*

**UR-048 Examine a developing society of personas, including without assigned tasks.** Use hypothetical examples to examine personas communicating, collaborating, and maturing over longer periods, including periods with no assigned task. Their characteristics and behavior should shape both the interactions and their development over time.

Examine how a society-like pattern emerges through ongoing interactions in two settings: outside assigned tasks, and when groups work together on a task or need. Also examine how this maturation helps them perform later work better.

![UR-048: Hypothetical personas socialize and develop both outside assigned tasks and while working together, with possible benefits for later cooperation.](assets/user-requirements/ur-048-developing-persona-society.webp)

*In the picture: Examine society-like development through ongoing social and task interactions.*

### Sustained work and reasons to continue or stop

The design must explain what personas do when more time is available, and how they judge whether further work is worthwhile or the work is complete.

**UR-044 Examine sustained purposeful work and improvement.** Examine what happens when a persona has ample, or hypothetically unlimited, time to keep working on a user's task. Investigate whether continued work:

- Produces quality artifacts that meet the user's needs.
- Improves the task or its output.
- Improves and matures the persona itself.
- Involves useful interaction with other personas.

Include groups that continue collaborating over time to improve a shared task, work, or response to a user's need. Explain how this continued work and improvement should happen.

![UR-044: An extended-work example examines whether continued individual and group effort improves the artifact, serves the user's need, and contributes to persona development.](assets/user-requirements/ur-044-sustained-purposeful-work.webp)

*In the picture: Investigate what sustained work, collaboration, and reflection contribute when more time is available.*

**UR-045 Justify continuation and stopping.** Examine whether personas continue working usefully or stop arbitrarily with potentially low-quality work. Explain when and why a persona should continue or stop. Relate those choices to the user's task and the opportunity for further improvement.

![UR-045: A persona considers the user's need and remaining useful improvements when explaining whether to continue working or stop.](assets/user-requirements/ur-045-reasons-to-continue-or-stop.webp)

*In the picture: Tie continuation and stopping to the task and the value of further improvement.*

**UR-047 Let reflection, dialogue, and character shape completion and further improvement.** Explain how one persona can use self-reflection and self-questioning, and how multiple personas can question one another and clarify the work as they continue.

Their characteristic behaviors should shape individual or collective judgments about what can be improved, when and where to stop, and when to consider the work complete. These judgments should respond to the actual task, feedback, time, resources, and the persona's developing character and behavior. Personas should be able to deliver a result they judge sufficient for now and later choose to revisit or enhance it. Recording completed delivery must not permanently suppress that choice. Some personas may continue while others stop; they need not make the same choice, and neither stopping nor continuing should be forced by a fixed workflow.

![UR-047: Personas use reflection and dialogue to judge completion, may make different continuation choices, and can later revisit a delivered result.](assets/user-requirements/ur-047-reflect-deliver-revisit.webp)

*In the picture: Let characteristic judgment guide completion, further work, and later revisiting.*

### Quality through characteristic judgment

**UR-049 Let personas develop quality through reasoned judgment.** Personas should pursue quality through their own characteristic standards, self-critique, and exchanges with other personas. Their character should shape how they identify problems, disagree, respond to criticism, revise work, and judge whether to accept a contribution or result. An externally hardcoded quality score must not replace this reasoning. Objective factual and contract checks provide evidence for these judgments; passing those checks alone does not settle overall quality.

Keep this development distinct from reuse of knowledge, tools, skills, or procedural guides. Those are supporting assets. Characteristic fragments express voice, behavioral dispositions, and standards. A claim of character maturation must be visible in later behavior, not inferred merely from saving or reusing an asset. Better work is the aim, without a guarantee of improvement on every turn or from elapsed time.

![UR-049: Personas use characteristic standards, critique, disagreement, evidence, and revision to judge quality; factual checks inform rather than replace that judgment.](assets/user-requirements/ur-049-reasoned-quality-judgment.webp)

*In the picture: Develop quality through reasoned critique and characteristic judgment, informed by evidence.*

### Clarification and progress from sparse requests

A brief request may leave important questions open. Personas should seek useful clarification and still be able to make progress when the requester is unavailable.

**UR-046 Clarify sparse requests and proceed.** A user may start with a simple question or a bare description of a task or need. When more clarity is needed, the persona should ask useful questions of the user or relevant stakeholder.

The user or task owner may or may not answer. The persona should not wait indefinitely. It should be able to seek clarification from other personas, receive volunteered input from another persona, or form a reasonable interpretation of its own and proceed. Examine how these social interactions help clarify work when the original requester is unavailable.

![UR-046: A persona asks for useful clarification, then uses peer input or a reasonable interpretation to progress when the requester is unavailable.](assets/user-requirements/ur-046-clarify-and-proceed.webp)

*In the picture: Clarify sparse requests and make reasonable progress when the requester cannot answer.*

### Worked examples and design verification

Hypothetical walkthroughs should make the design's behavior concrete and expose gaps that need repair. They must show both the work being done and how the personas develop through it.

**UR-029 Compare three unique personas over time.** Use three personas with distinct initial profiles and initial LLM-authored fragments. Examine each persona's uniqueness and its own human-like aging and maturation based on its traits. Show its initial state, interactions, resulting fragments and assets, and characteristic behavior in later actions and communication.

![UR-029: Three distinct personas are followed from profiles and initial fragments through different interactions to later characteristic behavior and supporting assets.](assets/user-requirements/ur-029-three-personas-over-time.webp)

*In the picture: Compare each persona's own starting point, experiences, and later behavior.*

**UR-030 Include the house and circuit work cases.** Walk through these hypothetical cases:

| Case | What to examine |
|---|---|
| Four-bedroom house with three personas | How different characteristics shape approaches, choices, collaboration, and designs; how the work develops later characteristics, fragments, and assets |
| Five-watt DC-to-AC circuit with three personas | The same connections between distinct character, work, collaboration, designs, and subsequent development |
| House case with more time | Whether the personas continue improving the design or stop in between, what happens, and why |
| DC-to-AC case with five personas and more time | Whether the group continues improving the design or stops in between, what happens, and why |

![UR-030: Hypothetical walkthroughs cover a four-bedroom house and five-watt DC-to-AC circuit with three personas, plus extended house work and extended circuit work with five personas.](assets/user-requirements/ur-030-house-and-circuit-cases.webp)

*In the picture: Show the requested house and circuit examples, including more time and a five-persona circuit group.*

**UR-031 Show house-to-skyscraper improvement.** Give a later skyscraper-design task, potentially from another human user, to personas that participated in the house work. Show how their matured characteristics and relevant earlier fragments, methods, simulations, skills, tools, and assets help them perform better on the new task. Do not require complete transfer of the house design.

![UR-031: Personas from the house example bring relevant developed character, methods, tools, and assets to a new skyscraper task with new requirements.](assets/user-requirements/ur-031-house-to-skyscraper.webp)

*In the picture: Examine how house experience helps later skyscraper work without copying the whole solution.*

**UR-043 Show circuit-to-3D-printer improvement.** Include a later 3D-printer-design walkthrough involving personas that worked on the DC-to-AC circuit. Show how their maturation and relevant prior work help them perform better in designing the 3D printer.

![UR-043: Personas from the circuit example apply relevant developed character and prior resources while working through a later 3D-printer design task.](assets/user-requirements/ur-043-circuit-to-printer.webp)

*In the picture: Examine how circuit experience and maturation help later 3D-printer design.*

**UR-032 Walk through how the design should operate.** Provide step-by-step hypothetical walkthroughs showing:

- LLM requests and responses, including selected fragments and supporting context.
- Actions taken through the work.
- Changes to fragments and assets.
- Choices about the next context.
- How the personas develop through these interactions.

Show how an implementation of the design should perform. The examples exercise the design; they do not limit the kinds of tasks personas should handle.

Within the examples, examine tool and skill use, asset management, and retention of relevant data. Where several tools are available, examine whether personas choose suitable tools and use them effectively. Show how skills, characteristics, and behavior shape different tool preferences. Include tool installation when it is part of the work, including in the circuit and later 3D-printer examples.

![UR-032: A hypothetical walkthrough shows selected context, model requests and responses, tool use, observed actions, fragment and asset maintenance, and next-context choices.](assets/user-requirements/ur-032-step-by-step-walkthrough.webp)

*In the picture: Make each interaction, action, maintenance choice, and next-context decision concrete.*

**UR-033 Examine help, lack of help, and missed benefit.** Investigate what prior development helps, what does not help, and whether a potentially helpful resource or behavior is unused or absent. Examine domain-related resources alongside changes in characteristic behavior, affect, judgment, communication, and coordination. Use this examination to assess whether the design is solid.

![UR-033: An example examines helpful development, irrelevant prior material, and useful behavior or resources that were missing or went unused.](assets/user-requirements/ur-033-help-no-help-missed-help.webp)

*In the picture: Look for benefits, lack of benefit, and missed opportunities in both character and resources.*

**UR-034 Use the examples to find and repair design gaps.** Audit the proposed design against the walkthroughs and all user requirements. Identify what works, what fails, missing behavior, contradictions, and unresolved questions. Research those findings and refine the affected design. Appending examples or assurances alone is not enough.

![UR-034: Walkthroughs expose missing or conflicting behavior, and those findings lead to research and repairs in the affected design.](assets/user-requirements/ur-034-repair-design-gaps.webp)

*In the picture: Use walkthrough findings to improve the design itself.*

**UR-035 Deliver a robust, reliable blueprint.** Make the design solid and effective so that personas will work as intended when it is implemented. Research and repair gaps in pursuit of the user's goal that the persona design work completely and reliably.

![UR-035: Research and gap repairs produce a coherent blueprint intended to guide reliable future implementation.](assets/user-requirements/ur-035-reliable-blueprint.webp)

*In the picture: Deliver a robust design that explains how the personas should work when implemented.*
