from pathlib import Path
from datetime import datetime

SNIPPET_DIR = Path.home() / "granite-snippets"


def stash(text: str, directory: Path | None = None) -> Path:
    if directory is None:
        directory = SNIPPET_DIR
    directory.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = directory / f"snippet-{ts}.txt"
    path.write_text(text)
    return path
