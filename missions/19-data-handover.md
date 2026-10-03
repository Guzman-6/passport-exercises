# Mission: Create A Recoverable Project Handover

## Outcome

Create a handover that another authorized researcher can use without your
personal account or computer.

## Concept

A project handover is the documented transfer of ownership, access, locations,
and knowledge before a person leaves. It identifies the main approved code and
data, explains how to reproduce important results, confirms that successors
can access them, and names what may be cleaned up. A code revision is the exact
recorded version used for a result; an environment definition records the
software needed to run it.

A directory full of unexplained files is not a handover, even if the files still exist.

## Worked Example

Another authorized person could locate, verify, rerun, and safely retire the fictional project without hidden personal dependencies.

Check these points:

- **What is a successful handover?** An authorized successor can locate, verify, rerun, and maintain or retire the work.
- **How are credentials handled in a handover?** Rotate or provision access through approved channels; never place secrets in the document.

## Common Trap

Listing a folder without naming its owner, code revision, environment, access boundary, or retention decision.

## Your Action

Complete the fictional handover practice file so another authorized person can locate, verify, rerun, and retire the project.

**Follow these steps in order.** Use fictional values only. Never enter a real private path, person, credential, unpublished detail, or participant information.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Prepare the handover practice file

**Where:** The laptop or desktop in front of you

Press Prepare practice folder, enter it, and open workspace/handover/project-handover.md.

**Expected:** The fictional template is open in the practice repository.

**Continue when:** Replace every placeholder with fictional information.

**If not:** Do not use a real project document for this exercise.

### 2. Record current and successor ownership

**Where:** The laptop or desktop in front of you

Replace the two ownership placeholders with fictional role names. Use the example below so this public exercise contains no real person.

**Put this in the named Markdown file:**

```markdown
Current owner: Example Researcher

Authorized successor: Example Project Maintainer
```

**Expected:** Both ownership fields contain non-placeholder values.

**Continue when:** Record code and environment identity.

**If not:** Do not claim a handover without an authorized successor.

### 3. Record reproducible code

**Where:** The laptop or desktop in front of you

A code revision is the exact recorded version used for a result; an environment definition records the required software. Replace both placeholders with the fictional values below. A real handover would use the exact commit produced by git rev-parse HEAD and the committed environment file.

**Put this in the named Markdown file:**

```markdown
Revision: 0123456789abcdef0123456789abcdef01234567

Environment definition: environment.yml at the recorded revision
```

**Expected:** The revision has exactly 40 hexadecimal characters and the environment field is complete.

**Continue when:** Record the main approved and temporary data locations.

**If not:** Replace labels such as latest or current with an exact revision.

### 4. Record data locations and cleanup

**Where:** The laptop or desktop in front of you

Replace both data placeholders with the fictional paths below. They demonstrate a durable project location and a temporary copy without exposing a real lab path.

**Put this in the named Markdown file:**

```markdown
Main approved data location: P:\ExampleSupervisor\example-user\synthetic-project

Temporary locations to remove: D:\example-user\synthetic-project-cache
```

**Expected:** The durable and temporary roles are unambiguous.

**Continue when:** Add a verification command and expected result.

**If not:** Resolve which copy is the main approved copy before continuing.

### 5. Record how to verify the project

**Where:** The laptop or desktop in front of you

Replace the verification placeholders with the harmless fictional command and exact expected result below.

**Put this in the named Markdown file:**

```markdown
Verification command: python -m unittest discover -s tests -v

Expected result: All 12 synthetic tests pass.
```

**Expected:** The successor can tell success from failure.

**Continue when:** Assign access, retention, and deletion owners.

**If not:** Do not write works on my machine as verification.

### 6. Record access and retention actions

**Where:** The laptop or desktop in front of you

Use fictional role names for access and retention. Replace YYYY-MM-DD with a real future date for this exercise, such as a date 30 days from today. Then replace the Known Limitations placeholder with one fictional unresolved limitation.

**Put this in the named Markdown file:**

```markdown
Access owner: Example Project Maintainer

Retention owner: Example Data Steward

Temporary-copy deletion date: YYYY-MM-DD

Unresolved risk or limitation: Synthetic rerun has not been tested on a second operating system.
```

**Expected:** Both owners, a valid future date, and one fictional limitation replace all placeholders.

**Continue when:** Review the completed file.

**If not:** Do not delete or revoke anything without a named owner and date.

### 7. Check scope and placeholders

**Where:** The laptop or desktop in front of you

Confirm that only the fictional handover practice file changed, every placeholder is gone, and no real information was inserted.

**Open PowerShell on your Windows computer, then run:**

```powershell
git diff -- workspace/handover/project-handover.md
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git diff -- workspace/handover/project-handover.md
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git diff -- workspace/handover/project-handover.md
```

**Expected:** The diff is complete, fictional, and limited to one file.

**Continue when:** Run Check my work.

**If not:** Remove real or extra information before submitting.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 80% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

Record missing ownership or retention decisions explicitly rather than
inventing them. Use the
[project handover lab](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/project-handover.md) and ask the
supervisor to assign the next owner.

Useful references:

- [Project Handover](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/project-handover.md)
- [Data Steward](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/tracks/data-steward.md)

## Understand Before Accepting AI Output

An agent may format an inventory but cannot certify that paths exist, access
works, results reproduce, or disposal is approved. A person verifies each item.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
