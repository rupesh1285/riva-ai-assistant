import json
import os


def load_history(filepath="history.json"):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_history(history, filepath="history.json"):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
