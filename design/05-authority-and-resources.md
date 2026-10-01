# 5. Authority, resources, and bounded autonomy

[Design index](README.md) · [Previous: action](04-capabilities-and-action.md) · [Next: evidence](06-evidence-and-completion.md)

## Authority comes from people, not from generated decisions

A human or authorized institution controls the root delegation. Every downstream grant must be no broader than its controlling grant. A persona's preference, capability, group membership, reputation, model response, or working agreement cannot create new authority.

Autonomy means choosing and performing permitted actions without asking about every reversible detail. It does not mean unrestricted access, spending, publication, replication, or continued activity. A request to solve a problem is not blanket permission to contact third parties, change accounts, or operate machinery.

## What a grant must make clear

A grant identifies the controlling principal, permitted actor or delegation, work and environment scope, resources or destinations, allowed effects, content or payload envelope where relevant, limits, expiry, and revocation conditions. Material changes require a current authority check.

| Effect class | Examples of the boundary to specify |
|---|---|
| Observation | Which documents, accounts, records, or sensors may be read. |
| Local work | Which workspace may change and which computation may be used. |
| External communication | Which identity, destination, audience, and material may be affected. |
| Financial effect | Which expenditure or commitment is permitted and under which ceiling. |
| Physical effect | Which device, location, action, and operating conditions are permitted. |
| Replication | Whether additional personas may be created and within which bounds. |
| Administration | Who may change identity lifecycle, delegation, membership, or governance. |

These are generic authority boundaries, not task classifiers. The same publication rule can apply to many domains. Approval requests should describe the real effect in ordinary language rather than only naming a tool.

## Information and credentials

Access must be checked at use time and across all representations: full records, previews, search snippets, relationship views, counts, summaries, profiles, exports, and seed material. A private title or relationship can disclose information even when its body is hidden.

Credentials remain outside ordinary persona memory and model context. A connection can expose a safe label and permitted operations. Giving an untrusted tool the actual credential still gives it access to that credential; calling the reference opaque does not remove the risk.

Imported material cannot automatically execute, grant permissions, or become trusted operating instructions. Independent evaluator material must remain outside learner-controlled environments. Shared factual context does not imply shared secrets or unrestricted private memory.

## Resource conservation

Track the relevant dimensions separately: inference calls, input and output usage, elapsed time, concurrency, storage, paid operations, monetary exposure, and persona population. A deployment identifies which dimensions are measurable and enforceable; unknown quantities remain visible.

Before admission, reserve the required capacity. After observations arrive, reconcile actual usage, remaining reservations, and uncertain exposure. All descendants, initialization, retries, compaction, review, and reporting draw from the controlling allowance or an explicit transfer within it.

**Consumed resources, uncertain exposure, and outstanding reservations together must remain within the authorized ceiling for each enforced dimension.**

A transfer moves capacity; it does not copy it. A new persona has no new money. Retirement does not restore money already spent or reset birth limits. Concurrent requests cannot each use the same last unit of capacity. Unknown price or usage is not zero and must not be silently refunded.

A monetary ceiling can be called hard only where trustworthy upper bounds and execution controls support that claim. Otherwise the deployment must describe a weaker bound honestly and restrict actions accordingly.

## Protect the capacity needed to finish

Where review and repair are required, the principal or resource delegate should reserve explicit closeout capacity inside the root allowance. The amount is a work-specific decision, not a universal percentage or guarantee of sufficiency.

Ordinary production, optional improvements, additional births, and exploratory loops must not consume protected closeout capacity without authorized reallocation. Transfers preserve the same overall ceiling and uncertain exposure.

When production resources become insufficient, the system should preserve a useful baseline or partial result and expose the scope or funding decision needed. It must not spend everything generating outputs and then remain indefinitely “almost complete” because nobody can review or report them.

