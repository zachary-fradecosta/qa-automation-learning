# Git and GitHub Guide

## Check repository status

```powershell
git status
```

Use this before committing, pulling or pushing.

## Check the current branch

```powershell
git branch
```

## Stage changes

```powershell
git add .
```

## Create a commit

```powershell
git commit -m "type(scope): short description"
```

Examples:

```powershell
git commit -m "test(day13): add first API response test"
git commit -m "docs: organize QA automation guides"
```

## Push commits to GitHub

```powershell
git push -u origin main
```

## Update the local branch before starting work

```powershell
git pull --ff-only origin main
```

## Integrate remote changes before pushing

```powershell
git pull --rebase origin main
```

## If a rebase stops

```powershell
git status
```

After resolving conflicts:

```powershell
git add .
git rebase --continue
```

To cancel a rebase:

```powershell
git rebase --abort
```

## End-of-mission workflow

```powershell
pytest -v
git status
git add .
git commit -m "type(scope): short description"
git pull --rebase origin main
git push -u origin main
```

## Commit types

```text
test      → test creation or improvement
feat      → new functionality
fix       → bug fix
refactor  → code structure improvement
docs      → documentation update
chore     → maintenance task
```