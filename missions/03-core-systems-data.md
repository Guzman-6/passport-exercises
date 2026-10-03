# Mission: Map Systems And Research Data

## Outcome

Learn what GitHub, the NAS, Blade, Euler, and temporary storage are, then choose the correct place for code, durable data, graphical Windows work, and scheduled computation.

## Concept

A lab project normally uses several systems, each for a different purpose:

- GitHub stores reviewed source code and small text files.
- The IDEAL Lab NAS is durable shared storage for approved project data.
- Blade is a shared remote Windows computer for licensed graphical software.
- Euler is an ETH Zurich service made of many managed computers for research calculations. A CPU is the general-purpose processor used by most programs; a GPU is an accelerator used only by compatible programs. Both kinds of work are submitted through Slurm, the software that queues programs and assigns them to available compute nodes.
- Scratch and temporary folders hold replaceable working files, not the only copy of a result.

Durable storage is intended to keep required files under an approved ownership and recovery plan. Temporary storage may be purged. A GUI is a graphical user interface controlled with windows, menus, and buttons. A scheduled computation is a program submitted with its CPU, memory, and time needs so Slurm can place it on a suitable Euler compute node.

Choose a location from its purpose, owner, and retention rules, not from free disk space.

## Worked Example

The map separates code history, durable storage, temporary storage, graphical access, and scheduled computation.

Check these points:

- **Where does maintained source code belong?** In an approved GitHub repository.
- **Where should a heavy batch computation run?** In a Slurm allocation with explicit CPU, memory, and time limits on Euler or another approved compute system.
- **Where should the main durable copy of an approved collaborative dataset live?** In the supervisor-approved durable project location on NAS or another named project store.
- **What may be placed in scratch storage?** Temporary high-throughput files that can be recreated from recorded inputs.
- **Where should you use an approved Windows-only engineering GUI?** On Blade for interactive GUI work, while heavy batch computation uses an approved compute system.
- **What project context may you send to an AI service during onboarding?** Only the fictional practice files provided by the mission, unless the real data owner approved the exact service and content.

## Common Trap

Choosing a location without checking ownership, backup, lifetime, and where the
data will be processed.

## Your Action

Map code, durable data, temporary files, graphical Windows work, and scheduled computation to the correct lab systems.

**Follow these steps in order.** A CPU is the general-purpose processor used by most programs. A GPU is an accelerator used by compatible programs. Durable storage is intended to keep required files under an approved recovery plan; temporary storage may be purged. A GUI is an application controlled with windows, menus, and buttons. For each item, decide who owns it, how long it must survive, and where the work actually runs.

### 1. Read the system map before placing files

**Where:** This web page in your browser

Identify the role of each location: GitHub for reviewed source code, NAS for durable shared project data, Blade for licensed graphical Windows work, Euler for scheduled computation, and scratch or temporary folders for replaceable working files. Scheduled computation means submitting a program with requested CPU, memory, and time so a scheduler can choose where and when it runs.

- [Open the complete system decision table](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/environments-overview.md)

**Expected:** Each system has one clear purpose and temporary storage is not treated as durable.

**Continue when:** Place source code first.

**If not:** Do not answer from familiarity or free disk space; reread the decision table.

### 2. Place source code

**Where:** This web page in your browser

Keep source code and reviewable text in GitHub. Each contributor uses a separate clone, meaning their own working copy of the project. A branch keeps one line of work separate, and a pull request asks for that branch to be reviewed before it is combined with shared work.

**Expected:** Code has version history and no shared writable working tree.

**Continue when:** Continue to durable project data.

**If not:** Move code collaboration out of a shared NAS checkout before continuing.

### 3. Place durable project data

**Where:** This web page in your browser

Use the supervisor-approved NAS project folder or another explicitly approved durable project store. A dataset is a collection of research data; a checkpoint is a saved state from a computation or model; a deliverable is an output the project must keep.

**Expected:** The durable copy has a named owner and approved access.

**Continue when:** Continue to temporary data.

**If not:** Ask the supervisor which project location holds the main durable copy; do not invent one.

### 4. Identify temporary storage

**Where:** This web page in your browser

Scratch means temporary working storage intended for replaceable files. Use scratch, Blade D:, or another named temporary area only for working copies you can recreate. Record how needed results return to durable storage.

**Expected:** No irreplaceable file exists only in temporary storage.

**Continue when:** Continue to interactive GUI work.

**If not:** Copy and verify the required data in durable storage before proceeding.

### 5. Place Windows GUI work

**Where:** This web page in your browser

Use Blade for approved interactive Windows software such as computer-aided design (CAD) or simulation pre-processing and post-processing. Inside Blade, P: is a Windows drive letter for the connected durable project storage. Keep durable files there and move heavy computation elsewhere.

**Expected:** Blade is used interactively and does not hold the only durable copy.

**Continue when:** Continue to scheduled computation.

**If not:** Stop an unattended heavy workload and choose an approved compute system.

### 6. Place scheduled computation

**Where:** This web page in your browser

Euler login nodes are the computers reached first for access, file management, editing, and job control. Slurm is the scheduler that assigns submitted work to compute nodes. Run CPU or GPU computation on those compute nodes, not on a login node.

**Expected:** The Slurm job requests explicit CPU, memory, and time limits.

**Continue when:** Continue to the classification questions.

**If not:** Do not run the workload directly on an Euler login node.

### 7. Complete the placement map

**Where:** This web page in your browser

Classify every fictional item below. Use the named systems and durability rules, not the amount of free disk space.

**Expected:** Every item has one justified location.

**Continue when:** Run Check my work.

**If not:** Return to the relevant system rule and correct the placement.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 80% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

Do not guess a storage path or AI approval. Record the unresolved decision and
ask the project information owner or supervisor. The
[data and AI policy](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/policy/data-and-ai.md) defines the escalation
boundary.

Useful references:

- [Environments Overview](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/environments-overview.md)
- [Data And Ai Safety](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/data-and-ai-safety.md)
- [Data and AI policy](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/policy/data-and-ai.md)

## Understand Before Accepting AI Output

Zero-data-retention marketing does not decide whether project material may be
uploaded. The information owner, ETH policy, lab policy, account terms, and
data classification all still apply.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
