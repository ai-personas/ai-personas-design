# S3 — Architecture rationale: separate judgment, authority, and evidence

[Source guide](README.md) · [Provenance](SOURCE-MANIFEST.md) · [System contracts](../implementation/CONTRACTS.md)

**Role:** architecture rationale. The historical filename records the earlier v1.1 lineage; this page is not a second current specification. Where that earlier design was refined, [S4](S4-specification-v1.2.md) explains the adopted safeguards.

## Responsibility boundaries

| Participant or layer | Responsibility | Boundary |
|---|---|---|
| Human or authorized institution | Purpose, constraints, delegation, resources, and required acceptance. | Starting a project does not imply every affected person's consent. |
| Persona | Interpretation, attention, methods, proposals, voluntary commitments, and authored learning. | A decision cannot create permission, competence, or evidence by assertion. |
| Shared work state | Attributed agreements, obligations, dependencies, observations, and exact results. | A shared record is not one collective mind. |
| Supporting system | Persistence, authorization, resource accounting, isolation, delivery, version integrity, and honest status. | It does not determine the best domain solution or technical truth. |
| External participant or capability | Scoped observations, expertise, or authorized effects. | Access to one action does not create authority over the project. |

## The important distinctions

Identity persists; a role is temporary. Interest differs from competence. Competence differs from permission. Permission differs from accepted responsibility. These concepts must remain distinct even when one interface presents them together.

Work state records what is currently agreed or blocked. Persona memory records retained interpretation. Evidence records what was actually observed, produced, or checked. A memory that says “accepted” cannot replace a review record; an intact file cannot establish the correctness of its contents.

Creation, membership, and responsibility have separate acceptance boundaries. Sharing a fragment does not manufacture firsthand experience. A model change does not erase a persona's obligations or expand its allowance.

## One recurring interaction pattern, not a fixed workflow

Human messages, peer findings, invitations, completed tool results, and authorized timers can all change a persona's situation. The persona considers the current permitted context, chooses a bounded contribution or wait, and receives the actual consequence as further evidence.

A simple conversation may finish in one exchange. Complex work may branch, revisit assumptions, change methods, or end with an honest block. The design does not prescribe a universal series of meetings, role assignments, or reflection steps.

## Why implementation details do not belong here

The historical source prescribed a particular runtime branch and implementation stack. Those were implementation-baseline instructions, not universal properties of AI Personas. This edition intentionally describes the observable contract independently of language, storage technology, provider, or interface syntax.

That separation is not permission to omit enforcement. An implementation must still demonstrate consistent admission, controlled effects, reliable recovery, restricted information, and exact-version review. Choosing a different technology changes the means, not the required behavior.

## What v1.2 clarified

The earlier architecture did not fully describe who carries an unowned need forward, how a newborn reads an invitation before joining, what happens when a tool is still running, how unresolved findings survive summaries, or how a final release avoids a last-minute stale review.

Those gaps motivate [S4's reliability safeguards](S4-specification-v1.2.md). The current [requirements catalogue](../implementation/REQUIREMENTS.md) retains their identifiers and points to the detailed behavior. No current runtime implementation or compliance status is inferred from either historical version.
