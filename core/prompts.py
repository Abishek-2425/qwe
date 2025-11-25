def build_prompt(instruction: str, os_name: str):
    """
    Build a strict OS-aware prompt for generating shell commands.
    """

    # OS-specific guidance
    if os_name == "windows":
        os_rules = """
Use Windows command-prompt commands only.
Do NOT output Linux or macOS commands like ls, rm, grep, chmod, etc.
"""
    elif os_name == "mac":
        os_rules = """
Use macOS (BSD) shell commands.
Examples: ls, ps, df, du, top, open, rm, chmod.
Avoid Linux-only commands unless they work on macOS.
"""
    else:  # linux default
        os_rules = """
Use Linux shell commands.
Examples: ls, rm, cp, mv, grep, chmod, systemctl, journalctl, etc.
"""

    return f"""
You convert natural language into a **single** safe shell command.

Follow the OS rules below:
{os_rules}

Strict output format:
COMMAND: <one valid shell command>
EXPLANATION: <short explanation of what the command does>

Rules:
- Never output multiple commands.
- Never use &&, |, ;, or multiline commands.
- Never wrap commands in code blocks.
- The command must work on the target OS.
- Keep the explanation concise.

Instruction: "{instruction}"
"""

def build_explain_prompt(command: str):
    """
    Prompt for concise reverse-explanation of a shell command.
    """
    return f"""
Explain the following shell command concisely in exactly 3 points.

Format your explanation like this:

Purpose: <short explanation>
Main Effect: <short explanation>
Risk: <short explanation, or 'Minimal'>

COMMAND:
{command}

Use 1-2 sentences per point. Avoid Markdown symbols (*), code blocks, or extra sections.
"""
