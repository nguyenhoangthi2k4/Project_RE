## Project RE — Reverse Engineering Notes

This repository contains study notes, sample binaries, and utilities used for basic reverse engineering tasks on Windows. Below are quick links to commonly used tools and concise instructions for analyzing Python-based executables packaged with PyInstaller.

> Note: The “tools” section below lists links only (no deep write‑ups). The step‑by‑step guide focuses on unpacking/decompiling Python EXE files as requested.

---

## Tool links

- PyInstxtractor (PyInstaller Extractor) — https://github.com/extremecoders-re/pyinstxtractor
- pycdc (Python bytecode decompiler) — https://github.com/zrax/pycdc
- Ghidra — https://github.com/NationalSecurityAgency/ghidra
- Detect It Easy (DIE) — https://github.com/horsicq/DIE-engine
- Wireshark — https://www.wireshark.org/
- Process Monitor (Sysinternals) — https://learn.microsoft.com/sysinternals/downloads/procmon

---

## Unpack/decompile Python EXE (PyInstaller)

These steps show how to extract Python bytecode from a PyInstaller‑packed EXE and produce pseudocode from the resulting .pyc files.

### Prerequisites

- Windows PowerShell (v5.1+) — default on Windows
- Python 3.x installed and available on PATH (for running PyInstxtractor if using the .py version)
- Place the following files in the same directory:
	- Target EXE (e.g., `file.exe`)
	- `pyinstxtractor` (either `pyinstxtractor.py` or a built `pyinstxtractor.exe`)
	- `pycdc.exe`

> Important: The files `pyinstxtractor`, `pycdc`, and `file.exe` must be in the same folder to keep commands simple (as requested).

### 1) Extract with PyInstxtractor

Run one of the following, depending on what you have:

```powershell
# If you have a compiled pyinstxtractor.exe
./pyinstxtractor.exe ./file.exe

# OR if you have the Python script version
python ./pyinstxtractor.py ./file.exe
```

Expected result:
- A new folder appears next to the EXE, usually named `file.exe_extracted/`.
- Inside it, you’ll find `PYZ.pyz` and often `PYZ.pyz_extracted/` containing `.pyc` files.

### 2) Decompile .pyc to pseudocode with pycdc

Run pycdc on a specific `.pyc` file. For example:

```powershell
# Decompile a single .pyc file to console
./pycdc.exe ./file.exe_extracted/main.pyc

```

Tips:
- The actual .pyc paths vary by the original package structure. Explore `PYZ.pyz_extracted/` to locate relevant modules.
- If you get import or path errors, ensure you’re running the commands from the directory that contains `pyinstxtractor`, `pycdc.exe`, and the target `file.exe`.

---

## Notes

- Tool names sometimes appear with slightly different spellings online (e.g., "pyinstxtractor"). If using the Python script from GitHub, the filename is usually `pyinstxtractor.py`.
- Decompilation produces best‑effort pseudocode; variable names and structure may differ from the original source.

## Credits

- PyInstxtractor by extremecoders-re
- pycdc by zrax
- Additional tooling by their respective authors/organizations linked above

