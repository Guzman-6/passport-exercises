# Mission: Respond To Incidents And Own Automated Work

## Outcome

Stop and report an IT incident safely. An AI coding agent is software that can
inspect project files and request actions; learn who remains responsible when
it or other automation performs work.

## Concept

An incident is a real or suspected loss of confidentiality, access, control, or data. Stop the harmful action, preserve useful evidence, verify containment, and report through the private route.

An AI coding agent is a tool that can read project files and request edits or commands. Automation is software that performs steps without a person typing each one. The person who authorizes and reviews either kind of action remains responsible for it.

One example is a runaway Euler job: a program submitted to the shared cluster through Slurm that is consuming resources by mistake. Its numeric job ID identifies it; `scancel` stops it, `squeue` shows queued or running jobs, and `sacct` shows recorded job history. These commands are introduced here only so the fictional scenario is understandable; the Euler track teaches how to use them.

## Worked Example

The answer preserves evidence, contains risk, uses the private reporting path, and leaves accountability with a person.

Check these points:

- **Put the first incident-response actions in order.** Stop the risky action and preserve evidence. -> Contain or revoke what can cause further harm. -> Report through the private incident path. -> Document verified facts and follow-up.
- **Who owns an action taken by an AI coding agent?** The person who authorized and reviewed the action.
- **A mistaken Euler job is consuming resources. Put the immediate actions in order.** Record the job ID and stop it with scancel. -> Confirm with squeue or sacct that it stopped. -> Inspect the script and first meaningful error before resubmitting.
- **The only copy of a result was left in scratch and is now missing. What is the honest response?** Stop creating new files there, check approved recovery options, report the loss, and reconstruct only from recorded inputs if possible.

## Common Trap

Trying to make the incident look harmless before preserving evidence or notifying the owner.

## Your Action

Practise a safe incident response and confirm who remains responsible for automated actions.

**Follow these steps in order.** Use only the fictional scenarios below. If one resembles a current event, leave the exercise and use the private incident path.

### 1. Understand the incident examples

**Where:** This web page in your browser

An incident is a suspected loss of confidentiality, access, control, or data. An AI coding agent is a tool that can read project files and request edits or commands. Automation is software that performs steps without a person typing each one. In the Euler example, Slurm is the scheduler and a job is a submitted program identified by a number. scancel stops that job, squeue shows active jobs, and sacct shows recorded job history. You are learning the response order here, not running these commands.

- [Read the incident and help procedure](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/incidents-and-help.md)

**Expected:** You can explain the Euler example without needing to know Slurm syntax.

**Continue when:** Continue using only the fictional scenarios.

**If not:** Read the definitions again; do not experiment on a real account or job.

### 2. Confirm the scenario is fictional

**Where:** This web page in your browser

Do not enter real names, account identifiers, logs, credentials, job output, or project details in this public learning record.

**Expected:** The exercise contains fictional values only.

**Continue when:** Continue with the response order.

**If not:** Stop the exercise and open the real incident procedure.

### 3. Stop the risky action

**Where:** This web page in your browser

Stop the known harmful action without destroying evidence. For a runaway Euler job, record its job ID and cancel that job.

- [Choose the correct private incident route](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/incidents-and-help.md)

**Expected:** The immediate harmful action has stopped.

**Continue when:** Verify the stopped state.

**If not:** Stop trying to fix it alone. Use the linked incident procedure to send a private report to your supervisor or lab IT, ETH cyber incident support, or ETH High-Performance Computing (HPC) support.

### 4. Verify containment

**Where:** This web page in your browser

Check the affected service directly. Examples include confirming a token is revoked or using squeue or sacct to confirm a job stopped.

- [Choose the correct private incident route](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/incidents-and-help.md)

**Expected:** The service reports the contained state.

**Continue when:** Continue to reporting.

**If not:** Do not assume containment. Preserve the observed facts and use the linked private incident route.

### 5. Identify the private reporting route

**Where:** This web page in your browser

For each fictional scenario, use the linked procedure to identify the private contact. Contact your supervisor or lab IT for lab projects, NAS, or research data. Contact ETH cyber incident support for stolen credentials, phishing, malware, or attacks. Contact ETH High-Performance Computing (HPC) support for Euler service or account problems that contain no confidential research content. Do not send a real report for a fictional scenario. Public Passport submissions and public help issues are never incident channels.

- [Open the incident and help procedure](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/incidents-and-help.md)

**Expected:** You can name the correct private recipient for each fictional scenario without contacting that recipient.

**Continue when:** Continue to the accountability question.

**If not:** Use the linked decision list. If this is a real event, leave the exercise and report it privately; do not put its details in the Passport.

### 6. Keep a person accountable

**Where:** This web page in your browser

The person who authorizes and reviews an AI or automation action remains responsible for its commands, changes, publication, and consequences.

**Expected:** A named person owns every automated action.

**Continue when:** Continue to the scenarios.

**If not:** Stop automation that has no accountable reviewer.

### 7. Complete the scenarios

**Where:** This web page in your browser

Put the response actions in order and answer the accountability questions.

**Expected:** Every safety-critical scenario follows the documented order.

**Continue when:** Run Check my work.

**If not:** Use the feedback and retry with fictional information only.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 100% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

If one scenario resembles a real current event, stop writing the assessment
answer and select **This is a real incident**. The Passport leaves the exercise
without collecting incident details and opens the private reporting choices in
the incident guide. The
[incident scenarios lab](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/incident-scenarios.md) provides
additional safe examples.

Useful references:

- [Incidents And Help](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/incidents-and-help.md)
- [Incident Scenarios](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/incident-scenarios.md)
- [Agents And Interfaces](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/ai/agents-and-interfaces.md)

## Understand Before Accepting AI Output

An AI tool must not decide whether an incident is harmless, erase evidence, or
contact external services with protected details. You remain responsible for
stopping, preserving safe evidence, submitting the report, and verifying that
the documented incident path was followed.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
