import json
import os
from datetime import datetime

HISTORY_FILE = os.path.expanduser("~/.gensh-cli_history.json")

def save_history(prompt, cmd, risk):
    entry = {
        "prompt": prompt,
        "command": cmd,
        "risk": risk,
        "timestamp": datetime.now().isoformat()
    }

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump([entry], f, indent=2)
        return

    data = json.load(open(HISTORY_FILE))
    data.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)
