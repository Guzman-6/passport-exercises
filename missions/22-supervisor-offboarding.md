# Mission: Plan Handover And Offboarding

## Outcome

Transfer project ownership and records before removing a departing person's
access.

## Concept

Offboarding is the planned transfer of work and removal of access when someone
leaves a project or the lab. Starting only after accounts expire can lose data
and leave old access active. Transfer and verify required project records first;
remove access only after an authorized successor can use them.

## Worked Example

Operational actions have named owners and dates, and no project asset depends on the departing person's private account or storage.

Check these points:

- **Choose the safe high-level offboarding order.** Inventory and transfer ownership. -> Verify durable data, code, and documentation. -> Rotate shared credentials and remove access. -> Record completion and remaining retention decisions.
- **What must be removed from the project?** Dependencies on the departing person's private accounts, laptop, and undocumented knowledge.

## Common Trap

Removing accounts before transferring ownership, or assuming that access revocation also archives project knowledge.

## Your Action

Apply the safe order to a fictional departure: inventory, transfer, verify, clean temporary work, rotate credentials, revoke, and record.

**Follow these steps in order.** Offboarding is the planned transfer of work and removal of access when someone leaves. Preserve required project records and evidence. Do not delete broadly while ownership or retention is unresolved.

### 1. Inventory project dependencies

**Where:** This web page in your browser

List repositories, durable and temporary data, environments, services, shared credentials, devices, scheduled jobs, documentation, and undocumented knowledge.

**Expected:** The inventory covers every project dependency tied to the departing person.

**Continue when:** Assign an authorized successor.

**If not:** Keep access unchanged until the inventory is complete.

### 2. Transfer ownership

**Where:** This web page in your browser

Move repositories, service ownership, durable data responsibility, and operational knowledge to named authorized people or project-owned accounts.

**Expected:** No required asset depends on the departing person's private account or laptop.

**Continue when:** Verify code, data, and documentation.

**If not:** Do not remove the departing owner's access yet.

### 3. Verify the handover

**Where:** This web page in your browser

Have the successor locate the code revision, environment definition, main approved data copy, verification command, expected result, and known limitations.

**Expected:** The successor can reproduce the agreed verification command and result.

**Continue when:** Handle credentials and active work.

**If not:** Complete the handover before revocation.

### 4. Close active compute and temporary storage

**Where:** This web page in your browser

Record or stop active jobs, copy required results to durable storage, and assign deletion dates to scratch and Blade D: copies.

**Expected:** No required output remains only in temporary storage.

**Continue when:** Rotate shared credentials.

**If not:** Preserve state and ask the relevant system owner before deletion.

### 5. Rotate shared credentials

**Where:** This web page in your browser

Rotate project-owned shared secrets where permitted and remove personal tokens or keys from services. Never ask the departing person to publish a secret.

**Expected:** Remaining users have valid individually accountable access.

**Continue when:** Remove unnecessary access.

**If not:** Escalate privately to the service owner.

### 6. Remove access after verification

**Where:** This web page in your browser

Revoke repository, storage, compute, machine, AI-service, and group access according to each system owner's process.

**Expected:** Unneeded access is removed without deleting retained project records.

**Continue when:** Record completion and retention decisions.

**If not:** Do not improvise destructive cleanup.

### 7. Record completion

**Where:** This web page in your browser

For the fictional case, choose the correct sequence and decide how each unfinished or retained item is owned and dated.

**Expected:** Every completed and unfinished action has an accountable owner and date.

**Continue when:** Complete the scenarios and run Check my work.

**If not:** Keep the case open with a named owner for every unfinished action.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 100% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

Preserve data and access state while ownership or retention is unclear. Do not
perform broad deletion to “clean up.” Use the
[project handover lab](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/project-handover.md) and escalate to
the relevant owner.

Useful references:

- [Project Handover](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/project-handover.md)
- [Supervisor and staff track](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/tracks/supervisor-staff.md)
- [Completion record](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/assessment/completion-record.md)

## Understand Before Accepting AI Output

An agent cannot approve deletion, retention, ownership transfer, or access
revocation. The named owner of each system must confirm its own action.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
