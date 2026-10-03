# Mission: Place Euler Data And Freeze Run Inputs

## Outcome

Choose where Euler code, inputs, temporary work, results, and logs belong.
Record enough information for another person to repeat the run.

## Concept

Euler provides several storage areas. Names beginning with `$` below are shell variables: short names that resolve to paths. `$HOME` is small private storage for code and configuration. `/cluster/work/fuge` is shared working storage for approved lab projects. `$SCRATCH` is temporary high-throughput storage, and `$TMPDIR` exists only on the compute node during one job.

A reproducible run records the code revision, environment, inputs, configuration, command, logs, and durable output location. Neither scratch storage nor the submitted Slurm script alone preserves all of that information.

## Worked Example

The plan separates Git, approved Euler storage, scratch, and durable results and records enough inputs to rerun the job.

Check these points:

- **What is Euler scratch for?** Temporary high-throughput files that can be recreated.
- **What must a reproducible run identify?** Code revision, environment, exact unchanged inputs, parameters, resources, and outputs.

## Common Trap

Keeping the only copy in scratch, processing high-I/O workloads directly on an external NAS mount, or changing inputs in place.

## Your Action

Apply the reproducible-run sequence to a fictional Euler job before deciding where each file or result belongs.

**Follow these steps in order.** Names such as $HOME and $SCRATCH are shell variables: short names that resolve to paths on Euler. High input/output (high-I/O) work repeatedly reads or writes a large amount of data. Use the fictional scenario. Choose locations by ownership and durability, not convenience.

### 1. Know the Euler storage areas

**Where:** This web page in your browser

Use $HOME for small private code and configuration, /cluster/work/fuge for approved shared working data, $SCRATCH for replaceable high-throughput files, and $TMPDIR for temporary files inside one running job. Name the durable location that will hold the main copy after the run.

- [Open the Euler storage reference](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/storage.md)

**Expected:** You can identify which locations survive, which are shared, and which are temporary.

**Continue when:** Record the code revision for the fictional run.

**If not:** Do not place the only copy of a result in scratch or TMPDIR.

### 2. Record the code revision

**Where:** This web page in your browser

Use a reviewed Git commit as the code identifier. The commit's identifier records exactly which code version was used, but it does not stop someone from editing other uncommitted files in the active project folder.

**Expected:** The run plan names one exact commit and a clean or explicitly described source state.

**Continue when:** Choose the exact input location for this run.

**If not:** Do not call an uncommitted changing checkout reproducible.

### 3. Freeze input identity

**Where:** This web page in your browser

Place approved durable inputs in project storage and record a version or checksum. A checksum is a short calculated fingerprint used to detect whether a file changed. Copy the exact run inputs to a run-specific location when required.

**Expected:** The inputs used by the job can be identified later.

**Continue when:** Choose temporary working storage.

**If not:** Stop if a pending job points to files that collaborators may overwrite.

### 4. Use scratch only for replaceable work

**Where:** This web page in your browser

Use Euler scratch for high-throughput temporary files that can be rebuilt. Do not leave the only checkpoint or result there.

**Expected:** Every scratch item has a rebuild or copy-back rule.

**Continue when:** Choose the durable output destination.

**If not:** Copy and verify irreplaceable output in approved durable storage.

### 5. Name durable outputs and ownership

**Where:** This web page in your browser

Assign durable results to an approved Euler project/work location or NAS project location with a named owner and retention decision.

**Expected:** The main durable result location and its owner are stated explicitly.

**Continue when:** Record the software environment.

**If not:** Ask the project owner before inventing a durable location.

### 6. Record the environment

**Where:** This web page in your browser

Record modules, environment definition, application version, configuration, and the exact command or script used.

**Expected:** Another authorized user can reconstruct the software context.

**Continue when:** Keep run-specific logs with the run record.

**If not:** Do not rely on an undocumented interactive shell history.

### 7. Keep identifiable logs

**Where:** This web page in your browser

Use run-specific log names containing the job ID and retain the useful logs with the run metadata.

**Expected:** Each log maps to one submitted job and configuration.

**Continue when:** Complete the placement questions.

**If not:** Correct colliding or ambiguous log paths first.

### 8. Complete the run plan

**Where:** This web page in your browser

Place every fictional file or result and explain how the plan survives reruns, collaboration, and scratch cleanup.

**Expected:** Git, durable storage, scratch, environment metadata, and logs have distinct roles.

**Continue when:** Run Check my work.

**If not:** Return to the first file or result whose owner or durability is unclear.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 80% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

Do not invent permissions or recursively change a shared folder. Ask the data
owner which approved location holds the main durable copy, and use
[Euler storage](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/storage.md) for lifecycle and
collaboration recovery.

Useful references:

- [Euler storage](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/storage.md)
- [Slurm reference](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/slurm.md)
- [Data Placement](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/data-placement.md)

## Understand Before Accepting AI Output

Inspect every source and destination before copying or deleting. An agent must
not assume a temporary path is backed up or that a successful transfer is a
backup.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
