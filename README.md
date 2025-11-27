# Flexible Language Yielding Notables (flyn)

flyn is a natural-language to shell command generator and executor. Type what you want in plain English, and flyn converts it into an OS-specific shell command with safety checks, history, diagnostics, and configuration tools.

---

## Features

* Convert natural-language instructions into shell commands
* Multiple OS modes: Windows, Linux, macOS
* Built-in risk analysis for dangerous commands
* Persistent command history (last 50 commands)
* Configurable API key, model, OS, and temperature
* Diagnostic tools to validate API and model connectivity
* Explain shell commands with contextual breakdowns
* Version command to check currently installed flyn version

---

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd flyn
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -e .
```

This installs `typer`, `rich`, `google-generativeai`, and other required runtime packages.

---

## Usage

All commands use the `flyn` CLI.

### Run Commands

Generate shell commands from natural language:

```bash
flyn run "<instruction>" [--dry-run/--run]
```

* `--dry-run` (default) shows the command without executing it
* `--run` executes the generated command

**Example:**

```bash
flyn run "count the number of files in this folder"
```

Output:

```
Generated command: (Get-ChildItem -File | Measure-Object).Count
Explanation: Counts the number of files in the current directory.
Risk level: LOW
Dry run: Command not executed.
```

---

### Configuration

Manage flyn settings:

```bash
flyn config show
flyn config get <key>
flyn config set <key> <value>
flyn config reset
```

Default OS: **Windows**

Config keys include:

* `api_key`
* `model`
* `os`
* `temperature` (0.0–1.0 randomness)

Example:

```bash
flyn config set os linux
flyn config set temperature 0.3
```

---

### OS Quick Commands

Switch OS mode instantly:

```bash
flyn os windows
flyn os linux
flyn os mac
```

Or use explicit:

```bash
flyn os set <os>
```

---

### History

```bash
flyn history show   # Show last 50 commands
flyn history clear  # Clear history
```

---

### Tools

Diagnostic and reverse-analysis utilities:

```bash
flyn tools diagnose            # Check API key, model, config
flyn tools models              # List Gemini models
flyn tools explain "<command>" # Explain a shell command
```

---

### Version

```bash
flyn version
```

---

## Command Reference

| Command                          | Description                   |
| -------------------------------- | ----------------------------- |
| `flyn run "<instruction>"`       | Generate shell commands       |
| `flyn version`                   | Show flyn version             |
| `flyn config show`               | Show all configuration values |
| `flyn config get <key>`          | Get specific config value     |
| `flyn config set <key> <value>`  | Update config value           |
| `flyn config reset`              | Reset config to defaults      |
| `flyn os set <os>`               | Explicit OS mode              |
| `flyn os windows/linux/mac`      | Quick OS switch               |
| `flyn history show`              | Display history               |
| `flyn history clear`             | Clear history                 |
| `flyn tools diagnose`            | Validate config and API       |
| `flyn tools models`              | List Gemini models            |
| `flyn tools explain "<command>"` | Analyze a shell command       |

---

## Supported OS

* Windows (PowerShell)
* Linux (bash/sh)
* macOS (zsh/bash)

Commands are adapted to the selected OS automatically.

---

## Safety

* Every generated command undergoes analysis
* Risk levels: `LOW`, `MEDIUM`, `HIGH`
* Dangerous patterns (e.g., destructive deletion) are flagged

---

## Requirements

* Python ≥ 3.10
* Gemini API key
* Internet connection

---

## Development

* Source code: `flyn/cli` + `flyn/core`
* Config file: `flyn/config/settings.json`
* Use a virtual environment for development

---

Happy scripting with **flyn** — Flexible Language Yielding Notables, crafted to turn your thoughts into precise shell actions.

Powered by Python, fueled by curiosity. 🚀
