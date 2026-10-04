# Mission: Make And Verify A Reproducible Python Change

## Outcome

Expose a small calculation bug with a test, correct it, and inspect the two-file change.

## Concept

A reproducible change includes the code, dependencies and command another
person needs to repeat the check. A test is code that compares an observed
result with an expected one. A Git diff shows which lines changed.

The fictional function calculates total memory from CPU count and memory per
CPU. The existing test uses one CPU. It passes even though the function is
incomplete: a green test only covers the case it ran.

## Learning Challenge

Read the function before editing. Why can its one-CPU example pass while a
four-CPU example fails? Make a prediction, then use the regression test to
check it. This is a guided correction; the current verifier requires the
provided assertion and return form.

## Worked Example

<details>
<summary>How to read the intended failure</summary>

The assertion calls the function with four CPUs and 3 GiB per CPU and compares
its result with 12. Before the fix it observes 3. That mismatch is the bug this
exercise targets. An import, syntax or indentation error must be repaired
before it can demonstrate the same behavior failure.

</details>

## Common Trap

Changing the source before confirming that the regression test exposes the
bug. Keep the test and its expected value; do not weaken it to get green output.

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

Read passport_example.py and tests/test_passport_example.py. The function should calculate total requested memory. Before opening a model, explain why the one-CPU test passes and predict what changes with four CPUs at 3 GiB per CPU. If inputs and return values are new, read one function-and-return example at the optional link, then come back here; the rest of the Python course is not required.

- [Optional: function inputs and return values](https://www.w3schools.com/python/python_functions.asp)

**Expected:** You can compare the function inputs, its return value and the value the test expects.

**Continue when:** With one CPU, returning memory per CPU happens to give the correct total. More than one CPU exposes the missing multiplication. An assertion compares observed behavior with the expected result.

**If not:** Re-read the function inputs and do not edit by trial and error.

### 4. Add and run the regression test

**Where:** The laptop or desktop in front of you

In tests/test_passport_example.py, add the model method inside TotalMemoryTests at the same indentation as test_one_cpu. This guided exercise requires this assertion. Save and run the suite before changing the function. An AssertionError comparing values is the intended failure; an import or indentation error is a different problem.

<details>
<summary>Show the required regression method</summary>

**Put this in the named Python file:**

```python
def test_multiple_cpus(self) -> None:
    self.assertEqual(total_memory_gib(4, 3), 12)
```

</details>

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

In passport_example.py, change only the return calculation. Predict it first, then compare with the required model. Keep the validation for non-positive inputs: this guided exercise checks the shown form, rather than every possible correct implementation.

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

Stay in workspace/python_project. Review the changed files in this folder. Git diff shows line-by-line edits; . means the current folder. Check that source and tests changed, with no environment, cache or whitespace errors.

**Open PowerShell on your Windows computer, then run:**

```powershell
git status --short
git diff --check
git diff -- .
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git status --short
git diff --check
git diff -- .
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git status --short
git diff --check
git diff -- .
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

## Learning Check

### Practise

Try an answer before opening the explanation. These questions are for
practice; they do not affect your progress.

1. The test for one CPU passes. What does that establish?

   - The function works for every positive CPU count.
   - That one input worked; a multi-CPU case may still reveal a bug.
   - The environment needs reinstalling before testing another input.

<details class="learning-explanation">
<summary>See an explanation</summary>

A passing test supports the case it exercises. With one CPU, the incomplete return accidentally matches the total. The multi-CPU regression distinguishes the missing behavior.

</details>

2. Before the fix, the new test reports ModuleNotFoundError rather than comparing 3 and 12. What next?

   - Change the multiplication now; any red output is sufficient.
   - Delete the import so the suite passes.
   - Repair the folder/import or environment first, then reproduce the intended assertion failure.

<details class="learning-explanation">
<summary>See an explanation</summary>

A failed import means the test has not reached the behavior comparison. Keep the implementation unchanged until the intended regression actually runs and fails.

</details>

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
