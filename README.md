# IDEAL Lab IT Passport Exercises

This public repository contains fictional exercises and structured mission contracts
for the IDEAL Lab IT and Research Computing Passport `2.1.2`.
It contains no student records, research data, credentials, or privileged
workflow.

## Start Or Resume

Do not clone this repository manually. Install the public GitHub CLI extension,
then let it create or reuse your public learning record:

```text
gh extension install soheylm-passport-sandbox/gh-passport --force --pin v0.5.24
gh passport start
```

After setup, run this command from any folder:

```text
gh passport open
```

The browser remembers local navigation. The launcher writes only the current
mission's generated submission and declared synthetic exercise files. It never
stages arbitrary learner files. During the Git mission you create a separate
practice branch and PR yourself; before that mission, the Git transport stays
in the background.

The private controller publishes deterministic results on the submitted commit.
Routine learning does not wait for a person. Only exceptions and real operational
approvals enter the asynchronous help or approval queues.

If no automatic check appears after 30 minutes, submit one
[public, non-secret passport help request](https://github.com/soheylm-passport-sandbox/passport-exercises/issues/new?template=passport-help.yml)
and return later. Do not create an empty commit to wake the controller.

## Public Content Rule

Pull requests in this repository are public. Your GitHub username is
necessarily visible through the fork and PR. Use only the fictional values
requested by each exercise. Never submit passwords, tokens, private keys,
recovery codes, ETH usernames or email addresses, student numbers, other
private identifiers, real logs, unpublished research data, screenshots
containing private information, or confidential project details.

If a real incident or possible secret appears, stop. Revoke the credential if
needed and use the lab's private incident channel instead of the pull request.

## Repository Boundaries

- `missions/` contains generated fallback instructions and is not editable.
- `submissions/` receives launcher-generated structured public submissions.
- `workspace/` contains bounded fictional files used by practical exercises.
- `passport-curriculum.json` is the launcher-readable route catalogue.
- `passport.example.json` documents the format; `gh passport start` creates
  your actual `passport.json` only on its managed transport branch.

The canonical curriculum and handbook live in
[`IDEALLab/onboarding-IT`](https://github.com/IDEALLab/onboarding-IT).
