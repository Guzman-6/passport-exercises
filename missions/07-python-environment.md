# Mission: Create A Reproducible Python Environment

## Outcome

Python is a programming language. Create or safely reuse the practice project's Python environment and verify
which interpreter runs its files.

## Concept

A Python interpreter runs Python files.
Conda manages environments and creates separate installations; Miniforge provides Conda.
.gitignore tells Git not to record the named local folder.

| Item | Role in this project |
| --- | --- |
| `environment.yml` | Shared recipe: interpreter and dependencies to recreate |
| `.venv` | This computer's installation; `.gitignore` excludes it from Git |
| Active interpreter | The program this terminal actually runs as `python` |

Keep project packages out of Conda's shared `base` and the operating-system
Python. A matching version alone does not prove the right interpreter.

## Learning Challenge

Two terminals can both print Python 3.11 and use different installations.
What other observation would distinguish them? The verification step prints
that evidence. No completed environment needs rebuilding for this lesson update.

## Worked Example

<details>
<summary>Keep the two terminal windows straight</summary>

The server terminal keeps the local Passport running. Use a separate command
terminal for installation and practice. After installation or shell setup,
reopen only the command terminal, return using the Practice folder ready path,
and reactivate the project environment. A new shell loads setup changes; it
does not automatically return to your project or inherit activation.

</details>

## Common Trap

Reinstalling Conda because an old terminal cannot find it, or deleting an
existing .venv before identifying it. Follow the checks before changing anything.

## Your Action

Install or verify Miniforge, create the project environment from environment.yml, and prove that Git ignores .venv.

**Follow these steps in order.** Do not install packages into Conda's shared base environment or into the Python installation used by the operating system. Keep an existing .venv folder until you have identified what it contains.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Know what the Python environment contains

**Where:** This web page in your browser

Compare the three items in the model above: the shared recipe, this computer's installation, and the interpreter selected in this terminal. You will verify their relationship with paths, not just a prompt label.

**Expected:** You can distinguish the versioned environment.yml definition from the local .venv installation.

**Continue when:** Prepare the Python practice folder.

**If not:** Do not install packages globally or into base until the terms are clear.

### 2. Prepare the Python practice folder

**Where:** The laptop or desktop in front of you

Press Prepare practice folder in this step and run the displayed enter-folder command in your command terminal. Keep this page open: the Practice folder ready box shows your exact folder path and a Copy button for returning there later. After a page reload, press Prepare practice folder again to display the same folder; the launcher reuses it. The repository root is its top-level folder, containing environment.yml and .gitignore. Do not use the hidden .transport folder.

**Expected:** The practice repository and practice branch are active.

**Continue when:** Check whether Conda is already available.

**If not:** Do not create another clone; run gh passport doctor.

### 3. Check Conda

**Where:** The laptop or desktop in front of you

Run both checks. If both work, keep this installation and skip recovery and installation. If Conda was installed while this command terminal was open, wait for installation to finish and retry in a new command terminal; keep the separate Passport server terminal open.

**Open PowerShell on your Windows computer, then run:**

```powershell
conda --version
conda info --base
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
conda --version
conda info --base
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
conda --version
conda info --base
```

**Expected:** Conda prints a version and the base path of the installation that will manage this project environment.

**Continue when:** Skip installation and read the environment definition.

**If not:** If a newly opened command terminal still cannot find Conda, continue to Recover an existing Conda installation. Do not download another copy. If Self Service or IT says Conda is installed, keep that installation and ask IT for its supported terminal setup if recovery cannot find it.

### 4. Recover an existing Conda installation

**Where:** The laptop or desktop in front of you

Only after Conda is still missing in a new command terminal, inspect common installation folders with the helper. It deletes nothing and initializes the shell only if it finds exactly one installation. A managed installation elsewhere needs IT help. Windows: check for an existing Miniforge, Miniconda or Anaconda Prompt in the Start menu first.

<details>
<summary>Show the existing-installation recovery</summary>

**Open PowerShell on your Windows computer, then run:**

