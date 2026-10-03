# Mission: Configure Git Identity And GitHub Access

## Outcome

Configure Git, the file-history program on your computer, and GitHub, the service that stores shared repositories and reviews. Verify the account and commit identity used by the practice repository.

## Concept

Git is version-control software on your computer: it records file changes as commits. A repository is a project folder plus that history. GitHub stores a remote copy of a repository so people can share and review work. GitHub CLI is the command-line program named `gh` that signs in and performs GitHub actions.

Git author identity and GitHub login are separate. Check both before changing a project so commits have the correct author and go to the intended repository and branch.

## Worked Example

Git and GitHub CLI are available, GitHub CLI names the intended account, and Git identity is explicit.

Check these points:

- **What must gh auth status confirm?** The intended GitHub account is authenticated.
- **What should you do before repairing a failed tool check?** Read the named check and follow its specific recovery step.

## Common Trap

Changing SSH keys, deleting configuration, or reinstalling everything before reading the exact failed check.

## Your Action

Prepare the practice repository, verify Git and GitHub CLI, authenticate the intended account, and set a valid commit identity.

**Follow these steps in order.** Run one step at a time in the practice folder. Keep a working setup; repair only the check that fails.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Know what Git and GitHub do

**Where:** This web page in your browser

Git records versions of files on this computer. A repository is a project folder and its history. A branch keeps one line of work separate. GitHub stores a shared online copy of the repository. A clone is a separate working copy on your computer. Git saves the online address under a short name called a remote; origin is the usual name for the copy you cloned from. GitHub CLI is the program named gh that signs in and performs GitHub actions from a terminal.

- [Open the Git workflow reference](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/git_workflow.md)

**Expected:** You can distinguish Git on your computer from GitHub on the web.

**Continue when:** Prepare the isolated practice repository.

**If not:** Read the definitions before changing identity, login, branch, or remote settings.

### 2. Prepare the Git practice folder

**Where:** The laptop or desktop in front of you

Press Prepare practice folder in this step. Wait for the Passport to show one folder path and one practice branch. Run the displayed enter-folder command and keep this terminal in that folder.

**Expected:** The Passport reports a ready practice folder.

**Continue when:** Use the displayed enter-folder command.

**If not:** Do not create or delete folders manually; run gh passport doctor.

### 3. Check Git and GitHub CLI

**Where:** The laptop or desktop in front of you

Open PowerShell on Windows or the Terminal application on macOS or Linux. On Linux, the terminal normally starts the Bash shell. Run both checks after entering the practice folder.

**Open PowerShell on your Windows computer, then run:**

```powershell
git --version
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git --version
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git --version
```

**Open PowerShell on your Windows computer, then run:**

```powershell
gh --version
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
gh --version
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
gh --version
```

