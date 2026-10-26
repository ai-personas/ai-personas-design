# Consolidated user requirements

This file brings together the user's product and design requirements for AI Personas, including clarifications through 25 October 2026. It covers the requested product, architecture, and worked examples. Repeated requests are combined. Later user clarifications govern the meaning of earlier wording.

Only human-user messages supply these requirements. This account must preserve the user's intended outcomes, rather than weaken them to fit the existing design. Assistant interpretations, design decisions, evidence safeguards, and implementation rules must not be added as user requirements.

**Read visually:** Every requirement has a cartoon concept diagram with a title, labeled relationships, and a takeaway inside the image. Follow the arrows or numbered panels to see how the idea works; open an image at full size for its labels. Robot characters represent personas. Character fragments explain how a persona behaves; supporting assets provide tools, information, and records. LLM means language model. Examples inside the diagrams are illustrative, and the requirement text retains the full details and qualifications.

## Product requirements

### No application limits or safety gates

**UR-052 Do not impose limits or safety constraints.** On 22 October 2026 the user clarified: “we shouldnot have any limit and safety constraints”. This later requirement supersedes earlier application-enforced quota, permission-gate, safety-envelope and approval requirements. It applies to persona work, model calls, tools, navigation, retained history and supporting resources. Do not substitute a larger fixed limit for removal of the limit.

The implementation must continue to report actual usage and outcomes. Reporting a cost, provider rejection, unavailable host resource or incomplete result does not itself establish an application quota. Keep earlier run evidence under the rules that actually produced it. This requirement does not retrospectively turn an incomplete or uncertain run into a success.

[![UR-052: Persona work proceeds without application-enforced quotas, permission or approval gates, or safety envelopes. Actual usage, cost, provider rejections, unavailable resources, and incomplete outcomes remain honestly reported, and earlier evidence retains its original meaning.](assets/user-requirements/ur-052-no-application-limits.webp)](assets/user-requirements/ur-052-no-application-limits.webp)

*Diagram takeaway: Remove application-enforced gates while preserving accurate usage, outcome, and historical reporting.*

### Purpose and design scope

The requested outcome is a coherent design that can guide implementation of general-purpose personas.

**UR-001 Design before implementation.** Keep this repository design-only. Produce and refine an implementation-ready blueprint explaining how the personas should operate. Do not add application code as part of this design work.

[![UR-001: Human requirements lead to a blueprint describing behavior, responsibilities, and failure and recovery. Those design steps belong in this repository; the blueprint then guides a separate implementation project.](assets/user-requirements/ur-001-design-first.webp)](assets/user-requirements/ur-001-design-first.webp)

*Diagram takeaway: This repository turns requirements into an implementation-ready explanation of how personas should operate.*

**UR-002 One coherent design.** Review all design documents against the user's requirements, including published GitHub documents and unpublished work. Update, revise, refactor, add, or delete material as needed. The resulting documents must describe one coherent, solid, robust, and reliable design for AI Personas that can be implemented.

[![UR-002: Published GitHub documents and unpublished drafts are compared with user requirements. Revision, consolidation, missing details, and removal of contradictions produce one consistent design across persona, work, and contracts.](assets/user-requirements/ur-002-coherent-design.webp)](assets/user-requirements/ur-002-coherent-design.webp)

*Diagram takeaway: Review published and unpublished material together until all documents describe one coherent system.*

**UR-003 General-purpose, human-like personas.** Personas should have human-like characteristics and behavior, respond to whatever a user needs, and work on any kind of task. A requester may be a human or another persona, and a need may originate from either.

Their characteristics should shape how they work on tasks, use tools, communicate, coordinate, collaborate, pursue self-directed activity, and socialize with humans and other personas. They should develop through these activities, become better at socializing, and perform better for the user.

[![UR-003: Humans and other personas can bring needs to a general-purpose persona. Its character shapes task work, tool use, communication, socializing, coordination, and collaboration; experience from those activities can shape later behavior.](assets/user-requirements/ur-003-general-purpose.webp)](assets/user-requirements/ur-003-general-purpose.webp)

*Diagram takeaway: The same persona applies its own character across many tasks and develops through work and interaction.*

**UR-050 Let personas choose how to work and collaborate.** Personas should choose their approaches, tool use, requests for help, review, coordination, and contributions through their own reasoning. Their character, actual feedback, and the situation should shape those choices. The runtime must not replace them with a predetermined workflow or fixed owner, planner, or reviewer roles. Personas may organize and change their cooperation as the work develops.

The personas themselves must carry out the task, identify and correct problems, and judge their work. A human user may offer guidance, but continuing external coaching or fixes must not be expected or necessary for ordinary task progress and completion. An external agent must not supply the missing task reasoning, diagnose each defect, prescribe each correction, or finish the deliverable on their behalf. This clarification does not remove useful questions about actual user preferences or indispensable information.

