# Fragment recall — illustrated reading guide

[Start with the design](FRAGMENT-RECALL.md) · [Personal network](FRAGMENT-PERSONA.md) · [Contract](../implementation/FRAGMENT-RECALL-CONTRACT.md) · [Acceptance](../evaluation/FRAGMENT-RECALL.md)

These five original SVG illustrations are editable image assets, not Mermaid diagrams, product screenshots, or execution evidence. Each image has an accessible title and description, and a complete text reading below. Their colors distinguish parts of an illustration, not functional categories in the fragment graph. Images are explanatory; the written contracts define behavior.

## 1. One persona, two model roles

![Indexed retrieval, optional Jev assessment, checked context, and the primary work-and-learning call form one bounded loop.](../assets/visuals/fragment-recall-01-overview.svg)

A new task, reply, or result supplies entry points to the persona's indexed graph. The index finds permitted candidates without showing the model the whole archive. An optional Jev selector assesses a small shortlist. The context compiler checks its recommendations and combines them with current required information. The primary persona LLM performs work and authors fragment and connection changes in the same response. Accepted updates and future attention return to the graph.

A dashed path bypasses the selector only through the declared permitted local fallback. It does not bypass ownership, source permissions, versions, or funding. A solid return path represents accepted graph updates, not automatic self-training or replay of effects. The two model roles are distinct: only the primary persona LLM authors memory.

## 2. Connections with meaning

![A six-fragment network uses authored situations instead of folders or a root; current character is pinned only by an inclusion policy.](../assets/visuals/fragment-recall-02-graph.svg)

Six hypothetical first-person fragments describe a checking preference, a source-version test, a useful exchange with Rowan, a rounding exception, comparison of explanations, and preparation of a focused question. The fragments are not classified into mental functions. Directed edges say when one should recall another: a peer has replied, a check is needed, new evidence arrived, or an exception must accompany a method.

The current-character fragment A is consistently supplied by an explicit policy. It is not the parent of the graph. Connections can cycle, but traversal is bounded. The E-to-D edge brings the exception into consideration with the method. No edge means “execute this action,” and none certifies that a recollection is universally correct.

## 3. Large memory, small context

![Illustrative archive and shortlist sizes show that the whole graph is not sent to Jev or the persona LLM.](../assets/visuals/fragment-recall-03-selection.svg)

An illustrative archive of 10,000 fragments stays in storage. Indexed search proposes 24 candidate packets. At most two independent questions per candidate produce a possible 48-question selector batch; the normal path may skip the selector entirely. These counts are experimental design examples, not provider limits or measured performance.

The compiler receives valid assessments and protected current context. It fetches exact selected text, includes important qualifiers, and allows optional previews only within the remaining budget. Independent relevance judgments do not remove the need to handle duplication and coverage. A growing archive is not permission to grow the model request without a bound.

## 4. Learning happens in the work

![Three ordinary calls are separated by actual observations; each combines useful work with authored fragment changes.](../assets/visuals/fragment-recall-04-continuity.svg)

In the hypothetical first call, Iris sends a focused question and can retain only a tentative plan. A real reply arrives before the second call. In that call Iris chooses an actual check and writes a scoped interpretation of the exchange. The actual check result arrives before the third call, when Iris can repair or redirect work and revise a method from evidence.

Optional recall assessments can precede these calls, but no additional generative reflection call is inserted between work and fragment authorship. A requested effect is never represented as an observed result. Each accepted response also prepares attention for a subsequent need.

## 5. Permission before selection

![Current-store checks precede any selector disclosure, and a final recheck controls whether the primary call may proceed.](../assets/visuals/fragment-recall-05-boundaries.svg)

Before disclosure, the runtime checks owner and source access, the approved processing destination, and funded exposure. The selector receives only eligible material and returns advisory assessments. Remote-processing denial or an unavailable or invalid selector can lead only to a declared local fallback that respects the same source restrictions. Source denial itself is never permission to use the content locally.

A final check examines current versions, cancellation, character, authority, and the whole-request budget. A valid current request may reach the main LLM. A stale mandatory reference or a core that cannot fit blocks or follows bounded recovery. Fallback is not invented Jev approval, extra funding, broader access, or automatic replay. Real selector usage remains recorded even if the main call does not proceed.

## Artwork and review

The SVG files are self-contained vector artwork with no scripts, external images, embedded fonts, or external font requests. Text is selectable in supporting viewers. Repository Markdown embeds the SVG images directly, so no diagram-language renderer or executable build step is needed to read them. The illustrations were rendered to PNG and visually inspected during preparation. That verifies presentation only, not runtime or model behavior. Unchanged older artwork is not claimed as freshly validated.
