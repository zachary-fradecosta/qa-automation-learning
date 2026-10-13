# Python Project Guide

## Display the current directory

```powershell
Get-Location
```

## List files and folders

```powershell
Get-ChildItem
```

## Display the project tree

```powershell
tree /F /A
```

## Move to the parent directory

```powershell
cd ..
```

## Run a Python script

```powershell
python scripts/api_demo.py
```

## Run a Python module

```powershell
python -m scripts.day04_demo
```

Use module execution when the script requires project imports.

## Install project dependencies

```powershell
pip install -r requirements.txt
```

## Check a library version

```powershell
python -c "import requests; print(requests.__version__)"
```