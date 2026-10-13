import json
from utils import NOTES_FILE


def load_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Convert old format (list of strings) to new format
            if data and isinstance(data[0], str):
                return [
                    {"note": item, "date": "Date unknown", "tag": "Unknown"}
                    for item in data
                ]

            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)
