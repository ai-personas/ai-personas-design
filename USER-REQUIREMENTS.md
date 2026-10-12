# Consolidated user requirements

This file brings together the user's requirements from the AI Personas design conversation through 10 October 2026. It covers the requested product, architecture, examples, research, and delivery. Repeated requests are combined. Later user clarifications govern the meaning of earlier wording.

Only human-user messages supply these requirements. This account must preserve the user's intended outcomes, rather than weaken them to fit the existing design. Assistant interpretations, design decisions, evidence safeguards, and implementation rules must not be added as user requirements.

## Product requirements

### Purpose and design scope

The requested outcome is a coherent design that can guide implementation of general-purpose personas.

**UR-001 Design before implementation.** Keep this repository design-only. Produce and refine an implementation-ready blueprint explaining how the personas should operate. Do not add application code as part of this design work.

**UR-002 One coherent design.** Review all design documents against the user's requirements, including published GitHub documents and unpublished work. Update, revise, refactor, add, or delete material as needed. The resulting documents must describe one coherent, solid, robust, and reliable design for AI Personas that can be implemented.

**UR-003 General-purpose, human-like personas.** Personas should have human-like characteristics and behavior, respond to whatever a user needs, and work on any kind of task. A requester may be a human or another persona, and a need may originate from either.

Their characteristics should shape how they work on tasks, use tools, communicate, coordinate, collaborate, pursue self-directed activity, and socialize with humans and other personas. They should develop through these activities, become better at socializing, and perform better for the user.

### Persona identity and characteristic fragments

Characteristic fragments are prompt parts that express a particular persona's character and behavior. They help shape the operating persona; they are not simply a biography or a preferred writing style.

**UR-004 Start with a persona profile.** Define an initial profile using traits such as OCEAN—openness, conscientiousness, extraversion, agreeableness, and neuroticism—and VAD—valence, arousal, and dominance. Research and add other persona traits if needed. Express the profile's traits throughout the persona's characteristic fragments, in its own voice.

**UR-005 The initial LLM call authors the initial fragments.** Use the starting profile in the initial LLM call to produce the persona's initial characteristic fragments. These prompt parts must express its own voice and character and provide the starting point for subsequent development. Later creation, revision, and self-harmonization of fragments must preserve their persona-specific characteristic meaning.

**UR-006 Fragments embody character.** Every characteristic fragment must reflect its owner's unique traits and voice. It must carry that persona's characteristic and behavioral meaning, rather than attach a persona label to generic instructions. Selected fragments form the character-bearing part of the context supplied to the LLM.

**UR-007 The LLM and selected context constitute the operating persona.** The LLM provides reasoning. Selected characteristic fragments and relevant supporting context shape this persona's responses and decisions. Character must influence how the persona acts, rather than exist only in a separate profile or biography.

**UR-008 Unique character drives behavior throughout development.** From initialization through aging and maturation, each persona's characteristics must shape its actions, use of tools and skills, responses, communication with humans and peers, coordination, collaboration, and self-directed activity.

Character should influence both what it chooses to do and how much and in what way it communicates. Some personas may communicate more and others less; some may favor tools and others collaboration. Preserve each persona's uniqueness as it develops.

**UR-009 Fragments are not memories or plain knowledge.** Use “fragment” to mean a characteristic prompt part. Do not use it to mean an episodic memory, a general-purpose fact store, or plain domain knowledge. These character-bearing prompt parts help form the persona; a separate memory mechanism does not define it. Supporting histories and records may still be retained as assets.

**UR-010 Do not introduce a separate learning mechanism.** Explain maturation through ordinary LLM interactions that create, revise, organize, select, and delete fragments and assets. The user describes this as development of fragments and assets, rather than a separate learning or memory mechanism.

### Supporting assets and historical context

A persona also needs useful material that supports its work without defining its character. The design must keep that material identifiable, organized, and available for later use.

**UR-011 Keep assets identifiable separately from characteristic fragments.** Assets or supporting context include plain domain knowledge, data, tools, skills, scripts, code, historical messages, records of actions and tool interactions, and other useful resources.

These remain distinguishable from characteristic fragments even when the persona or LLM creates them. Plain assets need not be rewritten in the persona's voice. Authorship alone does not turn an asset into persona character.

