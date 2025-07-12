import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]/"granite-cli-assist"))
from granite_cli_assist import snippet


def test_stash(tmp_path):
    path = snippet.stash("hello", directory=tmp_path)
    assert path.read_text() == "hello"
    assert path.parent == tmp_path