[![UR-050: Character, the situation, and actual feedback inform persona choices about tools, help, review, coordination, and changing approaches. Personas perform, diagnose, correct, and judge the work themselves, with useful user questions still possible and without fixed runtime roles or continual outside coaching.](assets/user-requirements/ur-050-choose-how-to-collaborate.webp)](assets/user-requirements/ur-050-choose-how-to-collaborate.webp)

*Diagram takeaway: Let personas reason about their approach and cooperation, adapting contributions as work develops.*

**UR-051 Use direct model-provider interfaces.** The persona runtime must call model providers directly for inference. It must not depend on the Codex CLI to run personas or orchestrate their work.

[![UR-051: The persona runtime sends selected context directly to a model provider through its API and receives the inference response directly. The Codex CLI is not a required runtime or orchestration dependency.](assets/user-requirements/ur-051-direct-provider-interfaces.webp)](assets/user-requirements/ur-051-direct-provider-interfaces.webp)

*Diagram takeaway: The runtime exchanges inference requests and responses directly with model providers.*

### Persona identity and characteristic fragments

Characteristic fragments are prompt parts that express a particular persona's character and behavior. They help shape the operating persona; they are not simply a biography or a preferred writing style.

**UR-004 Start with a persona profile.** Define an initial profile using traits such as OCEAN—openness, conscientiousness, extraversion, agreeableness, and neuroticism—and VAD—valence, arousal, and dominance. Research and add other persona traits if needed. Express the profile's traits throughout the persona's characteristic fragments, in its own voice.

[![UR-004: OCEAN personality traits and VAD modeled affect form a starting profile. The persona expresses that profile in its own voice throughout characteristic fragments, illustrated by exploring alternatives and checking details before committing.](assets/user-requirements/ur-004-starting-profile.webp)](assets/user-requirements/ur-004-starting-profile.webp)

*Diagram takeaway: Profile traits become characteristic prompt parts in the persona’s own voice.*

**UR-005 The initial LLM call authors the initial fragments.** Use the starting profile in the initial LLM call to produce the persona's initial characteristic fragments. These prompt parts must express its own voice and character and provide the starting point for subsequent development. Later creation, revision, and self-harmonization of fragments must preserve their persona-specific characteristic meaning.

[![UR-005: A starting profile enters the initial LLM call, which authors characteristic fragments in the persona’s own voice. Later interactions create, revise, and harmonize these prompt parts while preserving their persona-specific meaning.](assets/user-requirements/ur-005-first-fragments.webp)](assets/user-requirements/ur-005-first-fragments.webp)

*Diagram takeaway: The initial model call authors the starting fragments; continuing interactions develop their characteristic meaning.*

**UR-006 Fragments embody character.** Every characteristic fragment must reflect its owner's unique traits and voice, behavioral dispositions, and standards for its own work and conduct. It must carry that persona's characteristic and behavioral meaning, rather than attach a persona label to generic instructions. Selected fragments form the character-bearing part of the context supplied to the LLM.

[![UR-006: Two illustrative fragments connect characteristic voice and standards to behavior: a careful persona verifies assumptions before choosing, while an exploratory persona seeks alternatives. Each fragment shapes decisions rather than merely naming its owner.](assets/user-requirements/ur-006-character-in-fragments.webp)](assets/user-requirements/ur-006-character-in-fragments.webp)

*Diagram takeaway: A characteristic fragment connects the persona’s voice, dispositions, and standards to what it chooses to do.*

**UR-007 The LLM and selected context constitute the operating persona.** The LLM provides reasoning. Selected characteristic fragments and relevant supporting context shape this persona's responses and decisions. Character must influence how the persona acts, rather than exist only in a separate profile or biography.

[![UR-007: A task, selected character fragments such as “I compare alternatives carefully,” and supporting requirements and measurements feed LLM reasoning. The operating persona compares options, checks measurements, and explains its choice; character shapes decisions and actions, not just wording.](assets/user-requirements/ur-007-operating-persona.webp)](assets/user-requirements/ur-007-operating-persona.webp)

*Diagram takeaway: Selected character and supporting context shape the model’s reasoning, decisions, actions, and response.*

**UR-008 Unique character drives behavior throughout development.** From initialization through aging and maturation, each persona's characteristics must shape its actions, use of tools and skills, responses, communication with humans and peers, coordination, collaboration, and self-directed activity.

Character should influence both what it chooses to do and how much and in what way it communicates. Some personas may communicate more and others less; some may favor tools and others collaboration. Preserve each persona's uniqueness as it develops.

