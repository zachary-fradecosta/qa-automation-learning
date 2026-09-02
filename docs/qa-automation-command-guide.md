# QA Automation Command Guide

A practical reference for commands learned during my QA Automation Engineer journey.

---

## Git and GitHub

### Check the repository status

```powershell
git status
```

Use this before committing, pulling or pushing changes.

### View the current branch

```powershell
git branch
```

### Stage all changes

```powershell
git add .
```

### Create a commit

```powershell
git commit -m "type(scope): short description"
```

Example:

```powershell
git commit -m "test(day10): strengthen user eligibility assertions"
```

### Push commits to GitHub

```powershell
git push -u origin main
```

### Safely update the local repository before starting work

```powershell
git pull --ff-only origin main
```

This command only updates the local branch when no local history diverges from the remote branch.

### Integrate remote changes before pushing

```powershell
git pull --rebase origin main
```

Use this when the remote branch contains commits that are missing locally.

### Check the remote repository URL

```powershell
git remote -v
```

### Check the local Git identity

```powershell
git config --local --get user.name
git config --local --get user.email
```

### If a rebase stops because of a conflict

```powershell
git status
```

After resolving the conflicted files:

```powershell
git add .
git rebase --continue
```

To cancel an in-progress rebase:

```powershell
git rebase --abort
```

---

## Pytest

### Check the installed Pytest version

```powershell
pytest --version
```

### Run the complete test suite

```powershell
pytest -v
```

`-v` means verbose mode: Pytest displays each test name and result.

### Run one test file

```powershell
pytest tests/test_user_helpers.py -v
```

### Run one specific test

```powershell
pytest tests/test_user_helpers.py::test_get_active_users -v
```

### Run smoke tests

```powershell
pytest -m smoke -v
```

### Run regression tests

```powershell
pytest -m regression -v
```

### Run smoke and regression tests

```powershell
pytest -m "smoke or regression" -v
```

### Run every test except smoke tests

```powershell
pytest -m "not smoke" -v
```

---

## Python

### Run a Python module

```powershell
python -m scripts.day04_demo
```

Running a module helps Python resolve project imports correctly.

### Run a Python file directly

```powershell
python scripts/day04_demo.py
```

Use this only when the script does not require package-style imports.

---

## Project Navigation

### Display the current directory

```powershell
Get-Location
```

### List files and folders

```powershell
Get-ChildItem
```

### Display the project tree

```powershell
tree /F /A
```

### Move to the parent folder

```powershell
cd ..
```

---

## End-of-Mission Checklist

Before committing a completed QA Automation mission:

```powershell
pytest -v
git status
git add .
git commit -m "type(scope): short description"
git pull --rebase origin main
git push -u origin main
```

---

## Useful Commit Types

```text
test      → test creation or test improvement
feat      → new functionality
fix       → bug fix
refactor  → code structure improvement
docs      → documentation update
chore     → maintenance task
```

Examples:

```powershell
git commit -m "test(day09): organize tests with pytest markers"
git commit -m "docs(readme): update learning journal"
git commit -m "refactor(project): move automation framework to repository root"
```