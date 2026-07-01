# Gendiff

[![Hexlet CI](https://github.com/JulianaCarvajal/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/JulianaCarvajal/python-project-174/actions)
[![CI](https://github.com/JulianaCarvajal/python-project-174/actions/workflows/ci.yml/badge.svg)](https://github.com/JulianaCarvajal/python-project-174/actions)
[![Maintainability](https://qlty.sh/gh/JulianaCarvajal/projects/python-project-174/maintainability.svg)](https://qlty.sh/gh/JulianaCarvajal/projects/python-project-174)
[![Code Coverage](https://qlty.sh/gh/JulianaCarvajal/projects/python-project-174/coverage.svg)](https://qlty.sh/gh/JulianaCarvajal/projects/python-project-174)

CLI Difference Calculator. Compares two configuration files and shows a difference.

Built as the **second project** of the *Python Developer* course at **Códica** (Module 2).

---

## Minimum Requirements

- **Python**: 3.13
- **OS**: Linux, macOS, or Windows
- **Package manager**: [`poetry`](https://python-poetry.org/)  

---

## Installation

If you don’t have `poetry`:

**macOS/Linux**
```sh
curl -sSL https://install.python-poetry.org | python3 -
```

**Windows (PowerShell)**
```sh
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Clone and set up the environment:

```sh
git clone https://github.com/JulianaCarvajal/python-project-174.git
cd python-project-174
poetry install
```

---

## Usage

The program takes two arguments: the file paths of the files you want to compare. You can run the console scripts directly:

```sh
gendiff file1 file2
```

### Options

`--format`:  format in which the comparison will be displayed.

---

## Examples

Pending

---

## Demo

[![asciicast](https://asciinema.org/a/94MzvnaChMotgFw6.svg)](https://asciinema.org/a/94MzvnaChMotgFw6)

---

## Project Structure

```
python-project-174/
├── gendiff/                
│   ├── scripts/                  
│   │   ├── gendiff.py
├── pyproject.toml            
├── poetry.lock           
├── .gitignore
└── README.md
```
