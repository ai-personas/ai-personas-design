# Decisions required for a deployment

[Implementation guide](README.md) · [Contracts](CONTRACTS.md) · [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) · [Status](STATUS.md)

The adopted target is a continuing persona with one accepted character account covering semantic OCEAN traits and a VAD modeled affect profile. Its primary LLM authors character-conditioned fragments, chooses next context, and returns explicit maintenance alongside each persona invocation's other work. A deployment supplies concrete operating limits and evidence for that target. It does not make semantic traits, modeled affect, or every-invocation maintenance optional; numeric representations remain optional.

Every decision below records an accountable owner, chosen policy or value, rationale, exact effective version, supporting evidence, remaining limitation, and conditions for reconsideration. Until a required boundary is resolved and demonstrated, restrict the affected capability or keep it in a clearly described test environment. This register is a decision checklist, not a production-readiness claim or a report that the separate runtime implements these choices.

## Core deployment choices

| Decision | Settled design requirement | Deployment supplies |
|---|---|---|
| Intended use | Domain-neutral choices do not guarantee every task is feasible. | Users, supported task and result scopes, exclusions, and claim-specific outside review. |
| Continuing identity | One accepted, versioned character account supplies semantic OCEAN and VAD meaning to both profile and prompt. | Creation and administration authority, truthful starting attribution, self-authorship and locked-character controls, baseline/current-state distinction, bounded generation if used, and lifecycle recovery. |
| Character representation | Natural language is sufficient; every authored fragment is character-conditioned and own-voice. | Optional facets or contextual operational tendencies with a stated purpose; any numeric anchors, provenance, display behavior, and validation. No independent profile author or deterministic trait-to-action policy. |
| Modeled affect | Baseline, transient state, outward expression, and authority stay distinct. | Event/source attribution, update and recovery rules, state lifetime, uncertainty, expression limits, and consistent version-bound views. Any numeric dynamics are tested engineering choices, not established psychological laws. |
| Primary inference | The primary LLM chooses work, authored learning, and next relevant fragments. | Exact provider/model configuration, supported inputs and outputs, request bounds, refusal and failure behavior, cancellation, metering, and continuity evidence. |
| Every-invocation maintenance | Every application-visible persona call has maintenance input; every accepted response has an explicit disposition alongside its work. | Audited call-path coverage, initialized and empty-store inputs, permission-filtered repair inputs, whole-response validation, accepted result records, allowed non-persona utilities, and provider-managed loop visibility. |
| Maintenance bounds | Mutation is selective; known unresolved candidates do not silently become no change. | Repair attempts, storage and context ceilings, deferral owner or ownership gap, prerequisite, trigger, resource and lifecycle bounds, terminal handling, and independent host stop/accounting behavior. |
| File-facing state | Named readable files, persona-chosen organization, scoped search, exact read, and attributable edits are the normal interface. | Current-state ownership, revision binding, path and rename behavior, conflict handling, atomic dependent saves, recovery, retention, and export semantics. |
| Storage | One accepted current state exists; an export or unsaved edit is not another authority. | A backend that demonstrates the contract. Canonical physical files need the same concurrency, revision, access, and crash guarantees as a transactional store. |
| Search | Literal search and explicitly supported regex operate over a declared eligible corpus. | Matching semantics, bounds, pagination, error and incomplete-result reporting, current-index recovery, and protection of private titles and counts. |
| Next context | The primary model's explicit work-scoped selection is faithfully assembled with mandatory state. | Exact selection/version records, preserve/replace/clear behavior, protected current self, qualification handling, fit limits, stale-selection recovery, and actual supplied-context evidence. |
| Qualification and provenance | Necessary corrections accompany usable full text; source restrictions follow derivatives. | Bounded exact required-accompaniment and ancestry checks, version revalidation, admission-time fit, withdrawal, erasure, and historical-source behavior. |
| Processing destinations | Read access is not permission to send data to every model or service. | Approved primary and any auxiliary destinations, data-handling terms, retention limits, disclosure controls, and credential mediation. |
| Autonomous effects | Every effect has current scoped authority independent of authored files. | Delegation, allowed effects and destinations, required approvals, durable intent, effect-unknown reconciliation, revocation, and actual enforcement. |
| Execution | A sandbox or read-only label is not a proven barrier. | Chosen host or isolated profile, tested trust model, private evaluator separation, installation policy, and external destinations. |
| Resources | Consumed use, reservations, and uncertainty remain inside one controlling allowance. | Measurable ceilings, conservative unknown usage, exposure quotations, population bounds, fairness, and protected closeout policy. |
| Acceptance | Authored judgment, independent assessment, human acceptance, and external assurance differ. | Adopted criteria, qualification and separation policy, exact subject and citation evidence, review gaps, and current release checks. |
| Delivery | Local creation, retained publication, submission, delivery, and acceptance are separate. | Actual recipient surfaces, supported artifacts, explicit audiences, current readability, durable receipts, and useful failure diagnostics. |
| Retention and recovery | Restart, renaming, retirement, and deletion cannot invent authority or success. | Retention and correction periods, backup and export boundaries, erasure behavior, durable notifications, effect reconciliation, and honest limits on recalling outside copies. |
| Optional exploration | Between-task activity starts disabled and requires finite explicit permission. | Environment, allowance, episode and recurrence bounds, expiry precision, foreground priority, scheduler assumptions, pause, and cancellation. |
| Evaluation | Target wording does not establish implementation or behavior. | Frozen fixtures, repeat counts, held-out tasks, rubrics, comparison controls, total costs, stopping rules, and bounded publication claims. |
| Distribution and contributions | Editing design does not select licensing or contribution terms. | Owner-approved terms, rights to material, attribution requirements, and evidence-governance responsibilities. |