Mechanical stopped-state reporting, current status, and preservation of existing evidence must remain possible without another successful model call. Review resources must also correspond to an actual accepted review responsibility; a reserved allowance alone does not create a reviewer or expertise.

The principal may preauthorize automatic use of protected funding when ordinary
call or token capacity is exhausted. This is an allowance policy for any domain,
not a task workflow. A transition requires an already runnable participant and a
current responsibility that the same persona accepted under the current mandate.
Where several qualify, a stable creation-order rule may choose the funding
reference; this does not assign a profession or prescribe the next activity.
Record the authority, exact commitment revision, quote and funding pool. Normal
updates may rebind that same commitment only while it remains eligible.

While ordinary production capacity still remains, each participant must be able
to see whether protected finishing is preauthorized and whether it has a current
accepted responsibility. Membership, a written plan and reserved capacity are
not acceptance. Make the existing offer and acceptance mechanisms usable before
exhaustion; do not silently assign ownership or preserve consent across changed
terms. The diagnostic is neither a reservation nor a promise of admission.

Each protected decision still passes current authority and full exposure checks.
Temporary concurrency, unavailable providers and unresolved effects do not trigger
a funding-pool switch. Paused and cancelled work stays stopped. Eligible runnable
participants receive a fair opportunity before another consumes a second finishing
turn; this promises neither a fixed number of funded turns nor successful review.
Optional exploration remains excluded. The interface distinguishes protected
capacity from current permission and feasibility to use it.

A completed local inference can retain unknown billed usage without leaving an
unresolved execution. Its exact call and accounting bindings must retain the full
conservative token, cost, call and remote exposure bounds. That accounting
uncertainty alone does not veto preauthorized finishing; every new quote still
counts the retained exposure against the same ceilings. A failed or interrupted
primary, response-only decision has the same treatment only when durable local
failure evidence proves its provider attempt ended without a saved action plan
or attempted actions, and both accounting ledgers retain their exact bindings
and complete conservative exposure. A terminal status alone is not evidence.
For a cancelled decision, the local transport receipt must establish closure,
the original decision epoch must be superseded, and no pending plan or attempted
action may remain. This exception does not apply to an unfenced cancellation.
Crash-only interruption, incomplete bindings, auxiliary or native operations
without equivalent closure evidence, and unresolved outside effects remain
blockers. Local closure does not prove remote cancellation: uncertain remote
capacity remains occupied and may independently prevent another admission.
This distinction neither reconciles unknown usage nor refunds resources, retries
an old call, resumes stopped work or creates an accepted responsibility.

## Pause, cancellation, and revocation

A relevant pause, cancellation, expiry, or revocation stops new affected admissions and initiates the applicable stop procedure for running effects. The system records the difference between stop requested, stop acknowledged, effect already occurred, and effect still unknown.

A task-level pause stops new persona decisions for that task and requests stopping
of its in-flight inference. Already dispatched tool jobs may finish; their
receipts and spending remain available. This pause survives restart, new input,
recovery timers and added participants. It does not pause other tasks that share
a persona or funding allowance. Stopping an existing tool job is a separate
choice, and neither choice rolls back an effect that already occurred.

An explicit task resume reactivates all eligible paused or waiting participation,
including individually paused participants. It does not renew cancelled or
removed participation, revive retired or quarantined personas, reopen sealed
history, or replace missing funding and authority. The interface distinguishes
participation queued for a fresh decision from participation that remains
blocked; a resume request is not proof that inference began.

Saving an operator task amendment also requests this resumption. The new mandate
and eligible participation transitions are adopted together, preserving the
original request and earlier versions. Decisions made against superseded scope
cannot supply new effects after the amendment, including after a rapid pause and
resume. A valid amendment can be saved while funding prevents execution; the
saved scope and the blocked resumption must both be visible. Adopting a mandate
without the task-amendment control does not independently override a pause.

