# Mission: Place Research Data Intentionally

## Outcome

Choose a safe location for each research file by asking who owns it, who may
see it, how long it must remain available, and where it will be used.

## Concept

Research data includes source measurements, derived datasets, checkpoints,
logs, results, and records needed to understand the work. The main approved
copy is the named version the project treats as correct; other copies are for
work, transfer, faster access, or backup. Sensitivity describes the harm or
access restriction associated with disclosure. Durability describes whether
the file is intended to survive failure or cleanup. Retention states how long
it must be kept.

A checksum is a calculated fingerprint used to check whether two file copies
contain the same data. It helps verify a copy; it does not decide whether the
storage location is durable or approved.

A file can be accessible without being durable, approved, backed up, or safe to share. Choose its location from sensitivity, owner, collaborators, compute needs, retention, and deletion rules.

## Worked Example

Every placement has a reason and no sensitive or durable data is assigned to an unapproved temporary location.

Check these points:

- **Should a research dataset be committed to the exercise or code repository?** No; use the supervisor-approved data location and version metadata instead.
- **What must happen to required output created on temporary storage?** Copy it to the approved durable project location and remove the temporary copy when appropriate.

## Common Trap

Using Git for datasets or checkpoints, or assuming a synced personal folder is approved project storage.

## Your Action

Apply the storage decision sequence to six fictional research files or results, then answer the placement scenarios.

**Follow these steps in order.** Sensitivity describes the harm or access restriction associated with disclosure. Durability describes whether a file must survive failure or cleanup. Retention states how long it must be kept. High input/output (high-I/O) work repeatedly reads or writes a large amount of data. Decide these points, ownership, collaboration, and where computation runs before choosing storage; free space alone is not a reason.

### 1. Classify sensitivity

**Where:** This web page in your browser

For each file or result produced or used by the project, decide whether it is public, internal, confidential, personal, or otherwise restricted under the project's approved classification.

**Expected:** The classification is explicit and justified.

**Continue when:** Name an information owner.

**If not:** Stop placement until the project owner resolves the classification.

### 2. Name the owner

**Where:** This web page in your browser

Identify who decides access, retention, and deletion for the file or result. A person who happens to have a copy is not automatically the owner.

**Expected:** One accountable owner is named.

**Continue when:** Decide durability and collaboration needs.

**If not:** Ask the supervisor; do not self-authorize access.

### 3. Decide how long it must survive

**Where:** This web page in your browser

Mark the file or result as durable, reproducible temporary work, a temporary copy kept for faster access, or disposable output. Record backup and recovery expectations.

**Expected:** Irreplaceable material is assigned to approved durable storage.

**Continue when:** Decide where collaborators and compute need it.

**If not:** Do not leave the only copy in scratch, Blade D:, or a laptop.

### 4. Match collaboration and compute locality

**Where:** This web page in your browser

Use GitHub for code, NAS or another approved project store for durable shared data, and approved Euler storage for active cluster I/O.

**Expected:** The location supports the actual collaborators and workload.

**Continue when:** Define retention and cleanup.

**If not:** Do not run high-I/O Euler work directly against external NAS.

### 5. Record retention and cleanup

**Where:** This web page in your browser

Name when temporary copies are removed and who confirms durable transfer or deletion.

**Expected:** Every temporary copy has an end condition.

**Continue when:** Complete the fictional placements.

**If not:** Keep the file or result unchanged until the person responsible for retention has decided what must happen.

### 6. Complete each placement

**Where:** This web page in your browser

Choose a location for every fictional file and check it against all five decisions above.

**Expected:** No sensitive or durable file or result is assigned to unapproved temporary storage.

**Continue when:** Run Check my work.

**If not:** Correct the first placement with an unresolved owner or durability rule.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 100% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

Do not create another ad hoc copy. Record the unresolved owner, classification,
or storage decision and ask the supervisor. Use the
[NAS guide](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/nas_ideal.md) only after the assigned
supervisor folder is known.

Useful references:

- [Data Placement](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/data-placement.md)
- [Data Steward](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/tracks/data-steward.md)
- [NAS guide](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/nas_ideal.md)
- [Data and AI policy](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/policy/data-and-ai.md)

## Understand Before Accepting AI Output

An agent cannot decide ownership, classification, retention, or approved
services. It must not scan or reorganize real project data to complete this
exercise.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
