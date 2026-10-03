# Mission: Use Blade For Graphical Work Without Losing Data

## Outcome

Connect by Remote Desktop to Blade, the lab's shared Windows computer for licensed graphical software. Use the correct temporary and durable storage drives and verify one file copy.

## Concept

Blade is the IDEAL Lab's shared Windows computer. You reach its graphical desktop through Remote Desktop Protocol (RDP) when you need licensed Windows engineering software such as Siemens NX or interactive pre/post-processing. ETH VPN, or Virtual Private Network, provides the official secure connection when the service is not reachable directly from your current network. Several people may be connected at once.

Blade is not the lab's permanent storage or its heavy-compute cluster. `P:` maps to durable project data on the NAS, `D:` is temporary local working space, and `C:` plus Desktop, Documents, and Downloads are not project storage.

## Worked Example

The test verifies the copy to P:, then removes both random probe files from
D: and P:. No probe file remains. Real project results belong on P:; they must
be retained rather than cleaned up like this disposable test. C: was not used,
and no heavy unattended compute was started.

Check these points:

- **Where does durable Blade project work belong?** In the approved P: supervisor and username folder.
- **What is Blade primarily for?** Interactive graphical Windows software and light prototyping.

## Common Trap

Keeping the only copy on C: or D:, treating Blade as a general machine-learning server, or exposing the real mapped path in the public submission.

## Your Action

Connect to Blade by RDP, verify the host, and complete a safe temporary-to-durable file round trip.

**Follow these steps in order.** Blade is the lab's shared remote Windows computer for licensed graphical software. RDP, or Remote Desktop Protocol, displays and controls its Windows desktop from your computer. Connect through RDP, use P: for durable project data, use D: only for temporary work, and never use C: or user folders for project storage.

**New to text commands?** A command is a line of text that tells a
computer to do one task. A terminal is the text application in which a
shell reads that command. Open PowerShell on Windows or the application
named Terminal on macOS or Linux. The application starts the correct
shell automatically; do not install a separate Bash or zsh application. Read
[Terminal and command basics](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/command-line-basics.md)
before continuing if these words are new.

### 1. Confirm Blade is the right system

**Where:** This web page in your browser

Blade is a shared Windows computer reached through Remote Desktop Protocol (RDP). Use it for interactive licensed Windows software, computer-aided design (CAD), simulation pre-processing and post-processing, and light prototypes. Use Euler or another approved compute system for long or unattended heavy workloads.

**Expected:** Your task requires the shared graphical Windows environment.

**Continue when:** Connect to the ETH network.

**If not:** Choose the appropriate compute or storage system instead.

### 2. Connect to ETH network or VPN

**Where:** The laptop or desktop in front of you

Use the campus network or connect ETH VPN before opening RDP. VPN means Virtual Private Network: the official secure connection used to reach ETH-only services from outside the campus network.