```powershell
& {
  $Candidates = @(
    (Join-Path $env:USERPROFILE "miniforge3\Scripts\conda.exe"),
    (Join-Path $env:USERPROFILE "mambaforge\Scripts\conda.exe"),
    (Join-Path $env:USERPROFILE "miniconda3\Scripts\conda.exe"),
    (Join-Path $env:USERPROFILE "anaconda3\Scripts\conda.exe"),
    (Join-Path $env:LOCALAPPDATA "miniforge3\Scripts\conda.exe"),
    (Join-Path $env:ProgramData "miniforge3\Scripts\conda.exe")
  )
  $Found = @($Candidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -Unique)
  $Found | ForEach-Object { Write-Host "found: $_" }
  if ($Found.Count -gt 1) { throw "STOP: multiple Conda installations found; choose one with setup help" }
  if ($Found.Count -eq 1) {
    $CondaExe = $Found[0]
    & $CondaExe --version
    & $CondaExe init powershell
    if ($LASTEXITCODE -ne 0) { throw "STOP: Conda initialization failed" }
    Write-Host "existing-conda-initialized"
  } else {
    Write-Host "no-common-conda-installation"
  }
}
```

</details>

<details>
<summary>Show the existing-installation recovery</summary>

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
(
found=''; count=0
for candidate in "$HOME/miniforge3/bin/conda" "$HOME/mambaforge/bin/conda" "$HOME/miniconda3/bin/conda" "$HOME/anaconda3/bin/conda"; do
  if [ -x "$candidate" ]; then found="$candidate"; count=$((count + 1)); printf 'found: %s\n' "$candidate"; fi
done
if [ "$count" -gt 1 ]; then printf 'STOP: multiple Conda installations found; choose one with setup help\n' >&2; exit 1; fi
if [ "$count" -eq 1 ]; then
  "$found" --version
  "$found" init zsh || { printf 'STOP: Conda initialization failed\n' >&2; exit 1; }
  printf 'existing-conda-initialized\n'
else
  printf 'no-common-conda-installation\n'
fi
)
```

</details>

<details>
<summary>Show the existing-installation recovery</summary>

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
(
found=''; count=0
for candidate in "$HOME/miniforge3/bin/conda" "$HOME/mambaforge/bin/conda" "$HOME/miniconda3/bin/conda" "$HOME/anaconda3/bin/conda"; do
  if [ -x "$candidate" ]; then found="$candidate"; count=$((count + 1)); printf 'found: %s\n' "$candidate"; fi
done
if [ "$count" -gt 1 ]; then printf 'STOP: multiple Conda installations found; choose one with setup help\n' >&2; exit 1; fi
if [ "$count" -eq 1 ]; then
  "$found" --version
  "$found" init bash || { printf 'STOP: Conda initialization failed\n' >&2; exit 1; }
  printf 'existing-conda-initialized\n'
else
  printf 'no-common-conda-installation\n'
fi
)
```

</details>

**Expected:** The final line is existing-conda-initialized or no-common-conda-installation.

**Continue when:** After existing-conda-initialized, skip installation and continue at Reopen and recheck Conda. After no-common-conda-installation, install only if Self Service, IT and any Start-menu Conda prompt do not indicate an existing installation. The check searches common folders only; an unlisted managed installation needs IT help, not a second copy.

**If not:** If more than one installation is listed, or a Start-menu Conda prompt exists at another path, stop and request help without including private information. Do not uninstall, rename, or overwrite any installation.

### 5. Install Miniforge on Windows only if needed

**Where:** The laptop or desktop in front of you

Skip this step if Self Service or IT already installed Conda; request its supported setup if needed. Run this step only after the recovery check printed no-common-conda-installation and no Conda prompt exists in the Start menu. Download the Windows x86-64 installer from the official page, run it for Just Me, keep the default personal installation folder and Start Menu shortcut, and leave Add Miniforge to PATH disabled. Open Miniforge Prompt from the Start menu, run conda --version, then run conda init powershell once. Close only that Miniforge Prompt, keep the terminal running the Passport open, and open a new PowerShell window.

- [Open official Miniforge installers](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe)

**Expected:** conda --version works in Miniforge Prompt without replacing another Conda installation.

**Continue when:** Continue at Reopen and recheck Conda.

**If not:** Stop if an existing installation or destination is reported; diagnose it instead of overwriting it.

### 6. Install Miniforge on macOS only if needed

**Where:** The laptop or desktop in front of you

