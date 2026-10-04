# Mission: Complete A Manual Pull Request Loop

## Outcome

Prepare one small change your colleague can understand, and explain exactly
which version reaches GitHub for review. Keep the shared `main` branch unchanged.

## Concept

### What exactly will your colleague receive?

You will add a reminder to a fictional project note, then open a draft
PR that a colleague could review. You do not need to contact anyone.
Follow the change through three places:

- Your file: the working tree is the folder you edit. Staging selects the
  saved content for the next commit.
- Your history: a commit records that selection on your computer. Your
  practice branch keeps it separate from `main`.
- Your review page: pushing sends your commits to GitHub. A pull request
  (PR) compares your branch with `main` for someone to review.

Leave the PR in draft: it is not ready to merge. The Conventional Commit
format is explained in step 7.

## Learning Challenge

<span id="step-terms"></span>

### What will this commit contain?

Imagine editing `meeting-note.md`. You add Monday, save, and stage the file.
Then you add Room 204 and save again, without staging again.

If you commit now, will it include Monday, Room 204, or both? Why?
Think it through before opening the explanation. No answer to submit.

## Worked Example

<details class="learning-explanation">
<summary>See the three versions</summary>

| Where the version is | What it contains |
| --- | --- |
| Last commit | Original note |
| Staging area: selected for the next commit | Original note + Monday |
| Working tree: saved in your editor | Original note + Monday + Room 204 |

The commit includes Monday, but not Room 204. Staging captures the saved
content at that moment; saving again does not update the selection.
To include the room, you would stage the newer version and review it.

You will inspect two diffs: your edit, then the selection for the commit.
Do not create `meeting-note.md`; it is only an example.

</details>