- [Open the ETH VPN instructions](https://unlimited.ethz.ch/en/help/network/vpn)

**Expected:** The Blade hostname is reachable from your computer.

**Continue when:** Open an RDP client.

**If not:** Fix network access before changing saved credentials.

### 3. Connect from Windows

**Where:** The laptop or desktop in front of you

Open Start, search for Remote Desktop Connection, and open it. Enter mavt-ide-s100w.d.ethz.ch as the computer. At the credential prompt choose More choices and Use a different account if needed, then sign in as d\<eth-username> with your own ETH password.

- [Open the complete Blade guide](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/remote.md)

- [Microsoft: use Remote Desktop on Windows](https://support.microsoft.com/en-us/windows/experience/connectivity-networking/how-to-use-remote-desktop)

**Expected:** A Windows desktop opens for your personal ETH account.

**Continue when:** Verify the remote hostname.

**If not:** Check VPN, the exact hostname, and d\username; remove a wrong saved account instead of using it.

### 4. Connect from macOS

**Where:** The laptop or desktop in front of you

Install Microsoft Windows App from the Mac App Store if it is absent. Open Windows App, select Devices, select +, choose Add PC, enter mavt-ide-s100w.d.ethz.ch in PC Name, and select Add. Double-click the new PC. At the credential prompt sign in as d\<eth-username> with your own ETH password; do not reuse another person's saved account.

- [Open the complete Blade guide](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/remote.md)

- [Microsoft: connect to a remote PC from macOS](https://learn.microsoft.com/en-us/windows-app/get-started-connect-devices-desktops-apps)

**Expected:** A Windows desktop opens for your personal ETH account.

**Continue when:** Verify the remote hostname.

**If not:** Check VPN, the exact hostname, and d\username before changing any remote setting.

### 5. Connect from Linux

**Where:** The laptop or desktop in front of you

Search your applications for Remmina. If it is installed, open it, choose RDP, enter mavt-ide-s100w.d.ethz.ch as the server, and sign in as d\<eth-username> with your own ETH password. If Remmina is absent on a personal Linux computer, use your distribution's Software application or the official Remmina installation guide; install the RDP client and plugin only. On an ETH-managed computer, request software installation instead. Do not install a remote-desktop server, change a firewall, or alter Blade security settings.

- [Open the complete Blade guide](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/remote.md)

- [Official Remmina installation guide](https://remmina.org/how-to-install-remmina/)

**Expected:** A Windows desktop opens for your personal ETH account.

**Continue when:** Verify the remote hostname.

**If not:** Check VPN, protocol RDP, the exact hostname, and d\username. If the client or RDP plugin cannot be installed through the approved software source, use the Passport help form without including private information; do not install remote services.

### 6. Verify the remote computer

**Where:** The remote Blade Windows desktop

Open PowerShell inside the remote Blade desktop and run the block below. The hostname check is required. The GPU line is informational and may say that the query is unavailable.

**Open PowerShell inside the remote Blade Windows desktop, then run:**

```powershell
& {
  $HostName = $env:COMPUTERNAME
  $HostName
  if ($HostName -ne 'mavt-ide-s100w') { throw "STOP: this is not the assigned Blade server" }
  if (Get-Command nvidia-smi -ErrorAction SilentlyContinue) {
      nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
  } else {
      'GPU query unavailable; hostname is correct.'
  }
}
```

**Expected:** The first line is mavt-ide-s100w. A GPU line may follow, but it is not required to prove the Blade connection.

**Continue when:** Locate the approved P: project folder.

**If not:** Disconnect if the hostname is not the assigned Blade server.

### 7. Confirm P: and D: paths

**Where:** The remote Blade Windows desktop

Obtain the supervisor first name and approval to use that project folder. Open P:\SupervisorFirstName and create one folder named exactly with your short ETH username if it is absent. The temporary folder is D:\eth-username. Do not use C:, Desktop, Documents, Downloads, or other mapped drives.

**Expected:** The approved P: username folder exists and the D: username folder is clearly temporary.

**Continue when:** Run the harmless file round trip.

**If not:** Ask the supervisor or lab IT for the correct P: folder before creating project data.

### 8. Copy, verify, and clean one test file

**Where:** The remote Blade Windows desktop

Run this PowerShell block on Blade. It first refuses files, shortcuts, and junctions at either target. It then creates a random non-sensitive file on D:, copies it to the approved P: folder, verifies equal hashes, and removes both probe files.

**Open PowerShell inside the remote Blade Windows desktop, then run:**

```powershell
& {
  $Supervisor = (Read-Host "Supervisor first name").Trim()
  $EthUser = $env:USERNAME
  if ([string]::IsNullOrWhiteSpace($Supervisor) -or $Supervisor -in @('.', '..') -or $Supervisor -match '[\\/:*?"<>|]') { throw "STOP: invalid supervisor folder name" }
  if ($EthUser -notmatch '^[A-Za-z0-9._-]+$') { throw "STOP: invalid ETH username" }
  if (-not (Test-Path -LiteralPath 'P:\' -PathType Container)) { throw "STOP: P: is not available" }
  if (-not (Test-Path -LiteralPath 'D:\' -PathType Container)) { throw "STOP: D: is not available" }
  $Durable = Join-Path "P:\$Supervisor" $EthUser
  $Temporary = Join-Path "D:\" $EthUser
  if (-not (Test-Path -LiteralPath $Durable -PathType Container)) { throw "STOP: approved P: username folder not found" }
  $DurableItem = Get-Item -Force -LiteralPath $Durable
  if (-not $DurableItem.PSIsContainer -or ($DurableItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "STOP: approved P: path is not a real directory" }
  if (Test-Path -LiteralPath $Temporary) {
    $TemporaryItem = Get-Item -Force -LiteralPath $Temporary
    if (-not $TemporaryItem.PSIsContainer -or ($TemporaryItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "STOP: D: username path is not a real directory" }
  } else {
    New-Item -ItemType Directory -Path $Temporary -ErrorAction Stop | Out-Null
    $TemporaryItem = Get-Item -Force -LiteralPath $Temporary
    if (-not $TemporaryItem.PSIsContainer -or ($TemporaryItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "STOP: new D: username path is not a real directory" }
  }
  $Name = "passport-$([guid]::NewGuid().ToString('N')).txt"
  $TempFile = Join-Path $Temporary $Name
  $DurableFile = Join-Path $Durable $Name
  $CopyVerified = $false
  try {
    Set-Content -LiteralPath $TempFile -Value "IDEAL Passport synthetic Blade storage check" -ErrorAction Stop
    Copy-Item -LiteralPath $TempFile -Destination $DurableFile -ErrorAction Stop
    $CopyVerified = (Get-FileHash -LiteralPath $TempFile -ErrorAction Stop).Hash -eq (Get-FileHash -LiteralPath $DurableFile -ErrorAction Stop).Hash
  } finally {
    Remove-Item -LiteralPath $TempFile -Force -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath $DurableFile -Force -ErrorAction SilentlyContinue
  }
  $TemporaryRemoved = -not (Test-Path -LiteralPath $TempFile)
  $ProbeRemoved = -not (Test-Path -LiteralPath $DurableFile)
  "copy_verified=$CopyVerified temporary_removed=$TemporaryRemoved probe_removed=$ProbeRemoved"
  if (-not ($CopyVerified -and $TemporaryRemoved -and $ProbeRemoved)) { throw "STOP: copy verification or probe cleanup failed" }
}
```

**Expected:** The final line says copy_verified=True, temporary_removed=True, and probe_removed=True.

**Continue when:** Confirm the successful copy in the Passport; no probe file remains.

**If not:** Read the first error. The finally block attempts to remove both random probe files even after a failure. If either remains, remove only the two displayed passport probe paths; do not broaden folder permissions or delete the username folder.

### 9. Leave heavy work off Blade

**Where:** The remote Blade Windows desktop

Do not start overnight training, broad sweeps, or unscheduled heavy computation. Do not install a Windows Subsystem for Linux (WSL) distribution or enable Windows features without approval.

**Expected:** Only the interactive graphical application or light prototype remains on Blade.

**Continue when:** Return to the local Passport.

**If not:** Stop the workload safely and move it to an approved scheduled compute system.

### 10. Record the safe result

**Where:** The laptop or desktop in front of you

Enter only the hostname and yes/no storage confirmations in the local Passport. Do not publish the supervisor name, mapped path, credentials, or screenshot.

**Expected:** The result confirms the correct host, durable copy, D: cleanup, and no C: usage.

**Continue when:** Run Check my work and submit once.

**If not:** Reconnect and verify the exact missing condition before attesting.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 100% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

Check VPN, exact hostname, account format, and assigned supervisor folder. Do
not use another person's saved credentials, install remote services, or select
another mapped drive. Use the
[remote access guide](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/remote.md).

Useful references:

- [Blade remote access](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/remote.md)
- [NAS guide](https://github.com/IDEALLab/onboarding-IT/blob/main/onboarding_IT_guides/nas_ideal.md)

## Understand Before Accepting AI Output

An agent must not install system features, choose another drive, or run a heavy
local workload because Euler access is inconvenient. Verify host, storage, and
shared-resource impact.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