- [Install Git](https://git-scm.com/downloads)

- [Install GitHub CLI](https://cli.github.com/)

**Expected:** Each command prints a version and no command-not-found error.

**Continue when:** Continue to GitHub authentication.

**If not:** Install only the missing tool from its official link, close the terminal, reopen it, and rerun this step.

### 4. Check the GitHub account

**Where:** The laptop or desktop in front of you

Run the status command before changing anything. Read the username shown under github.com.

**Open PowerShell on your Windows computer, then run:**

```powershell
gh auth status --active --hostname github.com
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
gh auth status --active --hostname github.com
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
gh auth status --active --hostname github.com
```

**Expected:** gh auth status names the intended GitHub username.

**Continue when:** Keep the working login and skip the next step.

**If not:** If no account or the wrong account is shown, use the next step. Never put a token in a repository URL.

### 5. Sign in only when needed

**Where:** The laptop or desktop in front of you

Run this only when the previous check showed no account or the wrong account. Enter the intended GitHub username. The command first tries to select an account already stored on this computer; otherwise it opens a new browser login. It does not remove another account.

**Open PowerShell on your Windows computer, then run:**

```powershell
& {
  $GitHubUser = Read-Host "Intended GitHub username"
  if ($GitHubUser -notmatch "^[A-Za-z0-9-]+$") { throw "STOP: invalid GitHub username" }
  gh auth switch --hostname github.com --user $GitHubUser
  if ($LASTEXITCODE -ne 0) { gh auth login --hostname github.com --git-protocol https --web }
  gh auth status --active --hostname github.com
}
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
(
printf 'Intended GitHub username: '; read -r github_user
case "$github_user" in ''|*[^A-Za-z0-9-]*) printf 'STOP: invalid GitHub username\n' >&2; exit 1;; esac
if ! gh auth switch --hostname github.com --user "$github_user"; then gh auth login --hostname github.com --git-protocol https --web; fi
gh auth status --active --hostname github.com
)
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
(
printf 'Intended GitHub username: '; read -r github_user
case "$github_user" in ''|*[^A-Za-z0-9-]*) printf 'STOP: invalid GitHub username\n' >&2; exit 1;; esac
if ! gh auth switch --hostname github.com --user "$github_user"; then gh auth login --hostname github.com --git-protocol https --web; fi
gh auth status --active --hostname github.com
)
```

**Expected:** The final status names the intended GitHub username.

**Continue when:** Continue to the commit identity.

**If not:** Stop before creating commits. Finish the browser login or use the help path for the exact error.

### 6. Inspect your commit identity

**Where:** The laptop or desktop in front of you

From the practice repository, print the effective name and email Git will attach to its commits and the configuration file each value comes from. A GitHub no-reply address is acceptable if you use it consistently.

**Open PowerShell on your Windows computer, then run:**

```powershell
git config --show-origin --get user.name
git config --show-origin --get user.email
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git config --show-origin --get user.name
git config --show-origin --get user.email
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git config --show-origin --get user.name
git config --show-origin --get user.email
```

**Expected:** Each line names a configuration source followed by a non-empty name or valid email address.

**Continue when:** Keep the existing values and continue.

**If not:** Set only the missing or incorrect values in the next step.

### 7. Set identity only if needed

**Where:** The laptop or desktop in front of you

Use this step only if the previous check was empty or wrong. Enter the author name and a verified GitHub email or GitHub-provided no-reply email. This sets the identity only in the practice repository, so it cannot silently change your other projects. The email identifies commits; it is not an ETH password or login.

**Open PowerShell on your Windows computer, then run:**

```powershell
& {
  $GitName = Read-Host "Commit author name"
  $GitEmail = Read-Host "GitHub email or no-reply email"
  if ([string]::IsNullOrWhiteSpace($GitName) -or $GitEmail -notmatch "^[^@\s]+@[^@\s]+$") { throw "STOP: invalid name or email" }
  git config --local user.name "$GitName"
  git config --local user.email "$GitEmail"
  git config --show-origin --get user.name
  git config --show-origin --get user.email
}
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
(
printf 'Commit author name: '; read -r git_name
printf 'GitHub email or no-reply email: '; read -r git_email
if [ -z "$git_name" ] || ! printf '%s\n' "$git_email" | grep -Eq '^[^[:space:]@]+@[^[:space:]@]+$'; then printf 'STOP: invalid name or email\n' >&2; exit 1; fi
git config --local user.name "$git_name"
git config --local user.email "$git_email"
git config --show-origin --get user.name
git config --show-origin --get user.email
)
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
(
printf 'Commit author name: '; read -r git_name
printf 'GitHub email or no-reply email: '; read -r git_email
if [ -z "$git_name" ] || ! printf '%s\n' "$git_email" | grep -Eq '^[^[:space:]@]+@[^[:space:]@]+$'; then printf 'STOP: invalid name or email\n' >&2; exit 1; fi
git config --local user.name "$git_name"
git config --local user.email "$git_email"
git config --show-origin --get user.name
git config --show-origin --get user.email
)
```

- [Open GitHub email settings](https://github.com/settings/emails)

**Expected:** The repeated check prints the values you entered and names .git/config as their source.

**Continue when:** Continue to the optional student benefit.

**If not:** Do not continue with an empty identity; correct the value or request help without including private information.

### 8. Students: verify your ETH email for GitHub Education

**Where:** This web page in your browser

Students: open GitHub email settings on the same account confirmed above. If a verified ETH email is already listed, keep it and continue. Otherwise add the ETH email, open GitHub's verification message in your ETH mailbox, and finish verification. Do not make the address public unless you choose to.

- [Verify GitHub email addresses](https://github.com/settings/emails)

**Expected:** Eligible students see their ETH address marked Verified. Staff and other ineligible learners skip this student-only step.

**Continue when:** Eligible students open the Education application in the next step. Everyone else skips it and continues to the repository check.

**If not:** Continue the manual Git route while resolving email verification. Never submit mailbox codes to the Passport.

### 9. Students: apply for GitHub Education

**Where:** This web page in your browser

GitHub Education is GitHub's student-verification program; approved accounts can see the current Student Developer Pack benefits. Students: open Education benefits on the same account. If GitHub already shows approved student benefits, keep them and skip the application. Otherwise select Start an application and submit only the proof requested through that GitHub page. Staff and learners who are not eligible skip this step. Approval may take time and does not block Git practice.

- [Open GitHub Education benefits](https://github.com/settings/education/benefits)

- [Read the official application steps](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student)

**Expected:** Eligible students see approved benefits or a pending application. Staff and other ineligible learners skip this student-only step.

**Continue when:** Continue now. If your route later includes the AI tool mission, that mission will check whether Copilot is available.

**If not:** Continue the manual Git route. Do not buy a product to pass this mission.

### 10. Inspect repository, branch, and remote

**Where:** The laptop or desktop in front of you

Confirm that you are inside the Passport practice clone, meaning its separate working copy on this computer. Check its practice branch and the saved online address called the remote. The usual remote name is origin. Its URL must contain no password or token.

**Open PowerShell on your Windows computer, then run:**

```powershell
git status --short --branch
git remote -v
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git status --short --branch
git remote -v
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git status --short --branch
git remote -v
```

**Expected:** The branch starts with practice/. The lines beginning with origin point to the expected GitHub repository and contain no password or token.

**Continue when:** Run Check my work.

**If not:** Return to Prepare practice folder; do not edit the remote until the mismatch is understood.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 80% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

If the editor is missing, install only the editor; do not clone again. If the
remote or branch is wrong, stop and run `gh passport doctor`. Do not delete the
folder, reset Git, replace SSH keys, or paste a token into the remote URL.
Use **Request help without posting secrets** on the Passport progress page if the
doctor's named recovery command does not resolve the problem. Submit one issue
without private information and return later; the reviewer does not need to be
online.

Useful references:

- [Git workflow](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/git_workflow.md)
- [VS Code](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/vscode.md)

## Understand Before Accepting AI Output

Do not let an AI assistant insert tokens, rewrite credential helpers, change
the remote, or switch branches without explaining the exact reason. Verify the
identity, remote, and branch yourself before accepting its claim of success.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
