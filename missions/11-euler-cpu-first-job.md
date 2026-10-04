# Mission: Submit And Control A Tiny Euler CPU Job

## Outcome

Follow one tiny CPU job from an inspected script to its recorded result and output.

## Concept

Euler has login nodes and compute nodes. Prepare files and control jobs from
the login node. Slurm is the scheduler; it runs actual computation on a compute node. A batch job is a submitted script, not merely a file in a folder.
sbatch submits one batch script and returns its job ID. Keep that number in
$HOME, your small private Euler folder, and use the same numeric job ID later.

| Stage | What you inspect | What it establishes |
| --- | --- | --- |
| Create and inspect | Script text and syntax result | The file is ready, not running |
| Submit once | Returned numeric ID | Slurm accepted that submission |
| Observe | `squeue` for that ID | Whether it is currently queued or running |
| Read the result | `sacct`, `seff` and its output | Recorded state, resources and expected calculation |

GiB is the memory unit used here. The teaching request is one CPU, 1 GiB per
CPU, two minutes, no GPU and the already verified Euler Python environment.
This is a workflow test, not a resource recommendation for a research program.

## Learning Challenge

If the script prints correctly but the queue is empty, what has actually
happened so far? Decide which stage you reached before trying another command.
The recipe follows one job throughout; you do not need a second submission.

## Worked Example

<details>
<summary>Read the completed job without mixing its rows</summary>

| Form observation | Where to compare it |
| --- | --- |
| Account | Main row: normal/es_fuge or es_fuge; normal/es+ is truncated |
| State and exit code | Main row: COMPLETED and 0:0 |
| CPU and requested memory | Main row: one CPU and 1G (per-CPU suffix may appear) |
| Observed memory | Relevant .batch step; not the requested value |
| Program output | Same ID: python_environment=passport-python and 5 squared is 25 |

Read seff for that same job. Keep actual logs and identifiers private; enter
only the requested observations in the local form.

</details>

## Common Trap

Submitting again because a short job disappeared from the queue. Keep the
stored ID and read its accounting and logs; queue visibility is not its outcome.




## Your Action

Create one small Python CPU batch script, inspect it, submit it once, and verify its queue, accounting, environment, efficiency, and output.

**Follow these steps in order.** Run every Euler command on the same login node. The recipe stores one job ID in $HOME/passport-euler/first-job.id so it survives logout; never resubmit because a job is pending.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Know where an Euler job runs

**Where:** This web page in your browser

Follow the four stages in the lifecycle above. Before connecting, distinguish preparing a file from asking Slurm to run it. Keep the same numeric job ID for every observation after submission.

**Expected:** You can distinguish the login node from the compute node and state what sbatch, squeue, sacct, and seff do.

**Continue when:** Connect to the login node.

**If not:** Do not run a workload until the login-node and compute-node roles are clear.

### 2. Connect to Euler

**Where:** The laptop or desktop in front of you

From your local terminal, connect with the tested euler alias. The prompt should change to an Euler login node.

**Open PowerShell on your Windows computer, then run:**

```powershell
ssh euler
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
ssh euler
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
ssh euler
```

**Expected:** The shell prompt is on an Euler login node.

**Continue when:** Confirm the login-node context and lab share.

**If not:** Return to the SSH mission; do not use password fallback as a tunnel workaround.

### 3. Confirm the login node and account

**Where:** The remote Euler computer after you connect from your computer

Run these read-only checks on Euler before creating a job. The host must be a login node and my_share_info must list es_fuge.

**After SSH connects to Euler, run this in the same text window:**

```bash
hostname
my_share_info
```

**Expected:** The hostname is an Euler login node and es_fuge appears in your share information.

**Continue when:** Create the small job script.

**If not:** Stop if es_fuge is absent. Do not guess another account; use the access help path.

### 4. Create and inspect the job script

**Where:** The remote Euler computer after you connect from your computer

Paste the whole creation block, including EOF and the final closing parenthesis. It creates or safely reuses the training script, checks its syntax and prints it; it does not run the calculation. Compare its CPU, memory, time, account, environment and log directives with the small teaching request above before submitting.

**After SSH connects to Euler, run this in the same text window:**

