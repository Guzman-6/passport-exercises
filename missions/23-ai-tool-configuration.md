# Mission: Set Up One AI Coding Tool Safely

## Outcome

An AI coding tool can inspect project files and propose edits or commands.
Set up one such tool for the fictional practice project. Learn which account
provides access, what may cost money, where any secret access key is stored,
and how to confirm that setup changed no project file.

## Concept

An artificial-intelligence (AI) setup contains several parts. A model generates text. A provider or gateway supplies access and billing. A coding agent uses the model while reading files or requesting tools. An editor is the application where you view, control, and review that work. An application programming interface (API) key is a secret that authorizes programmatic service use and may spend money.

Choose one complete setup option, not only a model name. Account ownership, cost limits, permissions, and data rules still apply independently.

## Worked Example

The components are classified correctly and no credential appears in a file, prompt, screenshot, or Git diff.

Check these points:

- **What is OpenRouter in this stack?** A provider or gateway for model access, routing, billing, and limits.
- **Where may an API key be stored?** In the supported operating-system keychain or approved secret store.

## Common Trap

Calling OpenRouter an agent, confusing a model with an editor, or pasting an API key into settings tracked by Git.

## Your Action

Configure one AI coding tool, open only the fictional practice repository, and prove that a read-only request changes no file.

**Follow these steps in order.** An artificial-intelligence (AI) model generates a response. A provider supplies access and billing. A coding agent may read files and request tools. An editor is the application where you see and control it. An application programming interface (API) key is a secret that authorizes programmatic service use and may spend money. Identify these parts first. Use the no-cost Copilot Student option if eligible; any personal paid service remains your financial responsibility.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Identify the components

**Where:** This web page in your browser

Identify each part of the setup: the model generates a response; the provider or gateway supplies access and billing; the coding agent can read files or request tools; the editor is the application where you control it. For example, OpenRouter is a gateway, not a coding agent. You do not need to configure a tool protocol for this lesson.

- [Read agents and interfaces](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/ai/agents-and-interfaces.md)

**Expected:** You can name the role of every component in the chosen setup.

**Continue when:** Choose one setup option.

**If not:** Do not configure credentials until the billing path and agent are clear.

### 2. Choose one setup option

**Where:** This web page in your browser

Use exactly one option. Eligible students use VS Code with GitHub Copilot Student. If you deliberately choose Zed with a personal OpenRouter account, skip the two Copilot-only steps and follow the linked Zed procedure. Use another option only when its owner has supplied written setup, data, cost, and permission rules. If no option is available, leave this lesson pending and continue the non-AI lessons.

- [Compare supported AI setup options](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/ai/README.md)

**Expected:** You have selected one option and can name its account owner, payer, editor, and agent interface.

**Continue when:** Follow only the selected option below.

**If not:** Leave this lesson pending and continue manually. Do not create a paid account merely to pass.

### 3. Copilot option: activate the Student benefit

**Where:** This web page in your browser

Do this step only for the Copilot option. After GitHub Education approval, open Education benefits. If Copilot Student is already active, keep it. Otherwise select the Copilot Student activation offered by GitHub. If GitHub asks for payment or a payment method, stop; payment is not required for this option.

- [Open Education benefits](https://github.com/settings/education/benefits)

- [Read Copilot Student setup](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/ai/vscode-copilot-student.md)

**Expected:** GitHub identifies the Student benefit without a paid checkout.

**Continue when:** Continue to the Copilot VS Code step. Zed users skip to the Zed step.

**If not:** Continue manual onboarding while verification is pending; do not purchase access to pass.

### 4. Copilot option: connect VS Code

**Where:** The laptop or desktop in front of you

Do this step only for the Copilot option. VS Code is the editor used here. An extension is an add-on installed inside the editor; GitHub Copilot is the coding-agent extension. Install or open VS Code. Open Extensions, install GitHub Copilot from publisher GitHub if it is absent, then select the Copilot icon, choose Use AI Features, and sign in with the same GitHub account used for the Passport. If more than one GitHub account is present, use the Accounts menu to select the intended account for Copilot.

- [Download VS Code](https://code.visualstudio.com/)

- [Follow the IDEAL Lab VS Code setup](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/vscode.md)

**Expected:** VS Code shows the intended GitHub account and opens its Chat or Agent interface.

**Continue when:** Continue to Prepare the fictional practice repository.

**If not:** Use the Accounts menu to select the intended account. Do not purchase a plan or grant unexplained access to pass this mission.

### 5. Zed option: follow the personal OpenRouter procedure

**Where:** This web page in your browser

Do this step only for the Zed option; Copilot users skip it. Follow the linked procedure from start to finish: create a separate personal key, set a low key limit before use, and enter it only through Zed's provider UI so the operating-system keychain stores it. The lab does not provide credits, reimburse charges, or accept liability for personal usage or loss.

- [Read the optional Zed and OpenRouter procedure](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/ai/zed-openrouter.md)

**Expected:** For the Zed option, a dedicated limited key is stored outside files and Git. For the Copilot option, this step is skipped.

**Continue when:** Continue to Prepare the fictional practice repository.

**If not:** Revoke an exposed key and stop requests until account activity is understood.

### 6. Open the fictional practice repository

**Where:** The laptop or desktop in front of you

Press Prepare practice folder, run the displayed enter-folder command, and open that exact folder in the editor configured above. Check the editor title or file tree before opening the agent. Do not use a research repository for this test.

**Expected:** The editor is open at the Passport practice repository and the terminal is at its root.

**Continue when:** Run the read-only prompt.

**If not:** Run gh passport doctor; do not substitute another repository or create a second clone.

### 7. Run a read-only agent check

**Where:** The laptop or desktop in front of you

Start a new agent chat for the open practice repository and paste the prompt below. Do not approve an edit or terminal command.

**Paste this into the agent:**

```text
Read the repository instructions and list the top-level files and folders you can see. Do not edit files, run terminal commands, install software, or access anything outside this repository. Tell me when you are finished.
```

**Expected:** The response refers to files that exist in the practice repository and no edit or command was attempted.

**Continue when:** Verify the working tree yourself.

**If not:** Stop the agent and inspect every action it attempted.

### 8. Verify that configuration changed no project file

**Where:** The laptop or desktop in front of you

Run the limited Git status command at the practice repository's root, meaning its top-level folder. It checks the AI practice files and common editor or credential-file locations without confusing this lesson with unfinished files from another exercise.

**Open PowerShell on your Windows computer, then run:**

```powershell
git status --short -- workspace/agent_task .vscode .zed .env .env.local
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git status --short -- workspace/agent_task .vscode .zed .env .env.local
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git status --short -- workspace/agent_task .vscode .zed .env .env.local
```

**Expected:** The command prints nothing: no AI practice file, editor setting, transcript, or credential file changed.

**Continue when:** Complete the questions and run Check my work.

**If not:** Do not commit the change; remove it safely and rotate any exposed credential.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 100% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

Use the offline route. Purchasing access is never a recovery requirement. For
technical symptoms, use [AI-agent troubleshooting](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/troubleshooting/ai-agents.md).

Useful references:

- [AI coding agents](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/ai/README.md)
- [Vscode Copilot Student](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/ai/vscode-copilot-student.md)
- [Zed Openrouter](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/ai/zed-openrouter.md)
- [Cost Context And Failures](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/ai/cost-context-and-failures.md)

## Understand Before Accepting AI Output

Budget limits reduce financial exposure but do not prove data approval,
correctness, or safe execution. You remain responsible for charges on a
personal account and for every accepted command and diff.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