An amendment invalidates the old decision's action authority immediately, but is
not itself a request to cancel an already admitted bounded inference transport.
Let that attempt finish its bounded wait so late metering can settle honestly;
only a fresh decision may act on the amended mandate. Explicit pause,
cancellation and revocation retain their stop semantics. Draining an old
response must not dispatch its action plan, restore its obsolete scope, or
resume otherwise stopped work.

See [recovery and delivery refinements](RECOVERY-AND-DELIVERY.md) for the related
consent, reader-identity, artifact-delivery and acceptance boundaries.

Late receipts remain available for accounting and recovery. They cannot authorize new adoption or publication after the grant ends. A compensating action, such as withdrawing a submission, needs its own permission and evidence; stopping does not automatically undo an external effect.

Mandatory current authority and cancellation information must survive context selection and reach affected decisions. A stale worker cannot act merely because its older context contained permission.

## Bounded activity and fairness

An active persona need not consume inference while idle. An authorized event, explicit schedule, bounded self-wake, or exploration allowance may activate it. Waiting identifies a meaningful condition or a clear dormant state.

Repeated reminders, status updates, retries, and persona creation remain inside finite ceilings. Narrative changes cannot reset those ceilings. Mechanical fairness can prevent one participant from monopolizing resources, but it does not decide the human value of competing projects. That tradeoff belongs to the adopted allocation authority.

When available capacity cannot meet accepted obligations, expose the conflict. Do not conceal abandonment of one commitment inside a busy history for another.

### Optional exploration is bounded across the whole episode

The [personal-development rules](PERSONA-DEVELOPMENT.md) permit a persona to choose a question, methods and collaborators within an explicitly funded episode. The episode allowance belongs to its work, not separately to each participation. Later invitations, reviews, initialization and nested inference consume the same episode allowance and retain its original expiry. Starting another run, changing participants or removing a copied status field must not create fresh capacity or turn optional exploration into foreground user work. Root accounting and protected finishing capacity remain independent additional limits.

An episode does not authorize creation or resumption of a different work item outside its limits. Separate self-directed work needs a separately permitted exploration opportunity, or a new explicit operator authorization. This restriction does not assign professions, choose tools, prevent collaboration within the episode or restrict ordinary authorized user work.

At execution time, a scheduled question and its supporting sources must still be readable under current authority. Imported or withdrawn history is not a live trigger. The permitted environment must remain available and the funding must not have expired. Work instructions, invitations and other previews derived from the question retain its exact provenance and current access restrictions; executing an authorized schedule on behalf of the user is not permission to drop those restrictions.

A bounded scheduler must eventually consider later eligible opportunities despite an unchanged prefix of future, paused or otherwise ineligible entries, including across restart. This is mechanical queue fairness, not a domain priority score, a new inference trigger or permission to spend while idle. A failed start must leave no partially created work, invitation, participation or consumed episode and must not prevent unrelated opportunities from being considered. Its honest blocked disposition remains visible; repeated polling must not fabricate novelty or repeatedly attempt the same failed start.

Concluding an episode must not abandon a collaborator's accepted responsibility or obscure pending or uncertain actions. Its owner must first obtain the applicable dispositions and preserve unresolved effects honestly. A concluded episode cannot remain executable through a later participant's run. Cancellation, a useful negative finding, partial delivery and successful completion remain distinct; closing participation does not undo effects or establish that the original need was met.

## Deployment decisions and assurance

An implementation must declare its grant model, enforcement boundary, resource measurements, unknown-usage policy, closeout policy, revocation behavior, and recovery procedure before autonomous effects are enabled. A diagram or a permission label does not establish that these mechanisms work.

See GOV-01–GOV-04 and UX-02 in the [requirements](../implementation/REQUIREMENTS.md), the [deployment decisions](../implementation/DEPLOYMENT-DECISIONS.md), and M05–M07, M11–M13, M23, and M25 in the [acceptance catalogue](../evaluation/ACCEPTANCE.md).
