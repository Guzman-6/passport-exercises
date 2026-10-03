# Mission: Cap And Calculate Euler Job Arrays

## Outcome

Correct a practice script that starts many similar Euler tasks. Limit how many
can run at once and give every task its own log file.

## Concept

A Slurm job array submits many similar tasks from one script. The array range sets the total number of tasks; the value after `%` limits how many may run at the same time. This concurrency cap controls simultaneous demand, not total work.

Every task also needs a distinct log name, and the combined CPU, memory, and GPU request must be calculated before submission.

## Worked Example

The checker accepts exactly ten tasks with at most one running at a time and
distinct logs for every task. No command submits the practice file to Euler.

Check these points:

- **What does %4 mean in --array=0-31%4?** At most four array tasks may run concurrently.
- **Which placeholders show the parent array and task index in log filenames?** %A for the parent job and %a for the task index.

## Common Trap

Submitting a large array without a concurrency cap, or giving every task the
same fixed log filename. `%j` is a distinct job ID for each array task; it does
not inherently cause collisions. This exercise requires `%A_%a` so filenames
also show which array and task index produced the log.

## Your Action

Correct the fictional Slurm array practice file, add a concurrency cap, and make every task log name unique.

**Follow these steps in order.** The supplied file is deliberately unsafe. Edit it locally and never submit it to Euler.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Understand an array and its concurrency cap

**Where:** This web page in your browser

A job array creates many similar Slurm tasks from one script. The range sets the total number of tasks. The value after %, called the concurrency cap, limits how many tasks may run at the same time. Each task still reserves its own CPU, memory, GPU, and time and needs a distinct log name.

- [Open the job-array lab](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/euler-job-arrays.md)

**Expected:** You can distinguish total task count from the maximum running at once.

**Continue when:** Open the deliberately unsafe local practice file.

**If not:** Do not submit a real array until you can calculate its simultaneous resource total.

### 2. Prepare the array practice file

**Where:** The laptop or desktop in front of you

Press Prepare practice folder, enter it, and open workspace/slurm/array_job.slurm.txt.

**Expected:** The unsafe practice file is open in the separate practice repository.

**Continue when:** Inspect it without submitting.

**If not:** Do not create your own replacement script or use Euler for this exercise.

### 3. Inspect the cap and log names

**Where:** The laptop or desktop in front of you

Read the array and log settings. The practice file allows 100 tasks without a concurrency cap. Its %j log names use each task's distinct job ID, but do not directly show the parent array and task index. This exercise uses %A_%a to make that relationship visible.

**Expected:** You can explain the missing concurrency cap and why parent/index labels make array logs easier to trace.

**Continue when:** Edit only the required directives.

**If not:** Review the array and log-name explanation before editing.

### 4. Add a small concurrency cap

**Where:** The laptop or desktop in front of you

Replace the unsafe array directive with the exact line below. It creates ten tasks, numbered 0 through 9, and allows at most one to run at a time.

**Put this in the named Bash file:**

```bash
#SBATCH --array=0-9%1
```

**Expected:** The directive is exactly --array=0-9%1.

**Continue when:** Make the logs unique.

**If not:** Do not use an uncapped range or a zero cap.

### 5. Use parent and task IDs in logs

**Where:** The laptop or desktop in front of you

Replace both log directives with the two exact lines below. %A is the parent job ID and %a is the array task index.

**Put this in the named Bash file:**

```bash
#SBATCH --output=logs/%x_%A_%a.out
#SBATCH --error=logs/%x_%A_%a.err
```

**Expected:** Each array task has a distinct output and error path.

**Continue when:** Inspect the local diff.

**If not:** Correct both settings before pressing Check my work.

### 6. Calculate the concurrent resource total

**Where:** The laptop or desktop in front of you

Before using any array in a real project, multiply the cap by each task's CPU, memory, and GPU request. For --array=0-9%3 with 2 CPUs and 4 GiB per CPU, three tasks can run together: 3 x 2 = 6 CPUs and 3 x 2 x 4 GiB = 24 GiB. Then add your other active jobs and arrays; the cap applies only to this array.

**Expected:** You can calculate the maximum simultaneous tasks, CPUs, system memory, and GPUs before submission.

**Continue when:** Review the edited practice file.

**If not:** Keep the cap at one until the per-task and combined totals are known.

### 7. Review the edited file

**Where:** The laptop or desktop in front of you

Confirm that only the fictional practice file changed and that no command submitted it.

**Open PowerShell on your Windows computer, then run:**

```powershell
git diff -- workspace/slurm/array_job.slurm.txt
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git diff -- workspace/slurm/array_job.slurm.txt
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git diff -- workspace/slurm/array_job.slurm.txt
```

**Expected:** The diff changes only the array cap and the two log names.

**Continue when:** Run Check my work.

**If not:** Remove every unrelated change before continuing.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 100% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

Reduce the cap to `%1` and validate a representative input. If many tasks fail
identically, cancel the array and debug one task. Use the
[job arrays lab](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/euler-job-arrays.md) for dependent or
heterogeneous workloads.

Useful references:

- [Euler job arrays](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/euler-job-arrays.md)
- [Slurm reference](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/slurm.md)

## Understand Before Accepting AI Output

Calculate concurrency yourself and include other submissions. A personal or
lab limit is a ceiling, not a target for an agent to consume.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
