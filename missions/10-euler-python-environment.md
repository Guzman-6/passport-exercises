# Mission: Create A Small Python Environment On Euler

## Outcome

Python is a programming language. Set up a small, separate interpreter and
package set, called a Python environment, directly on Euler. Make every
scheduled Python job select that environment explicitly.

## Concept

Python files are run by a program called an interpreter; packages add reusable
code. Your laptop and Euler are separate computers with different operating
systems and software. An environment created on one cannot be copied safely to
the other. Euler provides software modules, which select a maintained
application version for the current shell. A project environment then adds the
Python interpreter and packages needed by that project.

Recreate the environment on Euler from a reviewed definition, and make every Slurm batch script load its module and activate its environment before running Python.

On Euler, `$HOME` is the small private folder assigned to your account. This
mission uses a training folder there; it does not copy the environment from
your laptop.

## Worked Example

The training environment uses the documented Euler Python module, lives in the
dedicated training folder under `$HOME`, and prints `euler-python-env-ok` after
its path and version are verified.

Check these points:

- **Can a laptop `.venv` be copied to Euler?** No; recreate it on Euler.
- **Where does activation happen for a job?** Inside the Slurm script.

## Common Trap

Copying `.venv` from another machine, installing into a shared base
environment, or activating Python only in the login shell and assuming the job
will reproduce that setup.

## Your Action

Create or safely reuse one small Euler-native Python virtual environment and verify how a Slurm job activates it.

**Follow these steps in order.** Your laptop environment and Euler environment are separate. Run these steps on Euler after the SSH mission prints config-ok. This exercise creates no Slurm job and installs no project package.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Separate laptop and Euler software

**Where:** This web page in your browser

Python is a programming language, and an interpreter is the program that runs Python files. Your laptop and Euler are different computers. An Euler module selects a maintained software version in the current shell; a project environment adds that project's Python interpreter and packages. Both must be selected again inside each submitted batch job.

- [Read the Euler Python environment reference](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/python-environments.md)

**Expected:** You know why a laptop environment is not copied to Euler and why a job script activates its own environment.

**Continue when:** Connect to Euler with the tested alias.

**If not:** Read the linked Euler Python reference again. You do not need the laptop Python track unless it appears in your assigned route.

### 2. Connect to Euler

**Where:** The laptop or desktop in front of you

From the local terminal, connect with the verified euler alias. Run every later command in the Euler Bash shell that opens.

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

**Continue when:** Check the documented Python module.

**If not:** Return to the SSH mission. Do not run Euler commands in the local shell.

### 3. Check the Euler Python module

**Where:** The remote Euler computer after you connect from your computer

