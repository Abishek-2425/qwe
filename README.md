# **flyn — v2.0**

**flyn** is a next-generation natural-language → shell command engine.
Describe what you want in plain English, and flyn produces a safe, validated, OS-aware shell command — with beautiful output, risk analysis, explanations, and optional execution.

v2.0 introduces a completely redesigned architecture that is modular, safer, cleaner, and extensible.
Everything from the CLI to the core engine has been rebuilt.

---

## **✨ What’s New in v2.0**

### **New Commands**

* `flyn show "<instruction>"` — generate a command (no execution)
* `flyn run "<instruction>"` — generate + safely execute
* `flyn exp "<command>"` — explain any shell command
* `flyn config` — full configuration system

### **New Architecture**

* Dedicated **engine pipeline**: generate → parse → validate → execute
* Modular **generation backends** (Google GenAI, mock, extensible for future)
* Structured **executors** for bash, zsh, PowerShell, CMD
* Dedicated **render layer** for spacing, blocks, and colors
* Centralized **safety system** with severity levels
* Clean **config system** using TOML defaults + loader

### **Improved Safety**

* Multi-stage risk analysis
* Detection of destructive patterns
* Execution blocking for dangerous commands
* Caution prompts for moderate-risk commands
* Dry-run display of the final shell command

### **Beautiful Output**

* Colorized sections
* Clean spacing + layout blocks
* Separate stdout/stderr
* Icons and human-friendly formatting

---

# **Installation**

Clone the repository:

```bash
git clone <repo-url>
cd flyn
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

Install in editable mode:

```bash
pip install -e .
```

---

# **Usage (v2.0 CLI)**

## **🔹 Generate a command**

```bash
flyn show "<instruction>"
```

Example:

```bash
flyn show "list all files sorted by size"
```

Output:

```
Generated Command:
  ls -lS

Risk Level: Safe
Notes:
  • Simple read-only listing command
```

---

## **🔹 Generate AND execute**

```bash
flyn run "<instruction>"
```

Example:

```bash
flyn run "create a folder called temp_data"
```

If safe:

* command runs immediately
  If caution/danger:
* you receive a confirmation prompt

---

## **🔹 Explain a shell command**

```bash
flyn exp "<command>"
```

Example:

```bash
flyn exp "rm -rf /var/www/html"
```

Output includes:

* Purpose
* Main effect
* Risk assessment
* Dangerous flags
* Safer alternatives (if possible)

---

## **🔹 Configuration**

Manage flyn settings:

```bash
flyn config
flyn config get <key>
flyn config set <key> <value>
flyn config reset
```

Configurable keys include:

* `backend` — which LLM backend to use
* `shell` — preferred local shell
* `confirm_risky` — ask before running dangerous commands
* `log_level` — info/debug
* `api_key` — for backends requiring it

Defaults are stored in:

```
~/.config/flyn/defaults.toml
```

---

# **How It Works (v2.0 Engine)**

Every command flows through the redesigned v2.0 pipeline:

1. **Generate** — Natural language → Raw command suggestion
2. **Parse** — Clean + normalize the command
3. **Validate** — Check safety, structure, destructive patterns
4. **Render** — Display beautifully formatted output
5. **Execute** (only in `run`) — OS-aware execution with error capture

This architecture isolates responsibilities and makes the system predictable, testable, and easy to extend.

---

# **Supported Backends**

flyn v2.0 supports modular LLM backends.

Included:

* Google Generative AI backend
* Mock backend for testing and offline usage

Pluggable:

* OpenAI
* Local LLaMA models
* Custom enterprise backends

---

# **Supported Shells**

flyn automatically detects your environment:

* PowerShell (Windows)
* CMD (Windows fallback)
* Bash / Zsh (Linux/macOS)

You can override it in config.

---

# **Safety Model**

Risk levels:

* **Safe** — No destructive action
* **Caution** — Potentially irreversible or sensitive
* **Danger** — Highly destructive (blocked unless forced)

Patterns detected:

* Recursive deletion
* Disk formatting commands
* Privileged operations
* Wildcard-based destructive operations
* Pipe chains with destructive consequences

---

# **Development Notes**

Source layout:

```
flyn/
  cli/              # CLI entry & commands
  cli/render/       # visual formatting and UI blocks
  core/engine/      # parse/validate/run pipeline
  core/generation_backends/ # LLM adapters
  config/           # config loader + defaults
```

Run tests:

```bash
pytest
```

---

# **Why flyn exists**

Every OS has its own shell, syntax, and quirks.
Humans think in **intent**, not **syntax**.

flyn bridges the gap:

> You think → flyn writes → shell executes safely.

---

# **License**

MIT