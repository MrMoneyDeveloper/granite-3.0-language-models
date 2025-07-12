import json
from pathlib import Path
from uuid import uuid4

HISTORY_PATH = Path.home() / ".granite_history.json"


def load():
    if HISTORY_PATH.exists():
        return json.loads(HISTORY_PATH.read_text())
    return {}


def log_summary(session_id: str, summary: str) -> None:
    history = load()
    history[session_id] = summary
    HISTORY_PATH.write_text(json.dumps(history, indent=2))


def search(term: str):
    term = term.lower()
    return {k: v for k, v in load().items() if term in v.lower()}