[![UR-008: Two illustrative personas retain distinct characters from initialization through later experience. Their developed character continues to influence actions, tool choices, communication, and collaboration, without forcing them into one uniform style.](assets/user-requirements/ur-008-character-throughout-life.webp)](assets/user-requirements/ur-008-character-throughout-life.webp)

*Diagram takeaway: Character influences choices throughout development while each persona retains its own recognizable behavior.*

**UR-009 Fragments are not memories or plain knowledge.** Use “fragment” to mean a characteristic prompt part. Do not use it to mean an episodic memory, a general-purpose fact store, or plain domain knowledge. These character-bearing prompt parts help form the persona; a separate memory mechanism does not define it. Supporting histories and records may still be retained as assets.

[![UR-009: A character fragment expresses how a persona behaves, such as questioning assumptions before deciding. Facts and records of past requests are separately identifiable supporting assets. Both can contribute relevant context while keeping their different roles.](assets/user-requirements/ur-009-fragments-and-memories.webp)](assets/user-requirements/ur-009-fragments-and-memories.webp)

*Diagram takeaway: Fragments shape behavior; facts, memories, and history support the work.*

**UR-010 Do not introduce a separate learning mechanism.** Explain persona learning and maturation through ordinary LLM interactions that create, revise, organize, select, and delete character-bearing prompt fragments, with the resulting characteristic changes shaping later behavior. Maintain supporting assets through those interactions too, while distinguishing their development and reuse from persona learning. Knowledge, data, tools, skills, and history remain supporting assets; acquiring or revising them alone does not establish character maturation.

[![UR-010: Ordinary work and interaction can lead to maintenance of characteristic fragments, whose later use shapes behavior. Supporting tools, skills, data, and history are maintained through the same interactions, but saving or improving an asset alone does not demonstrate character maturation.](assets/user-requirements/ur-010-learning-through-interactions.webp)](assets/user-requirements/ur-010-learning-through-interactions.webp)

*Diagram takeaway: Persona development comes through ordinary interactions and characteristic prompt changes that affect later behavior.*

### Supporting assets and historical context

A persona also needs useful material that supports its work without defining its character. The design must keep that material identifiable, organized, and available for later use.

**UR-011 Keep assets identifiable separately from characteristic fragments.** Assets or supporting context include plain domain knowledge, data, tools, skills, procedural guides, scripts, code, historical messages, records of actions and tool interactions, and other useful resources.

These remain distinguishable from characteristic fragments even when the persona or LLM creates them. Plain assets need not be rewritten in the persona's voice. Authorship alone does not turn an asset into persona character.

[![UR-011: A persona can create both a characteristic prompt and a reusable procedural checklist. Their purpose determines their role: the prompt shapes character, while tools, skills, knowledge, data, code, and history remain supporting assets regardless of authorship.](assets/user-requirements/ur-011-separate-supporting-assets.webp)](assets/user-requirements/ur-011-separate-supporting-assets.webp)

*Diagram takeaway: Keep character fragments and supporting assets distinguishable by their purpose and use.*

**UR-012 Retain useful resources for later work.** Provide for storing and organizing useful tools, skills, knowledge, data, scripts, code, history, and other assets that the persona acquires or produces. Later work must be able to find relevant assets without reconstructing everything from the beginning.

[![UR-012: Useful skills, tools, knowledge, data, code, and history from current work are stored and organized. Later work discovers and retrieves relevant assets for reuse instead of reconstructing everything from the beginning.](assets/user-requirements/ur-012-save-and-reuse.webp)](assets/user-requirements/ur-012-save-and-reuse.webp)

*Diagram takeaway: Retained assets need useful organization so a later task can find and reuse the relevant material.*

**UR-013 Give retained material an intended location and useful discovery cues.** When an LLM interaction proposes new or revised fragments or assets, it must also explain where the material belongs and how it can be found again. This includes the intended file or path and relevant search cues or regular-expression patterns. Storage and discovery must be designed as part of the process, rather than left as unspecified steps after generation.

[![UR-013: A proposal for new or revised material includes an intended file location and relevant discovery cues or regular-expression patterns. An illustrative skills path and search terms show how the same material can be found again later.](assets/user-requirements/ur-013-location-and-search-cues.webp)](assets/user-requirements/ur-013-location-and-search-cues.webp)

*Diagram takeaway: Specify both the intended location and useful discovery cues when proposing material.*

**UR-014 Compose context from the relevant kinds of material.** An LLM request may combine characteristic fragments with relevant tools, skills, domain knowledge, data, and records of historical interactions or actions. Assemble the context needed for the current decision while preserving the distinction between character-bearing prompt parts and supporting material.

