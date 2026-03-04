import json
import os

FILE = "shopping_list/shopping.json"


def load_list():
    """Nolasa iepirkumu sarakstu no JSON faila."""
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_list(items):
    """Saglabā iepirkumu sarakstu JSON failā."""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)