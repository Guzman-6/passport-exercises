# Mission: Measure And Right-Size An Euler Job

## Outcome

Read the completed training job's accounting, then reason about a separate
fictional representative run. No new job is required.

## Concept

Requested resources and resources actually used are different. sacct reports
recorded fields; seff summarizes efficiency for the same job. Use this table
as a lookup while reading the output, rather than memorizing six definitions.

| Resource | Reservation | Observation to compare |
| --- | --- | --- |
| CPU | AllocCPUS | CPU efficiency in seff; allocated does not mean used |
| Memory | ReqMem, with its units and per-CPU/total meaning | MaxRSS on the relevant job step |
| Time | Requested maximum time | Elapsed, the actual run time |

State and ExitCode say how the job ended. Inspect a software failure before
changing its resources. The tiny training job helps locate these fields; only
a representative workload can support a production sizing decision.

## Learning Challenge

A serial run reserved four CPUs, 16 GiB per CPU and two hours, but took 20
minutes with 22% CPU efficiency and 9 GiB MaxRSS. Before reading the model,
which reservations look unsupported by this evidence? The official questions
ask you to choose the next test for this fictional case.

## Worked Example

<details>
<summary>Reason about the next test</summary>

Four times 16 GiB reserves 64 GiB. If the program is serial, more allocated CPUs
do not make its computation parallel. Compare memory and time with the observed
values, leave sensible headroom, and test the reduced request on representative
input. One sample does not establish every production input's needs. An import
error needs a software fix, not an unexplained increase in resources.

</details>

## Common Trap

Treating a deliberately tiny calculation as a production benchmark, or
increasing every resource after an error without diagnosing it.

## Your Action

Read sacct and seff for the existing tiny job, then choose a next test from the separate fictional representative-run scenario. Submit no new job.

**Follow these steps in order.** Connect to Euler and reuse the job ID from the first-job mission. This mission does not submit another job.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Distinguish requested and used resources

**Where:** This web page in your browser

Use the compact field guide above while reading your existing job. Requested resources describe its reservation, not measured use. The tiny training job locates the fields; the separate fictional serial run supplies the sizing exercise.

**Expected:** You can distinguish allocated resources from measured use.

**Continue when:** Connect and recover the existing job ID.

**If not:** Return to the first-job mission; do not submit another job for this exercise.

### 2. Connect to Euler

**Where:** The laptop or desktop in front of you

From the local terminal, connect with the tested euler alias. Run every later command in the Euler shell that opens.

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

**Expected:** The prompt changes to an Euler login node.

**Continue when:** Recover the existing training job ID on Euler.

**If not:** Return to the SSH access mission; do not run Euler commands in the local shell.

### 3. Use the existing job ID

**Where:** The remote Euler computer after you connect from your computer

Read the job ID saved by the previous mission. If the file is missing, list recent accounting records and identify the single passport-cpu job instead of submitting another job.

**After SSH connects to Euler, run this in the same text window:**

```bash
id_file="$HOME/passport-euler/first-job.id"
if [ -s "$id_file" ]; then printf 'Stored job ID: '; cat "$id_file"; else sacct -X -u "$USER" --starttime today --format=JobID,JobName,State,Elapsed; fi
```

**Expected:** You identify the existing passport-cpu job ID.

**Continue when:** Inspect its detailed accounting.

**If not:** Stop if you cannot identify one unambiguous training job.

### 4. Read the accounting fields

**Where:** The remote Euler computer after you connect from your computer