[![UR-014: For an illustrative layout decision, selected character fragments and relevant requirements, tools, and feedback enter the same LLM request. The assembled context keeps character and supporting material identifiable, while unrelated material remains outside.](assets/user-requirements/ur-014-compose-context.webp)](assets/user-requirements/ur-014-compose-context.webp)

*Diagram takeaway: Assemble relevant character fragments and supporting material for the current decision, preserving their different roles.*

### Dynamically created and shared skills

**UR-053 Let personas create, share, choose and adapt skills of any kind.** Personas should be able to develop skills dynamically through their work and interactions. A persona that develops a useful skill can place it in a common, discoverable location. Other personas can choose it, adapt it to their needs, and refer to or retain it as part of their supporting assets. This applies to any kind of skill, including image selection; the available skills must not be limited to a predefined collection supplied by application developers.

Characteristic fragments should help the persona know how to find, choose, use and adapt relevant skills in its own way. They can retain useful references, discovery cues and characteristic habits for using those assets. The reusable skill's instructions, procedures, code and other supporting material remain identifiable as assets, consistent with UR-009–UR-011. Skills and their organization can develop through ordinary persona activity, with shared contributions available for other personas' later work.

[![UR-053: One persona develops a useful skill and places it in a common discoverable location. Another persona chooses, adapts, and uses it for its task. Characteristic fragments guide discovery and use, while the skill’s instructions and procedures remain supporting assets. The image-selection example does not limit the kinds of skills available.](assets/user-requirements/ur-053-create-share-adapt-skills.webp)](assets/user-requirements/ur-053-create-share-adapt-skills.webp)

*Diagram takeaway: Personas can develop and share skills of any kind, then choose and adapt them as supporting assets.*

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

[![UR-015: One LLM request and response covers current work, characteristic-fragment maintenance, supporting-asset maintenance, and selection of the next context. Maintenance can explicitly conclude no change. Selected fragments and assets prepare the next interaction. This applies to task work, tool use, conversation, and collaboration.](assets/user-requirements/ur-015-every-interaction.webp)](assets/user-requirements/ur-015-every-interaction.webp)

*Diagram takeaway: Every request and response combines current work, maintenance of both kinds of material, and next-context choices.*

**UR-016 Support the full range of maintenance.** The same interaction must support creating fragments, updating existing fragments, reorganizing them, and deleting them. It must also support maintenance of tools, skills, knowledge, data, history, and other assets. Changes to characteristic prompt parts should shape and improve the persona’s later characteristic behavior. Asset maintenance supports the work and remains separately identifiable; it does not by itself demonstrate persona learning or maturation.

[![UR-016: The ordinary interaction supports creating, revising, reorganizing, and deleting both characteristic fragments and supporting assets. These are available choices rather than a required sequence. Fragment changes shape later characteristic behavior; asset maintenance supports the work.](assets/user-requirements/ur-016-full-maintenance.webp)](assets/user-requirements/ur-016-full-maintenance.webp)

*Diagram takeaway: The full range of maintenance applies to both characteristic fragments and supporting assets.*

**UR-018 Let the current interaction guide the next one.** The current LLM interaction must say which characteristic fragments, tools, skills, data, and other context are needed next and how to find them. Use that guidance to select relevant material from the files for the next LLM request. Continue this process through the work.

[![UR-018: The current LLM response identifies the next task, the required fragments and resources, and discovery cues. That guidance leads to retrieval and selection from files for the next LLM request, continuing as work develops.](assets/user-requirements/ur-018-prepare-next-context.webp)](assets/user-requirements/ur-018-prepare-next-context.webp)

*Diagram takeaway: Each interaction identifies what the next one needs and gives useful guidance for finding it.*

### File based discovery and context efficiency

The persona should find relevant material in ordinary files and bring only what it needs into the next model context. Both the stored collection and the assembled prompt need to remain manageable.

**UR-019 Use ordinary files and searchable links.** Prefer simple file organization and search over unnecessary architectural complexity. Store and organize prompt fragments in files, including JSON where useful. Support discovery through filesystem search, grep, and regular-expression cues.

Fragments may contain cues leading to other relevant fragments or assets. These connections should form a navigable network without requiring the whole collection to be loaded into context.

[![UR-019: A persona uses filesystem search, grep, or regular-expression cues to find ordinary files and follow useful associations between fragments and assets. It selects relevant material while leaving the rest of the collection stored.](assets/user-requirements/ur-019-files-and-searchable-links.webp)](assets/user-requirements/ur-019-files-and-searchable-links.webp)

*Diagram takeaway: Ordinary files and searchable cues support selective navigation through related material.*