Optional: [another explanation of staging](https://www.w3schools.com/git/git_staging_environment.asp).
Read just that page, then return here; you do not need its Next links or commands.

## Common Trap

Select the named practice file, not every file with `git add .`.
**Keep the PR in draft; do not merge it.** The Passport handles its
background submission separately.

## Your Action

Make one small manual change, review both diffs, create a Conventional Commit, push it, and open a draft pull request.

**Follow these steps in order.** Work in the prepared practice folder, using the same terminal throughout. Leave the PR open in draft.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Open the practice folder

**Where:** The laptop or desktop in front of you

Click Prepare practice folder. Run its enter-folder command in your terminal, then keep that terminal in this folder.

**Expected:** Your terminal is in the exact folder shown by preparation, on its practice branch.

**Continue when:** The prepared copy gives you a practice branch without changing another project. Read its task before choosing any file to edit.

**If not:** Retry the preparation or run gh passport doctor. Do not create another clone.

### 2. Inspect before editing

**Where:** The laptop or desktop in front of you

Run these commands to read the task and note. Stop if the branch differs from the prepared practice branch or unexpected edits appear.

**Open PowerShell on your Windows computer, then run:**

```powershell
git status --short --branch
Get-Content -LiteralPath workspace/manual_task/README.md
Get-Content -LiteralPath workspace/manual_task/project-note.md
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git status --short --branch
sed -n '1,160p' workspace/manual_task/README.md
sed -n '1,160p' workspace/manual_task/project-note.md
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git status --short --branch
sed -n '1,160p' workspace/manual_task/README.md
sed -n '1,160p' workspace/manual_task/project-note.md
```

**Expected:** The branch starts with practice/. No modified file is listed. The task names project-note.md as the file to edit.

**Continue when:** You know the starting version and the scope of the change. The task README is an instruction, not a file to modify.

**If not:** Stop if the branch is different or changes already exist. Inspect them before editing; do not reset the repository.

### 3. Open the same folder in your editor

**Where:** The laptop or desktop in front of you

In VS Code, choose File > Open Folder and select the exact practice-folder path shown by the Passport. Open workspace/manual_task/project-note.md. Edit it yourself, without an AI agent.

- [Download VS Code](https://code.visualstudio.com/download)

**Expected:** Your editor shows project-note.md inside the prepared practice folder.

**Continue when:** Your editor and terminal point to the same practice folder, so the file you save is the file Git will inspect.

**If not:** Compare the editor folder with the preparation path. If needed, install VS Code using the download link. Do not edit the handbook or a research repository.

### 4. Write a reminder your colleague can use

**Where:** The laptop or desktop in front of you

In workspace/manual_task/project-note.md, add a ## Verification heading and one short sentence in your own words about reviewing the staged diff before publishing. Include the terms staged diff and review. Save only this file. Put the text in your editor, not the terminal.

**Put this in the named Markdown file:**

```markdown
## Verification

The staged diff must be reviewed before publishing.
```

**Expected:** The saved note has your heading and reminder. No other file has changed.

**Continue when:** Saving updates your working file. The next diff lets you decide whether these are the lines you want your colleague to receive.

**If not:** Correct only the mistaken lines in your editor. Do not reset or delete the practice folder.

### 5. Read your change as a reviewer

**Where:** The laptop or desktop in front of you

Read every added (+) and removed (-) line. Is this the change you intended? Fix anything unexpected in the editor before staging.

**Open PowerShell on your Windows computer, then run:**

```powershell
git status --short
git diff -- workspace/manual_task/project-note.md
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git status --short
git diff -- workspace/manual_task/project-note.md
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git status --short
git diff -- workspace/manual_task/project-note.md
```

**Expected:** Only workspace/manual_task/project-note.md is modified. Its diff shows your heading and reminder, without unrelated changes or private information.

**Continue when:** A diff compares two versions. Here, git diff compares your saved file with the staged version. Next, select only the named file.

**If not:** Correct unexpected content before staging. If another file changed, understand why before continuing.

### 6. What will this commit contain?

**Where:** The laptop or desktop in front of you

Run the block to stage the note, then read the staged diff. Confirm every line before committing. If you edit again, stage and review the newer version.

**Open PowerShell on your Windows computer, then run:**

```powershell
git add -- workspace/manual_task/project-note.md
git diff --cached --check
git diff --cached
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git add -- workspace/manual_task/project-note.md
git diff --cached --check
git diff --cached
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git add -- workspace/manual_task/project-note.md
git diff --cached --check
git diff --cached
```

- [Optional: exact-file staging explained](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/git_workflow.md#staging-review)

**Expected:** The staged diff contains only the intended note change. The whitespace check prints nothing when it passes.

**Continue when:** git add selects the current saved content. git diff --cached compares that selection with the last commit; --check checks whitespace. The selection is what your next commit will record.

**If not:** For an unintended staged path, use git restore --staged on that path to keep the edit but remove it from the selection. Correct and review again.

### 7. Record the version you chose

**Where:** The laptop or desktop in front of you

Will your colleague see this new commit on GitHub? Think about that, then run the command.

**Open PowerShell on your Windows computer, then run:**

```powershell
git commit -m "docs(practice): explain staged diff review"
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git commit -m "docs(practice): explain staged diff review"
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git commit -m "docs(practice): explain staged diff review"
```

**Expected:** Git prints a new commit with the subject docs(practice): explain staged diff review.

**Continue when:** The commit is recorded on your computer. It reaches GitHub when you push. The Conventional Commit format is type(scope): summary: docs means documentation, practice names the area, and the summary describes the change.

**If not:** Read the first Git error and ask for help if needed. Do not force the operation or skip hooks.

### 8. Push and open a draft pull request

**Where:** The laptop or desktop in front of you

Which command shares your commit, and which asks for review? Run the prepared git push command, then its gh pr create command, one at a time. Keep --draft. Leave the PR open in draft; do not merge it.

**Expected:** One open draft PR proposes your practice branch to main. Opening it has not merged your change into main.

**Continue when:** Pushing sends your commits to your GitHub branch. A PR compares that branch with main for review. Opening it does not change main.

**If not:** If a PR already exists, inspect it with gh pr status. Do not create a second one or force-push.

### 9. Review what GitHub received

**Where:** The laptop or desktop in front of you

Run both commands to open your PR; the local Passport fills in your fork and branch. Do not run gh repo set-default. In Files changed, check that the reminder makes sense and the diff matches your reviewed edit.

**Open PowerShell on your Windows computer, then run:**

```powershell
gh pr status --repo {{fork_repository}}
gh pr view {{practice_branch}} --repo {{fork_repository}} --web
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
gh pr status --repo {{fork_repository}}
gh pr view {{practice_branch}} --repo {{fork_repository}} --web
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
gh pr status --repo {{fork_repository}}
gh pr view {{practice_branch}} --repo {{fork_repository}} --web
```

**Expected:** You are the author; your practice branch targets main. Only project-note.md changed, with your reviewed reminder and commit subject. Leave the PR open in draft; do not merge it.

**Continue when:** Compare your saved note, recorded commit and PR diff: they should show the same reminder. You can now use Check my work, then Submit lesson.

**If not:** If no PR appears, return to Push and open a draft pull request. Otherwise correct the same branch and push again. Do not configure a default repository, create a second PR, merge, or delete the existing PR.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Try the two practice situations, then answer the two lesson questions.
Review the fictional file you will submit,
and confirm the results you personally observed. **Check my work** verifies
the practice branch, the bounded change, the commit and the draft PR. Passing
this check enables **Submit lesson**. Completion is recorded only when the
automatic GitHub check passes. Both lesson answers and every required check
must pass; you can retry with feedback.

## Learning Check

### Practise

Try an answer before opening the explanation. These questions are for
practice; they do not affect your progress.

1. You staged your note, then saved one more correction. You want that correction in the next commit. What should you do before committing?

   - Commit now; saving includes the correction.
   - Stage the note again, then review the staged diff.
   - Push the branch to include the saved correction.

<details class="learning-explanation">
<summary>See an explanation</summary>

Stage the note again to select the newer saved version, then review git diff --cached. Saving alone does not update the selection; pushing sends existing commits to GitHub.

</details>

2. You commit a fix on your practice branch but have not pushed. Your colleague looks for that commit on GitHub. What must happen before they can see it there?

   - Open a draft PR so GitHub uploads the local commit.
   - Make another local commit to update the GitHub copy.
   - Push the practice branch so GitHub receives the commit.

<details class="learning-explanation">
<summary>See an explanation</summary>

Committing records the change on your computer; pushing sends it to GitHub. A draft PR gives your colleague a review page for a pushed branch. Neither action merges it into main.

</details>

## If Blocked

Do not use `git reset --hard`, broad deletion, or force push as a first repair.
Preserve `git status`, the current branch, and the diff, then use the
[first safe PR lab](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/first-safe-pr.md#safe-recovery) recovery section or ask
for help through the non-secret dashboard issue form.

Useful references:

- [PR recovery](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/first-safe-pr.md#safe-recovery): read the matching failure, then return here.
- [Git recovery](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/git_workflow.md#troubleshooting): use only the row matching your error.

## Understand Before Accepting AI Output

This mission is deliberately manual. An agent may explain a Git concept but
must not perform the change, invent test output, or choose files to stage.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