Load the dated Euler software stack used by this training release and verify the interpreter before creating anything. This affects only the current shell.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
set -eu
module purge
module load stack/2024-06 python/3.11.6
version="$(python --version 2>&1)"
printf '%s\n' "$version"
[ "$version" = "Python 3.11.6" ] || { printf 'STOP: expected Python 3.11.6, got %s\n' "$version" >&2; exit 1; }
printf 'module-python-ok\n'
)
```

- [Euler Python environment reference](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/python-environments.md)

**Expected:** The final two lines are Python 3.11.6 and module-python-ok.

**Continue when:** Inspect the dedicated environment path.

**If not:** Run module spider python and use the help path with its non-secret output. Do not guess a replacement module.

### 4. Inspect before creating

**Where:** The remote Euler computer after you connect from your computer

Inspect the exact training path. This checks ownership, activation, the selected Python, and both ways of starting pip. It keeps a valid environment and stops if an old moved environment or an incomplete directory is found.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
set -eu
umask 077
module purge
module load stack/2024-06 python/3.11.6
[ "$(python -c 'import platform; print(platform.python_version())')" = 3.11.6 ] || {
  printf 'STOP: the loaded module must provide Python 3.11.6.\n' >&2; exit 1
}
root="$HOME/passport-euler"
base="$root/venvs"
venv="$base/passport-python"
# <!-- passport-snippet:euler-environment-check -->
check_directories() {
  python - "$@" <<'PY'
import os, stat, sys
for name in sys.argv[1:]:
    info = os.lstat(name)
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o022:
        raise SystemExit("STOP: training paths must be real directories owned by you, without group/other write access.")
PY
}
verify_environment() (
  check_directories "$root" "$base" "$venv" "$venv/bin" || exit 1
  [ -f "$venv/pyvenv.cfg" ] && [ ! -L "$venv/pyvenv.cfg" ] &&
    [ -f "$venv/bin/activate" ] && [ ! -L "$venv/bin/activate" ] &&
    [ -x "$venv/bin/python" ] && [ -x "$venv/bin/pip" ] || {
    printf 'STOP: the training environment is incomplete or unsafe.\n' >&2; exit 1
  }
  . "$venv/bin/activate" || exit 1
  [ "${VIRTUAL_ENV:-}" = "$venv" ] && [ "$(command -v python)" = "$venv/bin/python" ] || {
    printf 'STOP: activation points to another location; use the training-environment recovery instructions.\n' >&2; exit 1
  }
  python - "$venv" <<'PY' || exit 1
import pathlib, platform, sys
import pip
expected = pathlib.Path(sys.argv[1])
assert pathlib.Path(sys.prefix).resolve() == expected.resolve(), "wrong environment prefix"
assert pathlib.Path(sys.executable).parent.resolve() == (expected / "bin").resolve(), "wrong interpreter directory"
assert pathlib.Path(sys.executable).name == "python", "wrong interpreter"
assert platform.python_version() == "3.11.6", "wrong Python version"
assert expected.resolve() in pathlib.Path(pip.__file__).resolve().parents, "pip belongs to another environment"
PY
  module_pip="$(python -m pip --version)" || exit 1
  entry_pip="$("$venv/bin/pip" --version)" || exit 1
  [ "$module_pip" = "$entry_pip" ] || { printf 'STOP: pip entrypoint uses another environment.\n' >&2; exit 1; }
  printf '%s\n' "$module_pip"
  deactivate
)
# <!-- /passport-snippet:euler-environment-check -->
for directory in "$root" "$base"; do
  if [ -e "$directory" ] || [ -L "$directory" ]; then check_directories "$directory"; fi
done
if [ ! -e "$venv" ] && [ ! -L "$venv" ]; then
  printf 'environment-target-available\n'
else
  [ ! -e "$venv/.passport-create-in-progress" ] || {
    printf 'STOP: a creation may still be running; do not move this environment. Ask lab IT if interrupted.\n' >&2; exit 1
  }
  verify_environment
  printf 'existing-environment-ok\n'
fi
)
```