**UR-012 Retain useful resources for later work.** Provide for storing and organizing useful tools, skills, knowledge, data, scripts, code, history, and other assets that the persona acquires or produces. Later work must be able to find relevant assets without reconstructing everything from the beginning.

**UR-013 Give retained material an intended location and useful discovery cues.** When an LLM interaction proposes new or revised fragments or assets, it must also explain where the material belongs and how it can be found again. This includes the intended file or path and relevant search cues or regular-expression patterns. Storage and discovery must be designed as part of the process, rather than left as unspecified steps after generation.

**UR-014 Compose context from the relevant kinds of material.** An LLM request may combine characteristic fragments with relevant tools, skills, domain knowledge, data, and records of historical interactions or actions. Assemble the context needed for the current decision while preserving the distinction between character-bearing prompt parts and supporting material.

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

**UR-016 Support the full range of maintenance.** The same interaction must support creating fragments, updating existing fragments, reorganizing them, and deleting them. It must also support maintenance of tools, skills, knowledge, data, history, and other assets. These changes are how the persona and its characteristic behavior are shaped and improved.

**UR-018 Let the current interaction guide the next one.** The current LLM interaction must say which characteristic fragments, tools, skills, data, and other context are needed next and how to find them. Use that guidance to select relevant material from the files for the next LLM request. Continue this process through the work.

### File based discovery and context efficiency

The persona should find relevant material in ordinary files and bring only what it needs into the next model context. Both the stored collection and the assembled prompt need to remain manageable.

**UR-019 Use ordinary files and searchable links.** Prefer simple file organization and search over unnecessary architectural complexity. Store and organize prompt fragments in files, including JSON where useful. Support discovery through filesystem search, grep, and regular-expression cues.

Fragments may contain cues leading to other relevant fragments or assets. These connections should form a navigable network without requiring the whole collection to be loaded into context.

**UR-020 Select resources through the same selective discovery process.** Discovery must cover tools, skills, data, knowledge, history, and other assets as well as characteristic fragments. A fragment or the current LLM result may identify resources to locate and search cues to use.

**UR-021 Select before loading the next model context.** Do not send the persona's hundreds of tools, full catalogue, or entire fragment and asset collection in an LLM request for the model to filter. Use the current request's need and selection instructions to retrieve only the relevant information for a subsequent request.

**UR-022 Minimize unnecessary context and token cost.** Select the information each request needs instead of loading unnecessary material. Tokens cost money, so the design must minimize their cost. Research whether the approach is effective and what cost savings it provides.

**UR-023 Keep both the collection and the prompt compact.** Prevent fragments from growing indefinitely or becoming an inconsistent, bloated collection. Revise, combine, and reorganize them while retaining needed characteristic material. This should let the persona navigate its resources, select the right fragments at the right time, and assemble compact, coherent context.

**UR-024 Keep organization useful as the persona develops.** Resource organization and discovery cues must evolve with the fragments and assets. After revision or reorganization, the persona must still be able to find useful earlier material. Merely accumulating files that are rarely used does not meet this requirement.

### Development and later usefulness

Development should change how the persona behaves and works across experience. The requested benefit is better later performance, including useful transfer from earlier work where it applies.

**UR-025 Development arises through interaction.** Tasks, environmental interactions, communication and socializing with humans and other personas, and self-directed interactions must shape subsequent characteristic fragments and assets. Explain how these ordinary interactions reshape the persona without a separate learning process.

**UR-026 Maturation affects the whole persona.** Personas should develop over their lifetime in a human-like way. Their characteristics, behavior, affect, communication, coordination, collaboration, and ways of working should mature, and that development should be reflected throughout their work and actions.

Their fragments and assets should improve and become better organized so that the right prompts and resources can be used at the right time.

**UR-027 Later stages should perform better.** A matured persona should be better than its earlier self. Show how improved fragments, assets, characteristic behavior, prompting, and ways of working help it perform subsequent work better. Examine this benefit across its behavior and actions.

**UR-028 Examine useful transfer without assuming complete domain transfer.** Earlier work should help later work through relevant fragments, skills, tools, assets, methods, simulations, and developed characteristic behavior. The user does not expect every part of earlier work, or its entire domain solution, to transfer. Work through the new task on its own and examine which parts of prior development help.

**UR-048 Examine a developing society of personas, including without assigned tasks.** Use hypothetical examples to examine personas communicating, collaborating, and maturing over longer periods, including periods with no assigned task. Their characteristics and behavior should shape both the interactions and their development over time.