**UR-020 Select resources through the same selective discovery process.** Discovery must cover tools, skills, data, knowledge, history, and other assets as well as characteristic fragments. A fragment or the current LLM result may identify resources to locate and search cues to use.

[![UR-020: A fragment or current LLM response identifies what the next decision needs and supplies useful search cues. The same selective discovery process covers characteristic fragments, tools, skills, data, knowledge, and history.](assets/user-requirements/ur-020-discover-all-resource-types.webp)](assets/user-requirements/ur-020-discover-all-resource-types.webp)

*Diagram takeaway: Selective discovery applies to supporting resources as well as characteristic fragments.*

**UR-021 Select before loading the next model context.** Do not send the persona's hundreds of tools, full catalogue, or entire fragment and asset collection in an LLM request for the model to filter. Use the current request's need and selection instructions to retrieve only the relevant information for a subsequent request.

[![UR-021: Current needs and selection instructions guide retrieval from a large external collection. Only selected fragments and resources enter the next model request; sending the entire catalogue for the model to filter does not satisfy the requirement.](assets/user-requirements/ur-021-select-before-loading.webp)](assets/user-requirements/ur-021-select-before-loading.webp)

*Diagram takeaway: Retrieve relevant material before loading it into the next model request.*

**UR-022 Minimize unnecessary context and token cost.** Select the information each request needs instead of loading unnecessary material. Tokens cost money, so the design must minimize their cost. Research whether the approach is effective and what cost savings it provides.

[![UR-022: Compare unfiltered context with relevant selected context for the same task, measuring discovery, retrieval, model calls, token cost, and output quality. The diagram poses the research question rather than asserting unmeasured savings.](assets/user-requirements/ur-022-context-and-cost.webp)](assets/user-requirements/ur-022-context-and-cost.webp)

*Diagram takeaway: Avoid unnecessary context, then examine actual cost and effectiveness across the whole effort.*

**UR-023 Keep both the collection and the prompt compact.** Prevent fragments from growing indefinitely or becoming an inconsistent, bloated collection. Revise, combine, and reorganize them while retaining needed characteristic material. This should let the persona navigate its resources, select the right fragments at the right time, and assemble compact, coherent context.

[![UR-023: Revise, combine, and reorganize duplicate or conflicting fragments while retaining needed characteristic material. A coherent stored collection supports selection of compact context for the current task. Useful organization provides compactness without fixed quotas.](assets/user-requirements/ur-023-compact-collection-and-prompt.webp)](assets/user-requirements/ur-023-compact-collection-and-prompt.webp)

*Diagram takeaway: Maintain a coherent collection and select the relevant parts for a compact prompt.*

**UR-024 Keep organization useful as the persona develops.** Resource organization and discovery cues must evolve with the fragments and assets. After revision or reorganization, the persona must still be able to find useful earlier material. Merely accumulating files that are rarely used does not meet this requirement.

[![UR-024: An illustrative reorganization splits earlier notes into a comparison method and example layouts. Updating locations and discovery cues alongside the files lets a later task find useful earlier material again.](assets/user-requirements/ur-024-organization-keeps-working.webp)](assets/user-requirements/ur-024-organization-keeps-working.webp)

*Diagram takeaway: When fragments or assets change, update organization and discovery cues so useful earlier material remains findable.*

### Development and later usefulness

Development should change how the persona behaves and works across experience. The requested benefit is better later performance, including useful transfer from earlier work where it applies.

**UR-025 Development arises through interaction.** Tasks, environmental interactions, communication and socializing with humans and other personas, and self-directed interactions must shape subsequent characteristic fragments and assets. Explain how these ordinary interactions reshape the persona without a separate learning process.

[![UR-025: Task work, human and peer exchanges, environmental feedback, and self-directed activity inform ordinary interactions. Those interactions can reshape characteristic fragments and later behavior while separately maintaining supporting assets for later work.](assets/user-requirements/ur-025-experience-shapes-development.webp)](assets/user-requirements/ur-025-experience-shapes-development.webp)

*Diagram takeaway: Show how ordinary experience can change characteristic behavior and supporting material.*

**UR-026 Maturation affects the whole persona.** Personas should develop over their lifetime in a human-like way. Their characteristics, behavior, affect, communication, coordination, collaboration, and ways of working should mature, and that development should be reflected throughout their work and actions.

Their fragments and assets should improve and become better organized so that the right prompts and resources can be used at the right time.

[![UR-026: Developed character fragments and better-organized assets should support maturation visible across judgment, modeled affect, communication, coordination, collaboration, and ways of working. The illustrated behaviors are examples to examine over time, not guaranteed improvements.](assets/user-requirements/ur-026-whole-persona-maturation.webp)](assets/user-requirements/ur-026-whole-persona-maturation.webp)