- [Recover an affected training environment safely](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/python-environments.md#recover-a-broken-passport-training-environment)

**Expected:** The final line is environment-target-available or existing-environment-ok.

**Continue when:** Create only when absent, otherwise reuse it.

**If not:** Follow the linked recovery procedure only for this Passport training environment. Leave unfamiliar paths, shared permissions, and in-progress creations for lab IT to inspect.

### 5. Create or reuse the environment

**Where:** The remote Euler computer after you connect from your computer

Create the environment directly at its final path, after exclusively claiming an empty directory. A valid existing environment is checked and kept. A failed creation is retained for recovery; nothing is recursively deleted or overwritten.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
set -eu
umask 077
module purge
module load stack/2024-06 python/3.11.6
[ "$(python -c 'import platform; print(platform.python_version())')" = 3.11.6 ] || {
  printf 'STOP: the loaded module must provide Python 3.11.6.\n' >&2; exit 1
}
root="$HOME/passport-euler"
base="$root/venvs"
venv="$base/passport-python"
# <!-- passport-snippet:euler-environment-check -->
check_directories() {
  python - "$@" <<'PY'
import os, stat, sys
for name in sys.argv[1:]:
    info = os.lstat(name)
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o022:
        raise SystemExit("STOP: training paths must be real directories owned by you, without group/other write access.")
PY
}
verify_environment() (
  check_directories "$root" "$base" "$venv" "$venv/bin" || exit 1
  [ -f "$venv/pyvenv.cfg" ] && [ ! -L "$venv/pyvenv.cfg" ] &&
    [ -f "$venv/bin/activate" ] && [ ! -L "$venv/bin/activate" ] &&
    [ -x "$venv/bin/python" ] && [ -x "$venv/bin/pip" ] || {
    printf 'STOP: the training environment is incomplete or unsafe.\n' >&2; exit 1
  }
  . "$venv/bin/activate" || exit 1
  [ "${VIRTUAL_ENV:-}" = "$venv" ] && [ "$(command -v python)" = "$venv/bin/python" ] || {
    printf 'STOP: activation points to another location; use the training-environment recovery instructions.\n' >&2; exit 1
  }
  python - "$venv" <<'PY' || exit 1
import pathlib, platform, sys
import pip
expected = pathlib.Path(sys.argv[1])
assert pathlib.Path(sys.prefix).resolve() == expected.resolve(), "wrong environment prefix"
assert pathlib.Path(sys.executable).parent.resolve() == (expected / "bin").resolve(), "wrong interpreter directory"
assert pathlib.Path(sys.executable).name == "python", "wrong interpreter"
assert platform.python_version() == "3.11.6", "wrong Python version"
assert expected.resolve() in pathlib.Path(pip.__file__).resolve().parents, "pip belongs to another environment"
PY
  module_pip="$(python -m pip --version)" || exit 1
  entry_pip="$("$venv/bin/pip" --version)" || exit 1
  [ "$module_pip" = "$entry_pip" ] || { printf 'STOP: pip entrypoint uses another environment.\n' >&2; exit 1; }
  printf '%s\n' "$module_pip"
  deactivate
)
# <!-- /passport-snippet:euler-environment-check -->
for directory in "$root" "$base"; do
  if [ ! -e "$directory" ] && [ ! -L "$directory" ]; then
    mkdir -m 700 -- "$directory" || { printf 'STOP: a training parent appeared concurrently; inspect again.\n' >&2; exit 1; }
  fi
  check_directories "$directory"
done
if [ -e "$venv" ] || [ -L "$venv" ]; then
  [ ! -e "$venv/.passport-create-in-progress" ] || {
    printf 'STOP: a creation may still be running; do not move this environment. Ask lab IT if interrupted.\n' >&2; exit 1
  }
  verify_environment
  printf 'existing-environment-kept\n'
else
  # Claim the final directory exclusively; never run venv over an existing target.
  mkdir -m 700 -- "$venv" || { printf 'STOP: the target appeared concurrently; inspect again.\n' >&2; exit 1; }
  mkdir -- "$venv/.passport-create-in-progress"
  trap 'rmdir -- "$venv/.passport-create-in-progress"' EXIT
  trap 'exit 1' HUP INT TERM
  printf 'passport-python-training-v1\n' > "$venv/.passport-training-environment"
  # venv records absolute paths. Create and test it at its permanent location.
  python -m venv "$venv" || {
    printf 'STOP: creation failed; the partial training directory was kept for safe recovery.\n' >&2; exit 1
  }
  verify_environment
  printf 'created-environment-ok\n'
fi
)
```

- [Recover an affected training environment safely](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/python-environments.md#recover-a-broken-passport-training-environment)

**Expected:** The command prints existing-environment-kept or created-environment-ok and does not overwrite an existing path.

**Continue when:** Activate and verify the exact interpreter.

**If not:** Keep the first error and follow the linked recovery procedure. Do not rerun venv over an existing target, use sudo, or install into base.

### 6. Verify the active interpreter

**Where:** The remote Euler computer after you connect from your computer

Activate the training environment in this temporary shell and check its activation path, selected interpreter, Python version, and pip entrypoint. The success marker appears only after every check passes. Enter only that marker in the Passport.

**After SSH connects to Euler, run this in the same text window:**

```bash
(
set -eu
umask 077
module purge
module load stack/2024-06 python/3.11.6
[ "$(python -c 'import platform; print(platform.python_version())')" = 3.11.6 ] || {
  printf 'STOP: the loaded module must provide Python 3.11.6.\n' >&2; exit 1
}
root="$HOME/passport-euler"
base="$root/venvs"
venv="$base/passport-python"
# <!-- passport-snippet:euler-environment-check -->
check_directories() {
  python - "$@" <<'PY'
import os, stat, sys
for name in sys.argv[1:]:
    info = os.lstat(name)
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o022:
        raise SystemExit("STOP: training paths must be real directories owned by you, without group/other write access.")
PY
}
verify_environment() (
  check_directories "$root" "$base" "$venv" "$venv/bin" || exit 1
  [ -f "$venv/pyvenv.cfg" ] && [ ! -L "$venv/pyvenv.cfg" ] &&
    [ -f "$venv/bin/activate" ] && [ ! -L "$venv/bin/activate" ] &&
    [ -x "$venv/bin/python" ] && [ -x "$venv/bin/pip" ] || {
    printf 'STOP: the training environment is incomplete or unsafe.\n' >&2; exit 1
  }
  . "$venv/bin/activate" || exit 1
  [ "${VIRTUAL_ENV:-}" = "$venv" ] && [ "$(command -v python)" = "$venv/bin/python" ] || {
    printf 'STOP: activation points to another location; use the training-environment recovery instructions.\n' >&2; exit 1
  }
  python - "$venv" <<'PY' || exit 1
import pathlib, platform, sys
import pip
expected = pathlib.Path(sys.argv[1])
assert pathlib.Path(sys.prefix).resolve() == expected.resolve(), "wrong environment prefix"
assert pathlib.Path(sys.executable).parent.resolve() == (expected / "bin").resolve(), "wrong interpreter directory"
assert pathlib.Path(sys.executable).name == "python", "wrong interpreter"
assert platform.python_version() == "3.11.6", "wrong Python version"
assert expected.resolve() in pathlib.Path(pip.__file__).resolve().parents, "pip belongs to another environment"
PY
  module_pip="$(python -m pip --version)" || exit 1
  entry_pip="$("$venv/bin/pip" --version)" || exit 1
  [ "$module_pip" = "$entry_pip" ] || { printf 'STOP: pip entrypoint uses another environment.\n' >&2; exit 1; }
  printf '%s\n' "$module_pip"
  deactivate
)
# <!-- /passport-snippet:euler-environment-check -->
[ ! -e "$venv/.passport-create-in-progress" ] || {
  printf 'STOP: a creation may still be running; wait for it or ask lab IT.\n' >&2; exit 1
}
verify_environment
printf 'python_environment=passport-python\neuler-python-env-ok\n'
)
```

- [Recover an affected training environment safely](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/python-environments.md#recover-a-broken-passport-training-environment)

**Expected:** The output includes python_environment=passport-python, euler-python-env-ok, and pip from the same environment.

**Continue when:** Learn where these lines belong in a job.

**If not:** Use the linked recovery procedure if this is the training environment affected by the earlier recipe. Do not copy a laptop environment or change shell startup files.

### 7. Put setup inside the Slurm script

**Where:** The remote Euler computer after you connect from your computer

Read this batch-script fragment. Do not run a workload on the login node. Every Python job must load its module and activate its environment inside the submitted script before the Python command.

**Put this in the named Bash file:**

```bash
module purge
module load stack/2024-06 python/3.11.6
. "$HOME/passport-euler/venvs/passport-python/bin/activate"
python your_script.py
```

**Expected:** You can identify the three environment lines that must precede the program in a Slurm script.

**Continue when:** Complete the questions and confirmation.

**If not:** Do not rely on a login-shell activation to define an unattended job.

### 8. Confirm the safe marker

**Where:** The laptop or desktop in front of you

Return to the local Passport, enter only euler-python-env-ok, complete the questions, and run Check my work.

**Expected:** The local check accepts the exact environment marker and all three safety decisions.

**Continue when:** Submit once and continue to the first CPU job.

**If not:** Repeat only the verification step on Euler; do not recreate a working environment.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. The automatic check confirms the exact
safe marker printed by the Euler environment command. A score of 100% is
required, and every safety-critical question must be correct.

## If Blocked

Keep the first non-secret error. Use `module spider python` if the dated module
cannot be loaded. Do not use `sudo`, delete an existing environment, copy a
laptop environment, or install into `base`. See the
[Euler Python environment reference](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/reference/euler/python-environments.md).

## Understand Before Accepting AI Output

Personally verify the Python version, environment path, and the activation
lines in the batch script. An agent must not choose a different module, delete
an environment, or install packages without your review.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
