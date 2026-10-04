# Mission: Map Systems And Research Data

## Outcome

Decide where one fictional project's files belong and explain which copy must survive.

## Concept

### One project, several places

Two students are studying how a beam bends. Their program and measurements are
not the same kind of file, and the computer that runs a calculation need not be
the place that keeps its result.

| Fictional item | Why the project needs it |
| --- | --- |
| `analyse.py` | Program both students will edit |
| `measurements.csv` | Approved input that must remain available |
| Working mesh | Replaceable file built for the calculation |
| `report.pdf` | Result the thesis must retain |

## Learning Challenge

Before reading the steps, choose one item that could safely be recreated after
its working copy disappears. What would you need to record to rebuild it?
There is no file to upload for this question. The steps help you check your reasoning.

## Worked Example

<details>
<summary>See a possible route through the project</summary>

Code is reviewed on GitHub from each student's separate clone. The approved
input stays in its owner-approved durable store. A working copy can travel to
an approved compute location; a scheduled job produces the result. The result
returns to approved durable storage and is verified before working copies are
cleaned. Blade supplies the approved Windows interface when needed; it is not
a replacement for scheduled heavy compute or durable storage.

</details>

## Common Trap

A folder called `archive` is still temporary if the service's lifetime rules say
so. Decide from ownership and retention, rather than a folder name or free space.

## Your Action

Use the fictional beam-test project to decide where its code, input data, temporary files and retained result belong. No files or permissions are changed.

**Follow these steps in order.** Stay on this page. For each part of the fictional project, make your choice before opening Explanation and help. Do not move real files, connect to a service or change permissions.

### 1. Follow one project

**Where:** This web page in your browser

Two students study a beam. They have analyse.py (their program), measurements.csv (approved input data), a replaceable mesh for calculations, and report.pdf (the result to keep). Which of these must remain available after a temporary folder is cleaned?

**Expected:** Separate the files that must survive from working copies that can be rebuilt.

**Continue when:** Durable means intended to retain required files under an approved ownership and recovery plan. Temporary files may be purged. A file extension does not tell you its approval or lifetime.

**If not:** If the only copy cannot be recreated, treat that as an unresolved preservation decision; do not call it temporary.

### 2. Share changes to analyse.py

**Where:** This web page in your browser

Both students want to edit the program. Choose how they can propose changes without overwriting one shared working copy.

**Expected:** Each person has their own working copy; reviewed code has a shared history.

**Continue when:** GitHub stores reviewed source code and small text files. Each student uses a separate clone, their own copy for editing. A shared writable NAS checkout is not the collaboration route.

**If not:** Do not invent a shared checkout for this plan. The later Git lesson teaches how to propose a reviewed change.

### 3. Keep the approved input

**Where:** This web page in your browser

The supervisor has named an approved NAS project folder for measurements.csv. Who decides whether a second service is allowed to hold that dataset?

**Expected:** The main input has a named information owner and an approved durable location.

**Continue when:** The NAS is durable shared storage for approved project data. Its owner approves access and other destinations. Having a login or free space does not grant permission.

**If not:** For a real project, ask the information owner about an unnamed location. No approval or transfer is performed here.

### 4. Separate a working copy from the result

**Where:** This web page in your browser

The mesh can be rebuilt from recorded inputs. report.pdf is needed for the thesis. Decide which may have its only copy in temporary storage and how the report returns to the approved project store.

**Expected:** A replaceable working file can be rebuilt; the retained result has a verified durable copy.

**Continue when:** Scratch and temporary folders hold replaceable working files. Copy a required result to the approved durable location and verify the copy before planned cleanup. A matching checksum proves equal content, not durability or permission.

**If not:** Revise the fictional plan if a required result exists only in temporary storage. Do not delete or move any actual file.

### 5. Choose where to use the graphical tool

**Where:** This web page in your browser

The project uses approved Windows-only engineering software to inspect the mesh with menus and buttons. Choose the computer for that interactive work and the destination of the saved result.

**Expected:** Interactive work and durable storage have separate roles.

**Continue when:** Blade is a shared remote Windows computer for licensed graphical software. A GUI is its windows-and-buttons interface. P: connects approved durable project storage; C: and D: must not hold the only retained copy.

**If not:** Do not start a long unattended calculation on Blade. This exercise grants no access and requires no connection.

### 6. Choose where the long calculation runs

**Where:** This web page in your browser

The beam calculation will run unattended for hours. Plan where it runs, rather than starting it in the shell used to log in.

**Expected:** The plan uses an approved scheduled job with explicit CPU, memory and time limits.

**Continue when:** Euler login nodes are for access, editing, files and job control. Slurm assigns jobs to compute nodes. A CPU is a general-purpose processor; a GPU helps only compatible programs. Heavy work belongs in an allocation on Euler or approved compute.

**If not:** Do not run heavy work on a login node. No job is submitted in this lesson.

### 7. Check your decisions

**Where:** This web page in your browser

Trace the code, input, working copy and retained report through your plan. Then try the questions below. Only fictional practice content may go to an AI service unless its owner approved the exact service and content.

**Expected:** You can explain ownership, lifetime and processing location without guessing a real path.

**Continue when:** The six questions check these decisions. They do not verify a real folder, backup, permission setting or Euler job.

**If not:** Open the explanation for the decision you cannot yet justify. Ask privately about real data approval rather than putting project details into the exercise.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

The six questions assess your placement decisions. They do not inspect real
storage, backups, permissions or an Euler job. Use **Check my work**, then
**Submit lesson** when the local check passes. Completion follows the trusted
GitHub check. A score of 80% and every safety-critical answer are required.

## Learning Check

### Practise

Try an answer before opening the explanation. These questions are for
practice; they do not affect your progress.

1. A result in scratch matches the original checksum. It cannot be regenerated. Is it ready for the project to keep?

   - Yes; the checksum makes scratch durable.
   - No; verify a copy in the owner-approved durable location before cleanup.
   - Yes; rename its folder to archive.

<details class="learning-explanation">
<summary>See an explanation</summary>

A checksum confirms the content of a copy. It does not change storage lifetime or authorize a destination. An irreplaceable result needs a verified approved durable copy.

</details>

2. Two students need to change analyse.py. The dataset already has an approved shared NAS folder. How should they edit the code?

   - Edit one shared writable Git checkout next to the data.
   - Use separate clones and propose reviewed changes through GitHub.
   - Email two complete folders named final and final2.

<details class="learning-explanation">
<summary>See an explanation</summary>

Sharing approved data does not mean sharing one writable Git working tree. Separate clones let each student make and review their own change before proposing it to the shared repository.

</details>

## If Blocked

For a real project, ask its information owner or supervisor about an unresolved
location or AI approval. Keep real names, paths and data out of the public
exercise. Use the Passport's non-secret help form for a lesson problem.

- [System decision table](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/environments-overview.md#decision-table): optional lookup for one location, then return here.
- [Data and AI policy](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/policy/data-and-ai.md): the approval boundary for real work.

## Understand Before Accepting AI Output

An agent's suggested destination does not create permission, a backup or a
retention plan. Check those facts with the owner before accepting a real plan.

## Finish And Continue

Submit once after the local check passes. Continue when your progress shows
the automatic GitHub result as passed; reading a page is not completion.
