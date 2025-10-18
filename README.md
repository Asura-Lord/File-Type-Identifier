# 🕵️‍♂️ File Type Identifier & Malware Hint Scanner — Hacker Edition

![repo-size](https://img.shields.io/badge/Asura--Lord-File--Type--Identifier-blue) ![python](https://img.shields.io/badge/python-3.10%2B-brightgreen) ![streamlit](https://img.shields.io/badge/streamlit-ready-orange) ![license](https://img.shields.io/badge/license-MIT-green)

> _"Hackers hide malware in plain sight. This tool reveals the truth."_

---

## Table of Contents
- [Overview](#overview)  
- [Why This Matters](#why-this-matters)  
- [Features](#features)  
- [Quick Start (run in ~60s)](#quick-start-run-in-60s)  
- [Installation (Windows / Linux / macOS)](#installation-windows--linux--macos)  
- [Usage & Examples](#usage--examples)  
- [How it Detects Suspicious Files](#how-it-detects-suspicious-files)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [Security & Responsible Use](#security--responsible-use)  
- [License](#license)  
- [Live Preview & Screenshots](#live-preview--screenshots)  
- [Contact & Support](#contact--support)

---

## Overview
A compact Python + Streamlit tool that reads the **magic bytes** (file headers) to determine a file's real type and flags mismatches with the visible extension. Great for triage, teaching digital forensics basics, and demoing how attackers disguise payloads.

---

## Why This Matters
Attackers often hide harmful executables behind benign-looking names (e.g. `invoice.pdf.exe`). OSes and users rely on extensions, but **true identity** is in the file header. This tool mimics a basic forensic check used by analysts to spot those tricks.

---

## Features
- Detects file type using magic bytes
- Flags files when extension ≠ detected header type
- Small, editable signature DB for common formats (JPG, PNG, PDF, EXE, ZIP, etc.)
- Optional SHA256/MD5 hashing for further offline lookup
- Lightweight CLI + Streamlit GUI (fast & minimal)
- Educational notes about common obfuscation techniques

---

## Quick Start (run in ~60s)
Clone, create venv, install, run:

**Windows (PowerShell)**  
```powershell
git clone https://github.com/Asura-Lord/File-Type-Identifier.git
cd File-Type-Identifier
python -m venv .venv
.\\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
python -m streamlit run app.py
Linux / macOS (Bash)

bash
Copy code
git clone https://github.com/Asura-Lord/File-Type-Identifier.git
cd File-Type-Identifier
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
python3 -m streamlit run app.py
Open the local URL printed by Streamlit (usually http://localhost:8501).

Installation (notes)
Keep the project lightweight: only install streamlit if you want the GUI. The core scanner uses only Python standard libraries.

Add .venv/ to .gitignore to avoid pushing your virtual environment.

.gitignore example:

markdown
Copy code
.venv/
__pycache__/
*.pyc
temp_*
scans.db
logs.json
Usage & Examples
Upload a file in the Streamlit UI or pass a path to the CLI script.

The tool displays:

File name

Declared extension

Detected (header) type

Status: Safe or ⚠️ Suspicious File!

Optional: SHA256 hash for external lookup

Example table:

File Name	Extension	Detected	Status
report.pdf	pdf	PDF	✅ Safe
cat.jpg	jpg	PE/EXE	⚠️ Suspicious File!

How it Detects Suspicious Files
Reads first 4–16 bytes (magic bytes) of a file.

Tries to match those bytes with known signatures in a small DB.

Extracts file extension from filename.

If extension and detected type mismatch → mark as Suspicious.

(Optional) Compute MD5/SHA256 for further offline checks (VirusTotal etc. — API usage should be consented).

Project Structure
graphql
Copy code
File-Type-Identifier/
├─ app.py             # Streamlit front-end (UI)
├─ file_scan.py       # Core scanner logic (magic bytes, hashing)
├─ signatures.json    # (optional) external signatures DB
├─ requirements.txt   # Minimal deps (streamlit)
├─ README.md
└─ .gitignore
Example minimal requirements.txt:

ini
Copy code
streamlit==1.38.0
TIP: If you only want CLI, you don't need to install anything beyond Python 3.8+.

Contributing
Contributions welcome: add signatures, improve detection, add CLI flags, or make a small tests suite.

How to contribute:

Fork the repo

Create a branch (git checkout -b feature/x)

Add tests where applicable

Open a Pull Request with a clear description and security considerations

Security & Responsible Use
This tool does not execute files — it only reads bytes and computes hashes.

Never open suspicious files on your production host. Use VMs or sandboxes for deeper analysis.

Handle scan logs and file paths as potentially sensitive information.

If integrating external APIs (VirusTotal, Hybrid Analysis), respect API terms and user privacy.

License
MIT License — 2025 Asura-Lord
(See LICENSE file in repo for full text.)

Live Preview & Screenshots
Live Preview: Paste your Streamlit cloud link here when deployed (e.g. https://share.streamlit.io/your-user/your-repo)

Screenshots: Add screenshots to /docs/ or root and reference them here:

markdown
Copy code
![UI Screenshot](docs/screenshot_main.png)
![Suspicious Example](docs/screenshot_suspicious.png)
Contact & Support
Author: Asura-Lord — https://github.com/Asura-Lord

Issues / feature requests: https://github.com/Asura-Lord/File-Type-Identifier/issues

⚠️ Final Note (Hacker style):
Weak file checks are an easy win for attackers. Use this tool to triage downloads and attachments — always verify before you open. Keep it legal, keep it isolated, keep it dangerous. 🖤

makefile
Copy code
::contentReference[oaicite:0]{index=0}