<!-- passport-snippet:euler-cpu-tiny-request -->
```bash
(
set -eu
work_dir="$HOME/passport-euler"
script="$work_dir/first-job.slurm"
mkdir -p "$work_dir/logs"
tmp="$(mktemp "$work_dir/.first-job.XXXXXX")"
trap 'if [ -n "${tmp:-}" ]; then rm -f "$tmp"; fi' EXIT
cat > "$tmp" <<'EOF'
#!/usr/bin/env bash
#SBATCH --job-name=passport-cpu
#SBATCH --account=es_fuge
#SBATCH --time=00:02:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err

set -euo pipefail
module purge
module load stack/2024-06 python/3.11.6
venv="$HOME/passport-euler/venvs/passport-python"
[ -x "$venv/bin/python" ] || {
  printf 'STOP: complete the Euler Python environment mission first.\n' >&2
  exit 1
}
. "$venv/bin/activate"
python - <<'PYTHON'
import os
import pathlib
import platform
import socket
import sys

expected = pathlib.Path.home() / "passport-euler" / "venvs" / "passport-python"
if pathlib.Path(sys.prefix) != expected or platform.python_version() != "3.11.6":
    raise SystemExit("STOP: unexpected Python environment")
print(f"job_id={os.environ['SLURM_JOB_ID']}")
print(f"host={socket.gethostname()}")
print(f"cpus={os.environ['SLURM_CPUS_PER_TASK']}")
print("python_environment=passport-python")
for number in range(1, 6):
    print(f"{number} squared is {number * number}")
PYTHON
EOF
if [ -e "$script" ]; then
  cmp -s "$tmp" "$script" || {
    printf 'STOP: %s already exists with different content.\n' "$script" >&2
    exit 1
  }
  printf 'existing-script-ok\n'
else
  mv "$tmp" "$script"
  tmp=''
  printf 'created-script-ok\n'
fi
cd "$work_dir"
bash -n first-job.slurm
sed -n '1,100p' first-job.slurm
)
```
<!-- /passport-snippet:euler-cpu-tiny-request -->

**Expected:** created-script-ok or existing-script-ok, followed by script text ending at PYTHON. EOF and the following creation-command lines are not printed as part of the script. No job was submitted here; an empty queue is normal.

**Continue when:** After checking the script, use Step 5 to submit it once.

**If not:** Correct the script before sbatch; do not submit a script you have not read.

### 5. Submit once and record the job ID

**Where:** The remote Euler computer after you connect from your computer

Submit only when no stored job ID exists. If this step was already completed, the command reuses the stored numeric ID and does not submit another job.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
set -eu
cd "$HOME/passport-euler"
id_file="$HOME/passport-euler/first-job.id"
if [ -e "$id_file" ]; then
  [ -s "$id_file" ] || { printf 'STOP: %s is empty. Ask for help before submitting.\n' "$id_file" >&2; exit 1; }
  job_id="$(cat "$id_file")"
  case "$job_id" in ''|*[^0-9]*) printf 'STOP: stored job ID is invalid.\n' >&2; exit 1;; esac
  printf 'Existing job, not resubmitted: %s\n' "$job_id"
else
  submission="$(sbatch --parsable first-job.slurm)"
  job_id="${submission%%;*}"
  case "$job_id" in ''|*[^0-9]*) printf 'STOP: sbatch did not return a numeric job ID.\n' >&2; exit 1;; esac
  printf '%s\n' "$job_id" > "$id_file"
  chmod 600 "$id_file"
  printf 'Submitted job: %s\n' "$job_id"
fi
)
```

**Expected:** One numeric job ID is printed and stored, including on clusters where sbatch appends a cluster name; rerunning the step says Existing job, not resubmitted.

**Continue when:** Inspect that job in the queue.

**If not:** Read the sbatch error and fix its cause; do not submit a second copy.

### 6. Inspect the queue

**Where:** The remote Euler computer after you connect from your computer

Query only the recorded job. No row means it is not currently visible in the active queue; accounting and logs establish what happened. Keep its ID and do not submit a duplicate.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
job_id="$(cat "$HOME/passport-euler/first-job.id")"
case "$job_id" in ''|*[^0-9]*) printf 'STOP: stored job ID is invalid.\n' >&2; exit 1;; esac
squeue -j "$job_id" -o "%.18i %.2t %.30R"
)
```

- [Only if needed: stop this recorded job](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/euler-first-job.md#stop-the-recorded-job-if-needed)

**Expected:** The job is pending or running, or it has already left the queue.

**Continue when:** Read accounting for that same ID. If the request is wrong and must be stopped, use the optional cancellation section; do not cancel a successful job merely for practice.

**If not:** If the ID is wrong, recover it with squeue -u "$USER" or sacct; do not resubmit.

### 7. Verify completion with sacct

**Where:** The remote Euler computer after you connect from your computer

Run this for the same job. If it says job-not-finished, wait 30 seconds and run this same step again. Never return to sbatch while waiting.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
set -eu
job_id="$(cat "$HOME/passport-euler/first-job.id")"
case "$job_id" in ''|*[^0-9]*) printf 'STOP: stored job ID is invalid.\n' >&2; exit 1;; esac
state="$(sacct -X -n -j "$job_id" --format=State | awk 'NF {print $1; exit}' | cut -d+ -f1)"
case "$state" in
  COMPLETED) printf 'job-completed\n' ;;
  PENDING|RUNNING|CONFIGURING|COMPLETING) printf 'job-not-finished: %s; wait 30 seconds and rerun this step; do not resubmit\n' "$state"; exit 2 ;;
  '') printf 'accounting-not-ready; wait 30 seconds and rerun this step; do not resubmit\n'; exit 2 ;;
  *) printf 'STOP: job ended in %s; inspect both logs before changing resources.\n' "$state" >&2; sacct -j "$job_id" --format=JobID,JobName,User,Account%40,State,ExitCode,Elapsed,AllocCPUS,ReqMem,MaxRSS; exit 1 ;;
