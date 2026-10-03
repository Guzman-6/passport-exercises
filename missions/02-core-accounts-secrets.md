# Mission: Protect Accounts And Secrets

## Outcome

Learn which sign-in information must stay secret, protect your GitHub and ETH
accounts, and practise what to do if secret information is exposed.

## Concept

An account is your personal identity on a service. A credential, such as a password, token, private key, or recovery code, proves that identity and must not be shared. A token is secret text that authorizes account or service access. An SSH key pair has a private key that stays on your computer and a public file ending in `.pub` that may be given to the named service. A password manager is an encrypted application for storing unique passwords and recovery information. Two-factor authentication (2FA) asks for a second proof after the password, which limits the damage if the password is stolen.

A passphrase is a password-like secret that unlocks an SSH private key on your
computer. It does not make the private key safe to share.

Commands and automated tools run under your identity. A leaked credential may provide access to private repositories, research data, or shared compute even when your password was not disclosed.

## Worked Example

Every credential-critical answer is correct before the mission can pass.

Check these points:

- **A token may have been exposed. What comes first?** Revoke or rotate it, then report through the private incident path.
- **When a service asks for an SSH key, which file may be shared?** Only the public key ending in .pub.
- **How should you verify GitHub two-factor authentication without exposing a secret?** Check the authentication status in your own GitHub security settings; never submit a recovery code.

## Common Trap

Pasting a real token, private key, recovery code, or screenshot to prove that it exists.

## Your Action

Set up the minimum account protections, learn what may never be submitted, then answer the credential scenarios.

**Follow these steps in order.** Use your own account pages. Never paste a password, token, private key, one-time code, or recovery code into the Passport.

### 1. Prepare an approved password manager

**Where:** This web page in your browser

A password manager is an encrypted application for storing unique passwords and recovery information. Keep a working approved password manager if you already use one. Otherwise, on a personal computer follow ETH's KeePass guidance and use KeePassXC; on an ETH-managed device ask the responsible IT support before installing software. Do not store ETH passwords in an unapproved cloud-hosted vault.

- [Read the ETH KeePass guidance](https://unlimited.ethz.ch/help/security/passwort-manager-keepass)

**Expected:** You have an approved private place for unique passwords and recovery codes, or you have requested installation help for a managed device.

**Continue when:** Enable GitHub two-factor authentication.

**If not:** Do not create plain-text password notes or reuse a password while waiting for support.

### 2. Enable GitHub two-factor authentication

**Where:** This web page in your browser

Two-factor authentication (2FA) asks for a second proof after your password. Open your personal GitHub password and authentication settings, enable 2FA, configure the recovery methods offered by GitHub, and store the recovery codes in the approved private location from the previous step. Never upload a recovery code to the Passport.

- [Open GitHub authentication settings](https://github.com/settings/security)

- [Read GitHub recovery-method guidance](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication-recovery-methods)

**Expected:** GitHub reports that two-factor authentication is enabled and the recovery-code view is closed after secure storage.

**Continue when:** Continue to file-based secrets.

**If not:** Complete GitHub account recovery privately; never submit a recovery code as evidence.

### 3. Keep secrets outside Git

**Where:** This web page in your browser

Store local secrets only in an approved secret store or an ignored local file. Ignored means Git is configured not to record that file. A token is secret text that authorizes account or service access. An SSH key pair has a private key that stays on your computer and a public file ending in .pub that may be given to the named service. A sample environment file may show the names of settings a program needs, but never their real secret values.

**Expected:** No secret value is inside any file that Git is asked to record or share.

**Continue when:** Continue to the exposure procedure.

**If not:** Remove the value from the project files and any staged Git change, then rotate it if it may have been exposed.

### 4. Know the first response to exposure

**Where:** This web page in your browser

If a credential may be exposed, revoke it, meaning disable it, or rotate it, meaning replace it with a new one. Do this first, preserve useful evidence, and report through the private incident path. Deleting a message or a recorded Git version is not sufficient.

- [Open the incident and help procedure](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/incidents-and-help.md)

**Expected:** The compromised credential can no longer be used.

**Continue when:** Document only non-secret facts and continue.

**If not:** Stop using the affected account. Use the linked incident procedure to contact your supervisor or lab IT, ETH cyber incident support, or ETH High-Performance Computing (HPC) support, according to the affected system.

### 5. Complete the scenarios

**Where:** This web page in your browser

Answer every question below using the rules above. Treat every credential question as safety-critical.

**Expected:** All credential-critical answers are correct.

**Continue when:** Run Check my work.

**If not:** Read the feedback and retry; do not guess around a secret-handling rule.

The Passport presents the questions and required confirmation in the
browser. Do not create or edit a submission JSON file by hand.

## Check Your Work

Use **Check my work** before submitting. This check runs on your computer and
checks only the practical work in this lesson. A score of 100% is required, and every
safety-critical question must be correct. Failed attempts provide targeted
feedback and can be retried without penalty.

## If Blocked

If you suspect a real exposure, stop the exercise and follow
[Incidents and getting help](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/incidents-and-help.md). Do not
post the secret in a GitHub issue or ask an AI tool to inspect it.

Useful references:

- [Accounts And Security](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/accounts-and-security.md)
- [Incidents And Help](https://github.com/IDEALLab/onboarding-IT/blob/main/docs/core/incidents-and-help.md)

## Understand Before Accepting AI Output

An AI-generated cleanup command may destroy evidence without revoking the
credential. Verify the issuing service, scope, and incident path yourself.

## Finish And Continue

When **Check my work** passes, use **Submit lesson** once. The launcher
publishes only this lesson's generated submission after private information is excluded. Continue when the
progress page shows the automatic GitHub result as passed; a check on your computer alone is not a pass.