Load the stored ID. If it was missing, enter the passport-cpu ID you identified and save it. Then query state, exit code, elapsed time, allocated CPUs, requested memory, and maximum resident memory. Continue only after the main job is COMPLETED with exit code 0:0.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
set -eu
id_file="$HOME/passport-euler/first-job.id"
if [ -e "$id_file" ] && [ ! -s "$id_file" ]; then printf 'STOP: %s exists but is empty. Ask for help before changing it.\n' "$id_file" >&2; exit 1; fi
if [ -s "$id_file" ]; then job_id="$(cat "$id_file")"; else read -r -p 'Existing passport-cpu job ID: ' job_id; fi
case "$job_id" in ''|*[^0-9]*) printf 'STOP: job ID must contain digits only.\n' >&2; exit 1;; esac
if [ ! -e "$id_file" ]; then mkdir -p "$(dirname "$id_file")"; printf '%s\n' "$job_id" > "$id_file"; chmod 600 "$id_file"; fi
sacct -j "$job_id" --format=JobID,JobName,State,ExitCode,Elapsed,AllocCPUS,ReqMem,MaxRSS
state="$(sacct -X -n -j "$job_id" --format=State | awk 'NF {print $1; exit}' | cut -d+ -f1)"
exit_code="$(sacct -X -n -j "$job_id" --format=ExitCode | awk 'NF {print $1; exit}')"
[ "$state" = COMPLETED ] && [ "$exit_code" = 0:0 ] || { printf 'STOP: wait for COMPLETED 0:0 or inspect the failed job; do not resubmit. Current result: %s %s\n' "${state:-unavailable}" "${exit_code:-unavailable}" >&2; exit 1; }
printf 'accounting-ready\n'
)
```

**Expected:** sacct shows the main job and its steps, the main job is COMPLETED with exit code 0:0, MaxRSS is read from the relevant step when available, and the final line is accounting-ready.

**Continue when:** Read the efficiency summary.

**If not:** Wait for accounting to appear or verify the job ID; do not resubmit.

### 5. Read seff

**Where:** The remote Euler computer after you connect from your computer

Use seff for a concise CPU and memory efficiency summary, while keeping sacct as the source for exact fields.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
job_id="$(cat "$HOME/passport-euler/first-job.id")"
case "$job_id" in ''|*[^0-9]*) printf 'STOP: stored job ID is invalid.\n' >&2; exit 1;; esac
seff "$job_id"
)
```

**Expected:** seff reports the same job's CPU and memory efficiency.

**Continue when:** Decide what evidence is representative.

**If not:** Use sacct and application logs if seff is unavailable.

### 6. Interpret before changing resources

**Where:** The remote Euler computer after you connect from your computer

Compare allocated CPU count, requested memory and time with measured use. The tiny job checks the workflow and field lookup; its utilization is not representative of a production input.

- [Only if needed: accounting fields and job steps](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/slurm.md#completed-job-accounting)

**Expected:** You can explain AllocCPUS, ReqMem, MaxRSS, Elapsed, State, and ExitCode.

**Continue when:** Use the fictional representative run for the next-test decision. MaxRSS belongs to a reported step and its units; do not multiply or interpret it blindly across a parallel/MPI workload.

**If not:** Return to the field definitions; do not increase resources by guesswork.

### 7. Choose the next measured request

**Where:** The remote Euler computer after you connect from your computer

Use the representative serial-run scenario in the questions, not the tiny calculation, to choose the next test. Before reading the model, compare reserved and used resources and decide what headroom is justified. This lesson asks for a decision; it does not submit that request.

**Expected:** Your selected next test has a reason for its CPU, total memory and time values.

**Continue when:** Complete the questions and local confirmation.

**If not:** Measure a representative input before claiming a production allocation.

### 8. Submit accounting evidence

**Where:** The laptop or desktop in front of you

Enter the existing job ID and confirm that you personally inspected sacct and seff. Do not paste logs into the public record.

**Expected:** The result contains only the requested inspection facts and no username, path, log, or other private value.

**Continue when:** Run Check my work and submit once.

**If not:** Return to Euler and inspect the named command before attesting.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 80% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## Learning Check

### Practise

Try an answer before opening the explanation. These questions are for
practice; they do not affect your progress.

1. A single-task request uses three CPUs and 4 GiB per CPU. MaxRSS is 6 GiB on the relevant step. Which comparison is correct?

   - Requested 4 GiB total and used 6 GiB; increase resources immediately.
   - Requested 12 GiB total; compare observed 6 GiB with that reservation and representative variation.
   - Used 18 GiB because every recorded memory value must be multiplied by CPU count.

<details class="learning-explanation">
<summary>See an explanation</summary>

The request reserves 3 x 4 = 12 GiB. MaxRSS is an observation for a reported step, not a per-CPU request to multiply again. Use units, workload structure and representative variation before a future sizing decision.

</details>

## If Blocked

Do not increase resources when fields are unclear. Use
[Euler resource optimization](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/euler-resource-optimization.md)
and ask for help for MPI/multiprocess workloads, highly variable inputs, or
disagreeing metrics.

Useful references:

- [Euler resource optimization](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/euler-resource-optimization.md)
- [Slurm reference](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/slurm.md)

## Understand Before Accepting AI Output

Verify arithmetic, per-CPU versus total memory, representativeness, and the
parallelism claim. An agent cannot infer scaling merely from CPU availability.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