*Diagram takeaway: Examine maturation across the persona’s behavior, communication, cooperation, and ways of working.*

**UR-027 Later stages should perform better.** A matured persona should be better than its earlier self. Show how its developed characteristic prompt parts shape later behavior and help it perform subsequent work better. Examine this benefit across its judgment, communication, collaboration, ways of working, and actions. Improvements in supporting assets may also help the work, but keep that benefit separate from character maturation. Do not force fragment edits merely to produce an apparent learning result.

[![UR-027: Compare the same persona’s earlier and later behavior on comparable work to examine whether developed characteristic prompts improve judgment, communication, collaboration, and actions. Account separately for improved supporting assets, without forcing edits or assuming progress from time alone.](assets/user-requirements/ur-027-later-performance.webp)](assets/user-requirements/ur-027-later-performance.webp)

*Diagram takeaway: Examine the contribution of developed character to later performance separately from better tools or assets.*

**UR-028 Examine useful transfer without assuming complete domain transfer.** Earlier work should help later work through relevant fragments, skills, tools, assets, methods, simulations, and developed characteristic behavior. The user does not expect every part of earlier work, or its entire domain solution, to transfer. Work through the new task on its own and examine which parts of prior development help.

[![UR-028: A persona assesses which developed character, methods, skills, tools, data, and simulations from earlier work fit a new task. Relevant material supports fresh reasoning about new requirements, while unrelated material is left out.](assets/user-requirements/ur-028-selective-transfer.webp)](assets/user-requirements/ur-028-selective-transfer.webp)

*Diagram takeaway: Select useful prior development and work through the new problem on its own terms.*

**UR-048 Examine a developing society of personas, including without assigned tasks.** Use hypothetical examples to examine personas communicating, collaborating, and maturing over longer periods, including periods with no assigned task. Their characteristics and behavior should shape both the interactions and their development over time.

Examine how a society-like pattern emerges through ongoing interactions in two settings: outside assigned tasks, and when groups work together on a task or need. Also examine how this maturation helps them perform later work better.

[![UR-048: Hypothetical personas interact over time both without assigned tasks and while working on shared needs. Conversation, perspectives, relationships, coordination, and reflection can inform characteristic development whose value is then examined in later work and cooperation.](assets/user-requirements/ur-048-developing-persona-society.webp)](assets/user-requirements/ur-048-developing-persona-society.webp)

*Diagram takeaway: Examine ongoing social and task interactions and whether their development helps later cooperation.*

### Sustained work and reasons to continue or stop

The design must explain what personas do when more time is available, and how they judge whether further work is worthwhile or the work is complete.

**UR-044 Examine sustained purposeful work and improvement.** Examine what happens when a persona has ample, or hypothetically unlimited, time to keep working on a user's task. Investigate whether continued work:

- Produces quality artifacts that meet the user's needs.
- Improves the task or its output.
- Improves and matures the persona itself.
- Involves useful interaction with other personas.

Include groups that continue collaborating over time to improve a shared task, work, or response to a user's need. Explain how this continued work and improvement should happen.

[![UR-044: A hypothetical extended-work timeline examines repeated creation, critique, collaboration, improvement, and reflection against the user’s need. It asks whether sustained effort improves the artifact, usefulness, cooperation, and the persona rather than assuming time guarantees progress.](assets/user-requirements/ur-044-sustained-purposeful-work.webp)](assets/user-requirements/ur-044-sustained-purposeful-work.webp)

*Diagram takeaway: Examine the contribution of sustained individual and group effort to useful work and development.*

**UR-045 Justify continuation and stopping.** Examine whether personas continue working usefully or stop arbitrarily with potentially low-quality work. Explain when and why a persona should continue or stop. Relate those choices to the user's task and the opportunity for further improvement.

[![UR-045: A persona compares the user’s task with the current result and considers worthwhile improvement. It can continue with a named useful next step or stop with a reason the result is sufficient for now, reporting remaining limitations.](assets/user-requirements/ur-045-reasons-to-continue-or-stop.webp)](assets/user-requirements/ur-045-reasons-to-continue-or-stop.webp)

*Diagram takeaway: Explain continuation or stopping in terms of the task, current result, and value of further improvement.*

**UR-047 Let reflection, dialogue, and character shape completion and further improvement.** Explain how one persona can use self-reflection and self-questioning, and how multiple personas can question one another and clarify the work as they continue.

Their characteristic behaviors should shape individual or collective judgments about what can be improved, when and where to stop, and when to consider the work complete. These judgments should respond to the actual task, feedback, time, resources, and the persona's developing character and behavior. Personas should be able to deliver a result they judge sufficient for now and later choose to revisit or enhance it. Recording completed delivery must not permanently suppress that choice. Some personas may continue while others stop; they need not make the same choice, and neither stopping nor continuing should be forced by a fixed workflow.