Skip this step if Self Service or IT already installed Conda; request its supported setup if needed. Run this step only after the recovery check printed no-common-conda-installation. The block downloads the versioned Miniforge 26.5.3-0 installer for this Mac and its published SHA-256 checksum into a temporary directory. It verifies the checksum before starting the interactive installer. Answer yes when asked to initialize zsh.

<details>
<summary>Show the installer only after the absence checks passed</summary>

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

<!-- passport-snippet:miniforge-macos-installer -->
```zsh
(
set -eu
tag="26.5.3-0"
temporary="$(mktemp -d "${TMPDIR:-/tmp}/ideal-passport-miniforge.XXXXXX")"
asset="Miniforge3-$tag-MacOSX-$(uname -m).sh"
installer="$temporary/$asset"
checksum="$installer.sha256"
cleanup() { rm -f -- "$installer" "$checksum"; rmdir -- "$temporary" 2>/dev/null || true; }
trap cleanup EXIT HUP INT TERM
printf 'Operating system: '; uname -s
printf 'Architecture: '; uname -m
case "$(uname -m)" in
  arm64|x86_64) ;;
  *) printf 'STOP: this Mac architecture has no approved installer in release %s.\n' "$tag" >&2; exit 1 ;;
esac
command -v curl >/dev/null || { printf 'STOP: curl is unavailable; use the official installer link.\n' >&2; exit 1; }
command -v shasum >/dev/null || { printf 'STOP: shasum is unavailable; do not run the installer.\n' >&2; exit 1; }
curl -fL --output "$installer" "https://github.com/conda-forge/miniforge/releases/download/$tag/$asset"
curl -fL --output "$checksum" "https://github.com/conda-forge/miniforge/releases/download/$tag/$asset.sha256"
(
  cd "$temporary"
  shasum -a 256 -c "$asset.sha256"
)
printf 'checksum-ok\n'
bash "$installer"
)
```
<!-- /passport-snippet:miniforge-macos-installer -->

</details>