Examine how a society-like pattern emerges through ongoing interactions in two settings: outside assigned tasks, and when groups work together on a task or need. Also examine how this maturation helps them perform later work better.

### Sustained work and reasons to continue or stop

The design must explain what personas do when more time is available, and how they judge whether further work is worthwhile or the work is complete.

**UR-044 Examine sustained purposeful work and improvement.** Examine what happens when a persona has ample, or hypothetically unlimited, time to keep working on a user's task. Investigate whether continued work:

- Produces quality artifacts that meet the user's needs.
- Improves the task or its output.
- Improves and matures the persona itself.
- Involves useful interaction with other personas.

Include groups that continue collaborating over time to improve a shared task, work, or response to a user's need. Explain how this continued work and improvement should happen.

**UR-045 Justify continuation and stopping.** Examine whether personas continue working usefully or stop arbitrarily with potentially low-quality work. Explain when and why a persona should continue or stop. Relate those choices to the user's task and the opportunity for further improvement.

**UR-047 Let reflection, dialogue, and character shape completion and further improvement.** Explain how one persona can use self-reflection and self-questioning, and how multiple personas can question one another and clarify the work as they continue.

Their characteristic behaviors should shape individual or collective judgments about what can be improved, when and where to stop, and when to consider the work complete. These judgments should take account of the time available. Examine how personas can deliver work they judge sufficient for now and return to improve it when more time becomes available.

### Clarification and progress from sparse requests

A brief request may leave important questions open. Personas should seek useful clarification and still be able to make progress when the requester is unavailable.

**UR-046 Clarify sparse requests and proceed.** A user may start with a simple question or a bare description of a task or need. When more clarity is needed, the persona should ask useful questions of the user or relevant stakeholder.

The user or task owner may or may not answer. The persona should not wait indefinitely. It should be able to seek clarification from other personas, receive volunteered input from another persona, or form a reasonable interpretation of its own and proceed. Examine how these social interactions help clarify work when the original requester is unavailable.

### Worked examples and design verification

Hypothetical walkthroughs should make the design's behavior concrete and expose gaps that need repair. They must show both the work being done and how the personas develop through it.

**UR-029 Compare three unique personas over time.** Use three personas with distinct initial profiles and initial LLM-authored fragments. Examine each persona's uniqueness and its own human-like aging and maturation based on its traits. Show its initial state, interactions, resulting fragments and assets, and characteristic behavior in later actions and communication.

**UR-030 Include the house and circuit work cases.** Walk through these hypothetical cases:

| Case | What to examine |
|---|---|
| Four-bedroom house with three personas | How different characteristics shape approaches, choices, collaboration, and designs; how the work develops later characteristics, fragments, and assets |
| Five-watt DC-to-AC circuit with three personas | The same connections between distinct character, work, collaboration, designs, and subsequent development |
| House case with more time | Whether the personas continue improving the design or stop in between, what happens, and why |
| DC-to-AC case with five personas and more time | Whether the group continues improving the design or stops in between, what happens, and why |

**UR-031 Show house-to-skyscraper improvement.** Give a later skyscraper-design task, potentially from another human user, to personas that participated in the house work. Show how their matured characteristics and relevant earlier fragments, methods, simulations, skills, tools, and assets help them perform better on the new task. Do not require complete transfer of the house design.

**UR-043 Show circuit-to-3D-printer improvement.** Include a later 3D-printer-design walkthrough involving personas that worked on the DC-to-AC circuit. Show how their maturation and relevant prior work help them perform better in designing the 3D printer.

**UR-032 Walk through how the design should operate.** Provide step-by-step hypothetical walkthroughs showing:

- LLM requests and responses, including selected fragments and supporting context.
- Actions taken through the work.
- Changes to fragments and assets.
- Choices about the next context.
- How the personas develop through these interactions.

Show how an implementation of the design should perform. The examples exercise the design; they do not limit the kinds of tasks personas should handle.

Within the examples, examine tool and skill use, asset management, and retention of relevant data. Where several tools are available, examine whether personas choose suitable tools and use them effectively. Show how skills, characteristics, and behavior shape different tool preferences. Include tool installation when it is part of the work, including in the circuit and later 3D-printer examples.