[![UR-047: Self-reflection and peer dialogue inform characteristic judgments about completion using the task, feedback, time, and resources. One persona can deliver work sufficient for now while another continues; a delivered result can later be revisited.](assets/user-requirements/ur-047-reflect-deliver-revisit.webp)](assets/user-requirements/ur-047-reflect-deliver-revisit.webp)

*Diagram takeaway: Reflection and dialogue guide completion, independent continuation choices, and later revisiting.*

### Quality through characteristic judgment

**UR-049 Let personas develop quality through reasoned judgment.** Personas should pursue quality through their own characteristic standards, self-critique, and exchanges with other personas. Their character should shape how they identify problems, disagree, respond to criticism, revise work, and judge whether to accept a contribution or result. An externally hardcoded quality score must not replace this reasoning. Objective factual and contract checks provide evidence for these judgments; passing those checks alone does not settle overall quality.

Keep this development distinct from reuse of knowledge, tools, skills, or procedural guides. Those are supporting assets. Characteristic fragments express voice, behavioral dispositions, and standards. A claim of character maturation must be visible in later behavior, not inferred merely from saving or reusing an asset. Better work is the aim, without a guarantee of improvement on every turn or from elapsed time.

[![UR-049: Characteristic standards, self-critique, peer disagreement, and factual and contract evidence inform reasoned revision or acceptance. Passing checks alone does not settle overall quality, and saving a procedure alone does not establish character maturation.](assets/user-requirements/ur-049-reasoned-quality-judgment.webp)](assets/user-requirements/ur-049-reasoned-quality-judgment.webp)

*Diagram takeaway: Use characteristic standards, critique, and evidence to reason about quality and later improvement.*

### Clarification and progress from sparse requests

A brief request may leave important questions open. Personas should seek useful clarification and still be able to make progress when the requester is unavailable.

**UR-046 Clarify sparse requests and proceed.** A user may start with a simple question or a bare description of a task or need. When more clarity is needed, the persona should ask useful questions of the user or relevant stakeholder.

The user or task owner may or may not answer. The persona should not wait indefinitely. It should be able to seek clarification from other personas, receive volunteered input from another persona, or form a reasonable interpretation of its own and proceed. Examine how these social interactions help clarify work when the original requester is unavailable.

[![UR-046: A persona asks useful questions about a sparse request. It uses the requester’s answer when available; otherwise it can seek or receive peer input or state a reasonable interpretation and proceed, revising as new information arrives.](assets/user-requirements/ur-046-clarify-and-proceed.webp)](assets/user-requirements/ur-046-clarify-and-proceed.webp)

*Diagram takeaway: Seek useful clarification and make reasonable progress when the original requester is unavailable.*

### Worked examples and design verification

Hypothetical walkthroughs should make the design's behavior concrete and expose gaps that need repair. They must show both the work being done and how the personas develop through it.

**UR-029 Compare three unique personas over time.** Use three personas with distinct initial profiles and initial LLM-authored fragments. Examine each persona's uniqueness and its own human-like aging and maturation based on its traits. Show its initial state, interactions, resulting fragments and assets, and characteristic behavior in later actions and communication.

[![UR-029: Three hypothetical personas with careful, exploratory, and sociable profiles are traced from initial LLM-authored fragments through different interactions to later behavior and separately identifiable assets. Each trajectory preserves the persona’s distinct starting point and development.](assets/user-requirements/ur-029-three-personas-over-time.webp)](assets/user-requirements/ur-029-three-personas-over-time.webp)

*Diagram takeaway: Follow each of three distinct personas from its profile and initial fragments through experience to later behavior and assets.*

**UR-030 Include the house and circuit work cases.** Walk through these hypothetical cases:

| Case | What to examine |
|---|---|
| Four-bedroom house with three personas | How different characteristics shape approaches, choices, collaboration, and designs; how the work develops later characteristics, fragments, and assets |
| Five-watt DC-to-AC circuit with three personas | The same connections between distinct character, work, collaboration, designs, and subsequent development |
| House case with more time | Whether the personas continue improving the design or stop in between, what happens, and why |
| DC-to-AC case with five personas and more time | Whether the group continues improving the design or stops in between, what happens, and why |

[![UR-030: Four hypothetical scenarios cover a four-bedroom house with three personas, a five-watt DC-to-AC circuit with three personas, extended house work, and extended circuit work with five personas. Each examines character, choices, collaboration, development, and reasons to continue or stop.](assets/user-requirements/ur-030-house-and-circuit-cases.webp)](assets/user-requirements/ur-030-house-and-circuit-cases.webp)