Backend choice is an implementation choice within the file-facing contract, not a second persona design. A simple interface must not conceal required graph bookkeeping, a separate automatic author, or another model taking ownership of selection. Equally, familiar files do not eliminate the trusted records needed for permissions, exact observations, commitments, accounting, and recovery.

## Host and isolated execution profiles

Declare the initial execution default and make its consequences clear before use. A deployment can initially offer host tools or an isolated environment, but the operator's subsequent explicit mode and capability choices remain controlling. Restart must not silently reset a disabled capability or replace chosen isolation with broader host access. Mode changes use actual authorized controls and are visible before affected jobs are admitted. An informed, specifically authorized launch policy can define its scope, but neither restart nor persona prose supplies new authority or bypasses withdrawal.

The earlier handbook's specific instruction to re-enable host tools on ordinary CLI startup despite saved disabled state is retired as a universal prescription. This is a deliberate target-design change, recorded under [implementation choices](../DESIGN-DECISIONS.md#implementation-choices-no-longer-fixed-by-the-handbook). It is not a claim that an existing launcher has changed; [implementation status](STATUS.md) must report that gap honestly.

This profile supplies host-account tools without an application sandbox or a separate application execution grant for every tool. Installation, filesystem work, network use, and subprocesses remain limited by the host account, actual user delegation, and applicable approval requirements. A discovered command list is not an allowlist and does not itself authorize arbitrary effects. Host access promises neither administrator privileges, working package registries, nor successful installation. No persona file, learned procedure, or generated instruction can change the selected mode, enable a disabled capability, or widen an operator's grant.

The selected host profile provides no confidentiality between personas sharing readable files and credentials. Record-level access controls cannot enforce confidentiality outside their actual mediation boundary. A deployment claiming stronger isolation must enforce it outside persona-editable state and keep evaluator material and secrets inaccessible accordingly. Deliberate isolation cannot silently fall back to host access after failure.

Mode changes do not resume paused or canceled work, reopen archived stages, erase charges, reset uncertain remote exposure, or turn failures into success. Host tools remain subject to real funding and accounting; an unrestricted test profile is not a prerequisite or a substitute for normal accounting. Stop and configuration receipts describe their actual extent without promising rollback of completed effects or containment of every already-started subprocess.

Validation covers the declared initial default, new and existing data, a subsequent explicit disabled state, chosen isolation, authorized mode changes, restart, and actual operations. Check actual filesystem writes, subprocesses, and installation separately from settings or prompt text. A normal startup must preserve the current authorized boundary rather than fabricate a new permission event. This target does not report that its implementation has passed those checks.

## Optional features and their conditional safeguards

| Feature | Required declaration before use |
|---|---|
| E1: functional embodiment or enriched profiles | Which relationships the display explains; do not infer human consciousness, feelings, competence, or physical embodiment from profile richness. |
| E2: community or institution | Accountable sponsor, charter, real representation, membership, delegated powers, resource allocation, information policy, conflict and appeal routes, renewal, and disposition of obligations at exit or dissolution. |
| E3: sensitive human-facing use | Transparent AI identity, meaningful memory and exit choices, domain-specific policy and evidence, and no invented credentials, diagnoses, relationships, or human endorsements. |
| E4: ongoing service | Accepted owner, actual triggers, freshness, missed-event and disconnection handling, per-episode and overall bounds, renewal, retention, actual accepting escalation recipients, fallback when unavailable, and stop behavior. |
| E4: physical interface | Specific device and environment, permitted effects, required observations, operating conditions, override, observation-loss response, conflicting-controller response, safe stop, delayed effects, and independent commissioning or qualified assurance. |
| E5: conformance aids | Which claims and optional features a profile covers, exact requirement and evaluator versions, explicit omissions, and proportional use of worksheets rather than mandatory task ceremony. |
| E6: public contribution and evidence | Adoption authority, exact historical results and criteria, source rights, transparent limits, and owner-approved distribution terms. |
| Cross-host activation | Explicitly disabled activation or a separate tested transfer, exclusivity, revocation, privacy, authority, and failure contract. Read-only exchange is not activation authority. |
| Auxiliary retrieval experiment | Specific demonstrated retrieval problem, allowed destinations and data, exact file references, measured total cost and quality, bounded fallback, and primary-model ownership of final next-context choice. |
| Numeric trait or affect representation | Optional declared engineering anchors, actual provenance, and a consistent view of the same accepted character account. Required semantic OCEAN/VAD meaning remains even without numbers. Existing values are neither fabricated nor silently erased; scores create no task router, effort quota, authority, or validated psychology claim. |

Enabling personal exploration does not enable a perpetual service or physical control. A service's simulated stakeholders do not supply human consent; extra personas do not multiply votes or funding. Completing an episode does not renew it. Absence of an essential human escalation recipient requires narrower operation or safe pause under the adopted policy.

An optional feature cannot exempt a persona LLM call from maintenance. A narrowly scoped OCR, image, or mechanical transformation service need not author fragments when it is genuinely a non-persona utility; its output remains attributable input for the next governed persona decision. Classify by what the call decides, not by its name. Provider-internal routing or token computation is not an observable persona-call inventory.

## What the design deliberately does not select

This edition selects the persona-facing mechanism and its behavioral responsibilities. It does not choose a vendor, price, cloud service, storage engine, universal numerical budget, professional tolerance, retention period, benchmark success threshold, or repository license. An optional helper or extension must justify its actual burden and evidence within the same authority and resource boundaries. Publication of these decisions cannot make the separate runtime compliant.

Use the [decision worksheet](../templates/README.md#design-decision-and-evaluation-record) for the chosen scope, accountable owner, evidence, and unresolved feature restriction. An unresolved implementation question belongs here or in a scoped implementation gap, not in a competing active persona architecture.