**UR-033 Examine help, lack of help, and missed benefit.** Investigate what prior development helps, what does not help, and whether a potentially helpful resource or behavior is unused or absent. Examine domain-related resources alongside changes in characteristic behavior, affect, judgment, communication, and coordination. Use this examination to assess whether the design is solid.

**UR-034 Use the examples to find and repair design gaps.** Audit the proposed design against the walkthroughs and all user requirements. Identify what works, what fails, missing behavior, contradictions, and unresolved questions. Research those findings and refine the affected design. Appending examples or assurances alone is not enough.

**UR-035 Deliver a robust, reliable blueprint.** Make the design solid and effective so that personas will work as intended when it is implemented. Research and repair gaps in pursuit of the user's goal that the persona design work completely and reliably.

## Research and delivery requirements

These requirements govern the requested design assignment and its publication. They are not fixed schedules, runtime loops, or mandatory timing rules for the future persona system.

**UR-036 Research thoroughly.** Conduct deep research on the current design and the user's requirements. Cover trait choices, fragment and asset organization, retrieval, context efficiency, behavior, maturation, and gaps exposed by the worked examples.

**UR-037 Follow the latest research window and update cadence.** Conduct the renewed five-hour internal audit and research requested on **10 October 2026 at 14:21:32 UTC**, through **10 October at 19:21:32 UTC**. Review the complete design against the user's requirements and make needed design fixes. Continue concise progress updates every ten minutes.

This renewed the preceding audit request and followed the earlier assignments below. All times are UTC in 2026; the table lists the requests from most recent to oldest.

| Request time | Requested end | Scope of that request |
|---|---|---|
| 10 October, 13:47:48 | 10 October, 18:47:48 | Five-hour complete line-by-line audit, including the hypothetical house case with more time and the hypothetical DC-to-AC case with five personas given more time to improve the work or justify stopping |
| 10 October, 09:00:23 | 10 October, 14:00:23 | Five-hour review of file organization and discovery through grep/search and regular-expression cues, with the detailed focus below |
| 10 October, 02:12:20 | 10 October, 12:12:20 | Ten-hour complete review, including tool and skill use, asset management, relevant retained data, selection of tools shaped by character, and installation where applicable in the examples |
| 10 October, 00:24:11 | 10 October, 10:24:11 | Assignment concerning sustained work, improvement, and justified continuation or stopping |
| 9 October, 22:09:20 | 10 October, 08:09:20 | Earlier ten-hour assignment |

The **09:00:23 request** focused on whether file organization and search cues connecting fragments as a navigable network effectively select the right characteristic fragments, prompt parts, and other context for each persona's current need at each LLM call. It called for avoiding unwanted fragments and bloated context, using step-by-step hypothetical examples to identify issues, and making needed design or case updates.

These requests followed earlier five-hour and ten-hour assignments and the clarification that ten-minute updates are suitable.

**UR-038 Audit the whole requirement set and design.** Thoroughly research and audit every published and unpublished design document line by line against all user requirements. Identify issues, determine how the design should work, and make the updates, revisions, or deletions needed to align the whole design with those requirements. Use multiple research agents for this assignment.

**UR-039 Publish reviewed design fixes incrementally; keep audit work internal.** Publish completed, reviewed design fixes to the GitHub remote research branch in ai-personas-design. Continue the remaining work instead of waiting for the entire research period to end. The earlier assignment requested a new branch.

Keep audit reports, internal audit walkthroughs, and research process notes internal. Use their findings to repair the design rather than publishing them as audit files.

**UR-040 Consolidate human-user requirements in one file and publish it.** Rephrase all relevant human-user messages as requirements in a single design document and push it to the remote branch. Include later clarifications and combine repeated requests. Only the user's messages supply these requirements.

## Historical investigation and runtime requests

The following requirements record earlier assignments. The later request in UR-001 makes the current repository design-only.

**UR-041 Investigate and fix the reported runtime root causes.** The 1 October assignment requested GPT 6 Pro to examine the linked implementation and design branches and investigate the supplied house-run problem report. It requested finding and fixing the root causes, establishing a GitHub write session before starting, and pushing the changes.

**UR-042 Run the earlier model comparison.** The 4 October assignment requested starting AiPersonas and running house-design and DC-to-AC circuit-design tasks with GPT 5.6 Sol and Luna to observe how the system worked and what issues arose.