- [Open Miniforge release 26.5.3-0](https://github.com/conda-forge/miniforge/releases/tag/26.5.3-0)

**Expected:** The operating system is Darwin, the matching versioned installer prints Miniforge3-...sh: OK before it runs, and installation finishes without replacing another Conda installation.

**Continue when:** Close this command terminal after the installer finishes, open a new Terminal window, and continue at Reopen and recheck Conda.

**If not:** If curl is unavailable, use the official release link and choose the MacOSX installer for this Mac's architecture. Stop if the architecture or destination is unclear; do not overwrite an existing Conda installation.

### 7. Install Miniforge on Linux only if needed

**Where:** The laptop or desktop in front of you

Skip this step if Self Service or IT already installed Conda; request its supported setup if needed. Run this step only after the recovery check printed no-common-conda-installation. The block downloads the versioned Miniforge 26.5.3-0 installer for this Linux computer and its published SHA-256 checksum into a temporary directory. It verifies the checksum before starting the interactive installer. Answer yes when asked to initialize Bash. Do not use sudo.

<details>
<summary>Show the installer only after the absence checks passed</summary>

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

<!-- passport-snippet:miniforge-linux-installer -->
```bash
(
set -eu
tag="26.5.3-0"
temporary="$(mktemp -d "${TMPDIR:-/tmp}/ideal-passport-miniforge.XXXXXX")"
asset="Miniforge3-$tag-$(uname -s)-$(uname -m).sh"
installer="$temporary/$asset"
checksum="$installer.sha256"
cleanup() { rm -f -- "$installer" "$checksum"; rmdir -- "$temporary" 2>/dev/null || true; }
trap cleanup EXIT HUP INT TERM
printf 'Operating system: '; uname -s
printf 'Architecture: '; uname -m
case "$(uname -m)" in
  aarch64|ppc64le|x86_64) ;;
  *) printf 'STOP: this Linux architecture has no approved installer in release %s.\n' "$tag" >&2; exit 1 ;;
esac
command -v curl >/dev/null || { printf 'STOP: curl is unavailable; use the official installer link.\n' >&2; exit 1; }
command -v sha256sum >/dev/null || { printf 'STOP: sha256sum is unavailable; do not run the installer.\n' >&2; exit 1; }
curl -fL --output "$installer" "https://github.com/conda-forge/miniforge/releases/download/$tag/$asset"
curl -fL --output "$checksum" "https://github.com/conda-forge/miniforge/releases/download/$tag/$asset.sha256"
(
  cd "$temporary"
  sha256sum -c "$asset.sha256"
)
printf 'checksum-ok\n'
bash "$installer"
)
```
<!-- /passport-snippet:miniforge-linux-installer -->

</details>

- [Open Miniforge release 26.5.3-0](https://github.com/conda-forge/miniforge/releases/tag/26.5.3-0)

**Expected:** The operating system is Linux, the matching versioned installer prints Miniforge3-...sh: OK before it runs, and installation finishes without replacing another Conda installation.

**Continue when:** Close this command terminal after the installer finishes, open a new Terminal window, which normally starts Bash, and continue at Reopen and recheck Conda.

**If not:** If curl is unavailable, use the official release link and choose the Linux installer for this computer's architecture. Stop if the architecture or destination is unclear; do not use sudo or overwrite another Conda installation.

### 8. Reopen and recheck Conda

**Where:** The laptop or desktop in front of you

After installation or conda init, close only the command terminal and open a new one; leave the terminal running the Passport open. If Conda already worked without setup changes, keep that terminal. Run the checks below before returning to the practice folder.

**Open PowerShell on your Windows computer, then run:**

```powershell
conda --version
conda info --base
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
conda --version
conda info --base
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
conda --version
conda info --base
```

**Expected:** Conda prints a version and one base installation path without a command-not-found error.

**Continue when:** Keep this command terminal open. Return to the exact practice folder before reading environment.yml.

**If not:** Do not install another copy. On Windows, try Miniforge Prompt and run conda info --base. On any platform, request help with the command-not-found message and the base path already found; do not include your username or full home path.

### 9. Return to the practice folder and read the definition

**Where:** The laptop or desktop in front of you

In the new command terminal, first run the enter-folder command from the Practice folder ready box under Prepare the Python practice folder. If that box is missing after a page reload, press Prepare practice folder to show it again; this reuses your existing folder. Then run the read-only checks below. The first two paths must identify the same folder as the Passport path. The branch must be practice/ followed by your GitHub username in lowercase. environment.yml at that root selects conda-forge, nodefaults and Python 3.11. Keep the file unchanged.

**Open PowerShell on your Windows computer, then run:**

```powershell
(Get-Location).Path
git rev-parse --show-toplevel
git status --short --branch
Get-Content -LiteralPath environment.yml
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
pwd -P
git rev-parse --show-toplevel
git status --short --branch
cat environment.yml
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
pwd -P
git rev-parse --show-toplevel
git status --short --branch
cat environment.yml
```

**Expected:** The current folder and Git root both identify the Passport practice folder, the practice branch is active, and the file names conda-forge, nodefaults and Python 3.11. Windows may display the same folder with backslashes or forward slashes.

**Continue when:** Inspect the .venv target before creating it.

**If not:** Stop if a path or branch differs, Git says not a repository, or the file is missing or changed. Copy the enter-folder command again and repeat these checks. Do not create a replacement environment.yml, run git init, clone again, or change branches to hide the error. Ask for help with the named failed check, without sharing private paths.

### 10. Inspect the environment path

**Where:** The laptop or desktop in front of you

Check whether .venv already exists before creating anything. A symbolic link is a path that redirects to another file or folder; this recipe will not follow one. A normal project folder using Python 3.11 is kept. A link, incomplete environment, or different Python version stops the recipe; nothing is deleted.

**Open PowerShell on your Windows computer, then run:**

```powershell
& {
  if (Test-Path -LiteralPath .venv) {
    $Target = Get-Item -Force -LiteralPath .venv
    if (($Target.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "STOP: .venv is a link or reparse point; nothing was changed" }
    if (-not $Target.PSIsContainer) { throw "STOP: .venv exists but is not a directory; nothing was changed" }
    conda list --prefix ./.venv | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "STOP: .venv is not a readable Conda environment" }
    $Python = Join-Path $Target.FullName "python.exe"
    if (-not (Test-Path -LiteralPath $Python -PathType Leaf)) { throw "STOP: .venv has no Python interpreter" }
    & $Python -I -c "import sys; assert sys.version_info[:2] == (3, 11)"
    if ($LASTEXITCODE -ne 0) { throw "STOP: existing .venv does not use Python 3.11" }
    Write-Host "existing-conda-environment"
  } else {
    Write-Host "ready-to-create"
  }
}
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
(
if [ -L .venv ]; then
  printf 'STOP: .venv is a symbolic link; nothing was changed\n' >&2
  exit 1
elif [ -e .venv ]; then
  [ -d .venv ] && [ -x .venv/bin/python ] || { printf 'STOP: .venv is not a complete environment; nothing was changed\n' >&2; exit 1; }
  conda list --prefix ./.venv >/dev/null || { printf 'STOP: .venv is not a readable Conda environment\n' >&2; exit 1; }
  .venv/bin/python -I -c 'import sys; assert sys.version_info[:2] == (3, 11)' || { printf 'STOP: existing .venv does not use Python 3.11\n' >&2; exit 1; }
  printf 'existing-conda-environment\n'
else
  printf 'ready-to-create\n'
fi
)
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
(
if [ -L .venv ]; then
  printf 'STOP: .venv is a symbolic link; nothing was changed\n' >&2
  exit 1
elif [ -e .venv ]; then
  [ -d .venv ] && [ -x .venv/bin/python ] || { printf 'STOP: .venv is not a complete environment; nothing was changed\n' >&2; exit 1; }
  conda list --prefix ./.venv >/dev/null || { printf 'STOP: .venv is not a readable Conda environment\n' >&2; exit 1; }
  .venv/bin/python -I -c 'import sys; assert sys.version_info[:2] == (3, 11)' || { printf 'STOP: existing .venv does not use Python 3.11\n' >&2; exit 1; }
  printf 'existing-conda-environment\n'
else
  printf 'ready-to-create\n'
fi
)
```

**Expected:** The final line is ready-to-create or existing-conda-environment. An existing environment has been confirmed as a real directory using Python 3.11.

**Continue when:** Verify the Git ignore rule before creating or reusing the environment.

**If not:** Stop if the path is a link, incomplete, unreadable, or uses another Python version. Identify who created it before removing or replacing anything.

### 11. Verify the environment path is ignored

**Where:** The laptop or desktop in front of you

Ask Git whether the future .venv contents are excluded before creating anything there. --no-index makes the check work even when the path does not exist yet.

**Open PowerShell on your Windows computer, then run:**

```powershell
git check-ignore -v --no-index .venv/conda-meta/history
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
git check-ignore -v --no-index .venv/conda-meta/history
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
git check-ignore -v --no-index .venv/conda-meta/history
```

**Expected:** Git prints the .gitignore rule that covers .venv/.

**Continue when:** Create or reuse the environment.

**If not:** Stop and correct .gitignore before creating the environment or committing project files.

### 12. Create or reuse the project Conda environment

**Where:** The laptop or desktop in front of you

If the earlier path check printed existing-conda-environment, keep it and let this command report reused-conda-environment. Otherwise, create the project-local .venv from the committed environment.yml. Do not install packages into base and do not replace the definition with a manual package list.

**Open PowerShell on your Windows computer, then run:**

```powershell
& {
  if (Test-Path -LiteralPath .venv) {
    $Target = Get-Item -Force -LiteralPath .venv
    if (($Target.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0 -or -not $Target.PSIsContainer) { throw "STOP: existing .venv is not a safe project directory" }
    conda list --prefix ./.venv | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "STOP: existing .venv is not readable by Conda" }
    $Python = Join-Path $Target.FullName "python.exe"
    & $Python -I -c "import sys; assert sys.version_info[:2] == (3, 11)"
    if ($LASTEXITCODE -ne 0) { throw "STOP: existing .venv does not use Python 3.11" }
    Write-Host "reused-conda-environment"
  } else {
    conda env create --prefix ./.venv --file environment.yml -y
    if ($LASTEXITCODE -ne 0) { throw "STOP: Conda environment creation failed" }
  }
}
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
(
if [ -L .venv ]; then
  printf 'STOP: existing .venv is a symbolic link\n' >&2
  exit 1
elif [ -e .venv ]; then
  [ -d .venv ] && [ -x .venv/bin/python ] || { printf 'STOP: existing .venv is incomplete\n' >&2; exit 1; }
  conda list --prefix ./.venv >/dev/null || { printf 'STOP: existing .venv is not readable by Conda\n' >&2; exit 1; }
  .venv/bin/python -I -c 'import sys; assert sys.version_info[:2] == (3, 11)' || { printf 'STOP: existing .venv does not use Python 3.11\n' >&2; exit 1; }
  printf 'reused-conda-environment\n'
else
  conda env create --prefix ./.venv --file environment.yml -y
fi
)
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
(
if [ -L .venv ]; then
  printf 'STOP: existing .venv is a symbolic link\n' >&2
  exit 1
elif [ -e .venv ]; then
  [ -d .venv ] && [ -x .venv/bin/python ] || { printf 'STOP: existing .venv is incomplete\n' >&2; exit 1; }
  conda list --prefix ./.venv >/dev/null || { printf 'STOP: existing .venv is not readable by Conda\n' >&2; exit 1; }
  .venv/bin/python -I -c 'import sys; assert sys.version_info[:2] == (3, 11)' || { printf 'STOP: existing .venv does not use Python 3.11\n' >&2; exit 1; }
  printf 'reused-conda-environment\n'
else
  conda env create --prefix ./.venv --file environment.yml -y
fi
)
```

**Expected:** Conda creates .venv from environment.yml, or the final line is reused-conda-environment for the valid environment already present.

**Continue when:** If creation succeeded or the command printed reused-conda-environment, skip the channel-terms recovery and continue at Activate the project environment.

**If not:** If Conda reports CondaToSNonInteractiveError for repo.anaconda.com/pkgs/main or /pkgs/r, use the next recovery step. Do not accept terms just to unblock this exercise. For other failures, stop and ask for help; preserve any existing or incomplete .venv.

### 13. Recover only from a Conda channel-terms error

**Where:** The laptop or desktop in front of you

Skip this step if creation or reuse succeeded. Use it only after CondaToSNonInteractiveError names repo.anaconda.com/pkgs/main or /pkgs/r. Some installations check configured channels before reading environment.yml, so nodefaults alone does not prevent this early error. In your local command terminal, at the practice repository root, the guarded command below reads the same definition and selects only conda-forge for this invocation. It needs stable Conda 26.3 or newer, leaves the ToS plugin enabled, and does not change global settings or accept terms. Keep the terminal running the Passport open.

<details>
<summary>Show recovery for the named channel-terms error</summary>

**Open PowerShell on your Windows computer, then run:**

```powershell
& {
  if (Get-Item -Force -LiteralPath .venv -ErrorAction SilentlyContinue) { throw "STOP: .venv already exists; return to Inspect the environment path. Nothing was replaced." }
  git ls-files --error-unmatch -- environment.yml *> $null
  if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath environment.yml -PathType Leaf)) { throw "STOP: use environment.yml in the practice repository" }
  git diff --quiet -- environment.yml
  if ($LASTEXITCODE -ne 0) { throw "STOP: environment.yml has changed; return to Read the environment definition" }
  git diff --cached --quiet -- environment.yml
  if ($LASTEXITCODE -ne 0) { throw "STOP: environment.yml has staged changes; return to Read the environment definition" }
  git check-ignore -q --no-index .venv/conda-meta/history
  if ($LASTEXITCODE -ne 0) { throw "STOP: .venv must be ignored by Git" }
  $PassportCondaVersion = conda --version
  if ($LASTEXITCODE -ne 0) { throw "STOP: Conda version could not be checked" }
  $PassportVersion = [regex]::Match([string]$PassportCondaVersion, '^conda (\d+)\.(\d+)\.(\d+)$')
  if (-not $PassportVersion.Success -or [int]$PassportVersion.Groups[1].Value -lt 26 -or ([int]$PassportVersion.Groups[1].Value -eq 26 -and [int]$PassportVersion.Groups[2].Value -lt 3)) { throw "STOP: this recovery needs stable Conda 26.3 or newer. Ask IT about an approved update; do not reinstall or accept terms to unblock this exercise." }
  conda create --prefix ./.venv --file environment.yml --override-channels --channel conda-forge --no-default-packages -y
  if ($LASTEXITCODE -ne 0) { throw "STOP: Conda recovery failed; keep the error type and ask for help" }
}
```

</details>

<details>
<summary>Show recovery for the named channel-terms error</summary>

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
(
if [ -e .venv ] || [ -L .venv ]; then
  printf 'STOP: .venv already exists; return to Inspect the environment path. Nothing was replaced.\n' >&2
  exit 1
fi
git ls-files --error-unmatch -- environment.yml >/dev/null 2>&1 &&
  git diff --quiet -- environment.yml && git diff --cached --quiet -- environment.yml &&
  [ -f environment.yml ] || { printf 'STOP: use the unchanged environment.yml in the practice repository.\n' >&2; exit 1; }
git check-ignore -q --no-index .venv/conda-meta/history || { printf 'STOP: .venv must be ignored by Git.\n' >&2; exit 1; }
passport_conda_version="$(conda --version)" || exit 1
printf '%s\n' "$passport_conda_version" | awk '
  $1 == "conda" && $2 ~ /^[0-9]+\.[0-9]+\.[0-9]+$/ {
    split($2, v, "."); if (v[1] > 26 || (v[1] == 26 && v[2] >= 3)) ok = 1
  }
  END { exit !ok }
' || { printf 'STOP: this recovery needs stable Conda 26.3 or newer. Ask IT about an approved update; do not reinstall or accept terms to unblock this exercise.\n' >&2; exit 1; }
conda create --prefix ./.venv --file environment.yml --override-channels --channel conda-forge --no-default-packages -y
)
```

</details>

<details>
<summary>Show recovery for the named channel-terms error</summary>

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
(
if [ -e .venv ] || [ -L .venv ]; then
  printf 'STOP: .venv already exists; return to Inspect the environment path. Nothing was replaced.\n' >&2
  exit 1
fi
git ls-files --error-unmatch -- environment.yml >/dev/null 2>&1 &&
  git diff --quiet -- environment.yml && git diff --cached --quiet -- environment.yml &&
  [ -f environment.yml ] || { printf 'STOP: use the unchanged environment.yml in the practice repository.\n' >&2; exit 1; }
git check-ignore -q --no-index .venv/conda-meta/history || { printf 'STOP: .venv must be ignored by Git.\n' >&2; exit 1; }
passport_conda_version="$(conda --version)" || exit 1
printf '%s\n' "$passport_conda_version" | awk '
  $1 == "conda" && $2 ~ /^[0-9]+\.[0-9]+\.[0-9]+$/ {
    split($2, v, "."); if (v[1] > 26 || (v[1] == 26 && v[2] >= 3)) ok = 1
  }
  END { exit !ok }
' || { printf 'STOP: this recovery needs stable Conda 26.3 or newer. Ask IT about an approved update; do not reinstall or accept terms to unblock this exercise.\n' >&2; exit 1; }
conda create --prefix ./.venv --file environment.yml --override-channels --channel conda-forge --no-default-packages -y
)
```

</details>

- [Understand the error and safe recovery](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/python_setup.md#recover-from-a-conda-channel-terms-error)

**Expected:** Only conda-forge is selected and .venv is created with Python 3.11, without a terms prompt. The command stops before creation if .venv exists, the definition changed, Git does not ignore .venv, or Conda is too old.

**Continue when:** Continue at Activate the project environment, then verify the interpreter and pip paths. No reset, new Passport, or edited environment.yml is needed.

**If not:** Preserve .venv if it exists and return to the inspection step. For old Conda, ask IT about an approved update of the existing installation; do not install a second distribution. If terms, channel-policy, permission, or network errors remain, stop and use the linked help path. Do not disable plugins, change .condarc, or enable automatic ToS acceptance.

### 14. Activate the project environment

**Where:** The laptop or desktop in front of you

Activate the environment by its local .venv folder path. Activation changes which Python this terminal uses; it does not change the project files.

**Open PowerShell on your Windows computer, then run:**

```powershell
conda activate ./.venv
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
conda activate ./.venv
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
conda activate ./.venv
```

**Expected:** The shell accepts the command without an activation error.

**Continue when:** Verify the interpreter path.

**If not:** Windows: open Miniforge Prompt and run conda init powershell. macOS: run conda init zsh. Linux Bash: run conda init bash. Run it once, close only that command terminal, keep the terminal running the Passport open, open a new command terminal, return to the practice root, and retry.

### 15. Verify the active interpreter

**Where:** The laptop or desktop in front of you

Print the executable path and Python version. The path, not only the prompt decoration, proves which environment is active.

**Open PowerShell on your Windows computer, then run:**

```powershell
python -c "import sys; print(sys.executable); print(sys.version)"
```

**Open Terminal on your Mac; zsh starts inside it automatically. Then run:**

```zsh
python -c "import sys; print(sys.executable); print(sys.version)"
```

**Open Terminal on your Linux computer; Bash normally starts inside it automatically. Then run:**

```bash
python -c "import sys; print(sys.executable); print(sys.version)"
```

**Expected:** The executable path is inside the practice repository .venv directory and Python reports version 3.11.

**Continue when:** If you use VS Code, check its Python extension in the next step. Other-editor and terminal-only users can skip that extension step.

**If not:** Do not install packages until the interpreter path is correct.

### 16. Install the Python extension if you use VS Code

**Where:** The laptop or desktop in front of you

Skip this step for another editor or terminal-only work. In a local VS Code window, use File > Open Folder to open the exact Practice folder ready path. Open Extensions with Ctrl+Shift+X on Windows/Linux or Command+Shift+X on macOS. Search @id:ms-python.python, choose Python by Microsoft, and click Install if it is missing. If it is installed but disabled, enable it for this workspace. Save your files and reload the VS Code window if prompted; keep the separate Passport terminal open. This extension connects the editor to Python; it does not replace the Conda environment you just verified.

- [Python extension setup and missing-command help](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/vscode.md#python-extension)

- [Official Python extension by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

**Expected:** Python by Microsoft is installed and enabled in the current local VS Code workspace. No extra Python installation or new environment is needed.

**Continue when:** Open workspace/python_project/passport_example.py from the Explorer, then select the existing interpreter in the next step.

**If not:** If VS Code shows Restricted Mode, use the linked folder-trust guidance before enabling Python features. Trust only the recognized practice folder after reviewing its contents; do not disable Workspace Trust globally. If device policy blocks installation or enabling, ask IT for the approved extension. Keep using the verified command terminal; the terminal-only route remains valid.

### 17. Use the same interpreter in your editor

**Where:** The laptop or desktop in front of you

Terminal activation and editor selection are separate. After the Python extension is enabled and a .py file is open in VS Code, press Ctrl+Shift+P on Windows/Linux or Command+Shift+P on macOS. Run Python: Select Interpreter and select the exact executable printed by Verify the active interpreter, inside this practice folder's .venv. Then open Terminal > New Terminal, return to the practice folder, and repeat Activate the project environment and Verify the active interpreter there. An already-open terminal may still use the previous environment. For another editor, select the same verified interpreter through its settings. Terminal-only users need no editor extension or setting.

- [Select the interpreter and recover a missing command](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/vscode.md#conda-environments-in-vs-code)

- [Read the VS Code Python environment instructions](https://code.visualstudio.com/docs/python/environments)

**Expected:** The editor selects the same .venv interpreter as the verified command terminal; a new integrated terminal reports that same interpreter and Python 3.11. Terminal-only users keep their verified terminal.

**Continue when:** Run Check my work.

**If not:** If Python: Select Interpreter is missing, return to the Python extension step and check that Python by Microsoft is enabled in this local workspace. If .venv is not listed, use the linked recovery guide. Keep the working terminal environment; do not select base, install another Python, or recreate .venv to make it appear.

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

1. A terminal reports Python 3.11 from base; another reports Python 3.11 from this practice folder's .venv. Are they interchangeable for this lesson?

   - Yes; matching versions prove the same environment.
   - No; use the project .venv interpreter and verify its path.
   - Yes; an editor setting automatically changes every terminal.

<details class="learning-explanation">
<summary>See an explanation</summary>

Matching version numbers do not identify the environment. The executable path must be inside this project's .venv. Editor selection and an already-open terminal are separate.

</details>

## If Blocked

Do not repeatedly reinstall into `base`. Record `conda info --envs`, the Python
path, and the exact error without credentials. Use the
[reproducible Python lab](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/reproducible-python.md) or ask for
help before deleting an existing environment.

Useful references:

- [Python setup](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/python_setup.md)
- [Reproducible Python](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/labs/reproducible-python.md)

## Understand Before Accepting AI Output

An agent may suggest packages that are unnecessary, unmaintained, or fetched
from an unapproved source. Review dependency purpose and project declarations
before installation.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
