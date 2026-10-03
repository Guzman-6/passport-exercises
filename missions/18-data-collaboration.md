# Mission: Design Safe Shared Data Collaboration

## Outcome

Plan how team members share code and data without editing one common project
folder or granting unnecessarily broad file access.

## Concept

Code and data are shared differently. Each developer uses a separate Git clone for code and exchanges reviewed changes through GitHub. A Git working tree is the checked-out project folder, including its current branch, staged changes, and uncommitted edits; sharing one writable tree mixes those states and file ownership between people.

Datasets, checkpoints, logs, and results instead use an approved shared data location with a named owner. Permissions state who may read or change files. A detailed access-control list (ACL) can grant extra permissions to named people or groups. Write boundaries name the folders each person or program may change. Version and cleanup rules identify the main approved copy and when temporary copies are removed.

## Worked Example

Collaborators have the minimum required access, shared data has an owner, and each developer keeps a separate Git clone.

Check these points:

- **How should several students collaborate on code?** Each uses a separate clone and collaborates through branches and PRs.
- **What is the safe response to a shared-folder permission problem?** Inspect the owner, group, detailed access-control list (ACL), and intended folder boundary before making a narrow change.

## Common Trap

Using one shared Git working tree or broad recursive permission changes such as `chmod 777` to solve collaboration problems.

## Your Action

Apply the collaboration rules to a fictional team sharing source data, derived results, code, and credentials.

**Follow these steps in order.** A dataset is a collection of research data. A checkpoint is a saved program or model state. Permissions state who may read or change files. A detailed access-control list (ACL) can grant extra permissions to named people or groups. Use only the fictional scenario below; do not apply permissions to a real shared folder in this mission.

### 1. Name the dataset owner

**Where:** This web page in your browser

Identify the person responsible for classification, access approval, retention, and final deletion.

**Expected:** One accountable information owner is named.

**Continue when:** List the collaborators' actual tasks.

**If not:** Do not grant access until ownership is clear.

### 2. Grant only needed access

**Where:** This web page in your browser

Give each role read or write access according to its task. Avoid world-writable permissions and shared credentials.

**Expected:** No collaborator receives broader access than needed.

**Continue when:** Define the write boundary.

**If not:** Reduce the proposed permission or obtain owner approval.

### 3. Define where writes occur

**Where:** This web page in your browser

Keep source data that must not change separate from derived data, checkpoints, and logs. Name which folders each program may modify.

**Expected:** Concurrent work cannot silently overwrite the main approved inputs.

**Continue when:** Separate code collaboration from data sharing.

**If not:** Make source files read-only or use clearly versioned copies before collaboration starts.

### 4. Use separate Git clones

**Where:** This web page in your browser

Each developer keeps a separate clone and shares code through GitHub. The shared data folder is not a shared Git working tree.

**Expected:** Git ownership and file permissions cannot collide inside one shared checkout.

**Continue when:** Define names and record where generated data came from and how it was produced.

**If not:** Move the repository out of the shared writable data directory.

### 5. Define conflict and recovery rules

**Where:** This web page in your browser

Record who resolves duplicate outputs, how versions are identified, where the durable copy lives, and how temporary work is cleaned.

**Expected:** A collaborator can recover without guessing which copy is the main approved one.

**Continue when:** Complete the structured questions.

**If not:** Do not start shared writes until the main approved copy is named.

### 6. Complete the collaboration plan

**Where:** This web page in your browser

Choose permissions, ownership, write boundaries, and recovery actions for the fictional scenario.

**Expected:** The plan uses minimum access and separate code clones.

**Continue when:** Run Check my work.

**If not:** Use the feedback to correct the unsafe decision.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 80% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

Do not guess numeric group IDs or apply broad recursive commands. Ask the
storage owner to inspect the smallest affected directory. Use
[Euler storage](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/storage.md) for the maintained
setgid/default ACL procedure when Euler is the approved system.

Useful references:

- [Data Placement](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/data-placement.md)
- [Euler storage](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/storage.md)
- [NAS guide](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/nas_ideal.md)

## Understand Before Accepting AI Output

An agent must not apply recursive permission changes based only on a pasted
path. Verify system, owner, group, inheritance, existing contents, and rollback
before any real change.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