esac
sacct -j "$job_id" --format=JobID,JobName,User,Account%40,State,ExitCode,Elapsed,AllocCPUS,ReqMem,MaxRSS
)
```

**Expected:** After job-completed, read the main row: your user, normal/es_fuge or es_fuge, COMPLETED, 0:0, one CPU and 1G requested memory. Account%40 gives the account column room; normal/es+ is truncated, not an account value. MaxRSS may be on the .batch step.

**Continue when:** Use Account%40 to read the full account column, then inspect seff for the same ID. Read the small field guide above; keep actual account/user/job details private.

**If not:** If the state is FAILED, TIMEOUT, or OUT_OF_MEMORY, inspect logs before changing resources.

### 8. Inspect seff

**Where:** The remote Euler computer after you connect from your computer

Read the requested-versus-used CPU and memory summary for the same job.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
job_id="$(cat "$HOME/passport-euler/first-job.id")"
case "$job_id" in ''|*[^0-9]*) printf 'STOP: stored job ID is invalid.\n' >&2; exit 1;; esac
seff "$job_id"
)
```

**Expected:** seff names the recorded job and reports CPU and memory use.

**Continue when:** Verify the program output.

**If not:** Use sacct and logs if seff is not yet available; do not invent utilization values.

### 9. Verify the environment and output markers

**Where:** The remote Euler computer after you connect from your computer

Read only the two expected lines from the output file for the stored job ID. They prove that the batch script used the training environment and completed its calculation.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
job_id="$(cat "$HOME/passport-euler/first-job.id")"
case "$job_id" in ''|*[^0-9]*) printf 'STOP: stored job ID is invalid.\n' >&2; exit 1;; esac
output="$HOME/passport-euler/logs/passport-cpu_$job_id.out"
grep -Fx "python_environment=passport-python" "$output"
grep -Fx "5 squared is 25" "$output"
)
```

**Expected:** The command prints exactly python_environment=passport-python and 5 squared is 25.

**Continue when:** Enter the observed values in the local confirmation fields.

**If not:** Inspect both output and error logs for this job before changing or rerunning anything.

### 10. Check and submit the mission

**Where:** The laptop or desktop in front of you

Return to the local Passport and enter the facts you personally observed for this one job. Job ID is used locally and is excluded from public evidence. Do not enter a username, path or log. Check my work compares the entered facts; the automatic check does not connect to Euler to repeat your observations. Then submit once.

**Expected:** The Passport accepts the job ID, account, owner check, queue check, final state, resources, Python environment check, seff check, and output marker.

**Continue when:** Continue to accounting and right-sizing.

**If not:** Re-read the same job with sacct, seff, and its logs; do not submit another job.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 100% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## Learning Check

### Practise

Try an answer before opening the explanation. These questions are for
practice; they do not affect your progress.

1. The creation command printed existing-script-ok and the script. You have not used the submission step. Why might squeue be empty?

   - The file exists, but no job has been submitted by that command.
   - The calculation already finished; record success without checking.
   - Euler lost the file; create it repeatedly until a job appears.

<details class="learning-explanation">
<summary>See an explanation</summary>

Creating or printing a script is a file operation. Inspect it, then use the guarded submission step once if no ID is stored. Its returned ID lets you follow the actual job; neither the marker nor an empty queue proves execution.

</details>

## If Blocked

For an invalid account, stop and check `my_share_info`. For a pending job,
inspect `myjobs -j "$job_id"` instead of submitting duplicates. Read the first
meaningful error before changing resources. Use the
[first Euler job lab](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/euler-first-job.md) for recovery.

Useful references:

- [First Euler job](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/euler-first-job.md)
- [Slurm reference](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/slurm.md)
- [IDEAL Lab Euler share policy](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/policy/euler-share.md)

## Understand Before Accepting AI Output

Personally read the script, record the real job ID, know how to cancel it, and
inspect output and accounting. An agent must not submit or enlarge the job.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
