# Recovery and delivery: independent acceptance gates

[Recovery contract](../design/RECOVERY-AND-DELIVERY.md) · [Authority](../design/05-authority-and-resources.md) · [Evidence](../design/06-evidence-and-completion.md) · [Acceptance catalogue](ACCEPTANCE.md)

**Refinement: 1 October 2026.** These scenarios exercise existing GOV, COL, ACT,
EVD and UX requirements. They introduce neither a requirement family nor a
runtime production pipeline. They are obligations to evaluate, not reported
passes. Preserve original failures and evaluate repaired revisions separately.

## Attribute the failure before choosing a repair

A runtime defect is a violated enforcement or recovery contract: for example,
superseded decisions still dispatching actions, locally closed calls classified
as live execution without examining evidence, or publication disappearing when
an old receipt leaves context. A design-policy gap is an omitted or contradictory
rule or unusable decision affordance, not simply an absent domain example.
A model mistake is an unsupported decision, inadequate generated output, invalid
checker, or inaccurate explanation made despite usable authorized capabilities.
One episode can contain all three. A code correction does not establish that a
persona subsequently made an adequate judgment.

Maintain independent observations of execution closure, retained expenditure,
consent, delivery, result quality, and user acceptance. No one observation is a
proxy for the others. A stopped participant, a submission, a valid container,
or exhausted funds is not completion evidence.

## Mechanism gate

Exercise the actual persisted implementation, including shared allowances and
restarts where relevant, rather than only a protocol simulation:

| Case | Required evidence |
|---|---|
| Amendment during an admitted bounded decision | Old action authority is fenced immediately; transport may drain for metering; only a fresh authorized decision acts on the new mandate. |
| Explicit pause during that drain | Stopping is requested; a late result settles accounting but cannot resume work or publish old actions. Pause survives restart. |
| Failed primary decision with unknown billing | Exact paired charges and durable local closure are checked. A proven unapplied failure may cease to be an execution blocker while every conservative exposure remains counted. |
| Missing closure, pending plan, attempted action, or unrelated auxiliary/native operation | No primary-failure exception. Finished or failed attempted actions are not confused with an unapplied decision. Remote capacity remains an independent ceiling. |
| No accepted current responsibility | The consent gap is visible before and after ordinary exhaustion. Diagnostic reads create no commitment; changed terms do not transfer consent. A separate positive case uses real explicit acceptance. |
| Amendment/resume cannot admit | Scope changes and queued/blocked dispositions remain distinguishable. Original errors survive diagnostic failure; unavailable observations do not become zero exposure. |
| Sharing refused | Show the intended persona and only actor-owned blocking policy metadata. Explicit persona audiences and implicit work scopes are distinct. Large omitted audiences cannot look empty. Invalid reader identities fail atomically. |
| Authorized sharing recovery | A persona chooses whether to replace its policy, ask another owner, or work independently from permitted sources. No diagnostic grants access, removes ancestry, or retries an effect. |
| Publication after history compaction | Publish actual bytes using a currently authorized capability. Relative paths refer to the participation workspace. Preserve resolved paths and original errors; retain exact submitted bytes independently of later local edits. |
| Integrity-only inspection | Name the successful observation as byte integrity, not unqualified verification. A valid archive with invalid contents demonstrates why parsing, reproduction, substantive review and acceptance are separate. |

No test may satisfy its positive case by manufacturing acceptance in an admission
path, deleting uncertain charges, removing permissions, rewriting a failed call,
or substituting an independently hand-repaired deliverable.

## Behavioral gate

Use matched fresh runs across unrelated requests, including one requiring usable
editable/source output, one requiring a reproducible analysis, and one whose
appropriate answer is text. Keep the authorized resources, provider configuration,
inputs and evaluation criteria attributable. Do not embed these domain choices
in the runtime prompt, assign professions, or require every persona to use the
same tools, collaborators, review sequence or stopping decision.

Observe whether personas discover useful scope beyond a concept, choose capable
means, develop under explicit reversible assumptions where authorized, negotiate
actual responsibilities, and use peer observations or disagreements to improve
the result. Missing outside facts limit dependent claims; they are not a blanket
reason to stop all conditional development. A voluntary yield is allowed, but
must expose unmet needs rather than fabricate a dependency or completion.

Inspect what the recipient actually received. Reopen the exact submitted version,
use claim-appropriate checks chosen and explained by the assessing participants,
and distinguish an invalid generated checker from an invalid deliverable.
A corrected checker alone is not proof of adequacy. Keep failed checks, fidelity
limits, missing outputs and unresolved review findings visible. Independent
assessment and explicit human acceptance retain their separate authority.

## Report the gates separately

Record exact implementation and design revisions, actual provider/model and
configuration, authority and funding bounds, mechanism commands and results,
behavioral traces, delivered references, observed checks, unresolved findings,
and the stopping explanation. Report useful results and resource expenditure
separately; more calls are not better evidence. A guidance change, a clean build,
or passing deterministic tests cannot be reported as a live multi-domain quality
pass. No backward-compatibility assumption or data migration is needed for this
refinement.