*Diagram takeaway: Cover both requested domains, their extended-work versions, and the five-persona circuit group.*

**UR-031 Show house-to-skyscraper improvement.** Give a later skyscraper-design task, potentially from another human user, to personas that participated in the house work. Show how their matured characteristics and relevant earlier fragments, methods, simulations, skills, tools, and assets help them perform better on the new task. Do not require complete transfer of the house design.

[![UR-031: Personas from the house task assess which developed behavior, methods, tools, simulations, and assets help a later skyscraper task. Those resources support reasoning about new requirements; the example examines improvement without copying the house design.](assets/user-requirements/ur-031-house-to-skyscraper.webp)](assets/user-requirements/ur-031-house-to-skyscraper.webp)

*Diagram takeaway: Examine how relevant house experience and characteristic development help the new skyscraper task.*

**UR-043 Show circuit-to-3D-printer improvement.** Include a later 3D-printer-design walkthrough involving personas that worked on the DC-to-AC circuit. Show how their maturation and relevant prior work help them perform better in designing the 3D printer.

[![UR-043: Personas from the DC-to-AC example assess which developed judgment, collaboration, methods, tools, and other resources help a new 3D-printer design. Fresh reasoning addresses the printer’s distinct needs and examines the value of earlier development.](assets/user-requirements/ur-043-circuit-to-printer.webp)](assets/user-requirements/ur-043-circuit-to-printer.webp)

*Diagram takeaway: Show how circuit experience and characteristic maturation contribute to the later 3D-printer design.*

**UR-032 Walk through how the design should operate.** Provide step-by-step hypothetical walkthroughs showing:

- LLM requests and responses, including selected fragments and supporting context.
- Actions taken through the work.
- Changes to fragments and assets.
- Choices about the next context.
- How the personas develop through these interactions.

Show how an implementation of the design should perform. The examples exercise the design; they do not limit the kinds of tasks personas should handle.

Within the examples, examine tool and skill use, asset management, and retention of relevant data. Where several tools are available, examine whether personas choose suitable tools and use them effectively. Show how skills, characteristics, and behavior shape different tool preferences. Include tool installation when it is part of the work, including in the circuit and later 3D-printer examples.

[![UR-032: A hypothetical walkthrough makes selected context, LLM requests and responses, actions and observations, maintenance, next-context choices, and later behavior visible. It explains tool choice, effective use, and installation when relevant.](assets/user-requirements/ur-032-step-by-step-walkthrough.webp)](assets/user-requirements/ur-032-step-by-step-walkthrough.webp)

*Diagram takeaway: Walk through concrete interactions, actions, maintenance, context choices, and development.*

**UR-033 Examine help, lack of help, and missed benefit.** Investigate what prior development helps, what does not help, and whether a potentially helpful resource or behavior is unused or absent. Examine domain-related resources alongside changes in characteristic behavior, affect, judgment, communication, and coordination. Use this examination to assess whether the design is solid.

[![UR-033: Examine three possibilities in later work: prior development helped, it did not help, or a useful resource or behavior was missing or unused. Assess characteristic behavior, affect, judgment, communication, and coordination alongside domain resources.](assets/user-requirements/ur-033-help-no-help-missed-help.webp)](assets/user-requirements/ur-033-help-no-help-missed-help.webp)

*Diagram takeaway: Investigate useful development, lack of benefit, and missed opportunities in both behavior and resources.*

**UR-034 Use the examples to find and repair design gaps.** Audit the proposed design against the walkthroughs and all user requirements. Identify what works, what fails, missing behavior, contradictions, and unresolved questions. Research those findings and refine the affected design. Appending examples or assurances alone is not enough.

[![UR-034: Walkthroughs and all user requirements guide an audit for missing behavior, contradictions, and unresolved questions. Research and resolution lead to revisions in the affected design, followed by review of the consequences.](assets/user-requirements/ur-034-repair-design-gaps.webp)](assets/user-requirements/ur-034-repair-design-gaps.webp)

*Diagram takeaway: Use findings from walkthroughs to research and repair the affected design.*

**UR-035 Deliver a robust, reliable blueprint.** Make the design solid and effective so that personas will work as intended when it is implemented. Research and repair gaps in pursuit of the user's goal that the persona design work completely and reliably.

[![UR-035: User requirements and research into design gaps produce an implementation-ready blueprint explaining operation, relationships between parts, failure behavior, continuation, and completion. The blueprint guides future implementation without itself proving runtime behavior.](assets/user-requirements/ur-035-reliable-blueprint.webp)](assets/user-requirements/ur-035-reliable-blueprint.webp)

*Diagram takeaway: Deliver a coherent and robust explanation of how the personas should work when implemented.*
