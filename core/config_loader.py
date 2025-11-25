import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config", "settings.json")

DEFAULT_CONFIG = {
    "gemini_api_key": "",
    "model": "gemini-2.0-flash",
    "os": "windows",
    "temperature": 0.4
}

def load_config():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=2)

    with open(CONFIG_PATH, "r") as f:
        data = json.load(f)

    merged = DEFAULT_CONFIG.copy()
    merged.update({k: v for k, v in data.items() if v is not None})
    return merged

def update_config(key: str, value):
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=2)

    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    config[key] = value

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

    return True
