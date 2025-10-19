Sure — I cleaned, polished and formatted your README into a single ready-to-copy `README.md`. It’s compact, attractive, practical, and keeps the “hacker” vibe while giving exact commands (clone → venv → install → run) for Windows and Linux/macOS. Just copy-paste the whole block below into your repo’s `README.md`.

````markdown
# 🕵️‍♂️ File Type Identifier & Malware Hint Scanner — Hacker Edition

![repo](https://img.shields.io/badge/Asura--Lord-File--Type--Identifier-blue) ![python](https://img.shields.io/badge/python-3.10%2B-brightgreen) ![streamlit](https://img.shields.io/badge/streamlit-1.38.0-orange) ![license](https://img.shields.io/badge/license-MIT-green)

> **Hackers hide malware in plain sight. This tool reveals the truth.**

---

## 🔭 Table of Contents
- [Overview](#overview)  
- [Why This Matters](#why-this-matters)  
- [Features](#features)  
- [Quick Start (60s)](#quick-start-60s)  
- [Installation Notes & Commands](#installation-notes--commands)  
- [Usage & Examples](#usage--examples)  
- [How It Detects Suspicious Files](#how-it-detects-suspicious-files)  
- [Signatures DB (format)](#signatures-db-format)  
- [Project Structure](#project-structure)  
- [Requirements & .gitignore](#requirements--gitignore)  
- [Contributing](#contributing)  
- [Security & Responsible Use](#security--responsible-use)  
- [License](#license)  
- [Live Preview & Screenshots](#live-preview--screenshots)  
- [Contact & Support](#contact--support)

---

## Overview
A compact Python tool (CLI + optional Streamlit GUI) that reads **magic bytes** (file header) and identifies the file’s real type. If a file’s visible extension and its header disagree, it flags the file as **suspicious** for safe triage and investigation.

This is fast, local, and educational — ideal for triage, phishing analysis, and learning how attackers disguise payloads.

---

## Why This Matters
Attackers frequently rename malware to look harmless (e.g., `invoice.pdf.exe`). Operating systems often rely on extensions, while the **true identity** lives in the file header (magic bytes). This tool surfaces mismatches so you can investigate in an isolated environment.

---

## Features
- Detects file type via magic-bytes (header signatures)  
- Flags files where `extension ≠ detected type`  
- Small, editable **`signatures.json`** DB for common formats (JPG, PNG, PDF, EXE, ZIP, etc.)  
- Optional SHA256 / MD5 hashing for offline lookups (VirusTotal)  
- Lightweight CLI and optional Streamlit GUI for visual triage  
- Optional heuristics: entropy check, double-extension detection, archive inner-file check  

---

## Quick Start (run in ~60s)

> Clone → create venv → install → run (Streamlit GUI or CLI)

### Windows (PowerShell)
```powershell
# 1) clone repo
git clone https://github.com/Asura-Lord/File-Type-Identifier.git
cd File-Type-Identifier

# 2) create & activate venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3) upgrade pip + install minimal deps (only Streamlit needed for GUI)
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 4) run GUI (recommended)
python -m streamlit run app.py

# OR run CLI
python file_scan.py /path/to/file_or_folder --hash sha256
````

### Linux / macOS (Bash)

```bash
# 1) clone
git clone https://github.com/Asura-Lord/File-Type-Identifier.git
cd File-Type-Identifier

# 2) venv
python3 -m venv .venv
source .venv/bin/activate

# 3) upgrade + install
python3 -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 4) run GUI
python3 -m streamlit run app.py

# OR CLI
python3 file_scan.py /path/to/file_or_folder --hash sha256
```

> If `streamlit` is not found in PowerShell, use `python -m streamlit run app.py` to avoid PATH issues.

---

## Installation Notes

* The **core scanner** uses only Python standard libraries. Install `streamlit` only for GUI.
* Add `.venv/` to `.gitignore`.
* Keep `signatures.json` small and specific to reduce false positives.

Example `.gitignore`:

```text
.venv/
__pycache__/
*.pyc
temp_*
scans.db
logs.json
```

---

## Usage & Examples

### CLI

```bash
# scan a single file
python file_scan.py /path/to/file.exe

# scan a folder recursively and output CSV
python file_scan.py ./downloads --recursive --output scans.csv --hash sha256
```

### Streamlit GUI

* Run `python -m streamlit run app.py`
* Upload a file or point to a folder
* View: file name, declared extension, detected header type, SHA256 (if requested), entropy and warnings

Example result table:

| File Name  | Extension | Detected | Status              |
| ---------- | --------- | -------- | ------------------- |
| report.pdf | pdf       | PDF      | ✅ Safe              |
| cat.jpg    | jpg       | PE/EXE   | ⚠️ Suspicious File! |

---

## How It Detects Suspicious Files

1. **Read magic bytes** (first 4–16 bytes).
2. **Match against signatures** in `signatures.json`.
3. **Extract extension** from filename.
4. If `extension != detected_type` → mark as **Suspicious**.
5. Optional hints: compute **SHA256/MD5**, run **entropy** heuristic, inspect contained files in archives.

**Important**: this is a triage tool — it does **not** execute files and is **not** a full AV replacement.

---

## Signatures DB (format)

`signatures.json` is a small JSON list of signature objects. Example:

```json
[
  {
    "label": "PDF",
    "extensions": ["pdf"],
    "magic": "25504446",
    "offset": 0
  },
  {
    "label": "PNG",
    "extensions": ["png"],
    "magic": "89504E470D0A1A0A",
    "offset": 0
  },
  {
    "label": "PE/EXE",
    "extensions": ["exe", "dll"],
    "magic": "4D5A",
    "offset": 0
  }
]
```

* `magic` is a hex string (uppercase/lowercase OK).
* `offset` is where the magic bytes begin (usually 0).
* Keep entries focused to reduce collisions and mis-identification.

---

## Project Structure

```
File-Type-Identifier/
├─ app.py             # Streamlit front-end
├─ file_scan.py       # Core scanner (CLI + helpers)
├─ signatures.json    # External signatures DB (editable)
├─ requirements.txt   # Minimal dependencies (streamlit)
├─ README.md
└─ .gitignore
```

---

## Requirements

Minimal `requirements.txt` (only needed for GUI):

```
streamlit==1.38.0
pefile==2024.12.31    # optional: if PE inspection is included
```

> If you only run CLI and basic checks, you may not need any extra packages.

---

## Contributing

Contributions are welcome:

* Improve or add signatures to `signatures.json`
* Add CLI flags or output formats (JSON/CSV)
* Add tests and CI (pytest)
* Implement optional VirusTotal hash lookup (only with API key and consent)

How to contribute:

1. Fork → `git checkout -b feature/…`
2. Code + tests
3. Open PR with description and security implications

---

## Security & Responsible Use

* The tool **does not execute files**. Still: **do not open suspicious files on production hosts**. Use isolated VMs or sandboxes.
* Treat logs and paths as sensitive data. Do not upload suspicious samples to public services without permission.
* If integrating VirusTotal or similar, follow API rules and user consent.

---

## License

MIT License — 2025 Asura-Lord
(See `LICENSE` file for full text)

---

## Live Preview & Screenshots

* Deploy to Streamlit Cloud (optional) and paste the link here when available.
* Add screenshots to `docs/` and reference them:

```markdown
![Main UI](docs/screenshot_main.png)
![Suspicious Example](docs/screenshot_suspicious.png)
```

---

## Contact & Support

Author: **Asura-Lord** — [https://github.com/Asura-Lord](https://github.com/Asura-Lord)
Issues / feature requests: [https://github.com/Asura-Lord/File-Type-Identifier/issues](https://github.com/Asura-Lord/File-Type-Identifier/issues)

---

> **Final note:** this tool is a fast, local triage helper. Use it to catch obvious disguises and to gather hashes for follow-up. Keep it legal, keep it isolated, keep it dangerous. 🖤

