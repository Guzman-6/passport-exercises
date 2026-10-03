# Mission: Make And Verify A Reproducible Python Change

## Outcome

Reproduce a small Python bug with a test, fix it, rerun all tests, and inspect
exactly which lines changed.

## Concept

A reproducible change can be checked again by another person from the recorded code, dependencies, inputs, configuration, and command. A test is code that checks an expected behavior and reports success or failure.

For a bug fix, first run a test that exposes the missing behavior, then change the implementation, rerun all declared tests, and review the Git diff. “It works on my machine” alone is not evidence.

## Worked Example

The hidden behavior check and the visible tests pass without committing the environment or generated files.

Check these points:

- **When may you record that tests passed?** After you personally ran the named test command and observed success.
- **What belongs in the commit?** Source, tests, and declared dependencies needed to reproduce the change.

## Common Trap

Accepting a passing command from an agent without personally running it in the intended environment.

## Your Action

Reproduce a Python bug, add a regression test, make the smallest fix, and rerun the tests in the project Conda environment.

**Follow these steps in order.** A test must fail for the missing behavior before the implementation is changed, then pass after the correction.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Open the Python practice project

**Where:** The laptop or desktop in front of you

Press Prepare practice folder in this step and run the displayed enter-folder command. Then activate ./.venv and move to workspace/python_project with the command below.

**Open PowerShell on your Windows computer, then run:**

```powershell
conda activate ./.venv
cd workspace/python_project
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
conda activate ./.venv
cd workspace/python_project
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
conda activate ./.venv
cd workspace/python_project
```

**Expected:** The terminal is in workspace/python_project and uses the project environment.

**Continue when:** Run the unchanged baseline.

**If not:** Return to the environment mission; do not use a different Python.

### 2. Run the baseline test

**Where:** The laptop or desktop in front of you

Run the complete declared test command before editing.

**Open PowerShell on your Windows computer, then run:**

```powershell
python -m unittest discover -s tests -v
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
python -m unittest discover -s tests -v
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
python -m unittest discover -s tests -v
```

**Expected:** The existing one-CPU test passes.

**Continue when:** Read the source and existing test.

**If not:** Stop and repair the environment or baseline before changing code.

### 3. Explain the missing behavior

**Where:** The laptop or desktop in front of you

Read passport_example.py and tests/test_passport_example.py. Work out the expected total for four CPUs at 3 GiB per CPU.

**Expected:** You expect 12 GiB and can explain why the current function returns the wrong value.

**Continue when:** Add the regression test first.

**If not:** Re-read the function inputs and do not edit by trial and error.

### 4. Add and run the regression test

**Where:** The laptop or desktop in front of you

Open tests/test_passport_example.py. Add the shown method inside the TotalMemoryTests class, save the file, then run the suite before fixing the function.

**Put this in the named Python file:**

```python
def test_multiple_cpus(self) -> None:
    self.assertEqual(total_memory_gib(4, 3), 12)
```

**Open PowerShell on your Windows computer, then run:**

```powershell
python -m unittest discover -s tests -v
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
python -m unittest discover -s tests -v
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
python -m unittest discover -s tests -v
```

**Expected:** The new test fails for the expected 3-versus-12 behavior.

**Continue when:** Make the smallest implementation fix.

**If not:** If the test passes or fails for another reason, correct the test before editing the implementation.

### 5. Correct the implementation

**Where:** The laptop or desktop in front of you

Open passport_example.py. Keep the existing input validation and replace only the current return line with the line shown below.

**Put this in the named Python file:**

```python
return cpus * memory_per_cpu_gib
```

**Expected:** The function returns the total while invalid non-positive inputs still raise ValueError.

**Continue when:** Run the complete suite again.

**If not:** Revert only the mistaken edit in your editor and return to the failing test.

### 6. Run the complete tests

**Where:** The laptop or desktop in front of you

Run the same declared command in the same activated environment.

**Open PowerShell on your Windows computer, then run:**

```powershell
python -m unittest discover -s tests -v
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
python -m unittest discover -s tests -v
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
python -m unittest discover -s tests -v
```

**Expected:** All visible tests pass.

**Continue when:** Review repository state and diff.

**If not:** Read the first failing traceback and fix its cause; do not delete or weaken a test.

### 7. Review the reproducible change

**Where:** The laptop or desktop in front of you

Confirm that only source and tests changed, no environment or cache is tracked, and the diff has no whitespace errors.

**Open PowerShell on your Windows computer, then run:**

```powershell
git status --short
git diff --check
git diff -- workspace/python_project
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git status --short
git diff --check
git diff -- workspace/python_project
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git status --short
git diff --check
git diff -- workspace/python_project
```

**Expected:** The diff contains the intended source and regression test only.

**Continue when:** Run Check my work.

**If not:** Remove generated files from the change and review again.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 80% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

Return to the last passing baseline, inspect the first failing assertion, and
reduce the problem. Do not delete tests, broaden tolerances, or install random
packages merely to make the check green.

Useful references:

- [Reproducible Python](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/reproducible-python.md)
- [Code contributor track](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/tracks/code-contributor.md)

## Understand Before Accepting AI Output

If an agent explains the failure, independently inspect the affected source and
test. Do not accept a test that only repeats the implementation or a claim that
was not personally run.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
