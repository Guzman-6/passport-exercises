# Mission: Start And Resume Your Passport

## Outcome

Open the assigned Passport, understand where progress is stored, and reopen
the same Passport later.

## Concept

Before using a lab system, know its role. Git records file history; GitHub stores shared project folders, called repositories, and their reviews. Network-attached storage (NAS) is durable shared project storage. Blade is a shared remote Windows computer for licensed graphical software. Euler is an ETH Zurich service made of many managed computers for research calculations. A CPU is the general-purpose processor used by most programs; a GPU is an accelerator used only by compatible programs. Euler schedules both kinds of work.

The Passport itself runs locally, meaning on the computer in front of you. It appears in your web browser, such as Chrome, Edge, Firefox, or Safari. It remembers your draft and current page on that computer. An automatic Passport check on GitHub records whether submitted work passed.

Some lessons use text commands. A command is one instruction for a computer. A
terminal is the application where you type or paste it. A shell is the program
inside the terminal that reads it: PowerShell on Windows, zsh on macOS, and
Bash on Linux or Euler. On macOS and Linux, open the application named
Terminal; it starts zsh or Bash automatically. Bash runs inside that terminal;
no separate Bash application is needed for this course.

## Worked Example

Your saved lesson list reopens on this computer, and GitHub records a result
only after you submit an exercise.

Check these points:

- **Which source proves that submitted work passed?** The automatic Passport check shown on GitHub for the submitted work.
- **How do you reopen the real passport later?** Run gh passport open; the launcher remembers the managed folder on this computer.

## Common Trap

Treating a remembered browser page as proof that a lesson passed.

## Your Action

Confirm that you are in your local Passport, review your assigned lessons, then prove that you can close and reopen it.

**Follow these steps in order.** Do not submit anything from a public course preview. Complete each check before moving to the next one.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Confirm the page mode

**Where:** This web page in your browser

Read the banner at the top of the page. Your working copy must say that this is your local Passport. A page labelled Public course preview is only an example and cannot save or submit work.

**Expected:** The banner identifies your local Passport.

**Continue when:** Continue to the computer check.

**If not:** Return to How to start and launch your Passport before continuing.

### 2. Check your operating system

**Where:** This web page in your browser

Open the Passport progress page and confirm that it names the operating system on the computer in front of you: Windows, macOS, or Linux.

**Expected:** The operating system shown on the progress page matches this computer.

**Continue when:** Continue to the command basics.

**If not:** Stop before platform-specific work, submit one help request without private information, and return later. Keep this Passport; do not create a second one or alter its files.

### 3. Learn where commands run

**Where:** This web page in your browser

Every command names the computer and application where it runs. Your computer or local means the laptop or desktop in front of you; remote means another computer reached through the network. A terminal is the text application you open. A shell is the program inside it that reads commands: PowerShell on Windows, zsh on macOS, and Bash on Linux or Euler. On Windows, open PowerShell. On macOS or Linux, open Terminal; it starts zsh or Bash automatically. You do not need to install a separate Bash or zsh application. A prompt is the text and cursor showing that the shell is ready. Paste only the displayed command after that prompt, press Enter once, and read the output before continuing. A path is the address of a file or folder.

- [Open terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)

**Expected:** You can distinguish a terminal from a shell and identify the machine named above a command.

**Continue when:** Continue to the system map.

**If not:** Reopen How to start and read Before step 1 before running any command.

### 4. Meet the systems used by the lab

**Where:** This web page in your browser

Read the short system map. Git and GitHub manage code history and review. The NAS stores durable shared project data. Blade is a shared remote Windows computer for licensed graphical software. Euler is an ETH Zurich service made of many managed computers for research calculations. A CPU is the general-purpose processor used by most programs; a GPU is an accelerator used only by compatible programs. Euler schedules both kinds of work. Later lessons explain access; do not connect to any of these systems in this step.

- [Open the laptop, NAS, Blade, and Euler map](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/environments-overview.md)

**Expected:** You can state in one sentence what GitHub, NAS, Blade, and Euler are used for.

**Continue when:** Review why each lesson was assigned to you.

**If not:** Read the linked system map before choosing or removing a responsibility.

### 5. Review your assigned lessons

**Where:** This web page in your browser

Read the lesson list from top to bottom. Each lesson teaches and checks one practical skill. Related lessons are grouped by topic. The Passport automatically adds any earlier lessons needed for the work you selected. Check that the list covers what you expect to do in the lab.

**Expected:** You can explain why each optional group of lessons appears.

**Continue when:** Continue when the lesson list matches your work.

**If not:** Use the help request without private information if a required responsibility is missing or an irrelevant one was assigned.

### 6. Know where progress is stored

**Where:** This web page in your browser

Draft answers stay on this computer. When you submit a lesson, the launcher creates a small public submission record on GitHub containing only the requested safe answers. An automatic Passport check reads that submitted record and reports the official result on GitHub. A checked box in the browser alone is not an official pass.

**Expected:** You can distinguish a local draft, a public submission record, and the automatic GitHub result.

**Continue when:** Continue to the resume test.

**If not:** Re-read the status explanation before submitting any lesson.

### 7. Close and reopen the Passport

**Where:** The laptop or desktop in front of you

The Passport page is provided by a small local server: a program running on this computer in the terminal you kept open. Close this browser tab. Return to that terminal. Hold the Ctrl key and tap C once; do not type the characters Ctrl+C. This asks the local server to stop. Wait until the normal PowerShell, zsh, or Bash prompt returns, then paste and run the open command below. Do not reinstall the extension or clone another repository.

**Open PowerShell on your Windows computer, then run:**

```powershell
gh passport open
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
gh passport open
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
gh passport open
```

**Expected:** The first local server stops, then the browser reopens the same Passport and lesson list from a new local server.

**Continue when:** Return to this lesson and select Check my work.

**If not:** If Ctrl+C does not return a prompt, open one new terminal. Run gh passport doctor there, then request help without including private information if the same Passport cannot be found.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 80% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

If `gh passport open` stops, run `gh passport doctor`. Keep only its non-secret
check names and statuses. Do not delete the Passport folder, regenerate SSH
keys, reset Git, or change file permissions.
Use **Request help without posting secrets** on the progress page if the named
recovery step does not resolve the problem. The public issue is assigned to
the lab maintainer for asynchronous triage; nobody needs to be online when you
submit it.

Use the [glossary](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/glossary.md) when a term is unfamiliar.

Useful references:

- [Passport start page](https://github.com/IDEALLab/onboarding-IT/blob/main/README.md)
- [Glossary](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/glossary.md)

## Understand Before Accepting AI Output

An AI tool cannot determine which systems, project data, or responsibilities
your supervisor approved. Do not let it invent access, edit `passport.json`,
or claim that the trusted check passed when you did not observe that result.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
